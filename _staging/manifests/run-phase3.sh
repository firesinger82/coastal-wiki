#!/usr/bin/env bash
# Phase 3 — target manifest 생성 + source 와 diff verify.
# 정책: plan.md Phase 3 (D2·F4).
# 모든 manifest 는 Phase 1 과 동일한 root-relative 명령 사용.
set -uo pipefail

WIKI="/home/firesinger/coastal-wiki"
OUT="$WIKI/_staging/manifests"
LOG="$OUT/phase3.log"
: > "$LOG"

FAILED=0

log() {
    printf '[%s] %s\n' "$(date '+%H:%M:%S')" "$*" | tee -a "$LOG"
}

verify_area() {
    local label="$1"
    local root="$2"
    local find_extra="${3:-}"

    if [ ! -d "$root" ]; then
        log "SKIP [$label] : $root 없음"
        return
    fi

    local src_sha="$OUT/sha256-source-${label}.txt"
    local tgt_sha="$OUT/sha256-target-${label}.txt"
    local src_files="$OUT/files-source-${label}.txt"
    local tgt_files="$OUT/files-target-${label}.txt"

    if [ ! -f "$src_sha" ]; then
        log "SKIP [$label] : source manifest $src_sha 없음 (Phase 1 누락?)"
        FAILED=$((FAILED+1))
        return
    fi

    log "BEGIN [$label] target root=$root"

    # target 측 root-relative 파일 목록 + sha256
    (cd "$root" && eval "find . -type f $find_extra" | LC_ALL=C sort) > "$tgt_files"
    (cd "$root" && eval "find . -type f $find_extra -print0" | LC_ALL=C sort -z \
        | xargs -0 sha256sum) > "$tgt_sha" 2>>"$LOG"

    local src_n tgt_n
    src_n=$(wc -l < "$src_files")
    tgt_n=$(wc -l < "$tgt_files")
    log "  files: src=$src_n tgt=$tgt_n"

    # 파일 목록 diff
    if ! diff -q "$src_files" "$tgt_files" >/dev/null 2>&1; then
        log "  FAIL [files diff]"
        diff -u "$src_files" "$tgt_files" | head -30 | sed 's/^/    /' | tee -a "$LOG"
        FAILED=$((FAILED+1))
        return
    fi

    # sha256 manifest diff
    if ! diff -q "$src_sha" "$tgt_sha" >/dev/null 2>&1; then
        log "  FAIL [sha256 diff]"
        diff -u "$src_sha" "$tgt_sha" | head -30 | sed 's/^/    /' | tee -a "$LOG"
        FAILED=$((FAILED+1))
        return
    fi

    log "  PASS [$label] ($tgt_n files, sha256 일치)"
}

verify_single_file() {
    local label="$1"
    local target_file="$2"

    local src_sha="$OUT/sha256-source-${label}.txt"
    if [ ! -f "$src_sha" ]; then
        log "SKIP [$label] : source manifest 없음"
        return
    fi
    if [ ! -f "$target_file" ]; then
        log "FAIL [$label] : target $target_file 없음"
        FAILED=$((FAILED+1))
        return
    fi

    local expected_sha actual_sha
    expected_sha=$(awk '{print $1}' "$src_sha")
    actual_sha=$(sha256sum "$target_file" | awk '{print $1}')

    if [ "$expected_sha" = "$actual_sha" ]; then
        log "  PASS [$label] ($target_file)"
    else
        log "  FAIL [$label] : sha256 mismatch"
        log "    expected: $expected_sha"
        log "    actual:   $actual_sha"
        FAILED=$((FAILED+1))
    fi
}

log "=== Phase 3 시작 ==="

# 1) testsuite
verify_area "adcirc-testsuite" "$WIKI/models/ADCIRC/raw/source_code/adcirc-testsuite"

# 2) <model>-source (adcirc 는 testsuite 제외)
verify_area "adcirc-source"   "$WIKI/models/ADCIRC/raw/source_code"  "-not -path './adcirc-testsuite/*'"
verify_area "delft3d-source"  "$WIKI/models/Delft3D/raw/source_code"
verify_area "efdc-source"     "$WIKI/models/EFDC/raw/source_code"
verify_area "roms-source"     "$WIKI/models/ROMS/raw/source_code"
verify_area "swan-source"     "$WIKI/models/SWAN/raw/source_code"
verify_area "xbeach-source"   "$WIKI/models/XBeach/raw/source_code"

# 3) <model>-manuals
verify_area "adcirc-manuals"  "$WIKI/models/ADCIRC/raw/manuals"
verify_area "delft3d-manuals" "$WIKI/models/Delft3D/raw/manuals"
verify_area "efdc-manuals"    "$WIKI/models/EFDC/raw/manuals"
verify_area "roms-manuals"    "$WIKI/models/ROMS/raw/manuals"
verify_area "swan-manuals"    "$WIKI/models/SWAN/raw/manuals"
verify_area "xbeach-manuals"  "$WIKI/models/XBeach/raw/manuals"

# 4) 각 모델 manifest.md (single file)
verify_single_file "adcirc-meta"  "$WIKI/models/ADCIRC/manifest.md"
verify_single_file "delft3d-meta" "$WIKI/models/Delft3D/manifest.md"
verify_single_file "efdc-meta"    "$WIKI/models/EFDC/manifest.md"
verify_single_file "roms-meta"    "$WIKI/models/ROMS/manifest.md"
verify_single_file "swan-meta"    "$WIKI/models/SWAN/manifest.md"
verify_single_file "xbeach-meta"  "$WIKI/models/XBeach/manifest.md"

# 5) knowledge
verify_area "knowledge" "$WIKI/_staging/from-modeling-wiki/knowledge"

# 6) mw-archive
for sub in protocols templates context experiments indexes graphify-out specs; do
    verify_area "mw-${sub}" "$WIKI/_archive/modeling-wiki/${sub}"
done

# README.md
verify_single_file "mw-README" "$WIKI/_archive/modeling-wiki/README.md"

# ---------- 추가 검증: research/ 격리 + raw 트리 ignored ----------
log "[추가] research isolation validator (working tree)"
if bash "$WIKI/tools/validate-research-isolation.sh" >>"$LOG" 2>&1; then
    log "  PASS"
else
    log "  FAIL"
    FAILED=$((FAILED+1))
fi

log "[추가] models/*/raw/ git-ignored 확인"
ignored_ok=1
for d in models/*/raw/source_code models/*/raw/manuals; do
    [ -d "$WIKI/$d" ] || continue
    # 디렉토리 내 임의 파일이 ignored 인지 (디렉토리 자체보다는 파일 패턴)
    sample=$(find "$WIKI/$d" -type f 2>/dev/null | head -1)
    [ -z "$sample" ] && continue
    rel="${sample#$WIKI/}"
    if ! (cd "$WIKI" && git check-ignore -q "$rel" 2>/dev/null); then
        log "  FAIL: $rel 가 ignored 아님 (.gitignore 누락?)"
        ignored_ok=0
    fi
done
if [ $ignored_ok -eq 1 ]; then
    log "  PASS"
else
    FAILED=$((FAILED+1))
fi

log "=== Phase 3 완료 ==="
log "총 검증 영역: $(ls "$OUT"/sha256-source-*.txt 2>/dev/null | wc -l)"
log "FAILED: $FAILED"
exit $FAILED

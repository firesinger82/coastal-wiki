#!/usr/bin/env bash
# Phase 2 — rsync /mnt/e → coastal-wiki (원본 보존, copy only).
# 정책: plan.md Phase 2 (D2).
# rsync 옵션:
#   -a  archive (perms, times, recursive)
#   --partial --append-verify  중단·재실행 resume
#   --info=progress2 진행률 출력
set -uo pipefail

WIKI="/home/firesinger/coastal-wiki"
LOG="$WIKI/_staging/manifests/phase2.log"
: > "$LOG"

log() {
    printf '[%s] %s\n' "$(date '+%H:%M:%S')" "$*" | tee -a "$LOG"
}

rsync_copy() {
    local label="$1"
    local src="$2"
    local dst="$3"
    local extra="${4:-}"   # 추가 rsync 옵션 (예: --exclude)

    if [ ! -d "$src" ]; then
        log "SKIP [$label] : $src 없음"
        return
    fi

    log "BEGIN [$label] $src → $dst"
    mkdir -p "$(dirname "$dst")"

    # trailing slash 보장 (디렉토리 내용물 복사)
    local src_slash="${src%/}/"
    eval "rsync -a --partial --append-verify $extra '$src_slash' '$dst/'" \
        >> "$LOG" 2>&1

    local rc=$?
    if [ $rc -ne 0 ]; then
        log "  ERROR rsync rc=$rc"
        return $rc
    fi

    # 빠른 count 검증 (sha256 verify 는 Phase 3 에서)
    local src_n dst_n
    src_n=$(find "$src" -type f 2>/dev/null | wc -l)
    dst_n=$(find "$dst" -type f 2>/dev/null | wc -l)
    log "  files: src=$src_n dst=$dst_n"
    if [ "$src_n" != "$dst_n" ]; then
        log "  WARN: count mismatch — Phase 3 에서 sha256 diff 로 추적"
    fi
    log "END [$label]"
}

log "=== Phase 2 시작 ==="

# 1) 16GB adcirc-testsuite (full) → models/ADCIRC/raw/source_code/adcirc-testsuite/
rsync_copy "adcirc-testsuite" \
    "/mnt/e/modeling-wiki/raw/code/adcirc/adcirc-testsuite" \
    "$WIKI/models/ADCIRC/raw/source_code/adcirc-testsuite"

# 2) /mnt/e/models/<m>/source_code → models/<MODEL>/raw/source_code/
#    adcirc 는 lean testsuite 제외 (full 은 위에서 별도 처리)
rsync_copy "adcirc-source" \
    "/mnt/e/models/adcirc/source_code" \
    "$WIKI/models/ADCIRC/raw/source_code" \
    "--exclude='adcirc-testsuite/'"
rsync_copy "delft3d-source"  "/mnt/e/models/delft3d/source_code"  "$WIKI/models/Delft3D/raw/source_code"
rsync_copy "efdc-source"     "/mnt/e/models/efdc/source_code"     "$WIKI/models/EFDC/raw/source_code"
rsync_copy "roms-source"     "/mnt/e/models/roms/source_code"     "$WIKI/models/ROMS/raw/source_code"
rsync_copy "swan-source"     "/mnt/e/models/swan/source_code"     "$WIKI/models/SWAN/raw/source_code"
rsync_copy "xbeach-source"   "/mnt/e/models/xbeach/source_code"   "$WIKI/models/XBeach/raw/source_code"

# 3) /mnt/e/models/<m>/manuals → models/<MODEL>/raw/manuals/
rsync_copy "adcirc-manuals"  "/mnt/e/models/adcirc/manuals"  "$WIKI/models/ADCIRC/raw/manuals"
rsync_copy "delft3d-manuals" "/mnt/e/models/delft3d/manuals" "$WIKI/models/Delft3D/raw/manuals"
rsync_copy "efdc-manuals"    "/mnt/e/models/efdc/manuals"    "$WIKI/models/EFDC/raw/manuals"
rsync_copy "roms-manuals"    "/mnt/e/models/roms/manuals"    "$WIKI/models/ROMS/raw/manuals"
rsync_copy "swan-manuals"    "/mnt/e/models/swan/manuals"    "$WIKI/models/SWAN/raw/manuals"
rsync_copy "xbeach-manuals"  "/mnt/e/models/xbeach/manuals"  "$WIKI/models/XBeach/raw/manuals"

# 4) /mnt/e/models/<m>/manifest.md → models/<MODEL>/manifest.md (authored 단일 파일)
for m in adcirc delft3d efdc roms swan xbeach; do
    case "$m" in
        adcirc)  M="ADCIRC"  ;;
        delft3d) M="Delft3D" ;;
        efdc)    M="EFDC"    ;;
        roms)    M="ROMS"    ;;
        swan)    M="SWAN"    ;;
        xbeach)  M="XBeach"  ;;
    esac
    src="/mnt/e/models/$m/manifest.md"
    dst="$WIKI/models/$M/manifest.md"
    if [ -f "$src" ]; then
        mkdir -p "$(dirname "$dst")"
        cp -p "$src" "$dst"
        log "COPY [${m}-meta] $src → $dst"
    fi
done

# 5) modeling-wiki/knowledge → _staging/from-modeling-wiki/knowledge/
rsync_copy "knowledge" \
    "/mnt/e/modeling-wiki/knowledge" \
    "$WIKI/_staging/from-modeling-wiki/knowledge"

# 6) modeling-wiki/{운영 자산} → _archive/modeling-wiki/<sub>/
for sub in protocols templates context experiments indexes graphify-out specs; do
    rsync_copy "mw-${sub}" \
        "/mnt/e/modeling-wiki/${sub}" \
        "$WIKI/_archive/modeling-wiki/${sub}"
done

# README.md 단일 파일
if [ -f /mnt/e/modeling-wiki/README.md ]; then
    cp -p /mnt/e/modeling-wiki/README.md "$WIKI/_archive/modeling-wiki/README.md"
    log "COPY [mw-README] /mnt/e/modeling-wiki/README.md → _archive/modeling-wiki/README.md"
fi

log "=== Phase 2 완료 ==="

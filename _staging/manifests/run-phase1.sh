#!/usr/bin/env bash
# Phase 1 — source manifest 생성 (read-only).
# 정책: plan.md Phase 1 (D2·F4 반영).
# 모든 manifest 는 root-relative 경로 + sha256.
set -uo pipefail

WIKI="/home/firesinger/coastal-wiki"
OUT="$WIKI/_staging/manifests"
mkdir -p "$OUT"

LOG="$OUT/phase1.log"
: > "$LOG"

log() {
    printf '[%s] %s\n' "$(date '+%H:%M:%S')" "$*" | tee -a "$LOG"
}

manifest_area() {
    local label="$1"
    local root="$2"
    local find_extra="${3:-}"   # 추가 find 옵션 (예: -not -path ...)

    if [ ! -d "$root" ]; then
        log "SKIP [$label] : $root 없음"
        return
    fi

    log "BEGIN [$label] root=$root"

    local sha_file="$OUT/sha256-source-${label}.txt"
    local files_file="$OUT/files-source-${label}.txt"
    local size_file="$OUT/size-source-${label}.txt"

    # 파일 목록 (root-relative, sorted)
    (cd "$root" && eval "find . -type f $find_extra -print0" | LC_ALL=C sort -z) \
        | xargs -0 -I{} echo "{}" > "$files_file"

    local n
    n=$(wc -l < "$files_file" 2>/dev/null || echo 0)
    log "  files: $n"

    # sha256 (root-relative)
    (cd "$root" && eval "find . -type f $find_extra -print0" | LC_ALL=C sort -z \
        | xargs -0 sha256sum) > "$sha_file" 2>>"$LOG"

    # 크기·count
    {
        echo "label: $label"
        echo "root: $root"
        echo "files: $n"
        echo "size: $(du -sh "$root" 2>/dev/null | awk '{print $1}')"
        echo "manifest_sha256: $(sha256sum "$sha_file" | awk '{print $1}')"
        echo "generated: $(date -Iseconds)"
    } > "$size_file"

    log "END [$label]"
}

log "=== Phase 1 시작 ==="

# 1) 16GB adcirc-testsuite full
manifest_area "adcirc-testsuite" "/mnt/e/modeling-wiki/raw/code/adcirc/adcirc-testsuite"

# 2) /mnt/e/models/<m>/source_code (adcirc 는 testsuite 제외)
manifest_area "adcirc-source"   "/mnt/e/models/adcirc/source_code"   "-not -path './adcirc-testsuite/*'"
manifest_area "delft3d-source"  "/mnt/e/models/delft3d/source_code"
manifest_area "efdc-source"     "/mnt/e/models/efdc/source_code"
manifest_area "roms-source"     "/mnt/e/models/roms/source_code"
manifest_area "swan-source"     "/mnt/e/models/swan/source_code"
manifest_area "xbeach-source"   "/mnt/e/models/xbeach/source_code"

# 3) /mnt/e/models/<m>/manuals
manifest_area "adcirc-manuals"  "/mnt/e/models/adcirc/manuals"
manifest_area "delft3d-manuals" "/mnt/e/models/delft3d/manuals"
manifest_area "efdc-manuals"    "/mnt/e/models/efdc/manuals"
manifest_area "roms-manuals"    "/mnt/e/models/roms/manuals"
manifest_area "swan-manuals"    "/mnt/e/models/swan/manuals"
manifest_area "xbeach-manuals"  "/mnt/e/models/xbeach/manuals"

# 4) /mnt/e/modeling-wiki/knowledge (164 files → _staging/from-modeling-wiki/)
manifest_area "knowledge" "/mnt/e/modeling-wiki/knowledge"

# 5) modeling-wiki 운영 자산 (→ _archive/modeling-wiki/)
for sub in protocols templates context experiments indexes graphify-out specs; do
    manifest_area "mw-${sub}" "/mnt/e/modeling-wiki/${sub}"
done

# README.md 단일 파일은 manifest_area 안 돌리고 sha256 만 직접
if [ -f /mnt/e/modeling-wiki/README.md ]; then
    sha256sum /mnt/e/modeling-wiki/README.md > "$OUT/sha256-source-mw-README.txt"
    log "BEGIN+END [mw-README]: single file"
fi

# 6) 각 모델의 manifest.md (acquisition metadata)
for m in adcirc delft3d efdc roms swan xbeach; do
    f="/mnt/e/models/$m/manifest.md"
    if [ -f "$f" ]; then
        sha256sum "$f" > "$OUT/sha256-source-${m}-meta.txt"
        log "BEGIN+END [${m}-meta]: $f"
    fi
done

log "=== Phase 1 완료 ==="
log "총 manifest: $(ls "$OUT"/sha256-source-*.txt 2>/dev/null | wc -l)"
log "총 size files: $(ls "$OUT"/size-source-*.txt 2>/dev/null | wc -l)"

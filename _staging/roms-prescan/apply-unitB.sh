#!/usr/bin/env bash
# ROMS Unit B — roms_4dvar.md 내용 정정 (snapshot 은 이미 57aecf5, 교체 없음)
# 실행: sudo bash ~/coastal-wiki/_staging/roms-prescan/apply-unitB.sh
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/roms-prescan"
F="models/ROMS/source-analysis/roms_4dvar.md"
BK="/opt/coastal-snapshots"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }

say "0. before-hash"
BEFORE="$(sha256sum "$WIKI/$F" | cut -d' ' -f1)"
EXPECT="7bd2f5e0083fdc8c07785c24127fd4bf83898968a9c78a68fd59aa576aef3e48"
[ "$BEFORE" = "$EXPECT" ] || die "before-hash 불일치 ($BEFORE)"
echo "OK: $BEFORE"

say "1. 백업"
mkdir -p "$BK"
tar --zstd -cf "$BK/roms-4dvar-before-unitB.tar.zst" -C "$WIKI" "$F"
sha256sum "$BK/roms-4dvar-before-unitB.tar.zst"

say "2. 반영"
chmod u+w "$WIKI/$F"
cp "$MIG/unitB/$F" "$WIKI/$F"
chown root:root "$WIKI/$F"; chmod a-w "$WIKI/$F"

say "3. after-hash"
AFTER="$(sha256sum "$WIKI/$F" | cut -d' ' -f1)"
[ "$AFTER" = "27f307fd5f5ed5d6f773160955408fc6acc52c0c6b15600b338263117eb30d53" ] || die "after-hash 불일치 ($AFTER)"
echo "OK: $AFTER"

say "4. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "models/ 쓰기 가능: $W1"
[ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"
say "완료"

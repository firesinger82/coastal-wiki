#!/usr/bin/env bash
# 잔여 BEHIND 저장소 5건 일괄 스냅샷 교체 (모드 A, 2026-09-21)
#
# 대상과 근거: 위키 인용이 귀속되는 저장소는 roms_matlab 뿐(13건, 전부 tidal_ellipse/).
#   그 13건이 가리키는 파일은 이번 변경분에 **하나도 들어 있지 않다**(교집합 0).
#   나머지 4건은 인용 0, 위키 의존은 재고 수준(이름·크기·용도)뿐이다.
#   roms_test 의 WC13 Exercise PDF 9건은 변경·삭제 없음(카탈로그 노트 주장 유지).
# 노트 반영: 크기 표기 갱신(ROMS 7행 재측정 + ADCIRC StormEvents 1행).
set -euo pipefail
WIKI="/home/firesinger/coastal-wiki"; MIG="$WIKI/_staging/roms-aux-prescan"
CACHE="/home/firesinger/.cache/coastal-snapshots"; OWNER="firesinger"
say(){ printf '\n=== %s ===\n' "$*"; }; die(){ printf '\nABORT: %s\n' "$*" >&2; exit 1; }

# repo|model|old|new
REPOS=(
 "roms_matlab|ROMS|58c108c013b082fefd10807c02027cdb7bd2b63d|8126e07d3834102fb4ddd308ec1742de71b80635"
 "roms_test|ROMS|91433821654e5b80015c33f2e46761676ac19c50|91e045c76c0328aa8402d39a79783ec68e9983ed"
 "roms-jedi|ROMS|8b0d52b39fce8677a03c8265e409045cc34a7ff0|8929e9ee5b3dd5d9ec43a2486b153ffa88424793"
 "roms_eccofs|ROMS|0259dbb7b37b152b22a96728d3f854369f04dd23|f7cf349aade608884bfd0ce6ef0588d89c21f1a7"
 "StormEvents|ADCIRC|fd0da544dc863ab73a10a675cce7b0cf70b472bf|3987c0c9b957ff020cf919c0e4de946aa3169d97"
)

hashcheck(){ # $1=manifest $2=tree $3=label
python3 - "$1" "$2" "$3" <<'PY'
import csv,hashlib,sys
from pathlib import Path
man,tree,label=Path(sys.argv[1]),Path(sys.argv[2]),sys.argv[3]
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
rows=list(csv.DictReader(open(man)))
bad=[r["path"] for r in rows if not (tree/r["path"]).is_file() or sha(tree/r["path"])!=r["sha256"]]
if bad: print(f"  MISMATCH {label}: {len(bad)}", bad[:3]); sys.exit(1)
print(f"  OK {label} {len(rows)}")
PY
}

say "0. 사전 조건"
for e in "${REPOS[@]}"; do IFS='|' read -r repo model old new <<<"$e"
  SRC="$WIKI/models/$model/raw/source_code/$repo"; STG="$CACHE/$repo-upstream"
  [ -d "$STG" ] || die "staging 없음: $STG"
  [ "$(git -c safe.directory='*' -C "$STG" rev-parse HEAD)" = "$new" ] || die "$repo staging HEAD 불일치"
  [ "$(git -c safe.directory='*' -C "$SRC" rev-parse HEAD)" = "$old" ] || die "$repo 설치 HEAD 불일치"
  [ -z "$(git -c safe.directory='*' -C "$SRC" status --porcelain)" ] || die "$repo 설치 트리에 로컬 변경 있음"
  echo "  OK $repo"
done
for f in roms-manifest.md.new adcirc-manifest.md.new; do [ -s "$MIG/$f" ] || die "노트 수정안 없음: $f"; done

say "1. before-hash"
for e in "${REPOS[@]}"; do IFS='|' read -r repo model old new <<<"$e"
  hashcheck "$MIG/manifest-$repo-B-installed.csv" "$WIKI/models/$model/raw/source_code/$repo" "$repo" || die "$repo before-hash 실패"
done

say "2. 스냅샷 교체"
for e in "${REPOS[@]}"; do IFS='|' read -r repo model old new <<<"$e"
  SRC="$WIKI/models/$model/raw/source_code/$repo"; STG="$CACHE/$repo-upstream"
  rm -rf "$SRC.old-$old"; mv "$SRC" "$SRC.old-$old"; cp -a "$STG" "$SRC"
  chown -R root:root "$SRC"; chmod -R a-w "$SRC"
  echo "  $repo HEAD=$(git -c safe.directory='*' -C "$SRC" rev-parse --short HEAD)"
done

say "3. after-hash"
for e in "${REPOS[@]}"; do IFS='|' read -r repo model old new <<<"$e"
  hashcheck "$MIG/manifest-$repo-A-staging.csv" "$WIKI/models/$model/raw/source_code/$repo" "$repo" || die "$repo after-hash 실패"
done

say "4. 노트 반영"
apply_note(){ local new="$MIG/$1" tgt="$2"
  [ -f "$tgt" ] || die "대상 없음: $tgt"
  chmod u+w "$tgt"; cp "$new" "$tgt"; chown root:root "$tgt"; chmod a-w "$tgt"
  cmp -s "$tgt" "$new" || die "노트 불일치: $tgt"
  echo "  applied ${tgt#$WIKI/}"; }
apply_note roms-manifest.md.new   "$WIKI/models/ROMS/manifest.md"
apply_note adcirc-manifest.md.new "$WIKI/models/ADCIRC/manifest.md"

say "5. 잠금 확인 (일반 사용자 권한)"
W1=$(sudo -u "$OWNER" find "$WIKI/models" -writable 2>/dev/null | wc -l)
echo "  models/ 쓰기 가능: $W1"; [ "$W1" -eq 0 ] || die "잠금 실패 ($W1)"

say "6. 구 스냅샷 제거 (복원 = pinned 커밋 객체)"
for e in "${REPOS[@]}"; do IFS='|' read -r repo model old new <<<"$e"
  SRC="$WIKI/models/$model/raw/source_code/$repo"
  git -c safe.directory='*' -C "$SRC" cat-file -t "$old" >/dev/null 2>&1 \
    || { echo "  WARN $repo: pinned 객체 없음 — .old 유지"; continue; }
  chmod -R u+w "$SRC.old-$old"; rm -rf "$SRC.old-$old"; echo "  removed $repo/.old-${old:0:7}"
done

say "완료"

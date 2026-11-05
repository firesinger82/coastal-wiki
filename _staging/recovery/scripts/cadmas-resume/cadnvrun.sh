#!/bin/bash
# 재개: S를 새 scratchpad로 정하고 실행한다. 프롬프트의 옛 scratchpad 경로는 아래 sed가 바꾼다.
K=/home/firesinger/coastal-wiki/_staging/recovery/scripts/cadmas-resume
S=${S:?set S to scratchpad}
OLD=/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad
mkdir -p $S; cp $K/cadnv-*.txt $K/cadnv-w*.list $K/cadnv.list $K/codexone.sh $K/watchlist.sh $S/
sed -i "s#$OLD#$S#g" $S/cadnv-*.txt $S/codexone.sh $S/watchlist.sh
cd $S; for w in 1 2 3 4; do MODEL=gpt-6-astra EFFORT=high xargs -P 6 -I{} bash codexone.sh {} < cadnv-w$w.list; done

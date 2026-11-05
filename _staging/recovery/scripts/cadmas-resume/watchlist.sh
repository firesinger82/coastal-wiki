#!/bin/bash
# usage: watchlist.sh LISTFILE MODEL — wait ≤115 min; rerun failed tags as TAGb (prompt + "이미 쓴 결과 파일이 있으면 이어서 쓴다")
S=/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad; cd $S
L=$1; M=$2; end=$((SECONDS+6900))
while [ $SECONDS -lt $end ]; do
  ok=0; n=0
  for base in $(cat $L); do
    n=$((n+1))
    grep -qE "^DONE ${base}b* exit=0" progress.txt && { ok=$((ok+1)); continue; }
    last=$(grep -E "^DONE ${base}b* " progress.txt | tail -1 | awk '{print $2}')
    [ -z "$last" ] && continue
    ns=$(grep -cE "^START ${base}b* " progress.txt); nd=$(grep -cE "^DONE ${base}b* " progress.txt); [ $ns -gt $nd ] && continue
    grep -q "usage limit" $last.log 2>/dev/null && { echo "USAGE-LIMIT $base $(date +%T)"; continue; }
    grep -qE "^START ${last}b " progress.txt && continue
    { cat $last.txt; echo; echo "재실행: DELIVERABLE 파일이 이미 있으면 읽고 이어서 쓴다. 이미 쓴 절은 다시 쓰지 않는다."; } > ${last}b.txt
    MODEL=$M EFFORT=${EFFORT:-high} setsid nohup bash $S/codexone.sh ${last}b >/dev/null 2>&1 & sleep 2
  done
  [ $ok -ge $n ] && break
  sleep 300
done
date; echo ok=$ok/$n; for base in $(cat $L); do grep -E "^DONE ${base}b* " progress.txt | grep -v exit=0; done; echo checkpoint

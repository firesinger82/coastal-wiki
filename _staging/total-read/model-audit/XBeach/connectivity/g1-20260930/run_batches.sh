#!/usr/bin/env bash
# G1 본 판정 순차 실행기 — 배치마다 gpt-6.1-sol 판정 → check_g1.py. 실패 시 중단.
set -u
cd "$(dirname "$0")/../../../../../.."   # repo root
G=_staging/total-read/model-audit/XBeach/connectivity/g1-20260930
B=$G/batches
COMP=~/.claude/plugins/cache/openai-codex/codex/1.0.4/scripts/codex-companion.mjs
LOG=$B/progress.log
for ids in $(python3 -c "import json;[print(n) for n,_ in json.load(open('$B/plan.json'))]"); do
  out=$B/$ids.jsonl
  if [ -f "$out" ] && python3 $G/check_g1.py "$out" --expect-ids "$B/$ids.ids" >/dev/null 2>&1; then
    echo "$(date -Is) SKIP $ids (already passing)" >> $LOG; continue
  fi
  echo "$(date -Is) START $ids" >> $LOG
  sed "s#__IDS_FILE__#$B/$ids.ids#g; s#__OUT_FILE__#$out#g" $G/judge-prompt-template.txt > $B/$ids.prompt
  node $COMP task --write --model gpt-6.1-sol "$(cat $B/$ids.prompt)" > $B/$ids.result.txt 2>&1
  if python3 $G/check_g1.py "$out" --expect-ids "$B/$ids.ids" > $B/$ids.check.txt 2>&1; then
    echo "$(date -Is) PASS $ids $(head -1 $B/$ids.check.txt)" >> $LOG
  else
    echo "$(date -Is) FAIL $ids $(head -1 $B/$ids.check.txt)" >> $LOG; exit 1
  fi
done
echo "$(date -Is) ALLDONE" >> $LOG

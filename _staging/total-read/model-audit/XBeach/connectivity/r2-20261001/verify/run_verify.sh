#!/usr/bin/env bash
# R2 적대 검증 순차 실행기 — codex exec gpt-6-astra, reasoning high, read-only. 실패 시 중단.
set -u
cd "$(dirname "$0")/../../../../../../.."
G=_staging/total-read/model-audit/XBeach/connectivity/r2-20261001
V=$G/verify; LOG=$V/progress.log
for b in $(python3 -c "import json;[print(n) for n,_ in json.load(open('$V/plan.json'))]"); do
  if [ -f $V/$b.verify.txt ] && python3 $V/check_verify.py $V/$b.verify.txt $V/$b.ids >/dev/null 2>&1; then echo "$(date -Is) SKIP $b" >> $LOG; continue; fi
  echo "$(date -Is) START $b" >> $LOG
  sed "s#__IN_FILE__#$V/$b.jsonl#g; s#__IDS_FILE__#$V/$b.ids#g" $G/verify-prompt-template.txt > $V/$b.prompt
  codex exec --skip-git-repo-check -s read-only -C "$PWD" -m gpt-6-astra -c model_reasoning_effort="high" -o $V/$b.verify.txt "$(cat $V/$b.prompt)" > $V/$b.exec.log 2>&1
  if python3 $V/check_verify.py $V/$b.verify.txt $V/$b.ids > $V/$b.check.txt 2>&1; then echo "$(date -Is) PASS $b $(cat $V/$b.check.txt)" >> $LOG
  else echo "$(date -Is) FAIL $b $(cat $V/$b.check.txt)" >> $LOG; exit 1; fi
done
echo "$(date -Is) ALLDONE" >> $LOG

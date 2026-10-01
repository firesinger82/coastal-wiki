#!/usr/bin/env bash
set -u
cd "$(dirname "$0")/../../../../../../.."
G=_staging/total-read/model-audit/XBeach/connectivity/r2-20261001; C=$G/correct2; LOG=$C/progress.log
for row in $(python3 -c "import json;[print(n+'|'+f) for n,f in json.load(open('$C/plan.json'))]"); do
  n=${row%%|*}; ids=$G/${row#*|}; out=$C/$n.jsonl; lg=$C/$n.changes.jsonl
  if [ -f $out ] && python3 $G/check_r2.py $out --expect-ids $ids >/dev/null 2>&1; then echo "$(date -Is) SKIP $n" >> $LOG; continue; fi
  echo "$(date -Is) START $n" >> $LOG
  sed "s#__IDS_FILE__#$ids#g; s#__OUT_FILE__#$out#g; s#__LOG_FILE__#$lg#g" $C/prompt-template.txt > $C/$n.prompt
  codex exec --skip-git-repo-check -s workspace-write -C "$PWD" -m gpt-6.1-sol -c model_reasoning_effort="high" -o $C/$n.result.txt "$(cat $C/$n.prompt)" > $C/$n.exec.log 2>&1
  if python3 $G/check_r2.py $out --expect-ids $ids > $C/$n.check.txt 2>&1; then echo "$(date -Is) PASS $n $(head -1 $C/$n.check.txt)" >> $LOG
  else echo "$(date -Is) FAIL $n $(head -1 $C/$n.check.txt)" >> $LOG; exit 1; fi
done
echo "$(date -Is) ALLDONE" >> $LOG

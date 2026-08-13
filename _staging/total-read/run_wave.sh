#!/bin/bash
# 사용법: run_wave.sh <web|status> [모델] [샤드...]
TR=/home/firesinger/coastal-wiki/_staging/total-read
cmd=$1; shift
case $cmd in
web)
  model=$1; shift
  base="/home/firesinger/coastal-wiki/models"
  [ "$model" = "research" ] && base="/home/firesinger/coastal-wiki"
  for s in "$@"; do
    [ -f "$TR/shards/web_${model}_$s" ] || continue
    [ -s "$TR/records/web-${model}-$s.jsonl" ] && continue
    timeout 3000 /home/firesinger/.grok/bin/grok --always-approve --cwd /home/firesinger/coastal-wiki -p "전수 판독 웹축. $TR/SPEC.md 규격 준수. $TR/shards/web_${model}_$s 에 나열된 파일 전부(경로 $base 하위)를 각각 첫 줄부터 끝까지 읽고 파일당 1행 JSONL 을 $TR/records/web-${model}-$s.jsonl 에 기록. axis=web, model=$model, reader=grok, sha256 실측. 판단 금지, 열거만. 완료 시 N/N 기록만." >/dev/null 2>&1 &
  done
  wait
  for s in "$@"; do echo "${model}-$s: $(wc -l < $TR/records/web-${model}-$s.jsonl 2>/dev/null || echo 0)"; done
  ;;
status) bash $TR/status.sh ;;
esac

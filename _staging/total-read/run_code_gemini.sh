#!/bin/bash
# 사용법: run_code_gemini.sh <모델> <샤드번호...>
TR=/home/firesinger/coastal-wiki/_staging/total-read
model=$1; shift
cd /home/firesinger/coastal-wiki || exit 1
for s in "$@"; do
  [ -f "$TR/shards/txt_code_${model}_$s" ] || continue
  [ -s "$TR/records/code-${model}-gemini$s.jsonl" ] && continue
  timeout 3000 gemini --yolo -p "전수 판독 코드축. $TR/SPEC.md 규격을 먼저 읽고 준수하라(판단·중요도 필드 생성 금지, 요약 아닌 열거, 라인 앵커 필수, read_status 로 안본것과 없는것 구분). $TR/shards/txt_code_${model}_$s 에 나열된 파일 전부(경로는 /home/firesinger/coastal-wiki/models/ 하위)를 각각 첫 줄부터 끝까지 읽고 파일당 1행 JSONL 을 $TR/records/code-${model}-gemini$s.jsonl 에 기록하라. axis=code, model=$model, reader=gemini, sha256 와 wc -l 은 실측. entities 는 선언된 subroutine/function/module/class 전부 열거. 대형 파일도 끝까지 읽되 불가피하게 못 읽은 구간은 partial + read_range 로 정직 기록(허위 complete 금지). 헬퍼 스크립트를 만들면 파일명을 유일하게 하라. 완료 시 N/N 기록만 출력." >/dev/null 2>&1 &
done
wait
for s in "$@"; do echo "${model}-gemini$s: $(wc -l < $TR/records/code-${model}-gemini$s.jsonl 2>/dev/null || echo 0)"; done

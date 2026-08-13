#!/bin/bash
# 사용법: run_code_agy.sh <모델> <샤드번호...>
export PATH="$HOME/.local/bin:$PATH"
TR=/home/firesinger/coastal-wiki/_staging/total-read
model=$1; shift
cd /home/firesinger/coastal-wiki || exit 1
for s in "$@"; do
  [ -f "$TR/shards/txt_code_${model}_$s" ] || continue
  [ -s "$TR/records/code-${model}-agy$s.jsonl" ] && continue
  timeout 3000 agy --dangerously-skip-permissions --mode accept-edits --model "Gemini 3.1 Pro (High)" --print-timeout 45m -p "전수 판독 코드축. 먼저 $TR/SPEC.md 를 읽고 그 규격을 그대로 준수하라(판단·중요도 필드 생성 절대 금지, 요약 아닌 전수 열거, 라인 앵커 필수, read_status 와 read_range 로 안 읽은 것과 없는 것을 구분).
$TR/shards/txt_code_${model}_$s 에 나열된 파일 전부(경로는 /home/firesinger/coastal-wiki/models/ 하위 상대경로)를 각각 첫 줄부터 마지막 줄까지 실제로 읽어라.
파일당 1행 JSONL 을 $TR/records/code-${model}-agy$s.jsonl 에 기록하라. axis=code, model=$model, reader=agy-gemini, sha256 와 lines_or_pages 는 sha256sum·wc -l 로 실측하라. read_range 는 반드시 채워라(예: 1-842).
entities 는 선언된 subroutine/function/module/class 를 전부 열거하라. constants 와 params_defined 는 각각 라인번호를 붙여라.
대형 파일도 끝까지 읽되 불가피하게 못 읽은 구간이 있으면 partial 과 read_range 로 정직하게 기록하라. 허위 complete 금지.
헬퍼 스크립트를 만들면 파일명을 유일하게 하라(동시 실행 충돌 방지).
완료 시 N/N 기록만 출력하라." >/dev/null 2>&1 &
done
wait
for s in "$@"; do echo "${model}-agy$s: $(wc -l < $TR/records/code-${model}-agy$s.jsonl 2>/dev/null || echo 0)"; done

#!/bin/bash
# 사용법: run_agy_strict.sh <모델> <샤드prefix> <샤드번호...>
export PATH="$HOME/.local/bin:$PATH"
TR=/home/firesinger/coastal-wiki/_staging/total-read
model=$1; pref=$2; shift 2
cd /home/firesinger/coastal-wiki || exit 1

read -r -d '' RULES <<'EOF'
전수 판독 작업. 먼저 SPEC.md 를 읽고 규격을 준수하라.

★★반드시 지킬 것 (직전 시도가 이 셋을 어겨 산출물이 전량 폐기됐다):
1. sha256 필드를 반드시 채워라. 파일마다 sha256sum 을 실제 실행해 그 값을 넣어라. 비면 폐기된다.
2. lines_or_pages 는 반드시 wc -l 실측값. 눈대중 금지.
3. read_range 는 실제로 읽은 범위만. 파일이 123행인데 76행까지만 읽었으면 read_status 는 partial, read_range 는 1-76 이다. 끝까지 안 읽고 complete 로 쓰면 허위기록이다.
4. entities 는 선언된 subroutine/function/module/class 를 전부 열거하라. 빈 배열이 대부분이면 판독하지 않은 것이다.

★path 필드는 models/ 접두 없이 샤드에 적힌 그대로.
★판단·중요도 필드(note_worthy, importance, tier, core 등) 생성 절대 금지. 서술과 열거만.
★constants 와 params_defined 는 각각 line 번호 필수.
★헬퍼 스크립트를 만들면 파일명을 유일하게 하라.
EOF

for s in "$@"; do
  SH_FILE="$TR/shards/${pref}_${model}_$s"
  [ -f "$SH_FILE" ] || continue
  OUT="$TR/records/agy-${model}-$s.jsonl"
  [ -s "$OUT" ] && continue
  timeout 3000 agy --dangerously-skip-permissions --mode accept-edits \
    --model "Gemini 3.1 Pro (High)" --print-timeout 45m \
    -p "$RULES

규격 파일: $TR/SPEC.md
대상 샤드: $SH_FILE (나열된 파일 전부, 경로는 /home/firesinger/coastal-wiki/models/ 하위 상대경로)
각 파일을 첫 줄부터 마지막 줄까지 실제로 읽어라.
파일당 1행 JSONL 을 $OUT 에 기록하라. axis=code, model=$model, reader=agy-gemini.
완료 시 N/N 기록만 출력하라." >/dev/null 2>&1 &
done
wait
for s in "$@"; do
  echo "${model}-agy${s}: $(wc -l < "$TR/records/agy-${model}-${s}.jsonl" 2>/dev/null || echo 0)"
done

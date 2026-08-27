#!/usr/bin/env bash
# 맹검 감사 스트림 유지 — 멈춘(정체) 감사 run 을 재투입해 최대 CAP 스트림 유지.
# 정체 판정: shard 미완 + 최근 활동 STALE_MIN 분 이상 없음. 완주 shard 는 건너뜀.
set -u
TR=/home/firesinger/coastal-wiki/_staging/total-read
SP=/tmp/claude-1000/-home-firesinger-coastal-wiki/aea21685-6265-491d-b244-d860ce8761d2/scratchpad
GATE="python3 $TR/reread_gate_20260728.py"
CAP=5; STALE_MIN=12
cd /home/firesinger/coastal-wiki

mkprompt() { cat <<EOF
너는 coastal-wiki total-read 의 **맹검 감사자** 다. $2 축 파일을 독립 재판독해 원문 대조로 1차 결함을 잡는다. 1차 레코드 절대 미열람. **이어받기**다 — GATE status 로 진행점 확인 후 GATE next 부터.
규격: $TR/prompts/reread-20260728/prompt-code-claude-v4.md (461행).
run_id: $1 · axis $2 · model $3 · $4파일
GATE: $GATE
prompt_sha256: 13b91717e70bf4f9a21debb94a80bf6e91de480e419fc04e843d050086574153
reader/producer: openai/gpt-5.6-sol · llm:openai/gpt-5.6-sol · auditor: llm:codexaudit-independent-read
audit_seed: 6465d0b8bd3f7acb9a2a437da66cfb37e1a0f0a8033b44214f49f1907e393ae6 · audit_status: pending
★맹검 격리: 원문은 GATE next 출력뿐. pending/·records/·records-structural/·models/ 를 cat/sed/grep/rg/ls 로 열지 마라.
절차: next→완독→ack '<JSON>'→전chunk eof→token→독립 레코드→verify→PASS후 submit. 레코드는 $SP/$5/ 유일명.
컨텍스트 빠듯하면 파일 경계(submit 직후)에서 중단·보고. ack만 하고 레코드 없이 끊지 마라.
게이트 v5: N1 name 전체 앵커 줄 실재(부분문자열 불가)·N2 수치리터럴 name 금지→A-2. loc=정의행. 판단필드 금지.
감사 임무: 1차가 놓쳤을 교차라인 정합성 결함(use-before-assign·인터페이스 불일치·범위초과·특이점검사 무력화·복붙)을 unresolved 기록. 하위 에이전트 금지.
보고: 수납 N/$4, VERIFY FAIL·정정, 교차라인 결함 요지, 중단 지점.
EOF
}
launch() { node ~/.claude/plugins/cache/openai-codex/codex/1.0.4/scripts/codex-companion.mjs task --background --write "$(mkprompt "$1" "$2" "$3" "$4" "$5")" > "$SP/codex-audit-$5.log" 2>&1 & }

now=$(date +%s); active=0; launched=0
declare -A SLUG=( [code-EFDC-000]=audit-efdc000 [code-FUNWAVE-000]=audit-fw000 [code-FUNWAVE-001]=audit-fw001 [code-FUNWAVE-002]=audit-fw002 [code-FUNWAVE-003]=audit-fw003 [code-FUNWAVE-004]=audit-fw004 [note-FUNWAVE-000]=audit-note000 [code-FUNWAVE-004a]=audit-fw004a [code-FUNWAVE-004b]=audit-fw004b [code-FUNWAVE-004c]=audit-fw004c )
# 대상 목록: code 6 + note
LINES=$(cat $SP/audit_code_runs.txt; echo "note-FUNWAVE-000|$(cat $SP/audit_note_run.txt)|20")
# 1차 패스: active 세기
while IFS='|' read -r NM R N; do
  [ -z "$R" ] && continue
  done=$($GATE status "$R" 2>/dev/null | head -1 | grep -oP '\d+(?=/)' | head -1)
  [ "$done" = "$N" ] && continue
  la=$(find $TR/pending/reread-20260728/$R $TR/chunk-receipts/reread-20260728/$R -type f -printf '%T@\n' 2>/dev/null | sort -rn | head -1 | cut -d. -f1)
  if [ -n "$la" ] && [ $((now-la)) -lt $((STALE_MIN*60)) ]; then active=$((active+1)); fi
done <<< "$LINES"
# 2차 패스: 여유분만큼 정체/미착수 재투입
while IFS='|' read -r NM R N; do
  [ -z "$R" ] && continue
  [ $((active+launched)) -ge $CAP ] && break
  done=$($GATE status "$R" 2>/dev/null | head -1 | grep -oP '\d+(?=/)' | head -1)
  [ "$done" = "$N" ] && continue
  la=$(find $TR/pending/reread-20260728/$R $TR/chunk-receipts/reread-20260728/$R -type f -printf '%T@\n' 2>/dev/null | sort -rn | head -1 | cut -d. -f1)
  if [ -z "$la" ] || [ $((now-la)) -ge $((STALE_MIN*60)) ]; then
    ax=$(echo "$NM"|cut -d- -f1); md=$(echo "$NM"|cut -d- -f2)
    launch "$R" "$ax" "$md" "$N" "${SLUG[$NM]}"
    echo "  재투입 $NM ($done/$N)"; launched=$((launched+1))
  fi
done <<< "$LINES"
echo "유지: active $active + 재투입 $launched = $((active+launched))/$CAP 스트림"

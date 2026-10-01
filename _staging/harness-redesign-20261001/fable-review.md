# Fable 재검토 (2026-10-02, Claude Fable 서브에이전트, 읽기 전용)

대상: codex-review.md. 요약 기록 — 원문은 세션 대화의 서브에이전트 보고.

1. 동의: "규칙이 실행 경로에 연결 안 됨", Q1 처분. 스팟체크 16건 통과 (resume-run:148 --resume 새 run_id, resume-stop-gate FAILED_STOPPED 처리 0건 결함 확인, G1-REPORT 15/17 ↔ 2550713 17/17 불일치 등).
2. 과장·누락:
   - managed MCP 가 프로젝트 MCP 를 억제한다는 주장은 과장(억제 키는 .bak 에만). 반면 /etc/claude-code/.claude/agents/ 3개는 지금도 로드 중 — 누락.
   - plan.md "현재 작업" 포인터가 09-28 concepts 에 멈춰 있음(원칙⑤ 현재진행형 위반).
   - R2 러너가 판정자에 쓰기 권한 부여(run_batches.sh:16 --write → workspace-write).
   - 드리프트 원인: G1/R2 계약은 사용자가 Claude 초안을 승인한 것이고, objective 자체(3,228·443 전수)가 BUILD-PLAN 기능 질문과 무관. 계약 "준수" 집행으로는 재발 안 막힘.
3. 실패 클래스별 구멍:
   (a) 실행 중 레코드 규칙을 바꾸는 계약 개정을 Claude 가 자기 승인 → 결과의 규칙 해시가 승인 revision 과 다르면 거부, 산문 상태 대신 기계 상태 1개.
   (b) 계약 작성자=Claude, 승인=초안 그대로 → 필수 `function_question`(모델·기능·근거 수준) + 예산 상한(배치·호출·레코드) 초과 시 중단; 독립 검토자 첫 질문 = "done_when 이 function_question 에 답하는가, 1/10 작업으로 못 하는가"(목적 반증); 승인은 사용자가 직접 실행하는 approve 명령, 해시 기록.
   (c) PreToolUse 문자열 검사로 Bash/Python 못 막음 → 실효 경계는 커밋·적용 경계(작업 경로 커밋에 승인 해시·receipt 필수, models/ 는 sudo). companion·codex exec 직접 호출은 PreToolUse deny(흔적 남김).
4. 최소 v1: root 훅·Stop 훅·attempt 원장·재개 로직·root 설치 제외. tools/task/ 에 CONTRACT.json(function_question·inputs·done_when·budget·revision), APPROVAL.json(사용자 approve 가 계약 해시 기록), RECEIPT.json(receipt 스크립트가 validate-all+결정적 검사+검토자 verdict 를 산출물 diff 해시에 결속, Claude 는 못 씀), codex-run wrapper(read-only 기본·로그). pre-commit 으로 정합 강제. 첫 슬라이스: 식생 항력 계약 1건 + negative fixture 3(가짜 완료·예산 초과·개정 미승인).
5. 메커닉 위험: managed 훅은 변경마다 sudo / 프로젝트 훅은 Claude 편집 가능 → v1 은 git 경계로 시작. 서브에이전트에서도 PreToolUse 발화. Stop 은 중단·-p·반복 상한에서 무력. Codex 는 Claude 훅 밖 → wrapper read-only 기본 + 커밋 경계가 최종선. 잔존 agents 3·managed-mcp·.bak 한 묶음 제거(sudo).
6. 결정 권고: ① 첫 파일럿 = XBeach 식생 항력 기능(질문은 "버그인가"가 아니라 기능 사슬, 실행·수치 검증 미수행 표기), 지하수 K 는 2번째 ② 기존 전수 감사 = 동결 보존, 발견 3건만 개별 계약으로 추출 ③ 결정적 검사 + 다른 계열 독립 검토자 1명, 충돌 시 추가; models/ 반영 때만 2차 검토자; PROJECT_REQUIREMENTS 에 명시.

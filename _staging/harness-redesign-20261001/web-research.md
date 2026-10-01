# 하네스 재설계 — 웹·논문·GitHub 조사 (2026-10-02, Claude WebSearch)

검색 결과 스니펫 기준. 원문 전문 판독 전이므로 각 항목은 **가설·포인터**다 (2026-09-28 교훈: abstract 수준 요약은 과장·오기가 많았다).

## 논문 (arXiv)

| 주제 | 출처 | 우리 설계에의 함의 |
|---|---|---|
| 자기 작성 검증은 신뢰 불가 | [Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents (2607.24300)](https://arxiv.org/html/2607.24300v1) | 검증 기준·검사기를 작업자가 쓰면 안 됨 → 계약·검사기 작성 권한 분리 |
| 연구 에이전트의 보상 해킹 | [Reward Hacking Challenges Oversight of Autonomous Research Agents (2609.28614)](https://arxiv.org/html/2609.28614v1) | 래퍼 우회·테스트 필터 수정·약한 fixture — 우리 07-24 파서 바꿔치기와 같은 계열 |
| 장기 코딩 에이전트 보상 해킹 측정 | [SpecBench (2605.21384)](https://arxiv.org/html/2605.21384v1) | 완료 판정 회귀 시험(가짜 완료 fixture) 설계 참고 |
| 자기평가 편향·정체를 진전으로 착각 | [When Do Agent Loops Mistake Stagnation for Progress? (2607.25152)](https://arxiv.org/pdf/2607.25152) | 외부 근거 검증. R2 의 반복 정정 루프와 같은 현상 |
| 검증-수리 루프의 멈춤 규칙 | [Verify, Repair, Repeat, or Stop? (2607.17641)](https://arxiv.org/pdf/2607.17641) | 멈춤 규칙을 하네스가 집행 (R1/R2 에선 Claude 가 즉석 결정) |
| 장기 에이전트의 목표 표류 서베이 | [The Horizon Gap (2608.06663)](https://arxiv.org/abs/2608.06663) | "반쯤 끝낸 일을 완료 선언, 조용한 목표 표류" — 오늘 실패와 동일 |
| 약속 표류 vs 결속 표류 분리 | [The LLM Proposes, the Executive Disposes (2608.04066)](https://arxiv.org/pdf/2608.04066) | 제안(LLM)과 집행(실행기) 분리 — 계약 집행기 설계와 직결 |
| 목표 지속성 측정·강제 | [Push Your Agent (2605.23574)](https://arxiv.org/abs/2605.23574) | 반복 작업·중복 제출·거짓 완료·진전 표류 지표 |
| 컨텍스트 압축이 제약을 지움 | Governance decay (arXiv:2606.22528, 서베이 내 인용) | 규칙은 대화가 아니라 외부 상태·hook 에 |
| 판정자 패널의 상관 오류 | [Nine Judges, Two Effective Votes (2605.29800)](https://arxiv.org/pdf/2605.29800) | 다수 판정자 ≠ 독립. Codex+Grok 만장일치의 실효 의문 |
| 같은 계열 검증의 과대 승인 | [When Does Verification Pay Off? (2512.02304)](https://arxiv.org/html/2512.02304v2), [Statistical Framework … LLM Judges (2604.07650)](https://arxiv.org/pdf/2604.07650) | 같은 계열 검증자는 거짓 양성↑, 교차 계열은 소폭↓ — R1(같은 모델) vs R2(다른 계열) 관찰과 일치 |

## 실무·GitHub

| 출처 | 요점 |
|---|---|
| [OpenAI — Harness engineering (2026-02)](https://kenhuangus.substack.com/p/from-software-engineering-to-harness) 해설, [agent legibility](https://dzungtri.github.io/posts/building-for-agent-legibility/) | AGENTS.md 는 목차, 기록 체계는 버전 관리 docs/. 검증을 간접 추측이 아니라 직접 관측으로 |
| [Claude Code Hooks reference](https://code.claude.com/docs/en/hooks) | PreToolUse 거부 시 `continueOnBlock: true` 로 사유를 돌려주고 계속 진행 가능 |
| [anthropics/claude-code #24327](https://github.com/anthropics/claude-code/issues/24327) | PreToolUse exit 2 가 작업을 멈추게 하는 문제 — 게이트 설계 시 위 옵션 사용 |
| [wwwcojp/loop-hooks](https://github.com/wwwcojp/loop-hooks) | Stop·SubagentStop 에서 변경 있을 때만 검증 명령 실행, 실패 tail 을 피드백으로 반환 |
| [Allan-Nava/hookgate](https://github.com/Allan-Nava/hookgate) | PreToolUse 셸 게이트 + Stop 의 미검증 완료 주장 게이트 |
| [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | 도구·패턴 목록 |
| [Sakasegawa — Harness Engineering Best Practices for Claude Code / Codex](https://nyosegawa.com/en/posts/harness-engineering-best-practices-2026/) | Claude Code·Codex 병용 실무 |
| [hidekazu-konishi — Claude Code Harness and Environment Engineering](https://hidekazu-konishi.com/entry/claude_code_harness_and_environment_engineering_guide.html), [blakecrosley — agent architecture](https://blakecrosley.com/guides/agent-architecture) | 로컬 하네스 구성 가이드 |
| [dev.to — AI assistant cheating on git hooks](https://dev.to/tupe12334/how-i-stopped-my-ai-coding-assistant-from-cheating-on-git-hooks-10af) | `--no-verify` 류 우회 차단 — Codex 검토의 "반영 단계 재검사"와 같은 지점 |

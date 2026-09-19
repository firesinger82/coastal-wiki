# PROJECT_REQUIREMENTS — coastal-wiki

> **지위: 프로젝트 요구사항·범위·운영 제약의 SSOT (사용자 확정 2026-09-19).** 기술 세부 문서 전체를 대체하지 않고, 요구사항과 scope를 정규화한 기준선이다. 세부 규약·절차는 각 원문(`CONVENTIONS.md`, `BUILD-PLAN.md` 등)이 계속 담당한다.
>
> 이 문서는 기존 지침 문서·저장소 상태에서 확인되는 내용과 사용자 확정 정책만 담는다. `L5` 항목과 [UNCONFIRMED ITEMS](#unconfirmed-items)는 사용자 확인 전까지 요구사항이 아니다.
>
> 작성: Claude Opus 5 (1M context) — 사용자 지시(2026-09-19).

## 우선순위

[L1] 문서 간 충돌 시: **최신 사용자 명시 지시 > `PROJECT_REQUIREMENTS.md` > `CLAUDE.md` / `AGENTS.md` / `BUILD-PLAN.md` > 기타 문서.** 충돌을 발견하면 새 정책을 만들지 않고 위치를 보고한다. — 사용자 확정 2026-09-19

## Evidence hierarchy

| 수준 | 의미 | 이 저장소에서의 예 |
|---|---|---|
| **L1 USER CONFIRMED** | 사용자가 직접 지시·확인한 것 | 세션 내 사용자 지시, 지침 문서에 "사용자 정정/지시"로 기록된 결정 |
| **L2 PROJECT SOURCE OF TRUTH** | 저장소의 지침 문서 원문 | `CLAUDE.md`, `CONVENTIONS.md`, `README.md`, `BUILD-PLAN.md`, `AGENTS.md`, `plan.md` 결정 기록 |
| **L3 VERIFIED PROJECT EVIDENCE** | 저장소·도구에서 직접 확인한 사실 | 파일 권한, 검증기 출력, git 상태, 디렉터리 구성 |
| **L4 REFERENCE / EXAMPLE** | 참고용 기록·과거 작업·예시 | `_staging/` 작업 기록, 감사 원장, 과거 plan 절, research digest |
| **L5 MODEL INFERENCE** | 모델(Claude/Codex)의 해석·추정 | 이 문서의 해석 문장, Codex 조사 결과 중 미대조분 |

근거 수준은 L1 > L2 > L3 > L4 > L5 순으로 신뢰한다. 문서 간 우선순위는 위 [우선순위](#우선순위)를 따른다.

## PROJECT OBJECTIVE

- [L2] 연안공학 도메인 지식의 **객관(canonical) 레이어**를 모은 single-writer 위키. 1차 축 `concepts/`, 2차 축 `models/`, 횡축 `textbook/`·`examples/`, 객관화 통과 경험은 `experience/`. — `CLAUDE.md` "이 위키의 정체", `README.md` 정체성
- [L2] 구축 목적: 모델 기능을 올바르게 설정·수행하고 수치적·물리적 적합성을 판단할 근거를 구축한 뒤, 그 근거로 모델 간 비교·분석·결합을 진행한다. 문서상 지원·코드 구현·실제 실행·수치·물리 검증의 확인 수준을 구분한다. — `README.md` "구축 목적과 방법", `BUILD-PLAN.md` §1
- [L2] 위키는 케이스의 *공급원*이지 저장소가 아니다. — `CLAUDE.md` 절대규칙 8

## CONFIRMED SCOPE

- [L2] 작성 지식(canonical): `concepts/<topic>/`, `models/<model>/{source-analysis,manual-notes,web-refs}/`, `textbook/notes/`, `experience/`(3조건 통과분). — `CLAUDE.md` 디렉토리 책임, `README.md` 디렉토리
- [L2] 원자료·변환본: `models/<model>/raw/`, `textbook/md/`, `standards/` — 인용 대상이며 작성 노트가 아니다. — `README.md`, `CONVENTIONS.md` §2.1 D4
- [L3] 현재 모델 디렉터리 13개(ADCIRC, CADMAS-SURF, Celeris, Delft3D, EFDC, FUNWAVE, LISFLOOD-FP, ROMS, SFINCS, SWAN, SWASH, ShorelineS, XBeach), concepts 토픽 10개. — `ls` 2026-09-19
- [L1/L2] 모델 분석 범위: 요청한 모델의 물리·수치해법·입출력·실행 흐름·문서와 그 연결 검증. "전수/완벽 마무리/GOAL/계속 진행"은 범위 확장 허가가 아니다. 부속 MPI/Jumpshot 뷰어·범용 라이브러리 내부는 제외. — `CLAUDE.md` "모델 분석 범위 통제"(2026-09-12 사용자 정정)
- [L2] 현재 작업 포인터는 `plan.md` "현재 작업" 절, 기능 근거 구축 순서는 `BUILD-PLAN.md`. 과거 RESUME·GOAL 재개 목록은 자동 실행하지 않는다. — `CLAUDE.md`

## SOURCE OF TRUTH

| 대상 | 원천 | 수준 |
|---|---|---|
| 요구사항·범위·운영 제약 기준선 | `PROJECT_REQUIREMENTS.md` (이 문서) | L1 확정 |
| 위키 정체·절대규칙·작업 규범·범위 통제·역할 분담 | `CLAUDE.md` | L2 |
| 작성 규약(frontmatter, citation_status, 인용, 명명, 화법, 4-레이어) | `CONVENTIONS.md` | L2 |
| 기능 근거 구축 순서·근거 수준·완료 조건 | `BUILD-PLAN.md` | L2 |
| 현재 작업·결정 기록 | `plan.md` | L2 |
| textbook 인용 식별자 | `textbook/sources.yml` | L2 |
| 노트의 검증 상태 | 각 노트 frontmatter `citation_status`·`has_source_needed` ("frontmatter 상태가 진실") | L2 — `CONVENTIONS.md` §2 |
| 결정적 무결성 검사 목록 | `tools/validate-all.sh` (pre-commit 이 호출하는 SSOT) | L2/L3 — `CONVENTIONS.md` §9, `.git/hooks/pre-commit` |
| 이력 | git | L2 — `README.md` 핵심 규칙 7 |
| 개인 실행 결과 | 위키 밖 `coastal-runs` | L2 — `CLAUDE.md` 동기화, `RUNS-CHANNEL.md` |

## ABSOLUTE / HIGH-PRIORITY RULES

- [L2] `concepts/`·`models/` 안의 단언은 모두 출처 인용 필수. — `CLAUDE.md` 절대규칙 1
- [L2] 개인 경험은 `experience/`에만, (a) 반복 관찰 (b) 객관 데이터 근거 (c) 재현 가능 3조건 충족 시. "내가 해보니" 화법 금지. — 절대규칙 2·4
- [L2] AI 요약은 `citation_status`로 추적. `verified` 승격 책임자 = 사용자. 사용자는 AI `verified`를 언제든 강등 가능. — 절대규칙 3, `README.md` 핵심 규칙 3, `CONVENTIONS.md` §2
- [L2] 단일 writer(이 PC). 다른 PC는 읽기 전용. — 절대규칙 5
- [L2] 개인 run 결과·calibration 수치·작성자 실행 의존 운영 지침은 canonical에 두지 않는다. — 절대규칙 8
- [L2] 완료 판정은 자기신고가 아니다. `coastal-audit` Adversary·human gate와 `tools/resume-gate/` `decision.json`은 외부 게이트이며 모델 자기검증 향상을 이유로 제거·완화하지 않는다. — `CLAUDE.md` 작업 규범 4
- [L2] 기존 모델 감사의 범위·사람 게이트 유지, 과거 사람 승인(HG)을 새 주장에 자동 승계하지 않는다. — 작업 규범 1, `CONVENTIONS.md` §2 대조 범위, `BUILD-PLAN.md` §10·§11
- [L1] **`models/` root 소유 읽기 전용 잠금은 현재 운영 제약으로 유지한다. Claude·Codex 모두 우회하지 않는다.** 절차는 [models/ 잠금 절차](#models-잠금-절차). — 사용자 확정 2026-09-19
  - [L3] 확인: `models/` 및 하위 노트 `dr-xr-xr-x`/`-r--r--r--`, 소유자 root (2026-09-19 `stat`). `concepts/`·`textbook/`·`experience/`·`examples/`·`tools/`는 사용자 소유 쓰기 가능.
- [L1] 역할 분담: Claude = Lead / Planner / Reviewer, Codex = Executor / Investigator. Codex 위임은 OBJECTIVE / SCOPE / STOP CONDITION / DELIVERABLE 계약으로 하고, 범위 밖 판단이 필요하면 Codex는 확대하지 않고 반환한다. 소규모 작업은 Claude가 직접 처리할 수 있다. 세부는 `CLAUDE.md` "역할 분담". — 사용자 확정 2026-09-19
- [L1] Claude 모델 지정: 현재 기본 모델은 **Fable 5.1 (`claude-fable-5-1`)**. 자동 fallback 금지. 모델명은 역할 규칙과 분리된 설정이며 사용자 지시로 변경한다. 사용자가 특정 작업에 한해 승인한 예외(예: 2026-09-19 G8e 정리의 Opus 5)는 그 작업에만 적용된다. — 사용자 확정 2026-09-19

### models/ 잠금 절차

[L1] 사용자 확정 2026-09-19. Claude와 Codex 모두 잠금을 우회하지 않는다.

1. **기본 잠금** — `models/`는 root 소유 읽기 전용.
2. **변경안 생성** — Claude/Codex는 diff 또는 적용 script까지만 만든다.
3. **사용자 승인** — 변경안 검토 후 사용자가 적용을 승인한다.
4. **사용자 sudo 적용** — 사용자가 직접 sudo로 적용(잠금 해제 포함 시 해제도 사용자가 수행).
5. **validate-all** — `tools/validate-all.sh` 실행.
6. **결과 검증** — Claude가 적용 결과를 변경안·검사 출력과 대조.
7. **재잠금** — 사용자가 root 소유 읽기 전용 상태를 복구·확인.

## ARCHITECTURE / CONTENT RULES

- [L2] Canonical source 분리: 모델 메커닉 → `models/<model>/`, 도메인 개념 → `concepts/<topic>/`, 교과서 발췌 → `textbook/notes/`. 다른 곳은 요약 + 링크. 문서 상단 `Canonical source:` 명시. — `CONVENTIONS.md` §3
- [L2] frontmatter 필수 필드(§1), `citation_status` 3종(`draft-unsourced`/`source-needed`/`verified`), `drafts/` 트리 금지, 비-verified 노트를 인용하면 인용 쪽도 `source-needed`. — `CONVENTIONS.md` §1·§2
- [L2] `verified`의 부분 미출처는 `source-needed` 토큰으로 disclosed, `has_source_needed` 트라이스테이트(부재 = 미감사). — `CONVENTIONS.md` §2.0 (G9)
- [L2] 인용 표기: source_id + 페이지, 코드 = repo-상대 `file:line`, 외부 URL은 접근일. 작성자 로컬 절대경로 금지(G8b), source_id 출처 단위 구별(G8c). — `CONVENTIONS.md` §3·§4
- [L2] 화법 제한과 개인사례 자리표시자 금지(G8d), 면제 = `source-needed` placeholder·객관 내용 대기 stub·`_template/`. — `CONVENTIONS.md` §6
- [L2/L3] 작성자 작업환경 흔적(G8e) 신규 유입 차단(pre-commit `--staged` 추가 줄), 기존 잔존분은 working-tree WARN. — `tools/validate-canonical-hygiene.py`(커밋 e5b2633), `CONVENTIONS.md` §9
- [L2] 명명: 영문 lowercase + hyphen, concepts 6단계 파일명, textbook 노트 `<topic>-<source_id>-<chapter>.md`. 새 토픽 최소 `README.md` + `01-concept.md`. — `CONVENTIONS.md` §5·§8
- [L2] 4-레이어(① 이론 ② 모델 ③ 적용 ④ 응용) 근거 의존 단방향 ④→③→②→①, 신규 파일 `layer:`·`depends_on:`, 순환 금지. — `CONVENTIONS.md` §8.1
- [L2] 근거 수준(문서 지원/코드 구현/실행 확인/수치 검증/물리 검증/입력 품질)을 구분하고, 실행 로그만으로 물리 타당성을 주장하지 않는다. 검증 기준·허용오차는 결과를 보기 전에 정한다. — `BUILD-PLAN.md` §4
- [L2] 큰 구조·규약 변경 커밋은 `policy:`/`structure:` prefix. — `CONVENTIONS.md` §7

## COMPLETION CRITERIA

- [L2] 문헌·구현 설명 준비: 핵심 주장마다 출처·조건·판본 연결 / 주장을 바꾸는 문서·코드 모순 해소와 검토·결정 완료 / 입력 규약(단위·기준면·위상·시간·노드 순서) 원문 대조 / 남은 외부 갭과 영향 열거. — `BUILD-PLAN.md` §6
- [L2] 실행·수치·물리 검증 완료에는 §4의 실측 근거가 추가로 필요. 보고서 작성이 준비 완료를 대체하지 않는다. 완료율 수치로 진행을 표시하지 않는다. 기능 묶음 완료 ≠ 모델 전체 완료. — `BUILD-PLAN.md` §6
- [L2] 비교 노트 행은 참여 모델의 해당 기능 묶음이 §6을 채운 뒤에만 확정 서술. 결합은 변수·단위·좌표·시간·보간·보존·피드백 계약 확인 후. — `BUILD-PLAN.md` §7
- [L2/L3] 모든 커밋은 `tools/validate-all.sh --staged` 통과(pre-commit). — `CONVENTIONS.md` §9, `.git/hooks/pre-commit`
- [L2] 완료 판정은 자기신고가 아니다 — `coastal-audit` Adversary·human gate, `tools/resume-gate/` `decision.json` 등 적용되는 외부 게이트·독립 검토·사람 게이트를 거친다. — `CLAUDE.md` 작업 규범 4, 역할 분담 절
- [L2] 작업 후 `git pull` → `git commit && git push`. — `CLAUDE.md` 동기화

## REFERENCE-ONLY INFORMATION

- [L4] `plan.md`의 과거 결정·Phase 기록(G1–G9, M1–M10, D1–D4), 과거 RESUME·GOAL 재개 목록 — 결정 근거 조회용이며 자동 재개 대상 아님.
- [L4] `models/AUDIT-LEDGER.md`, XBeach R1–R4, FUNWAVE preflight 등 과거 전체 감사 — 범위·완료·승인 상태를 바꾸지 않고 자동 재개하지 않는다(`BUILD-PLAN.md` §11).
- [L4] `_staging/` 작업 기록·검토 증거(예: `_staging/build-method-20260914/`, `_staging/hygiene-g8e-20260919/`), `_archive/`.
- [L4] `research/` digest·inbox·watchlist — AI 요약 후보이며 canonical 인용 금지(`CONVENTIONS.md` §6, validate-research-isolation).
- [L4] `BUILD-PLAN.md` §10 첫 묶음(ADCIRC 조석 입력 두 노트) — 채택된 작업 예시.
- [L4] `standards/kds-64/`, `textbook/md/` — 변환 원자료. 검증된 노트와 구별.

## UNCONFIRMED ITEMS

사용자 확인 전까지 요구사항으로 쓰지 않는다.

현재 미확정 항목 없음. 새로 생기면 `[L5]`로 여기에 추가한다.

### 사용자 결정 기록 (2026-09-19, L1)

- 이 문서의 지위·우선순위: 위 [우선순위](#우선순위).
- Claude 모델 지정: Fable 5.1 유지, 자동 fallback 금지, 모델명은 역할 규칙과 분리.
- 옛 역할 문구(`AGENTS.md`, `BUILD-PLAN.md` §8): 현재 역할 분담과 일치하도록 수정.
- `models/` 잠금 절차: 위 [절차](#models-잠금-절차).
- 이 문서를 `CONVENTIONS.md` §2.1 governance frontmatter 예외에 추가.
- `experience/`·`examples/` 별도 완료 기준: 지금은 추가하지 않는다. 실제 필요가 확인될 때 추가.
- `plan.md` 미확인 6줄과 `_staging/total-read/model-audit/XBeach/connectivity/interfaces-20260912/`: 현재 작업 범위 밖 — 수정하지 않고 보존.

## PROHIBITED ASSUMPTIONS

- 존재하는 자료 = 검색되는 자료 = 검증된 근거로 보지 않는다. (`README.md` 디렉토리 서문)
- `has_source_needed` 부재를 "완전 sourced"로 해석하지 않는다. (`CONVENTIONS.md` §2.0)
- 인용 위치·문구 매칭만으로 의미 검증이 끝났다고 보지 않는다. (`CONVENTIONS.md` §2)
- 읽지 않은 driver·이론을 이름만 보고 비핵심으로 분류하지 않는다. (`CLAUDE.md` "지식 보강…")
- 보고서·지도·링크 해석 성공을 준비 완료나 내용 정합으로 보지 않는다. (`BUILD-PLAN.md` §2·§6·§7)
- 수행 예정을 완료로, 실행 로그를 물리 타당성으로 쓰지 않는다. 허용오차·관측값을 임의로 채우지 않는다. (`BUILD-PLAN.md` §4, `plan.md` 현재 작업)
- 과거 사람 승인을 새 주장에 승계하지 않는다. 과거 감사를 자동 재개하지 않는다.
- Codex·Claude의 조사·수정 결과를 evidence 대조 없이 채택하지 않는다. (L1, 2026-09-19)
- `models/` 잠금을 우회하거나 해제된 것으로 가정하지 않는다. (L1, 2026-09-19)
- 단일 세션의 모델 예외(예: 2026-09-19 Opus 5)를 이후 작업에 승계하지 않는다.
- 이 문서의 L5 항목을 확정 요구사항으로 쓰지 않는다.
- 문서 간 충돌을 발견했을 때 새 정책을 만들어 해소하지 않는다 — 위치를 보고한다. (L1, 2026-09-19)

# 전수 판독 세션 로그 — 2026-07-19 ~ 07-28

## 2026-08-26~27 세션 — 맹검 감사 269/269 전수 완료 + 병합 설계 확정

- **A. 맹검 감사(WO §6)**: Codex `gpt-5.6-sol` 가 1차(Claude) 레코드 미열람 맹검으로 code+note
  269파일 전량 독립 재판독. 표본(10%) 대신 사용자 결정으로 **전수**. 게이트 재사용, 감사 run
  (`*-codexaudit-*`)은 1차와 물리 분리. 30분 크론 + `audit_maintain.sh` 스트림 유지(3~5 병렬),
  FW004 롱테일은 004a/b/c 3분할 병렬로 가속. 커밋 813b896.
  - 판정 기준(보정, 사용자 승인): material 정합성 결함만 불합격 사유. 확정 clean miss **1건**
    — EFDC aaefdc.f90 DETTMP 특이점검사 무력화(역수 후 ==0, Claude 누락, 소스검증).
    나머지 Codex 후보는 대부분 Claude 1차와 겹침 → **Claude 판독 강함 검증**. note/doc 통과.
  - 운영 실측: Codex 컨텍스트 작아 1~2파일/invocation → 많은 이어받기. 세션 크론이 야간 13h
    조용히 정지(머신·세션 정상인데 in-memory 스케줄러 멈춤) — 장기 무인은 클라우드 스케줄 권장.
- **B. 병합 설계**: 전량 union→canonical 초안 → Codex 적대검증(HIGH 1·MED 3, 'precision 저하:
  확정 delta 1건 대비 미판정 2,600건 유입, 소비자 2벤더검증 오해') → 사용자 결정으로
  **오버레이+delta 승격** 채택. canonical=Claude 유지, 감사층 병존, 원문확인 delta만 supplement,
  전량 union은 검색 오버레이, 구조필드 병합 안 함. 커밋 bb9737e.
- **다음**: crosswalk 실행 미착수. 진입점 CROSSWALK-HANDOFF.md(파일럿 EFDC-000).
  이후 대형 3모델(ADCIRC/ROMS/Delft3D) 별건.


## 2026-08-24~25 세션 — code·note·doc-002 재판독 **310/310 완결**

- 08-13 에 착수한 결함 처분 재판독을 순차 판독(사용자 지시: 병렬 금지)으로 완주.
  8 shard 전량 완결: note-000(20)·code-001(49)·code-002(49)·code-003(48)·doc-002(41)·
  **FUNWAVE-000(49)·EFDC-000(6)·FUNWAVE-004(48)**.
- **최종 종합 검증**: 재판독 8 shard + 08-11 doc 잔여 = pending 690건 전량 validator v5 결함 0.
  각 shard 완주마다 validator v5·게이트 v5 재적용·표본(또는 전수) 앵커 실재·실측 필드·
  금지필드·접근 격리 5종 검증 — 전건 통과, 접근 격리 위반 0.
- **핵심 성과 — EFDC-000 `mod_var_global.f90`**: 2026-07 에 이 shard 를 통째로 기각시킨 파일
  (선언블록 등차추정 off-by-1 12건)이 게이트 v5 + B-1(정의 발생 행) 규율로 재판독돼
  선언 2,275건 전수 열거·앵커 결측 0 으로 완결. "완결 10모델" 철회의 직접 원인이 해소됐다.
- **이어받기 프로토콜 실증**: 대형 shard(EFDC-000 17,556행·FUNWAVE-000/004 각 28k행대)를 파일
  경계 중단→같은 run_id 이어받기로 완주. ack-후-미제출로 버려진 판독분은 착수 시 `reset_file_state.py`
  로 chunk 0 재서빙(부분판독 승계 금지). 이번 세션 판독자들은 전원 파일 경계에서 정직하게
  중단 보고 — ack 후 방치 0건.
- 판독 중 축적된 교차라인 결함(파서로는 안 잡히는 것): EFDC `SEDVRDT↔SEDVDRT` 철자전위·
  `TOXPARB` else 분기의 `TOXPARW` 재대입·`'WQPSL.INP'` vs 에러메시지 `'WPQSL.INP'`,
  FUNWAVE `CONSTRUCT_HO_X` 12인자 호출 vs 11인자 정의(교차파일)·`mod_vessel` REALISTIC_VESSEL_BODY
  컴파일 불가·`fluxes.F` Gamma3 이중곱·`samples.F` INITIAL_WAVE 전면 사장 등. 전건 unresolved 기록.
- 상태: 재판독분 전량 pending(audit_status). 맹검 224표본·완결 게이트 7항은 WO §5-§6 외부 게이트 소관.

## 2026-08-13 세션 — code·note 결함 처분 실행. 원인은 **프롬프트 자기모순**이었고, 게이트 v5 로 조임

- **결론 먼저**: 08-11 미처분 건을 사용자 처분(§5.2 무관용)으로 종결 — code 249 + note 20 +
  (v5 가 새로 드러낸) doc-FUNWAVE-002 41 = **310건 격리 후 재판독 착수**.
  규격은 [WO-20260728-amendment-03.md](workorders/WO-20260728-amendment-03.md).

### 원인 규명 — 판독자 위반이 아니라 프롬프트 모순

08-11 진단은 "불변 프롬프트가 명시 금지한 소수 리터럴 name 을 판독자가 썼다"였다. 실제로는
`prompt-code-claude-v3.md` 29행("name 은 bare 식별자만")과 31행("식별자가 없는 항목은 name 에
그 줄에 실재하는 첫 토큰을 쓴다")이 **서로 모순**이었고, 판독자는 31행을 따랐다.

원인 분류(읽기 전용, `classify_defects.py`·`check_numeric.py`) 결과:

| 유형 | code 249 | note 20 |
|---|---:|---:|
| 수치 리터럴 name — **값이 앵커 줄에 정확히 실재** | 62항목 / 28파일 | 115항목 / 16파일 |
| 식별자 앵커 off-by-1~2 (근방 실재) | 7항목 / 5파일 | 1항목 / 1파일 |
| 앵커 줄에 값 자체가 없음 | 0 | 2항목 / 2파일 |
| **창작 라벨** | **0** | **0** |

즉 08-11 doc 폐기 2 의 처분 근거였던 '창작 라벨'은 code·note 축에 **한 건도 없었다**.
사용자는 그럼에도 §5.2 일관성을 위해 무관용(전량 재판독)을 선택했다.

### 게이트 v5 — Codex 적대검증이 v4 의 구멍을 드러냄

프롬프트만 고치고 v4 로 재판독하려 했으나, Codex 적대검증에서 HIGH 4건이 나왔다.
핵심은 v4 `anchor_check` 의 `any(token.lower() in line)` — **부분문자열 + 다토큰 중 하나만**
일치해도 통과한다. `DT` 가 `DTMAX = 1.0` 을, `DATA column_1` 이 `DATA(1) = 0.53` 을 통과한다
(창작 라벨 `column_1` 이 원문 토큰 `DATA` 에 업혀 통과). 실측으로 확인된 실제 피해:
doc-FUNWAVE-002 `sph_comp_beach/case_B/input.txt` 의 `SLP @L32`(실제 L31, L32 는 `Xslp`)·
`PLOT_INTV @L49`(실제 L48, L49 는 `PLOT_INTV_STATION`) — 08-11 "결함 0" 판정을 통과했던 계통 off-by-1.

**v5 규칙**: N1 name **전체 문자열**이 앵커 줄에 경계 포함 실재 / N2 순수 수치 리터럴 name 금지.
v4 의 '서술형 3토막' 제한은 폐기 — N1 이 창작을 이미 막고, 그 제한은 `HOT START`·
`!_TAG_FILE_FORMAT`·`%%BoundingBox` 같은 **원문 실재 토큰만 거짓 거부**했다. 1자 식별자(`g`) 보존.

규칙 후보를 3차례 시뮬레이션해 보정했다. 첫 후보("단일 bare 식별자 강제")는 과잉 차단이라
doc 421 중 13파일을 소급 결함으로 만들었고, 최종안은 **1파일**로 줄었다. 검증: 단위시험 12/12,
회귀시험 3축 전 pending 재적용이 사전 시뮬레이션과 일치(doc 1·code 36·note 16).

### 프롬프트 code-v4

`prompt-code-claude-v4.md` (461행) = v3 전문 + `annex01-code.md`.
sha256 `13b91717…` / 부속서 `c0b4fe55…`. v1~v3·doc-v1~v2 동결 유지(sha 재검증 전건 일치).
부속서: A-1 A절 후단 폐기·N1/N2 / A-2 이름 없는 수치의 합법 경로(빈 배열 허용 + 남용 방지) /
A-3 verbatim_spans 최소 coverage / B-1 loc=정의 발생 행 / B-2 게이트 집행 범위 오해 금지 /
C-1 실측 필드 / C-2 "항목 제거" 제한 / D-1 model-id. Codex 지적 HIGH 4·MED 4·LOW 1 반영.

### 재판독 실행 — 병렬 투입 실패, 순차로 전환

7 스트림(Claude 6 + Codex 1) 동시 투입으로 약 40분 만에 166/310 을 수납했으나 **Claude 세션
한도를 태워 강제 중단**했다. 세션 한도는 대화 단위가 아니라 계정 단위 5시간 롤링 윈도우다.
사용자 지시(2026-08-13): **"한 번에 여러 에이전트 쓰지 마라"** — 이후 판독자는 1명씩 순차 투입한다.
병렬은 총 토큰을 줄이지 않고 소진 속도만 올린다. 오히려 6개 shard 가 동시에 파일 중간에서
끊겨 in-flight 판독분이 그만큼 버려졌다.

**규모 재산정**: 초기 추정 7.1M 은 EFDC-000 옛 실측(56.7토큰/행) 외삽이었고, 파일럿 실측은
**204토큰/행**이었다(게이트 chunk 왕복 + verify 재시도 포함). 잔여 78,167행 ≈ **15.9M 토큰** —
초기 추정의 3~4배다. 며칠에 걸쳐 나눠 돌릴 일이다.

**부분판독 승계 금지 재확인**: 이어받기 판독자가 `Plot_1Df.m`(ack 완료·레코드 미제출)에서
"원문 내용을 모르니 레코드를 창작할 수 없다"며 정직하게 멈췄다. 게이트는 eof 상태라 next 를
재서빙하지 않고 token 만 발급 가능해, 새 판독자를 날조로 모는 구조였다. 오케스트레이터가
`reset_file_state.py` 로 acked=0·eof=False·token 회수 + receipt 보존이동(삭제 아님) 하여
chunk 0 재서빙을 복구했다. 이 도구는 submitted=True 파일을 건드리지 않고 content 를 만들지도
읽지도 않는다.

### 미해결로 남긴 것 (disclosed)

- **빈 배열·부실 verbatim_spans 는 게이트가 잡지 못한다.** `anchor_check` 는 배열에 든 항목만
  순회하므로 `constants: []` 는 무검사 통과다. 부속서가 규범으로 금지하고 맹검 표본이 사후에
  잡을 뿐, 기계 집행은 없다.
- `calls`·`io` 앵커는 게이트 미검사. 검사 범위 확대는 doc 421 에 추가 소급 영향을 낳으므로
  이번 승인 범위에서 제외했다(부속서 B-2 로 명문화).

## 2026-08-11 세션 — doc/FUNWAVE 421 완주. 단 **두 차례 전량 폐기·재생산** 후

- **결론 먼저**: doc/FUNWAVE semantic **421/421 수납, validator 전수 결함 0, 큐 대조 누락·중복·큐밖 0**
  (큐 701 = semantic 421 + 승인 예외 280). shard 11개(000~007·010·013·014) 완주,
  008·009·011·012 는 전량 수치격자 예외라 판독 대상 없음. 전 레코드 pending(맹검 §6 미실시).
- 이 세션에서 **두 번 전량 폐기**했다. 폐기분은 삭제 없이 파일별 sha256 매니페스트와 함께 보존.

### 폐기 1 — model-id 오귀속 203건 (`pending-superseded/20260811-modelid/`)
- 적발: 레코드가 `reader/producer = openai/gpt-5`(163) · `openai/gpt-5.2-codex`(37) 로 기록됐으나,
  codex 세션 rollout 의 `"model"` 실측은 **doc-000~006 전 run 이 `gpt-5.6-sol`**.
  Codex base instruction 의 "an agent based on GPT-5" 를 자기 ID 로 적은 것.
- 증거: `analysis/model-id-provenance-20260811.json` (run_id ↔ 세션파일 ↔ 실측 model).
- 처분(사용자): **전량 재판독**. 08-03/04 생산분 201 + 당일 2 = 203건 격리.
- 교훈: 판독자의 자기신고 model-id 는 신뢰 불가. 런타임 증거(rollout `"model"`)로 대조해야 한다.

### 폐기 2 — 게이트 v3 probe 를 통과한 앵커 결함 79건 (`pending-superseded/20260811-anchorrule/`)
- 적발: 재생산 중 표본 대조에서 66건 중 **17건 결함**. v3 `anchor_check` 는 name 토큰이 없어도
  **수치 부분일치**로 통과시켰다(`1.0000000e-06` 의 `1.0` 이 다른 수치줄에 있으면 PASS).
  - off-by-1 계열 6건: `FroudeCap @L105`(주석줄) vs 실제 대입줄 106 등
  - 창작 라벨 11건: 헤더 없는 수치파일에 `column_1`·`row_count`·`spectral_floor`·`Core`·
    `Length/Width/Alpha1`(vessel_00001 L4 는 `20.0, 10.0, 0.5…` 뿐) 을 만들어 붙임
  - bytes 전사 오류 1건: rec 4449 / 실측 4487 (sha 는 일치 — 필드만 틀림)
- 처분(사용자): **게이트 v4 즉시 조임 + 라벨 창작 금지 + 결함 shard 전체 재생산**.
- **게이트 v4** (`reread_gate_20260728.py`): ① `anchor_check` — constants·params_defined 의 name 은
  서술형 금지·식별자 토큰 필수·**그 토큰이 앵커 줄에 문자 그대로 실재**해야 통과.
  ② `submit` 에 실측 필드 대조 추가(bytes·lines_or_pages·read_range·chunk_manifest_sha256).
  회귀시험: 기존 79건 중 19건이 v4 에서 차단됨을 확인 후 투입.
- **프롬프트 doc-v2** `6cf7a860c6df7ae9be72df257fa94e4c76854401be2c28e9f2cc817100f8ff33`
  (`prompt-doc-codex-v2.md` = v1 전문 + 부속서03): 앵커 규율 강화(주석줄 ≠ 대입줄),
  헤더 없는 수치 데이터 파일은 **라벨 창작 금지 · constants/params 빈 배열 허용 ·
  구조는 what_it_is, 수치는 verbatim_spans 원문 그대로**, 실측 필드 전사 규칙.
- v4 체제 재생산분은 12건·52건·113건·185건·421건 시점 전수 검증에서 **줄곧 결함 0**.

### 운영에서 확인된 것
- **이어받기 프로토콜 실증**: 판독자 3명이 컨텍스트 소진으로 중단(doc-000 31/47·004 9/47·014 19/43),
  전원 미독분을 `complete` 로 위장하지 않고 정직 보고. 같은 run_id 를 새 판독자가 물려받아
  완주 → 세 shard 모두 결함 0·누락 0. 부분 ack 파일은 chunk 0 부터 재서빙(승계 금지) 유지.
- 병렬 8스트림(codex-companion background task) 운영. 게이트 verify 거부는 정상 작동 신호로,
  doc-004 판독자는 첫 청크 계통 off-by-1 81건을 제출 전에 정정했다.
- 오케스트레이터 검증기 신설: `validate_pending_20260811.py` (E1 실측필드·E2 앵커실재·
  E3 스키마/금지필드·E4 model-id). content 를 만들지 않고 검출만 한다.

### ★미처분 — code·note 축에 같은 결함 (다음 세션 최우선)
v4 validator 를 기존 pending 에 돌린 결과:
- **code 249건 중 33건 결함** (000 c095c7c3 1 · 000 378e42d7 13 · 001 11 · 002 3 · 003 1 · 004 4)
- **note 20건 중 17건 결함**
- 유형: 압도적 다수가 `name` 에 **숫자 리터럴**(`'100' @L41`·`'0.055' @L16`) — 불변 프롬프트가
  명시 금지한 "소수 리터럴 name". 소수는 앵커 미실재(`LAYER_012 @L131`·`Coherent_Percentage @L1`).
- 현재 기준(§5.2 무관용)이면 해당 shard 전체 불합격. doc 와 같은 처분 시 **269건 재판독**.
  canonical `records/` 는 무오염(전부 pending) — 사용자 처분 대기.

## 2026-08-04 세션(속) — 사용자 중지 지시, doc 4/15 시점 동결

- 중지 시점까지 추가 완주: doc-001 47/47(§5.1 semantic 40+mech 7, 앵커 3,709/3,709) · doc-002 47/47(41+6, 1,102/1,102) · doc-003 47/47(46+1, 2,792/2,792).
- **FUNWAVE 누적 §5.1 전건 통과**: code 5 shard(243) + note 1 shard(20) + doc 4 shard(000~003, semantic 172) = **semantic 435파일**, 전부 pending(맹검 미실시 — 표본은 전 초안 완료 후 seed 고정).
- doc-004 는 27/47 에서 중단 — 취소로 부분 ack 된 funwave_tvd_3.0.tex(13/15) 를 chunk 0 재서빙 상태로 초기화(부분판독 승계 금지). 재개점: 기존 run `…T001030Z-18cf131d` 이어받기.
- 잔여: doc-004(잔여 20) + doc-005~014(10 shard) → 이후 맹검 표본 고정(§6)·canonical 승격 게이트.

## 2026-08-03~04 세션 — FUNWAVE 재개: code축 5/5·note 완주, doc축 진행, 예외 보완(부속서02)

- 재개(월한도 리셋): code-002 완주 49/49(§5.1 앵커 706/706)·code-003 완주 48/48(591/591)·code-004 완주 48/48(1,274/1,274) — **code축 5 shard 전부 §5.1 통과**(EFDC-000 포함 249파일). note-FUNWAVE-000 완주 20/20(319/319) — 위키 노트 간 상충(v3.0↔v3.6·쇄파 임계 표기·verified/미검증 병존) 다수 열거.
- **doc축 개시(Codex=1차, WO §2.1)**: prompt-doc-codex-v1(85d32dc7…), 게이트 v3.2~3.4(수치격자 자동 skip·CHUNK-HEADER 메타 확장·앵커 probe 보강·보완 예외 로드). doc-000 완주 47/47(§5.1 semantic 45 전건 통과, producer=llm:openai/gpt-5), doc-001·002 진행.
- **부속서02(2026-08-04 사용자 승인)**: 수치벌크 보완 예외 — lines>=10,000 ∧ 비-code ∧ min(head,mid 64KB) 수치비율>=0.70, 8건(FUNWAVE 2·LISFLOOD 6, `numeric-bulk-exceptions-20260804.txt` 939869dd…) mechanical 등록. 경위: doc-001 의 coupling_file_v2.txt(104,019행·521chunks) 단일 컨텍스트 완독 불가 + Codex 의 정직한 제출 거부. semantic 분모 1,883→**1,875**.
- 프로토콜 사건 처리: Codex 출력 절단으로 ack-후-미독 1건 → 파일 상태 초기화 후 재판독(부분판독 승계 금지 선례 적용), 이후 전 배치에 파일 리다이렉트 의무화. Claude 배치 수기 집계 초과 2회 → status 기반 카운트로 교정. 접근 감사 전 배치 청정(Codex 파일럿의 자진신고 rg 1건은 금지 3경로 미접촉 확인).

## 2026-07-28~29 세션(속4) — (a) 대화형 계속: FUNWAVE 000·001 완주, 002·003 중 월한도 도달

- 배치 체제 확립: 게이트 v3.1(CHUNK-HEADER 에 source_bytes·chunk_manifest_sha256 추가), 에이전트당 13~17파일 배치 + 같은 run_id 이어받기, shard 2개 병렬 스트림.
- **code-FUNWAVE-000 완주(49/49) → §5.1 전건 통과** (앵커 513/513, 접근 감사 4에이전트 위반 0, pending).
- **code-FUNWAVE-001 완주(49/49) → §5.1 전건 통과** (앵커 871/871, 접근 감사 4에이전트 위반 0, pending). 중간 API 단절 1회는 같은 에이전트 재개(SendMessage)로 프로토콜 무결 복구.
- **code-FUNWAVE-002: 17/49 수납** (전건 verify PASS), 다음 파일 nesting_tools/coupling_file_multi_blocks.m (acked 0/2).
- **code-FUNWAVE-003: 11/48 수납**, 현재 파일 tide_frf_abc_data/postprocessing/plot_time_series.m 은 **ack 완료(eof)·미제출** — 재개 에이전트는 이 파일을 다시 읽을 수 없으므로(컨텍스트 소실) ★orchestrator 가 state 를 이 파일 시작 전으로 되돌리거나(acked 0 초기화+receipt 마지막 파일분 삭제) 새 run 재생산 판단 필요. 중단 사유: **Claude 월 지출 한도 도달**(claude.ai/settings/usage 에서 상향 필요).
- 판독 품질 관찰: FUNWAVE 벤치마크 스크립트군에서 실행불가 코드(plot_current.py import os 누락)·정수나눗셈 보간 퇴화(convert.f)·플롯≠산출물 rand 이중추첨(mk_2d_1d_spec_frf.m) 등 교차라인 결함 다수 축적.
- 진척: code축 679 중 EFDC 6 + FUNWAVE 126 = **132 제출**(이 중 §5.1 통과 104 + 진행분 28), 잔여 FUNWAVE 63·LISFLOOD-FP 430·note 68.

## 2026-07-28 세션(속3) — 비용 승인, shard 000 v2 기각→v3 §5.1 통과

- 사용자 비용 승인으로 shard code-EFDC-000 재생산 착수.
- **v2 run** (프롬프트 v2, 앵커 자가대조 의무): 6/6 제출·자가대조로 앵커 수십 건 사전 정정했으나 validator 에서 **진짜 앵커 오류 1건**(mod_netcdf BDATE loc 704, 실제 710; 1,172앵커 중 1) → §5.2 무관용으로 shard 재기각(records-rejected).
- **게이트 v3**: submit 에 validator 동일 로직의 앵커 자동검사 내장 + `verify` 커맨드(스크립트 허용 범위 — 앵커 실재 검증만, content 미생성). 프롬프트 v3 `234ba5fc…`.
- **v3 run** (`…T051046Z-c095c7c3`): 6/6 수납, verify 가 제출 전 계통 off-by-1 18건(mod_scaninp) 등 적발·정정. **§5.1 최종검증 전건 통과** — 앵커 1,126/1,126 실재, 해시·행수·receipt(109 chunk)·금지필드·prompt sha 전건 정상, 접근 로그 감사 6 에이전트 위반 0. unresolved 계 86건(교차라인 의미결함 다수, 3회 독립 판독에서 NPFORT elseif 사장·set_nc_flags 사문화·SCANWRSER 라벨 낙하 등 핵심 결함 재현 일치).
- shard 000 은 **pending** — §5.2.3 맹검 표본(전 초안 완료 후 seed 로 일괄 고정) 통과 후에만 canonical 승격.
- 실측 비용: v3 1회전 1.25M 서브에이전트 토큰(6파일·21,164라인). v1~v3 총 3.7M.
- 잔여: code shard 14개(FUNWAVE 5·LISFLOOD-FP 9)·note 3개 = Claude 축 17 shard(약 740파일), doc 991(Codex)·web 145(Grok) 축은 별도.

## 2026-07-28 세션(속2) — 수치격자 예외 승인·집행

- 사용자 승인("수치격자 예외 승인")으로 게이트 3항 mechanical 예외 확장: 결정론 기준(bytes≥100,000 ∧ 선두 65,536B 수치문자비율≥0.95) 355건(전부 doc축: FUNWAVE 278·LISFLOOD-FP 77, 881MB). 승인 목록 `reread-queue/numeric-grid-exceptions-20260728.txt` (sha256 c3e33097…), mechanical 레코드 `records/numgrid-{FUNWAVE,LISFLOOD-FP}-20260728.jsonl` 등록, SPEC 개정 + `workorders/WO-20260728-amendment-01.md`(WO 원본 동결 유지).
- semantic 재판독 분모 2,238 → **1,883** (code 679·doc 991·web 145·note 68), 맹검 표본 224 → **189**. 검산 일치.
- 잔여 대기: code축 재판독 비용 승인(shard 000 실측 1회전 ≈1.2M 서브에이전트 토큰) — 승인 시 프롬프트 v2 로 shard 000 재생산부터.

## 2026-07-28 세션(속) — WO 고정 + 파일럿 shard 000 기각 (게이트 실동 검증)

- **Codex 작업지시 고정**: `workorders/WO-20260728-reread.md` (입력 해시 동결·50 shard 결정론 분할·스키마 v2 레코드·200라인 chunk 순차 수신확인·EMIT_ALLOWED 토큰·validator/게이트·맹검 seed `6465d0b8…`·표본 224·중복 640 canonical 규칙). 검증: 입력 해시 5건 실측 일치, shard 50개 생성 알고리즘 재현 → WO 표와 전건 일치.
- **집행 게이트 구축**: `reread_gate_20260728.py` (init/next/ack/token/submit — receipt 검증 실패 시 차단), 불변 프롬프트 v1 `5e289c83…`.
- **파일럿 shard code-EFDC-000 (6파일·109 chunks·21,164라인) 완주**: 판독자 Claude(fable-5) 에이전트 6명, chunk 수신확인 109/109 전건 통과, 접근 로그 감사 위반 0(전원 게이트 경유만), 금지필드 0, 해시·행수·재결합 전건 일치. **의미 판독 실증**: unresolved 102건 — 교차라인 결함 다수(aaefdc stale-K DZC·input.f90 NPFORT elseif 사장·SEDVDRT 이름전치·mod_netcdf set_nc_flags 사문화·mod_scaninp LVC broadcast 순서 등).
- **validator 에서 shard 기각(§5.2)**: 748앵커 중 진짜 오류 27건(전부 off-by-1~2, mod_var_global 헤더블록 계통 12건) → 무관용 규정으로 shard 전체 `records-rejected/code-EFDC-semantic-reread20260728-000--….jsonl` + reason.json. 검증기 오탐 2계열(주석형 name·1글자 식별자)도 판별해 기록.
- **프롬프트 v2** `872e1269…`: bare-identifier name 강제 + 제출 전 앵커 자가대조 의무.
- 부수: 중복 640행 provenance 분석(`analysis/dup-canonical-proposal-20260728.jsonl`, sha충돌 0)·수치격자 분류(`analysis/numeric-grid-candidates-20260728.json`: ≥0.1MB 중 355개·881MB가 수치격자 — 예외 확장은 게이트 문언 변경이라 **사용자 결정 대기**).
- 실측 비용: 파일당 ~15만-37만 subagent 토큰(파일 크기 비례), shard 000 1회전 ≈ 1.2M 토큰. code축 679파일 전체 재판독 규모 산정 후 진행 여부 사용자 확인 필요.

## 2026-07-28 세션 — 방법 감사 처분 실행 (사용자 승인) ★아래 07-24 "완결" 3건 철회

- [METHOD-AUDIT-20260724.md](METHOD-AUDIT-20260724.md) 진단 확정: 아래 07-24 EFDC·FUNWAVE·LISFLOOD-FP "완결" 3건은 **LLM 판독이 아니라 결정론적 구조 인덱스** — `complete`·`reader: codex` 오귀속. 사용자 승인으로 처분 실행:
  - 3파일 2,248행 `records/` → `records-structural/20260724/` **강등·격리** (사전/사후 sha256 검증, `manifest.json`에 원본·정규화v2·생성기 해시 기록)
  - 필드 정규화 v2: `artifact_class: structural_index`·`producer: script:<이미터>`·`read_method: deterministic_parse`·`comprehension_status: not_performed`·`read_status→scan_status`·`reader` 제거
  - 비어 있지 않은 텍스트 **2,238건 재판독 큐 복귀** (`reread-queue/`, FUNWAVE 0-byte 10건 mechanical 예외)
  - 생성기 4개(final 드라이버 3 + 원본 이미터)에 격리 배너 + `ALLOW_STRUCTURAL_EMIT` 실행 가드 — semantic `records/` 출력 금지
  - SPEC.md 에 **스키마 v2·스크립트 허용/금지·축별 역할(1차/맹검)·파일별 완료 프로토콜·완결 게이트 7조건** 추가
  - status.sh 를 `(model, 정규화 path)` canonical key 집계로 교정 → 현재 **22,269 / 71,143 (31.3%)**, 중복 640행 미해소
- **"완결 10모델" 철회.** 앞선 7모델도 script-산 확정/구조-only 의심 혼입(감사 §3 표: CADMAS 1,361·SFINCS 379·XBeach 121·SWASH 106 script 확정, Celeris 409 의심) — 완결 게이트 재통과 전 "재판독 불필요" 금지.
- 다음: 감사 §3 절차 6~8(중복 canonical 해소 → 맹검 층화표본 → 완결 재계산) + 재판독 큐 2,238 + ADCIRC/ROMS/Delft3D 잔여.

## 2026-07-24 세션 — LISFLOOD-FP 완결(10번째 모델)

- 잔여 1,092 판독 완료 → **LISFLOOD-FP 콘텐츠 커버리지 1,684/1,684 (100%)**. 전역 23,425→**24,517** (34.5%).
- 구성: C/C++/CUDA .h/.cpp/.cu/.cuh/.hpp/.tpp 430(HDF5/netCDF windep 헤더 포함) · 데이터/파라미터 par·asc·bci·wd·bdy·dem·river 등 645 · Python 31 · md 9 · svg 8.
- ★**base 이미터 버그 회피**: base `parse_text` 는 `.h` 를 **Fortran 파서로 라우팅** — LISFLOOD 의 C/C++ 헤더에 오적용. **C/C++/CUDA 전용 파서 추가**(함수·struct·class·enum·union·namespace·typedef·#define·#include 라인앵커 열거)로 오버라이드. 드라이버 `helpers/emit_lisflood_final_20260724_e3a9.py`.
- ★**공백 포함 파일명 처리**: `find | .split()` 가 공백 파일명(`... user manual +bridge.docx`)을 쪼개 유령 경로 42개를 만들어 미판독을 1,134로 부풀림 → **NUL-구분 find**로 정정, 실제 1,092.
- 바이너리 처리: exe/xls/xlsx/docx/pptx/pdf 36건은 이미 mechanical-sweep(해시+MIME) 완료 → 미판독 아님. PDF 유저매뉴얼은 doc-extracted 파이프라인에서 별도 텍스트추출·판독됨(claude complete) — 공백 없음 확인.
- 검증: 스키마·금지필드·앵커결측 **0/1,092**, 표본 15건 독립 재실측 전건 일치, C 파서 앵커 실재 대조(namespace lis·struct GhostRaster·FUNCTION elements) 통과. 미판독 0(.git 도 없음).

## 2026-07-24 세션 — FUNWAVE 완결(9번째 모델)

- 잔여 974 판독 완료 → **FUNWAVE 콘텐츠 커버리지 1,396/1,396 (100%)**. 전역 22,451→**23,425** (32.9%).
- 구성: 일반 텍스트/데이터 txt·out·dat·noext 595 · MATLAB .m 132 · Fortran .f/.f90/.F 94 · Python .py 17 · md 20 · eps(ASCII PostScript) 36 · 기타. 빈 파일 10건 포함(전량 read).
- 방법: EFDC 완결에 쓴 codex 결정론적 이미터를 **MATLAB(`function`/`classdef`)·Python(`def`/`class`) 엔티티 열거로 확장** + UTF-8 실패 시 **latin-1 폴백**(ISO-8859 소스 .m 2·.tex 1 → failed 아닌 complete로 정상 판독, read_range에 인코딩 명기). 드라이버 `helpers/emit_funwave_final_20260724_b7d1.py`.
- 검증: 스키마·금지필드·앵커결측 **0/974**, 표본 15건 **독립 재실측 전건 일치**, 앵커 실재 대조(MATLAB FUNCTION·Fortran SUBROUTINE·latin-1) 통과. 미판독 59건 = `.git/` 플러밍뿐(범위 외).
- ★진짜 바이너리 0 — .mod조차 ASCII 텍스트(컴파일 산물 아님), .eps는 ASCII PostScript. null바이트/디코드 검사로 사전 분류.

## 2026-07-24 세션 — EFDC 완결(8번째 모델)

- 잔여 182 판독 완료 → **EFDC 콘텐츠 커버리지 10,060/10,060 (100%)**. 전역 레코드 22,269→**22,451** (31.6%).
- 구성: confluence JSON 137(EK 지식베이스 135·ETG 2) · f90 소스 6(input.f90 7,679행 포함) · source-analysis md 39.
- 방법: 기채택 **codex 결정론적 이미터** 재사용 — sha256sum/wc 실측 + 라인앵커 충실 파싱(JSON/Fortran/Markdown). 샤드 아닌 잔여-파일 목록으로 구동(기존 레코드 미접촉·중복 레코드파일 0). 드라이버 `helpers/emit_rest_efdc_final_20260724_9c4e.py` → `records/rest-efdc-final-20260724.jsonl`.
- 검증(자기신고 불신 원칙): 스키마·금지필드·앵커결측 **0/182**, 표본 12건 sha256·bytes·행수 **독립 재실측 전건 일치**, 앵커 실재 대조(f90 MODULE/FUNCTION·md H2·JSON title/body) 통과.
- 미판독 58건 = 벤더 체크아웃 내부 `.git/` 플러밍뿐 → 모델 콘텐츠 아님, 범위 외(disclosed).


## 발단

2026-07-19, COAWST full-PDF 승격 작업 중 **"MDPI가 왜 paywall이지?"** 를 확인해 본 게 계기.
→ 논문 인용 전수감사(canonical 50 노트·142 인용) → 결함 20여 건 적발
→ **"AI 가 안 읽고 판정한 것"이 위키 전반의 구조적 문제**임이 드러남
→ 사용자 지시: **"판단하지 말고 모든 코드·매뉴얼·웹정보·크롤링분 전부 읽고 결과를 저장"**

## 왜 필요했나 — 07-19 논문 감사 적발 내역

| 유형 | 사례 |
|---|---|
| 결론 반전 | SWAN ST6 "default 최우수" → 원문은 **열위**(0.52 vs Komen 0.42). 인용 4수치 전부 원문 부재 |
| 인용 오귀속 | "GNN+ridge" 서술에 붙은 PII 가 실제로는 **Zhu 2023 CNN 논문** (진짜 출처 = Kuehn 2024) |
| 교재 미수록 식 | `C_D×10³=0.51+0.080·U` 를 "Pugh + Garratt" 로 귀속 → 교재 grep **"Garratt" 0건**. 실제는 Smith&Banke. 교재의 동일조건 답 1.60 m 존재도 누락(위키는 1.79 m) |
| 실재하지 않는 저자 | LISFLOOD "Shaw, **Sharma**, Bates" → 실제 Shaw·Kesserwani·Neal·Bates·Sharifian |
| 실재하지 않는 도구 | `pyplosa` (PyPI JSON 404, 대조군과 동일) |
| 상태 stale | WW3 Issue #1600 "OPEN" → 실제 2026-06-15 CLOSED |
| 죽은 링크 | openearth.eu/xbeach 404 · adcirc/adcircpy 404 · shorelines.nl 파킹도메인 |
| 시대착오 | XBeach "Katrina/**Sandy** 후" → Roelvink 2009 는 Sandy(2012)보다 3년 앞섬 |

**교훈: 자기 신고가 아니라 외부 사실과의 대조에서만 걸린다.**

## '전수' 재정의 철회

기존 `AUDIT-LEDGER.md` 는 "전수"를 **티어 분류**로 재정의하고("이게 '전수'의 정의이자 증명") 13/13 종결을 보고했음.
- 실측 분모는 원장 기재의 **약 5배**(ADCIRC 는 56→1,130, 20배)
- 판정 오류 실증: SWASH Ch2/5 "비코어"→재판정 코어 / SWAN `swanmain` "S요약 충분"→C 재분류 후 **운영 함정 9건** 발견
- → plan.md 에 TR-0~TR-8 계획 수립, Codex 적대검토 **NO-SHIP** 판정 수령(분모 미확정·판독증거 부재·자기채점) → 전면 재설계

## 확정 분모 (인벤토리 재산출 후)

**71,143 파일** — 확장자 allowlist 가 아니라 전 파일 기준.
★초기 인벤토리 결함: EFDC 에서 **8,884 건 누락** 발견(`manuals/confluence` 8,587 + 소스 236). 이후 전 모델 재스윕.

## 산출물

- `SPEC.md` — 판독 기록 규격(판단 금지·열거 강제·라인앵커 필수·read_status 로 미판독/부재 구분)
- `records/*.jsonl` — 파일당 1레코드
- `PROVENANCE.json` / `PROVENANCE.md` — 모델별 Merkle 루트·repo 메타·버전
- `records-rejected/` — 규격 미달 격리분

## 진척 (2026-07-22 세션 종료 시점)

**레코드 22,269 / 71,143 (30.9%)** — 세션 종료 시점 실측

axis: doc 8,428 · web 6,836 · code 6,745 · note 218
status: complete 11,221 · failed 10,885(대부분 바이너리 기계기록) · partial 121

### 완결 7모델
| 모델 | 파일 |
|---|---:|
| CADMAS-SURF | 1,400 |
| Celeris | 666 |
| SWAN | 609 |
| XBeach | 583 |
| SFINCS | 508 |
| ShorelineS | 496 |
| SWASH | 202 |

### 잔여
| 모델 | 진척 | 잔여 |
|---|---|---:|
| EFDC | 9,878/10,060 | **182** (거의 완료) |
| ADCIRC | 3,048/10,687 | 7,639 |
| ROMS | 2,457/11,661 | 9,204 |
| LISFLOOD-FP | 592/1,684 | 1,092 |
| FUNWAVE | 422/1,396 | 974 |
| Delft3D | 1,154/31,187 | 30,033 |

## 벤더 판정 (실측 기반)

| 벤더 | 판정 | 근거 |
|---|---|---|
| **codex** | ✅ 채택 | SWASH 176/176 전건 대조 — 행수 불일치 0, read_range 조기종료 0, 앵커 2,159건 중 위치오차 10건(0.5%), **날조 0** |
| **claude** | ✅ 채택 | 전건 실측 재검증. 단 초기 프롬프트 미비로 read_range 결측 379/1,251 발생 → 프롬프트 수정 후 해소 |
| **grok** | 웹축만 ✅ | 웹 2,274건 규격 충족(read_range 결측 0·entities 중앙값 55) / **코드축 200건 read_range 전건 결측 → 격리** |
| **agy-gemini** | ❌ 제외 | 1차 sha256 전건 결측 + 허위 complete(index.rst 76행 기록/실측 123행). 2차(경고 후) **sha256 40/40 날조** — bytes·행수는 정확했으나 해시만 창작 |

★교훈: 벤더 단위가 아니라 **축·프롬프트 단위**로 판정해야 함(Grok 은 웹축 프롬프트에선 규격 준수, 코드축에선 미준수).

## 판독이 실제로 잡아낸 것 (판단 없이 unresolved 기록분)

- **SWAN** `mod_xnl4v5`(8,989행, 기존 T티어 면제): BQF 쓰기/읽기 필드 불일치, `xc_hh` g=9.81 하드코딩, `iq_cple` 4·5 문서화-미구현 / `ocpcre.ftn` 헤더 목차의 RDHMS 가 2,612행 어디에도 없음 / `fftpack51`(15,110행) 오류루틴 이름 오전달
- **LISFLOOD** `VersionHistory.h` 가 8.1.0 선언하나 실제 v8.2 (이력이 2020 에서 끊김) — **소스 내 버전 선언 신뢰 불가** 사례
- **EFDC** `netcdf_meta.h` NC_VERSION 4.7.0 vs `libnetcdf.settings` 4.9.2 불일치 / HOUS 변종들이 원본의 가드 누락(`KBT-1<=0`·`MTSCC>0`) / `svdcmp.for` DO ITS=1,30 인데 미수렴 검사는 ITS==60(도달불가) / `valkh.for` NTAB==1001 검사 DO 종료 후 성립불가
- **ShorelineS** `transport_soulsbyvanrijn.m` L72-80 미정의 변수 대입 / `update_bathy.m` L34 미정의 `tnow` / `wave_diffraction.m` L546 죽은 블록 인자수 불일치
- **CADMAS** `mod_comm.f90:242` STOC/CADMAS 디렉토리 분리 봉인(주석 "一旦封印する") / `c_mpi_waitall.f` ISTATUS 단일크기 선언

## 다음 세션 재개 방법

★**[RESUME.md](RESUME.md) 를 먼저 읽을 것** — 재개 절차·벤더 배정·프롬프트 필수문구·운영 주의사항이 정리돼 있음.

```
bash _staging/total-read/status.sh          # 진척 확인
ls _staging/total-read/shards/txt_all_*     # 잔여 샤드
```
샤드는 `(path, sha256)` 키라 **레코드 없는 파일만 재실행**하면 이어짐.
재개 우선순위: 재판독 큐 2,238(EFDC·FUNWAVE·LISFLOOD-FP — 07-24 "완결"은 07-28 철회·구조 인덱스로 강등) → ADCIRC 7,639 → ROMS 9,204 → Delft3D 30,033

## 미해결 (disclosed)

- 로컬 코퍼스가 **upstream 전량인지 미검증** — Merkle 로 "읽은 것"은 고정했으나 "받을 때 빠진 것"은 다루지 못함
- 기존 위키 노트(467건)와 판독 레코드의 **역대조 미실시** — 노트 주장이 원문과 맞는지는 판독 완료 후 별도 단계
- 교차 검증(자기 축 자기 감사 금지) 미실시

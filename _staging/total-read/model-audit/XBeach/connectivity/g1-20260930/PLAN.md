# XBeach R1-G1 — 호출 후보 판정 계획 (2026-09-30)

사용자 지시(2026-09-30): 모델 분석 복귀, XBeach 연결 분석 잔여(R1-G1~G3)부터. 토큰 대량 작업은 Codex `gpt-6-sol`.
범위: [remaining-gaps.json](../runtime-20260912/remaining-gaps.json) R1-G1 — **동결 입력 3,228 후보**(`call-candidates.jsonl`, 호출문 2,242 + 함수/generic 참조 986, 호출자 51파일). 새 입력·부속 도구 내부·솔버 패치 없음 ([CLAUDE.md 범위 통제](../../../../../../CLAUDE.md#모델-분석-범위-통제)).

## 판정 범주 (후보 1건당 정확히 1개)

| 범주 | 조건 | 필수 근거 |
|---|---|---|
| `edge` | 모델 내 특정 정의로 결속 | 대상 procedure_id + 선언 가시성(use/모듈) 근거 file:line |
| `generic_edge` | generic → 특정 specific 결속 | interface 블록 file:line + 실인자 타입·rank 근거 |
| `intrinsic` | Fortran/C 내장 | 이름만 (내부 판독 금지) |
| `external_interface` | MPI·netCDF 등 외부 라이브러리 | 호출 인터페이스까지만 |
| `guard_excluded` | 어떤 빌드 계열에서도 CPP 조건이 참이 될 수 없음 | build-mode-20260912/build-map.json 의 대상별 정의 + 가드 file:line |
| `guard_conditional` | 일부 빌드 계열·실행 조건에서만 도달 | 계열/조건 명시 |
| `not_a_call` | 배열 참조·변수 등 오탐 | 선언 file:line |
| `unresolved` | 위로 결속 불가 | 사유 — 미해결로 남김(지우지 않음) |

재사용: runtime-20260912/interfaces.json·procedures.jsonl, build-mode-20260912/build-map.json, lifecycle/physics 판정, interfaces-20260912(G2/G3 검토 통과분).

## 실행

- 샤드 8개([shards.json](shards.json), 호출자 파일 단위, 약 400건씩). Codex `gpt-6-sol`, `--write` 는 이 디렉터리만. 샤드 순차(병렬 금지).
- 산출: `G1-NN.jsonl` (id, category, target, evidence[file:line + 인용], note).

## 완료 조건

1. **결정적 검사**(스크립트): 3,228 id 전부 정확히 1회, 범주 유효, evidence 의 file:line 실재·인용문 원문 일치, `edge` 대상 procedure_id 가 procedures.jsonl 에 존재.
2. **적대 검증**(Codex `gpt-6-astra`): `unresolved`·`guard_excluded`·`generic_edge` 전건 + 나머지 범주 층화 무작위 10%. REFUTED 비율이 샤드별 5% 초과면 그 샤드 재판정.
3. **Claude 검증**: 적대 검증의 REFUTED·NARROWED 원문 대조, 판정.
4. 결과 요약을 모델 연결 노트에 반영 — `models/` 는 SCOPED EDIT(사용자 sudo) 경유.
5. R1 종료 선언은 G1·G2·G3 모두 위 조건 충족 시에만. R2·R3 전체·R4 는 별도(자동 착수 안 함). 사람 승인 발급 없음.

카운트 정책: 범주별 개수는 인벤토리이며 결함 수·진행률이 아니다.

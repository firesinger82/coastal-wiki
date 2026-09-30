# XBeach R1-G1 — 호출 후보 판정 계획 v2 (2026-09-30)

사용자 지시(2026-09-30): 모델 분석 복귀, XBeach 연결 분석 잔여(R1-G1~G3)부터. 토큰 대량 작업은 Codex `gpt-6.1-sol`.
범위: [remaining-gaps.json](../runtime-20260912/remaining-gaps.json) R1-G1 — **동결 입력 3,228 후보**(`call-candidates.jsonl`, 호출문 2,242 + 함수/generic 참조 986, 호출자 51파일). 새 입력·부속 도구 내부·솔버 패치 없음 ([CLAUDE.md 범위 통제](../../../../../../CLAUDE.md#모델-분석-범위-통제)).
빌드·동적 대상 탐색은 **모델 인터페이스에서 멈춘다** — 외부 라이브러리 구현이나 전체 호출 그래프 재탐색으로 확대하지 않는다.

v1 → v2: Codex 적대 검토([plan-review.txt](plan-review.txt), blocker 3·major 6) 전건 반영.

## 1. 레코드 스키마 — 결속(resolution)과 적용 조건(applicability) 분리

후보 1건 = 레코드 1개. `resolution` 은 하나, 조건별 결속은 `bindings[]` 로 여러 개.

| `resolution` | 필수 근거 (`evidence[]` 의 role) |
|---|---|
| `direct_edge` | `call_site`, `visibility`(USE / 동일 scope / host(CONTAINS) 중 하나), `definition`(실행 정의 — 인터페이스 선언 불인정), `compatibility`(인자 수·타입) |
| `generic_edge` | `call_site`, `visibility`, `generic_interface`, `specific_signature`, `compatibility`(인자 수·keyword·optional·type·**kind**·rank 대응) |
| `indirect_interface` | `call_site`, `pointer_or_binding_decl`(procedure pointer·type-bound), `abstract_interface`, `registration`(등록·association 경로) — 실제 대상을 모르면 명시 |
| `intrinsic` | `call_site`, `shadowing_check`(같은 scope 에 동명 모델 정의·가림 없음) — 이름만으로 분류 금지 (예: `iso_c_utils.f90` 의 모델 함수 `strlen`) |
| `external_interface` | `call_site`, `external_decl`(모듈 USE·interface·bind(C)), `link_evidence`(빌드 설정) — 구현 내부 조사 없음 |
| `not_a_call` | `call_site`, `scope_declaration`(해당 scope 의 배열·변수 선언) |
| `unresolved` | `call_site` + `reason`, `missing_evidence`, `impact`(R1 종료 판단에 미치는 영향) |

**`bindings[]`** (결속 대상이 조건별로 다르면 여러 개): `target`(아래 ID 규칙), `applicability`:
- `build`: 프로젝트/구성별 파일 포함 상태 — [build-map.json](../build-mode-20260912/build-map.json) 의 autotools·projects·per-file 제외. 값 `included|excluded|unknown` + 근거.
- `cpp`: 호출 위치에 걸리는 전처리 조건식 전체와, 명시한 빌드 집합에서의 참/거짓/미정. 목록에 없는 매크로(`SHIFT_TIMER`, 컴파일러 매크로 `__GFORTRAN__` 등)는 **미정**이지 불가능이 아니다.
- `runtime`: 실행 조건식 전체 — 단일행 IF, ELSE 부정, 앞선 조기 종료(`return`/`exit`/`stop`)를 포함. 기존 `contracts.json` 의 여섯 모드가 모든 실행 조건을 증명한다고 간주하지 않는다.
- `status`: `confirmed|excluded|undetermined`. 빌드에서 제외돼 결속을 조사하지 않은 경우도 명시하고 **해결된 호출로 집계하지 않는다**.

**대상 ID 규칙**
- 원본 정의: `procedures.jsonl` 의 `id` (예 `src/xbeachlibrary/interp.F90:8:linear_interp_2d`).
- 생성 대상: `gen:<출력명>@<출력 sha256 앞 12>:<생성 행>:<이름>` + `template_sha256` + 소비자 include 위치 (근거 [generated-links.json](../runtime-20260912/generated-links.json)·G3 [review-response-20260930](../interfaces-20260912/review-response-20260930.json)). **생성물 행을 원본 `.F90` 행처럼 인용하지 않는다** (예: `writelog` 후보 524건 → 생성 `writelog_a` 등).
- 외부/내장: `ext:<심볼>` / `intrinsic:<이름>`.

**evidence 항목**: `{role, path, line_start, line_end, quote, sha256}` — quote 는 해당 행 원문 부분 문자열. 입력 SHA manifest(`inputs.json`)에 없는 파일 인용 금지.

## 2. 실행

- 샤드 8개([shards.json](shards.json), 호출자 파일 소유 유지). 큰 샤드는 **ID 구간 하위 배치**로 나눈다. 반복 패턴(예 `params.F90` 의 `readkey_*`)은 공유 근거 레지스트리(`shared-evidence.json`)로 가시성·generic 근거를 한 번 기록하고 레코드가 참조하되, **호출 위치·인자 대응은 레코드마다 개별 기록**.
- **파일럿 먼저**: 위험 층을 섞은 60건으로 `gpt-6.1-sol` 1회 → 실제 입력·출력 토큰, 스키마 준수, 검사 통과율을 측정하고 배치 크기를 정한다.
- 샤드·배치 순차(병렬 금지). 산출 `G1-NN[-bK].jsonl`. 중단·재개 시 ID 합집합 검사.

## 3. 검증

1. **결정적 검사** (`check_g1.py`): ① 3,228 id 전부 정확히 1회 ② 스키마·범주 유효, resolution 별 필수 role 존재 ③ evidence 의 path·행 실재, quote 원문 일치, sha256 = inputs.json ④ `target` 참조 무결성 — 원본 id 는 procedures.jsonl, `gen:` 는 generated-links 레지스트리 ⑤ `call_site` 행 = 후보의 line_start. **통과는 인용 일치일 뿐 결속 타당성이 아니다.**
2. **적대 검증** (Codex `gpt-6-astra`, seed·표본 ID 고정 파일로 기록):
   - 전건: `unresolved`, `generic_edge`, `indirect_interface`, `not_a_call`, `bindings` 가 2개 이상인 것, `status≠confirmed` 인 것, 생성 대상, `intrinsic`.
   - 층화 무작위: 나머지 `direct_edge`·`external_interface` 의 10% (샤드별, 분모 = 해당 층 레코드 수, 올림).
   - **REFUTED·NARROWED 는 비율과 무관하게 전건 정정·재검증.** 한 층의 표본 REFUTED 비율이 5% 를 넘으면 그 층 전체로 검증을 확대하고, 같은 규칙으로 판정된 후보까지 재검토.
3. **Claude 검증**: REFUTED·NARROWED 원문 대조 후 판정.

## 4. 완료 조건과 한계

- **G1 판정 기록 완료** = 위 1–3 통과 + REFUTED/NARROWED 처리 완료.
- **R1-G1 공백 해소 선언**은 별도: `unresolved`·`undetermined` 목록, 각 영향, **사용자 수용 결정**이 있어야 한다. 기록 완료만으로 해소를 선언하지 않는다.
- 3,228건은 **동결 후보 집합**이지 전체 호출 그래프가 아니다. G2 에서 찾은 동결 밖 호출(`wave_boundary_update.f90:1308 → linear_interp_2d` = source edge·빌드 도달 미확정, `test/testgenmodule.F90:306 → xmpi_getrow` = test-only)은 분모에 몰래 추가하지 않고 교차 참조로 남긴다. 3,228건 완료로 호출 그래프 완전성을 주장하지 않는다.
- G2/G3 는 [review-response-20260930](../interfaces-20260912/review-response-20260930.json) 으로 대응: 58건 중 55 유지, 3 정정.
- R1 종료는 G1(해소 선언 포함)·G2·G3 가 모두 충족될 때만. R2·R3 전체·R4 는 자동 착수 안 함. 사람 승인 발급 없음.
- 결과 요약의 `models/` 반영은 R1 단위로 한 번, SCOPED EDIT(사용자 sudo).

카운트 정책: 범주별 개수는 인벤토리이며 결함 수·진행률이 아니다.

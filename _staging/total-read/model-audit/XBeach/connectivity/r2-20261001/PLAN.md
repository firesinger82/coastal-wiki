# XBeach R2 — 수식 위치별 근거 결속 계획 v2 (2026-10-01)

사용자 지시(2026-10-01): R1 마무리 후 "XBeach R2로 진행". 범위·종료 조건은 09-12 동결 [remaining.json](../remaining-20260912/remaining.json) R2 와 [equation-scope.json](../remaining-20260912/equation-scope.json) 그대로 — **번호 캡션 위치 443곳**(Kingsday 174 · Master 179 · 비정수압 보고서 90). 443곳은 풀어야 할 식 443개도, 결함·미판독 수도 아니다(README §37).
범위 밖: 새 Native(MathType) 해독기, 글꼴·렌더 원인 조사, 전체 재렌더, 저자 의도 추측. 기존 이미지·영수증으로 설명할 수 없으면 `unresolved` 로 끝낸다 — 그것을 범위 확장의 이유로 삼지 않는다.

v1 → v2: Codex 적대 검토([plan-review.txt](plan-review.txt), blocker 2·major 6) 전건 반영.

## 1. 레코드 스키마 — 독립 축

위치 1곳 = 레코드 1개. `id` = equation-scope caption id (같은 번호의 다른 위치는 별개).

| 축 | 값 | 규칙 |
|---|---|---|
| `association` | `objects[]`(0..N, 각 원본 locator·relationship·preview 경로·sha256) + `page`(물리 렌더 페이지 또는 후보 목록) + `status`: `unique`/`ambiguous`/`none` | 문단·표 셀 구조로 연결. **빈 문단에서 이전 객체로 후퇴 금지.** 모호하면 후보로 남김 |
| `body_status` | `readable` · `absent_at_caption` · `present_unreadable` · `association_unresolved` | 빈 렌더 ≠ 원본 부재 (예: master 2.40 본문 렌더 빈칸·preview 판독 가능 / kingsday 2.38 객체 있음·preview 빈칸) |
| `equation_content` | `{images_used[{path,region,sha256}], transcription, uncertain_symbols[], reviewer_note}` 또는 `null`(본체 부재·판독 불가) | 시각 관측은 원문 `quote` 와 분리. 전체 페이지 판독 이력만으로 개별 식 판독을 갈음하지 않음 |
| `document_role` | `model_relation` · `definition_or_assumption` · `derivation_or_validation` · `unknown` | 정의·가정식에는 코드 부재 증명을 요구하지 않음 |
| `implementation_relation` | `mapped` · `mapped_with_differences` · `document_only` · `not_applicable` · `unresolved` | `mapped*` 는 소스 `file:line` 인용 + 항·계수·부호·조건 대응 설명. `document_only` 는 근거 있는 범위 판단(검색 범위 명시) — **검색 실패는 `unresolved`** |
| `evidence_origin[]` | `existing_contract` · `existing_judgment` · `new_comparison` (복수) | 각 재사용 근거에 `claims_resolved`(무엇을 해결) · `gaps_left`(무엇을 남김). 기호 영수증(예 nonhydro 𝕋)은 그 기호 의미만 해결 |
| `document_differences[]` | 다른 판본·표현과의 차이 + 양쪽 locator | 선택적 복수, 구현 대응과 공존 |
| `symbols[]` | 이 식의 기호: 정의 문단 locator·정의 인용·연결 식 | **페이지가 아니라 정의·참조 문단으로 연결**, 페이지 경계 허용 (예: master 33272 식 p.44 / 기호 설명 p.45) |
| `closure_status` | `resolved` · `documented_limit` · `unresolved` | 설명되지 않은 모델 의미·구현 관계가 남으면 반드시 `unresolved` |

## 2. 실행

1. **근거 꾸러미 어댑터(결정적, Codex 구현·Claude 검증)** — 기존 산출물만 사용:
   - DOCX(kingsday·master): 원본 XML ordinal → 소속 문단/표 셀 → 그 단락의 OLE relationship(0..N) → preview 이미지 → 물리 렌더 페이지(render.pdf 텍스트·페이지 이미지 대조).
   - DOC(nonhydro): word stream byte offset → outer-field 166개 순서 → 변환본 command 순서(일치 확인됨) → 변환 문단 → 객체·페이지.
   - 검증 조건: 객체 수 0..N 기록, 반복 번호(master 2.110×3, nonhydro 2.9×2 등)가 서로 다른 객체·페이지로 갈리는지, 모호하면 `ambiguous`.
   - 산출 `packets/<id>.json` + `association-check.json`.
2. **파일럿 30곳** (세 문서·계약 유무·반복 번호·빈 렌더·본체 부재·기호 영수증 사례 포함, seed 고정) — Codex 가 이미지를 실제로 열어 판독했는지(롤아웃 근거)·품질·토큰 측정.
3. **본 판정**: Codex `gpt-6.1-sol` 배치 순차, 매 배치 `check_r2.py`.
4. **적대 검증** (`gpt-6.1-sol` max):
   - **전건**: `association`(locator 연결) · 재사용 근거의 `claims_resolved` 범위 · `body_status≠readable` · 반복 번호 · `implementation_relation∈{mapped_with_differences, document_only, unresolved}` · `document_differences` 있음 · 기호 영수증을 쓴 레코드.
   - **층별 20%**(층 = 문서 × implementation_relation, 올림, seed·표본 ID 파일 고정): 나머지 `mapped`·`not_applicable`.
   - REFUTED·NARROWED 전건 정정·재검증. 한 층 표본 REFUTED > 5% 면 그 층 전건 확대. 같은 규칙 오류는 전체 스윕. 멈춤 규칙은 [R1 PLAN §5](../g1-20260930/PLAN.md#5-공통-전제와-멈춤-규칙-2026-10-01-사용자-승인) 와 같다. 최종 검증 결과는 최종 JSONL sha256 에 결속.

## 3. 결정적 검사 `check_r2.py`

443 id 전부 1회 · 축 값 유효 · `association.objects` 의 locator·sha256 이 원본/어댑터 산출과 일치 · `images_used` 경로·sha256 실재 · evidence path·행/페이지 실재·quote 일치 · 재사용 대상(계약·XH·앵커·영수증) 실재 · `mapped*` 에 소스 인용 존재 · `closure_status=resolved` 인데 `implementation_relation=unresolved` 같은 모순 금지.

## 4. 상태와 한계

세 상태를 따로 기록한다.
- **기록 완료**: 443건 처분 + 위 검사·검증 통과.
- **의미·구현 공백**: `closure_status=unresolved` 목록과 영향. 공백이 남으면 R2 는 동결 조건상 **미완**이다.
- **사용자 결정**: 공백을 수용할지. **수용만으로 동결 완료 조건을 충족했다고 기록하지 않는다.**

시각 판독은 AI 판독이며 수학적 검증이 아니다. `models/` 반영은 Codex 가 diff/script 를 제출하고 Claude 가 검증 → 사용자 sudo 적용(SCOPED EDIT). R3 전체·R4 는 자동 착수 안 함. 사람 승인 발급 없음.

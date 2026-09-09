# Claude Sonnet 문서 적대적 검토 4

## 총평

`_staging/total-read/model-audit/XBeach/closure/document-inventory/canonical/models/XBeach/manual-notes/` 하위 4개 draft(discrepancies-and-version-drift 954행, kingsday-technical-reference 463행, master-manual 583행, nonhydrostatic-report-2010 317행)를 전량 읽고, `exact-207.jsonl`·`all-207-disposition.jsonl`·`document-canonical-mapping.json`·`retrieval-docx-evidence.json`·`manual-code-adjudications.json`·`document-inventory/page-aware/*.md`(OpenDataLoader 재생성본) 대비 기계적/의미적 검증을 수행했다. 결론: **207건 커버리지·인용 무결성·소스코드 판정의 정확성은 기계 검증으로 확인됐고 심각한 조작·날조는 발견되지 않았다.** 다만 **신뢰도 등급의 본문 미표시(B1)**는 실제 blocker이고, 중복점수 낮은 병합(B2)은 경미하지만 명시 보완이 필요하다.

## 확인된 사실 (검증 완료, 문제 없음)

1. **207건 완전 커버리지**: 4개 draft에 XH001–XH207 전부 등장, 교차 파일 중복 0건.
2. **원문 finding 텍스트 무손상**: `exact-207.jsonl`의 207개 finding 문장이 예외 없이 draft 어딘가에 정확한 부분문자열로 존재 — 리포터 주장이 몰래 재서술되거나 대체된 사례 없음.
3. **판정(disposition) 일치**: `all-207-disposition.jsonl`의 `disposition` 필드 207건 전부가 해당 draft 섹션의 `**판정:**` 문구와 키워드 수준에서 일치.
4. **소스코드 인용 정확성**: `manual-code-adjudications.json`의 `wci` 항목 인용(`wave_instationary.F90:131-138`)을 실제 저장소 파일과 대조 — SHA-256, 라인 내용 모두 정확히 일치. 나머지 `nuh`/`bedfriction`/`dilatancy`/`adaptation-time`/`posdwn`/`secorder`/`dthetaS_XB` 판정도 evidence 블록에 실제 소스 quote(line_start/end, SHA)가 동반되어 있어 "overbroad source-code adjudication"으로 볼 근거가 없음(28건 전부 이 형식).
5. **17개 미정렬 DOCX-only 행**: PDF page 주장이 전혀 없음(`grep`으로 확인, 0건 위반). draft 인용문 안의 직접 인용(“…”) 26건 전량이 `retrieval-docx-evidence.json`의 `evidence_blocks[].quote`와 정확히 일치 — "실제 인용을 리포터 주장으로 바꿔치기"한 사례 없음. block index 목록도 evidence의 모든 block을 빠짐없이 인용.
6. **master-manual.md 비파괴적 확장 확인**: 라이브 버전(`models/XBeach/manual-notes/xbeach-master-manual.md`, 292행) 본문 17개 섹션 중 16개가 draft에 완전 동일 문자열로 보존됨. 유일하게 다른 1곳(§9.1 적응시간 식)은 삭제가 아니라 `Ts=max(fTs·h/ws, Tsmin)` 식에 소스 snapshot 판정(oldTsmin 분기)을 캐비어트로 덧붙인 것으로, 파괴적 손실이 아니라 정당한 보강.
7. **고위험 수치 claim 표본 검증**:
   - XH025(vardens 15주파수/13방향 vs 16행×12값): page-aware p.67-68 원문 대조 결과 실제로 표가 변환 과정에서 뒤섞여 있음(여러 행이 한 줄로 뭉쳐짐) → draft가 "변환 손상값 제외" 판정을 내린 것이 타당.
   - XH193(standing-wave L=100m, kH=0.5, 100×100, CFL=0.5): non-hydrostatic p.35 원문과 완전 일치.
   - XH177/XH203(1D `solver=2`(Thomas) vs `ny>2` `solver=1`(SIP)): p.54, p.63 원문과 완전 일치, 후속 매뉴얼과의 드리프트 서술도 정확.
   - XH036(단정밀도 NetCDF 출력, 토큰중첩 12.5%로 최저): kingsday p.9 원문에 "Output is single precision / Default outputformat NetCDF" 확인 — 낮은 토큰중첩에도 불구하고 페이지 배정 자체는 정확했음(다만 이는 B1 문제의 심각도를 줄이는 것이지 없애는 것은 아님).

## 블로커 1 (실질적) — 저신뢰 DOC→PDF page 매핑이 본문에서 구분되지 않음

`all-207-disposition.jsonl`의 `page_map.status`는 4가지: `direct-pdf-representation`(101), `cross-format-mapped`(74, 토큰중첩≥0.70), `cross-format-partial`(15, 중첩 0.125–0.69), `cross-format-retrieval-candidate`(17, no PDF claim). REPORT.md는 "15 DOC(X)/OLE rows have partial cross-format maps and **retain that limitation explicitly**"라고 명시하지만, 실제 4개 draft 파일 전체를 `grep "부분|partial|저신뢰|낮은"`으로 검색하면 **0건**이다. 즉 `cross-format-partial`인 15건도 고신뢰(≥0.70) 74건과 동일하게 "DOC/DOCX→동일 work PDF 정렬"이라는 무차별 문구로 인용된다.

해당 15개 XH ID(토큰중첩률): XH005(0.47), XH008(0.66), XH016(0.45), XH019(0.52), XH022(0.54), XH036(0.125), XH100(0.67), XH112(0.50), XH118(0.26), XH161(0.55), XH165(0.46), XH166(0.67), XH167(0.19), XH170(0.58), XH177(0.69).

frontmatter `citation_status: verified`는 검증됐다는 강한 표시인데, 페이지 지목 신뢰도가 문서마다 12.5%~69%로 편차가 큰 상태가 본문에 노출되지 않는 것은 CONVENTIONS.md §2 취지(AI 요약과 원본 구분, 검증 상태 명시)와 REPORT.md 자체 서술 간의 불일치다. XH036·XH177은 위 표본검증에서 실제로 페이지가 맞았지만, XH167(중첩 19%, N-009/XH167·XH187)처럼 검증하지 않은 나머지 13건은 우연히 틀렸을 가능성을 배제할 수 없다.

**수정안**: 15개 XH ID의 출처 locator 줄에 "(부분 정렬, 토큰중첩 XX%)" 같은 신뢰도 태그를 추가하거나, 최소한 파일 상단 "출처 고정" 절 아래에 "이 문서에는 부분 정렬(cross-format-partial) 행이 포함되며 해당 행은 원본 DOCX를 1차 근거로 본다"는 한 줄 고지를 넣는다. 근본 데이터(JSONL)는 이미 정확하므로 표시만 추가하면 된다.

## 블로커 2 (경미) — 중복점수 낮은 병합의 동치성 오인 소지

71개 다중-XH 섹션 중 29개는 `cross_format_duplicate_score`가 0.5 미만(예: XH001/XH052=0.34, XH041/XH093=0.31~0.43, XH018/XH072=0.43~0.46)이다. 확인 결과 draft는 **원문장을 각각 별도 bullet으로 그대로 보존**하고 병합 후 새 문장을 합성하지 않으므로 정보 손실이나 사실 왜곡은 없다. 다만 XH001(DOCX: ny=0/dtheta/snells만 언급)과 XH052(PDF: 같은 내용 + stationary 모드의 infragravity 생략, 비정수압 sandy morphology 미검증까지 추가)는 같은 절제목·같은 "판정" 문구 아래 놓여 완전 동치처럼 보일 수 있다. 이는 REPORT.md의 "Claim granularity differs across the paired readers" 경고를 draft 본문에서 재확인하기 어렵게 만든다.

**수정안**: 병합 캡션("같은 work의 DOC/DOCX와 PDF 표현을 한 사실 단위로 합쳤다…")에 duplicate_score가 낮은 경우 "완전 동일 문장이 아니라 대상·범위가 다를 수 있다" 취지의 조건부 문구를 추가하거나, disposition.jsonl의 `duplicate_confidence`(high/probable)를 캡션에 노출.

## 부수 관찰 (blocker는 아님)

- `_staging/.../closure/canonical/_archive/XBeach/20260909/xbeach-first-baseline-case-selection.md`는 현재 `models/XBeach/source-analysis/`에 살아있는 파일과 동일 제목이다. 이번 리뷰 범위(manual-notes 4건)에 포함되지 않으므로 깊이 조사하지 않았으나, CLAUDE.md 절대규칙 #8(케이스 선택은 canonical 부적합)과 관련될 수 있어 별도 확인이 필요할 수 있다.
- "add-source-and-version-scoped-manual-fact" 판정의 한글 표기("판본 한정 새 사실로 채택")가 "판본 한정 사실로 채택"(다른 카테고리)과 육안상 거의 구분되지 않는다 — 기계적으로는 다른 disposition이므로 문제는 없으나 가독성 개선 여지.

## 기계적 매핑 vs 의미적 증명 — 정직한 평가

- **기계적으로 강함**: ID 커버리지, 원문 텍스트 보존, 판정-데이터 일치, evidence 인용(DOCX block quote·source code quote) — 전부 프로그램적으로 재현 가능하고 실제로 일치했다.
- **의미적으로는 표본 검증 수준**: 207건 중 직접 원문 대조한 것은 posdwn, vardens 손상표, standing-wave 파라미터, solver=1/2, XH036 단정밀도 NetCDF 등 소수(≈10건)이며, 나머지는 토큰정렬 알고리즘의 산출물(page_map)과 draft의 내부 일관성만 검증했다. 즉 "페이지 번호가 실제로 그 페이지를 가리키는가"는 15건(부분정렬)에 대해서는 4건 미만만 직접 육안 대조했다.
- REPORT.md가 스스로 명시한 한계("Token alignment and canonical anchor hits alone cannot upgrade any row to verified")는 draft 프론트매터의 `citation_status: verified` 일괄 부여와 긴장 관계에 있다 — 이 지적을 B1으로 정리했다.

## 이 리뷰의 한계

- 207건 중 약 15~20건만 원문(page-aware markdown 또는 retrieval-docx-evidence) 대조로 직접 검증했고 나머지는 스키마·구조적 일치성 검사에 의존했다.
- DOCX/DOC의 원본 zip/xml을 직접 파싱하지 않고 `retrieval-docx-evidence.json`이 이미 추출한 block quote를 신뢰했다 — 이 JSON 자체의 생성 스크립트(`build_retrieval_docx_evidence.py`)는 로직 검토를 하지 않았다.
- `document-canonical-mapping.json`(207건 전체, 44만자)은 구조만 훑었고 개별 항목 검증은 생략했다.
- 도구 호출 45회·한국어 1800단어 한도 내에서 우선순위를 신뢰도 표시 누락(가장 확산성 높은 구조적 결함)에 두었다.

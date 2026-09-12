---
title: "COASTAL-WIKI는 무엇을 위해 어디까지 읽어야 하는가 — Grok·Claude·문헌 조사"
origin: codex-user-requested-research
discovered_date: 2026-09-12
source_url: null
source_type: mixed
query: "LLM wiki curation, exhaustive reading, citation support, scientific documentation, maintenance evaluation"
citation_status: draft-unsourced
promote_candidate: undecided
---

2026-09-12 사용자 요청에 따라 Grok으로 X를 수집하고, 논문·공식 구축 문서를 대조한 뒤 Claude의 독립 의견을 받았다. **이 자료만으로 전수 검토가 불필요하다거나 현재 방식이 최선이라고 결론 낼 수는 없다.** 선택한 원문의 충실한 판독, 위키에 게시하는 주장의 검증, 모델 전체의 연결 감사는 각각 목적과 종료 조건을 정할 필요가 있다. 이는 이번 조사에서 도출한 제안이며 정책 채택·XBeach 완료 판정이 아니다.

## 수집 내역과 확인 수준

| 자료 | 확보한 결과 | 확인 한계 |
|---|---|---|
| Grok X 검색 | `grok-4.20-reasoning`, 주제별 3회 + 특정 게시물 재조회 1회. 중복 제거한 게시물 ID 후보 23개 중 21개에 해당 ID의 도구 인용이 있음 | 23개 모두 유효한 연구 사례라는 뜻이 아니다. 직접 브라우저 X 본문 접근은 실패했다. 내용은 Grok이 검색·요약한 것이며 독립 원문 판독으로 표시하지 않음 |
| 논문 | 아래 8편의 공식 서지·초록 확인, 일부 방법·한계 절 추가 확인 | 전편 정독·실험 재현은 아님. 논문별 확인 범위는 근거 묶음에 기록 |
| 구축·문서화 사례 | Karpathy Gist, microsoft/llmwiki, MITgcm, Diátaxis, nashsu/llm_wiki 등 5건 | 구현·운영 방법 설명과 정확성 실증을 구분 |
| Claude | 실제 검토 응답 수신·저장, 로컬 기록과 대조 | 별도 제공자의 AI 의견이며 사람 승인·독립 실험이 아님. 일부 로컬 상태 해석은 정정 |

[기계 판독 목록](../inbox/2026-09-12-wiki-purpose-review/catalog.json), [서지·확인 범위 상세](../inbox/2026-09-12-wiki-purpose-review/evidence-brief.md), [Claude 검토와 대조 판정](../inbox/2026-09-12-wiki-purpose-review/review-adjudication.md)을 함께 보존한다. 검색은 2026-01-01부터 2026-09-12까지의 제한된 공개 X 표본이며 인기도·보편적 합의를 측정하지 않았다.

## GitHub와 X에서 얻은 단서

**원문을 선택하는 일과 선택한 원문을 충실히 읽는 일은 양립한다.** Karpathy는 사람이 자료를 고르고, 원본·생성 위키·작성 규약을 분리하며, 한 자료씩 요약과 변경을 확인하는 방식을 설명한다. 일괄 입력도 선택지로 둔다. 자료에서 위키를 갱신하고, 질문에서 나온 유용한 연결을 다시 축적하며, 정기적으로 모순·누락을 찾는 구조다. 이는 개인 운영 제안이지 정확성이 입증된 표준은 아니다. [원 제안 Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

Grok이 재조회한 [Karpathy의 4월 6일 글](https://x.com/karpathy/status/2041162213160091996)도 원문 읽기·생각하기를 계속한다는 취지다. 따라서 “LLM 위키는 원문을 안 읽는 방식”으로 해석하면 틀린 비교가 된다. [Kothari의 글](https://x.com/thenightshipper/status/2089638769653883208)은 요약 페이지끼리 인용하면서 최초 근거와 멀어지는 문제를, [Mor의 글](https://x.com/mohitmor_ai/status/2043363748174508364)은 유지에 드는 토큰 비용을 비판한다. 후자의 두 글은 문제 제기이며 재현 가능한 정량 실험으로 확인하지 않았다. 세 글의 X 내용은 [Grok 재조회 응답](../inbox/2026-09-12-wiki-purpose-review/grok-verification.json)에 의존한다.

[microsoft/llmwiki](https://github.com/microsoft/llmwiki)와 [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)는 소스 자료에서 위키를 구성하는 구현 사례다. 전자는 선택한 폴더의 재귀 수집도 지원한다. “다른 위키는 전수 처리를 하지 않는다”는 근거로 사용할 수 없으며, 기능 설명 자체가 결과의 정확성을 보장하지도 않는다.

**과학 위키에서는 이론·알고리즘·코드의 연결을 유지할 이유가 있다.** [MITgcm 문서](https://mitgcm.readthedocs.io/en/latest/)와 [알고리즘 문서 소스](https://github.com/MITgcm/MITgcm/blob/master/doc/algorithm/algorithm.rst)는 그 연결을 제공한다. [기여 규칙](https://mitgcm.readthedocs.io/en/latest/contributing/contributing.html)의 코드 변경 회귀 시험과 문서 렌더링 확인은 검사 대상에 따라 검증을 달리하는 사례다. 모든 위키 문서를 쓰기 전에 전체 소스를 감사해야 한다는 요구로 해석하지 않는다.

[Diátaxis](https://diataxis.fr/how-to-use-diataxis/)는 독자의 필요에서 작은 문서 개선을 시작하는 방식을 제시하면서, [reference](https://diataxis.fr/reference/)에서는 정확하고 범위에 충실한 설명을 요구한다. 작은 단위로 구축하는 것과 내용의 엄격함을 낮추는 것은 별개다.

## 논문 8편이 실제로 말해 주는 것

| 논문 | 이번 판단에 도움이 되는 점 | 적용 한계 |
|---|---|---|
| [ALCE, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.398/) | 답의 품질과 인용 지지를 따로 평가. 원문 일부를 베껴 인용 점수만 높이는 퇴행도 점검 | 인용 품질만으로 답의 유용성이나 수치 해법 정합성을 판단할 수 없음 |
| [FActScore, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.741/) | 문장을 원자적 주장으로 나누고 근거 지지 비율을 측정 | 사실적 정밀도이며 빠뜨린 분야 전체의 회수율은 아님. 이번에는 서지·초록 확인 |
| [Lost in the Middle, TACL 2024](https://aclanthology.org/2024.tacl-1.9/) | 입력이 길다는 사실과 필요한 근거를 잘 활용한다는 사실을 구분 | 당시 모델·과제에서의 결과. 현재 모델의 오류율로 이전하지 않음 |
| [GraphRAG, arXiv 2404.16130v2](https://arxiv.org/html/2404.16130v2) | 전체 자료를 가로지르는 질문에는 넓은 구조·요약도 유용하다는 반론 | 뉴스·팟캐스트 중심 평가. 환각 감소나 연안모델 코드 감사 효과를 입증하지 않음 |
| [Good enough practices in scientific computing, 2017](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) | 문서화·재현성 실천을 비용과 효용에 맞춰 단계적으로 도입 | 과학 계산 실무 권고이며 전수·선별 감사의 비교 실험은 아님 |
| [WiCER, arXiv 2605.07068v1](https://arxiv.org/html/2605.07068v1) | 위키 압축에서 빠진 사실을 진단 질문으로 찾아 보강 | 특정 사실 보강이 다른 사실을 밀어내기도 함. 제한된 모델·자료·메모리 조건, preprint |
| [WikiLoop, arXiv 2607.26604v1](https://arxiv.org/html/2607.26604v1) | 편집을 후속 질문의 성능과 관계없는 질문의 퇴보로 평가 | 격리 복사본 편집을 평가 후 폐기. 장기 영구 편집의 오류 누적은 검증하지 않음, preprint |
| [문서 QA 환각 평가, arXiv 2603.08274v1](https://arxiv.org/abs/2603.08274v1) | 문서의 사실을 찾는 능력과 없는 사실을 만들어 내지 않는 능력을 분리 | 이번에는 서지·초록만 확인. X에 나온 오류율을 현재 모델에 적용하지 않음, preprint |

논문들은 평가 방법과 실패 조건의 참고 자료다. 이번에 찾은 자료 중 **연안 수치모델 위키에서 전수 감사와 선별 감사를 직접 비교해 우열을 입증한 연구는 없다.** 이는 이번 검색의 한계이며 그런 연구가 어디에도 없다는 단정은 아니다.

## Claude의 반론과 종합 판단

Claude는 “확정한 자료는 충실하게 읽고, 연결 분석은 핵심 체계에 맞춰 깊이를 정하며, 나머지는 질문으로 보강”하는 조합을 제안했다. 특히 질문 목록만 통과하면 질문에 없는 위험을 놓칠 수 있다는 지적은 반영할 가치가 있다. 다만 “456파일은 이미 모두 읽었다”, “현재 종료 조건이 없다”는 해석은 실제 기록과 맞지 않아 채택하지 않았다. 기존 [R1–R4 목록](../../_staging/total-read/model-audit/XBeach/connectivity/remaining-20260912/remaining.json)은 이미 범위를 고정하고 있다. 검토해야 할 것은 그 고정된 깊이가 위키의 목적에 적합한지다. [검토 원문과 판정](../inbox/2026-09-12-wiki-purpose-review/review-adjudication.md)

저장소의 현재 목적은 **연안공학 개념·이론을 중심으로 모델 구현과 근거를 연결하고, 이후 분석·케이스 구축에 공급하는 객관 지식 기반**이다. 실무 질문에 답하는 기능은 이에 포함될 수 있지만, 개인 실행 요령 모음으로 축소할 이유는 없다. [README](../../README.md), [CLAUDE.md](../../CLAUDE.md)

이 목적 아래 다음을 구분하는 안이 검토 후보가 된다.

| 판단 대상 | 보여 줄 근거 | 이것만으로 말할 수 없는 것 |
|---|---|---|
| 다룰 범위 | 개념·물리·수치해법·모델 기능 지도와 포함/제외 이유 | 파일명만 보고 전체를 이해했다는 주장 |
| 선택한 원문 판독 | 고정 판본·대상과 실제 읽은 근거, 미판독 표시 | 모든 호출·모드 연결 검증 완료 |
| 게시 주장 | 출처 위치와 내용 지지, 수치·조건·판본 차이 | 모델 전체 결함이 없다는 보증 |
| 연결 감사 | 핵심 체계의 진입·조건·상태 전달과 미해결 계약 | 동봉 라이브러리 내부까지 자동 확대 |
| 위키 활용 | 개념·이론·모델 비교 질문, 답 없는 질문, 변경 후 회귀 | 준비한 질문 밖의 공백까지 제거 |
| 완료 판정 | 같은 산출물의 외부 검토와 필요한 실제 사용자 결정 | AI 자기 판정이나 새 표의 생성 |

다음 판단은 이 후보를 기존 목적·범위와 비교해 채택 여부를 정하는 일이다. 작은 평가를 한다면 기존 근거를 재사용하고, 시작 전에 대상·답의 근거·미해결 처리·종료 조건을 고정할 수 있다. 이번 세션에서는 그 실험이나 새 감사 작업을 실행하지 않았다. XBeach 미완 기록·승인 이력은 유지하며, 목적 재검토를 이유로 미완을 완료로 바꾸지 않는다.

## 원자료와 재실행 경로

- Grok: [원 제안 검색](../inbox/2026-09-12-wiki-purpose-review/grok-originals.json), [실패·비판 검색](../inbox/2026-09-12-wiki-purpose-review/grok-failures.json), [평가 검색](../inbox/2026-09-12-wiki-purpose-review/grok-evaluation.json), [특정 글 재조회](../inbox/2026-09-12-wiki-purpose-review/grok-verification.json), [검색 스크립트](../prompts/2026-09-12-wiki-purpose-x-search.py).
- Claude: [전달한 질문](../prompts/2026-09-12-wiki-purpose-claude.txt), [응답 JSON](../inbox/2026-09-12-wiki-purpose-review/claude-review.json), [읽기용 추출](../inbox/2026-09-12-wiki-purpose-review/claude-review.md), [대조 판정](../inbox/2026-09-12-wiki-purpose-review/review-adjudication.md).
- 목록: [서지·한계 상세](../inbox/2026-09-12-wiki-purpose-review/evidence-brief.md), [목록 생성 스크립트](../prompts/2026-09-12-wiki-purpose-catalog.py). Grok 재검색은 외부 호출이지만 목록 재생성은 저장된 응답만 읽는다.

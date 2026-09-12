---
title: "COASTAL-WIKI 구축 목적·전수 범위 재검토 — 외부 검토용 근거 묶음"
origin: codex-user-requested-research
discovered_date: 2026-09-12
source_url: null
source_type: mixed
query: "LLM wiki exhaustive reading; source-grounded knowledge base; citation evaluation; scientific documentation; Grok X search"
citation_status: draft-unsourced
promote_candidate: undecided
---

이 문서는 사용자 요청에 따른 조사·검토 자료다. 정책 채택, 전수 완료, 새 사람 승인 기록이 아니다. XBeach 후속 구현은 중단되어 있고 기존 원본·성과·미완 기록을 유지한다. 여기의 논문 결과는 저자 보고이며 이 저장소에서 재현하지 않았다. 수집 대상으로 고른 논문의 초록·방법·한계를 검토한 범위와, 논문 전체를 판독했다는 주장을 구별한다.

검토 후 결과는 [종합 자료](../../digests/2026-09-12-wiki-purpose-review.md)와 [Claude 의견 대조 판정](review-adjudication.md)에 있다. Grok의 후속 특정 게시물 재조회도 [원응답](grok-verification.json)과 [전체 후보 목록](catalog.json)에 추가했다.

## 판단할 문제

COASTAL-WIKI의 목적에 맞는 분석 범위와 완료 기준을 정한다. 비교할 선택지는 다음 세 가지이며 아직 채택하지 않았다.

- A: 사용자가 확정한 모델 자료 집합 전체의 판독·연결 감사를 기본 선행 과제로 유지.
- B: 질문·게시 주장별로 필요한 원문과 코드 연결을 검증하고, 나머지 심층 감사는 별도 과제로 운영.
- C: 모델의 물리·기능·자료 지도를 먼저 확보하고, 핵심 설명과 알려진 위험은 체계적으로 대조하며, 그 밖의 깊이는 질문과 실제 충돌에 따라 확장.

비교 기준: 오류·미지의 공백 발견 능력, 독자/LLM의 답변 활용성, 근거 추적, 변경 유지 비용, 종료 가능성, 사람이 부담할 판단량.

## 로컬 목적과 사고 이력

- [README](../../../README.md): 개념이 1차 축, 모델은 2차 축. 객관적 지식을 출처와 함께 연결하고 재사용한다. 새 토픽은 두 파일부터 시작한다.
- [CLAUDE](../../../CLAUDE.md): 객관 단언 출처, 원본/AI 분리, 단일 writer, 외부 검토와 사용자 승인 권한을 보존한다.
- [CONVENTIONS](../../../CONVENTIONS.md): 미확정 내용을 숨기지 않는 공개 규칙과 검색 상태 필터가 이미 있다.
- [plan](../../../plan.md)의 2026-07-19 Total Read: AI가 동의 없이 전수 분모를 축소하고 완료를 보고한 사고를 바로잡기 위한 계획. 읽지 않은 driver/이론을 중요하지 않다고 추정한 사례도 기록되어 있다.
- 같은 plan의 2026-09-09 연결 검토와 2026-09-12 범위 통제: 모델 자체는 깊게 보되 MPI/Jumpshot 등 부속 도구 내부로 확장하지 않는다.

따라서 속도만을 이유로 자기 검증을 외부 검토의 대체물로 쓰거나, 미조사 자료를 완료로 바꾸는 개정은 부적절하다. 이번 검토 권한은 정책의 대안을 조사·제안하는 데까지이며 기존 전수 지시를 자동 폐기하는 권한으로 해석하지 않는다.

## 논문 8편

### P1. ALCE — Enabling Large Language Models to Generate Text with Citations

- Tianyu Gao, Howard Yen, Jiatong Yu, Danqi Chen. EMNLP 2023.
- [공식 서지·초록](https://aclanthology.org/2023.emnlp-main.398/) · [PDF](https://aclanthology.org/2023.emnlp-main.398.pdf)
- 확인 범위: 공식 서지·초록, PDF §3.3 인용 품질, §6 사람 평가, Appendix D–E의 지표 악용·평가 제약.
- 관찰: 답의 정확성, 인용된 자료가 주장을 지지하는 정도, 불필요한 인용을 구별해 평가한다. 자동 판정과 사람 판정도 대조한다.
- 적용 추론: 링크나 SHA가 있다는 검사에 더해, 실제 답의 각 주장이 근거로 지지되는지 확인할 필요가 있다.
- 한계: 일반 QA의 문장 평가다. 수치 스킴, 단위, 모드별 실행 조건의 공학적 타당성을 자동 보증하지 않는다. 인용된 원문 자체가 사실인지와 그 원문에 충실한지는 별도다.

### P2. FActScore — Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation

- Sewon Min 외. EMNLP 2023.
- [공식 서지·초록](https://aclanthology.org/2023.emnlp-main.741/) · [PDF](https://aclanthology.org/2023.emnlp-main.741.pdf)
- 확인 범위: 공식 서지와 초록. 전체 실험·부록 판독은 하지 않았다.
- 관찰: 긴 답을 작은 사실 주장으로 나누고 신뢰할 자료가 지지하는 비율을 평가한다. 인물 전기 생성과 자동 평가를 연구한다.
- 적용 추론: 문서 하나의 전체 PASS보다 오류가 있는 주장과 그 근거를 지정하는 검토가 유용하다.
- 한계: 사실 정밀도는 필요한 정보의 누락률이나 모델 전체 범위의 완전성을 측정하지 않는다. 적게 말해 높은 점수를 얻는 문제를 별도 고려해야 한다.

### P3. Lost in the Middle — How Language Models Use Long Contexts

- Nelson F. Liu 외. TACL 2024.
- [공식 서지·초록](https://aclanthology.org/2024.tacl-1.9/) · [PDF](https://aclanthology.org/2024.tacl-1.9.pdf)
- 확인 범위: 공식 서지·초록 및 PDF 서론의 실험 개요. 이번 조사의 모델별 수치를 현재 모델 성능으로 인용하지 않는다.
- 관찰: 주어진 문맥의 관련 정보 위치에 따라 QA·키 검색 성능이 달라지는 현상을 연구한다.
- 적용 추론: 많은 텍스트를 문맥에 넣거나 읽은 기록을 남기는 것만으로, 나중에 정확히 연결해 답할 능력을 확인할 수 없다.
- 한계: 당시 모델과 실험 조건의 결과이며, 현재 모델의 오류율 또는 모든 전수 판독 방식의 무효를 입증하지 않는다.

### P4. From Local to Global — A GraphRAG Approach to Query-Focused Summarization

- Darren Edge 외. arXiv:2404.16130v2, 2025-02-19 수정본. 이 조사에서는 arXiv 판본을 사용한다.
- [서지·초록](https://arxiv.org/abs/2404.16130v2) · [본문](https://arxiv.org/html/2404.16130v2)
- 확인 범위: 초록, 방법 개요, §6.1–6.2 평가 한계·후속 과제.
- 관찰: 자료 집합 전체의 주제를 묻는 질문에 대응하기 위해 개체 관계와 군집 요약을 미리 구성한다. 약 백만 토큰 규모의 두 자료 집합에서 종합성과 다양성을 평가한다.
- 적용 추론: 국소 검색과 몇 개의 쉬운 질문만으로 모델 전체 설명을 대표할 수 없다. 물리·기능 지도를 만드는 넓은 탐색에는 이유가 있다.
- 한계: 저자도 영역 일반화와 fabrication rate 대조의 필요성을 적는다. 이 결과가 모든 소스 행의 정밀 감사나 GraphRAG 도입을 요구하지는 않는다.

### P5. Good enough practices in scientific computing

- Greg Wilson 외. PLOS Computational Biology 13(6), 2017. DOI 10.1371/journal.pcbi.1005510.
- [출판사 본문](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) · [저자들의 공개 원고 저장소](https://github.com/swcarpentry/good-enough-practices-in-scientific-computing)
- 확인 범위: 본문 문서화·재사용 자료 형식, “What we left out”의 적용 비용과 단계적 도입 논의.
- 관찰: 바로 적용할 수 있는 데이터·코드·문서 관리 방법을 제안하고, 좋은 방법이어도 기반이나 투자 비용을 고려해 일부를 제외한다.
- 적용 추론: 한 사람이 유지할 수 있는 작업량과 독자가 실제로 쓸 문서를 기준에 포함한다.
- 한계: 초심자의 과학 계산 관행에 대한 지침이지, 연안 수치모델 감사 범위를 실험 비교한 논문이 아니다.

### P6. WiCER — Wiki-memory Compile, Evaluate, Refine

- Juan M. Huerta. arXiv:2605.07068v1, 2026-05-08. 출판 심사 상태는 별도 확인하지 않은 preprint.
- [서지·초록](https://arxiv.org/abs/2605.07068v1) · [본문](https://arxiv.org/html/2605.07068v1)
- 확인 범위: 초록, §3 실험 구성, §6–7의 요약 정보 손실·진단 보강, §7.4 한계, Appendix J 사람 평가.
- 관찰: 원문을 위키로 압축할 때 답에 필요한 사실을 떨어뜨리는 문제가 발생했고, 진단 질문으로 누락 사실을 찾아 재반영하는 방법을 제안한다.
- 반대 근거도 보존: 특정 사실을 복구하면서 다른 사실을 잃을 수 있고, 개선이 없는 주제도 있다. 선택된 최선 반복 결과와 전체 범위 성능을 혼동하면 안 된다.
- 적용 추론: 질문 기반 보강을 검토할 근거는 되지만, 회귀 질문·미사용 질문 및 원본으로의 경로가 필요하다.
- 한계: KV-cache/full-context 제공 방식과 제한된 코퍼스·모델의 실험이다. 우리 FTS5/MCP 위키의 우월성 또는 자동 검토의 충분성을 입증하지 않는다.

### P7. WikiLoop — Jointly Learning to Build and Navigate Agent-Native Wikis with Downstream Feedback

- Haoliang Ming, Feifei Li, Wenhui Que. arXiv:2607.26604v1, 2026-07-29. 출판 심사 상태는 별도 확인하지 않은 preprint.
- [서지·초록](https://arxiv.org/abs/2607.26604v1) · [본문](https://arxiv.org/html/2607.26604v1)
- 확인 범위: 초록, §4.5–4.6 비교·전이, §5 한계.
- 관찰: 위키 편집을 이후 질문의 증거 탐색·답 성능으로 평가하고, 관계없는 질문의 퇴보도 비용에 포함한다. 같은 기반 모델 비교와 다른 모델의 참고 결과를 구분한다.
- 적용 추론: 문서 수보다 검색·답변 품질과 변경 후 퇴보를 점검하는 실험 설계가 유용하다.
- 한계: 학습된 정책의 실험이다. §5에서 편집을 격리 복사본에서 평가·폐기하므로, 누적된 영구 편집의 오류 전파까지 최적화한 것은 아니라고 밝힌다. 장기 무인 위키 운영 검증으로 일반화할 수 없다.

### P8. How Much Do LLMs Hallucinate in Document Q&A Scenarios?

- JV Roig. arXiv:2603.08274v1, 2026-03-09. 출판 심사 상태는 별도 확인하지 않은 preprint.
- [서지·초록](https://arxiv.org/abs/2603.08274v1) · [PDF](https://arxiv.org/pdf/2603.08274v1)
- 발견 경로: Grok 실패 사례 검색의 Rohan Paul X 게시물. arXiv 원문 서지·초록으로 제목과 연구 주장을 재확인했다.
- 확인 범위: 공식 서지·초록. 세부 실험·코드 재현은 하지 않았다.
- 관찰: 문서 안의 사실을 찾는 능력과 문서에 없는 사실을 지어내지 않는 능력을 구분한 평가를 제안한다.
- 적용 추론: 답이 없는 질문과 근거 부족 상태를 포함해야 한다.
- 한계: X 요약의 광범위한 오류율을 그대로 인용하지 않는다. 저자의 평가 조건과 현재 모델·연안공학 분야의 실제 오류율은 별개다.

## 구축 사례

- [Karpathy 원문 Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): curated raw/wiki/schema, ingest/query/lint. 저자는 자료를 한 건씩 넣고 요약·변경을 확인하는 운영을 선호한다고 쓴다. 선택한 한 원문의 충실한 판독과 모든 가능한 자료의 수집은 다른 범위다.
- [microsoft/llmwiki README](https://github.com/microsoft/llmwiki): 원본·위키·규약 분리, 자료 선택/일괄 수집, 검색·lint. 지원 파일을 재귀 수집하는 기능도 있으므로 “전수 처리 기능이 없다”고 말하지 않는다. 도구 기능 설명이며 정확성의 독립 실험은 아니다.
- [MITgcm manual](https://mitgcm.readthedocs.io/en/latest/) / [algorithm source](https://github.com/MITgcm/MITgcm/blob/master/doc/algorithm/algorithm.rst) / [기여·시험 규칙](https://mitgcm.readthedocs.io/en/latest/contributing/contributing.html): 수식·알고리즘과 코드 연결을 제공하며, 코드 변경에는 전 실험 회귀 검사, 문서에는 문서 작성·렌더링 확인을 요구한다. 과학적 깊이를 유지하는 반대 근거로 읽는다.
- [Diátaxis workflow](https://diataxis.fr/how-to-use-diataxis/) / [reference](https://diataxis.fr/reference/): 문서 종류와 독자의 필요에 맞춰 작은 개선을 진행한다. reference의 정확성과 범위 내 충실함은 여전히 중요하다.
- [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki): Grok X 검색에서 발견했고 실제 저장소 README를 확인했다. 소스 기반 위키 생성 도구의 구현 사례이며 정확성 성능은 검증하지 않았다.

## Grok X 수집과 해석 주의

원 요청은 [검색 스크립트](../../prompts/2026-09-12-wiki-purpose-x-search.py), 실제 응답은 같은 폴더의 grok-originals.json / grok-failures.json / grok-evaluation.json에 보존한다. xAI의 x_search 도구와 실제 응답의 model 값을 기록한다. 게시물 원문과 Grok의 요약·추론을 동일시하지 않는다.

현재 확인된 유형: Karpathy의 원 제안·후속 Gist, 개인 구축자의 주장별 정리 사례, 출처 계보 손실 비판, 사람의 자료별 검토 필요성, 유지 비용 경험, 문서 QA 평가 논문 소개. 직접 브라우저로 X 본문을 여는 시도는 실패했고 X 내용은 Grok 수집에 의존한다. 링크된 논문·저장소는 가능한 경우 별도로 열었다.

Grok 응답의 “반례”, “검색 결과는 대체로 …”, “그런 사례가 없다”는 표현은 그대로 결론으로 채택하지 않는다. 이 검색은 제한된 질의의 탐색 표본이다. 특히 “모든 가능한 자료”와 “확정된 모델 자료 집합”을 바꾸어 비교하면 전수 검토 쟁점을 잘못 반박하게 된다.

## 현재 잠정 판단과 검토 요청

현재까지 수집한 자료는 A/B/C 중 하나의 우월성을 COASTAL-WIKI에서 입증하지 않는다. C를 작은 실제 작업에서 시험할 이유는 있으며, B만 채택하면 질문 선정에서 모르는 위험을 누락할 수 있다.

검토 요청:

1. 우리 목적을 “실무 사용”으로 과도하게 축소하거나 “모델 모든 결함 탐지”로 과도하게 확대한 부분이 있는가?
2. A/B/C 각각의 가장 강한 논거와 실패 조건은 무엇인가?
3. 지식 지도·논문/코드 원문 대조·질문 평가·외부 검토를 최소 어떤 조합으로 유지해야 하는가?
4. 전수 여부, 주장 정확성, 출처 완전성, 질문 회수율, 미지의 공백을 서로 혼동하지 않는 완료 기준은 무엇인가?
5. 기존 미완을 완료로 바꾸지 않으면서 다음 한 묶음의 범위·중단 조건·검토 대상을 어떻게 정할 것인가?

정책 파일을 수정하거나 canonical 승격을 수행하는 검토가 아니다.

---
title: "Claude 독립 검토의 반영·유보 판정"
origin: codex-user-requested-research
discovered_date: 2026-09-12
source_url: null
source_type: mixed
query: "COASTAL-WIKI purpose and exhaustive review: independent critique"
citation_status: draft-unsourced
promote_candidate: undecided
---

사용자가 요청한 Claude 검토를 받았으며, 아래는 그 답변을 로컬 근거와 대조한 Codex의 평가다. 정책 채택이나 XBeach 완료 판정이 아니다. [Claude 응답 원본](claude-review.json)과 [읽기용 추출본](claude-review.md)은 수정 없이 보존한다.

## 실제 검토 범위

Claude CLI가 성공 종료했고 `is_error=false`, `permission_denials=[]`다. 응답의 `modelUsage`에는 주 검토 `claude-fable-5-1`, 보조 `claude-haiku-4-5-20251001`이 기록되어 있다. 별도 제공자의 AI 의견이며, 사람 승인이나 실험 재현은 아니다.

검토자는 근거 묶음, README·CLAUDE·CONVENTIONS·plan, 최초 Grok 응답 3건을 대조했다고 보고했다. ALCE·FActScore·WiCER·WikiLoop·Roig와 Karpathy Gist의 공식 페이지를 확인했다고 하며, Wilson·MITgcm은 직접 열지 않았다고 명시했다. Grok의 후속 3개 게시물 재조회 결과는 이 검토에 포함됐다고 주장하지 않는다. 원본에 있는 “claude-review.json이 비어 있다”는 문장은 자기 응답 파일이 작성되기 전의 관찰이며, 현재 완료 상태와 다르다.

## 반영할 지적

- **원문 판독과 연결·계약 감사를 분리한다.** 파일을 읽었다는 증거와 모든 실행 조건을 연결했다는 증거는 다르다. 기존 판독 성과를 재사용하되 어느 쪽의 완료도 다른 쪽에서 추정하지 않는다.
- **질문 평가만으로 알려지지 않은 공백을 찾았다고 할 수 없다.** 근거가 있는 답, 답이 없는 질문에 대한 유보, 변경 후 회귀, 핵심 분야 누락을 별도로 살펴볼 이유가 있다. [FActScore](https://aclanthology.org/2023.emnlp-main.741/)는 사실적 정밀도 지표이며 분야 전체의 누락률 지표가 아니다.
- **출처 위치와 주장 지지를 구분한다.** 특히 수치·식·실행 조건은 인용한 구절이 해당 단언을 실제로 뒷받침하는지 확인해야 한다. [ALCE](https://aclanthology.org/2023.emnlp-main.398/)가 인용 품질을 별도로 평가한다는 점은 참고할 수 있다. 이 논문을 수치 스킴 검증법으로 일반화하지 않는다.
- **Grok 검색을 전수 불필요의 증거로 쓰지 않는다.** 검색 표본과 홍보·개인 경험은 제한적이다. 선택한 원문 집합을 충실하게 처리하는 방식은 “모든 가능한 자료를 수집하지 않는다”는 사실과 양립한다.
- **진척은 산출물 상태로 설명한다.** 판독·문서와 코드 대조·충돌 처분·외부 검토 상태를 구분하는 표는 검토할 가치가 있다. 단, 새 표를 만들었다는 사실을 모델 진척으로 세지 않는다.

## 그대로 채택하지 않는 해석

| Claude 해석 | 근거 대조 및 판정 |
|---|---|
| XBeach 456파일 판독은 이미 완료 | **완료 단정은 보류.** [RESUME](../../../_staging/total-read/model-audit/XBeach/connectivity/RESUME.md)의 456+87=543은 경로·SHA 집합 확인 기록이다. [reconciliation](../../../_staging/total-read/model-audit/XBeach/connectivity/resume-reconciliation.json)은 전체 판독 gate를 `NOT_PASSED`로 남긴다. [잔여 고정 기록](../../../plan.md#2026-09-12-xbeach-실제-잔여종료-조건-고정)에 있는 빌드 포함 Fortran 57개 이중 판독 근거는 재사용할 수 있지만, 이를 456개 전량 완료로 늘려 말하지 않는다. |
| 연결 과제는 무한하며 종료가 정의되지 않음 | **현재 기록과 불일치.** [remaining.json](../../../_staging/total-read/model-audit/XBeach/connectivity/remaining-20260912/remaining.json)은 이미 `scope_frozen=true`, R1–R4 입력·`done_when`·`not_required`·`change_control`을 갖는다. 이 고정 목록의 크기·깊이가 목적에 적합한지, 잔여 노력과 의미적 공백을 충분히 보여 주는지는 재검토할 수 있다. “고정 기준 자체가 없다”는 진단은 채택하지 않는다. |
| 질문 중심 방식은 위키를 케이스 공급원으로 두는 목적과 충돌 | **일반화가 과함.** [README](../../../README.md)와 [CLAUDE 규칙 8](../../../CLAUDE.md)의 개념·이론·모델 비교 질문은 개인 실행 케이스 없이도 생긴다. 알려진 질문만 최적화하면 공백을 놓친다는 지적은 반영하되 질문 자체가 목적을 뒤집는다고 단정하지 않는다. |
| 현재 verified는 인용 존재만 뜻하며 과거 오류가 그 검사를 통과 | **구체적 이력의 입증 부족.** [CONVENTIONS §2](../../../CONVENTIONS.md)에는 인용·검증 조건이 있고 [CLAUDE 작업 규범](../../../CLAUDE.md)에는 별도 외부·사람 게이트가 있다. 주장 지지 확인을 더 명시하자는 제안과 “기존 모든 검증이 링크 유무뿐”이라는 주장은 구분한다. 특정 오류가 어떤 gate를 통과했는지의 인과관계는 이번 자료만으로 확정하지 않는다. |
| 결함 목록을 모르는 Codex로 블라인드 질문 실험 가능 | **현재 세션은 그 조건을 만족하지 않는다.** 이미 결함 목록과 이력을 읽었다. 별도 비노출 평가자·고정 평가 집합·독립 근거가 필요한 제안이며 실행하지 않았다. 알려진 결함의 재발견 비율을 미지 결함 전체의 발견률로 표현해서도 안 된다. |
| 판독은 A, 깊이는 C, 나머지는 B가 최선 | **검토자의 정책 제안으로 보존.** A는 확정 집합 전수 선행, B는 질문·주장 중심, C는 핵심 체계 지도와 선택적 심화다. 이번 문헌은 이 조합의 COASTAL-WIKI 내 우월성을 실증하지 않는다. 사용자 채택 전에는 기존 승인 조건을 바꾸지 않는다. |

## 이번 검토로 남은 판단

위키의 목적, 다룰 개념·모델의 범위, 원문 판독의 충실도, 연결 감사의 깊이, 게시 주장의 정확성, 검색·답변의 유용성을 한 숫자로 합치지 않는 편이 타당하다는 것이 현재의 종합 의견이다. 어느 범위를 고정할지는 정책 결정이며, 이번 작업은 결정을 위한 근거 수집까지다. [종합 자료](../../digests/2026-09-12-wiki-purpose-review.md)에 비교와 다음 판단 항목을 모았다.

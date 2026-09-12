# XBeach 고정 잔여 목록 — 2026-09-12

기준 커밋은 `cd8c769`이다. 이번 기록은 **기존 분석과 겹치는 일을 걷어내고 종료 대상을 고정한 작업표**다. 모델 전체 완료 판정이나 새로운 사람 승인 영수증이 아니다. 이후 재개는 이 목록의 R1~R4를 따른다. 상위 RESUME/GOAL의 과거 “나머지 전부” 문구에서 새 작업을 만들지 않는다.

## 지금 상태

“경계조건·표사 공식·선택 기능 분석이 통째로 남았다”는 이전 보고는 부정확하다. 이 분야의 기존 노트와 소스 판독 기록이 있다. 실제 잔여는 **그 결과의 전체 연결 대조, 수식별 근거 대응, 이미 드러난 문서 충돌 정정, 최종 검토**다. 아직 전부 끝나지는 않았으며, 네 행은 작업 묶음이지 작은 수정 네 건이라는 뜻이 아니다.

[source-reuse.json](source-reuse.json)은 현재 src 파일마다 기존 판독 영수증·연결 원장·노트의 파일명 언급을 연결한다. 빌드에 포함되는 Fortran 57개는 모두 기존 이중 판독 기록과 현재 원본 SHA가 일치한다. 파일명 언급은 근거를 찾는 위치일 뿐, 그 노트가 모든 호출 조건을 검증했다는 뜻은 아니다. 판독과 연결 대조를 구별한다.

## 다시 작업하지 않을 결과

| 기존 산출물 | 재사용 범위 | 근거 |
|---|---|---|
| 2026-09-09 감사·위키 반영 | 승인 소스 보충 103건, 이월 13건, 문서 XH001~207 판정·위키 연결 | [기존 완료 원장](../../closure/README.md) |
| 모델 소스 판독 | 현재 빌드 포함 소스의 판독 기록. 새 버전 전체 독해를 시작하지 않음 | [src별 재사용 위치](source-reuse.json) |
| lifecycle | SC-001~012 재판정, 네 진입점 계열, 오류 종료·hotstart·BMI 상태 계약 | [재판정](../lifecycle/resolution-20260912/adjudication.json), [검토](../lifecycle/resolution-20260912/review-response.json) |
| physics | U01~U04의 소스 판정과 해당 최소 재현. 소스 결함 패치는 별개 | [재판정](../physics/resolution-20260912/adjudication.json), [검토](../physics/resolution-20260912/review-response.json) |
| 빌드·생성·상위 모드 | src 역할, Autotools/Windows 대상, include 생성, 여섯 dispatcher 경로 | [연결 결과](../build-mode-20260912/README.md) |
| 문서 전체 페이지 판독 | 두 매뉴얼 DOCX·PDF 및 비정수압 보고서 DOC·PDF의 기존 페이지 판독. 다시 렌더하거나 처음부터 읽지 않음 | [DOCX 전체 시각 판독](../manuals-docx-read/full-visual-read/receipt.json), [매뉴얼 PDF](../manuals-visual-read/read-receipts.json), [보고서](../nonhydro-read/read-receipt.json), [보고서 최종 본문](../nonhydro-read/body-field-recovery/receipt.json) |
| 그 밖의 기존 manuals 입력 | 원래 87경로 preflight의 수치 입력 7개는 전 토큰·공간장 판독으로 보충했고 병렬화 보고서는 14페이지 시각 판독으로 보충. 기존 입력 사례를 새 수치 실험으로 확대하지 않음 | [원래 목록](../manuals-preflight/REPORT.md), [수치 입력 보충](../manuals-preflight/numeric-read/REPORT.md), [병렬화 보고서](../lifecycle/parallel-report-read.json), [전체 파일 후속 대응](../resume-reconciliation.json). 폰트 리소스 내부는 모델 잔여가 아님 |
| 확인한 수식 쟁점 | 매뉴얼 (2.5)~(2.10), B.37/C.37 구현 대응, 침투식 +1/시간 이산화, 보고서 𝕋·≪·∼ 네 위치 | [수식 계약](../build-mode-20260912/contracts.json), [침투식](../INFILTRATION-DOCUMENT-CODE-COMPARISON.md), [𝕋](../nonhydro-read/stress-tensor-symbol/receipt.json), [≪·∼](../nonhydro-read/solitary-wave-symbols/receipt.json) |

이 표의 “재사용”은 각 근거에 적힌 범위만 의미한다. 과거 whole_model_read_gate=NOT_PASSED를 PASS로 바꾸거나, 원본 결함을 수정했다고 판정하지 않는다.

## 고정된 잔여와 종료 조건

| ID | 실제 남은 산출물 | 이미 있는 것 | 종료 조건 |
|---|---|---|---|
| **R1 실행 연결 대조** | 현재 모델 소스의 호출·정의·조건을 하나의 전체 대응표로 결속. 경계/표사/선택 기능의 내부 분기를 기존 상위 흐름에 이어 붙임 | src 역할, 빌드 대상, lifecycle 53 edge·physics 14 상태 전달, 여섯 상위 dispatcher, 경계/표사/식생/선박/지하수 노트 | 고정된 빌드 포함 소스·wrapper의 모델 루틴이 진입점/빌드/모드와 연결되거나 비활성·도움 루틴·생성 interface로 근거 있게 분류됨. 모델 호출 양단과 실행/CPP 조건, 핵심 상태 소비 시점의 설명 없는 공백이 없어야 함. 명시된 문서/소스 제약은 별도 처분으로 남김. |
| **R2 수식 근거 대조** | 세 기술 문서의 수식 위치를 기존 의미 판독·코드 근거에 연결하고, 연결되지 않는 부분만 원문 대조 | 전체 페이지/Native 구조 판독, XH001~207 문서 판정, 위의 개별 수식 계약 | 고정 수식 위치마다 기존 판정 재사용 / 코드 대응 확인 / 판본 차이 / 원본 본체 부재 / 구현 범위 밖의 문서 정식 등 명시적 처분과 근거가 있음. 문서 의미·구현 관계를 설명하지 못한 항목은 미완 유지. 인접한 inline 기호도 해당 식·문단과 연결. 모르는 기호를 임의로 복원하지 않음. |
| **R3 위키 정정·반영** | 아래 C1~C4 및 R1/R2에서 같은 입력 범위 안에 확인된 충돌의 정정. 새 분석이 필요한 곳은 R1/R2에 연결 | 새 계약 검토본 네 편과 기존 노트 49편, source-audit 보충·문서 판본별 노트 | 현재 모델 경로를 설명하는 노트가 고정 소스·최종 판정과 충돌하지 않고, 새 대조 결과에 위키 앵커가 있음. 변경 대상 manifest·출처·링크·설치 바이트 검사를 통과. 기존 승인 292개는 불변. |
| **R4 최종 검토·승인** | R1~R3의 최종 결과·차이·남긴 제약을 모은 단일 검토 패킷 | 기존 네 신규 draft와 각각의 검토 기록. 과거 승인은 보존 | 최종 외부 검토 지적을 처리하고 필수 검사·커밋·푸시 완료. 사용자에게 필요한 새 주장 승인만 구체적인 최종 결과로 제출. 사용자 승인 전에는 검토본/미승인 상태를 유지하며 AI가 HG를 발급하지 않음. |

R1의 범위는 [source-reuse.json](source-reuse.json)의 현재 src 129개 역할 집합 중 빌드 포함 Fortran 57개와 Python wrapper 2개다. 이미 판정한 빌드·27개 생성 include 경로는 재사용하고, 비연결 모델 소스 11개는 현재 실행 경로에 넣지 않는다. 템플릿 생성 interface는 소비자와 결속한다. 외부 MPI/netCDF 등의 내부는 진입하지 않는다. R1은 모든 입력 조합의 실제 수치 실험이나 모든 내부 분기의 새 수학적 증명을 요구하는 항목이 아니다.

R2의 정확한 위치 집합은 [equation-scope.json](equation-scope.json)에 있다. 저장된 번호 위치는 Kingsday 174, Master 179, 비정수압 보고서 90곳이다. **443곳은 새로 풀어야 할 식 443개가 아니다.** 같은 번호의 반복도 있으며 inline 기호를 포함한 Native 객체 874개와도 다른 집합이다. 번호/객체 수를 잔여 오류나 완료율로 쓰지 않는다. 기존 새 계약에 직접 연결한 매뉴얼 번호 위치는 14곳이고, 다른 위치는 기존 문서/소스 근거를 먼저 연결해야 한다. 이 연결표가 없는 부분을 미완 산출물로 잡았으며, 모두 미판독이라고 판정한 것이 아니다.

기존 자료만으로 R1/R2의 최종 대조표가 채워져 있지는 않다. 따라서 현시점에 “거의 완료”, “몇 퍼센트 남음”, “곧 끝남”을 산출할 근거는 없다. 향후 보고는 R1~R4 중 어떤 산출물이 닫혔고 어떤 구체적 공백이 남았는지로 한다.

## 현재 특정한 정정 위치 (R3)

| ID | 대상 | 확인된 정정 이유·필요한 대조 |
|---|---|---|
| C1 | `xbeach_wave_boundary_generation.md`의 제목·§2/§4, `wave/xbeach_wave_boundary.md`의 newer-interface 설명 | 빌드 제외된 `wave_boundary_update/main` 분석과 현재 `waveparamsnew` 실행 경로가 섞여 있다. 이미 [source-audit 보충](../../../../../../models/XBeach/source-analysis/xbeach-source-audit-supplements.md)의 B10/B16/B20은 prototype으로 한정했고, [빌드 원장](../build-mode-20260912/build-map.json)도 제외를 확인했다. 알고리즘의 재사용 가능한 설명은 유지하되 현재 호출 관계로 오인되지 않게 정정. |
| C2 | `xbeach_wave_action_balance.md` §5/§6, `xbeach_wave_stationary.md`의 두 구현 설명 | 현재 stationary 호출은 `wave_stationary_directions`; `wave_directions`/`wave_stationary`는 조사한 빌드 목록 밖이다. [빌드/모드 계약](../build-mode-20260912/contracts.json)과 기존 보충의 `wave_directions` B5 판정에 맞춰 구형/활성 구현을 구분. |
| C3 | `xbeach_intrawave_sediment_transport.md` §2/§4, `xbeach_morphology.md`의 입력/dispatch 범위 | “intrasedtr는 입력 불가·자동 선택” 설명과 달리 `params.F90:932-945` 입력 목록은 `intrasedtr`를 포함한다. 입력 이름 목록과 `morphevolution.F90:173-190`의 실제 case 목록을 구분하고, 입력된 이름이 실제 어느 계산으로 이어지는지는 R1에서 확인. 이름 개수를 실행 공식 개수로 바꾸지 않음. [원문과 현재 노트의 인용](correction-evidence.json) |
| C4 | `INFILTRATION-DOCUMENT-CODE-COMPARISON.md`의 미반영 보충 | +1 관계·암시적 시간 이산화·제한 조건은 이미 대조했으나 이 기록은 staging에 머문다. [기존 비교](../infiltration-document-code-comparison.json)를 지하수 또는 매뉴얼 노트에 출처와 함께 반영. 원문 오류의 저자 의도를 새로 조사하지 않음. |

C1~C4는 위키 정정 후보의 위치 고정이며, 이번 기록만으로 canonical을 수정하거나 새 소스 결함을 확정하지 않았다. 다른 모순이 같은 동결 자료 안에서 확인되면 R1/R2/R3의 하위 처분으로 기록하고 상위 작업 묶음은 늘리지 않는다.

## 다음 실행 순서

먼저 C3의 표사 입력과 실제 분기를 R1에서 대조해 정정한다. 이어 이미 있는 빌드 근거로 C1/C2의 구형 파랑 구현 귀속을 맞추고 C4 침투식 보충을 반영한다. 이 정정들은 R1/R2 전체가 끝날 때까지 기다릴 일이 아니다. 그 뒤 R1의 나머지 호출/조건 공백과 R2의 수식 위치별 근거를 채우고, 동일한 최종 결과로 R4를 수행한다. R3 전체의 종결만 R1/R2 최종 판정에 의존한다.

## 범위를 늘리지 않는 규칙

- 노트의 “Next expansion”, 실습 제안, 추가 성능 비교·개인 케이스는 필수 잔여가 아니다.
- 모든 원본 솔버 결함을 패치하거나 모든 모드 조합을 실행해 무오류를 보장하는 것은 이번 위키 분석의 종료 조건이 아니다. 구체적 모순 검증에 필요한 최소 재현은 해당 R1/R2 안에서 수행한다.
- 0a의 저자 의도, 불투명한 서식 payload, 원본 빈 수식, 글꼴 네모의 내부 원인은 문서 제약으로 남길 수 있다. 모델 의미가 이미 판정된 기호를 다시 미확정 작업으로 돌리지 않는다. 모델 의미가 실제로 미해결인 항목은 R2에서 그대로 미완이다.
- MPI/Jumpshot·범용 의존성·설치 도구 내부, 새 모델·새 판본·새 benchmark는 자동 범위가 아니다.
- **입력 추가는 사용자 요청이 있을 때만 한다.** 기존 입력의 잘못된 분류를 수정할 경우 이유·영향·기존 ID를 함께 남긴다. 새 파일 수를 늘려 진행률을 만들어내지 않는다.
- R1~R4의 산출물·검토·필요한 승인이 갖춰지면 이 XBeach 작업은 종료한다. “더 완벽하게”를 이유로 다음 연구 주제를 덧붙이지 않는다.

## 재현과 검증

`reconcile.py`는 원래 원장의 정확한 src 집합·원본 SHA·기존 판독 기록을 대조하고 현재 노트의 재사용 위치, 문서 필드/객체 위치를 저장한다. 구조/해시/목록 대조이며 의미 승인 도구가 아니다. `input-bindings.json`은 이번 기준 입력을 고정한다. 미래 canonical 변경 뒤에도 이번 파일은 당시 snapshot으로 보존한다.

`python3 _staging/total-read/model-audit/XBeach/connectivity/remaining-20260912/validate.py`는 고정 집합과 출처 인용·재사용 영수증·불변 이력을 검사한다. R1/R2 내용 검토나 최종 HG 성공을 대신하지 않는다.

[독립 Codex 검토](codex-review.txt)는 잔여 목록의 범위·미완 구분은 유지된다고 판단했고, 재생성 시 필수 근거 14개가 누락되는 P2 한 건을 지적했다. 생성기에 해당 근거를 포함하고 validator가 필수 집합의 누락을 거부하도록 수정했다. [재생성·누락 거부 확인](regeneration-check.json)은 77개 연결 보존, 네 산출물의 바이트 동일 재생성, 14개 제거 시 실패를 확인한다. 수정 후 검증은 로컬에서 수행했으며 별도 두 번째 독립 검토로 표현하지 않는다. [검토 반영 기록](review-response.json)을 보존하며 R1~R4와 새 사람 승인은 여전히 미완이다.

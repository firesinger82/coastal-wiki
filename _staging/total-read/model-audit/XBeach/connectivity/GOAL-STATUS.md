# XBeach 完了 목표 추적

## 2026-09-12 R1 실행 연결 보강·7개 문서 정정 — 최신 재개 지점

[실행 연결 보강](runtime-20260912/README.md)에서 선박 `ph`/nonh `pres·dp`, 운동량 잔차 부호·2차 보정 호출, 식생·강우·조도 갱신 시점, 출력 공급자/rank, 생성 로그·콜백을 소스에 결속했다. 기존 문서 7개를 [정확한 manifest](runtime-20260912/install-manifest.json)대로 반영했다. 독립 검토의 선박 소비 OR 조건 누락 P2를 수정하고 [후속 검토](runtime-20260912/codex-followup.txt)를 완료했다. 원문 48구간·생성 출력 27개·문서 링크·설치 바이트·기존 불변 기록 292개와 소유자/권한을 확인했다.

**R1 전체는 아직 미완이다.** 호출 후보 인덱스는 전체 의미 도달성 증명이 아니다. 다음 대조는 [R1-G1/G2/G3](runtime-20260912/remaining-gaps.json)의 generic/가시성/실행 조건, 미분류 정의, 동적 wrapper·생성 interface 연결이다. R2 수식별 대응 및 R3/R4 전체도 미완이며 입력 집합은 늘리지 않았다. [후속 상태](remaining-20260912/progress.json)가 현재 반영 상태다. 과거 C1~C4와 이번 정정을 다시 미완으로 세지 않는다.

Codex 하위 검토 프로세스의 읽기 전용 파일시스템 시작 실패와 승인 실행 경로는 [실행 메모](runtime-20260912/EXECUTION-NOTES.md)에 기록했다. 같은 유형을 기본 sandbox에서 반복 실패시키지 않는다. 전체 모델 완료·새 사람 승인·GOAL 도구 상태는 변경하지 않았다.

## 2026-09-12 초기 정정 R3-C1~C4 반영 — 이전 재개 기록

[정정 네 건](corrections-20260912/README.md)을 기존 위키 문서 8개에 반영했다. `intrasedtr`의 명시 입력과 12개 입력→실제 공식 분기를 구분했고, 활성 파랑 경계·stationary 루틴의 귀속과 위상 처리를 고쳤으며, 기존 침투식 비교를 매뉴얼 노트에 넣었다. [후속 상태](remaining-20260912/progress.json)가 아래 동결 목록의 초기 네 정정 상태보다 우선한다. 과거 입력·검증 snapshot은 원래 해시를 보존한다.

다음은 고정 R1의 기존 루틴·호출 조건·핵심 상태 소비 근거에서 미연결 부분을 대조하고, R2의 기존 수식 판정과 위치를 결속하는 일이다. 처리한 네 정정을 다시 미완으로 세지 않는다. R3 전체는 R1/R2의 최종 결과에 의존하므로 아직 종결하지 않았다. 전체 모델 완료·새 사람 승인·GOAL 도구 상태는 변경하지 않았다.

## 2026-09-12 실제 잔여 고정 — 다음 재개의 기준

현재 잔여의 기준은 [고정 작업표 R1~R4](remaining-20260912/README.md)와 [기계 판독 목록](remaining-20260912/remaining.json)이다. 기존 판독·경계/표사/선택 기능 노트를 미작성으로 다시 세지 않는다. R1은 기존 실행 연결 근거의 전체 대조, R2는 세 기술 문서 수식의 기존 판정·구현 대응 결속, R3는 특정한 위키 충돌 정정·반영, R4는 그 최종 결과의 검토·필요 승인이다. 각 입력 집합·재사용 근거·종료 조건을 고정했다.

이미 확인한 정정은 구형 파랑 코드의 활성 경로 오인, stationary 구현 귀속, intrasedtr 입력 설명, staging 침투식 보충의 미반영이다. 현재 노트와 원문 인용은 [정정 근거](remaining-20260912/correction-evidence.json)에 있다. 새 발견은 동결 입력 안의 해당 R 항목에서 처리한다. 노트의 Next expansion, 새 버전·새 사례, 부속 도구 내부를 필수 잔여로 붙이지 않는다. 목록 작성·검사 성공 자체는 모델 완료가 아니며 R1~R4는 아직 미완이다.

## 2026-09-12 사용자 정정 — 재개 시 우선 적용

**MPI/Jumpshot 뷰어 등 부속 도구 내부 판독은 중단하며 XBeach 완료 조건에서 제외한다.** “전수·완벽·GOAL·계속”을 동봉 의존성 전체 역어셈블리 지시로 해석하지 않는다. 아래 과거 로그의 Java/Python 미판독 수와 컨테이너 내부 판독 지시는 다음 작업이 아니다. 원본과 판독 영수증은 이력으로 보존하며, 제외 항목을 판독 완료로 바꾸지 않는다.

다음 작업은 XBeach 자체의 물리·수치해법·입출력·실행 흐름, 매뉴얼 수식의 의미 대조, lifecycle/physics 연결 검증과 검토본 정리다. 부속 도구 조사 예외와 진행 보고 기준은 [공통 범위 통제](../../../../../CLAUDE.md#모델-분석-범위-통제)를 따른다. 모델 자체의 검토·승인 조건은 유지한다.


## 2026-09-12 모델 작업 재개 결과

- **물리 연결 쟁점 XB-PHY-U01~U04:** [재판정](physics/resolution-20260912/adjudication.json)과 [외부 검토·반영](physics/resolution-20260912/review-response.json)을 저장했다. 입경의 로컬 배열 덮어쓰기는 원문 Fortran 반복문으로 1D/2D 재현했다. 침투량 단위 오류는 다음 gwflow 초기화 전 노출 상태로 영향을 한정했다. 지형–지하수의 수심 갱신 시점과 Q3D/Van Rijn 1993 분기를 정리했다. 이 네 쟁점은 정적 판정이 있는 상태이며 원본 솔버 패치나 전체 계산 검증 완료가 아니다.
- **문서 기호 4곳:** [응력 텐서 𝕋 두 곳](nonhydro-read/stress-tensor-symbol/receipt.json), [고립파 ≪·∼ 두 곳](nonhydro-read/solitary-wave-symbols/receipt.json)의 의미를 원본 PDF 시각 판독 및 DOC Native/문단 결속으로 확인했다. 이 네 곳의 의미는 다시 미확정 과제로 반복하지 않는다. DOC 렌더의 네모·배치 문제와 나머지 수식 의미 대조는 별도다.
- **위키 반영:** Q3D 실행 조건·설정표·pitfall 정정, 비정수압 보고서 기호 보충, 연결 계약 검토본 1편과 목차를 [설치 manifest](physics/resolution-20260912/install-manifest.json)의 다섯 경로에 반영했다. 새 연결 노트는 draft-unsourced이며 사람 승인을 발급하지 않았다. 기존 승인·crosswalk·closure 292개는 불변이다.

## 2026-09-12 lifecycle 계약 후속 정리

[XB-SC-001~012 재판정](lifecycle/resolution-20260912/adjudication.json)과 [Claude 검토·수정 확인](lifecycle/resolution-20260912/review-response.json)을 완료했다. 초기화·hotstart·스텝·종료와 독립 실행/BMI/dynamic/Python 진입점의 계약을 소스에 연결했다. `hotstartflow=1`의 재계산 유속, MPI 초기화 경고 5·6 후 첫 step 전 출력의 미대입 반환, 오류 1의 프로세스 종료, getter local의 암시적 SAVE를 기존 후보 설명과 구분한다. BMI 시간 setter가 출력 인덱스를 재배치하지 않는다는 한계도 기록했다.

[최소 재현](lifecycle/resolution-20260912/probe-results.json)은 정상 출력 반환·오류 출력 STOP 1·getter local 유지만 확인한다. 전체 모델 또는 MPI 실행 검증을 뜻하지 않는다. [연결 검토본](../../../../../models/XBeach/source-analysis/xbeach-lifecycle-state-contracts.md)은 draft-unsourced이며 새 사람 승인을 발급하지 않는다. 기존 원장과 승인 이력은 그대로 보존한다. [설치 manifest](lifecycle/resolution-20260912/install-manifest.json)의 다섯 문서를 반영하고 [인용·프로브·설치 검증](lifecycle/resolution-20260912/validation.json)을 통과했다. 원본 인용 67곳과 기존 불변 이력 292개가 일치한다.

## 2026-09-12 빌드·모드·수식 대응 후속

[모델 빌드·파일 역할](build-mode-20260912/build-map.json)은 Autotools, 여덟 모델 프로젝트와 일곱 solution, 전체 src 파일 집합을 대조한다. 별도 Windows BMI 대상과 코어 의존, 대상별 정의·제외 파일, 생성 include 소비자를 기록했다. Python 소스 생성기는 임시 복사본에서 실행해 출력 집합을 확인했다. [분기·수식 계약](build-mode-20260912/contracts.json)은 기존 여섯 dispatcher 경로를 다시 빌드 대상과 연결하고, (2.5)~(2.10)의 파수 보정 및 B.37/C.37의 지형 갱신을 원문과 대조한다. 기존 과거 원장을 덮어쓰지 않는다.

파수 보정량의 모델 의미와 `sourcesink`/침식 부호는 판정이 있는 상태다. B.37/C.37의 `a`는 원문에 남겨 둔 저자 의도 미정 표기이며, 대응 코드에 별도 a 의존 항이 없음을 기록했다. 글꼴 문제의 내부 원인이나 이 a의 출처를 찾기 위해 부속 도구로 확장하지 않는다.

[독립 Codex 원문 검토·반영](build-mode-20260912/review-response.json)을 마쳤다. Claude 시도는 사용량 한도로 중단된 이력이며 실제 검토 제공자와 구분한다. [설치 manifest](build-mode-20260912/install-manifest.json)의 여섯 문서에 새 빌드·수식 검토본, 기존 wave dispatcher/input 계약 정정, 목차를 반영했다. [인용·생성·설치 검증](build-mode-20260912/validation.json)은 출처 40구간, 생성 include 27개, 설치 바이트와 불변 이력 292개를 확인한다. 두 신규 노트는 draft-unsourced다. 전체 솔버 실행이나 모든 루틴 도달성의 검증을 대신하지 않는다.

이 후속 작업의 실제 잔여는 상단 [고정 작업표 R1~R4](remaining-20260912/README.md)를 따른다. 경계·표사·선택 기능 전체가 미작성이라는 뜻으로 해석하지 않는다. lifecycle 12개·physics 네 쟁점·여섯 dispatcher와 기존 분야 노트는 재사용하며, 전체 완료·새 사람 승인은 별도다.

2026-09-12 도구 상태 확인: GOAL은 **paused**다. 이 문서는 상태 추적이며 도구를 자동 재개하거나 완료 처리하지 않는다. 아래 활성화 문구는 당시 이력이다.

2026-09-11 사용자 요청으로 GOAL 활성화: XBeach 전수 판독 → 연결 분석 → 검증 → canonical → 필요한 신규 HG를 끝까지 진행한다. 기준은 plan.md의 전수 판독/연결 계획에 위 사용자 범위 정정을 적용한 것이다. 전체 gate는 NOT_PASSED이며 아래는 완료 영수증이 아니다.

- DOCX Native 486개: 현재 463개 기계적 수용. 색상 0 참조 12개·RULER 불일치 8개·Master 3개는 길이 있는 확장 payload를 보존하고 본문 구조를 판독했으나 payload 의미는 미해결. 색상/정렬 20개도 별도 진단 옵션으로 구조를 확보했으나 strict에서는 계속 거부한다. 전체 486개 구조 대응은 strict 463 + opaque 3 + 조건부 20이다. 조건부 20개 원본 WMF는 전량 시각 대조했다. 세 침투식의 연산자 부재는 현재 코드의 +1 관계와 대조했고 원본 표기는 그대로 보존했다. 암시적 시간 이산화 및 제한 조건 차이를 기록했다. 수용된 식도 전체 의미/렌더 대조는 별도다.
- 비정수압 보고서 DOC: 388개 Native 전체 구조 판독. 새 두 스트림의 Euclid Math Two/F093는 응력 텐서 𝕋로 국소 의미 확인. 고립파 ≪·∼ 두 곳도 원본 PDF와 대조했다. 남은 수식 의미/inline 배치 확인은 별도다.
- 부속 ZIP/JAR·PE/AR/MSI 내부: 모델과 직접 관련 없는 구현 판독은 범위 제외. 과거 판독 수는 이력이며 XBeach 진행률이나 완료의 필수 조건이 아니다. 모델에 필요한 의존성 인터페이스 확인만 공통 범위 통제에 따라 수행한다.
- 기존 lifecycle/physics 연결 후보: 모델 자체의 판독 전제 충족 후 entry/build/mode 및 orphan/unknown을 검증하고 확정한다.
- canonical: 기존 승인 103개·crosswalk·closure 불변 보존. 새 분석 결과의 검토본을 만들고 기존 절차에 따라 반영한다.
- 필요한 외부 검토·사람 승인: 결과물을 먼저 준비한다. 기존 승인을 새 주장에 재사용하거나 자기 승인하지 않는다.
- FUNWAVE: XBeach 완료 전에는 기존 읽기 전용 preflight 상태 유지.

상세 증거와 재현 명령은 RESUME.md, 최신 기계 검증은 resume-validation.json에 있다. 위 모델 범위의 필수 작업이 종결되기 전까지 전체 완료로 표시하지 않는다.

2026-09-12 추가: base/io 9종 465줄을 직접 읽고 동일 SHA 54경로에 결속했다. 누적 Java 13/413종(66경로), Python 150종 미판독. [입출력 판독](bytecode-read/base-io-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 후속: SLOG2 헤더·디렉토리 7종 전체 판독. 누적 Java 20/413종, 남은 Java 393종/Python 150종. [근거](bytecode-read/slog2-header-read.json). 전체 gate NOT_PASSED.

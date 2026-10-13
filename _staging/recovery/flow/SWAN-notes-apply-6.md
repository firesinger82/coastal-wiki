# SWAN 담당 노트 반영 6 — 출력·수치 명령 (2026-10-13)

수정 파일은 아래 담당 노트 7개와 이 DELIVERABLE이다. 노트 수는 아래 「노트별 추가·수정 줄 범위」 표에서 셌다.
보고서의 `[10-13 ...]` 최종 결론과 원문 인용을 반영했다.
줄 번호는 반영 후 노트에서 센 값이다.

## 입력 보고서

| 보고서 | 반영 범위 |
|---|---|
| [R1](../compare/swan-theory-numerics-vs-code.md) | 담당 수치 명령 노트의 기본값 유지와 해법 구분 수정안. |
| [R2](../compare/swan-theory-sources-vs-code.md) | 담당 노트를 가리키는 수정안 행 없음. |
| [R3](../compare/swan-theory-obstacles-setup-qc-bc-vs-code.md) | NT-046의 set-up SOR 종료 기준. |
| [R4](../compare/swan-inputs-setup-vs-code.md) | 중첩 격자 명령 수정안과 출력 시각·COMPUTE 결론. |
| [R5](../compare/swan-inputs-physics-numerics-vs-code.md) | 담당 NUMERIC·PROP·COMPUTE·HOTFILE 행과 출력 변수 노트 행. |
| [R6](../compare/swan-outputs-vs-code.md) | 출력 수정안 N-001–N-022와 차이 결론 101행. |
| [R7](../compare/swan-implementation-history-vs-code.md) | N-031의 NetCDF 빌드 참조 줄. |
| [R8](SWAN-callflow.md) | N1-012의 TABLE 병렬 NetCDF 분기와 COMPUTE 상태 유지. |

## 노트별 추가·수정 줄 범위

범위는 이 작업 시작 시점의 노트와 반영 후 노트를 줄 단위로 비교한 결과다.
차이 표의 행 수는 각 노트의 `## 문서와 코드 차이 (10-13 대조)`에서 보고서 접두사가 붙은 행 ID를 센 값이다.
R6:O-098의 등록 기본값 표는 차이 행 수에 다시 더하지 않았다.

| 노트 | 추가·수정 위치 (노트:줄) | 차이 표 행 수 |
|---|---|---|
| [models/SWAN/manual-notes/swan-command-numerics-output-reference.md](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md) | `swan-command-numerics-output-reference.md:7`<br>`swan-command-numerics-output-reference.md:12`<br>`swan-command-numerics-output-reference.md:22`<br>`swan-command-numerics-output-reference.md:30–31`<br>`swan-command-numerics-output-reference.md:35–37`<br>`swan-command-numerics-output-reference.md:46`<br>`swan-command-numerics-output-reference.md:50`<br>`swan-command-numerics-output-reference.md:52–65`<br>`swan-command-numerics-output-reference.md:74`<br>`swan-command-numerics-output-reference.md:83`<br>`swan-command-numerics-output-reference.md:87`<br>`swan-command-numerics-output-reference.md:90`<br>`swan-command-numerics-output-reference.md:92–97`<br>`swan-command-numerics-output-reference.md:111`<br>`swan-command-numerics-output-reference.md:113–118`<br>`swan-command-numerics-output-reference.md:126–127`<br>`swan-command-numerics-output-reference.md:137`<br>`swan-command-numerics-output-reference.md:139–140`<br>`swan-command-numerics-output-reference.md:144–191` | 35 |
| [models/SWAN/manual-notes/swan-output-variable-definitions.md](../../../models/SWAN/manual-notes/swan-output-variable-definitions.md) | `swan-output-variable-definitions.md:7`<br>`swan-output-variable-definitions.md:12`<br>`swan-output-variable-definitions.md:22`<br>`swan-output-variable-definitions.md:24`<br>`swan-output-variable-definitions.md:30`<br>`swan-output-variable-definitions.md:32–33`<br>`swan-output-variable-definitions.md:46`<br>`swan-output-variable-definitions.md:50–54`<br>`swan-output-variable-definitions.md:60`<br>`swan-output-variable-definitions.md:63–64`<br>`swan-output-variable-definitions.md:72`<br>`swan-output-variable-definitions.md:74–77`<br>`swan-output-variable-definitions.md:85–91`<br>`swan-output-variable-definitions.md:97–98`<br>`swan-output-variable-definitions.md:101–103`<br>`swan-output-variable-definitions.md:114–115`<br>`swan-output-variable-definitions.md:117`<br>`swan-output-variable-definitions.md:120–121`<br>`swan-output-variable-definitions.md:132`<br>`swan-output-variable-definitions.md:136–244` | 65 |
| [models/SWAN/manual-notes/swan-spectral-file-format.md](../../../models/SWAN/manual-notes/swan-spectral-file-format.md) | `swan-spectral-file-format.md:7`<br>`swan-spectral-file-format.md:12`<br>`swan-spectral-file-format.md:22`<br>`swan-spectral-file-format.md:26`<br>`swan-spectral-file-format.md:32`<br>`swan-spectral-file-format.md:34–36`<br>`swan-spectral-file-format.md:63–65`<br>`swan-spectral-file-format.md:80–104` | 12 |
| [models/SWAN/source-analysis/swan-output-writers-implementation.md](../../../models/SWAN/source-analysis/swan-output-writers-implementation.md) | `swan-output-writers-implementation.md:6`<br>`swan-output-writers-implementation.md:11`<br>`swan-output-writers-implementation.md:34`<br>`swan-output-writers-implementation.md:39–43`<br>`swan-output-writers-implementation.md:52`<br>`swan-output-writers-implementation.md:54`<br>`swan-output-writers-implementation.md:56`<br>`swan-output-writers-implementation.md:65`<br>`swan-output-writers-implementation.md:67`<br>`swan-output-writers-implementation.md:69`<br>`swan-output-writers-implementation.md:119`<br>`swan-output-writers-implementation.md:148`<br>`swan-output-writers-implementation.md:157`<br>`swan-output-writers-implementation.md:167`<br>`swan-output-writers-implementation.md:175`<br>`swan-output-writers-implementation.md:178`<br>`swan-output-writers-implementation.md:186`<br>`swan-output-writers-implementation.md:191–192`<br>`swan-output-writers-implementation.md:204–221` | 11 |
| [models/SWAN/source-analysis/swan-output-formats.md](../../../models/SWAN/source-analysis/swan-output-formats.md) | `swan-output-formats.md:6`<br>`swan-output-formats.md:11`<br>`swan-output-formats.md:27`<br>`swan-output-formats.md:60`<br>`swan-output-formats.md:62–63`<br>`swan-output-formats.md:70–71`<br>`swan-output-formats.md:81`<br>`swan-output-formats.md:126–128`<br>`swan-output-formats.md:168`<br>`swan-output-formats.md:182`<br>`swan-output-formats.md:188`<br>`swan-output-formats.md:222–239` | 11 |
| [models/SWAN/source-analysis/swan-vtk-output.md](../../../models/SWAN/source-analysis/swan-vtk-output.md) | `swan-vtk-output.md:6`<br>`swan-vtk-output.md:11`<br>`swan-vtk-output.md:21`<br>`swan-vtk-output.md:33`<br>`swan-vtk-output.md:59`<br>`swan-vtk-output.md:61`<br>`swan-vtk-output.md:74`<br>`swan-vtk-output.md:83`<br>`swan-vtk-output.md:87`<br>`swan-vtk-output.md:89–90`<br>`swan-vtk-output.md:98`<br>`swan-vtk-output.md:115–120`<br>`swan-vtk-output.md:122`<br>`swan-vtk-output.md:124`<br>`swan-vtk-output.md:126–140` | 3 |
| [models/SWAN/source-analysis/swan-nesting-io-implementation.md](../../../models/SWAN/source-analysis/swan-nesting-io-implementation.md) | `swan-nesting-io-implementation.md:6`<br>`swan-nesting-io-implementation.md:11`<br>`swan-nesting-io-implementation.md:34–36`<br>`swan-nesting-io-implementation.md:46–47`<br>`swan-nesting-io-implementation.md:69`<br>`swan-nesting-io-implementation.md:95`<br>`swan-nesting-io-implementation.md:102`<br>`swan-nesting-io-implementation.md:112`<br>`swan-nesting-io-implementation.md:114`<br>`swan-nesting-io-implementation.md:133–144` | 5 |

## 본문 수정안 반영 행 ID

이 목록에는 기존 문장의 수정과 조건 보충에 사용한 행 ID를 적었다.
유지한 문장과 식은 다음 절에 적었다.
차이 결론을 다른 노트에 배정한 행도 본문 수정에 사용한 경우 이 목록에 포함했다.

| 보고서 | 본문에 반영한 행 ID |
|---|---|
| R1 | R1:TN-077, R1:TN-106, R1:TN-172, R1:TN-173, R1:TN-174 |
| R2 | 담당 노트를 가리키는 본문 수정안 없음. |
| R3 | R3:NT-046 |
| R4 | R4:T1-014, R4:T1-300, R4:T1-304 |
| R5 | R5:PN-082, R5:PN-084, R5:PN-087, R5:PN-089, R5:PN-090, R5:PN-091, R5:PN-092, R5:PN-093, R5:PN-094, R5:PN-096, R5:PN-097, R5:PN-098, R5:PN-099, R5:PN-100, R5:PN-101, R5:PN-102, R5:PN-106, R5:PN-110, R5:PN-116, R5:PN-120, R5:PN-121, R5:PN-123, R5:PN-125, R5:PN-126, R5:PN-127, R5:PN-128, R5:PN-129, R5:PN-131, R5:PN-132, R5:PN-134, R5:PN-142, R5:PN-173, R5:PN-174, R5:PN-179, R5:PN-184, R5:PN-188 |
| R6 | R6:N-001, R6:N-002, R6:N-003, R6:N-004, R6:N-005, R6:N-006, R6:N-007, R6:N-008, R6:N-009, R6:N-010, R6:N-011, R6:N-012, R6:N-013, R6:N-014, R6:N-015, R6:N-016, R6:N-017, R6:N-018, R6:N-019, R6:N-020, R6:N-021, R6:N-022, R6:O-022, R6:O-024, R6:O-045, R6:O-046, R6:O-104, R6:O-106, R6:O-110, R6:O-112, R6:O-116 |
| R7 | R7:N-031 |
| R8 | R8:N1-012 |

## 유지한 문장과 식

문장과 식의 내용은 유지했다.
기존 내부 링크는 상대 Markdown 링크로 바꿨다.

| 위치 (노트:줄) | 유지 근거 |
|---|---|
| `models/SWAN/manual-notes/swan-command-numerics-output-reference.md:43` | R1 §4의 TN-077·106·172–174 |
| `models/SWAN/manual-notes/swan-command-numerics-output-reference.md:30` | R5 §4.5의 PN-079 |
| `models/SWAN/manual-notes/swan-command-numerics-output-reference.md:112` | R5 §4.2의 PN-096–102 및 R8 §6의 COMPUTE 일치 행 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:30` | R5 §4.5 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:70` | R5 §4.3의 PN-118 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:79` | R5 §4.3의 PN-122 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:112` | R5 §4.3의 PN-136 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:113` | R5 §4.3의 PN-137 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:116` | R5 §4.3의 PN-130 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:41` | R5 §4.5의 절대·상대 주기 정의 유지 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:42` | R5 §4.5의 절대·상대 주기 정의 유지 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:43` | R5 §4.5의 절대·상대 주기 정의 유지 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:44` | R5 §4.5의 절대·상대 주기 정의 유지 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:47` | R5 §4.5의 절대·상대 주기 정의 유지 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:48` | R5 §4.5의 절대·상대 주기 정의 유지 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:125` | R5 §4.3의 PN-139 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:129` | R5 §4.3의 PN-141 |
| `models/SWAN/manual-notes/swan-output-variable-definitions.md:130` | R5 §4.3의 PN-141 |

## 차이 결론 반영 행 ID

담당 노트의 차이 표에는 합계 142행을 넣었다.
이 수는 아래 보고서별 행 ID 목록에서 셌다.
담당 노트의 차이 표에서 일치 행은 0개다.
담당 노트의 차이 표에서 같은 행 ID를 중복한 행은 0개다.

| 보고서 | 반영 행 수 | 반영한 행 ID |
|---|---|---|
| R1 | 0 | 관련 차이 결론 5행은 아래 「다른 작업 담당」 표에 배정했다. |
| R2 | 0 | 담당 노트에 해당하는 차이 결론 없음. |
| R3 | 1 | R3:NT-046 |
| R4 | 2 | R4:T1-014, R4:T1-039 |
| R5 | 34 | R5:PN-081, R5:PN-082, R5:PN-083, R5:PN-084, R5:PN-087, R5:PN-090, R5:PN-092, R5:PN-093, R5:PN-095, R5:PN-098, R5:PN-099, R5:PN-101, R5:PN-102, R5:PN-104, R5:PN-106, R5:PN-110, R5:PN-116, R5:PN-118, R5:PN-120, R5:PN-121, R5:PN-123, R5:PN-125, R5:PN-126, R5:PN-127, R5:PN-128, R5:PN-129, R5:PN-131, R5:PN-134, R5:PN-137, R5:PN-142, R5:PN-173, R5:PN-174, R5:PN-179, R5:PN-188 |
| R6 | 101 | R6:O-002, R6:O-010, R6:O-011, R6:O-012, R6:O-014, R6:O-015, R6:O-017, R6:O-018, R6:O-020, R6:O-022, R6:O-024, R6:O-025, R6:O-028, R6:O-029, R6:O-031, R6:O-032, R6:O-033, R6:O-034, R6:O-036, R6:O-045, R6:O-046, R6:O-049, R6:O-050, R6:O-051, R6:O-052, R6:O-055, R6:O-056, R6:O-058, R6:O-059, R6:O-061, R6:O-063, R6:O-067, R6:O-073, R6:O-074, R6:O-075, R6:O-076, R6:O-077, R6:O-085, R6:O-086, R6:O-090, R6:O-091, R6:O-093, R6:O-097, R6:O-098, R6:O-099, R6:O-104, R6:O-105, R6:O-106, R6:O-107, R6:O-108, R6:O-110, R6:O-111, R6:O-112, R6:O-113, R6:O-114, R6:O-116, R6:O-118, R6:O-119, R6:O-120, R6:O-121, R6:O-122, R6:O-123, R6:O-124, R6:O-125, R6:O-126, R6:O-127, R6:O-128, R6:O-129, R6:O-130, R6:O-131, R6:O-132, R6:O-133, R6:O-134, R6:O-135, R6:O-136, R6:O-137, R6:O-138, R6:O-139, R6:O-140, R6:N-001, R6:N-002, R6:N-003, R6:N-004, R6:N-005, R6:N-006, R6:N-007, R6:N-008, R6:N-009, R6:N-010, R6:N-011, R6:N-012, R6:N-013, R6:N-014, R6:N-015, R6:N-016, R6:N-017, R6:N-018, R6:N-019, R6:N-020, R6:N-021, R6:N-022 |
| R7 | 1 | R7:N-031 |
| R8 | 3 | R8:T1-001, R8:T1-013, R8:N1-012 |

## 다른 작업 담당

아래 행의 차이 결론은 문서 근거·주제와 노트 제목이 더 가까운 담당 노트 밖에 배정했다.
본문 수정 여부는 각 행의 이유에 적었다.
R6의 차이 결론 101행은 모두 이번 담당 노트에 배정했다.

| 행 ID | 담당 노트 | 이유 |
|---|---|---|
| R1:TN-077 | [models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md](../../../models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md) | 차이 결론의 문서 근거는 swantech의 정지 조건 기본값이다. 담당 명령 노트에서는 일반 기본값을 유지하고 예외 조건을 보충했다. |
| R1:TN-106 | [models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md](../../../models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md) | 차이 결론의 문서 근거는 swantech §3.8의 계수와 활성 조건이다. 담당 명령 노트에서는 기본 비활성을 유지했다. |
| R1:TN-172, R1:TN-173, R1:TN-174 | [models/SWAN/manual-notes/swan-tech-ch6-iterative-solvers.md](../../../models/SWAN/manual-notes/swan-tech-ch6-iterative-solvers.md) | 차이 결론의 주제는 swantech §6.1·§6.2의 SIP와 스펙트럼 SWSOR 해법이다. 담당 명령 노트에서는 SIGIMPL·SETUP·SWSOR의 검사량을 구분했다. |
| R4:T1-015 | [models/SWAN/manual-notes/swan-usage-general.md](../../../models/SWAN/manual-notes/swan-usage-general.md) | 문서 근거는 사용자 매뉴얼 §2.6의 출력 영역 포함 방향이다. |
| R4:T1-300, R4:T1-304 | [models/SWAN/source-analysis/swan-command-file-reference.md](../../../models/SWAN/source-analysis/swan-command-file-reference.md) | 차이 결론의 주제는 명령 지원과 입력 문자열 수이다. 담당 중첩 노트의 SET FREQ·SET DIR 안내와 출력 형식 노트의 중첩 입력 예제는 수정했다. |
| R5:PN-085 | [models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md](../../../models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md) | 차이 결론의 주제는 SWSTPC의 TMREL 정규화 구현이다. |
| R5:PN-184 | [models/SWAN/source-analysis/swan-setup-solver-swancom1-crosswalk.md](../../../models/SWAN/source-analysis/swan-setup-solver-swancom1-crosswalk.md) | 차이 결론의 직접 노트 근거는 set-up solver의 RESM 설명이다. 담당 명령 노트의 SIP·SOR 설명도 수정했다. |

## 담당 범위인데 넣지 않은 행과 이유

없음.

## 확인 결과

- 담당 수정안의 본문 반영과 차이 결론 행 ID의 배정을 대조했다.
- 담당 노트의 차이 표 142행은 모두 여섯 열이다.
- 담당 노트의 `last_source_check`는 모두 `2026-10-13 (recovery 대조 반영)`이다.
- 담당 노트의 `verification_method`에는 `2026-10-13 recovery 대조 보고서 R1–R8 반영`을 한 번씩 덧붙였다.
- 담당 노트의 `citation_status`는 작업 시작 시점과 같다.
- 담당 노트의 Markdown 링크 대상 파일은 모두 존재한다.
- 담당 노트에 절대 경로와 이중 대괄호 링크가 없다.
- 담당 노트의 `git diff --check`는 오류 없이 끝났다.

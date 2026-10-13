# SWAN recovery 노트 반영 — 작업 7

작성일: 2026-10-13.

R7 §4의 담당 수정안 29행을 반영했다.
R7 §5의 담당 차이 결론 285행을 반영했다.
이 숫자는 담당 노트의 `R7:` 표 행과 R7 §4의 담당 노트 경로를 고유 행 ID로 집계한 값이다.

문서 판은 SWAN Cycle III 41.51 매뉴얼과 웹 수정 이력·패치이다.
swanpgr의 문서 판은 v1.3(2006-03-22)이다.
코드 판은 VERNUM 41.51과 원본 저장소 HEAD 43e9bbb(2026-07-13 patch B)이다.
판 근거는 [R7 §1](../compare/swan-implementation-history-vs-code.md#1-요약)과 [git 판정](../compare/SWAN-git-verify-A.md)이다.

## 노트별 추가·수정 줄 범위

줄 번호는 이 기록을 작성한 현재 파일 기준이다.
범위는 담당 노트의 `git diff --unified=0`에서 추가·수정 구간을 읽은 값이다.

| 노트 | 추가·수정 줄 범위 (노트:줄) | 반영 내용 |
|---|---|---|
| [manual-notes/swan-implementation-manual.md](../../../models/SWAN/manual-notes/swan-implementation-manual.md) | `models/SWAN/manual-notes/swan-implementation-manual.md:7–8, 23–25, 31, 35, 48, 51, 61–64, 68–70, 75–76, 86–87, 96–98, 103, 112, 116–119, 134, 142–144, 158–160, 164, 167, 172–175, 179, 183, 188–189, 209–214, 218, 224–225, 231–233, 237–240, 242–322` | 문서·코드 판, classic 배포 범위, 소스 목록, 전처리 조건, CMake, 시간 형식, 부하 분할, 실행 래퍼, 메모리 권고, 차이 표 72행. |
| [manual-notes/swan-programming-rules.md](../../../models/SWAN/manual-notes/swan-programming-rules.md) | `models/SWAN/manual-notes/swan-programming-rules.md:7–8, 44, 49, 66–68, 111, 147, 156–158, 160–220` | SAVE 규칙·예제, 비교 연산자 오기, STRACE 집계, 작성 규칙의 기존 예외, 차이 표 52행. |
| [manual-notes/swan-documentation-stack.md](../../../models/SWAN/manual-notes/swan-documentation-stack.md) | `models/SWAN/manual-notes/swan-documentation-stack.md:5, 7–8, 85, 107, 135, 157, 161, 164, 168, 183–185, 197–199, 201, 207–230, 238, 240, 242–246, 250–253, 257–434` | 문서 판, 스위치 개수, 작성 규칙의 적용 범위, 장별 대조 연결, 문서 구성·배포 표 12행, 수정 이력·패치 표 148행. |
| [manual-notes/README.md](../../../models/SWAN/manual-notes/README.md) | `models/SWAN/manual-notes/README.md:1–4, 6–25` | 템플릿 안내를 담당 노트의 탐색 문서로 바꿨다. 차이 결론은 연결한 담당 노트에 배정했다. |
| [README.md](../../../models/SWAN/README.md) | `models/SWAN/README.md:1–5, 15, 21–28, 33, 40, 44–45, 48–62, 67–77` | 소스 판·98커밋 이력, 매뉴얼 판 구분, R1–R8 포인터, R2·R4 주요 노트 연결, R5 명령 참조 연결, 차이 표 1행. |

## 반영한 노트 수정안 (R1–R7 §4, R8 §6)

| 보고서 | 반영 행 또는 원문 위치 | 담당 노트의 반영 |
|---|---|---|
| [R1](../compare/swan-theory-numerics-vs-code.md) | 행 ID 없는 README 수정안, 보고서 375행 | 모델 README:19의 격자 문장을 유지했다. 소스 판과 수치해법 대조 포인터를 추가했다. |
| [R2](../compare/swan-theory-sources-vs-code.md) | 행 ID 없는 README 수정안, 보고서 410행 | 모델 README 주요 노트 목록에 코드 판과 R2 링크를 추가했다. |
| [R3](../compare/swan-theory-obstacles-setup-qc-bc-vs-code.md) | R3:NT-051 | 모델 README:19의 격자 문장을 유지했다. 전체 격자 지원을 물리 모듈 전체의 지원으로 확대하지 않는 결론을 추가했다. |
| [R4](../compare/swan-inputs-setup-vs-code.md) | R4:T1-002 (수정안 표) | 모델 README:19의 격자 문장을 유지했다. R4 §1·§2의 판과 명령별 조건을 연결했다. |
| [R5](../compare/swan-inputs-physics-numerics-vs-code.md) | 행 ID 없는 README 수정안, 보고서 345행 | 매뉴얼의 41.51 기준을 유지했다. 명령 참조의 주요 노트 줄에 R5 링크를 추가했다. |
| [R6](../compare/swan-outputs-vs-code.md) | 보고서 368–371행 | README 수정안을 만들지 않는다는 판정을 따랐다. R6 탐색 포인터를 함께 수록했다. |
| [R8](SWAN-callflow.md) | 행 ID 없는 README 일치 행, 보고서 740행 | 모델 README:19의 격자 문장을 유지했다. R8 §4 흐름도·§6 수정안·§8 결론을 연결했다. |

### R7 수정안 행 ID

아래 ID는 [R7 §4](../compare/swan-implementation-history-vs-code.md#4-노트-대조와-수정안)의 담당 수정안이다.

담당 노트: [manual-notes/swan-implementation-manual.md](../../../models/SWAN/manual-notes/swan-implementation-manual.md).

`R7:N-001`, `R7:N-002`, `R7:N-003`, `R7:N-004`, `R7:N-005`, `R7:N-006`, `R7:N-007`, `R7:N-008`, `R7:N-009`, `R7:N-010`, `R7:N-011`, `R7:N-012`, `R7:N-013`, `R7:N-014`, `R7:N-015`, `R7:N-016`, `R7:N-017`, `R7:N-018`, `R7:N-019`, `R7:N-020`, `R7:N-021`, `R7:N-035`.

담당 노트: [manual-notes/swan-programming-rules.md](../../../models/SWAN/manual-notes/swan-programming-rules.md).

`R7:N-022`, `R7:N-023`, `R7:N-024`.

담당 노트: [manual-notes/swan-documentation-stack.md](../../../models/SWAN/manual-notes/swan-documentation-stack.md).

`R7:N-025`, `R7:N-026`.

담당 노트: [README.md](../../../models/SWAN/README.md).

`R7:N-033`, `R7:N-034`.

R7:N-004는 현행 AB 패치 표기를 덧붙였다.
R7:N-034는 모델 README의 75파일 인벤토리 문장을 그대로 유지했다.
R3:NT-051·R4:T1-002·R8의 README 일치 행은 차이 표에 넣지 않았다.

## 반영한 차이 결론 행 ID (R7 §5)

이 목록은 담당 노트의 차이 표에서 고유 행 ID로 집계했다.
각 행은 노트 하나에만 있다.

### manual-notes/swan-implementation-manual.md — 72행

노트의 차이 표: `models/SWAN/manual-notes/swan-implementation-manual.md:251–322`.

- `R7:I-003`, `R7:I-008`, `R7:I-013`, `R7:I-015`, `R7:I-016`, `R7:I-022`, `R7:I-024`, `R7:I-025`

- `R7:I-029`, `R7:I-030`, `R7:I-032`, `R7:I-033`, `R7:I-043`, `R7:I-045`, `R7:I-048`, `R7:I-049`

- `R7:I-052`, `R7:I-053`, `R7:I-056`, `R7:I-057`, `R7:I-058`, `R7:I-059`, `R7:R-003`, `R7:R-006`

- `R7:R-007`, `R7:R-010`, `R7:C-001`, `R7:C-002`, `R7:C-003`, `R7:C-004`, `R7:C-005`, `R7:C-006`

- `R7:C-007`, `R7:C-008`, `R7:C-009`, `R7:C-010`, `R7:C-011`, `R7:C-012`, `R7:C-013`, `R7:C-014`

- `R7:C-015`, `R7:C-016`, `R7:C-017`, `R7:C-019`, `R7:C-020`, `R7:C-021`, `R7:C-023`, `R7:C-024`

- `R7:C-025`, `R7:C-026`, `R7:C-028`, `R7:N-001`, `R7:N-002`, `R7:N-003`, `R7:N-005`, `R7:N-006`

- `R7:N-007`, `R7:N-008`, `R7:N-009`, `R7:N-010`, `R7:N-011`, `R7:N-012`, `R7:N-013`, `R7:N-014`

- `R7:N-015`, `R7:N-016`, `R7:N-017`, `R7:N-018`, `R7:N-019`, `R7:N-020`, `R7:N-021`, `R7:N-035`

### manual-notes/swan-programming-rules.md — 52행

노트의 차이 표: `models/SWAN/manual-notes/swan-programming-rules.md:169–220`.

- `R7:P-001`, `R7:P-002`, `R7:P-003`, `R7:P-006`, `R7:P-007`, `R7:P-008`, `R7:P-009`, `R7:P-010`

- `R7:P-011`, `R7:P-012`, `R7:P-013`, `R7:P-014`, `R7:P-015`, `R7:P-016`, `R7:P-017`, `R7:P-018`

- `R7:P-019`, `R7:P-021`, `R7:P-023`, `R7:P-024`, `R7:P-025`, `R7:P-026`, `R7:P-027`, `R7:P-028`

- `R7:P-029`, `R7:P-030`, `R7:P-031`, `R7:P-033`, `R7:P-034`, `R7:P-035`, `R7:P-036`, `R7:P-037`

- `R7:P-039`, `R7:P-040`, `R7:P-041`, `R7:P-042`, `R7:P-043`, `R7:P-044`, `R7:P-045`, `R7:P-046`

- `R7:P-047`, `R7:P-048`, `R7:P-049`, `R7:P-050`, `R7:P-051`, `R7:P-052`, `R7:P-053`, `R7:P-054`

- `R7:P-055`, `R7:N-022`, `R7:N-023`, `R7:N-024`

### manual-notes/swan-documentation-stack.md — 160행

노트의 차이 표: `models/SWAN/manual-notes/swan-documentation-stack.md:268–434`.

- `R7:Q-002`, `R7:Q-005`, `R7:Q-007`, `R7:Q-008`, `R7:Q-018`, `R7:H-47p`, `R7:H-112`, `R7:H-131`

- `R7:H-133p`, `R7:H-139`, `R7:H-170p`, `R7:H-195`, `R7:H-202`, `R7:H-213p`, `R7:H-219`, `R7:H-219p`

- `R7:H-228p`, `R7:H-291`, `R7:H-306`, `R7:H-326`, `R7:H-333`, `R7:H-336p`, `R7:H-374p`, `R7:H-472`

- `R7:H-480p`, `R7:H-492`, `R7:H-501`, `R7:H-529`, `R7:H-531`, `R7:H-532`, `R7:H-534`, `R7:H-538`

- `R7:H-566`, `R7:H-583`, `R7:H-587`, `R7:H-589`, `R7:H-591`, `R7:H-599`, `R7:H-601`, `R7:H-686`

- `R7:H-695`, `R7:H-749`, `R7:H-755`, `R7:H-778`, `R7:H-789`, `R7:H-813`, `R7:H-837`, `R7:H-840`

- `R7:H-846`, `R7:H-849`, `R7:H-852`, `R7:H-855`, `R7:H-858`, `R7:H-861`, `R7:H-864`, `R7:H-867`

- `R7:H-870`, `R7:H-873`, `R7:H-890`, `R7:H-894`, `R7:H-903`, `R7:H-910`, `R7:H-913`, `R7:H-921`

- `R7:H-936`, `R7:H-940`, `R7:H-944`, `R7:H-945`, `R7:H-949p`, `R7:H-955`, `R7:H-959`, `R7:H-961`

- `R7:H-966`, `R7:H-968`, `R7:H-979`, `R7:H-1006`, `R7:H-1056`, `R7:H-1081`, `R7:H-1088`, `R7:H-1097`

- `R7:H-1121`, `R7:H-1123`, `R7:H-1124`, `R7:H-1128`, `R7:H-1134`, `R7:H-1149`, `R7:H-1150`, `R7:H-1151`

- `R7:H-1170`, `R7:H-1174`, `R7:H-1180`, `R7:H-1182`, `R7:H-1183`, `R7:H-1197`, `R7:H-1204`, `R7:H-1205`

- `R7:H-1208`, `R7:H-1212`, `R7:H-1214`, `R7:H-1215`, `R7:H-1227`, `R7:H-1228`, `R7:H-1229`, `R7:H-1234`

- `R7:H-1240`, `R7:H-1242`, `R7:H-1257`, `R7:H-1263`, `R7:H-1268`, `R7:H-1273`, `R7:H-1274`, `R7:H-1275`

- `R7:H-1305`, `R7:H-1319`, `R7:H-1331`, `R7:H-1336`, `R7:H-1337`, `R7:H-1346`, `R7:H-1350`, `R7:H-1354`

- `R7:H-1358`, `R7:H-1360`, `R7:H-1371`, `R7:H-1373`, `R7:H-1375`, `R7:H-1386`, `R7:H-1388`, `R7:H-1389`

- `R7:H-1390`, `R7:H-1397`, `R7:H-1398`, `R7:H-1399`, `R7:H-1418`, `R7:H-1419`, `R7:H-1447`, `R7:H-1455`

- `R7:H-1464`, `R7:H-1480`, `R7:H-1482`, `R7:H-1504`, `R7:H-1514`, `R7:H-1531`, `R7:H-1547`, `R7:H-1596`

- `R7:H-1603`, `R7:H-1611`, `R7:H-1620`, `R7:H-1638`, `R7:D-002`, `R7:D-003`, `R7:D-005`, `R7:D-007`

- `R7:D-008`, `R7:D-009`, `R7:D-010`, `R7:D-011`, `R7:D-012`, `R7:S-002`, `R7:N-025`, `R7:N-026`

### README.md — 1행

노트의 차이 표: `models/SWAN/README.md:77–77`.

- `R7:N-033`

## 다른 작업 담당

R7의 다른 작업 담당 차이 결론은 22행이다.
이 숫자는 [R7 §5](../compare/swan-implementation-history-vs-code.md#5-차이-결론)에서 담당 노트의 제목보다 아래 노트의 주제가 가까운 행을 센 값이다.

| 행 ID | 항목 | 다른 작업 담당 노트 | 배정 이유 |
|---|---|---|---|
| `R7:ED-040` | NUMERIC | [manual-notes/swan-command-numerics-output-reference.md](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md) | 명령 구문·위치 인자·출력 조건. |
| `R7:ED-043` | QUANTITY | [manual-notes/swan-command-numerics-output-reference.md](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md) | 명령 구문·위치 인자·출력 조건. |
| `R7:ED-044` | OUTPUT OPTIONS | [manual-notes/swan-command-numerics-output-reference.md](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md) | 명령 구문·위치 인자·출력 조건. |
| `R7:ED-045` | BLOCK·TABLE 출력량 | [manual-notes/swan-command-numerics-output-reference.md](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md) | 명령 구문·위치 인자·출력 조건. |
| `R7:ED-046` | SPECOUT | [manual-notes/swan-command-numerics-output-reference.md](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md) | 명령 구문·위치 인자·출력 조건. |
| `R7:ED-051` | READINP 괄호 | [manual-notes/swan-command-setup-grid-reference.md](../../../models/SWAN/manual-notes/swan-command-setup-grid-reference.md) | 명령 구문·위치 인자·출력 조건. |
| `R7:ED-052` | QUANTITY POWER·REF 순서 | [manual-notes/swan-command-numerics-output-reference.md](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md) | 명령 구문·위치 인자·출력 조건. |
| `R7:H-1162e` | GEN1·GEN2의 FIT 고풍속 보호 | [source-analysis/swan-wind-formulations-implementation.md](../../../models/SWAN/source-analysis/swan-wind-formulations-implementation.md) | GEN1·GEN2의 FIT 항력 조건과 결함 후보는 바람 입력 구현 주제이다. |
| `R7:F-010` | 실험실부터 전 지구 규모 | [manual-notes/swan-usage-general.md](../../../models/SWAN/manual-notes/swan-usage-general.md) | 실험실부터 전 지구 규모의 물리·설정·적용 주제. |
| `R7:S-001` | 설정의 적용 범위 | [manual-notes/swan-usage-general.md](../../../models/SWAN/manual-notes/swan-usage-general.md) | 설정의 적용 범위의 물리·설정·적용 주제. |
| `R7:S-003` | Janssen 사용 비권고 | [source-analysis/swan-wind-formulations-implementation.md](../../../models/SWAN/source-analysis/swan-wind-formulations-implementation.md) | Janssen 사용 비권고의 물리·설정·적용 주제. |
| `R7:S-006` | 지역 규모 시험·개방 연안 | [manual-notes/swan-usage-general.md](../../../models/SWAN/manual-notes/swan-usage-general.md) | 지역 규모 시험·개방 연안의 물리·설정·적용 주제. |
| `R7:S-012` | 복잡한 수심에서 가변 쇄파 권고 | [manual-notes/swan-tech-ch2-dissipation-detailed.md](../../../models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md) | 복잡한 수심에서 가변 쇄파 권고의 물리·설정·적용 주제. |
| `R7:S-016` | 복잡한 현장 정확성 | [manual-notes/swan-usage-general.md](../../../models/SWAN/manual-notes/swan-usage-general.md) | 복잡한 현장 정확성의 물리·설정·적용 주제. |
| `R7:S-018` | 파일 주석의 출처·용도·도입판 | [manual-notes/swan-usage-general.md](../../../models/SWAN/manual-notes/swan-usage-general.md) | 파일 주석의 출처·용도·도입판의 물리·설정·적용 주제. |
| `R7:S-019` | 수렴 설정 권고 | [manual-notes/swan-command-numerics-output-reference.md](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md) | 수렴 설정 권고의 물리·설정·적용 주제. |
| `R7:S-056` | 구판 LTA 기본값과 현재 전달계수 | [manual-notes/swan-tech-ch2-nonlinear-detailed.md](../../../models/SWAN/manual-notes/swan-tech-ch2-nonlinear-detailed.md) | 구판 LTA 기본값과 현재 전달계수의 물리·설정·적용 주제. |
| `R7:N-027` | OpenMP 실행 명령 | [source-analysis/swan-parallel-implementation.md](../../../models/SWAN/source-analysis/swan-parallel-implementation.md) | OpenMP 실행 명령 구현. |
| `R7:N-028` | MPI 입력 전달 | [source-analysis/swan-parallel-implementation.md](../../../models/SWAN/source-analysis/swan-parallel-implementation.md) | MPI 입력 전달 구현. |
| `R7:N-029` | 혼합 병렬 권고 | [source-analysis/swan-parallel-implementation.md](../../../models/SWAN/source-analysis/swan-parallel-implementation.md) | 혼합 병렬 권고 구현. |
| `R7:N-030` | ADCIRC와 COH 전처리 구분 | [source-analysis/swan-adcirc-coupling.md](../../../models/SWAN/source-analysis/swan-adcirc-coupling.md) | ADCIRC와 COH 전처리 구분 구현. |
| `R7:N-031` | netCDF 참조 줄 | [source-analysis/swan-output-formats.md](../../../models/SWAN/source-analysis/swan-output-formats.md) | netCDF 참조 줄 구현. |

R7 §4의 `R7:N-032`는 [소스 인벤토리](../../../models/SWAN/source-analysis/swan-source-coverage-audit.md)의 삭제 기록 유지 담당이다.
R3 §4의 `R3:NT-051` 중 set-up 세부 조건은 [경계조건·2D set-up 노트](../../../models/SWAN/manual-notes/swan-tech-ch4-5-bc-2d-setup.md) 담당이다.

### R1–R6·R8의 다른 작업 담당 차이 결론

아래 ID는 각 보고서의 차이 결론 표에서 일치 행을 제외한 목록이다.
담당 노트는 각 보고서의 노트 수정안 표에서 해당 주제로 연결한 노트이다.

### [R1](../compare/swan-theory-numerics-vs-code.md) — 125행

다른 작업 담당: 수치해법·굴절·반복 해법·병렬·비구조 격자의 manual-notes 및 source-analysis.

- `R1:TN-001`, `R1:TN-003`, `R1:TN-004`, `R1:TN-005`, `R1:TN-006`, `R1:TN-008`, `R1:TN-017`, `R1:TN-021`

- `R1:TN-023`, `R1:TN-026`, `R1:TN-027`, `R1:TN-028`, `R1:TN-031`, `R1:TN-034`, `R1:TN-044`, `R1:TN-045`

- `R1:TN-055`, `R1:TN-056`, `R1:TN-057`, `R1:TN-058`, `R1:TN-059`, `R1:TN-063`, `R1:TN-066`, `R1:TN-068`

- `R1:TN-070`, `R1:TN-073`, `R1:TN-074`, `R1:TN-075`, `R1:TN-076`, `R1:TN-077`, `R1:TN-078`, `R1:TN-080`

- `R1:TN-081`, `R1:TN-082`, `R1:TN-085`, `R1:TN-087`, `R1:TN-088`, `R1:TN-089`, `R1:TN-094`, `R1:TN-095`

- `R1:TN-096`, `R1:TN-098`, `R1:TN-099`, `R1:TN-100`, `R1:TN-101`, `R1:TN-102`, `R1:TN-104`, `R1:TN-106`

- `R1:TN-107`, `R1:TN-108`, `R1:TN-112`, `R1:TN-115`, `R1:TN-116`, `R1:TN-117`, `R1:TN-118`, `R1:TN-120`

- `R1:TN-121`, `R1:TN-122`, `R1:TN-123`, `R1:TN-127`, `R1:TN-134`, `R1:TN-138`, `R1:TN-139`, `R1:TN-140`

- `R1:TN-145`, `R1:TN-147`, `R1:TN-148`, `R1:TN-153`, `R1:TN-156`, `R1:TN-158`, `R1:TN-161`, `R1:TN-162`

- `R1:TN-163`, `R1:TN-164`, `R1:TN-165`, `R1:TN-166`, `R1:TN-168`, `R1:TN-171`, `R1:TN-172`, `R1:TN-173`

- `R1:TN-174`, `R1:TN-175`, `R1:TN-176`, `R1:TN-178`, `R1:TN-183`, `R1:TN-185`, `R1:TN-186`, `R1:TN-187`

- `R1:TN-188`, `R1:TN-190`, `R1:TN-191`, `R1:TN-194`, `R1:TN-201`, `R1:TN-203`, `R1:TN-204`, `R1:TN-211`

- `R1:TN-218`, `R1:TN-220`, `R1:TN-222`, `R1:TN-223`, `R1:TN-224`, `R1:TC-001`, `R1:TC-002`, `R1:TC-003`

- `R1:TC-004`, `R1:TC-005`, `R1:TC-006`, `R1:TC-007`, `R1:TC-008`, `R1:TC-009`, `R1:TC-010`, `R1:TC-011`

- `R1:TC-012`, `R1:TC-013`, `R1:TC-014`, `R1:TC-015`, `R1:TC-016`, `R1:TC-018`, `R1:TC-019`, `R1:TC-020`

- `R1:TC-021`, `R1:TC-022`, `R1:TC-023`, `R1:TC-024`, `R1:TC-025`

### [R2](../compare/swan-theory-sources-vs-code.md) — 138행

다른 작업 담당: 원천항·바람·백파·바닥 마찰·비선형 상호작용·식생·얼음·Bragg의 manual-notes 및 source-analysis.

- `R2:SS-036`, `R2:SS-038`, `R2:SS-039`, `R2:SS-201`, `R2:SS-049`, `R2:SS-051`, `R2:SS-055`, `R2:SS-056`

- `R2:SS-057`, `R2:SS-204`, `R2:SS-205`, `R2:SS-210`, `R2:SS-067`, `R2:SS-212`, `R2:SS-214`, `R2:SS-077`

- `R2:SS-084`, `R2:SS-088`, `R2:SS-089`, `R2:SS-215`, `R2:SS-216`, `R2:SS-217`, `R2:SS-361`, `R2:SS-362`

- `R2:SS-363`, `R2:SS-231`, `R2:SS-232`, `R2:SS-090`, `R2:SS-091`, `R2:SS-233`, `R2:SS-234`, `R2:SS-235`

- `R2:SS-093`, `R2:SS-236`, `R2:SS-094`, `R2:SS-095`, `R2:SS-100`, `R2:SS-219`, `R2:SS-220`, `R2:SS-106`

- `R2:SS-107`, `R2:SS-108`, `R2:SS-222`, `R2:SS-109`, `R2:SS-112`, `R2:SS-113`, `R2:SS-115`, `R2:SS-116`

- `R2:SS-270`, `R2:SS-274`, `R2:SS-287`, `R2:SS-118`, `R2:SS-119`, `R2:SS-121`, `R2:SS-126`, `R2:SS-127`

- `R2:SS-129`, `R2:SS-501`, `R2:SS-502`, `R2:SS-503`, `R2:SS-504`, `R2:SS-506`, `R2:SS-507`, `R2:SS-508`

- `R2:SS-509`, `R2:SS-510`, `R2:SS-511`, `R2:SS-512`, `R2:SS-513`, `R2:SS-514`, `R2:SS-515`, `R2:SS-516`

- `R2:SS-517`, `R2:SS-518`, `R2:SS-519`, `R2:SS-520`, `R2:SS-521`, `R2:SS-522`, `R2:SS-523`, `R2:SS-524`

- `R2:SS-525`, `R2:SS-526`, `R2:SS-527`, `R2:SS-528`, `R2:SS-529`, `R2:SS-530`, `R2:SS-531`, `R2:SS-532`

- `R2:SS-533`, `R2:SS-534`, `R2:SS-535`, `R2:SS-536`, `R2:SS-537`, `R2:SS-538`, `R2:SS-539`, `R2:SS-540`

- `R2:SS-701`, `R2:SS-702`, `R2:SS-703`, `R2:SS-704`, `R2:SS-705`, `R2:SS-706`, `R2:SS-707`, `R2:SS-708`

- `R2:SS-709`, `R2:SS-710`, `R2:SS-711`, `R2:SS-712`, `R2:SS-713`, `R2:SS-714`, `R2:SS-715`, `R2:SS-716`

- `R2:SS-717`, `R2:SS-718`, `R2:SS-719`, `R2:SS-720`, `R2:SS-721`, `R2:SS-722`, `R2:SS-723`, `R2:SS-724`

- `R2:SS-725`, `R2:SS-726`, `R2:SS-727`, `R2:SS-728`, `R2:SS-729`, `R2:SS-730`, `R2:SS-731`, `R2:SS-733`

- `R2:SS-734`, `R2:SS-735`, `R2:SS-736`, `R2:SS-737`, `R2:SS-738`, `R2:SS-739`, `R2:SS-740`, `R2:SS-741`

- `R2:SS-742`, `R2:SS-743`

### [R3](../compare/swan-theory-obstacles-setup-qc-bc-vs-code.md) — 213행

다른 작업 담당: 장애물·set-up·QC·경계조건의 manual-notes 및 source-analysis.

- `R3:OQ-003`, `R3:OQ-006`, `R3:OQ-009`, `R3:OQ-013`, `R3:OQ-014`, `R3:OQ-015`, `R3:OQ-017`, `R3:OQ-018`

- `R3:OQ-019`, `R3:OQ-020`, `R3:OQ-022`, `R3:OQ-023`, `R3:OQ-024`, `R3:OQ-025`, `R3:OQ-027`, `R3:OQ-029`

- `R3:OQ-030`, `R3:SU-001`, `R3:SU-002`, `R3:SU-003`, `R3:SU-004`, `R3:SU-005`, `R3:SU-006`, `R3:SU-007`

- `R3:SU-008`, `R3:SU-009`, `R3:SU-010`, `R3:SU-011`, `R3:SU-012`, `R3:SU-013`, `R3:SU-014`, `R3:SU-015`

- `R3:SU-016`, `R3:SU-019`, `R3:SU-020`, `R3:SU-021`, `R3:SU-024`, `R3:SU-026`, `R3:SU-027`, `R3:SU-028`

- `R3:SU-029`, `R3:SU-030`, `R3:SU-031`, `R3:SU-032`, `R3:SU-033`, `R3:SU-035`, `R3:SU-037`, `R3:SU-038`

- `R3:SU-041`, `R3:QC-001`, `R3:QC-002`, `R3:QC-003`, `R3:QC-004`, `R3:QC-005`, `R3:QC-006`, `R3:QC-007`

- `R3:QC-008`, `R3:QC-009`, `R3:QC-010`, `R3:QC-011`, `R3:QC-012`, `R3:QC-013`, `R3:QC-014`, `R3:QC-015`

- `R3:QC-016`, `R3:QC-017`, `R3:QC-018`, `R3:QC-019`, `R3:QC-020`, `R3:QC-022`, `R3:QC-023`, `R3:QC-024`

- `R3:QC-025`, `R3:QC-026`, `R3:QC-027`, `R3:QC-028`, `R3:QC-029`, `R3:QC-030`, `R3:QC-031`, `R3:QC-032`

- `R3:QC-033`, `R3:QC-034`, `R3:QC-035`, `R3:QC-036`, `R3:QC-037`, `R3:QC-038`, `R3:QC-039`, `R3:QC-040`

- `R3:QC-041`, `R3:QC-042`, `R3:QC-044`, `R3:QC-045`, `R3:QC-046`, `R3:QC-047`, `R3:QC-048`, `R3:QC-049`

- `R3:QC-050`, `R3:QC-051`, `R3:QC-052`, `R3:QC-053`, `R3:QC-054`, `R3:QC-055`, `R3:QC-056`, `R3:QC-057`

- `R3:QC-058`, `R3:QC-059`, `R3:QC-060`, `R3:QC-061`, `R3:QC-063`, `R3:QC-064`, `R3:QC-065`, `R3:QC-066`

- `R3:QC-067`, `R3:QC-068`, `R3:QC-069`, `R3:QC-073`, `R3:QC-074`, `R3:QC-075`, `R3:QC-076`, `R3:QC-078`

- `R3:QC-079`, `R3:QC-080`, `R3:QC-081`, `R3:QC-082`, `R3:QC-083`, `R3:QC-086`, `R3:QC-087`, `R3:QC-089`

- `R3:BC-005`, `R3:BC-006`, `R3:BC-007`, `R3:BC-011`, `R3:BC-013`, `R3:BC-014`, `R3:BC-015`, `R3:SU-042`

- `R3:CP-001`, `R3:CP-002`, `R3:CP-003`, `R3:CP-004`, `R3:CP-005`, `R3:CP-006`, `R3:CP-007`, `R3:CP-008`

- `R3:CP-010`, `R3:CP-011`, `R3:CP-012`, `R3:CP-013`, `R3:CP-014`, `R3:CP-015`, `R3:CP-016`, `R3:CP-017`

- `R3:CP-018`, `R3:CP-019`, `R3:CP-020`, `R3:CP-021`, `R3:CP-023`, `R3:CP-024`, `R3:CP-025`, `R3:CP-026`

- `R3:CP-028`, `R3:CP-029`, `R3:CP-030`, `R3:CP-031`, `R3:NT-001`, `R3:NT-002`, `R3:NT-003`, `R3:NT-004`

- `R3:NT-005`, `R3:NT-006`, `R3:NT-007`, `R3:NT-008`, `R3:NT-009`, `R3:NT-010`, `R3:NT-011`, `R3:NT-012`

- `R3:NT-013`, `R3:NT-014`, `R3:NT-015`, `R3:NT-016`, `R3:NT-017`, `R3:NT-018`, `R3:NT-019`, `R3:NT-020`

- `R3:NT-021`, `R3:NT-022`, `R3:NT-023`, `R3:NT-024`, `R3:NT-025`, `R3:NT-026`, `R3:NT-027`, `R3:NT-028`

- `R3:NT-029`, `R3:NT-030`, `R3:NT-031`, `R3:NT-032`, `R3:NT-033`, `R3:NT-034`, `R3:NT-035`, `R3:NT-036`

- `R3:NT-037`, `R3:NT-038`, `R3:NT-039`, `R3:NT-040`, `R3:NT-041`, `R3:NT-042`, `R3:NT-043`, `R3:NT-044`

- `R3:NT-045`, `R3:NT-046`, `R3:NT-047`, `R3:NT-049`, `R3:NT-052`

### [R4](../compare/swan-inputs-setup-vs-code.md) — 87행

다른 작업 담당: 일반 사용·격자·입력·경계 설정의 manual-notes 및 source-analysis.

- `R4:T1-001`, `R4:T1-003`, `R4:T1-004`, `R4:T1-005`, `R4:T1-006`, `R4:T1-007`, `R4:T1-009`, `R4:T1-011`

- `R4:T1-012`, `R4:T1-013`, `R4:T1-014`, `R4:T1-015`, `R4:T1-018`, `R4:T1-020`, `R4:T1-024`, `R4:T1-037`

- `R4:T1-038`, `R4:T1-039`, `R4:T1-050`, `R4:T1-054`, `R4:T1-055`, `R4:T1-058`, `R4:T1-060`, `R4:T1-061`

- `R4:T1-062`, `R4:T1-066`, `R4:T1-084`, `R4:T1-085`, `R4:T1-088`, `R4:T1-089`, `R4:T1-095`, `R4:T1-096`

- `R4:T1-097`, `R4:T1-136`, `R4:T1-137`, `R4:T1-144`, `R4:T1-147`, `R4:T1-174`, `R4:T1-175`, `R4:T1-176`

- `R4:T1-182`, `R4:T1-185`, `R4:T1-187`, `R4:T1-191`, `R4:T1-192`, `R4:T1-194`, `R4:T1-220`, `R4:T1-221`

- `R4:T1-222`, `R4:T1-223`, `R4:T1-224`, `R4:T1-225`, `R4:T1-226`, `R4:T1-227`, `R4:T1-228`, `R4:T1-229`

- `R4:T1-230`, `R4:T1-231`, `R4:T1-232`, `R4:T1-233`, `R4:T1-234`, `R4:T1-235`, `R4:T1-236`, `R4:T1-237`

- `R4:T1-238`, `R4:T1-239`, `R4:T1-240`, `R4:T1-241`, `R4:T1-250`, `R4:T1-251`, `R4:T1-252`, `R4:T1-253`

- `R4:T1-254`, `R4:T1-300`, `R4:T1-301`, `R4:T1-302`, `R4:T1-303`, `R4:T1-304`, `R4:T1-305`, `R4:T1-306`

- `R4:T1-307`, `R4:T1-308`, `R4:T1-309`, `R4:T1-310`, `R4:T1-311`, `R4:T1-312`, `R4:T1-313`

### [R5](../compare/swan-inputs-physics-numerics-vs-code.md) — 115행

다른 작업 담당: 물리·수치 명령의 manual-notes 및 source-analysis.

- `R5:PN-003`, `R5:PN-008`, `R5:PN-011`, `R5:PN-012`, `R5:PN-014`, `R5:PN-015`, `R5:PN-016`, `R5:PN-018`

- `R5:PN-021`, `R5:PN-024`, `R5:PN-025`, `R5:PN-032`, `R5:PN-038`, `R5:PN-041`, `R5:PN-042`, `R5:PN-045`

- `R5:PN-046`, `R5:PN-048`, `R5:PN-051`, `R5:PN-052`, `R5:PN-053`, `R5:PN-058`, `R5:PN-059`, `R5:PN-060`

- `R5:PN-061`, `R5:PN-064`, `R5:PN-065`, `R5:PN-066`, `R5:PN-068`, `R5:PN-070`, `R5:PN-072`, `R5:PN-074`

- `R5:PN-075`, `R5:PN-078`, `R5:PN-192`, `R5:PN-081`, `R5:PN-082`, `R5:PN-083`, `R5:PN-084`, `R5:PN-085`

- `R5:PN-087`, `R5:PN-090`, `R5:PN-092`, `R5:PN-093`, `R5:PN-095`, `R5:PN-098`, `R5:PN-099`, `R5:PN-101`

- `R5:PN-102`, `R5:PN-104`, `R5:PN-106`, `R5:PN-110`, `R5:PN-116`, `R5:PN-118`, `R5:PN-120`, `R5:PN-121`

- `R5:PN-123`, `R5:PN-125`, `R5:PN-126`, `R5:PN-127`, `R5:PN-128`, `R5:PN-129`, `R5:PN-131`, `R5:PN-134`

- `R5:PN-137`, `R5:PN-142`, `R5:PN-143`, `R5:PN-144`, `R5:PN-145`, `R5:PN-146`, `R5:PN-147`, `R5:PN-148`

- `R5:PN-149`, `R5:PN-150`, `R5:PN-151`, `R5:PN-152`, `R5:PN-153`, `R5:PN-154`, `R5:PN-155`, `R5:PN-156`

- `R5:PN-157`, `R5:PN-158`, `R5:PN-159`, `R5:PN-160`, `R5:PN-161`, `R5:PN-162`, `R5:PN-163`, `R5:PN-164`

- `R5:PN-165`, `R5:PN-166`, `R5:PN-167`, `R5:PN-168`, `R5:PN-169`, `R5:PN-170`, `R5:PN-171`, `R5:PN-172`

- `R5:PN-173`, `R5:PN-174`, `R5:PN-175`, `R5:PN-189`, `R5:PN-190`, `R5:PN-191`, `R5:PN-176`, `R5:PN-177`

- `R5:PN-178`, `R5:PN-179`, `R5:PN-180`, `R5:PN-181`, `R5:PN-182`, `R5:PN-183`, `R5:PN-184`, `R5:PN-185`

- `R5:PN-186`, `R5:PN-187`, `R5:PN-188`

### [R6](../compare/swan-outputs-vs-code.md) — 101행

다른 작업 담당: 출력 명령·출력량·스펙트럼 형식·출력 writer의 manual-notes 및 source-analysis.

- `R6:O-002`, `R6:O-010`, `R6:O-011`, `R6:O-012`, `R6:O-014`, `R6:O-015`, `R6:O-017`, `R6:O-018`

- `R6:O-020`, `R6:O-022`, `R6:O-024`, `R6:O-025`, `R6:O-028`, `R6:O-029`, `R6:O-031`, `R6:O-032`

- `R6:O-033`, `R6:O-034`, `R6:O-036`, `R6:O-045`, `R6:O-046`, `R6:O-049`, `R6:O-050`, `R6:O-051`

- `R6:O-052`, `R6:O-055`, `R6:O-056`, `R6:O-058`, `R6:O-059`, `R6:O-061`, `R6:O-063`, `R6:O-067`

- `R6:O-073`, `R6:O-074`, `R6:O-075`, `R6:O-076`, `R6:O-077`, `R6:O-085`, `R6:O-086`, `R6:O-090`

- `R6:O-091`, `R6:O-093`, `R6:O-097`, `R6:O-098`, `R6:O-099`, `R6:O-104`, `R6:O-105`, `R6:O-106`

- `R6:O-107`, `R6:O-108`, `R6:O-110`, `R6:O-111`, `R6:O-112`, `R6:O-113`, `R6:O-114`, `R6:O-116`

- `R6:O-118`, `R6:O-119`, `R6:O-120`, `R6:O-121`, `R6:O-122`, `R6:O-123`, `R6:O-124`, `R6:O-125`

- `R6:O-126`, `R6:O-127`, `R6:O-128`, `R6:O-129`, `R6:O-130`, `R6:O-131`, `R6:O-132`, `R6:O-133`

- `R6:O-134`, `R6:O-135`, `R6:O-136`, `R6:O-137`, `R6:O-138`, `R6:O-139`, `R6:O-140`, `R6:N-001`

- `R6:N-002`, `R6:N-003`, `R6:N-004`, `R6:N-005`, `R6:N-006`, `R6:N-007`, `R6:N-008`, `R6:N-009`

- `R6:N-010`, `R6:N-011`, `R6:N-012`, `R6:N-013`, `R6:N-014`, `R6:N-015`, `R6:N-016`, `R6:N-017`

- `R6:N-018`, `R6:N-019`, `R6:N-020`, `R6:N-021`, `R6:N-022`

### [R8](SWAN-callflow.md) — 29행

다른 작업 담당: 실행·배열 수명·수렴·출력 호출 흐름의 manual-notes 및 source-analysis.

- `R8:T1-001`, `R8:T1-002`, `R8:T1-003`, `R8:T1-004`, `R8:T1-005`, `R8:T1-006`, `R8:T1-007`, `R8:T1-008`

- `R8:T1-009`, `R8:T1-010`, `R8:T1-011`, `R8:T1-012`, `R8:T1-013`, `R8:T1-014`, `R8:T1-015`, `R8:N1-001`

- `R8:N1-002`, `R8:N1-003`, `R8:N1-004`, `R8:N1-005`, `R8:N1-006`, `R8:N1-007`, `R8:N1-008`, `R8:N1-009`

- `R8:N1-010`, `R8:N1-011`, `R8:N1-012`, `R8:N1-013`, `R8:N1-014`

## 처리 기준과 검증

R7 §5에서 일치로 정정된 10행을 차이 표에서 제외했다.
제외 ID는 `R7:I-009`, `R7:I-010`, `R7:I-011`, `R7:I-012`, `R7:I-026`, `R7:I-028`, `R7:P-020`, `R7:C-018`, `R7:C-022`, `R7:C-027`이다.
분류는 각 행의 최종 10-13 태그를 반영한 R7 §5를 사용했다.

A 행 24개는 결론 문장에 git 판정 HASH와 날짜를 포함한다.
`R7:H-472`, `R7:H-566`, `R7:H-755`, `R7:H-1228`의 HASH와 날짜는 41.45 비교 커밋 `122b595`(2023-02-28)이다.
이 네 행의 후속 공개판 판정은 [git 판정의 기준](../compare/SWAN-git-verify-A.md)을 따른다.
과거 `HASH:src/파일:줄` 인용은 원문 형식을 유지했다.

`R7:H-1121`, `R7:D-005`, `R7:D-011`은 보고서의 실행·측정 한계 문장을 제외했다.
각 행의 나머지 결론 문장은 보고서 원문을 그대로 사용했다.
문서 체계 노트의 장별 보강 대기 문장은 R1–R3의 대조 결과 연결로 바꿨다.

고친 노트 5개는 `last_source_check: "2026-10-13 (recovery 대조 반영)"`를 포함한다.
고친 노트 5개는 `verification_method`에 지정한 R1–R8 반영 구절을 포함한다.
`citation_status`는 시작 상태를 유지했다.
원본 저장소의 읽기 전용 `git rev-list --count HEAD`는 98을 반환했다.
원본 저장소의 읽기 전용 `git log`에서 이력 기간은 2022-07-30~2026-07-13이다.

담당 차이 표의 행 ID·항목·분류·결론 문장을 R7 §5와 대조했다.
차이 표 285행의 열 수는 모두 6개이다.
차이 표의 행 ID 중복은 0개이다.
담당 노트의 `git diff --check`를 통과했다.
수정 이력·패치 소절의 148행은 H·Q 행으로 구성한다.
담당 노트의 상대 링크는 대상 파일에 연결한다.
위키 링크 문법과 개인 절대경로는 없다.

## 담당 범위인데 넣지 않은 행과 이유

없음.
R7 §4의 담당 수정안 29행과 R7 §5의 담당 차이 결론 285행을 모두 반영했다.
R1–R8의 모델 README 수정안과 유지 판정을 반영했다.

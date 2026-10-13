# SWAN 노트 반영 4 (2026-10-13)

R1–R8의 `[10-13 ...]` 최종 결론을 담당 노트에 반영했다. 문서 판은 SWAN Cycle III 41.51 매뉴얼과 웹 수정 이력·패치이다. 코드 판은 VERNUM 41.51과 원본 저장소 HEAD `43e9bbb`(2026-07-13, patch B)이다. 실제 patch B 변경 커밋은 `0dabfa4`(2026-07-13)이다.

## 입력 보고서

| 보고서 | 확정 입력 |
|---|---|
| R1 | [swan-theory-numerics-vs-code.md](../compare/swan-theory-numerics-vs-code.md) |
| R2 | [swan-theory-sources-vs-code.md](../compare/swan-theory-sources-vs-code.md) |
| R3 | [swan-theory-obstacles-setup-qc-bc-vs-code.md](../compare/swan-theory-obstacles-setup-qc-bc-vs-code.md) |
| R4 | [swan-inputs-setup-vs-code.md](../compare/swan-inputs-setup-vs-code.md) |
| R5 | [swan-inputs-physics-numerics-vs-code.md](../compare/swan-inputs-physics-numerics-vs-code.md) |
| R6 | [swan-outputs-vs-code.md](../compare/swan-outputs-vs-code.md) |
| R7 | [swan-implementation-history-vs-code.md](../compare/swan-implementation-history-vs-code.md) |
| R8 | [SWAN-callflow.md](SWAN-callflow.md) |

보조 근거는 [git A 판정](../compare/SWAN-git-verify-A.md), [git D 판정](../compare/SWAN-git-verify-D.md), [git E 판정](../compare/SWAN-git-verify-E.md), [외부 원문](../compare/SWAN-external-sources.md)이다.

## 노트별 추가·수정 줄 범위

줄 범위는 작업 시작본과 현재 본문을 비교해 산출했다. 표의 줄 번호는 반영 후 노트를 기준으로 한다. 상대 Markdown 링크로 바꾼 줄도 범위에 포함했다.

| 노트 | 추가·수정 위치 | 반영 내용 |
|---|---|---|
| [swan-foundation.md](../../../models/SWAN/source-analysis/swan-foundation.md) | `models/SWAN/source-analysis/swan-foundation.md:6–7, 28, 32–34, 60, 68, 161, 186, 224, 226–421` | 기본 전파법 정정. R8 흐름도 원문 3개. E 대표 표. 명령 읽기 차이 표. |
| [swan-propagation-implementation.md](../../../models/SWAN/source-analysis/swan-propagation-implementation.md) | `models/SWAN/source-analysis/swan-propagation-implementation.md:6–7, 34, 70–73, 75, 77–79, 85, 91–96, 98–100, 143, 152–154, 180, 182, 184, 186, 188, 194–195, 197, 199, 203, 205, 211, 267–312` | 행렬 결합 방향. 음해법 시간차분. 해법 선택. 제한기 조건. 수렴 기준. 차이 표. |
| [swan-schemes-implementation.md](../../../models/SWAN/source-analysis/swan-schemes-implementation.md) | `models/SWAN/source-analysis/swan-schemes-implementation.md:6–7, 18, 38, 82, 99, 104, 141, 144, 148, 168–185` | GSE의 격자별 경로. 회절의 BSBT 덮어쓰기 조건. 모드 불일치 오류. 차이 표. |
| [swan-time-stepping-implementation.md](../../../models/SWAN/source-analysis/swan-time-stepping-implementation.md) | `models/SWAN/source-analysis/swan-time-stepping-implementation.md:6–7, 66, 69, 132, 139–141, 158–171` | AC1 소비 위치. DELTC 입력. HOTSTART 시각 조건. 차이 표. |
| [swan-unstructured-time-step.md](../../../models/SWAN/source-analysis/swan-unstructured-time-step.md) | `models/SWAN/source-analysis/swan-unstructured-time-step.md:6–7, 55, 85, 95, 98, 103–104, 107, 113, 126–134, 137, 139–140, 142, 144–145, 150–170` | AC2 차원. nsweep 선택. 반복별 sweep 수 감소. GRAPH·FIXFRONT. 수송 조립 계층. 차이 표. |
| [swan-stationary-vs-nonstationary.md](../../../models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md) | `models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md:6–7, 66, 147, 149, 171, 182, 184, 214–225` | 정상·비정상 기본 기법. AC1 할당·복사 조건. TMREL 후보 연결. 적용 권고 구분. 차이 표. |
| [swan-data-structures-implementation.md](../../../models/SWAN/source-analysis/swan-data-structures-implementation.md) | `models/SWAN/source-analysis/swan-data-structures-implementation.md:6–7, 33, 37, 70, 105, 112, 114, 119, 146–159` | AC1 할당·복사. JCOMPDA. 기억 배열 초기화. OpenMP 저장소. 해법별 초기화. 차이 표. |
| [swan-parallel-implementation.md](../../../models/SWAN/source-analysis/swan-parallel-implementation.md) | `models/SWAN/source-analysis/swan-parallel-implementation.md:6–7, 18, 50, 91, 118, 120, 179–184, 190–191, 198, 225–249` | halo 선택. MPI wrapper 범위. MPI·OpenMP 빌드 선택. 실행 예시. METIS 경로. 차이 표. |
| [swan-source-coverage-audit.md](../../../models/SWAN/source-analysis/swan-source-coverage-audit.md) | `models/SWAN/source-analysis/swan-source-coverage-audit.md:6–7, 27, 38–41, 107–124, 144, 157, 170, 184, 200, 206, 210, 229, 240, 243, 251–258, 276–277, 279, 283–284, 286, 289–298` | SwanThreadBounds 삭제 기록 유지. 구판 목록 연결. 현재 front 순회. 차이 표. |

## 반영한 행 ID

### 본문 수정·유지와 호출 근거

아래 행은 담당 노트의 기존 문장 정정과 유지에 사용했다. R1:TN-036, R7:I-035, R8:V12와 R8:V25는 본문 연결에 옮긴 원문 근거이다.

| 보고서 | 행 ID |
|---|---|
| R1 | R1:TN-036, R1:TN-040, R1:TN-046, R1:TN-073, R1:TN-077, R1:TN-080, R1:TN-081, R1:TN-082, R1:TN-088, R1:TN-169, R1:TN-175, R1:TN-176, R1:TN-181, R1:TN-184, R1:TN-185, R1:TN-190, R1:TN-193, R1:TN-203, R1:TN-204, R1:TN-218, R1:TC-008, R1:TC-019, R1:TC-020 |
| R3 | R3:NT-048 |
| R5 | R5:PN-085, R5:PN-176, R5:PN-180, R5:PN-186, R5:PN-187 |
| R7 | R7:I-035, R7:N-027, R7:N-028, R7:N-029, R7:N-032 |
| R8 | R8:N1-001, R8:N1-002, R8:N1-003, R8:N1-004, R8:N1-005, R8:N1-006, R8:N1-007, R8:N1-008, R8:N1-013, R8:N1-014, R8:T1-002, R8:T1-003, R8:T1-004, R8:T1-006, R8:T1-007, R8:T1-014, R8:T1-015, R8:V12, R8:V25 |

R8 §6의 시간 반복 `DO 500 IT = IT0, MTC` 서술을 유지했다. R8 §6의 출력 조건 `OUTR(2) > 0` 및 `TIMCO >= TNEXT` 서술을 유지했다. R3:NT-048의 회절 서술을 유지하고 IDIFFR 조건을 덧붙였다. R7:N-032의 삭제 기록을 유지하고 구현 매뉴얼의 구판 목록을 연결했다.

### 문서와 코드 차이 표

아래 목록은 담당 노트의 차이 표에서 반영한 행 ID를 모은 것이다. 차이 표의 행 수는 아래 목록을 보고서별 행 ID로 센 97행이다.

| 보고서 | 행 ID |
|---|---|
| R1 | R1:TN-003, R1:TN-044, R1:TN-045, R1:TN-058, R1:TN-059, R1:TN-063, R1:TN-073, R1:TN-074, R1:TN-075, R1:TN-077, R1:TN-080, R1:TN-081, R1:TN-082, R1:TN-087, R1:TN-088, R1:TN-171, R1:TN-172, R1:TN-173, R1:TN-174, R1:TN-175, R1:TN-176, R1:TN-178, R1:TN-183, R1:TN-185, R1:TN-190, R1:TN-203, R1:TN-204, R1:TC-001, R1:TC-002, R1:TC-003, R1:TC-004, R1:TC-005, R1:TC-006, R1:TC-007, R1:TC-016, R1:TC-018, R1:TC-019, R1:TC-020, R1:TC-021, R1:TC-022, R1:TC-024, R1:TC-025 |
| R4 | R4:T1-013, R4:T1-039, R4:T1-066, R4:T1-303 |
| R5 | R5:PN-081, R5:PN-083, R5:PN-084, R5:PN-087, R5:PN-090, R5:PN-093, R5:PN-098, R5:PN-099, R5:PN-151, R5:PN-155, R5:PN-173, R5:PN-174, R5:PN-180, R5:PN-187 |
| R7 | R7:I-049, R7:I-053, R7:I-057, R7:I-059, R7:C-002, R7:C-003, R7:C-004, R7:C-013, R7:C-014, R7:C-017, R7:C-020, R7:N-002, R7:N-027, R7:N-028, R7:N-029 |
| R8 | R8:T1-001, R8:T1-002, R8:T1-003, R8:T1-004, R8:T1-005, R8:T1-006, R8:T1-007, R8:T1-009, R8:T1-010, R8:T1-013, R8:T1-014, R8:T1-015, R8:N1-001, R8:N1-002, R8:N1-003, R8:N1-004, R8:N1-005, R8:N1-006, R8:N1-007, R8:N1-008, R8:N1-013, R8:N1-014 |

### 코드 결함 후보 대표 표

대표 표는 [swan-foundation.md](../../../models/SWAN/source-analysis/swan-foundation.md)의 `models/SWAN/source-analysis/swan-foundation.md:373–411`에 있다. 표의 39행은 R1–R7 §5와 R8 §8에서 최종 결론이 E인 보고서별 행 ID를 센 값이다. 같은 원인의 행도 보고서별로 보존했다.

| 보고서 | E 행 ID |
|---|---|
| R1 | R1:TN-076, R1:TN-162, R1:TN-163, R1:TN-165, R1:TC-010, R1:TC-011, R1:TC-023 |
| R2 | R2:SS-089, R2:SS-516 |
| R3 | R3:QC-086, R3:BC-005, R3:CP-003, R3:CP-004, R3:CP-007, R3:CP-012, R3:CP-013, R3:CP-014, R3:CP-015 |
| R4 | R4:T1-011, R4:T1-097, R4:T1-174, R4:T1-182, R4:T1-194 |
| R5 | R5:PN-061, R5:PN-085, R5:PN-127, R5:PN-128 |
| R6 | R6:O-012, R6:O-052, R6:O-063, R6:O-077, R6:O-099, R6:O-110, R6:O-112, R6:O-138, R6:O-139, R6:O-140 |
| R7 | R7:H-1162e |
| R8 | R8:T1-011 |

### 계산 흐름 원문

[swan-foundation.md](../../../models/SWAN/source-analysis/swan-foundation.md)의 `models/SWAN/source-analysis/swan-foundation.md:227–365`에 R8 §4.1·§4.2·§4.3 Mermaid 원문을 옮겼다. 각 그림에 한 문장 설명과 R8 상대 링크를 붙였다. 상자 문자열과 file:line은 R8 원문과 같다.

## 다른 작업 담당

### 담당 노트 밖의 일반 차이 행

아래 행은 행의 문서 근거·주제에 가까운 노트가 이번 담당 목록 밖에 있다. 이 목록은 R1–R7 §5와 R8 §8의 최종 차이 행에서 E 행·일치 행·위 차이 표의 97행을 제외해 만들었다.

| 보고서 | 다른 작업 담당 행 ID | 주제별 담당 노트 |
|---|---|---|
| R1 | R1:TN-001, R1:TN-004, R1:TN-005, R1:TN-006, R1:TN-008, R1:TN-017, R1:TN-021, R1:TN-023, R1:TN-026, R1:TN-027, R1:TN-028, R1:TN-031, R1:TN-034, R1:TN-055, R1:TN-056, R1:TN-057, R1:TN-066, R1:TN-068, R1:TN-070, R1:TN-078, R1:TN-085, R1:TN-089, R1:TN-094, R1:TN-095, R1:TN-096, R1:TN-098, R1:TN-099, R1:TN-100, R1:TN-101, R1:TN-102, R1:TN-104, R1:TN-106, R1:TN-107, R1:TN-108, R1:TN-112, R1:TN-115, R1:TN-116, R1:TN-117, R1:TN-118, R1:TN-120, R1:TN-121, R1:TN-122, R1:TN-123, R1:TN-127, R1:TN-134, R1:TN-138, R1:TN-139, R1:TN-140, R1:TN-145, R1:TN-147, R1:TN-148, R1:TN-153, R1:TN-156, R1:TN-158, R1:TN-161, R1:TN-164, R1:TN-166, R1:TN-168, R1:TN-186, R1:TN-187, R1:TN-188, R1:TN-191, R1:TN-194, R1:TN-201, R1:TN-211, R1:TN-218, R1:TN-220, R1:TN-222, R1:TN-223, R1:TN-224, R1:TC-008, R1:TC-009, R1:TC-012, R1:TC-013, R1:TC-014, R1:TC-015 | 지배식·이론 유도·QC·장애물·스펙트럼 보간·GSE의 manual-notes와 개별 source-analysis 노트. |
| R2 | R2:SS-036, R2:SS-038, R2:SS-039, R2:SS-201, R2:SS-049, R2:SS-051, R2:SS-055, R2:SS-056, R2:SS-057, R2:SS-204, R2:SS-205, R2:SS-210, R2:SS-067, R2:SS-212, R2:SS-214, R2:SS-077, R2:SS-084, R2:SS-088, R2:SS-215, R2:SS-216, R2:SS-217, R2:SS-361, R2:SS-362, R2:SS-363, R2:SS-231, R2:SS-232, R2:SS-090, R2:SS-091, R2:SS-233, R2:SS-234, R2:SS-235, R2:SS-093, R2:SS-236, R2:SS-094, R2:SS-095, R2:SS-100, R2:SS-219, R2:SS-220, R2:SS-106, R2:SS-107, R2:SS-108, R2:SS-222, R2:SS-109, R2:SS-112, R2:SS-113, R2:SS-115, R2:SS-116, R2:SS-270, R2:SS-274, R2:SS-287, R2:SS-118, R2:SS-119, R2:SS-121, R2:SS-126, R2:SS-127, R2:SS-129, R2:SS-501, R2:SS-502, R2:SS-503, R2:SS-504, R2:SS-506, R2:SS-507, R2:SS-508, R2:SS-509, R2:SS-510, R2:SS-511, R2:SS-512, R2:SS-513, R2:SS-514, R2:SS-515, R2:SS-517, R2:SS-518, R2:SS-519, R2:SS-520, R2:SS-521, R2:SS-522, R2:SS-523, R2:SS-524, R2:SS-525, R2:SS-526, R2:SS-527, R2:SS-528, R2:SS-529, R2:SS-530, R2:SS-531, R2:SS-532, R2:SS-533, R2:SS-534, R2:SS-535, R2:SS-536, R2:SS-537, R2:SS-538, R2:SS-539, R2:SS-540, R2:SS-701, R2:SS-702, R2:SS-703, R2:SS-704, R2:SS-705, R2:SS-706, R2:SS-707, R2:SS-708, R2:SS-709, R2:SS-710, R2:SS-711, R2:SS-712, R2:SS-713, R2:SS-714, R2:SS-715, R2:SS-716, R2:SS-717, R2:SS-718, R2:SS-719, R2:SS-720, R2:SS-721, R2:SS-722, R2:SS-723, R2:SS-724, R2:SS-725, R2:SS-726, R2:SS-727, R2:SS-728, R2:SS-729, R2:SS-730, R2:SS-731, R2:SS-733, R2:SS-734, R2:SS-735, R2:SS-736, R2:SS-737, R2:SS-738, R2:SS-739, R2:SS-740, R2:SS-741, R2:SS-742, R2:SS-743 | 원천항의 manual-notes와 바람·백파·ST6·XNL·Bragg·원천항 조립 source-analysis 노트. |
| R3 | R3:OQ-003, R3:OQ-006, R3:OQ-009, R3:OQ-013, R3:OQ-014, R3:OQ-015, R3:OQ-017, R3:OQ-018, R3:OQ-019, R3:OQ-020, R3:OQ-022, R3:OQ-023, R3:OQ-024, R3:OQ-025, R3:OQ-027, R3:OQ-029, R3:OQ-030, R3:SU-001, R3:SU-002, R3:SU-003, R3:SU-004, R3:SU-005, R3:SU-006, R3:SU-007, R3:SU-008, R3:SU-009, R3:SU-010, R3:SU-011, R3:SU-012, R3:SU-013, R3:SU-014, R3:SU-015, R3:SU-016, R3:SU-019, R3:SU-020, R3:SU-021, R3:SU-024, R3:SU-026, R3:SU-027, R3:SU-028, R3:SU-029, R3:SU-030, R3:SU-031, R3:SU-032, R3:SU-033, R3:SU-035, R3:SU-037, R3:SU-038, R3:SU-041, R3:QC-001, R3:QC-002, R3:QC-003, R3:QC-004, R3:QC-005, R3:QC-006, R3:QC-007, R3:QC-008, R3:QC-009, R3:QC-010, R3:QC-011, R3:QC-012, R3:QC-013, R3:QC-014, R3:QC-015, R3:QC-016, R3:QC-017, R3:QC-018, R3:QC-019, R3:QC-020, R3:QC-022, R3:QC-023, R3:QC-024, R3:QC-025, R3:QC-026, R3:QC-027, R3:QC-028, R3:QC-029, R3:QC-030, R3:QC-031, R3:QC-032, R3:QC-033, R3:QC-034, R3:QC-035, R3:QC-036, R3:QC-037, R3:QC-038, R3:QC-039, R3:QC-040, R3:QC-041, R3:QC-042, R3:QC-044, R3:QC-045, R3:QC-046, R3:QC-047, R3:QC-048, R3:QC-049, R3:QC-050, R3:QC-051, R3:QC-052, R3:QC-053, R3:QC-054, R3:QC-055, R3:QC-056, R3:QC-057, R3:QC-058, R3:QC-059, R3:QC-060, R3:QC-061, R3:QC-063, R3:QC-064, R3:QC-065, R3:QC-066, R3:QC-067, R3:QC-068, R3:QC-069, R3:QC-073, R3:QC-074, R3:QC-075, R3:QC-076, R3:QC-078, R3:QC-079, R3:QC-080, R3:QC-081, R3:QC-082, R3:QC-083, R3:QC-087, R3:QC-089, R3:BC-006, R3:BC-007, R3:BC-011, R3:BC-013, R3:BC-014, R3:BC-015, R3:SU-042, R3:CP-001, R3:CP-002, R3:CP-005, R3:CP-006, R3:CP-008, R3:CP-010, R3:CP-011, R3:CP-016, R3:CP-017, R3:CP-018, R3:CP-019, R3:CP-020, R3:CP-021, R3:CP-023, R3:CP-024, R3:CP-025, R3:CP-026, R3:CP-028, R3:CP-029, R3:CP-030, R3:CP-031, R3:NT-001, R3:NT-002, R3:NT-003, R3:NT-004, R3:NT-005, R3:NT-006, R3:NT-007, R3:NT-008, R3:NT-009, R3:NT-010, R3:NT-011, R3:NT-012, R3:NT-013, R3:NT-014, R3:NT-015, R3:NT-016, R3:NT-017, R3:NT-018, R3:NT-019, R3:NT-020, R3:NT-021, R3:NT-022, R3:NT-023, R3:NT-024, R3:NT-025, R3:NT-026, R3:NT-027, R3:NT-028, R3:NT-029, R3:NT-030, R3:NT-031, R3:NT-032, R3:NT-033, R3:NT-034, R3:NT-035, R3:NT-036, R3:NT-037, R3:NT-038, R3:NT-039, R3:NT-040, R3:NT-041, R3:NT-042, R3:NT-043, R3:NT-044, R3:NT-045, R3:NT-046, R3:NT-047, R3:NT-049, R3:NT-052 | 장애물·회절·set-up·QC·경계·초기 조건의 manual-notes와 개별 source-analysis 노트. |
| R4 | R4:T1-001, R4:T1-003, R4:T1-004, R4:T1-005, R4:T1-006, R4:T1-007, R4:T1-009, R4:T1-012, R4:T1-014, R4:T1-015, R4:T1-018, R4:T1-020, R4:T1-024, R4:T1-037, R4:T1-038, R4:T1-050, R4:T1-054, R4:T1-055, R4:T1-058, R4:T1-060, R4:T1-061, R4:T1-062, R4:T1-084, R4:T1-085, R4:T1-088, R4:T1-089, R4:T1-095, R4:T1-096, R4:T1-136, R4:T1-137, R4:T1-144, R4:T1-147, R4:T1-175, R4:T1-176, R4:T1-185, R4:T1-187, R4:T1-191, R4:T1-192, R4:T1-220, R4:T1-221, R4:T1-222, R4:T1-223, R4:T1-224, R4:T1-225, R4:T1-226, R4:T1-227, R4:T1-228, R4:T1-229, R4:T1-230, R4:T1-231, R4:T1-232, R4:T1-233, R4:T1-234, R4:T1-235, R4:T1-236, R4:T1-237, R4:T1-238, R4:T1-239, R4:T1-240, R4:T1-241, R4:T1-250, R4:T1-251, R4:T1-252, R4:T1-253, R4:T1-254, R4:T1-300, R4:T1-301, R4:T1-302, R4:T1-304, R4:T1-305, R4:T1-306, R4:T1-307, R4:T1-308, R4:T1-309, R4:T1-310, R4:T1-311, R4:T1-312, R4:T1-313 | 사용·명령·격자·경계·초기 조건의 manual-notes와 명령 파일·격자 리더·경계 source-analysis 노트. |
| R5 | R5:PN-003, R5:PN-008, R5:PN-011, R5:PN-012, R5:PN-014, R5:PN-015, R5:PN-016, R5:PN-018, R5:PN-021, R5:PN-024, R5:PN-025, R5:PN-032, R5:PN-038, R5:PN-041, R5:PN-042, R5:PN-045, R5:PN-046, R5:PN-048, R5:PN-051, R5:PN-052, R5:PN-053, R5:PN-058, R5:PN-059, R5:PN-060, R5:PN-064, R5:PN-065, R5:PN-066, R5:PN-068, R5:PN-070, R5:PN-072, R5:PN-074, R5:PN-075, R5:PN-078, R5:PN-192, R5:PN-082, R5:PN-092, R5:PN-095, R5:PN-101, R5:PN-102, R5:PN-104, R5:PN-106, R5:PN-110, R5:PN-116, R5:PN-118, R5:PN-120, R5:PN-121, R5:PN-123, R5:PN-125, R5:PN-126, R5:PN-129, R5:PN-131, R5:PN-134, R5:PN-137, R5:PN-142, R5:PN-143, R5:PN-144, R5:PN-145, R5:PN-146, R5:PN-147, R5:PN-148, R5:PN-149, R5:PN-150, R5:PN-152, R5:PN-153, R5:PN-154, R5:PN-156, R5:PN-157, R5:PN-158, R5:PN-159, R5:PN-160, R5:PN-161, R5:PN-162, R5:PN-163, R5:PN-164, R5:PN-165, R5:PN-166, R5:PN-167, R5:PN-168, R5:PN-169, R5:PN-170, R5:PN-171, R5:PN-172, R5:PN-175, R5:PN-189, R5:PN-190, R5:PN-191, R5:PN-176, R5:PN-177, R5:PN-178, R5:PN-179, R5:PN-181, R5:PN-182, R5:PN-183, R5:PN-184, R5:PN-185, R5:PN-186, R5:PN-188 | 물리 명령·수치 명령·출력 정의의 manual-notes와 관련 물리·명령 source-analysis 노트. |
| R6 | R6:O-002, R6:O-010, R6:O-011, R6:O-014, R6:O-015, R6:O-017, R6:O-018, R6:O-020, R6:O-022, R6:O-024, R6:O-025, R6:O-028, R6:O-029, R6:O-031, R6:O-032, R6:O-033, R6:O-034, R6:O-036, R6:O-045, R6:O-046, R6:O-049, R6:O-050, R6:O-051, R6:O-055, R6:O-056, R6:O-058, R6:O-059, R6:O-061, R6:O-067, R6:O-073, R6:O-074, R6:O-075, R6:O-076, R6:O-085, R6:O-086, R6:O-090, R6:O-091, R6:O-093, R6:O-097, R6:O-098, R6:O-104, R6:O-105, R6:O-106, R6:O-107, R6:O-108, R6:O-111, R6:O-113, R6:O-114, R6:O-116, R6:O-118, R6:O-119, R6:O-120, R6:O-121, R6:O-122, R6:O-123, R6:O-124, R6:O-125, R6:O-126, R6:O-127, R6:O-128, R6:O-129, R6:O-130, R6:O-131, R6:O-132, R6:O-133, R6:O-134, R6:O-135, R6:O-136, R6:O-137, R6:N-001, R6:N-002, R6:N-003, R6:N-004, R6:N-005, R6:N-006, R6:N-007, R6:N-008, R6:N-009, R6:N-010, R6:N-011, R6:N-012, R6:N-013, R6:N-014, R6:N-015, R6:N-016, R6:N-017, R6:N-018, R6:N-019, R6:N-020, R6:N-021, R6:N-022 | 출력 명령·물리량·스펙트럼 형식의 manual-notes와 출력·중첩·VTK source-analysis 노트. |
| R7 | R7:I-003, R7:I-008, R7:I-013, R7:I-015, R7:I-016, R7:I-022, R7:I-024, R7:I-025, R7:I-029, R7:I-030, R7:I-032, R7:I-033, R7:I-043, R7:I-045, R7:I-048, R7:I-052, R7:I-056, R7:I-058, R7:R-003, R7:R-006, R7:R-007, R7:R-010, R7:P-001, R7:P-002, R7:P-003, R7:P-006, R7:P-007, R7:P-008, R7:P-009, R7:P-010, R7:P-011, R7:P-012, R7:P-013, R7:P-014, R7:P-015, R7:P-016, R7:P-017, R7:P-018, R7:P-019, R7:P-021, R7:P-023, R7:P-024, R7:P-025, R7:P-026, R7:P-027, R7:P-028, R7:P-029, R7:P-030, R7:P-031, R7:P-033, R7:P-034, R7:P-035, R7:P-036, R7:P-037, R7:P-039, R7:P-040, R7:P-041, R7:P-042, R7:P-043, R7:P-044, R7:P-045, R7:P-046, R7:P-047, R7:P-048, R7:P-049, R7:P-050, R7:P-051, R7:P-052, R7:P-053, R7:P-054, R7:P-055, R7:Q-002, R7:Q-005, R7:Q-007, R7:Q-008, R7:Q-018, R7:ED-040, R7:ED-043, R7:ED-044, R7:ED-045, R7:ED-046, R7:ED-051, R7:ED-052, R7:H-47p, R7:H-112, R7:H-131, R7:H-133p, R7:H-139, R7:H-170p, R7:H-195, R7:H-202, R7:H-213p, R7:H-219, R7:H-219p, R7:H-228p, R7:H-291, R7:H-306, R7:H-326, R7:H-333, R7:H-336p, R7:H-374p, R7:H-472, R7:H-480p, R7:H-492, R7:H-501, R7:H-529, R7:H-531, R7:H-532, R7:H-534, R7:H-538, R7:H-566, R7:H-583, R7:H-587, R7:H-589, R7:H-591, R7:H-599, R7:H-601, R7:H-686, R7:H-695, R7:H-749, R7:H-755, R7:H-778, R7:H-789, R7:H-813, R7:H-837, R7:H-840, R7:H-846, R7:H-849, R7:H-852, R7:H-855, R7:H-858, R7:H-861, R7:H-864, R7:H-867, R7:H-870, R7:H-873, R7:H-890, R7:H-894, R7:H-903, R7:H-910, R7:H-913, R7:H-921, R7:H-936, R7:H-940, R7:H-944, R7:H-945, R7:H-949p, R7:H-955, R7:H-959, R7:H-961, R7:H-966, R7:H-968, R7:H-979, R7:H-1006, R7:H-1056, R7:H-1081, R7:H-1088, R7:H-1097, R7:H-1121, R7:H-1123, R7:H-1124, R7:H-1128, R7:H-1134, R7:H-1149, R7:H-1150, R7:H-1151, R7:H-1170, R7:H-1174, R7:H-1180, R7:H-1182, R7:H-1183, R7:H-1197, R7:H-1204, R7:H-1205, R7:H-1208, R7:H-1212, R7:H-1214, R7:H-1215, R7:H-1227, R7:H-1228, R7:H-1229, R7:H-1234, R7:H-1240, R7:H-1242, R7:H-1257, R7:H-1263, R7:H-1268, R7:H-1273, R7:H-1274, R7:H-1275, R7:H-1305, R7:H-1319, R7:H-1331, R7:H-1336, R7:H-1337, R7:H-1346, R7:H-1350, R7:H-1354, R7:H-1358, R7:H-1360, R7:H-1371, R7:H-1373, R7:H-1375, R7:H-1386, R7:H-1388, R7:H-1389, R7:H-1390, R7:H-1397, R7:H-1398, R7:H-1399, R7:H-1418, R7:H-1419, R7:H-1447, R7:H-1455, R7:H-1464, R7:H-1480, R7:H-1482, R7:H-1504, R7:H-1514, R7:H-1531, R7:H-1547, R7:H-1596, R7:H-1603, R7:H-1611, R7:H-1620, R7:H-1638, R7:F-010, R7:D-002, R7:D-003, R7:D-005, R7:D-007, R7:D-008, R7:D-009, R7:D-010, R7:D-011, R7:D-012, R7:S-001, R7:S-002, R7:S-003, R7:S-006, R7:S-012, R7:S-016, R7:S-018, R7:S-019, R7:S-056, R7:C-001, R7:C-005, R7:C-006, R7:C-007, R7:C-008, R7:C-009, R7:C-010, R7:C-011, R7:C-012, R7:C-015, R7:C-016, R7:C-019, R7:C-021, R7:C-023, R7:C-024, R7:C-025, R7:C-026, R7:C-028, R7:N-001, R7:N-003, R7:N-005, R7:N-006, R7:N-007, R7:N-008, R7:N-009, R7:N-010, R7:N-011, R7:N-012, R7:N-013, R7:N-014, R7:N-015, R7:N-016, R7:N-017, R7:N-018, R7:N-019, R7:N-020, R7:N-021, R7:N-022, R7:N-023, R7:N-024, R7:N-025, R7:N-026, R7:N-030, R7:N-031, R7:N-033, R7:N-035 | 구현 매뉴얼·프로그래밍 규칙·문서 판·웹 수정 이력·패치·개별 물리 구현 노트. |
| R8 | R8:T1-008, R8:T1-012, R8:N1-009, R8:N1-010, R8:N1-011, R8:N1-012 | DIA·제한기·곡률 식·명령 매핑·출력 writer의 해당 주제 노트. |

R5:PN-176의 SET TIMINC·SET TIMEFORMAT 수정은 담당 시간 전진 노트에 반영했다. 같은 행의 ST6·TRIAD·XNL·MDIA 문법과 차이 표는 해당 물리·명령 노트 담당이다. R5:PN-186의 반복 횟수 축소 권고는 담당 정상·비정상 노트에 반영했다. 같은 행의 백파·준비 시간·회절 권고와 차이 표는 해당 주제 노트 담당이다. R7:N-034가 가리키는 모델 README 줄은 다른 작업 담당이다.

### E 행의 주제별 차이 표

이 작업은 E 행의 대표 표를 맡았다. E 행의 주제별 차이 표는 아래 담당으로 넘겼다. 대표 표에 반영한 사실과 주제별 차이 표 담당을 구별한다.

| E 행 ID | 주제별 차이 표 담당 |
|---|---|
| R1:TN-076, R5:PN-085, R8:T1-011 | [swan-tech-ch3-solution-iteration-limiter.md](../../../models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md) |
| R1:TN-162, R1:TN-163, R1:TN-165, R1:TC-010, R1:TC-011 | [swan-tech-ch3-obstacles-spectral-ops.md](../../../models/SWAN/manual-notes/swan-tech-ch3-obstacles-spectral-ops.md) |
| R1:TC-023 | [swan-propagation-implementation.md](../../../models/SWAN/source-analysis/swan-propagation-implementation.md) |
| R2:SS-089, R2:SS-516 | [swan-xnl4-exact-quadruplet.md](../../../models/SWAN/source-analysis/swan-xnl4-exact-quadruplet.md) |
| R3:QC-086, R3:CP-012, R3:CP-013, R3:CP-014, R3:CP-015 | [swan-quasi-coherent.md](../../../models/SWAN/source-analysis/swan-quasi-coherent.md) |
| R3:BC-005 | [swan-tech-ch4-5-bc-2d-setup.md](../../../models/SWAN/manual-notes/swan-tech-ch4-5-bc-2d-setup.md) |
| R3:CP-003, R3:CP-004, R3:CP-007, R5:PN-061 | [swan-diffraction-obstacles.md](../../../models/SWAN/source-analysis/swan-diffraction-obstacles.md) |
| R4:T1-011 | [swan-time-stepping-implementation.md](../../../models/SWAN/source-analysis/swan-time-stepping-implementation.md) |
| R4:T1-097 | [swan-command-setup-grid-reference.md](../../../models/SWAN/manual-notes/swan-command-setup-grid-reference.md) |
| R4:T1-174, R4:T1-182 | [swan-boundary-implementation.md](../../../models/SWAN/source-analysis/swan-boundary-implementation.md) |
| R4:T1-194 | [swan-main-boundary-init-sourcemap.md](../../../models/SWAN/source-analysis/swan-main-boundary-init-sourcemap.md) |
| R5:PN-127, R5:PN-128, R6:O-052, R6:O-063, R6:O-077, R6:O-099, R6:O-138, R6:O-139 | [swan-output-variable-definitions.md](../../../models/SWAN/manual-notes/swan-output-variable-definitions.md) |
| R6:O-012 | [swan-nesting-io-implementation.md](../../../models/SWAN/source-analysis/swan-nesting-io-implementation.md) |
| R6:O-110 | [swan-output-formats.md](../../../models/SWAN/source-analysis/swan-output-formats.md) |
| R6:O-112, R6:O-140 | [swan-output-writers-implementation.md](../../../models/SWAN/source-analysis/swan-output-writers-implementation.md) |
| R7:H-1162e | [swan-wind-formulations-implementation.md](../../../models/SWAN/source-analysis/swan-wind-formulations-implementation.md) |

## 담당 범위의 미반영 행

없음. 담당 노트를 가리키는 수정안은 본문에 반영했다. 담당 노트에 배정한 일반 차이 행은 차이 표에 반영했다. 최종 E 행은 대표 표에 반영했다. E 행의 주제별 차이 표는 위 인계 목록의 담당이다.

## 반영 확인

담당 노트의 차이 표 행 ID는 위 배정 목록과 일치한다. E 대표 표 행 ID는 R1–R7 §5와 R8 §8의 최종 E 목록과 일치한다. 차이 표에는 일치 행을 넣지 않았다. A 행의 결론 문장에는 변경 커밋과 날짜가 있다.

각 노트의 citation_status를 유지했다. 각 노트의 last_source_check는 `2026-10-13 (recovery 대조 반영)`이다. 각 노트의 verification_method에 `2026-10-13 recovery 대조 보고서 R1–R8 반영`을 덧붙였다.

Mermaid 원문 3개는 R8 §4 원문과 문자 단위로 일치한다. Mermaid·jsdom SVG 렌더링의 상자 수는 각각 29개·30개·28개이다. 상자 수는 렌더링한 SVG의 `g.node` 요소를 센 값이다. 렌더링의 문자 폭은 근사 측정값을 사용했다.

상대 링크의 대상 파일은 존재한다. 담당 노트와 이 문서에는 개인 절대 경로와 이중 대괄호 표기가 없다. 소스 인벤토리의 `.ftn90` 57개와 `.ftn` 18개는 `models/SWAN/raw/source_code/swan/src/`의 `*.ftn90`과 `*.ftn` glob을 각각 세어 대조했다.

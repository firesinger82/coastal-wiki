---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/mod_Variables_MPI_Mapping.f90
lines: 177
sha256: 8173377a1fe9c2947b63ea179f22be7b88293a188d7bf428cc8907862fb779ad
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_Variables_MPI_Mapping.f90 — 판독 구간 기록

구간은 1행부터 177행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | EFDC+ 표제·저작권·GPLv2·개발사 안내(1–11). 경계 조건(boundary conditions)과 기타 매핑(mapping)용 전역(global) 배열 설명·저자·2019-11-01 날짜(12–16). Variables_MPI_Mapping 모듈 시작·implicit none·빈 줄(17–20). |
| 21–39 | 시작 시 17행 Variables_MPI_Mapping 선언부 안. IL_Global/JL_Global은 주석상 지역(local) L 기반 전역 I/J, IL_GL/JL_GL은 전역 L 기반 전역 I/J의 1차원 정수 배열이다(21–24). La_local_no_ghost·num_active_l_local 정수(26·28). Save NNoGhost 정수와 NoGhost 1차원 정수, IsGhost 논리, GhostMask 기본 Real 배열 선언(30–33). NoGhost 주석은 유령 셀(ghost cells)을 제외한 활성 셀이라고 적는다(31). 서·동 연결용 lij_west/east_conn_outside 1차원 정수 배열과 offset_connectors_for_ns 정수 선언(35–38). |
| 40–58 | 시작 시 17행 Variables_MPI_Mapping 선언부 안. mapping_ij 형식(type)은 process/local_i/local_j/global_i/global_j/local_l/global_l 정수 필드를 가진다(40–49). 같은 형식의 1차원 allocatable loc_to_glob·all_loc_to_glob·active_loc_to_glob·sorted_loc_to_glob를 선언한다(51–54). 주석은 각각 지역 대응·비활성 셀까지의 전체 대응·활성 셀 대응·전역 L로 인덱싱하는 정렬 대응을 적는다. GWCSER_Global은 기본 Real 3차원 지하수 농도 시계열(groundwater concentration series) 배열, NGWSL_Global은 정수 1차원이다(56–57). |
| 59–100 | 시작 시 17행 Variables_MPI_Mapping 선언부 안. “Global periodic boundary conditions” 주석이 두 번 나온다(59·65). NPBW/NPBE/NPBN/NPBS_GL 스칼라 정수 선언(60–63). IPB/JPB/LPB/ISPB의 S/W/E/N 접미사 그룹을 각각 1차원 allocatable 정수 배열로 선언한다(66–84). ISPR의 S/W/E/N 그룹(86–89), NPSER의 S/W/E/N 그룹(91–94), NPSER에 1을 붙인 S1/W1/E1/N1 그룹(96–99)도 같은 자료형·차원이다. 빈 줄 포함. |
| 101–117 | 시작 시 17행 Variables_MPI_Mapping 선언부 안. 지역값은 Map_OpenBC_Pressure에서 매핑한다는 주석(101). PCB와 PSB의 E/N/S/W_GL 그룹은 2차원 allocatable 기본 real이다(102–110). TPCOORD의 S/W/E/N_GL 그룹은 1차원 allocatable 기본 real이다(112–115). End Map_OpenBC_Pressure 주석·빈 줄(116–117). 이 구간에는 해당 루틴 호출이 없다. |
| 118–143 | 시작 시 17행 Variables_MPI_Mapping 선언부 안. 농도(concentration) 전역 배열 주석(118). S/E/W/N 각 그룹의 ICB·JCB·NTSCR_GL은 1차원 정수, NCSER_GL은 2차원 정수 allocatable이다(119–137). CBS_GL/CBE_GL/CBW_GL/CBN_GL은 3차원 allocatable 기본 real이다(139–142). 빈 줄 포함. |
| 144–160 | 시작 시 17행 Variables_MPI_Mapping 선언부 안. 하천(river) 전역 배열 구역의 IQS_GL/JQS_GL/NQSMUL_GL/NQSMF_GL/NQSERQ_GL/NCSERQ_GL/GRPID_GL/LQS_GL와 QSSE_GL/QFACTOR_GL/QWIDTH_GL/CQSE_GL 선언은 모두 주석 처리되어 있다(144–159). JQS_GL 주석 끝에는 delme가 있다(146). 빈 줄 포함(154·160). |
| 161–177 | 시작 시 17행 Variables_MPI_Mapping 선언부 안. MLTMSR_GL 스칼라 정수(161). ILTMSR_GL/JLTMSR_GL/NTSSSS_GL/MTMSRP_GL/MTMSRC_GL/MTMSRA_GL/MTMSRUE_GL/MTMSRUT_GL/MTMSRU_GL/MTMSRQE_GL/MTMSRQ_GL/MLTM_GL은 1차원 allocatable 정수 배열이다(162–173). CLTMSR_GL은 요소 길이 20의 1차원 allocatable 문자열이다(175). 모듈 종료·빈 줄(174·176–177). 실행 루틴·조건·계산식은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46: global_j 필드는 주석상 전역 J이다. 같은 주석의 대응 지역 인덱스 설명은 “local I”라고 적혀 있다.


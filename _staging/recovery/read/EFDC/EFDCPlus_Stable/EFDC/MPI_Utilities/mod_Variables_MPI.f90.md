---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/mod_Variables_MPI.f90
lines: 197
sha256: c5e828bfa650660c0e9563a3051652305fa6f56aa5612a132fda9973e35f6bde
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_Variables_MPI.f90 — 판독 구간 기록

구간은 1행부터 197행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | EFDC+ 표제·저작권·GPLv2·개발사 안내(1–11). Variables_MPI 목적·저자·2019년 변수 이동·MPI 추가 이력(12–23). 모듈 시작·GLOBAL 사용·implicit none·빈 줄(25–30). |
| 31–59 | 시작 시 25행 Variables_MPI 선언부 안. 전역(global) I/J 시작 위치 ic_pos/jc_pos(31), 수집된 단계 수 nincrmt_reduce 및 초 단위 동적 시간 간격(dynamic timestep) dtdyn_reduce(33–34), 입력 프로세스(process) 수 NPFOR_Readin(36)을 선언한다. 3차원·1차원 수신 크기 recv_counts_3d/recv_counts_1d, 메시지 stride/send_size_1d(38–42). LA_global/LCM_Global/ICM_Global/JCM_Global, 부분 영역(subdomain)의 Start/End_Global_LA(45–51). 유령 셀(ghost cells) 시작·끝 위치 추적 배열 4개와 길이 12 filename_out(53–58). 빈 줄 포함. |
| 60–82 | 시작 시 25행 Variables_MPI 선언부 안. process_id·num_Processors 선언(60–61). 기본 master 값은 `integer :: master_id = 0              !< Defines the master node/process ID` (62)이다. 로그 이름 4개는 길이 24(64–67). 프로세스별 유닛(file unit)의 기준값은 `integer :: mpi_efdc_out_unit = 100    !< Unit so each process writes out its own EFDCLOG.OUT` (70), `integer :: mpi_log_unit = 200         !< General log unit` (71), `integer :: mpi_comm_unit = 300        !< MPI setup debug file for the communication of ghost cell values` (72), `integer :: mpi_mapping_unit = 400     !< Log of global to local cell mapping per process` (73), `integer :: mpi_qdwaste_unit = 800     !< QDWASTE log unit` (74), `integer :: mpi_error_unit = 900       !< Log of error messages per process` (75)이다. 두 진단 플래그(flag)의 기본값은 `logical :: MPI_DEBUG_FLAG = .FALSE.   !< Boolean that turns on some print statements for debugging MPI code. This flag should be an input option at some point.` (77), `logical :: MPI_Write_Flag = .FALSE.   !< Flag to enable MPI-specific diagnostic output` (78)이다. ScatterV/GatherV의 변위(displacement)·수신 수 배열 선언(80–81). |
| 83–113 | 시작 시 25행 Variables_MPI 선언부 안. 2요소 domain_coords/dimensions/is_periodic와 reorder·DSIcomm을 MPI 토폴로지(topology)용으로 선언한다(83–89). 표류체(drifter) 총수 NPD_TOT(91–92). 영역 분할(domain decomposition) 기본값은 `integer :: n_ghost_rows = 2             !< Number of ghost rows/cols on each side of domain` (95), `integer :: decomp_input_unit  = 123     !< unit for writing to DECOMP.inp` (96), `integer :: decomp_output_unit = 124     !< unit for writing to DECOMP.out` (97)이다. x/y 분할 수·활성 영역 수(99–101), 분할 폭/높이 배열·0 비활성/1 활성이라는 decomp_active 주석과 process_map 선언(103–106). IB/IE/JB/JE_Decomp 경계 배열과 지역 최대 폭 max_width_x/max_width_y(108–112). |
| 114–138 | 시작 시 25행 Variables_MPI 선언부 안. 전체 영역 ic_global/jc_global/lc_global와 카르테시안(Cartesian) 프로세스 좌표 x_id/y_id(114–119). 지역(local) I/J와 전역 I/J의 양방향 매핑(mapping) IL2IG/JL2JG/IG2IL/JG2JL(121–125). 전 프로세스 최대 폭 global_max_width_x/y(127–128). real(RKD) XCOR_Global/YCOR_Global은 주석상 m 또는 도(degrees), Area_Global은 m²이다(130–132). LWDIR_Global 3차원 인덱스, UMASK/VMASK_Global 1차원 정수, FWDIR_Global 2차원 real(RKD) 바람 취송거리(fetch length) 선언(134–137). |
| 139–176 | 시작 시 25행 Variables_MPI 선언부 안. mapping_lij 형식(type)은 정수 PR/IL/JL/LL/IG/JG/LG로 프로세스 번호와 지역·전역 I/J/L을 저장한다(139–148). 해당 형식의 1차원 할당 가능 Map2Global/Map2Local은 지역·전역 L 변환용이다(150–151). LIJ_Global/IJCT_GLOBAL/IJCTLT_GLOBAL 2차원 정수 배열(153–155). 네 방향 이웃 그림 주석(157–165), nbr_west/east/south/north(167–170), 인터페이스(interface) 목록 Comm_Cells 3차원과 개수 nComm_Cells 2차원(171–172). lmap·size_mpi 선언·빈 줄(174–176). |
| 177–197 | 시작 시 25행 Variables_MPI 선언부 안. “likely no longer needed” 주석이 작업 분배(task division) 변수 구역을 감싼다(177–193). num_task_per_process/lower_task_bound/upper_task_bound/num_elem_to_each_array와 new_three_dim_data_type 선언(180–184). 계산·broadcast·scatter·gather·caltran의 시작/끝/총시간은 Double Precision, Save 선언이다(186–191). DoublePrecision 논리 플래그 선언(195), 빈 줄·모듈 종료(194·196–197). 실행 루틴은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 69–78: MPI 로그 유닛 기준값과 두 진단 플래그 기본값을 모듈 선언에서 직접 설정한다. MPI_DEBUG_FLAG 주석은 향후 입력 옵션이어야 한다고 적는다(77).
- 95–97: 유령 행/열 수는 2이고 DECOMP.inp/out 유닛은 123/124로 선언 초기화한다.
- 140–148·186–191·195: mapping_lij의 정수 필드, Save 시간 변수와 DoublePrecision 선언에는 명시적 초기값이 없다. 외부 초기화 여부는 이 파일에서 확인할 수 없다.
- 178–193: 작업 분배·시간 변수 구역은 더 이상 필요하지 않을 수 있다는 주석을 갖는다. 변수 선언 자체는 주석 처리되어 있지 않다.


---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Communication/Mod_Gather_Drifter.f90
lines: 164
sha256: 0c79b0a37e3a97008e1a9f54a46e8fe4c03921ea50244d28e66a04db4f8bd736
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Gather_Drifter.f90 — 판독 구간 기록

구간은 1행부터 164행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | EFDC+ 소속·웹사이트·저장소·2021–2024 DSI 저작권·GNU GPLv2 머리말 및 DSI 개발 구분 주석(1–11). Mod_Gather_Drifter와 표류체(drifter) 정보 모으기(gather)의 모듈 설명, 작성자·날짜 주석(12–19), 빈 줄(20). |
| 21–52 | `Mod_Gather_Drifter` 모듈 시작(21). GLOBAL·Variables_MPI·Variables_MPI_Drifter·MPI 사용(23–26), implicit none·save(28·30). 공개 Gather_Drifter 제네릭 인터페이스(generic interface)는 Gather_Int_Drifter와 Gather_Real_Drifter_RK8을 등록한다(32–39). contains(41), DSI 개발·모듈 설명·작성자·날짜의 반복 주석(42–52). |
| 53–74 | 시작 시 21행 `Mod_Gather_Drifter` 모듈 안. `Gather_Int_Drifter(size_local_1d, Soln_Local_1D, size_global_1d, Soln_Global_1D)` 시작(53), implicit none(55). size_local_1d/size_global_1d는 정수 intent(in), 정수 로컬 배열은 intent(in), 정수 전역 배열은 intent(inout)이며 각각 해당 크기의 1차원 배열(58–61). 지역 정수 ierr/i와 allocatable 정수 displacements_index/recv_counts 선언(64–67). `If(.not.allocated(recv_counts) )then` (69)에서 두 배열을 active_domains 크기로 할당(70–71). 조건 종료(72), 1차원 배열의 활성 셀(active cell) 개수만 보내려는 주석·빈 줄(73–74). |
| 75–104 | 시작 시 21행 모듈·53행 `Gather_Int_Drifter` 안. `send_size_1d = size_local_1d` (75), recv_counts 전체 0 초기화(77). 메시지 전달 인터페이스(Message Passing Interface, MPI)의 전체 모으기(allgather) 호출 `call MPI_Allgather(send_size_1d,   1, MPI_Int, recv_counts, 1, MPI_Int, DSIcomm, ierr)` (80)은 DSIcomm의 각 프로세스 전송 개수 한 개를 recv_counts에 모은다. displacements_index(1)=0(83). `do i = 2, active_domains` (85)에서 변위(displacement)의 누적식은 `displacements_index(i) = displacements_index(i-1) + recv_counts(i-1)` (86). 가변 개수 모으기(gatherv) 호출은 `call MPI_Gatherv(Soln_Local_1D,  send_size_1d, MPI_Integer, &                         ! *** Send buff` (91), 계속행 `Soln_Global_1D, recv_counts,  displacements_index, MPI_Integer,   &  ! *** Recv buff` (92), `master_id, DSIcomm, ierr)` (93)이며 MPI_Integer 자료를 master_id에 모은다. `if(MPI_DEBUG_FLAG )then` (95)이면 active_domains/send_size_1d/recv_counts/displacements_index를 `(a,20i5)` 형식으로 기록(96–99). 조건 종료, 빈 줄, 루틴 종료(100–104). |
| 105–136 | 시작 시 21행 `Mod_Gather_Drifter` 모듈 안. DSI 개발·모듈 설명·작성자·날짜 반복 주석(105–115). `Gather_Real_Drifter_RK8(size_local_1d,  Soln_Local_1D, size_global_1d, Soln_Global_1D)` 시작(116), implicit none(118). size_local_1d/size_global_1d는 정수 intent(in), real(RKD) 로컬 배열은 intent(in), 전역 배열은 intent(inout)이며 각 크기의 1차원 배열(121–124). 지역 정수 ierr/i와 allocatable 정수 displacements_index/recv_counts 선언(127–130). `If(.not.allocated(recv_counts) )then` (132)에서 두 배열을 active_domains 크기로 할당(133–134). 조건 종료·빈 줄(135–136). |
| 137–164 | 시작 시 21행 모듈·116행 `Gather_Real_Drifter_RK8` 안. 표류체 개수만 보내려는 주석(137). `send_size_1d = size_local_1d` (138), recv_counts와 displacements_index 전체 0 초기화(140–141). `call MPI_Allgather(send_size_1d, 1, MPI_Int, recv_counts, 1, MPI_Int, DSIcomm, ierr)` (144)로 각 프로세스 전송 개수를 모은다. displacements_index(1)=0(147), `do i = 2, active_domains` (149)에서 `displacements_index(i) = displacements_index(i-1) + recv_counts(i-1)` (150). `if( MPI_DEBUG_FLAG )then` (153)이면 displacements_index를 `(a,3010i5)` 형식으로 기록(154). 가변 개수 모으기 호출은 `call MPI_Gatherv(Soln_Local_1D,  send_size_1d, mpi_real8, &                         ! *** Send buff` (158), 계속행 `Soln_Global_1D, recv_counts,  displacements_index, mpi_real8,   &  ! *** Recv buff` (159), `master_id, DSIcomm, ierr)` (160)이며 자료형 인수는 mpi_real8, 기준 프로세스는 master_id, 통신자(communicator)는 DSIcomm이다. 루틴 종료·빈 줄·모듈 종료(162–164). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 58–61·75–93·121–124·138–160: size_global_1d는 전역 배열 크기 선언에 사용된다. 두 루틴에는 recv_counts 합계와 size_global_1d를 비교하는 조건이 없다.
- 69–86·132–150: 두 루틴은 active_domains 크기로 배열을 할당하고 displacements_index(1)에 대입한다. 이 파일에는 active_domains>=1이나 DSIcomm의 프로세스 수와 active_domains의 일치를 검사하는 조건이 없다.
- 122·124·158–160: 실수 자료 배열은 real(RKD)로 선언된다. MPI_Gatherv 자료형 인수는 mpi_real8으로 고정되어 있다. RKD의 정의는 이 파일에 없다.
- 64·80·91–93·127·144·158–160: ierr는 MPI_Allgather와 MPI_Gatherv의 반환 인수로 사용된다. 이 파일에는 ierr 검사 조건이 없다.
- 23–26·58–67·75·121–130·138: 두 루틴은 send_size_1d에 size_local_1d를 대입한다. send_size_1d의 선언은 두 루틴의 인수·지역변수 선언과 이 모듈의 직접 선언에 없다. 이 파일은 GLOBAL·Variables_MPI·Variables_MPI_Drifter를 use한다(23–25).

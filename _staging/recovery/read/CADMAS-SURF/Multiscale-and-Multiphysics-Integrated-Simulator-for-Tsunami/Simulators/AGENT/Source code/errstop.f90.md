---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/errstop.f90
lines: 19
sha256: 2ad385248f4db973ad248156fec539954fa518425a3d387241a3b68d1694575e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# errstop.f90 — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 계산을 정지한다는 주석(3). 장래 STOP을 MPI_ABORT로 대체할 것을 예상하며 다른 곳에서는 STOP을 쓰지 않는다는 주석(4–5). `implicit none`(7), `include 'mpif.h'`(8) 및 인수를 선언한다. 루틴명·오류 코드를 출력한 뒤 MPI(Message Passing Interface)의 mpi_abort를 호출한다(16–18). 원문: `subroutine errstop(rout,icode)` (1); `!----------------------------------------` (2); `!計算を停止する` (3); `!  (将来的にSTOP文をMPI_ABORTに置き換えること` (4); `!   を想定し、ここ以外ではSTOP文を使用しない` (5); `!----------------------------------------` (6); `  implicit none` (7); `  include 'mpif.h'` (8); `!` (9); `![arguments]` (10); `  character(*),intent(in):: rout` (11); `  integer,intent(in):: icode` (12); `  integer:: ierr` (13); `!` (14); `!` (15); `  write(*,*) 'Stop at subroutine: ',trim(rout)` (16); `  write(*,*) '        error code= ',icode` (17); `  call mpi_abort(mpi_comm_world,icode,ierr)` (18); `end subroutine errstop` (19) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4–5·18: 주석은 STOP의 장래 대체를 설명하지만 현재 실행문은 이미 mpi_abort 호출이다.

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/errstp.f
lines: 10
sha256: 28b4eaaf222cb2a9deb75dd94dd0c0bcf8cd88e4ebdc40379ad2c02276b5b782
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# errstp.f — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | ERRSTP는 mpif.h를 포함한다(1–3). ITO에 오류 표제 '*** ERROR NO. ***'를 A 형식으로 출력한다(5). 이어서 NO를 I3 형식으로 출력한다(6). 메시지 전달 인터페이스(Message Passing Interface, MPI)의 MPI_ABORT를 MPI_COMM_WORLD·오류 코드 0·IERR 인수로 호출한다(8). 빈 줄·END를 포함한다. 포함 파일 내부는 판독 대상이 아니다. 원문: `      SUBROUTINE ERRSTP(NO,ITO)` (1); `      INCLUDE 'mpif.h'` (3); `      WRITE(ITO,'(A)') '*** ERROR NO. ***'` (5); `      WRITE(ITO,'(I3)') NO` (6); `      CALL MPI_ABORT(MPI_COMM_WORLD,0,IERR)` (8); `      END` (10). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–8: 출력하는 오류 번호는 NO이며, MPI_ABORT에 전달하는 오류 코드는 0으로 고정되어 있다.

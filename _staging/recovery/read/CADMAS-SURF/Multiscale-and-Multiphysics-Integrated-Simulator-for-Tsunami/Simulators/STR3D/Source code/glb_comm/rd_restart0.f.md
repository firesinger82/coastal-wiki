---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/rd_restart0.f
lines: 29
sha256: 8665475c4bd6683a053906c253036b3ab561d44a43b93f7661a92705b3534d13
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rd_restart0.f — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | M_VAL·MPI_PARAM과 암시적 배정밀도를 사용한다(3–8). .rsti000 파일을 비형식(unformatted)으로 열고 프로세스 1에서 IRST를 받는다(10–12). 원문: `      SUBROUTINE RD_RESTART0(KK,IFL,FLNAME,NLEN)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      CHARACTER*256 FLNAME` (7); `      DIMENSION KK(*)` (8); `      OPEN(IFL,FILE=FLNAME(1:NLEN)//'.rsti000',FORM='UNFORMATTED')` (10); `      CALL M_MPI_RECV_I(IRST,1,1)` (12). |
| 14–29 | 시작 시 1행 rd_restart0 루틴 안. 무한 DO에서 ISTEP·NNOW를 읽는다(14–16). KK(92) 양수이면 접촉·마찰 상태 레코드도 읽는다(18–19). ICPL=2이면 NNOW>=IRST에서, 그 외이면 ISTEP==IRST에서 루프를 끝낸다(21–27). 원문: `      DO` (14); `        READ(IFL) ISTEP,NNOW` (16); `        IF( KK(92) > 0 )` (18); `     &    READ(IFL) ISLV0,ISLVP,RSLV0,U0,RL0,IFRIC,ISTK,FRIC` (19); `        IF( ICPL == 2 ) THEN` (21); `          IF( NNOW >= IRST ) EXIT` (22); `        ELSE` (23); `          IF( ISTEP == IRST ) EXIT` (24); `        ENDIF` (25); `      ENDDO` (27); `      END` (29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–27: 재시작 검색 READ에는 END=·IOSTAT= 처리가 없으며 이 루틴에는 CLOSE 문이 없다.

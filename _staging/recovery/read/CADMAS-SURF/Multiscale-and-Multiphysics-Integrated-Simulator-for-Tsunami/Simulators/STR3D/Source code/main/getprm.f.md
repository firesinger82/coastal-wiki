---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/getprm.f
lines: 35
sha256: 5654eefd9dcf3c6e847ab10923927165e6c66ed7faed970eecdc240ae42e9470
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# getprm.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | GETPRM은 기본 입력 data.bdf·메모리(memory) 8000 MB·행렬 해법(matrix solver) 4(MUMPS)·전처리(preconditioning) 1(불완전 Cholesky)을 설정한다(6–9). ICHK=1이면 기본값 설정 후 반환한다(11). IARGC와 GETARG로 인수 쌍을 읽고 -F·-M·-S·-P에 따라 파일명·메모리·해법·전처리를 갱신한다(13–28). 알 수 없는 옵션이면 메시지 출력 후 STOP한다(29–32). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE GETPRM(FLNAME,MEM,ISLV,IPRE,ICHK)` (1) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (3) <br> `      CHARACTER*256 STRING,FLNAME` (4) <br> `      FLNAME = 'data.bdf' ! INPUT DATA FILE` (6) <br> `      MEM    = 8000       ! MEMORY : 8000(MB)` (7) <br> `      ISLV   = 4          ! MATRIX SOLVER : MUMPS` (8) <br> `      IPRE   = 1          ! CG PRE-CONDITIONING : INCOMPLETE CHOLESKY DECOMPOSITION` (9) <br> `      IF( ICHK == 1 ) RETURN` (11) <br> `      NARG=IARGC()` (13) <br> `      DO 100 I=1,NARG,2` (15) <br> `        CALL GETARG(I,STRING)` (16) <br> `        IF(STRING(1:2) .EQ. '-F') THEN` (17) <br> `          CALL GETARG(I+1,STRING)` (18) <br> `          READ(STRING,'(A256)') FLNAME` (19) <br> `        ELSEIF(STRING(1:2) .EQ. '-M') THEN` (20) <br> `          CALL GETARG(I+1,STRING)` (21) <br> `          READ(STRING,'(I6)') MEM` (22) <br> `        ELSEIF(STRING(1:2) .EQ. '-S') THEN` (23) <br> `          CALL GETARG(I+1,STRING)` (24) <br> `          READ(STRING,'(I1)') ISLV` (25) <br> `        ELSEIF(STRING(1:2) .EQ. '-P') THEN` (26) <br> `          CALL GETARG(I+1,STRING)` (27) <br> `          READ(STRING,'(I1)') IPRE` (28) <br> `        ELSE` (29) <br> `          WRITE(*,*) 'SOLVER PARAMETER IS WRONG, PROGRAM STOPPED!'` (30) <br> `          STOP` (31) <br> `        ENDIF` (32) <br> `  100 CONTINUE` (33) <br> `      END` (35) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–28: 명령행 인수는 간격 2로 순회한다. 마지막 옵션의 값 존재 여부를 검사하거나 READ에 IOSTAT를 받는 문장은 없다.

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/fmp_ous.f
lines: 31
sha256: 66a539e7a4b0e827240b452a7a33292490307beb60f4b60be1fe5caebd332a35
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_ous.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | FMP_OUS는 MPI_PARAM과 실수 IMPLICIT 선언을 사용한다. MYRANK=0이면 출력 집합 번호 IOUT, Step·Time 제목, 고정 문자열 0,23, 및 시간·후속 레코드를 기록한다. 원문: `      SUBROUTINE FMP_OUS(IOUT,ISTEP,TIME,IFL)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      CHARACTER*1 C /','/` (5); `      IF( MYRANK == 0 ) THEN` (7); `        WRITE(IFL,'(I0,A)') IOUT,C` (9); `        WRITE(IFL,'(A,I0,A,1PE10.4)') 'Step ',ISTEP,'  Time ',TIME` (11); `        WRITE(IFL,'(A)') '0,23,'` (13); `        WRITE(IFL,'(1PE10.4,A)') TIME,C` (15); `        WRITE(IFL,'(A)') '1,'` (17); `        WRITE(IFL,'(A)') '<NULL>'` (19) |
| 21–31 | 시작 시 7행 `IF( MYRANK == 0 ) THEN` 블록 안이다. 이 IF는 29행 `ENDIF`에서 닫힌다. ELSEIF MYRANK=1은 IOUT·ISTEP·TIME을 목적지 0으로 전송한다. 전송 루틴·인수는 아래와 같다. 조건과 루틴을 닫는다. 원문: `      ELSEIF( MYRANK == 1 ) THEN` (21); `        CALL M_MPI_SEND_I(IOUT,1,0)` (23); `        CALL M_MPI_SEND_I(ISTEP,1,0)` (25); `        CALL M_MPI_SEND_D(TIME,1,0)` (27); `      ENDIF` (29); `      END` (31) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–29: MYRANK=0과 MYRANK=1에만 실행 분기가 있다. 다른 순위(rank)에 대한 ELSE는 없다.

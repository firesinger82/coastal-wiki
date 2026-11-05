---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_TABLEM1.f
lines: 22
sha256: 75fc256d9bcc974e4ca829da9cdc699d5375d8c7e9cc50f21296206a4765ea3b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_TABLEM1.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | RD_TABLEM1의 IMPLICIT·TBM1(2,*)·ITBM1R(*)·X(4)·Y(4)을 선언한다(1–5). 카드(card)의 ID를 읽고 ITBM1R(ID)에 I1을 등록한다(7–8). 10행 무한 루프(loop)는 다음 레코드(record)를 읽고 TB_END(N,CHAR)를 호출한다(11–12). 13행 READ의 내포 DO(implied DO)는 N개의 X·Y 쌍을 읽는다. TBM1(1,I2+1:I2+N)에 X(1:N)을 복사한다(14). TBM1(2,I2+1:I2+N)에 Y(1:N)을 복사한다(15). I2를 N만큼 증가시킨다(16). N<4이면 EXIT하며(17), 끝 위치 I2를 ITM1로 반환한다(20). 원문: `      SUBROUTINE RD_TABLEM1( ITM1, TBM1, ITBM1R, I1, I2, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION TBM1(2,*), ITBM1R(*), X(4), Y(4)` (5); `      READ(CHAR,'(BN,8X,I8)') ID` (7); `      ITBM1R(ID) = I1` (8); `      DO` (10); `        READ(ITI,'(A80)') CHAR` (11); `        CALL TB_END( N, CHAR )` (12); `        READ(CHAR,'(BN,8X,8F8.0)') ( X(I), Y(I), I = 1, N )` (13); `        TBM1(1,I2+1:I2+N) = X(1:N)` (14); `        TBM1(2,I2+1:I2+N) = Y(1:N)` (15); `        I2 = I2 + N` (16); `        IF( N < 4 ) EXIT` (17); `      ENDDO` (18); `      ITM1 = I2` (20); `      END` (22). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–17: 연속행 표식을 검사하지 않고 TB_END가 반환한 N<4를 종료 조건으로 사용한다.

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_MAT1.f
lines: 49
sha256: 45d53fa3f6761c900d9e367b299475263feec37ea06deab5daeeb45367a4c6af
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_MAT1.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | RD_MAT1의 IMPLICIT·AMAT(*)·IMATR(*) 및 문자 선언을 포함한다(1–6). MID·E·RNU·RHO·A·POR·GE를 읽는다(8). AMAT(1:2)·AMAT(4:6)에 읽은 값을 배치한다(10–14). 16행 AMAT(3) 식은 상수 1.D3을 사용한다. 원문: `      SUBROUTINE RD_MAT1( AMAT, IMATR, I_MAT, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION AMAT(*), IMATR(*)` (6); `      READ(CHAR,'(BN,8X,I8,F8.0,8X,5F8.0)') MID, E, RNU, RHO, A, POR,GE` (8); `      AMAT(1) = E` (10); `      AMAT(2) = RNU` (11); `      AMAT(4) = GE` (12); `      AMAT(5) = A` (13); `      AMAT(6) = POR` (14); `      AMAT(3) = ( 1.D0 - POR ) * RHO + POR * 1.D3` (16). [11-04 전수 검증 정정] |
| 18–49 | 시작 시 1행 RD_MAT1 안. 다음 행을 읽고(18), 20행 연속행 조건과 22행 MID<100 조건으로 분기한다. 작은 MID는 ST를 AMAT(14)에 저장한다(24–26). ELSE(28)는 POR·RKF·RK를 읽어 AMAT(7:10)에 배치하며 RK를 9.8D3으로 나눈다(30–35). 37행은 새 POR로 AMAT(3)을 다시 계산한다. 비연속행 ELSE(41)는 BACKSPACE한다(43). IMATR(MID)에 I_MAT를 등록하고 종료한다(47–49). 원문: `      READ(ITI,'(A80)') CHAR` (18); `      IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (20); `        IF( MID < 100 ) THEN` (22); `          READ(CHAR,'(BN,8X,F8.0)') ST` (24); `          AMAT(14) = ST` (26); `        ELSE` (28); `          READ(CHAR,'(BN,8X,3F8.0)') POR, RKF, RK` (30); `          AMAT(7) = POR` (32); `          AMAT(8) = RKF` (33); `          AMAT(9) = RK / 9.8D3` (34); `          AMAT(10) = 1.D3  ! RHOF` (35); `          AMAT(3) = ( 1.D0 - POR ) * RHO + POR * 1.D3` (37); `        ENDIF` (39); `      ELSE` (41); `        BACKSPACE(ITI)` (43); `      ENDIF` (45); `      IMATR(MID) = I_MAT` (47); `      END` (49). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14·30–37: 첫 카드(card)의 POR는 AMAT(6)에 저장된다. MID>=100의 연속행에서는 새 POR를 AMAT(7)에 저장하고 AMAT(3)을 다시 계산하지만 AMAT(6)은 갱신하지 않는다.
- 16·34–37: AMAT(3) 계산에는 1.D3을 직접 사용한다. AMAT(9) 계산에서는 RK를 9.8D3으로 나눈다. [11-04 전수 검증 정정]

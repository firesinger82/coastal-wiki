---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_MAT9.f
lines: 35
sha256: 9d9b3433732b84ee3490029fe8f531b4b9b7a74e49decdd2793fc8c39e6b5323
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_MAT9.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | RD_MAT9의 IMPLICIT·MAT(2)·AMAT(33)·IMATR(*)·G(21)·A(6) 선언을 포함한다(1–6). 세 레코드(record)에서 MID·G(1:21)·RHO·A(1)를 읽는다(8–12). 다음 행의 16행 조건이 참이면 A(2:6)·TREF·GE를 읽는다(17). ELSE(18)는 이 값들을 0으로 설정한 후 BACKSPACE한다(19–22). 원문: `      SUBROUTINE RD_MAT9( MAT, AMAT, IMATR, I_MAT, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION MAT(2), AMAT(33), IMATR(*), G(21), A(6)` (6); `      READ(CHAR,'(BN,8X,I8,7F8.0)') MID, G(1:7)` (8); `      READ(ITI,'(BN,8X,8F8.0)') G(8:15)` (10); `      READ(ITI,'(BN,8X,8F8.0)') G(16:21), RHO, A(1)` (12); `      READ(ITI,'(A80)') CHAR` (14); `      IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (16); `        READ(CHAR,'(BN,8X,7F8.0)') A(2:6), TREF, GE` (17); `      ELSE` (18); `        A(2:6) = 0.` (19); `        TREF = 0.` (20); `        GE = 0.` (21); `        BACKSPACE(ITI)` (22); `      ENDIF` (23). |
| 25–35 | 시작 시 1행 RD_MAT9 안. MAT(1)은 1이다(25). AMAT(3)·AMAT(4)·AMAT(6)에 RHO·GE·TREF를 배치한다(27–29). G와 A를 각각 AMAT(7:27)·AMAT(28:33)에 복사한다(30–31). IMATR(MID)에 I_MAT를 등록한다(33). 주석·END를 포함한다(34–35). 원문: `      MAT(1) = 1` (25); `      AMAT(3) = RHO` (27); `      AMAT(4) = GE` (28); `      AMAT(6) = TREF` (29); `      AMAT(7:27) = G(:)` (30); `      AMAT(28:33) = A(:)` (31); `      IMATR(MID) = I_MAT` (33); `      END` (35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·25–31: MAT(2)와 AMAT(1:2)·AMAT(5)는 이 루틴에서 대입하지 않는다.

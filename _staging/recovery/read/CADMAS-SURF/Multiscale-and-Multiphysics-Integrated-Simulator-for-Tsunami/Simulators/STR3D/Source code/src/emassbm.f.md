---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/emassbm.f
lines: 31
sha256: 0a26d5ecc2c3ae76836987ceef9e982c859bcd3d972ef785f972dacd1faf8a5e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# emassbm.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | EMASSBM의 암시적 형과 배열 및 PI의 DATA 상수를 선언한다. LENGTH에 GRID(1,KN(1))·GRID(1,KN(2))와 3을 전달한다. 해석: EMASS는 두 절점의 질량행렬이며 RL은 두 절점 사이 길이이다. 원문: `      SUBROUTINE EMASSBM(EMASS,AMAT,DIM,GRID,ITYPE,KN,LUMP,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION GRID(3,*),KN(2),AMAT(*),EMASS(2,2),DIM(*)` (4); `      DATA PI /3.141592654D0/` (5); 주석 원문 `C----&------------------------------------------------------------------` (6); `      CALL LENGTH(RL,GRID(1,KN(1)),GRID(1,KN(2)),3)` (7). [11-04 전수 검증 정정] |
| 9–19 | 시작 시 1행 EMASSBM 루틴 안. ITYPE의 0·1·2·3 분기에 따라 A를 계산한다. 마지막 ELSE는 없다. `EM=AMAT(3)*A*RL`로 EM을 계산한다. 해석: A는 직접 입력·원형·직사각형·중공 원형 단면적에 해당한다. 해석: AMAT(3)이 밀도이고 RL이 길이라면 EM은 전체 질량이다. 원문: `      IF(ITYPE .EQ. 0) THEN` (9); `        A=DIM(1)` (10); `      ELSEIF( ITYPE .EQ. 1 ) THEN` (11); `        A=PI*DIM(1)*DIM(1)` (12); `      ELSEIF( ITYPE .EQ. 2 ) THEN` (13); `        A=DIM(1)*DIM(2)` (14); `      ELSEIF(ITYPE .EQ. 3) THEN` (15); `        A=PI*( DIM(1)*DIM(1) - DIM(2)*DIM(2) )` (16); `      ENDIF` (17); `      EM=AMAT(3)*A*RL` (19). [11-04 전수 검증 정정] |
| 20–31 | 시작 시 1행 EMASSBM 루틴 안. LUMP=0이면 EM의 절반을 EMASS(1,1)·EMASS(2,1)에 저장한다. ELSE에서는 2×2 행렬의 대각에 EM/3, 비대각에 EM/6을 둔다. 반환문과 루틴 끝을 포함한다. 원문: `      IF( LUMP .EQ. 0 ) THEN` (20); `        EMASS(1,1) = EM*.5` (21); `        EMASS(2,1) = EM*.5` (22); `      ELSE` (23); `        EMASS(1,1) = EM/3.D0` (24); `        EMASS(1,2) = EM/6.D0` (25); `        EMASS(2,1) = EM/6.D0` (26); `        EMASS(2,2) = EM/3.D0` (27); `      ENDIF` (28); `      RETURN` (30); `      END` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–19: ITYPE 0–3 이외의 ELSE는 없다. 그 경우 이 파일에서 A를 설정하는 문장이 없다.
- 20–28: LUMP=0에서는 EMASS의 첫 열만 대입한다. 두 번째 열은 이 분기에서 설정하지 않는다.

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/sol0.f
lines: 62
sha256: 478248dfb7cc50f011d613bdf8d1450d87e28586d6438b58a317e3ffba98b8c3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sol0.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | SOL0 입구와 배열 선언이다(1–5). ST>0에서 KOJI3D(S,PR,TR,ITO)를 호출한다(7–9). PR(1)이 ST 이상이면 IST=1로 설정한다(11–13). PR(1)과 PR(4:6)을 0으로 설정한 뒤 AXB를 호출한다(17–19). 해석: PR(1)을 최대 주응력, PR(4:6)을 전단 성분으로 보는 설명은 이 구간만으로 확인되지 않는다. DSOL1·HARFC·HARFTA2로 D를 계산하고 반환한다(21–25). 원문: `      SUBROUTINE SOL0(IST,SY,S,D,E,ANU,ST,IYLD,HD,ALP,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION S(6),PR(6),TR(3,3),T1(6,6),T2(6,6),DCR(21),WK1(6,6)`<br>`     &         ,WK2(6),WK3(21),D(21),DE(21),DFDS(6),DRDE(6),DEPDE(6,6)` (4–5); `      IF( ST > 0. ) THEN` (7); `        CALL KOJI3D(S,PR,TR,ITO)` (9); `        IF( PR(1) >= ST ) THEN` (11); `          IST = 1` (13); `          CALL CHTNSR(TR,T1,T2)` (15); `          PR(1) = 0.` (17); `          PR(4:6) = 0.` (18); `          CALL AXB(S,T1,PR,6,6,1)` (19); `          CALL DSOL1(DCR,E,ANU)` (21); `          CALL HARFC(WK1,T1,DCR,6,6)` (22); `          CALL HARFTA2(D,WK1,T1,6,6)` (23); `          RETURN` (25); `        ENDIF` (27); `      ENDIF` (29) [11-04 전수 검증 정정] |
| 31–62 | 시작 시 SOL0 루틴(1) 안이다. IYLD>0에서 YFUNC를 호출한다(31–33). 해석: YFUNC를 항복함수로 보는 설명은 호출 이름에 따른 해석이다. F>=SY이면 IST=2와 SY=F를 설정하고 DSOL0·DFDSG·HARFC·AXB·HARFAB으로 D를 계산한다(35–58). 원문: `      IF( IYLD > 0 ) THEN` (31); `        CALL YFUNC(F,S,IYLD,ALP)` (33); `        IF( F >= SY ) THEN` (35); `          IST = 2` (37); `          SY = F` (39); `          CALL DSOL0(DE,E,ANU)` (41); `          CALL DFDSG(DFDS,S,IYLD,ALP)` (42); 주석: `C         ----- [DRAM/DEPS] -----` (44); `          CALL HARFC(WK2,DFDS,DE,1,6)` (46); `          DRDE(:) = WK2(:) / ( HD + DOT_PRODUCT(WK2,DFDS) )` (47); 주석: `C         ----- [DEPS_P/DEPS] -----` (49); `          CALL AXB(DEPDE,DFDS,DRDE,6,1,6)` (51); 주석: `C         ----- [Dp] -----` (53); `          CALL HARFAB(WK3,DE,DEPDE,6)` (55); `          D(:) = DE(:) - WK3(:)` (56); `        ENDIF` (58); `      ENDIF` (60); `      END` (62) 해석: D를 접선행렬로 보는 설명은 호출과 `[Dp]` 주석(53)에 따른 해석이다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47: DRDE의 분모는 HD+DOT_PRODUCT(WK2,DFDS)이다. 이 계산 앞에는 분모 0 여부를 검사하는 문장이 없다.
- 7–60: 두 활성 조건에 들지 않으면 IST·D를 새로 설정하는 별도 ELSE가 없다.

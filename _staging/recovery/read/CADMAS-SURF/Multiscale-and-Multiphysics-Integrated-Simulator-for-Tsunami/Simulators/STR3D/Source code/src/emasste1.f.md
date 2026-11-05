---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/emasste1.f
lines: 48
sha256: 976bb5bf01ac962936d687b2407949e916850b608b50811a60642896cc805b83
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# emasste1.f — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | EMASSTE1의 인수와 배열을 선언한다. `要素質量行列`은 요소 질량행렬(element mass matrix), `物性テーブル`은 물성표(material property table), `節点座標`는 절점좌표(nodal coordinate), `要素の構成節点番号`는 요소를 구성하는 절점 번호다. LUMP=0은 집중질량(lumped mass), LUMP=1은 일관질량(consistent mass)이다. IG의 DATA 값은 2다. 해석: DATA NG·WGT·RL은 적분점 수·가중치·체적좌표 표에 해당한다. 원문: `      SUBROUTINE EMASSTE1(EMASS,AMAT,GRID,KN,LUMP,ITO)` (1); 주석 원문 `C     EMASS : OUT : 要素質量行列` (3); 주석 원문 `C     AMAT  : IN  : 物性テーブル` (4); 주석 원문 `C     GRID  : IN  : 節点座標` (5); 주석 원문 `C     KN    : IN  : 要素の構成節点番号` (6); 주석 원문 `C     LUMP  : IN  : =0:lumped mass, =1:consistent mass` (7); `      IMPLICIT REAL*8(A-H,O-Z)` (9); `      DIMENSION NG(2),WGT(2),RL(4,4,2),XYZ(3,4),GRID(3,*),KN(4),AMAT(*)`<br>`     &         ,EMASS(4,4),HTH(4,4)` (10–11); `      DATA NG  / 1, 4 /` (12); `      DATA WGT / .166666666666667D0, .0416666666666667D0 /` (13); `      DATA RL  / 4*0.25D0, 12*0.D0`<br>`     &         , .58541020D0, .13819660D0, .13819660D0, .13819660D0`<br>`     &         , .13819660D0, .58541020D0, .13819660D0, .13819660D0`<br>`     &         , .13819660D0, .13819660D0, .58541020D0, .13819660D0`<br>`     &         , .13819660D0, .13819660D0, .13819660D0, .58541020D0 /` (14–18); `      DATA IG / 2 /` (19). [11-04 전수 검증 정정] |
| 21–37 | 시작 시 1행 EMASSTE1 루틴 안. SHIFT1으로 네 절점 좌표를 복사하고 RHO를 AMAT(3)에서 읽는다. CLEAR1으로 EMASS의 16개 값을 초기화한다. NG(IG) 루프에서 LUMP=0이면 RMULT2에 RL과 RHO를 전달한다. ELSE에서는 AXB(HTH,RL(1,I,IG),RL(1,I,IG),4,1,4)를 호출한 뒤 RMULT2를 호출한다. 해석: AXB가 행렬 곱을 수행한다면 HTH는 해당 RL 벡터의 외적이다. 원문: `      DO 100 I=1,4` (21); `        CALL SHIFT1(XYZ(1,I),GRID(1,KN(I)),3)` (22); `  100 CONTINUE` (23); `      RHO=AMAT(3)` (25); `      CALL CLEAR1(EMASS,16)` (27); `      DO 200 I=1,NG(IG)` (29); `        IF(LUMP .EQ. 0) THEN` (30); `          CALL RMULT2(EMASS,RL(1,I,IG),RHO,4)` (31); `        ELSE` (32); `          CALL AXB(HTH,RL(1,I,IG),RL(1,I,IG),4,1,4)` (33); `          CALL RMULT2(EMASS,HTH,RHO,16)` (34); `        ENDIF` (35); `  200 CONTINUE` (36). [11-04 전수 검증 정정] |
| 38–48 | 시작 시 1행 EMASSTE1 루틴 안. TETVOL(XYZ,V)를 호출한 뒤 DET=6*V를 계산한다. 해석: TETVOL의 V가 체적이면 DET는 체적의 6배이다. LUMP=0이면 NT=4, 그 외에는 NT=16을 선택한다. RMULT1에 DET*WGT(IG)를 전달하여 지정 길이의 질량값을 보정한다. 반환문과 루틴 끝을 포함한다. 원문: `      CALL TETVOL(XYZ,V)` (38); `      DET=6.D0*V` (39); `      IF(LUMP .EQ. 0) THEN` (40); `        NT=4` (41); `      ELSE` (42); `        NT=16` (43); `      ENDIF` (44); `      CALL RMULT1(EMASS,EMASS,DET*WGT(IG),NT)` (45); `      RETURN` (47); `      END` (48). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·19·29·45: IG는 DATA로 2에 고정되어 있다. 이 파일에는 IG 변경문이 없으므로 NG의 두 번째 값 4와 WGT의 두 번째 값을 사용한다.
- 1·3–48: ITO는 인수에 있지만 본문에서 참조하지 않는다.

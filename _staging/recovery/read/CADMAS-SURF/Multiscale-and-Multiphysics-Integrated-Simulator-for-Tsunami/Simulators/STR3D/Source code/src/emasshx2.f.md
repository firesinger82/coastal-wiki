---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/emasshx2.f
lines: 66
sha256: e03d2dd1e8ab65986a66eeafd5abdb784127a62ae7038f81bffef56661ba1828
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# emasshx2.f — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | EMASSHX2의 인수와 배열을 선언한다. `要素質量行列`은 요소 질량행렬(element mass matrix), `物性テーブル`은 물성표(material property table), `節点座標`는 절점좌표(nodal coordinate)다. `要素の構成節点番号`는 요소를 구성하는 절점 번호, `要素の構成節点数`는 그 절점 수다. LUMP=0은 집중질량(lumped mass), LUMP=1은 일관질량(consistent mass)이라는 주석이다. XG·WG DATA는 적분 좌표와 가중치(weight)를 저장한다. 원문: `      SUBROUTINE EMASSHX2(EMASS,AMAT,GRID,KN,ND,LUMP,ITO)` (1); 주석 원문 `C     EMASS : OUT : 要素質量行列` (3); 주석 원문 `C     AMAT  : IN  : 物性テーブル` (4); 주석 원문 `C     GRID  : IN  : 節点座標` (5); 주석 원문 `C     KN    : IN  : 要素の構成節点番号` (6); 주석 원문 `C     ND    : IN  : 要素の構成節点数` (7); 주석 원문 `C     LUMP  : IN  : =0:lumped mass, =1:consistent mass` (8); `      IMPLICIT REAL*8(A-H,O-Z)` (10); `      DIMENSION WG(3,3),XG(3,3),XYZ(3,20),GRID(3,*),KN(ND),P(3,20)`<br>`     &         ,AMAT(*),EMASS(ND,ND),H(20),HTH(400)` (11–12); `      DATA XG / 3*0.0D0`<br>`     &        , -.577350269189626D0, .577350269189626D0, 0.0D0`<br>`     &        , -.774596669241483D0, 0.0D0, .774596669241483D0 /` (13–15); `      DATA WG / 2.0D0, 2*0.0D0`<br>`     &        , 2*1.0D0, 0.0D0`<br>`     &        , 0.55555555555555556D0, 0.88888888888888889D0`<br>`     &        , 0.55555555555555556D0 /` (16–19). |
| 21–36 | 시작 시 1행 EMASSHX2 루틴 안. ND=8이면 NG=2, 그 외에는 NG=3으로 둔다. NT=ND*ND를 계산하고 SHIFT1으로 좌표를 복사한다. RHO를 AMAT(3)에서 읽고 CLEAR1으로 EMASS를 초기화한다. VOL을 0으로 둔다. 원문: `      IF(ND .EQ. 8) THEN` (21); `        NG=2` (22); `      ELSE` (23); `        NG=3` (24); `      ENDIF` (25); `      NT=ND*ND` (26); `      DO 200 I=1,ND` (28); `        CALL SHIFT1(XYZ(1,I),GRID(1,KN(I)),3)` (29); `  200 CONTINUE` (30); `      RHO=AMAT(3)` (32); `      CALL CLEAR1(EMASS,NT)` (34); `      VOL=0.` (35). |
| 37–59 | 시작 시 1행 EMASSHX2 루틴 안. I·J·K 적분 루프에서 SFNHX2·DERHX2·DET3를 호출한다. LUMP=0 및 ND=8에서는 RMULT2(EMASS,H,WGT*RHO*DET,ND)를 호출한다. LUMP=0의 다른 ND에서는 VOL을 누적하고 RMULT3를 호출한다. LUMP가 0이 아니면 AXB와 RMULT2를 차례로 호출한다. 해석: RMULT2가 배율 누적을 수행한다면 첫 경로는 집중질량을 누적한다. 해석: AXB가 행렬 곱을 수행한다면 HTH는 H의 외적이다. 원문: `      DO 100 I=1,NG` (37); `      DO 100 J=1,NG` (38); `      DO 100 K=1,NG` (39); `        XG1=XG(I,NG)` (40); `        XG2=XG(J,NG)` (41); `        XG3=XG(K,NG)` (42); `        WGT=WG(I,NG)*WG(J,NG)*WG(K,NG)` (43); `        CALL SFNHX2(XG1,XG2,XG3,ND,H)` (44); `        CALL DERHX2(XG1,XG2,XG3,ND,P)` (45); `        CALL DET3(DET,ND,P,XYZ,ITO)` (46); `        IF( LUMP .EQ. 0 ) THEN` (47); `          IF(ND .EQ. 8) THEN` (48); `            CALL RMULT2(EMASS,H,WGT*RHO*DET,ND)` (49); `          ELSE` (50); `            VOL=VOL+WGT*DET` (51); `            CALL RMULT3(EMASS,H,WGT*DET,ND)` (52); `          ENDIF` (53); `        ELSE` (54); `          CALL AXB(HTH,H,H,ND,1,ND)` (55); `          CALL RMULT2(EMASS,HTH,WGT*RHO*DET,NT)` (56); `        ENDIF` (57); `  100 CONTINUE` (58). [11-04 전수 검증 정정] |
| 60–66 | 시작 시 1행 EMASSHX2 루틴 안. LUMP=0이고 ND>8이면 SUMVEC(EMASST,EMASS,ND)를 호출한다. 이어 RMULT1에 RHO*VOL/EMASST를 전달한다. 51–52행에서 이 경로는 RHO를 곱하지 않은 WGT*DET를 사용했다. 해석: EMASST는 밀도 보정 전 EMASS 성분의 합이며 보정 후 전체 질량 자체로 단정할 수 없다. 반환문과 루틴 끝을 포함한다. 원문: `      IF(LUMP .EQ. 0 .AND. ND .GT. 8) THEN` (60); `        CALL SUMVEC(EMASST,EMASS,ND)` (61); `        CALL RMULT1(EMASS,EMASS,RHO*VOL/EMASST,ND)` (62); `      ENDIF` (63); `      RETURN` (65); `      END` (66). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–12·21–25: 작업 배열의 절점 크기는 20, HTH 길이는 400이다. ND=8 이외의 모든 값은 NG=3을 사용한다.
- 60–62: RHO*VOL/EMASST를 계산하기 전 EMASST=0 검사는 없다.

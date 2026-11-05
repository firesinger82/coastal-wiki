---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/emasspn2.f
lines: 58
sha256: a65990e6952f24479026e958eaa76835ee374dddd03f255a5b27515cae2a9bee
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# emasspn2.f — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | EMASSPN2의 인수와 15절점 배열을 선언한다. `要素質量行列`은 요소 질량행렬(element mass matrix), `物性テーブル`은 물성표(material property table), `節点座標`는 절점좌표(nodal coordinate), `要素の構成節点番号`는 요소를 구성하는 절점 번호다. LUMP=0은 집중질량(lumped mass), LUMP=1은 일관질량(consistent mass)이다. 해석: DATA는 평면 7점과 축 방향 3점의 적분 좌표·가중치 표에 해당한다. 원문: `      SUBROUTINE EMASSPN2(EMASS,AMAT,GRID,KN,LUMP,ITO)` (1); 주석 원문 `C     EMASS : OUT : 要素質量行列` (3); 주석 원문 `C     AMAT  : IN  : 物性テーブル` (4); 주석 원문 `C     GRID  : IN  : 節点座標` (5); 주석 원문 `C     KN    : IN  : 要素の構成節点番号` (6); 주석 원문 `C     LUMP  : IN  : =0:lumped mass, =1:consistent mass` (7); `      IMPLICIT REAL*8(A-H,O-Z)` (9); `      DIMENSION AMAT(*),EMASS(15,15),H(15),P(3,15),RG(7),SG(7),TG(3)`<br>`     &          ,X(3,15),GRID(3,*),KN(15),HTH(15,15),WGI(7),WGJ(3)` (10–11); `      DATA RG /`<br>`     &  0.101286507323456D0, 0.797426985353087D0, 0.101286507323456D0,`<br>`     &  0.470142064105115D0, 0.470142064105115D0, 0.059715871789770D0,`<br>`     &  0.333333333333333D0 /` (13–16); `      DATA SG /`<br>`     &  0.101286507323456D0, 0.101286507323456D0, 0.797426985353087D0,`<br>`     &  0.059715871789770D0, 0.470142064105115D0, 0.470142064105115D0,`<br>`     &  0.333333333333333D0 /` (17–20); `      DATA TG / -.774596669241483D0, 0.0D0, .774596669241483D0 /` (21); `      DATA WGI / 3*0.062969590272414D0, 3*0.066197076394253D0, 0.1125D0/` (23); `      DATA WGJ / 0.55555555555555556D0, 0.88888888888888889D0`<br>`     &         , 0.55555555555555556D0 /` (24–25). [11-04 전수 검증 정정] |
| 27–33 | 시작 시 1행 EMASSPN2 루틴 안. KN으로 좌표를 모으고 RHO를 AMAT(3)에서 얻는다. EMASS 전체와 VOL을 0으로 초기화한다. 원문: `      X(:,:) = GRID(:,KN(:))` (27); `      RHO = AMAT(3)` (29); `      EMASS(:,:) = 0.` (31); `      VOL = 0.` (32). |
| 34–52 | 시작 시 1행 EMASSPN2 루틴 안. JG·IG의 3×7점 적분(integration) 루프에서 SFNPN2·DERPN2·DET3를 호출한다. LUMP=0이면 체적을 누적하고 H의 제곱 적분을 첫 열에 더한다. ELSE에서는 AXB(HTH,H,H,15,1,15)를 호출한다. 이어 HTH*RHO*DET*WGI(IG)*WGJ(JG)를 EMASS에 더한다. 해석: AXB가 행렬 곱을 계산한다면 HTH는 H의 외적이다. 해석: RHO는 밀도 계수에 해당한다. 원문: `      DO JG = 1, 3` (34); `        DO IG = 1, 7` (35); `          CALL SFNPN2(H,15,RG(IG),SG(IG),TG(JG))` (37); `          CALL DERPN2(P,15,RG(IG),SG(IG),TG(JG))` (39); `          CALL DET3(DET,15,P,X,ITO)` (40); `          IF( LUMP == 0 ) THEN` (42); `            VOL = VOL + DET*WGI(IG)*WGJ(JG)` (43); `            EMASS(:,1) = EMASS(:,1) + H(:)*H(:)*DET*WGI(IG)*WGJ(JG)` (44); `          ELSE` (45); `            CALL AXB(HTH,H,H,15,1,15)` (46); `            EMASS(:,:) = EMASS(:,:) + HTH(:,:)*RHO*DET*WGI(IG)*WGJ(JG)` (47); `          ENDIF` (48); `        ENDDO` (50); `      ENDDO` (51). [11-04 전수 검증 정정] |
| 53–58 | 시작 시 1행 EMASSPN2 루틴 안. LUMP=0이면 SUMVEC(EMASST,EMASS,15)를 호출한다. 첫 열에 RHO*VOL/EMASST를 곱한다. 해석: SUMVEC이 합산을 수행한다면 EMASST는 첫 열의 15개 저장값의 합이다. 루틴 끝을 포함한다. 원문: `      IF( LUMP == 0 ) THEN` (53); `        CALL SUMVEC(EMASST,EMASS,15)` (54); `        EMASS(:,1) = EMASS(:,1) * RHO * VOL / EMASST` (55); `      ENDIF` (56); `      END` (58). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 53–55: RHO*VOL/EMASST를 적용하기 전에 EMASST=0을 검사하는 조건문은 없다.

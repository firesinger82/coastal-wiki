---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_gdpth.f
lines: 63
sha256: fa5d2b04d39ccae8ebf9054b54f06288ba41c1a6e0f562f064eb16ef85ee7381
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_gdpth.f — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | SF_GDPTH 선언, INCLUDE 세 개와 배열·포인터(pointer) 범위(1–12). NNOD 길이 DELZ를 할당하고 0으로 시작한다(14–16). 절점(node) IG=1:NNOD를 순회하고 IRGRID<=0은 건너뛴다(18–22). SF_IJ로 수평 셀 번호를 풀고 POS의 x·y를 얻는다(24–27). 원문: `      SUBROUTINE SF_GDPTH(DELZ0,DZ,LNDC,IRGRID,IGNO,POS,XX,YY)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'VF_A0PRM.h'` (5)<br>`      INCLUDE 'VF_ANUMBI.h'` (6)<br>`      INCLUDE 'SF_STRUCT.h'` (7)<br>연속문: `      DIMENSION DELZ0(NNOD0),DZ(NUMI,NUMJ),LNDC(NUMI,NUMJ),IRGRID(NNOD)` (9); `     &         ,IGNO(NNOD),POS(3,NNOD),XX(MAXG1,NUMI),YY(MAXG1,NUMJ)` (10)<br>`      REAL(8), POINTER :: DELZ(:)` (12)<br>`      ALLOCATE( DELZ(NNOD) )` (14)<br>`      DELZ(:) = 0.D0` (16)<br>`      DO IG = 1, NNOD` (18)<br>`        IJ = IRGRID(IG)` (20)<br>`        IF( IJ <= 0 ) CYCLE` (22)<br>`        CALL SF_IJ(I,J,IJ)` (24)<br>`        XG = POS(1,IG)` (26)<br>`        YG = POS(2,IG)` (27) |
| 29–63 | 시작 시 18행 `DO IG = 1, NNOD` 안이다. 이 루프는 53행 `ENDDO`에서 닫힌다. 55–59행 IPART 조건 사슬에는 ELSE가 없다. XG를 `XX(1,I) + .5D0 * XX(2,I)`와 비교하여 IM·IP를 정한다(29–35). YG를 `YY(1,J) + .5D0 * YY(2,J)`와 비교하여 JM·JP를 정한다(40–46). XL·YL·X·Y는 아래 인용한 식으로 계산한다(37–49). 해석: 비교 기준은 셀 중심이고 XL·YL은 인접 셀 폭의 평균이다. SF_INTPL_DPTH로 DELZ(IG)를 구한다(51). IG 루프 종료 후 IPART=0이면 SF_MPI_REDUCE_D, IPART=1이면 SF_REDUCE_D를 호출하고 DELZ를 해제한다(53–61). 원문: `        IF( XG <= XX(1,I) + .5D0 * XX(2,I) ) THEN` (29)<br>`          IM = I - 1` (30)<br>`          IP = I` (31)<br>`        ELSE` (32)<br>`          IM = I` (33)<br>`          IP = I + 1` (34)<br>`        ENDIF` (35)<br>`        XL = .5D0 * ( XX(2,IM) + XX(2,IP) )` (37)<br>`        X  = XG - .5D0 * ( XX(1,IM) + XX(1,IP) )` (38)<br>`        IF( YG <= YY(1,J) + .5D0 * YY(2,J) ) THEN` (40)<br>`          JM = J - 1` (41)<br>`          JP = J` (42)<br>`        ELSE` (43)<br>`          JM = J` (44)<br>`          JP = J + 1` (45)<br>`        ENDIF` (46)<br>`        YL = .5D0 * ( YY(2,JM) + YY(2,JP) )` (48)<br>`        Y  = YG - .5D0 * ( YY(1,JM) + YY(1,JP) )` (49)<br>`        CALL SF_INTPL_DPTH(DELZ(IG),DZ,LNDC,I,IM,IP,J,JM,JP,XL,X,YL,Y)` (51)<br>`      ENDDO` (53)<br>`      IF( IPART == 0 ) THEN` (55)<br>`        CALL SF_MPI_REDUCE_D(DELZ,DELZ0,NNOD,0)` (56)<br>`      ELSEIF( IPART == 1 ) THEN` (57)<br>`        CALL SF_REDUCE_D(DELZ0,NNOD0,DELZ,IGNO,NNOD)` (58)<br>`      ENDIF` (59)<br>`      DEALLOCATE( DELZ )` (61)<br>`      END` (63) [11-04 전수 검증 보완] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55–59: IPART는 0과 1만 처리한다. 다른 값에서 DELZ0를 설정하는 분기는 이 파일에 없다.

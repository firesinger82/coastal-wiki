---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_gpres.f
lines: 72
sha256: 611a5d7f8d53c1e700ca078a90c83e7b692cf3b754401c623e4514ef748450d0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_gpres.f — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | SF_GPRES 선언, INCLUDE 세 개와 배열·포인터(pointer) 범위(1–12). DATA G0=9.8D3을 둔다(14). PRES를 NNOD 길이로 할당하고 0으로 시작한다(16–18). IG 루프에서 IPGRID 첫 지표가 양수일 때만 SF_IJK를 호출한다(20–26). Z에는 POS(3,IG)를 넣는다(28). Z0는 `Z0 = ZZ(1,K) + .5D0 * ZZ(2,K)`로 계산한다(29). 해석: Z는 절점 높이이고 Z0는 셀 중심 높이다. 원문: `      SUBROUTINE SF_GPRES(PRES0,PP,IPGRID,IGNO,POS,ZZ,NF)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'VF_A0PRM.h'` (5)<br>`      INCLUDE 'VF_ANUMBI.h'` (6)<br>`      INCLUDE 'SF_STRUCT.h'` (7)<br>연속문: `      DIMENSION PRES0(NNOD0),PP(NUMI,NUMJ,NUMK),IPGRID(2,NNOD)` (9); `     &         ,POS(3,NNOD),ZZ(MAXG1,NUMK),NF(NUMI,NUMJ,NUMK),IGNO(NNOD)` (10)<br>`      REAL(8), POINTER :: PRES(:)` (12)<br>`      DATA G0 / 9.8D3 /` (14)<br>`      ALLOCATE( PRES(NNOD) )` (16)<br>`      PRES(:) = 0.` (18)<br>`      DO IG = 1, NNOD` (20)<br>`        IJK = IPGRID(1,IG)` (22)<br>`        IF( IJK <= 0 ) CYCLE` (24)<br>`        CALL SF_IJK(I,J,K,IJK)` (26)<br>`        Z = POS(3,IG)` (28)<br>`        Z0 = ZZ(1,K) + .5D0 * ZZ(2,K)` (29) [11-04 전수 검증 정정] |
| 31–63 | 시작 시 20행 `DO IG = 1, NNOD` 안이다. 이 루프는 62행 `ENDDO`에서 닫힌다. 31–47행 바깥 조건 사슬에는 ELSE가 없다. 49–60행 선택문에는 CASE DEFAULT가 없다. Z>=Z0이면 위쪽 NF를 먼저, 아래쪽 NF를 다음에 검사하고 Z<Z0이면 아래쪽을 먼저 검사하여 INTP=1·2·3을 선택한다(31–47). CASE 1은 위 셀, CASE 2는 아래 셀 압력과 선형 보간(linear interpolation)한다(49–57). CASE 3은 PP+(Z0-Z)*G0로 보정한다(58–60). IG 루프를 닫는다(62). 원문: `        IF( Z >= Z0 ) THEN` (31)<br>`          IF( NF(I,J,K+1) >= 0 ) THEN` (32)<br>`            INTP = 1` (33)<br>`          ELSEIF( NF(I,J,K-1) >= 0 ) THEN` (34)<br>`            INTP = 2` (35)<br>`          ELSE` (36)<br>`            INTP = 3` (37)<br>`          ENDIF` (38)<br>`        ELSEIF( Z < Z0 ) THEN` (39)<br>`          IF( NF(I,J,K-1) >= 0 ) THEN` (40)<br>`            INTP = 2` (41)<br>`          ELSEIF( NF(I,J,K+1) >= 0 ) THEN` (42)<br>`            INTP = 1` (43)<br>`          ELSE` (44)<br>`            INTP = 3` (45)<br>`          ENDIF` (46)<br>`        ENDIF` (47)<br>`        SELECT CASE( INTP )` (49)<br>`        CASE( 1 )` (50)<br>`          DZ = Z - Z0` (51)<br>`          CZ = ZZ(3,K+1)` (52)<br>`          PRES(IG) = ( DZ * PP(I,J,K+1)  + (CZ - DZ) * PP(I,J,K) ) / CZ` (53)<br>`        CASE( 2 )` (54)<br>`          DZ = Z0 - Z` (55)<br>`          CZ = ZZ(3,K)` (56)<br>`          PRES(IG) = ( DZ * PP(I,J,K-1)  + (CZ - DZ) * PP(I,J,K) ) / CZ` (57)<br>`        CASE( 3 )` (58)<br>`          PRES(IG) = PP(I,J,K) + ( Z0 - Z ) * G0` (59)<br>`        END SELECT` (60)<br>`      ENDDO` (62) [11-04 전수 검증 보완] |
| 64–72 | 시작 시 1행 SF_GPRES 루틴 안. IPART=0이면 SF_MPI_REDUCE_D로 PRES를 PRES0에 모은다(64–65). IPART=1이면 IGNO를 포함해 SF_REDUCE_D를 호출한다(66–67). 64–68행 IPART 조건 사슬에는 ELSE가 없다. PRES를 해제하고 종료한다(70–72). 원문: `      IF( IPART == 0 ) THEN` (64)<br>`        CALL SF_MPI_REDUCE_D(PRES,PRES0,NNOD,0)` (65)<br>`      ELSEIF( IPART == 1 ) THEN` (66)<br>`        CALL SF_REDUCE_D(PRES0,NNOD0,PRES,IGNO,NNOD)` (67)<br>`      ENDIF` (68)<br>`      DEALLOCATE( PRES )` (70)<br>`      END` (72) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14·59: 수직 압력 보정 계수 G0는 DATA 문에서 9.8D3으로 고정한다.
- 32–43: 인접 셀 접근에 K+1·K-1을 사용한다. 해당 블록에는 K의 상한·하한 검사가 없다.

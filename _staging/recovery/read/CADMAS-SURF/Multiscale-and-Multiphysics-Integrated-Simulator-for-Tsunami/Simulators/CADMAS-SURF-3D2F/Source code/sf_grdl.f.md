---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_grdl.f
lines: 59
sha256: 48e2af6aa7187355c90a9e3c31d26baeca3abedeba1561c3fdca171afbb8cbf2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_grdl.f — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | SF_GRDL 선언과 배열 범위(1–5). DATA IP는 아래 인용한 12개 지표 쌍을 고정한다(7–8). 해석: 이 지표 쌍은 8절점 요소의 모서리 연결이다. NNP개 좌표를 X로 모은다(10). CASE NNP=4에서는 네 점 평균 XG에서 각 점까지 SF_LENGTH 거리를 구하고 나머지 EL(5:12)을 1.D20으로 둔다(12–21). 거리 계산의 근거는 같은 원문 디렉터리의 `sf_length.f:6–12`이다. 원문: `      SUBROUTINE SF_GRDL(GRDL,GRID,NP,NNP)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>연속문: `      DIMENSION X(3,8),GRID(3,*),NP(NNP),IP(2,12),XG(3),EL(12)` (4); `     &         ,GRDL(*)` (5)<br>연속문: `      DATA IP / 1,2, 2,3, 3,4, 4,1, 5,6, 6,7, 7,8, 8,5,` (7); `     &          1,5, 2,6, 3,7, 4,8 /` (8)<br>`      X(:,1:NNP) = GRID(:,NP(1:NNP))` (10)<br>`      SELECT CASE( NNP )` (12)<br>`      CASE( 4 )` (13)<br>`        XG(:) = ( X(:,1) + X(:,2) + X(:,3) + X(:,4) ) / 4.D0` (15)<br>`        DO I = 1, 4` (17)<br>`          CALL SF_LENGTH(EL(I),X(1,I),XG,3)` (18)<br>`        ENDDO` (19)<br>`        EL(5:12) = 1.D20` (21) [11-04 전수 검증 정정] |
| 23–59 | 시작 시 12행 `SELECT CASE( NNP )` 안이다. 이 선택문은 51행 `END SELECT`에서 닫힌다. CASE 6은 대응 절점(node) 사이 길이의 절반 세 개와 두 삼각형 중심까지 거리 여섯 개를 계산하며 EL(10:12)은 1.D20이다(23–42). CASE 8은 IP의 12개 지표 쌍에 대해 SF_LENGTH 반환값의 절반을 계산한다(44–49). 해석: 이는 모서리 길이의 절반이다. 선택문 뒤 EL의 최솟값과 각 절점의 기존 GRDL 중 작은 값을 저장한다(51–57). 거리 계산의 근거는 같은 원문 디렉터리의 `sf_length.f:6–12`이다. 원문: `      CASE( 6 )` (23)<br>`        DO I = 1, 3` (25)<br>`          CALL SF_LENGTH(EL(I),X(1,I),X(1,I+3),3)` (26)<br>`          EL(I) = EL(I) * .5D0` (27)<br>`        ENDDO` (28)<br>`        XG(:) = ( X(:,1) + X(:,2) + X(:,3) ) / 3.D0` (30)<br>`        DO I = 1, 3` (32)<br>`          CALL SF_LENGTH(EL(I+3),X(1,I),XG,3)` (33)<br>`        ENDDO` (34)<br>`        XG(:) = ( X(:,4) + X(:,5) + X(:,6) ) / 3.D0` (36)<br>`        DO I = 1, 3` (38)<br>`          CALL SF_LENGTH(EL(I+6),X(1,I+3),XG,3)` (39)<br>`        ENDDO` (40)<br>`        EL(10:12) = 1.D20` (42)<br>`      CASE( 8 )` (44)<br>`        DO I = 1, 12` (46)<br>`          CALL SF_LENGTH(EL(I),X(1,IP(1,I)),X(1,IP(2,I)),3)` (47)<br>`          EL(I) = EL(I) * .5D0` (48)<br>`        ENDDO` (49)<br>`      END SELECT` (51)<br>`      EL_MIN = MINVAL( EL )` (53)<br>`      DO I = 1, NNP` (55)<br>`        GRDL(NP(I)) = DMIN1( GRDL(NP(I)), EL_MIN )` (56)<br>`      ENDDO` (57)<br>`      END` (59) [11-04 전수 검증 보완] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–53: NNP 선택문은 4·6·8만 처리하고 CASE DEFAULT가 없다. EL 전체의 MINVAL 호출은 선택문 밖에 있다.

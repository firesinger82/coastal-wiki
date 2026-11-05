---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gnpflw.f
lines: 74
sha256: 0a2bb534c61f5d5fe41014e459461769b0f27e5799156fb4cb62dc8404267314
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gnpflw.f — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | GNPFLW는 요소 유량(flux) 계산과 전역 절점 항 누적을 준비한다. 실수 IMPLICIT·배열 선언은 아래와 같다. AMAT(7:10)에서 POR·RKF·RK·RHOF를 읽는다. 해석: POR는 공극률(porosity)로 보인다. KN에 해당하는 좌표를 X로 모은다. 원문: `      SUBROUTINE GNPFLW(FLI,FLO,FCP,VELG,VELE,GRID,UG1,UG2,UG3,PG1,PG2` (1); `     &                 ,PG3,KN,ND,AMAT,GRAV,DT1,DT2,ALP,BETA,IDYN,ITO)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION FI(ND),FO(ND),FP(3,ND),VELG(3,*),VELE(3),GRID(3,*)` (5); `     &         ,UG1(6,*),UG2(6,*),UG3(6,*),PG1(*),PG2(*),PG3(*),KN(ND)` (6); `     &         ,AMAT(*),GRAV(3),X(3,ND),UD(3,ND),UDD(3,ND),P(ND),PB(ND)` (7); `     &         ,PD(ND),FLI(*),FLO(*),FCP(3,*)` (8); `      POR  = AMAT(7)` (10); `      RKF  = AMAT(8)` (11); `      RK   = AMAT(9)` (12); `      RHOF = AMAT(10)` (13); `      X(:,:) = GRID(:,KN(:))` (15) [11-04 전수 검증 정정] |
| 17–46 | IDYN=1이면 DT12를 계산하고 UG1·UG2·UG3로 UD·UDD를 차분한다. P는 ALP로 PG1·PG3를 가중한다. PB는 BETA로 PG1·PG2·PG3를 가중한다. PD는 PG3와 PG1의 차분이다. 해석: UD·UDD는 속도(velocity)·가속도(acceleration)로 보인다. 해석: PG1·PG2·PG3는 세 시점의 압력으로 보인다. 23–24행과 28–29행은 각각 한 계산문이다. ELSEIF IDYN=0이면 UD·UDD·PD는 0, P·PB는 PG3이다. 원문: `      IF( IDYN == 1 ) THEN` (17); `        DT12 = .5D0 * ( DT1 + DT2 )` (19); `        UD(:,:) = ( UG3(1:3,KN(:)) - UG1(1:3,KN(:)) ) / DT12 * .5D0` (21); `        UDD(:,:) = ( ( UG3(1:3,KN(:)) - UG2(1:3,KN(:)) ) / DT2 -` (23); `     &               ( UG2(1:3,KN(:)) - UG1(1:3,KN(:)) ) / DT1 ) / DT12` (24); `        P(:) = ( 1.D0 - ALP ) * PG1(KN(:)) + ALP * PG3(KN(:))` (26); `        PB(:) = BETA * PG3(KN(:)) + ( 1.D0 - 2.D0 * BETA ) * PG2(KN(:))` (28); `     &        + BETA * PG1(KN(:))` (29); `        PD(:) = ( PG3(KN(:)) - PG1(KN(:)) ) / DT12 * .5D0` (31); `      ELSEIF( IDYN == 0 ) THEN` (33); `        UD(:,:) = 0.` (35); `        UDD(:,:) = 0.` (37); `        P(:) = PG3(KN(:))` (39); `        PB(:) = PG3(KN(:))` (41); `        PD(:) = 0.` (43); `      ENDIF` (45) [11-04 전수 검증 정정] |
| 47–74 | ND=4·10·6·15·8·20에 따라 GNPFTE1·GNPFTE2·GNPFPN2·GNPFHX2로 분기한다. GNPFPN2에 전달하는 NI·NJ는 ND=6에서 3·2이며 ND=15에서 7·3이다. 이 두 인수는 `geo/gnpfpn2.f:1,37–38`의 루프 상한이다. GNPFHX2에 전달하는 NG는 ND=8에서 2이며 ND=20에서 3이다. NG는 `geo/gnpfhx2.f:1,21–23`의 세 루프 상한이다. 해석: PN·HX는 각각 삼각기둥(prism)·육면체(hexahedron)를 가리키는 것으로 보인다. 각 호출 연속행 전체를 아래에 인용한다. FI·FO·FP를 KN의 전역 FLI·FLO·FCP에 더한다. 원문: `      SELECT CASE( ND )` (47); `      CASE( 4 )` (48); `        CALL GNPFTE1(FI,FO,FP,VELG,VELE,X,UD,UDD,P,PB,PD,POR,RKF,RK,RHOF` (49); `     &              ,GRAV,ITO)` (50); `      CASE( 10 )` (51); `        CALL GNPFTE2(FI,FO,FP,VELG,VELE,X,UD,UDD,P,PB,PD,POR,RKF,RK,RHOF` (52); `     &              ,GRAV,ITO)` (53); `      CASE( 6 )` (54); `        CALL GNPFPN2(FI,FO,FP,VELG,VELE,ND,3,2,X,UD,UDD,P,PB,PD,POR,RKF` (55); `     &              ,RK,RHOF,GRAV,ITO)` (56); `      CASE( 15 )` (57); `        CALL GNPFPN2(FI,FO,FP,VELG,VELE,ND,7,3,X,UD,UDD,P,PB,PD,POR,RKF` (58); `     &              ,RK,RHOF,GRAV,ITO)` (59); `      CASE( 8 ) ` (60); `        CALL GNPFHX2(FI,FO,FP,VELG,VELE,ND,2,X,UD,UDD,P,PB,PD,POR,RKF,RK` (61); `     &              ,RHOF,GRAV,ITO)` (62); `      CASE( 20 ) ` (63); `        CALL GNPFHX2(FI,FO,FP,VELG,VELE,ND,3,X,UD,UDD,P,PB,PD,POR,RKF,RK` (64); `     &              ,RHOF,GRAV,ITO)` (65); `      END SELECT` (66); `      FLI(KN(:)) = FLI(KN(:)) + FI(:)` (68); `      FLO(KN(:)) = FLO(KN(:)) + FO(:)` (70); `      FCP(:,KN(:)) = FCP(:,KN(:)) + FP(:,:)` (72); `      END` (74) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–45: IDYN=1·0 이외의 값을 처리하는 ELSE는 없다.
- 47–66·68–72: ND 선택에는 CASE DEFAULT가 없다. 선택 뒤 전역 누적문을 무조건 수행한다.
- 21–31: 동적 차분식에 DT1·DT2·DT12 분모가 있다. 이 파일에는 해당 값의 0 검사문이 없다.

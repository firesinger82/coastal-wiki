---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/gnpflw_s.f
lines: 74
sha256: 514d5ac145a994ad0e225f8d9e25ea61f172af117507ca77540cb39296d1a9f4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gnpflw_s.f — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | GNPFLW_S의 연속 인수·암시적 형·배열 선언. AMAT(7:10)에서 POR·RKF·RK·RHOF를 각각 얻고 요소 좌표를 모은다. 원문: 연속문(1–2): `      SUBROUTINE GNPFLW_S(FLI,FLO,FCP,VELG,VELE,GRID,UG1,UG2,UG3,PG1,PG3` <br> `     &                   ,KN,ND,AMAT,GRAV,DT1,DT2,ALP,IDYN,ITO)`; `      IMPLICIT REAL*8(A-H,O-Z)` (4); 연속문(5–8): `      DIMENSION FI(ND),FO(ND),FP(3,ND),VELG(3,*),VELE(3),GRID(3,*)` <br> `     &         ,UG1(6,*),UG2(6,*),UG3(6,*),PG1(*),PG3(*),KN(ND),AMAT(*)` <br> `     &         ,GRAV(3),X(3,ND),UD(3,ND),UDD(3,ND),P(ND),PB(ND),PD(ND)` <br> `     &         ,FLI(*),FLO(*),FCP(3,*)`; `      POR  = AMAT(7)` (10); `      RKF  = AMAT(8)` (11); `      RK   = AMAT(9)` (12); `      RHOF = AMAT(10)` (13); `      X(:,:) = GRID(:,KN(:))` (15). [11-04 전수 검증 정정] |
| 17–46 | GNPFLW_S 루틴 안. IDYN=1이면 DT1·DT2의 평균과 UG·PG 배열의 차분 및 가중합을 계산한다. 21행 UD 차분 대입은 주석 처리된 코드이며 실행 대입은 UD=0이다. 해석: UG는 변위이고 PG는 압력이며 DT1·DT2는 시간 간격으로 읽힌다. IDYN=0은 UD·UDD·PD를 0, P·PB를 PG3으로 둔다. 원문: `      IF( IDYN == 1 ) THEN` (17); `        DT12 = .5D0 * ( DT1 + DT2 )` (19); `!       UD(:,:) = ( UG3(1:3,KN(:)) - UG1(1:3,KN(:)) ) / DT12 * .5D0` (21); `        UD(:,:) = 0.` (22); 연속문(24–25): `        UDD(:,:) = ( ( UG3(1:3,KN(:)) - UG2(1:3,KN(:)) ) / DT2 -` <br> `     &               ( UG2(1:3,KN(:)) - UG1(1:3,KN(:)) ) / DT1 ) / DT12`; `        P(:) = ( 1.D0 - ALP ) * PG1(KN(:)) + ALP * PG3(KN(:))` (27); `        PB(:) = PG3(KN(:))` (29); `        PD(:) = ( PG3(KN(:)) - PG1(KN(:)) ) / DT12 * .5D0` (31); `      ELSEIF( IDYN == 0 ) THEN` (33); `        UD(:,:) = 0.` (35); `        UDD(:,:) = 0.` (37); `        P(:) = PG3(KN(:))` (39); `        PB(:) = PG3(KN(:))` (41); `        PD(:) = 0.` (43); `      ENDIF` (45). [11-04 전수 검증 정정] |
| 47–74 | GNPFLW_S 루틴 안. 절점 수에 따라 GNPFTE1·GNPFTE2·GNPFPN2·GNPFHX2를 호출한다. ND=6·15이면 GNPFPN2에 각각 3·2와 7·3을 전달한다. ND=8·20이면 GNPFHX2에 각각 2와 3을 전달한다. 해석: 이 정수 인수들은 쐐기·육면체 요소의 적분 점 수로 읽힌다. 요소 결과 FI·FO·FP를 FLI·FLO·FCP에 누적한다. 원문: `      SELECT CASE( ND )` (47); `      CASE( 4 )` (48); 연속문(49–50): `        CALL GNPFTE1(FI,FO,FP,VELG,VELE,X,UD,UDD,P,PB,PD,POR,RKF,RK,RHOF` <br> `     &              ,GRAV,ITO)`; `      CASE( 10 )` (51); 연속문(52–53): `        CALL GNPFTE2(FI,FO,FP,VELG,VELE,X,UD,UDD,P,PB,PD,POR,RKF,RK,RHOF` <br> `     &              ,GRAV,ITO)`; `      CASE( 6 )` (54); 연속문(55–56): `        CALL GNPFPN2(FI,FO,FP,VELG,VELE,ND,3,2,X,UD,UDD,P,PB,PD,POR,RKF` <br> `     &              ,RK,RHOF,GRAV,ITO)`; `      CASE( 15 )` (57); 연속문(58–59): `        CALL GNPFPN2(FI,FO,FP,VELG,VELE,ND,7,3,X,UD,UDD,P,PB,PD,POR,RKF` <br> `     &              ,RK,RHOF,GRAV,ITO)`; `      CASE( 8 ) ` (60); 연속문(61–62): `        CALL GNPFHX2(FI,FO,FP,VELG,VELE,ND,2,X,UD,UDD,P,PB,PD,POR,RKF,RK` <br> `     &              ,RHOF,GRAV,ITO)`; `      CASE( 20 ) ` (63); 연속문(64–65): `        CALL GNPFHX2(FI,FO,FP,VELG,VELE,ND,3,X,UD,UDD,P,PB,PD,POR,RKF,RK` <br> `     &              ,RHOF,GRAV,ITO)`; `      END SELECT` (66); `      FLI(KN(:)) = FLI(KN(:)) + FI(:)` (68); `      FLO(KN(:)) = FLO(KN(:)) + FO(:)` (70); `      FCP(:,KN(:)) = FCP(:,KN(:)) + FP(:,:)` (72); `      END` (74). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–25: UG3·UG1 차분을 UD에 대입하는 문장은 주석이다. 실행문은 UD를 0으로 둔다. UDD는 UG3·UG2·UG1의 차분을 DT2·DT1·DT12로 나누어 계산한다. [11-04 전수 검증 정정]
- 17–45·47–66: IDYN 분기는 1·0만, ND 분기는 4·10·6·15·8·20만 있다. 나머지 값 처리 분기는 없다.

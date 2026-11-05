---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/npflow.f
lines: 37
sha256: feef18ed9fea7fac8304e27f005607e656fe19f0783a7f21749e1e2d32a2d4e6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# npflow.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | NPFLOW는 FLI·FLO·FCP를 초기화하고 요소별 GNPFLW 호출을 준비한다. 해석: VELG·VELE와 FCP는 간극수 유량(pore water flux)과 결합력에 해당하는 것으로 보인다. 실수 IMPLICIT·연속 DIMENSION과 GRAV의 DATA 문을 아래에 그대로 적었다. GRAV는 (0,0,-9.8)로 설정한다. 해석: GRAV는 중력(gravity)으로 보인다. KK에서 요소 범위 세 값을 얻고 FLI·FLO·FCP를 0으로 초기화한다. 원문: `      SUBROUTINE NPFLOW(FTI,FLI,FLO,FCP,VELG,MGP,VELE,KK,NNOD,RR,GRID` (1); `     &                 ,IELM,NM,AMAT,UG1,UG2,UG3,PG1,PG2,PG3,DT1,DT2` (2); `     &                 ,IDYN,ITO)` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION FLI(NNOD),FLO(NNOD),FCP(3,NNOD),VELG(3,MGP,*),VELE(3,*)` (6); `     &         ,GRID(3,NNOD),UG1(6,NNOD),UG2(6,NNOD),UG3(6,NNOD)` (7); `     &         ,PG1(NNOD),PG2(NNOD),PG3(NNOD),AMAT(33,*),GRAV(3)` (8); `     &         ,IELM(NM,*),KK(*),RR(*),FTI(6,NNOD)` (9); `      DATA GRAV / 0.D0, 0.D0, -9.8D0 /` (10); `      NELM = KK(12)` (12); `      NELMC = KK(29)` (13); `      NELMX = KK(32)` (14); `      FLI(:) = 0.` (16); `      FLO(:) = 0.` (17); `      FCP(:,:) = 0.` (18) [11-04 전수 검증 정정] |
| 20–37 | 전체 요소 범위에서 `I > NELM .AND. I <= NELM + NELMC`인 구간을 건너뛴다. 해석: 이 구간은 접촉 요소 구간으로 보인다. ITYP·ND·IMAT를 읽고 ITYP=6이면 GNPFLW를 호출한다. 28–31행은 조건부 호출 한 문장이다. RR(7)·RR(4)와 시점별 변위·압력·시간 간격을 전달한다. 모든 요소 처리 뒤 FTI의 첫 세 성분에서 FCP를 뺀다. 원문: `      DO I = 1, NELM + NELMC + NELMX` (20); `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (22); `        ITYP = IELM(2,I)` (24); `        ND   = IELM(3,I)` (25); `        IMAT = IELM(4,I)` (26); `        IF( ITYP == 6 )` (28); `     &    CALL  GNPFLW(FLI,FLO,FCP,VELG(1,1,I),VELE(1,I),GRID,UG1,UG2` (29); `     &                ,UG3,PG1,PG2,PG3,IELM(8,I),ND,AMAT(1,IMAT),GRAV` (30); `     &                ,DT1,DT2,RR(7),RR(4),IDYN,ITO)` (31); `      ENDDO` (33); `      FTI(1:3,:) = FTI(1:3,:) - FCP(:,:)` (35); `      END` (37) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10: GRAV의 세 번째 성분 -9.8D0은 DATA 문 상수이다. 해석: 이 성분은 수직 중력으로 보인다. [11-04 전수 검증 정정]
- 16–18·35: FLI·FLO·FCP는 이 루틴에서 0으로 초기화한다. FTI는 초기화 없이 기존 값에서 FCP를 뺀다.

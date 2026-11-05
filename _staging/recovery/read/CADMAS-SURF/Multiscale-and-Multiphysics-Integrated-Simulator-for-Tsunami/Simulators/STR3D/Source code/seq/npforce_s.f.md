---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/npforce_s.f
lines: 79
sha256: 149be9738d2559a94da42dc7be930d1cb35329af855e84280043cf500719b044
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# npforce_s.f — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | NPFORCE_S의 연속 인수·암시적 형·배열 선언. 요소 수와 RR(4)·RR(5)의 BETA·W4를 얻는다. DT1과 DT2의 산술평균 DT12를 계산한다. 최신 힘·압력력 작업 구간을 0으로 초기화한다. 원문: 연속문(1–3): `      SUBROUTINE NPFORCE_S(FTI,FCK,FCD,FCM,FCMD,FCP,EPS,S,MGP,KK,NNOD` <br> `     &                    ,NESTF,RR,GRID,IELM,NM,AMAT,RODA,BARD,BVEC,D` <br> `     &                    ,UG,VG,PPND,DT1,DT2,ITER,ITER2,IDYN,ITO)`; `      IMPLICIT REAL*8(A-H,O-Z)` (5); 연속문(6–10): `      DIMENSION KK(*),RR(*),FCK(6,NNOD,3),FCD(6,NNOD,4),FCM(6,NNOD,3)` <br> `     &         ,FCMD(6,NNOD,3),IELM(NM,*),FC(60),EPS(6*MGP,*),S(6*MGP,*)` <br> `     &         ,D(21*MGP,*),GRID(3,NNOD),UG(6,NNOD),AMAT(33,*)` <br> `     &         ,EMASS(NESTF),FTI(6,NNOD),VG(12,*),RODA(*),BARD(6,*)` <br> `     &         ,BVEC(3,*),FCP(3,NNOD,2),PPND(NNOD)`; `      NELM = KK(12)` (12); `      NELMC = KK(29)` (13); `      NELMX = KK(32)` (14); `      BETA = RR(4)` (16); `      W4 = RR(5)` (17); `      DT12 = .5D0 * ( DT1 + DT2 )` (19); `      FCK(:,:,3) = 0.` (21); `      FCD(:,:,4) = 0.` (22); `      FCM(:,:,3) = 0.` (23); `      FCMD(:,:,3) = 0.` (24); `      FCP(:,:,2) = 0.` (26). [11-04 전수 검증 정정] |
| 28–62 | NPFORCE_S 루틴 안. I=1부터 NELM+NELMC+NELMX까지 반복하되 NELM < I <= NELM+NELMC 구간은 건너뛴다. 유형 1·4는 자유도 6, 나머지는 3이다. ENPFRC·ENPFADD로 내부력을 계산·누적한다. GE를 계산해 ENPFADDG, 질량 행렬(mass matrix)을 얻어 ENPFADDM을 호출한다. 지정 조건에서 EFRCP로 압력력을 계산한다. 원문: `      DO I = 1, NELM + NELMC + NELMX` (28); `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (30); `        ITYP = IELM(2,I)` (32); `        IF( ITYP == 1 .OR. ITYP == 4 ) THEN` (33); `          NDF = 6` (34); `        ELSE` (35); `          NDF = 3` (36); `        ENDIF` (37); `        NNP = IELM(3,I)` (38); `        IMAT = IELM(4,I)` (39); `        I5 = IELM(5,I)` (40); `        I7 = IELM(7,I)` (41); 연속문(43–44): `        CALL ENPFRC(FC,EPS(1,I),S(1,I),GRID,UG,VG(1,I7),ITYP,IELM(8,I)` <br> `     &             ,NNP,RODA(I5),BARD(1,I5),BVEC(1,I7),D(1,I),KK(2),ITO)`; `        CALL ENPFADD(FCK(1,1,3),FC,NDF,NNP,IELM(8,I))` (46); `        GE = AMAT(4,IMAT) / W4` (48); `        CALL ENPFADDG(FCD(1,1,4),GE,FC,NDF,NNP,IELM(8,I))` (50); 연속문(52–53): `        CALL EMASSMTX(EMASS,GRID,ITYP,NDF,NNP,IELM(6,I),IELM(8,I)` <br> `     &               ,AMAT(1,IMAT),RODA(I5),BARD(1,I5),KK(30),ITO)`; 연속문(55–56): `        CALL ENPFADDM(FCM(1,1,3),FCMD(1,1,3),EMASS,UG,IELM(8,I),NDF,NNP` <br> `     &               ,AMAT(5,IMAT))`; 연속문(58–59): `        IF( ITYP == 2 .AND. I5 == 1 ) ` <br> `     &    CALL EFRCP(FCP(1,1,2),GRID,PPND,IELM(8,I),NNP,ITO)`; `      ENDDO` (61). [11-04 전수 검증 정정] |
| 63–79 | NPFORCE_S 루틴 안. 첫 이중 반복에서 FCD의 현재 이력을 맞춘다. IDYN=1이면 FCM·FCMD·FCD의 차분 항과 FCK의 BETA 가중합으로 FTI를 만든다. 해석: 이 항들은 질량·감쇠·강성 기여로 읽힌다. IDYN=0이면 최신 FCK를 사용한다. 처음 세 힘 성분에서 두 압력력 항을 뺀다. 원문: `      IF( ITER == 1 .AND. ITER2 == 1 ) FCD(:,:,3) = FCD(:,:,4)` (63); `      IF( IDYN == 1 ) THEN` (65); 연속문(66–72): `        FTI(:,:) = ( FCM(:,:,3)/DT2 - ( 1.D0/DT2 + 1.D0/DT1 )*FCM(:,:,2)` <br> `     &             + FCM(:,:,1)/DT1 ) / DT12` <br> `     &           + ( FCMD(:,:,3) - FCMD(:,:,1) ) / DT12 * .5D0` <br> `     &           + ( ( FCD(:,:,4) - FCD(:,:,3) ) / DT2 ` <br> `     &             + ( FCD(:,:,2) - FCD(:,:,1) ) / DT1 ) * .5D0` <br> `     &           + ( BETA * FCK(:,:,3) + ( 1.D0 - 2.D0*BETA )*FCK(:,:,2)` <br> `     &             + BETA * FCK(:,:,1) )`; `      ELSEIF( IDYN == 0 ) THEN` (73); `        FTI(:,:) = FCK(:,:,3)` (74); `      ENDIF` (75); `      FTI(1:3,:) = FTI(1:3,:) - FCP(:,:,1) - FCP(:,:,2)` (77); `      END` (79). 65·73행의 IF/ELSEIF 사슬에는 ELSE가 없다. [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48: GE=AMAT(4,IMAT)/W4를 계산한다. 이 파일에는 W4=0 검사문이 없다.
- 65–77: IDYN 분기는 1·0만 있다. 77행의 FCP(:,:,1)·FCP(:,:,2) 차감문은 해당 분기 밖에 있다. [11-04 전수 검증 정정]

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/npforced.f
lines: 61
sha256: f86b6f71c7caf98050de193a1d3ea0b438fd30f8698ebb92d6a543868431b0c0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# npforced.f — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | NPFORCED는 요소 수와 RR의 BETA,W4를 읽고 평균 시간 간격(time step) DT12를 구한다(10–17). FTI를 FTID로 복사한다(19). ESTF,EMASS는 길이 1830, DFC는 길이 60으로 선언된다(5–8). 원문: 연속문(1–2): `      SUBROUTINE NPFORCED(FTID,KK,NNOD,RR,GRID,IELM,NM,AMAT,RODA,BARD` (1); `     &                   ,BVEC,DUG,UGP,VGP,FTI,D,S,MGP,DT1,DT2,IDYN,ITO)` (2). `      IMPLICIT REAL*8(A-H,O-Z)` (4). 연속문(5–8): `      DIMENSION ESTF(1830),GRID(3,NNOD),UGP(6,NNOD),IELM(NM,*)` (5); `     &         ,D(21*MGP,*),S(6*MGP,*),DUG(6,NNOD),KK(*),RR(*)` (6); `     &         ,AMAT(33,*),EMASS(1830),VGP(12,*),RODA(*),BARD(6,*)` (7); `     &         ,BVEC(3,*),FTI(6,NNOD),FTID(6,NNOD),DFC(60)` (8). `      NELM = KK(12)` (10). `      NELMC = KK(29)` (11). `      NELMX = KK(32)` (12). `      BETA = RR(4)` (14). `      W4 = RR(5)` (15). `      DT12 = .5D0 * ( DT1 + DT2 )` (17). `      FTID(:,:) = FTI(:,:)` (19). |
| 21–41 | 시작 시 1–2행 NPFORCED 루틴 안. 요소 루프에서 NELMC 구간을 건너뛴다(21–23). ITYP=1 또는 4이면 NDF=6, 그 밖에는 3으로 한다(25–30). 요소 절점·재료·주소를 읽고 N1,N2를 계산하여 ESTFMTX를 호출한다(31–40). 원문: `      DO I = 1, NELM + NELMC + NELMX` (21). `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (23). `        ITYP = IELM(2,I)` (25). `        IF( ITYP == 1 .OR. ITYP == 4 ) THEN` (26). `          NDF = 6` (27). `        ELSE` (28). `          NDF = 3` (29). `        ENDIF` (30). `        NNP = IELM(3,I)` (31). `        IMAT = IELM(4,I)` (32). `        I5 = IELM(5,I)` (33). `        I7 = IELM(7,I)` (34). `        N1 = NNP * NDF` (36). `        N2 = N1 * ( N1 + 1 ) / 2` (37). 연속문(39–40): `        CALL ESTFMTX(ESTF,GRID,UGP,VGP(1,I7),ITYP,IELM(8,I),NNP,RODA(I5)` (39); `     &              ,BARD(1,I5),BVEC(1,I7),D(1,I),S(1,I),KK(2),ITO)` (40). |
| 42–61 | 시작 시 1–2행 NPFORCED 루틴·21행 `DO I = 1, NELM + NELMC + NELMX` 안. 이 루프는 59행 `ENDDO`에서 닫힌다. IDYN=1일 때 EMASSMTX를 호출하고 CM,GE 및 시간 계수로 ESTF를 갱신한다(42–53). 이 조건 밖에서 ENPFRCD와 ENPFADD를 호출하여 요소 힘을 FTID에 더한다(55–57). 루프 종료와 END를 포함한다. 원문: `        IF( IDYN == 1 ) THEN` (42). 연속문(44–45): `          CALL EMASSMTX(EMASS,GRID,ITYP,NDF,NNP,IELM(6,I),IELM(8,I)` (44); `     &                 ,AMAT(1,IMAT),RODA(I5),BARD(1,I5),KK(30),ITO)` (45). `          CM = AMAT(5,IMAT)` (47). `          GE = AMAT(4,IMAT) / W4` (48). 연속문(50–51): `          ESTF(1:N2) = ( 1.D0/DT2 + .5D0*CM ) / DT12 * EMASS(1:N2)` (50); `     &               + ( .5D0/DT2*GE + BETA ) * ESTF(1:N2)` (51). `        ENDIF` (53). `        CALL ENPFRCD(DFC,ESTF,DUG,IELM(8,I),NDF,NNP)` (55). `        CALL ENPFADD(FTID,DFC,NDF,NNP,IELM(8,I))` (57). `      ENDDO` (59). `      END` (61). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–8·36–40·50–51: 작업 배열 ESTF와 EMASS의 크기는 1830, DFC는 60으로 고정되며 N1,N2와의 크기 비교는 이 파일에 없다.
- 17·48–51: W4,DT2,DT12로 나누는 식 앞에 해당 값의 0 검사는 없다.

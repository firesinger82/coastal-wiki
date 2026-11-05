---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/mergdp.f
lines: 21
sha256: 83a9e113eb1a9ddfb8a4d33b6dd20234c6b694bb85e854c904c0b1c6e09e818b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mergdp.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | MERGDP는 실수 IMPLICIT 선언과 배열 범위를 아래와 같이 사용한다. 절점 I=1,NNOD에서 INDOP(I)>0이면 DP(IFR)를 DPG(I)에 복사한다. 해석: DP는 해 벡터로 보인다. INDOP(I)=0이면 DPG를 0으로 만든다. PG에 DPG를 더한다. IMPC>0이면 추가 위치 PG(NNOD+NNODC+1)를 첫 인수로 GSURF를 호출한다. 원문: `      SUBROUTINE MERGDP(PG,DPG,DP,INDOP,IELM,NM,IBEL,IMPC,NNOD,NNODC` (1); `     &                 ,NELM)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION PG(*),DPG(NNOD),DP(*),INDOP(NNOD),IELM(NM,NELM)` (5); `     &         ,IBEL(NELM)` (6); `      DO I = 1, NNOD` (8); `        IFR = INDOP(I)` (9); `        IF( IFR > 0 ) THEN` (10); `          DPG(I) = DP(IFR)` (11); `        ELSEIF( IFR == 0 ) THEN` (12); `          DPG(I) = 0.` (13); `        ENDIF` (14); `      ENDDO` (15); `      PG(1:NNOD) = PG(1:NNOD) + DPG(:)` (17); `      IF( IMPC > 0 ) CALL GSURF(PG(NNOD+NNODC+1),PG,IELM,NM,NELM,IBEL,1)` (19); `      END` (21) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–14·17: IFR<0에 대해 DPG(I)를 대입하는 분기는 없다. 다음 PG 누적은 DPG 전체를 사용한다.

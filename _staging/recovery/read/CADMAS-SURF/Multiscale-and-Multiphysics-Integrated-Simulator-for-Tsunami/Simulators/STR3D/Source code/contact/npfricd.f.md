---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/npfricd.f
lines: 41
sha256: 0d929416a335ad482397ca7c25863ecb0c3c8435b5b0f2796a4bcec238bbf8b5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# npfricd.f — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | NPFRICD는 마찰력(friction force)의 변위 증분(displacement increment) 기여를 FTI에 더한다. NINDC 루프에서 IFRIC(1,I)=0인 항을 건너뛰고 NS,IST,MA를 읽는다(11–17). 인수·배열 선언과 주석을 포함한다. 원문: 연속문(1–3): `      SUBROUTINE NPFRICD(FTI,NINDC,ISLV,INDC,IEDG,IELC,IELQ,IEDQ,IFCQ` (1); `     &                  ,IFRIC,U0,RL0,FRIC,UG,DUG,IFMDL,MITER0,IDYN,BETA` (2); `     &                  ,DT,ITER)` (3). `      IMPLICIT REAL*8(A-H,O-Z)` (5). 연속문(6–9): `      DIMENSION U0(3,4,NINDC),RL0(3,NINDC),ISLV(2,NINDC),INDC(NINDC)` (6); `     &         ,IEDG(6,*),IELC(3,*),UG(6,*),IFRIC(10,NINDC)` (7); `     &         ,FRIC(10,NINDC),KN(5),ESTF(120),DUG(6,*),IELQ(4,*)` (8); `     &         ,IFCQ(*),IEDQ(*),FTI(6,*),DFC(3,20)` (9). `      DO I = 1, NINDC` (11). `        IF( IFRIC(1,I) == 0 ) CYCLE` (13). `        NS = INDC(I)` (15). `        IST = ISLV(1,I)` (16). `        MA  = ISLV(2,I)` (17). |
| 19–29 | 시작 시 1–3행 NPFRICD 루틴·11행 `DO I = 1, NINDC` 안. 이 루프는 39행 `ENDDO`에서 닫힌다. IST=2이면 ESTFEDGE를 호출하고 IST=3이면 ESTFFACE를 호출하여 ND,KN,ESTF를 받는다(19–28). 각 호출은 U0,RL0,FRIC,UG 및 시간·모델 인수를 전달한다. 원문: `        IF( IST == 2 ) THEN` (19). 연속문(20–22): `          CALL ESTFEDGE(ND,KN,ESTF,NS,IEDG(1,MA),IEDQ(MA),IELQ,U0(1,1,I)` (20); `     &                 ,RL0(1,I),FRIC(1,I),FRIC(2,I),FRIC(3,I),FRIC(6,I)` (21); `     &                 ,UG,DT,IFMDL)` (22). `        ELSEIF( IST == 3 ) THEN` (23). 연속문(24–27): `          CALL ESTFFACE(ND,KN,ESTF,NS,IELC(1,MA),IFCQ(MA),IELQ,U0(1,1,I)` (24); `     &                 ,RL0(1,I),IFRIC(2,I),IFRIC(3,I),IFRIC(9,I)` (25); `     &                 ,FRIC(1,I),FRIC(2,I),FRIC(3,I),FRIC(6,I),UG,DT` (26); `     &                 ,IFMDL,MITER0,IDYN,ITER)` (27). `        ENDIF` (28). 19–28행 IST 분기 사슬에는 ELSE가 없다. [11-04 전수 검증 보완] |
| 30–41 | 시작 시 1–3행 NPFRICD 루틴·11행 `DO I = 1, NINDC` 안. 이 루프는 39행 `ENDDO`에서 닫힌다. IDYN=1이면 N을 `3*ND * ( 3*ND + 1 ) / 2`로 구한다(30–31). ESTF(1:N)에 BETA를 곱한다(32). 해석: N은 3*ND 자유도의 삼각형 저장 항 수이다. ENPFRCD로 DFC를 계산하고 KN 절점의 FTI에 더한다(35–37). 루프 종료와 END를 포함한다. 원문: `        IF( IDYN == 1 ) THEN` (30). `          N = 3*ND * ( 3*ND + 1 ) / 2` (31). `          ESTF(1:N) = BETA * ESTF(1:N)` (32). `        ENDIF` (33). `        CALL ENPFRCD(DFC,ESTF,DUG,KN,3,ND)` (35). `        FTI(1:3,KN(1:ND)) = FTI(1:3,KN(1:ND)) + DFC(:,1:ND)` (37). `      ENDDO` (39). `      END` (41). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–37: IFRIC(1,I)가 0이 아니고 IST가 2,3 모두 아니면 ND,KN,ESTF를 설정하는 호출 없이 후속 계산으로 진행한다.

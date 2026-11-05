---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/force.f
lines: 21
sha256: 0b2acc2a05584012191b45f5b6ff1108b5632931ed67c532aeefa913a380ea9b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# force.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | FORCE의 배열 선언과 I=1..NN 반복 구간이다. 해석: 절점별 하중을 처리한다. ID가 0이면 SHIFT1에 FC0·FC(1,I)·6을 전달한다. 해석: 여섯 성분을 복사한다. ELSE에서는 TRNSMTX6를 호출한다. AXB에 FC(1,I)와 FC(4,I)를 각각 전달한다. 해석: 앞뒤 세 성분을 각각 변환한다. RMULT2에 FT·FC0·SI·6을 전달하고 루틴을 끝낸다. 원문: `      SUBROUTINE FORCE(NN,FC,NFC,SI,ICRD,TR,GRID,FT,ITO)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； 연속문(4–5): `      DIMENSION FT(6,*),NFC(2,NN),FC(6,NN),FC0(6),TRG(9),ICRD(*)` (4)； `     &         ,GRID(3,*),TR(12,*)` (5)； `      DO 100 I=1,NN` (7)； `        II=NFC(1,I)` (8)； `        ID=NFC(2,I)` (9)； `        IF( ID .EQ. 0 ) THEN` (10)； `          CALL SHIFT1(FC0,FC(1,I),6)` (11)； `        ELSE` (12)； `          CALL TRNSMTX6(TRG,ICRD(ID),GRID(1,II),TR(1,ID),ITO)` (13)； `          CALL AXB(FC0(1),TRG,FC(1,I),3,3,1)` (14)； `          CALL AXB(FC0(4),TRG,FC(4,I),3,3,1)` (15)； `        ENDIF` (16)； `        CALL RMULT2(FT(1,II),FC0,SI,6)` (17)； `  100 CONTINUE` (18)； `      RETURN` (20)； `      END` (21)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

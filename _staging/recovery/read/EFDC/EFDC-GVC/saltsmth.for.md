---
file: models/EFDC/raw/source_code/EFDC-GVC/saltsmth.for
lines: 190
sha256: 77b0a239b9598562f252a9d9406196d25e9afcb88f21e0ffed97a51751ad269c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# saltsmth.for — 판독 구간 기록

구간은 1행부터 190행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 머리말·변경 이력 주석과 `SUBROUTINE SALTSMTH` 선언(1–20). `EFDC.PAR`·`EFDC.CMN`을 포함한다(21–22). `IF(NSBMAX.GT.10)  GOTO 1001` (26)로 특수 염분(salinity) 초기화 버전 2에 진입한다. 비활성 대체 분기는 `C     IF(NSBMAX.GT.10)THEN` (27), `C       IF(MOD(NSBMAX,10).EQ.0) GOTO 1000` (28)이며 나머지도 주석이다(29–31). 구분 주석까지 포함한다(32–34). |
| 35–73 | 시작 시 6행 SALTSMTH 루틴 안. K=1..KC에서 SAL을 TVAR3S로 복사한다(35–39). NSM=1..NSBMAX·L=2..LA 반복에서 `IF(LCT(L).GT.0.AND.LCT(L).LT.9)THEN` (44)이면 네 이웃 값을 가져온다(45–50). `IF(IJCT(I  ,J+1).EQ.9) HTN=TVAR3S(L)` (51), `IF(IJCT(I  ,J-1).EQ.9) HTS=TVAR3S(L)` (52), `IF(IJCT(I+1,J  ).EQ.9) HTE=TVAR3S(L)` (53), `IF(IJCT(I-1,J  ).EQ.9) HTW=TVAR3S(L)` (54)로 경계 이웃을 현재 셀 값으로 치환한다. 평활화(smoothing) 식은 `TVAR3N(L)=(1.-WSMB)*TVAR3S(L)+0.25*WSMB*(HTN+HTS+HTE+HTW)` (55). 모든 L의 TVAR3N을 TVAR3S로 복사한다(59–61). NSM 반복 뒤 SAL·SAL1을 TVAR3N으로 바꾸고(65–68), K 반복을 닫은 뒤 `GOTO 2000` (72)으로 종료부에 간다. |
| 74–131 | 시작 시 6행 SALTSMTH 루틴 안. 특수 초기화 버전 1 블록 전체가 주석이다(74–131). 비활성 K·NSM·L 반복과 이웃 복사(80–97)에 이어 `C       IF(LCT(L).GT.0.AND.LCT(L).LT.9)THEN` (91), `C        IF(IJCT(I  ,J+1).EQ.9) HTN=TVAR3S(L)` (98), `C        IF(IJCT(I  ,J-1).EQ.9) HTS=TVAR3S(L)` (99), `C        IF(IJCT(I+1,J  ).EQ.9) HTE=TVAR3S(L)` (100), `C        IF(IJCT(I-1,J  ).EQ.9) HTW=TVAR3S(L)` (101)을 적는다. 비활성 계산은 `C        TVAR3N(L)=(1.-WSMB)*TVAR3S(L)+0.25*WSMB*(HTN+HTS+HTE+HTW)` (102). `C        IF(SALINIT(L,K).GT.0.0) TVAR3N(L)=SALINIT(L,K)` (107)은 양의 초기 염분을 덮어쓰는 주석 코드다. TVAR3S·SAL·SAL1 복사와 완료 출력도 주석이다(110–122). `C     CALL SALPLTH(1,SAL)` (124)은 실행되지 않는다. 버전 2 제목·구분 주석을 포함한다(126–131). |
| 132–160 | 시작 시 6행 SALTSMTH 루틴 안. 1001 레이블(132) 뒤 K=1..KC에서 SAL을 TVAR3S로 복사한다(134–138). NSM=1..NSBMAX·L=2..LA에서 북·남 인덱스를 구한다(140–144). 가중 차분은 `TVAR3N(L)=TVAR3S(L)+(WSMB/HMP(L))` (145), 연속행 `     &        *( HRU(L+1)*(TVAR3S(L+1)-TVAR3S(L  ))` (146), `     &          -HRU(L  )*(TVAR3S(L  )-TVAR3S(L-1))` (147), `     &          +HRV(LN )*(TVAR3S(LN )-TVAR3S(L  ))` (148), `     &          -HRV(L  )*(TVAR3S(L  )-TVAR3S(LS )) )` (149)이다. `IF(SALINIT(L,K).GT.0.0) TVAR3N(L)=SALINIT(L,K)` (153)로 양의 지정값을 적용한다. TVAR3N을 TVAR3S에 복사하고 NSM 반복을 닫는다(156–160). |
| 161–181 | 시작 시 6행 SALTSMTH 루틴·134행 K 루프 안. L=2..LA의 SAL·SAL1을 TVAR3N으로 바꾸고 K·NSM 완료 메시지를 출력한 뒤 K 루프를 닫는다(162–168). `NEWSALT.INP`를 열고 삭제한 뒤 다시 연다(170–172). IONE=1을 쓰고 L=2..LC−1에서 L·IL·JL·전체 K의 SAL을 출력한 뒤 닫는다(173–178). `C     CALL SALPLTH(1,SAL)` (180)은 주석이다. |
| 182–190 | 시작 시 6행 SALTSMTH 루틴 안. 구분 주석(182–183), 버전 1·2 완료 형식 6000·6001(184–185), 정수 1개 형식 9101(186), `9102 FORMAT(3I5,12F6.2)` (187)을 정의한다. 2000 레이블·RETURN·END로 끝난다(188–190). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44–60: 일반 평활화는 LCT 조건을 만족하는 셀에만 TVAR3N을 대입한다. 뒤의 복사는 모든 L=2..LA의 TVAR3N을 읽는다.
- 35–68 및 134–165: NSM 반복 밖에서 TVAR3N을 초기화하는 문장은 없다. 두 경로 모두 NSM 반복 뒤 TVAR3N을 SAL·SAL1에 복사한다.
- 26–31·80–124: 실행 중인 경로 선택은 NSBMAX>10 검사 한 개다. 버전 1 특수 초기화는 전부 주석이다.
- 145–149: 버전 2 계산은 HMP(L)을 분모로 사용한다. 이 블록에는 HMP(L)=0 검사가 없다.
- 175–187: 출력은 KC개 SAL 값을 전달한다. 형식 9102에는 12개의 F6.2 필드가 지정되어 있다.

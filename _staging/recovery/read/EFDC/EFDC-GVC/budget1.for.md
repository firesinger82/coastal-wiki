---
file: models/EFDC/raw/source_code/EFDC-GVC/budget1.for
lines: 164
sha256: 0ec9422839b34a1dbc467df8a4832164c2b4e1a71faba8b18ee2c87892abef83
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# budget1.for — 판독 구간 기록

구간은 1행부터 164행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | BUDGET1 입구(6). 작성자·버전·수정 이력과 전체 퇴적물(sediment) 수지(budget) 목적(8–23). EFDC.PAR·EFDC.CMN 포함(27–28). NBUD>1이면 RETURN한다(32). 수량·염분(salt)·퇴적물 및 플럭스(flux) 초기화 주석(36–39). 원문: `IF(NBUD.GT.1) RETURN` (32). |
| 40–59 | 시작 시 6행 BUDGET1 루틴 안. 초기 체적·염분 질량·하상(sediment bed) 질량·부유 퇴적물(suspended sediment) 질량·퇴적물 유출입·체적 유출입·염분 유출입을 0으로 만든다(40–49). K=1..KB·L=2..LA의 SEDBT·SNDBT를 0으로 만든다(53–58). 원문: `VOLMBEG=0.` (40). `SMASSBEG=0.` (41). `BSEDBEG=0.` (42). `SSEDBEG=0.` (43). `SEDIN=0.` (44). `SEDOUT=0.` (45). `VOLMOUT=0.` (46). `SMASSOUT=0.` (47). `VOLMIN=0.` (48). `SMASSIN=0.` (49). `SEDBT(L,K)=0.` (55). `SNDBT(L,K)=0.` (56). |
| 60–100 | 시작 시 6행 BUDGET1 루틴 안. N≤1이면 종류별 SEDB1·SNDB1을 합산한다(60–75). N>1이면 SEDB·SNDB를 합산한다(77–92). 수층(water column)·하상 교환 누적용이라는 VOLBW3 주석(93). K=1..KB·L=2..LA에서 VOLBW3=0을 설정하고 SCB·DXYP·종류별 질량 합으로 BSEDBEG를 더한다(94–99). 원문: `IF(N.LE.1)THEN` (60). `SEDBT(L,K)=SEDBT(L,K)+SEDB1(L,K,NS)` (64). `SNDBT(L,K)=SNDBT(L,K)+SNDB1(L,K,NS)` (71). `IF(N.GT.1)THEN` (77). `SEDBT(L,K)=SEDBT(L,K)+SEDB(L,K,NS)` (81). `SNDBT(L,K)=SNDBT(L,K)+SNDB(L,K,NS)` (88). `VOLBW3(L,K)=0.` (96). `BSEDBEG=BSEDBEG+SCB(L)*DXYP(L)*(SEDBT(L,K)+SNDBT(L,K))` (97). |
| 101–138 | 시작 시 6행 BUDGET1 루틴 안. N≤1은 H1P·SED1·SND1, N>1은 HP·SED·SND를 사용한다(101–133). 각 경로는 종류·수층 K=1..KC·L=2..LA의 SCB·면적·수심·농도·DZC를 곱해 SSEDBEG를 합산한다(105·112·122·129). SEDBEG는 하상과 부유 질량 합이다(135). 원문: `IF(N.LE.1)THEN` (101). `SSEDBEG=SSEDBEG+SCB(L)*DXYP(L)*H1P(L)*SED1(L,K,NS)*DZC(K)` (105). `SSEDBEG=SSEDBEG+SCB(L)*DXYP(L)*H1P(L)*SND1(L,K,NS)*DZC(K)` (112). `IF(N.GT.1)THEN` (118). `SSEDBEG=SSEDBEG+SCB(L)*DXYP(L)*HP(L)*SED(L,K,NS)*DZC(K)` (122). `SSEDBEG=SSEDBEG+SCB(L)*DXYP(L)*HP(L)*SND(L,K,NS)*DZC(K)` (129). `SEDBEG=BSEDBEG+SSEDBEG` (135). |
| 139–164 | 시작 시 6행 BUDGET1 루틴 안. N≤1이면 H1P로 VOLMBEG, SAL1으로 SMASSBEG를 더한다(139–148). N>1이면 HP·SAL을 사용한다(150–159). 체적은 SPB·면적·수심을 곱하고 염분 질량은 SCB·면적·수심·염분·DZC를 곱한다(141·145·152·156). 마지막 주석·RETURN·END로 끝난다(160–164). 원문: `IF(N.LE.1)THEN` (139). `VOLMBEG=VOLMBEG+SPB(L)*DXYP(L)*H1P(L)` (141). `SMASSBEG=SMASSBEG+SCB(L)*DXYP(L)*H1P(L)*SAL1(L,K)*DZC(K)` (145). `IF(N.GT.1)THEN` (150). `VOLMBEG=VOLMBEG+SPB(L)*DXYP(L)*HP(L)` (152). `SMASSBEG=SMASSBEG+SCB(L)*DXYP(L)*HP(L)*SAL(L,K)*DZC(K)` (156). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60–92·101–133·139–159: 초기 집계는 N≤1에서 이름에 1이 붙은 상태 배열을 사용한다. N>1에서는 현재 상태 배열을 사용한다.
- 61–91·102–132: 퇴적물 합계 루프에는 종류 수 반복 범위만 있다. 이 파일에는 ISTRAN(6)·ISTRAN(7) 조건이 없다.
- 97·105·112·122·129·141·145·152·156: 체적 집계는 SPB를 사용한다. 퇴적물·염분 질량 집계는 SCB를 사용한다.
- 32·94–99: NBUD>1의 RETURN은 VOLBW3를 0으로 만드는 루프보다 앞에 있다.


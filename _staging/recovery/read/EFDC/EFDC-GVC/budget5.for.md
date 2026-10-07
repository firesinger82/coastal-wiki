---
file: models/EFDC/raw/source_code/EFDC-GVC/budget5.for
lines: 339
sha256: 663f189d337c9536d8294d7c23ae51f82970ffd1c126699f4ab8ea7d0b2702d8
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# budget5.for — 판독 구간 기록

구간은 1행부터 339행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–43 | BUDGET5 입구와 작성자·버전·수정 이력, 전체 퇴적물(sediment) 수지(budget) 목적(6–23). EFDC.PAR·EFDC.CMN 포함(27–28). NBUD=NTSMMT일 때만 기간 말 집계 분기를 연다(34). 호출 진단 WRITE는 주석이고 FORMAT 6666은 남아 있다(35–36). 영역 말 부유 퇴적물(suspended sediment)·하상(sediment bed) 집계 주석(40–43). 원문: `IF(NBUD.EQ.NTSMMT)THEN` (34). |
| 44–73 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. SDFLUX·SSEDEND·BSEDEND·VOLMEND·SMASSEND를 0으로 만든다(44–48). N=NTSMMT이면 이전 H1P로 체적을 계산하고 ELSE는 HP를 사용한다(50–58). 염분(salt) 질량도 N=NTSMMT이면 H1P·SAL1, ELSE는 HP·SAL을 사용하며 K=1..KC·L=2..LA에서 합산한다(60–72). 원문: `SDFLUX=0.` (44). `SSEDEND=0.` (45). `BSEDEND=0.` (46). `VOLMEND=0.` (47). `SMASSEND=0.` (48). `IF(N.EQ.NTSMMT)THEN` (50). `VOLMEND=VOLMEND+SPB(L)*DXYP(L)*H1P(L)` (52). `ELSE` (54). `VOLMEND=VOLMEND+SPB(L)*DXYP(L)*HP(L)` (56). `IF(N.EQ.NTSMMT)THEN` (60). `SMASSEND=SMASSEND+SCB(L)*DXYP(L)*H1P(L)*SAL1(L,K)*DZC(K)` (63). `ELSE` (66). `SMASSEND=SMASSEND+SCB(L)*DXYP(L)*HP(L)*SAL(L,K)*DZC(K)` (69). |
| 74–125 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. L=2..LA의 SCB*VOLBW3(L,KB)를 SDFLUX에 더한다(76–78). 하상 총합 배열을 0으로 만든다(80–85). N=NTSMMT이면 SEDB1·SNDB1, ELSE는 SEDB·SNDB에 SCB를 곱해 합산한다(88–118). BSEDEND 집계에서 SCB·면적을 다시 곱한다(120–124). 원문: `SDFLUX=SDFLUX+SCB(L)*VOLBW3(L,KB)` (77). `SEDBT(L,K)=0.` (82). `SNDBT(L,K)=0.` (83). `IF(N.EQ.NTSMMT)THEN` (88). `SEDBT(L,K)=SEDBT(L,K)+SCB(L)*SEDB1(L,K,NS)` (92). `SNDBT(L,K)=SNDBT(L,K)+SCB(L)*SNDB1(L,K,NS)` (99). `ELSE` (103). `SEDBT(L,K)=SEDBT(L,K)+SCB(L)*SEDB(L,K,NS)` (107). `SNDBT(L,K)=SNDBT(L,K)+SCB(L)*SNDB(L,K,NS)` (114). `BSEDEND=BSEDEND+SCB(L)*DXYP(L)*(SEDBT(L,K)+SNDBT(L,K))` (122). |
| 126–157 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. N=NTSMMT이면 H1P·SED1·SND1로, ELSE는 HP·SED·SND로 부유 질량을 합산한다(126–156). 반복 범위는 점착성(cohesive)·비점착성(noncohesive) 종류, K=1..KC·L=2..LA이다. 각 항은 SCB·면적·수심·농도·DZC를 곱한다(130·137·145·152). 원문: `IF(N.EQ.NTSMMT)THEN` (126). `SSEDEND=SSEDEND+SCB(L)*DXYP(L)*H1P(L)*SED1(L,K,NS)*DZC(K)` (130). `SSEDEND=SSEDEND+SCB(L)*DXYP(L)*H1P(L)*SND1(L,K,NS)*DZC(K)` (137). `ELSE` (141). `SSEDEND=SSEDEND+SCB(L)*DXYP(L)*HP(L)*SED(L,K,NS)*DZC(K)` (145). `SSEDEND=SSEDEND+SCB(L)*DXYP(L)*HP(L)*SND(L,K,NS)*DZC(K)` (152). |
| 158–182 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. SEDEND는 부유·하상 질량 합이다(158). 누적 퇴적물·수량·염분 유출입 및 교환량에 DT를 곱한다(159–165). 예상 말 질량·체적과 실제 말 값의 차이를 계산한다(167–173). 두 상대 오차(relative error)를 -9999로 시작한다(175–177). SEDEND≠0이면 RSDERDE, SEDOUT≠0이면 RSDERDO를 계산한다(179–181). 원문: `SEDEND=SSEDEND+BSEDEND` (158). `SEDOUT=DT*SEDOUT` (159). `SEDIN=DT*SEDIN` (160). `VOLMOUT=DT*VOLMOUT` (161). `VOLMIN=DT*VOLMIN` (162). `SMASSIN=DT*SMASSIN` (163). `SMASSOUT=DT*SMASSOUT` (164). `SDFLUX=DT*SDFLUX` (165). `SEDBMO=SEDBEG+SEDIN-SEDOUT` (167). `VOLMBMO=VOLMBEG+VOLMIN-VOLMOUT` (168). `SMASSBMO=SMASSBEG+SMASSIN-SMASSOUT` (169). `SEDERR=SEDEND-SEDBMO` (171). `VOLMERR=VOLMEND-VOLMBMO` (172). `SMASSERR=SMASSEND-SMASSBMO` (173). `RSDERDE=-9999.` (175). `RSDERDO=-9999.` (177). `IF(SEDEND.NE.0.) RSDERDE=SEDERR/SEDEND` (179). `IF(SEDOUT.NE.0.) RSDERDO=SEDERR/(SEDIN+SEDOUT)` (181). |
| 183–216 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. JSSBAL=1이면 BUDGET.OUT·BUDGET2.OUT·BUDGET3.OUT을 삭제 후 재생성하고 기간·시작일 머리말을 쓴다(189–205). BUDGETH.OUT·BUDGETF.OUT 조작은 주석이다(193–194·198–199·206–207). JSSBAL=0으로 바꾼다(208). ELSE는 세 파일을 추가 쓰기(append)로 연다(209–215). 원문: `IF(JSSBAL.EQ.1)THEN` (189). `JSSBAL=0` (208). `ELSE` (209). |
| 217–239 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. 퇴적물·수량·염분 결과를 유닛(unit) 89·93·94에 출력한다(217–223). SDFLUX를 포함한 부유·하상 예상 질량과 오차를 계산한다(226–229). SSEDOUT·BSEDOUT을 정의한 뒤 예상 질량·오차를 다시 계산한다(231–236). 말 질량이 0이 아닐 때만 부유·하상 상대 오차를 계산한다(237–238). 원문: `SSEDBMO=SSEDBEG+SEDIN-SEDOUT+SDFLUX` (226). `BSEDBMO=BSEDBEG-SDFLUX` (227). `SSEDERR=SSEDEND-SSEDBMO` (228). `BSEDERR=BSEDEND-BSEDBMO` (229). `SSEDOUT=SEDOUT-SEDIN-SDFLUX` (231). `BSEDOUT=SDFLUX` (232). `SSEDBMO=SSEDBEG-SSEDOUT` (233). `BSEDBMO=BSEDBEG-BSEDOUT` (234). `SSEDERR=SSEDEND-SSEDBMO` (235). `BSEDERR=BSEDEND-BSEDBMO` (236). `IF(SSEDEND.NE.0.)SSEDERE=SSEDERR/SSEDEND` (237). `IF(BSEDEND.NE.0.)BSEDERE=BSEDERR/BSEDEND` (238). |
| 240–264 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. 부유·하상 상세 출력과 유닛 96 머리말은 주석이다(240–249). L=2..LA에서 VOLBW3(L,KB)에 DT를 곱한다(250–251). 종류 1의 이전 표층 질량, 현재 KB층 질량, 하상 교환량을 계산한다(252–254). 이를 쓰는 WRITE는 주석이다(255–256). 실제 세 결과 파일을 닫는다(259–261). 원문: `VOLBW3(L,KB)=DT*VOLBW3(L,KB)` (251). `SEDBTMP1=DXYP(L)*SEDB1(L,KBT(L),1)` (252). `SEDBTMP=DXYP(L)*SEDB(L,KB,1)` (253). `SFLXTMP=DT*DXYP(L)*SEDF(L,0,1)` (254). |
| 265–296 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. 주석 처리된 상세 진단용 FORMAT 9510..9517·9600·9601을 정의한다(265–274). FORMAT 888은 퇴적물 수지 목적·기간·시작일·변수 설명과 열 이름을 정의한다(276–294). FORMAT 892는 N과 실수 10개 출력 형식이다(295). |
| 297–325 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. FORMAT 893은 수량 수지 설명과 열 이름이다(297–309). 머리말의 VOLMBMO 식은 VOLMBEG-(VOLMIN+VOLMOUT)로 적혀 있다(305). FORMAT 894는 염분 수지 제목과 변수·열 설명이다(311–323). 여러 설명은 물 체적과 VOLM 변수 이름을 사용한다(315–321). FORMAT 895는 N과 실수 6개 형식이다(324). |
| 326–339 | 시작 시 6행 BUDGET5 루틴·34행 기간 말 집계 분기 안. 주석 뒤 NBUD=0으로 기간 계수기를 재설정한다(328–330). 기간 말 분기가 닫힌다(332). 해당 분기 밖에서 매 호출 NBUD에 1을 더한다(334). 마지막 주석·RETURN·END로 끝난다(336–339). 원문: `NBUD=0` (330). `NBUD=NBUD+1` (334). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 92·99·107·114·122: 종류별 하상 총합에 SCB를 곱한다. BSEDEND 집계는 해당 총합에 SCB를 다시 곱한다.
- 159–165·251: 누적 유출입과 교환량을 DT로 곱한다. 이 파일에는 ISDYNSTP 또는 TIMESEC 조건이 없다.
- 175–181: RSDERDO 초기값은 -9999이다. 계산 조건은 SEDOUT≠0이다. 계산 분모는 SEDIN+SEDOUT이다. 분모 합이 0인지 검사하는 조건은 없다.
- 237–238: SSEDERE·BSEDERE 대입은 각각 SSEDEND≠0·BSEDEND≠0 조건 안에만 있다. 이 루틴에는 해당 변수의 기본값 대입이나 ELSE 대입이 없다.
- 76–78·251–254: 교환량 집계와 DT 갱신의 층 인덱스는 KB이다. SEDBTMP1은 KBT(L)의 종류 1을 사용한다. SEDBTMP는 KB의 종류 1을 사용한다.
- 250–257: VOLBW3의 DT 갱신과 임시 질량·플럭스 계산은 실행문이다. 해당 값을 쓰는 WRITE는 주석이다.
- 168·305: 실행 VOLMBMO 식은 VOLMBEG+VOLMIN-VOLMOUT이다. 출력 머리말의 식은 VOLMBEG-(VOLMIN+VOLMOUT)이다.
- 169·173·315–321: 실제 염분 수지는 SMASSBEG·SMASSIN·SMASSOUT·SMASSEND를 사용한다. 염분 출력 설명은 물 체적 및 VOLM 변수 식을 적는다.
- 50·60·88·126: 이전 상태 배열을 사용하는 조건은 N=NTSMMT이다. 바깥 기간 말 집계 조건은 NBUD=NTSMMT이다.


---
file: models/EFDC/raw/source_code/EFDC-GVC/bedplth.for
lines: 300
sha256: ce2bd8462c49e0d66dbc75c185b14734acf9ec43cbdfcf7e7e023ca8fb542aa3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# bedplth.for — 판독 구간 기록

구간은 1행부터 300행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | BEDPLTH 입구와 하상(sediment bed) 속성 출력 목적(6·21). 소류사(bed load) 출력 추가 이력(16–17). EFDC.PAR·EFDC.CMN 포함(25–26). 제어 주석은 ISBPH의 1·2, ISBEXP의 0=ASCII·1=Explorer 바이너리(binary), NPBPH·ISRBPH, 밀도·두께·공극률(porosity)·간극비(void ratio) 및 퇴적물 출력 옵션을 설명한다(30–46). |
| 50–96 | 시작 시 6행 BEDPLTH 루틴 안. JSBPH=1의 최초 호출 분기를 연다(50). ISBEXP=0이면 BEDSUM·BEDSED·BEDSND·BEDVDR·BEDPOR·BEDLAY·BEDBDN.OUT을 각각 삭제 후 재생성하고 머리말을 쓴다(52–94). ASCII 분기가 닫힌다(96). 원문: `IF(JSBPH.EQ.1)THEN` (50). `IF(ISBEXP.EQ.0)THEN` (52). |
| 97–121 | 시작 시 6행 BEDPLTH 루틴·50행 JSBPH=1 분기 안. BEDARD.OUT은 ISBEXP 분기 밖에서 삭제 후 재생성하고 머리말을 쓴다(98–102). BEDBDL.OUT·BEDTOX.OUT 생성 코드는 주석이다(104–116). JSBPH=0으로 바꾼 뒤 최초 호출 분기를 닫는다(118–120). 원문: `JSBPH=0` (118). |
| 122–143 | 시작 시 6행 BEDPLTH 루틴 안. ISDYNSTP=0이면 DT·N·TBEGIN·TCON으로 출력 시간을 계산한다(124–126). ELSE는 TIMESEC/TCON이다(127–129). 전체 종류 수 NSXD=NSED+NSND를 계산한다(131). ISBEXP=0 출력 분기를 연다(133). BEDSUM.OUT에 시간과 셀별 KBT·BELV·표층 두께·간극비·종류별 체적 분율(volume fraction)을 추가한다(135–142). 원문: `IF(ISDYNSTP.EQ.0)THEN` (124). `TIME=DT*FLOAT(N)+TCON*TBEGIN` (125). `TIME=TIME/TCON` (126). `ELSE` (127). `TIME=TIMESEC/TCON` (128). `NSXD=NSED+NSND` (131). `IF(ISBEXP.EQ.0)THEN` (133). `KTMP=KBT(L)` (138). |
| 144–169 | 시작 시 6행 BEDPLTH 루틴·133행 ISBEXP=0 분기 안. ISBSED≥1이면 BEDSED.OUT을 추가 쓰기(append)로 연다(144–146). ISBSED=1은 SEDB 단위면적 질량을 출력한다(147–156). ISBSED≥2는 VFRBED를 출력한다(157–166). 두 경로는 L=2..LA·K=1..KB의 첫 종류를 먼저 쓰고 NSED>1이면 나머지 종류를 쓴다(148–165). 파일을 닫는다(167–168). 원문: `IF(ISBSED.GE.1)THEN` (144). `IF(ISBSED.EQ.1)THEN` (147). `IF(NSED.GT.1) THEN` (150). `IF(ISBSED.GE.2)THEN` (157). `IF(NSED.GT.1) THEN` (160). |
| 170–195 | 시작 시 6행 BEDPLTH 루틴·133행 ISBEXP=0 분기 안. ISBSND≥1이면 BEDSND.OUT을 연다(170–172). ISBSND=1은 SNDB 질량, ISBSND≥2는 VFRBED의 비점착성(noncohesive) 종류를 출력한다(173–192). 첫 체적 분율 인덱스는 NSED+1이다(185). NSND>1이면 질량 종류 2..NSND 또는 체적 종류 NSED+2..NSED+NSND를 추가한다(176–190). 파일을 닫는다(193–194). 원문: `IF(ISBSND.GE.1)THEN` (170). `IF(ISBSND.EQ.1)THEN` (173). `IF(NSND.GT.1)THEN` (176). `IF(ISBSND.GE.2)THEN` (183). `IF(NSND.GT.1)THEN` (186). |
| 196–232 | 시작 시 6행 BEDPLTH 루틴·133행 ISBEXP=0 분기 안. ISBVDR≥1·ISBPOR≥1·ISBLAY≥1·ISBBDN≥1의 독립 분기를 검사한다(196·205·214·224). 각 출력은 시간과 L=2..LA·K=1..KB의 간극비, 공극률, 하상 바닥 표고(bed bottom elevation)·총 두께·각 층 두께, 용적밀도(bulk density)를 추가한다(197–231). 원문: `IF(ISBVDR.GE.1)THEN` (196). `IF(ISBPOR.GE.1)THEN` (205). `IF(ISBLAY.GE.1)THEN` (214). `IF(ISBBDN.GE.1)THEN` (224). |
| 233–246 | 시작 시 6행 BEDPLTH 루틴·133행 ISBEXP=0 분기 안. ISBARD≥1이면 BEDARD.OUT에 시간과 셀별 점착성(cohesive)·비점착성 종류의 SEDFDTAP·SEDFDTAN·SNDFDTAP·SNDFDTAN 쌍을 출력한다(233–242). ASCII 출력 분기가 닫힌다(245). 원문: `IF(ISBARD.GE.1)THEN` (233). |
| 247–269 | 시작 시 6행 BEDPLTH 루틴 안. QSBDLDX·QSBDLDY의 BEDBDL.OUT 출력 및 TOXB의 BEDRST.TOX 출력 블록은 전부 주석이다(247–268). 이 구간에는 실행되는 출력 문장이 없다. |
| 270–300 | 시작 시 6행 BEDPLTH 루틴 안. 좌표·속성 및 각 파일 머리말 FORMAT을 정의한다(270–286). 시간 및 추가 수치 형식 122·906..913을 정의한다(287–295). 주석·RETURN·END로 루틴이 끝난다(296–300). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34·52·133–245: 주석은 ISBEXP=1 바이너리 출력을 설명한다. 이 파일의 실제 속성 출력 분기는 ISBEXP=0뿐이다.
- 40–45·157–166·183–192: 주석은 출력 옵션 2와 3을 서로 다른 질량 분율로 설명한다. 실행 코드는 옵션 ≥2에서 같은 VFRBED를 출력한다. 비점착성 옵션 주석의 변수 이름도 ISBSED로 적혀 있다.
- 52–96·98–102·233–245: BEDARD.OUT 초기 생성은 ISBEXP 검사 밖에 있다. BEDARD.OUT 값 출력은 ISBEXP=0 분기 안에 있다.
- 16–17·104–108·247–258: 수정 이력은 소류사 수송량 출력을 추가했다고 적는다. 실제 파일 생성과 QSBDLDX·QSBDLDY 출력 블록은 주석이다.
- 139–140·274: BEDSUM.OUT 값 출력은 KBT 뒤에 BELV·HBED·VDRBED를 쓴다. 머리말은 KBT·HTOP·VOIDR을 적고 BELV에 대응하는 별도 이름은 적지 않는다.


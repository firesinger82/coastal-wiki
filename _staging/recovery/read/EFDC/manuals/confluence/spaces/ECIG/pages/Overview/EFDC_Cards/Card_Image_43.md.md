---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_43.md
lines: 52
sha256: dc91a13c182f8f54050a8a3bea9c915f28b0cd5be61dd5f00002e2e75e002a17
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_43.md — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | C43 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 독성 오염물질(toxic contaminant) 초기조건(initial conditions) 및 매개변수 제목을 제시한다(10). 물·퇴적물 상(phase)의 독성 물질 농도와 C44–C46 분배 계수(partition coefficient)의 단위 변경을 허용하되 의미 있는 결과에는 일관된 단위를 반드시 써야 한다고 적는다(12–16). ISTRAN(5)=0일 때도 자료가 필요하다고 적는다(18). 빈 줄과 주석 표식도 포함한다(11–21). 원문: ` C43 TOXIC CONTAMINANT INITIAL CONDITIONS AND PARAMETERS ` (10); ` \* USER MAY CHANGE UNITS OF WATER AND SED PHASE TOX CONCENTRATION ` (12); ` \* AND PARTIATION COEFFICIENT ON C44 - C46 BUT CONSISTENT UNITS MUST ` (14); ` \* MUST BE USED FOR MEANINGFUL RESULTS ` (16); ` \* DATA REQUIRED EVEN IT ISTRAN(5) IS 0 ` (18). |
| 22–31 | 물질 식별자와 초기화 유형 — 독성 물질 식별자를 정의하며 기본 자료 행 수는 1이라고 적는다(22). 수주(water column)와 하상(bed)의 공간 일정 초기조건, 수주만·하상만·두 영역 모두 공간 가변인 초기조건 옵션을 구분한다(24–30). 원문: ` \* NTOXN: TOXIC CONTAMINANT NUMBER ID (1 LINE OF DATA BY DEFAULT) ` (22); ` \* ITXINT: 0 FOR SPATIALLY CONSTANT WATER COL AND BED INITIAL CONDITIONS ` (24); ` \*             1 FOR SPATIALLY VARIABLE WATER COLUMN INITIAL CONDITIONS ` (26); ` \*             2 FOR SPATIALLY VARIABLE BED INITIAL CONDITIONS ` (28); ` \*             3 FOR SPATIALLY VARIABLE WATER COL AND BED INITIAL CONDITION ` (30). |
| 32–41 | 초기 하상 단위와 농도 — 전체 독성 물질 농도(total tox)를 mg/m^3으로 입력하는 옵션과 퇴적물 질량당 흡착 독성 물질 질량(sorbed mass tox/mass sed)을 mg/kg으로 입력하는 옵션을 구분한다(32–34). 수주의 초기 전체 독성 물질 농도는 ug/l 단위이며 하상 농도는 ITXBDUT를 참조한다(36–38). 원문: ` \* ITXBDUT: SET TO 0 FOR INITIAL BED GIVEN BY TOTAL TOX (mg/m^3) ` (32); ` \* SET TO 1 FOR INITIAL BED GIVEN BY SORBED MASS TOX/MASS SED(mg/kg) ` (34); ` \* TOXINTW: INIT WATER COLUNM TOT TOXIC VARIABLE CONCENTRATION (ug/l) ` (36); ` \* TOXINTB: INIT SED BED TOXIC CONC SEE ITXBDUT ` (38). |
| 42–51 | 1차 감소(first order decay) — 수주와 퇴적물 하상 각각의 감소율 단위는 1/sec다(42·46). 두 영역의 기준 온도(reference temperature) 단위는 DEG C다(44·48). 원문: ` \* RKTOXW: FIRST ORDER WATER COL DECAY RATE FOR TOX VARIABLE IN 1/sec ` (42); ` \* TKTOXW: REF TEMP FOR 1ST ORDER WATER COL DECAY DEG C ` (44); ` \* RKTOXB: FIRST ORDER SED BED DECAY RATE FOR TOX VARIABLE IN 1/sec ` (46); ` \* TKTOXB: REF TEMP FOR 1ST ORDER SED BED DECAY DEG C ` (48). |
| 52–52 | C43 입력 형식 — 입력 열 이름과 COMMENTS 항목만 제시한다(52). 파일은 이 줄에서 끝난다. 원문: ` C43 NTOXN  ITXINT  ITXBDUT  TOXINTW  TOXINTB  RKTOXW  TKTOXW  RKTOXB  TRTOXB  COMMENTS ` (52). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 48·52행: 하상 기준 온도 설명의 이름은 `TKTOXB`다(48). 입력 열 이름은 `TRTOXB`다(52). 이 파일은 두 이름의 관계를 명시하지 않는다.

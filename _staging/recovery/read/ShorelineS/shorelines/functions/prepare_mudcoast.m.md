---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_mudcoast.m
lines: 136
sha256: 905906c989161aca6b38d532eeba9eace312a3896599cae9b84c72446ede0eb2
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_mudcoast.m — 판독 구간 기록

구간은 1행부터 136행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–79 | 함수 시그니처는 `function [MUD]=prepare_mudcoast(S)` (1). 주석은 이질 해안(mud coast)의 세립 퇴적물(fine sediment) 속성, 침식 임계 전단응력(critical shear stress), 침식률, 수송 구역 폭, 침강 속도(fall velocity), 갯벌(mudflat)·맹그로브(mangrove) 폭 및 하천 공급 파일을 설명한다(2–51). 입력 스위치 S.mud의 주석 범위는 0 또는 1이다(9). 이 파일에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(52–79). |
| 80–109 | MUD를 만들고 used에 S.mud를 복사한다(80–81). `if MUD.used` (82) 안에서 taucr·M·B·w·Bfcrit·Bmmin·Bmmax·MHW·MSL·Tfm에 S.mudtaucr·mudm·mudb·mudw·mudbfcrit·mudbmmin·mudbmmax·mudmhw·mudmsl·mudtfm을 각각 복사한다(84–94). `MUD.dm     = MUD.MHW-MUD.MSL;` (93)로 평균해수면(mean sea level)에 대한 고수위 차를 계산한다. 하천 xriv·yriv·nriv·tstart·tend·rate와 맹그로브 xmgv·ymgv·nmgv·Bf·Bm·Bfm을 빈 배열로 초기화한다(95–108). |
| 110–120 | 시작 시 82행 MUD.used 분기 안. `if ~isempty(findstr(lower(S.ldbriverdisch),'.riv'))` (110)이면 로그를 출력하고 load를 호출한다(111–113). `MUD.nriv=size(riv,1);` (114), `MUD.xriv=[riv(:,1),riv(:,3)];` (115), `MUD.yriv=[riv(:,2),riv(:,4)];` (116), `MUD.tstart=datenum(num2str(riv(:,5)),'yyyymmdd');` (117), `MUD.tend=datenum(num2str(riv(:,6)),'yyyymmdd');` (118)를 계산한다. 7열의 연간 체적 공급률을 rate에 복사하고 조건을 닫는다(119–120). |
| 121–136 | 시작 시 82행 MUD.used 분기 안. `if ~isempty(findstr(lower(S.ldbmangrove),'.mgv'))` (121)이면 로그 뒤 load(124)를 호출한다. `MUD.nmgv = size(mgv,1);` (125)로 개수를 구한다. 1부터 5열을 xmgv·ymgv·Bf·Bm·Bfm에 각각 복사한다(126–130). struct2log 호출은 주석이다(134). 빈 줄과 내부 조건·바깥 조건·함수 종료를 포함한다(131–136). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37·44·80–136: 출력 주석은 ldbriverdisch·ldbmangrove 필드를 열거한다. 본문에는 두 MUD 필드를 대입하는 문장이 없다.
- 80–109: MUD.used가 거짓이면 구조체에는 used만 대입한다. 다른 물리·하천·맹그로브 필드 초기화는 참 분기 안에 있다.
- 115–116·126–127: 파일에서 읽은 좌표를 대입하는 블록에는 xyoffset 보정식이 없다.

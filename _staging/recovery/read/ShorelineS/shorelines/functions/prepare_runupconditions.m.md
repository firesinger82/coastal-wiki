---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_runupconditions.m
lines: 176
sha256: 1749153a207180aecd7547c0035fc90b35d02dd5e458854680971824a030fbb9
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_runupconditions.m — 판독 구간 기록

구간은 1행부터 176행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–69 | 함수 시그니처는 `function [RUNUP]=prepare_runupconditions(S,TIME)` (1). 주석은 처오름(runup) 계산용 정수위(still water level), 외해 파고·주기·파향과 시계열(time series) 파일, 위치 개수·좌표·SWL·WVD 출력을 설명한다(2–41). 이 파일에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(42–69). |
| 70–91 | 준비 로그 뒤 `if S.dune \|\| S.transmission==1` (72)이면 RUNUP을 만든다(76). swl0·watfile·mergeconditions를 같은 이름의 S 필드에서 복사한다(77–79). `if isempty(RUNUP.watfile)` (82) 안에서 `if isfield(S,'watclimfile')` (84)이면 이전 입력 S.watclimfile을 복사한다(85). 기본값은 `RUNUP.nloc=0;` (90), SWL은 빈 배열이다(91). |
| 92–111 | 시작 시 72행 사구·투과 조건 안. `if ~isempty(RUNUP.watfile)` (92)이면 로그와 `[SWL]=get_inputfiledata(RUNUP.watfile,TIME);` (95) 호출 뒤 `RUNUP.nloc=length(SWL);` (96), SWL 복사(97). `if isfield(S,'watlocfile')` (100)이면 load(101)한 1·2열을 x·y에 복사한다(102–103). `else` (104)는 `for kk=1:length(SWL)` (105)에서 각 SWL의 x·y를 복사한다(106–107). 루프·조건 종료와 빈 줄을 포함한다. |
| 112–135 | 시작 시 72행 사구·투과 조건 안. `if S.dune` (112)이면 dune·wvdfile을 같은 이름의 S 필드에서, Hs·Tp·Dir를 S.hso·S.tper·S.phiw0에서 복사한다(116–120). `if isempty(RUNUP.wvdfile)` (123)이면 S.wvcfile을 복사한다(124). 그 안 `if isfield(S,'waveclimfile')` (126), `if ~isempty(S.waveclimfile)` (127)이면 S.waveclimfile로 다시 대입한다(128). 기본값은 `RUNUP.nlocw=0;` (134), WVD는 빈 배열이다(135). |
| 136–155 | 시작 시 72행 사구·투과 조건·112행 사구 분기 안. `if ~isempty(RUNUP.wvdfile)` (136)이면 `[WVD]=get_inputfiledata(RUNUP.wvdfile,TIME);` (139), `RUNUP.nlocw=length(WVD);` (140), WVD 복사(141). `if isfield(S,'WaveLocfile')` (144)이면 load(145)한 1·2열을 xw·yw에 복사한다(146–147). `else` (148)는 `for kk=1:length(WVD)` (149)에서 각 WVD의 x·y를 복사한다(150–151). 루프·조건 종료와 빈 줄을 포함한다. |
| 156–176 | 시작 시 72행 사구·투과 조건·112행 사구 분기 안. `if length(RUNUP.WVD)~=length(RUNUP.SWL)` (157) 안에서 `if (length(RUNUP.WVD)>1 && length(RUNUP.SWL)~=1) \|\| (length(RUNUP.WVD)~=1 && length(RUNUP.SWL)>1)` (158)이면 위치 개수 불일치 경고를 출력한다(159). 자료 복제와 좌표 대응을 위한 두 elseif 블록은 모두 주석이다(160–167). 내부 조건과 사구 분기를 닫는다(168–170). struct2log 호출은 주석이다(172). 72행의 `else` (173)는 RUNUP을 빈 배열로 만든다(174). 조건과 함수를 닫는다(175–176). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 72·112·116–135: 파랑 관련 필드와 RUNUP.dune는 S.dune 참 분기 안에서만 대입한다. 수위 관련 필드는 투과 스위치만 켜진 경우에도 대입한다.
- 90–110·134–154: nloc·nlocw는 기본 0이며 SWL·WVD는 빈 배열이다. 대응하는 x·y·xw·yw를 빈 배열로 초기화하는 별도 문장은 없다.
- 157–169: 위치 개수가 다른 경우에도 158행 조건이 참일 때만 경고를 출력한다. 단일 위치 시계열을 복제하는 코드는 주석이다. [10-12 전수 검증 정정]
- 100–103·144–147: 위치 파일 입력은 필드 존재 여부만 검사한다. 파일명 비어 있음 검사와 xyoffset 보정식은 해당 블록에 없다.

---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_climatechange.m
lines: 154
sha256: 24a33f8feb35bf13ebc25921fa04b5252e848ddbcfdf6dd2970eb639ff12c7c4
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_climatechange.m — 판독 구간 기록

구간은 1행부터 154행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | 함수 시그니처는 `function [CC]=prepare_climatechange(S,TIME)` (1). 입력 주석은 S.ccslr·S.cchs·S.ccdir에 일정 변화율 또는 초기 시점 이후 변화 시계열(time series)을 받는다고 설명한다(8–10). CC 시간축과 해수면·파고·파향 보정 출력 설명, 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(11–47). 이 파일에는 S 필드 기본값 대입이 없다. |
| 48–60 | 로그와 초기화 주석 뒤 CC를 만든다(48–51). 기본값은 `CC.timenum=NaN;` (52), `CC.SLR=0.0;` (53), `CC.HS=0.0;` (54), `CC.DIR=0.0;` (55), `CC.HScor=1.0;` (57), `CC.PHIcor=0.0;` (58), `CC.SLRo=0.0;` (59). 주석은 HScor를 외해 파고에 곱하는 계수, PHIcor를 파향에 더하는 보정, SLRo를 Bruun 식에 사용하는 변화율로 설명한다. 이 구간은 해당 루틴을 호출하지 않는다. |
| 61–91 | 해수면 상승(sea level rise) 입력을 처리한다. `if isscalar(S.ccslr)` (62)는 timenum을 비우고 S.ccslr를 SLR로 복사한다(63–64). `elseif (ischar(S.ccslr) && ~isempty(S.ccslr)) \|\| (isnumeric(S.ccslr) && length(S.ccslr)>=2)` (66) 안에서 `if ischar(S.ccslr)` (67)이면 load, `else` (69)이면 직접 복사한다. try/catch는 `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmdd');` (73), `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmddHHMM');` (76), `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmddHHMMSS');` (78)를 순서대로 시도한다. `if CC.timenum(1)>TIME.timenum0 \|\| CC.timenum(end)<TIME.tend` (83)이면 error를 호출한다(84). `CC.SLR=interpNANs(CCraw(:,2));` (87)로 누락값 보간 루틴을 호출한다. 분기 종료와 빈 줄을 포함한다(89–91). |
| 92–122 | 파고 입력을 처리한다. `if isscalar(S.cchs)` (93)는 timenum을 비우고 S.cchs를 HS로 복사한다(94–95). `elseif (ischar(S.cchs) && ~isempty(S.cchs)) \|\| (isnumeric(S.cchs) && length(S.cchs)>=2)` (97) 안에서 `if ischar(S.cchs)` (98)이면 load, `else` (100)이면 직접 복사한다. try/catch의 날짜 변환식은 `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmdd');` (105), `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmddHHMM');` (108), `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmddHHMMSS');` (110). `if CC.timenum(1)>TIME.timenum0 \|\| CC.timenum(end)<TIME.tend` (115)이면 error를 호출한다(116). `CC.HS=interpNANs(CCraw(:,2));` (119)를 계산한다. 주석은 이 값이 초기 상황에 대한 상대 변화라고 적는다. |
| 123–154 | 파향 입력을 처리한다. `if isscalar(S.ccdir)` (123)는 timenum을 비우고 S.ccdir를 DIR로 복사한다(124–125). `elseif (ischar(S.ccdir) && ~isempty(S.ccdir)) \|\| (isnumeric(S.ccdir) && length(S.ccdir)>=2)` (127) 안에서 `if ischar(S.ccdir)` (128)이면 load, `else` (130)이면 직접 복사한다. try/catch의 날짜 변환식은 `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmdd');` (134), `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmddHHMM');` (137), `CC.timenum=datenum(num2str(CCraw(:,1)),'yyyymmddHHMMSS');` (139). `if CC.timenum(1)>TIME.timenum0 \|\| CC.timenum(end)<TIME.tend` (144)이면 error를 호출한다(145). `CC.DIR=interpNANsDIR(CCraw(:,2));` (148)를 계산한다. struct2log 호출은 주석이며 함수 종료와 빈 줄을 포함한다(150–154). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 62–64·93–95·123–125: 세 스칼라 입력 분기는 각각 동일한 CC.timenum을 빈 배열로 만든다. 시계열 분기도 동일한 CC.timenum을 다시 대입한다(73–78·105–110·134–139).
- 9·54·95·119: 파고 입력의 머리말과 스칼라 분기 주석은 m/yr을 적는다. 초기값 주석은 %/year을 적는다. 시계열 대입 주석은 fraction을 적는다.
- 18·55·58·125·148: 파향 출력 머리말은 radians cartesian을 적는다. DIR 초기값과 스칼라 분기 주석은 °/yr을 적는다(55·125). PHIcor 초기값 주석은 °를 적는다(58). 마지막 보간 대입 주석은 fraction을 적는다. [10-12 전수 검증 정정]

---
file: models/ShorelineS/raw/source_code/shorelines/functions/introduce_climatechange.m
lines: 116
sha256: f1b890a5f413adba218dc09846f32e88cc9b433ffa46c35ec48779d238a292cc
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# introduce_climatechange.m — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 함수 시그니처(1). 현재 시각의 기후변화(climate change) 보정을 만드는 설명과 CC·TIME 입출력 주석(4–22). 입력 주석은 SLR을 m/yr, HS를 m, DIR을 deg로 적는다(9–11). 출력은 해수면 상승률(sea level rise rate) SLRo, 상대 파고 계수 HScor, 방향 변화 PHIcor이다(20–22). 원문: `function [CC]=introduce_climatechange(CC,TIME,i_mc)` (1). |
| 24–51 | 시작 시 1행 introduce_climatechange 함수 안. 2022년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(24–51). |
| 52–63 | 시작 시 1행 introduce_climatechange 함수 안. 첫 해안 구간에서만 계산한다(52). CC.timenum이 NaN이면 즉시 반환한다(53). timenum이 비면 시작부터 경과한 일수를 365로 나눠 연수로 만든다(56–58). SLRo는 CC.SLR, HScor는 1에 CC.HS와 경과 연수의 곱을 더한 값, PHIcor는 CC.DIR과 경과 연수의 곱이다(59–61). 원문: `if i_mc==1` (52), `if isnan(CC.timenum); return; end` (53), `if isempty(CC.timenum)` (56), `dt=(TIME.tnow-TIME.timenum0)/365.;` (58), `CC.SLRo   = CC.SLR;              % rate of sea level rise at considered time instance (m/yr)` (59), `CC.HScor  = 1 + CC.HS * dt;      % relative increase of Hs at considered moment w.r.t. t0 [-]` (60), `CC.PHIcor = CC.DIR * dt;         % rotation of the wave direction at considered moment w.r.t. t0 [delta °]` (61). |
| 64–73 | 시작 시 1행 introduce_climatechange 함수·52행 i_mc==1 분기·56행 timenum 검사 안. 64행 else는 시계열(time series) 경로이다. 이전 시각부터의 일수를 365로 나눈다(65). 평균 timenum이 1e7보다 크면 yyyymmdd, 1e4보다 작으면 yyyy로 datenum 변환한다(68–72). 원문: `else` (64), `dt      = (TIME.tnow-TIME.tprev)/365.;` (65), `if mean(CC.timenum)>1e7 % time as a string of yearmonthday's` (68), `CC.timenum=datenum(num2str(CC.timenum,'%1.0f'),'yyyymmdd');` (69), `elseif mean(CC.timenum)<1e4 % time as a string of years` (70), `CC.timenum=datenum(num2str(CC.timenum,'%1.0f'),'yyyy');` (71). |
| 74–95 | 시작 시 1행 introduce_climatechange 함수·52행 i_mc==1 분기·64행 시계열 else 안. timenum과 SLR의 길이가 같을 때 구간 내 양의 dt이면 현재·이전 SLR을 interp1로 얻고 그 차이를 dt로 나눈다(74–79). 그 외에는 인접 SLR 차이를 인접 timenum 차이로 나눈 slrrate를 만들고 시간 조건에 따라 첫 값 또는 마지막 값을 사용한다(83–90). 길이가 다르면 SLRo를 0으로 둔다(92–94). 원문: `if length(CC.timenum(:))==length(CC.SLR(:))` (74), `if dt>0.0 && TIME.tprev>=min(CC.timenum(:)) && TIME.tnow<=max(CC.timenum(:))` (76), `slr     = interp1(CC.timenum(:),CC.SLR(:),TIME.tnow);   % SLR amount since simulation start in [m]` (77), `slrprev = interp1(CC.timenum(:),CC.SLR(:),max(TIME.tprev,min(CC.timenum)));` (78), `CC.SLRo = (slr-slrprev)/dt;   % instantanious rate for coastline_change` (79), `else` (83), `slrrate = diff(CC.SLR(:))./diff(CC.timenum(:));` (84), `if TIME.tnow<=min(CC.timenum(:)) \|\| TIME.tprev<=min(CC.timenum(:)) \|\| dt==0` (85), `CC.SLRo = slrrate(1);   % instantanious rate for coastline_change` (86), `else` (87), `CC.SLRo = slrrate(end);   % instantanious rate for coastline_change` (88), `else` (92), `CC.SLRo=0.0;` (93). |
| 96–116 | 시작 시 1행 introduce_climatechange 함수·52행 i_mc==1 분기·64행 시계열 else 안. timenum과 HS 길이가 같으면 interp1로 상대 증가분을 보간한다(96–98). NaN이면 error를 호출하고, 정상값이면 1을 더해 HScor로 둔다(99–102). timenum과 DIR 길이가 같으면 방향의 sine·cosine을 각각 보간하고 atan2d로 방향을 복원한다(105–108). NaN이면 error를 호출한다(109–110). PHIcor 대입과 바깥 조건·함수 종료(112–116). 원문: `if length(CC.timenum(:))==length(CC.HS(:))` (96), `hsfactor     = interp1(CC.timenum(:),CC.HS(:),TIME.tnow);` (98), `if isnan(hsfactor)` (99), `error('Could not determine slr related wave height change factor. Check your input time series');` (100), `CC.HScor = 1+hsfactor;` (102), `if length(CC.timenum(:))==length(CC.DIR(:))` (105), `sinrate      = interp1(CC.timenum(:),sind(CC.DIR(:)),TIME.tnow);` (106), `cosrate      = interp1(CC.timenum(:),cosd(CC.DIR(:)),TIME.tnow);` (107), `dirchange    = atan2d(sinrate,cosrate);` (108), `if isnan(dirchange)` (109), `error('Could not determine the absolute change in wave direction. Check your input time series');` (110), `CC.PHIcor = dirchange;` (112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·77–79·84–88: 입력 주석은 CC.SLR을 m/yr로 적는다. 시계열 내부 주석은 CC.SLR 보간값을 누적 상승량 m로 적는다. 76행 조건을 만족하면 상승량 차이를 연수 dt로 나눈다. 76행 조건을 만족하지 않으면 인접 SLR 차이를 datenum 차이로 나누어 slrrate를 만든다. 이 분기에는 dt가 0인 경우도 포함된다. [10-12 전수 검증 정정]
- 10·60·97·102: HS 입력 주석은 m 단위 변화로 적는다. 실행식은 HScor에 1을 더하며, 97행 주석은 HS를 초기 파고의 상대 증가분으로 설명한다.
- 96–113: HS 또는 DIR의 길이가 timenum과 다를 때 HScor·PHIcor를 설정하는 else는 없다.
- 74–88: 길이가 같은 경우에도 표본 수가 둘 이상인지 검사하는 조건은 없다. slrrate의 첫 값 또는 마지막 값에 접근한다.

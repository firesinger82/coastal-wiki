---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_channel.m
lines: 137
sha256: 5264e25f0c3bfe7b97e7ad3735a1a3075a15f908bfbe7e64d7c9829ac600c361
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_channel.m — 판독 구간 기록

구간은 1행부터 137행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | 함수 시그니처는 `function [CHANNEL]=prepare_channel(S)` (1). 주석은 이동 수로(migrating channel) 구조체 초기화와 S.channel·channelwidth·channelfac·channeldischrate·channeldischr·ldbchannel·xrmc·yrmc·xyoffset 입력을 설명한다(2–25). 수로 폭은 m, 계수는 무차원이며 이 파일에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(26–54). |
| 55–97 | 준비 로그 뒤 CHANNEL을 만들고 used를 S.channel에서 복사한다. 좌표·폭·계수·유량 필드는 빈 배열로 초기화한다(55–65). `if S.channel` (67) 안에서 `if strcmpi(S.ldbchannel,'manual') \|\| strcmpi(S.ldbchannel,'interactive')` (69)이면 그림 11과 안내문을 만들고 `select_multi_polygon('k')` (73)을 호출한다. 안내문 위치는 `xl(1)+0.02*diff(xl)`과 `yl(2)-0.01*diff(yl)`이다(72). 좌표를 저장하고 안내문을 숨긴 뒤 rivers.mat를 저장한다(74–77). `elseif ~isempty(S.xrmc)` (78)는 S.xrmc·S.yrmc를 복사한다. `elseif ~isempty(S.ldbchannel)` (82)는 load를 호출한다. `if isstruct(xy_channel)` (84)이면 `CHANNEL.xrmc=xy_channel.xrmc(:)'-S.xyoffset(1);` (86), `CHANNEL.yrmc=xy_channel.yrmc(:)'-S.xyoffset(2);` (87). `else` (88)에서는 `if size(xy_channel,2)>2` (90)일 때 `xy_channel=xy_channel';` (91)로 전치한 뒤 `CHANNEL.xrmc=xy_channel(:,1)'-S.xyoffset(1);` (93), `CHANNEL.yrmc=xy_channel(:,2)'-S.xyoffset(2);` (94)를 계산한다. 내부 조건을 닫고 빈 줄을 포함한다(95–97). [10-12 전수 검증 보완] |
| 98–119 | 시작 시 67행 S.channel 분기 안. 수로 수는 `nriv=sum(isnan(CHANNEL.xrmc))+1;` (100). 폭·계수·두 유량 값을 각각 S.channelwidth·S.channelfac·S.channeldischrate·S.channeldischr에서 복사한다(101–104). `if length(CHANNEL.width)<nriv` (107)이면 `CHANNEL.width=repmat(S.channelwidth,[nriv,1]);` (108). `if length(CHANNEL.fac)<nriv` (110)이면 `CHANNEL.fac=repmat(S.channelfac,[nriv,1]);` (111). `if length(CHANNEL.disch_rate)<nriv` (113)이면 `CHANNEL.disch_rate=repmat(S.channeldischrate,[nriv,1]);` (114). `if length(CHANNEL.disch_R)<nriv` (116)이면 `CHANNEL.disch_R=repmat(S.channeldischr,[nriv,1]);` (117). 각 조건의 종료와 빈 줄을 포함한다. |
| 120–137 | 시작 시 67행 S.channel 분기 안. 구조체 입력을 비권장으로 표시한 주석 뒤 `if ~isempty(S.ldbchannel)` (121), `if strcmpi(matname(end-3:end),'.mat')` (123)이면 channels 구조체를 만들고 load를 호출한다. `n_chan=length(channels);` (126), `for ichan=1:n_chan` (127)에서 channels의 channelwidth·channelfac를 CHANNEL에 복사한다(128–129). 루프와 조건을 닫는다(130–132). struct2log 호출은 주석이다(135). 바깥 분기와 함수를 닫는다(136–137). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13·82–83: 입력 주석은 ldbchannel에 직접 Nx2 행렬을 허용한다고 적는다. 실행 분기는 ldbchannel을 load 인수로 전달한다.
- 100: nriv는 xrmc의 NaN 개수에 1을 더한다. 이 계산 앞에는 xrmc가 빈 배열인지 검사하는 조건이 없다.
- 121–125: .mat 접미사 판정은 matname(end-3:end)를 사용한다. 이 분기에는 문자열 길이를 검사하는 조건이 없다.
- 123–129: .mat 분기는 앞에서 설정한 폭과 계수를 channels 구조체 필드로 다시 대입한다.

---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_transportpoints.m
lines: 99
sha256: d4be45ac941bc0ab7e05e4db5890f8071f55911af23efdfe3f0d4c6097e1e3f5
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_transportpoints.m — 판독 구간 기록

구간은 1행부터 99행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–43 | 함수 시그니처는 `function [COAST]=get_transportpoints(COAST,i_mc_range)` (1). 해안 구간(coastal segment) 좌표·기본 격자 간격(grid spacing)·양끝 돌제(groyne) 표식과 선택 구간 입력, 수송점(transport point) 좌표 출력을 설명한다(2–15). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(16–43). |
| 44–60 | 시작 시 1행 get_transportpoints 함수 안. `if nargin==1` (45)이면 전체 구간 기본값 식 `i_mc_range=[1:COAST.n_mc];` (46), xq_mc·yq_mc 빈 배열 초기화(47–48). 구간 반복은 `for i_mc=i_mc_range` (52). get_one_polygon 호출은 `[x,y,n_mc]=get_one_polygon(COAST.x_mc,COAST.y_mc,i_mc);` (53). `if length(x)>1` (55)이면 인접 해안점 중간 좌표식 `xq=(x(1:end-1)+x(2:end))/2;` (58); `yq=(y(1:end-1)+y(2:end))/2;` (59). get_cyclic 호출은 `cyclic=get_cyclic(x,y,COAST.ds0);` (60). 주석·빈 줄을 포함한다(44·50–51·54·56–57). |
| 61–84 | 시작 시 1행 get_transportpoints 함수 안. 시작 시 52행 i_mc 반복·55행 점 수 분기 안. `if cyclic` (61)이면 순환 끝점 결합식 `xq=[xq(end),xq,xq(1)];` (62); `yq=[yq(end),yq,yq(1)];` (63). `else` (64)에서는 왼쪽 조건 `if COAST.BNDgroyne(i_mc,1)==0       % extend grid when it is an open coast without a structure` (65). 구조물이 없을 때 외삽(extrapolation) 식은 `xq=[1.5*x(1)-0.5*x(2),xq];` (66); `yq=[1.5*y(1)-0.5*y(2),yq];` (67). `else                                % use first coastline point in case a groyne is present` (68)이면 첫 해안점 결합식 `xq=[x(1),xq];` (69); `yq=[y(1),yq];` (70). 오른쪽 조건은 `if COAST.BNDgroyne(i_mc,2)==0       % extend grid when it is an open coast without a structure` (72). 외삽식은 `xq=[xq,1.5*x(end)-0.5*x(end-1)];` (73); `yq=[yq,1.5*y(end)-0.5*y(end-1)];` (74). `else                                % use last coastline point in case a groyne is present` (75)이면 마지막 해안점 결합식 `xq=[xq,x(end)];` (76); `yq=[yq,y(end)];` (77). 경계·순환 분기를 닫는다(71·78–79). 점 수 조건의 `else` (80)에서는 짧은 구간 경고를 출력하고 xq=x·yq=y를 복사한다(81–83). 점 수 분기를 닫는다(84). |
| 85–99 | 시작 시 1행 get_transportpoints 함수 안. 시작 시 52행 i_mc 반복 안이며 점 수 분기 밖. `if isempty(COAST.xq_mc)` (87)이면 COAST.xq_mc·yq_mc에 새 좌표를 복사한다(88–89). `elseif length(i_mc_range)>1` (90)이면 NaN 구분자를 넣어 붙이는 식 `COAST.xq_mc=[COAST.xq_mc,nan,xq];` (91); `COAST.yq_mc=[COAST.yq_mc,nan,yq];` (92). `else` (93)이면 insert_section 호출 `[COAST.xq_mc,COAST.yq_mc]=insert_section(xq,yq,COAST.xq_mc,COAST.yq_mc,i_mc);` (94). 분기·구간 반복·함수 종료와 주석·빈 줄을 포함한다(85–86·95–99). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·45–49·52: 주석은 선택 구간을 비워 전체 구간을 평가하라고 적는다. 전체 범위 초기화 조건은 nargin==1이며, 두 번째 인수가 빈 배열인 경우를 위한 분기는 없다.
- 53: get_one_polygon의 n_mc 출력은 이후 실행문에서 참조하지 않는다.
- 87–94: COAST.xq_mc가 비어 있지 않고 선택 구간 수가 2 이상이면 기존 좌표 끝에 새 구간을 붙인다. 기존 구간 교체 호출은 선택 구간 수가 1인 else 안에 있다.

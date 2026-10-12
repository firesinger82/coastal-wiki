---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_riverdischarges.m
lines: 92
sha256: a66dcf69f93c84f3ed00996ddbb8eb4b665331f9be5ed0010ab725cc8669276a
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_riverdischarges.m — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | 함수 시그니처는 `function [MUD]=get_riverdischarges(TIME,COAST,TRANSP,MUD)` (1). 하천 유입(river discharge) 날짜·좌표·체적률(volume rate)과 길이당 체적률 출력을 설명한다(2–22). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(23–50). |
| 51–80 | 시작 시 1행 get_riverdischarges 함수 안. MUD.rate_density를 COAST.n개의 0 배열로 초기화한다(51). `if MUD.used` (52)이면 하천 반복 `for i_n=1:MUD.nriv` (53). `if TIME.tnow>=MUD.tstart(i_n) && TIME.tnow<=MUD.tend(i_n)` (54)이면 dxmud를 비우고(57), 해안 요소(coastal element) 반복 `for i_mc=1:COAST.n_mc` (58). get_one_polygon 호출은 `[ xc,yc,~,~,~ ] = get_one_polygon( COAST.x_mc,COAST.y_mc,i_mc );` (59). 하구 양끝 거리·최근접 인덱스(index)·영향 구간 식은 `dist1=hypot(xc-MUD.xriv(i_n,1),yc-MUD.yriv(i_n,1));` (60); `dist2=hypot(xc-MUD.xriv(i_n,2),yc-MUD.yriv(i_n,2));` (61); `idx1=find(dist1==min(dist1),1);` (62); `idx2=find(dist2==min(dist2),1);` (63); `idx{i_mc}=[min(idx1,idx2):max(idx1,idx2)];` (64). get_cyclic 호출은 `cyclic=get_cyclic(xc,yc,COAST.ds0);` (66). 누적 거리·점 간격 식은 `s=[0,cumsum((diff(xc).^2+diff(yc).^2).^0.5)];` (68); `ds0=diff(s);` (69); `ds=[ds0(1),(ds0(1:end-1)+ds0(2:end))/2,ds0(end)];` (70). `if COAST.cyclic(i_mc)` (71)이면 양끝 간격식 `ds(1)=(ds0(1)+ds0(end))/2;` (72); `ds(end)=(ds0(1)+ds0(end))/2;` (73). 최소 길이 계수는 `dxmin=1e-5;` (75). 하구 길이 제한식은 `dxmud(i_mc)=max(sum(ds(idx{i_mc})),dxmin);` (76). `if isnan(dxmud(i_mc))` (77)이면 dxmud를 0으로 설정한다(78). 분기·해안 요소 반복을 닫는다(79–80). |
| 81–92 | 시작 시 1행 get_riverdischarges 함수 안. 시작 시 52행 MUD.used 분기·53행 하천 반복·54행 시간 분기 안. 하천 유입 배분 주석과 빈 줄을 포함한다(81–84). 배분 비율 식은 `fraction = dxmud./sum(dxmud);` (85). `if ~isempty(idx{COAST.i_mc})` (86)이면 현재 요소의 체적률 밀도 누적식 `MUD.rate_density(idx{COAST.i_mc})=MUD.rate_density(idx{COAST.i_mc})+MUD.rate(i_n)./dxmud(COAST.i_mc).*fraction(COAST.i_mc);` (87). 조건·시간 분기·하천 반복·MUD.used 분기·함수를 닫는다(88–92). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·51–91: 입력 TRANSP는 실행문에서 참조하지 않는다.
- 14–16·53·60–61: 입력 주석은 MUD.x·MUD.y·MUD.n을 적는다. 실행문은 MUD.xriv·MUD.yriv·MUD.nriv를 사용한다.
- 66·71: get_cyclic 결과 cyclic은 이후 참조하지 않는다. 점 간격 보정 분기는 COAST.cyclic(i_mc)를 사용한다.
- 75–87: dxmud를 dxmin=1e-5 이상으로 제한한 뒤 NaN이면 0으로 바꾼다. fraction의 sum(dxmud) 분모에는 별도 하한이나 0 검사문이 없다.

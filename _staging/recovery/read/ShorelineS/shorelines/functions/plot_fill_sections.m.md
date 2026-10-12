---
file: models/ShorelineS/raw/source_code/shorelines/functions/plot_fill_sections.m
lines: 174
sha256: daaea3064f742600212cbeddb36df93ede2c77ab99957490b18a6b66687f3c71
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# plot_fill_sections.m — 판독 구간 기록

구간은 1행부터 174행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 함수 시그니처(1). 해안 구간의 육지 다각형을 그리며 열린 구간에는 육지 쪽 점을 추가한다는 주석(4–6). 원문: `function [FORMAT] = plot_fill_sections(COAST,FORMAT,TIME)` (1). |
| 8–35 | 시작 시 1행 plot_fill_sections 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(8–35). |
| 36–56 | 시작 시 1행 plot_fill_sections 함수 안. 전체 해안 좌표는 COAST에서 가져온다(36–37). 시간 단계는 TIME.it에서 가져온다(39). 육지 폭·범위·저장 경계·채움 옵션은 FORMAT에서 가져온다(38·40–46·51–52). ds0가 스칼라가 아니면 셋째 열 최솟값을 쓴다(47–50). x_mc의 NaN 수에 1을 더해 구간 수를 얻는다(54–55). 원문: `x_mc=COAST.x_mc;` (36), `y_mc=COAST.y_mc;` (37), `ld=FORMAT.ld;` (38), `it=TIME.it;` (39), `xmax=FORMAT.xmax;` (40), `ymax=FORMAT.ymax;` (41), `xmin=FORMAT.xmin;` (42), `ymin=FORMAT.ymin;` (43), `nmax=FORMAT.nmax;` (44), `xb=FORMAT.xb;` (45), `yb=FORMAT.yb;` (46), `ds0=COAST.ds0;` (47), `if ~isscalar(ds0)` (48), `ds0=min(ds0(:,3));` (49), `usefill=FORMAT.usefill;` (51), `usefillpoints=FORMAT.usefillpoints;` (52), `nans=find(isnan(x_mc));` (54), `n_mc=length(nans)+1;` (55). [10-12 전수 검증 정정] |
| 57–78 | 시작 시 1행 plot_fill_sections 함수 안. 각 해안 구간 루프(57). NaN이 없으면 전체 배열, 있으면 첫·마지막·중간 구간 조건에 따른 시작·끝 인덱스를 사용한다(58–73). x·y 슬라이스를 얻어 x0·y0 cell 배열에 보관한다(74–77). 원문: `for i_mc=1:n_mc` (57), `nans=find(isnan(x_mc));` (58), `if isempty(nans)` (59), `i1=1;` (60), `i2=length(x_mc);` (61), `else` (62), `if i_mc==1` (63), `i1=1;` (64), `i2=nans(i_mc)-1;` (65), `elseif i_mc==n_mc;` (66), `i1=nans(i_mc-1)+1;` (67), `i2=length(x_mc);` (68), `else` (69), `i1=nans(i_mc-1)+1;` (70), `i2=nans(i_mc)-1;` (71), `x=x_mc(i1:i2);` (74), `y=y_mc(i1:i2);` (75), `x0{i_mc}=x;` (76), `y0{i_mc}=y;` (77). |
| 79–92 | 시작 시 1행 plot_fill_sections 함수·57행 구간 루프 안. right 기본값은 1이다(80). 비어 있지 않은 구간에서 양 끝 거리가 ds0보다 크면 right=1을 유지한다(81–84). 그 외에는 min(get_clockpoly(x,y)+1,1)을 사용한다(85–87). 구간 루프 종료(90). right==0 구간을 IDlake로 찾는다(91). 원문: `right(i_mc)=1;` (80), `if ~isempty(x)` (81), `if hypot(x(end)-x(1),y(end)-y(1))>ds0` (82), `right(i_mc)=1;` (84), `else` (85), `right(i_mc)=min(get_clockpoly(x,y)+1,1);` (87), `IDlake=find(right==0);` (91). |
| 93–102 | 시작 시 1행 plot_fill_sections 함수 안. IDlake가 아닌 구간을 먼저, IDlake 구간(91행 `IDlake=find(right==0);`)을 나중에 도는 구간 루프이다(93). [10-12 검증 정정] 저장한 x·y를 가져오고 notclosed=1로 둔다(94–96). 좌표가 비었거나 양 끝 차이 제곱합이 정확히 0이면 notclosed=0으로 둔다(97–101). 원문: `for i_mc=[setdiff([1:n_mc],IDlake),IDlake]` (93), `x=x0{i_mc};` (94), `y=y0{i_mc};` (95), `notclosed=1;    % <- notclosed option recently added for Ameland (check?)` (96), `if isempty(x)` (97), `notclosed=0;` (98), `elseif (x(1)-x(end)).^2+(y(1)-y(end)).^2 == 0` (99), `notclosed=0;` (100). |
| 103–129 | 시작 시 1행 plot_fill_sections 함수·93행 채움 순서 루프 안. if 0 블록은 실행되지 않는 육지 경계 구성 대안이다(103). 그 안 조건은 육지 또는 첫 구간이고 열린 경우이다(105). 평균 좌표 차이·벡터 길이·양 끝 법선점을 구한다(106–110). 직선 기울기 RC의 분모가 0이면 1e-5를 쓴다(114–117). 직선 아래 점을 골라 l3=100의 법선 이동 후 역순 경계를 덧붙인다(118–126). 두 조건 종료(127–128). 원문: `if 0` (103), `if (right(i_mc) \|\| i_mc==1) && notclosed  % <- notclosed option recently added for Ameland (check?)` (105), `dx=diff(x);dx=[dx(1),(dx(1:end-1)+dx(2:end))/2,dx(end)];` (106), `dy=diff(y);dy=[dy(1),(dy(1:end-1)+dy(2:end))/2,dy(end)];` (107), `l2=(dx.^2+dy.^2).^0.5;` (108), `xclose = [x(end)+dy(end)/l2(end),x(1)+dy(1)/l2(1)];` (109), `yclose = [y(end)-dx(end)/l2(end),y(1)-dx(1)/l2(1)];` (110), `RC = diff(yclose)/diff(xclose);` (114), `if diff(xclose)==0` (115), `RC = diff(yclose)/1e-5;` (116), `B = yclose(1)-RC*xclose(1);` (118), `ID = find(y<RC*x+B);` (119), `l3=100;` (122), `xclose = [xclose(1),fliplr(x(ID)+l3*dy(ID)./l2(ID)),xclose(2)];` (123), `yclose = [yclose(1),fliplr(y(ID)-l3*dx(ID)./l2(ID)),yclose(2)];` (124), `x = [x,xclose];` (125), `y = [y,yclose];` (126). |
| 130–151 | 시작 시 1행 plot_fill_sections 함수·93행 채움 순서 루프 안. usefill==1이면 현재 좌표로 채움 배열을 시작한다(130–132). 저장 경계가 해당 구간까지 있고 구간이 열려 있으면 xb·yb를 재사용해 닫는다(133–136). 그 외에는 열린 구간이고 ld가 있을 때 plot_insert_land_fill을 호출한다(137–140). usefillpoints가 비영이면 저장 경계의 첫·마지막 점을 뺀다(142–145). 그 외 경로는 저장 경계를 비운다(146–149). 원문: `if usefill==1` (130), `xfill=x;` (131), `yfill=y;` (132), `if length(xb)>=i_mc && notclosed` (133), `xfill=[x,xb{i_mc},x(1)];` (135), `yfill=[y,yb{i_mc},y(1)];` (136), `else` (137), `if notclosed && ~isempty(ld)` (139), `[xfill,yfill,xb{i_mc},yb{i_mc},xmax,ymax,xmin,ymin,nmax] = plot_insert_land_fill(x,y,ld,it,xmax,ymax,xmin,ymin,i_mc,n_mc,nmax,usefillpoints);` (140), `if usefillpoints~=0` (142), `xb{i_mc}=xb{i_mc}(2:end-1);` (143), `yb{i_mc}=yb{i_mc}(2:end-1);` (144), `else` (146), `xb{i_mc}=[];` (147), `yb{i_mc}=[];` (148). |
| 152–174 | 시작 시 1행 plot_fill_sections 함수·93행 채움 순서 루프·130행 usefill 선택 분기 안. right가 참이면 [.9 .9 0.4]로 육지를, 거짓이면 [.9 .9 1]로 호수를 채운다(153–157). 158행 else는 usefill이 1이 아닌 경우이며 빨간 선을 그린다(159). hold on 후 구간 루프를 끝내고 hold off한다(161–164). 갱신한 범위·nmax·xb·yb를 FORMAT에 저장한다(167–173). 함수 종료(174). 원문: `if right(i_mc)` (153), `fill(xfill,yfill,[.9 .9 0.4]);` (154), `else` (155), `fill(xfill,yfill,[.9 .9 1]);` (156), `else` (158), `plot(x,y,'r','linewidth',2)` (159), `hold on` (161), `hold off` (164), `FORMAT.xmax=xmax;` (167), `FORMAT.ymax=ymax;` (168), `FORMAT.xmin=xmin;` (169), `FORMAT.ymin=ymin;` (170), `FORMAT.nmax=nmax;` (171), `FORMAT.xb=xb;` (172), `FORMAT.yb=yb;` (173). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·140: 주석의 보조 루틴 이름은 plot_insert_landfill.m이다. 실행 호출 이름은 plot_insert_land_fill이다.
- 103–128: 육지 경계를 별도로 구성하는 블록은 if 0으로 감싸져 있다.
- 82·99: 육지/호수 분류는 끝점 거리와 ds0를 비교한다. notclosed 판정은 양 끝 차이 제곱합이 정확히 0인지 비교한다.

---
file: models/ShorelineS/raw/source_code/shorelines/functions/plot_insert_land_fill.m
lines: 115
sha256: 890ea8aec12210629e1baabde15fe5c55c86bbb8a164bb2fc34d194d8fc0f7b6
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# plot_insert_land_fill.m — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 함수 시그니처(1). 열린 해안선 배후 그림용 육지 다각형을 만드는 설명(4–7). usefillpoints==0 방식은 육지 쪽 두 점을 쓰고, usefillpoints>=1 방식은 지정 점 수를 사용한다고 적는다. 원문: `function [x,y,xb,yb,xmax,ymax,xmin,ymin,nmax] = plot_insert_land_fill(x,y,ld,it,xmax,ymax,xmin,ymin,i_mc,n_mc,nmax,usefillpoints)` (1). |
| 9–36 | 시작 시 1행 plot_insert_land_fill 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(9–36). |
| 37–57 | 시작 시 1행 plot_insert_land_fill 함수 안. 양 끝 좌표 거리 dist·distmax와 처음 두 점 거리 ds0를 계산한다(37–39). usefillpoints==0 또는 3점 미만이면 양 끝 방향 방식이다(42). 초기 단계이거나 i_mc가 저장 xmin 길이보다 크면 해당 구간의 최소·최대 좌표와 nmax를 설정한다(43–55). atan2d로 양 끝 방향 o를 구한다(56). 원문: `dist=((y(end)-y(1)).^2+(x(end)-x(1)).^2).^0.5;` (37), `distmax=((x(end)-x(1)).^2+(y(end)-y(1)).^2).^0.5; %max( max(((y-y(1)).^2+(x-x(1)).^2).^0.5), max(((y-y(end)).^2+(x-x(end)).^2).^0.5));` (38), `ds0=hypot(x(2)-x(1),y(2)-y(1));` (39), `if usefillpoints==0 \|\| length(x)<3` (42), `if it==0  % this value should store` (43), `xmin(i_mc)=min(x);` (44), `ymin(i_mc)=min(y);` (45), `xmax(i_mc)=max(x);` (46), `ymax(i_mc)=max(y);` (47), `nmax=n_mc;` (48), `elseif i_mc>length(xmin)` (49), `xmin(i_mc)=min(x);` (50), `ymin(i_mc)=min(y);` (51), `xmax(i_mc)=max(x);` (52), `ymax(i_mc)=max(y);` (53), `nmax=n_mc;` (54), `o=atan2d((y(end)-y(1)),(x(end)-x(1)));` (56). |
| 58–79 | 시작 시 1행 plot_insert_land_fill 함수·42행 양 끝 방향 분기 안. dist>0.2*distmax와 usefillpoints==0이면 방향을 네 범위로 나눈다(59–69). -45..45 방향은 아래, 절댓값 135 이상은 위, 45..135는 오른쪽, -135..-45는 왼쪽으로 전체 범위와 ld를 사용해 두 육지 점을 붙인다(61–71). xb·yb는 수정한 배열의 마지막·첫 점이다(73–74). 75행 else는 원래 끝 두 점·첫 두 점을 저장한다(76–77). 원문: `if dist>0.2*distmax & usefillpoints==0` (59), `if o >= -45 &&  o<=45   %% Shoreline horizontal & land on the right side (down)` (60), `x=[xmin(i_mc),x,xmax(i_mc)];` (61), `y=[min(ymin)-ld,y,min(ymin)-ld];` (62), `elseif abs (o) >= 135  %% Shoreline horizontal & land on the left side (up)` (63), `x=[xmax(i_mc),x,xmin(i_mc)];` (64), `y=[max(ymax)+ld,y,max(ymax)+ld];` (65), `elseif o > 45 &&  o<135    %% vertical Shoreline  & land on the right side` (66), `x=[max(xmax)+ld,x,max(xmax)+ld];` (67), `y=[ymin(i_mc),y,ymax(i_mc)];` (68), `elseif o < -45 &&  o>-135   %% vertical Shoreline  & land on the left side` (69), `x=[min(xmin)-ld,x,min(xmin)-ld];` (70), `y=[ymax(i_mc),y,ymin(i_mc)];` (71), `xb=[x(end),x(1)];` (73), `yb=[y(end),y(1)];` (74), `else` (75), `xb=[x(end-1),x(end),x(1),x(2)];` (76), `yb=[y(end-1),y(end),y(1),y(2)];` (77). |
| 80–98 | 시작 시 1행 plot_insert_land_fill 함수·42행 방식 선택 분기 안. 80행 else는 여러 육지 점을 만드는 경로이다. ceil·콜론 구간으로 방향용 ido와 좌표용 idx를 만들고 교대로 추출한 ido4·idx4를 조정한다(86–90). 인접점 방향 o를 mod 360으로 만든다(91). 각 육지 점 루프에서 get_smoothdata의 angleavgmean·3 옵션으로 구간 평균 방향을 얻는다(93–95). x2·y2는 idx4 위치 좌표이다(96–97). 원문: `else` (80), `ido=ceil([1:(length(x)-2)/max(usefillpoints*2-2,1):length(x)-1]);` (86), `idx=ceil([1:(length(x)-1)/(length(ido)-1):length(x)]);` (87), `ido4=ido([1,2:2:length(ido)-1,length(ido)]);` (88), `idx4=idx([1,2:2:length(idx)-1,length(idx)]);` (89), `idx4=[idx4(1),floor((idx4(2:end-2)+idx4(3:end-1))/2),idx4(end)];` (90), `o=mod(atan2d(diff(x),diff(y))-90,360);` (91), `o2=[];` (92), `for oo=1:usefillpoints` (93), `o2(oo)=mean(get_smoothdata(o([ido4(oo):ido4(oo+1)]),'angleavgmean',3));` (94), `x2=x(idx4);` (96), `y2=y(idx4);` (97). |
| 99–115 | 시작 시 1행 plot_insert_land_fill 함수·80행 여러 육지 점 else 안. dist>0.2*distmax이면 x2·y2를 각 평균 방향의 sine·cosine에 ld를 곱한 만큼 이동하고 뒤집어 xb·yb와 원래 좌표 뒤에 붙인다(100–104). 그 외에는 끝 두 점·첫 두 점을 저장한다(105–107). 방식 분기 종료(109). 주석 처리한 그림 명령·빈 줄·함수 종료(111–115). 원문: `if dist>0.2*distmax % may be check that dist>2*ds0 ?                %&& n_mc==1` (100), `xb=[x(end),fliplr(x2-sind(o2)*ld),x(1)];` (101), `yb=[y(end),fliplr(y2-cosd(o2)*ld),y(1)];` (102), `x=[x,fliplr(x2-sind(o2)*ld),x(1)];` (103), `y=[y,fliplr(y2-cosd(o2)*ld),y(1)];` (104), `else` (105), `xb=[x(end-1),x(end),x(1),x(2)];` (106), `yb=[y(end-1),y(end),y(1),y(2)];` (107). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37–38: dist와 distmax는 모두 같은 두 끝점의 유클리드 거리(Euclidean distance)이다. distmax 행의 전체 거리 최댓값 대안은 주석이다.
- 39: ds0는 처음 두 점 거리로 계산되지만 이후 실행식에서 참조하지 않는다.
- 39·42: 처음 두 점 x(2)·y(2)를 참조한 다음 length(x)<3 조건을 검사한다.
- 43–55·80–109: 최소·최대 범위와 nmax 갱신은 양 끝 방향 방식 안에 있다. 여러 육지 점 방식에는 해당 필드를 갱신하는 대입이 없다.

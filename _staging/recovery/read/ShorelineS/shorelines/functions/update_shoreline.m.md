---
file: models/ShorelineS/raw/source_code/shorelines/functions/update_shoreline.m
lines: 116
sha256: 9f6d8456bafadb8daa6632301a2717c4c38b6e99297770180b69890161edfac8
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# update_shoreline.m — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 함수 시그니처(1), 격자 수심 지형(bathymetry)에서 해안선을 갱신하는 목적(4), 저작권·LGPL·무보증·빈 줄(6–33). ds0를 가져오고 비스칼라이면 세 번째 열의 최소값으로 바꾼다(34–37). 입력 S·COAST·FORMAT의 기본값 설정문은 없다. 원문: `function [FORMAT,COAST]=update_shoreline(S,COAST,FORMAT)` (1), `ds0=COAST.ds0;` (34), `if ~isscalar(ds0)` (35), `ds0=min(ds0(:,3));` (36). |
| 39–63 | 시작 시 1행 함수 안. S.tideinteraction 조건에서 distmax·해안 변위 배열·지형 변화 sedero를 정한다(39–42). yesplot=false와 if yesplot 그림 준비 블록이 있다(43–46). 격자 루프에서 get_disttopolyline의 마지막 인수로 10000을 넘기며 dist<distmax인 셀의 체적 변화 dV를 ds0·h0·nt로 나눠 해당 해안점 변위에 더한다(50–55). 같은 조건에서 plot·hold on을 실행한다(56–57). NaN 구분자로 요소 수를 세고 기존 해안 좌표를 보관한다(61–63). 원문: `if S.tideinteraction` (39), `distmax=abs(S.seamin/S.seaslope);` (40), `dntide_mc=COAST.x_mc*0;` (41), `sedero=S.zg-S.zg0;` (42), `yesplot=false;` (43), `if yesplot` (44), `figure(12);clf;` (45), `xg=S.xg;` (47), `yg=S.yg;` (48), `zg=S.zg;` (49), `for i=1:size(xg,2)` (50), `for j=1:size(xg,1)` (51), `[dist(j,i),ip]=get_disttopolyline(COAST.x_mc,COAST.y_mc,xg(j,i),yg(j,i),10000);` (52), `if dist(j,i)<distmax` (53), `dV=(sedero(j,i))*S.dsdn(j,i);` (54), `dntide_mc(ip)=dntide_mc(ip)+dV/ds0/COAST.h0/COAST.nt;` (55), `plot([COAST.x_mc(ip),xg(j,i)],[COAST.y_mc(ip),yg(j,i)],'m');` (56), `hold on` (57), `n_mc=length(find(isnan(COAST.x_mc)))+1;` (61), `x_mc_old=COAST.x_mc;` (62), `y_mc_old=COAST.y_mc;` (63). [10-12 전수 검증 정정] |
| 64–95 | 시작 시 1행 함수·39행 조석 상호작용 참 분기 안. 요소별 get_one_polyvar로 좌표와 변위를 얻는다(64–67). n=length(x)−1이며 양 끝 거리가 ds0 미만이면 cyclic으로 판단한다(69–72). 순환 해안은 get_mod, 열린 해안은 max/min으로 이웃 인덱스를 정한다(73–80). 변위를 접선에 수직인 dx·dy로 바꾸고 좌표에 더한다(81–88). 순환 해안의 마지막 점을 첫 점으로 복사한 뒤 insert_section을 호출한다(89–95). 원문: `for i_mc=1:n_mc` (64), `x=get_one_polyvar(COAST.x_mc,i_mc);` (65), `y=get_one_polyvar(COAST.y_mc,i_mc);` (66), `dntide=get_one_polyvar(dntide_mc,i_mc);` (67), `n=length(x)-1;` (69), `cyclic = hypot(x(end)-x(1),y(end)-y(1))<ds0;` (72), `for i=1:n` (73), `if cyclic` (74), `im1=get_mod(i-1,n);` (75), `ip1=get_mod(i+1,n);` (76), `else` (77), `im1=max(i-1,1);` (78), `ip1=min(i+1,n+1);` (79), `dn=dntide(i);` (81), `dx(i)=-dn*(y(ip1)-y(im1))/hypot(x(ip1)-x(im1),y(ip1)-y(im1));` (82), `dy(i)= dn*(x(ip1)-x(im1))/hypot(x(ip1)-x(im1),y(ip1)-y(im1));` (83), `for i=1:n` (85), `x(i)=x(i)+dx(i);` (86), `y(i)=y(i)+dy(i);` (87), `if cyclic` (89), `x(n+1)=x(1);` (90), `y(n+1)=y(1);` (91), `[COAST.x_mc,COAST.y_mc]=insert_section(x,y,COAST.x_mc,COAST.y_mc,i_mc);` (94). |
| 96–116 | 시작 시 1행 함수·39행 조석 상호작용 참 분기 안이며 요소 루프 밖. COAST.dntide를 저장하고 pcolor·caxis·colorbar·shading·plot으로 지형 변화와 해안선을 표시한다(97–105). FORMAT.ifig가 있으면 1 증가, 없으면 1000을 설정한다(106–110). 이미지 저장과 pause는 주석이다(111–114). 조건과 함수가 끝난다(115–116). 원문: `COAST.dntide=dntide_mc;` (97), `pcolor(xg,yg,sedero);` (98), `cmax=max(max(abs(sedero)));` (99), `caxis([-cmax cmax])` (100), `colorbar;` (101), `shading flat;` (102), `hold on` (103), `plot(x_mc_old,y_mc_old,COAST.x_mc,COAST.y_mc,'linewidth',2);` (104), `axis equal` (105), `if isfield(FORMAT,'ifig')` (106), `FORMAT.ifig=FORMAT.ifig+1;` (107), `else` (108), `FORMAT.ifig=1000;` (109). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 43–46·56–57·98–105: yesplot=false는 그림 초기화 조건에만 사용된다. 셀 plot과 마지막 지형·해안선 도시는 yesplot 조건 밖에 있다.
- 49: zg는 S.zg 대입 이후 이 파일에서 참조되지 않는다.
- 69·73·85·89–92: n=length(x)−1로 두 좌표 갱신 루프를 제한한다. 마지막 좌표를 별도로 대입하는 조건은 cyclic일 때만 있다.
- 82–83: 이웃 점 간 hypot을 분모로 쓴다. 해당 거리가 0인지 검사하는 조건은 이 블록에 없다.

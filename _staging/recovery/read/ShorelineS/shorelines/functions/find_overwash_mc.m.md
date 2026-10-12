---
file: models/ShorelineS/raw/source_code/shorelines/functions/find_overwash_mc.m
lines: 206
sha256: 1df070b71fbdb6b2f85b950065ecccfc6c97103b192b54ab875f33584122aab6
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# find_overwash_mc.m — 판독 구간 기록

구간은 1행부터 206행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–63 | 함수 시그니처 `function [ COAST,SPIT ] = find_overwash_mc(COAST,WAVE,SPIT,STRUC,TRANSP,DUNE,MUD,TIME)` (1). 장벽(barrier) 바다 쪽에서 육지 쪽으로 월파(overwash) 표사를 옮기는 과정·차폐(shadowing) 회피·교차 검사·입출력 필드 설명(4–35). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(36–63). |
| 64–88 | 광선 시작 이격값 `eps=5;` (65), yesplot=0(66), 전체 좌표 크기의 dxt·dyt 0 초기화(67–68). 구간 루프 `for ii=1:COAST.n_mc` (73), get_segmentdata 호출(75). 짧은 구간 조건 `if length(COAST.x)<3` (77)이면 return(78). SPIT.width 0 초기화(80). 수송점 파향의 중간 방향 `phiw_coast=mod(atan2d(sind(0.5*(WAVE.PHI(1:end-1)+WAVE.PHI(2:end))),cosd(0.5*(WAVE.PHI(1:end-1)+WAVE.PHI(2:end)))),360.0);` (83). 해안 법선(shore normal) 방향 검사선 좌표 `x_nl=[COAST.x-eps*sind(COAST.PHIcxy);COAST.x-SPIT.spitwidth*sind(COAST.PHIcxy)];` (86); `y_nl=[COAST.y-eps*cosd(COAST.PHIcxy);COAST.y-SPIT.spitwidth*cosd(COAST.PHIcxy)];` (87). 자료 선택·계산·호출의 원문은 `[COAST,WAVE,~]=get_segmentdata(COAST,WAVE,TRANSP,DUNE,MUD,ii);` (75). |
| 89–131 | 시작 시 73행 ii 루프 안. 점 루프 `for i=1:length(COAST.x)` (90), 차폐 회피 `if ~COAST.shadow(i)` (92). 비활성 옛 방식 `if 0 % old approach` (93), 순환 조건 `if COAST.cyclic` (94), 인덱스·내부 조건 `im1=i-1;if im1<1;im1=COAST.n-1;end` (95); `ip1=i+1;if ip1>COAST.n;ip1=2;end` (96), 비순환 `else` (97)의 인덱스 제한 `im1=max(i-1,1);` (98); `ip1=min(i+1,COAST.n);` (99). 해안선·구조물 get_intersections 호출(104·108). 유효 해안 교차·구조물 무교차 조건 `if ~isempty(xcr) & ~isnan(xcr) & ~isnan(ycr) & isempty(xhr)` (110). 인접 후보 `ind_mc=unique([ind_mc,ind_mc+1]);` (113), 후보 좌표 복사(114–115), 거리·정렬·최소 폭 `distance           = hypot(xcr2-COAST.x(i),ycr2-COAST.y(i));` (116); `[dist2,ids]        = sort(distance);` (117); `[SPIT.width(i)]    = min(distance);` (118), 가까운 두 인덱스 복사(119–120), 제한 및 정규화 가중치 `weight_j           = max(min(1-distance(ids(1))/SPIT.spitwidth,1),0);` (121); `weight_jp1         = max(min(1-distance(ids(2))/SPIT.spitwidth,1),0);` (122); `wght2              = weight_j+weight_jp1;` (123); `weight_j           = min(weight_j/wght2,1);` (124); `weight_jp1         = min(weight_jp1/wght2,1);` (125). 그림·로그는 주석 처리(127–130). 자료 선택·계산·호출의 원문은 `[xcr,ycr,~,~,ind_mc,~,ui,~]=get_intersections(COAST.x_mc,COAST.y_mc,x_nl(:,i),y_nl(:,i));` (104); `[xhr,yhr]=get_intersections(STRUC.xhard,STRUC.yhard,x_nl(:,i),y_nl(:,i));` (108). |
| 132–146 | 시작 시 73행 ii·90행 i 루프·92행 비차폐 참 분기·110행 유효 교차 참 분기 안. 방법 선택 `switch lower(SPIT.method)` (133). 기본 방법 `case ('default')` (134), 시간 척도 조건 `if SPIT.owtimescale>0` (135), 바다 쪽·배후 장벽(backbarrier) 이동 `dn_sea  = -TIME.dt/SPIT.owtimescale*max(SPIT.spitwidth-SPIT.width(i),0)*max(cosd(phiw_coast(i)-COAST.PHIcxy(i)),0);` (136); `dn_back = -dn_sea  *(SPIT.Dsf+SPIT.bheight)/(SPIT.Dbb+SPIT.bheight);` (137). 시간 척도 대체 `else` (138)의 이동 `dn_sea  = -SPIT.owscale*max(SPIT.spitwidth-SPIT.width(i),0)*max(cosd(phiw_coast(i)-COAST.PHIcxy(i)),0);` (139); `dn_back = -dn_sea  *(SPIT.Dsf+SPIT.bheight)/(SPIT.Dbb+SPIT.bheight);` (140). 사구(dune) 월파 `case ('dune_overwash')` (142)는 dn_sea=0(143)과 `dn_back = TIME.dt*COAST.ql(i)/(COAST.dcelev(i)+SPIT.Dbb);` (144). switch 종료(145). |
| 147–160 | 시작 시 73행 ii·90행 i 루프·92행 비차폐 참 분기·110행 유효 교차 참 분기 안. 비활성 이동법 `if 0 % old approach` (148), 간격·좌표 증분 `ds_sea=hypot(COAST.x(ip1)-COAST.x(im1),COAST.y(ip1)-COAST.y(im1));` (149); `dx=-dn_sea*(COAST.y(ip1)-COAST.y(im1))/ds_sea;` (150); `dy= dn_sea*(COAST.x(ip1)-COAST.x(im1))/ds_sea;` (151). 실행 경로 `else` (152)의 증분 `dx= dn_sea*sind(COAST.PHIcxy_mc(j));` (153); `dy= dn_sea*cosd(COAST.PHIcxy_mc(j));` (154). 바다 쪽 점의 전체 배열 누적 `dxt(i+COAST.i1-1)=dxt(i+COAST.i1-1)+dx;` (158); `dyt(i+COAST.i1-1)=dyt(i+COAST.i1-1)+dy;` (159). |
| 161–178 | 시작 시 73행 ii·90행 i 루프·92행 비차폐 참 분기·110행 유효 교차 참 분기 안. 비활성 배후 이동법 `if 0 % old approach` (162), 간격·가중 좌표 증분 `ds_back=hypot(COAST.x_mc(j+1)-COAST.x_mc(j),COAST.y_mc(j+1)-COAST.y_mc(j));` (163); `dxt(j)=-dn_back*(COAST.y_mc(j+1)-COAST.y_mc(j))/ds_back*weight_j;` (164); `dyt(j)= dn_back*(COAST.x_mc(j+1)-COAST.x_mc(j))/ds_back*weight_j;` (165); `dxt(jp1)=-dn_back*(COAST.y_mc(jp1)-COAST.y_mc(j))/ds_back*weight_jp1;` (166); `dyt(jp1)= dn_back*(COAST.x_mc(jp1)-COAST.x_mc(j))/ds_back*weight_jp1;` (167). 실행 `else` (168)의 두 배후 점 증분 `dxt(j)= dn_back*sind(COAST.PHIcxy_mc(j))*weight_j;` (169); `dyt(j)= dn_back*cosd(COAST.PHIcxy_mc(j))*weight_j;` (170); `dxt(jp1)= dn_back*sind(COAST.PHIcxy_mc(jp1))*weight_jp1;` (171); `dyt(jp1)= dn_back*cosd(COAST.PHIcxy_mc(jp1))*weight_jp1;` (172). 조건·루프 종료(173–177). |
| 179–206 | 순환 경계 구간 루프 `for ii=1:COAST.n_mc` (180), get_segmentdata 호출(181). 순환 조건 `if COAST.cyclic` (182), 양끝 증분 차이·차폐 조건 `if hypot(dxt(i1)-dxt(i2),dyt(i1)-dyt(i2)) > 1 & COAST.shadow(1)` (183), 증분 합 `sumdxt=dxt(i1)+dxt(i2);` (185); `sumdyt=dyt(i1)+dyt(i2);` (186), 양끝에 같은 합 복사(187–190). NaN 증분 0 대입(196–197), 좌표 갱신 `COAST.x_mc = COAST.x_mc + dxt;` (198); `COAST.y_mc = COAST.y_mc + dyt;` (199). 그림 조건 `if yesplot` (201)의 plot·hold off·drawnow(202–204). 함수 종료(206). 자료 선택·계산·호출의 원문은 `[COAST,WAVE,TRANSP,i1,i2] = get_segmentdata(COAST,WAVE,TRANSP,DUNE,MUD,ii);` (181). 추가 원문: `dxt(isnan(dxt))=0;` (196). `dyt(isnan(dyt))=0;` (197). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 65·86–87: 검사선은 해안에서 5만큼 이격한 점과 SPIT.spitwidth만큼 이격한 점으로 만든다.
- 77–78: 한 구간의 점 수가 3 미만이면 현재 구간만 건너뛰는 대신 함수 전체에서 return한다.
- 110: 교차 조건은 ~isnan(xcr)·~isnan(ycr)를 &로 연결하며 모든 교차에 대한 all 또는 any 호출은 없다.
- 121–125: wght2로 가중치를 정규화하며 wght2가 0인지 검사하는 분기는 없다.
- 133–145: switch에는 default·dune_overwash case만 있으며 otherwise와 switch 앞 dn_sea·dn_back 초기화는 없다.
- 153–154·158–159: 바다 쪽 i점의 증분 방향은 배후 후보 j의 COAST.PHIcxy_mc를 사용한다.
- 158–159·169–172: 바다 쪽 증분은 기존 dxt·dyt에 더한다. 배후 점 증분은 기존 값을 더하지 않고 대입한다.
- 80·118·73–177: SPIT.width는 각 ii에서 새로 초기화되므로 함수 출력에 마지막 처리 구간의 배열이 남는다.
- 1·108: STRUC.xhard·yhard 교차 출력 xhr·yhr 중 조건에는 xhr만 사용한다.

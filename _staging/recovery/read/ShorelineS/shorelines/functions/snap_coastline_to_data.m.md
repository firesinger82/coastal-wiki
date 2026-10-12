---
file: models/ShorelineS/raw/source_code/shorelines/functions/snap_coastline_to_data.m
lines: 45
sha256: 91c1d591d397266cd1e197e3a040723188d1e89aae63ae688a43252674c9616a
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# snap_coastline_to_data.m — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 함수 시그니처가 없는 MATLAB 스크립트(script)이다. 고정 자료는 `xm=[100,200,400,300];` (1), `ym=[20,30,-10,-20];` (2), `xd=[0,350,1000];` (3), `yd=[0,0,0];` (4), `ds0=10;` (5), `dsf=.001;` (6). S 구조체 입력과 S 필드 기본값은 없다. 빈 줄을 포함한다(7). |
| 8–22 | 선택 해안선(coastline)의 거리와 보간(interpolation) 격자를 만든다. `ds=hypot(diff(xd),diff(yd));` (9), `sd=[0,cumsum(ds)];` (10), `ns=ceil(sd(end)/ds0);` (12), `ds=sd(end)/ns;` (13), `sc=[0:ds:sd(end)];` (14), `xc=interp1(sd,xd,sc);` (15), `yc=interp1(sd,yd,sc);` (16). 세밀 격자는 `ns=ceil(sd(end)/dsf);` (18), `ds=sd(end)/ns;` (19), `sf=[0:ds:sd(end)];` (20), `xf=interp1(sd,xd,sf);` (21), `yf=interp1(sd,yd,sf);` (22). 두 해상도 구분 주석을 포함한다. |
| 23–34 | 측정점과 세밀 해안선 사이 거리를 구한다. `dist=hypot(xm-xf',ym-yf');` (24), `[distmin,ind]=min(dist);` (25), `dirc=atan2d(yf(ind+1)-yf(ind-1),xf(ind+1)-xf(ind-1));` (26), `dirm=atan2d(ym-yf(ind-1),xm-xf(ind-1));` (27), `dmin=distmin.*sign(sind(dirm-dirc));` (28). `[ind,ind2]=sort(ind);` (30), `dmin=dmin(ind2);` (31), `corr=interp1(sf(ind),dmin,sc);` (32), `corr(isnan(corr))=0;` (33). figure·plot으로 해안선·측정점·보정값을 표시한다(34). |
| 35–45 | `dirc=zeros(size(xc));` (35). 끝점과 내부 방향식은 `dirc(1)=atan2d(yc(2)-yc(1),xc(2)-xc(1));` (36), `dirc(end)=atan2d(yc(end)-yc(end-1),xc(end)-xc(end-1));` (37), `dirc(2:end-1)=atan2d(yc(3:end)-yc(1:end-2),xc(3:end)-xc(1:end-2));` (38). 보정식은 `dx= corr.*sind(dirc);` (39), `dy= corr.*cosd(dirc);` (40), `xccorr=xc+dx;` (41), `yccorr=yc+dy;` (42). figure·plot으로 원래·측정·보정 해안선을 표시하고 axis equal을 호출한다(43–44). 마지막 빈 줄을 포함한다(45). 이 파일에는 조건·루프가 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–6: 측정점·해안선 좌표와 두 격자 간격은 스크립트에 고정되어 있다.
- 25–27: 최근접 인덱스 ind를 구한 뒤 ind+1·ind-1을 바로 참조한다. 해당 참조 앞에 끝점 인덱스 검사는 없다.
- 32–33: 보정값 보간 뒤 모든 NaN 보정값을 0으로 대입한다.

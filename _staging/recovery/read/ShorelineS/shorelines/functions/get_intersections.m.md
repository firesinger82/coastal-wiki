---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_intersections.m
lines: 229
sha256: 12ddb808f130a847c699a7f93bcc7e6a1f01c0d7781537f14c1bda729d4d4f58
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_intersections.m — 판독 구간 기록

구간은 1행부터 229행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–61 | 함수 시그니처는 `function [xcr,ycr,indc,inds,indi,indj,ui,uj]=get_intersections(xi0,yi0,xj0,yj0)` (1). 다각형(polygon) 교차점(crossing) 좌표·정수 인덱스(index)·선분(segment) 내 비율·분수 인덱스의 입력·출력 설명과 자기 교차 호출 형태를 적는다(2–33). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(34–61). |
| 62–109 | 시작 시 1행 get_intersections 함수 안. 허용 오차(tolerance)는 `eps=1e-5;` (62). removesameindex·disentangle을 0으로 초기화한다(63–64). `if nargin==2` (65)이면 두 번째 다각형에 첫 번째 좌표를 복사하고 removesameindex=1로 설정한다(66–68). `elseif nargin==3` (69)이면 같은 복사와 removesameindex=1·disentangle=1을 설정한다(70–73). 행 벡터(row vector) 변환식은 `xi0=xi0(:)';` (75); `yi0=yi0(:)';` (76); `xj0=xj0(:)';` (77); `yj0=yj0(:)';` (78). 여섯 출력 배열을 비운다(80–85). 선분 수 식은 `m0=length(xi0)-1;` (87); `n0=length(xj0)-1;` (88). 시작점 확장식은 `xi=repmat(xi0(1:m0)',[1,n0]);` (90); `yi=repmat(yi0(1:m0)',[1,n0]);` (91); `xj=repmat(xj0(1:n0),[m0,1]);` (92); `yj=repmat(yj0(1:n0),[m0,1]);` (93). 선분의 x·y 최솟값·최댓값 식은 `ximin=min(repmat(xi0(1:m0)',[1,n0]),repmat(xi0(2:m0+1)',[1,n0]));` (95); `ximax=max(repmat(xi0(1:m0)',[1,n0]),repmat(xi0(2:m0+1)',[1,n0]));` (96); `yimin=min(repmat(yi0(1:m0)',[1,n0]),repmat(yi0(2:m0+1)',[1,n0]));` (97); `yimax=max(repmat(yi0(1:m0)',[1,n0]),repmat(yi0(2:m0+1)',[1,n0]));` (98), `xjmin=min(repmat(xj0(1:n0),[m0,1]),repmat(xj0(2:n0+1),[m0,1]));` (100); `xjmax=max(repmat(xj0(1:n0),[m0,1]),repmat(xj0(2:n0+1),[m0,1]));` (101); `yjmin=min(repmat(yj0(1:n0),[m0,1]),repmat(yj0(2:n0+1),[m0,1]));` (102); `yjmax=max(repmat(yj0(1:n0),[m0,1]),repmat(yj0(2:n0+1),[m0,1]));` (103). nn=0으로 초기화한다(105). 좌표차 확장식은 `dx1=repmat(diff(xi0)',[1,n0]);` (106); `dy1=repmat(diff(yi0)',[1,n0]);` (107); `dx2=repmat(diff(xj0),[m0,1]);` (108); `dy2=repmat(diff(yj0),[m0,1]);` (109). |
| 110–144 | 시작 시 1행 get_intersections 함수 안. 기울기(gradient)·절편 식은 `rc1 = dy1./dx1;` (112); `rc2 = dy2./dx2;` (113); `y1r = yi-xi.*rc1;` (114); `y2r = yj-xj.*rc2;` (115). 일반 교차 후보식은 `xcr1 = (y2r-y1r)./(rc1-rc2);` (118); `ycr1 = rc1.*xcr1+y1r;` (119). 수직 선분용 후보는 xi·xj를 복사하고 `ycr2 = rc2.*xcr2+y2r;` (121), `ycr3 = rc1.*xcr3+y1r;` (123)을 계산한다(120·122). xc·yc를 NaN으로 초기화한다(126·130). 좌표차 조건에 따른 후보 배치는 `xc(dx1==0 & dx2~=0)=xcr2(dx1==0 & dx2~=0);` (127); `xc(dx1~=0 & dx2==0)=xcr3(dx1~=0 & dx2==0);` (128); `xc(dx1~=0 & dx2~=0)=xcr1(dx1~=0 & dx2~=0);` (129), `yc(dx1==0 & dx2~=0)=ycr2(dx1==0 & dx2~=0);` (131); `yc(dx1~=0 & dx2==0)=ycr3(dx1~=0 & dx2==0);` (132); `yc(dx1~=0 & dx2~=0)=ycr1(dx1~=0 & dx2~=0);` (133). 134행은 주석이다. 선분 범위 밖 검사식은 `idnan1=xc<max(ximin,xjmin)-eps \| xc>min(ximax,xjmax)+eps;` (138), `idnan2=yc<max(yimin,yjmin)-eps \| yc>min(yimax,yjmax)+eps;` (141). 각각의 검사 인덱스로 xc·yc를 NaN으로 대체한다(139–140·142–143). 빈 줄·주석을 포함한다(110–111·116–117·124–125·135–137·144). |
| 145–178 | 시작 시 1행 get_intersections 함수 안. `if removesameindex==1` (147)이면 같은 선분과 인접 선분을 제외한다. 제거 인덱스 식은 `idremove=[1:m0+1:m0*n0];` (148), `idremove=[2:m0+1:m0*n0];` (151), `idremove=[m0+1:m0+1:m0*n0];` (154). 각 인덱스의 xc·yc를 NaN으로 설정한다(149–150·152–153·155–156). 그 안에서 `if disentangle==0` (159)이면 `mat0=meshgrid([1:m0],[1:n0]);` (160), `idmat=mat0>mat0';` (161)을 계산하고 한쪽 교차 후보를 NaN으로 만든다(162–163). `if xi0(1)==xi0(end) && yi0(1)==yi0(end) && ~isempty(xc)` (167)이면 닫힌 다각형의 첫·마지막 선분 접점을 양쪽에서 NaN으로 만든다(168–171). 두 분기 종료 뒤 교차 후보 검색과 단일 출력용 식은 `idnotnan=find(~isnan(xc));` (176), `xcr=min(length(idnotnan),1);` (177). 주석·빈 줄을 포함한다. |
| 179–196 | 시작 시 1행 get_intersections 함수 안. `if nargout>1` (179)이면 xcr·ycr에 후보 좌표를 복사한다(180–181). 인덱스 검색식은 `[indi,indj]=find(~isnan(xc));` (184). 비율 설명 주석 뒤 반복은 `for nn=1:length(xcr)` (190). i·j는 해당 교차점 인덱스를 복사한다(191–192). 각 다각형의 선분 내 비율 식은 `ui(1,nn)=((xcr(nn)-xi0(i)).*(xi0(i+1)-xi0(i))+(ycr(nn)-yi0(i))*(yi0(i+1)-yi0(i))) ./ ((xi0(i+1)-xi0(i)).^2+(yi0(i+1)-yi0(i)).^2);` (193), `uj(1,nn)=((xcr(nn)-xj0(j)).*(xj0(j+1)-xj0(j))+(ycr(nn)-yj0(j))*(yj0(j+1)-yj0(j))) ./ ((xj0(j+1)-xj0(j)).^2+(yj0(j+1)-yj0(j)).^2);` (194). 반복을 닫고 빈 줄을 포함한다(195–196). |
| 197–229 | 시작 시 1행 get_intersections 함수 안. 시작 시 179행 nargout>1 분기 안. 비율의 범위 제한식은 `ui=max(ui,0);` (199); `uj=max(uj,0);` (200); `ui=min(ui,1);` (201); `uj=min(uj,1);` (202). 첫 다각형의 분수 인덱스 중복 제거는 `[~,idu]=uniquetol(indi(:)+ui(:),eps);` (203). 선택된 인덱스로 xcr·ycr·indi·indj·ui·uj를 줄인다(204–209). 두 번째 다각형 중복 제거는 `[~,idv]=uniquetol(indj(:)+uj(:),eps);` (210). 같은 여섯 배열을 다시 선택한다(211–216). plot 문장은 주석이다(217–218). double 행 벡터 변환식은 `xcr=double(xcr(:)');` (220); `ycr=double(ycr(:)');` (221); `indi=double(indi(:)');` (222); `indj=double(indj(:)');` (223); `ui=double(ui(:)');` (224); `uj=double(uj(:)');` (225). 최종 분수 인덱스 식은 `indc=double(indi+ui);` (226), `inds=double(indj+uj);` (227). 분기·함수를 닫는다(228–229). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 62·138·141·203·210: 지역 변수 eps는 1e-5로 고정되어 있다. 좌표 범위 검사와 uniquetol 호출이 같은 값을 사용한다.
- 69–73: 인수가 3개이면 세 번째 입력 xj0의 전달값을 xi0로 덮어쓴다. disentangle은 전달값과 관계없이 1로 설정한다.
- 126–133: 후보 배치식에는 dx1==0과 dx2==0이 동시에 참인 경우를 채우는 문장이 없다. xc·yc의 초기값은 NaN이다.
- 176–181·226–228: 출력 수가 1개이면 xcr는 교차 후보 존재 여부를 나타내는 min(length(idnotnan),1) 값이다. 좌표와 분수 인덱스 계산은 nargout>1 분기 안에 있다.

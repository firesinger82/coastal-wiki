---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_smoothangles.m
lines: 126
sha256: 2a83449107e0aa896392aa2c8614a9301251b5e25fe4015381dca8c1dff25e7a
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_smoothangles.m — 판독 구간 기록

구간은 1행부터 126행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | 함수 시그니처는 `function [COAST,TRANSP]=get_smoothangles(COAST,TRANSP)` (1). 해안 방향(coastline orientation) 변화각을 제한하여 수송(transport)을 평활화(smoothing)하는 목적과 입출력을 설명한다(2–20). 입력 주석은 maxangle 기본 60도·권장 30–90도를 적는다(11). 이 구간에는 해당 필드 기본값 실행 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(21–48). |
| 49–64 | 시작 시 1행 get_smoothangles 함수 안. 파랑 조건 수·수송점 수와 방향차 식은 `nw       = size(TRANSP.QS,1); % number of wave conditions taken along at this timestep (can be more than 1 in case of simultaneous wave conditions)` (50); `nq       = size(TRANSP.QS,2); % number of coastline points` (51); `COAST.dPHIc=mod(diff(COAST.PHIc)+180,360)-180;` (52). `if COAST.clockwise && nw==1` (53)이면 볼록(convex) 계수 `convexfactor=0.5; % factor determines sensitivity to max angles at concvex sections (e.g. if set to 0.5 then a gradual transition from 50% to 100% of maxangle is achieved for convex sections)` (55), 후보 검색식 `idc1=find(COAST.dPHIc>COAST.maxangle*convexfactor & TRANSP.idrev(1:end-1)==0 & TRANSP.idrev(2:end)==0);` (56), 오목(concave) 계수 `concavefactor=0.5; % factor determines sensitivity to max angles at concave sections (e.g. if set to 0.5 then a gradual transition from 50% to 100% of maxangle is achieved for concave sections)` (57), 후보 검색식 `idc2=find(COAST.dPHIc<-COAST.maxangle*concavefactor & TRANSP.idrev(1:end-1)==0 & TRANSP.idrev(2:end)==0);` (58). 후보 합치기·차폐 제외식은 `idc=unique([idc1,idc2]);` (59); `idc=setdiff(idc,find(TRANSP.shadow & abs(COAST.dPHIc)<90)); % exclude shadowed areas` (60). `if ~COAST.cyclic` (61)이면 경계점 제외식 `idc=setdiff(idc,[1,2,length(COAST.dPHIc)-1,length(COAST.dPHIc)]); % exclude boundary points` (62). 분기 종료·빈 줄·주석을 포함한다(49·54·63–64). |
| 65–82 | 시작 시 1행 get_smoothangles 함수 안. 시작 시 53행 clockwise·nw==1 분기 안. `if ~isempty(idc)` (65)이면 QS0·QS0a·QS1·QS2에 원래 수송을 복사한다(67·70–71). get_smoothdata 호출과 대체식은 주석이다(68–69). 제한 계수 식은 `factor = min(max(abs(2*abs(COAST.dPHIc(idc))-COAST.maxangle/2)/(COAST.maxangle/2),0),1);  % scale from 0 to 1 for the range +0.5*maxangle° to +1*maxangle°` (72). 평활화에서 제외할 위치의 조건식은 `ids=COAST.dPHIc(idc).*(QS0(idc)-QS0(idc+1))<0;` (75). 해당 ids의 factor를 0으로 만든다(76). 양쪽 수송방향 가중치(weight) 식은 `QSfac1=(QS0(idc)+QS0(idc+1))/2<=0; % smoothing only downdrift of the spike (to the left for negative transport)` (77); `QSfac2=(QS0(idc)+QS0(idc+1))/2>=0; % smoothing only downdrift of the spike (to the right for positive transport)` (78); `fac=max((QSfac1+QSfac2),1);` (79); `QSfac1=QSfac1./fac;` (80); `QSfac2=QSfac2./fac;` (81). 빈 줄과 설명 주석을 포함한다(66·73–74·82). [10-12 전수 검증 정정] |
| 83–103 | 시작 시 1행 get_smoothangles 함수 안. 시작 시 53행 clockwise·nw==1 분기·65행 후보 존재 분기 안. 왼쪽 평활 반복은 `for nn=length(idc):-1:1 % sweep from right to left` (85). 누적식은 `QS1(idc(nn))=(1-factor(nn).*QSfac1(nn)).*QS0(idc(nn))+factor(nn).*QSfac1(nn).*min(QS1(idc(nn)+1),QS0(idc(nn)));` (87). 대체식은 주석이다(84·86). 오른쪽 반복은 `for nn=1:length(idc) % sweep from left to right` (92). 누적식은 `QS2(idc(nn)+1)=(1-factor(nn).*QSfac2(nn)).*QS0(idc(nn)+1)+factor(nn).*QSfac2(nn).*max(QS2(idc(nn)),QS0(idc(nn)+1));` (94). 대체식은 주석이다(91·93). ids를 0 배열로 만들고(98), 양쪽 혼합 계수·최종 수송 식은 `ids(idc)=-factor.*QSfac1;` (99); `ids(idc+1)=ids(idc+1)+factor.*QSfac2;` (100); `ids=(ids+1)/2;` (101); `TRANSP.QS=QS1.*(1-ids)+QS2.*ids;` (102). 반복 종료·설명 주석·빈 줄을 포함한다(83·88–90·95–97·103). |
| 104–126 | 시작 시 1행 get_smoothangles 함수 안. 시작 시 53행 clockwise·nw==1 분기·65행 후보 존재 분기 안. 디버그(debug) 조건은 `if 0` (105). 그 안의 후보 식은 `idc1=idc((factor.*QSfac1)>0.3);` (106); `idc2=idc((factor.*QSfac2)>0.3)+1;` (107); `idc3=unique([idc1,idc2]);` (108). hold on·plot·fprintf로 후보 위치와 수송을 출력한다(109–115). figure(111)·clf로 그림을 초기화하고 원래·최종 수송과 후보를 그린 뒤 figure(11)로 돌아간다(116–122). 118행 plot은 주석이다. 원래 수송의 표시 좌표식은 `plot([1:length(COAST.x)+1]-0.5,QS0,'b-');hold on` (117). 첫 후보의 표시 좌표식은 `plot(idc-0.5,QS0(idc),'m*');` (119). 다음 후보의 표시 좌표식은 `plot(idc+0.5,QS0(idc+1),'m*');` (120). 최종 수송의 표시 좌표식은 `plot([1:length(COAST.x)+1]-0.5,TRANSP.QS,'r-')` (121). 디버그·후보·clockwise 분기와 함수를 닫는다(123–126). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 52–53·102: COAST.dPHIc는 항상 계산한다. TRANSP.QS 평활 대입은 COAST.clockwise가 참이고 nw==1인 분기 안에 있다.
- 105–123: 디버그 그림과 출력은 상수 조건 if 0 안에 있다.

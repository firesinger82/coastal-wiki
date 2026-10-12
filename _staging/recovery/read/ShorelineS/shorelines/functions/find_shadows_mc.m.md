---
file: models/ShorelineS/raw/source_code/shorelines/functions/find_shadows_mc.m
lines: 124
sha256: be9b2f7883925f1d6a3f62b62bee63a25cd1cc68b3d1cdf92bba3145487dc453
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# find_shadows_mc.m — 판독 구간 기록

구간은 1행부터 124행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | 함수 시그니처 `function [ shadowS,elementnr ] = find_shadows_mc(xq,yq,x_mc,y_mc,PHIo,PHItdp,PHIbr,distw)` (1). 해안선·구조물·입사 파향으로 차폐(shadowing) 지점을 정하는 목적과 입력·출력 주석(4–21). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(22–49). |
| 50–64 | 수송점 수(51). 스칼라 외해 방향 조건 `if length(PHIo)==1` (52), 배열 확장 `PHIo=repmat(PHIo,[1,nq]);` (53). 선택 인수 조건 `if nargin<6` (55); `if nargin<7` (58); `if nargin<8` (61)에서 PHItdp=PHIo·PHIbr=PHItdp·distw=[] 기본값(56·59·62). 추가 원문: `nq=length(xq);` (51). [10-12 전수 검증 보완] |
| 65–74 | 쇄파대(surf zone)·쇄파점 부근(breaker zone)의 기본 길이와 외해 광선 길이 `lenSURF=250;` (66); `lenBREAKER=50;` (67); `len=repmat(5*hypot(max(xq)-min(xq),max(yq)-min(yq)),[1,nq]);` (68). 파랑 출력 지점 거리 조건 `if ~isempty(distw)` (69), 길이 제한·나머지 외해 거리 하한 1 `lenBREAKER=min(lenBREAKER,distw*0.5);  % breaker zone cannot be more than 50% of distance to nearest wave output station 'distw'` (70); `lenSURF=min(lenSURF,distw*1);        % surfzone cannot be more than 80% of distance to nearest wave output station 'distw'` (71); `len=max(distw-lenBREAKER-lenSURF,1);   % offshore distance of ray is remainder that is not the surfzone or breaker zone, with minimum width of 1` (72). [10-12 전수 검증 정정] |
| 75–91 | 빈 수송점 조건 `if nq==0` (76)에서 shadowS=[](77). 비어 있지 않은 `else` (78)은 shadowS=false·elementnr 셀 배열 초기화(79–80), 조건 행 루프 `for j=1:size(PHIbr,1)` (81). 쇄파 파향·근해 파향·외해 파향을 순서대로 잇는 x·y 광선의 연속 행 `xw=[xq+1.*sind(PHIbr(j,:));...` (83); `xq+lenBREAKER.*sind(PHIbr(j,:));...` (84); `xq+lenBREAKER.*sind(PHIbr(j,:))+lenSURF.*sind(PHItdp(j,:));...` (85); `xq+lenBREAKER.*sind(PHIbr(j,:))+lenSURF.*sind(PHItdp(j,:))+len.*sind(PHIo(j,:))];` (86); `yw=[yq+1.*cosd(PHIbr(j,:));...` (87); `yq+lenBREAKER.*cosd(PHIbr(j,:));...` (88); `yq+lenBREAKER.*cosd(PHIbr(j,:))+lenSURF.*cosd(PHItdp(j,:));...` (89); `yq+lenBREAKER.*cosd(PHIbr(j,:))+lenSURF.*cosd(PHItdp(j,:))+len.*cosd(PHIo(j,:))];` (90). |
| 92–112 | 시작 시 76행 if의 78행 else·81행 j 루프 안. 점 루프 `for i=1:size(PHIbr,2)` (92). 단일 출력 조건 `if nargout==1` (94), indc=[](95), 한 광선 교차 호출 `[xx1]=get_intersections(x_mc,y_mc,xw(:,i),yw(:,i));` (96), shadowS에 xx1 대입(97). 복수 출력 `else` (98)의 호출 `[xx1,yy1,indc]=get_intersections(x_mc,y_mc,xw,yw);` (99), 차폐 판정 `shadowS(j,i)=~isempty(xx1);` (100). 교차 인덱스 조건 `if ~isempty(indc)` (103), section0=[](104), 교차 루프 `for cc=1:length(indc)` (105), NaN 구분자 개수로 구간 번호 `jjcross=sum(isnan(x_mc(1:floor(indc(cc)))))+1;` (106), section0 복사(107), elementnr에 고유 구간 번호(109). 추가 원문: `elementnr{j,i}=unique(section0);` (109). [10-12 전수 검증 보완] |
| 113–124 | 시작 시 76행 if의 78행 else·81행 j·92행 i 루프 안. 비활성 디버그 조건 `if 0` (113), figure 100 초기화·수송점·해안선·선택 광선 그림과 axis equal·drawnow(114–119). 분기·루프·함수 종료(120–124). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·8–20: 입력 주석에는 x·y·hard, 출력 주석에는 xS·yS가 있으나 실행 시그니처는 xq·yq 입력과 shadowS·elementnr 출력이다.
- 71: 주석은 distw의 80%를 적는다. 실행식은 distw*1을 사용한다.
- 76–80: nq==0 경로는 shadowS만 대입하며 elementnr 대입이 없다.
- 96·99: 단일 출력 경로는 xw(:,i)·yw(:,i)를 전달한다. 복수 출력 경로는 xw·yw 전체를 전달한다.
- 97·100: 단일 출력 경로는 xx1을 shadowS에 대입한다. 복수 출력 경로는 ~isempty(xx1)을 대입한다.

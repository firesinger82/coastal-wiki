---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_smoothdata.m
lines: 108
sha256: aa576354b6c6fa662253cb5794cf453fc9167244dcae776631447df23f627b62
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_smoothdata.m — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 함수 시그니처는 `function [VAR]=get_smoothdata(VAR,smoothtype,smoothsteps,movwindow)` (1). 평활화(smoothing) 대상, 각도(angle)·벡터(vector)·스칼라(scalar) 방식, 반복 횟수 또는 혼합 계수, 이동 평균(moving average) 창(window) 입력을 설명한다(2–12). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(13–40). |
| 41–53 | 시작 시 1행 get_smoothdata 함수 안. `if nargin<3` (41)이면 기본값은 `smoothsteps=1;` (42), `movwindow=2;` (43). `if isempty(VAR)` (46)이면 `smoothsteps=0;` (47)로 평활 횟수를 0으로 설정한다. `if size(VAR,1)>1 && size(VAR,2)==1` (50)이면 행 벡터(row vector) 변환식 `VAR=VAR(:)';` (51). 분기 종료와 빈 줄을 포함한다(44–45·48–49·52–53). |
| 54–83 | 시작 시 1행 get_smoothdata 함수 안. 행 반복은 `for kk=1:size(VAR,1)` (54). VAR2에 해당 행을 복사한다(55). 평활 반복은 `for nn=1:max(smoothsteps,1)` (56). `if strcmpi(smoothtype,'avgmean')` (57)이면 평균 식 `VAR2=mean(VAR2);` (58). 중앙 각도 평활 분기 조건은 `elseif ((strcmpi(smoothtype,'angle') \|\|  strcmpi(smoothtype,'vector')) && nargin<4) ...` (59); `\|\| strcmpi(smoothtype,'anglemean') && nn<max(smoothsteps,1)` (60). 사인(sine)·코사인(cosine) 변환·인접 평균·복원·방향 제한식은 `sVAR=sind(VAR2(:))';` (61); `cVAR=cosd(VAR2(:))';` (62); `sVARavg=[sVAR(1),(sVAR(1:end-1)+sVAR(2:end))/2,sVAR(end)];` (63); `cVARavg=[cVAR(1),(cVAR(1:end-1)+cVAR(2:end))/2,cVAR(end)];` (64); `sVAR2=(sVARavg(1:end-1)+sVARavg(2:end))/2;` (65); `cVAR2=(cVARavg(1:end-1)+cVARavg(2:end))/2;` (66); `VAR2=atan2d(sVAR2,cVAR2);` (67); `VAR2=mod(VAR2,360);` (68). `if smoothsteps<1` (69)이면 alfa에 smoothsteps를 복사하고(70), 혼합식 `VAR2=atan2d((1-alfa)*sVAR+alfa*sVAR2,(1-alfa)*cVAR+alfa*cVAR2);` (71)과 제한식 `VAR2=mod(VAR2,360);` (72). `elseif (strcmpi(smoothtype,'angle') \|\| strcmpi(smoothtype,'vector')) && nargin==4` (74)이면 smoothdata 이동 평균·방향 복원식 `cVAR=smoothdata(cosd(VAR2),'movmean',movwindow);` (75); `sVAR=smoothdata(sind(VAR2),'movmean',movwindow);` (76); `VAR2=atan2d(sVAR,cVAR);` (77); `VAR2=mod(VAR2,360);` (78). `elseif strcmpi(smoothtype,'angleavgmean')` (79)이면 성분 평균·방향 복원식 `sVAR=mean(sind(VAR2));` (80); `cVAR=mean(cosd(VAR2));` (81); `VAR2=atan2d(sVAR,cVAR);` (82); `VAR2=mod(VAR2,360);` (83). |
| 84–108 | 시작 시 1행 get_smoothdata 함수 안. 시작 시 54행 kk 반복·56행 nn 반복·57행 방식 선택 if 블록 안. `elseif nargin==4` (84)이면 이동 평균식 `VAR2=smoothdata(VAR2,'movmean',movwindow);` (85). `elseif strcmpi(smoothtype,'anglemean') && nargin<4` (86)이면 성분 변환·인접점 평균·방향 복원식 `sVAR=sind(VAR2(:))';` (87); `cVAR=cosd(VAR2(:))';` (88); `sVARavg=(sVAR(1:end-1)+sVAR(2:end))/2;` (89); `cVARavg=(cVAR(1:end-1)+cVAR(2:end))/2;` (90); `VAR2=atan2d(sVARavg,cVARavg);` (91); `VAR2=mod(VAR2,360);` (92). `else` (93)이면 행 변환·중앙 평균식 `VAR2=VAR2(:)';` (94); `VARavg=[VAR2(1),(VAR2(1:end-1)+VAR2(2:end))/2,VAR2(end)];` (95); `VAR2=(VARavg(1:end-1)+VARavg(2:end))/2;` (96). 방식 분기·nn 반복을 닫는다(97–98). `if ~(strcmpi(smoothtype,'anglemean') && nn==max(smoothsteps,1))` (99)이면 VAR 해당 행에 VAR2를 복사한다(100). `else` (101)이면 `VAR(kk,1:end-1)=VAR2;` (102)로 끝 열을 제외한 구간에 VAR2를 복사한다. 그 안에서 `if kk==size(VAR,1)` (103)이면 `VAR=VAR(:,1:end-1);` (104)로 VAR의 마지막 열을 제거한다. 분기·kk 반복·함수를 닫는다(105–108). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46–47·56: 빈 입력은 smoothsteps=0으로 설정한다. 반복 범위는 max(smoothsteps,1)을 사용한다. 비어 있지 않은 입력에 smoothsteps=0을 전달해도 이 반복의 상한은 1이다.
- 50–51·99–107: 열 벡터 입력은 행 벡터로 바꾼다. 함수 끝에는 원래 열 방향을 복원하는 문장이 없다.

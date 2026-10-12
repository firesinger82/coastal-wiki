---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_polydistance.m
lines: 93
sha256: 867a30f10608f04113840386c910276dfdb8493cba8255008788f90845599b39
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_polydistance.m — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | 함수 시그니처는 `function [dmin,xcr,ycr,ujmin,dmax,xcm,ycm,ujmax] = get_polydistance(Xr,Yr,Xc,Yc,Lcrit)` (1). 입력 주석은 기준선(reference line)·해안선(coastline) 좌표를 설명한다(4–8). 출력 주석은 xcr·ycr를 가까운 교차점(crossing)의 좌표로 설명한다(12–13). 출력 주석은 dmax·xcm·ycm·ujmax를 가장 먼 교차점에 관한 값으로 설명한다(15–18). 출력 주석은 거리의 부호와 연안 방향(alongshore) 위치 인덱스(index)를 설명한다(11·14–18). 예제와 저작권·연락처·LGPL 2.1 이상·무보증 주석·빈 줄을 포함한다(20–50). [10-12 전수 검증 정정] |
| 51–74 | 시작 시 1행 get_polydistance 함수 안. `if nargin<5` (52)이면 양쪽 최대 횡단 거리(cross-shore distance)의 기본값은 `Lcrit=500;  % maximum cross-shore distance to reference line (at both sides)` (53). Xr·Yr을 열 벡터(column vector)로 바꾼다(55–56). 좌표차와 점별 평균 접선(tangent) 성분 식은 `dx=Xr(2:end)-Xr(1:end-1); %for line in-between each reference point` (57); `dy=Yr(2:end)-Yr(1:end-1);` (58); `dx2 = [dx(1);(dx(2:end)+dx(1:end-1))/2;dx(end)];` (59); `dy2 = [dy(1);(dy(2:end)+dy(1:end-1))/2;dy(end)];` (60). xcr·ycr·dmin·ujmin을 NaN 배열로 만든다(61–64). `if nargout>4` (65)이면 xcm·ycm·dmax·ujmax도 NaN으로 초기화한다(66–69). 접선 길이와 법선(normal) 양끝 좌표 식은 `Lxy=(dx2.^2+dy2.^2).^0.5;` (71); `Xrnormal = [Xr,Xr]+[-Lcrit./Lxy.*dy2,Lcrit./Lxy.*dy2];` (72); `Yrnormal = [Yr,Yr]+[Lcrit./Lxy.*dx2,-Lcrit./Lxy.*dx2];` (73). 주석·빈 줄을 포함한다(51·74). |
| 75–93 | 시작 시 1행 get_polydistance 함수 안. 기준점 반복은 `for ii=1:length(Xr)` (75). quick 대입은 주석이다(76). 법선과 해안의 get_intersections 호출은 `[xcr0,ycr0,~,~,~,~,ui,uj]=get_intersections(Xrnormal(ii,:),Yrnormal(ii,:),Xc,Yc);` (77). `if ~isempty(xcr0)` (78)이면 최소 비율 위치 검색식 `imin=find(ui==min(ui));` (79). xcr·ycr와 ujmin에 해당 값을 복사한다(80–81·83). 부호 있는 거리식은 `dmin(ii)=(0.5-ui(imin))*Lcrit*2;` (82). 그 안에서 `if nargout>4` (84)이면 최대 비율 검색식 `imax=find(ui==max(ui));` (85), 해당 좌표·ujmax 복사(86–87·89), 거리식 `dmax(ii)=(0.5-ui(imax))*Lcrit*2;` (88). 분기·반복·함수를 닫는다(90–93). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57–60·71–73: dx(1)·dx(end)·dy(1)·dy(end)를 사용한다. 이 파일에는 기준점 수가 2 이상인지 또는 Lxy가 0인지 확인하는 조건이 없다.
- 79·82·85·88: dmin·dmax 선택 기준은 abs(거리)가 아니라 ui의 최솟값·최댓값이다.
- 77·83·89: ujmin·ujmax에는 get_intersections의 마지막 출력 uj를 복사한다. 이 호출에서 선분 정수 인덱스 출력은 ~로 받는다.
- 79–81·85–87: imin·imax의 find 호출에는 첫 결과만 선택하는 인수가 없다. 이어지는 좌표 대입은 한 ii 원소에 수행한다.

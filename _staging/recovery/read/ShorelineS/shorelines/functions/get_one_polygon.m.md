---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_one_polygon.m
lines: 84
sha256: 3e55a482a9e5768e15aaf2fa61e35a54c341ea17210e1070e108b203323ab7ab
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_one_polygon.m — 판독 구간 기록

구간은 1행부터 84행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 함수 시그니처는 `function [ x,y,n_mc,i1,i2 ] = get_one_polygon( x_mc,y_mc,i_mc )` (1). 두 인수와 세 인수의 호출 형태를 설명한다(2–5). 다각형(polygon) 추출 함수의 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(6–33). |
| 34–50 | 시작 시 1행 get_one_polygon 함수 안. `if nargin<3` (34)이면 i_mc=y_mc·y_mc=x_mc로 두 인수를 재배치한다(35–36). NaN 검색과 연속 NaN 중 뒤쪽 원소 선택식은 `nans=find(isnan(x_mc));` (39), `nansremove=nans([false,diff(nans)==1]);` (40). 대체 선택식은 주석이다(41). `if ~isempty(nansremove)` (43)이면 유지 인덱스(index) 식 `idkeep=setdiff([1:length(x_mc)],nansremove);` (44), x_mc·y_mc 선택(45–46), 재검색식 `nans=find(isnan(x_mc));` (47). 다각형 수 식은 `n_mc=length(nans)+1;` (50). 빈 줄·분기 종료를 포함한다. |
| 51–84 | 시작 시 1행 get_one_polygon 함수 안. i_mc 제한식은 주석이다(51). `if isempty(nans)` (52)이면 i1=1과 `i2=length(x_mc);` (54). `else` (55)에서는 `if i_mc==1` (56)이면 i1=1과 `i2=nans(i_mc)-1;` (58). `elseif i_mc==n_mc` (59)이면 `i1=nans(i_mc-1)+1;` (60), `i2=length(x_mc);` (61). `elseif i_mc>n_mc` (62)이면 마지막 구간 시작·끝 식 `i1=nans(n_mc-1)+1;` (64), `i2=length(x_mc);` (65). `else` (66)이면 중간 구간 경계식 `i1=nans(i_mc-1)+1;` (67), `i2=nans(i_mc)-1;` (68). x·y에 i1:i2 구간을 복사한다(71–72). `if isempty(x_mc(~isnan(x_mc)))` (74)이면 n_mc=0으로 설정한다(75). `if nargin<3 && nargout==4` (78)이면 두 인수·네 출력 호출에 맞춰 y=n_mc·n_mc=i1·i1=i2로 출력 위치를 바꾼다(79–81). 분기·함수 종료와 빈 줄을 포함한다(69–70·76–77·82–84). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40·44–47·71–72: 연속 NaN을 제거한 x_mc·y_mc에서 구간 경계를 계산한다. 반환 i1·i2는 이 정리된 배열의 경계이다.
- 51·62–65: i_mc를 n_mc로 제한하는 문장은 주석이다. i_mc>n_mc 분기는 마지막 구간을 선택한다.

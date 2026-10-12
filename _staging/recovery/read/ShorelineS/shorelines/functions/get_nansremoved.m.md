---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_nansremoved.m
lines: 51
sha256: 37416d018b2652cfc6030bb32285da5c159ad033e970b4f6ad9ca5ba01bcaf2e
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_nansremoved.m — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 함수 시그니처는 `function [x_mc,y_mc] = get_nansremoved(x_mc,y_mc)` (1). 주석 시그니처·저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(2–31). |
| 32–51 | 시작 시 1행 get_nansremoved 함수 안. NaN 위치 검색식은 `nans=find(isnan(x_mc));` (32). 연속 NaN의 앞 원소에 표식을 넣는 식은 `x_mc(nans(diff(nans)==1))=-2e10;` (33), `y_mc(nans(diff(nans)==1))=-2e10;` (34). 표식 제거식은 `x_mc=x_mc(x_mc~=-2e10);` (35), `y_mc=y_mc(y_mc~=-2e10);` (36). `if ~isempty(x_mc)` (37) 안에서 `if isnan(x_mc(1))` (38)이면 x의 첫 원소를 `x_mc=x_mc(2:end);` (39)로 제거한다. y의 첫 원소를 `y_mc=y_mc(2:end);` (40)로 제거한다. 별도 `if ~isempty(x_mc)` (43) 안에서 `if isnan(x_mc(end))` (44)이면 x의 마지막 원소를 `x_mc=x_mc(1:end-1);` (45)로 제거한다. y의 마지막 원소를 `y_mc=y_mc(1:end-1);` (46)로 제거한다. 분기·함수 종료와 빈 줄을 포함한다(41–42·47–51). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–36: NaN 위치는 x_mc에서만 검색한다. 제거 표식 -2e10의 필터는 x_mc와 y_mc에 각각 적용한다. 원래 데이터가 -2e10인지 구분하는 별도 조건은 없다.

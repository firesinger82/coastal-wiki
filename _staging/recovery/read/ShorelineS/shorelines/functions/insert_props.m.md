---
file: models/ShorelineS/raw/source_code/shorelines/functions/insert_props.m
lines: 47
sha256: 631dba2a48efc515db7b6ba485886a29eaa7b498cfb5fff6059cab6cd4669735
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# insert_props.m — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 함수 시그니처는 `function [props_mc,i1,i2]=insert_props(propsnew,props_mc,i_mc)` (1). 여러 해안선(multi-coastline)의 속성(property) 행렬에서 각 행을 속성으로 취급하여 새 구간을 삽입한다는 설명과 예를 적는다(2–8). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(9–36). |
| 37–47 | 시작 시 1행 insert_props 함수 안. 행 수·NaN 구분 열 계산식은 `nrows=size(propsnew,1);` (37), `nans=zeros(nrows,1)*nan;` (38). 첫 속성 행에서 구간 경계를 얻는 get_one_polyvar 호출은 `[ propsold,i1,i2,n_mc ] = get_one_polyvar( props_mc(1,:),i_mc );` (40). `if i_mc<=n_mc` (41)이면 전체 행 교체식 `props_mc=[props_mc(:,1:i1-1),propsnew,props_mc(:,i2+1:end)];` (43). `else` (44)이면 NaN 구분 열과 새 자료를 붙이는 식 `props_mc=[props_mc,nans,propsnew];` (45). 설명 주석·분기·함수 종료를 포함한다(39·42·46–47). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40: get_one_polyvar의 propsold 출력은 이후 실행문에서 참조하지 않는다.
- 39–43: 교체 구간의 i1·i2는 props_mc의 첫 행에서만 얻는다. 다른 속성 행의 NaN 위치를 비교하는 조건은 없다.

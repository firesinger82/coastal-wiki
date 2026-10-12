---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_one_polyvar.m
lines: 56
sha256: 5795780e8a21158751d5234849d3b10031042827196cb86daac3218ed8c1c2b4
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_one_polyvar.m — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 함수 시그니처는 `function [ v,i1,i2,n_mc] = get_one_polyvar( v_mc,i_mc )` (1). NaN으로 나뉜 다각형 변수(polygon variable)를 추출한다. 주석 시그니처·저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(2–31). |
| 32–56 | 시작 시 1행 get_one_polyvar 함수 안. NaN 검색과 구간 수 식은 `nans=find(isnan(v_mc));` (32), `n_mc=length(nans)+1;` (33). `if isempty(nans)` (34)이면 i1=1과 `i2=length(v_mc);` (36). `else` (37)에서는 `if i_mc==1` (38)이면 i1=1과 `i2=nans(i_mc)-1;` (40). `elseif i_mc==n_mc;` (41)이면 `i1=nans(i_mc-1)+1;` (42), `i2=length(v_mc);` (43). `elseif i_mc>n_mc` (44)이면 i1=i2=0·v=[]로 설정하고 return한다(45–48). `else` (49)이면 중간 구간 경계식 `i1=nans(i_mc-1)+1;` (50), `i2=nans(i_mc)-1;` (51). 분기를 닫고 v_mc(i1:i2)를 v에 복사한다(52–54). 빈 줄·함수 종료를 포함한다(55–56). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–43: NaN이 없으면 i_mc를 검사하지 않고 전체 v_mc를 선택한다. 구간 수 n_mc는 빈 입력에서도 length(nans)+1로 계산한다.
- 32–33·38–51: 연속 NaN을 제거하는 문장이 없다. 각 NaN은 구간 수 계산에 포함된다.

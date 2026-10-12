---
file: models/ShorelineS/raw/source_code/shorelines/functions/insert_section.m
lines: 74
sha256: 7b84e0e7f68bbde8f09b090e140788230563da36be92dfc4aa59b6097134e212
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# insert_section.m — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 함수 시그니처(1)와 사용법·입출력 주석(2–25). NaN으로 구분한 해안선 구간(coastal segment) 배열에서 i_mc 구간을 새 데이터로 교체한다. 두 좌표 배열을 함께 처리하는 호출과 단일 배열의 3인수 호출을 설명한다. 원문: `function [x_mc,y_mc,i1,i2]=insert_section(xnew,ynew,x_mc,y_mc,i_mc)` (1). |
| 27–54 | 시작 시 1행 insert_section 함수 안. IHE Delft·Deltares의 2020년 저작권, 작성자·연락처, LGPL 2.1 이상과 무보증 안내(27–53). 빈 줄(54). |
| 55–67 | 시작 시 1행 insert_section 함수 안. 3인수 호출에서는 인수를 재배치한다(55–60). NaN을 -1e10으로 바꾸는 두 문장은 주석이다(62–63). get_one_polygon으로 원래 구간의 양 끝 인덱스를 얻고, 그 구간을 xnew·ynew로 교체한다(64–66). 원문: `if nargin==3` (55), `i_mc=x_mc;` (56), `x_mc=ynew;` (57), `y_mc=ynew;` (58), `ynew=xnew;` (59), `[ xold,yold,n_mc,i1,i2 ] = get_one_polygon( x_mc,y_mc,i_mc );%% insert x,y back into COAST.x_mc,COAST.y_mc` (64), `x_mc=[x_mc(1:i1-1),xnew,x_mc(i2+1:end)];` (65), `y_mc=[y_mc(1:i1-1),ynew,y_mc(i2+1:end)];` (66). |
| 68–74 | 시작 시 1행 insert_section 함수 안. 3인수·3출력 호출에서는 두 번째 출력에 원래 i1, 세 번째 출력에 원래 i2를 넣는다(68–71). 함수 종료와 빈 줄(73–74). 원문: `if nargout==3 && nargin==3` (68), `y_mc=i1;` (69), `i1=i2;` (70). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18: xnew 설명은 y-coordinates와 xnew 자신과의 동일 크기를 적는다.
- 64–66: get_one_polygon의 xold·yold·n_mc 출력은 이후 이 함수에서 참조하지 않는다.

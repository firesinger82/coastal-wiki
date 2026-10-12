---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_interpolated_waves_from_grid.m
lines: 78
sha256: 4638ce1f90cac5395515ca14fd5de10f4249c0e4efdc61871cd1e91782da88cd
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_interpolated_waves_from_grid.m — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | 함수 시그니처는 `function [H,phiw_cd,x_cd,y_cd]=get_interpolated_waves_from_grid(x,y,n,nq,surfwidth,xg,yg,Hg,phiwg)` (1). 해안선(coastline) 좌표·셀(cell) 수·수송점 수·쇄파대(surf zone) 폭·파랑 격자(wave grid)·파고(wave height)·파향(wave direction) 입력과 네 출력의 설명이 있다(2–22). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(23–50). |
| 51–66 | 시작 시 1행 get_interpolated_waves_from_grid 함수 안. H·phiw_cd를 빈 배열로 초기화한다(51–52). 폐쇄수심(depth of closure) 위치를 만든다는 주석과 주석 처리한 COAST.n 대입이 있다(53–54). 반복은 `for i=1:nq` (55). 인덱스(index) 식은 `i1=mod(i-1,n);` (56), `i2=mod(i,n);` (57). 좌표차와 거리 식은 `dX=x(i2)-x(i1);` (59); `dY=y(i2)-y(i1);` (60); `Hyp=hypot(dX,dY);` (61). 이동량은 `dx=surfwidth*sind(phiwg(1,1));` (62), `dy=surfwidth*cosd(phiwg(1,1));` (63). 파랑 추출 좌표는 `x_cd(i)=0.5*(x(i1)+x(i2))+dx;` (64), `y_cd(i)=0.5*(y(i1)+y(i2))+dy;` (65). 반복을 닫는다(66). |
| 67–78 | 시작 시 1행 get_interpolated_waves_from_grid 함수 안. 격자값 추출 반복은 `for i=1:nq` (67). `if ~isnan(x)` (68)이면 `[row,col]=find_in_grid(xg,yg,x_cd(i),y_cd(i));` (69)로 find_in_grid를 호출한다. 그 안에서 `if (size(row,1)>1)` (70)이면 `break %continue%/break to check` (71)로 반복을 중단한다. H·phiw_cd에 Hg·phiwg의 row,col 값을 복사한다(73–74). 분기·반복을 닫고(75–76), phiw_cd의 NaN을 phiwg(1,1)로 대체한다(77). 함수가 끝난다(78). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55–59: i=1에서 56행 식은 i1=mod(0,n)을 계산한다. 다음 좌표차 식은 x(i1)를 참조한다. 이 블록에는 인덱스에 1을 더하는 문장이 없다.
- 59–65: dX·dY로 계산한 Hyp는 이후 실행문에서 참조하지 않는다. dx·dy는 모든 위치에서 phiwg(1,1)을 사용한다.
- 67–76: NaN 조건은 x(i)가 아닌 x 전체를 사용한다. row의 첫 차원 크기가 1보다 크면 break를 실행하여 남은 추출 반복을 중단한다.

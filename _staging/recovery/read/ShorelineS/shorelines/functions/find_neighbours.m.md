---
file: models/ShorelineS/raw/source_code/shorelines/functions/find_neighbours.m
lines: 66
sha256: 262105460074960b34f5ad6eec17a8e0f458d9b7078afb14f223faaa4dffcfbd
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# find_neighbours.m — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 함수 시그니처 `function [icm1,icm2,icp1,icp2]=find_neighbours(x_mc,y_mc,i_mc)` (1). 순환 여부를 고려한 양쪽 첫째·둘째 이웃 인덱스와 입력·출력 설명(4–17). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(18–45). |
| 46–61 | get_sectionnr·get_one_polygon 호출 `section=get_sectionnr(x_mc);` (46); `[x, y, n_mc, i1, i2] = get_one_polygon(x_mc, y_mc, section(i_mc));` (47). 끝점 제외 수·국소 인덱스·순환 판정 `n=length(x)-1;` (48); `i=i_mc-i1+1;` (49); `cyclic=hypot(x(end)-x(1),y(end)-y(1))<10;` (50). 순환 조건 `if cyclic` (51)에서 get_mod로 네 이웃 계산 `im1=get_mod(i-1,n);` (52); `im2=get_mod(i-2,n);` (53); `ip1=get_mod(i+1,n);` (54); `ip2=get_mod(i+2,n);` (55). 비순환 `else` (56) 경로의 양끝 제한 `im1=max(i-1,1);` (57); `im2=max(i-2,1);` (58); `ip1=min(i+1,n+1);` (59); `ip2=min(i+2,n+1);` (60). |
| 62–66 | 전체 배열 인덱스로 변환 `icm1=im1+i1-1;` (62); `icm2=im2+i1-1;` (63); `icp1=ip1+i1-1;` (64); `icp2=ip2+i1-1;` (65). 함수 종료(66). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47: n_mc와 i2는 get_one_polygon에서 받지만 이후 실행 계산에서 사용되지 않는다.
- 50: 순환 판정은 양끝점 거리 10 미만으로 고정되어 있다.
- 4–10·46–49: 주석은 i_mc를 해안 구간 인덱스로 적는다. 실행문은 section(i_mc)로 구간을 고르고 i_mc-i1+1을 국소 점 인덱스로 계산한다.

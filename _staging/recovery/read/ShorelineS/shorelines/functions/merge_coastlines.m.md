---
file: models/ShorelineS/raw/source_code/shorelines/functions/merge_coastlines.m
lines: 85
sha256: 8b18582002fdd7239a3ad093426c6e869aa1f6a0e333943fd606c2339272c975
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# merge_coastlines.m — 판독 구간 기록

구간은 1행부터 85행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 함수 시그니처(1). 자기 교차(self-intersection)가 있는 해안 구간을 병합·분할한다는 설명(4–5). COAST 전체 좌표와 격자 크기를 입력으로, 갱신한 전체 좌표를 출력으로 적는다(7–16). 원문: `function [COAST,merged] = merge_coastlines(COAST,i_mc)` (1). |
| 18–45 | 시작 시 1행 merge_coastlines 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(18–45). |
| 46–66 | 시작 시 1행 merge_coastlines 함수 안. eps=1, s(1)=0, yesplot=0을 설정한다(47–49). get_one_polygon으로 구간 좌표·전체 구간 수를 가져오고 누적 거리를 만든다(50–51). get_cyclic이 참이면 양 끝의 중간 좌표로 첫 점·마지막 점을 일치시킨 뒤 insert_section으로 전체 배열에 넣는다(54–63). get_intersections로 교차점과 구간 인덱스를 얻고 x 좌표의 unique를 계산한다(64–65). 원문: `eps=1;` (47), `s(1)=0;` (48), `yesplot=0;` (49), `[ COAST.x,COAST.y,COAST.n_mc ] = get_one_polygon( COAST.x_mc,COAST.y_mc,i_mc );` (50), `s=[0,cumsum(hypot(diff(COAST.x),diff(COAST.y)))];` (51), `cyclic=get_cyclic(COAST.x,COAST.y,COAST.ds0);` (54), `if cyclic` (55), `x1=.5*(COAST.x(1)+COAST.x(end));` (56), `y1=.5*(COAST.y(1)+COAST.y(end));` (57), `COAST.x(1)=x1;` (58), `COAST.y(1)=y1;` (59), `COAST.x(end)=x1;` (60), `COAST.y(end)=y1;` (61), `[COAST.x_mc,COAST.y_mc]=insert_section(COAST.x,COAST.y,COAST.x_mc,COAST.y_mc,i_mc);` (62), `[xx,yy,indi,indj]=get_intersections(COAST.x,COAST.y);` (64), `xx0=unique(xx);` (65). |
| 67–76 | 시작 시 1행 merge_coastlines 함수 안. merged를 0으로 둔다(67). 서로 다른 교차 x 좌표가 2개이면 첫 두 indi·indj를 정렬한다(68–69). 교차점을 직접 넣는 대안식은 주석이다(70–71). 기존 좌표 슬라이스를 바깥 구간과 닫힌 내부 구간으로 나누고 NaN으로 구분한다(72–73). merged=1로 바꾸고 insert_section을 호출한다(74–76). 원문: `merged=0;` (67), `if length(xx0)==2` (68), `indi=sort([indi(1:2),indj(1:2)]);` (69), `xnew=[[COAST.x(1:floor(indi(1))),COAST.x(ceil(indi(4)):length(COAST.x))],nan,[COAST.x(ceil(indi(2)):floor(indi(3))),COAST.x(ceil(indi(2)))]];` (72), `ynew=[[COAST.y(1:floor(indi(1))),COAST.y(ceil(indi(4)):length(COAST.y))],nan,[COAST.y(ceil(indi(2)):floor(indi(3))),COAST.y(ceil(indi(2)))]];` (73), `merged=1;` (74), `[COAST.x_mc,COAST.y_mc]=insert_section(xnew,ynew,COAST.x_mc,COAST.y_mc,i_mc);` (76). |
| 77–85 | 시작 시 1행 merge_coastlines 함수·68행 교차 개수 분기 안. 77행 elseif는 서로 다른 교차 x 좌표가 1개인 경우이다. 첫 indi·indj를 정렬하고, 기존 좌표를 NaN으로 구분한 두 구간으로 만든다(78–80). merged=1과 insert_section 호출(81–83). 분기·함수 종료(84–85). 원문: `elseif length(xx0)==1` (77), `indi=sort([indi(1),indj(1)]);` (78), `xnew=[[COAST.x(1:floor(indi(1))),COAST.x(ceil(indi(2)):length(COAST.x))],nan,[COAST.x(ceil(indi(1)):floor(indi(2))),COAST.x(ceil(indi(1)))]];` (79), `ynew=[[COAST.y(1:floor(indi(1))),COAST.y(ceil(indi(2)):length(COAST.y))],nan,[COAST.y(ceil(indi(1)):floor(indi(2))),COAST.y(ceil(indi(1)))]];` (80), `merged=1;` (81), `[COAST.x_mc,COAST.y_mc]=insert_section(xnew,ynew,COAST.x_mc,COAST.y_mc,i_mc);` (83). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47·49·51: eps·yesplot·s는 설정 후 이 함수의 병합 조건·좌표 계산에 사용하지 않는다.
- 64–68·77: 교차 개수 분기는 unique(xx)의 길이를 사용한다. yy를 포함한 좌표쌍의 고유 개수를 계산하지 않는다.
- 68–84: 교차 x 고유값 개수 1과 2만 처리한다. 그 외 개수의 else는 없다.

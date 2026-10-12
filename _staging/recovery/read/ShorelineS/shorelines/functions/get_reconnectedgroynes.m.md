---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_reconnectedgroynes.m
lines: 79
sha256: 1e72dca88a777e0ced8a903d27672074366862b29a482296c519fcc42ad1ce20
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_reconnectedgroynes.m — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 함수 시그니처는 `function [COAST]=get_reconnectedgroynes(COAST,GROYNE)` (1). 돌제(groyne) 양쪽의 해안 구간(coastal segment) 연결을 위한 COAST·GROYNE 설명이 있다. 입력·출력 주석에는 WAVE·TRANSP도 적혀 있다(2–14). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(15–42). |
| 43–56 | 시작 시 1행 get_reconnectedgroynes 함수 안. COAST0에 입력 COAST를 보관한다(43). `if isfield(GROYNE,'idcoast')` (44)이면 돌제 반복 `for ig=1:size(GROYNE.idcoast,1)` (45). GROYNE.idcoast의 두 열을 i_mc1·i_mc2에 복사한다(48–49). `if ~isnan(i_mc1)` (50)이면 첫 구간의 get_one_polygon 호출 `[x1,n_mc1,i1start,i1end ] = get_one_polygon( COAST0.x_mc,i_mc1);` (51). `if ~isnan(i_mc2)` (53)이면 두 번째 구간 호출 `[x2,n_mc2,i2start,i2end ] = get_one_polygon( COAST0.x_mc,i_mc2);` (54). 분기 종료와 빈 줄·설명 주석을 포함한다(46–47·52·55–56). |
| 57–79 | 시작 시 1행 get_reconnectedgroynes 함수 안. 시작 시 44행 idcoast 존재 분기·45행 ig 반복 안. `if isnan(i_mc1) \|\| isnan(i_mc2)` (58)이면 한쪽 돌제라는 주석만 둔다(59). `elseif i2start-1==i1end+1` (60)이면 돌제 인덱스 식 `igroyne = i1end+1;` (62). 평균점 방식은 주석이다(63–64). 최초 구조물 교차 때 저장한 점을 사용한다는 주석 뒤 GROYNE.xg·yg를 복사한다(65–68). 좌표 결합식은 `COAST.x_mc=[COAST.x_mc(1:i1end),xg,COAST.x_mc(i2start:end)];` (70), `COAST.y_mc=[COAST.y_mc(1:i1end),yg,COAST.y_mc(i2start:end)];` (71). `else` (72)이면 비인접 구간 경고를 출력한다(73). 분기·돌제 반복을 닫는다(74–75). 같은 idcoast 분기 안에서 수송점(transport point) 재생성 호출은 `[COAST]=get_transportpoints(COAST);` (77). 분기·함수를 닫는다(78–79). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·6–7·12–13: 실행 시그니처의 인수는 COAST·GROYNE이며 출력은 COAST 하나이다. WAVE·TRANSP는 입출력 설명 주석에만 있다.
- 51·54·62: x1·x2·n_mc1·n_mc2와 igroyne은 대입 후 실행문에서 참조하지 않는다.
- 43·51·54·70–71: 구간 경계는 처음 복사한 COAST0에서 얻는다. 결합 좌표는 현재 COAST.x_mc·y_mc에서 가져온다.

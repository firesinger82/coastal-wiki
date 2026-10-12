---
file: models/ShorelineS/raw/source_code/shorelines/functions/find_in_grid.m
lines: 39
sha256: 98c3fc84cea3da1d07800dd3ce04bbd2ca00b59bcb1e2eb3928003ab83efdb84
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# find_in_grid.m — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 함수 시그니처 `function [row,col]=find_in_grid(x,y,x0,y0);` (1). 반복 시그니처 주석(2), 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(4–31). |
| 32–39 | 검색 범위·각 좌표축의 범위 마스크 `range=50000;` (32); `inrange=abs(x-x0)<range&abs(y-y0)<range;` (33). dist는 x 크기 0 배열(34). 범위 내 유클리드 거리(Euclidean distance)·범위 밖 대체값·최소 거리·같은 거리 위치 검색 `dist(inrange)=hypot(x(inrange)-x0,y(inrange)-y0);` (35); `dist(~inrange)=1.e10;` (36); `mindist=min(min(dist));` (37); `[row,col,val]=find(dist==mindist);` (38). 함수 종료(39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·36: 검색 범위는 50000, 범위 밖 거리는 1.e10으로 고정되어 있다.
- 37–38: 최소 거리와 같은 모든 위치를 find로 반환한다. 후보가 모두 범위 밖인 경우를 별도로 처리하는 분기는 없다.
- 38: val은 find의 세 번째 출력으로 받으며 이후 사용하지 않는다.

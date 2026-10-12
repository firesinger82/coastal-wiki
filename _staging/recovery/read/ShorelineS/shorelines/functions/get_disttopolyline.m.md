---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_disttopolyline.m
lines: 53
sha256: 8506689964dea5f2f9ccc0d1c0b8af9c708ab155f7c27467d241dee03f5420ba
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_disttopolyline.m — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 함수 시그니처 `function [distance,i]=get_disttopolyline(x,y,x0,y0,range)` (1). 점과 다중선(polyline)의 최단 거리 목적·구문 주석(4–8). 저작권·연락처·LGPL 2.1 이상·무보증(9–36). OpenEarthTools 소개 주석과 빈 줄(37–42). |
| 43–53 | 두 좌표축의 범위 마스크 `inrange=abs(x-x0)<range&abs(y-y0)<range;` (45). r 0 배열(46). 범위 내 제곱 거리·범위 밖 대체값 `r(inrange)=(x(inrange)-x0).^2+(y(inrange)-y0).^2;` (47); `r(~inrange)=1.e10;` (48). min으로 값·인덱스 검색 `[value,i]=min(r);` (51), 거리 제곱근 `distance=sqrt(value);` (52). 함수 종료(53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·7: 구문 예시 함수 이름은 locate_in_curvi_grid이며 실행 함수 이름과 다르다.
- 45–52: 거리 계산은 다중선의 저장 점에 대해 수행한다. 선분 내부 투영점 거리를 계산하는 문장은 없다.
- 48·51–52: 범위 밖 제곱 거리는 1.e10이다. 범위 내 점이 없을 때 별도 분기는 없다.

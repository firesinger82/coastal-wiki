---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_cumdist.m
lines: 37
sha256: 5f10eedecc57472fab9864439e9bb27147b36d827526f3bbb95a8d93132b4e88
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_cumdist.m — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 함수 시그니처 `function [ s ] = get_cumdist(x,y)` (1). 선을 따른 누적 거리(cumulative distance) 목적(4). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(6–33). |
| 34–37 | 인접점 거리·0에서 시작하는 누적 거리 `ds = hypot(diff(x),diff(y));` (34); `s = [0,cumsum(ds)];` (35). 함수 종료·빈 줄(36–37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34–35: 입력의 NaN을 따로 분리하거나 누적 합을 다시 시작하는 분기는 없다.

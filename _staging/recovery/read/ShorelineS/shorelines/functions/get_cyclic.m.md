---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_cyclic.m
lines: 40
sha256: 0751b1778d599796b01cefa2f614d1edc79d45046912f66f3384ec2822294876
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_cyclic.m — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 함수 시그니처 `function [ cyclic ] = get_cyclic(x,y,ds0)` (1). 다중선(polyline)의 순환 여부를 끝점 거리로 판정한다는 주석(4). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(6–33). |
| 34–40 | 격자 간격 비스칼라 조건 `if ~isscalar(ds0)` (34)이면 세 번째 열 최솟값 `ds0=min(ds0(:,3));` (35). 거리 허용 비율·순환 판정 `frac   = 0.2;` (37); `cyclic = hypot(x(end)-x(1),y(end)-y(1)) < frac*ds0;` (38). 함수 종료·빈 줄(39–40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34–35: 비스칼라 ds0는 세 번째 열에 접근하며 열 수 검사는 없다.
- 37–38: 순환 거리 허용 비율은 ds0의 0.2로 고정되어 있다.

---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_randsample.m
lines: 54
sha256: 7d33b81c188336e5b9acf4f56655904e0114a4041b2c36e23480008a88045ff8
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_randsample.m — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | 함수 시그니처는 `function [y]= get_randsample(n,k,wght)` (1). 파랑 조건(wave condition)의 발생 확률(probability)에 따른 표본(sample) 추출을 설명한다(2–13). 입력 주석은 k가 1이어야 한다고 적는다(8). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(14–41). |
| 42–54 | 시작 시 1행 get_randsample 함수 안. 가중치(weight) 행 벡터(row vector) 변환식은 `wght=wght(:)';` (42). `if isempty(wght)` (43)이면 균등 정수 표본식 `y = randi(n,k,1);` (44). `elseif length(wght)==n` (45)이면 가중치 합·정규화·누적 확률 식은 `sumwght = sum(wght);` (46); `p = wght / sumwght;` (47); `pcum=min([0,cumsum(p)],1);` (48). 누적 확률의 마지막 값은 `pcum(end) = 1;              % make sure the cumulative is exactly 1` (49). rand·histc 추출식은 `[~,y] = histc(rand(k,1),pcum);` (50). 분기 뒤 열 벡터(column vector) 변환식 `y = y(:);` (52). 빈 줄·함수 종료를 포함한다(51·53–54). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 43–51: 가중치가 비어 있지 않고 길이가 n과 다를 때의 else 분기는 없다. 이 경우를 위한 y 대입은 이 파일에 없다.
- 46–50: wght 합으로 나누기 전에 양수 합 또는 음수 가중치를 검사하는 조건이 없다.

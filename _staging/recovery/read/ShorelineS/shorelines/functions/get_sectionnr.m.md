---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_sectionnr.m
lines: 41
sha256: d6b889aed1efa340b6e1be751a14cbf4e09aa22efc8dab97265f1e7c43b9058a
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_sectionnr.m — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 함수 시그니처는 `function [section] = get_sectionnr(x_mc)` (1). NaN으로 나뉜 해안 구간(coastal section) 번호를 반환한다. 주석 시그니처·저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(2–31). |
| 32–41 | 시작 시 1행 get_sectionnr 함수 안. NaN 검색식은 `nans=find(isnan(x_mc));` (32). 출력 초기화식은 `section=zeros(size(x_mc))+nan;;` (33). 길이 계산식은 `n=length(x_mc);` (34). 첫 구간 번호 식은 `section(1:nans(1)-1)=1;` (35). 반복은 `for i=1:length(nans)-1;` (36). 중간 구간 번호 식은 `section(nans(i)+1:nans(i+1)-1)=i+1;` (37). 마지막 구간 번호 식은 `section(nans(end)+1:end)=length(nans)+1;` (39). 반복·함수 종료와 빈 줄을 포함한다(38·40–41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·35·39: nans(1)·nans(end)를 사용한다. NaN이 없는 입력에 대한 isempty(nans) 분기는 없다.
- 34: 지역 변수 n은 길이 대입 이후 참조하지 않는다.

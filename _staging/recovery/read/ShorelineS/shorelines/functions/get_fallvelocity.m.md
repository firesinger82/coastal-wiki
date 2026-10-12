---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_fallvelocity.m
lines: 39
sha256: e77df4c81fc8d758118a0c2cb8ad3284e59c62be8624a71cc3b9575cd1128b8a
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_fallvelocity.m — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 함수 시그니처 `function [ws] = get_fallvelocity(D50,rhos,sal,temp)` (1). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(4–31). |
| 32–39 | 온도 기반 동점성계수(kinematic viscosity)·중력가속도·염분 및 온도 기반 물 밀도·밀도비·무차원 입경(dimensionless grain size)·침강속도(fall velocity) `nu     = (1.14-0.031*(temp-15)+0.00068*(temp-15)^2)*10^-6;  % approximately 1e-6 at 20c;` (32); `g      = 9.81;` (33); `rhow   = max(1000+(0.8-(temp*0.002))*sal,1000);` (34); `s      = rhos/rhow;` (35); `Dster  = D50*((s-1)*g/(nu^2))^(1/3);` (36); `ws     = nu/D50*(sqrt(10.36^2 + 1.049*Dster.^3)-10.36);` (37). 물 밀도 하한은 1000(34). 함수 종료와 빈 줄(38–39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–34: 중력가속도는 9.81, 물 밀도 하한은 1000으로 고정되어 있다.
- 32·35–37: temp의 제곱·밀도비·입경 식에는 행렬 연산자 ^와 /가 있다. Dster의 세제곱에는 원소별 연산자 .^를 사용한다.

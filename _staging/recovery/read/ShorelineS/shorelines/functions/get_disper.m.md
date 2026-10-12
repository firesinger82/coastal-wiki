---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_disper.m
lines: 45
sha256: 6b77307e25d69ac366edc158652abbf23e123e20c3847fa0605082ab890ee702
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_disper.m — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 함수 시그니처 `function [k,C,Cg,n]=get_disper(h,T)` (1). Guo (2002) 근사 분산(dispersion) 해라는 주석(4). 수심·주기 입력과 파수(wave number)·파속(wave celerity)·군속도(group velocity)·n 출력(6–15). n의 주석 범위는 0.5..1(14). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(16–38). |
| 39–45 | 중력가속도·각주파수(angular frequency)·근사 파수·파속·군속도 비·군속도 `g=9.81;` (39); `sigma=2*pi./T;` (40); `k = sigma.^2./g.*(1-exp(-(sigma.*sqrt(h./g)).^2.5)).^(-0.4);` (41); `C = sigma./k;` (42); `n = 0.5+k.*h./sinh(2.*k.*h);` (43); `Cg=n.*C;` (44). 함수 종료(45). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39: 중력가속도는 9.81로 고정되어 있다.
- 40–43: 주기·파수·sinh(2*k*h)를 분모에 사용한다. 입력 0값을 처리하는 별도 조건은 없다.

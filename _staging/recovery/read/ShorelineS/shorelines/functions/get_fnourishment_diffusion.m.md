---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_fnourishment_diffusion.m
lines: 44
sha256: ec8d4e7711c3f0ee4e71d729ceae28bf19b8776ec76ac456e251de55c2b55b3b
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_fnourishment_diffusion.m — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 함수 시그니처 `function [K]=get_fnourishment_diffusion(V)` (1). 네덜란드 개방 해안(Dutch open coast)에 기반한 해안 전면 양빈(shoreface nourishment) 확산 계수(diffusion coefficient)라는 주석·입출력(4–12). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(13–40). |
| 41–44 | 체적의 선형 계수식·최소 계수 `K = -4.86E-5 * V + 0.035 ;` (41); `K(K < 0.001) = 0.001;` (42). 함수 종료·빈 줄(43–44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–42: 체적 계수 -4.86E-5, 절편 0.035, 계수 하한 0.001이 고정되어 있다.

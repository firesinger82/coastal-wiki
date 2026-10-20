---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/Details.h
lines: 60
sha256: ab83e4053831b8776458e01eea76e33aa8f67d2701ea207843eabec3626da4c0
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Details.h — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | `#pragma once` (1), SubDetails.h 포함(3), `lis::cuda::acc_nugrid` 이름공간(namespace)(5–10). Details 구조체(struct)(12–13)의 활성 SubDetails 필드는 z0·z1x·z1y(17·22·27), n0·n1x·n1y(30–32), h0·h1x·h1y(34–36). eta·qx·qy 계열과 zxy 선언은 주석(14–16·19–21·24–26·28). 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 38–60 | 시작 시 12행 Details 구조체 안. 생성자(constructor)는 num_details·non_uniform_n·startfile을 받는다(38–43). 초기화 목록 `z0(num_details),` (45), `z1x(num_details),` (46), `z1y(num_details),` (47)는 세 지형 계열에 같은 개수를 전달한다. 삼항식은 `n0(non_uniform_n ? num_details : 0),` (48), `n1x(non_uniform_n ? num_details : 0),` (49), `n1y(non_uniform_n ? num_details : 0),` (50), `h0(startfile ? num_details : 0),` (51), `h1x(startfile ? num_details : 0),` (52), `h1y(startfile ? num_details : 0)` (53). 생성자 본문은 비어 있다(54). 구조체·이름공간 종료와 빈 줄(55–60). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

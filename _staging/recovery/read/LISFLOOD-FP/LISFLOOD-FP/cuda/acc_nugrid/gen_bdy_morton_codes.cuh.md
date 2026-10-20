---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/gen_bdy_morton_codes.cuh
lines: 23
sha256: 01b75392fef62c35cba83ec2adaa853427af1e7118a6c56357a3cc5707c7da32
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# gen_bdy_morton_codes.cuh — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1), 모턴 코드(Morton code) 생성·방향·Boundary 헤더를 포함한다(3–5). 전처리 조건 분기는 없다. |
| 7–23 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(7–12) 안에 `void gen_bdy_morton_codes` (14)를 선언한다. 경계·매개변수·방향을 각각 const 참조로 받으며 기본값은 없다(15–19). 이름 공간 종료(21–23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

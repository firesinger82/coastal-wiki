---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/generate_all_morton_codes.cuh
lines: 26
sha256: 79ed26e7a782ea745c2fd342316a62866b848f7c5b7800ea71d46e0038faa7e0
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# generate_all_morton_codes.cuh — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1), CUDA 실행 환경·장치 실행 매개변수·CUDA 도구·모턴 코드(Morton code) 생성 및 형식·1차원 인덱스 헤더 포함(3–8). 전처리 조건 분기는 없다. |
| 10–26 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(10–15) 안에 `__global__ void generate_all_morton_codes` (17)를 선언한다. 모턴 코드 포인터·정수 순서 포인터·격자 폭을 받으며 기본값은 없다(18–22). 이름 공간 종료(24–26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

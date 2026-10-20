---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/project_assem_sol.cuh
lines: 31
sha256: cb45d74d63701b1cb2f8150ac4ef9e7f7163fb7270aeb6b16e148726caa1c8db
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# project_assem_sol.cuh — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–10 | `#pragma once`와 블록 수 계산·해 재삽입·유의 상세 트리 순회(significant detail tree traversal)·역 Z순서(reverse Z-order)·실수/정수 파일 출력 헤더를 포함한다(1–9). 전처리 조건 분기는 없다. 원문: `#pragma once` (1). |
| 11–18 | CUDA 커널(kernel) `load_soln_coeffs`를 선언한다(11–17). 조립 해·척도 계수(scale coefficients)·최세 원소 수를 값으로 받는다(14–16). 빈 줄을 포함한다(18). 원문: `__global__` (11). |
| 19–31 | CUDA 호스트 함수(host function) `project_assem_sol` 원형이다(19–31). 격자 크기·유의 상세 포인터·척도 계수·작업 해·해석기 매개변수·Morton 코드(Morton code) 배열 두 개·현재 해·출력 해를 받는다(22–30). 기본 인수와 실행 본문은 없다. 원문: `__host__` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

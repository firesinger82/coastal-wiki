---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Tridiag_js.md
lines: 25
sha256: 7e4177a2735de870855a6d4e340fecb4f5f7eaf0572c8df9bb6d38e1281c3726
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Tridiag_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Tridiag.js`

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 원문 링크와 병렬 순환 축소(Parallel Cyclic Reduction, PCR) 삼중대각 바인드 그룹(bind group) 설명이다(1–7). `0`은 `p`, `s`, 크기·변형별 uniform, `1`은 기본 행렬과 `two` 가변 PCR 계수 텍스처(texture) 사이에서 선택하는 입력, `2` 현재 상태, `3` 현재/중간 UV-star, `4`는 `1`과 짝인 임시 계수, `5` 임시 해, `6` COULWAVE용 `txBottom`이다(11–17). binding `4`와 `5`는 출력이며 binding `1`은 해당 방향의 계수 입력이다(12·15–16). [11-04 전수 검증 보완] |
| 19–25 | `Run_Tridiag_Solver.js`가 x/y 셰이더를 반복 실행하며 같은 배치의 여러 그룹으로 계수를 교대해 전체 복사를 피한다(21). 표준 PCR은 바인딩 `6`을 사용하지 않지만 COULWAVE와 공통 경로를 유지하려고 포함한다(25). solver 경로를 나누지 않고 binding `6`을 제거하면 안 된다고 안내한다(25). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25: 문서는 표준 PCR에서 바인딩 `6`을 사용하지 않는다고 명시한다.

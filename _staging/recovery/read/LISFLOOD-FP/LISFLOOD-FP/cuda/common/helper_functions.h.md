---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/common/helper_functions.h
lines: 59
sha256: b4c13046419d85bc9c895807b753f0359822761d97efe859b4e24097db240799
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# helper_functions.h — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | NVIDIA 2019 저작권·재배포 조건·무보증 주석(1–26), 빈 줄(27), SDK의 문자열·타이머·이미지 보조 함수라는 설명(28–29). |
| 30–54 | `#ifndef COMMON_HELPER_FUNCTIONS_H_` (30), `#define COMMON_HELPER_FUNCTIONS_H_` (31)의 헤더 가드(header guard) 안. `#ifdef WIN32` (33)에서 `#pragma warning(disable : 4996)` (34), `#endif` (35). assert·exception·math·stdio·stdlib(38–42), STL 헤더(44–48), helper_image·helper_string·helper_timer(51–53)를 포함한다. |
| 55–59 | 시작 시 30행 헤더 가드 안. `#ifndef EXIT_WAIVED` (55)에서 `#define EXIT_WAIVED 2` (56), `#endif` (57). 빈 줄(58), `#endif  // COMMON_HELPER_FUNCTIONS_H_` (59). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

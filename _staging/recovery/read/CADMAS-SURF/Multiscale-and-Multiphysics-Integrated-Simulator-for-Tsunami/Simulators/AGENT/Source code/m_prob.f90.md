---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/m_prob.f90
lines: 12
sha256: 92da30724e46657f3699fb7647ac4113fd82a769cc6c8cfb4ca5c32e5673e472
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_prob.f90 — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | m_prob 모듈은 `implicit none`(2), ini_prob·relaxation_rate, 길이 128의 두 디렉터리 문자열과 두 정수 플래그를 선언한다(5–9). 이 파일에 초기값 대입은 없다. 원문: `module m_prob` (1); `  implicit none` (2); `  !prob` (4); `  reaL(8):: ini_prob,relaxation_rate` (5); `  character(128) tsunami_prob_directory` (6); `  character(128) n_pot_directory` (7); `  integer:: flag_WPprob` (8); `  integer:: flag_RPprob` (9); `end module m_prob` (12) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

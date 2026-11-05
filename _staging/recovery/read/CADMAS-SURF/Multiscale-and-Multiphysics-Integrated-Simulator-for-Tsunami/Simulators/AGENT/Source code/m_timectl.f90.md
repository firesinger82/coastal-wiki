---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/m_timectl.f90
lines: 17
sha256: 04519350a0b8d32cf760bcf65fd0b59574abbfb65b457791194ec6d874e98749
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_timectl.f90 — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 시간 적분 제어 데이터 주석(4). nstep은 현재 계산 스텝 수(6), maxstep은 최대 스텝 수(7), time·dt·time_start·time_end는 현재 시각·시간 간격·시작 시각·종료 시각이며 단위는 s다(9–12). `implicit none`(2)과 정수·실수 변수를 선언한다(15–16). 원문: `module m_timectl` (1); `  implicit none` (2); `!----------------------------------------` (3); `! 時間積分制御データ` (4); `!` (5); `! nstep      現在の計算ステップ数` (6); `! maxstep    最大ステップ数` (7); `!` (8); `! time       現在の時刻(s)` (9); `! dt         時間刻み(s)` (10); `! time_start 計算開始時刻(s)` (11); `! time_end   計算終了時刻(s)` (12); `!----------------------------------------` (13); `!` (14); `  integer::nstep,maxstep` (15); `  real(8)::time,dt,time_start,time_end,time_begin_s,time_end_s` (16); `end module m_timectl` (17) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

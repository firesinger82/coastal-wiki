---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/slope_function.f90
lines: 26
sha256: 935ab92c8d21a9197104038ecd51d52a88c898e6449cabd11b2abc514684fdd8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# slope_function.f90 — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 사면 경사에 따른 이동 속력 변화율 계산 주석(3). 입력 주석(5)의 S는 높이 차/두 점 거리인 무차원 경사(6), 출력 주석(8)의 F는 무차원 이동 속력 보정 계수(9)다. `implicit none`(11)과 인수를 선언한다. 18행 정수 선언은 주석 처리되었다. 원문: `subroutine slope_function(S,F)` (1); `!----------------------------------------` (2); `! 斜面勾配による移動速度の変化率を計算` (3); `!` (4); `! <入力>` (5); `! S: 斜面勾配(=高低差/2点間の距離)[-]` (6); `!` (7); `! <出力>` (8); `! F: 移動速度の補正係数[-]` (9); `!----------------------------------------` (10); `  implicit none` (11); `!` (12); `![arguments]` (13); `  real(8),intent(in):: S` (14); `  real(8),intent(out):: F` (15); `!` (16); `![local variables]` (17); `!  integer:: i,j` (18); `!` (19); `!` (20) |
| 21–26 | 시작 시 1행 루틴 안. 아래를 편집하라는 주석(21), 예시는 하이킹 함수(hiking function)라는 주석(22). 원문의 지수함수 식(23)으로 F를 계산하고 반환한다. 원문: `! 以下を編集` (21); `! サンプル：ハイキング関数` (22); `  F=1.191246*exp(-3.5d0*abs(S+0.05d0))` (23); `!` (24); `  return` (25); `end subroutine slope_function` (26) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23: 계수 1.191246·-3.5d0과 경사 이동값 0.05d0은 식에 직접 고정되어 있다.

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ATIMER.h
lines: 18
sha256: 040c1c5ca9588bac174f7c0bd5dacd40fe068734ceed9946f6d1fb2f93c82e75
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ATIMER.h — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 종료·현재 시각, 현재·고정·초기·최소·최대 시간 간격 및 안전율(safety factor)을 COMMON으로 공유한다. 2–3행은 연속된 한 문장이다. 선언과 주석만 있으며 기본값 대입은 없다. 원문: `C-*- mode:fortran; -*-` (1); `      COMMON /VF_ATIMER/ TEND,TNOW,` (2); `     &                   DTNOW,DTCNST,DTINIT,DTMIN,DTMAX,DTSAFE` (3); `CD=== 概要 ===========================================================` (5) (개요); `CDT   VF_ATIMER.h:時間制御関連(解析時刻および時間刻み幅等):実数` (7) (해석 시각·시간 간격 등 시간 제어 관련 실수); `C==== 内容 ===========================================================` (9) (내용); `CD    TEND   : CNS : R*8 : 解析終了時刻` (11) (해석 종료 시각); `CD    TNOW   : TRN : R*8 : 解析時刻` (12) (해석 시각); `CD    DTNOW  : TRN : R*8 : 時間刻み幅` (13) (시간 간격); `CD    DTCNST : CNS : R*8 : 時間刻み幅の一定値` (14) (고정 시간 간격); `CD    DTINIT : CNS : R*8 : 時間刻み幅の初期値` (15) (초기 시간 간격); `CD    DTMIN  : CNS : R*8 : 時間刻み幅の最小値` (16) (최소 시간 간격); `CD    DTMAX  : CNS : R*8 : 時間刻み幅の最大値` (17) (최대 시간 간격); `CD    DTSAFE : CNS : R*8 : 時間刻み幅の安全率` (18) (시간 간격 안전율). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_ATIMER.h
lines: 17
sha256: 241129d9e12b23f2353d1deba53ce2921badc5df8a9f1720c47af206fc18ea2f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ATIMER.h — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | /VF_ATIMER/의 1–2행은 한 COMMON 문장이다. 종료·현재 시각 및 현재/고정/초기/최소/최대 시간 간격(time step)과 안전계수를 공유한다. 변수 설명만 있으며 실제 기본값 대입은 없다. 원문: `      COMMON /VF_ATIMER/ TEND,TNOW,` (1); `     &                   DTNOW,DTCNST,DTINIT,DTMIN,DTMAX,DTSAFE` (2); `CD=== 概要 ===========================================================` (4) (개요); `CDT   VF_ATIMER.h:時間制御関連(解析時刻および時間刻み幅等):実数` (6) (해석 시각과 시간 간격 등 시간 제어 관련 실수); `C==== 内容 ===========================================================` (8) (내용); `CD    TEND   : CNS : R*8 : 解析終了時刻` (10) (해석 종료 시각); `CD    TNOW   : TRN : R*8 : 解析時刻` (11) (해석 시각); `CD    DTNOW  : TRN : R*8 : 時間刻み幅` (12) (시간 간격); `CD    DTCNST : CNS : R*8 : 時間刻み幅の一定値` (13) (고정 시간 간격); `CD    DTINIT : CNS : R*8 : 時間刻み幅の初期値` (14) (시간 간격 초기값); `CD    DTMIN  : CNS : R*8 : 時間刻み幅の最小値` (15) (시간 간격 최솟값); `CD    DTMAX  : CNS : R*8 : 時間刻み幅の最大値` (16) (시간 간격 최댓값); `CD    DTSAFE : CNS : R*8 : 時間刻み幅の安全率` (17) (시간 간격 안전계수) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

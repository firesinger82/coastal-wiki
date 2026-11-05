---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ATIMEI.h
lines: 17
sha256: 21ee8e466ae3e322b56639b84e97931aaf85f90d1025e5e2ae39cdc0c4a11439
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ATIMEI.h — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 종료·현재 스텝(step), 시간 간격 계산 방법, 유속·압력 하위 반복(subloop) 횟수를 COMMON으로 공유한다. IDTTYP=0은 일정 간격, 0 이외는 자동이다. LOOPS=1은 통상 계산, 1 초과는 하위 반복 사용이라는 주석이다. 초기값 대입은 없다. 원문: `C-*- mode:fortran; -*-` (1); `      COMMON /VF_ATIMEI/ NEND,NNOW,IDTTYP,LOOPS` (2); `CD=== 概要 ===========================================================` (4) (개요); `CDT   VF_ATIMEI.h:時間制御関連(解析時刻および時間刻み幅等):整数` (6) (해석 시각·시간 간격 등 시간 제어 관련 정수); `C==== 内容 ===========================================================` (8) (내용); `CD    NEND   : CNS : I*4 : 解析終了ステップ` (10) (해석 종료 스텝); `CD    NNOW   : TRN : I*4 : 解析ステップ` (11) (해석 스텝); `CD    IDTTYP : CNS : I*4 : 時間刻み幅の計算方法` (12) (시간 간격 계산 방법); `CD                         = 0:一定` (13) (일정); `CD                         !=0:自動` (14) (자동); `CD    LOOPS  : CNS : I*4 : 流速・圧力計算のサブループ回数` (15) (유속·압력 계산 하위 반복 횟수); `CD                         =1 :通常計算` (16) (통상 계산); `CD                         >1 :サブループ有り` (17) (하위 반복 있음). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

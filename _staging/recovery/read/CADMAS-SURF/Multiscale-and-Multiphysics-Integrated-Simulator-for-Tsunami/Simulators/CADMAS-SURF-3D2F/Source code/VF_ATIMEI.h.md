---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_ATIMEI.h
lines: 16
sha256: 7584edaecb7fd873d925ab3bab97b5c596982a7f2d65b09ce81e2f6e439d0534
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ATIMEI.h — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | /VF_ATIMEI/는 종료 단계·현재 단계·시간 간격(time step) 계산 방식·유속/압력 하위 반복 횟수를 공유한다. IDTTYP의 0은 일정, 비영은 자동이며 LOOPS의 1은 일반 계산, 1 초과는 하위 반복 사용이라는 주석이다. 값 대입은 없다. 원문: `      COMMON /VF_ATIMEI/ NEND,NNOW,IDTTYP,LOOPS` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_ATIMEI.h:時間制御関連(解析時刻および時間刻み幅等):整数` (5) (해석 시각과 시간 간격 등 시간 제어 관련 정수); `C==== 内容 ===========================================================` (7) (내용); `CD    NEND   : CNS : I*4 : 解析終了ステップ` (9) (해석 종료 단계); `CD    NNOW   : TRN : I*4 : 解析ステップ` (10) (해석 단계); `CD    IDTTYP : CNS : I*4 : 時間刻み幅の計算方法` (11) (시간 간격 계산 방식); `CD                         = 0:一定` (12) (0: 일정); `CD                         !=0:自動` (13) (비영: 자동); `CD    LOOPS  : CNS : I*4 : 流速・圧力計算のサブループ回数` (14) (유속·압력 계산 하위 반복(subloop) 횟수); `CD                         =1 :通常計算` (15) (1: 일반 계산); `CD                         >1 :サブループ有り` (16) (1 초과: 하위 반복 있음) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

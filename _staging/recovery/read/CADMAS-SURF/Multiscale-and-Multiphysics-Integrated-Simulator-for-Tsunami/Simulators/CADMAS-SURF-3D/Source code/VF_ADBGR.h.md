---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ADBGR.h
lines: 14
sha256: 345515a35600c9d161b0aba4eef78c41d8badfb05d07cce2ca77364ba76a12fc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ADBGR.h — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `COMMON /VF_ADBGR/ RDBGF,RDBGTD(3)`(2)을 보존한다. 개요는 디버그(debug) 관련 실수다. 원문: `C-*- mode:fortran; -*-` (1); `      COMMON /VF_ADBGR/ RDBGF,RDBGTD(3)` (2); `CD=== 概要 ===========================================================` (4) (개요); `CDT   VF_ADBGR.h:デバッグ関連:実数` (6) (디버그(debug) 관련 실수); `C==== 内容 ===========================================================` (8) (내용) |
| 10–14 | 직육면체 상자의 지정 F값과 TD용 지정 속도 V값 및 속도 x/y/z 성분을 설명한다. 각 일본어 원문에 한국어 뜻을 붙인다. 원문: `CD    RDBGF     : CNS : I*4 : 矩形ボックスへのF値指定データ(F値)` (10) (직육면체 상자의 지정 F값); `CD    RDBGTD(3) : CNS : I*4 : 矩形ボックスへのTD用速度指定データ(V値)` (11) (직육면체 상자의 TD용 지정 속도 V값); `CD                            (1):x方向速度` (12) (x 방향 속도); `CD                            (2):y方向速度` (13) (y 방향 속도); `CD                            (3):z方向速度` (14) (z 방향 속도) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·10–11: 개요는 실수라고 설명하지만 두 항목의 자료형 표기는 I*4다. 이 파일에는 별도 형식 선언문이 없다.

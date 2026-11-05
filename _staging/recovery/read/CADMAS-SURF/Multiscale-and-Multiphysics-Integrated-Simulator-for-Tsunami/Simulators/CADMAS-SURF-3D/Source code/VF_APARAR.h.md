---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_APARAR.h
lines: 13
sha256: 984ece572956ebb4a5b377edf7cd8ffecbe385de81021ce11fff5d5ef8c8b01b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_APARAR.h — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 병렬 영역의 전역 수평 좌표 최솟값·최댓값을 COMMON으로 공유한다. 선언과 설명만 있고 초기값은 없다. 원문: `C-*- mode:fortran; -*-` (1); `      COMMON /VF_APARAR/ GLXMIN,GLXMAX,GLYMIN,GLYMAX` (2); `CD=== 概要 ===========================================================` (4) (개요); `CDT   VF_APARAR.h:並列化関連:実数` (6) (병렬화 관련 실수); `C==== 内容 ===========================================================` (8) (내용); `CD    GLXMIN           : CNS : R*8 : 全体のx方向格子座標の最小値` (10) (전체 x방향 격자 좌표 최솟값); `CD    GLXMAX           : CNS : R*8 : 全体のx方向格子座標の最大値` (11) (전체 x방향 격자 좌표 최댓값); `CD    GLYMIN           : CNS : R*8 : 全体のy方向格子座標の最小値` (12) (전체 y방향 격자 좌표 최솟값); `CD    GLYMAX           : CNS : R*8 : 全体のy方向格子座標の最大値` (13) (전체 y방향 격자 좌표 최댓값). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

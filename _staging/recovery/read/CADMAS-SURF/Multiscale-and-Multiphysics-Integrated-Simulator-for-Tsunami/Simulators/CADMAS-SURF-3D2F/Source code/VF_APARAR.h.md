---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_APARAR.h
lines: 12
sha256: 365d19dd79a8b434f40cf8180da8b8c4362c52b12212f0f6cdbee1e4248eec47
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_APARAR.h — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | /VF_APARAR/는 전체 격자의 x·y방향 최소·최대 좌표를 공유한다. 개요와 변수 설명만 있으며 계산식과 초기값은 없다. 원문: `      COMMON /VF_APARAR/ GLXMIN,GLXMAX,GLYMIN,GLYMAX` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_APARAR.h:並列化関連:実数` (5) (병렬화 관련 실수); `C==== 内容 ===========================================================` (7) (내용); `CD    GLXMIN           : CNS : R*8 : 全体のx方向格子座標の最小値` (9) (전체 x방향 격자 좌표 최솟값); `CD    GLXMAX           : CNS : R*8 : 全体のx方向格子座標の最大値` (10) (전체 x방향 격자 좌표 최댓값); `CD    GLYMIN           : CNS : R*8 : 全体のy方向格子座標の最小値` (11) (전체 y방향 격자 좌표 최솟값); `CD    GLYMAX           : CNS : R*8 : 全体のy方向格子座標の最大値` (12) (전체 y방향 격자 좌표 최댓값) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

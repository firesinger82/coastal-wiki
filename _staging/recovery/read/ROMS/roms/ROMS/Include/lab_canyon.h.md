---
file: models/ROMS/raw/source_code/roms/ROMS/Include/lab_canyon.h
lines: 32
sha256: e97b69a11c165da3e3ff8651255987cf327619ef991d47d9d0aa634d6ea86b10
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# lab_canyon.h — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·극좌표(polar coordinates) Lab Canyon 설정 주석과 LAB_CANYON·roms_lab_canyon.in을 포함한다(1–13). 빈 줄을 포함한다(14). |
| 15–27 | 시작 시 열린 전처리 조건 없음. 운동량·선형 항력(linear bottom drag)·2차 점성/S면 혼합·DJ_GRADPS·수직 스플라인·추적자 2차 확산/지오포텐셜 면 혼합·SOLVE3D·CURVGRID·AVERAGES를 정의한다(15–27). 원문: `#define UV_COR` (15); `#define UV_ADV` (16); `#define UV_LDRAG` (17); `#define UV_VIS2` (18); `#define MIX_S_UV` (19); `#define DJ_GRADPS` (20); `#define SPLINES_VDIFF` (21); `#define SPLINES_VVISC` (22); `#define TS_DIF2` (23); `#define MIX_GEO_TS` (24); `#define SOLVE3D` (25); `#define CURVGRID` (26); `#define AVERAGES` (27). |
| 28–32 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·표면 운동량/추적자 플럭스·바닥 추적자 플럭스 옵션을 정의한다(28–32). 원문: `#define ANA_GRID` (28); `#define ANA_INITIAL` (29); `#define ANA_SMFLUX` (30); `#define ANA_STFLUX` (31); `#define ANA_BTFLUX` (32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

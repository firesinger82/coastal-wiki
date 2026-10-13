---
file: models/ROMS/raw/source_code/roms/ROMS/Include/overflow.h
lines: 31
sha256: 5b8c6e30cdce531a18cf1ea9346390436de8acfacfe35877e25119aecd87dc52
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# overflow.h — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·중력 월류(gravitational overflow) 시험 주석과 OVERFLOW·roms_overflow.in을 포함한다(1–13). 빈 줄을 포함한다(14). |
| 15–26 | 시작 시 열린 전처리 조건 없음. 운동량·이차 항력·2차 점성/S면 혼합·DJ_GRADPS·수직 스플라인·추적자 2차 확산/등밀도 면 혼합·SOLVE3D·AVERAGES를 정의한다(15–26). 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#define UV_VIS2` (18); `#define MIX_S_UV` (19); `#define DJ_GRADPS` (20); `#define SPLINES_VDIFF` (21); `#define SPLINES_VVISC` (22); `#define TS_DIF2` (23); `#define MIX_ISO_TS` (24); `#define SOLVE3D` (25); `#define AVERAGES` (26). |
| 27–31 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·표면 운동량/추적자 플럭스·바닥 추적자 플럭스 옵션을 정의한다(27–31). 원문: `#define ANA_GRID` (27); `#define ANA_INITIAL` (28); `#define ANA_SMFLUX` (29); `#define ANA_STFLUX` (30); `#define ANA_BTFLUX` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

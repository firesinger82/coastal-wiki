---
file: models/ROMS/raw/source_code/roms/ROMS/Include/grav_adj.h
lines: 33
sha256: 736044b053bedaacea270a3c5ea571f2514f71339a1506e100e5ec2f69c72c69
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# grav_adj.h — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·중력 조정(gravitational adjustment) 시험 주석과 GRAV_ADJ·roms_grav_adj.in을 포함한다(1–13). 빈 줄을 포함한다(14). |
| 15–25 | 시작 시 열린 전처리 조건 없음. UV_ADV/UV_VIS2/UV_LDRAG·MIX_S_UV·DJ_GRADPS·수직 스플라인·TS_DIF2/MIX_S_TS·SOLVE3D·AVERAGES를 정의한다(15–25). 원문: `#define UV_ADV` (15); `#define UV_VIS2` (16); `#define UV_LDRAG` (17); `#define MIX_S_UV` (18); `#define DJ_GRADPS` (19); `#define SPLINES_VDIFF` (20); `#define SPLINES_VVISC` (21); `#define TS_DIF2` (22); `#define MIX_S_TS` (23); `#define SOLVE3D` (24); `#define AVERAGES` (25). |
| 26–33 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·표면 운동량 및 추적자 플럭스·바닥 추적자 플럭스·OUT_DOUBLE·추적자/운동량 진단 출력을 정의한다(26–33). 원문: `#define ANA_GRID` (26); `#define ANA_INITIAL` (27); `#define ANA_SMFLUX` (28); `#define ANA_STFLUX` (29); `#define ANA_BTFLUX` (30); `#define OUT_DOUBLE` (31); `#define DIAGNOSTICS_TS` (32); `#define DIAGNOSTICS_UV` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

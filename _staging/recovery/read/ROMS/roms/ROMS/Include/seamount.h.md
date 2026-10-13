---
file: models/ROMS/raw/source_code/roms/ROMS/Include/seamount.h
lines: 31
sha256: 592c908dadb61577c380ccd8f0ddffb9a27183ff2501ebdbe6c35272f576a854
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# seamount.h — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·해산(seamount) 시험 주석과 SEAMOUNT·roms_seamount.in을 포함한다(1–13). 빈 줄을 포함한다(14). |
| 15–25 | 시작 시 열린 전처리 조건 없음. 운동량·이차 항력·2차 점성/S면 혼합·DJ_GRADPS·수직 스플라인·TS_DIF2/MIX_GEO_TS·SOLVE3D를 정의한다(15–25). 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#define UV_VIS2` (18); `#define MIX_S_UV` (19); `#define DJ_GRADPS` (20); `#define SPLINES_VDIFF` (21); `#define SPLINES_VVISC` (22); `#define TS_DIF2` (23); `#define MIX_GEO_TS` (24); `#define SOLVE3D` (25). |
| 26–31 | 시작 시 열린 전처리 조건 없음. 해석 진단·격자·초기 조건·표면 운동량/추적자 플럭스·바닥 추적자 플럭스 옵션을 정의한다(26–31). 원문: `#define ANA_DIAG` (26); `#define ANA_GRID` (27); `#define ANA_INITIAL` (28); `#define ANA_SMFLUX` (29); `#define ANA_STFLUX` (30); `#define ANA_BTFLUX` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

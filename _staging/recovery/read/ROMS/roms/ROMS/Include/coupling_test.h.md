---
file: models/ROMS/raw/source_code/roms/ROMS/Include/coupling_test.h
lines: 33
sha256: e32f895139047f4c70dae57dcad209bf4ae984d5e80ca58605ab53d8ded5da62
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# coupling_test.h — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·대기와 해양 양방향 결합(atmosphere-ocean two-way coupling) WRF/ROMS 시험 주석을 포함한다(1–10). COUPLING_TEST와 roms_coupling_test.in을 적는다(11–12). 주석 종료·빈 줄을 포함한다(13–14). |
| 15–26 | 시작 시 열린 전처리 조건 없음. UV_ADV/UV_COR/UV_QDRAG·SPLINES_VDIFF/SPLINES_VVISC·DJ_GRADPS·SALINITY·SOLVE3D·AVERAGES를 정의한다(15–26). UV_VIS2/TS_DIF2/MIX_GEO_TS를 해제한다(18·22–23). 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#undef  UV_VIS2` (18); `#define SPLINES_VDIFF` (19); `#define SPLINES_VVISC` (20); `#define DJ_GRADPS` (21); `#undef  TS_DIF2` (22); `#undef  MIX_GEO_TS` (23); `#define SALINITY` (24); `#define SOLVE3D` (25); `#define AVERAGES` (26). |
| 27–33 | 시작 시 열린 전처리 조건 없음. ANA_GRID/ANA_INITIAL·해석 표면 온도/염분 및 바닥 온도/염분 플럭스·ANA_VMIX를 정의한다(27–33). 원문: `#define ANA_GRID` (27); `#define ANA_INITIAL` (28); `#define ANA_STFLUX` (29); `#define ANA_SSFLUX` (30); `#define ANA_BTFLUX` (31); `#define ANA_BSFLUX` (32); `#define ANA_VMIX` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

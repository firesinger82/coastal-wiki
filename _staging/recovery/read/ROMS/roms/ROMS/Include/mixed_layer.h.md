---
file: models/ROMS/raw/source_code/roms/ROMS/Include/mixed_layer.h
lines: 43
sha256: a6cb13f6528d6ddfd65bc3a20dd1f09e5dde3d8e58f788780193697665bba7f8
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mixed_layer.h — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스와 열 성층(thermal stratification)·바람 응력에 의한 직사각 주기 격자의 혼합층 심화(mixed layer deepening) 주석을 포함한다(1–11). MIXED_LAYER·roms_mixed_layer.in·주석 종료·빈 줄을 포함한다(12–15). |
| 16–29 | 시작 시 열린 전처리 조건 없음. WRITE_GRID·OUT_DOUBLE·ANA_GRID·SALINITY·SOLVE3D·수직 스플라인·해석 초기 조건·표면 운동량/추적자/염분 및 바닥 추적자/염분 플럭스를 정의한다(16–28). 빈 줄을 포함한다(29). 원문: `#define WRITE_GRID` (16); `#define OUT_DOUBLE` (17); `#define ANA_GRID` (18); `#define SALINITY` (19); `#define SOLVE3D` (20); `#define SPLINES_VDIFF` (21); `#define SPLINES_VVISC` (22); `#define ANA_INITIAL` (23); `#define ANA_SMFLUX` (24); `#define ANA_STFLUX` (25); `#define ANA_BTFLUX` (26); `#define ANA_SSFLUX` (27); `#define ANA_BSFLUX` (28). |
| 30–43 | 시작 시 열린 전처리 조건 없음. MY25_MIXING을 해제하고 GLS_MIXING을 정의한다(30–31). GLS_MIXING이면 KANTHA_CLAYSON/N2S2_HORAVG/RI_SPLINES/CRAIG_BANNER/CHARNOK를 정의하고 ZOS_HSIG/TKE_WAVEDISS를 해제한다(33–41). 빈 줄 뒤 UV_LOGDRAG를 정의한다(42–43). 원문: `#undef  MY25_MIXING` (30); `#define GLS_MIXING` (31); `#if defined GLS_MIXING` (33); `# define KANTHA_CLAYSON` (34); `# define N2S2_HORAVG` (35); `# define RI_SPLINES` (36); `# define CRAIG_BANNER` (37); `# define CHARNOK` (38); `# undef  ZOS_HSIG` (39); `# undef  TKE_WAVEDISS` (40); `#endif` (41); `#define UV_LOGDRAG` (43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

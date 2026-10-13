---
file: models/ROMS/raw/source_code/roms/ROMS/Include/dogbone.h
lines: 42
sha256: e0a4886ed6200100ac019ec327fd418a37dcd98d7636280b6525f0bb121421c2
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# dogbone.h — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·DOGBONE 응용 설명을 포함한다(1–10). 주석은 composite grid 시험이며 makefile의 Ngrids만 변경하고 이 헤더는 변경하지 않도록 적는다(11–12). 주석 종료·빈 줄을 포함한다(13–14). |
| 15–23 | 시작 시 열린 전처리 조건 없음. NESTING·SOLVE3D·UV_ADV·UV_QDRAG·ANA_SMFLUX·MASKING을 정의한다(15–22). 빈 줄을 포함한다(23). 원문: `#define NESTING` (15); `#define SOLVE3D` (16); `#define UV_ADV` (18); `#define UV_QDRAG` (19); `#define ANA_SMFLUX` (21); `#define MASKING` (22). |
| 24–42 | 시작 시 열린 전처리 조건 없음. SOLVE3D 조건에서 DJ_GRADPS·SALINITY·수직 스플라인·해석 표면/바닥 추적자 및 염분 플럭스·GLS_MIXING을 정의한다(24–33). 중첩 GLS_MIXING 조건은 KANTHA_CLAYSON/N2S2_HORAVG/RI_SPLINES를 정의한다(34–38). 두 조건 종료·OUT_DOUBLE 정의·빈 줄을 포함한다(39–42). 원문: `#ifdef SOLVE3D` (24); `# define DJ_GRADPS` (25); `# define SALINITY` (26); `# define SPLINES_VDIFF` (27); `# define SPLINES_VVISC` (28); `# define ANA_STFLUX` (29); `# define ANA_SSFLUX` (30); `# define ANA_BTFLUX` (31); `# define ANA_BSFLUX` (32); `# define GLS_MIXING` (33); `# if defined GLS_MIXING` (34); `#  define KANTHA_CLAYSON` (35); `#  define N2S2_HORAVG` (36); `#  define RI_SPLINES` (37); `# endif` (38); `#endif` (39); `#define OUT_DOUBLE` (41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

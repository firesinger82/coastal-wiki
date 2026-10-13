---
file: models/ROMS/raw/source_code/roms/ROMS/Include/riverplume1.h
lines: 47
sha256: b8d761a2fb9861f2fa06c8a79d24a324972c0ed89bc608f256659465065c14de
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# riverplume1.h — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·원본 버전 하천 플룸(river plume) 시험 주석과 RIVERPLUME1·roms_riverplume1.in을 포함한다(1–13). 빈 줄을 포함한다(14). |
| 15–28 | 시작 시 열린 전처리 조건 없음. 운동량·DJ_GRADPS·수직 스플라인·TS_DIF2/MIX_GEO_TS·NONLIN_EOS·SALINITY·MASKING·SOLVE3D·AVERAGES를 정의한다(15–27). 빈 줄을 포함한다(28). 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#define DJ_GRADPS` (18); `#define SPLINES_VDIFF` (19); `#define SPLINES_VVISC` (20); `#define TS_DIF2` (21); `#define MIX_GEO_TS` (22); `#define NONLIN_EOS` (23); `#define SALINITY` (24); `#define MASKING` (25); `#define SOLVE3D` (26); `#define AVERAGES` (27). |
| 29–38 | 시작 시 열린 전처리 조건 없음. LMD_MIXING을 정의한다(29). 해당 조건에서 LMD_RIMIX/LMD_CONVEC/LMD_SKPP/LMD_BKPP/LMD_NONLOCAL/RI_SPLINES를 정의한다(30–37). 빈 줄을 포함한다(38). 원문: `#define LMD_MIXING` (29); `#ifdef LMD_MIXING` (30); `# define LMD_RIMIX` (31); `# define LMD_CONVEC` (32); `# define LMD_SKPP` (33); `# define LMD_BKPP` (34); `# define LMD_NONLOCAL` (35); `# define RI_SPLINES` (36); `#endif` (37). |
| 39–47 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·점원·표면 운동량/복사/염분/추적자 플럭스·바닥 염분/추적자 플럭스 옵션을 정의한다(39–47). 원문: `#define ANA_GRID` (39); `#define ANA_INITIAL` (40); `#define ANA_PSOURCE` (41); `#define ANA_SMFLUX` (42); `#define ANA_SRFLUX` (43); `#define ANA_SSFLUX` (44); `#define ANA_STFLUX` (45); `#define ANA_BSFLUX` (46); `#define ANA_BTFLUX` (47). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

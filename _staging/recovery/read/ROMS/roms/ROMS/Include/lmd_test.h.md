---
file: models/ROMS/raw/source_code/roms/ROMS/Include/lmd_test.h
lines: 45
sha256: d30d39a24784ea761de115d18bb5daf03a133673761ded246bdb13cdd12907a8
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# lmd_test.h — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·K-profile parameterization 시험 주석과 LMD_TEST·roms_lmd_test.in을 포함한다(1–13). 빈 줄을 포함한다(14). |
| 15–27 | 시작 시 열린 전처리 조건 없음. 운동량·DJ_GRADPS·수직 스플라인·NONLIN_EOS·SALINITY·AVERAGES·STATIONS·SOLVE3D를 정의한다(15–27). 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#define UV_VIS2` (18); `#define MIX_S_UV` (19); `#define DJ_GRADPS` (20); `#define SPLINES_VDIFF` (21); `#define SPLINES_VVISC` (22); `#define NONLIN_EOS` (23); `#define SALINITY` (24); `#define AVERAGES` (25); `#define STATIONS` (26); `#define SOLVE3D` (27). |
| 28–37 | 시작 시 열린 전처리 조건 없음. LMD_MIXING을 정의한다(28). 해당 조건에서 LMD_RIMIX/LMD_CONVEC/LMD_DDMIX/LMD_SKPP/LMD_BKPP/LMD_NONLOCAL/RI_SPLINES를 정의한다(29–37). 원문: `#define LMD_MIXING` (28); `#ifdef LMD_MIXING` (29); `# define LMD_RIMIX` (30); `# define LMD_CONVEC` (31); `# define LMD_DDMIX` (32); `# define LMD_SKPP` (33); `# define LMD_BKPP` (34); `# define LMD_NONLOCAL` (35); `# define RI_SPLINES` (36); `#endif` (37). |
| 38–45 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·표면 운동량/복사/염분/추적자 플럭스·바닥 염분/추적자 플럭스 옵션을 정의한다(38–45). 원문: `#define ANA_GRID` (38); `#define ANA_INITIAL` (39); `#define ANA_SMFLUX` (40); `#define ANA_SRFLUX` (41); `#define ANA_SSFLUX` (42); `#define ANA_STFLUX` (43); `#define ANA_BSFLUX` (44); `#define ANA_BTFLUX` (45). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

---
file: models/ROMS/raw/source_code/roms/ROMS/Include/benchmark.h
lines: 57
sha256: 9e623be2f598ee6e30f75d325d767cb6ccb5c280296485ae772422b6b5dfa4c5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# benchmark.h — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·Benchmark 설정 설명을 포함한다(1–9). 주석은 small/medium/large별 입력 파일을 적고 BENCHMARK 적용 매크로와 입력 목록을 적는다(10–14). 주석 종료·빈 줄을 포함한다(15–16). |
| 17–31 | 시작 시 열린 전처리 조건 없음. 운동량·압력 경도(pressure gradient)·수직 스플라인·추적자 확산(tracer diffusion)·단파복사·비선형 상태방정식(nonlinear equation of state)·염분·곡선 격자(curvilinear grid)·3차원 옵션을 정의한다(17–31). 원문: `#define UV_ADV` (17); `#define UV_COR` (18); `#define UV_QDRAG` (19); `#define UV_VIS2` (20); `#define MIX_S_UV` (21); `#define DJ_GRADPS` (22); `#define SPLINES_VDIFF` (23); `#define SPLINES_VVISC` (24); `#define TS_DIF2` (25); `#define MIX_GEO_TS` (26); `#define SOLAR_SOURCE` (27); `#define NONLIN_EOS` (28); `#define SALINITY` (29); `#define CURVGRID` (30); `#define SOLVE3D` (31). |
| 32–39 | 시작 시 열린 전처리 조건 없음. LMD_MIXING을 정의한 뒤 그 조건 안에서 LMD_RIMIX/LMD_CONVEC/LMD_SKPP/LMD_NONLOCAL/RI_SPLINES를 정의한다(32–39). 원문: `#define LMD_MIXING` (32); `#ifdef LMD_MIXING` (33); `# define LMD_RIMIX` (34); `# define LMD_CONVEC` (35); `# define LMD_SKPP` (36); `# define LMD_NONLOCAL` (37); `# define RI_SPLINES` (38); `#endif` (39). |
| 40–49 | 시작 시 열린 전처리 조건 없음. BULK_FLUXES를 정의한다(40). 그 조건 안에서 해석 바람·기온·대기압·습도·강우·운량과 LONGWAVE를 정의한다(41–49). 원문: `#define BULK_FLUXES` (40); `#ifdef BULK_FLUXES` (41); `# define ANA_WINDS` (42); `# define ANA_TAIR` (43); `# define ANA_PAIR` (44); `# define ANA_HUMIDITY` (45); `# define ANA_RAIN` (46); `# define LONGWAVE` (47); `# define ANA_CLOUD` (48); `#endif` (49). |
| 50–57 | 시작 시 열린 전처리 조건 없음. SPHERICAL·해석 격자·해석 초기 조건·ALBEDO와 해석 복사/표면 염분/바닥 염분/바닥 추적자 플럭스 옵션을 정의한다(50–57). 원문: `#define SPHERICAL` (50); `#define ANA_GRID` (51); `#define ANA_INITIAL` (52); `#define ALBEDO` (53); `#define ANA_SRFLUX` (54); `#define ANA_SSFLUX` (55); `#define ANA_BSFLUX` (56); `#define ANA_BTFLUX` (57). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–14: 크기별 설명의 입력 이름은 roms_benchmark1.in·roms_benchmark2.in·roms_benchmark3.in이다. Input script 목록의 이름은 benchmark1.in·benchmark2.in·benchmark3.in이다.

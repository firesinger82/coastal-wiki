---
file: models/ROMS/raw/source_code/roms/ROMS/Include/bl_test.h
lines: 81
sha256: 9de428b68160c1f22ca900917cbd3d5ef48676fb592a544dd47cf88e5825097d
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# bl_test.h — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·Boundary Layers Test 주석과 BL_TEST·roms_bl_test.in·stations_bl_test.in을 포함한다(1–14). 빈 줄을 포함한다(15). |
| 16–32 | 시작 시 열린 전처리 조건 없음. 운동량·수직 스플라인·복사·비선형 상태방정식·염분·평균/관측점(stations) 출력·SOLVE3D·RADIATION_2D를 정의한다(16–31). 빈 줄을 포함한다(32). 원문: `#define UV_ADV` (16); `#define UV_SADVECTION` (17); `#define UV_COR` (18); `#define UV_VIS2` (19); `#define MIX_S_UV` (20); `#define DJ_GRADPS` (21); `#define SPLINES_VDIFF` (22); `#define SPLINES_VVISC` (23); `#define SOLAR_SOURCE` (24); `#define NONLIN_EOS` (25); `#define SALINITY` (26); `#define AVERAGES` (27); `#define STATIONS` (28); `#define SOLVE3D` (29); `#define RADIATION_2D` (31). |
| 33–50 | 시작 시 열린 전처리 조건 없음. MY25_MIXING을 해제하고 해당 조건 안에 N2S2_HORAVG/KANTHA_CLAYSON/RI_SPLINES 정의를 둔다(33–38). LMD_MIXING을 정의하고 해당 조건에서 RIMIX/CONVEC/SKPP/BKPP/NONLOCAL/DDMIX/RI_SPLINES를 정의한다(40–49). 빈 줄을 포함한다(50). 원문: `#undef  MY25_MIXING` (33); `#ifdef MY25_MIXING` (34); `# define N2S2_HORAVG` (35); `# define KANTHA_CLAYSON` (36); `# define RI_SPLINES` (37); `#endif` (38); `#define LMD_MIXING` (40); `#ifdef LMD_MIXING` (41); `# define LMD_RIMIX` (42); `# define LMD_CONVEC` (43); `# define LMD_SKPP` (44); `# define LMD_BKPP` (45); `# define LMD_NONLOCAL` (46); `# define LMD_DDMIX` (47); `# define RI_SPLINES` (48); `#endif` (49). |
| 51–64 | 시작 시 열린 전처리 조건 없음. BULK_FLUXES를 정의한다(51). 그 조건 안에 LONGWAVE와 해석 운량·습도·대기압·기온·강우·바람을 정의한다(52–59). ELSE는 ANA_SMFLUX·ANA_STFLUX를 정의한다(60–63). 빈 줄을 포함한다(64). 원문: `#define BULK_FLUXES` (51); `#ifdef BULK_FLUXES` (52); `# define LONGWAVE` (53); `# define ANA_CLOUD` (54); `# define ANA_HUMIDITY` (55); `# define ANA_PAIR` (56); `# define ANA_TAIR` (57); `# define ANA_RAIN` (58); `# define ANA_WINDS` (59); `#else` (60); `# define ANA_SMFLUX` (61); `# define ANA_STFLUX` (62); `#endif` (63). |
| 65–81 | 시작 시 열린 전처리 조건 없음. SG_BBL을 해제한다(65). SG_BBL 조건은 SG_CALC_UB/SG_CALC_ZNOT/ANA_SEDIMENT/ANA_WWAVE, ELSE는 UV_QDRAG를 정의한다(66–73). 공통 해석 격자·초기 조건·ALBEDO·복사/염분/바닥 추적자 플럭스 옵션을 정의한다(75–81). 원문: `#undef SG_BBL` (65); `#ifdef SG_BBL` (66); `# define SG_CALC_UB` (67); `# define SG_CALC_ZNOT` (68); `# define ANA_SEDIMENT` (69); `# define ANA_WWAVE` (70); `#else` (71); `# define UV_QDRAG` (72); `#endif` (73); `#define ANA_GRID` (75); `#define ANA_INITIAL` (76); `#define ALBEDO` (77); `#define ANA_SRFLUX` (78); `#define ANA_SSFLUX` (79); `#define ANA_BSFLUX` (80); `#define ANA_BTFLUX` (81). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–38·65–73: MY25_MIXING과 SG_BBL은 각각 조건 검사 앞에서 해제한다. 해당 참 분기들의 옵션 정의는 소스에 남아 있다.

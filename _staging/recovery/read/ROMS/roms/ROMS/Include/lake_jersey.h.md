---
file: models/ROMS/raw/source_code/roms/ROMS/Include/lake_jersey.h
lines: 66
sha256: f78847613cca3e9ea9c0f5190e3fd6ce33cbad8ecc308b552b37d439461b1c8b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# lake_jersey.h — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스와 바람으로 강제하는 Lake Jersey 주석을 포함한다(1–10). LAKE_JERSEY·roms_lake_jersey.in·sediment_lake_jersey.in을 적는다(11–15). 빈 줄을 포함한다(16). |
| 17–33 | 시작 시 열린 전처리 조건 없음. 운동량·DJ_GRADPS·NONLIN_EOS·SALINITY·SOLVE3D·MASKING을 정의한다(17–23). 해석 표면 운동량/추적자/염분/수동 추적자/복사·바닥 추적자/염분/수동 추적자 플럭스를 정의한다(25–32). 빈 줄을 포함한다(33). 원문: `#define UV_ADV` (17); `#define UV_COR` (18); `#define DJ_GRADPS` (19); `#define NONLIN_EOS` (20); `#define SALINITY` (21); `#define SOLVE3D` (22); `#define MASKING` (23); `#define ANA_SMFLUX` (25); `#define ANA_STFLUX` (26); `#define ANA_SSFLUX` (27); `#define ANA_BPFLUX` (28); `#define ANA_BTFLUX` (29); `#define ANA_BSFLUX` (30); `#define ANA_SPFLUX` (31); `#define ANA_SRFLUX` (32). |
| 34–56 | 시작 시 열린 전처리 조건 없음. 바닥 경계층 구분 주석과 SSW_BBL 정의를 포함한다(34–36). SG_BBL이면 SG_CALC_ZNOT을 정의하고 SG_LOGINT를 해제한다(37–40). MB_BBL이면 MB_CALC_ZNOT을 정의하고 세 MB 거칠기 옵션을 해제한다(41–46). SSW_BBL이면 SSW_CALC_UB/SSW_CALC_ZNOT을 정의하고 SSW_LOGINT를 해제한다(47–51). 셋 중 하나면 ANA_WWAVE를 정의한다(53–55). 빈 줄을 포함한다(56). 원문: `#define SSW_BBL` (36); `#ifdef SG_BBL` (37); `# define SG_CALC_ZNOT` (38); `# undef  SG_LOGINT` (39); `#endif` (40); `#ifdef MB_BBL` (41); `# define MB_CALC_ZNOT` (42); `# undef  MB_Z0BIO` (43); `# undef  MB_Z0BL` (44); `# undef  MB_Z0RIP` (45); `#endif` (46); `#ifdef SSW_BBL` (47); `# define SSW_CALC_UB` (48); `# define SSW_CALC_ZNOT` (49); `# undef  SSW_LOGINT` (50); `#endif` (51); `#if defined MB_BBL \|\| defined SG_BBL \|\| defined SSW_BBL` (53); `# define ANA_WWAVE` (54); `#endif` (55). |
| 57–66 | 시작 시 열린 전처리 조건 없음. SEDIMENT를 정의한다(57). SEDIMENT 조건은 SUSPLOAD/BEDLOAD_SOULSBY를 정의하고 SED_MORPH를 해제한다(58–62). SEDIMENT 또는 세 BBL 중 하나면 ANA_SEDIMENT를 정의한다(63–65). 마지막 빈 줄을 포함한다(66). 원문: `#define SEDIMENT` (57); `#ifdef SEDIMENT` (58); `# define SUSPLOAD` (59); `# define BEDLOAD_SOULSBY` (60); `# undef  SED_MORPH` (61); `#endif` (62); `#if defined SEDIMENT \|\| defined SG_BBL \|\| defined MB_BBL \|\| defined SSW_BBL` (63); `# define ANA_SEDIMENT` (64); `#endif` (65). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–51: SSW_BBL은 이 파일에서 정의한다. SG_BBL·MB_BBL 조건도 있지만 이 파일에는 두 매크로의 정의나 해제가 없다.

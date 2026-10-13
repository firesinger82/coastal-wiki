---
file: models/ROMS/raw/source_code/roms/ROMS/Include/inlet_test.h
lines: 74
sha256: ea79ceac90cabc2382312be2deaef43386e6ef050fbf1f0c1cdb1c824a305335
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# inlet_test.h — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스와 SWAN/ROMS 파랑-해양 양방향 결합 시험 주석을 포함한다(1–10). INLET_TEST와 ROMS·결합·퇴적물 입력 파일을 적는다(11–15). 빈 줄을 포함한다(16). |
| 17–38 | 시작 시 열린 전처리 조건 없음. UV_VIS2/MIX_S_UV·MASKING·UV_ADV·수직 스플라인·DJ_GRADPS·FSOBC_REDUCED·SOLVE3D·SWAN_COUPLING·WEC_VF·해석 초기장/표면 운동량 플럭스/자유수면 및 2차원 운동량 경계를 정의한다(17–33). ANA_GRID·UV_COR를 해제한다(19·22). SWAN_COUPLING이면 MCT_LIB를 정의한다(35–37). 빈 줄을 포함한다(38). 원문: `#define UV_VIS2` (17); `#define MIX_S_UV` (18); `#undef  ANA_GRID` (19); `#define MASKING` (20); `#define UV_ADV` (21); `#undef  UV_COR` (22); `#define SPLINES_VDIFF` (23); `#define SPLINES_VVISC` (24); `#define DJ_GRADPS` (25); `#define FSOBC_REDUCED` (26); `#define SOLVE3D` (27); `#define SWAN_COUPLING` (28); `#define WEC_VF` (29); `#define ANA_INITIAL` (30); `#define ANA_SMFLUX` (31); `#define ANA_FSOBC` (32); `#define ANA_M2OBC` (33); `#ifdef SWAN_COUPLING` (35); `# define MCT_LIB` (36); `#endif` (37). |
| 39–48 | 시작 시 열린 전처리 조건 없음. 주석은 다음 다섯 옵션 중 하나만 정의하도록 적는다(39). UV_LOGDRAG/UV_QDRAG/MB_BBL/SG_BBL을 해제하고 SSW_BBL을 정의한다(40–44). SSW_BBL이면 SSW_CALC_ZNOT을 정의한다(45–47). 빈 줄을 포함한다(48). 원문: `#undef  UV_LOGDRAG` (40); `#undef  UV_QDRAG` (41); `#undef  MB_BBL` (42); `#undef  SG_BBL` (43); `#define SSW_BBL` (44); `#ifdef SSW_BBL` (45); `# define SSW_CALC_ZNOT` (46); `#endif` (47). |
| 49–65 | 시작 시 열린 전처리 조건 없음. SOLVE3D 조건에서 GLS_MIXING을 정의하고 그 중첩 조건에 KANTHA_CLAYSON/N2S2_HORAVG/RI_SPLINES를 정의한다(49–55). SEDIMENT를 정의하고 중첩 조건에서 SUSPLOAD/SED_MORPH를 정의하며 BEDLOAD_SOULSBY/BEDLOAD_MPM을 해제한다(56–62). SEDIMENT 또는 세 BBL 중 하나면 ANA_SEDIMENT를 정의한다(63–65). 원문: `#ifdef SOLVE3D` (49); `# define GLS_MIXING` (50); `# ifdef GLS_MIXING` (51); `#  define KANTHA_CLAYSON` (52); `#  define N2S2_HORAVG` (53); `#  define RI_SPLINES` (54); `# endif` (55); `# define SEDIMENT` (56); `# ifdef SEDIMENT` (57); `#  define SUSPLOAD` (58); `#  undef  BEDLOAD_SOULSBY` (59); `#  undef  BEDLOAD_MPM` (60); `#  define SED_MORPH` (61); `# endif` (62); `# if defined SEDIMENT \|\| defined SG_BBL \|\| defined MB_BBL \|\| defined SSW_BBL` (63); `#  define ANA_SEDIMENT` (64); `# endif` (65). |
| 66–74 | 시작 시 `#ifdef SOLVE3D` (49) 안. 시작 시 49행 SOLVE3D 블록 안. ANA_STFLUX/ANA_SSFLUX/ANA_BPFLUX/ANA_BTFLUX/ANA_BSFLUX/ANA_SPFLUX/ANA_SRFLUX를 정의한다(66–72). 외부 조건 종료·빈 줄을 포함한다(73–74). 원문: `# define ANA_STFLUX` (66); `# define ANA_SSFLUX` (67); `# define ANA_BPFLUX` (68); `# define ANA_BTFLUX` (69); `# define ANA_BSFLUX` (70); `# define ANA_SPFLUX` (71); `# define ANA_SRFLUX` (72); `#endif` (73). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

---
file: models/ROMS/raw/source_code/roms/ROMS/Include/shoreface.h
lines: 83
sha256: ae7314edf2e93c2d2841e40cdd4d3a3aeaac286f66a9cea30d7231915e28ae1f
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# shoreface.h — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·평면 해빈(planar beach)의 shoreface 시험 주석과 SHOREFACE를 포함한다(1–11). Input scripts 주석은 roms_shoreface.h와 sediment_shoreface.h를 적는다(12–13). 주석 종료·빈 줄을 포함한다(14–15). |
| 16–33 | 시작 시 열린 전처리 조건 없음. 2차 점성/S면 혼합·운동량/추적자 진단·AVERAGES·WET_DRY·WEC_VF·WDISS_CHURTHOR·BOTTOM_STREAMING/SURFACE_STREAMING·OUT_DOUBLE·운동량 이류·DJ_GRADPS·SALINITY·수직 스플라인·SOLVE3D를 정의한다(16–32). 빈 줄을 포함한다(33). 원문: `#define UV_VIS2` (16); `#define MIX_S_UV` (17); `#define DIAGNOSTICS_UV` (18); `#define DIAGNOSTICS_TS` (19); `#define AVERAGES` (20); `#define WET_DRY` (21); `#define WEC_VF` (22); `#define WDISS_CHURTHOR` (23); `#define BOTTOM_STREAMING` (24); `#define SURFACE_STREAMING` (25); `#define OUT_DOUBLE` (26); `#define UV_ADV` (27); `#define DJ_GRADPS` (28); `#define SALINITY` (29); `#define SPLINES_VDIFF` (30); `#define SPLINES_VVISC` (31); `#define SOLVE3D` (32). |
| 34–44 | 시작 시 열린 전처리 조건 없음. MASKING을 정의하고 해당 조건에서 ANA_MASK를 정의한다(34–37). 해석 격자·초기 조건·자유수면/2차원 운동량 경계·표면 운동량 플럭스와 UV_QDRAG를 정의한다(38–43). 빈 줄을 포함한다(44). 원문: `#define MASKING` (34); `#ifdef MASKING` (35); `# define ANA_MASK` (36); `#endif` (37); `#define ANA_GRID` (38); `#define ANA_INITIAL` (39); `#define ANA_FSOBC` (40); `#define ANA_M2OBC` (41); `#define ANA_SMFLUX` (42); `#define UV_QDRAG` (43). |
| 45–62 | 시작 시 열린 전처리 조건 없음. SOLVE3D 조건에서 SSW_BBL을 해제하고 그 중첩 조건에 SSW_CALC_ZNOT 정의·SSW_LOGINT 해제를 남긴다(45–50). SEDIMENT를 정의하고 그 조건에서 SED_MORPH를 해제하며 SUSPLOAD/BEDLOAD_MPM을 정의하고 BEDLOAD_SOULSBY를 해제한다(52–58). SEDIMENT 또는 세 BBL 중 하나면 ANA_SEDIMENT를 정의한다(59–61). 빈 줄을 포함한다(62). 원문: `#ifdef SOLVE3D` (45); `# undef  SSW_BBL` (46); `# ifdef SSW_BBL` (47); `#  define SSW_CALC_ZNOT` (48); `#  undef  SSW_LOGINT` (49); `# endif` (50); `# define SEDIMENT` (52); `# ifdef SEDIMENT` (53); `#  undef  SED_MORPH` (54); `#  define SUSPLOAD` (55); `#  define BEDLOAD_MPM` (56); `#  undef  BEDLOAD_SOULSBY` (57); `# endif` (58); `# if defined SEDIMENT \|\| defined SG_BBL \|\| defined MB_BBL \|\| defined SSW_BBL` (59); `#  define ANA_SEDIMENT` (60); `# endif` (61). |
| 63–83 | 시작 시 `#ifdef SOLVE3D` (45) 안. 시작 시 45행 SOLVE3D 블록 안. 해석 표면/바닥 추적자·염분·수동 추적자 및 복사 플럭스를 정의하고 ANA_VMIX를 해제한다(63–70). GLS_MIXING을 정의하고 내부 조건에서 KANTHA_CLAYSON/N2S2_HORAVG/RI_SPLINES를 정의하며 CRAIG_BANNER/CHARNOK/ZOS_HSIG/TKE_WAVEDISS를 해제한다(72–81). 빈 줄·외부 조건 종료를 포함한다(82–83). 원문: `# define ANA_STFLUX` (63); `# define ANA_SSFLUX` (64); `# define ANA_BPFLUX` (65); `# define ANA_BTFLUX` (66); `# define ANA_BSFLUX` (67); `# define ANA_SPFLUX` (68); `# define ANA_SRFLUX` (69); `# undef  ANA_VMIX` (70); `# define GLS_MIXING` (72); `# if defined GLS_MIXING` (73); `#  define KANTHA_CLAYSON` (74); `#  define N2S2_HORAVG` (75); `#  define RI_SPLINES` (76); `#  undef CRAIG_BANNER` (77); `#  undef CHARNOK` (78); `#  undef ZOS_HSIG` (79); `#  undef TKE_WAVEDISS` (80); `# endif` (81); `#endif` (83). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–13: Input scripts 주석에 적은 두 파일의 확장자는 `.h`이다.
- 46–50: SSW_BBL은 중첩 조건 검사 바로 앞에서 해제한다. 그 뒤 SSW_BBL 참 분기의 옵션 지시문이 남아 있다.

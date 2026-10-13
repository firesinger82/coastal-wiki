---
file: models/ROMS/raw/source_code/roms/ROMS/Include/lake_signell.h
lines: 90
sha256: fae5c5a29b38707d25c95c3ac6e4e685978adc80077b7b9bb6d580899f2b32b4
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# lake_signell.h — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·바람 강제 폐쇄 분지(closed basin) 주석과 LAKE_SIGNELL·ROMS/floats/퇴적물 입력 파일을 포함한다(1–15). 빈 줄을 포함한다(16). |
| 17–28 | 시작 시 열린 전처리 조건 없음. UV_ADV·DJ_GRADPS·수직 스플라인·TS_MPDATA·SALINITY·SOLVE3D·MASKING·AVERAGES·FLOATS를 정의하고 UV_COR를 해제한다(17–27). 빈 줄을 포함한다(28). 원문: `#define UV_ADV` (17); `#undef  UV_COR` (18); `#define DJ_GRADPS` (19); `#define SPLINES_VDIFF` (20); `#define SPLINES_VVISC` (21); `#define TS_MPDATA` (22); `#define SALINITY` (23); `#define SOLVE3D` (24); `#define MASKING` (25); `#define AVERAGES` (26); `#define FLOATS` (27). |
| 29–55 | 시작 시 열린 전처리 조건 없음. 주석은 네 바닥 마찰/경계층 옵션 중 하나를 선택하도록 적는다(29). UV_LOGDRAG/MB_BBL/SG_BBL을 해제하고 SSW_BBL을 정의한다(31–34). SG/MB/SSW별 거칠기·궤도 속도·보간 옵션을 정의하거나 해제한다(36–50). 세 BBL 중 하나면 ANA_WWAVE를 정의한다(52–54). 빈 줄을 포함한다(55). 원문: `#undef UV_LOGDRAG` (31); `#undef MB_BBL` (32); `#undef SG_BBL` (33); `#define SSW_BBL` (34); `#ifdef SG_BBL` (36); `# define SG_CALC_ZNOT` (37); `# undef  SG_LOGINT` (38); `#endif` (39); `#ifdef MB_BBL` (40); `# define MB_CALC_ZNOT` (41); `# undef  MB_Z0BIO` (42); `# undef  MB_Z0BL` (43); `# undef  MB_Z0RIP` (44); `#endif` (45); `#ifdef SSW_BBL` (46); `# define SSW_CALC_UB` (47); `# define SSW_CALC_ZNOT` (48); `# undef  SSW_LOGINT` (49); `#endif` (50); `#if defined MB_BBL \|\| defined SG_BBL \|\| defined SSW_BBL` (52); `# define ANA_WWAVE` (53); `#endif` (54). |
| 56–78 | 시작 시 열린 전처리 조건 없음. SEDIMENT를 정의하고 SUSPLOAD/BEDLOAD_SOULSBY를 정의하며 SED_MORPH를 해제한다(56–61). SEDIMENT 또는 BBL이면 ANA_SEDIMENT, MASKING이면 ANA_MASK를 정의한다(62–67). 해석 격자·초기장·표면/바닥 플럭스·복사 옵션을 정의한다(68–77). 빈 줄을 포함한다(78). 원문: `#define SEDIMENT` (56); `#ifdef SEDIMENT` (57); `# define SUSPLOAD` (58); `# define BEDLOAD_SOULSBY` (59); `# undef  SED_MORPH` (60); `#endif` (61); `#if defined SEDIMENT \|\| defined SG_BBL \|\| defined MB_BBL \|\| defined SSW_BBL` (62); `# define ANA_SEDIMENT` (63); `#endif` (64); `#ifdef MASKING` (65); `# define ANA_MASK` (66); `#endif` (67); `#define ANA_GRID` (68); `#define ANA_INITIAL` (69); `#define ANA_SMFLUX` (70); `#define ANA_STFLUX` (71); `#define ANA_SSFLUX` (72); `#define ANA_BPFLUX` (73); `#define ANA_BTFLUX` (74); `#define ANA_BSFLUX` (75); `#define ANA_SPFLUX` (76); `#define ANA_SRFLUX` (77). |
| 79–90 | 시작 시 열린 전처리 조건 없음. 수직 혼합 모형 하나를 선택하도록 적는 주석을 포함한다(79–80). ANA_VMIX·MY25_MIXING을 해제하고 GLS_MIXING을 정의한다(81–83). GLS 또는 MY25 조건에서 KANTHA_CLAYSON/N2S2_HORAVG/RI_SPLINES를 정의하고 CRAIG_BANNER/CHARNOK를 해제한다(84–90). 원문: `#undef ANA_VMIX` (81); `#undef MY25_MIXING` (82); `#define GLS_MIXING` (83); `#if defined GLS_MIXING \|\| defined MY25_MIXING` (84); `# define KANTHA_CLAYSON` (85); `# define N2S2_HORAVG` (86); `# define RI_SPLINES` (87); `# undef CRAIG_BANNER` (88); `# undef CHARNOK` (89); `#endif` (90). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22·56–61: TS_MPDATA를 정의한다. SEDIMENT 조건은 SUSPLOAD와 BEDLOAD_SOULSBY를 정의하고 SED_MORPH를 해제한다. 이 기록은 해당 옵션의 실행 결과를 확인하지 않았다.

---
file: models/ROMS/raw/source_code/roms/ROMS/Include/bio_toy.h
lines: 110
sha256: c2e94f28c0705569a39e09c802f8a8b244032c5353bffc875da93fd1d3080324
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# bio_toy.h — 판독 구간 기록

구간은 1행부터 110행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·수직 1차원 생물 모델(biology model) 설정 주석을 포함한다(1–10). BIO_TOY·roms_bio_toy.in·생물 모델별 입력 파일들을 적는다(11–14). 주석 종료·빈 줄을 포함한다(15–16). |
| 17–39 | 시작 시 열린 전처리 조건 없음. 운동량·DJ_GRADPS·수직 스플라인·단파복사·비선형 상태방정식·염분·평균 출력(averages)·SOLVE3D를 정의한다(17–28). LMD_MIXING을 정의하고 그 조건 안에서 RIMIX/CONVEC/SKPP/BKPP/NONLOCAL/RI_SPLINES 옵션을 정의한다(30–38). 빈 줄을 포함한다(39). 원문: `#define UV_ADV` (17); `#define UV_SADVECTION` (18); `#define UV_COR` (19); `#define UV_QDRAG` (20); `#define DJ_GRADPS` (21); `#define SPLINES_VDIFF` (22); `#define SPLINES_VVISC` (23); `#define SOLAR_SOURCE` (24); `#define NONLIN_EOS` (25); `#define SALINITY` (26); `#define AVERAGES` (27); `#define SOLVE3D` (28); `#define LMD_MIXING` (30); `#ifdef LMD_MIXING` (31); `# define LMD_RIMIX` (32); `# define LMD_CONVEC` (33); `# define LMD_SKPP` (34); `# define LMD_BKPP` (35); `# define LMD_NONLOCAL` (36); `# define RI_SPLINES` (37); `#endif` (38). |
| 40–56 | 시작 시 열린 전처리 조건 없음. BULK_FLUXES를 정의한다(40). 참 분기는 LONGWAVE·ANA_RAIN, ELSE는 ANA_SMFLUX·ANA_STFLUX를 정의한다(41–47). 공통 ANA_SSFLUX/ANA_BSFLUX/ANA_BTFLUX와 생물 옵션 구분 주석을 포함한다(49–56). 원문: `#define BULK_FLUXES` (40); `#ifdef BULK_FLUXES` (41); `# define LONGWAVE` (42); `# define ANA_RAIN` (43); `#else` (44); `# define ANA_SMFLUX` (45); `# define ANA_STFLUX` (46); `#endif` (47); `#define ANA_SSFLUX` (49); `#define ANA_BSFLUX` (50); `#define ANA_BTFLUX` (51). |
| 57–81 | 시작 시 열린 전처리 조건 없음. BIO_FENNEL을 정의하고 ECB/ECOSIM/NEMURO/NPZD_FRANKS/NPZD_IRON/NPZD_POWELL을 해제한다(57–63). BIO_FENNEL 조건은 CARBON/DENITRIFICATION/BIO_SEDIMENT/DIAGNOSTICS_BIO를 정의한다(65–70). ECB 조건은 해석 초기 조건·해석 생물장과 같은 옵션·OXYGEN을 정의한다(72–80). 빈 줄을 포함한다(81). 원문: `#define BIO_FENNEL` (57); `#undef  ECB` (58); `#undef  ECOSIM` (59); `#undef  NEMURO` (60); `#undef  NPZD_FRANKS` (61); `#undef  NPZD_IRON` (62); `#undef  NPZD_POWELL` (63); `#ifdef BIO_FENNEL` (65); `# define CARBON` (66); `# define DENITRIFICATION` (67); `# define BIO_SEDIMENT` (68); `# define DIAGNOSTICS_BIO` (69); `#endif` (70); `#ifdef ECB` (72); `# define ANA_INITIAL` (73); `# define ANA_BIOLOGY` (74); `# define CARBON` (75); `# define DENITRIFICATION` (76); `# define BIO_SEDIMENT` (77); `# define DIAGNOSTICS_BIO` (78); `# define OXYGEN` (79); `#endif` (80). |
| 82–110 | 시작 시 열린 전처리 조건 없음. ECOSIM/BIO_FENNEL/ECB이면 ANA_SPFLUX·ANA_BPFLUX·ANA_CLOUD를 정의한다(82–86). NEMURO는 HOLLING_GRAZING을 정의하고 IVLEV_EXPLICIT을 해제하며 두 플럭스를 정의한다(88–93). NPZD_FRANKS/NPZD_POWELL도 두 플럭스를 정의한다(95–98). NPZD_IRON은 두 플럭스를 정의하고 IRON_LIMIT/IRON_RELAX를 해제한다(100–105). BULK_FLUXES 또는 ECOSIM은 ANA_CLOUD·PAPA_CLM을 정의한다(107–110). 원문: `#if defined ECOSIM \|\| defined BIO_FENNEL \|\| defined ECB` (82); `# define ANA_SPFLUX` (83); `# define ANA_BPFLUX` (84); `# define ANA_CLOUD` (85); `#endif` (86); `#if defined NEMURO` (88); `# define HOLLING_GRAZING` (89); `# undef  IVLEV_EXPLICIT` (90); `# define ANA_SPFLUX` (91); `# define ANA_BPFLUX` (92); `#endif` (93); `#if defined NPZD_FRANKS \|\| defined NPZD_POWELL` (95); `# define ANA_SPFLUX` (96); `# define ANA_BPFLUX` (97); `#endif` (98); `#if defined NPZD_IRON` (100); `# define ANA_SPFLUX` (101); `# define ANA_BPFLUX` (102); `# undef  IRON_LIMIT` (103); `# undef  IRON_RELAX` (104); `#endif` (105); `#if defined BULK_FLUXES \|\| defined ECOSIM` (107); `# define ANA_CLOUD` (108); `# define PAPA_CLM` (109); `#endif` (110). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57·65–69·82–85·107–109: 이 파일이 정의한 BIO_FENNEL과 BULK_FLUXES 조건에서는 ANA_CLOUD를 85행과 108행에서 각각 정의한다.

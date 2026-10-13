---
file: models/ROMS/raw/source_code/roms/ROMS/Include/test_head.h
lines: 104
sha256: 1947e105d826c583412a5bbd9a917ce5b8107b19fd161558cc73ccd88244d82d
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# test_head.h — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 저작권·MIT/X 형식 라이선스·License_ROMS.md 안내(1–7). 주석은 퇴적물(sediment) 곶 시험의 응용 플래그 TEST_HEAD와 입력 파일 roms_test_head.in·coupling_test_head.in·sediment_test_head.in을 지정한다(9–14). |
| 17–40 | 무조건 전처리 설정. CURVGRID·UV_COR·SALINITY를 해제하고 WET_DRY·WEC_VF·SWAN_COUPLING·MASKING·OUT_DOUBLE·UV_ADV·DJ_GRADPS·SOLVE3D를 정의한다(17–27). SSH_TIDES·UV_TIDES·ANA_FSOBC·ANA_M2OBC·FSOBC_REDUCED를 정의한다(29–33). 바닥 항력(bottom drag) 설정은 UV_LOGDRAG를 정의하고 UV_QDRAG·MB_BBL·SG_BBL·SSW_BBL을 해제한다(35–39). 전처리 원문: `#undef  CURVGRID` (17); `#define WET_DRY` (18); `#define WEC_VF` (19); `#define SWAN_COUPLING` (20); `#define MASKING` (21); `#define OUT_DOUBLE` (22); `#define UV_ADV` (23); `#undef  UV_COR` (24); `#define DJ_GRADPS` (25); `#undef  SALINITY` (26); `#define SOLVE3D` (27); `#define SSH_TIDES` (29); `#define UV_TIDES` (30); `#define ANA_FSOBC` (31); `#define ANA_M2OBC` (32); `#define FSOBC_REDUCED` (33); `#define UV_LOGDRAG` (35); `#undef  UV_QDRAG` (36); `#undef  MB_BBL` (37); `#undef  SG_BBL` (38); `#undef  SSW_BBL` (39). |
| 41–64 | SWAN_COUPLING 조건은 MCT_LIB를 정의한다(41–43). SG_BBL·MB_BBL·SSW_BBL의 독립 조건들은 각각 거칠기 관련 매크로를 정의하거나 해제한다(45–58). MB_BBL·SG_BBL·SSW_BBL·WEC_VF 중 하나가 정의되면 ANA_WWAVE를 해제한다(59–60). 그 안의 ANA_WWAVE 미정의 조건에는 실행 지시문이 없다(61–62). 빈 줄도 포함한다(44·64). 전처리 원문: `#ifdef SWAN_COUPLING` (41); `# define MCT_LIB` (42); `#endif` (43); `#ifdef SG_BBL` (45); `# define SG_CALC_ZNOT` (46); `# undef  SG_LOGINT` (47); `#endif` (48); `#ifdef MB_BBL` (49); `# define MB_CALC_ZNOT` (50); `# undef  MB_Z0BIO` (51); `# undef  MB_Z0BL` (52); `# undef  MB_Z0RIP` (53); `#endif` (54); `#ifdef SSW_BBL` (55); `# define SSW_CALC_ZNOT` (56); `# undef  SSW_LOGINT` (57); `#endif` (58); `#if defined MB_BBL \|\| defined SG_BBL \|\| defined SSW_BBL \|\| defined WEC_VF` (59); `# undef ANA_WWAVE` (60); `# ifndef ANA_WWAVE` (61); `# endif` (62); `#endif` (63). |
| 65–85 | SOLVE3D 조건에서 SPLINES_VDIFF·SPLINES_VVISC·SEDIMENT를 정의한다(65–68). 내부 SEDIMENT 조건은 SED_MORPH·SUSPLOAD·BEDLOAD_MPM을 정의하고 SED_DENS·BEDLOAD_SOULSBY를 해제한다(69–75). 내부 SEDIMENT·SG_BBL·MB_BBL·SSW_BBL 중 하나가 정의되면 ANA_SEDIMENT를 해제한다(76–78). 같은 SOLVE3D 조건에서 ANA_STFLUX·ANA_SSFLUX·ANA_BPFLUX·ANA_BTFLUX·ANA_BSFLUX·ANA_SPFLUX·ANA_SRFLUX를 정의한다(79–85). 전처리 원문: `#ifdef SOLVE3D` (65); `# define SPLINES_VDIFF` (66); `# define SPLINES_VVISC` (67); `# define SEDIMENT` (68); `# ifdef SEDIMENT` (69); `#  define SED_MORPH` (70); `#  undef  SED_DENS` (71); `#  define SUSPLOAD` (72); `#  define BEDLOAD_MPM` (73); `#  undef  BEDLOAD_SOULSBY` (74); `# endif` (75); `# if defined SEDIMENT \|\| defined SG_BBL \|\| defined MB_BBL \|\| defined SSW_BBL` (76); `#  undef ANA_SEDIMENT` (77); `# endif` (78); `# define ANA_STFLUX` (79); `# define ANA_SSFLUX` (80); `# define ANA_BPFLUX` (81); `# define ANA_BTFLUX` (82); `# define ANA_BSFLUX` (83); `# define ANA_SPFLUX` (84); `# define ANA_SRFLUX` (85). |
| 86–104 | 시작 시 `#ifdef SOLVE3D` (65) 안. SOLVE3D 조건 내부에서 ANA_VMIX를 해제하고 MY25_MIXING을 정의하며 GLS_MIXING을 해제한다(87–89). 내부 GLS_MIXING 또는 MY25_MIXING 조건은 KANTHA_CLAYSON·N2S2_HORAVG·RI_SPLINES를 정의하고 CRAIG_BANNER·CHARNOK·ZOS_HSIG·TKE_WAVEDISS를 해제한다(90–98). SOLVE3D 조건이 닫힌 뒤 ANA_GRID·ANA_INITIAL을 해제하고 ANA_SMFLUX를 정의한다(99–103). 마지막 빈 줄을 포함한다(104). 전처리 원문: `# undef  ANA_VMIX` (87); `# define MY25_MIXING` (88); `# undef  GLS_MIXING` (89); `# if defined GLS_MIXING \|\| defined MY25_MIXING` (90); `#  define KANTHA_CLAYSON` (91); `#  define N2S2_HORAVG` (92); `#  define RI_SPLINES` (93); `#  undef  CRAIG_BANNER` (94); `#  undef  CHARNOK` (95); `#  undef  ZOS_HSIG` (96); `#  undef  TKE_WAVEDISS` (97); `# endif` (98); `#endif` (99); `#undef  ANA_GRID` (101); `#undef  ANA_INITIAL` (102); `#define ANA_SMFLUX` (103). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 59–63: ANA_WWAVE를 해제한 직후의 `# ifndef ANA_WWAVE` (61) 블록은 `# endif` (62)만 포함한다.

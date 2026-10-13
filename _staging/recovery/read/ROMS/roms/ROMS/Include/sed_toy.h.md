---
file: models/ROMS/raw/source_code/roms/ROMS/Include/sed_toy.h
lines: 83
sha256: 3451d939bcbb63ddf56e66786fbdb113493cfb44dd85af859fae529826034c80
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sed_toy.h — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·수직 1차원 퇴적물 시험 주석과 SED_TOY·ROMS/퇴적물 입력 파일을 포함한다(1–14). 빈 줄을 포함한다(15). |
| 16–39 | 시작 시 열린 전처리 조건 없음. BODYFORCE/LOG_PROFILE/SALINITY를 해제하고 DJ_GRADPS·OUT_DOUBLE·해석 격자/초기장/표면 운동량 플럭스·SOLVE3D를 정의한다(16–24). SOLVE3D 조건에 수직 스플라인·해석 퇴적물·표면/바닥 수동 추적자/염분/추적자·복사 플럭스를 정의한다(25–36). ANA_VMIX·ANA_WWAVE 해제·빈 줄을 포함한다(37–39). 원문: `#undef  BODYFORCE` (16); `#undef  LOG_PROFILE` (17); `#define DJ_GRADPS` (18); `#undef  SALINITY` (19); `#define OUT_DOUBLE` (20); `#define ANA_GRID` (21); `#define ANA_INITIAL` (22); `#define ANA_SMFLUX` (23); `#define SOLVE3D` (24); `#ifdef SOLVE3D` (25); `# define SPLINES_VDIFF` (26); `# define SPLINES_VVISC` (27); `# define ANA_SEDIMENT` (28); `# define ANA_BPFLUX` (29); `# define ANA_BSFLUX` (30); `# define ANA_BTFLUX` (31); `# define ANA_SPFLUX` (32); `# define ANA_SRFLUX` (33); `# define ANA_SSFLUX` (34); `# define ANA_STFLUX` (35); `#endif` (36); `#undef  ANA_VMIX` (37); `#undef  ANA_WWAVE` (38). |
| 40–63 | 시작 시 열린 전처리 조건 없음. UV_LOGDRAG를 정의하고 UV_LDRAG/UV_QDRAG를 해제한다(40–42). SG_BBL/MB_BBL/SSW_BBL을 각 조건 검사 앞에서 해제한다(44·50·58). 해당 분기에는 각각 거칠기/보간 옵션의 define/undef 지시문을 남긴다(45–62). 빈 줄을 포함한다(63). 원문: `#define UV_LOGDRAG` (40); `#undef  UV_LDRAG` (41); `#undef  UV_QDRAG` (42); `#undef  SG_BBL` (44); `#ifdef SG_BBL` (45); `# undef  SG_CALC_ZNOT` (46); `# undef  SG_LOGINT` (47); `#endif` (48); `#undef  MB_BBL` (50); `#ifdef MB_BBL` (51); `# undef  MB_CALC_ZNOT` (52); `# undef  MB_Z0BIO` (53); `# undef  MB_Z0BL` (54); `# undef  MB_Z0RIP` (55); `#endif` (56); `#undef SSW_BBL` (58); `#ifdef SSW_BBL` (59); `# define SSW_CALC_ZNOT` (60); `# undef  SSW_LOGINT` (61); `#endif` (62). |
| 64–74 | 시작 시 열린 전처리 조건 없음. GLS_MIXING을 정의한다(64). 해당 조건에서 KANTHA_CLAYSON/N2S2_HORAVG/RI_SPLINES를 정의하고 CRAIG_BANNER/CHARNOK/ZOS_HSIG/TKE_WAVEDISS를 해제한다(65–73). 빈 줄을 포함한다(74). 원문: `#define GLS_MIXING` (64); `#ifdef GLS_MIXING` (65); `# define KANTHA_CLAYSON` (66); `# define N2S2_HORAVG` (67); `# define RI_SPLINES` (68); `# undef  CRAIG_BANNER` (69); `# undef  CHARNOK` (70); `# undef  ZOS_HSIG` (71); `# undef  TKE_WAVEDISS` (72); `#endif` (73). |
| 75–83 | 시작 시 열린 전처리 조건 없음. SEDIMENT를 정의한다(75). 해당 조건에서 SUSPLOAD/SED_DENS/SED_MORPH를 정의하고 BEDLOAD_SOULSBY/BEDLOAD_MPM/SED_BIODIFF를 해제한다(76–83). 원문: `#define SEDIMENT` (75); `#ifdef SEDIMENT` (76); `# define SUSPLOAD` (77); `# undef  BEDLOAD_SOULSBY` (78); `# undef  BEDLOAD_MPM` (79); `# define SED_DENS` (80); `# define SED_MORPH` (81); `# undef  SED_BIODIFF` (82); `#endif` (83). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44–62: SG_BBL·MB_BBL·SSW_BBL은 각 조건 검사 앞에서 해제한다. 그 뒤의 조건 분기 안에 관련 옵션 지시문들이 남아 있다.

---
file: models/ROMS/raw/source_code/roms/ROMS/Include/upwelling.h
lines: 88
sha256: 72e5630393c5619ca0a299ff8d1174148d7f88eaf50625d152feb5fa1fecc20f
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# upwelling.h — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 저작권·MIT/X 형식 라이선스 안내(1–7). 용승(upwelling) 시험이라는 주석은 응용 플래그 UPWELLING과 입력 파일 roms_upwelling.in을 지정한다(9–12). |
| 15–42 | UV_ADV·UV_COR·UV_LDRAG·UV_VIS2·MIX_S_UV·SPLINES_VDIFF·SPLINES_VVISC·DJ_GRADPS·TS_DIF2·MIX_S_TS를 정의한다(15–27). MIX_GEO_UV·TS_DIF4·MIX_GEO_TS를 해제한다(19·25–26). SALINITY·SOLVE3D·AVERAGES·DIAGNOSTICS_TS·DIAGNOSTICS_UV를 정의한다(29–33). ANA_GRID·ANA_INITIAL·ANA_SMFLUX·ANA_STFLUX·ANA_SSFLUX·ANA_BTFLUX·ANA_BSFLUX를 정의한다(35–41). 전처리 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_LDRAG` (17); `#define UV_VIS2` (18); `#undef  MIX_GEO_UV` (19); `#define MIX_S_UV` (20); `#define SPLINES_VDIFF` (21); `#define SPLINES_VVISC` (22); `#define DJ_GRADPS` (23); `#define TS_DIF2` (24); `#undef  TS_DIF4` (25); `#undef  MIX_GEO_TS` (26); `#define MIX_S_TS` (27); `#define SALINITY` (29); `#define SOLVE3D` (30); `#define AVERAGES` (31); `#define DIAGNOSTICS_TS` (32); `#define DIAGNOSTICS_UV` (33); `#define ANA_GRID` (35); `#define ANA_INITIAL` (36); `#define ANA_SMFLUX` (37); `#define ANA_STFLUX` (38); `#define ANA_SSFLUX` (39); `#define ANA_BTFLUX` (40); `#define ANA_BSFLUX` (41). |
| 43–65 | GLS_MIXING 또는 MY25_MIXING 조건은 KANTHA_CLAYSON·N2S2_HORAVG·RI_SPLINES를 정의한다(43–46). else는 ANA_VMIX를 정의한다(47–49). BIO_FENNEL·ECB·ECOSIM·NEMURO·NPZD_POWELL 중 하나가 정의되면 ANA_BIOLOGY·ANA_SPFLUX·ANA_BPFLUX·ANA_SRFLUX를 정의한다(51–60). NEMURO 조건은 HOLLING_GRAZING을 정의하고 IVLEV_EXPLICIT을 해제한다(62–65). 전처리 원문: `#if defined GLS_MIXING \|\| defined MY25_MIXING` (43); `# define KANTHA_CLAYSON` (44); `# define N2S2_HORAVG` (45); `# define RI_SPLINES` (46); `#else` (47); `# define ANA_VMIX` (48); `#endif` (49); `#if defined BIO_FENNEL  \|\| \` (51); `    defined ECB         \|\| \` (52); `    defined ECOSIM      \|\| \` (53); `    defined NEMURO      \|\| \` (54); `    defined NPZD_POWELL` (55); `# define ANA_BIOLOGY` (56); `# define ANA_SPFLUX` (57); `# define ANA_BPFLUX` (58); `# define ANA_SRFLUX` (59); `#endif` (60); `#if defined NEMURO` (62); `# define HOLLING_GRAZING` (63); `# undef  IVLEV_EXPLICIT` (64); `#endif` (65). |
| 66–88 | BIO_FENNEL 조건은 CARBON·DENITRIFICATION·BIO_SEDIMENT·DIAGNOSTICS_BIO를 정의한다(67–72). ECB 조건은 같은 네 매크로에 OXYGEN을 추가한다(74–80). PERFECT_RESTART 조건은 앞에서 정의한 AVERAGES·DIAGNOSTICS_TS·DIAGNOSTICS_UV와 조건부 DIAGNOSTICS_BIO를 해제하고 OUT_DOUBLE을 정의한다(82–88). 전처리 원문: `#ifdef BIO_FENNEL` (67); `# define CARBON` (68); `# define DENITRIFICATION` (69); `# define BIO_SEDIMENT` (70); `# define DIAGNOSTICS_BIO` (71); `#endif` (72); `#ifdef ECB` (74); `# define CARBON` (75); `# define DENITRIFICATION` (76); `# define BIO_SEDIMENT` (77); `# define DIAGNOSTICS_BIO` (78); `# define OXYGEN` (79); `#endif` (80); `#ifdef PERFECT_RESTART` (82); `# undef  AVERAGES` (83); `# undef  DIAGNOSTICS_BIO` (84); `# undef  DIAGNOSTICS_TS` (85); `# undef  DIAGNOSTICS_UV` (86); `# define OUT_DOUBLE` (87); `#endif` (88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 82–88: PERFECT_RESTART 조건의 마지막 설정은 AVERAGES·DIAGNOSTICS_BIO·DIAGNOSTICS_TS·DIAGNOSTICS_UV 해제와 OUT_DOUBLE 정의이다. 앞의 AVERAGES·DIAGNOSTICS_TS·DIAGNOSTICS_UV 정의는 31–33행에 있다.

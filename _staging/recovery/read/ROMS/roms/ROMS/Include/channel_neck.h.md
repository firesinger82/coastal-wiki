---
file: models/ROMS/raw/source_code/roms/ROMS/Include/channel_neck.h
lines: 74
sha256: 8aebb99a934422641a3aa357088c5e5cc50c56c9330762195e370a32ffe3804b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# channel_neck.h — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·협착 수로(channel with a constriction) 주석과 CHANNEL_NECK·입력 파일 둘을 포함한다(1–14). CORRELATION을 정의하고 AD_SENSITIVITY/MULTI_DOMAIN/OPT_OBSERVATIONS/OPT_PERTURBATION/SANITY_CHECK/TLM_DRIVER를 해제한다(15–21). 빈 줄을 포함한다(22). 원문: `#undef  AD_SENSITIVITY` (15); `#define CORRELATION` (16); `#undef  MULTI_DOMAIN` (17); `#undef  OPT_OBSERVATIONS` (18); `#undef  OPT_PERTURBATION` (19); `#undef  SANITY_CHECK` (20); `#undef  TLM_DRIVER` (21). |
| 23–38 | 시작 시 열린 전처리 조건 없음. 운동량·MIX_GEO_UV·DJ_GRADPS·SOLVE3D·MASKING·해석 표면/바닥 플럭스를 정의한다(23–36). TS_DIF2/MIX_GEO_TS/ANA_INITIAL/ANA_VMIX를 해제한다(29–30·33·37). 빈 줄을 포함한다(38). 원문: `#define UV_ADV` (23); `#define UV_COR` (24); `#define UV_LDRAG` (25); `#define UV_VIS2` (26); `#define MIX_GEO_UV` (27); `#define DJ_GRADPS` (28); `#undef  TS_DIF2` (29); `#undef  MIX_GEO_TS` (30); `#define SOLVE3D` (31); `#define MASKING` (32); `#undef  ANA_INITIAL` (33); `#define ANA_SMFLUX` (34); `#define ANA_STFLUX` (35); `#define ANA_BTFLUX` (36); `#undef  ANA_VMIX` (37). |
| 39–59 | 시작 시 열린 전처리 조건 없음. CORRELATION이면 VCONVOLUTION·IMPLICIT_VCONV를 정의한다(39–42). TLM_DRIVER와 OPT_PERTURBATION의 각 조건은 FORWARD_READ를 정의하고 FORWARD_MIXING을 해제한다(44–52). SANITY_CHECK는 ANA_PERTURB·FORWARD_READ를 정의하고 FORWARD_MIXING을 해제한다(54–58). 빈 줄을 포함한다(59). 원문: `#ifdef CORRELATION` (39); `# define VCONVOLUTION` (40); `# define IMPLICIT_VCONV` (41); `#endif` (42); `#ifdef TLM_DRIVER` (44); `# define FORWARD_READ` (45); `# undef  FORWARD_MIXING` (46); `#endif` (47); `#ifdef OPT_PERTURBATION` (49); `# define FORWARD_READ` (50); `# undef  FORWARD_MIXING` (51); `#endif` (52); `#ifdef SANITY_CHECK` (54); `# define ANA_PERTURB` (55); `# define FORWARD_READ` (56); `# undef  FORWARD_MIXING` (57); `#endif` (58). |
| 60–74 | 시작 시 열린 전처리 조건 없음. AD_SENSITIVITY는 FORWARD_READ 정의·FORWARD_MIXING 해제를 수행한다(60–63). OPT_OBSERVATIONS는 VCONVOLUTION/IMPLICIT_VCONV/FORWARD_READ 정의·FORWARD_MIXING 해제를 수행한다(65–70). MULTI_DOMAIN이면 MASKING을 해제한다(72–74). 원문: `#ifdef AD_SENSITIVITY` (60); `# define FORWARD_READ` (61); `# undef  FORWARD_MIXING` (62); `#endif` (63); `#ifdef OPT_OBSERVATIONS` (65); `# define VCONVOLUTION` (66); `# define IMPLICIT_VCONV` (67); `# define FORWARD_READ` (68); `# undef  FORWARD_MIXING` (69); `#endif` (70); `#ifdef MULTI_DOMAIN` (72); `# undef MASKING` (73); `#endif` (74). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–21·44–74: TLM_DRIVER/OPT_PERTURBATION/SANITY_CHECK/AD_SENSITIVITY/OPT_OBSERVATIONS/MULTI_DOMAIN은 앞에서 해제한다. 뒤에 각 매크로의 조건 분기가 남아 있다.

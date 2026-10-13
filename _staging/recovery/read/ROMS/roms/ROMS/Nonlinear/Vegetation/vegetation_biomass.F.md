---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Vegetation/vegetation_biomass.F
lines: 235
sha256: 575650c2c978cacca250143f74f291371e48625a965d89bd1a969cc38cfe5cd6
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# vegetation_biomass.F — 판독 구간 기록

구간은 1행부터 235행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | cppdefs.h를 포함한다(1). 2–4행 주석은 이 파일을 사용하지 않는 옛 식생 속성 갱신 방법이라고 적는다. 이 판독은 그 주석과 실제 호출 여부를 구분한다. sed_biomass_mod를 시작하고 NONLINEAR·SEDIMENT·SED_BIOMASS가 모두 정의된 구현을 연다(5–7). 저작권·라이선스·퇴적물 생물량(biomass) 계산 설명과 빈 문헌 주석을 포함한다(9–21). PRIVATE를 기본으로 하고 sed_biomass를 공개한다(23–28). 조건·전처리 원문: `#include "cppdefs.h"` (1). `#if defined NONLINEAR && defined SEDIMENT && defined SED_BIOMASS` (7). |
| 30–76 | 시작 시 전처리 `#if defined NONLINEAR && defined SEDIMENT && defined SED_BIOMASS` (7) 안. sed_biomass(ng,tile)의 모듈 사용·인수·MyFile 선언이다(31–46). tile.h를 포함한다(48). PROFILE에서 wclock_on/off를 호출한다(51·71). sed_biomass_tile에 nstp·nnew·z_w·Dstp_max·bottom·settling_flux를 전달한다(53–69). MASKING에서 rmask, 그 안의 WET_DRY에서 rmask_wet, SPECTRAL_LIGHT에서 SgrN을 전달한다(57–65). RETURN과 루틴 종료를 포함한다(74–76). 조건·전처리 원문: `# include "tile.h"` (48). `# ifdef PROFILE` (50). `# endif` (52). `# ifdef MASKING` (57). `#  ifdef WET_DRY` (59). `#  endif` (61). `# endif` (62). `# ifdef SPECTRAL_LIGHT` (63). `# endif` (65). `# ifdef PROFILE` (70). `# endif` (72). |
| 77–106 | 시작 시 전처리 `#if defined NONLINEAR && defined SEDIMENT && defined SED_BIOMASS` (7) 안. sed_biomass_tile의 인수 목록이다(78–93). MASKING·WET_DRY·SPECTRAL_LIGHT에 따라 마스크(mask)와 SgrN 인수를 넣는다(82–90). mod_param·mod_scalars·mod_sediment를 가져오고 격자·타일(tile) 경계와 시간 인덱스 nstp·nnew를 선언한다(96–105). 조건·전처리 원문: `# ifdef MASKING` (82). `#  ifdef WET_DRY` (84). `#  endif` (86). `# endif` (87). `# ifdef SPECTRAL_LIGHT` (88). `# endif` (90). |
| 107–147 | 시작 시 전처리 `#if defined NONLINEAR && defined SEDIMENT && defined SED_BIOMASS` (7) 안. 시작 시 78행 sed_biomass_tile 안. ASSUMED_SHAPE에서는 하한만 지정한 배열을 선언하고 z_w의 수직 하한을 0으로 지정한다(107–120). # else 분기에서 z_w의 상한은 UBk, Dstp_max의 마지막 크기는 24, bottom은 MBOTP, settling_flux는 NST이다(121–134). 지역 정수·실수와 SEAGRASS_BOTTOM의 sgr_kgmmol을 선언한다(139–144). set_bounds.h를 포함한다(146). 조건·전처리 원문: `# ifdef ASSUMED_SHAPE` (107). `#  ifdef MASKING` (108). `#   ifdef WET_DRY` (110). `#   endif` (112). `#  endif` (113). `#  ifdef SPECTRAL_LIGHT` (114). `#  endif` (116). `# else` (121). `#  ifdef MASKING` (122). `#   ifdef WET_DRY` (124). `#   endif` (126). `#  endif` (127). `#  ifdef SPECTRAL_LIGHT` (128). `#  endif` (130). `# endif` (135). `# ifdef SEAGRASS_BOTTOM` (142). `# endif` (144). `# include "set_bounds.h"` (146). |
| 148–182 | 시작 시 전처리 `#if defined NONLINEAR && defined SEDIMENT && defined SED_BIOMASS` (7) 안. 시작 시 78행 타일 루틴 안. 시간당 모델 단계 수는 `nbio_steps=MAX(1,INT(3600.0_r8/dt(ng)))` (155). j=Jstr..Jend 루프(160)에서 시간당 갱신 조건(164)이 참일 때 i 루프(165)를 실행한다. 저장 인덱스와 수심(depth)은 `sstp=1+MOD(iic(ng)-ntstart(ng),24)` (169); `Dstp=z_w(i,j,N(ng))-z_w(i,j,0)` (173). 해당 수심을 Dstp_max에 복사하고 cff=0에서 k=1..nTbiom을 돈다(174–176). 최대값 누적은 `cff=MAX(cff,Dstp_max(i,j,k))` (177). 결과를 bottom의 imaxD에 복사한다(179). i 루프와 조건을 닫는다(180–181). 조건·전처리 원문: `IF (MOD(iic(ng),nbio_steps).eq.0) THEN` (164). |
| 183–211 | 시작 시 전처리 `#if defined NONLINEAR && defined SEDIMENT && defined SED_BIOMASS` (7) 안. 시작 시 78행 타일 루틴·160행 J_LOOP 안. SEAGRASS_BOTTOM에서 i=Istr..Iend를 돈다(185–186). 그 안의 SEAGRASS_SINK에서 해초(seagrass) 질소량의 단위 변환과 원기둥 높이 식은 `sgr_kgmmol = 2.8e-5_r8` (193); `cff = SgrN(i,j)*sgr_kgmmol/                                   &` (196); `&                    (0.25_r8*sgr_diam*sgr_diam*pi*sgr_density)` (197); `bottom(i,j,isgrH) = cff/bottom(i,j,isgrD)` (199). 높이 조건은 원문에 .lg. 연산자로 적혀 있다(201). 참 분기의 밀도 보정은 `bottom(i,j,isgrD)=bottom(i,j,isgrD)*                     &` (202); `&                    bottom(i,j,isgrH)/sgr_Hthres` (203)이며 높이를 sgr_Hthres로 복사한다(204). 187·194–195·206–208행의 직경·밀도·높이 기본값과 else 예시는 주석이다. cpp 조건과 i 루프를 닫는다(209–211). 조건·전처리 원문: `# ifdef SEAGRASS_BOTTOM` (185). `#  ifdef SEAGRASS_SINK` (188). `IF (bottom(i,j,isgrH).lg.sgr_Hthres) THEN` (201). `#  endif` (209). `# endif` (211). |
| 212–235 | 시작 시 전처리 `#if defined NONLINEAR && defined SEDIMENT && defined SED_BIOMASS` (7) 안. 시작 시 78행 타일 루틴·160행 J_LOOP 안. i=Istr..Iend 루프에서 종류 번호 ised=1과 cff=0을 넣는다(215–220). 생물량 식 예시는 주석이다(221). MASKING이면 `cff=cff*rmask(i,j)` (223), 그 안의 WET_DRY이면 `cff=cff*rmask_wet(i,j)          ! not sure this is needed` (225). 침강 플럭스(settling flux) 누적은 `settling_flux(i,j,ised)=settling_flux(i,j,ised)+cff` (228). i/j 루프·RETURN·루틴·바깥 전처리 조건·모듈 종료와 빈 줄까지 포함한다(229–235). 조건·전처리 원문: `# ifdef MASKING` (222). `#  ifdef WET_DRY` (224). `#  endif` (226). `# endif` (227). `#endif` (234). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2–4: 파일 미사용 설명은 원문 주석에 있다. 이 파일 밖의 호출 관계는 이번 판독에서 확인하지 않았다.
- 155·164·169: 시간당 갱신 조건은 MOD(iic,nbio_steps)이다. 저장 인덱스는 시간당 단계 수로 나누지 않은 iic-ntstart를 24로 나눈 나머지로 정한다.
- 132·169·176: 명시 크기 Dstp_max와 저장 인덱스는 24를 사용한다. 최대값 루프의 상한은 nTbiom을 사용한다.
- 201: 높이 비교 조건의 원문 연산자는 .lg.이다. 이 판독에서 컴파일은 수행하지 않았다.
- 219–228: 종류 번호는 1로 고정된다. cff는 활성 코드에서 0으로 설정되고 마스크를 곱한 뒤 settling_flux에 더해진다. 221행의 생물량 계산 예시는 주석이다.
- 88–90·114–116·128–130·188–199: SgrN 인수와 선언은 SPECTRAL_LIGHT 조건에 있다. SgrN을 참조하는 해초 높이 식은 SEAGRASS_BOTTOM과 SEAGRASS_SINK 조건에 있다.
- 105·160–230: nstp와 nnew는 입력 인수로 선언되지만 타일 실행문에서 사용되지 않는다.

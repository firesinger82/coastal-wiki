---
title: "ROMS Include — cppdefs·globaldefs·전처리 옵션 체계"
model: ROMS
component: ROMS/Include
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Include/). cppdefs.h(옵션 카탈로그·ROMS_HEADER include), globaldefs.h(내부 파생 매크로·옵션 조정), ROMS/Utility/checkdefs.F(별도 오류 검사), set_bounds.h/set_bounds_xtr.h/tile.h(타일 경계 매크로), upwelling.h(앱 헤더 예시) file:line 인용; 2026-10-14 ROMS recovery 대조 보고서 반영" # [10-14 전수 검증 정정]
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/README.md
---

# ROMS Include — cppdefs·globaldefs·전처리 옵션 체계

> ROMS 빌드 시 물리·수치 기능을 켜고 끄는 C-preprocessor(CPP) 옵션 계층의 본체. (경로: roms/ROMS/Include/)

CPP는 컴파일할 기능을 선택한다. `SOLVE3D`가 정의된 추적자 이류는 `Hadvection`·`Vadvection` 입력을 읽는다 (`ROMS/Utility/read_phypar.F:418-442`). 기후장·점소스의 논리 스위치도 해당 전처리 조건 안에서 실행 시 입력을 읽는다 (`ROMS/Utility/read_phypar.F:1078-1108`). 단일 실행 파일의 모든 선택이 컴파일 때 고정되는 것은 아니다 ([RBH-3448](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)). `Include/`의 파일군은 다음과 같다.

| 파일군 | 역할 | 대표 |
|---|---|---|
| `cppdefs.h` | 주석 옵션 카탈로그 + 앱 헤더 include 디스패치 | cppdefs.h |
| `globaldefs.h` | 내부 파생 매크로 자동 유도 + 옵션 파생·조정 | globaldefs.h |
| `<app>.h` (35개) | 응용별 옵션 묶음(사용자 선택) | upwelling.h, wc13.h, double_gyre.h … |
| `set_bounds*.h`, `tile.h` | 타일 경계 인덱스 헤더(F 파일에 inline include) | set_bounds.h, tile.h |

<!-- count: models/ROMS/raw/source_code/roms/ROMS/Include/*.h = 40 -->
현재 Include의 `*.h`는 40개이다. `cppdefs.h`·`globaldefs.h`·`set_bounds.h`·`set_bounds_xtr.h`·`tile.h`를 제외하면 응용 헤더는 35개이다. 수량은 해당 디렉터리의 `*.h` 파일명을 센 값이다 ([RBH-3451](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

---

## 1. 빌드 디스패치 메커니즘 — cppdefs.h

`cppdefs.h`의 앞부분은 CPP 옵션의 짧은 설명을 담은 주석 카탈로그다 (`ROMS/Include/cppdefs.h:11`). 이 주석 카탈로그는 모든 소스의 CPP 조건 이름을 열거하지 않는다. `ALBEDO_CSIM`과 `ADLER32_CHECKSUM`은 다른 파일에도 나타난다 (`ROMS/Nonlinear/SeaIce/ice_albedo.F:137`; `ROMS/Utility/get_hash.F:17`). `get_hash.F`는 파일 시작에서 `#undef ADLER32_CHECKSUM`을 적용한다 (`ROMS/Utility/get_hash.F:2`). 그 조건문의 존재를 활성 기능의 근거로 사용하지 않는다 ([RBH-3449](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

> `** The following is short description of all available CPP options.` — `cppdefs.h:11`

makefile은 `ROMS_APPLICATION`의 응용 이름을 소문자 파일명으로 바꾼다 (`makefile:230-232`). `cppdefs.h`는 `ROMS_HEADER` 뒤에서 `globaldefs.h`를 포함한다 (`ROMS/Include/cppdefs.h:753-754,763`).

```c
#if defined ROMS_HEADER
# include ROMS_HEADER
#else
   CPPDEFS - Choose an appropriate ROMS application.
#endif
```

코드 블록의 출처는 `ROMS/Include/cppdefs.h:753-757`이다. 756행의 미정의 응용 오류 토큰은 실제 코드이다. 뒤의 include는 `#include "globaldefs.h"`이다 (`ROMS/Include/cppdefs.h:763`). 헤더 카탈로그에 그 흐름이 명시돼 있다:

> `**    ROMS_HEADER="upwelling.h"` — `cppdefs.h:744`
> `**  in the makefile. ROMS will include the associated header file located` — `cppdefs.h:739`

makefile:78의 `ROMS_APPLICATION ?= UPWELLING`은 `ROMS_APPLICATION`이 아직 설정되지 않았을 때 기본값을 지정한다. `cppdefs.h:736`은 같은 대입을 설명하는 주석이다. `cppdefs.h`는 `ROMS_HEADER` 뒤에서 `globaldefs.h`를 포함한다 (`ROMS/Include/cppdefs.h:753-754,763`).

### 사전 정의 응용(pre-defined applications)
`cppdefs.h`의 사례 카탈로그와 현재 동봉 헤더 목록은 다르다. `BASIN`·`UPWELLING`·`WINDBASIN`의 카탈로그 줄은 각각 684·713·715다 (`ROMS/Include/cppdefs.h:684,713,715`). `ADRIA02`와 `NJ_BIGHT`는 카탈로그에 있지만 해당 이름의 헤더는 현재 Include에 없다. 응용 헤더 수는 35개다 ([RT1-1524](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안), [RBH-3451](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

---

## 2. 옵션 카탈로그 분류 (cppdefs.h 주석)

cppdefs.h 주석은 옵션을 물리/수치 도메인별로 군집화한다. 대표 군:

| 도메인 | 시작 행 | 대표 옵션 |
|---|---|---|
| 운동량 방정식 | `cppdefs.h:13` | `UV_ADV`(이류 토글, `:33`), `UV_COR`(코리올리, `:34`), `UV_VIS2`/`UV_VIS4`(조화/이중조화 점성, `:39`/`:40`), `UV_SMAGORINSKY`(`:41`), `UV_*DRAG`(바닥마찰, `:43`–`:45`) |
| 바로트로픽 시간적분 | `cppdefs.h:49` | `STEP2D_FB_LF_AM3`(`:55`), `STEP2D_FB_AB3_AM4`(`:56`) |
| 추적자(tracer) | `cppdefs.h:63` | `TS_DIF2`/`TS_DIF4`(`:65`/`:66`), `NONLIN_EOS`(비선형 상태방정식, `:71`), `SALINITY`(`:73`), `T_PASSIVE`(수동추적자, `:69`) |
| 압력경도 알고리즘 | `cppdefs.h:90` | `DJ_GRADPS`(스플라인 밀도 야코비안, `:97`), `PJ_GRADP`(`:98`), `WJ_GRADP`(`:101`) |
| 표면 플럭스/대기경계층 | `cppdefs.h:106` | `BULK_FLUXES`(`:117`), `COOL_SKIN`(`:118`), `LONGWAVE`(`:119`), `EMINUSP`(`:121`) |
| 파랑 거칠기(bulk flux) | `cppdefs.h:124` | `COARE_TAYLOR_YELLAND`(`:126`), `COARE_OOST`(`:127`), `DRENNAN`(`:128`) |

각 옵션은 `** NAME    설명` 형식 한 줄로 문서화된다. 예: `** UV_ADV                  to turn ON or OFF advection terms`(`cppdefs.h:33`), `** NONLIN_EOS              if using nonlinear equation of state`(`cppdefs.h:71`).

운동량 이류의 **기본값** 규칙(주석): 옵션 미선택 시 3D 운동량 수평이류는 3차 풍상편향, 2D는 4차 중심차분, 수직은 4차 중심차분 — `cppdefs.h:15-18`. 즉 운동량 이류 플래그를 켤 필요 없음:

> `**   is the case, no flags for momentum advection need to be activated.` — `cppdefs.h:18`

`UV_SADVECTION`의 소스 주석은 이상화한 응용이면서 수직 해상도가 높은 응용에서만 사용하도록 권고한다 (`ROMS/Include/cppdefs.h:30-31`).

---

## 3. 내부 파생 매크로 — globaldefs.h (핵심 메커닉)

`globaldefs.h`의 정의를 수정하지 않을 것을 소스 주석이 강하게 권고한다 (`ROMS/Include/globaldefs.h:11-13`).

> `** WARNING: This  file  contains  a set of  predetermined macro definitions` — `globaldefs.h:11`
> `** It is strongly recommended to NOT modify any of the definitions below.` — `globaldefs.h:13`

`globaldefs.h`는 옵션을 파생·조정한다. `checkdefs.F`는 별도 오류 검사를 수행한다. `Q_PSOURCE`가 정의되고 `Master`가 참이면 폐기된 질량 점소스 옵션이라는 오류 문구를 출력한다. 이 경로는 `exit_flag=5`를 대입한다 (`ROMS/Utility/checkdefs.F:3819-3829`; [RBH-3450](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

### (a) 플랫폼·병렬 내부 스위치
- `MPI` 정의 시 내부 `DISTRIBUTE` 자동 정의(`globaldefs.h:46-48`) — 분산메모리 코드 경로 전체의 게이트.
- `DISTRIBUTE`가 정의된 조건에서 각 통신 계열의 명시적 선택이 없으면 해당 `ALLREDUCE`를 정의한다. 이 규칙은 `BOUNDARY`·`COLLECT`·`REDUCE`뿐 아니라 `ASSEMBLE`에도 있다 (`ROMS/Include/globaldefs.h:57-63,71-76,85-91,100-106`).
- `#define PROFILE` 무조건 — 시간 프로파일링 ON (`globaldefs.h:112`).

### (b) 상위 → 하위 파생 (대표: 4D-Var / adjoint)
`TANGENT`와 `ADJOINT`는 각각 `globaldefs.h`의 별도 조건식으로 정의한다. 두 목록은 동일하지 않다 (`ROMS/Include/globaldefs.h:361-393,395-427`). `AD_SENSITIVITY`와 `AFT_EIGENMODES`가 `TANGENT`도 항상 정의한다고 쓰지 않는다 ([DA1-815](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md#4-노트-대조와-수정안)).

`# define TANGENT`의 출처는 `ROMS/Include/globaldefs.h:392`이다. `# define ADJOINT`의 출처는 `ROMS/Include/globaldefs.h:426`이다.

(`globaldefs.h:361-393`, `globaldefs.h:395-427`). 유사하게:
- `TL_IOMS`(접선선형의 표현자 모드) — `ARRAY_MODES`/`R4DVAR` 등에서 파생 (`globaldefs.h:429-437`).
- `WEAK_CONSTRAINT`는 인용한 `RBL4DVAR`·`R4DVAR`·`SP4DVAR` 등의 조건에서 파생된다 (`ROMS/Include/globaldefs.h:559-576`). CPP 파생과 실행 시 강제약·약제약의 NSA 판정을 구분한다. `CORRELATION` 또는 `WEAK_CONSTRAINT`가 정의된 경로에서 `SP4DVAR`는 `NSA=2`를 설정한다. `SP4DVAR`가 없을 때 `IF (nADJ(ng).lt.ntimes(ng)) THEN`이면 `NSA=2`이다. 이 시간 조건의 ELSE 분기는 `NSA=1`을 설정한다 (`ROMS/Utility/read_phypar.F:4745-4753`; [RT2-395](../../../_staging/recovery/compare/roms-da-representer-vs-code.md#4-노트-대조와-수정안)). [10-14 전수 검증 정정]
- `FOUR_DVAR` — `I4DVAR`/`WEAK_CONSTRAINT`/`TLM_CHECK` 등에서 (`globaldefs.h:582-592`).
- `OBSERVATIONS`(4D-Var 관측 처리) — `I4DVAR`/`R4DVAR`/`VERIFICATION` 등에서 (`globaldefs.h:627-644`).
- `TLM_OBS` — `globaldefs.h:646-659`.
- `BACKGROUND` — `I4DVAR` 정의 시 (`globaldefs.h:594-596`).

**Deprecated 옵션 호환**: 구 이름을 신 이름으로 매핑. `IS4DVAR → I4DVAR`(`globaldefs.h:264-268`), `W4DPSAS → RBL4DVAR`(`globaldefs.h:276-280`), `W4DVAR → R4DVAR`(`globaldefs.h:294-298`).

호환 정의의 도입 판은 `9e75e6e9`이다 ([DA1-816](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md#4-노트-대조와-수정안)). `W4DVAR_SENSITIVITY`를 정의하면 `R4DVAR_ANA_SENSITIVITY`를 정의한다 (`ROMS/Include/globaldefs.h:300-302`; [RT2-396](../../../_staging/recovery/compare/roms-da-representer-vs-code.md#4-노트-대조와-수정안)).

**Split 4D-Var**: `SPLIT_I4DVAR` 등이 있으면 내부 `SPLIT_4DVAR` 정의(`globaldefs.h:310-315`), 그리고 unsplit 짝(`I4DVAR` 등)도 같이 켜 디렉티브 변경 최소화 (`globaldefs.h:322-336`).

기타 물리 파생:
- `BIOLOGY`는 `BIO_FENNEL`·`ECB`·`ECOSIM`·`HYPOXIA_SRM`·`NEMURO`·`NPZD_FRANKS`·`NPZD_IRON`·`NPZD_POWELL`·`RED_TIDE` 중 하나에서 파생된다 (`ROMS/Include/globaldefs.h:817-827`).
- 해빙: `ICE_MODEL` → `SEAICE`, 그리고 `ICE_ADVECT→ICE_SMOLAR`, `ICE_MOMENTUM→ICE_EVP`, `ICE_THERMO→ICE_MK` (`globaldefs.h:799-810`).
- `UV_U3ADV_SPLIT`는 `VISC_3DCOEF`를 정의한다. 이 경로는 `UV_SMAGORINSKY`가 있으면 해제한다 (`ROMS/Include/globaldefs.h:1221-1235`).
- 그 뒤 `#if !defined DIFF_3DCOEF && defined TS_SMAGORINSKY` 조건은 `DIFF_3DCOEF`를 정의한다 (`ROMS/Include/globaldefs.h:1241-1242`).
- `#if !defined VISC_3DCOEF && defined UV_SMAGORINSKY` 조건은 `VISC_3DCOEF`를 정의한다 (`ROMS/Include/globaldefs.h:1244-1245`).
- `VEG_HMIXING`은 별도 조건에서 `VISC_3DCOEF`를 정의한다 (`ROMS/Include/globaldefs.h:1251-1252`).
- 부유 생물 거동: `FLOATS && FLOAT_OYSTER → FLOAT_BIOLOGY` (`globaldefs.h:833-836`).

굴 유생의 성장·탁도·염분 반응·정착은 [sediment-ice-vegetation 보고서의 ROI1·RBO1·ROT1·RCO1-028–RCO1-030](../../../_staging/recovery/compare/roms-sediment-ice-vegetation-vs-code.md#5-차이-결론)을 참조한다. 해석: 염분 반응의 재귀식은 중간 강도의 코드 결함 후보이다 ([RN1-047](../../../_staging/recovery/compare/roms-sediment-ice-vegetation-vs-code.md#4-노트-대조와-수정안)).

### (c) 모순 해소·일관성 강제 (`#undef`)
사용자가 호환 안 되는 조합을 넣으면 globaldefs.h 가 조용히 끈다:
- `SOLVE3D` 정의 시 `COSINE2`(2D 시간평균필터) `#undef` (`globaldefs.h:119-120`).
- 같은 `SOLVE3D` 분기는 `POWER_LAW`를 정의한다 (`ROMS/Include/globaldefs.h:121`).
- `UV_DRAG_GRID`(공간변동 바닥마찰)인데 BBL/SEDIMENT/`UV_*DRAG` 중 아무것도 없으면 `UV_DRAG_GRID` `#undef` (`globaldefs.h:781-788`); 이어 `ANA_DRAG`도 `UV_DRAG_GRID` 없으면 `#undef` (`globaldefs.h:790-793`).
- `UV_U3ADV_SPLIT`(3차 풍상 분할이류) 시 `UV_C4ADVECTION`/`UV_VIS4` 강제 ON, `UV_VIS2`/`UV_SMAGORINSKY` 강제 OFF + `VISC_3DCOEF` (`globaldefs.h:1221-1235`) — cppdefs.h:20-28 의 설명과 짝.
- `ANA_BIOLOGY` 인데 `BIOLOGY` 없으면 `#undef ANA_BIOLOGY` (`globaldefs.h:1070-1072`).

### 강제 강제력: 강제 파일 필요 여부 자동 판단 (`FRC_FILE`)
`SOLVE3D` 하에서 표면/바닥 플럭스를 해석식(`ANA_*`)·결합(`*_COUPLING`)·bulk 로 다 못 채우면 내부 `FRC_FILE`(강제 NetCDF 필요)을 자동 정의하는 대형 OR 블록 (`globaldefs.h:1010-1064`). 예: `BULK_FLUXES` 이면 `ANA_SMFLUX`/`ANA_STFLUX` 를 `#undef`(`globaldefs.h:1011-1018`)하고, 필요한 대기 입력(`LONGWAVE`/`ANA_PAIR`/`ANA_TAIR`/`ANA_WINDS`…) 미충족 시 `FRC_FILE` (`globaldefs.h:1027-1058`).

`FRC_FILE`은 원문의 복합 OR 조건을 적용한다. 외력 파일의 OR 목록은 `SOLVE3D` 분기와 2D 분기를 구분한다. 대기 입력의 여러 항목은 `!FRC_COUPLING` 조건도 포함한다 (`ROMS/Include/globaldefs.h:1019-1064`). 이 조건을 외부 파일 전체의 필요 여부로 넓히지 않는다 ([RBH-3470](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

---

## 4. 앱 헤더(`<app>.h`) 작성 규약 — 예: upwelling.h

사용자 응용 헤더는 그 앱에 필요한 옵션을 단순 `#define`/`#undef` 로 나열한다. `upwelling.h`(default 예제):

- 물리 코어: `UV_ADV`/`UV_COR`/`UV_LDRAG`/`UV_VIS2`(`upwelling.h:15-18`), `DJ_GRADPS`(`:23`), `TS_DIF2`(`:24`), `SALINITY`/`SOLVE3D`(`:29-30`).
- 출력: `upwelling.h`는 `AVERAGES`·`DIAGNOSTICS_TS`·`DIAGNOSTICS_UV`를 정의한다 (`ROMS/Include/upwelling.h:31-33`). 뒤의 `PERFECT_RESTART` 분기는 세 옵션을 해제하고 `OUT_DOUBLE`을 정의한다 (`ROMS/Include/upwelling.h:82-88`). 이 선택은 upwelling 애플리케이션 설정이다 ([OMD-N024·OMD-N025](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안)).
- UPWELLING의 해석 옵션은 선택한 grid·initial·forcing 자료 파일의 읽기를 대체한다 (`ROMS/Include/upwelling.h:35-41`). 물리 입력 파일과 metadata 파일은 별도로 필요하다 ([RT1-1525](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안)). 물리 입력 스크립트는 `ROMS/Utility/inp_par.F:141,143`에서 처리한다. upwelling 헤더의 입력 스크립트 설명은 `ROMS/Include/upwelling.h:12`이다 ([RBH-3471](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

앱 헤더가 **조건부 자기 구성**도 한다 — 난류모형 선택에 따라 분기:
```c
#if defined GLS_MIXING || defined MY25_MIXING
# define KANTHA_CLAYSON
# define N2S2_HORAVG
# define RI_SPLINES
#else
# define ANA_VMIX
#endif
```
(`upwelling.h:43-49`). 생물모형(`BIO_FENNEL` 등) 선택 시 추가 `ANA_*` 플럭스 자동 정의 (`upwelling.h:51-60`), `BIO_FENNEL` 시 `CARBON`/`DENITRIFICATION`/`BIO_SEDIMENT`/`DIAGNOSTICS_BIO` (`upwelling.h:67-72`). `PERFECT_RESTART` 시 출력 옵션 재조정 + `OUT_DOUBLE` (`upwelling.h:82-88`). 즉 globaldefs.h 와 앱 헤더 양쪽에서 파생 로직이 분산돼 있다.

UPWELLING의 `ANA_VMIX` 대입은 `            Akv(i,j,k)=2.0E-03_r8+8.0E-03_r8*EXP(z_w(i,j,k)/150.0_r8)`이다 (`ROMS/Functionals/ana_vmix.h:204`). 선택 조건과 원문은 [testcases 보고서 §3의 RT1-1411](../../../_staging/recovery/compare/roms-testcases-vs-code.md#3-코드에만-있는-처리)을 참조한다 ([RT1-1526 수정안](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안)).

ESTUARY_TEST의 격자 분기는 `Esize=300.0_r8`를 사용한다 (`ROMS/Functionals/ana_grid.h:282`). `SOLVE3D`·`SALINITY`의 nonlinear 초기장 분기는 `IF (xr(i,j).le.30000.0_r8) then`에서 염분 30을 대입한다 (`ROMS/Functionals/ana_initial.h:661-662`). SED_TOY의 `SEDIMENT` bed 초기화는 각 층에 0.01 m를 대입한다 (`ROMS/Functionals/ana_sediment.h:331`). LAKE_SIGNELL의 `SOLVE3D` nonlinear 초기 수온은 10이다 (`ROMS/Functionals/ana_initial.h:720`). `SALINITY`가 있으면 염분은 30이다 (`ROMS/Functionals/ana_initial.h:721-722`). 각 값은 해당 ANA 함수가 선택되고 인용한 호출·분기 조건을 충족할 때 대입한다 ([RT1-1536](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안)).

다른 헤더 규모: `wc13.h`(174행, 4D-Var 현실 응용), `double_gyre.h`(가장 큰 이상화 예, 8.8KB)가 옵션을 가장 많이 묶고, `soliton.h`/`windbasin.h` 등은 수십 줄짜리 최소 구성.

---

## 5. 타일 경계 매크로 — set_bounds.h / set_bounds_xtr.h / tile.h

이들은 옵션 토글이 아니라 **MPI/OpenMP 타일 분할 인덱스를 서브루틴 안에 inline 주입**하는 헤더다. 거의 모든 계산 커널 F 파일이 시작부에서 include 한다.

### tile.h — private 작업배열 경계
자동 private 저장배열의 경계는 `BOUNDS(ng)%...(tile)`에서 가져온다 (`ROMS/Include/tile.h:9-38`). `NESTING`의 private work 하한은 `Istr-4`·`Jstr-4`이다. 다른 분기의 하한은 `Istr-3`·`Jstr-3`이다 (`ROMS/Include/tile.h:15-25`). MPI 통신 halo 폭은 `NghostPoints`가 정한다 ([RCN-1982](../../../_staging/recovery/compare/roms-coupling-nesting-parallel-vs-code.md#4-노트-대조와-수정안)).

```c
#ifdef NESTING
      IminS=BOUNDS(ng)%Istr(tile)-4
      ImaxS=BOUNDS(ng)%Iend(tile)+3
      JminS=BOUNDS(ng)%Jstr(tile)-4
      JmaxS=BOUNDS(ng)%Jend(tile)+3
#else
      IminS=BOUNDS(ng)%Istr(tile)-3
      ImaxS=BOUNDS(ng)%Iend(tile)+3
      JminS=BOUNDS(ng)%Jstr(tile)-3
      JmaxS=BOUNDS(ng)%Jend(tile)+3
#endif
```

### set_bounds.h — staggered 변수 경계 인덱스 일괄 주입
RHO/U/V/PSI 등 staggered 위치별 타일 경계(`Istr`,`IstrU`,`IstrR`,`IstrB`,`IstrP`,`IstrM`,`IstrT` 와 J 짝)를 모두 선언·대입한다 (`set_bounds.h:21-54`). 추가로 가장자리 오프셋 인덱스(`Istrm3`=Istr-3, `IstrUm2`=IstrU-2, `Iendp2i`=Iend+2 내부, … 주석 친절) (`set_bounds.h:56-74`). 값의 출처:

> `** The lower and upper bounds are allocated and assigned in "inp_par.F"`
> `** by calling "get_tile" which is located in the "get_bounds.F" file.` — `set_bounds.h:9-10`

> `**  ...  Notice that if tile=-1, it will set the values for the global grid.` — `set_bounds.h:17-18`

### set_bounds_xtr.h — 확장(extra) 타일 변형
구조는 set_bounds.h 와 동일하나 출처가 `xtr_BOUNDS(ng)%...` (`set_bounds_xtr.h:30`) — 확장 고스트/오버랩 영역용 별도 경계 세트.

---

## 6. 요약: 옵션 선택 메커니즘 흐름

```
makefile: ROMS_APPLICATION ?= UPWELLING
        → -DROMS_HEADER="upwelling.h"
cppdefs.h
   ├ (주석) CPP 옵션 설명 카탈로그
   ├ #include ROMS_HEADER  → upwelling.h  (사용자 옵션 #define)   cppdefs.h:754
   └ #include "globaldefs.h"                                       cppdefs.h:763
globaldefs.h
   ├ 플랫폼/MPI 내부 스위치 (DISTRIBUTE 등)
   ├ 상위옵션 → 하위 내부스위치 파생 (TANGENT/ADJOINT/BIOLOGY/SEAICE/FRC_FILE…)
   ├ deprecated 매핑 (IS4DVAR→I4DVAR…)
   └ 모순 옵션 #undef (일관성 강제)
[컴파일] 각 .F 커널 → #include "set_bounds.h"/"tile.h" 로 타일 경계 주입
```

기능 판정에는 응용 헤더·globaldefs의 파생 규칙과 실제 소비 커널을 함께 사용한다. `checkdefs`의 오류 검사와 `read_phypar`의 실행 시 입력도 판정 근거이다 ([RBH-3475](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

---

## 관련 노트
- [roms_main_driver_dispatch](roms_main_driver_dispatch.md) — `SOLVE3D`/4D-Var 드라이버 옵션이 분기하는 main 디스패치
- [roms_4dvar](roms_4dvar.md) — `I4DVAR`/`RBL4DVAR`/`R4DVAR` 등 globaldefs.h 가 파생하는 동화 모드 본체
- [roms_grid_metrics](roms_grid_metrics.md) — `BOUNDS(ng)%...` 타일 경계 구조체의 실제 할당
- [roms_nesting](roms_nesting.md) — NESTING의 private work 하한과 MPI 통신 halo 폭의 대조

## 문서와 코드 차이 (10-14 대조)

문서 판은 ROMS 위키 wikitext(2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json))이다. 코드 판은 원본 저장소 HEAD `57aecf58`(2026-09-18, roms-4.2 이후 4.3 개발)이다.

차이 행은 [roms_include_cppdefs-differences-1.md](roms_include_cppdefs-differences-1.md), [roms_include_cppdefs-differences-2.md](roms_include_cppdefs-differences-2.md), [roms_include_cppdefs-differences-3.md](roms_include_cppdefs-differences-3.md)에 있다.

결론별 개수: A 56개, B 34개, C 533개, D 0개, E 20개, F 46개, 합계 689개 ([배정표 모음](../../../_staging/recovery/assign/)의 `ROMS-assign-*.tsv`에서 3열이 `source-analysis/roms_include_cppdefs.md`인 행을 셈).

---
title: "ROMS Include — cppdefs·globaldefs·전처리 옵션 체계"
model: ROMS
component: ROMS/Include
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Include/). cppdefs.h(옵션 카탈로그·ROMS_HEADER include), globaldefs.h(내부 파생 매크로·일관성 체크·error), set_bounds.h/set_bounds_xtr.h/tile.h(타일 경계 매크로), upwelling.h(앱 헤더 예시) file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/README.md
---

# ROMS Include — cppdefs·globaldefs·전처리 옵션 체계

> ROMS 빌드 시 물리·수치 기능을 켜고 끄는 C-preprocessor(CPP) 옵션 계층의 본체. (경로: roms/ROMS/Include/)

ROMS는 컴파일 타임에 `#define` CPP 매크로로 기능을 토글하는 **단일 빌드 = 단일 구성** 모델이다. `Include/`는 그 옵션 체계의 심장으로, 세 종류 파일로 구성된다.

| 파일군 | 역할 | 대표 |
|---|---|---|
| `cppdefs.h` | 전 옵션 카탈로그(문서) + 앱 헤더 include 디스패치 | cppdefs.h |
| `globaldefs.h` | 사용자 옵션 → **내부 파생 매크로** 자동 유도 + 일관성 체크/error | globaldefs.h |
| `<app>.h` (37개) | 응용별 옵션 묶음(사용자 선택) | upwelling.h, wc13.h, double_gyre.h … |
| `set_bounds*.h`, `tile.h` | 타일 경계 인덱스 헤더(F 파일에 inline include) | set_bounds.h, tile.h |

---

## 1. 빌드 디스패치 메커니즘 — cppdefs.h

`cppdefs.h`는 앞부분 전체(1~749행)가 **사용 가능한 모든 CPP 옵션의 짧은 설명**을 담은 주석 카탈로그다. 헤더 자체가 그렇게 선언한다:

> `** The following is short description of all available CPP options.` — `cppdefs.h:11`

파일 끝에서 실제 디스패치가 일어난다. 사용자가 makefile에 지정한 `ROMS_APPLICATION` 값에 따라 C-preprocessor 가 `ROMS_HEADER` 정의(소문자 + `.h`)를 넘기고, cppdefs.h 가 그 헤더를 include 한다:

```c
#if defined ROMS_HEADER
# include ROMS_HEADER          // cppdefs.h:751-752
#else
   CPPDEFS - Choose an appropriate ROMS application.   // 미정의 시 컴파일 에러 유발
#endif
...
#include "globaldefs.h"        // cppdefs.h:761
```

(`cppdefs.h:751`, `cppdefs.h:752`, `cppdefs.h:755`, `cppdefs.h:761`). 헤더 카탈로그에 그 흐름이 명시돼 있다:

> `**    ROMS_HEADER="upwelling.h"` — `cppdefs.h:742`
> `**  in the makefile. ROMS will include the associated header file located` — `cppdefs.h:737`

따라서 **빌드 순서**는: makefile `ROMS_APPLICATION ?= UPWELLING` (`cppdefs.h:734`) → `ROMS_HEADER="upwelling.h"` → cppdefs.h 가 `upwelling.h` include(사용자 옵션 set) → 이어서 `globaldefs.h` include(내부 파생 + 검증).

### 사전 정의 응용(pre-defined applications)
cppdefs.h:680~713 이 동봉 예제 목록을 분류한다 — Idealized Test Problems(`cppdefs.h:680`)에 `BASIN`(`cppdefs.h:682`), `BENCHMARK`(`cppdefs.h:683`), `DOUBLE_GYRE`(`cppdefs.h:691`), `UPWELLING`(default, `cppdefs.h:711`), `WEDDELL`(`cppdefs.h:712`), `WINDBASIN`(`cppdefs.h:713`); Climatological 에 `DAMEE_4`; Realistic 에 `ADRIA02`, `NJ_BIGHT`, `WC13`(California Current, `wc13.h`). 각 `<app>.h`가 Include/ 에 있다(총 37개 헤더 파일).

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

⚠ `UV_SADVECTION`(스플라인 수직이류) 경고: 이상화·고해상도에만 사용 — `cppdefs.h:30-31`.

---

## 3. 내부 파생 매크로 — globaldefs.h (핵심 메커닉)

`globaldefs.h`는 사용자가 직접 만지면 안 되는 **자동 유도 정의** 모음이다. 헤더가 명시:

> `** WARNING: This  file  contains  a set of  predetermined macro definitions` — `globaldefs.h:11`
> `** It is strongly recommended to NOT modify any of the definitions below.` — `globaldefs.h:13`

작동 패턴은 세 가지: (a) 플랫폼/MPI 내부 스위치, (b) 사용자 상위 옵션 → 다수 하위 내부 스위치 파생, (c) 모순 옵션 자동 `#undef`(일관성 강제).

### (a) 플랫폼·병렬 내부 스위치
- `MPI` 정의 시 내부 `DISTRIBUTE` 자동 정의(`globaldefs.h:46-48`) — 분산메모리 코드 경로 전체의 게이트.
- MPI 통신 디폴트: `mp_boundary`/`mp_collect`/`mp_reduce` 가 사용자가 명시 안 하면 `*_ALLREDUCE` 변형을 기본 선택 (`globaldefs.h:57-63`, `71-76`, `85-91`, `100-106`) — "더 효율적"이 이유로 주석에 적힘(`globaldefs.h:53`).
- `#define PROFILE` 무조건 — 시간 프로파일링 ON (`globaldefs.h:112`).

### (b) 상위 → 하위 파생 (대표: 4D-Var / adjoint)
ROMS 4D-Var 동화의 거대한 OR 블록이 백미다. 수십 개 드라이버 옵션 중 **하나라도** 켜지면 내부 `TANGENT` / `ADJOINT` 가 정의된다:

```c
#if defined ARRAY_MODES || defined I4DVAR || defined RBL4DVAR ||
    defined R4DVAR || defined SP4DVAR || ... (수십 개)
# define TANGENT          // globaldefs.h:392
#endif
#if defined AD_SENSITIVITY || ... || defined TL_R4DVAR
# define ADJOINT          // globaldefs.h:426
#endif
```

(`globaldefs.h:361-393`, `globaldefs.h:395-427`). 유사하게:
- `TL_IOMS`(접선선형의 표현자 모드) — `ARRAY_MODES`/`R4DVAR` 등에서 파생 (`globaldefs.h:429-437`).
- `WEAK_CONSTRAINT` — `RBL4DVAR`/`R4DVAR`/`SP4DVAR` 등 약제약 4D-Var 류에서 파생 (`globaldefs.h:560-576`).
- `FOUR_DVAR` — `I4DVAR`/`WEAK_CONSTRAINT`/`TLM_CHECK` 등에서 (`globaldefs.h:582-592`).
- `OBSERVATIONS`(4D-Var 관측 처리) — `I4DVAR`/`R4DVAR`/`VERIFICATION` 등에서 (`globaldefs.h:627-644`).
- `TLM_OBS` — `globaldefs.h:646-659`.
- `BACKGROUND` — `I4DVAR` 정의 시 (`globaldefs.h:594-596`).

**Deprecated 옵션 호환**: 구 이름을 신 이름으로 매핑. `IS4DVAR → I4DVAR`(`globaldefs.h:264-268`), `W4DPSAS → RBL4DVAR`(`globaldefs.h:276-280`), `W4DVAR → R4DVAR`(`globaldefs.h:294-298`).

**Split 4D-Var**: `SPLIT_I4DVAR` 등이 있으면 내부 `SPLIT_4DVAR` 정의(`globaldefs.h:310-315`), 그리고 unsplit 짝(`I4DVAR` 등)도 같이 켜 디렉티브 변경 최소화 (`globaldefs.h:322-336`).

기타 물리 파생:
- 생물(biology): `BIO_FENNEL`/`ECOSIM`/`NEMURO`/`NPZD_*`/`RED_TIDE` 중 하나 → 내부 `BIOLOGY` (`globaldefs.h:801-811`).
- 해빙: `ICE_MODEL` → `SEAICE`, 그리고 `ICE_ADVECT→ICE_SMOLAR`, `ICE_MOMENTUM→ICE_EVP`, `ICE_THERMO→ICE_MK` (`globaldefs.h:783-794`).
- 점성 3D 계수: `UV_SMAGORINSKY`/`TS_SMAGORINSKY`/`VEG_HMIXING` → `VISC_3DCOEF`/`DIFF_3DCOEF` (`globaldefs.h:1225-1237`).
- 부유 생물 거동: `FLOATS && FLOAT_OYSTER → FLOAT_BIOLOGY` (`globaldefs.h:817-820`).

### (c) 모순 해소·일관성 강제 (`#undef`)
사용자가 호환 안 되는 조합을 넣으면 globaldefs.h 가 조용히 끈다:
- `SOLVE3D` 정의 시 `COSINE2`(2D 시간평균필터) `#undef` (`globaldefs.h:119-120`).
- `UV_DRAG_GRID`(공간변동 바닥마찰)인데 BBL/SEDIMENT/`UV_*DRAG` 중 아무것도 없으면 `UV_DRAG_GRID` `#undef` (`globaldefs.h:765-772`); 이어 `ANA_DRAG`도 `UV_DRAG_GRID` 없으면 `#undef` (`globaldefs.h:774-777`).
- `UV_U3ADV_SPLIT`(3차 풍상 분할이류) 시 `UV_C4ADVECTION`/`UV_VIS4` 강제 ON, `UV_VIS2`/`UV_SMAGORINSKY` 강제 OFF + `VISC_3DCOEF` (`globaldefs.h:1205-1219`) — cppdefs.h:20-28 의 설명과 짝.
- `ANA_BIOLOGY` 인데 `BIOLOGY` 없으면 `#undef ANA_BIOLOGY` (`globaldefs.h:1054-1056`).

### 강제 강제력: 강제 파일 필요 여부 자동 판단 (`FRC_FILE`)
`SOLVE3D` 하에서 표면/바닥 플럭스를 해석식(`ANA_*`)·결합(`*_COUPLING`)·bulk 로 다 못 채우면 내부 `FRC_FILE`(강제 NetCDF 필요)을 자동 정의하는 대형 OR 블록 (`globaldefs.h:994-1048`). 예: `BULK_FLUXES` 이면 `ANA_SMFLUX`/`ANA_STFLUX` 를 `#undef`(`globaldefs.h:995-1002`)하고, 필요한 대기 입력(`LONGWAVE`/`ANA_PAIR`/`ANA_TAIR`/`ANA_WINDS`…) 미충족 시 `FRC_FILE` (`globaldefs.h:1011-1042`).

---

## 4. 앱 헤더(`<app>.h`) 작성 규약 — 예: upwelling.h

사용자 응용 헤더는 그 앱에 필요한 옵션을 단순 `#define`/`#undef` 로 나열한다. `upwelling.h`(default 예제):

- 물리 코어: `UV_ADV`/`UV_COR`/`UV_LDRAG`/`UV_VIS2`(`upwelling.h:15-18`), `DJ_GRADPS`(`:23`), `TS_DIF2`(`:24`), `SALINITY`/`SOLVE3D`(`:29-30`).
- 출력: `AVERAGES`(`:31`), `DIAGNOSTICS_TS`/`DIAGNOSTICS_UV`(`:32-33`).
- 해석식 강제(이상화 → 외부파일 불필요): `ANA_GRID`/`ANA_INITIAL`/`ANA_SMFLUX`/`ANA_STFLUX`/… (`upwelling.h:35-41`).

앱 헤더가 **조건부 자기 구성**도 한다 — 난류모형 선택에 따라 분기:
```c
#if defined GLS_MIXING || defined MY25_MIXING
# define KANTHA_CLAYSON      // upwelling.h:44
# define N2S2_HORAVG / RI_SPLINES
#else
# define ANA_VMIX            // upwelling.h:48  (해석 수직혼합)
#endif
```
(`upwelling.h:43-49`). 생물모형(`BIO_FENNEL` 등) 선택 시 추가 `ANA_*` 플럭스 자동 정의 (`upwelling.h:51-60`), `BIO_FENNEL` 시 `CARBON`/`DENITRIFICATION`/`BIO_SEDIMENT`/`DIAGNOSTICS_BIO` (`upwelling.h:67-72`). `PERFECT_RESTART` 시 출력 옵션 재조정 + `OUT_DOUBLE` (`upwelling.h:82-88`). 즉 globaldefs.h 와 앱 헤더 양쪽에서 파생 로직이 분산돼 있다.

다른 헤더 규모: `wc13.h`(174행, 4D-Var 현실 응용), `double_gyre.h`(가장 큰 이상화 예, 8.8KB)가 옵션을 가장 많이 묶고, `soliton.h`/`windbasin.h` 등은 수십 줄짜리 최소 구성.

---

## 5. 타일 경계 매크로 — set_bounds.h / set_bounds_xtr.h / tile.h

이들은 옵션 토글이 아니라 **MPI/OpenMP 타일 분할 인덱스를 서브루틴 안에 inline 주입**하는 헤더다. 거의 모든 계산 커널 F 파일이 시작부에서 include 한다.

### tile.h — private 작업배열 경계
자동 private 저장배열의 수평 시작/끝 인덱스(`IminS`,`ImaxS`,`JminS`,`JmaxS`)와 배열 상하한(`LBi`,`UBi`,…)을 `BOUNDS(ng)%...(tile)` 에서 뽑아 로컬 변수로 설정 (`tile.h:9-38`). NESTING 여부로 고스트폭이 다르다 — 둥지격자면 `Istr-4`까지, 아니면 `Istr-3` (`tile.h:15-25`):

```c
#ifdef NESTING
      IminS=BOUNDS(ng)%Istr(tile)-4   // tile.h:16
#else
      IminS=BOUNDS(ng)%Istr(tile)-3   // tile.h:21
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
   ├ (주석) 전 옵션 카탈로그 1~749
   ├ #include ROMS_HEADER  → upwelling.h  (사용자 옵션 #define)   cppdefs.h:752
   └ #include "globaldefs.h"                                       cppdefs.h:761
globaldefs.h
   ├ 플랫폼/MPI 내부 스위치 (DISTRIBUTE 등)
   ├ 상위옵션 → 하위 내부스위치 파생 (TANGENT/ADJOINT/BIOLOGY/SEAICE/FRC_FILE…)
   ├ deprecated 매핑 (IS4DVAR→I4DVAR…)
   └ 모순 옵션 #undef (일관성 강제)
[컴파일] 각 .F 커널 → #include "set_bounds.h"/"tile.h" 로 타일 경계 주입
```

ROMS 옵션 체계의 본질: **사용자는 앱 헤더에서 최소 의도만 선언하고, globaldefs.h 가 나머지 내부 스위치를 파생·정합화한다.** 이 때문에 어떤 기능이 켜졌는지 추적하려면 cppdefs.h 카탈로그(문서)와 globaldefs.h(파생 규칙)를 함께 봐야 한다.

---

## 관련 노트
- [[roms_main_driver_dispatch]] — `SOLVE3D`/4D-Var 드라이버 옵션이 분기하는 main 디스패치
- [[roms_4dvar]] — `I4DVAR`/`RBL4DVAR`/`R4DVAR` 등 globaldefs.h 가 파생하는 동화 모드 본체
- [[roms_grid_metrics]] — `BOUNDS(ng)%...` 타일 경계 구조체의 실제 할당
- [[roms_nesting]] — `NESTING` 매크로가 tile.h 고스트폭을 바꾸는 맥락

# ROMS Phase 1 의미 검토

검토일: 2026-09-20. 계약: `phase1-task.md`의 후보 8건 + 추가 조사 A/B. 위키 문장 수정안은 포함하지 않는다.

## 요약

- **후보 8건: UPDATE_REQUIRED 2, REVIEW_ONLY 6, NO_ACTION 0, UNRESOLVED 0.** 개별 근거는 `phase1-codex.csv`에 기록했다.
- **R1-3**: `BOTTOM_ALBEDO`의 온도 tracer에서 표면·바닥 FC에 단파 보정항이 생겨, 조건 없이 적힌 기존 등식이 성립하지 않는다. `BEHAVIOR_CHANGE`.
- **R1-7**: `Vinfo(25)`가 `Vinfo(Natt)`/`Natt=26`으로 확장되고 `range` 속성을 실제 기록한다. `INTERFACE_CHANGE`.
- 나머지 6건은 해당 문장의 주장이 유지된다. 코드 변경이 없다는 뜻이 아니며, broad 인용 내부의 변경만으로 UPDATE_REQUIRED를 부여하지 않았다.
- **A**: 기존 본문을 분리한 신규 파일이 있다. mono convolution은 기존 구현에서 파생된 분리·정리이고, multi convolution은 공통 흐름에 새 scale 루프·implicit 연산·가중합을 추가한 구현이다. `get_state`의 요청된 8개 헤더는 기존 상태 분기 본문에서 추적된다.
- **B**: `roms_4dvar.md` 전체 427줄을 읽었다. 기존 비용함수·outer/inner loop·최소화 호출 경로는 유지되지만, §I/J의 일부 파일 매핑·반복 횟수·입력 단위·구현 상태 설명은 새 소스와 불일치한다. 노트 전체를 REVIEW_ONLY로 일괄 처리할 수 없다. 확인되지 않은 호환성·역사·수치 주장들은 아래 UNRESOLVED로 분리했다.

## 비교 기준과 판정 해석

| 항목 | 값 |
|---|---|
| old | `32c79b7435ee0a1a2cdd78fee07264e3bd93bb98` |
| new | `57aecf589a408b1e5490d2db7f9bd0196062a44e` |
| 비교 저장소 | `/home/firesinger/.cache/coastal-snapshots/roms-upstream` |
| 입력 | `_staging/roms-prescan/phase1-candidates.csv`, 8행 |
| 비교 규모 | `git diff --name-status`로 193파일, A=35/M=158 확인; 범위 안 6커밋 |

이 문서에서 **old/new의 소스 좌표는 위 커밋의 repo 상대 경로**다. 위키 좌표는 `models/ROMS/` 아래 현재 노트의 줄 번호다. 현재 snapshot HEAD는 new와 같고 시작 시 작업트리 변경은 없었다. 후보 소스 5개 경로, `User/Functionals/ana_initial.h`, `i4dvar.F`의 pinned raw 파일을 비교했으며, 이 7개 경로 모두 old git blob과 byte 일치했다.

CSV의 `semantic_meaning_changed`는 **인용이 뒷받침하던 문장이 새 판본에도 성립하는지**를 뜻한다. FALSE는 파일 전체의 실행 동작이 불변이라는 뜻이 아니다. UPDATE_REQUIRED만 계약에 정해진 `reason_type`을 부여하고 나머지는 비웠다. 후보 CSV에서 끝이 잘린 `wiki_claim`은 해당 노트 실제 줄 전체를 읽어 기록했다. 좌표 치환이나 위키 편집은 수행하지 않았다.

검토는 로컬 git의 양쪽 blob·diff·호출부·선언부를 이용했다. 컴파일·수치 실험이나 외부 PDF/웹 자료 재검증은 수행하지 않았고, 그 증거가 필요한 주장은 통과로 처리하지 않았다.

## 후보 8건

| ID | 판정 | 문장 수준 판단 |
|---|---|---|
| R1-1 | REVIEW_ONLY | public wrapper, `tile.h`, GRID/OCEAN 인자와 tile 호출 구조 유지. 추가 내용은 Master의 kernel 출력. 인용 대상은 아래 증거로 식별. |
| R1-2 | REVIEW_ONLY | `pre_step3d.F`가 shortwave penetration을 처리한다는 Source basis 설명은 유지. 반사광 처리 추가는 그 역할과 충돌하지 않음. |
| R1-3 | UPDATE_REQUIRED | new `ROMS/Nonlinear/pre_step3d.F:966-979`: `BOTTOM_ALBEDO && itrc.eq.itemp`일 때 FC의 두 경계값에 `dt*srflx*swdk` 추가. |
| R1-4 | REVIEW_ONLY | new `ROMS/Nonlinear/pre_step3d.F:964-1000`: 경계 FC 설정 → `FC(k)-FC(k-1)` → tracer 갱신이라는 적용 경로 유지. R1-3의 등식 주장과 구별. |
| R1-5 | REVIEW_ONLY | new `ROMS/Modules/mod_ocean.F:297-320`의 FOUR_DVAR 조건 추가는 작업 배열 가용성을 확대. T_OCEAN/OCEAN이 핵심 상태를 보관한다는 주장 유지. |
| R1-6 | REVIEW_ONLY | new `ROMS/Utility/read_phypar.F:976-977`의 BOT_ALBEDO 입력은 NtileI/J 읽기·검사와 무관. 해당 코드 유지. |
| R1-7 | UPDATE_REQUIRED | new `ROMS/Utility/def_var.F:127,1147`, `ROMS/Modules/mod_ncparam.F:114`: Vinfo 인자 용량 26. `def_var.F:997-1013,2026-2042`에 range 기록 구현. |
| R1-8 | REVIEW_ONLY | 주요 계산 블록을 열거한 문장. swdk/중간 tracer/이류/연속방정식/FC/새 tracer/운동량 블록 유지. 각 블록의 세부 계산식 불변을 단언한 문장이 아님. |

R1-3의 이전 등식은 옵션 비활성 분기와 비온도 tracer에 여전히 성립한다(new `ROMS/Nonlinear/pre_step3d.F:981-992`). 영향은 #77 `acfb0667`의 선택적 동작이다. #75 때문에 ROMS 전체 플럭스 경로가 바뀐 것으로 해석하지 않는다.

### R1-1: AMBIGUOUS_SAME_MODEL 해소 근거

대상은 **`ROMS/Functionals/ana_initial.h`**로 판단한다. 이름이 같거나 public NLM 블록이 닮았다는 이유로 고르지 않았다.

1. `source-analysis/roms_analytical_functionals.md:4,7,17`은 component 및 직접 읽은 경로를 `ROMS/Functionals`로 명시한다.
2. 같은 노트 `:28-29`는 `User/Functionals`를 별도 사용자 템플릿으로 구별한다.
3. 같은 노트 `:36-38`은 `ana_initial.h`의 NLM/TLM/RPM/ADM별 분기와 `#ifdef TANGENT`를 설명한다. old 공식 파일 `:54-84`에 TLM/RPM·ADM 분기가 있다. old User 파일은 `:32-53`에서 NLM 분기만 수행하고 종료한다.
4. old 공식 파일은 1121줄, User 파일은 256줄로 서로 다르다. 공식 파일 old `:31-53`의 래퍼 구조는 new `:33-59`에 유지된다. new `:35-37`은 `IF (Master)`와 `WRITE(stdout,10) KernelString(model)` 추가다.

노트의 기존 세부 좌표에는 오차가 있지만 위 경로·분기 증거를 없애지는 않는다. 예를 들어 노트 `:58`의 `ANANAME(2)`는 old 공식 파일 `:95`의 `ANANAME(10)`과 다르다. 이는 이번 hunk로 생긴 의미 변경이 아니며 별도 CSV 후보로 추가하지 않았다.

## A. NEW FILE RULE

### A-1. convolution: 분리된 기존 경로와 추가된 multi 경로

| 신규 파일 (new) | 기존 구현의 출처 (old) | 새 좌표·성격 |
|---|---|---|
| `ROMS/Utility/convolve_mono.h` | `ROMS/Utility/convolve.F:115-209` convolve, `:212-802` error_covariance, `:807-906` saddlec | 각각 `:124-222`, `:225-821`, `:826-925`로 이동·정리. 예: old `:199-719` ↔ new `:212-732`는 공백 정규화 후 같은 521줄. |
| `ROMS/Utility/convolve_multi.h` | 같은 old convolve/error_covariance/saddlec 흐름 | 각각 `:132-253`, `:256-898`, `:903-1026`. `:186-238`에 Nscale 루프, ns 인자, sum_multi_B 추가. 단순 이동만으로 설명할 수 없음. |
| `ROMS/Adjoint/ad_convolution_mono.h` | `ROMS/Adjoint/ad_convolution.F:83-204` wrapper, `:207-1610` tile | new `:121-196`, `:199-1638`. 예: old `:881`의 ad_conv_r2d_tile 호출은 new `:791`; iADM 상수를 tile의 model 인자로 일반화하는 등 정리도 있음. |
| `ROMS/Adjoint/ad_convolution_multi.h` | 위 ADM convolution의 변수·정규화·경계 처리 골격에서 파생 | wrapper `:139-216`, tile `:219-1574`. `:139,149`에서 ns 필수 인자; `:842-951`의 type-bound CI/vertical diffusion 호출로 implicit 경로 구현. |
| `ROMS/Tangent/tl_convolution_mono.h` | `ROMS/Tangent/tl_convolution.F:84-206` wrapper, `:209-1614` tile | new `:121-196`, `:199-1630`. 예: old `:927`의 tl_conv_r2d_tile 호출은 new `:839`. |
| `ROMS/Tangent/tl_convolution_multi.h` | 위 TLM convolution 골격에서 파생 | wrapper `:139-216`, tile `:219-1576`. `:897-978`에 CI 및 별도 implicit vertical diffusion 경로. 단순 파일명 변경이 아님. |

분리 후 기존 `.F`는 없어지지 않는다. new `ROMS/Utility/convolve.F:91-95`, `ROMS/Adjoint/ad_convolution.F:95-99`, `ROMS/Tangent/tl_convolution.F:95-99`가 `MULTI_SCALE_B` 유무에 따라 `*_multi.h`/`*_mono.h`를 include한다. 따라서 `.F`의 신규파일 판정만 보거나 `.F` 본문 삭제를 기능 삭제로 간주하면 의미 검토를 놓친다. mono 구현도 정리·인터페이스 내부 변경이 있으므로 byte 동일 이동이라고 단정하지 않는다.

### A-2. get_state: 기존 상태 분기를 헤더로 추출

아래 old 범위는 모두 **`ROMS/Utility/get_state.F`의 해당 IF 분기 전체**다. new 본문 범위는 **`ROMS/Utility/get_state_<mode>_<backend>.h`**에서 라이선스·설명 헤더 이후 구간이다. 마지막 열은 new `get_state.F`의 실제 include 줄이다.

| mode | old nf90 분기 → new nf90 본문 | old pio 분기 → new pio 본문 | new include (nf90 / pio) |
|---|---|---|---|
| **nlm** | 516-2493 → 19-1994 | 8286-10611 → 19-2341 | 517 / 1031 |
| **adm** | 3681-4840 → 19-1177 | 11982-13325 → 19-1360 | 539 / 1053 |
| **generic** | 6350-6671 → 20-339 | 15015-15390 → 20-393 | 578 / 1092 |
| **frc** | 6680-7014 → 19-351 | 15399-15787 → 19-405 | 589 / 1103 |
| tlm | 2502-3672 → 20-1187 | 10620-11973 → 20-1370 | 528 / 1042 |
| nrm | 4849-5526 → 19-691 | 13334-14092 → 19-772 | 553 / 1067 |
| std | 5535-6341 → 19-820 | 14101-15006 → 19-919 | 567 / 1081 |
| tlm_forcing | 7029-7530 → 20-519 | 15802-16378 → 20-594 | 606 / 1120 |
| tcs | 7540-7875 → 20-353 | 16388-16777 → 20-407 | 618 / 1132 |

굵게 표시한 4개 mode가 계약에서 지정한 8개 헤더에 해당한다.

요청된 8개 헤더의 nf90/PIO 읽기 호출과 대상 배열을 기존 본문과 대조했다. 7개는 공백·Fortran 주석을 제외한 줄 목록이 일치했고, `nlm_nf90`의 남은 차이도 `netcdf_get_ivar` / `FoundError` 인자를 어느 위치에서 다음 줄로 나누는지에 있었다. 새 헤더 설명은 NLM→일반 상태, ADM→ad_ 배열, GENERIC→d_ 배열, FRC→f_ 배열에 대응한다. 실제 신규 get_state 헤더 수는 **9 mode × 2 backend = 18**이다.

### A-3. 기존 파일의 위키 인용 여부

검색 범위는 계약 안의 `models/ROMS/**/*.md`이며 raw는 제외했다. 다른 모델·concepts 전체의 인용 유무로 일반화하지 않는다.

| 기존 파일 | 실제 발견한 인용·언급 | 영향 |
|---|---|---|
| `get_state.F` | `source-analysis/roms_io_netcdf.md:166`의 `get_state.F:11-12`; `web-refs/roms-official-resources.md:166`의 refactor 설명 | 초기조건 등 요청 상태를 NetCDF에서 읽는다는 역할 주장은 유지. old/new `get_state.F:11-12,92-160` 및 new include 분기로 확인. 분리 자체를 UPDATE_REQUIRED로 올릴 근거 없음. web-ref의 16개라는 숫자는 실제 18개와 불일치. |
| `convolve.F` | `web-refs/roms-official-resources.md:161` | 해당 web-ref는 이미 mono/multi 분리를 기술한다. source-analysis에서 이 정확한 파일명의 직접 인용은 발견하지 못함. |
| `ad_convolution.F` | `web-refs/roms-official-resources.md:159` | 분리가 이미 언급됨. `source-analysis/roms_4dvar.md:51,53`은 파일명 직접 인용 대신 i4dvar.F를 통해 같은 루틴을 설명하므로 B에서 별도 검토. |
| `tl_convolution.F` | `source-analysis/roms_tangent_linear_model.md:198`; `web-refs/roms-official-resources.md:160` | tangent 디렉터리에 convolution 모듈이 있다는 설명 유지. 4dvar 노트 `:52-53`의 간접 호출 근거는 B에서 검토. |

## B. roms_4dvar.md 전체 영향

### B-1. 유지되는 알고리즘 주장

| 노트 부분 | 판정과 실제 소스 근거 |
|---|---|
| §A/C, `:26-38,65-81`: family·outer loop·TL/AD 실행 | **REVIEW_ONLY**. `i4dvar_roms.h`, `rbl4dvar_roms.h`, `r4dvar_roms.h`, `tl_r4dvar_roms.h`는 old/new blob 동일. `ROMS/Drivers/i4dvar_roms.h:292-317`의 background→increment→analysis 유지. i4dvar.F old `:551-2482`는 new `:562-2493`, rbl4dvar.F old `:400-2813`는 new `:411-2824`와 byte 동일인 대응 블록으로 확인. |
| §B, `:42-46`: Jb+Jo, background 비용과 innovation | **REVIEW_ONLY**. new `ROMS/Drivers/i4dvar.F:1475-1493,1529-1555`에서 back_cost·Jb/Jo 보고 유지. old `:1464-1482,1518-1544`와 동일. `ROMS/Adjoint/ad_misfit.F:194-196`의 `ObsErr*(NLmodVal+TLmodVal-ObsVal)`도 동일. |
| §B, `:51-52`: model/minimization 공간 변환 순서 | **기존 mono 경로에 대해 REVIEW_ONLY**. old i4dvar.F `:1412-1433,1619-1637` ↔ new `:1423-1444,1630-1648` 동일. ad_variability→ad_convolution, tl_convolution→tl_variability(+tl_balance) 호출 순서 유지. multi와의 무조건적 호환은 아래 별도 문제. |
| §B, `:57-63`: R/Cobs 및 최소화 solver | **REVIEW_ONLY**. new i4dvar.F `:1524` cgradient; rbl4dvar.F `:1354,1364,1595` rpcg_lanczos/congrad; r4dvar.F `:1013,1259` congrad. cgradient.F/congrad.F/rpcg_lanczos.F 및 ad_congrad.F/ad_rpcg_lanczos.F blob은 old/new 동일. |
| §D/F: observation, reverse-time AD 및 TL/AD main kernel | **REVIEW_ONLY**인 기존 경로. ad_misfit.F·ad_main3d.F·tl_main3d.F blob 동일. 바뀐 세 driver의 주된 실행부도 위 대응 블록 유지. new s4dvar.in의 설정 좌표는 이동했지만 관측 파일 지정 기능을 없애지 않음. |
| §E/G: nonlinear basis trajectory, disk·split 상태 I/O | **인용된 경로는 REVIEW_ONLY**. i4dvar.F old `:1026-1063` ↔ new `:1037-1074`; split 설명 old `:862-867` ↔ new `:873-878`; r4dvar.F old `:367-373` ↔ new `:378-384` 동일. get_state의 추출은 A 참조. 이 근거로 모든 unsplit trajectory가 RAM에만 있다는 일반화를 검증한 것은 아님. |
| §H: WC13 설정 | `ROMS/External/wc13.h`는 동일. `roms_wc13.in` 변경은 #77의 BOT_ALBEDO 설정·설명이며 `APARNAM=i4dvar.in`은 old `:1223`에서 new `:1224`로 유지. 외부 실행 결과까지 확인한 것은 아님. |

**작업 지시서의 전제 정정:** `ROMS/Adjoint/ad_congrad.F`는 이 비교 구간에서 바뀌지 않았다. old/new blob 모두 `e2882b2a472760a54409200b987415c1fcf8dba4`. 그 `:62-92`의 `(H M B M' H' + Cobs) w = d` 설명과 최소화 경로를 #75의 수정 대상으로 단정할 수 없다. 반면 세 `*4dvar.F`는 바뀌었으며, 주된 차이는 USE 추가와 prior_error의 새 사전 계산·입력 경로다.

### B-2. 새 B 연산자의 확인된 구현과 노트 불일치

다음은 8행 CSV에 추가하지 않은 **필수 조사 B의 결과**다. PR 시점 설명이 당시에도 틀렸다고 단정하지 않으며, new snapshot의 구현 설명으로 쓸 수 있는지를 판정했다.

| 노트 주장 | new 소스 근거 | 판정 |
|---|---|---|
| `:125,181,420`: PR OPEN, merge 후 검증 예정 | new의 조상 `f03bcbbfa2e8833ad5c329c899ef709a14234d94`는 2026-06-10의 `Implementing multi-scale background error covariance matrix (#75)` 커밋이며 해당 코드가 포함됨. 현재 GitHub의 원격 상태 조회가 아닌 pinned 비교의 구현 포함 사실. | **UPDATE_REQUIRED / SEMANTIC_CHANGE**: new에 미반영인 기능처럼 취급할 수 없음. 역사적 날짜 표시는 별개. |
| `:168-178`: multiscale_driver.h가 Nscale dispatch, multiscale_sum_B.h가 가중합 | new git tree에는 두 파일명이 없음. 실제 scale 루프는 `ROMS/Utility/convolve_multi.h:186-238,335-416`; 가중합 호출 `:236`, 구현 `ROMS/Utility/sum_multi_B.F:303-314`의 `self%Bwgt(isFsur,ns)*tl_zeta`. CLASS/solver include는 `roms_multiscale.F:133,355-427,982-999`. | **UPDATE_REQUIRED / SEMANTIC_CHANGE**: 소스 책임·호출 경로 매핑 불일치. 단순 rename 이력은 확인하지 못했으므로 SYMBOL_RENAME_ONLY로 단정하지 않음. |
| `:155,176`: CG로 eigen extrema 추정, CI가 implicit diffusion 수행 | `ROMS/Utility/multiscale_eigen.F:724-743`에서 scale별 tl_CG_2d; `multiscale_CIsolver.h:30-43`에서 extrema를 이용한 CI. i4dvar.F `:2628-2688`, r4dvar.F `:1949-2019`, rbl4dvar.F `:2974-3044`의 normalization·eigen compute/write/read 경로. | **핵심 역할 유지**. 이 CG는 assimilation inner-loop의 cgradient/congrad/rpcg를 대체하지 않음. |
| `:177,197,207`: NiterCI/2 forward + NiterCI/2 adjoint | `tl_convolution_multi.h:897-900`은 `NiterCI(ns,ng)` 그대로 전달. `multiscale_CIsolver.h:121-127`에서 나누는 값은 `Mlap/ifac`; CI 루프 `:229`는 `0..NiterCI`, adjoint `:542`는 `NiterCI..0`. | **UPDATE_REQUIRED / SEMANTIC_CHANGE**: half diffusion applications와 CI 반복 한도를 혼동한 설명. NiterCI 짝수라는 입력 파일 설명 자체는 `s4dvar.in:321-325`에 유지. |
| `:192`: HdecayMX/MY 입력 단위 km | `ROMS/External/s4dvar.in:327-328`은 m, `:341-342`는 50.0d+3. `read_asspar.F:709-720`은 값을 HdecayX/Y에 그대로 대입. | **UPDATE_REQUIRED / INTERFACE_CHANGE**: 현재 입력 규약과 노트의 단위 불일치. 이전 PR PDF의 단위나 표기 오류 발생 시점은 미판정. |
| `:209`: debug를 끈 뒤, “미정의 시” diagnostic·추가 scalar product 발생 | `multiscale_CIsolver.h:220-225,265-274`는 `#ifdef MULTI_SCALE_DEBUG` 안에서 dot product와 residual 출력. | **UPDATE_REQUIRED / SEMANTIC_CHANGE**: 괄호 속 조건 방향이 구현과 반대. debug를 끈다는 앞부분의 취지는 소스와 일치. |
| §I의 Matérn·anisotropic·가중합·vertical separability 핵심 | `ad_convolution_multi.h:44-69`의 Matérn·implicit horizontal·separable vertical 설명, `sum_multi_B.F:17-21,303-314`, `s4dvar.in:1013-1035`의 Nscale/Mlap/Bwgt/solver 규약으로 큰 구조 확인. | **핵심 구조 유지**. PDF의 모든 수식·수치 결과를 소스가 검증한다는 뜻은 아님. |
| §J.4의 현재 기본값 Mlap=10/NiterCG=20 | `ROMS/External/s4dvar.in:284-294,319`에서 확인. | **현재 값은 확인**. 이를 빠른 수렴·성능 개선의 입증으로 연결한 `:332,356`은 UNRESOLVED. |

새 prior_error 경로는 `MULTI_SCALE_B && NONUNIFORM_SCALES`에서 공간 가변 scale을 읽고, normalization 계산 시 eigen extrema를 계산·기록하거나 기존 normalization 파일에서 읽는다. i4dvar.F new `:2594-2602,2628-2688`, r4dvar.F `:1914-1922,1949-2019`, rbl4dvar.F `:2939-2947,2974-3044`. 단일 비용함수가 다른 형태로 교체됐다는 증거는 없다.

### B-3. 세 드라이버 multi-scale 호환 단정은 보류

노트 `:263,363`은 I4DVAR/R4DVAR/RBL4DVAR 모두 multi-scale B 호환이라고 한다. **I4DVAR까지 포함한 무조건적 호환 주장은 UNRESOLVED**다. 초기화 코드가 추가됐다는 사실만으로 전체 경로 호환을 확정할 수 없다.

- new `ROMS/Drivers/i4dvar.F:1442,1644`는 각각 `ad_convolution(ng,tile,LADJ2,Lweak,2)`, `tl_convolution(ng,tile,Lcon,Lweak,2)`라는 **5인자** 호출을 유지한다.
- new `ROMS/Adjoint/ad_convolution.F:95-98`, `ROMS/Tangent/tl_convolution.F:95-98`는 MULTI_SCALE_B일 때 multi 헤더를 선택한다. 그 두 헤더 `:139,147-149`의 같은 이름 public routine은 `(ng,tile,ns,Linp,Lweak,ifac)`라는 **6개의 필수 인자**를 선언한다. 선택적 ns나 이 호출을 수용하는 overload는 해당 모듈에 없다.
- R4DVAR/RBL4DVAR는 `error_covariance`를 호출한다(new r4dvar.F `:1128,1360`, rbl4dvar.F `:1475,1697-1702`). 선택된 `convolve_multi.h`는 `:198,217`에서 ns를 포함한 6인자 호출을 한다.

위 호출부·선언부 불일치는 소스로 확인한 사실이다. 실제 빌드 구성의 성공/실패나 세 driver의 수치적 동등성은 이 검토에서 실행하지 않았으므로 그 결과를 추측하지 않는다. 노트의 “세 파일 동시 수정 ⇒ 세 경로 호환” 추론을 근거로 승격하지 않는다.

## UNRESOLVED 목록과 검토 한계

후보 R1-1~R1-8에는 남은 UNRESOLVED가 없다. 추가 조사 B에는 다음이 남는다. 모두 **소스만으로 확인되지 않은 주장**이며, 이번 commit 때문에 새로 틀렸다는 판정도 아니다.

| 항목 | 대상·근거 부족 |
|---|---|
| U-B1: 전체 driver 호환 | 위 B-3. I4DVAR MULTI_SCALE_B의 호출 인터페이스 불일치가 관찰되므로 세 driver 모두 호환이라는 단정을 확인하지 못함. |
| U-B2: PDF 수식·WC13 결과·한국 적용 | §I.1의 Bessel/Daley·negative-lobe 허용 범위, §I.5-7의 잔차/수렴횟수/곡선 수치, §I.8 및 §J.7의 KOOS-EJS 적용 이득은 현재 소스의 호출·변수만으로 검증되지 않음. 로컬 허용 자료에서 해당 PDF 원본을 찾지 못했고 외부로 범위를 확대하지 않음. Matérn/가중합이라는 코드 구조의 확인과 구별. |
| U-B3: §J의 5개 역사적 commit과 개선 원인 | `7a1f5d9d,b7312fb1,952d7eab,16601076,23919237`는 제공된 git repo에서 commit object를 조회할 수 없음. 현재 기본값·tracer_metadata 모듈 존재는 확인하지만, 각 역사 diff의 수량·병렬 버그가 race/broadcast 문제였다는 원인·그 이전 변경의 regression 추측은 확인 못함. 기본 반복수 감소만으로 빠른 수렴이 입증됐다는 주장도 미확인. |
| U-B4: §J.2 template 사용 | 노트 `:272`의 def_info.F가 Bcorrelation CDL template을 사용한다는 직접 연결은 확인 못함. new def_info.F에서 Bcorrelation/`.cdl` 참조가 발견되지 않음. 템플릿 파일 존재와 런타임 사용은 다른 주장. |
| U-B5: 실무 규칙·Decision Guide·Common Pitfalls의 일반화 | 노트 `:367-396`의 권장 loop 횟수, J_final/J_initial 임계값, 1e-10 검사 임계, 추천 correlation 길이, `Q=B`이면 strong constraint와 같다는 설명, 모든 unsplit trajectory가 RAM에 있다는 단정은 이번 소스 근거로 확인 못함. 위 B-1에서 확인한 구체적 I/O·solver 경로와 구별. |

§I.4의 Mlap 조건은 입력 파일 설명상 “짝수, >2”이지만 실제 `read_asspar.F:1775-1778`의 검사는 `.lt.2`와 홀수 여부다. 문서 의도와 입력 검사의 경계값을 동일한 보장으로 취급하지 않았다. B 연산자의 수치 정확성·성능을 새로 감사하거나 범위를 확대하지 않았다.

검토 중 관찰한 8건 밖 불일치는 위 MD에만 기록했다. CSV는 원래 8개 ID를 그대로 유지하며 위키 본문·권한·소스 snapshot을 수정하지 않았다.

## 재현과 산출물 검사

주요 재현 명령은 다음과 같다.

```sh
git -C ~/.cache/coastal-snapshots/roms-upstream diff 32c79b7 57aecf5 -- ROMS/Nonlinear/pre_step3d.F ROMS/Utility/def_var.F
git -C ~/.cache/coastal-snapshots/roms-upstream diff 32c79b7 57aecf5 -- ROMS/Drivers/i4dvar.F ROMS/Drivers/r4dvar.F ROMS/Drivers/rbl4dvar.F
git -C ~/.cache/coastal-snapshots/roms-upstream show 32c79b7:ROMS/Utility/get_state.F
git -C ~/.cache/coastal-snapshots/roms-upstream show 57aecf5:ROMS/Utility/get_state.F
git -C ~/.cache/coastal-snapshots/roms-upstream rev-parse 32c79b7:ROMS/Adjoint/ad_congrad.F 57aecf5:ROMS/Adjoint/ad_congrad.F
```

산출물: `_staging/roms-prescan/phase1-codex.csv`, `_staging/roms-prescan/phase1-codex.md`. 원래 요청 경로에 저장했으며 fallback은 필요하지 않았다. CSV 헤더·8개 ID와 순서·원문 줄 일치·필수 reason_type·판정 집계·소스 좌표의 파일 범위 검사를 통과했다.

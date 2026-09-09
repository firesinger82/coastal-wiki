# Claude Sonnet 적대적 검토 2

## 검토 결과

**검증 범위**: closure의 local8 전건(`resolution-ledger.json`)과 승인된 source60 canonical draft(`xbeach-source-audit-supplements.md`) 중 hotstart 상태 덮어쓰기(2건)·비활성 prototype 배제(build-system 교차검증)·경계조건 dnvsum·격자 sentinel 등 강한/비직관적 주장 8건을 실제 원본(`models/XBeach/raw/source_code`)과 대조. `Makefile.am`, 전체 `.vfproj`(8개), `.sln`을 grep해 대체 빌드 시스템 존재 여부까지 확인.

### local8 8건 — 전건 확인, 반박 결론 모두 성립

1. **spaceparamsdef.F90 (ranges_init)** — `init()`이 direct 실행과 BMI(`xbeach_bmi.f90:initialize`) 양쪽의 유일한 진입점이고, `ranges_init`이 16개 bound를 모두 할당함을 확인. **다만 call_path 서술에 정밀성 문제 발견** (아래 별도 기술).
2. **drifters.F90 (MPI_MIN)** — `call drifter`는 `libxbeach.F90` 단일 호출지만 존재하며 직전에 `flow`가 무조건 실행됨을 확인. 결합 경계검사가 idrift/jdrift를 함께 갱신/함께 sentinel 처리함을 원본에서 재확인. 반박 타당.
3. **vegetation.F90 (species iostat)** — `count_lines`와 이후 `(a)` 읽기가 동일 파일을 대상으로 함을 확인. NARROWED 판정 타당.
4. **vsm_u_XB.f90 (n>=2)** — 저장소 전체에서 `vsm_u_XB` 호출자는 `flow_timestep.F90`의 `par%nz>1` 가드 1곳뿐임을 grep으로 재확인. NARROWED 판정 타당.
5. **xbeachlibrary_IFX_dynamic.vfproj / xbeachlibrary_dynamic.vfproj** — `introspection.F90`, `libxbeach_dynamic.F90`에 `USEMPI`/`USENETCDF` 관련 `ifdef`가 전혀 없음을 확인. `.sln`의 `ProjectDependencies` GUID(`{4BD9BE9F-...}`)가 static `xbeachlibrary.vfproj`와 정확히 일치함을 확인. REFUTATION_CONFIRMED 타당.
6. **README.parallel** — 문서 원문이 SAVE 패턴을 명시적으로 비판하고 대안을 제시하는 문맥임을 전문 대조로 재확인. 타당.
7. **netcdf_attributes.f90** — 배열 getter(`nf90_get_att_FourByteInt` 등)가 실패 상태와 무관하게 임시배열 전체를 복사하는 코드를 직접 확인. SPLIT 판정(B2만 부분 반박, 나머지 STANDS) 타당.

### 강한/비직관적 60건 표본 검증 — 오류 없음

- **hotstart uu/vv 덮어쓰기(B11, initialize.F90)**: `libxbeach.F90`에서 `hotstart_init_1`(uu/vv 읽음, L165) → `flow_init`(uu=vv=0으로 무조건 재설정, L172, L1042 부근) → `hotstart_init_2`(uu/vv 재읽기 없음, L188) 순서를 원본에서 직접 확인. 주장 정확.
- **hotstart depfile sentinel(B0, params.F90)**: `par%hotstart` 기본값이 `params.def:92`에서 `-123`으로 선언되고, depfile 필요 여부 검사(L160)가 `par%hotstart`의 실제 readkey 호출(L312, 검사보다 152줄 뒤)보다 먼저 실행됨을 확인. 즉 검사 시점에 `par%hotstart`는 항상 sentinel(-123, `.ne.1`)이므로 신규 hotstart 요청도 무조건 depfile을 요구. 매우 비직관적이지만 정확한 주장.
- **비활성 prototype 배제(B0/B6/B7/B10/B16/B20, wave_boundary_*)**: `wave_boundary_datastore.f90`, `wave_boundary_main.f90`, `wave_boundary_update.f90`가 `Makefile.am`(autotools)에도, 8개 `.vfproj` 전체(grep 결과 0건)에도, CMakeLists(부재)에도 포함되지 않음을 확인. `BUILDXBEACH` 매크로는 두 파일 자기 자신 안에서만 참조되고 어떤 빌드 파일에서도 정의되지 않음. 배제 주장은 두 빌드 시스템(autotools + Windows vfproj) 전체에 걸쳐 성립.
- **boundaryconditions.F90 B15 (ny=2 → dnvsum=0)**: `ranges_init`의 `jmin_vv=2, jmax_vv=s%ny-1` 공식에서 `ny=2`일 때 `jmax_vv=1<jmin_vv=2`가 되어 Fortran에서 빈 슬라이스가 되고 `sum()`이 0을 반환함을 직접 산출·확인. 정확.
- **params.F90 B1 (음수 dx/dy)**: `readkey_dbl` 기본값 `-1.d0`이 가변격자(`vardx=1`)·Delft3D 격자변환 양쪽에서 "값 없음" sentinel로 실제 사용됨을 원본에서 확인(`par%dx=-1.d0 ! Why?` 주석 포함). NARROWED 근거 타당.
- **wave_directions.F90 B5**: 해당 subroutine 전체가 `Makefile.am`에 없고 저장소 어디서도 호출되지 않음(실행경로 완전 배제, 주장보다 더 강한 근거). ncoutput.F90 B23의 `STATUS=` 미지정 direct-access `OPEN`은 Fortran 기본 동작상 기존 파일을 truncate하지 않으므로 "이전 run의 초과 record 잔존" 주장과 일치.

### 발견한 정밀성 문제 1건 (오류는 아니나 수정 권고)

`XBeach-000:spaceparamsdef.F90:0` 항목의 `call_path` 필드:
> `"libxbeach_module:init -> optional space_distribute_space -> ranges_init -> nonh/means/output initialization -> executestep computations"`

이 서술은 `space_distribute_space`와 `ranges_init` 사이에 아무것도 없는 것처럼 읽히지만, 실제 `libxbeach.F90` init() 시퀀스에는 `hotstart_init_1`, `setbathy_init`, `readtide`, `readwind`, `flow_init`, `discharge_init`, `drifter_init`, `wave_init`, `gw_init`, `rainfall_init`, `sed_init`, `ship_init`, `veggie_init`, `hotstart_init_2` — 총 13개 서브루틴이 `ranges_init` **이전**에 실행됩니다(`libxbeach.F90:158-207`). 직접 grep으로 이 13개 서브루틴 정의부 전체를 확인한 결과 `imin_ee/imax_ee/.../imin_zs/imax_zs` 등 module-scope range bound 변수를 참조하는 곳은 없었습니다(유일하게 이 변수들을 쓰는 `vegetation.F90`의 `vegatt`/`swvegatt`/`porcanflow`는 `veggie_init`이 아니라 `libxbeach.F90:303`의 executestep 단계에서, 즉 `ranges_init` 이후에 호출됩니다).

**결론적으로 `REFUTATION_CONFIRMED` 판정 자체는 옳습니다** — "no earlier active stencil use was found"라는 `reason` 필드 문장은 정확합니다. 그러나 `call_path` 필드가 실제로 존재하는 13개의 중간 초기화 단계를 생략해, 검토자가 "grid 분산 직후 바로 ranges_init"이라고 오인할 위험이 있습니다. `canonical_ready_ko` 요약("공간 분할 직후 `ranges_init`에서 16개 범위를 모두 지정")도 같은 축약을 반복합니다.

**수정안**: `call_path`를 `"libxbeach_module:init -> (optional MPI) space_distribute_space -> [hotstart_init_1, setbathy_init, readtide, readwind, flow_init, discharge_init, drifter_init, wave_init, gw_init, rainfall_init, sed_init, ship_init, veggie_init] (none reference the module-scope range bounds) -> ranges_init -> hotstart_init_2 -> nonh/means/output initialization -> executestep computations"`로 확장하고, 이 13개 서브루틴이 range bound를 참조하지 않는다는 확인 근거를 evidence 배열에 추가할 것을 권고합니다.

### 검증 한계

35회 tool call·1600단어 제한 내에서 60건 전량을 원본 대조하지는 못했습니다. 표본은 hotstart 상태(2건), 빌드 배제(6건 중 대표 사례), 경계조건 dnvsum, 격자 sentinel, 죽은 코드(wave_directions), 파일 truncation(ncoutput)으로 리스크가 높은 비직관적 주장 위주로 선택했습니다. 나머지 미표본 항목(주로 STANDS 단순 나눗셈/미검증 계열)은 이번 세션에서 원본 재대조를 수행하지 않았습니다.

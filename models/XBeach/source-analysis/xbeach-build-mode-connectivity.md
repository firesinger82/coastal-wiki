---
title: "XBeach 빌드 대상·소스 생성·모드 연결"
canonical_source: self
citation_status: draft-unsourced
note_author: "Codex"
note_date: 2026-09-12
verification_method: "원본 빌드 선언·호출·피호출 정의 대조와 임시 복사본 소스 생성; 새 연결 주장 검토본"
---

AI가 작성한 연결 검토본이다. 소스 기준은 `models/XBeach/raw/source_code/trunk/`이며, 아래 짧은 경로는 이 루트를 기준으로 한다. [빌드·파일 역할 원장](../../../_staging/total-read/model-audit/XBeach/connectivity/build-mode-20260912/build-map.json)과 [분기 계약](../../../_staging/total-read/model-audit/XBeach/connectivity/build-mode-20260912/contracts.json)에 원본 SHA와 행을 연결했다. **컴파일 목록 포함, 모듈 의존, 실제 루틴 실행 도달성은 각각 다른 증거다.**

## 빌드 대상과 API

| 계열 | 소스 배치 | 모델 진입점 |
|---|---|---|
| Autotools | `src/xbeachlibrary/Makefile.am:3-60`은 코어·`introspection`·BMI를 한 라이브러리 소스 목록에 둔다. `src/xbeach/Makefile.am:2-8`은 입력/프로그램을 이 라이브러리에 연결한다. | 프로그램 또는 BMI |
| Visual Fortran / IFX static | `xbeachlibrary.vfproj`와 `xbeachlibrary_IFX.vfproj`는 코어를 static library로 선언한다. `introspection`과 BMI는 이 목록에 없다. | 해당 static library를 사용하는 아래 세 대상 |
| Windows 실행 파일 | `xbeach.vfproj` 및 `xbeach_IFX.vfproj`의 `Files`에는 `input.F90`, `xbeach.F90`, `introspection.F90`이 있다. | `readinput → init → executestep/outputext → final` |
| Windows dynamic API | `xbeachlibrary_dynamic.vfproj` 및 `xbeachlibrary_IFX_dynamic.vfproj`의 `Files`에는 `introspection.F90`, `libxbeach_dynamic.F90`이 있다. | C 이름 `init/executestep/outputext/finalize` |
| Windows BMI API | `xbeachlibrary_bmi.vfproj` 및 `xbeachlibrary_IFX_bmi.vfproj`의 `Files`에는 `xbeach_bmi.f90`이 있다. | C 이름 `initialize/update/finalize` 및 변수/시간 API |

Windows 프로젝트 경로는 `src/xbeach/` 또는 `src/xbeachlibrary/`다. 일곱 `XBeach_VS*.sln`의 `ProjectDependencies`에서 실행·dynamic·BMI 대상의 static 코어 의존을 확인했다. IFX solution은 IFX 프로젝트를 선택한다. 이 선언으로 실제 Windows 링크 성공이나 DLL export 검사를 대신하지 않는다. 프로젝트별 파일 행·설정·solution 대응은 위 원장에 보존했다. 함수 본문 근거: `src/xbeach/xbeach.F90:1-33`, `src/xbeachlibrary/libxbeach_dynamic.F90:12-38`, `src/xbeachlibrary/xbeach_bmi.f90:35-78`.

Autotools는 `--with-mpi`와 `--with-netcdf` 두 축을 각각 선택한다. MPI 선택은 `USEMPI/HAVE_MPI_WTIME`, NetCDF 선택은 `USENETCDF` 컴파일 정의로 연결된다. Windows에서는 **대상별** 정의와 제외 파일을 읽어야 한다. 예를 들어 `MPI_netcdf_Release|x64`의 두 static 프로젝트에는 두 기능 정의가 있지만 같은 이름의 실행·dynamic·BMI 프로젝트에는 해당 전처리 정의가 직접 적혀 있지 않다. 설정 이름만으로 모든 번역 단위의 정의를 동일하다고 처리하지 않는다. (`configure.ac:42-54,71-80`; `src/xbeachlibrary/Makefile.am:99-108`; 각 `.vfproj`의 `Configurations/Configuration/Tool`)

XBeach Python wrapper는 제공된 라이브러리의 `init/executestep/outputext`를 호출한다. 별도 솔버 빌드나 BMI의 `initialize` 이름과 자동 호환되는 인터페이스로 세지 않는다. (`src/pybeach/xbeach/libxbeach.py:61-72`; [lifecycle 계약](xbeach-lifecycle-state-contracts.md))

## 생성 파일과 비연결 소스

`generate.py`는 `variables.def`와 `params.def`를 읽고 `templates/*.mako`를 같은 이름의 `.inc`로 렌더한다. 템플릿 인수가 없으면 전체 목록을 생성한다. 원본 생성기를 임시 복사본에서 실행해 생성 파일 집합을 확인했다. (`scripts/generate.py:33-41,215-262`; [생성 재현](../../../_staging/total-read/model-audit/XBeach/connectivity/build-mode-20260912/generation-probe.json))

`BUILT_SOURCES`는 생성 가능한 파일 전체 목록이 아니다. `RF.inc`, `RFveg.inc`, `genmpi_coll.inc`, `genmpi_distr.inc`, `nh_pars.inc`, `paramsdecl.inc`, `space_alloc_arrays_dummies.inc`, `xmpi_bcast.inc`도 템플릿에서 생성되지만 그 목록에는 없다. `spacedecl.inc` 규칙이 인수 없이 생성기를 실행하므로 함께 생성되는 경로를 기록한다. 이 사실만으로 모든 병렬/증분 make 순서가 안전하다고 판정하지 않는다. (`src/xbeachlibrary/Makefile.am:62-92`; `scripts/generate.py:219-231`)

Windows prebuild는 `build/generate_and_copy_gen_files.bat`에서 `scripts/dist/generate.exe`를 호출한다. 이름이 비슷하다는 이유로 이 실행물과 현재 Python 원본의 출력이 동일하다고 보증하지 않는다. 모델이 호출하는 인터페이스까지만 기록했다. (`src/xbeachlibrary/build/generate_and_copy_gen_files.bat:18-23`)

확인한 Autotools와 여덟 모델 프로젝트의 합집합에 없는 Fortran 파일은 다음과 같다: `beachwizard.F90`, `demo.F90`, `general_mpi_new.F90`, `wave_bc_nextgen.f90`, `wave_boundary_datastore.f90`, `wave_boundary_init.f90`, `wave_boundary_main.f90`, `wave_boundary_update.f90`, `wave_directions.F90`, `wave_stationary.F90`, `xmpinew.F90`. 이들은 `src/xbeachlibrary/`에 존재하지만 이 빌드의 활성 솔버로 간주하지 않는다. `demo.F90:1-8`은 상태 이름 조회 예제 프로그램이다. `waveparams.F90`은 Autotools 목록에는 남아 있으나, 조사한 `src`의 활성 `use waveparams` 문은 없다. 컴파일 목록만으로 실행 경로를 추가하지 않는다. (각 `Makefile.am`/`.vfproj` 파일 목록과 원장의 `module_use_index`)

## 물리 모드의 실제 분기

공통 드라이버는 오류가 없을 때 `wave_bc` 이후 `swave==1`이면 `wave`, `flow==1` 또는 NONH이면 `flow`를 호출한다. 그 뒤 표사와 지형 갱신 조건을 검사한다. (`src/xbeachlibrary/libxbeach.F90:293-310`)

| 모드·조건 | 도달하는 계산 | 시간 조건 |
|---|---|---|
| stationary | `wave_dispersion(0) → wave_stationary_directions(0)` | `abs(mod(t,wavint)) < 0.001*dt` 또는 새 stationary 경계 |
| surfbeat, `single_dir!=1` | WCI에 따른 분산 계산 → `wave_instationary` | 정상 물리 스텝마다 |
| surfbeat, `single_dir==1` | 평균장 갱신 → 조건부 방향 계산 → 에너지용 분산 재계산 → `wave_instationary` | 방향 계산만 `wavint`/새 경계/첫 스텝 조건; 에너지는 매 스텝 |
| nonh, `nonhq3d!=1` | `nonh_1lay_pred → flow_secondorder_advUV → nonh_1lay_cor` | 정상 물리 스텝마다 |
| nonh, `nonhq3d==1`, `s%ny==0` | `nonh_2lay_pred_2dV → flow_secondorder_advUV → nonh_2lay_cor_2dV` | 정상 물리 스텝마다 |
| nonh, `nonhq3d==1`, `s%ny!=0` | `nonh_2lay_pred_3d → flow_secondorder_advUV → nonh_2lay_cor_3d` | 정상 물리 스텝마다 |

근거: `src/xbeachlibrary/wave_timestep.F90:75-115`, `flow_timestep.F90:635-658`, `nonh.F90:201-249`. NONH 입력은 `swave=1`을 경고 후 0으로, `secorder=0`을 경고 후 1로 바꾼다. NONH pressure 경로는 `wave`의 case가 아니라 `flow` 내부다. (`params.F90:1559-1563,1740-1747`)

MPI는 위 물리 모드와 별개의 컴파일 축이다. `solver.F90:14`의 “MPI이면 nonh 제외”라는 오래된 주석을 현재 빌드 조건으로 사용하지 않는다. 빌드 목록에 `nonh/solver/flow_secondorder`가 있고 실제 pressure 호출 및 solver 내부 MPI 분기가 남아 있다. (`flow_timestep.F90:630-658`; `solver.F90:205-214`)

stationary 또는 `single_dir`의 MPI 입력에서는 `swave==1`, 전역 `par%ny>0`일 때 자동 분할이 `MPIBOUNDARY_X`로 설정되며, 작은 `ny`는 종료된다. `MPIBOUNDARY_MAN`은 이 자동 분기의 명시적 예외다. NONH의 2DV/3D dispatcher는 별도로 **로컬 `s%ny`**를 검사한다. (`params.F90:1884-1910`; `nonh.F90:209-230`)

이 문서는 저장된 빌드 선언·전체 `src` 파일 역할과 위 여섯 dispatcher 경로를 연결한다. 경계 종류·표사 공식·선택 기능까지 포함한 모든 루틴의 실행 도달성이나 전체 모델 검증 완료를 뜻하지 않는다.

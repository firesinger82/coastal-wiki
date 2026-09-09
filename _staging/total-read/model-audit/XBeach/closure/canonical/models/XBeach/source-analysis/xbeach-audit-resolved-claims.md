---
title: "XBeach 감사 쟁점의 후속 판정과 적용 조건"
canonical_source: self
layer: 2
depends_on: []
citation_status: verified
has_source_needed: false
verification_by: "Codex source cross-ref; Claude Sonnet adversarial review"
verification_date: 2026-09-09
verification_method: "Source and referenced-note cross-reference; independent MSI identity/disassembly where applicable"
note_author: "Codex"
note_date: 2026-09-09
---

# XBeach 감사 쟁점의 후속 판정과 적용 조건

서로 모순된 소스 해석과 원문 확인에 실패했던 반증을 다시 대조한 AI 분석이다. 각 항목은 원본 소스 또는 포함 바이너리의 해당 경로에 한정한다. 반증된 실패 시나리오와 여전히 성립하는 제한 조건을 구분한다. 기존 감사 영수증의 의미를 새 주장에 확장하지 않는다.

<a id="xb-hard-01"></a>

## XB-HARD-01 · wave_boundary_main.f90

`wave_boundary_main`의 seed 처리에는 잠재적 컴파일 결함이 있다. 저장소 타입의 `randomseed`는 비할당 정수 스칼라인데 `ALLOCATED`와 `DEALLOCATE`에 전달된다. 따라서 “미할당 seed 벡터 대입” 해석은 기각한다. 확인한 Makefile.am과 6개 vfproj에는 이 모듈이 없으므로 해당 빌드의 실행 결함으로 확대하지 않는다. (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_datastore.f90:16-30`; `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_main.f90:121-135,221-224`; `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/Makefile.am:4-60`.)

<a id="xb-hard-02"></a>

## XB-HARD-02 · morphevolution.F90

`waveturb`의 `vv==0` 분기는 `s%kturb` 대신 작업배열 `kturbv`를 평균한다. 배열은 호출마다 0으로 초기화되고 j가 증가하는 순서로 갱신되므로 두 피연산자는 모두 0이다. “이전 호출의 잔존값 사용” 해석은 기각한다. Lagrangian 이류에서는 같은 0의 `vv`를 곱해 이 면의 flux 차이가 없지만, Eulerian 이류는 `vev`를 곱하므로 `vv==0`, `vev!=0` 조건에서 잘못된 0이 영향을 줄 수 있다. (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90:2863-2874,2918-2938`.)

<a id="xb-hard-03"></a>

## XB-HARD-03 · README.txt.txt

`trunk/lib/README.txt.txt`는 빈 파일이 아니다. 2개 비어 있지 않은 줄에서 win32 사전 빌드 라이브러리만 안내하며, 함께 제공되는 x64 MPICH를 안내하지 않는다. 이는 아키텍처 목록의 누락이다. (`models/XBeach/raw/source_code/trunk/lib/README.txt.txt:1-2`; `models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpi.h:1-15`.)

<a id="xb-hard-04"></a>

## XB-HARD-04 · mpicxx.h

x64 `mpicxx.h`의 네 `Clone` 구현은 `MPI_Comm_dup` 반환값을 확인하지 않는다. 제공 MSI의 실제 `mpich2mpi.dll`은 dispatcher이며, 전달 대상이 아직 없고 공통 초기화 호출이 0을 반환하면 출력 포인터를 쓰지 않은 채 `0x10`을 반환한다. 기존 반증이 검사한 `_1BE…` 멤버는 MSI File 테이블상 `mpich2mpi.dll`이 아니라 `mpich2nemesisp.dll`이므로, 그 backend의 null 대입을 전체 배포본에 일반화할 수 없다. 따라서 초기화 실패 또는 아직 검증되지 않은 선택 backend의 오류 복귀에서는 미정의 `ncomm` wrapper 위험을 유지한다. 이는 제공 아티팩트의 정적 가능성 판정이며 XBeach 실행 중 해당 DLL 로드나 분기 실행을 주장하지 않는다. (`models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpicxx.h:1567-1580,1658-1671,2328-2341,2443-2456`; MSI File 행 `_1BE…`/`_7D9…`; 실제 `mpich2mpi.dll` RVA `0x97a0`, `0x10f30`.)

<a id="xb-hard-05"></a>

## XB-HARD-05 · mpicxx.h

x64 `mpicxx.h`의 `NULL_COPY_FN` 본문은 `attr_out`을 대입하지 않고 `flag=1`로 만든다. 그러나 함께 제공된 `cxx.lib`의 Comm/Datatype/Win `Create_keyval`은 이 함수 포인터를 C null callback(0)으로 치환하므로 일반 등록 뒤 복제에서 미정의 포인터가 설치된다는 주장은 기각한다. 본문 직접 호출이나 별도 전달 callback은 이 치환을 거치지 않으므로 낮은 우선순위의 결함으로 남긴다. (`models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpicxx.h:409,1471,1904`; `models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpi.h:265-271`; `models/XBeach/raw/source_code/trunk/lib/x64/mpich/lib/cxx.lib`, 각 Create_keyval 함수 +0x04–+0x2c의 relocation 포함 역어셈블리.)

### MPICH 바이너리 식별과 범위

위 판정의 제공 MSI는 `models/XBeach/raw/source_code/trunk/lib/x64/mpich/mpich2-1.4.1p1-win-x86-64.msi`(SHA-256 `ac0399228624f48f143245caa26a79fadda1214d8368942c5f37ff4aed27fa47`)이다. MSI `File` 테이블과 cabinet 멤버를 대조하면 다음과 같다.

| MSI File 식별자 | 파일명 | SHA-256 |
|---|---|---|
| `_1BE96E15F472462586C19E8C77FF7927` | mpich2nemesisp.dll | `df1cb786d8054c5f730f1f1ea1e97b3099d76f6935302ae6d4f2232efbace87a` |
| `_7D9F6BC68D3B438D9D6834EF34F3754F` | mpich2mpi.dll | `feca14fe75d28ba1a3f8e229b41c7b3eb0680124600ef1a55ee8d3faa8c5c795` |
| `_00D89EB1B52A45B79628A8A91613E9C1` | cxx.lib | `6fd6a3e6a61347ec912ee96b0b0031d2c672be916277dc693d6efdac5c6127dc` |

첫 backend의 `MPI_Comm_dup` 오류 경로는 `MPI_COMM_NULL`을 대입하지만, 두 번째 dispatcher의 초기 설정 실패 분기는 같은 보장을 제공하지 않는다. `cxx.lib`는 저장소 원본과 추출본의 바이트 해시가 같다. 따라서 Clone 기각을 배포본 전체로 확장하지 않으며, NULL_COPY_FN의 일반 등록 반증만 해당 archive 범위에서 유지한다. 설치·실행 없이 추출·역어셈블리한 결과다. [원본 MSI 테이블·재현 근거](../../../_staging/total-read/model-audit/XBeach/closure/local-refutations/mpich-identity/identity-ledger.json).

<a id="xb-local-01"></a>

## XB-LOCAL-01

계산 범위 전역 정수는 선언 시 초기값이 없지만, XBeach의 지원 초기화 경로는 공간 분할 직후 `ranges_init`에서 16개 범위를 모두 지정한 다음 비정수압·평균·출력 초기화와 시간 적분으로 진행한다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/spaceparamsdef.F90:57`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/spaceparams.F90:1453`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/libxbeach.F90:207`). 따라서 정상 lifecycle의 미초기화 사용 결함으로 보지 않으며, 초기화 전 직접 모듈 접근은 지원 계약 밖이다.

<a id="xb-local-02"></a>

## XB-LOCAL-02

MPI drifter는 `flow` 직후 호출되며, 활성 유동 분기마다 `uu`와 `vv` halo를 교환한다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:630`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/libxbeach.F90:301`). 각 rank는 하나의 결합 경계검사로 두 좌표를 함께 갱신하거나 두 좌표를 모두 sentinel로 바꾼 뒤 각각 `MPI_MIN`을 적용한다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/drifters.F90:40`). 따라서 제공된 경로에서는 서로 다른 rank의 좌표 성분이 섞인다는 결함이 입증되지 않는다.

<a id="xb-local-03"></a>

## XB-LOCAL-03

정적인 species 목록은 `count_lines`로 레코드 수를 센 뒤 같은 수만큼 문자 형식 `(a)`로 다시 읽으므로, 단순히 목록이 짧거나 비수치 텍스트라는 이유로 이름이 미정의가 되는 경로는 성립하지 않는다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/readkey.F90:1108`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:102`). 다만 두 번째 읽기의 `iostat`를 검사하지 않으므로 두 pass 사이 파일 변경이나 실제 읽기 오류는 즉시 보고되지 않는 낮은 수준의 I/O 진단 위험으로 남는다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90:110`).

<a id="xb-local-04"></a>

## XB-LOCAL-04

XBeach 내부 호출은 `par%nz>1`일 때만 `par%nz`를 `n`으로 전달하므로 기본 solver 경로에서 `n=1`은 도달하지 않는다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:956`). 그러나 `vsm_u_XB`는 공개 모듈 절차이고, 인터페이스에는 `n>=2` 조건이나 실행 검사가 없는데 구현은 `n-1`로 나누고 `sigz(2)`·`sigz(n-1)`을 참조한다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vsm_u_XB.f90:5`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vsm_u_XB.f90:38`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vsm_u_XB.f90:209`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vsm_u_XB.f90:319`). 외부 직접 호출 시 `n>=2`가 필요한 인터페이스 계약 경고로 유지한다.

<a id="xb-local-05"></a>

## XB-LOCAL-05

IFX dynamic wrapper의 `MPI_netcdf_*` 구성에는 `USEMPI`·`USENETCDF` 정의가 없지만, 이 프로젝트는 macro 분기가 없는 `introspection.F90`와 `libxbeach_dynamic.F90`만 컴파일하고 같은 구성명의 static library에 의존한다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xbeachlibrary_IFX_dynamic.vfproj:162`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xbeachlibrary_IFX_dynamic.vfproj:185`, `models/XBeach/raw/source_code/trunk/XBeach_VS2022_IFX.sln:22`). 실제 기능 선택은 static library 구성에서 두 macro를 모두 정의해 수행한다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xbeachlibrary_IFX.vfproj:162`). 따라서 wrapper-local macro 누락을 MPI+netCDF 기능 불일치로 보지 않는다.

<a id="xb-local-06"></a>

## XB-LOCAL-06

legacy dynamic wrapper의 `MPI_netcdf_*` 구성에도 `USEMPI`·`USENETCDF` 정의는 없지만, 프로젝트는 macro 분기가 없는 두 wrapper 소스만 컴파일하며 같은 구성명의 static library에 의존한다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xbeachlibrary_dynamic.vfproj:147`, `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xbeachlibrary_dynamic.vfproj:184`, `models/XBeach/raw/source_code/trunk/XBeach_VS2017.sln:22`). 기능 macro와 MPI/netCDF library 선택은 static 구성에 들어 있다 (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xbeachlibrary.vfproj:147`). 따라서 wrapper-local macro 누락만으로 기능 불일치를 주장할 수 없다.

<a id="xb-local-07"></a>

## XB-LOCAL-07

`README.parallel`은 SAVE allocatable 패턴을 권장하는 것이 아니라, 여러 `spacepar` 크기를 사용할 때 저장 배열의 크기가 틀릴 수 있다고 명시적으로 경고한 뒤 SAVE가 없는 지역 allocatable을 대안으로 제시한다 (`models/XBeach/raw/source_code/trunk/doc/README.parallel:139`). 따라서 이 문단을 saved workspace lifecycle 결함으로 분류한 주장은 문맥을 반대로 읽은 것으로 기각한다.

<a id="xb-local-08"></a>

## XB-LOCAL-08

번들된 legacy netCDF-Fortran 래퍼의 `nf90_inquire_attribute`는 같은 이름을 조회하는 `nf_inq_attid`와 `nf_inq_att`의 상태 중 뒤의 상태를 반환한다. 안정된 dataset에서는 두 호출의 공식 실패 조건이 같으므로 별도의 `attnum` 오류가 가려진다는 주장은 기각한다 ([Unidata netCDF-Fortran F77 Interface Guide §7.3](https://docs.unidata.ucar.edu/netcdf-fortran/current/nc_f77_interface_guide.html#nf_005finq_005fatt-family), acc. 2026-09-09; `models/XBeach/raw/source_code/trunk/lib/win32/netcdff90/netcdf_attributes.f90:40`). 그러나 래퍼는 실패 상태에서도 미초기화된 type·length 및 scalar 임시값을 출력에 복사하고, 정수 변환 배열은 실제 속성 길이보다 큰 임시 배열 전체를 복사한다 (`models/XBeach/raw/source_code/trunk/lib/win32/netcdff90/netcdf_attributes.f90:52`, `models/XBeach/raw/source_code/trunk/lib/win32/netcdff90/netcdf_attributes.f90:187`, `models/XBeach/raw/source_code/trunk/lib/win32/netcdff90/netcdf_attributes.f90:231`). 이는 XBeach solver 결함이 아니라 포함된 외부 netCDF 래퍼의 오류·출력 계약 위험이다.

---
title: "SWAN Implementation Manual (swanimp v41.51) — source file map + build (GNU make/CMake) + switch.pl + MPI/Metis/netCDF + swaninit + run/test verbatim"
topic: swan
canonical_source: external
external_source: "swanimp (SWAN Implementation Manual, Cycle III version 41.51, SWAN team 2026-03-13). Chapters 1 Introduction(material) / 2 Patch files / 3 Installation(classic GNU make + switch.pl + MPI/Metis/netCDF + CMake) / 4 swaninit / 5 Run / 6 Testing. 공식: http://www.swan.tudelft.nl + GitLab https://gitlab.tudelft.nl/citg/wavemodels/swan."
citation_status: verified
verification_method: "models/SWAN/raw/manuals/website_markdown/online_doc/swanimp/ node1-21.md 전 노드 직접 read. 빌드 명령·switch.pl 옵션·macros.inc 변수·swaninit 필드·swanrun 구문 verbatim. swantech doc-stack §4 TOC와 cross-check."
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — build/switch/run 명령 verbatim, source file list ↔ source-analysis cross-walk"
verification_date: 2026-06-03
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-programming-rules.md
  - models/SWAN/source-analysis/swan-foundation.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-parallel-implementation.md
---

# SWAN Implementation Manual (swanimp v41.51) — verified

> swanimp (Implementation Manual, Cycle III 41.51) node1-21 직접 read. **설치·빌드·실행·테스트**의 객관 레이어. swanuse(input 명세)·swantech(이론)와 별개로 "SWAN을 컴퓨터에 올리고 돌리는 절차"를 다룸. source-analysis 의 파일 인벤토리([[swan-source-coverage-audit]])와 build switch 의 1차 출처.

## 1. Implementation 5단계 (node1 verbatim)

> "Implementation involves the following steps: 1. Copying the source code … 2. If necessary, applying patches … 3. Making a few adaptions in installation-dependent parts of the code. 4. Compiling and linking … 5. Testing of the built SWAN."

→ steps 3·4 는 `switch.pl` + `make` 로 **완전 자동화 가능** (node1). 배포물: source code, **pre-built Windows release**, User/Implementation/Technical/Programming 4 docs, utilities, test cases. GitLab 호스팅 **since 41.41** ([[swan-documentation-stack]] §1과 일치).

## 2. The material — source file 인벤토리 (node2) ★

tarball `swan4151.tar.gz`. **본 표는 [[swan-source-coverage-audit]] / [[swan-foundation]] 의 1차 출처** (어떤 .ftn/.ftn90 이 무슨 역할인지 공식 분류):

| 역할 | 파일 |
|---|---|
| main program | `swanmain.ftn` |
| pre-processing | `swanpre1.ftn` `swanpre2.ftn` `SwanBndStruc.ftn90` |
| computational | `swancom1.ftn` … `swancom5.ftn` |
| post-processing | `swanout1.ftn` `swanout2.ftn` `SwanVTKWriteHeader/Data/PDataSets.ftn90` |
| service | `swanser.ftn` `SwanIntgratSpc.ftn90` |
| Bragg scattering | `SwanBraggScat.ftn90` |
| QCM | `SwanQCM.ftn90` |
| ST6 package | `SdsBabanin.ftn90` |
| parallel MPI | `swanparll.ftn` |
| unstructured grids (routines) | `SwanReadGrid/ReadADCGrid/ReadTriangleGrid/ReadEasymeshGrid`, `SwanInitCompGrid`, `SwanCheckGrid`, `SwanCreateEdges`, `SwanGridTopology/Vert/Cell/Face`, `SwanPrintGridInfo`, `SwanFindPoint`, `SwanPointinMesh`, `SwanBpntlist`, `SwanPrepComp`, `SwanVertlist`, `SwanCompUnstruc`, `SwanDispParm`, `SwanPropvelX/S`, `SwanSweepSel`, `SwanTranspAc/X`, `SwanGradDepthorK`, `SwanGradVel`, `SwanDiffPar`, `SwanGSECorr`, `SwanInterpolatePoint/Ac/Output`, `SwanConvAccur`, `SwanConvStopc`, `SwanThreadBounds`, `SwanFindObstacles`, `SwanCrossObstacle`, `SwanComputeForce` (.ftn90) |
| parallel + unstructured | `SwanParallel.ftn90` |
| netCDF | `nctablemd.ftn90` `agioncmd.ftn90` `swn_outnc.ftn90` |
| couplers | `couple2adcirc.ftn90` `swan2coh.ftn90` |
| installation | `ocpids.ftn` |
| command reading | `ocpcre.ftn` |
| miscellaneous | `ocpmix.ftn` |
| general modules | `swmod1.ftn` `swmod2.ftn` |
| XNL modules | `m_constants.ftn90` `m_fileio.ftn90` `serv_xnl4v5.ftn90` `mod_xnl4v5.ftn90` |
| unstructured modules | `SwanGriddata.ftn90` `SwanGridobjects.ftn90` `SwanCompdata.ftn90` |
| spectral partitioning | `SwanSpectPart.ftn` |
| FFT | `fftpack51.ftn90` |

- **확장자 규칙**: fixed form = `for`/`f`, free form = `f90`. 원본은 `ftn`/`ftn90` → `switch.pl`이 OS별로 변환.
- `fftpack51` = John Burkardt (FSU) 가 Fortran 90 으로 번역한 FFT 라이브러리.
- 수정 후 공식 반영 원하면 SWAN team (m.zijlema@tudelft.nl) 에 제출. DUT 는 modified version 미지원.
- 부속 파일: `INSTALL.README`, `Makefile`, `macros.inc`, `which.cmd`, `platform.pl`, `switch.pl`, `SWANRUN.README`, `swanrun`/`swanrun.bat`, `machinefile`, `swanhcat.ftn`+`hcat.nml`(hotfile 병합), `swan.edt`(edit file), `plotunswan.m`/`plotgrid.m`(unstructured Matlab).

## 3. Patch files (node3)

릴리스 사이 bug fix/feature 는 patchfile 로 배포. 명명: `41.51.A` → `B` → `C`… 적용 후 출력 버전이 `41.51ABC` 로 갱신.
```
patch -p0 < patchfile
```
→ 적용 후 **재컴파일** 필요. 브라우저 cut&paste 금지(tab 손실). Linux: CR 제거 `dos2unix` 또는 `cat 41.51.[A-C] | tr -d '\r' | patch`. Windows 는 SWAN 사이트의 patch 프로그램 사용.

## 4. Classic build — GNU make (node6-8)

빌드 전 **Perl ≥ 5.0.0** 필요(`platform.pl`/`switch.pl`). 3 run mode: serial / shared(OpenMP) / distributed(MPI).

```
make config        # macros.inc 생성 (1회, 필수 선행)
make ser           # serial
make omp           # parallel, shared (OpenMP)
make mpi           # parallel, distributed (MPI)
make clean         # object/module 정리
make clobber       # 이전 컴파일 잔여 파일 삭제
```
- Windows: Nmake(Visual Studio) 필요. OpenMP 는 Intel® Fortran 필요. MPI 는 Intel® MPI library.
- `make ser/omp/mpi` 중 **하나를 반드시 `make config` 1회로 선행**.

### 4.1 OpenMP vs MPI (node5, node7)
- **OpenMP**: 컴파일러 directive, shared-memory(laptop multi-core). 적은 thread 수에서 좋은 성능.
- **MPI**: 독립 프로세서 + interconnect(Linux cluster). MPICH/OpenMPI. **큰 시뮬레이션에서만** 유리(통신시간 ≪ 계산시간). [[swan-parallel-implementation]] 의 빌드 측 대응.
- F2003 stream I/O + F2008 OS command line 두 statement 사용(41.41+) — gfortran·Intel® Fortran 지원.

## 5. switch.pl — 소스 전처리 스위치 (node10) ★

```
perl switch.pl [-dos] [-unix] [-f95] [-jac] [-mpi] [-metis] [-cray] [-sgi]
               [-cvis] [-timg] [-matl4] [-impi] [-adcirc] [-netcdf] *.ftn
```
`!` + prefix 로 시작하는 컬럼 1-4 의 switch 를 제거하여 활성화:

| 옵션 | 효과 |
|---|---|
| `-dos`/`-unix` | TAB·dir separator 설정. `!DOS`/`!UNIX` 제거 (OCPINI in ocpids.ftn, TXPBLA in swanser.ftn). 그 외 OS 는 DIRCH1/DIRCH2/TABC/ITABVL 수동 변경. **`-unix` 는 ftn→f, ftn90→f90 자동 변환** |
| `-f95` | SWTSTA/SWTSTO 의 `CPU_TIME` 활성(`!F95`). 상세 timing (command `TEST itest=1`) |
| `-jac` | **block Jacobi**(`!JAC` 제거, `!WFR` 유지). 비/준정상 simulation 권장. **반드시 `-mpi` 뒤에** |
| (기본) | **block wavefront**(`!WFR` 자동 제거) — 수렴특성 보존(non-stationary 권장) |
| `-mpi` | `!MPI` 제거 (swanparll.ftn, swancom1.ftn, swmod1.ftn) |
| `-metis` | `!METIS` 제거 (unstructured mesh partition) |
| `-cray`/`-sgi` | `!/Cray`/`!/SGI` — 256자 초과 line RECL OPEN (OCPINI, FOR in ocpmix.ftn) |
| `-cvis` | `!CVIS` — Compaq Visual Fortran MPI 의 SHARED OPEN(Windows 다중 executable 파일열기 문제) |
| `-timg` | `!TIMG` — wall-clock/CPU timing 을 PRINT 파일에 출력 |
| `-matl4` | `!MatL4` — Level 4 MAT-File(IBM Power6 등 1-byte record 미지원). 기본은 `!MatL5`(Level 5, MATLAB 5+) |
| `-impi` | `!/impi` — `USE MPI` 미지원 컴파일러용 module MPI(swmod1.ftn) |
| `-adcirc` | `!ADC` 제거(coupled ADCIRC+SWAN). standalone 은 `!NADC` 제거 |
| `-netcdf` | `!NCF` 제거 |

예: Linux cluster + Intel® + MPI:
```
perl switch.pl -unix -f95 -mpi *.ftn *.ftn90
```
> **block Jacobi vs block wavefront** (node10 verbatim): Jacobi = subdomain interface 를 explicit 처리(높은 병렬성, 수렴특성 저하 가능). wavefront = 순차 알고리즘 연산순서 보존(수렴특성 유지, serial start-up/shut-down 으로 병렬효율 다소 저하). → 비/준정상엔 Jacobi, 그 외엔 wavefront 권장. ([[swan-parallel-implementation]] / [[swan-tech-ch7-parallel]] §7.2 와 정합)

## 6. 수동 컴파일·링크 (node11)

- F90 컴파일러 필수(F77 불가). MPI 시 `mpif90`(Intel® 은 `mpiifx`).
- ANSI F90 준수, **예외: 19 continuation line 한계 위반**(현존 컴파일러 문제없음).
- INTEGER/REAL/LOGICAL 에 동일 byte 할당 확인(보통 4 byte; 슈퍼컴은 8 — REAL 8 + INTEGER 4 면 오작동).
- binary MATLAB(unformatted) record length 1-byte 옵션: Intel® `/assume:byterecl`(Win) 또는 `-assume byterecl`(Linux).
- **module 선컴파일 순서** (node11 verbatim): `swmod1.f, swmod2.f` → `SwanSpectPart.f90` → `m_constants/m_fileio/serv_xnl4v5/mod_xnl4v5.f90` → `SwanGriddata/Gridobjects/Compdata.f90` → `SwanParallel.f90` → `SdsBabanin.f90` → `SwanIEM.f90` → `SwanBraggScat.f90` → `SwanQCM.f90`.
```
mpif90 <modules> ocp*.f swan*.f Swan*.f90 -o swan.exe
```
링크는 옵션/공유라이브러리(math, NAG) 없이. executable 은 `swan.exe` 로 rename 권장.

## 7. MPI / Metis / netCDF (node12-14)

- **MPI** (node12): Linux 는 설치 전제. Windows 는 Intel® MPI(oneAPI HPC Toolkit). `macros.inc` 에서 `INCS_MPI`/`LIBS_MPI` 비우고 `F90_MPI` 의 `ifx`→`mpiifx` 후 `make mpi`.
- **Metis** (node13): SWAN **41.45A+**. unstructured mesh 분할(distributed-memory). **multilevel k-way method**. MPI 필요. metis.h 의 `IDXTYPEWIDTH`·`REALTYPEWIDTH`=32, GKlib 필요, **Metis 5.2.1** 테스트됨. `macros.inc` 에 `METISROOT` 정의 후 `make mpi`.
- **netCDF** (node14): SWAN **40.91A+**. spectra·map 의 netCDF 출력. netCDF **4.5.x+** + Fortran interface enable. `macros.inc` 에 `NETCDFROOT` 정의.

## 8. CMake build (node15-18) — since 41.41 ★ 신규

cross-platform. **CMake 3.12+** 권장. generator 로 **Ninja**(GNU make 와 유사, 더 빠름) 권장.

```
git clone https://gitlab.tudelft.nl/citg/wavemodels/swan.git && cd swan
mkdir build && cd build         # out-of-source build (src 비오염)
cmake .. -G Ninja               # ./swan/CMakeLists.txt + ./swan/src/CMakeLists.txt
cmake --build .
cmake --install .               # 기본 /usr/local/swan (Win: C:\PROGRAM FILES\swan)
cmake --install . --prefix /your/dir
```
설치 후 `/bin`(executable) `/lib` `/mod` `/doc`(pdf) `/tools` `/misc`(machinefile, swan.edt) 생성.

### 8.1 `-D` 옵션 (node17)
| option | default |
|---|---|
| `CMAKE_INSTALL_PREFIX` | /usr/local/swan |
| `CMAKE_PREFIX_PATH` | empty |
| `CMAKE_Fortran_COMPILER` | CMake 결정 |
| `MPI` / `OPENMP` / `METIS` / `NETCDF` | **OFF** |
| `CMAKE_VERBOSE_MAKEFILE` | OFF |

예: `cmake .. -GNinja -DNETCDF=ON -DMPI=ON`. netCDF/Metis custom 경로는 `export NetCDF_ROOT=…`/`Metis_ROOT=…` 또는 `-DCMAKE_PREFIX_PATH=…`(세미콜론 구분). clean: `cmake -P clobber.cmake` (node18).

## 9. swaninit — 사용자 초기화 파일 (node19) ★

첫 실행 시 생성. 해당 디렉토리 run 에만 적용. **현행 version = 4**. 필드:

| 필드 | 기본/의미 |
|---|---|
| version | **4** (유효성 검증) |
| institute | `Delft University of Technology` (변경 가능) |
| command file ref/name | 3 / `INPUT` |
| print file ref/name | 4 / `PRINT` |
| test file ref/name | 4 / (= print) |
| screen ref | 6 (abnormal end 시 진단용) |
| highest file ref | 99999 |
| comment id | `$` (VAX 등 충돌 시 `!`) |
| TAB char | [TAB] 키 |
| dir sep char | `\` → `/` (OS별 치환) |
| time coding option | **1** (default) |
| processor speed ×N | 100 (heterogeneous machine 부하분배) |

- **time coding option** (node19 verbatim): 1 `19870530.153000`(ISO, 권장·millennium 문제없음) / 2 `30-May-87 15:30:00` / 3 `05/30/87` / 4 `15:30:00` / 5 `87/05/30` / 6 `8705301530`(WAM). **ISO 외 옵션은 유효범위 1911-01-01 ~ 2010-12-31**.
- processor speed: % of 100. 예 1.5배 빠른 노드 = `150`/`100` → 1000 active point 를 600/400 자동 분배(MPI 부하균형, [[swan-tech-ch7-parallel]] §7.1 load balancing 의 사용자측).

## 10. Run instructions (node20)

명령 파일(`.swn`) 완성 후 실행. `swan.edt` = 전체 command set template.
```
swanrun filename [nprocs]                   # Windows .bat (default nprocs=1)
./swanrun -input filename [-omp n | -mpi n]  # UNIX (chmod +rx 선행)
./swanrun -input f31har01 -omp 4 > swanout & # 예
```
- `PATH` 에 swan.exe 디렉토리 추가: `export PATH=${PATH}:/usr/local/swan` (csh: `setenv`). OpenMP: `export OMP_NUM_THREADS=4`.
- MPI run 은 `mpirun`/`mpiexec`. machinefile 1 노드/line, `node7:4`(콜론=core 수; Windows 는 space). swan.exe 를 모든 노드 공유.
- 출력: `PRINT`(MPI 면 `PRINT-001`…), table/spectra/block(사용자 이름), `Errfile`(에러 시만 생성), `ERRPTS`(비수렴 등 grid-point). hotfile 다중→단일 병합 `hcat.exe`(swanhcat.ftn, 40.51A+, `hcat.nml`).
- pre-built Windows 는 Intel® Fortran Classic + DLL → **Intel® Fortran Runtime 설치 필요**.

## 11. Testing SWAN (node21)

패키지 = `swan.exe` + `swan.edt` + `swanrun(.bat)`. 사이트의 test 입출력(`.swn` command, `.bot` bottom 등)으로 구성 테스트. **결과는 마지막 자리까지 동일할 필요 없음**. 메모리 권장: test ≥ 50 MB, 현실 case 100-500 MB, 1D < 5 MB.

## 12. 연결

- [[swan-documentation-stack]] — 4 docs TOC (본 노트가 swanimp 의 deep 화)
- [[swan-programming-rules]] — swanpgr (코드 스타일; switch/ANSI F90 한계 cross-ref)
- [[swan-source-coverage-audit]] / [[swan-foundation]] — §2 source file map 의 실제 분석
- [[swan-parallel-implementation]] / [[swan-tech-ch7-parallel]] — §5 OpenMP/MPI + §5 block Jacobi/wavefront + §9 load balancing
- 공식: http://www.swan.tudelft.nl, GitLab https://gitlab.tudelft.nl/citg/wavemodels/swan

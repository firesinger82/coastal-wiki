---
file: models/ADCIRC/raw/source_code/adcirc/docs/getting_started/index.rst
lines: 158
sha256: 23e6fdceef7c7b749247c94fc2e8f6574ecc839a3f0e5e1945af656a2e3c6378
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.rst — 판독 구간 기록

구간은 1행부터 158행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | Getting Started / Prerequisites — Fortran 컴파일러, MPI 구현, 선택 사항이지만 권장하는 NetCDF, CMake 사용 시 최소 버전, SWAN 결합(coupling) 시 Perl을 제시한다(9–15). 원문: `* Fortran compiler (gfortran, Intel Fortran)` (11); `* MPI implementation (OpenMPI, MPICH)` (12); `* NetCDF libraries (optional but recommended)` (13); `* CMake (version 3.12 or higher) if using CMake build method` (14); `* Perl (required for SWAN coupling)` (15). |
| 17–33 | Building ADCIRC / Traditional Build Method — 두 빌드 방법 중 전통적인 make 방법을 소개한다(20–32). 소스 복제와 work 디렉터리 이동 및 Intel·NetCDF 옵션을 포함하는 빌드 명령 예시이다(25–32). 원문: `    git clone https://github.com/adcirc/adcirc.git` (27); `    cd adcirc/work` (28); `    make adcirc padcirc adcprep compiler=intel NECDF=enable netcdf4=enable` (32). |
| 34–66 | CMake Build Method / 구성 — 소스 복제와 빌드 디렉터리 생성 후 기본 구성, 일반 옵션 구성 및 ccmake 대화형 구성(interactive configuration)을 제시한다(37–62). NetCDF-Fortran 설치 문제 시 경로를 명시하도록 안내한다(64–65). 원문: `    git clone https://github.com/adcirc/adcirc.git` (39); `    mkdir build` (40); `    cd build` (41); `    # Configure with defaults` (47); `    cmake ..` (48); `    ` (49); `    # Configure with common options` (50); `    cmake .. \` (51); `        -DBUILD_ADCIRC=ON \` (52); `        -DBUILD_PADCIRC=ON \` (53); `        -DBUILD_ADCPREP=ON \` (54); `        -DENABLE_OUTPUT_NETCDF=ON \` (55); `        -DCMAKE_BUILD_TYPE=Release \` (56); `    # Use cmake and ccmake for interactive option selection` (60); `    cmake ..` (61); `    ccmake ..` (62); `    # If you encounter issues with the netcdf-fortran installation, specify the path to the netcdf-fortran installation explicitly:` (64); `    ccmake .. -DNETCDF_F90_ROOT=/path/to/netcdf-fortran-install` (65). |
| 67–95 | CMake Build Method / Available build options — 실행 파일, 출력 형식, 디버그(debug), 아키텍처(architecture)별 옵션 목록이다(67–94). MPI·Perl·NetCDF 의존 조건을 해당 옵션과 함께 제시한다(71–83). 원문: `   * BUILD_ADCIRC: Build serial ADCIRC executable` (71); `   * BUILD_PADCIRC: Build parallel ADCIRC executable (requires MPI)` (72); `   * BUILD_ADCPREP: Build parallel preprocessor (requires MPI)` (73); `   * BUILD_ADCSWAN: Build serial coupled SWAN+ADCIRC (requires Perl)` (74); `   * BUILD_PADCSWAN: Build parallel coupled SWAN+ADCIRC (requires MPI and Perl)` (75); `   * BUILD_SWAN: Build serial SWAN executable` (76); `   * BUILD_PUNSWAN: Build parallel unstructured SWAN` (77); `   * BUILD_UTILITIES: Build ADCIRC utility programs` (78); `   * ENABLE_OUTPUT_NETCDF: Enable NetCDF output format` (82); `   * ENABLE_OUTPUT_XDMF: Enable XDMF output format (requires NetCDF)` (83); `   * DEBUG_FULL_STACK: Enable detailed stack trace` (87); `   * DEBUG_LOG_LEVEL: Force debug log level for screen messages` (88); `   * Various component-specific debug options (e.g., DEBUG_WIND_TRACE, DEBUG_MESH_TRACE)` (89); `   * Machine-specific optimizations for different platforms (IBM, SGI, SUN, CRAY)` (93); `   * VECTOR_COMPUTER: Enable vector computer optimizations` (94). |
| 96–106 | CMake Build Method / 빌드 — 4개 코어, 사용 가능한 모든 코어, 단일 코어의 make 예시를 제시한다(96–105). 원문: `    # Build using 4 cores` (98); `    make -j4` (99); `    ` (100); `    # Build using all available cores` (101); `    make -j` (102); `    ` (103); `    # Build using single core` (104); `    make` (105). |
| 107–129 | Running ADCIRC — 격자(mesh), 모델 매개변수와 선택 절점 속성(nodal attributes) 파일을 열거한다(110–116). 직렬 실행(serial execution)과 병렬 실행(parallel execution)의 격자 분할·입력 전처리·실행 명령을 제시한다(118–128). 원문: `   * fort.14 (mesh file)` (114); `   * fort.15 (model parameters)` (115); `   * fort.13 (optional nodal attributes)` (116); `    ./adcirc` (122); `    adcprep --np <number_of_processors> --partmesh   # partition the mesh` (126); `    adcprep --np <number_of_processors> --prepall    # prepare all the files` (127); `    mpirun -np <number_of_processors> ./padcirc      # run the parallel code` (128). |
| 130–158 | Example Run — NetCDF 출력의 사분원환 2차원 조석(tidal) 사례에 대한 테스트 저장소와 실행 예시이다(133–149). 관측 지점 수위, 전체 절점 수위와 전체 절점 속도 시계열(time series)의 출력 파일을 설명한다(151–155). 입력·출력 파일 문서 참조와 마지막 빈 줄을 포함한다(157–158). 원문: `    # Clone the ADCIRC Test Suite` (137); `    git clone https://github.com/adcirc/adcirc-testsuite.git` (138); `    # Go to the directory for a quarter annular 2D test case with netcdf format output` (140); `    cd adcirc-testsuite/adcirc/adcirc_quarterannular-2d-netcdf` (141); `    # Run ADCIRC in serial` (143); `    ./adcirc` (144); `    # Run ADCIRC in parallel with 4 processors` (146); `    adcprep --np 4 --partmesh   # partition the mesh` (147); `    adcprep --np 4 --prepall    # prepare all the files` (148); `    mpirun -np 4 ./padcirc      # run the parallel code` (149); `* fort.61.nc - elevation time series at specified stations` (153); `* fort.63.nc - elevation time series at all nodes` (154); `* fort.64.nc - velocity time series at all nodes` (155). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 25·30행: 전통 빌드 단계 번호가 `1.` 다음 `3.`으로 이어지며 `2.` 단계는 없다.
- 32행: NetCDF로 보이는 빌드 옵션 이름이 원문에서 `NECDF=enable`로 적혀 있다. 이 판독에서는 명령 실행으로 옵션의 유효성을 확인하지 않았다.
- 39–41·48행: `git clone https://github.com/adcirc/adcirc.git` 다음에 `mkdir build`, `cd build`, `cmake ..`를 제시한다. 복제한 `adcirc` 디렉터리로 이동하는 명령은 이 CMake 단계에 없다.
- 51–56행: 일반 CMake 옵션 예시의 마지막 옵션 `-DCMAKE_BUILD_TYPE=Release` 뒤에도 줄 연결 기호 `\`가 있다.

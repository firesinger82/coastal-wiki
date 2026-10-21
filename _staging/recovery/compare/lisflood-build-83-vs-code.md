# LISFLOOD-FP 빌드·8.3 배포 설명과 코드 대조

분류별 개수(5절의 고유 행 ID 기준): A 9개·B 13개·C 38개·D 0개·E 15개·F 0개·H 13개·X 0개.

## 1 요약

이 보고서는 사용자가 지정한 빌드 파일과 README·INSTALL의 빌드·실행·설정 문장을 대조한다.
이 보고서는 8.3 배포 README의 변경 표와 패치 전체를 대조한다.
이 보고서는 모델을 실행하지 않았다.
이 보고서는 빌드 도구와 외부 라이브러리를 설치하지 않았다.
이 보고서는 현재 노트를 수정하지 않는다.

README의 NUMA 경로 변수와 CUDA 아키텍처 안내 위치는 코드와 다르다.
INSTALL의 Makefile.new는 배포 파일 이름과 다르다.
8.3 패치는 최대 수심 격자·건조 NoData 원자 덧셈·flux pass 동기화·NoData 기본값·시작 판 이름을 바꾼다.
8.3 패치는 전역 sync를 바꾸고 format 파일을 삭제한다.
8.3은 Apple Metal FV1 경로를 추가한다.
패치 뒤에도 MaxField 출력 정밀도 인수와 선택적 tracer 호출의 결함 후보가 남는다.
Metal의 adaptoff 처리와 CFL 임계값은 CPU FV1과 다르다.

`현재:`의 기준 경로는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`다.
판 표시가 없는 코드 인용도 이 경로를 기준으로 한다.
`배포 README:`·`float 설정:`·`패치:`의 기준 경로는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP-8.3-package/`다.
`v8.0:`의 기준 경로는 `_staging/recovery/extract/LISFLOOD-FP/external/v8.0/LISFLOOD-FP-trunk/`다.
`v8.1:`의 기준 경로는 `_staging/recovery/extract/LISFLOOD-FP/external/v8.1/LISFLOOD-FP-trunk/`다.
`v8.2:`의 기준 경로는 `_staging/recovery/extract/LISFLOOD-FP/external/v8.2/LISFLOOD-FP/`다.
`v8.3:`의 기준 경로는 `_staging/recovery/extract/LISFLOOD-FP/external/v8.3/LISFLOOD-FP-8.3/source/`다.
`노트:`의 기준 경로는 `models/LISFLOOD-FP/`다.
README에는 쪽 번호가 없으므로 파일의 줄 번호를 인용한다.
이 작업은 제공된 매뉴얼 3종의 전체 항목을 다시 판정하는 작업이 아니다.

패치 대조는 원자료를 수정하지 않고 수행했다.
대조 스크립트는 각 hunk의 삭제·문맥 줄을 8.2 원문과 비교했다.
대조 스크립트는 메모리에서 만든 적용 결과를 현재 파일과 비교했다.
패치의 20개 경로와 35개 hunk가 모두 일치했다.
이 수는 `lisflood-8.2-to-8.3.patch`의 `diff -ruN`과 `@@`를 세어 얻었다.
패치 적용 비교에서는 CRLF와 LF를 같은 줄 구분으로 취급했다.
별도 바이트 비교에서는 v8.3 `source/` 아래 일반 파일 601개가 모두 현재 원자료의 같은 경로와 일치했다.
이 수는 v8.3 `source/`를 재귀 열거하여 얻었다.
현재 원자료에는 v8.3 축소 배포본에서 뺀 옛 빌드 파일과 매뉴얼 등이 추가로 남아 있다.

판정 열의 `일치`는 해당 문장이나 설정의 정적 대응을 뜻한다.
판정 열의 `불일치`·`문서에만`·`코드에만`은 마지막 절의 결론 한 개와 연결한다.
실행 결과가 필요한 주장은 `불일치(H)`로 표시한다.
이 표시는 주장이 거짓이라는 뜻이 아니다.
빌드 파일 사이의 값 차이는 먼저 선택 가능한 구성 차이인지 확인한다.
코드 결함 후보는 반대 근거와 적용 매크로 조건을 함께 적는다.

## 2 대조 표

### 2.1 README.md·INSTALL.md 절차

| 행 ID | 문서 원문 | 코드 원문 | 판정 | 이유 |
|---|---|---|---|---|
| LN1-001 | `README.md:2` `LISFLOOD-FP can be compiled on Windows or Linux using [CMake](https://cmake.org) version 3.13 or above.` | `CMakeLists.txt:1` `cmake_minimum_required(VERSION 3.13 FATAL_ERROR)` | 일치 | 프로젝트가 선언한 최저 CMake 판은 3.13이다. 특정 컴파일러·CUDA 조합의 성공을 실행 확인으로 확대하지 않는다. |
| LN1-002 | `README.md:5` `Launch Visual Studio 2019 and open lisflood-fp as a local folder.` | `CMakeSettings.json:5` `"name": "msvc-x64-Debug",`·`CMakeSettings.json:16` `"name": "msvc-x64-Release",` | 일치 | 로컬 폴더 CMake 구성 이름이 문서와 같다. IDE 메뉴 조작 자체는 LN1-005에서 구분한다. |
| LN1-003 | `README.md:6` `Choose the msvc-x64-Debug or msvc-x64-Release configuration, then Rebuild All.` | `CMakeSettings.json:7` `"configurationType": "Debug",`·`CMakeSettings.json:18` `"configurationType": "Release",`·`CMakeSettings.json:8,19` `"inheritEnvironments": [ "msvc_x64_x64" ],` | 일치 | 두 구성은 MSVC x64 환경을 상속한다. |
| LN1-004 | `README.md:9` `Close Visual Studio, then run launch_vs2019_intel64.bat, which assumes that Visual Studio 2019 Community Edition is installed` | `launch_vs2019_intel64.bat:1` `call "C:\Program Files (x86)\IntelSWTools\compilers_and_libraries\windows\bin\ipsxe-comp-vars.bat" intel64 vs2019`·`launch_vs2019_intel64.bat:2` `start "VS2019" /B "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe"` | 일치 | 배치 파일은 Intel 환경을 먼저 설정한다. 배치 파일은 VS2019 Community의 고정 경로를 실행한다. |
| LN1-005 | `README.md:10` `Choose the intel-x64-Debug or intel-x64-Release configuration`·`README.md:11` `Visual Studio can compile with either MSVC or Intel compiler by choosing the appropriate configuration.` | `CMakeSettings.json:27,50` `"name": "intel-x64-Debug",`·`"name": "intel-x64-Release",`·`CMakeSettings.json:38–45,61–68`의 `CMAKE_C_COMPILER`·`CMAKE_CXX_COMPILER` 값은 `icl.exe`다. | 일치 | Intel 구성은 컴파일러를 명시한다. MSVC 구성은 상속 환경을 사용한다. |
| LN1-006 | `README.md:14` `To run lisflood.exe from Visual Studio, switch the Solution Explorer to CMake Targets View` | `CMakeLists.txt:67` `add_executable(lisflood)` | 불일치(H) | 실행 대상 이름은 대응한다. IDE 화면 전환과 디버그 설정 방법은 외부 도구 사용법이다. |
| LN1-007 | `README.md:18` `Ensure a recent version of CMake is installed.`·`README.md:22` `sudo snap install cmake --classic`·`README.md:23` `sudo apt install libnuma-dev libnetcdf-dev` | `CMakeLists.txt:1` `cmake_minimum_required(VERSION 3.13 FATAL_ERROR)` | 불일치(H) | 패키지 관리자와 설치 명령은 외부 도구 사용법이다. 보고서는 이 명령을 실행하지 않았다. |
| LN1-008 | `README.md:19` `Also ensure libnuma-dev is installed` | `CMakeLists.txt:204–205` `if (UNIX AND NOT APPLE)`<br>`find_package(NUMA REQUIRED)` | 일치 | Linux 경로는 NUMA를 필수 탐색한다. Apple 경로는 8.3에서 제외했다. |
| LN1-009 | `README.md:19` `for NetCDF output and dynamic rainfall support, ensure libnetcdf-dev is also installed.` | `config.default.cmake:1` `set(_NETCDF 1)`·`CMakeLists.txt:210,218,222` `if (_NETCDF)`·`find_package(NetCDF REQUIRED)`·`target_compile_definitions(lisflood-base INTERFACE _NETCDF=1)`·`pars.cpp:999–1002` `#if (_NETCDF != 1)`<br>`fprintf(stderr, "ERROR: dynamic rain requires lisflood to be compiled with NetCDF support\n");`<br>`exit(1);`<br>`#endif` | 일치 | 기본 구성은 NetCDF를 요구한다. 동적 강우 설정은 NetCDF 비활성 빌드에서 종료한다. |
| LN1-010 | `README.md:26,29–30` `Then open a terminal at in the root lisflood-fp directory:`·`cmake -S . -B build`·`cmake --build build` | `CMakeLists.txt:8` `project(lisflood-fp)`·`CMakeLists.txt:67–69` `add_executable(lisflood)`<br>`target_sources(lisflood PRIVATE lisflood.cpp)`<br>`target_link_libraries(lisflood PRIVATE lisflood-base)` | 일치 | 명령의 소스 디렉터리는 루트 CMakeLists를 사용한다. |
| LN1-011 | `README.md:33` `The lisflood executable is written to the build directory.` | `CMakeLists.txt:67` `add_executable(lisflood)`·`CMakeSettings.json:9` `"buildRoot": "${projectDir}\\out\\build\\${name}",` | 일치 | 바로 앞 Linux 명령의 단일 구성 빌드 디렉터리에 해당한다. Windows 구성 경로를 뜻하지 않는다. |
| LN1-012 | `README.md:34,37` `If libnuma is installed in a non-standard location, use`·`cmake -S . -B build -DNUMA_ROOT=<path>` | `cmake/Modules/FindNUMA.cmake:8–14` `find_path(NUMA_INCLUDE_DIRS`<br>`NAMES numa.h numaif.h`<br>`HINTS ${NUMA_ROOT_DIR}/include)`<br>`find_library(NUMA_LIBRARIES`<br>`NAMES numa`<br>`HINTS ${NUMA_ROOT_DIR}/lib)` | 불일치(B) | 문서는 `NUMA_ROOT`를 넘긴다. 모듈은 `NUMA_ROOT_DIR`를 읽는다. v8.0·v8.1에도 같은 불일치가 있다. |
| LN1-013 | `README.md:42` `The default build configuration is given in config.default.cmake. To customise the build, copy and modify this file.` | `CMakeLists.txt:10–11` `set(_CONFIG config.default.cmake CACHE FILEPATH "CMake config file")`<br>`include(${_CONFIG})` | 일치 | `_CONFIG`를 바꾸지 않으면 기본 파일을 포함한다. |
| LN1-014 | `README.md:43,49,59–60` `edit the appropriate configuration in CMakeSettings.json:`·`"cmakeCommandArgs": "-D_CONFIG=<filename>",`·`cmake -S . -B build -D_CONFIG=<filename>`·`cmake --build build` | `CMakeLists.txt:10–11` `set(_CONFIG config.default.cmake CACHE FILEPATH "CMake config file")`<br>`include(${_CONFIG})`·`CMakeSettings.json:11,22,33,56` `"cmakeCommandArgs": "",` | 일치 | Windows와 Linux 예제는 같은 캐시 변수에 파일 이름을 넣는다. |
| LN1-015 | `README.md:64` `CMake automatically compiles LISFLOOD-FP FV1 and DG2 CUDA solvers if the [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) is installed.` | `CMakeLists.txt:72–74` `check_language(CUDA)`<br>`if (CMAKE_CUDA_COMPILER)`<br>`enable_language(CUDA)`·`CMakeLists.txt:98–117`의 FV1·FV2·DG2·ACC 소스·`CMakeLists.txt:119–175`의 acc_nugrid 소스·`CMakeLists.txt:178` `add_subdirectory(cuda/adaptive)` | 일치 | FV1과 DG2의 자동 포함은 맞는다. 조건의 정확한 판정 대상은 설치 파일의 존재가 아니라 CMake의 CUDA 컴파일러 탐색 성공이다. 추가 해법 누락은 LN1-180에서 다룬다. |
| LN1-016 | `README.md:65` `To customise the CUDA compute capabilities, see config.default.cmake.` | `CMakeLists.txt:4–6` `if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)`<br>`set(CMAKE_CUDA_ARCHITECTURES 61)`<br>`endif()`·`config.default.cmake:1–8`에는 이 변수가 없다. | 불일치(B) | 배포된 기본 설정에는 compute capability 설정이 없다. 사용자는 `-DCMAKE_CUDA_ARCHITECTURES=...`로 루트 기본값을 덮어쓸 수 있다. |
| LN1-017 | `INSTALL.md:1,3` `To compile with the new Makefile:`·`CONFIG=config/<file> make -f Makefile.new <target>` | `makefile:1` `-include $(CONFIG)`·`makefile:122` `$(eval $(call app,lisflood,lisflood.cpp))` | 불일치(B) | 실제 파일 이름은 `makefile`이다. v8.0·v8.1·v8.2에도 `INSTALL.md:3`은 같은 이름을 적는다. 해당 배포본에도 `Makefile.new`가 없다. |

`LN1-012`와 `LN1-017`의 과거 판 대조는 판 차이를 배제한다.
`v8.0:VersionHistory.h:16–18`은 `8`, `0`, `3`을 정의한다.
`v8.1:VersionHistory.h:16–18`과 `v8.2:VersionHistory.h:16–18`은 `8`, `1`, `0`을 정의한다.
`rg -i -n 'Makefile\.new|NUMA_ROOT'`는 현재 원자료 전체와 v8.0·v8.1 전체에서 문서의 잘못된 이름과 `cmake/Modules/FindNUMA.cmake:10,14`의 `NUMA_ROOT_DIR`를 찾았다.
같은 검색은 `Makefile.new`의 구현 파일이나 `NUMA_ROOT`를 직접 읽는 자체 모듈을 찾지 못했다.
이 두 행은 구현 전체 부재가 아니라 문서의 이름 오기이므로 B로 분류한다.

### 2.2 빌드 파일 전체 목록

다음 표는 파일 열거 결과 42개를 기록한다.
이 수는 지정된 이름·확장자·디렉터리를 현재 원자료에서 재귀 열거하여 얻었다.
`test/makefile`도 같은 이름의 모델 빌드 파일이므로 포함했다.
`source 집합`의 실제 파일 이름은 다음 소스 표에 모두 적는다.
이 목록 표는 파일의 선언을 기록한다.
선언 사이의 차이는 2.5절에서 별도 판정한다.

| 행 ID | 빌드 파일과 원문 줄 | 정의하는 매크로·설정 | source 집합·연결 |
|---|---|---|---|
| LN1-020 | `CMakeLists.txt:25–69,72–184,190–237` | `CMakeLists.txt:77` `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)`·`CMakeLists.txt:222,224`의 `_NETCDF=1/0`·`CMakeLists.txt:228`의 `_DEBUG` | CPU 공통 파일·`lisflood.cpp`·조건부 CUDA 전체·세 보조 실행 파일·조건부 Metal을 연결한다. C++ 표준은 `CMakeLists.txt:19` `set(CMAKE_CXX_STANDARD 14)`다. |
| LN1-021 | `CMakeSettings.json:5–70` | `msvc-x64-Debug`, `msvc-x64-Release`, `intel-x64-Debug`, `intel-x64-Release`를 정의한다. Intel 구성의 C·C++ 컴파일러 값은 `icl.exe`다. | 추가 소스나 직접 전처리 정의가 없다. 각 구성은 루트 CMakeLists를 사용한다. |
| LN1-022 | `cmake/Modules/FindNUMA.cmake:8–17,23–29` | `NUMA_ROOT_DIR`를 탐색 힌트로 읽는다. `NUMA_LIBRARIES`·`NUMA_INCLUDE_DIRS`·`NUMA::NUMA`를 제공한다. | 모델 소스와 매크로 정의가 없다. 루트는 `NUMA::NUMA` 대신 변수 값을 직접 연결한다. |
| LN1-023 | `cmake/Modules/FindNetCDF.cmake:12–35,37–54,56–96` | CMake config, pkg-config, 헤더·라이브러리 수동 탐색 순서다. `cmake/Modules/FindNetCDF.cmake:82–84` `find_package_handle_standard_args(NetCDF`<br>`REQUIRED_VARS NetCDF_LIBRARY NetCDF_INCLUDE_DIR`<br>`VERSION_VAR NetCDF_VERSION)` | 모델 소스와 전처리 정의가 없다. `NetCDF::NetCDF`를 제공한다. |
| LN1-024 | `config/aws-gcc-nvidia-t4:1–7` | `CUDA := yes`·`NETCDF := yes`·`-D_NUMERIC_MODE=1 -D_NETCDF=0`·CUDA `compute_75/sm_75` | makefile 설정이다. `NETCDF := yes`는 makefile에서 읽지 않는다. 실제 코드 값은 `_NETCDF=0`이다. |
| LN1-025 | `config/bessemer-gcc-gpu:1,3–6` | `CUDA := yes`·`-D_NUMERIC_MODE=1 -D_NETCDF=1`·CUDA `compute_70/sm_70` | makefile 설정이다. `-lgomp -lnuma -lnetcdf`를 연결한다. |
| LN1-026 | `config/bluecrystal-intel:1–2` | `-D_NUMERIC_MODE=1 -D_NETCDF=0 -D_ONLY_RECT=0` | makefile 설정이다. Intel 최적화·OpenMP 옵션을 준다. |
| LN1-027 | `config/bluecrystal3-intel:10–15` | `set(_NETCDF 1)`·`add_compile_definitions(_NUMERIC_MODE=1)`·`add_compile_definitions(_ONLY_RECT=1)` | CMake 설정이다. NetCDF include·library 절대 경로를 지정한다. |
| LN1-028 | `config/bluepebble-intel:11–14` | `_NETCDF=0`, `_NUMERIC_MODE=1`, `_ONLY_RECT=1` | CMake 설정이다. `CMAKE_CXX_FLAGS`에 Intel 옵션을 지정한다. |
| LN1-029 | `config/bluepebble-intel-netcdf:11–16` | `_NETCDF=1`, `_NUMERIC_MODE=1`, `_ONLY_RECT=1` | CMake 설정이다. NetCDF include·library 절대 경로를 지정한다. |
| LN1-030 | `config/local:1–3` | `-D_NUMERIC_MODE=1 -D_NETCDF=1` | makefile 설정이다. `-fopenmp`·`-lgomp -lnuma -lnetcdf`를 준다. |
| LN1-031 | `config/sharc-gcc-cpu:1–3` | `-D_NUMERIC_MODE=1 -D_NETCDF=0` | makefile 설정이다. `-fopenmp`·`-lgomp -lnuma`를 준다. |
| LN1-032 | `config/sharc-gcc-gpu:1–5` | `-D_NETCDF=1 -D_NUMERIC_MODE=1`·`CUDA := yes`·CUDA `compute_37/sm_37` | makefile 설정이다. `-lgomp -lnuma -lnetcdf`를 준다. |
| LN1-033 | `config/sharc-intel-cpu:1–2` | `-D_NUMERIC_MODE=1 -D_NETCDF=0 -D_ONLY_RECT=0` | makefile 설정이다. Intel 최적화·OpenMP 옵션을 준다. |
| LN1-034 | `config.default.cmake:1–8` | `_NETCDF=1`, `_NUMERIC_MODE=1`, `_ONLY_RECT=1`, `_PROFILE_MODE=0`, `_DISABLE_WET_DRY=0`, `_CALCULATE_Q_MODE=1`, `_SGM_BY_BLOCKS=0`, `_BALANCE_TYPE=0` | 루트가 기본 포함하는 CMake 설정이다. `_NETCDF`만 CMake 변수다. 나머지는 컴파일 정의다. |
| LN1-035 | `cuda/adaptive/CMakeLists.txt:1–13` | 추가 매크로가 없다. | 하위 디렉터리 7개와 `cuda_adaptive_simulate.cu`를 `lisflood`에 추가한다. |
| LN1-036 | `cuda/adaptive/input/CMakeLists.txt:4–14` | 추가 매크로가 없다. | 입력 소스 11개를 추가한다. 수는 해당 `target_sources` 항목을 센 값이다. |
| LN1-037 | `cuda/adaptive/mra/CMakeLists.txt:4–27` | 추가 매크로가 없다. | MRA 소스 24개를 추가한다. 수는 해당 `target_sources` 항목을 센 값이다. |
| LN1-038 | `cuda/adaptive/neighbours/CMakeLists.txt:4–8` | 추가 매크로가 없다. | 이웃 소스 5개를 추가한다. 수는 해당 `target_sources` 항목을 센 값이다. |
| LN1-039 | `cuda/adaptive/operators/CMakeLists.txt:4–9` | 추가 매크로가 없다. | 연산자 소스 6개를 추가한다. 수는 해당 `target_sources` 항목을 센 값이다. |
| LN1-040 | `cuda/adaptive/output/CMakeLists.txt:4–17` | 추가 매크로가 없다. | 출력 소스 14개를 추가한다. 수는 해당 `target_sources` 항목을 센 값이다. |
| LN1-041 | `cuda/adaptive/utilities/CMakeLists.txt:4–5` | 추가 매크로가 없다. | `cuda_utils.cu`·`get_num_blocks.cpp`를 추가한다. |
| LN1-042 | `cuda/adaptive/zorder/CMakeLists.txt:4–11` | 추가 매크로가 없다. | Z-order 소스 8개를 추가한다. 수는 해당 `target_sources` 항목을 센 값이다. |
| LN1-043 | `launch_vs2019_intel64.bat:1–2` | Intel 환경을 불러온다. 자체 매크로 정의가 없다. | IDE를 실행한다. 소스 목록이 없다. |
| LN1-044 | `linuxdep/build.sh:16–18,22–25,32–42` | `CC=icc`, `CXX=icpc`, `CFLAGS='-O3 -xHost -ip'`, `CXXFLAGS='-O3 -xHost -ip'` | HDF5 1.8.14와 NetCDF 4.3.2의 외부 빌드 절차다. 모델 소스나 모델 매크로를 정의하지 않는다. |
| LN1-045 | `lisflood.sln:6,10–27,30–65` | 직접 매크로가 없다. x86 solution 구성은 Win32 project 구성에 연결된다. | `"lisflood", "lisflood.vcxproj"`를 연결한다. |
| LN1-046 | `lisflood.vcxproj:162–540,542–700` | `lisflood.vcxproj:235,270` `_ONLY_RECT=0`·`lisflood.vcxproj:305,340` `_ONLY_RECT=0;_NUMERIC_MODE=0`·`lisflood.vcxproj:375,410,445,480` `_NUMERIC_MODE=0`·`lisflood.vcxproj:502,524` `WIN32;_DEBUG;_CONSOLE;%(PreprocessorDefinitions)` | CPU 공통 집합·`lisflood.cpp`·`tests.cpp`를 컴파일한다. CUDA·Metal 소스가 없다. |
| LN1-047 | `lisflood.vcxproj.filters:18–136,140–219` | 매크로가 없다. | ClCompile 40개와 ClInclude 27개는 project와 같다. 수는 XML Include 속성을 센 값이다. 이 파일은 IDE 분류를 정한다. |
| LN1-048 | `lisflood_intel.sln:6,10–14,17–26` | 직접 매크로가 없다. x64 구성만 연결한다. | `"lisflood_intel", "lisflood_intel.vcxproj"`를 연결한다. |
| LN1-049 | `lisflood_intel.vcxproj:36–56,79–231,234–313` | `lisflood_intel.vcxproj:125` `_ONLY_RECT=0`·`lisflood_intel.vcxproj:160` `_ONLY_RECT=0;_NUMERIC_MODE=0`·`lisflood_intel.vcxproj:195` `_NUMERIC_MODE=0`·`lisflood_intel.vcxproj:216` `WIN32;_DEBUG;_CONSOLE;%(PreprocessorDefinitions)` | CPU 공통 집합·`lisflood.cpp`를 컴파일한다. Toolset은 `Intel C++ Compiler 19.0`이다. |
| LN1-050 | `make_block0bal0.mk:1,3–9` | `-D _NUMERIC_MODE=0 -D _SGM_BY_BLOCKS=0 -D _BALANCE_TYPE=0` | `$(MAINOBJS)`를 재사용한다. 자체 소스 목록이 없다. |
| LN1-051 | `make_block0bal1.mk:1,3–9` | `-D _NUMERIC_MODE=0 -D _SGM_BY_BLOCKS=0 -D _BALANCE_TYPE=1` | `$(MAINOBJS)`를 재사용한다. 자체 소스 목록이 없다. |
| LN1-052 | `make_block1bal0.mk:1,3–9` | `-D _NUMERIC_MODE=0 -D _SGM_BY_BLOCKS=1 -D _BALANCE_TYPE=0` | `$(MAINOBJS)`를 재사용한다. 자체 소스 목록이 없다. |
| LN1-053 | `make_block1bal1.mk:1,3–9` | `-D _NUMERIC_MODE=0 -D _SGM_BY_BLOCKS=1 -D _BALANCE_TYPE=1` | `$(MAINOBJS)`를 재사용한다. 자체 소스 목록이 없다. |
| LN1-054 | `make_disable_vec.mk:4–11` | `-no-vec -no-simd -D _NUMERIC_MODE=0` | `$(MAINOBJS)`를 재사용한다. `-no-vec`·`-no-simd`는 컴파일러 옵션이다. |
| LN1-055 | `make_disable_wet_dry.mk:3–9` | `-D _NUMERIC_MODE=0 -D _DISABLE_WET_DRY=1` | `$(MAINOBJS)`를 재사용한다. 자체 소스 목록이 없다. |
| LN1-056 | `make_qmode1.mk:3–9` | `-D _NUMERIC_MODE=0 -D _CALCULATE_Q_MODE=1` | `$(MAINOBJS)`를 재사용한다. 자체 소스 목록이 없다. |
| LN1-057 | `make_qmode2.mk:3–9` | `-D _NUMERIC_MODE=0 -D _CALCULATE_Q_MODE=2` | `$(MAINOBJS)`를 재사용한다. 자체 소스 목록이 없다. |
| LN1-058 | `makefile:1–160` | `makefile:53–55` `ifdef CUDA`<br>`NVCCFLAGS += -Icuda/common -Icuda -ccbin $(CXX)`<br>`CXXFLAGS += -Icuda/common -Icuda -DCUDA` | CPU 집합·조건부 CUDA 일부·테스트·전처리 실행 파일을 정의한다. `CONFIG` 값으로 포함할 파일을 선택한다. |
| LN1-059 | `metal/CMakeLists.txt:3–35` | `metal/CMakeLists.txt:29` `target_compile_definitions(lisflood-metal PUBLIC METAL_ENABLED)` | `metal_integrate.cpp`·`fv1/metal_fv1_simulate.mm`를 정적 라이브러리에 넣는다. `fv1/metal_fv1_kernels.metal`은 xcrun으로 별도 컴파일한다. |
| LN1-060 | `result_check.mk:1–7` | `-D _NUMERIC_MODE=1 -D RESULT_CHECK=1` | `$(MAINOBJS)`를 재사용한다. 자체 소스 목록이 없다. |
| LN1-061 | `test/makefile:3–7,12–18` | `test/makefile:18` `$(CC_GCC) $(CFLAGS_GCC) -D _NUMERIC_MODE=1 -c $< -o $@` | 테스트 객체 5개와 외부에서 받아야 하는 `$(LISFLOOD_OBJS)`를 연결한다. |

`_CONFIG`로 포함하는 파일은 CMake 문법을 사용해야 한다.
`CONFIG`로 포함하는 파일은 make 문법을 사용해야 한다.
`config/`에는 두 문법의 파일이 함께 있다.
`config/bluecrystal3-intel:6`의 주석 명령은 `-D_CONFIG=config/bluepebble-intel-netcdf`를 적는다.
이 주석은 자기 파일을 선택하는 명령이 아니다.
이 주석이 선택하는 파일도 유효한 CMake 설정이다.
이 경로 차이만으로 컴파일 결함을 단정하지 않는다.


### 2.3 소스 목록의 전 항목 대응

다음 표는 빌드 파일에 명시된 서로 다른 소스 경로 227개를 기록한다.
이 수는 CMake source 인수와 make source 인수와 Visual Studio ClCompile 항목의 합집합을 센 값이다.
표는 하위 CMakeLists의 상대 경로를 현재 원자료 루트 경로로 환산한다.
각 인용 뒤의 백틱은 빌드 파일에 적힌 원문 토큰이다.
Visual Studio 경로의 역슬래시는 원문대로 남겼다.
`없음`은 해당 빌드 파일의 명시 목록에 없다는 뜻이다.
이 목록 표의 서로 다른 포함 범위는 LN1-100·LN1-101·LN1-102에서 판정한다.
루트 CMake의 CPU 공통 집합은 38개다.
루트 CMake의 직접 CUDA 집합은 96개다.
하위 CMake의 adaptive 집합은 71개다.
이 세 수는 각각 해당 target_sources 항목을 센 값이다.
CMake CUDA 집합은 `CMAKE_CUDA_COMPILER`가 있을 때만 포함된다.
make CUDA 집합은 `ifdef CUDA`가 참일 때만 포함된다.
Metal 집합은 `APPLE`이고 두 framework 탐색이 성공할 때만 포함된다.

| 행 ID | 소스 경로 | CMake 원문 | make 원문 | VS project 원문 | Intel project 원문 | filters 원문 |
|---|---|---|---|---|---|---|
| LN1-300 | `boundary.cpp` | `CMakeLists.txt:27` `boundary.cpp` | `makefile:6` `boundary.cpp` | `lisflood.vcxproj:542` `<ClCompile Include="boundary.cpp" />` | `lisflood_intel.vcxproj:234` `<ClCompile Include="boundary.cpp" />` | `lisflood.vcxproj.filters:18` `<ClCompile Include="boundary.cpp">` |
| LN1-301 | `ch_flow.cpp` | `CMakeLists.txt:28` `ch_flow.cpp` | `makefile:7` `ch_flow.cpp` | `lisflood.vcxproj:544` `<ClCompile Include="ch_flow.cpp" />` | `lisflood_intel.vcxproj:236` `<ClCompile Include="ch_flow.cpp" />` | `lisflood.vcxproj.filters:24` `<ClCompile Include="ch_flow.cpp">` |
| LN1-302 | `chkpnt.cpp` | `CMakeLists.txt:29` `chkpnt.cpp` | `makefile:8` `chkpnt.cpp` | `lisflood.vcxproj:543` `<ClCompile Include="chkpnt.cpp" />` | `lisflood_intel.vcxproj:235` `<ClCompile Include="chkpnt.cpp" />` | `lisflood.vcxproj.filters:21` `<ClCompile Include="chkpnt.cpp">` |
| LN1-303 | `fp_acc.cpp` | `CMakeLists.txt:30` `fp_acc.cpp` | `makefile:9` `fp_acc.cpp` | `lisflood.vcxproj:545` `<ClCompile Include="fp_acc.cpp" />` | `lisflood_intel.vcxproj:237` `<ClCompile Include="fp_acc.cpp" />` | `lisflood.vcxproj.filters:27` `<ClCompile Include="fp_acc.cpp">` |
| LN1-304 | `fp_flow.cpp` | `CMakeLists.txt:31` `fp_flow.cpp` | `makefile:10` `fp_flow.cpp` | `lisflood.vcxproj:546` `<ClCompile Include="fp_flow.cpp" />` | `lisflood_intel.vcxproj:238` `<ClCompile Include="fp_flow.cpp" />` | `lisflood.vcxproj.filters:30` `<ClCompile Include="fp_flow.cpp">` |
| LN1-305 | `fp_trent.cpp` | `CMakeLists.txt:32` `fp_trent.cpp` | `makefile:11` `fp_trent.cpp` | `lisflood.vcxproj:547` `<ClCompile Include="fp_trent.cpp" />` | `lisflood_intel.vcxproj:239` `<ClCompile Include="fp_trent.cpp" />` | `lisflood.vcxproj.filters:33` `<ClCompile Include="fp_trent.cpp">` |
| LN1-306 | `infevap.cpp` | `CMakeLists.txt:33` `infevap.cpp` | `makefile:12` `infevap.cpp` | `lisflood.vcxproj:548` `<ClCompile Include="infevap.cpp" />` | `lisflood_intel.vcxproj:240` `<ClCompile Include="infevap.cpp" />` | `lisflood.vcxproj.filters:36` `<ClCompile Include="infevap.cpp">` |
| LN1-307 | `input.cpp` | `CMakeLists.txt:34` `input.cpp` | `makefile:13` `input.cpp` | `lisflood.vcxproj:549` `<ClCompile Include="input.cpp" />` | `lisflood_intel.vcxproj:241` `<ClCompile Include="input.cpp" />` | `lisflood.vcxproj.filters:39` `<ClCompile Include="input.cpp">` |
| LN1-308 | `iterateq.cpp` | `CMakeLists.txt:35` `iterateq.cpp` | `makefile:14` `iterateq.cpp` | `lisflood.vcxproj:550` `<ClCompile Include="iterateq.cpp" />` | `lisflood_intel.vcxproj:242` `<ClCompile Include="iterateq.cpp" />` | `lisflood.vcxproj.filters:42` `<ClCompile Include="iterateq.cpp">` |
| LN1-309 | `output.cpp` | `CMakeLists.txt:36` `output.cpp` | `makefile:15` `output.cpp` | `lisflood.vcxproj:558` `<ClCompile Include="output.cpp" />` | `lisflood_intel.vcxproj:250` `<ClCompile Include="output.cpp" />` | `lisflood.vcxproj.filters:48` `<ClCompile Include="output.cpp">` |
| LN1-310 | `pars.cpp` | `CMakeLists.txt:37` `pars.cpp` | `makefile:16` `pars.cpp` | `lisflood.vcxproj:559` `<ClCompile Include="pars.cpp" />` | `lisflood_intel.vcxproj:251` `<ClCompile Include="pars.cpp" />` | `lisflood.vcxproj.filters:51` `<ClCompile Include="pars.cpp">` |
| LN1-311 | `por_flow.cpp` | `CMakeLists.txt:38` `por_flow.cpp` | `makefile:17` `por_flow.cpp` | `lisflood.vcxproj:560` `<ClCompile Include="por_flow.cpp" />` | `lisflood_intel.vcxproj:252` `<ClCompile Include="por_flow.cpp" />` | `lisflood.vcxproj.filters:54` `<ClCompile Include="por_flow.cpp">` |
| LN1-312 | `sgc.cpp` | `CMakeLists.txt:39` `sgc.cpp` | `makefile:18` `sgc.cpp` | `lisflood.vcxproj:561` `<ClCompile Include="sgc.cpp" />` | `lisflood_intel.vcxproj:253` `<ClCompile Include="sgc.cpp" />` | `lisflood.vcxproj.filters:57` `<ClCompile Include="sgc.cpp">` |
| LN1-313 | `util.cpp` | `CMakeLists.txt:40` `util.cpp` | `makefile:19` `util.cpp` | `lisflood.vcxproj:669` `<ClCompile Include="util.cpp" />` | `lisflood_intel.vcxproj:282` `<ClCompile Include="util.cpp" />` | `lisflood.vcxproj.filters:60` `<ClCompile Include="util.cpp">` |
| LN1-314 | `utility.cpp` | `CMakeLists.txt:41` `utility.cpp` | `makefile:20` `utility.cpp` | `lisflood.vcxproj:670` `<ClCompile Include="utility.cpp" />` | `lisflood_intel.vcxproj:283` `<ClCompile Include="utility.cpp" />` | `lisflood.vcxproj.filters:81` `<ClCompile Include="utility.cpp">` |
| LN1-315 | `weir_flow.cpp` | `CMakeLists.txt:42` `weir_flow.cpp` | `makefile:21` `weir_flow.cpp` | `lisflood.vcxproj:671` `<ClCompile Include="weir_flow.cpp" />` | `lisflood_intel.vcxproj:284` `<ClCompile Include="weir_flow.cpp" />` | `lisflood.vcxproj.filters:63` `<ClCompile Include="weir_flow.cpp">` |
| LN1-316 | `lisflood2/DataTypes.cpp` | `CMakeLists.txt:43` `lisflood2/DataTypes.cpp` | `makefile:22` `lisflood2/DataTypes.cpp` | `lisflood.vcxproj:552` `<ClCompile Include="lisflood2\DataTypes.cpp" />` | `lisflood_intel.vcxproj:244` `<ClCompile Include="lisflood2\DataTypes.cpp" />` | `lisflood.vcxproj.filters:87` `<ClCompile Include="lisflood2\DataTypes.cpp">` |
| LN1-317 | `lisflood2/file_tool.cpp` | `CMakeLists.txt:44` `lisflood2/file_tool.cpp` | `makefile:23` `lisflood2/file_tool.cpp` | `lisflood.vcxproj:553` `<ClCompile Include="lisflood2\file_tool.cpp" />` | `lisflood_intel.vcxproj:245` `<ClCompile Include="lisflood2\file_tool.cpp" />` | `lisflood.vcxproj.filters:66` `<ClCompile Include="lisflood2\file_tool.cpp">` |
| LN1-318 | `lisflood2/lis2_output.cpp` | `CMakeLists.txt:45` `lisflood2/lis2_output.cpp` | `makefile:24` `lisflood2/lis2_output.cpp` | `lisflood.vcxproj:556` `<ClCompile Include="lisflood2\lis2_output.cpp" />` | `lisflood_intel.vcxproj:248` `<ClCompile Include="lisflood2\lis2_output.cpp" />` | `lisflood.vcxproj.filters:78` `<ClCompile Include="lisflood2\lis2_output.cpp">` |
| LN1-319 | `lisflood2/lisflood_processing.cpp` | `CMakeLists.txt:46` `lisflood2/lisflood_processing.cpp` | `makefile:25` `lisflood2/lisflood_processing.cpp` | `lisflood.vcxproj:554` `<ClCompile Include="lisflood2\lisflood_processing.cpp" />` | `lisflood_intel.vcxproj:246` `<ClCompile Include="lisflood2\lisflood_processing.cpp" />` | `lisflood.vcxproj.filters:69` `<ClCompile Include="lisflood2\lisflood_processing.cpp">` |
| LN1-320 | `lisflood2/sgm_fast.cpp` | `CMakeLists.txt:47` `lisflood2/sgm_fast.cpp` | `makefile:26` `lisflood2/sgm_fast.cpp` | `lisflood.vcxproj:555` `<ClCompile Include="lisflood2\sgm_fast.cpp" />` | `lisflood_intel.vcxproj:247` `<ClCompile Include="lisflood2\sgm_fast.cpp" />` | `lisflood.vcxproj.filters:72` `<ClCompile Include="lisflood2\sgm_fast.cpp">` |
| LN1-321 | `lisflood2/windows_ext.cpp` | `CMakeLists.txt:48` `lisflood2/windows_ext.cpp` | `makefile:27` `lisflood2/windows_ext.cpp` | `lisflood.vcxproj:557` `<ClCompile Include="lisflood2\windows_ext.cpp" />` | `lisflood_intel.vcxproj:249` `<ClCompile Include="lisflood2\windows_ext.cpp" />` | `lisflood.vcxproj.filters:75` `<ClCompile Include="lisflood2\windows_ext.cpp">` |
| LN1-322 | `rain/rain.cpp` | `CMakeLists.txt:49` `rain/rain.cpp` | `makefile:28` `rain/rain.cpp` | `lisflood.vcxproj:562` `<ClCompile Include="rain/rain.cpp" />` | `lisflood_intel.vcxproj:254` `<ClCompile Include="rain/rain.cpp" />` | `lisflood.vcxproj.filters:135` `<ClCompile Include="rain/rain.cpp">` |
| LN1-323 | `swe/boundary.cpp` | `CMakeLists.txt:50` `swe/boundary.cpp` | `makefile:29` `swe/boundary.cpp` | `lisflood.vcxproj:563` `<ClCompile Include="swe\boundary.cpp">` | `lisflood_intel.vcxproj:255` `<ClCompile Include="swe\boundary.cpp">` | `lisflood.vcxproj.filters:90` `<ClCompile Include="swe\boundary.cpp">` |
| LN1-324 | `swe/dg2.cpp` | `CMakeLists.txt:51` `swe/dg2.cpp` | `makefile:30` `swe/dg2.cpp` | `lisflood.vcxproj:577` `<ClCompile Include="swe\dg2.cpp" />` | `lisflood_intel.vcxproj:258` `<ClCompile Include="swe\dg2.cpp" />` | `lisflood.vcxproj.filters:93` `<ClCompile Include="swe\dg2.cpp">` |
| LN1-325 | `swe/fields.cpp` | `CMakeLists.txt:52` `swe/fields.cpp` | `makefile:32` `swe/fields.cpp` | `lisflood.vcxproj:608` `<ClCompile Include="swe\fields.cpp">` | `lisflood_intel.vcxproj:268` `<ClCompile Include="swe\fields.cpp" />` | `lisflood.vcxproj.filters:96` `<ClCompile Include="swe\fields.cpp">` |
| LN1-326 | `swe/flux.cpp` | `CMakeLists.txt:53` `swe/flux.cpp` | `makefile:33` `swe/flux.cpp` | `lisflood.vcxproj:622` `<ClCompile Include="swe\flux.cpp" />` | `lisflood_intel.vcxproj:269` `<ClCompile Include="swe\flux.cpp" />` | `lisflood.vcxproj.filters:99` `<ClCompile Include="swe\flux.cpp">` |
| LN1-327 | `swe/fv1.cpp` | `CMakeLists.txt:54` `swe/fv1.cpp` | `makefile:34` `swe/fv1.cpp` | `lisflood.vcxproj:623` `<ClCompile Include="swe\fv1.cpp" />` | `lisflood_intel.vcxproj:270` `<ClCompile Include="swe\fv1.cpp" />` | `lisflood.vcxproj.filters:102` `<ClCompile Include="swe\fv1.cpp">` |
| LN1-328 | `swe/hll.cpp` | `CMakeLists.txt:55` `swe/hll.cpp` | `makefile:35` `swe/hll.cpp` | `lisflood.vcxproj:638` `<ClCompile Include="swe\hll.cpp" />` | `lisflood_intel.vcxproj:274` `<ClCompile Include="swe\hll.cpp" />` | `lisflood.vcxproj.filters:105` `<ClCompile Include="swe\hll.cpp">` |
| LN1-329 | `swe/input.cpp` | `CMakeLists.txt:56` `swe/input.cpp` | `makefile:36` `swe/input.cpp` | `lisflood.vcxproj:639` `<ClCompile Include="swe\input.cpp">` | `lisflood_intel.vcxproj:275` `<ClCompile Include="swe\input.cpp">` | `lisflood.vcxproj.filters:108` `<ClCompile Include="swe\input.cpp">` |
| LN1-330 | `swe/output.cpp` | `CMakeLists.txt:57` `swe/output.cpp` | `makefile:37` `swe/output.cpp` | `lisflood.vcxproj:653` `<ClCompile Include="swe\output.cpp">` | `lisflood_intel.vcxproj:278` `<ClCompile Include="swe\output.cpp">` | `lisflood.vcxproj.filters:111` `<ClCompile Include="swe\output.cpp">` |
| LN1-331 | `swe/stats.cpp` | `CMakeLists.txt:58` `swe/stats.cpp` | `makefile:38` `swe/stats.cpp` | `lisflood.vcxproj:667` `<ClCompile Include="swe\stats.cpp" />` | `lisflood_intel.vcxproj:281` `<ClCompile Include="swe\stats.cpp" />` | `lisflood.vcxproj.filters:114` `<ClCompile Include="swe\stats.cpp">` |
| LN1-332 | `swe/fv1/modifiedvars.cpp` | `CMakeLists.txt:59` `swe/fv1/modifiedvars.cpp` | `makefile:44` `swe/fv1/modifiedvars.cpp` | `lisflood.vcxproj:624` `<ClCompile Include="swe\fv1\modifiedvars.cpp">` | `lisflood_intel.vcxproj:271` `<ClCompile Include="swe\fv1\modifiedvars.cpp">` | `lisflood.vcxproj.filters:129` `<ClCompile Include="swe\fv1\modifiedvars.cpp">` |
| LN1-333 | `swe/dg2/dg2_output.cpp` | `CMakeLists.txt:60` `swe/dg2/dg2_output.cpp` | `makefile:39` `swe/dg2/dg2_output.cpp` | `lisflood.vcxproj:578` `<ClCompile Include="swe\dg2\dg2_output.cpp" />` | `lisflood_intel.vcxproj:259` `<ClCompile Include="swe\dg2\dg2_output.cpp" />` | `lisflood.vcxproj.filters:132` `<ClCompile Include="swe\dg2\dg2_output.cpp">` |
| LN1-334 | `swe/dg2/fields.cpp` | `CMakeLists.txt:61` `swe/dg2/fields.cpp` | `makefile:40` `swe/dg2/fields.cpp` | `lisflood.vcxproj:579` `<ClCompile Include="swe\dg2\fields.cpp">` | `lisflood_intel.vcxproj:260` `<ClCompile Include="swe\dg2\fields.cpp">` | `lisflood.vcxproj.filters:117` `<ClCompile Include="swe\dg2\fields.cpp">` |
| LN1-335 | `swe/dg2/friction.cpp` | `CMakeLists.txt:62` `swe/dg2/friction.cpp` | `makefile:41` `swe/dg2/friction.cpp` | `lisflood.vcxproj:592` `<ClCompile Include="swe\dg2\friction.cpp" />` | `lisflood_intel.vcxproj:263` `<ClCompile Include="swe\dg2\friction.cpp" />` | `lisflood.vcxproj.filters:120` `<ClCompile Include="swe\dg2\friction.cpp">` |
| LN1-336 | `swe/dg2/modifiedvars.cpp` | `CMakeLists.txt:63` `swe/dg2/modifiedvars.cpp` | `makefile:42` `swe/dg2/modifiedvars.cpp` | `lisflood.vcxproj:593` `<ClCompile Include="swe\dg2\modifiedvars.cpp">` | `lisflood_intel.vcxproj:264` `<ClCompile Include="swe\dg2\modifiedvars.cpp">` | `lisflood.vcxproj.filters:123` `<ClCompile Include="swe\dg2\modifiedvars.cpp">` |
| LN1-337 | `swe/dg2/slope_limiter.cpp` | `CMakeLists.txt:64` `swe/dg2/slope_limiter.cpp` | `makefile:43` `swe/dg2/slope_limiter.cpp` | `lisflood.vcxproj:607` `<ClCompile Include="swe\dg2\slope_limiter.cpp" />` | `lisflood_intel.vcxproj:267` `<ClCompile Include="swe\dg2\slope_limiter.cpp" />` | `lisflood.vcxproj.filters:126` `<ClCompile Include="swe\dg2\slope_limiter.cpp">` |
| LN1-338 | `lisflood.cpp` | `CMakeLists.txt:68` `lisflood.cpp` | `makefile:122` `lisflood.cpp` | `lisflood.vcxproj:551` `<ClCompile Include="lisflood.cpp" />` | `lisflood_intel.vcxproj:243` `<ClCompile Include="lisflood.cpp" />` | `lisflood.vcxproj.filters:45` `<ClCompile Include="lisflood.cpp">` |
| LN1-339 | `cuda/cuda_boundary.cu` | `CMakeLists.txt:80` `cuda/cuda_boundary.cu` | `makefile:57` `cuda/cuda_boundary.cu` | 없음 | 없음 | 없음 |
| LN1-340 | `cuda/cuda_dem.cu` | `CMakeLists.txt:81` `cuda/cuda_dem.cu` | `makefile:58` `cuda/cuda_dem.cu` | 없음 | 없음 | 없음 |
| LN1-341 | `cuda/cuda_flow.cu` | `CMakeLists.txt:82` `cuda/cuda_flow.cu` | `makefile:59` `cuda/cuda_flow.cu` | 없음 | 없음 | 없음 |
| LN1-342 | `cuda/cuda_geometry.cu` | `CMakeLists.txt:83` `cuda/cuda_geometry.cu` | `makefile:60` `cuda/cuda_geometry.cu` | 없음 | 없음 | 없음 |
| LN1-343 | `cuda/cuda_hll.cu` | `CMakeLists.txt:84` `cuda/cuda_hll.cu` | `makefile:61` `cuda/cuda_hll.cu` | 없음 | 없음 | 없음 |
| LN1-344 | `cuda/cuda_max_field.cu` | `CMakeLists.txt:85` `cuda/cuda_max_field.cu` | `makefile:62` `cuda/cuda_max_field.cu` | 없음 | 없음 | 없음 |
| LN1-345 | `cuda/cuda_rain.cu` | `CMakeLists.txt:86` `cuda/cuda_rain.cu` | `makefile:64` `cuda/cuda_rain.cu` | 없음 | 없음 | 없음 |
| LN1-346 | `cuda/cuda_sample.cu` | `CMakeLists.txt:87` `cuda/cuda_sample.cu` | `makefile:65` `cuda/cuda_sample.cu` | 없음 | 없음 | 없음 |
| LN1-347 | `cuda/cuda_simulate.cu` | `CMakeLists.txt:88` `cuda/cuda_simulate.cu` | `makefile:66` `cuda/cuda_simulate.cu` | 없음 | 없음 | 없음 |
| LN1-348 | `cuda/cuda_snapshot.cu` | `CMakeLists.txt:89` `cuda/cuda_snapshot.cu` | `makefile:68` `cuda/cuda_snapshot.cu` | 없음 | 없음 | 없음 |
| LN1-349 | `cuda/cuda_solver.cu` | `CMakeLists.txt:90` `cuda/cuda_solver.cu` | `makefile:67` `cuda/cuda_solver.cu` | 없음 | 없음 | 없음 |
| LN1-350 | `cuda/cuda_stats.cu` | `CMakeLists.txt:91` `cuda/cuda_stats.cu` | `makefile:69` `cuda/cuda_stats.cu` | 없음 | 없음 | 없음 |
| LN1-351 | `cuda/cuda_unifiedallocator.cu` | `CMakeLists.txt:92` `cuda/cuda_unifiedallocator.cu` | `makefile:63` `cuda/cuda_unifiedallocator.cu` | 없음 | 없음 | 없음 |
| LN1-352 | `cuda/cuda_util.cu` | `CMakeLists.txt:93` `cuda/cuda_util.cu` | `makefile:70` `cuda/cuda_util.cu` | 없음 | 없음 | 없음 |
| LN1-353 | `cuda/ghostraster.cpp` | `CMakeLists.txt:94` `cuda/ghostraster.cpp` | `makefile:71` `cuda/ghostraster.cpp` | 없음 | 없음 | 없음 |
| LN1-354 | `cuda/io.cpp` | `CMakeLists.txt:95` `cuda/io.cpp` | `makefile:72` `cuda/io.cpp` | 없음 | 없음 | 없음 |
| LN1-355 | `cuda/sample.cpp` | `CMakeLists.txt:96` `cuda/sample.cpp` | `makefile:73` `cuda/sample.cpp` | 없음 | 없음 | 없음 |
| LN1-356 | `cuda/stats.cpp` | `CMakeLists.txt:97` `cuda/stats.cpp` | `makefile:74` `cuda/stats.cpp` | 없음 | 없음 | 없음 |
| LN1-357 | `cuda/fv1/cuda_fv1_flow.cu` | `CMakeLists.txt:98` `cuda/fv1/cuda_fv1_flow.cu` | `makefile:75` `cuda/fv1/cuda_fv1_flow.cu` | 없음 | 없음 | 없음 |
| LN1-358 | `cuda/fv1/cuda_fv1_simulate.cu` | `CMakeLists.txt:99` `cuda/fv1/cuda_fv1_simulate.cu` | `makefile:76` `cuda/fv1/cuda_fv1_simulate.cu` | 없음 | 없음 | 없음 |
| LN1-359 | `cuda/fv1/cuda_fv1_snapshot.cu` | `CMakeLists.txt:100` `cuda/fv1/cuda_fv1_snapshot.cu` | `makefile:77` `cuda/fv1/cuda_fv1_snapshot.cu` | 없음 | 없음 | 없음 |
| LN1-360 | `cuda/fv1/cuda_fv1_solver.cu` | `CMakeLists.txt:101` `cuda/fv1/cuda_fv1_solver.cu` | `makefile:78` `cuda/fv1/cuda_fv1_solver.cu` | 없음 | 없음 | 없음 |
| LN1-361 | `cuda/fv2/cuda_fv2_dem.cu` | `CMakeLists.txt:102` `cuda/fv2/cuda_fv2_dem.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-362 | `cuda/fv2/cuda_fv2_flow.cu` | `CMakeLists.txt:103` `cuda/fv2/cuda_fv2_flow.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-363 | `cuda/fv2/cuda_fv2_simulate.cu` | `CMakeLists.txt:104` `cuda/fv2/cuda_fv2_simulate.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-364 | `cuda/fv2/cuda_fv2_slope_limit.cu` | `CMakeLists.txt:105` `cuda/fv2/cuda_fv2_slope_limit.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-365 | `cuda/fv2/cuda_fv2_snapshot.cu` | `CMakeLists.txt:106` `cuda/fv2/cuda_fv2_snapshot.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-366 | `cuda/fv2/cuda_fv2_solver.cu` | `CMakeLists.txt:107` `cuda/fv2/cuda_fv2_solver.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-367 | `cuda/dg2/cuda_dg2_dem.cu` | `CMakeLists.txt:108` `cuda/dg2/cuda_dg2_dem.cu` | `makefile:79` `cuda/dg2/cuda_dg2_dem.cu` | 없음 | 없음 | 없음 |
| LN1-368 | `cuda/dg2/cuda_dg2_flow.cu` | `CMakeLists.txt:109` `cuda/dg2/cuda_dg2_flow.cu` | `makefile:80` `cuda/dg2/cuda_dg2_flow.cu` | 없음 | 없음 | 없음 |
| LN1-369 | `cuda/dg2/cuda_dg2_simulate.cu` | `CMakeLists.txt:110` `cuda/dg2/cuda_dg2_simulate.cu` | `makefile:81` `cuda/dg2/cuda_dg2_simulate.cu` | 없음 | 없음 | 없음 |
| LN1-370 | `cuda/dg2/cuda_dg2_slope_limit.cu` | `CMakeLists.txt:111` `cuda/dg2/cuda_dg2_slope_limit.cu` | `makefile:82` `cuda/dg2/cuda_dg2_slope_limit.cu` | 없음 | 없음 | 없음 |
| LN1-371 | `cuda/dg2/cuda_dg2_snapshot.cu` | `CMakeLists.txt:112` `cuda/dg2/cuda_dg2_snapshot.cu` | `makefile:83` `cuda/dg2/cuda_dg2_snapshot.cu` | 없음 | 없음 | 없음 |
| LN1-372 | `cuda/dg2/cuda_dg2_solver.cu` | `CMakeLists.txt:113` `cuda/dg2/cuda_dg2_solver.cu` | `makefile:84` `cuda/dg2/cuda_dg2_solver.cu` | 없음 | 없음 | 없음 |
| LN1-373 | `cuda/acc/cuda_acc_flow.cu` | `CMakeLists.txt:114` `cuda/acc/cuda_acc_flow.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-374 | `cuda/acc/cuda_acc_simulate.cu` | `CMakeLists.txt:115` `cuda/acc/cuda_acc_simulate.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-375 | `cuda/acc/cuda_acc_snapshot.cu` | `CMakeLists.txt:116` `cuda/acc/cuda_acc_snapshot.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-376 | `cuda/acc/cuda_acc_solver.cu` | `CMakeLists.txt:117` `cuda/acc/cuda_acc_solver.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-377 | `cuda/acc/cuda_acc_max.cu` | `CMakeLists.txt:118` `cuda/acc/cuda_acc_max.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-378 | `cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu` | `CMakeLists.txt:119` `cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-379 | `cuda/acc_nugrid/get_num_blocks.cpp` | `CMakeLists.txt:120` `cuda/acc_nugrid/get_num_blocks.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-380 | `cuda/acc_nugrid/cuda_utils.cu` | `CMakeLists.txt:121` `cuda/acc_nugrid/cuda_utils.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-381 | `cuda/acc_nugrid/read_gauge_points.cu` | `CMakeLists.txt:122` `cuda/acc_nugrid/read_gauge_points.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-382 | `cuda/acc_nugrid/read_point_srcs.cu` | `CMakeLists.txt:123` `cuda/acc_nugrid/read_point_srcs.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-383 | `cuda/acc_nugrid/read_bdy_conds.cu` | `CMakeLists.txt:124` `cuda/acc_nugrid/read_bdy_conds.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-384 | `cuda/acc_nugrid/gen_bdy_morton_codes.cu` | `CMakeLists.txt:125` `cuda/acc_nugrid/gen_bdy_morton_codes.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-385 | `cuda/acc_nugrid/preflag_details.cu` | `CMakeLists.txt:126` `cuda/acc_nugrid/preflag_details.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-386 | `cuda/acc_nugrid/get_modal_values.cu` | `CMakeLists.txt:127` `cuda/acc_nugrid/get_modal_values.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-387 | `cuda/acc_nugrid/read_raster_file.cpp` | `CMakeLists.txt:128` `cuda/acc_nugrid/read_raster_file.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-388 | `cuda/acc_nugrid/generate_all_morton_codes.cu` | `CMakeLists.txt:129` `cuda/acc_nugrid/generate_all_morton_codes.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-389 | `cuda/acc_nugrid/sort_finest_scale_coefficients_z_order.cu` | `CMakeLists.txt:130` `cuda/acc_nugrid/sort_finest_scale_coefficients_z_order.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-390 | `cuda/acc_nugrid/copy_finest_coefficients.cu` | `CMakeLists.txt:131` `cuda/acc_nugrid/copy_finest_coefficients.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-391 | `cuda/acc_nugrid/get_max_scale_coefficients.cu` | `CMakeLists.txt:132` `cuda/acc_nugrid/get_max_scale_coefficients.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-392 | `cuda/acc_nugrid/preflag_topo.cu` | `CMakeLists.txt:133` `cuda/acc_nugrid/preflag_topo.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-393 | `cuda/acc_nugrid/encode_and_thresh_topo.cu` | `CMakeLists.txt:134` `cuda/acc_nugrid/encode_and_thresh_topo.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-394 | `cuda/acc_nugrid/get_reg_tree.cu` | `CMakeLists.txt:135` `cuda/acc_nugrid/get_reg_tree.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-395 | `cuda/acc_nugrid/reg_new.cu` | `CMakeLists.txt:136` `cuda/acc_nugrid/reg_new.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-396 | `cuda/acc_nugrid/project_assem_sol.cu` | `CMakeLists.txt:137` `cuda/acc_nugrid/project_assem_sol.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-397 | `cuda/acc_nugrid/reinsert_assem_sol.cu` | `CMakeLists.txt:138` `cuda/acc_nugrid/reinsert_assem_sol.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-398 | `cuda/acc_nugrid/traverse_tree_of_sig_details.cu` | `CMakeLists.txt:139` `cuda/acc_nugrid/traverse_tree_of_sig_details.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-399 | `cuda/acc_nugrid/reverse_z_order_assembled_solution.cu` | `CMakeLists.txt:140` `cuda/acc_nugrid/reverse_z_order_assembled_solution.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-400 | `cuda/acc_nugrid/write_reals_to_file.cu` | `CMakeLists.txt:141` `cuda/acc_nugrid/write_reals_to_file.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-401 | `cuda/acc_nugrid/write_raster_maps.cu` | `CMakeLists.txt:142` `cuda/acc_nugrid/write_raster_maps.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-402 | `cuda/acc_nugrid/write_soln_vtk.cu` | `CMakeLists.txt:143` `cuda/acc_nugrid/write_soln_vtk.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-403 | `cuda/acc_nugrid/reverse_z_order_act_idcs.cu` | `CMakeLists.txt:144` `cuda/acc_nugrid/reverse_z_order_act_idcs.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-404 | `cuda/acc_nugrid/get_compaction_flags.cu` | `CMakeLists.txt:145` `cuda/acc_nugrid/get_compaction_flags.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-405 | `cuda/acc_nugrid/compaction.cu` | `CMakeLists.txt:146` `cuda/acc_nugrid/compaction.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-406 | `cuda/acc_nugrid/count_neighbours.cu` | `CMakeLists.txt:147` `cuda/acc_nugrid/count_neighbours.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-407 | `cuda/acc_nugrid/find_nonuniform_neighbours.cu` | `CMakeLists.txt:148` `cuda/acc_nugrid/find_nonuniform_neighbours.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-408 | `cuda/acc_nugrid/count_interfaces_per_neighbours.cu` | `CMakeLists.txt:149` `cuda/acc_nugrid/count_interfaces_per_neighbours.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-409 | `cuda/acc_nugrid/sort_nghbr_assem_sol_row_major.cu` | `CMakeLists.txt:150` `cuda/acc_nugrid/sort_nghbr_assem_sol_row_major.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-410 | `cuda/acc_nugrid/init_neighbours.cu` | `CMakeLists.txt:151` `cuda/acc_nugrid/init_neighbours.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-411 | `cuda/acc_nugrid/init_interfaces.cu` | `CMakeLists.txt:152` `cuda/acc_nugrid/init_interfaces.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-412 | `cuda/acc_nugrid/find_interfaces.cu` | `CMakeLists.txt:153` `cuda/acc_nugrid/find_interfaces.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-413 | `cuda/acc_nugrid/load_interface_q_vol.cu` | `CMakeLists.txt:154` `cuda/acc_nugrid/load_interface_q_vol.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-414 | `cuda/acc_nugrid/load_neighbour_h.cu` | `CMakeLists.txt:155` `cuda/acc_nugrid/load_neighbour_h.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-415 | `cuda/acc_nugrid/compute_q.cu` | `CMakeLists.txt:156` `cuda/acc_nugrid/compute_q.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-416 | `cuda/acc_nugrid/update_h.cu` | `CMakeLists.txt:157` `cuda/acc_nugrid/update_h.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-417 | `cuda/acc_nugrid/calculate_dt.cu` | `CMakeLists.txt:158` `cuda/acc_nugrid/calculate_dt.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-418 | `cuda/acc_nugrid/get_dt_CFL.cu` | `CMakeLists.txt:159` `cuda/acc_nugrid/get_dt_CFL.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-419 | `cuda/acc_nugrid/init_h.cu` | `CMakeLists.txt:160` `cuda/acc_nugrid/init_h.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-420 | `cuda/acc_nugrid/init_q.cu` | `CMakeLists.txt:161` `cuda/acc_nugrid/init_q.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-421 | `cuda/acc_nugrid/read_all_bdy_conds.cu` | `CMakeLists.txt:162` `cuda/acc_nugrid/read_all_bdy_conds.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-422 | `cuda/acc_nugrid/read_num_stage_points.cpp` | `CMakeLists.txt:163` `cuda/acc_nugrid/read_num_stage_points.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-423 | `cuda/acc_nugrid/read_num_bdy_cells.cpp` | `CMakeLists.txt:164` `cuda/acc_nugrid/read_num_bdy_cells.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-424 | `cuda/acc_nugrid/read_num_point_srcs.cpp` | `CMakeLists.txt:165` `cuda/acc_nugrid/read_num_point_srcs.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-425 | `cuda/acc_nugrid/write_gauge_point_data.cu` | `CMakeLists.txt:166` `cuda/acc_nugrid/write_gauge_point_data.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-426 | `cuda/acc_nugrid/unifiedallocator.cu` | `CMakeLists.txt:167` `cuda/acc_nugrid/unifiedallocator.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-427 | `cuda/acc_nugrid/rain.cu` | `CMakeLists.txt:168` `cuda/acc_nugrid/rain.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-428 | `cuda/acc_nugrid/write_mass_data.cu` | `CMakeLists.txt:169` `cuda/acc_nugrid/write_mass_data.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-429 | `cuda/acc_nugrid/rain_uniform.cu` | `CMakeLists.txt:170` `cuda/acc_nugrid/rain_uniform.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-430 | `cuda/acc_nugrid/update_max.cu` | `CMakeLists.txt:171` `cuda/acc_nugrid/update_max.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-431 | `cuda/acc_nugrid/write_max_maps.cu` | `CMakeLists.txt:172` `cuda/acc_nugrid/write_max_maps.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-432 | `cuda/acc_nugrid/init_max.cu` | `CMakeLists.txt:173` `cuda/acc_nugrid/init_max.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-433 | `cuda/acc_nugrid/write_chkpnt.cu` | `CMakeLists.txt:174` `cuda/acc_nugrid/write_chkpnt.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-434 | `cuda/acc_nugrid/read_chkpnt.cu` | `CMakeLists.txt:175` `cuda/acc_nugrid/read_chkpnt.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-435 | `preprocess/generateDG2DEM.cpp` | `CMakeLists.txt:190` `preprocess/generateDG2DEM.cpp` | `makefile:131` `preprocess/generateDG2DEM.cpp` | 없음 | 없음 | 없음 |
| LN1-436 | `preprocess/generateDG2start.cpp` | `CMakeLists.txt:193` `preprocess/generateDG2start.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-437 | `postprocess/DG2downscale.cpp` | `CMakeLists.txt:196` `postprocess/DG2downscale.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-438 | `cuda/adaptive/cuda_adaptive_simulate.cu` | `cuda/adaptive/CMakeLists.txt:12` `cuda_adaptive_simulate.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-439 | `cuda/adaptive/input/read_and_project_modes_dg2.cu` | `cuda/adaptive/input/CMakeLists.txt:4` `read_and_project_modes_dg2.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-440 | `cuda/adaptive/input/read_and_project_modes_fv1.cu` | `cuda/adaptive/input/CMakeLists.txt:5` `read_and_project_modes_fv1.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-441 | `cuda/adaptive/input/read_bound_conds.cpp` | `cuda/adaptive/input/CMakeLists.txt:6` `read_bound_conds.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-442 | `cuda/adaptive/input/read_cell_size.cpp` | `cuda/adaptive/input/CMakeLists.txt:7` `read_cell_size.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-443 | `cuda/adaptive/input/read_keyword_bool.cpp` | `cuda/adaptive/input/CMakeLists.txt:8` `read_keyword_bool.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-444 | `cuda/adaptive/input/read_keyword_int.cpp` | `cuda/adaptive/input/CMakeLists.txt:9` `read_keyword_int.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-445 | `cuda/adaptive/input/read_keyword_real.cpp` | `cuda/adaptive/input/CMakeLists.txt:10` `read_keyword_real.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-446 | `cuda/adaptive/input/read_keyword_str.cpp` | `cuda/adaptive/input/CMakeLists.txt:11` `read_keyword_str.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-447 | `cuda/adaptive/input/read_raster_file.cpp` | `cuda/adaptive/input/CMakeLists.txt:12` `read_raster_file.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-448 | `cuda/adaptive/input/read_test_case.cpp` | `cuda/adaptive/input/CMakeLists.txt:13` `read_test_case.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-449 | `cuda/adaptive/input/read_command_line_params.cpp` | `cuda/adaptive/input/CMakeLists.txt:14` `read_command_line_params.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-450 | `cuda/adaptive/mra/decoding.cu` | `cuda/adaptive/mra/CMakeLists.txt:4` `decoding.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-451 | `cuda/adaptive/mra/decoding_all.cu` | `cuda/adaptive/mra/CMakeLists.txt:5` `decoding_all.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-452 | `cuda/adaptive/mra/encode_and_thresh_flow.cu` | `cuda/adaptive/mra/CMakeLists.txt:6` `encode_and_thresh_flow.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-453 | `cuda/adaptive/mra/encode_and_thresh_topo.cu` | `cuda/adaptive/mra/CMakeLists.txt:7` `encode_and_thresh_topo.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-454 | `cuda/adaptive/mra/encoding_all.cu` | `cuda/adaptive/mra/CMakeLists.txt:8` `encoding_all.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-455 | `cuda/adaptive/mra/extra_significance.cu` | `cuda/adaptive/mra/CMakeLists.txt:9` `extra_significance.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-456 | `cuda/adaptive/mra/get_max_from_array.cu` | `cuda/adaptive/mra/CMakeLists.txt:10` `get_max_from_array.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-457 | `cuda/adaptive/mra/get_max_scale_coeffs.cu` | `cuda/adaptive/mra/CMakeLists.txt:11` `get_max_scale_coeffs.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-458 | `cuda/adaptive/mra/get_modal_values.cu` | `cuda/adaptive/mra/CMakeLists.txt:12` `get_modal_values.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-459 | `cuda/adaptive/mra/get_nodal_values.cu` | `cuda/adaptive/mra/CMakeLists.txt:13` `get_nodal_values.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-460 | `cuda/adaptive/mra/get_reg_tree.cu` | `cuda/adaptive/mra/CMakeLists.txt:14` `get_reg_tree.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-461 | `cuda/adaptive/mra/init_eta_temp.cu` | `cuda/adaptive/mra/CMakeLists.txt:15` `init_eta_temp.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-462 | `cuda/adaptive/mra/init_nodal_values.cu` | `cuda/adaptive/mra/CMakeLists.txt:16` `init_nodal_values.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-463 | `cuda/adaptive/mra/init_sig_details.cu` | `cuda/adaptive/mra/CMakeLists.txt:17` `init_sig_details.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-464 | `cuda/adaptive/mra/insert_point_srcs.cu` | `cuda/adaptive/mra/CMakeLists.txt:18` `insert_point_srcs.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-465 | `cuda/adaptive/mra/modal_projections.cu` | `cuda/adaptive/mra/CMakeLists.txt:19` `modal_projections.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-466 | `cuda/adaptive/mra/preflag_details.cu` | `cuda/adaptive/mra/CMakeLists.txt:20` `preflag_details.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-467 | `cuda/adaptive/mra/preflag_topo.cu` | `cuda/adaptive/mra/CMakeLists.txt:21` `preflag_topo.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-468 | `cuda/adaptive/mra/regularisation.cu` | `cuda/adaptive/mra/CMakeLists.txt:22` `regularisation.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-469 | `cuda/adaptive/mra/refine_high_wall.cu` | `cuda/adaptive/mra/CMakeLists.txt:23` `refine_high_wall.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-470 | `cuda/adaptive/mra/reinsert_assem_sol.cu` | `cuda/adaptive/mra/CMakeLists.txt:24` `reinsert_assem_sol.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-471 | `cuda/adaptive/mra/reinsert_point_srcs.cu` | `cuda/adaptive/mra/CMakeLists.txt:25` `reinsert_point_srcs.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-472 | `cuda/adaptive/mra/traverse_tree_of_sig_details.cu` | `cuda/adaptive/mra/CMakeLists.txt:26` `traverse_tree_of_sig_details.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-473 | `cuda/adaptive/mra/zero_details.cu` | `cuda/adaptive/mra/CMakeLists.txt:27` `zero_details.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-474 | `cuda/adaptive/neighbours/add_ghost_cells.cu` | `cuda/adaptive/neighbours/CMakeLists.txt:4` `add_ghost_cells.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-475 | `cuda/adaptive/neighbours/compaction.cu` | `cuda/adaptive/neighbours/CMakeLists.txt:5` `compaction.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-476 | `cuda/adaptive/neighbours/find_neighbours.cu` | `cuda/adaptive/neighbours/CMakeLists.txt:6` `find_neighbours.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-477 | `cuda/adaptive/neighbours/get_compaction_flags.cu` | `cuda/adaptive/neighbours/CMakeLists.txt:7` `get_compaction_flags.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-478 | `cuda/adaptive/neighbours/load_soln_and_nghbr_coeffs.cu` | `cuda/adaptive/neighbours/CMakeLists.txt:8` `load_soln_and_nghbr_coeffs.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-479 | `cuda/adaptive/operators/copy_to_buf_assem_sol.cu` | `cuda/adaptive/operators/CMakeLists.txt:4` `copy_to_buf_assem_sol.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-480 | `cuda/adaptive/operators/dg2_update.cu` | `cuda/adaptive/operators/CMakeLists.txt:5` `dg2_update.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-481 | `cuda/adaptive/operators/friction_implicit.cu` | `cuda/adaptive/operators/CMakeLists.txt:6` `friction_implicit.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-482 | `cuda/adaptive/operators/fv1_update.cu` | `cuda/adaptive/operators/CMakeLists.txt:7` `fv1_update.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-483 | `cuda/adaptive/operators/get_dt_CFL.cu` | `cuda/adaptive/operators/CMakeLists.txt:8` `get_dt_CFL.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-484 | `cuda/adaptive/operators/limit_slopes.cu` | `cuda/adaptive/operators/CMakeLists.txt:9` `limit_slopes.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-485 | `cuda/adaptive/output/append_reals_to_file.cu` | `cuda/adaptive/output/CMakeLists.txt:4` `append_reals_to_file.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-486 | `cuda/adaptive/output/project_assem_sol.cu` | `cuda/adaptive/output/CMakeLists.txt:5` `project_assem_sol.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-487 | `cuda/adaptive/output/write_bool_to_file.cu` | `cuda/adaptive/output/CMakeLists.txt:6` `write_bool_to_file.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-488 | `cuda/adaptive/output/write_c_prop_data.cu` | `cuda/adaptive/output/CMakeLists.txt:7` `write_c_prop_data.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-489 | `cuda/adaptive/output/write_cumulative_data.cpp` | `cuda/adaptive/output/CMakeLists.txt:8` `write_cumulative_data.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-490 | `cuda/adaptive/output/write_stage_point_data.cu` | `cuda/adaptive/output/CMakeLists.txt:9` `write_stage_point_data.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-491 | `cuda/adaptive/output/write_int_to_file.cu` | `cuda/adaptive/output/CMakeLists.txt:10` `write_int_to_file.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-492 | `cuda/adaptive/output/write_mesh_info.cpp` | `cuda/adaptive/output/CMakeLists.txt:11` `write_mesh_info.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-493 | `cuda/adaptive/output/write_raster_file.cu` | `cuda/adaptive/output/CMakeLists.txt:12` `write_raster_file.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-494 | `cuda/adaptive/output/write_reals_to_file.cu` | `cuda/adaptive/output/CMakeLists.txt:13` `write_reals_to_file.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-495 | `cuda/adaptive/output/write_all_raster_maps.cu` | `cuda/adaptive/output/CMakeLists.txt:14` `write_all_raster_maps.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-496 | `cuda/adaptive/output/write_all_raster_maps_dg2.cu` | `cuda/adaptive/output/CMakeLists.txt:15` `write_all_raster_maps_dg2.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-497 | `cuda/adaptive/output/write_all_raster_maps_fv1.cu` | `cuda/adaptive/output/CMakeLists.txt:16` `write_all_raster_maps_fv1.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-498 | `cuda/adaptive/output/write_soln_vtk.cu` | `cuda/adaptive/output/CMakeLists.txt:17` `write_soln_vtk.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-499 | `cuda/adaptive/utilities/cuda_utils.cu` | `cuda/adaptive/utilities/CMakeLists.txt:4` `cuda_utils.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-500 | `cuda/adaptive/utilities/get_num_blocks.cpp` | `cuda/adaptive/utilities/CMakeLists.txt:5` `get_num_blocks.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-501 | `cuda/adaptive/zorder/copy_finest_coefficients.cu` | `cuda/adaptive/zorder/CMakeLists.txt:4` `copy_finest_coefficients.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-502 | `cuda/adaptive/zorder/generate_all_morton_codes.cu` | `cuda/adaptive/zorder/CMakeLists.txt:5` `generate_all_morton_codes.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-503 | `cuda/adaptive/zorder/get_sorting_indices.cu` | `cuda/adaptive/zorder/CMakeLists.txt:6` `get_sorting_indices.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-504 | `cuda/adaptive/zorder/rev_z_order_act_idcs.cu` | `cuda/adaptive/zorder/CMakeLists.txt:7` `rev_z_order_act_idcs.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-505 | `cuda/adaptive/zorder/rev_z_order_assem_sol.cu` | `cuda/adaptive/zorder/CMakeLists.txt:8` `rev_z_order_assem_sol.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-506 | `cuda/adaptive/zorder/rev_z_order_reals.cu` | `cuda/adaptive/zorder/CMakeLists.txt:9` `rev_z_order_reals.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-507 | `cuda/adaptive/zorder/sort_finest_scale_coeffs_z_order.cu` | `cuda/adaptive/zorder/CMakeLists.txt:10` `sort_finest_scale_coeffs_z_order.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-508 | `cuda/adaptive/zorder/sort_neighbours_z_order.cu` | `cuda/adaptive/zorder/CMakeLists.txt:11` `sort_neighbours_z_order.cu` | 없음 | 없음 | 없음 | 없음 |
| LN1-509 | `metal/fv1/metal_fv1_kernels.metal` | `metal/CMakeLists.txt:18` `${CMAKE_CURRENT_SOURCE_DIR}/fv1/metal_fv1_kernels.metal` | 없음 | 없음 | 없음 | 없음 |
| LN1-510 | `metal/metal_integrate.cpp` | `metal/CMakeLists.txt:23` `${CMAKE_CURRENT_SOURCE_DIR}/metal_integrate.cpp` | 없음 | 없음 | 없음 | 없음 |
| LN1-511 | `metal/fv1/metal_fv1_simulate.mm` | `metal/CMakeLists.txt:24` `${CMAKE_CURRENT_SOURCE_DIR}/fv1/metal_fv1_simulate.mm` | 없음 | 없음 | 없음 | 없음 |
| LN1-512 | `swe/dg2new.cpp` | 없음 | `makefile:31` `swe/dg2new.cpp` | 없음 | 없음 | 없음 |
| LN1-513 | `test/test_lisflood.cpp` | 없음 | `makefile:47` `test/test_lisflood.cpp` | 없음 | 없음 | 없음 |
| LN1-514 | `test/test_dg2.cpp` | 없음 | `makefile:48` `test/test_dg2.cpp` | 없음 | 없음 | 없음 |
| LN1-515 | `test/test_flux.cpp` | 없음 | `makefile:49` `test/test_flux.cpp` | 없음 | 없음 | 없음 |
| LN1-516 | `test/test_fv1.cpp` | 없음 | `makefile:50` `test/test_fv1.cpp` | 없음 | 없음 | 없음 |
| LN1-517 | `test/test_slope_limiter.cpp` | 없음 | `makefile:51` `test/test_slope_limiter.cpp` | 없음 | 없음 | 없음 |
| LN1-518 | `preprocess/create1DDamBreak.cpp` | 없음 | `makefile:124` `preprocess/create1DDamBreak.cpp` | 없음 | 없음 | 없음 |
| LN1-519 | `preprocess/createDamBreakObstacle.cpp` | 없음 | `makefile:125` `preprocess/createDamBreakObstacle.cpp` | 없음 | 없음 | 없음 |
| LN1-520 | `preprocess/createHump.cpp` | 없음 | `makefile:126` `preprocess/createHump.cpp` | 없음 | 없음 | 없음 |
| LN1-521 | `preprocess/createLakeAtRestCones.cpp` | 없음 | `makefile:127` `preprocess/createLakeAtRestCones.cpp` | 없음 | 없음 | 없음 |
| LN1-522 | `preprocess/createLakeAtRestBlocks.cpp` | 없음 | `makefile:128` `preprocess/createLakeAtRestBlocks.cpp` | 없음 | 없음 | 없음 |
| LN1-523 | `preprocess/createRadialDamBreak.cpp` | 없음 | `makefile:129` `preprocess/createRadialDamBreak.cpp` | 없음 | 없음 | 없음 |
| LN1-524 | `preprocess/checkDynamicRain.cpp` | 없음 | `makefile:130` `preprocess/checkDynamicRain.cpp` | 없음 | 없음 | 없음 |
| LN1-525 | `preprocess/hll_util.cpp` | 없음 | `makefile:132` `preprocess/hll_util.cpp` | 없음 | 없음 | 없음 |
| LN1-526 | `tests.cpp` | 없음 | 없음 | `lisflood.vcxproj:668` `<ClCompile Include="tests.cpp" />` | 없음 | `lisflood.vcxproj.filters:84` `<ClCompile Include="tests.cpp">` |

### 2.4 매크로 값과 코드의 전처리 조건

이 절은 CMake 변수와 C/C++ 전처리 매크로를 구분한다.
`set(_NETCDF 1)`은 CMake 변수 대입이다.
루트 CMakeLists는 그 값을 `_NETCDF=1` 또는 `_NETCDF=0` 컴파일 정의로 바꾼다.
`CUDA := yes`는 make 변수 대입이다.
makefile의 `ifdef CUDA`는 비어 있지 않은 값을 검사한다.
따라서 `CUDA := no`도 그 분기를 켠다.
`CMAKE_CUDA_ARCHITECTURES`와 `METAL_ENABLED TRUE PARENT_SCOPE`는 그 자체로 C++ 매크로 정의가 아니다.
Metal 라이브러리의 PUBLIC 컴파일 정의가 `lisflood`의 `METAL_ENABLED`를 제공한다.
`WIN32`, `_CONSOLE`, `THRUST_IGNORE_CUB_VERSION_CHECK`도 빌드 파일에 실제로 나타나는 정의로 포함했다.

| 행 ID | 매크로 | 빌드 파일의 값 | 코드의 원문 조건·작용 | 판정 |
|---|---|---|---|---|
| LN1-070 | `_NETCDF` | 기본 CMake·float 설정은 1이다. bluepebble-intel은 0이다. NetCDF CMake 설정 둘은 1이다. make config의 값은 2.2절과 같다. VS는 직접 정의하지 않는다. | `lisflood.h:51–53` `#ifndef _NETCDF`<br>`#define _NETCDF 1`<br>`#endif`·`rain/rain.cpp:3` `#if _NETCDF == 1`·`cuda/cuda_rain.cu:5,46,98` `#if _NETCDF == 1`·`pars.cpp:999` `#if (_NETCDF != 1)` | 일치 |
| LN1-071 | `_NUMERIC_MODE` | 기본 CMake·make config·VS double은 1이다. float 설정·VS float·변형 `.mk`는 0이다. | `lisflood.h:75–87` `#if _NUMERIC_MODE == 1` 뒤 `#define NUMERIC_TYPE double`을 선택한다. `#else` 뒤 `#define NUMERIC_TYPE float`을 선택한다. `lisflood2/file_tool.cpp:16`·`lisflood2/file_tool.h:15`·`cuda/adaptive/types/real.h:3`도 같은 값을 검사한다. | 일치 |
| LN1-072 | `_ONLY_RECT` | 기본 CMake는 1이다. bluecrystal-intel·sharc-intel-cpu와 VS all_channel은 0이다. 그 밖의 미정의 경로는 헤더 기본값 1이다. | `lisflood.h:42–44` `#ifndef _ONLY_RECT`<br>`#define _ONLY_RECT 1`<br>`#endif`·`lisflood2/sgm_fast.cpp:142` `#if defined _ONLY_RECT && _ONLY_RECT == 1` | 일치 |
| LN1-073 | `_PROFILE_MODE` | 기본 CMake와 float 설정은 0이다. 다른 경로의 미정의 값도 `lisflood.h:40`에서 0이다. | `lisflood2/sgm_fast.cpp:18` `#if defined (__INTEL_COMPILER) && _PROFILE_MODE > 0`·`lisflood2/sgm_fast.cpp:4670` `#if _PROFILE_MODE < 2`·`lisflood2/sgm_fast.cpp:4837–4839` `#if _PROFILE_MODE > 1`<br>`//force stop`<br>`exit(0);` | 일치 |
| LN1-074 | `_DISABLE_WET_DRY` | 기본 CMake와 float 설정은 0이다. `make_disable_wet_dry.mk:9`는 1이다. | `lisflood2/sgm_fast.cpp:4219–4225` `#if _DISABLE_WET_DRY == 1` 분기에서 각 행의 `fp_h[j].start = 0;`·`fp_h[j].end = grid_cols;`를 대입한다. | 일치 |
| LN1-075 | `_CALCULATE_Q_MODE` | 기본 CMake·헤더는 1이다. make_qmode1은 1이다. make_qmode2는 2다. | `lisflood2/sgm_fast.cpp:58,74,95` `#if _CALCULATE_Q_MODE == 0`·`#if _CALCULATE_Q_MODE == 1`·`#if _CALCULATE_Q_MODE == 2`·`pars.cpp:926` `#if _CALCULATE_Q_MODE != 1` | 일치 |
| LN1-076 | `_SGM_BY_BLOCKS` | 기본 CMake·헤더는 0이다. block0 변형은 0이다. block1 변형은 1이다. | `lisflood2/lisflood_processing.cpp:1793` `#if _SGM_BY_BLOCKS == 1`·`lisflood2/sgm_fast.cpp:3639,3656,3834` `#if _SGM_BY_BLOCKS == 0`·`#if _SGM_BY_BLOCKS == 1` | 일치 |
| LN1-077 | `_BALANCE_TYPE` | 기본 CMake·헤더는 0이다. bal0 변형은 0이다. bal1 변형은 1이다. | `lisflood2/sgm_fast.cpp:3322,3356,3377,3967` `#if _BALANCE_TYPE == 1`·`lisflood2/sgm_fast.cpp:3325` `int work_this_row = ((row_end == -1) ? 0 : (row_end - row_start)) + 10;`·`lisflood2/sgm_fast.cpp:3327` `int work_this_row = 1;` | 일치 |
| LN1-078 | `RESULT_CHECK` | `result_check.mk:7`의 값은 1이다. 기본 CMake·make config·VS에는 정의가 없다. | `lisflood2/lisflood_processing.cpp:1536,2092` `#ifndef RESULT_CHECK`·`lisflood2/lisflood_processing.cpp:2161` `#ifdef RESULT_CHECK`·`lisflood2/sgm_fast.cpp:3458,4027,4101,4115,4165,4276`의 존재 검사·`sgc.cpp:726` `#ifdef RESULT_CHECK` | 일치 |
| LN1-079 | `CUDA` | 루트 CMake는 CUDA 컴파일러 탐색 성공 시 정의한다. makefile은 make 변수 CUDA의 `ifdef`가 참이면 `-DCUDA`를 추가한다. VS project에는 정의가 없다. | `lisflood.cpp:22,419` `#ifdef CUDA`·`lisflood.cpp:893` `#if defined (CUDA)`·`pars.cpp:1080` `#if !defined(CUDA) && !defined(METAL_ENABLED)` | 일치 |
| LN1-080 | `METAL_ENABLED` | `metal/CMakeLists.txt:29` `target_compile_definitions(lisflood-metal PUBLIC METAL_ENABLED)` | `lisflood.cpp:30,780` `#ifdef METAL_ENABLED`·`pars.cpp:1080` `#if !defined(CUDA) && !defined(METAL_ENABLED)` | 일치 |
| LN1-081 | `_DEBUG` | CMake Debug는 정의한다. VS Debug는 정의한다. make 설정에는 정의가 없다. | `lisflood2/sgm_fast.cpp:3106` `#if _DEBUG`·그 밖의 `#ifdef _DEBUG`는 다음 전처리 파일 표에 모두 적었다. | 일치 |
| LN1-082 | `WIN32`·`_CONSOLE` | VS Debug의 `PreprocessorDefinitions`에 있다. | `cuda/common/helper_functions.h:33` `#ifdef WIN32`·`cuda/common/helper_string.h:37` `#if defined(WIN32) \|\| defined(_WIN32) \|\| defined(WIN64) \|\| defined(_WIN64)`·모델 본체에는 `_CONSOLE` 조건이 없다. | 코드에만(C) |
| LN1-083 | `THRUST_IGNORE_CUB_VERSION_CHECK` | `CMakeLists.txt:77` `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)` | 모델 소스는 이 이름을 조건문에서 읽지 않는다. 외부 Thrust/CUB 헤더에 전달하는 정의다. | 코드에만(C) |

`RESULT_CHECK=0`도 존재 검사 분기를 켠다.
기본 CMake는 이 매크로를 아예 정의하지 않는다.
`_NUMERIC_MODE`는 정확히 1일 때만 double을 선택한다.
`_CALCULATE_Q_MODE=1`만 Froude 제한을 적용한다.
`_CALCULATE_Q_MODE=0`은 `CBRT(R*R*R*R)`를 사용한다.
`_CALCULATE_Q_MODE=2`는 `POW(R, C(4.0)/C(3.0))`를 사용한다.
다른 값도 `lisflood2/sgm_fast.cpp:107`의 마지막 분기를 선택하므로 잘못된 값 검사가 아니다.
이 구별은 같은 결과를 보장하는 단순 최적화 선택으로 요약할 수 없다.

전처리 조건의 전 파일 목록은 다음과 같다.
열거 범위는 루트의 `.cpp`·`.h`와 `lisflood2/`, `rain/`, `swe/`, `cuda/`, `metal/`, `preprocess/`, `postprocess/`, `test/`의 `.cpp`·`.h`·`.cu`·`.cuh`·`.mm`·`.metal`이다.
해당 파일 579개에서 블록 주석과 줄 주석을 제외하고 조건 지시문 224개를 찾았다.
조건 지시문을 가진 파일은 36개다.
이 세 수는 원문을 `nl -ba`로 읽은 뒤 조건 지시문을 추출하여 얻었다.
이 표는 분기 내부의 모든 수치 알고리즘을 별도 검증했다는 뜻이 아니다.
`cuda/common/helper_*`의 외부 SDK 이름은 호출 경계의 전처리 목록으로만 기록한다.

| 행 ID | 조건을 쓰는 파일 | 조건 지시문 원문 전부 |
|---|---|---|
| LN1-600 | `cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh` | `cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:3` `#ifndef THREADS_PER_BLOCK_MRA`<br>`cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:7` `#if   THREADS_PER_BLOCK_MRA == 64`<br>`cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:11` `#elif THREADS_PER_BLOCK_MRA == 256`<br>`cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:15` `#elif THREADS_PER_BLOCK_MRA == 1024`<br>`cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:22` `#ifndef NUM_VARS`<br>`cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:26` `#ifndef NUM_CHILDREN`<br>`cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:30` `#ifndef SIGNIFICANT`<br>`cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:34` `#ifndef INSIGNIFICANT` |
| LN1-601 | `cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu` | `cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:2` `#ifdef __INTELLISENSE__`<br>`cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:3` `#ifndef __CUDACC__` |
| LN1-602 | `cuda/acc_nugrid/rain.cu` | `cuda/acc_nugrid/rain.cu:6` `#if _NETCDF == 1`<br>`cuda/acc_nugrid/rain.cu:56` `#if _NETCDF == 1` |
| LN1-603 | `cuda/acc_nugrid/sort_finest_scale_coefficients_z_order.cuh` | `cuda/acc_nugrid/sort_finest_scale_coefficients_z_order.cuh:3` `#ifndef __CUDACC__` |
| LN1-604 | `cuda/adaptive/classes/Tracer.h` | `cuda/adaptive/classes/Tracer.h:5` `#if _USE_TRACER == 1` |
| LN1-605 | `cuda/adaptive/mra/extra_significance.cuh` | `cuda/adaptive/mra/extra_significance.cuh:3` `#ifndef M_BAR` |
| LN1-606 | `cuda/adaptive/types/real.h` | `cuda/adaptive/types/real.h:3` `#if _NUMERIC_MODE == 1` |
| LN1-607 | `cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh` | `cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh:3` `#ifndef THREADS_PER_BLOCK`<br>`cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh:7` `#if   THREADS_PER_BLOCK == 64`<br>`cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh:11` `#elif THREADS_PER_BLOCK == 256`<br>`cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh:15` `#elif THREADS_PER_BLOCK == 1024`<br>`cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh:22` `#ifndef SIGNIFICANT`<br>`cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh:26` `#ifndef INSIGNIFICANT` |
| LN1-608 | `cuda/common/helper_cuda.h` | `cuda/common/helper_cuda.h:31` `#ifndef COMMON_HELPER_CUDA_H_`<br>`cuda/common/helper_cuda.h:43` `#ifndef EXIT_WAIVED`<br>`cuda/common/helper_cuda.h:52` `#ifdef __DRIVER_TYPES_H__`<br>`cuda/common/helper_cuda.h:58` `#ifdef CUDA_DRIVER_API`<br>`cuda/common/helper_cuda.h:68` `#ifdef CUBLAS_API_H_`<br>`cuda/common/helper_cuda.h:107` `#ifdef _CUFFT_H_`<br>`cuda/common/helper_cuda.h:167` `#ifdef CUSPARSEAPI`<br>`cuda/common/helper_cuda.h:203` `#ifdef CUSOLVER_COMMON_H_`<br>`cuda/common/helper_cuda.h:237` `#ifdef CURAND_H_`<br>`cuda/common/helper_cuda.h:285` `#ifdef NVJPEGAPI`<br>`cuda/common/helper_cuda.h:321` `#ifdef NV_NPPIDEFS_H`<br>`cuda/common/helper_cuda.h:337` `#if ((NPP_VERSION_MAJOR << 12) + (NPP_VERSION_MINOR << 4)) <= 0x5000`<br>`cuda/common/helper_cuda.h:417` `#if ((NPP_VERSION_MAJOR << 12) + (NPP_VERSION_MINOR << 4)) <= 0x5000`<br>`cuda/common/helper_cuda.h:484` `#if ((NPP_VERSION_MAJOR << 12) + (NPP_VERSION_MINOR << 4)) >= 0x6000`<br>`cuda/common/helper_cuda.h:568` `#if ((NPP_VERSION_MAJOR << 12) + (NPP_VERSION_MINOR << 4)) >= 0x7000`<br>`cuda/common/helper_cuda.h:582` `#ifdef __DRIVER_TYPES_H__`<br>`cuda/common/helper_cuda.h:583` `#ifndef DEVICE_RESET`<br>`cuda/common/helper_cuda.h:587` `#ifndef DEVICE_RESET`<br>`cuda/common/helper_cuda.h:604` `#ifdef __DRIVER_TYPES_H__`<br>`cuda/common/helper_cuda.h:645` `#ifndef MAX`<br>`cuda/common/helper_cuda.h:701` `#ifdef __CUDA_RUNTIME_H__` |
| LN1-609 | `cuda/common/helper_functions.h` | `cuda/common/helper_functions.h:30` `#ifndef COMMON_HELPER_FUNCTIONS_H_`<br>`cuda/common/helper_functions.h:33` `#ifdef WIN32`<br>`cuda/common/helper_functions.h:55` `#ifndef EXIT_WAIVED` |
| LN1-610 | `cuda/common/helper_string.h` | `cuda/common/helper_string.h:29` `#ifndef COMMON_HELPER_STRING_H_`<br>`cuda/common/helper_string.h:37` `#if defined(WIN32) \|\| defined(_WIN32) \|\| defined(WIN64) \|\| defined(_WIN64)`<br>`cuda/common/helper_string.h:38` `#ifndef _CRT_SECURE_NO_DEPRECATE`<br>`cuda/common/helper_string.h:41` `#ifndef STRCASECMP`<br>`cuda/common/helper_string.h:44` `#ifndef STRNCASECMP`<br>`cuda/common/helper_string.h:47` `#ifndef STRCPY`<br>`cuda/common/helper_string.h:51` `#ifndef FOPEN`<br>`cuda/common/helper_string.h:54` `#ifndef FOPEN_FAIL`<br>`cuda/common/helper_string.h:57` `#ifndef SSCANF`<br>`cuda/common/helper_string.h:60` `#ifndef SPRINTF`<br>`cuda/common/helper_string.h:67` `#ifndef STRCASECMP`<br>`cuda/common/helper_string.h:70` `#ifndef STRNCASECMP`<br>`cuda/common/helper_string.h:73` `#ifndef STRCPY`<br>`cuda/common/helper_string.h:77` `#ifndef FOPEN`<br>`cuda/common/helper_string.h:80` `#ifndef FOPEN_FAIL`<br>`cuda/common/helper_string.h:83` `#ifndef SSCANF`<br>`cuda/common/helper_string.h:86` `#ifndef SPRINTF`<br>`cuda/common/helper_string.h:91` `#ifndef EXIT_WAIVED`<br>`cuda/common/helper_string.h:304` `#if defined(WIN32) \|\| defined(_WIN32) \|\| defined(WIN64) \|\| defined(_WIN64)`<br>`cuda/common/helper_string.h:338` `#ifdef _DEBUG` |
| LN1-611 | `cuda/cuda_atomic.cuh` | `cuda/cuda_atomic.cuh:5` `#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ < 600` |
| LN1-612 | `cuda/cuda_rain.cu` | `cuda/cuda_rain.cu:5` `#if _NETCDF == 1`<br>`cuda/cuda_rain.cu:46` `#if _NETCDF == 1`<br>`cuda/cuda_rain.cu:98` `#if _NETCDF == 1` |
| LN1-613 | `lisflood.cpp` | `lisflood.cpp:22` `#ifdef CUDA`<br>`lisflood.cpp:30` `#ifdef METAL_ENABLED`<br>`lisflood.cpp:39` `#ifdef TESTING`<br>`lisflood.cpp:419` `#ifdef CUDA`<br>`lisflood.cpp:780` `#ifdef METAL_ENABLED`<br>`lisflood.cpp:862` `#if defined (__INTEL_COMPILER)`<br>`lisflood.cpp:867` `#if defined (__AVX2__)`<br>`lisflood.cpp:870` `#if defined (__AVX__)`<br>`lisflood.cpp:873` `#if defined (__SSE4_2__)`<br>`lisflood.cpp:876` `#if defined (__SSE4_1__)`<br>`lisflood.cpp:879` `#if defined (__SSE3__)`<br>`lisflood.cpp:882` `#if defined (__SSE2__)`<br>`lisflood.cpp:885` `#if defined (__SSE__)`<br>`lisflood.cpp:893` `#if defined (CUDA)`<br>`lisflood.cpp:896` `#if defined (_PROFILE_MODE) && _PROFILE_MODE > 0`<br>`lisflood.cpp:899` `#if defined (_SGM_BY_BLOCKS) && _SGM_BY_BLOCKS > 0`<br>`lisflood.cpp:902` `#if defined (_BALANCE_TYPE) && _BALANCE_TYPE > 0`<br>`lisflood.cpp:905` `#if defined (_ONLY_RECT) && _ONLY_RECT == 1`<br>`lisflood.cpp:908` `#if defined (_DISABLE_WET_DRY) && _DISABLE_WET_DRY == 1`<br>`lisflood.cpp:911` `#if defined (_CALCULATE_Q_MODE) && (_CALCULATE_Q_MODE != 0)` |
| LN1-614 | `lisflood.h` | `lisflood.h:25` `#ifndef _SGM_BY_BLOCKS`<br>`lisflood.h:30` `#ifndef _BALANCE_TYPE`<br>`lisflood.h:36` `#ifndef _NUMERIC_MODE`<br>`lisflood.h:39` `#ifndef _PROFILE_MODE`<br>`lisflood.h:42` `#ifndef _ONLY_RECT`<br>`lisflood.h:45` `#ifndef _DISABLE_WET_DRY`<br>`lisflood.h:48` `#ifndef _CALCULATE_Q_MODE`<br>`lisflood.h:51` `#ifndef _NETCDF`<br>`lisflood.h:56` `#ifdef TESTING`<br>`lisflood.h:59` `#ifdef _MSC_VER`<br>`lisflood.h:63` `#ifdef _DEBUG`<br>`lisflood.h:68` `#ifndef cbrt`<br>`lisflood.h:71` `#ifndef cbrtf`<br>`lisflood.h:75` `#if _NUMERIC_MODE == 1`<br>`lisflood.h:99` `#ifdef __unix__`<br>`lisflood.h:102` `#elif __APPLE__`<br>`lisflood.h:110` `#if _XOPEN_SOURCE >= 600 \|\| _ISOC99_SOURCE \|\| _POSIX_C_SOURCE >= 200112L \|\| _MSC_VER >= 1800`<br>`lisflood.h:116` `#if _XOPEN_SOURCE >= 600 \|\| _ISOC99_SOURCE \|\| _POSIX_C_SOURCE >= 200112L \|\| _MSC_VER >= 1800` |
| LN1-615 | `lisflood2/file_tool.cpp` | `lisflood2/file_tool.cpp:7` `#if _NETCDF == 1`<br>`lisflood2/file_tool.cpp:16` `#if _NUMERIC_MODE == 1`<br>`lisflood2/file_tool.cpp:36` `#if _NETCDF == 1`<br>`lisflood2/file_tool.cpp:191` `#ifdef LATLONGMODE`<br>`lisflood2/file_tool.cpp:296` `#ifdef LATLONGMODE`<br>`lisflood2/file_tool.cpp:428` `#if _NETCDF == 1`<br>`lisflood2/file_tool.cpp:438` `#if _NETCDF == 1`<br>`lisflood2/file_tool.cpp:764` `#if _NETCDF == 1` |
| LN1-616 | `lisflood2/file_tool.h` | `lisflood2/file_tool.h:15` `#if _NUMERIC_MODE == 1` |
| LN1-617 | `lisflood2/lis2_output.cpp` | `lisflood2/lis2_output.cpp:83` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)` |
| LN1-618 | `lisflood2/lisflood2.h` | `lisflood2/lisflood2.h:5` `#if defined(_MSC_VER)` |
| LN1-619 | `lisflood2/lisflood_processing.cpp` | `lisflood2/lisflood_processing.cpp:19` `#ifdef __unix__`<br>`lisflood2/lisflood_processing.cpp:295` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:502` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:659` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1317` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1323` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1377` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1383` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1536` `#ifndef RESULT_CHECK`<br>`lisflood2/lisflood_processing.cpp:1631` `#if (_NETCDF == 1)`<br>`lisflood2/lisflood_processing.cpp:1729` `#ifdef __unix__`<br>`lisflood2/lisflood_processing.cpp:1758` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1763` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1784` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1793` `#if _SGM_BY_BLOCKS == 1`<br>`lisflood2/lisflood_processing.cpp:1802` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:1868` `#ifdef _DEBUG`<br>`lisflood2/lisflood_processing.cpp:2092` `#ifndef RESULT_CHECK`<br>`lisflood2/lisflood_processing.cpp:2161` `#ifdef RESULT_CHECK` |
| LN1-620 | `lisflood2/sgm_fast.cpp` | `lisflood2/sgm_fast.cpp:18` `#if defined (__INTEL_COMPILER) && _PROFILE_MODE > 0`<br>`lisflood2/sgm_fast.cpp:58` `#if _CALCULATE_Q_MODE == 0`<br>`lisflood2/sgm_fast.cpp:74` `#if _CALCULATE_Q_MODE == 1`<br>`lisflood2/sgm_fast.cpp:95` `#if _CALCULATE_Q_MODE == 2`<br>`lisflood2/sgm_fast.cpp:142` `#if defined _ONLY_RECT && _ONLY_RECT == 1`<br>`lisflood2/sgm_fast.cpp:216` `#if defined _ONLY_RECT && _ONLY_RECT == 1`<br>`lisflood2/sgm_fast.cpp:1121` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:1128` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:1221` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:1230` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:1249` `#ifdef _DEBUG`<br>`lisflood2/sgm_fast.cpp:1269` `#ifdef _DEBUG`<br>`lisflood2/sgm_fast.cpp:1450` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:1454` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:1630` `#ifdef _DEBUG`<br>`lisflood2/sgm_fast.cpp:1653` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:1662` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:1751` `#ifdef _DEBUG`<br>`lisflood2/sgm_fast.cpp:1771` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:1780` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:1864` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:1910` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:1959` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:1996` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:3031` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:3037` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:3106` `#if _DEBUG`<br>`lisflood2/sgm_fast.cpp:3170` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:3177` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:3199` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:3211` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:3262` `#if defined(_MSC_VER) && !defined(__INTEL_COMPILER)`<br>`lisflood2/sgm_fast.cpp:3281` `#if defined(_MSC_VER) && !defined(__INTEL_COMPILER)`<br>`lisflood2/sgm_fast.cpp:3310` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:3322` `#if _BALANCE_TYPE == 1`<br>`lisflood2/sgm_fast.cpp:3339` `#ifdef _DEBUG`<br>`lisflood2/sgm_fast.cpp:3356` `#if _BALANCE_TYPE == 1`<br>`lisflood2/sgm_fast.cpp:3366` `#ifdef _DEBUG`<br>`lisflood2/sgm_fast.cpp:3377` `#if _BALANCE_TYPE == 1`<br>`lisflood2/sgm_fast.cpp:3404` `#ifdef _DEBUG`<br>`lisflood2/sgm_fast.cpp:3428` `#ifdef __INTEL_COMPILER`<br>`lisflood2/sgm_fast.cpp:3435` `#if defined(__INTEL_COMPILER) \|\| defined(_MSC_VER)`<br>`lisflood2/sgm_fast.cpp:3458` `#ifdef RESULT_CHECK`<br>`lisflood2/sgm_fast.cpp:3639` `#if _SGM_BY_BLOCKS == 0`<br>`lisflood2/sgm_fast.cpp:3656` `#if _SGM_BY_BLOCKS == 1`<br>`lisflood2/sgm_fast.cpp:3834` `#if _SGM_BY_BLOCKS == 1`<br>`lisflood2/sgm_fast.cpp:3866` `#if defined(_MSC_VER) && !defined(__INTEL_COMPILER)`<br>`lisflood2/sgm_fast.cpp:3891` `#if defined(_MSC_VER) && !defined(__INTEL_COMPILER)`<br>`lisflood2/sgm_fast.cpp:3967` `#if _BALANCE_TYPE == 1`<br>`lisflood2/sgm_fast.cpp:4027` `#ifdef RESULT_CHECK`<br>`lisflood2/sgm_fast.cpp:4075` `#if defined (__INTEL_COMPILER) && _PROFILE_MODE > 0`<br>`lisflood2/sgm_fast.cpp:4101` `#if defined(RESULT_CHECK)`<br>`lisflood2/sgm_fast.cpp:4109` `#ifdef _MSC_VER`<br>`lisflood2/sgm_fast.cpp:4115` `#if defined(RESULT_CHECK)`<br>`lisflood2/sgm_fast.cpp:4165` `#if defined(RESULT_CHECK)`<br>`lisflood2/sgm_fast.cpp:4175` `#if (_NETCDF == 1)`<br>`lisflood2/sgm_fast.cpp:4219` `#if _DISABLE_WET_DRY == 1`<br>`lisflood2/sgm_fast.cpp:4276` `#if defined(RESULT_CHECK)`<br>`lisflood2/sgm_fast.cpp:4534` `#ifdef _DEBUGxx`<br>`lisflood2/sgm_fast.cpp:4670` `#if _PROFILE_MODE < 2`<br>`lisflood2/sgm_fast.cpp:4834` `#if defined (__INTEL_COMPILER) && _PROFILE_MODE > 0`<br>`lisflood2/sgm_fast.cpp:4837` `#if _PROFILE_MODE > 1` |
| LN1-621 | `lisflood2/sgm_fast.h` | `lisflood2/sgm_fast.h:75` `#ifdef RESULT_CHECK` |
| LN1-622 | `lisflood2/windows_ext.cpp` | `lisflood2/windows_ext.cpp:1` `#if defined(_MSC_VER) \|\| defined(_MSC_EXTENSIONS)`<br>`lisflood2/windows_ext.cpp:4` `#if defined(_MSC_VER) \|\| defined(_MSC_EXTENSIONS)` |
| LN1-623 | `lisflood2/windows_ext.h` | `lisflood2/windows_ext.h:1` `#ifndef LIS_WINDOWS_EXT_H_` |
| LN1-624 | `metal/fv1/metal_fv1_simulate.h` | `metal/fv1/metal_fv1_simulate.h:8` `#ifdef __APPLE__` |
| LN1-625 | `metal/fv1/metal_fv1_simulate.mm` | `metal/fv1/metal_fv1_simulate.mm:6` `#ifdef __APPLE__` |
| LN1-626 | `pars.cpp` | `pars.cpp:926` `#if _CALCULATE_Q_MODE != 1`<br>`pars.cpp:999` `#if (_NETCDF != 1)`<br>`pars.cpp:1080` `#if !defined(CUDA) && !defined(METAL_ENABLED)` |
| LN1-627 | `rain/rain.cpp` | `rain/rain.cpp:3` `#if _NETCDF == 1` |
| LN1-628 | `sgc.cpp` | `sgc.cpp:726` `#ifdef RESULT_CHECK` |
| LN1-629 | `sgc.h` | `sgc.h:11` `#ifdef RESULT_CHECK` |
| LN1-630 | `swe/dg2.cpp` | `swe/dg2.cpp:1020` `#ifndef _MSC_VER`<br>`swe/dg2.cpp:1078` `#ifndef _MSC_VER`<br>`swe/dg2.cpp:1094` `#ifndef _MSC_VER`<br>`swe/dg2.cpp:1109` `#ifndef _MSC_VER`<br>`swe/dg2.cpp:1124` `#ifndef _MSC_VER`<br>`swe/dg2.cpp:1139` `#ifndef _MSC_VER` |
| LN1-631 | `swe/dg2new.cpp` | `swe/dg2new.cpp:773` `#ifndef _MSC_VER` |
| LN1-632 | `swe/fv1.cpp` | `swe/fv1.cpp:591` `#ifndef _MSC_VER` |
| LN1-633 | `swe/stats.cpp` | `swe/stats.cpp:157` `#ifndef _MSC_VER` |
| LN1-634 | `tests.cpp` | `tests.cpp:2` `#ifdef TESTING` |
| LN1-635 | `utility.cpp` | `utility.cpp:56` `#if defined(_MSC_VER) \|\| defined (__INTEL_COMPILER)`<br>`utility.cpp:83` `#if defined(_MSC_VER) \|\| defined (__INTEL_COMPILER)` |

다음 표의 ‘빌드 정의 없음’은 앞의 42개 파일과 `config.float.cmake`에 명시 정의가 없다는 뜻이다.

| 행 ID | 어느 빌드 파일에도 명시 정의가 없는 조건 매크로 | 코드 원문·기본 분기 | 판정 |
|---|---|---|---|
| LN1-084 | `TESTING` | `lisflood.h:55` `//#define TESTING`는 주석이다. `lisflood.cpp:39–42` `#ifdef TESTING`<br>`RunTests();`<br>`exit(0);`<br>`#endif`·`tests.cpp:2` `#ifdef TESTING` | 코드에만(C) |
| LN1-085 | `LATLONGMODE` | `lisflood2/file_tool.cpp:191` `#ifdef LATLONGMODE`은 NetCDF lat/lon 차원 분기를 선택한다. `lisflood2/file_tool.cpp:296`의 같은 조건 양쪽에는 주석만 있다. 기본 빌드는 이 정의를 주지 않는다. | 코드에만(C) |
| LN1-086 | `_USE_TRACER` | `cuda/adaptive/classes/Tracer.h:5` `#if _USE_TRACER == 1`·`cuda/adaptive/classes/Tracer.h:26` `#define TRACE(name) Tracer tracer(name);`·`cuda/adaptive/classes/Tracer.h:30` `#define TRACE(name)` | 코드에만(C) |
| LN1-087 | `_DEBUGxx` | `lisflood2/sgm_fast.cpp:4534` `#ifdef _DEBUGxx`는 `.mass` 수치 서식 분기를 바꾼다. `_DEBUG`와 다른 이름이다. 기본 빌드는 `lisflood2/sgm_fast.cpp:4549`의 과학 표기 분기를 선택한다. | 코드에만(C) |
| LN1-088 | `THREADS_PER_BLOCK_MRA`, `NUM_VARS`, `NUM_CHILDREN`, `SIGNIFICANT`, `INSIGNIFICANT` | `cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:3–35`의 `#ifndef` 기본값은 각각 `256`, `4`, `4`, `true`, `false`다. `THREADS_PER_BLOCK_MRA`의 64·256·1024 분기는 `SHARED_MEMORY_BLOCK_DIM`을 8·16·32로 정의한다. 같은 분기는 `LVL_SINGLE_BLOCK`을 3·4·5로 정의한다. | 코드에만(C) |
| LN1-089 | `THREADS_PER_BLOCK`, `M_BAR` | `cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh:5` `#define THREADS_PER_BLOCK 256`·`cuda/adaptive/mra/extra_significance.cuh:3–5` `#ifndef M_BAR`<br>`#define M_BAR C(1.5)`<br>`#endif` | 코드에만(C) |
| LN1-090 | `_MSC_VER`, `_MSC_EXTENSIONS`, `__INTEL_COMPILER`, `__unix__`, `__APPLE__`, `__CUDA_ARCH__`, `__INTELLISENSE__`, `__CUDACC__`, `__AVX2__`, `__AVX__`, `__SSE4_2__`, `__SSE4_1__`, `__SSE3__`, `__SSE2__`, `__SSE__`, `_XOPEN_SOURCE`, `_ISOC99_SOURCE`, `_POSIX_C_SOURCE`, `_WIN32`, `_WIN64`, `WIN64` | 전처리 파일 표의 해당 원문 조건을 사용한다. `cuda/cuda_atomic.cuh:5` `#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ < 600`은 double atomicAdd 보완 경로다. `__CUDACC__`는 `cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:3–4`와 `cuda/acc_nugrid/sort_finest_scale_coefficients_z_order.cuh:3–4`에서도 정의한다. | 코드에만(C) |
| LN1-091 | `CUBLAS_API_H_`, `CUDA_DRIVER_API`, `CURAND_H_`, `CUSOLVER_COMMON_H_`, `CUSPARSEAPI`, `NPP_VERSION_MAJOR`, `NPP_VERSION_MINOR`, `NVJPEGAPI`, `NV_NPPIDEFS_H`, `_CUFFT_H_`, `__CUDA_RUNTIME_H__`, `__DRIVER_TYPES_H__` | `cuda/common/helper_cuda.h`의 조건문은 SDK 헤더의 포함 여부나 SDK 판을 검사한다. 정확한 모든 조건 줄은 LN1-608에 있다. 이들은 모델 설정의 누락 정의가 아니다. | 코드에만(C) |
| LN1-092 | `COMMON_HELPER_CUDA_H_`, `COMMON_HELPER_FUNCTIONS_H_`, `COMMON_HELPER_STRING_H_`, `LIS_WINDOWS_EXT_H_`, `EXIT_WAIVED`, `DEVICE_RESET`, `MAX`, `_CRT_SECURE_NO_DEPRECATE`, `STRCASECMP`, `STRNCASECMP`, `STRCPY`, `FOPEN`, `FOPEN_FAIL`, `SSCANF`, `SPRINTF`, `cbrt`, `cbrtf` | helper 헤더·호환 헤더는 `#ifndef`로 자체 정의를 보호한다. `lisflood.h:68–72`는 `cbrt`·`cbrtf`의 매크로 기본 정의를 둔다. include guard와 함수 이름 검사는 빌드 기능 스위치와 구분한다. | 코드에만(C) |

해석: LN1-090의 플랫폼·컴파일러 식별자는 도구 체인이 제공하는 값이다.
이 보고서는 이 값들을 모두 빌드 파일에 `-D`로 추가하라고 권하지 않는다.
`_USE_TRACER`는 미정의 상태에서 전처리 식 값 0으로 처리된다.
`LATLONGMODE`는 런타임 `latlong` 키워드와 다른 스위치다.
`pars.cpp:868–872`는 `latlong`을 읽고 `Statesptr->latlong = ON;`을 대입한다.
그 대입은 `LATLONGMODE`를 정의하지 않는다.

| 행 ID | 빌드 정의 없이 소스가 직접 정의하는 나머지 매크로 | 원문 근거 |
|---|---|---|
| LN1-640 | `LF_VersionMajor`, `LF_VersionMinor`, `LF_VersionInc`, `LF_CheckVersion`, `LF_Release` | `VersionHistory.h:16–19,23` `#define LF_VersionMajor 8`·`#define LF_VersionMinor 1`·`#define LF_VersionInc   0`·`#define LF_CheckVersion 0`·`#define LF_Release "8.3"` |
| LN1-641 | `NUMERIC_TYPE`, `NUMERIC_TYPE_NAME`, `NUM_FMT`, `FMAX`, `FMIN`, `POW`, `FABS`, `CBRT`, `SQRT`, `C` | `lisflood.h:75–97`의 double·float 분기다. `lisflood.h:85` `#define C(x) x`·`lisflood.h:96` `#define C(x) x##f` |
| LN1-642 | `FILE_SEP`, `STRCMPi`, `getmax`, `getmin`, `cbrt`, `cbrtf` | `lisflood.h:68–119`의 플랫폼·수학 호환 정의다. `lisflood.h:69` `#define cbrt(x) pow(x,1/3.0);`·`lisflood.h:72` `#define cbrtf(x) powf(x,1/3.0f);` |
| LN1-643 | `LINE_BUFFER_LEN`, `ON`, `OFF`, `CHKINTERVAL`, `NULLVAL`, `DEM_NO_DATA`, `DEFAULT_PRECISION`, `PARAM_FILE`, `CMD_LINE`, `TIME`, `TIME_SPACE`, `fix_small_negative` | `lisflood.h:122–138`의 값은 차례로 `4096`, `1`, `0`, `C(1.0)`, `C(-9999.0)`, `C(1e7)`, `6`, `0`, `1`, `1`, `2`다. `lisflood.h:138` `#define fix_small_negative(value) ((value < C(0.0) && value > -0.0001) ? C(0.0) : value)` |
| LN1-644 | `TINY`, `MODE_STRING` | `ch_flow.cpp:1020` `#define TINY C(1.e-20)`·`pars.cpp:15` `#define MODE_STRING(mode) (mode == CMD_LINE?"(Command Line)":"")` |
| LN1-645 | `ERRCODE`, `ERR`, `nc_put_att_NUMERIC_TYPE`, `nc_put_var1_NUMERIC_TYPE`, `NC_NUMERIC_TYPE` | `lisflood2/file_tool.cpp:13–24` `#define ERRCODE 2`·`#define ERR(e) {printf("Error: %s\n", nc_strerror(e)); exit(ERRCODE);}`와 double·float NetCDF API 매핑이다. |
| LN1-646 | `UNITS_LABEL`, `LONG_NAME_LABEL`, `MISSING_VALUE_LABEL`, `HEIGHT_UNITS_VALUE`, `FLOW_UNITS_VALUE`, `VELOCITY_UNITS_VALUE`, `TIME_DURATION_HOURS_UNITS_VALUE`, `TIME_UNITS_VALUE`, `TIME_HOURS_UNITS_VALUE`, `LONG_NAME_Longitude`, `UNITS_Longitude`, `LONG_NAME_Latitude`, `UNITS_Latitude` | `lisflood2/file_tool.cpp:27–34,146–147,198–202`의 출력 메타데이터 문자열이다. `lisflood2/file_tool.cpp:31` `#define HEIGHT_UNITS_VALUE "meters"`·`lisflood2/file_tool.cpp:32` `#define FLOW_UNITS_VALUE "meters3/second"` |
| LN1-647 | `NETCDF_IGNORE`, `NC_GET_VARA_NUMERIC_TYPE` | `lisflood2/file_tool.h:13` `#define NETCDF_IGNORE -1`·`lisflood2/file_tool.h:16,18` `#define NC_GET_VARA_NUMERIC_TYPE nc_get_vara_double`·`#define NC_GET_VARA_NUMERIC_TYPE nc_get_vara_float` |
| LN1-648 | `GRID_ALIGN_WIDTH`, `THREAD_SG_CELL_BLOCK` | `lisflood2/lisflood2.h:11–12` `#define GRID_ALIGN_WIDTH 8`<br>`#define THREAD_SG_CELL_BLOCK 64` |
| LN1-649 | `DELTA_EPOCH_IN_MICROSECS`, `LIS_WINDOWS_EXT_H_` | `lisflood2/windows_ext.cpp:5,7`의 `11644473600000000Ui64`·`11644473600000000ULL`과 `lisflood2/windows_ext.h:1–2`의 include guard다. |
| LN1-650 | `C`, `NUM_FRMT`, `NUM_FIG` | `cuda/adaptive/types/real.h:3–17`의 double·float 매핑이다. `cuda/adaptive/types/real.h:7–8` `#define NUM_FRMT "lf"`·`#define NUM_FIG  ".15"`·`cuda/adaptive/types/real.h:14–15` `#define NUM_FRMT "f"`·`#define NUM_FIG  ".8"` |
| LN1-651 | `TRACE`, `CHECK_CUDA_ERROR` | `cuda/adaptive/classes/Tracer.h:26,30`의 활성·빈 TRACE 정의와 `cuda/adaptive/utilities/CHECK_CUDA_ERROR.cuh:9`·`cuda/acc_nugrid/CHECK_CUDA_ERROR.cuh:9`의 `#define CHECK_CUDA_ERROR(ans) { CUDAAssert( (ans), __FILE__, __LINE__); }` |
| LN1-652 | `THREADS_PER_BLOCK`, `THREADS_PER_BLOCK_MRA`, `SHARED_MEMORY_BLOCK_DIM`, `LVL_SINGLE_BLOCK`, `NUM_VARS`, `NUM_CHILDREN`, `SIGNIFICANT`, `INSIGNIFICANT`, `M_BAR` | LN1-088·LN1-089에 정의와 조건을 적었다. `SHARED_MEMORY_BLOCK_DIM`·`LVL_SINGLE_BLOCK`도 빌드 파일이 아니라 각 BLOCK_VAR_MACROS 헤더가 정의한다. |
| LN1-653 | adaptive 필터의 `H0`, `H1`, `G0`, `G1`과 `HHk_ij`, `GAk_ij`, `GBk_ij`, `GCk_ij` 전체 | `cuda/adaptive/mra/Filters.h:5–200`이다. 여기서 `k`는 0·1·2·3이다. `ij`는 11·12·13·21·22·23·31·32·33이다. 뒤의 네 계열은 이 조합 144개다. `cuda/adaptive/mra/Filters.h:5` `#define H0  C(1.0) / sqrt( C(2.0) )`·`cuda/adaptive/mra/Filters.h:10` `#define HH0_11 ( C(1.0) / C(2.0) )`·`cuda/adaptive/mra/Filters.h:200` `#define GC3_33 ( -C(3.0) * sqrt( C(7.0) ) / C(28.0) )` |
| LN1-654 | acc_nugrid 필터의 `HHk_ij`, `GAk_ij`, `GBk_ij`, `GCk_ij` 전체 | `cuda/acc_nugrid/maskFilterHaar.h:31–221`이다. 인덱스 집합은 LN1-653과 같다. 이 파일도 144개를 직접 정의한다. `cuda/acc_nugrid/maskFilterHaar.h:31` `#define HH0_11 C(0.5) * ( C(1.0) / C(2.0) )`·`cuda/acc_nugrid/maskFilterHaar.h:221` `#define GC3_33 C(0.5) * ( -C(3.0) * SQRT( C(7.0) ) / C(28.0) )` |
| LN1-655 | `CUDA_BLOCK_SIZE_X`, `CUDA_BLOCK_SIZE_Y`, `CUDA_BLOCK_SIZE`, `DEFAULT_SAMPLE_BUFFER_SIZE` | `cuda/cuda_solver.cuh:2–4`의 값은 `16`, `16`, `256`이다. `cuda/cuda_sample.cuh:2` `#define DEFAULT_SAMPLE_BUFFER_SIZE 1` |
| LN1-656 | `DEPTH_THRESH`, `MIN_SAFE_H`, `TG_X`, `TG_Y` | `metal/fv1/metal_fv1_kernels.metal:11–12,384–385`의 값은 `1e-3f`, `1e-6f`, `16`, `16`이다. |
| LN1-657 | helper의 `COMMON_HELPER_CUDA_H_`, `COMMON_HELPER_FUNCTIONS_H_`, `COMMON_HELPER_STRING_H_`, `EXIT_WAIVED`, `DEVICE_RESET`, `checkCudaErrors`, `getLastCudaError`, `printLastCudaError`, `MAX` | `cuda/common/helper_cuda.h:32,44,584,588,607,610,629,646`·`cuda/common/helper_functions.h:31,56`·`cuda/common/helper_string.h:30,92`이다. `cuda/common/helper_cuda.h:607` `#define checkCudaErrors(val) check((val), #val, __FILE__, __LINE__)` |
| LN1-658 | helper의 `_CRT_SECURE_NO_DEPRECATE`, `STRCASECMP`, `STRNCASECMP`, `STRCPY`, `FOPEN`, `FOPEN_FAIL`, `SSCANF`, `SPRINTF` | `cuda/common/helper_string.h:39–87`의 Windows·POSIX 호환 정의다. `cuda/common/helper_string.h:42` `#define STRCASECMP _stricmp`·`cuda/common/helper_string.h:68` `#define STRCASECMP strcasecmp` |
| LN1-659 | `CATCH_CONFIG_MAIN` | `test/test_lisflood.cpp:1` `#define CATCH_CONFIG_MAIN`은 동봉 테스트 프레임워크에 main 생성을 요청한다. |

| 행 ID | 문서와 코드의 관계 | 판정 | 이유 |
|---|---|---|---|
| LN1-093 | README·INSTALL은 LN1-640–659의 소스 내부 매크로 목록을 설명하지 않는다. | 코드에만(C) | 이들은 빌드 파일의 누락 옵션 목록과 구분해야 한다. 필터 계수는 위 인덱스 집합으로 전부 열거했다. 계수의 물리·수학 유도는 이 빌드 대조의 대상이 아니다. |

`rain/rain.tpp`와 `rain/rain_stub.tpp`도 추가 검색했다.
두 파일에는 조건 지시문이나 `#define`이 없다.
동봉 테스트 프레임워크 `test/catch.hpp`의 내부 매크로는 모델의 기능 스위치 집계에서 제외했다.

### 2.5 빌드 파일 사이의 소스·매크로 차이 판정

| 행 ID | 문서·빌드 선언 | 다른 코드 경로의 원문 | 판정 | 이유 |
|---|---|---|---|---|
| LN1-100 | `CMakeLists.txt:26–65`의 CPU 공통 38개·`CMakeLists.txt:68`의 `lisflood.cpp` | `makefile:31` `swe/dg2new.cpp \`·`lisflood.vcxproj:668` `<ClCompile Include="tests.cpp" />`·Intel project는 공통 38개와 main만 포함한다. | 코드에만(C) | make는 dg2new를 추가한다. VS project는 tests.cpp를 추가한다. `lisflood.cpp:794–796`의 dg2new 호출은 주석이다. `tests.cpp:2`의 본문은 TESTING 조건부다. 현재 기본 경로의 해법 추가로 해석하지 않는다. |
| LN1-101 | `makefile:53–84`는 CUDA를 정의하고 FV1·DG2·공통 CUDA 일부만 목록에 넣는다. | `lisflood.cpp:427–450`은 같은 `#ifdef CUDA` 안에서 FV2·ACC·acc_nugrid·adaptive의 `simulation.run(...)`도 참조한다. `CMakeLists.txt:102–175,178`은 그 구현 소스를 연결한다. | 불일치(E) | 강함. make CUDA 소스 집합에는 참조한 해법들의 구현이 없다. 런타임에서 해법을 선택하지 않아도 링크 참조는 남는다. makefile에는 이를 제외하는 별도 전처리 가드가 없다. |
| LN1-102 | `CMakeLists.txt:190,193,196` `add_executable(generateDG2DEM preprocess/generateDG2DEM.cpp)`·`add_executable(generateDG2start preprocess/generateDG2start.cpp)`·`add_executable(DG2downscale postprocess/DG2downscale.cpp)` | `makefile:123–132`는 test_lisflood·create1DDamBreak·createDamBreakObstacle·createHump·createLakeAtRestCones·createLakeAtRestBlocks·createRadialDamBreak·checkDynamicRain·generateDG2DEM·hll_util을 정의한다. | 코드에만(C) | make에는 generateDG2start와 DG2downscale 대상이 없다. CMake에는 나머지 테스트·전처리 대상이 없다. 두 목록은 서로 다른 보조 실행 파일 집합을 제공한다. |
| LN1-103 | `config.default.cmake:2–3` `_NUMERIC_MODE=1`·`_ONLY_RECT=1` | `float 설정:2` `_NUMERIC_MODE=0`·`config/bluecrystal-intel:1`과 `config/sharc-intel-cpu:1`의 `_ONLY_RECT=0`·VS float·all_channel 정의 | 코드에만(C) | 정밀도와 단면 허용 범위는 구성별 선택이다. `lisflood.h`의 미정의 기본값을 적용한 뒤 비교해야 한다. 명시 정의가 없다는 이유로 값 0이라고 판단하면 안 된다. |
| LN1-104 | `config/aws-gcc-nvidia-t4:2` `NETCDF := yes` | 같은 파일 `config/aws-gcc-nvidia-t4:4`의 `-D_NETCDF=0`·`makefile:1` `-include $(CONFIG)`·`makefile:53` `ifdef CUDA` | 코드에만(C) | makefile은 make 변수 NETCDF를 참조하지 않는다. 이 구성의 실제 `_NETCDF` 값은 0이다. 변수 이름만 보고 NetCDF 지원을 켠 구성이라고 적으면 틀린다. |
| LN1-105 | `make_block*.mk`, `make_disable*.mk`, `make_qmode*.mk`, `result_check.mk`는 MAINOBJS·CFLAGS_RELEASE 등을 사용한다. | `makefile:1,160`의 include 대상은 `$(CONFIG)`와 `$(ALLDEPS)`다. 본문 `makefile:5–44,100–108`은 SRCS·CXXFLAGS·CXX를 사용한다. | 코드에만(C) | 현재 루트 makefile은 이 변형 파일들을 include하지 않는다. 현재 빌드 파일 집합에는 MAINOBJS·CFLAGS_RELEASE를 공급하는 공통 규칙이 없다. 선언만 있는 변형을 기본 make의 실제 지원 대상으로 적지 않는다. |
| LN1-106 | `test/makefile:12–18`는 LISFLOOD_OBJS·EXE_DOUBLE_GCC·LD_GCC·CC_GCC를 요구한다. | `makefile:46–51,123`은 별도 TEST_SRCS와 `test_lisflood` app 규칙을 만든다. | 코드에만(C) | 두 테스트 빌드 경로는 서로 다른 외부 변수·객체 체계를 사용한다. 루트 makefile은 test/makefile을 include하지 않는다. |
| LN1-107 | `config/`의 make 문법 파일과 CMake 문법 파일 | `makefile:1` `-include $(CONFIG)`·`CMakeLists.txt:11` `include(${_CONFIG})` | 코드에만(C) | `CONFIG=config/local`은 make용 선택이다. `-D_CONFIG=config/bluepebble-intel`은 CMake용 선택이다. 같은 디렉터리의 모든 파일을 두 도구에 공통으로 넣을 수 없다. |
| LN1-108 | `CMakeLists.txt:199–202` `find_package(OpenMP)`<br>`if (OpenMP_CXX_FOUND)`<br>`target_link_libraries(lisflood-base INTERFACE OpenMP::OpenMP_CXX)`<br>`endif()` | `lisflood2/sgm_fast.cpp:12` `#include <omp.h>`·`lisflood2/sgm_fast.cpp:3521` `NUMERIC_TYPE * tmp_row = tmp_thread_data[omp_get_thread_num()];`·`lisflood2/lisflood_processing.cpp:1851` `int thread_id = omp_get_thread_num();` | 불일치(E) | 강함. CMake 탐색은 선택 사항이다. 공통 소스는 OpenMP 헤더와 런타임 함수를 무조건 사용한다. 미탐색 시의 대체 구현이나 전처리 가드가 없다. 배포 README:68도 OpenMP를 필요 조건으로 적는다. |
| LN1-109 | `make_block1bal0.mk:9`·`make_block1bal1.mk:9`의 `_SGM_BY_BLOCKS=1` | `lisflood2/lisflood_processing.cpp:1799` `FP_xwidth, Fp_ywidth,`·같은 파일 `lisflood2/lisflood_processing.cpp:1698`은 `NUMERIC_TYPE* Fp_xwidth = (NUMERIC_TYPE*)memory_allocate(sizeof(NUMERIC_TYPE) * grid_cols_padded * (grid_rows + 1));`를 선언한다. `lisflood2/sgm_fast.cpp:3663–3664`는 ProcessSubGridQBlock의 마지막 max_Froude 인수를 빠뜨린다. | 불일치(E) | 강함. 기본값 0에서는 제외되는 분기의 정적 컴파일 결함 후보다. 같은 판의 행 경로는 올바른 이름과 인수 목록을 사용한다. 패치는 이 두 파일을 바꾸지 않는다. |
| LN1-110 | `lisflood.vcxproj:519–534`의 Debug Win32 | `lisflood.vcxproj:527`의 include 경로는 `windep\netCDF4-64\include`다. `lisflood.vcxproj:531`의 link 경로는 `windep\netCDF4-32\lib`다. `lisflood.vcxproj:428`의 Release_float Win32 include 경로는 `windep\netCDF4-32\include`다. | 코드에만(C) | Debug Win32의 헤더·라이브러리 경로 표기가 서로 다르다. 헤더 ABI가 실제로 달라 빌드가 실패한다고 단정하지 않는다. |
| LN1-111 | `lisflood.vcxproj:504,526` `<OpenMPSupport>false</OpenMPSupport>` | `lisflood_intel.vcxproj:218` `<OpenMPSupport>true</OpenMPSupport>` | 코드에만(C) | 두 project의 Debug OpenMP 설정이 다르다. CMake Debug는 탐색된 OpenMP 대상을 연결한다. Debug라는 이름만으로 병렬화 설정을 같다고 적지 않는다. |
| LN1-112 | `CMakeLists.txt:5` `set(CMAKE_CUDA_ARCHITECTURES 61)` | make GPU config의 NVCCFLAGS는 각각 75·70·37을 지정한다. `배포 README:79`는 명령행에서 80을 지정한다. | 코드에만(C) | 아키텍처 값은 빌드 경로와 사용자 선택에 따라 다르다. 이 값들은 C++ 조건 매크로 정의가 아니다. 실제 장치와 도구 체인에서의 실행 성공은 H다. |

`LN1-109`의 인수 목록은 다음과 같다.
`lisflood2/sgm_fast.cpp:1426–1433`:

```cpp
inline void ProcessSubGridQBlock(const int block_index, const int grid_cols_padded,
    const NUMERIC_TYPE depth_thresh, const NUMERIC_TYPE delta_time, const NUMERIC_TYPE g,
    const SubGridRowList * sub_grid_layout, SubGridState * sub_grid_state, const SGCprams * SGCptr,
    const NUMERIC_TYPE * h_grid,
    WetDryRowBound * wet_dry_bounds,
    NUMERIC_TYPE * Qx_grid, NUMERIC_TYPE * Qy_grid,
    NUMERIC_TYPE * Qx_old_grid, NUMERIC_TYPE * Qy_old_grid,
    const NUMERIC_TYPE max_Froude)
```

`lisflood2/sgm_fast.cpp:3639–3641`의 기본 행 경로는 다음과 같다.

```cpp
#if _SGM_BY_BLOCKS == 0
                ProcessSubGridQBlock(j, grid_cols_padded, depth_thresh, delta_time, g, sub_grid_layout_rows, sub_grid_state_rows, SGCptr, h_grid,
                    wet_dry_bounds, Qx_grid, Qy_grid, Qx_old_grid, Qy_old_grid, Parptr->max_Froude);
```

`lisflood2/sgm_fast.cpp:3656–3667`의 블록 경로는 다음과 같다.

```cpp
#if _SGM_BY_BLOCKS == 1
        if (sub_grid_layout_blocks->row_cols_padded > 0)
        {
#pragma omp barrier
#pragma omp for schedule(static) nowait
            for (int bi = 0; bi < wet_dry_bounds->block_count; bi++)
            {
                ProcessSubGridQBlock(bi, grid_cols_padded, depth_thresh, delta_time, g, sub_grid_layout_blocks, sub_grid_state_blocks, SGCptr, h_grid,
                    wet_dry_bounds, Qx_grid, Qy_grid, Qx_old_grid, Qy_old_grid);
                if (curr_time >= Parptr->SaveTotal && Statesptr->SGCvoutput == ON)
                {
                    SGC2_UpdateVelocitySubGrid_block(j, grid_cols_padded, depth_thresh, delta_time, sub_grid_layout_blocks, sub_grid_state_blocks, SGCptr, h_grid);
```

이 인용은 탭을 공백으로 표시한다.
인용의 식별자와 조건과 인수 순서는 원문과 같다.
블록 경로의 `j`는 그 위치의 `for` 변수가 아니다.
검색한 선언·정의에는 ProcessSubGridQBlock의 다른 오버로드나 기본 인수가 없다.
반대 근거는 기본 `_SGM_BY_BLOCKS=0`이다.
이 기본 구성에는 위 결함 후보 분기가 들어가지 않는다.

### 2.6 8.3 변경 표의 각 행

이 절에서 E는 README가 설명한 8.2 코드 결함의 귀속이다.
README의 수정 설명이 실제 패치와 맞으면 그 사실도 함께 적는다.
특정 GPU·격자에서 관측했다는 오류와 반복 실행 수치는 H로 분리한다.

| 행 ID | 배포 README 원문 | 8.2 코드 원문 | 현재 코드·패치 원문 | 판정·이유 |
|---|---|---|---|---|
| LN1-120 | `배포 README:32` `the maximum-depth grid is kept in CPU memory`·`allocated without the ghost cells the GPU writes`·``kept on the GPU at full size, copied to the CPU only when the `.max` file is written`` | `v8.2:cuda/cuda_max_field.cu:96–107`은 acceleration이 참이면 `maxH = GhostRaster::allocate_pinned_H(geometry);`를 실행한다. `v8.2:cuda/cuda_geometry.cu:42–43`은 `return static_cast<NUMERIC_TYPE*>(malloc_pinned(`<br>`lis::GhostRaster::elements_H(geometry)*sizeof(NUMERIC_TYPE)));`를 할당한다. `v8.2:cuda/ghostraster.cpp:11`은 `(geometry.xsz)*(geometry.ysz)`를 반환한다. | `cuda/cuda_max_field.cu:97–98` `maxH = GhostRaster::allocate_device(geometry);`<br>`cudaMemset(maxH, 0, lis::GhostRaster::elements(geometry)*sizeof(NUMERIC_TYPE));`·`cuda/cuda_max_field.cu:124–125` `NUMERIC_TYPE* h_maxH = GhostRaster::allocate_pinned(geometry);`<br>`cuda::copy(h_maxH, maxH, lis::GhostRaster::elements(geometry)*sizeof(NUMERIC_TYPE));`·`패치:94–134` | 불일치(E, 8.2). 강함. README의 설명과 수정은 맞는다. 실제 결함 조건은 output_precision이 0이 아닌 FV1·FV2·DG2 기본 호출이다. 아래 인수 연결을 봐야 한다. 8.3은 acceleration 인수와 무관하게 충분한 크기를 할당한다. |
| LN1-121 | `배포 README:32` `read and written over PCIe every time step` | `v8.2:cuda/cuda_util.cu:53` `checkCudaErrors(cudaMallocHost(&ptr, size));`·`v8.2:cuda/cuda_max_field.cu:25–26` `NUMERIC_TYPE& maxHvalue = maxH[j*cuda::pitch+i];`<br>`maxHvalue = FMAX(maxHvalue, H[j*cuda::pitch+i]);` | `cuda/fv1/cuda_fv1_simulate.cu:177` `max_field.update(d_U.H);`·`cuda/cuda_max_field.cu:106` `lis::cuda::update_max_field<<<grid_size, CUDA_BLOCK_SIZE>>>(maxH, H);` | 일치. 해석: 분리형 GPU에서 host pinned 배열을 커널이 매 단계 직접 읽고 쓰는 경로를 문서가 PCIe 접근으로 설명한다. 원문에 매 단계 cudaMemcpy 호출이 있는 것은 아니다. 실제 전송량·소요 시간은 이 대조에서 측정하지 않았다. |
| LN1-122 | `배포 README:33` `every NoData cell adds to one shared counter every time step, even when dry`·`dry NoData cells skip the addition` | `v8.2:cuda/cuda_boundary.cu:286–292,318–324`은 Hold를 저장하고 H를 0으로 만든 뒤 Q를 계산하여 항상 `accumulate_point_source_stats(mass_stats, Q);`를 호출한다. 같은 파일 `v8.2:cuda/cuda_boundary.cu:86–92`는 discharge가 0이면 else에서 `atomicAdd(&(mass_stats->out), -discharge);`를 실행한다. | `cuda/cuda_boundary.cu:289,321` `if (Hold == C(0.0)) continue; // dry: nothing to add to the mass balance`·`패치:75–90` | 불일치(E, 8.2). 중간. README의 수정 설명은 맞는다. 결함 후보는 불필요한 원자 덧셈의 경합이다. 0을 더하므로 건조 셀의 질량을 잘못 계상한다는 주장은 아니다. `drain_nodata`가 켜졌을 때만 이 경로를 호출한다. |
| LN1-123 | `배포 README:34` `the flux kernels do not synchronise their threads at the end of each pass`·`they do` | `v8.2:cuda/fv1/cuda_fv1_solver.cu:359–361`은 기존 쓰기 후 barrier 뒤 `if (threadIdx.x == 0) continue;`를 실행한다. 기존 `v8.2:cuda/fv1/cuda_fv1_solver.cu:379–384`에는 다음 pass 전에 모든 reader를 기다리는 barrier가 없다. FV2·DG2의 x·y 경로도 같다. | `cuda/fv1/cuda_fv1_solver.cu:361` `if (threadIdx.x != 0 && i <= cuda::geometry.xsz && j <= cuda::geometry.ysz)`·`cuda/fv1/cuda_fv1_solver.cu:380–381` `// shared memory is rewritten in the next pass: wait for every reader`<br>`__syncthreads();`·y `cuda/fv1/cuda_fv1_solver.cu:456,475–476`·`cuda/fv2/cuda_fv2_solver.cu:228,241–242,309,322–323`·`cuda/dg2/cuda_dg2_solver.cu:269,285–286,358,375–376`·`패치:138–260` | 불일치(E, 8.2). 강함. README의 수정 설명은 맞는다. shared 배열의 다음 pass 쓰기가 다른 warp의 이전 pass 읽기보다 먼저 일어날 수 있다. 패치는 x·y 모두 마지막 barrier를 추가한다. 패치는 첫 thread를 reader 조건에서 제외하여 그 thread도 barrier에 도달하게 한다. |
| LN1-124 | `배포 README:34` `on grids wider or taller than 1920 cells repeated runs give different results`·`배포 README:32` `large grids stop with cudaErrorIllegalAddress` | `cuda/cuda_solver.cuh:2–4`의 16·16·256과 `cuda/fv1/cuda_fv1_simulate.cu:28` `dim3 grid_size(128, 128);`·`cuda/fv1/cuda_fv1_solver.cu:315` `for (int i=global_i; i<=max_i; i+=(blockDim.x-1)*gridDim.x)` | 겹침 방향 stride는 `(16-1)*128=1920`이다. 이 수는 인용한 상수와 식으로 계산했다. | 불일치(H). stride와 수정 위치는 정적으로 대응한다. 오류 코드·모든 큰 격자의 중단·반복 실행 결과는 실행 주장이다. 이 보고서는 해당 현상을 실행 재현했다고 쓰지 않는다. |
| LN1-125 | `배포 README:35` `no GPU support on Apple computers`·`Metal back end`·`FV1` | v8.2에는 metal 디렉터리가 없다. `v8.2:CMakeLists.txt:72–77`의 GPU 선택은 CUDA다. | `CMakeLists.txt:231–237`의 APPLE 분기·`metal/CMakeLists.txt:22–29`의 라이브러리·`lisflood.cpp:780–788`의 FV1 분기·`패치:13–25,272–295,305–2950` | 일치. 8.3은 Metal FV1 구현을 추가한다. Apple 여부와 Metal framework 탐색 성공이 빌드 조건이다. 장치 존재 여부는 실행 시 다시 검사한다. Apple Silicon만 허용하는 processor 조건은 CMake에 없다. |
| LN1-126 | `배포 README:36` `does not compile with CUDA 12 on Linux (an unused global sync() clashes with the system's)`·`renamed` | `v8.2:cuda/adaptive/utilities/cuda_utils.cu:3–6` `__host__`<br>`cudaError_t sync()`<br>`{`<br>`return cudaDeviceSynchronize();`·`v8.2:cuda/adaptive/utilities/cuda_utils.cuh:9–10` `__host__`<br>`cudaError_t sync();` | `cuda/adaptive/utilities/cuda_utils.cu:4` `cudaError_t sync_device()`·`cuda/adaptive/utilities/cuda_utils.cuh:10` `cudaError_t sync_device();`·`패치:51–71` | 불일치(E, 8.2). 중간. 전역 이름과 반환형 충돌 후보가 실제로 있다. 패치는 선언과 정의를 함께 바꾼다. 이 환경의 `/usr/include/unistd.h:1005`는 `extern void sync (void) __THROW;`를 선언한다. CUDA 12 헤더의 구체적 포함 경로와 컴파일 실패는 실행 확인하지 않았다. 비활성 tracer 호출의 잔존은 LN1-135에서 다룬다. |
| LN1-127 | `배포 README:37` `a stray one-line file format in the top folder hides the C++ header <format> on macOS`·`removed` | `v8.2:format:1` `5` | `패치:264–268` `diff -ruN a/format b/format`·`@@ -1 +0,0 @@`·`-5`·현재 format 경로는 없다. `metal/CMakeLists.txt:26`은 `${CMAKE_SOURCE_DIR}`를 include 경로에 넣는다. | 불일치(E, 8.2). 중간. 소스 루트가 헤더 탐색 경로에 들어가고 외부 헤더가 `<format>`을 요구하면 이름 가림이 생긴다. 8.3은 그 파일을 삭제한다. 이 조건을 모든 8.2 Linux·Windows 빌드의 오류로 확대하지 않는다. macOS에서의 구체적 오류 출력은 확인하지 않았다. |
| LN1-128 | `배포 README:38` `generateDG2DEM`·`use an uninitialised NoData value`·`initialised as in lisflood` | `v8.2:preprocess/generateDG2DEM.cpp:43–44` `Pars pars;`<br>`Pars *Parptr = &pars;`·`v8.2:preprocess/generateDG2DEM.cpp:61` `LoadDEMData(Parptr, rawdem, fp, no_data_value);`·`v8.2:preprocess/generateDG2DEM.cpp:72` `dg2::initialise_field(converter, Parptr->nodata_elevation, Parptr,`<br>`Arrptr->DEM, Arrptr->DEM1x, Arrptr->DEM1y);` | `preprocess/generateDG2DEM.cpp:43–45` `Pars pars;`<br>`pars.nodata_elevation = DEM_NO_DATA; // same default as lisflood.cpp`<br>`Pars *Parptr = &pars;`·`패치:2981–2988` | 불일치(E, 8.2). 강함. `nodata_elevation` 키워드를 주지 않으면 초기 대입이 없었다. 본체 기본값과 LoadDEMData의 소비 경로가 이를 뒷받침한다. 패치는 설정 파일을 읽기 전에 기본값을 넣는다. |
| LN1-129 | `배포 README:38` `generateDG2start`·`use an uninitialised NoData value`·`initialised as in lisflood` | `v8.2:preprocess/generateDG2start.cpp:43–44` `Pars pars;`<br>`Pars *Parptr = &pars;`·`v8.2:preprocess/generateDG2start.cpp:61` `LoadDEMData(Parptr, rawdem, fp, no_data_value);`·`v8.2:preprocess/generateDG2start.cpp:72` `dg2::initialise_field(converter, Parptr->nodata_elevation, Parptr,`<br>`Arrptr->DEM, Arrptr->DEM1x, Arrptr->DEM1y);` | `preprocess/generateDG2start.cpp:43–45` `Pars pars;`<br>`pars.nodata_elevation = DEM_NO_DATA; // same default as lisflood.cpp`<br>`Pars *Parptr = &pars;`·`패치:2992–2999` | 불일치(E, 8.2). 강함. DEM 도구와 같은 조건의 결함이다. start 도구도 같은 기본값을 받는다. |
| LN1-130 | `배포 README:39` `prints its internal version number, 8.1.0`·`prints LISFLOOD-FP 8.3` | `v8.2:VersionHistory.h:16–18`은 8·1·0이다. `v8.2:lisflood.cpp:849` `printf(" LISFLOOD-FP version %d.%d.%d (%s)\n", LF_VersionMajor, LF_VersionMinor, LF_VersionInc, NUMERIC_TYPE_NAME);` | `VersionHistory.h:23` `#define LF_Release "8.3"`·`lisflood.cpp:859` `printf(" LISFLOOD-FP %s\n", LF_Release);`·`패치:29–47,296–304` | 불일치(E, 8.2). 강함. 배포 판과 시작 출력이 달랐다. 패치는 표시 이름을 분리한다. 내부 숫자를 8.3.0으로 바꾼 것은 아니다. checkpoint 호환 표식을 유지하려는 주석이 반대 근거다. |
| LN1-131 | `배포 README:14` `config.float.cmake           build settings: single precision`·`배포 README:79,107`의 `-D_CONFIG=$PWD/config.float.cmake` | `config.default.cmake:2` `add_compile_definitions(_NUMERIC_MODE=1)` | `float 설정:2` `add_compile_definitions(_NUMERIC_MODE=0)`·나머지 7줄은 config.default.cmake와 같다. | 일치. 사용자는 float 설정을 명시적으로 선택한다. 기본 파일 자체는 double로 남는다. |
| LN1-132 | `배포 README:14` `single precision, as the GPU solvers use` | `lisflood.h:75–97`의 NUMERIC_TYPE은 `_NUMERIC_MODE`에 따른다. | `cuda/adaptive/types/real.h:3–15`도 double·float를 모두 정의한다. `cuda/cuda_atomic.cuh:5`는 낮은 CUDA 아키텍처용 double atomicAdd 경로다. Metal 커널은 float를 직접 사용한다. | 불일치(B). 이 문장을 모든 GPU 구현이 single precision으로 고정되어 있다는 뜻으로 읽으면 코드와 다르다. 이 배포본의 권장 빌드가 float인 사실과 CUDA 구현의 자료형 선택 가능성을 구분한다. |
| LN1-133 | `배포 README:4–5` `The numerical method of 8.2 is unchanged.` | v8.2의 CPU 해법 파일들과 현재 CPU 해법 파일들은 바이트 비교에서 같다. 패치의 기존 CUDA 해법 수정은 할당·0 덧셈 생략·barrier·reader 가드다. | `패치:75–260`은 유량·하상 경사·RK 계수의 식을 바꾸지 않는다. `metal/fv1/metal_fv1_kernels.metal:3–4` `// Ported from CUDA implementation`<br>`// Same numerical algorithm - different GPU language` | 일치. 기존 8.2 해법 식의 보존이라는 범위에서 맞는다. 새 Metal 구현의 모든 입력·정밀도·옵션에 대한 수치 동일성을 증명한 문장으로 확대하지 않는다. Metal 옵션 차이는 LN1-137·LN1-138에 있다. |

최대 수심 격자의 호출 인수는 다음과 같다.
`cuda/fv1/cuda_fv1_simulate.cu:98–99`:

```cpp
    MaxField max_field(filenames.resrootname, geometry, pitch, offset,
            grid_size, pars.output_precision);
```

`cuda/fv2/cuda_fv2_simulate.cu:90–91`과 `cuda/dg2/cuda_dg2_simulate.cu:95–96`도 같은 인수 목록을 사용한다.
`cuda/cuda_max_field.cuh:13–23`은 다음 순서를 선언한다.

```cpp
    MaxField
    (
        const char* resrootname,
        Geometry& geometry,
        int pitch,
        int offset,
        dim3 grid_size,
        int acceleration,
        int precision = DEFAULT_PRECISION
    );
```

위 파일 4개는 v8.2와 현재 원자료의 바이트 비교에서 같다.
`lisflood.cpp:149`의 기본 `Params.output_precision = 3;`은 acceleration 인수에 들어간다.
따라서 8.2 기본 호출은 `_H` 크기 할당 분기를 선택한다.
`cuda/ghostraster.cpp:21`의 pitch는 `geometry.xsz + 2`다.
`cuda/cuda_max_field.cu:25`는 `maxH[j*cuda::pitch+i]`를 참조한다.
해석: xsz·ysz가 양수일 때 마지막 내부 셀의 인덱스 `ysz*(xsz+2)+xsz`는 `_H` 할당의 마지막 인덱스 `xsz*ysz-1`보다 크다.
이 차이는 작은 격자에서도 존재한다.
격자 크기에 따른 실제 중단 여부는 할당 배치와 실행 환경의 영향도 받는다.
반대 근거는 output_precision이 0일 때 선택하던 padded 할당 분기다.
8.3은 두 할당 분기를 없앴다.
8.3은 `maxH`만 device에 할당한다.
8.3은 사용하지 않던 totalHtm·maxHtm·initHtm의 pinned 할당도 없앴다.
패치는 이 구조체의 인수 순서까지 고치지는 않았다.

| 행 ID | 관련 문서·주석 원문 | 코드 원문 | 판정 | 이유·반대 근거 |
|---|---|---|---|---|
| LN1-134 | `배포 README:32`의 최대 수심 격자 수정과 별개인 출력 정밀도 잔존 | `pars.cpp:990` `if (read_integer_param(param_name, line_number, param_value_ptr, "output_precision", &Parptr->output_precision, verbose, mode))`·`cuda/cuda_max_field.cuh:20–21` `int acceleration,`<br>`int precision = DEFAULT_PRECISION`·`lisflood.h:130` `#define DEFAULT_PRECISION 6` | 불일치(E) | 강함. 세 호출은 output_precision을 acceleration에 전달한다. `.max`의 precision은 기본 6으로 남는다. `cuda/cuda_max_field.cu:126–127`은 그 precision을 writer에 전달한다. 패치는 메모리 크기 결함을 고쳤으나 이 인수 연결은 남겼다. `cuda/fv1/cuda_fv1_simulate.cu:119–121`의 Snapshot 호출은 `verbose, pars.output_precision);`을 전달한다. 이 출력 경로가 반대 근거다. |
| LN1-135 | `배포 README:36`의 `an unused global sync()` | `cuda/adaptive/classes/Tracer.h:5` `#if _USE_TRACER == 1`·`cuda/adaptive/classes/Tracer.h:19` `CHECK_CUDA_ERROR( sync() );`·`cuda/adaptive/utilities/cuda_utils.cuh:10` `cudaError_t sync_device();` | 불일치(E) | 중간. 기본 `_USE_TRACER` 미정의에서는 해당 호출을 컴파일하지 않는다. `_USE_TRACER=1`에서는 패치가 호출 이름을 바꾸지 않았다. 기본 빌드의 충돌 수정과 선택적 tracer 경로의 잔존 결함을 구분한다. CHECK_CUDA_ERROR는 cudaError_t를 요구한다. |
| LN1-136 | `배포 README:135–137` `On a Mac, FV1 runs on the Apple GPU and the other solvers on the CPU.` | `lisflood.cpp:773–805`의 CPU 선택은 SGC·fv1·dg2·그 밖의 IterateQ다. `pars.cpp:590–628`은 fv2·acc_nugrid·mwdg2·hwfv1 상태를 각각 켠다. | 불일치(B) | CPU DG2·classic·SGC 경로는 있다. CPU FV2·acc_nugrid·MWDG2·HWFV1 대응 호출은 없다. CUDA 없는 Mac에서 이 이름들이 각각 같은 해법의 CPU 구현으로 실행된다는 뜻은 성립하지 않는다. |
| LN1-137 | `배포 README:135` `As 8.2.`와 CPU FV1 옵션 처리 | `pars.cpp:300–302`는 `adaptoff`를 읽고 `Statesptr->adaptive_ts = OFF;`를 대입한다. `metal/fv1/metal_fv1_simulate.mm:1024` `NUMERIC_TYPE adaptive_dt = computeTimestep();`·`metal/fv1/metal_fv1_simulate.mm:1027` `adaptive_dt = states->adaptive_ts == ON ? (NUMERIC_TYPE)1e-6 : max_dt;` | 불일치(E) | 강함. Metal은 첫 단계만 adaptive_ts를 검사한다. 다음 단계부터는 adaptoff여도 computeTimestep 결과를 쓴다. CPU `swe/fv1.cpp:61–64`는 adaptive_ts가 ON일 때만 CFL 시간간격으로 바꾼다. 양쪽의 첫 단계 처리 일치가 반대 근거다. |
| LN1-138 | `배포 README:135` `As 8.2.`와 DepthThresh 설정 | `pars.cpp:679` `if (read_numeric_param(param_name, line_number, param_value_ptr, "depththresh", &Solverptr->DepthThresh, verbose, mode))`·`metal/fv1/metal_fv1_simulate.mm:291` `solverParams.depth_thresh = (float)solver.DepthThresh;`·`metal/fv1/metal_fv1_kernels.metal:648` `if (h > DEPTH_THRESH) {`·`metal/fv1/metal_fv1_kernels.metal:11` `#define DEPTH_THRESH 1e-3f` | 불일치(E) | 강함. Metal CFL 커널은 전달받은 사용자 임계값 대신 고정 매크로를 쓴다. 마찰·재구성 커널은 solver.depth_thresh를 쓴다. CPU `swe/fv1.cpp:599`는 `if (H > Solverptr->DepthThresh)`를 쓴다. fv1 뒤의 depththresh 또는 명령행 depththresh로 값을 바꾼 경우에 차이가 난다. 기본값 1e-3에서는 같은 임계값이라는 반대 근거가 있다. |
| LN1-139 | `metal/CMakeLists.txt:8–9` `-fno-fast-math keeps the GPU arithmetic identical to the`·`CPU solver's, so the verification cases are bit-for-bit reproducible.` | `metal/CMakeLists.txt:13` `COMMAND xcrun -sdk macosx metal -fno-fast-math`·`metal/fv1/metal_fv1_simulate.mm:255` `options.fastMathEnabled = YES;` | 코드에만(C) | 사전 컴파일과 소스 fallback은 fast math 설정이 다르다. 숫자 결과가 얼마나 다른지는 실행하지 않았다. 주석의 재현성 결과 자체는 LN1-163의 H에 포함한다. |

### 2.7 패치의 모든 hunk와 실제 판 차이

다음 표의 각 범위는 문맥 줄을 포함한 hunk 범위다.
대조 스크립트는 범위 전체에서 삭제 줄과 문맥 줄을 원문과 검사했다.
대조 스크립트는 추가 줄을 포함한 결과 전체를 현재 파일과 검사했다.
Metal 신규 파일은 첫 줄부터 마지막 줄까지 일치했다.
패치는 `config.float.cmake`를 추가하거나 기본 설정 파일을 바꾸지 않는다.
float 설정은 패치 밖의 별도 배포 파일이다.

| 행 ID | 변경 파일 | 패치 원문 | 8.2 범위 | 현재 범위 | 줄 단위 결과 |
|---|---|---|---|---|---|
| LN1-700 | `CMakeLists.txt` | `패치:4` `@@ -201,7 +201,7 @@` | `v8.2:CMakeLists.txt:201`부터 7줄 | `CMakeLists.txt:201`부터 7줄 | 일치 |
| LN1-701 | `CMakeLists.txt` | `패치:13` `@@ -226,4 +226,12 @@` | `v8.2:CMakeLists.txt:226`부터 4줄 | `CMakeLists.txt:226`부터 12줄 | 일치 |
| LN1-702 | `VersionHistory.h` | `패치:29` `@@ -18,12 +18,18 @@` | `v8.2:VersionHistory.h:18`부터 12줄 | `VersionHistory.h:18`부터 18줄 | 일치 |
| LN1-703 | `cuda/adaptive/utilities/cuda_utils.cu` | `패치:51` `@@ -1,7 +1,7 @@` | `v8.2:cuda/adaptive/utilities/cuda_utils.cu:1`부터 7줄 | `cuda/adaptive/utilities/cuda_utils.cu:1`부터 7줄 | 일치 |
| LN1-704 | `cuda/adaptive/utilities/cuda_utils.cuh` | `패치:63` `@@ -7,7 +7,7 @@` | `v8.2:cuda/adaptive/utilities/cuda_utils.cuh:7`부터 7줄 | `cuda/adaptive/utilities/cuda_utils.cuh:7`부터 7줄 | 일치 |
| LN1-705 | `cuda/cuda_boundary.cu` | `패치:75` `@@ -286,6 +286,7 @@` | `v8.2:cuda/cuda_boundary.cu:286`부터 6줄 | `cuda/cuda_boundary.cu:286`부터 7줄 | 일치 |
| LN1-706 | `cuda/cuda_boundary.cu` | `패치:83` `@@ -317,6 +318,7 @@` | `v8.2:cuda/cuda_boundary.cu:317`부터 6줄 | `cuda/cuda_boundary.cu:318`부터 7줄 | 일치 |
| LN1-707 | `cuda/cuda_max_field.cu` | `패치:94` `@@ -93,18 +93,9 @@` | `v8.2:cuda/cuda_max_field.cu:93`부터 18줄 | `cuda/cuda_max_field.cu:93`부터 9줄 | 일치 |
| LN1-708 | `cuda/cuda_max_field.cu` | `패치:116` `@@ -130,13 +121,16 @@` | `v8.2:cuda/cuda_max_field.cu:130`부터 13줄 | `cuda/cuda_max_field.cu:121`부터 16줄 | 일치 |
| LN1-709 | `cuda/dg2/cuda_dg2_solver.cu` | `패치:138` `@@ -266,9 +266,7 @@` | `v8.2:cuda/dg2/cuda_dg2_solver.cu:266`부터 9줄 | `cuda/dg2/cuda_dg2_solver.cu:266`부터 7줄 | 일치 |
| LN1-710 | `cuda/dg2/cuda_dg2_solver.cu` | `패치:149` `@@ -284,6 +282,8 @@` | `v8.2:cuda/dg2/cuda_dg2_solver.cu:284`부터 6줄 | `cuda/dg2/cuda_dg2_solver.cu:282`부터 8줄 | 일치 |
| LN1-711 | `cuda/dg2/cuda_dg2_solver.cu` | `패치:158` `@@ -355,9 +355,7 @@` | `v8.2:cuda/dg2/cuda_dg2_solver.cu:355`부터 9줄 | `cuda/dg2/cuda_dg2_solver.cu:355`부터 7줄 | 일치 |
| LN1-712 | `cuda/dg2/cuda_dg2_solver.cu` | `패치:169` `@@ -374,6 +372,8 @@` | `v8.2:cuda/dg2/cuda_dg2_solver.cu:374`부터 6줄 | `cuda/dg2/cuda_dg2_solver.cu:372`부터 8줄 | 일치 |
| LN1-713 | `cuda/fv1/cuda_fv1_solver.cu` | `패치:181` `@@ -358,9 +358,7 @@` | `v8.2:cuda/fv1/cuda_fv1_solver.cu:358`부터 9줄 | `cuda/fv1/cuda_fv1_solver.cu:358`부터 7줄 | 일치 |
| LN1-714 | `cuda/fv1/cuda_fv1_solver.cu` | `패치:192` `@@ -379,6 +377,8 @@` | `v8.2:cuda/fv1/cuda_fv1_solver.cu:379`부터 6줄 | `cuda/fv1/cuda_fv1_solver.cu:377`부터 8줄 | 일치 |
| LN1-715 | `cuda/fv1/cuda_fv1_solver.cu` | `패치:201` `@@ -453,9 +453,7 @@` | `v8.2:cuda/fv1/cuda_fv1_solver.cu:453`부터 9줄 | `cuda/fv1/cuda_fv1_solver.cu:453`부터 7줄 | 일치 |
| LN1-716 | `cuda/fv1/cuda_fv1_solver.cu` | `패치:212` `@@ -474,6 +472,8 @@` | `v8.2:cuda/fv1/cuda_fv1_solver.cu:474`부터 6줄 | `cuda/fv1/cuda_fv1_solver.cu:472`부터 8줄 | 일치 |
| LN1-717 | `cuda/fv2/cuda_fv2_solver.cu` | `패치:224` `@@ -225,9 +225,7 @@` | `v8.2:cuda/fv2/cuda_fv2_solver.cu:225`부터 9줄 | `cuda/fv2/cuda_fv2_solver.cu:225`부터 7줄 | 일치 |
| LN1-718 | `cuda/fv2/cuda_fv2_solver.cu` | `패치:235` `@@ -240,6 +238,8 @@` | `v8.2:cuda/fv2/cuda_fv2_solver.cu:240`부터 6줄 | `cuda/fv2/cuda_fv2_solver.cu:238`부터 8줄 | 일치 |
| LN1-719 | `cuda/fv2/cuda_fv2_solver.cu` | `패치:244` `@@ -306,9 +306,7 @@` | `v8.2:cuda/fv2/cuda_fv2_solver.cu:306`부터 9줄 | `cuda/fv2/cuda_fv2_solver.cu:306`부터 7줄 | 일치 |
| LN1-720 | `cuda/fv2/cuda_fv2_solver.cu` | `패치:255` `@@ -321,6 +319,8 @@` | `v8.2:cuda/fv2/cuda_fv2_solver.cu:321`부터 6줄 | `cuda/fv2/cuda_fv2_solver.cu:319`부터 8줄 | 일치 |
| LN1-721 | `format` | `패치:267` `@@ -1 +0,0 @@` | `v8.2:format:1`부터 1줄 | 현재에서 삭제 | 일치 |
| LN1-722 | `lisflood.cpp` | `패치:272` `@@ -27,6 +27,9 @@` | `v8.2:lisflood.cpp:27`부터 6줄 | `lisflood.cpp:27`부터 9줄 | 일치 |
| LN1-723 | `lisflood.cpp` | `패치:282` `@@ -774,6 +777,13 @@` | `v8.2:lisflood.cpp:774`부터 6줄 | `lisflood.cpp:777`부터 13줄 | 일치 |
| LN1-724 | `lisflood.cpp` | `패치:296` `@@ -846,7 +856,7 @@` | `v8.2:lisflood.cpp:846`부터 7줄 | `lisflood.cpp:856`부터 7줄 | 일치 |
| LN1-725 | `metal/CMakeLists.txt` | `패치:308` `@@ -0,0 +1,35 @@` | 8.2에 없음 | `metal/CMakeLists.txt:1`부터 35줄 | 일치 |
| LN1-726 | `metal/fv1/metal_fv1_kernels.metal` | `패치:347` `@@ -0,0 +1,991 @@` | 8.2에 없음 | `metal/fv1/metal_fv1_kernels.metal:1`부터 991줄 | 일치 |
| LN1-727 | `metal/fv1/metal_fv1_simulate.h` | `패치:1342` `@@ -0,0 +1,78 @@` | 8.2에 없음 | `metal/fv1/metal_fv1_simulate.h:1`부터 78줄 | 일치 |
| LN1-728 | `metal/fv1/metal_fv1_simulate.mm` | `패치:1424` `@@ -0,0 +1,1493 @@` | 8.2에 없음 | `metal/fv1/metal_fv1_simulate.mm:1`부터 1493줄 | 일치 |
| LN1-729 | `metal/metal_integrate.cpp` | `패치:2921` `@@ -0,0 +1,14 @@` | 8.2에 없음 | `metal/metal_integrate.cpp:1`부터 14줄 | 일치 |
| LN1-730 | `metal/metal_integrate.h` | `패치:2939` `@@ -0,0 +1,11 @@` | 8.2에 없음 | `metal/metal_integrate.h:1`부터 11줄 | 일치 |
| LN1-731 | `pars.cpp` | `패치:2954` `@@ -962,10 +962,11 @@` | `v8.2:pars.cpp:962`부터 10줄 | `pars.cpp:962`부터 11줄 | 일치 |
| LN1-732 | `pars.cpp` | `패치:2969` `@@ -1076,7 +1077,7 @@` | `v8.2:pars.cpp:1076`부터 7줄 | `pars.cpp:1077`부터 7줄 | 일치 |
| LN1-733 | `preprocess/generateDG2DEM.cpp` | `패치:2981` `@@ -41,6 +41,7 @@` | `v8.2:preprocess/generateDG2DEM.cpp:41`부터 6줄 | `preprocess/generateDG2DEM.cpp:41`부터 7줄 | 일치 |
| LN1-734 | `preprocess/generateDG2start.cpp` | `패치:2992` `@@ -41,6 +41,7 @@` | `v8.2:preprocess/generateDG2start.cpp:41`부터 6줄 | `preprocess/generateDG2start.cpp:41`부터 7줄 | 일치 |

패치 경로 밖의 모델·빌드 파일도 v8.2와 비교했다.
비교 대상은 현재 원자료의 루트 및 모델 하위 디렉터리의 `.cpp`·`.h`·`.cu`·`.cuh`·`.mm`·`.metal`·`.cmake`·`.json`·`.mk`·`.vcxproj`·`.filters`·`.sln`·`.bat`·`.sh`·`.md`와 CMakeLists.txt·makefile·format이다.
외부 라이브러리 묶음과 testing과 `.git`은 이 차이 검색에서 제외했다.
패치 밖에서 내용이 달라진 파일은 없었다.
패치는 기존 파일 13개를 바꾼다.
패치는 Metal 파일 6개를 추가한다.
패치는 format 파일 1개를 삭제한다.
이 세 수는 위 hunk 표의 경로를 변경 유형별로 센 값이다.

### 2.8 8.3 배포 README의 나머지 설정·실행·성과 문장

| 행 ID | 배포 README 원문 | 코드·파일 원문 | 판정 | 이유 |
|---|---|---|---|---|
| LN1-150 | `배포 README:12–15,19–24`의 `source/`·패치·float 설정·테스트 구성 | 배포 압축 해제 루트에는 README·LICENSE·source·patch·config.float.cmake·tests·paper가 있다. `패치:1` `diff -ruN a/CMakeLists.txt b/CMakeLists.txt`는 source root 기준의 a/b 경로를 쓴다. | 일치 | 패치를 전체 8.2에 적용하는 경로 구조는 맞는다. 위키 원자료는 축소 source 폴더를 대체한 것이 아니라 전체 8.2에 패치를 적용한 판이다. |
| LN1-151 | `배포 README:21–23` `without the files the CMake build does not use (Windows and Intel library bundles, the old makefiles, prebuilt binaries, manuals, test data and its git history)` | `CMakeLists.txt:211–216`의 WIN32·_NETCDF 경로는 `windep/netCDF4-64/include`·`windep/netCDF4-64/lib`·`"DLL's/*.dll"`를 사용한다. | 불일치(B) | Windows 라이브러리 묶음을 CMake가 전혀 쓰지 않는다는 설명은 플랫폼 조건을 빠뜨렸다. Linux·Mac 빌드에서는 그 Windows 분기를 사용하지 않는다. 축소 source에는 해당 Windows 묶음이 없다. |
| LN1-152 | `배포 README:24–26` `patch -p1 -E --binary < lisflood-8.2-to-8.3.patch`·`This folder is also a git repository whose two commits are the 8.2 source and the 8.3 changes, so git show displays exactly what changed.` | 패치의 `a/`·`b/` 경로와 format 삭제 hunk는 명령의 strip·삭제 의도에 맞는다. 배포 압축 해제 루트와 source 하위에는 `.git`이 없다. | 불일치(B) | 제공된 Zenodo 배포본에서 두 commit을 가진 저장소 설명은 성립하지 않는다. 이 보고서는 공개 git 저장소를 판 비교 근거로 사용하지 않았다. 패치 자체의 일치는 별도로 확인했다. |
| LN1-153 | `배포 README:67–68` `Needs a C++14 compiler`·`CMake 3.13 or later, NetCDF-C, OpenMP and libnuma.` | `CMakeLists.txt:1,19–21,199–224`의 최저 판·표준·의존성 탐색 | 일치 | Linux 기본 구성과 대응한다. NetCDF는 `_NETCDF=1` 조건이다. libnuma는 UNIX AND NOT APPLE 조건이다. OpenMP의 CMake 탐색은 선택 사항이라는 결함 후보는 LN1-108이다. |
| LN1-154 | `배포 README:67–79,83` `CUDA 11.4 or later (tested with 12.6)`·`module load cuda/12.6 netcdf4/4.9.3 cmake/3.28.3`·`cmake -S source -B build -DCMAKE_BUILD_TYPE=Release -D_CONFIG=$PWD/config.float.cmake -DCMAKE_CUDA_ARCHITECTURES=80`·`cmake --build build -j 16` | `CMakeLists.txt:4–11,72–77`은 사용자 아키텍처·설정 파일·CUDA 컴파일러를 받는다. CUDA 11.4 최저 판 검사는 없다. | 불일치(H) | 명령의 프로젝트 변수 대응은 맞는다. 특정 도구 체인 조합과 module 환경과 병렬 빌드 성공은 외부 도구·실행 환경 주장이다. 최소 CUDA 판을 소스가 강제한다고 쓰지 않는다. |
| LN1-155 | `배포 README:86–87` `If CMake does not find NetCDF, add`·`-DNetCDF_INCLUDE_DIR=<netcdf>/include -DNetCDF_LIBRARY=<netcdf>/lib/libnetcdf.so` | `cmake/Modules/FindNetCDF.cmake:56–63` `find_path(NetCDF_INCLUDE_DIR`·`find_library(NetCDF_LIBRARY`·`cmake/Modules/FindNetCDF.cmake:83` `REQUIRED_VARS NetCDF_LIBRARY NetCDF_INCLUDE_DIR` | 일치 | 수동 탐색 경로가 같은 캐시 변수 이름을 사용한다. 앞선 config·pkg-config 탐색이 성공하면 모듈은 먼저 반환한다. |
| LN1-156 | `배포 README:91–99`의 GPU node 실행·`srun --gres=gpu:1 --time=00:20:00 tests/quick_test.sh build/lisflood`·`nvidia-smi`·잘못된 architecture에서 실행 실패·`unset LD_LIBRARY_PATH` | CMake와 모델 소스는 scheduler 계정·partition·셸의 라이브러리 탐색 환경을 정하지 않는다. | 불일치(H) | 클러스터 운영과 외부 도구 사용법이다. architecture별 실행 성공이나 오류 형태는 이 보고서에서 시험하지 않았다. |
| LN1-157 | `배포 README:103–104` `Needs Xcode with its command-line tools and, from Homebrew,`·`brew install cmake libomp netcdf` | `metal/CMakeLists.txt:13,16`은 `xcrun -sdk macosx metal`과 `xcrun -sdk macosx metallib`를 호출한다. | 불일치(H) | xcrun 호출은 코드에 있다. Xcode·Homebrew 설치와 실제 SDK 준비는 외부 도구 사용법이다. |
| LN1-158 | `배포 README:107,111`의 `-DOpenMP_CXX_FLAGS="-Xclang -fopenmp -I/opt/homebrew/opt/libomp/include"`·`-DOpenMP_C_FLAGS=...`·`-DOpenMP_CXX_LIB_NAMES=omp`·`-DOpenMP_C_LIB_NAMES=omp`·`-DOpenMP_omp_LIBRARY=/opt/homebrew/opt/libomp/lib/libomp.dylib`·`cmake --build build -j 8 --target lisflood generateDG2DEM generateDG2start` | `CMakeLists.txt:67,190,193,199–201`의 대상과 OpenMP::OpenMP_CXX 연결 | 일치 | 모델 대상 이름은 일치한다. OpenMP 캐시 변수는 CMake의 외부 FindOpenMP가 처리한다. Homebrew 고정 경로의 존재나 그 환경의 빌드 성공을 확인한 것은 아니다. |
| LN1-159 | `배포 README:114–115` `The build writes metal_fv1_kernels.metallib next to build/lisflood; keep the two together.` | `metal/CMakeLists.txt:10` `set(METALLIB ${CMAKE_BINARY_DIR}/metal_fv1_kernels.metallib)`·`metal/fv1/metal_fv1_simulate.mm:222–231`은 실행 파일 디렉터리에서 같은 이름을 찾는다. | 일치 | 제시한 Release 단일 구성 빌드의 경로와 대응한다. 로더는 bundle과 현재 디렉터리도 먼저 탐색한다. |
| LN1-160 | `배포 README:43–45` `On the test cases that come with LISFLOOD-FP, wherever 8.2 runs, 8.3 writes the same output files, byte for byte, for FV1, FV2, DG2 and ACC (except the last digit of the mass-balance log, which varies between any two runs).` | 패치는 실행 출력 파일을 포함한 비교 증거가 아니다. | 불일치(H) | byte 비교 결과와 mass log의 마지막 자릿수 변화는 실행 주장이다. 예외절을 뺀 ‘모든 출력이 같다’로 요약하지 않는다. |
| LN1-161 | `배포 README:46–49` `8.2 stops with cudaErrorIllegalAddress under FV1, FV2 and DG2 on the Carlisle and EA test 5 cases (0.58 and 1.7 million cells) and on a 5.2 million-cell grid; 8.3 runs them. Largest grids tested: 5.2 million cells (FV1, FV2, DG2) and 10.6 million (FV1).` | 메모리 결함의 정적 근거는 LN1-120이다. | 불일치(H) | 사례별 중단·완주·최대 시험 격자 수는 실행 결과다. 숫자의 출처는 배포 README:46–49다. |
| LN1-162 | `배포 README:50–51` `NVIDIA Compute Sanitizer finds invalid memory accesses and shared-memory hazards in 8.2 and none in 8.3.` | 패치는 할당과 barrier를 바꾼다. | 불일치(H) | Sanitizer가 탐지한 오류 수와 ‘none’은 정적 대조가 확정할 수 없다. 이 보고서는 Sanitizer를 실행하지 않았다. |
| LN1-163 | `배포 README:52–58` `On a 24 h, 10.6 million-cell flood simulation on an NVIDIA A100, 8.3 needs 9.4 min where 8.2 (with the maximum-depth grid allocated at full size, the minimum for it to run) needed 105 min.`·`on a grid without NoData cells it is 72 % at 0.5 million cells and 85-89 % at 2 to 8 million, and a few seconds on small grids.`·`The Metal FV1 solver takes the same time steps as the CPU solver on the three cases of the paper and agrees with it to within single-precision rounding.` | 패치는 실행 시간·오차 표를 코드로 계산하여 고정하지 않는다. `metal/CMakeLists.txt:8–9`에도 bit-for-bit 재현성 주석이 있다. | 불일치(H) | 속도 수치·시험 조건·세 사례의 시간간격·반올림 범위 일치는 모두 실행 주장이다. 숫자의 출처는 배포 README:52–58이다. |
| LN1-164 | `배포 README:59–60` `The other GPU solvers of 8.2 (acc_nugrid and the adaptive MWDG2/HWFV1) are unchanged apart from the build fix` | 8.2와 현재의 `cuda/acc_nugrid/` 내용은 같다. adaptive의 변경은 utilities/cuda_utils.cu·cuh의 sync 이름뿐이다. | 일치 | 패치 경로와 전체 차이 검색이 이 범위를 뒷받침한다. 선택적 tracer의 잔존 호출은 별도 LN1-135다. |
| LN1-165 | `배포 README:60,62–63` `were not tested.`·`Tested on: Red Hat Enterprise Linux 8.10, GCC 8.5, CUDA 12.6, NVIDIA A100 (40 GB); macOS 27, Xcode 27, Apple M1 Max (32 GPU cores, 64 GB).` | 시험 이력은 모델 소스의 분기나 대입이 아니다. | 불일치(H) | 미시험 해법과 시험 환경에 관한 저자 보고다. 이 보고서의 실행 확인 사실로 옮기지 않는다. |
| LN1-166 | `배포 README:120,123` `build/lisflood -version`·`prints LISFLOOD-FP 8.3 among its start-up lines.` | `lisflood.cpp:286` `printversion(verbosemode);`·`lisflood.cpp:289` `for (i = 1; i < argc; i++) if (!strcmp(argv[i], "-version")) return(0);`·`lisflood.cpp:859` `printf(" LISFLOOD-FP %s\n", LF_Release);` | 일치 | -version은 parfile을 읽기 전에 출력하고 정상 반환한다. 이 결과는 소스 흐름에 대한 판정이다. |
| LN1-167 | `배포 README:126–131` `tests/quick_test.sh build/lisflood`·`GPU=metal tests/quick_test.sh build/lisflood`·`ends with QUICK TEST PASSED` | 테스트 스크립트의 기대 메시지는 모델 실행의 관측 결과가 아니다. | 불일치(H) | 외부 스크립트 사용법과 통과 결과다. 이 보고서는 테스트를 실행하지 않았다. |
| LN1-168 | `배포 README:135–136` ``Put `cuda` in the `.par` file, or pass `-cuda`, to run on the GPU; on a Mac `metal` / `-metal` means the same.`` | `pars.cpp:965–968`의 cuda·metal read_empty_param과 `Statesptr->cuda = ON;`·`pars.cpp:1031` `param_ptr = &argv[i][1];`·`pars.cpp:1036` `CheckParam(param_ptr, param_value, i, Fnameptr, Statesptr, Parptr, Solverptr, verbose, CMD_LINE);` | 일치 | 두 이름은 같은 GPU 상태를 켠다. 해당 해법 선택은 별도 상태다. GPU 상태 기본값은 `lisflood.cpp:268`의 OFF다. |
| LN1-169 | `배포 README:141–142` `GNU General Public License v3.0 (LICENSE), the licence cited in the LISFLOOD-FP 8.0 and 8.2 papers and agreed with the LISFLOOD-FP developers.` | `배포 LICENSE:1–2` `GNU GENERAL PUBLIC LICENSE`<br>`Version 3, 29 June 2007` | 불일치(H) | 동봉 파일의 판 표기는 대응한다. 논문의 라이선스 서술과 개발자의 합의 여부는 모델 코드 대조 대상이 아니다. |

## 3 코드에만 있는 처리

이 절의 ‘문서’는 이번 작업의 README·INSTALL·8.3 배포 README다.
이 절은 매뉴얼 3종 전체에 기능이 없다고 단정하지 않는다.
앞 절에서 이미 판정한 코드는 같은 행 ID를 참조한다.
이 참조는 분류별 개수에 다시 더하지 않는다.

`pars.cpp:965–971`은 문서의 두 GPU 키워드를 같은 상태에 연결한다.

```cpp
    if (read_empty_param(param_name, line_number, param_value_ptr, "cuda", verbose, mode) ||
        read_empty_param(param_name, line_number, param_value_ptr, "metal", verbose, mode))
    {
        Statesptr->cuda = ON; // the GPU switch, for CUDA and Metal alike
        if (verbose == ON) printf("GPU enabled\n");
        return;
    }
```

`lisflood.cpp:268–269`의 초기 상태는 다음과 같다.

```cpp
    SimStates.cuda = OFF;
    SimStates.fv1 = OFF;
```

`pars.cpp:582–589`의 FV1 해법 선택은 다음과 같다.

```cpp
    if (read_empty_param(param_name, line_number, param_value_ptr, "fv1", verbose, mode))
    {
        Statesptr->fv1 = ON;
        Solverptr->cfl = C(0.5);
        Solverptr->DepthThresh = C(1e-3);
        if (verbose == ON) printf("Using FV1 2D SWE solver\n");
        return;
    }
```

이 인용도 탭을 공백으로 표시한다.

| 행 ID | 문서에 없는 옵션·검사·처리 | 코드 원문과 조건 | 판정 |
|---|---|---|---|
| LN1-180 | 기본 CMake의 CUDA 해법 목록은 README의 FV1·DG2보다 넓다. | `CMakeLists.txt:102–178`은 FV2·ACC·acc_nugrid·adaptive를 추가한다. `lisflood.cpp:422–450`은 fv1·fv2·dg2·acceleration·acc_nugrid·mwdg2/hwfv1 상태를 각각 처리한다. | 코드에만(C) |
| LN1-181 | CMake는 주 실행 파일 외에 전처리·후처리 실행 파일을 만든다. | `CMakeLists.txt:190–197`은 generateDG2DEM·generateDG2start·DG2downscale을 만든다. README.md는 이 세 대상의 생성과 사용을 설명하지 않는다. 배포 README:111은 전처리 대상 둘만 명령에 적는다. | 코드에만(C) |
| LN1-182 | NetCDF를 끈 구성은 출력과 동적 강우에 같은 방식으로 대응하지 않는다. | `lisflood2/file_tool.cpp:431`은 `printf("WARNING: NetCDF selected but not enabled in this build\n");`를 실행한다. `lisflood2/file_tool.cpp:787–788`은 `if (output_params->ascii_out == ON \|\|`<br>`(output_params->netcdf_out == ON && write_netcdf == 0)) // if netcdf not implemented for this grid, default to ascii`에서 ASCII를 쓴다. `pars.cpp:996–1003`은 dynamicrainfile을 읽고 `_NETCDF != 1`이면 `exit(1);`을 실행한다. | 코드에만(C) |
| LN1-183 | GPU 지원이 없는 실행 파일은 GPU 요청을 거부한다. | `pars.cpp:1080–1086` `#if !defined(CUDA) && !defined(METAL_ENABLED)` 안에서 `Statesptr->cuda == ON`이면 오류를 출력하고 `exit(1);`을 실행한다. | 코드에만(C) |
| LN1-184 | max_Froude 키워드는 컴파일 모드를 요구한다. | `pars.cpp:923`은 `"max_Froude"`를 읽는다. `pars.cpp:926–930`은 `_CALCULATE_Q_MODE != 1`에서 오류와 제거 안내를 출력하고 `exit(EXIT_FAILURE);`을 실행한다. 본체 기본값은 `lisflood.cpp:144` `Params.max_Froude = C(10000.0);`이다. | 코드에만(C) |
| LN1-185 | 기본 CMake의 단면 제한과 성능·진단 모드는 별도 컴파일 선택이다. | `_ONLY_RECT=1`, `_CALCULATE_Q_MODE=1`, `_SGM_BY_BLOCKS=0`, `_BALANCE_TYPE=0`, `_DISABLE_WET_DRY=0`, `_PROFILE_MODE=0`의 효과는 LN1-072–077에 있다. `_PROFILE_MODE>1`은 `lisflood2/sgm_fast.cpp:4837–4839`에서 최종 출력 전에 `exit(0);`을 실행한다. 같은 모드는 `lisflood2/sgm_fast.cpp:4670–4688`의 `#if _PROFILE_MODE < 2` 조건에서 정기 격자 출력을 제외한다. | 코드에만(C) |
| LN1-186 | Metal 빌드와 실행은 두 단계의 가용성 조건을 사용한다. | `metal/CMakeLists.txt:6` `if(METAL_FRAMEWORK AND FOUNDATION_FRAMEWORK)`·`metal/fv1/metal_fv1_simulate.mm:1326–1328` `bool Simulator::is_available() {`<br>`id<MTLDevice> device = MTLCreateSystemDefaultDevice();`<br>`return device != nil;` | 코드에만(C) |
| LN1-187 | Metal shader 로더는 여러 위치와 소스 fallback을 사용한다. | `metal/fv1/metal_fv1_simulate.mm:209–258`은 bundle·현재 디렉터리·실행 파일 디렉터리·실행 파일 기준 `../metal/fv1/metal_fv1_kernels.metal` 순서로 탐색한다. `metal/fv1/metal_fv1_simulate.mm:1358–1365`는 초기화 실패 메시지 뒤 `return;`한다. | 코드에만(C) |
| LN1-188 | Metal은 rainfallmask·routing 조합을 명시적으로 거부한다. | `metal/fv1/metal_fv1_simulate.mm:1347–1355` `if (states.rainfallmask == ON \|\| states.routing == ON)`에서 오류 후 `std::exit(EXIT_FAILURE);`을 실행한다. `states.rainfall == ON && !arrays.rain`도 오류 후 종료한다. | 코드에만(C) |
| LN1-189 | Metal은 DEM의 GPU 기준면과 NoData 표고를 바꾼다. | `metal/fv1/metal_fv1_simulate.mm:531` `dem_offset = any_valid ? (float)min_valid : 0.0f;`·`metal/fv1/metal_fv1_simulate.mm:533` `const float kMargin = 1000.0f;`·`metal/fv1/metal_fv1_simulate.mm:536–541`은 벽·구덩이·범위 내부 표고를 구분한다. `metal/fv1/metal_fv1_simulate.mm:871,874–875`는 수위 경계도 같은 dem_offset으로 옮긴다. | 코드에만(C) |
| LN1-190 | Metal은 float GPU 배열과 NUMERIC_TYPE CPU 배열 사이에서 성분을 변환한다. | `metal/fv1/metal_fv1_simulate.mm:575–580`은 H·HU·DEM을 float로 변환한다. `metal/fv1/metal_fv1_simulate.mm:579` `d_HV[gpu_idx] = -(float)h_HV[cpu_idx];`·`metal/fv1/metal_fv1_simulate.mm:725` `h_HV[cpu_idx] = -(NUMERIC_TYPE)d_HV[gpu_idx];`는 HV 부호를 바꾼다. `metal/fv1/metal_fv1_kernels.metal:514`의 주석은 Metal의 y축이 south를 향한다고 적는다. | 코드에만(C) |
| LN1-191 | Metal의 point source·동적 강우·최대 수심은 별도 처리 경로를 갖는다. | `metal/fv1/metal_fv1_simulate.mm:891–958`은 point source를 shared GPU H에 직접 적용한다. `metal/fv1/metal_fv1_simulate.mm:1075`의 `if (time >= last_rain_time + 1.0 \|\| last_rain_time < 0)`은 강우 업로드 간격을 둔다. `metal/fv1/metal_fv1_simulate.mm:1263–1278`은 매 단계 maxH 커널을 제출한다. `metal/fv1/metal_fv1_simulate.mm:1476–1477`은 최종 `.max`를 CPU에 복사하여 쓴다. | 코드에만(C) |
| LN1-192 | GPU 요청만으로는 FV1 해법을 선택하지 않는다. | `pars.cpp:965–970`은 cuda·metal을 읽고 GPU 상태만 켠다. `pars.cpp:582–589`은 fv1 키워드에서 FV1 상태와 cfl·DepthThresh를 설정한다. `lisflood.cpp:773–788`은 SGC를 FV1보다 먼저 검사한다. | 코드에만(C) |
| LN1-193 | -version 외의 일반 실행은 마지막 인수로 parfile을 요구한다. | `pars.cpp:38–45` `if (argc == 1 \|\| argv[argc - 1][0] == '-')`이면 `printf("no parameter file specified\n");` 후 `exit(-1);`한다. `ReadParamFile(argv[argc-1], ...)` 뒤 명령행 설정을 읽는다. | 코드에만(C) |

기존 코드만 있는 진단·시험 선택은 LN1-082–093에 전부 열거했다.
기본 make와 옛 `.mk` 사이의 연결 누락은 LN1-105·LN1-106이다.
메모리 수정 뒤 남은 precision 인수는 LN1-134다.
비활성 tracer의 sync 호출은 LN1-135다.
Metal의 고정 시간간격·사용자 수심 임계값 차이는 LN1-137·LN1-138이다.

## 4 노트 대조와 수정안

다음 표는 현재 노트의 이번 작업 관련 문장만 대조한다.
이 보고서는 아래 수정안을 노트에 적용하지 않았다.
A의 판 기준은 사용자 제공 Zenodo 8.2 배포일 2024-07-29와 8.3 배포일 2026-10-13이다.
소스 내부의 연혁 날짜는 `VersionHistory.h:31`의 `8.3  Oct 07 2026`이다.
이 날짜는 Zenodo 배포일과 구분한다.
`v8.2:VersionHistory.h:27–28`에는 8.1·8.0 연혁만 있다.
`VersionHistory.h:21–23`은 checkpoint 숫자를 유지하고 8.3 표시 이름을 추가했다고 명시한다.
이 근거는 8.2 판독 노트와 현재 8.3 원자료의 차이를 A로 분류하는 기준이다.
옛 문서와 코드 사이에 이미 있던 오기는 A로 분류하지 않는다.

| 행 ID | 노트 원문 | 코드 원문·판 근거 | 판정 | 노트 수정안 |
|---|---|---|---|---|
| LN1-230 | `노트 README.md:1` `# LISFLOOD-FP — 2D 수리 침수 모델 (v8.2)`·`노트 README.md:11` `- **버전**: **v8.2** (2024-07-29).`·`노트 README.md:14` `- **canonical 정본 소스**: **Zenodo doi:10.5281/zenodo.13121102** (v8.2 아카이브).` | `v8.2:VersionHistory.h:16–18`의 8·1·0·현재 `VersionHistory.h:23` `#define LF_Release "8.3"`·`패치:29–47` | 불일치(A) | 현재 원자료는 Zenodo 8.2 전체 배포본에 8.3 패치를 적용한 판이다. 표시 판 이름은 8.3이다. 내부 checkpoint 숫자는 8.1.0으로 유지한다. 두 DOI의 역할을 나누어 적는다. |
| LN1-231 | `노트 README.md:13` `- **언어**: C++ + CUDA. CMake ≥3.13 빌드 (Windows MSVC/Intel · Linux). netCDF·libnuma 의존.` | `패치:13–25,305–343`·현재 `CMakeLists.txt:204` `if (UNIX AND NOT APPLE)`·`metal/CMakeLists.txt:22–29` | 불일치(A) | 현재 소스는 Apple Metal FV1을 추가한다. Metal host 구현은 Objective-C++ 파일을 포함한다. libnuma는 Linux 계열 UNIX 분기에서 요구한다. NetCDF는 _NETCDF 설정에 따른다. |
| LN1-232 | `노트 README.md:12` `- **라이선스**: **GNU GPL-2.0** (Zenodo 메타데이터; repo LICENSE 파일 본문 부재).`·`노트 web-refs/lisflood-fp-official-resources.md:31` `- license: **GPL-2.0** · file: LISFLOOD-FP-v8.2.zip (348 MB, 3170 files)` | 8.3 별도 패키지 `배포 LICENSE:1–2` `GNU GENERAL PUBLIC LICENSE`<br>`Version 3, 29 June 2007`·`배포 README:141–142` | 불일치(A) | 8.2 Zenodo 메타데이터 기록은 8.2에 귀속하여 보존한다. 8.3 별도 패키지는 GPL v3 본문을 동봉한다. 개발자 합의와 논문 라이선스 주장은 H로 구분한다. |
| LN1-233 | `노트 manual-notes/lisflood-fp-user-manual.md:363` ``libnuma 비표준 경로면 `-DNUMA_ROOT=<path>`.`` | `cmake/Modules/FindNUMA.cmake:10,14`의 `NUMA_ROOT_DIR`·같은 `v8.0:`·`v8.1:` 모듈의 같은 줄 | 불일치(B) | 비표준 NUMA 경로는 이 배포본의 자체 모듈에 맞추어 -DNUMA_ROOT_DIR=<path>로 지정한다. |
| LN1-234 | `노트 manual-notes/lisflood-fp-user-manual.md:367` ``compute capability는 `config.default.cmake`에서 조정.`` | `CMakeLists.txt:4–6`은 미정의 CMAKE_CUDA_ARCHITECTURES를 61로 설정한다. 기본 설정 파일에는 해당 변수가 없다. | 불일치(B) | CUDA 아키텍처는 -DCMAKE_CUDA_ARCHITECTURES=<값>으로 지정한다. 배포된 config.default.cmake에는 아키텍처 항목이 없다. |
| LN1-235 | `노트 manual-notes/lisflood-fp-user-manual.md:368` ``- (구) Makefile: `INSTALL.md` — `CONFIG=config/<file> make -f Makefile.new <target>`.`` | 현재와 v8.0·v8.1·v8.2의 INSTALL.md:3은 같은 오기를 갖는다. 실제 루트 파일은 `makefile:1–160`이다. | 불일치(B) | INSTALL의 Makefile.new 이름은 배포 파일 이름과 다르다. 실제 makefile을 명시하되 CUDA 소스 집합의 누락을 함께 적는다. |
| LN1-236 | `노트 manual-notes/lisflood-fp-user-manual.md:366` ``- 기본 구성은 `config.default.cmake`. 복사·수정 후 Windows는 `CMakeSettings.json`의 `cmakeCommandArgs`에 `-D_CONFIG=<filename>`, Linux는 `cmake -S . -B build -D_CONFIG=<filename>`.`` | `CMakeLists.txt:10–11`의 `_CONFIG`·`CMakeSettings.json:11,22,33,56`의 cmakeCommandArgs | 일치 | 기본 설명을 유지한다. 기본 _NUMERIC_MODE=1과 float 설정의 _NUMERIC_MODE=0을 추가한다. |
| LN1-237 | `노트 source-analysis/lisflood-fp-architecture-source-map.md:61` `**dg2new = multiwavelet 적응**`·`노트 source-analysis/lisflood-fp-architecture-source-map.md:83` ``- `swe/dg2new.cpp` — DG2 multiwavelet 적응 격자(v8.2 핵심, Kesserwani)`` | `v8.2:CMakeLists.txt:26–65`에는 dg2new가 없다. `v8.2:makefile:31`은 파일을 컴파일한다. `lisflood.cpp:794–796`의 실행 호출은 주석이다. 실제 adaptive는 `CMakeLists.txt:178`의 별도 디렉터리다. | 불일치(B) | dg2new는 비가동 CPU DG2 리팩터 구현이다. MWDG2·HWFV1은 CUDA adaptive 경로다. 소스 파일의 포함과 런타임 해법 선택을 구분한다. 기존 swe 노트:29–38의 정정과 맞춘다. |
| LN1-238 | `노트 source-analysis/lisflood-fp-swe-fv1-dg2.md:291` ``**이 코드는 `lisflood.cpp:784`에서 주석 처리되어 빌드/실행에 포함되지 않는다.**`` | `v8.2:makefile:31`과 현재 `makefile:31`은 `swe/dg2new.cpp \`를 적는다. CMake 목록에는 이 파일이 없다. 현재 `lisflood.cpp:794–796`은 호출을 주석 처리한다. | 불일치(B) | 기본 CMake는 dg2new를 컴파일하지 않는다. 옛 makefile은 이 파일을 컴파일한다. 본체는 어느 경로에서도 주석 처리된 DG2Solver 호출을 실행하지 않는다. |
| LN1-239 | `노트 source-analysis/lisflood-fp-swe-fv1-dg2.md:26–27` ``디스패치는 `lisflood.cpp:775` (`Statesptr->fv1 == ON`) / `:780` (`Statesptr->dg2 == ON`)에서 분기한다.`` | `v8.2:lisflood.cpp:775–782`의 CPU 호출·현재 `lisflood.cpp:778–793`의 METAL_ENABLED 조건과 CPU 호출·`패치:282–295` | 불일치(A) | 현재 FV1 상태 분기는 METAL_ENABLED와 GPU 요청과 장치 가용성을 검사한다. 조건이 맞으면 Metal FV1을 호출한다. 그 밖에는 CPU FV1을 호출한다. |
| LN1-240 | `노트 source-analysis/lisflood-fp-classic-acc-flow.md:46` ``\| `Statesptr->fv1==ON` \| `fv1::solve(...)` (:777) \| full SWE FV1 \|`` | 현재 `lisflood.cpp:780–788`·`패치:282–295`·노트 작성일 `노트 source-analysis/lisflood-fp-classic-acc-flow.md:9` `note_date: 2026-06-18` | 불일치(A) | 8.2의 CPU 분기 설명에 8.3의 Metal 조건부 호출을 추가한다. CUDA 분기를 지나지 않았다는 사실만으로 CPU 실행이라고 단정하지 않는다. |
| LN1-241 | `노트 source-analysis/lisflood-fp-io-boundary.md:61` ``CUDA 미컴파일 시 `cuda` 옵션 abort(1079-1085).`` | `v8.2:pars.cpp:1079` `#ifndef CUDA`·현재 `pars.cpp:1080` `#if !defined(CUDA) && !defined(METAL_ENABLED)`·`패치:2969–2977` | 불일치(A) | CUDA와 Metal을 모두 포함하지 않은 빌드에서만 GPU 요청을 거부한다. cuda와 metal 키워드는 같은 GPU 상태를 켠다. |
| LN1-242 | `노트 source-analysis/lisflood-fp-cuda-gpu.md:17` `솔버 패밀리는 4종으로 분기한다:`·`노트 source-analysis/lisflood-fp-cuda-gpu.md:229` `4개 솔버 패밀리(fv1/dg2/acc/acc_nugrid)` | `v8.2:CMakeLists.txt:102–107`의 FV2·`v8.2:CMakeLists.txt:178`의 adaptive 추가·현재 동일 목록·`lisflood.cpp:422–450`의 분기 | 불일치(B) | 현재 CUDA 디렉터리 계열은 FV1·FV2·DG2·ACC·acc_nugrid·adaptive다. adaptive는 HWFV1과 MWDG2 상태를 처리한다. FV2와 adaptive는 8.2에도 있었으므로 8.3 판 차이로 분류하지 않는다. |
| LN1-243 | `노트 source-analysis/lisflood-fp-cuda-gpu.md:109` ``shared 저장, `__syncthreads()` 후 좌/우 flux 차분으로 갱신:`` | v8.2의 기존 쓰기 후 barrier·현재 FV1 `cuda/fv1/cuda_fv1_solver.cu:380–381,475–476`의 reader 후 barrier·`패치:181–220` | 불일치(A) | 8.3 flux 커널은 shared 쓰기 후와 읽기 후에 각각 동기화한다. 첫 thread는 reader 작업만 건너뛴다. 마지막 barrier는 모든 참여 thread가 통과한다. |
| LN1-244 | `노트 source-analysis/lisflood-fp-cuda-gpu.md:195` ``- 통계/최대수심장/스냅샷/스테이지 샘플러 객체(`:97-133`).`` | `cuda/cuda_max_field.cu:97–98,124–135`의 device 할당·출력 복사·해제·`패치:94–134` | 코드에만(C) | 8.3 MaxField는 padded device 배열을 유지한다. `.max`를 쓸 때 host로 복사한다. precision 인수의 잔존 결함은 별도로 적는다. |
| LN1-245 | `노트 source-analysis/lisflood-fp-lisflood2-driver.md:165` ``blocks 경로(`:3663-3667`)는 `j` 변수 미정의 등 빌드 조건부 코드`` | `lisflood2/sgm_fast.cpp:3656–3667`·`lisflood2/lisflood_processing.cpp:1793–1800`·`config.default.cmake:7` `_SGM_BY_BLOCKS=0` | 일치 | 기본값 0에서는 이 분기를 제외한다. 값 1에서는 j·max_Froude 인수·FP_xwidth 철자 결함 후보가 있다. 관찰을 일반적인 두 전략의 동등 지원으로 확대하지 않는다. |
| LN1-246 | `노트 source-analysis/lisflood-fp-lisflood2-driver.md:152` `` `LATLONGMODE` 시 lat/lon``·`` `_NETCDF != 1` 빌드면 `StartNetCDF`(`:418-433`)가 경고만 출력하고 ascii fallback. `` | `lisflood2/file_tool.cpp:191,296`의 LATLONGMODE·`lisflood2/file_tool.cpp:431`의 경고·`lisflood2/file_tool.cpp:787–788`의 write_grid fallback | 일치 | LATLONGMODE는 제공된 빌드 파일에서 정의하지 않는다. 경고는 StartNetCDF가 출력한다. 실제 ASCII fallback은 write_grid가 수행한다. 런타임 latlong과 구분한다. |
| LN1-247 | `노트 source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:7` `raw v8.2 cuda/adaptive/ 직접 read`·`노트 source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:20` `` `lisflood.cpp:444-448`, CUDA 빌드 전용`` | 현재 `lisflood.cpp:447–450`·`패치:51–71`의 sync_device 변경·`VersionHistory.h:31–32` | 불일치(A) | 적응 해법 본체는 8.2와 같다. 8.3은 공통 utility의 전역 sync 이름을 바꾼다. 현재 본체 진입 줄은 447–450이다. 8.2 판독 근거와 현재 판의 줄을 나누어 표시한다. |
| LN1-248 | `노트 web-refs/lisflood-fp-official-resources.md:25` `**v8.2 정본 소스**`·`노트 web-refs/lisflood-fp-official-resources.md:29–30`의 8.2·2024-07-29·10.5281/zenodo.13121102 | `배포 README:19–24`의 8.2 기반 패치 설명·현재 `VersionHistory.h:23`의 LF_Release | 불일치(A) | 기존 8.2 서지 항목은 보존한다. 현재 원자료가 적용한 8.3 패키지와 패치의 역할을 별도 항목으로 추가한다. |

`source-analysis/lisflood-fp-channel-sgc.md`도 빌드·매크로·8.3 관련 표현으로 검색했다.
이 노트에서는 이번 빌드·배포 설명에 직접 대응하는 추가 수정 문장을 선정하지 않았다.
이 판단은 channel·SGC 수치식 전체의 일치를 판정한 것이 아니다.

## 5 차이 결론

이 절의 고유 행 ID는 88개다.
이 수는 2·3·4절에서 불일치 또는 코드에만으로 판정한 행 ID를 중복 없이 센 값이다.
파일 목록·소스 목록·전처리 목록·hunk 목록은 이 차이 개수에 다시 넣지 않았다.
E는 코드 결함 후보의 근거 강도를 함께 표시한다.
8.3이 고친 결함은 8.2에 귀속했다.
H는 코드에 대응하지 않는 주장으로 결론을 확정한 분류다.
H는 모델을 실행하여 확인했다는 뜻이 아니다.
이 작업에서는 D·F·X에 해당하는 차이 행이 없다.
문서의 잘못된 파일 이름은 같은 기능의 실제 파일이 있으므로 B로 분류했다.
논문의 식·계수를 추가로 가져와야만 판정할 항목은 이 빌드·배포 설명 범위에 없다.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| LN1-006 | Visual Studio 실행·디버그 절차 | H 코드 대조 대상 아님 | `README.md:14` `CMake Targets View`·`Add Debug Configuration`. | IDE 화면 조작은 외부 도구 사용법이다. |
| LN1-007 | Linux 설치 명령 | H 코드 대조 대상 아님 | `README.md:22–23` `sudo snap install cmake --classic`·`sudo apt install libnuma-dev libnetcdf-dev`. | 설치 명령의 성공은 코드 대조로 확인하지 않았다. |
| LN1-012 | NUMA 경로 변수 이름 | B 문서 오기 | `README.md:37` `-DNUMA_ROOT=<path>`·`cmake/Modules/FindNUMA.cmake:10` `HINTS ${NUMA_ROOT_DIR}/include)`. | 이 배포본의 NUMA 탐색 힌트 변수는 NUMA_ROOT_DIR다. |
| LN1-016 | CUDA 아키텍처 안내 위치 | B 문서 오기 | `README.md:65` `see config.default.cmake`·`CMakeLists.txt:5` `set(CMAKE_CUDA_ARCHITECTURES 61)`. | 배포된 기본 설정 파일에는 CUDA 아키텍처 항목이 없다. |
| LN1-017 | INSTALL의 makefile 이름 | B 문서 오기 | `INSTALL.md:3` `CONFIG=config/<file> make -f Makefile.new <target>`·`makefile:1` `-include $(CONFIG)`. | INSTALL의 Makefile.new는 실제 makefile의 파일 이름 오기다. |
| LN1-082 | VS Debug 추가 정의 | C 문서 누락 | `lisflood.vcxproj:502,524` `WIN32;_DEBUG;_CONSOLE;%(PreprocessorDefinitions)`. | VS Debug는 WIN32와 _CONSOLE도 정의한다. 모델 본체는 _CONSOLE 조건을 사용하지 않는다. |
| LN1-083 | Thrust/CUB 컴파일 정의 | C 문서 누락 | `CMakeLists.txt:77` `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)`. | THRUST_IGNORE_CUB_VERSION_CHECK는 모델 소스가 직접 검사하지 않는 컴파일 정의다. |
| LN1-084 | TESTING의 비활성 기본 상태 | C 문서 누락 | `lisflood.h:55` `//#define TESTING`·`lisflood.cpp:39–41` `#ifdef TESTING`·`RunTests();`·`exit(0);`. | TESTING은 소스에 있으나 제공된 빌드 파일은 이 매크로를 정의하지 않는다. |
| LN1-085 | LATLONGMODE와 latlong의 구별 | C 문서 누락 | `lisflood2/file_tool.cpp:191` `#ifdef LATLONGMODE`·`pars.cpp:870` `Statesptr->latlong = ON;`. | 런타임 latlong 키워드는 LATLONGMODE를 정의하지 않는다. |
| LN1-086 | 선택적 tracer | C 문서 누락 | `cuda/adaptive/classes/Tracer.h:5` `#if _USE_TRACER == 1`. | 제공된 빌드 파일은 _USE_TRACER를 정의하지 않는다. |
| LN1-087 | 별도 진단 서식 매크로 | C 문서 누락 | `lisflood2/sgm_fast.cpp:4534` `#ifdef _DEBUGxx`. | _DEBUGxx는 _DEBUG와 별개의 출력 서식 스위치다. |
| LN1-088 | acc_nugrid의 소스 내부 기본값 | C 문서 누락 | `cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:5` `#define THREADS_PER_BLOCK_MRA 256`·`cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh:23,27`의 `NUM_VARS 4`·`NUM_CHILDREN 4`. | acc_nugrid는 블록·트리 기본값을 소스 헤더에서 정의한다. |
| LN1-089 | adaptive의 소스 내부 기본값 | C 문서 누락 | `cuda/adaptive/utilities/BLOCK_VAR_MACROS.cuh:5` `#define THREADS_PER_BLOCK 256`·`cuda/adaptive/mra/extra_significance.cuh:4` `#define M_BAR C(1.5)`. | adaptive의 블록 크기 기본값은 256이다. M_BAR 기본값은 C(1.5)다. |
| LN1-090 | 플랫폼·컴파일러 식별 조건 | C 문서 누락 | `cuda/cuda_atomic.cuh:5` `#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ < 600`·LN1-600–635의 전체 조건 목록. | 플랫폼·컴파일러 식별 조건은 빌드 파일의 사용자 설정 매크로와 구분한다. |
| LN1-091 | 외부 SDK의 조건 이름 | C 문서 누락 | `cuda/common/helper_cuda.h:68` `#ifdef CUBLAS_API_H_`·`cuda/common/helper_cuda.h:337`의 NPP 판 식. | helper 헤더의 SDK 조건 이름은 모델 기능의 누락 정의가 아니다. |
| LN1-092 | include guard·호환 매크로 | C 문서 누락 | `lisflood.h:68–72`의 `#ifndef cbrt`·`#ifndef cbrtf`·`cuda/common/helper_string.h:29` `#ifndef COMMON_HELPER_STRING_H_`. | include guard와 호환 매크로는 헤더가 직접 정의한다. |
| LN1-093 | 그 밖의 소스 내부 매크로 | C 문서 누락 | LN1-640–659의 정의 목록·`lisflood.h:129` `#define DEM_NO_DATA C(1e7)`·`cuda/cuda_solver.cuh:2` `#define CUDA_BLOCK_SIZE_X 16`. | 자료형·상수·필터·오류 처리 매크로는 소스 내부 정의와 빌드 정의를 나누어 기록한다. |
| LN1-100 | CPU 소스 집합 차이 | C 문서 누락 | `makefile:31` `swe/dg2new.cpp \`·`lisflood.vcxproj:668` `<ClCompile Include="tests.cpp" />`. | make와 VS의 추가 소스 파일은 기본 CMake 소스 집합과 다르다. |
| LN1-101 | make CUDA 소스 누락 | E 코드 결함 후보(강함) | `makefile:53–84`의 CUDA 목록·`lisflood.cpp:427–450`의 FV2·ACC·acc_nugrid·adaptive 호출·`CMakeLists.txt:102–178`의 대응 구현 목록. `lisflood.cpp:429` `lis::cuda::fv2::Simulation simulation;` | 옛 makefile의 CUDA 목록은 현재 CUDA 진입점이 참조하는 모든 해법 구현을 연결하지 않는다. |
| LN1-102 | 보조 실행 파일 집합 차이 | C 문서 누락 | `CMakeLists.txt:193` `add_executable(generateDG2start preprocess/generateDG2start.cpp)`·`makefile:123–132`의 별도 app 대상. `CMakeLists.txt:193` `add_executable(generateDG2start preprocess/generateDG2start.cpp)` | CMake와 make의 테스트·전처리·후처리 대상 집합은 다르다. |
| LN1-103 | 구성별 정밀도·단면 값 차이 | C 문서 누락 | `config.default.cmake:2–3`의 `_NUMERIC_MODE=1`·`_ONLY_RECT=1`·`float 설정:2`의 `_NUMERIC_MODE=0`·`lisflood.vcxproj:305`의 `_ONLY_RECT=0;_NUMERIC_MODE=0`. `config.default.cmake:2` `add_compile_definitions(_NUMERIC_MODE=1)` | _NUMERIC_MODE와 _ONLY_RECT의 값은 구성별로 다르다. |
| LN1-104 | 사용하지 않는 make NETCDF 변수 | C 문서 누락 | `config/aws-gcc-nvidia-t4:2` `NETCDF := yes`·`config/aws-gcc-nvidia-t4:4` `-D_NETCDF=0`. | aws 구성의 코드 매크로 _NETCDF는 0이다. make 변수 NETCDF는 실제 기능 선택에 쓰이지 않는다. |
| LN1-105 | 변형 mk 파일의 연결 누락 | C 문서 누락 | `makefile:1,160` `-include $(CONFIG)`·`-include $(ALLDEPS)`·`make_block1bal1.mk:3`의 `$(MAINOBJS)`. | 동봉된 변형 mk 파일은 현재 루트 makefile에 연결되지 않는다. |
| LN1-106 | 별도 test/makefile의 외부 변수 | C 문서 누락 | `test/makefile:12–13`의 `$(LISFLOOD_OBJS)`·`$(EXE_DOUBLE_GCC)`·`$(LD_GCC)`. | test/makefile은 현재 루트 make와 다른 외부 변수 체계를 요구한다. |
| LN1-107 | 설정 파일 문법 차이 | C 문서 누락 | `config/local:1` `CXXFLAGS := -std=c++14 -Wall -O3 -fopenmp -static -D_NUMERIC_MODE=1 -D_NETCDF=1`·`config/bluepebble-intel:11` `set(_NETCDF 0)`. | config 디렉터리에서는 사용할 빌드 도구의 문법에 맞는 파일을 선택한다. |
| LN1-108 | 선택적 OpenMP 탐색 | E 코드 결함 후보(강함) | `CMakeLists.txt:199` `find_package(OpenMP)`·`lisflood2/sgm_fast.cpp:3521` `NUMERIC_TYPE * tmp_row = tmp_thread_data[omp_get_thread_num()];`·`배포 README:68` `OpenMP`. | OpenMP를 찾지 못한 구성에는 공통 소스의 OpenMP 참조를 대체하는 경로가 없다. |
| LN1-109 | SGM 블록 분기의 컴파일 결함 | E 코드 결함 후보(강함) | `lisflood2/lisflood_processing.cpp:1799` `FP_xwidth, Fp_ywidth,`·`lisflood2/sgm_fast.cpp:3663–3667`의 빠진 max_Froude 인수와 범위 밖 j. | _SGM_BY_BLOCKS=1 분기에는 같은 판의 행 경로와 모순되는 컴파일 결함 후보가 있다. |
| LN1-110 | VS Debug Win32 경로 표기 | C 문서 누락 | `lisflood.vcxproj:527`의 `netCDF4-64\include`·`lisflood.vcxproj:531`의 `netCDF4-32\lib`. | VS Debug Win32의 NetCDF 헤더 경로와 라이브러리 경로는 서로 다른 배포 디렉터리를 가리킨다. |
| LN1-111 | VS·Intel Debug OpenMP 설정 | C 문서 누락 | `lisflood.vcxproj:504` `<OpenMPSupport>false</OpenMPSupport>`·`lisflood_intel.vcxproj:218` `<OpenMPSupport>true</OpenMPSupport>`. | 두 Visual Studio project의 Debug OpenMP 설정은 다르다. |
| LN1-112 | CUDA 아키텍처 값 차이 | C 문서 누락 | `CMakeLists.txt:5`의 61·`config/aws-gcc-nvidia-t4:7`의 75·`config/bessemer-gcc-gpu:6`의 70·`config/sharc-gcc-gpu:5`의 37. `CMakeLists.txt:5` `set(CMAKE_CUDA_ARCHITECTURES 61)` | CUDA 아키텍처 값은 빌드 경로와 사용자 설정에 따라 다르다. |
| LN1-120 | 8.2 최대 수심 격자 메모리 | E 코드 결함 후보(강함; 8.2에서 발생, 8.3에서 수정) | `v8.2:cuda/cuda_max_field.cu:97` `maxH = GhostRaster::allocate_pinned_H(geometry);`·`cuda/fv1/cuda_fv1_simulate.cu:98–99`의 output_precision 인수·`패치:94–134`. | 8.3은 잘못 선택되던 작은 host 격자를 padded device 격자로 바꾸었다. |
| LN1-122 | 8.2 건조 NoData의 원자 덧셈 | E 코드 결함 후보(중간; 8.2에서 발생, 8.3에서 수정) | `v8.2:cuda/cuda_boundary.cu:92` `atomicAdd(&(mass_stats->out), -discharge);`·현재 `cuda/cuda_boundary.cu:289` `if (Hold == C(0.0)) continue; // dry: nothing to add to the mass balance`·`패치:79,87`. | 8.3은 drain_nodata 경로에서 건조 셀의 불필요한 0 원자 덧셈을 건너뛴다. |
| LN1-123 | 8.2 flux shared memory 동기화 | E 코드 결함 후보(강함; 8.2에서 발생, 8.3에서 수정) | `패치:153–154,173–174,196–197,216–217,239–240,259–260`의 reader 후 `__syncthreads();`. | 8.3은 FV1·FV2·DG2의 x·y flux pass 끝에 reader 동기화를 추가했다. |
| LN1-124 | 1920 셀·오류 코드·반복 실행 결과 | H 코드 대조 대상 아님 | `배포 README:32,34` `cudaErrorIllegalAddress`·`on grids wider or taller than 1920 cells repeated runs give different results`. | stride 식은 1920을 설명한다. 특정 격자의 오류와 반복 실행 결과는 실행 주장이다. |
| LN1-126 | 8.2 전역 sync 이름 충돌 | E 코드 결함 후보(중간; 8.2에서 발생, 8.3에서 수정) | `v8.2:cuda/adaptive/utilities/cuda_utils.cuh:10` `cudaError_t sync();`·`/usr/include/unistd.h:1005` `extern void sync (void) __THROW;`·`패치:51–71`. | 8.3은 전역 sync 선언과 정의를 sync_device로 바꾸었다. CUDA 12 환경의 실제 컴파일 실패는 이 보고서에서 재현하지 않았다. |
| LN1-127 | 8.2 format 파일의 헤더 이름 가림 | E 코드 결함 후보(중간; 8.2에서 발생, 8.3에서 수정) | `v8.2:format:1` `5`·`패치:264–268`의 삭제·`metal/CMakeLists.txt:26`의 `${CMAKE_SOURCE_DIR}` include 경로. | 8.3은 소스 루트가 include 경로일 때 헤더 이름을 가릴 수 있는 format 파일을 삭제했다. |
| LN1-128 | 8.2 generateDG2DEM NoData 기본값 | E 코드 결함 후보(강함; 8.2에서 발생, 8.3에서 수정) | `v8.2:preprocess/generateDG2DEM.cpp:43` `Pars pars;`·`input.cpp:1517` `DEM[i + j*Parptr->xsz] = Parptr->nodata_elevation;`·`패치:2985`. | 8.3은 generateDG2DEM이 설정을 읽기 전에 nodata_elevation 기본값을 넣는다. |
| LN1-129 | 8.2 generateDG2start NoData 기본값 | E 코드 결함 후보(강함; 8.2에서 발생, 8.3에서 수정) | `v8.2:preprocess/generateDG2start.cpp:43` `Pars pars;`·현재 `preprocess/generateDG2start.cpp:44` `pars.nodata_elevation = DEM_NO_DATA; // same default as lisflood.cpp`·`패치:2996`. | 8.3은 generateDG2start에도 같은 NoData 기본값을 넣는다. |
| LN1-130 | 8.2 시작 판 이름 | E 코드 결함 후보(강함; 8.2에서 발생, 8.3에서 수정) | `v8.2:lisflood.cpp:849`의 `LF_VersionMajor, LF_VersionMinor, LF_VersionInc` 출력·`패치:35` `+#define LF_Release "8.3"`·`패치:301`의 LF_Release 출력. | 8.3은 시작 판 이름을 8.3으로 표시한다. 내부 checkpoint 숫자는 8.1.0으로 유지한다. |
| LN1-132 | GPU 정밀도 일반화 | B 문서 오기 | `배포 README:14` `single precision, as the GPU solvers use`·`lisflood.h:75–97`·`cuda/adaptive/types/real.h:3–15`. | CUDA 구현의 자료형 선택 가능성과 이 배포본이 제시한 float 빌드를 구분한다. |
| LN1-134 | 수정 뒤 남은 max precision 인수 | E 코드 결함 후보(강함) | `cuda/cuda_max_field.cuh:20–21`의 acceleration·precision 순서·`cuda/fv1/cuda_fv1_simulate.cu:98–99`의 output_precision 전달·`cuda/fv1/cuda_fv1_simulate.cu:119–121`의 정상 Snapshot 전달. `cuda/fv1/cuda_fv1_simulate.cu:99` `grid_size, pars.output_precision);` | 8.3에도 MaxField 호출의 출력 정밀도 인수 연결 결함이 남는다. |
| LN1-135 | 선택적 tracer의 옛 sync 호출 | E 코드 결함 후보(중간) | `cuda/adaptive/classes/Tracer.h:5,19` `#if _USE_TRACER == 1`·`CHECK_CUDA_ERROR( sync() );`·`cuda/adaptive/utilities/cuda_utils.cuh:10` `cudaError_t sync_device();`. | _USE_TRACER=1에서는 이름을 바꾸지 않은 호출이 남는다. 기본 빌드는 이 경로를 컴파일하지 않는다. |
| LN1-136 | Mac의 모든 다른 해법 CPU 실행 설명 | B 문서 오기 | `배포 README:137` `the other solvers on the CPU`·`lisflood.cpp:773–805`의 SGC·FV1·DG2·IterateQ 분기. | Mac에서 CUDA 전용 해법까지 같은 해법의 CPU 구현으로 실행된다고 쓰면 안 된다. |
| LN1-137 | Metal adaptoff 처리 | E 코드 결함 후보(강함) | `metal/fv1/metal_fv1_simulate.mm:1024,1027`의 computeTimestep과 첫 단계 조건·`swe/fv1.cpp:61–64`의 adaptive_ts 조건. `metal/fv1/metal_fv1_simulate.mm:1024` `NUMERIC_TYPE adaptive_dt = computeTimestep();` | Metal은 첫 단계 이후 adaptoff에서도 CFL 시간간격을 사용한다. |
| LN1-138 | Metal CFL의 고정 DepthThresh | E 코드 결함 후보(강함) | `metal/fv1/metal_fv1_kernels.metal:11,648` `#define DEPTH_THRESH 1e-3f`·`if (h > DEPTH_THRESH) {`·`swe/fv1.cpp:599` `if (H > Solverptr->DepthThresh)`. | Metal CFL은 사용자 depththresh 대신 고정 1e-3 임계값을 사용한다. |
| LN1-139 | Metal shader fallback의 산술 옵션 | C 문서 누락 | `metal/CMakeLists.txt:13` `-fno-fast-math`·`metal/fv1/metal_fv1_simulate.mm:255` `options.fastMathEnabled = YES;`. | Metal의 사전 컴파일 경로와 소스 fallback 경로는 fast math 설정이 다르다. |
| LN1-151 | CMake가 Windows 묶음을 사용하지 않는다는 설명 | B 문서 오기 | `배포 README:21–23`·`CMakeLists.txt:212–216`의 `windep/netCDF4-64`·`DLL's/*.dll`. `CMakeLists.txt:212` `target_include_directories(lisflood-base INTERFACE windep/netCDF4-64/include) # TODO: x64 only` | Windows 묶음을 사용하지 않는다는 설명은 Linux·Mac 빌드 조건으로 한정해야 한다. |
| LN1-152 | 배포 폴더의 두 commit git 설명 | B 문서 오기 | `배포 README:25–26` `whose two commits are the 8.2 source and the 8.3 changes`·배포 루트와 source의 `.git` 부재. | 제공된 배포 압축 해제본에는 설명한 자체 git 저장소가 없다. |
| LN1-154 | CUDA 최소 판·module·빌드 환경 | H 코드 대조 대상 아님 | `배포 README:67–83` `CUDA 11.4 or later (tested with 12.6)`·module load·cmake build 명령. | 특정 CUDA·컴파일러·module 환경의 빌드 성공은 실행 환경 주장으로 남긴다. |
| LN1-156 | 클러스터 GPU 운영 | H 코드 대조 대상 아님 | `배포 README:91–99`의 srun·nvidia-smi·LD_LIBRARY_PATH 설명. `배포 README:94` `nvidia-smi` | 클러스터 운영 명령과 환경 조정은 외부 도구 사용법이다. |
| LN1-157 | Mac 도구 설치 | H 코드 대조 대상 아님 | `배포 README:103–104` `brew install cmake libomp netcdf`. | Xcode·Homebrew 준비는 모델 코드의 정적 대조 대상이 아니다. |
| LN1-160 | 8.2와 8.3 출력 byte 일치 | H 코드 대조 대상 아님 | `배포 README:43–45` `byte for byte`·`except the last digit of the mass-balance log`. | 출력 byte 일치는 질량 로그의 예외를 포함한 저자 실행 주장이다. |
| LN1-161 | 사례별 오류·완주·최대 격자 | H 코드 대조 대상 아님 | `배포 README:46–49`의 0.58·1.7·5.2·10.6 million cells. `배포 README:48` `Largest grids tested: 5.2 million cells` | 사례별 오류·완주·최대 시험 격자 수는 실행 결과다. |
| LN1-162 | Sanitizer 결과 | H 코드 대조 대상 아님 | `배포 README:50–51` `and none in 8.3`. | Sanitizer 무오류 주장은 이 정적 대조의 확인 결과가 아니다. |
| LN1-163 | 속도·재현성 수치 | H 코드 대조 대상 아님 | `배포 README:52–58`의 24 h·10.6 million·9.4 min·105 min·72 %·85-89 %·세 Metal 사례. `배포 README:53` `9.4 min where 8.2` | 성능과 수치 재현성 수치는 실행 주장으로 기록한다. |
| LN1-165 | 시험·미시험 이력 | H 코드 대조 대상 아님 | `배포 README:60,62–63` `were not tested`와 시험 플랫폼 목록. | 배포 저자의 시험 이력과 이 보고서의 코드 확인 범위를 구분한다. |
| LN1-167 | quick test 통과 | H 코드 대조 대상 아님 | `배포 README:126–131`의 명령과 `QUICK TEST PASSED`. | quick test 통과는 모델 실행 없이 확인한 사실로 옮기지 않는다. |
| LN1-169 | 라이선스 합의·논문 인용 | H 코드 대조 대상 아님 | `배포 README:141–142` `agreed with the LISFLOOD-FP developers`·`배포 LICENSE:2` `Version 3, 29 June 2007`. | 동봉 라이선스 본문과 개발자 합의·논문 주장의 확인 수준을 나눈다. |
| LN1-180 | 추가 CUDA 해법 | C 문서 누락 | `CMakeLists.txt:102–178`의 FV2·ACC·acc_nugrid·adaptive source 목록. `CMakeLists.txt:178` `add_subdirectory(cuda/adaptive)` | 기본 CMake의 CUDA 대상은 README의 FV1·DG2 목록보다 넓다. |
| LN1-181 | 보조 CMake 대상 | C 문서 누락 | `CMakeLists.txt:190,193,196`의 generateDG2DEM·generateDG2start·DG2downscale. `CMakeLists.txt:196` `add_executable(DG2downscale postprocess/DG2downscale.cpp)` | 기본 CMake는 주 실행 파일 외에 세 보조 실행 파일도 만든다. |
| LN1-182 | NetCDF 비활성 출력·강우 처리 차이 | C 문서 누락 | `lisflood2/file_tool.cpp:431,787–788`의 경고·ASCII 조건·`pars.cpp:999–1002`의 동적 강우 종료. `lisflood2/file_tool.cpp:431` `printf("WARNING: NetCDF selected but not enabled in this build\n");` | NetCDF 출력의 ASCII fallback과 동적 강우의 종료 조건을 구분한다. |
| LN1-183 | GPU 미지원 빌드 검사 | C 문서 누락 | `pars.cpp:1080` `#if !defined(CUDA) && !defined(METAL_ENABLED)`. | GPU 요청은 CUDA와 Metal이 모두 없는 빌드에서 거부된다. |
| LN1-184 | max_Froude 컴파일 조건 | C 문서 누락 | `pars.cpp:926–929` `#if _CALCULATE_Q_MODE != 1`과 `exit(EXIT_FAILURE);`. | max_Froude 키워드는 _CALCULATE_Q_MODE=1을 요구한다. |
| LN1-185 | 컴파일 모드의 동작 범위 | C 문서 누락 | `config.default.cmake:3–8`·`lisflood2/sgm_fast.cpp:4837–4839`의 profile 강제 종료. `lisflood2/sgm_fast.cpp:4837–4839` `#if _PROFILE_MODE > 1`·`exit(0);` | 단면·Froude 제한·블록·진단 모드의 조건을 빌드 설명에 추가한다. |
| LN1-186 | Metal 가용성 조건 | C 문서 누락 | `metal/CMakeLists.txt:6` `if(METAL_FRAMEWORK AND FOUNDATION_FRAMEWORK)`·`metal/fv1/metal_fv1_simulate.mm:1328` `return device != nil;`. | Metal은 빌드 시 framework와 실행 시 장치 가용성을 따로 검사한다. |
| LN1-187 | Metal shader 탐색·초기화 실패 | C 문서 누락 | `metal/fv1/metal_fv1_simulate.mm:209–258`의 탐색 순서·`metal/fv1/metal_fv1_simulate.mm:1359–1365`의 실패 후 반환. `metal/fv1/metal_fv1_simulate.mm:1359` `if (!sim.is_valid()) {`·`metal/fv1/metal_fv1_simulate.mm:1364` `return;` | Metal shader 초기화 실패 뒤 CPU FV1으로 자동 전환한다고 쓰지 않는다. |
| LN1-188 | Metal의 강우 옵션 거부 | C 문서 누락 | `metal/fv1/metal_fv1_simulate.mm:1347–1355`의 rainfallmask·routing·누락 rainfall 시계열 검사. `metal/fv1/metal_fv1_simulate.mm:1347` `if (states.rainfallmask == ON \|\| states.routing == ON) {` | Metal FV1의 rainfallmask·routing 거부 조건을 사용 설명에 추가한다. |
| LN1-189 | Metal DEM 기준면·NoData 변환 | C 문서 누락 | `metal/fv1/metal_fv1_simulate.mm:531,533–541`의 dem_offset·kMargin·gpu_nodata. `metal/fv1/metal_fv1_simulate.mm:533` `const float kMargin = 1000.0f; // far beyond any credible water depth` | Metal은 GPU DEM 기준면과 NoData 표고를 변환한다. |
| LN1-190 | Metal 자료형·HV 부호 변환 | C 문서 누락 | `metal/fv1/metal_fv1_simulate.mm:579` `d_HV[gpu_idx] = -(float)h_HV[cpu_idx];`·`metal/fv1/metal_fv1_simulate.mm:725` `h_HV[cpu_idx] = -(NUMERIC_TYPE)d_HV[gpu_idx];`. | Metal의 float 자료형과 HV 부호 변환을 CPU 경로와 구분한다. |
| LN1-191 | Metal point source·강우·max 처리 | C 문서 누락 | `metal/fv1/metal_fv1_simulate.mm:891–958,1075,1263–1278,1476–1477`. `metal/fv1/metal_fv1_simulate.mm:1075` `if (time >= last_rain_time + 1.0 \|\| last_rain_time < 0) {` | Metal의 point source·강우 업로드·최대 수심 처리 경로를 별도로 기록한다. |
| LN1-192 | GPU 요청과 해법 선택의 구별 | C 문서 누락 | `pars.cpp:965–968` `Statesptr->cuda = ON;`·`pars.cpp:582–589`의 별도 fv1 상태 설정. | cuda·metal 키워드는 GPU 요청을 켠다. 해법은 별도 키워드로 선택한다. |
| LN1-193 | 일반 실행의 parfile 인수 | C 문서 누락 | `pars.cpp:39` `if (argc == 1 \|\| argv[argc - 1][0] == '-')`·`pars.cpp:45`의 마지막 인수 ReadParamFile. | 일반 실행은 마지막 인수에 parfile을 요구한다. -version은 그 전에 반환한다. |
| LN1-230 | 현재 원자료의 판 표시 | A 판 차이 | `노트 README.md:11`의 v8.2·2024-07-29·`v8.2:VersionHistory.h:16–18`·현재 `VersionHistory.h:23,31`의 LF_Release 8.3·2026년 연혁. `VersionHistory.h:23` `#define LF_Release "8.3"` | 현재 원자료는 8.2에 8.3 패치를 적용한 판으로 설명한다. |
| LN1-231 | Metal과 Apple 빌드의 노트 누락 | A 판 차이 | `노트 README.md:13`의 C++·CUDA·Windows·Linux 설명·`패치:13–25,305–343`의 Apple 분기와 Metal 추가. `CMakeLists.txt:232` `if (APPLE)` | 현재 빌드 설명에 Apple Metal FV1과 조건부 NUMA 의존성을 추가한다. |
| LN1-232 | 8.2 메타와 8.3 동봉 라이선스 | A 판 차이 | `노트 README.md:12`·`노트 web-refs/lisflood-fp-official-resources.md:31`의 8.2 GPL-2.0 기록·`배포 LICENSE:2`의 v3 본문. | 8.2 메타데이터와 8.3 동봉 파일의 판 귀속을 나누어 적는다. |
| LN1-233 | 노트의 NUMA 변수 오기 | B 문서 오기 | `노트 manual-notes/lisflood-fp-user-manual.md:363`의 NUMA_ROOT·`cmake/Modules/FindNUMA.cmake:10,14`의 NUMA_ROOT_DIR. `cmake/Modules/FindNUMA.cmake:10` `HINTS ${NUMA_ROOT_DIR}/include)` | 노트의 NUMA 경로 변수 이름을 NUMA_ROOT_DIR로 고친다. |
| LN1-234 | 노트의 CUDA 아키텍처 위치 오기 | B 문서 오기 | `노트 manual-notes/lisflood-fp-user-manual.md:367`의 config.default.cmake 안내·`CMakeLists.txt:4–6`. `CMakeLists.txt:5` `set(CMAKE_CUDA_ARCHITECTURES 61)` | 노트는 CMAKE_CUDA_ARCHITECTURES의 명령행 설정을 안내해야 한다. |
| LN1-235 | 노트에 옮겨진 Makefile.new | B 문서 오기 | `노트 manual-notes/lisflood-fp-user-manual.md:368`·`v8.0:INSTALL.md:3`·`v8.1:INSTALL.md:3`·현재 makefile. `v8.0:INSTALL.md:3` `CONFIG=config/<file> make -f Makefile.new <target>` | Makefile.new 이름은 과거 배포본에서도 설명되지 않는 오기다. |
| LN1-237 | dg2new의 적응 해법 오인 | B 문서 오기 | `노트 source-analysis/lisflood-fp-architecture-source-map.md:61,83`·`lisflood.cpp:794–796`의 주석·`CMakeLists.txt:178`의 adaptive. `CMakeLists.txt:178` `add_subdirectory(cuda/adaptive)` | dg2new를 MWDG2 구현이라고 쓰지 않는다. |
| LN1-238 | dg2new의 빌드·실행 혼동 | B 문서 오기 | `노트 source-analysis/lisflood-fp-swe-fv1-dg2.md:291`·`v8.2:makefile:31` `swe/dg2new.cpp \`. | dg2new는 CMake 기본 목록에서 제외되지만 옛 make 목록에는 포함된다. 런타임 호출은 주석이다. |
| LN1-239 | FV1 분기의 판 차이 | A 판 차이 | `노트 source-analysis/lisflood-fp-swe-fv1-dg2.md:26–27`의 옛 CPU 분기·`v8.2:lisflood.cpp:775–782`·`패치:282–295`. `lisflood.cpp:782` `if (Statesptr->cuda == ON && metal_is_available())` | 8.3 FV1 분기에는 Metal 조건부 호출을 함께 적는다. |
| LN1-240 | classic 노트의 CPU 경로 표 | A 판 차이 | `노트 source-analysis/lisflood-fp-classic-acc-flow.md:9,46`의 2026-06-18 판독·CPU FV1 설명·`패치:282–295`. `lisflood.cpp:782` `if (Statesptr->cuda == ON && metal_is_available())` | CUDA 분기를 지나지 않은 현재 FV1 실행도 Metal을 선택할 수 있다. |
| LN1-241 | GPU 미지원 검사 판 차이 | A 판 차이 | `v8.2:pars.cpp:1079` `#ifndef CUDA`·`패치:2974` `+#if !defined(CUDA) && !defined(METAL_ENABLED)`. | 현재 GPU 미지원 검사는 CUDA와 Metal의 동시 부재를 검사한다. |
| LN1-242 | CUDA 패밀리 수의 기존 누락 | B 문서 오기 | `노트 source-analysis/lisflood-fp-cuda-gpu.md:17,229`의 4종 설명·`v8.2:CMakeLists.txt:102–107,178`의 FV2·adaptive. `v8.2:CMakeLists.txt:104` `cuda/fv2/cuda_fv2_simulate.cu` | FV2와 adaptive의 누락은 8.3에서 생긴 판 차이가 아니다. |
| LN1-243 | flux pass 끝 동기화의 판 차이 | A 판 차이 | `노트 source-analysis/lisflood-fp-cuda-gpu.md:109`·`v8.2:cuda/fv1/cuda_fv1_solver.cu:379–384`·`패치:196–197,216–217`. `cuda/fv1/cuda_fv1_solver.cu:381` `__syncthreads();` | 현재 flux 설명에는 pass 끝의 reader 동기화를 추가한다. |
| LN1-244 | 최대 수심 객체의 현재 메모리 설명 | C 문서 누락 | `노트 source-analysis/lisflood-fp-cuda-gpu.md:195`·`cuda/cuda_max_field.cu:97–98,124–135`. `cuda/cuda_max_field.cu:97` `maxH = GhostRaster::allocate_device(geometry);` | MaxField의 device 상주와 출력 시 host 복사를 노트에 추가한다. |
| LN1-247 | adaptive utility·진입 줄의 판 차이 | A 판 차이 | `노트 source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:7,20`의 v8.2 판독·`패치:51–71`·현재 `lisflood.cpp:447–450`. `cuda/adaptive/utilities/cuda_utils.cuh:10` `cudaError_t sync_device();` | adaptive 본체의 유지와 8.3 utility 이름 수정을 구분해 기록한다. |
| LN1-248 | 공식 자료 노트의 판 연결 | A 판 차이 | `노트 web-refs/lisflood-fp-official-resources.md:25,29–30`의 v8.2 서지·`배포 README:19–24`의 8.3 패치 설명. `VersionHistory.h:23` `#define LF_Release "8.3"` | 8.2 서지를 보존하고 현재 적용한 8.3 패키지를 별도로 연결한다. |

확인 범위는 문서·빌드 선언·전처리 조건·8.2와 8.3의 정적 판 차이다.
이 보고서는 모델 실행·컴파일·성능 측정·수치 재현성 시험을 수행하지 않았다.
현재 노트와 원자료는 수정하지 않았다.

분류별 개수(이 절의 고유 행 ID 기준): A 9개·B 13개·C 38개·D 0개·E 15개·F 0개·H 13개·X 0개. 열지 못한 대상 파일: 없음.

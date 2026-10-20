---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/README.md
lines: 65
sha256: c611c5c164a806591a0424f16e992407b504ca7a29291eb35aab3dac2c957a72
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# README.md — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–15 | 제목 `# Compilation` (1) 아래 Windows 또는 Linux에서 `CMake`의 `3.13` 이상을 사용한다고 적는다(2). `## Compiling on Windows with the MSVC compiler` (4)는 `Visual Studio 2019`에서 `lisflood-fp` 폴더를 열고(5), `msvc-x64-Debug` 또는 `msvc-x64-Release` 및 `Rebuild All`을 선택하도록 안내한다(6). `## Compiling on Windows with the Intel compiler` (8)는 `launch_vs2019_intel64.bat`와 `Visual Studio 2019 Community Edition`을 명시한다(9). `intel-x64-Debug` 또는 `intel-x64-Release` 및 `Rebuild All`을 선택한다(10). 배치 파일로 시작한 뒤 MSVC 또는 Intel 구성을 고를 수 있다고 적는다(11). `## Running or debugging on Windows` (13)는 `lisflood.exe`, `Solution Explorer`, `CMake Targets View`, `Add Debug Configuration`, `lisflood (executable)`을 안내한다(14). 빈 줄도 포함한다. |
| 16–40 | `## Compiling on Linux` (16)는 최근 CMake와 `libnuma-dev`를 요구한다고 적는다(18–19). NetCDF 출력과 동적 강우(dynamic rainfall) 지원에는 `libnetcdf-dev`를 적는다(19). Ubuntu 예시 명령은 `sudo snap install cmake --classic` (22), `sudo apt install libnuma-dev libnetcdf-dev` (23)이다. 저장소 루트에서 실행하는 빌드 명령은 `cmake -S . -B build` (29), `cmake --build build` (30)이다. 결과 `lisflood` 실행 파일을 `build`에 쓴다고 적는다(33). 비표준 NUMA 경로용 명령은 `cmake -S . -B build -DNUMA_ROOT=<path>` (37), `cmake --build build` (38)이다. 코드 울타리·빈 줄·설명도 포함한다. 명령은 문서 원문 인용이며 이 판독에서 실행하지 않았다. |
| 41–62 | `## Customising the build` (41)는 `config.default.cmake`를 복사·수정하도록 안내한다(42). Windows에서는 `CMakeSettings.json` (43)의 `"configurations": [` (45), `"name": "msvc-x64-Debug"` (47), `"cmakeCommandArgs": "-D_CONFIG=<filename>"` (49)를 예시로 든다. 48·50·52행의 비ASCII 원문 바이트는 각각 `0x85`이며 판독 출력에서는 `�`로 표시된다. Linux 예시 명령은 `cmake -S . -B build -D_CONFIG=<filename>` (59), `cmake --build build` (60)이다. 예시의 구분자·코드 울타리·빈 줄도 포함한다. |
| 63–65 | `## NVIDIA CUDA support` (63) 아래 `NVIDIA CUDA Toolkit`이 설치되면 CMake가 `LISFLOOD-FP FV1 and DG2 CUDA solvers`를 자동 컴파일한다고 적는다(64). CUDA 계산 능력(compute capabilities) 조정은 `config.default.cmake`를 보도록 안내한다(65). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48·50·52: 각 예시 줄에는 단일 비ASCII 바이트 `0x85`가 들어 있다. UTF-8로 표시한 판독 출력은 이 바이트를 `�`로 표시했다. 원문 바이트와 표시 문자를 구분한다.

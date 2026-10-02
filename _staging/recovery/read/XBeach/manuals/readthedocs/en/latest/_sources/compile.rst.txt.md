---
file: models/XBeach/raw/manuals/readthedocs/en/latest/_sources/compile.rst.txt
lines: 51
sha256: b3a6f98ee21f086eedf4e046967dce50b7cc62baf078ab19ff59721fdd04038e
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# compile.rst.txt — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | How to compile — 실행파일 다운로드와 직접 Windows/Linux 컴파일 선택, SVN trunk 소스 주소를 제시한다(4–10). 원문: `However it is also possible to compile XBeach yourself. Both a windows and a Linux version can be compiled. The source code is available at:` (8); `https://svn.oss.deltares.nl/repos/xbeach/trunk/` (10). |
| 12–15 | Compile on Windows — Fortran compiler·Visual Studio 및 소스 저장소 Solution 파일 요구사항(14). 원문: `To compile on Windows a Fortran compiler and visual Studio is required. To compile on Windows a Fortran compiler and visual Studio is required. The Solution file for Visual studio is present at the repository with the source code.` (14). |
| 16–40 | Compile on Linux / 준비 — gcc·hdf5·netcdf·openmpi·anaconda3 목록(19–29), 버전이 적힌 module load 예제(31–39). 원문: `Before XBeach can be compiled several libraries are requried. XBeach requires:` (19); `#. gcc` (21); `#. hdf5` (23); `#. netcdf` (25); `#. openmpi` (27); `#. anaconda3` (29); `To load the libraries the following code can be used:` (31); `.. code-block:: text` (33); `   module load anaconda3/py39_23.1.0-1` (35); `   module load gcc/12.2.0_gcc12.2.0` (36); `   module load hdf5/1.14.0_gcc12.2.0` (37); `   module load netcdf/4.9.2_4.6.1_gcc12.2.0` (38); `   module load openmpi/4.1.5_gcc12.2.0` (39). |
| 41–51 | Compile on Linux / 빌드 — Python과 mako 설치 안내(41), distclean→autogen→FCFLAGS/configure→make→install 명령(43–51). 빌드 옵션은 원문대로 기록하며 실제 설치/컴파일은 하지 않았다. 원문: `Next to Python, the mako package is required. To install mako run pip install mako in a Python terminal.` (41); `To compile XBeach the following commands can be run:` (43); `.. code-block:: text` (45); `   make distclean` (47); `   ./autogen.sh` (48); `   FCFLAGS="-mtune=corei7-avx -funroll-loops --param max-unroll-times=4 -ffree-line-length-none -O3 -ffast-math" ./configure  --with-netcdf --with-mpi` (49); `   make` (50); `   make install` (51). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14: Windows에 Fortran compiler와 Visual Studio가 필요하다는 동일 문장이 같은 행에서 두 번 반복된다.
- 10: 소스 저장소 주소는 `https://svn.oss.deltares.nl/repos/xbeach/trunk/`이며 특정 release 또는 revision을 지정하지 않는다.

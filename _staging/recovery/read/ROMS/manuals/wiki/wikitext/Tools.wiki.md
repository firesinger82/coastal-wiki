---
file: models/ROMS/raw/manuals/wiki/wikitext/Tools.wiki
lines: 42
sha256: 5e2930d3b66a07f7c564d05ad1e07758f900608a3be1b537683da1ec148f4330
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Tools.wiki — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Tools / NetCDF Format — 입출력은 자기 기술적(self-describing)·기계 독립(machine independent) NetCDF 파일이며 history·averages가 CF 1.0 격자 자료 규약을 100% 따른다고 문서가 적는다(1–5). 여러 접근 도구를 소개한다(5). 원문: `ROMS input and output files are self-describing, machine independent [http://www.unidata.ucar.edu/software/netcdf/ NetCDF] files.   The history and averages files are 100% compliant with the [http://cf-pcmdi.llnl.gov/ CF 1.0 Metadata Standard] for gridded data. These files can be accessed with a [http://www.unidata.ucar.edu/software/netcdf/software.html wide variety of software tools].  But some of our favorite tools are mentioned below.` (5). |
| 7–29 | Python — 과학 스크립트(scientific scripting), NetCDF와 C·Fortran 래퍼(wrapper) 사용을 소개한다(7–9). ROMS 출력 처리에 필요한 numpy·matplotlib/basemap·python-netcdf4를 제시하며 설치 지침 준수를 강조한다(11–15). ROMS 스크립트 저장소와 checkout·디렉터리 이동·빌드·설치 명령 예제를 인용한다(18–28). 원문: `* numpy:  http://numpy.scipy.org (basic numeric array mathematics)` (13); `* matplotlib:  http://matplotlib.sourceforge.net (and the basemap toolkit for geospatial plotting)` (14); `* python-netcdf4:  http://code.google.com/p/netcdf4-python/ (follow the install directions *exactly)` (15); `$ svn co http://pong.tamu.edu/svn/python/trunk/ python-roms` (20); `$ cd python-roms/roms` (24); `$ python setup.py build` (26); `$ sudo python setup.py install` (28). |
| 30–38 | MATLAB — MEXNC의 기계 의존 접근, 읽기 전용의 SNCTOOLS Java 방식, 더 이상 적극 개발하지 않는 NetCDF Toolbox를 소개한다(30–34). RSLICE의 임의 단면·유속·로컬/원격 접근, MEXNC가 필요한 ROMS_TOOLS, NetCDF-Java CF API 예제를 적는다(35–37). 원문: `* [http://mexcdf.sourceforge.net/ MEXNC, SNCTOOLS, and the NetCDF Toolbox]: ` (31); `** MEXNC: For maximum flexibility accessing NetCDF files with Matlab, you need to install the machine-dependent MEXNC for your system.  ` (32); `** SNCTOOLS: If you just want to access NetCDF files with Matlab (not write them), you can use use the SNCTOOLS, which have a mode that uses machine-independent Java instead of the machine-dependent MEXNC.` (33); `** NetCDF Toolbox: An overloaded "language" for dealing with NetCDF files, developed by Chuck Denham.  Not under active development.` (34); `* [http://marine.rutgers.edu/~jevans/rslice/rslice/doc/html/ch01.html RSLICE]: A GUI specifically for ROMS files.  Arbitrary vertical and horizontal slices, velocity overlays, and more. Accesses local NetCDF (or remote OpenDAP) files, and since it depends on SNCTOOLS, can work via Java without MEXNC.  ` (35); `* [http://www.brest.ird.fr/Roms_tools/ ROMS_TOOLS]: GUI and tools specifically for ROMS  files.  An integral part of the ROMS-AGRIF system.  Requires MEXNC.` (36); `* A [http://stellwagen.er.usgs.gov/rps/share/java_isosurface_demo2.m Example Isosurface Script] that demonstrates using the NetCDF-Java CF API.` (37). |
| 39–42 | Other Tools — 빠른 조회·애니메이션용 NcVIEW는 좌표 인덱스 공간에서만 그린다고 적는다(39–41). IDV는 CF NetCDF를 포함한 여러 형식에 대응하는 Java GUI이며 Unidata 개발을 설명한다(42). 원문: `* [http://meteora.ucsd.edu/~pierce/ncview_home_page.html NcVIEW]: A general non-ROMS specific NetCDF viewer, good for quick exploration and animation.  Plots in coordinate index space only, however.` (41); `* [http://www.unidata.ucar.edu/software/idv/ Integrated Data Viewer (IDV)]: A GUI for visualizing a variety of file formats, including CF-Compliant NetCDF.  A 100% Java application that uses the NetCDF-Java library.  Under active development by Unidata.` (42). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

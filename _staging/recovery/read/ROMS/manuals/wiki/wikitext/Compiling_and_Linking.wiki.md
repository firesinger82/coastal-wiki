---
file: models/ROMS/raw/manuals/wiki/wikitext/Compiling_and_Linking.wiki
lines: 29
sha256: 278f9db666ae3f05b8c5c535489bbfb47205ae60bb230b57baf2ebe1128c557c
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Compiling_and_Linking.wiki — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | Compiling and Linking — 제목, 임시 목차 앞 주석과 목차 지시문이다(1–3). |
| 4–14 | GNU make — make/gmake 버전 조회·3.81 출력 예시와 최소 3.80 요구 문구를 원문 그대로 옮긴다(6–13). 원문: ` To compile ROMS, first check to make sure that you have '''GNU make''' on your system. Typing "'''make -v'''" or "'''gmake -v'''" should bring up a message such as: ` (6); ` :GNU Make 3.81 ` (7); ` :Copyright (C) 2006  Free Software Foundation, Inc. ` (8); ` :This is free software; see the source for copying conditions. ` (9); ` :There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A ` (10); ` :PARTICULAR PURPOSE. ` (11); ` You want to have at least version 3.80, and 3.81 behaves better on some systems. If you don't have a fairly modern [http://www.gnu.org/software/make/ GNU make], it is freely available and quite portable. ` (13). |
| 15–20 | NetCDF — F90 인터페이스(interface) 설치 요구, 컴파일러별 make include 파일과 Linux-pgi.mk의 기본 디렉터리 설정, F77·F90 모두 설치 권고이다(17–19). 원문: ` You will also need to have the [http://www.unidata.ucar.edu/software/netcdf/ Netcdf] library, F90 interface, installed on your system. Tell ROMS how to find it according to the directions in [[makefile]]. Notice that there are several machine-dependent make include files in the '''Compilers''' sub-directory. For example, the locations of the NetCDF include and library directories are specified in file '''Linux-pgi.mk''' as: ` (17); ` <div class="box"><span class="red">NETCDF_INCDIR ?= </span>/opt/pgisoft/netcdf/include<br /><span class="red">NETCDF_LIBDIR ?=</span> /opt/pgisoft/netcdf/lib</div> ` (18); ` We recommend you to install both the Fortran F77 and F90 interfaces of the NetCDF library. ` (19). |
| 21–24 | User Changes — makefile의 사용자 스위치(user-defined switches) 설명 링크이다(23). |
| 25–29 | Compiling — cppdefs.h·Functionals·makefile 선택을 확인하고 make 또는 build Script를 실행하라는 안내와 make/gmake 설명 링크이다(27–29). 원문: ` Check over your [[cppdefs.h]] and [[Functionals]] one last time, check your choices as listed in [[makefile]], then launch '''make''' or the [[build Script]]. ` (27). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

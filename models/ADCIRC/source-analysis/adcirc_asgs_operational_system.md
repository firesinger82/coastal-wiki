---
title: "ADCIRC ASGS 운영 시스템 — 실시간 폭풍해일 예보 자동화 구조 (S-tier 요약)"
model: ADCIRC
component: ASGS (ADCIRC Surge Guidance System) — orchestration + Fortran/Perl 유틸리티
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "소스 직접 read: asgs/DESIGN-DESCRIPTION, asgs/README.md, asgs/asgs_main.sh, asgs/generateDynamicInput.sh, asgs/tides/tide_fac.f, asgs/doc/util/aswip.1.txt, asgs/output/FigureGen/FigureGen.F90, asgs/output/part_track_post.sh, asgs/get_atcf.pl·storm_track_gen.pl·control_file_gen.pl·get_nam.pl. 디렉토리는 ls/find로 카탈로그."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ADCIRC/README.md
---

# ADCIRC ASGS 운영 시스템 — 실시간 폭풍해일 예보 자동화 구조 (S-tier 요약)

> 요약 (경로: `models/ADCIRC/raw/source_code/asgs/`). ASGS(ADCIRC Surge Guidance System)는 ADCIRC를 실시간 폭풍해일 의사결정 지원을 위해 자동 구동하는 **운영 오케스트레이션 시스템**이며 ADCIRC 자체 코드가 아니다. 트리당 4,610 파일 (Fortran 102 + Perl/bash 324 글루)에 달하는 **S-tier 규모로 전수 전사 불가** — 본 노트는 디렉토리 구조 · 핵심 Fortran 유틸리티(`tide_fac`·`aswip`·`FigureGen`) · 입출력 전처리 카탈로그 · orchestration 골격(존재만 언급) 수준의 요약이다.
>
> ⚠ **S-tier 요약 노트**: 개별 Perl orchestration(`asgs_main.sh` 160 KB, `control_file_gen.pl` 65 KB, `storm_track_gen.pl` 46 KB 등)의 라인별 분석은 범위 밖. 대표 file:line만 인용한다.

## 1. ASGS 정체 — ADCIRC 코드가 아닌 운영 래퍼

ASGS는 "real time decision support를 위한 coastal ocean modelling 자동화 소프트웨어 인프라"이며, pre/post-processing용 standalone CLI 도구 모음을 제공한다 (`README.md:1-3`). 대화형 운영 셸 `asgsh`를 포함해 다중 ADCIRC 설치 관리·예보 운영을 담당한다 (`README.md:5-7`). 업스트림은 StormSurgeLive/asgs (`README.md:9`).

### 아키텍처 철학 (`DESIGN-DESCRIPTION`)

| 언어 | 역할 | 근거 |
|---|---|---|
| Bash | 워크플로 자동화의 1차 도구 (ubiquity·환경변수 관리·프로세스 관리) | `DESIGN-DESCRIPTION:34-46` |
| Perl | Bash 범위 넘는 복잡 데이터 처리 (CLI 플래그·STDIN 파이프) | `DESIGN-DESCRIPTION:48-67` |
| Fortran | ADCIRC/SWAN 출력 후처리 수치 유틸 — **historical reason, 신규는 deprecated** (신규는 C/C++) | `DESIGN-DESCRIPTION:78-82` |
| Python | ASGS 내부에서 제거 — operator 자체 환경 사용 | `DESIGN-DESCRIPTION:72-76` |

ASGS는 호스트 시스템 Perl이 아니라 **자체 Perl 환경을 빌드**하고 CPAN 모듈을 자체 설치하여 플랫폼 간 일관성을 보장한다 (`DESIGN-DESCRIPTION:62-67`). netCDF/HDF5 등 컴파일 라이브러리도 자체 빌드 (`DESIGN-DESCRIPTION:89-97`). 컴파일러는 GCC(gfortran)·Intel 두 스위트만 정식 지원 (`DESIGN-DESCRIPTION:130-132`).

## 2. 최상위 디렉토리 구조

`asgs/` 루트 (`ls -la` 카탈로그):

| 경로 | 책임 |
|---|---|
| `asgs_main.sh` (160 KB) | 메인 드라이버 — config.sh 처리 후 advisory cycle마다 1회 실행되는 루프 (`asgs_main.sh:4-7`) |
| `tides/` | 조석 nodal factor·equilibrium argument·경계조건 추출 Fortran |
| `util/` | 입력 전처리(`util/input`)·출력 후처리(`util/output`)·관리·메쉬 도구 |
| `input/` | advisory 다운로드·모니터, 메쉬·측정·노달속성, NAM 보간(`awip_lambert_interp.F`) |
| `output/` | 후처리 — FigureGen·PartTrack·TRACKING_FILES·netCDF 변환·KMZ/GIS·CERA 알림 |
| `config/`, `platforms/`, `cloud/` | Operator 설정·HPC 플랫폼 디스패치·클라우드 |
| `get_atcf.pl`·`get_nam.pl`·`get_flux.pl`·`storm_track_gen.pl`·`control_file_gen.pl` | 핵심 Perl 글루 (forcing 다운로드·fort.22/fort.15 생성) |
| `monitoring/`, `t/`, `doc/`, `docs/` | 모니터링·테스트·문서 |

## 3. Orchestration 골격 — `asgs_main.sh` (존재만 언급)

advisory cycle당 1회 도는 메인 루프 `while [ true ]` (`asgs_main.sh:2208`)가 골격. 한 사이클 내 ADCIRC 입력 준비 흐름:

1. **forcing 다운로드** — `downloadBackgroundMet` (NAM 등, `asgs_main.sh:2418`) 또는 ATCF 트랙(`get_atcf.pl`).
2. **vortex 전처리** — GAHM/ASYMMETRIC이면 `aswip` 실행하여 Rmax 사전계산 (`asgs_main.sh:2367-2382`).
3. **동적 입력 생성** — `generateDynamicInput.sh` source로 `tide_fac.out`·fort.13·fort.15·fort.26 생성 (`asgs_main.sh:1664`).
4. **도메인 분할/입력 패키징** — `prepFile partmesh/prepall/prep15/prep20/prep13` (`asgs_main.sh:565-581`) — ADCIRC `adcprep`를 래핑.
5. **실행 가능성 체크** — `tide_fac.x`·`aswip` 존재 검증 (`asgs_main.sh:1853-1858`).

설정은 3단계 우선순위(Operator config → default 파일 → 스크립트 내 초기값)로 머지 (`asgs_main.sh:readConfig()` 주석 `asgs_main.sh:38-53`). config defaults·model defaults·io defaults·forcing defaults를 순차 source (`asgs_main.sh:43-51`). ⚠ 개별 함수 라인별 분석은 본 노트 범위 밖.

## 4. 핵심 Fortran 유틸리티

### 4.1 `tide_fac` — 조석 nodal factor & equilibrium argument (`tides/tide_fac.f`)

조석 강제력에 필요한 **nodal factor(진폭 보정)와 Greenwich equilibrium argument(위상 기준)** 를 계산하는 프로그램 (`tides/tide_fac.f:1`, `PROGRAM TIDE_FAC` `:10`). 37개 조석 분조 지원 (`PARAMETER(NCNST=37)` `:12`). equilibrium argument는 Greenwich 자오선 기준 (`:16`).

CLI 옵션(메뉴 우회, ASGS 자동화용 — `jgf20110526` 추가 `:2-8`): `--length`(일)·`--year`·`--month`·`--day`·`--hour`·`-n/--numtidalconstituents`(분조 목록)·`--outputformat {simple|adcirc}`·`--outputdir` (`:46-91`). 출력 포맷 3종 — `WITHHEADER`(legacy)·`SIMPLEOUTPUT`(nf+eq arg만)·`ADCIRCOUTPUT`(fort.15 삽입형) (`:32-34`).

기본 7분조: M2 S2 N2 K1 K2 O1 Q1 (`:105-114`).

**계산 흐름** (`:139-146`):

| 단계 | 호출 | 의미 |
|---|---|---|
| 레코드 중간점 Julian time | `DAYJUL(YR,MONTH,DAY)` `:140`, `:555` | 율리우스 시간 |
| 레코드 중간점 node factor | `NFACS(YR,DAYJ,HRM)` `:143`, `:254` | nodal factor |
| 레코드 시작점 Greenwich equil. term | `GTERMS(YR,DAYJ,BHR,DAYJ,HRM)` `:146`, `:376` | equilibrium argument |

`NFACS`/`GTERMS`/`ORBIT` 식 출처 — **Schureman (1958), "Manual of Harmonic Analysis and Prediction of Tides", Special Publication #98, US Coast and Geodetic Survey** (`tides/tide_fac.f:246-249`). 보조 루틴: `ORBIT`(궤도 함수 `:456`)·`ANGLE`(`:501`)·`ARCTAN`(`:519`).

`ADCIRCOUTPUT` 모드는 분조별 tidal potential amplitude·frequency·earth tide reduction factor를 함께 쓴다 (예: M2 amp=0.242334, freq=0.000140518902509, factor=0.693 — `:197-201`).

**ASGS 호출** (`generateDynamicInput.sh:31`):
```
tide_fac.x --length $runLength --year ${CSDATE:0:4} --month ${CSDATE:4:2} \
  --day ${CSDATE:6:2} --hour ${CSDATE:8:2} -n ${#tidalConstituents[@]} \
  ${tidalConstituents[@]} --outputformat simple --outputdir $SCENARIODIR
```
출력 `tide_fac.out`는 fort.13/fort.15와 함께 시나리오 디렉토리에 생성 (`generateDynamicInput.sh:4`, `:30-39`).

### 4.2 `aswip` — asymmetric vortex 전처리 (`doc/util/aswip.1.txt`)

> ⚠ aswip 소스 본체는 ASGS 트리가 아니라 ADCIRC 코드(`adcirc/wind/aswip.F`)에 있고 ADCIRC와 함께 컴파일된다 (`doc/util/aswip.1.txt:133-134`). ASGS는 docs와 호출만 제공.

ATCF 포맷 fort.22(시각 열이 단조증가하게 채워진)를 읽어 ADCIRC **dynamic asymmetric vortex(NWS=19)** 또는 **GAHM(NWS=20)** 에 적합한 fort.22를 생성 (`aswip.1.txt:16-26`). NWS=15(HWind)는 시각화 분석만 (`:18-20`).

주요 옵션 (`:31-129`):

| 옵션 | 의미 |
|---|---|
| `-n NWS` | 입력 fort.22 모델 포맷 (15/19/20 지원, ATCF 기대) (`:102-108`) |
| `-m ISOTACH` | 한 사분면에 다중 isotach가 있을 때 Rmax 계산용 선택법 — NWS19=2(최고 isotach), NWS20=4(전부 사용) (`:80-88`) |
| `-z APPROACH` | radial wind 방향 — NWS19=1, NWS20=2 (`:90-93`) |
| `-g GEOFACTOR` | NWS20 개발 시 geostrophic(1, 권장) vs cyclostrophic(0) balance (`:69-73`) |
| `-r RMAX`, `-p %RMAX`, `-x %VMAX` | Rmax 일괄 설정·Rmax 가감·Vmax 강화/약화 (`:110-125`) |
| `-a/-v/-s` | 방위각별 Rmax / 5개 storm radii 풍속·기압 / 비정형 메쉬 풍장(VTK) 분석 출력 (`:31-52`) |

원작자 Robert Weaver·Rick Luettich, Jason Fleming이 모듈화·기상분석 기능 추가, Jie Gao가 GAHM 확장 (`:138-141`).

**ASGS 호출**: GAHM/ASYMMETRIC vortex일 때 `$ADCIRCDIR/aswip -n $BASENWS`로 Rmax 사전계산, 산출물 `NWS_${BASENWS}_fort.22`를 fort.22로 처리 (`asgs_main.sh:2363-2382`). 실패 시 fatal (`asgs_main.sh:2377`). SYMMETRIC(NWS=8)은 aswip 불필요 (`asgs_main.sh:2380-2387`).

### 4.3 기타 tides Fortran

| 파일 | 역할 |
|---|---|
| `tides/tides_ec2001.f` | ADCIRC 2DDI tidal data base에서 다른 모델 경계조건용 조석정보 추출 (Luettich·Westerink, UNC/Notre Dame) (`tides/tides_ec2001.f:3-22`) |
| `tides/ec2001v2d_tide_interp.f`, `tides/FES952_interp.f` | EC2001 / FES95.2 조석 데이터베이스 경계 보간 |
| `tides/tpxoBoundaryInterp.pl` | OSU TPXO 7.2 모델(h 바이너리)에서 fort.14 개경계 분조 진폭·위상 추출→fort.15 삽입 포맷 (`tides/tpxoBoundaryInterp.pl:3-16`) |

## 5. 입력 전처리 카탈로그 (`input/`, `util/input/`, Perl 글루)

| 도구 | 역할 | 근거 |
|---|---|---|
| `get_atcf.pl` | NHC에서 BEST·OFCL 트랙 파일 다운로드 (또는 로컬 로드) | `get_atcf.pl:3-6` |
| `storm_track_gen.pl` | 원시 ATCF → ADCIRC vortex용 fort.22 (기본: NHC 컨센서스 예보) | `storm_track_gen.pl:3-9` |
| `control_file_gen.pl` | YAML(stdin) 명세 기반 fort.15 생성→stdout | `control_file_gen.pl:3-4` |
| `get_nam.pl` | NCEP에서 nowcast/forecast용 배경 기상(NAM) 다운로드 | `get_nam.pl:3-4` |
| `get_flux.pl`·`set_flux.pl`·`stage_discharge.pl` | 하천 유량 경계 강제력 | (`asgs/` 루트) |
| `input/awip_lambert_interp.F`·`lambertInterpRamp.f` | NAM Lambert 격자 → ADCIRC 보간 (Fortran) | `ls input/` |
| `NAMtoOWIRamp.pl` (32 KB) | NAM → OceanWeather(OWI) ramp 포맷 변환 | `ls asgs/` |
| `input/advisoryDownloader.sh`·`advisoryMonitor.sh` | advisory 폴링·모니터 | `ls input/` |
| `util/input/nam_fort22_gen.pl`·`best2fcst.pl`·`track_offset.pl`·`pressure_predict.pl` | NAM fort.22·BEST→forecast·트랙 오프셋·기압 예측 | `ls util/input/` |

`generateDynamicInput.sh`가 한 시나리오의 동적 입력(`tide_fac.out`·fort.13·fort.15·fort.26)을 일괄 생성하는 진입점 (`generateDynamicInput.sh:1-4`, `:27`).

## 6. 출력 후처리 카탈로그 (`output/`)

ADCIRC/SWAN 결과(fort.63/64·maxele.63 등)를 시각화·배포 형식으로 변환. 대표 카테고리:

| 카테고리 | 도구 | 역할 |
|---|---|---|
| 그래픽 | `output/FigureGen/FigureGen.F90` | fort.14/13/63/64·maxele.63를 읽어 contour/벡터 발표용 이미지 생성 — "core에서 스크립트처럼 동작, 외부 SW에 system call" (Casey Dietrich) (`output/FigureGen/FigureGen.F90:2-18`) |
| 입자추적 | `output/PartTrack/`, `output/TRACKING_FILES/`, `output/part_track_post.sh` | particle track 입력 생성(`gen_part_track_input.sh`)·FigureGen 기반 입자 이미지(`FigureGen42_PartTrack_*`) (`ls output/PartTrack`, `ls output/TRACKING_FILES`) |
| netCDF 변환 | `output/adcirc2netcdf.f90`·`netcdf2adcirc.f90`·`convert_adc_native_2_netCDF.f90`·`asgsConvertToNETCDF.pl` | 네이티브 ↔ netCDF (`ls output/`) |
| KMZ/GIS | `output/POSTPROC_KMZGIS`·`asgsCreateKMZs.sh`·`kalpana.py` | Google Earth·GIS 산출 |
| 통계/시계열 | `output/pullStationTimeSeries.f90`·`pullTimeSeries.f90`·`stationProcessor.f90`·`collectMinMax.f90` | 관측소 시계열·min/max 추출 |
| OPeNDAP/THREDDS | `output/opendap_post.sh`·`createOPeNDAPFileList.sh`·`threddsConfig.xml` | 데이터 서버 배포 |
| 알림 | `output/cera_notify.sh`·`cera_post.sh`·`notify.sh`·`emailattach.py` | CERA·이메일 알림 |
| 검증/품질 | `output/checkAdcircMesh.f90`·`wetDryCheck.f90`·`inundationMask.f90`·`totalWaterDepthGradient.f90` | 메쉬·wet/dry·침수 마스크 검사 |

`part_track_post.sh`는 CONFIG·ADVISDIR·STORM·GRIDFILE 등 위치인자를 받아 입자추적 후처리를 수행 (`output/part_track_post.sh:20-30`). ⚠ 각 후처리 도구 본체 분석은 별도 노트 범위.

## 7. 관련 노트와의 경계

- met forcing(fort.22/NWS, GAHM/vortex) 메커닉 → `[[adcirc-met-forcing-implementation]]` (본 노트는 ASGS 측 `aswip` 호출만).
- 출력 파일 writer(fort.63 등) 메커닉 → `[[adcirc-output-writers-implementation]]` (본 노트는 ASGS 후처리 변환 도구 카탈로그만).

## 8. 한계 (S-tier 명시)

- `asgs_main.sh`(160 KB)·`control_file_gen.pl`(65 KB)·`storm_track_gen.pl`(46 KB) 등 핵심 orchestration의 **라인별 알고리즘은 미분석** — 본 노트는 진입점·호출 관계·대표 file:line에 한정.
- `FigureGen.F90`·PartTrack Fortran·netCDF 변환기 등 후처리 본체는 카탈로그 수준(헤더·역할)만 검증.
- 플랫폼 디스패치(`platforms/`·`platforms.sh`)·클라우드(`cloud/`)·HPC 큐 스크립트(`qscript.pl`) 미분석.
- `[source-needed]`: 개별 후처리 도구의 수치 알고리즘, config 파라미터 전체 카탈로그는 후속 노트 필요.

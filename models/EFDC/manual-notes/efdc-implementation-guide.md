---
title: "EFDC+ Computer Implementation Guide (R8.5.0) — 빌드·실행·입력파일(efdc.inp 카드)·출력 절차"
model: EFDC
doc: EFDC_Implementation_Guide.pdf
canonical_source: manual
citation_status: verified
verification_method: "EFDC_Implementation_Guide.pdf pdftotext -layout 직접 추출 후 전체 TOC(p.i) + 핵심 장 페이지 인용. 빌드/실행(p.1-4), 그리드 생성기(p.5-13), efdc.inp 카드 구조 C1~C91B(p.15-65), 필수/선택 공간파일(p.66-68), 모듈별 입력파일 표(p.69-73), 출력파일+GetEFDC(p.73-76), 샘플모델(p.77-79), 라이선스(p.80) 인용 확인"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/EFDC/README.md
  - models/EFDC/source-analysis/efdc-tidal-forcing-conventions-v12.md
---

# EFDC+ Computer Implementation Guide (R8.5.0) — 구현·입력 카드 절차

> EFDC+ 빌드(Intel Fortran+VS)·실행(serial/OpenMP)·Cartesian 그리드 생성·`efdc.inp` 카드 reference(C1~C91B)·모듈별 입력파일·바이너리 출력+GetEFDC 후처리를 다루는 82p 운영 매뉴얼. **물리 이론·process 식이 아니라 구현/입력카드 절차에 특화**. 지배방정식·난류폐쇄 이론·sediment process 식은 [[efdc-theory-v12-ch2-hydrodynamics]]·[[efdc-theory-doc-v12]]·[[efdc-sediment-theory-2003]] 참조. 파라미터 글로서리는 [[efdc-parameter-glossary-v1]].

## 1. 문서 정체

| 항목 | 값 |
|---|---|
| 제목 | EFDC+ Computer Implementation Guide (표지, p.표지) |
| Release | 8.5.0 (표지) |
| 발행처 | DSI, LLC (표지) |
| 날짜 | Jan 27, 2020 (표지) |
| 라이선스 | Apache License 2.0, Copyright 2019 DSI, LLC §1.6 (p.80) |

목적: 사용자·개발자에게 EFDC+ 코드의 build/run/develop 방법, 기본 모델 셋업·후처리, 샘플 모델 제공 (Ch.1 서문, p.1).

## 2. 전체 TOC (장별 페이지)

`efdc.inp` 카드 reference가 §1.3.1 Primary Run Control 하나에 p.15–65로 집중되어 매뉴얼의 절반 이상을 차지 (p.i TOC).

| § | 제목 | p. |
|---|---|---|
| 1 | Introduction | 1 |
| 1.1 | Getting Started | 1 |
| 1.1.1 | Build Instructions | 1 |
| 1.1.2 | Running | 3 |
| 1.2 | Cartesian Grid Generator User Guide | 5 |
| 1.2.1 | Generate Uniform Grid | 7 |
| 1.2.2 | Generate Radial Grid | 11 |
| 1.2.3 | Generate Telescoping Grid | 11 |
| 1.2.4 | Import Grids from Files | 12 |
| 1.3 | Input Files | 14 |
| 1.3.1 | Primary Run Control (efdc.inp 카드) | 15 |
| 1.3.2 | Required Spatial Files | 66 |
| 1.3.3 | General Transport | 69 |
| 1.3.4 | Sediment | 70 |
| 1.3.5 | Wave Parameter Files | 71 |
| 1.3.6 | Eutrophication Module | 71 |
| 1.3.7 | Toxics Module | 72 |
| 1.3.8 | Temperature Module | 73 |
| 1.4 | Output Files | 73 |
| 1.4.1 | Output Files | 73 |
| 1.4.2 | GetEFDC | 74 |
| 1.5 | Sample Models | 77 |
| 1.6 | License | 80 |

(p.i)

## 3. 빌드 (§1.1.1, p.1–3)

- 소스: GitHub `git clone https://github.com/dsi-llc/EFDCPlus` (p.1). 루트 하위 폴더: `EFDC`(소스+샘플 exe), `NetCDFLib`, `GridGenerator`, `GetEFDC`, `WASP`, `SampleModels`, `docs` (p.1).
- 빌드: Visual Studio(VS) + **Intel Fortran compiler**(선호·최다 테스트). 루트 `EFDC` 폴더의 `.sln` 솔루션 오픈. Windows 7+ / VS 2015+ 가정 (p.1).
- 사전빌드 exe 위치: `EFDC/DebugSP64/`, `EFDC/ReleaseDP64/`, `EFDC/ReleaseSP/`, `EFDC/ReleaseSP64/` (p.1).

### 빌드 구성 (8종, p.2)
DEBUG SP / DEBUG SP 64 / DEBUG DP / DEBUG DP 64 / Release SP / Release SP 64 / Release DP / Release DP 64. 표기 약어 (p.2):

| 약어 | 의미 |
|---|---|
| SP | Single Precision |
| DP | Double Precision |
| 64 | 64 bit compilation |

`64` 미표기 시 32bit (p.2).

### OpenMP 컴파일 설정 (verbatim, p.2)
VS Properties 페이지 설정 (제공 빌드에 이미 구성됨):

| 위치 | 설정 |
|---|---|
| Fortran\Preprocessor | OpenMP Conditional Compilation = `Yes` |
| Fortran\Preprocessor | Process OpenMP Directives = `Generate Parallel Code (/Qopenmp)` |
| Fortran\Libraries | Runtime Library = `Multithreaded DLL (/libs.dll /threads)` |
| Linker\Input | Additional Dependencies = `libiomp5md.lib` |

- 테스트된 Intel compiler: Intel 15, 19.3, 19.4 (p.2). 테스트된 VS: 2015, 2019(Preview 4) (p.2).

## 4. 실행 (§1.1.2, p.3–4)

- 실행 방법: (a) **EFDC Explorer GUI**(가장 간단), (b) 커맨드 프롬프트/배치 스크립트 (p.3). 본 가이드는 GUI 미사용 가정 (p.3).
- 실행 옵션: **Serial**(단일 코어, 특별 컴파일 불필요), **Multithreaded**(OpenMP 컴파일 시 멀티코어) (p.3).
- 멀티스레딩 기술: OpenMP 채택. Intel Hyper-Threading은 물리 코어당 2 thread (p.3). Tip: 계산집약 응용은 thread 수 = 물리 코어 수일 때 최적 throughput (p.3).
- 재현성: EFDC_DSI_OMP 모델은 thread 수와 무관하게 **정확히 동일한 결과**(모델 정밀도 내 차이=0) (p.4).

### 샘플 배치 스크립트 (verbatim, p.3–4)
```
SET KMP_AFFINITY=granularity=fine,compact,1,0
TITLE Sample Title of the Problem
CD "C:\Path\To\WorkingDirectory\"
"C:\Path\To\Exectuable\EFDCPlus.exe" -NT2 -NOP
```
- `KMP_AFFINITY=granularity=fine,compact,1,0`: OpenMP thread를 물리 처리유닛에 바인딩 (p.3).
- `-NT2`: 사용할 thread 수 지정 (여기서 2; -NT3,-NT4… 가능) (p.4). ⚠ Important: 논리 코어 수보다 많이 지정 금지 (p.4).
- 종료 화면에 CPU usage = Total CPU/#Cores 보고 (run time 영향 해석용) (p.4).

## 5. Cartesian Grid Generator (§1.2, p.5–13)

`GridGenerator.exe`로 그리드 생성·시각화·기본 입력파일 작성 (p.5). 4가지 옵션 (p.6):

| 옵션 | 핵심 입력 | p. |
|---|---|---|
| Generate Uniform Grid | Lower-Left·Upper-Right 좌표, X/Y 셀 크기 또는 셀 수, **Rotation Angle**(도), **UTM Zone**(1~60) | 7 |
| Generate Radial Grid | 기본값 채워진 Radial Grid Options | 11 |
| Generate Telescoping Grid | 기본값 채워진 Telescoping 프레임 | 11 |
| Import Grids from Files | 기존 그리드 파일 import | 12 |

- Bounding Polygon(=shoreline)으로 도메인 제한, **Remove Dry**로 폴리곤 외부 셀 제거 (p.8–9).
- Export 포맷: `*.CVL` 또는 `*.GRD` (p.10). Save Model로 EE10 로딩 가능 EFDC 모델 저장 (p.10).
- Import 지원 포맷: **CVLGrid**(DSI 곡선직교), **RGFGrid**(Deltares), **Grid95**, **DXDY/LYLY**(EFDC+ 그리드 descriptor), **ECOMSED**, **SEAGRID**, **CH3D**(USACE), **Corners**(셀 4모서리 좌표) (p.12).
- UTM Zone은 모델 계산에 미사용이나 좌표 변환·GIS export·NetCDF 출력에 중요 → OK 전 정확히 설정 (p.13).

## 6. efdc.inp 카드 구조 (§1.3.1, p.15–65)

`efdc.inp` = master 제어파일, 모든 실행 옵션 지정. 역사적으로 **card type**별 조직 (p.15). 주석: `*` 또는 `-`로 시작하는 줄은 무시 (p.15).

### 6.1 Run Control / Restart 파일 (p.15)
| 파일 | 설명 |
|---|---|
| `efdc.inp` | Master EFDC+ 제어파일 |
| `show.inp` | 런타임 reporting 옵션 |
| `efdcwin.inp` | 간이 제어 (deprecated) |
| `restart.inp` | hydrodynamic restart |
| `rstwd.inp` | wetting & drying restart |
| `temp.rst` | bed temperature restart |
| `wqwcrst.inp` | water quality restart |
| `wqsdrst.inp` | sediment diagenesis restart |
| `wqrpemrst.inp` | rooted plant & epiphyte restart |

### 6.2 카드 인덱스 (C1~C91B)
전체 카드는 단일 `efdc.inp`에 배치되어 실행 시 순차 read (p.15). 주요 카드 그룹 (각 카드 데이터라인 헤더는 p.15–65 해당 페이지에 verbatim):

| 카드 | 제목 | p. |
|---|---|---|
| C1 / C1A | Run Title / 그리드 구성·시간적분 모드 | 15 |
| C2 | Restart·일반제어·진단 스위치 | 16 |
| C3 | External mode 해법 옵션 | 17 |
| C4 | Long-term mass transport 적분 스위치 | 17 |
| C5 | 운동량 advection·수평확산·기타 스위치 | 18 |
| C6 | 용존·부유 constituent transport 스위치 | 18 |
| C7 / C8 | 시간 관련 정수 / 실수 파라미터 | 19 |
| C9 | 공간 관련·smoothing 파라미터 | 20 |
| C10 | 연직 layer thickness | 20 |
| C11 / C11A / C11B | 그리드·조도·수심 / 2-layer momentum·curvature 보정 / corner cell bed stress 보정 | 21 (C11B는 22) |
| C12 / C12A | 난류확산 파라미터 / 난류폐쇄 옵션 | 21–22 |
| C13 | 난류폐쇄 파라미터 | 22 |
| C14 / C14C | 조석·대기 forcing·지하수·subgrid channel / 시공간 변동 forcing | 22–23 |
| C15 | 주기 forcing(조석) constituent 기호·주기 | 23 |
| C16–C21 | 표면고도/압력 BC 파라미터 및 S/W/E/N 개방경계 forcing | 24~ |
| C22 / C22B | sediment·toxics·시계열 수 / Shellfish | — |
| C23–C35 | 유량·체적 source/sink·flow control·withdrawal/return·jet/plume | — |
| C36~C42A | sediment 초기화·bed 역학·cohesive/non-cohesive·bedload | — |
| C43A~C46E | toxics(IC·kinetics·volatilization·sorption·OC) / buoyancy·temp·dye·ice·대기 | — |
| C47~C66B | 농도 BC·data assimilation 등 | — |
| C67 / C68 | drifter 데이터 / 초기 drifter 위치 | — |
| C69 | Cartesian 셀 중심 경위도 상수 | — |
| C70~C91B | ASCII/binary dump·수평 contour·EE_Explorer linkage·3D field 출력·조화해석·시계열 출력·NetCDF | 63–65 |

(카드 헤더 위치는 §2 추출 grep로 라인별 확인; 페이지는 p.15–65 범위)

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)** — 위 카드 인덱스는 R8.5.0 매뉴얼(2020)을 정확히 기술하나, EFDC+ v12.4 소스(`EFDCPlus_Stable`, 로컬 clone 직접 확인 2026-07-04)는 다음이 다르다. 상세 규약은 [[efdc-tidal-forcing-conventions-v12]] 참조.
>
> - **C2A (매뉴얼 미기재)**: v12.4는 `ISRESTI==1 .and. ICONTINUE==1`(continuation restart)일 때 `SEEK('C2A')` 후 2줄 — `Restart_In_Ver`, `RESTARTF`(restart 파일명) — 를 읽는다 (`input.f90:198-200`). 본 매뉴얼 카드 인덱스에는 C2A가 없다.
> - **C22B (Shellfish) 미독**: v12.4 `input.f90`의 SEEK 카드 인벤토리에 C22B가 없다 — 이 카드는 읽히지 않는다. Shellfish 설정은 대신 `READ_SHELLFISH_JSON`(JSON 파일)으로 로드 (`input.f90:3941-3943`, `SHELLFISHMOD`).
> - **C67~C91B 계열 대량 미독**: v12.4가 SEEK하지 않는 카드 = **C66A/C66B, C68–C70, C73–C83, C89–C90** (drifter 초기위치·경위도 상수·ASCII dump 계열 등). SEEK 인벤토리에 살아있는 것은 C66, C67, C71/C71A/C71B, C72, C84–C88, C91/C91A/C91B/C91C 뿐 (v12.4 `input.f90` 전수 grep, 2026-07-04).
> - **C17 위상 규약**: 레거시 매뉴얼류의 "phase relative to time origin of TBEGIN" 서술과 달리, v12.4는 **절대 시간** `TIMESEC`로 합성한다: `hdmt.f90:89` `TIMESEC = TCON·TBEGIN` → `setopenbc.f90:232` `TN = TIMESEC` → η = PFAM·cos(2π(TIMESEC−PFPH)/TCP) (`input.f90:913-915` CPFAM0/SPFAM0 변환). 즉 PFPH는 **TCP와 같은 시간 단위(초)의 lag**이고 `PFPH = [TCON·TBEGIN + TCP·(G−(V0+u))/360] mod TCP`로 만들어야 한다. 도(°) 단위 위상을 그대로 넣으면 안 된다.

### 6.3 핵심 카드 상세 (verbatim 옵션·기본값)

**C1A 그리드·시간적분** (p.15): `IS2TIM`(0=three-time-level, 1=two-time-level), `IGRIDV`(0=표준 sigma 연직 또는 단일층 depth-avg, 1=Sigma-Zed 셀별 가변 layer(DSI), 2=Sigma-Zed 수평균일 두께(DSI)), `SGZMin`(SGZ 최소 layer 수), `SGZHPDelta`(IGRIDV>0 시 IC 대비 수위 상승 m). 데이터라인: `C1A IS2TIM IGRIDH IGRIDV SGZMin SGZHPDelta`.

**C3 External mode solver** (p.17): `RP`(over-relaxation), `RSQM`(목표 square residual), `ITERM`(최대 반복), `IRVEC`(0=conjugate gradient 무 scaling, 9=min diagonal scale, 99=normal form scale), `IWDRAG`(0=원 EFDC wind drag, 1=상대 수면속도 보정, 2=**Hersbach 2011 ECMWF**, 3=**simplified COARE 3.6** neutral+상대속도), `IDRYCK`(drying check당 반복, 2≤IDRYCK≤20), `FILT3TL`(3TL explicit filter 계수, `0.0625`).

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)**: v12.4의 C3 read 목록은 `RP, RSQM, ITERM, IRVEC, IATMP, IWDRAG, ITERHPM, ldum, ISDSOLV, tmp` (`input.f90:225`) — 매뉴얼의 **`IDRYCK`·`FILT3TL` 식별자는 v12.4 소스 어디에도 존재하지 않는다** (전 `.f90` grep 0건, 2026-07-04). 해당 슬롯은 `ITERHPM`/`ldum`/`ISDSOLV`/`tmp`로 대체. 또한 `IRVEC`은 **0 또는 9만 허용** — 99를 넣으면 `STOPP('INVALID IRVEC')`로 즉시 정지한다 (`input.f90:237`).

**C5 운동량 advection·misc** (p.18): `ISCDMA`(1=central diff momentum advection 3TL, 0=upwind), `ISHDMF`(1=수평 운동량 확산, 2=+water column), `ISDRY`(0=W&D 없음, 11=상수 drying depth HDRY+비선형반복, 99=가변 W&D depth cell-face masking), `ISRLID`(1=rigid lid 모드, 자유표면 없음), `ISVEG`(1=식생 저항, 2=+CBOT.LOG 진단), `IINTPG`(0=원 internal pressure gradient, 1=Jacobian, 2=finite volume).

**C6 constituent transport** (p.18): index 매핑 — turb intensity=0, SAL=1, TEM=2, DYE=3, SFL=4, TOX=5, SED=6, SND=7, CWQ=8. `ISTRAN`(≥1 transport 활성), `ISCDCA`(0=donor cell upwind 3TL, 1=central diff 3TL), `ISADAC`(1=anti-numerical diffusion 보정), `ISFCT`(1=flux limiting 추가).

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)**: v12.4의 C6 read는 `ISTRAN(NS), ISTOPT(NS), ldum, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)` (`input.f90:306`) — **3·6·7·8번째 슬롯은 더미(`ldum`)로 읽고 버린다**. 즉 매뉴얼이 3번째 슬롯에 문서화한 `ISCDCA` 등은 v12.4에서 **무시**된다 (자리는 유지해야 파싱이 맞음).

**C7 시간 정수** (p.19): `NTC`(reference time period 수), `NTSPTC`(reference period당 time step 수), `NTSTBC`(2TL trapezoidal 보정 step 간격, =mass balance print 간격), `NDRYSTP`(>0 시 isolated cell이 dry로 강제되기까지 step 수, 손실수는 QDWASTE 추적), `NRAMPUP`(dynamic time-stepping 시 step 고정 초기 loop 수).

**C8 시간 실수** (p.19): `TCON`(TBEGIN→초 변환 배수), `TBEGIN`(run 시간 원점), `TREF`(reference 주기 sec, 예 44714.16s 또는 86400s), `CORIOLIS`(=2*7.29E-5*SIN(LAT)), `DTSSFAC`(>0이면 dynamic time-stepping), `DTMAX`(dynamic stepping 최대 step 초).

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)**: v12.4의 C8 read는 `TCON, TBEGIN, TIDALP, CF, ISCORV, ISDCCA, ISCFL, ISCFLM, DTSSFAC, DTSSDHDT, DTMAX` (`input.f90:387`) — 매뉴얼의 `TREF`/`CORIOLIS`는 v12.4에서 **`TIDALP`/`CF`라는 이름**으로 같은 슬롯에 읽힌다 (의미 동일: reference 주기 / Coriolis 상수). 이름만 다르고 자리는 같으므로 파일 호환은 유지.

**C9 공간** (p.20): `IC`(I방향 셀 수), `JC`(J방향 셀 수), `LC`(활성 수평셀 수+2), `LVC`(가변크기 수평셀 수), `ISCO`(1=곡선직교 그리드, LVC=LC-2), `NDM`(수평 domain decomposition 수, 단일 프로세서=1), `ISMASK`(1=mask.inp로 셀 land 마스킹/thin barrier), `ISCONNECT`(1=N-S, 2=E-W, 3=양방향 셀 연결).

**C10 연직 layer** (p.20): `K`(layer 번호 1~KC), `DZC`(무차원 layer 두께, 합=1.0 必).

**C11 그리드·조도·수심** (p.21): `DXYCVT`(DX/DY→m 변환), `ZBRADJ`(log BL 조도 높이 조정 m), `HMIN`(입력 최소 수심 m), `HDRY`(셀/flow face가 dry되는 수심), `HWET`(withdrawal 차단 수심), `BELADJ`(bed 고도 조정 m).

**C11B corner cell bed stress** (p.22): `FSCORTBC`(보정계수 0~1, 1.0=무보정, 0.0=최대보정, **0.5 권장**).

**C12A 난류폐쇄 옵션** (p.21–22): `ISSTAB`(0=Galperin et al. 안정함수 in CALAVBOLD …). 데이터라인 `C12A ISSTAB ISSQL ISAVBMX ISFAVB ISINWV ISLLIM IFPROX XYRATIO`.

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)**: v12.4의 C12A 첫 슬롯은 `ISSTAB`이 아니라 **`ISTOPT(0)`** (난류 폐쇄 옵션 배열의 0번 원소)로 읽힌다: `read ... ISTOPT(0), ISSQL, ISAVBMX, ISFAVB, ISINWV, ISLLIM, IFPROX, XYRATIO, BC_EDGEFACTOR` (`input.f90:646`). `ISSTAB` 식별자는 v12.4 소스에 없고, 마지막에 `BC_EDGEFACTOR` 슬롯이 추가되어 9개 값을 읽는다.

**C14 forcing·subgrid channel** (p.22): `MTIDE`, `NWSER`(wind series 수), `NASER`(대기 series 수), `ISGWIT`(지하수), `ISCHAN`(subgrid channel), `ISWAVE`(1=boundary layer 영향만 WAVEBL.INP, …).

## 7. 필수·선택 공간 파일 (§1.3.2, p.66–68)

**필수** (p.66): `cell.inp`(셀 매핑/타입), `celllt.inp`(보조 셀타입), `dxdy.inp`(수평 셀 치수·수심·bed 고도·조도·식생), `lxly.inp`(셀 중심 좌표·방향), `corners.inp`(LPT용 모서리 좌표).
**선택** (p.66): `mask.inp`(thin barrier, NMASK>0), `layermask.inp`(layer face barrier, 10.1+), `mappgns.inp`(N-S 그리드 연결), `mappgew.inp`(E-W 연결), `moddxdy.inp`(dxdy 수정), `sgzlayer.inp`(IGRIDV=1 시 최하 활성 layer).

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)** — `mask.inp`의 `MTYPE` 의미: 레거시 매뉴얼(EPA 계열)은 1=west/U face, 2=south/V face, 3=네 면 전부, MTYPE 4 없음으로 기술하나, v12.4 `cellmask.f90:50-66`은 **1=U face(서쪽), 2=V face(남쪽), 3=U+V(서+남 두 면), 4=isolated waters**(자기 셀 U·V + 동쪽 셀 U + 북쪽 셀 V — 네 면 완전 고립, `cellmask.f90:165` 주석 "Change to MTYPE 4 for isolated waters")로 정의한다. 즉 "네 면 차단"은 3이 아니라 **4**다.

### cell.inp (p.66)
IC×JC 매트릭스. IC/JC는 C9에서 지정. **매핑은 좌하단부터 시작** (p.66). 셀 타입:

| 번호 | 의미 |
|---|---|
| 0 | water 셀과 변/모서리 미접 dry land |
| 1–4 | 삼각형 water 셀 (각각 land 위치 NE/SE/SW/NW) |
| 5 | 사각형 water 셀 |
| 9 | water 셀과 변/모서리 접하는 dry land 또는 개방경계 인접 가짜 dry land |

### dxdy.inp (p.67) / lxly.inp (p.67–68)
`dxdy.inp` 컬럼: `I J DX DY DEPTH BOTTOM_ELEV ZROUGH VEG_TYPE` (DX/DY=셀치수 m, DEPTH=초기수심 m, ZROUGH=log law 조도높이 z0 m) (p.67). `cell.inp`의 모든 셀 기술 必.
`lxly.inp` 컬럼: `I J X Y CUE CVE CUN CVN Wind_Shelter` (CUE/CVE/CUN/CVN=회전행렬 성분) (p.67–68).

## 8. 모듈별 입력파일 (§1.3.3–1.3.8, p.69–73)

| 모듈 | 대표 파일 (p.) |
|---|---|
| Hydro 파라미터 | `AHMAP.INP`(Smagorinsky), `AVMAP.INP`, `WSER.INP`(풍속·풍향 시계열), `WNDMAP.INP`(NWSER>1 가중), `RESTART.INP`, `RSTWD.INP`(ISDRY>0) (p.69) |
| 체적·수위 BC | `QSER.INP`, `PSER.INP`, `QWRS.INP`, `QCTL.INP`, `QCRULES.INP`(구조물 제어 규칙), `GWATER/GWSEEP/GWSER/GWMAP.INP`(지하수) (p.69) |
| Salt | `SALT.INP`(IC), `SSER.INP`(BC 시계열) (p.69) |
| LPT | `DRIFTER.INP` (p.69) |
| Shellfish | `SFBSER/SFL/SFSER.INP` (p.70) |
| Dye | `DYE.INP`, `DSER.INP` (p.70) |
| Sediment (원) | `SEDW/SEDB/SDSER`, `SNDW/SNDB/SNSER`, `BEDBDN/BEDDDN/BEDLAY`, `BEMAP/BESER`(bank erosion) (p.70) |
| **SEDZLJ** | `BED.SDF`(제어), `ERATE.SDF`(SEDFlume core), `CORE_FIELD.SDF`, `SEDBED_HOT.SDF`(restart) (p.70) |
| Wave | `WAVE.INP`, `WAVETIME.INP`, `WAVECELLS.INP`(IUSEWVCELLS>0 & ISWAVE>2), `SWAN_GRP/SWAN_LOC/SWAN_TBL.INP`(SWAN linkage) (p.71) |
| Eutrophication | `WQ3DWC.INP`(WC 제어), `KINETICS.INP`(DO zone), `WQICI.INP`, `WQPSL.INP`(mass loading), `SUNDAY.INP`(일평균 일사) (p.71) |
| Diagenesis | `WQ3DSD.INP`(제어), `WQSDICI.INP`, `WQSDMAP.INP`, `WQSDRST.INP/.BIN` (p.72) |
| RPEM | `WQRPEM.INP`(제어), `WQRPEMSIC.INP`, `WQRPEMRST.INP` (p.72) |
| MHK | `MHK.INP` (p.72) |
| Toxics | `TOXW/TOXB/TXSER`, `PARTMIX/PMXMAP`(bed 입자혼합), `DOCW/DOCB/FOCB/FPOCB/FPOCW/POCB/POCW` (OC) (p.72) |
| Temperature | `TEMP.INP`(IC), `TSER.INP`(BC), `ASER.INP`(대기), `ATMMAP.INP`(NASER>1), `PSHADE.INP`(shading), `SVHTFACT.INP`(ISVHEAT>0 표면열교환), `TEMB.INP`(bed temp) (p.73) |
| Ice | `ISER.INP`(ISICE=1), `ICEMAP.INP`(NISER>1), `ISTAT.INP`(ISICE=2), `ICE.INP`(ISICE>2 heat-coupled) (p.73) |

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)** — `WSER.INP`의 `ISWDINT`: DSI 블로그·wser 헤더는 `ISWDINT=2`를 "동/북 속도 성분 입력"으로 기술하나, v12.4 런타임(`caltsxy.f90:244-251`, TSWND의 유일한 런타임 소비처)은 **항상 1열=풍속, 2열=풍향(불어가는 쪽 나침반 방위, `DEGM=90−방향`으로 수학각 변환)** 으로 해석한다. `ISWDINT=2`의 read 처리는 두 열에 `WINDSCT` 배율만 곱할 뿐이어서 (`input.f90:6934-6939`) **성분 입력은 v12.4에서 조용히 오독된다**. 실재하는 옵션은 `ISWDINT=0`(불어가는 방향) / `=1`(불어오는 방향 — read 시 180° 반전, `input.f90:6923-6933`)뿐. 상세: [[efdc-tidal-forcing-conventions-v12]] §5.

## 9. 출력 파일 + GetEFDC (§1.4, p.73–76)

EFDC+는 **바이너리** 출력 생성, EE Modeling System(EEMS) GUI로 보거나 **GetEFDC**(Fortran 90 유틸)로 추출 (p.73). 바이너리 출력 (p.73):

| 파일 | 내용 |
|---|---|
| `EE_WS.OUT` | water depth |
| `EE_WC.OUT` | water column + sediment 최상층 |
| `EE_BC.OUT` | 계산된 경계 flow |
| `EE_BED.OUT` | sediment bed layer 정보 |
| `EE_WQ.OUT` | WC 수질 |
| `EE_SD.OUT` | sediment diagenesis |
| `EE_RPEM.OUT` | rooted plant & epiphyte |
| `EE_SEDZLJ.OUT` | SEDZLJ bed 데이터 |
| `EE_HYD.OUT` | water depth + velocity |

### GetEFDC (§1.4.2, p.74–76)
- 구성: main `getefdc.f90` + 8 모듈(`infomod`, `efdcpromod`, `tecmod`, `geteeoutmod`, `xyijconv`, `gethfreqout`, `globalvars`) (p.74). makefile은 `/GetEFDC/src` (Linux용; Windows는 VS) (p.74).
- 실행: `GetEFDC.exe getefdc.inp` (p.74).
- master `getefdc.inp` 핵심 파라미터 (p.74–75): `LAYK`(>0=layer k 데이터, 0=depth-avg, -1=High Frequency, -2=bed 위 높이 TS, -3=TMP.DAT→TECPLOT), `ZOPT`(LAYK=-2 시 1=수면 아래 깊이, 2=bed 위 높이), `JULTIME`(Julian time, 0=전 snapshot), `NLOC`(셀 수), `ROTA`(0=무회전, 1=true east/north 회전), `INDEX`(0=UTM X,Y, 1=I,J), `VPROF`/`TECPLOT`(0/1).
- 필수 입력파일: `getefdc.inp`, `efdc.inp`, `lxly.inp`, `dxdy.inp`, `cell.inp`, `corners.inp`, `mappgns.inp`, `mappgew.inp` (p.75).
- 출력: 작업모델 `#output` 하위 `RESULT` 폴더에 ASCII. 명명규칙 — 구성성분(예 SAL) + `TSK_<K>`(layer K 시계열) + `_DOM`(도메인)/`CEL`(선택셀); 연직 프로파일은 `_PROF`(예 `SAL_PROF.DAT`) (p.76).

## 10. 샘플 모델 (§1.5, p.77–79)

EFDC+ v8.5로 실행, GridGenerator로 시각화 (p.77).

| 모델 | 경로 | 규모 | 모듈 |
|---|---|---|---|
| Lake 2D | `SampleModels\Lake_T_HYD_WQ` | 355 수평셀, 1 layer | hydro·temp·WQ (p.77) |
| Ohio River | `SampleModels\Ohio_River_4` | 510 수평셀, 1·4 layer | hydro + dye (Mill Creek pulse) (p.78) |
| Lake Washington | `SampleModels/Lake_Washington` | 1,183 수평셀, 55 layer | temp + **Sigma-Zed** (성층 모의, pressure gradient 오차 저감) (p.79) |

## 11. 다른 노트와의 경계

- 본 노트 = **구현/입력 카드 절차** (빌드·실행·`efdc.inp` 카드·입력파일·출력).
- 지배방정식·process 식·이론은 [[efdc-theory-v12-ch2-hydrodynamics]]·[[efdc-theory-doc-v12]]·[[efdc-sediment-theory-2003]].
- 카드 파라미터 의미 글로서리: [[efdc-parameter-glossary-v1]].
- 그리드 시스템 기초: [[efdc-grid-system-foundation]] / 캘리브레이션: [[efdc-calibration-foundation]].
- 매뉴얼 전체 맵: [[efdc-manuals-overview]].
- **v12.4 소스 드리프트** (본 노트 내 ⚠️ 주석 블록들) 및 조석·바람 강제력 규약 상세: [[efdc-tidal-forcing-conventions-v12]] / 경계조건 런타임: [[efdc_boundary_conditions]].

---
title: "SWAN swanuse §4.4-4.5.3 command reference — start-up(PROJECT/SET/MODE/COORD) + grid(CGRID/READGRID) + input(INPGRID/READINP/WIND) + BC/IC(BOUND/INITIAL) verbatim"
topic: swan
canonical_source: external
external_source: "swanuse.pdf (User Manual, SWAN Cycle III version 41.51) §4.4 Start-up + §4.5.1 grid + §4.5.2 input + §4.5.3 BC/IC (p.26-56) + node23/25/26/27.md. command 구문·파라미터·default."
citation_status: verified
verification_method: "swanuse website_markdown node23(Start-up 278줄)/node25(CGRID 275)/node26(input 599)/node27(BC/IC 609) 직접 read: PROJECT/SET/MODE/COORDINATES/CGRID/READGRID/INPGRID/READINP/WIND/ICE/BOUND/BOUNDSPEC/INITIAL 구문+default verbatim."
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — command 구문·default 값 verbatim"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-command-physics-reference.md
  - models/SWAN/manual-notes/swan-command-numerics-output-reference.md
  - models/SWAN/manual-notes/swan-tech-ch4-5-bc-2d-setup.md
---

# SWAN swanuse §4.4-4.5.3 setup/grid/input/BC command reference — verified

> swanuse.pdf (User Manual v41.51) §4.4-4.5.3 직접 read. SWAN 입력파일의 **설정·격자·입력데이터·경계/초기조건** command 구문·default. Physics command 는 [[swan-command-physics-reference]], numerics/output 은 [[swan-command-numerics-output-reference]].

## 1. §4.4 Start-up

### 1.1 PROJECT
```
PROJECT 'name' 'nr' 'title1' 'title2' 'title3'
```
프로젝트 이름 + run 번호(nr) + 제목 3줄. 출력 헤더용.

### 1.2 SET — general parameters
```
SET [level] [nor] [depmin] [maxmes] [maxerr] [grav] [rho] [cdcap] [inrhog] [hsrerr] <NAUTical|CARTesian> [pwtail] [froudmax] [icewind] [excmark]
```
| param | default | 의미 |
|---|---|---|
| `[level]` | 0 | 공간·시간 일정 수위 상승 (m) |
| `[nor]` | 90° | 북쪽 방향 (x축 기준 반시계). spherical 시 변경 불가 |
| `[depmin]` | **0.05** | threshold 수심 (m), 이하 = depmin |
| `[maxmes]` | 200 | 종료 전 최대 error message 수 |
| `[maxerr]` | 1 | 계산중단 error level (1 warning/2 error/3 severe) |
| `[grav]` | 9.81 | 중력가속도 |
| `[rho]` | **1025** | 물 밀도 kg/m³ |
| `[cdcap]` | 99999 (제한없음) | 최대 wind drag coeff (제안 2.5e-3) |
| `[inrhog]` | 0 | 출력 0=variance / 1=true energy |
| `[hsrerr]` | 0.10 | Hs 부합 경고 임계 (structured only) |
| NAUTICAL / **CARTESIAN** | CARTESIAN | wind/wave 방향 convention |
| `[pwtail]` | GEN3 KOMEN/WESTH **4**, GEN1/2/JANSSEN 5 | high-freq tail power (GEN 뒤 SET 시 override) |
| `[froudmax]` | 0.8 | 최대 Froude (current/√gd, 초과시 maximize) |
| `[icewind]` | 0 | 0=wind input × open water fraction / 1=ice 무영향 |
| `[excmark]` | 999 | unstructured boundary vertex 제외 marker |

### 1.3 MODE
```
MODE <-> STATionary | NONSTationary> <-> TWODimensional | ONEDimensional>
```
**default STATIONARY TWODIMENSIONAL**. Nonstationary = (a)단일 nonstat (b)연속 stationary 시퀀스 (c)혼합 (COMPUTE).

### 1.4 COORDINATES
```
COORDINATES <-> CARTesian | SPHErical <-> CCM | QC>> REPeating
```
- **CARTESIAN default** (m). **SPHERICAL** (degrees, x=longitude Greenwich, y=latitude N; CCM=central conformal Mercator / QC=quasi-cartesian)
- nested run = coarse grid 와 동일 좌표계. spherical regular grid 는 E-W/N-S 정렬(alpc=alpinp=alpfr=0)
- REPEATING (academic, x방향 주기경계; SETUP 불가, regular only)

## 2. §4.5.1 Computational grid

### 2.1 CGRID (required)
```
CGRID <-> REGular [xpc][ypc][alpc][xlenc][ylenc][mxc][myc] | CURVilinear [mxc][myc] (EXCeption [xexc][yexc]) | UNSTRUCtured> <-> CIRcle | SECtor [dir1][dir2]> [mdc][flow][fhigh][msc]
```
- **REGULAR**(uniform rect, xpc/ypc origin, alpc=0 방향, xlenc/ylenc 길이, mxc/myc mesh 수=격자점−1) / **CURVILINEAR**(READGRID COOR, EXCEPTION xexc 무시점) / **UNSTRUCTURED**(READGRID UNSTRUC, [[swan-tech-ch8-unstructured-grid-scheme]])
- **spectral**: **CIRCLE default**(전원, Δθ=360/mdc) / SECTOR [dir1][dir2](Δθ=(dir2−dir1)/mdc). ⚠ **quadruplet(GEN3) 시 SECTOR는 spectrum sector보다 양쪽 30° 넓게** (아니면 부정확)
- `mdc` = θ mesh 수 (**최소 3/quadrant**), `flow`/`fhigh` = 최저/최고 주파수(Hz), `msc` = 주파수 수−1 (**최소 4**, **logarithmic** $f_{i+1}=\gamma f_i$, $\Delta f/f = \gamma−1$, msc=log(fhigh/flow)/log(1+Δf/f))
- nested 시 geographic·spectral range/resolution 이전 run 과 달라도 됨 (밖은 0)

### 2.2 READGRID
```
READGRID COORdinates [fac] 'fname' [idla] [nhedf] [nhedvec] <FREE|FORMAT|UNFORMAT>
READGRID UNSTRUCtured <-> TRIAngle | EASYmesh | ADCirc> 'fname'
```
curvilinear 좌표 / unstructured mesh (Triangle·Easymesh·ADCIRC fort.14, [[swan-grid-readers]]).

## 3. §4.5.2 Input grids and data

### 3.1 INPGRID
```
INPgrid <BOTtom|WLEVel|CURrent|FRiction|WInd|ICE|...> <-> REGular [xpinp][ypinp][alpinp][mxinp][myinp][dxinp][dyinp] | CURVilinear [stagrx][stagry][mxinp][myinp] | UNSTRUCtured> (EXCeption [excval]) (NONSTATionary [tbeginp][deltinp]<SEC|MIN|HR|DAY>[tendinp])
```
입력 데이터(수심 BOTTOM, 수위, 유속, friction, wind, ice 등)별 격자 정의. REGULAR(xpinp origin, alpinp 방향, mxinp/myinp/dxinp/dyinp) / CURVILINEAR(stagrx/y stagger) / UNSTRUCTURED. NONSTATIONARY (시간 tbeginp~tendinp, deltinp 간격).

### 3.2 READINP
```
READinp <BOTtom|WLEVel|CURrent|FRiction|WInd|...> [fac] 'fname' [idla] [nhedf] [nhedt] [nhedvec] <FREE|FORMAT|UNFORMAT>
```
`fac` = 곱 factor, `idla` = layout(1-6 격자 방향/순서), `nhedf/nhedt` = header 줄 수.

### 3.3 WIND / ICE (constant)
```
WIND [vel] [dir]        ! 10m 풍속(m/s) + 방향(deg, NAUTICAL/CARTESIAN)
ICE  [aice] [hice]      ! ice fraction + thickness
```
공간변화 시 INPGRID WIND/ICE + READINP. [[swan-tech-ch2-sources-sinks]] wind input.

## 4. §4.5.3 Boundary and initial conditions

### 4.1 BOUND SHAPESPEC (스펙트럼 형상)
```
BOUnd SHAPespec <-> JONswap [gamma] | PM | GAUSs [sigfr] | BIN> <-> PEAK | MEAN> <-> DSPR POWer | DEGRees>
```
경계 parametric spectrum 형상: **JONSWAP**(default gamma=3.3)/Pierson-Moskowitz/Gaussian/BIN, peak vs mean frequency, directional spread (power vs degrees).

### 4.2 BOUNDSPEC (경계 스펙트럼 지정)
```
BOUNDSPEC <SIDE <N|NW|...>|SEGMENT ...> <CONSTANT|VARIABLE> <PAR [hs][per][dir][dd]|FILE 'fname'>
```
- side/segment 별 parametric(PAR: Hs/period/dir/directional spread dd) 또는 file 스펙트럼. 여러 BOUNDSPEC 로 다측 경계 (한 command = 한 side/segment)

### 4.3 BOUNDNEST1/2/3 (nesting)
```
BOUNDNEST1 NEST 'fname' <CLOSED|OPEN>       ! SWAN coarse → nested
BOUNDNEST2 WAMNEST 'fname' ...               ! WAM
BOUNDNEST3 WWIII 'fname' ...                 ! WAVEWATCH III
```
대모델(SWAN/WAM/WW3) 경계 스펙트럼을 nested run 에 (CGRID 먼저). 1D 불가.

### 4.4 INITIAL
```
INITial <-> DEFAULT | ZERO | PAR [hs][per][dir][dd] | HOTStart <MULTiple|SINGle> 'fname' <FREE|UNFormatted>>
```
- **DEFAULT** = 2nd-gen first guess (stationary) / Kahma-Calkoen growth (nonstat, [[swan-tech-ch4-5-bc-2d-setup]] §A.4) / **ZERO**(무파) / **PAR**(균일 parametric) / **HOTSTART**(이전 run hotfile, MPI MULTIPLE/SINGLE)

## 5. command 순서 (§4.2)

`PROJECT → SET → MODE → COORDINATES → CGRID → (READGRID) → INPGRID/READINP (각 입력) → WIND/ICE → BOUND/BOUNDSPEC/BOUNDNEST → INITIAL → [physics] → [numerics] → output locations → output quantities → COMPUTE → STOP`

## 6. 한계

- INPGRID/READINP의 idla(1-6 layout)·NONSTATIONARY time format 정밀 옵션 + BOUNDSPEC SEGMENT 좌표 지정 detail 은 요약 — swanuse p.36-55 직접 또는 후속.
- COMPUTE/HOTFILE/STOP + NUMERIC/PROP + output(FRAME/BLOCK/TABLE/QUANTITY) → [[swan-command-numerics-output-reference]].

## 7. 연결

- [[swan-command-physics-reference]] — §4.5.4 physics (GEN/WCAPPING/...)
- [[swan-command-numerics-output-reference]] — §4.5.5-4.7 numerics/output/lock-up
- [[swan-documentation-stack]] — 4 docs + 57 command 목록
- [[swan-grid-readers]] — READGRID UNSTRUCTURED (ADCIRC/Triangle/Easymesh)
- [[swan-tech-ch4-5-bc-2d-setup]] — BC/IC 이론 (Ch 4)

---
title: "Delft3D D-Flow FM 격자생성(RGF)·유틸리티 — spline→곡선격자·transfinite interpolation·orthogonalization SOR"
model: Delft3D
component: dflowfm/grid-generation(RGF)+utils
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/). dflowfm_rgf의 tranfn2.f90(transfinite interpolation 본체), orthogrid.f90/ortsor.f90/sor.f90/atppar.f90(orthogonalization 외/중/내 iteration + 계수행렬), splrgfr.f90/makespl.f90/makes.f90(spline→곡선격자), bndsmt.f90(경계 스무딩), attractrepulse.f90, mappro.f90/mapprojections.f90(좌표투영), refine.f90; dflowfm_data의 m_orthosettings.f90/m_gridsettings.f90(파라미터 정의); dflowfm_utils의 tridag.f90, rest_f90/dlinedis2.f90/ludcmp.f90/pol2curvi.f90/m_snappol.f90 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_overview.md
  - models/Delft3D/README.md
---

# Delft3D D-Flow FM 격자생성(RGF)·유틸리티

> RGFGRID 계열 곡선격자 생성·직교화·유틸리티. (경로: `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_rgf/` + `dflowfm_utils/`)

D-Flow FM 커널 안에는 구 RGFGRID(Deltares 곡선격자 에디터)에서 이식된 격자생성·직교화 루틴이 `dflowfm_rgf/`(~100 파일)에 들어 있고, 수치·기하·I/O 유틸이 `dflowfm_utils/`(70 파일 + `rest_f90/` 95 파일)에 들어 있다. 본 노트는 **곡선격자 생성 파이프라인**(spline→grid, transfinite interpolation), **직교화(orthogonalization) 솔버**, 좌표투영, 핵심 수치 유틸을 다룬다. 비정형(unstructured) net 생성·플로우 커널은 별도 노트 [[delft3d_dflowfm_kernel_scheme]] 참조.

> GUI 주의: `dflowfm_kernel/src/dflowfm_gui/` 는 342개 `.[fF]90` 파일의 S-tier 인터랙티브 GUI(Interacter 기반 화면·메뉴·플롯)다. 본 노트는 **존재만 언급하고 미검수**한다.

---

## 1. 곡선격자 생성 파이프라인

### 1.1 Spline → 곡선격자: `splrgfr.f90`

`SPLRGFR()` 는 사용자가 그린 spline 집합(`xsp,ysp` in `m_splines`)을 받아 곡선격자(`xc,yc` in `m_grid`)를 만드는 최상위 루틴이다.

흐름 (`dflowfm_rgf/splrgfr.f90`):
1. `increasegrid(mfac*mcs, nfac*mcs)` 로 격자 배열 확장 (`splrgfr.f90:88`).
2. `SECTR(...)` — spline 교차(snijpunt) 검출 + spline을 m/n 방향으로 분류, 교차점 좌표 `TIJ`·블록 인덱스 `MN12` 생성 (`splrgfr.f90:124-127`). SECTR은 "한 spline이 m·n 양방향이면 spaghetty" / "두 spline이 한 번 넘게 교차하면 modify splines" 에러를 낸다 (`sectr.f90:144`, `sectr.f90:175`).
3. 각 spline에 대해 `MAKESPL(...)` 로 spline 위 등간격(arc-length) 격자점 보간 → 격자 외곽선(coarse grid edges) 채움 (`splrgfr.f90:139-176`). `I1<=NUMI` 면 가로(m), 아니면 세로(n) spline.
4. **블록별 내부 채움**: 각 (I,J) 블록의 4변(`X1..X4,Y1..Y4`)을 모아 `TRANFN2(...)` 로 transfinite interpolation → 내부 격자점 `XH,YH` 생성 후 미정의(`XYMIS`) 셀에만 채움 (`splrgfr.f90:197-257`, 호출 `splrgfr.f90:242`).
5. 결과 차원 `MC=MCR, NC=NCR` 설정 (`splrgfr.f90:258-259`).

격자 크기 보호: `MFAC>1000` 이면 "reduce MFAC and NFAC to about < 50" 에러 (`splrgfr.f90:83-86`); 생성 후 `MMAX-1`/`NMAX-1` 초과 시 "TOO MANY GRIDPOINTS" (`splrgfr.f90:180-191`).

### 1.2 Transfinite interpolation: `tranfn2.f90`

`TRANFN2(X1..X4, Y1..Y4, IMX, MX, NX, XRH, YRH)` 가 4변 경계로부터 내부 격자를 채우는 **거리가중 transfinite interpolation** 본체다 (`dflowfm_rgf/tranfn2.f90:43`). 헤더 주석(네덜란드어, verbatim):

```
!     1,2    VERTICALEN
!     3,4    HORIZONTALEN
!     D1234  REL. LIJN COORDINAAT 0-1
!     SI,SJ  REL. VELD COORDINAAT 0-1
!     TI,TJ  SCHATTING KOORDELENGTES
!     W1234  VELD WEEGFACTOR
```
(`tranfn2.f90:73-79`)

알고리즘:
- 4변의 누적상대거리 `D1..D4`(0~1)와 전체길이 `T1..T4` 를 `ABREL2` 로 계산 (`tranfn2.f90:106-109`).
- 인덱스가중 `RI=(I-1)/MFAC`, `RJ=(J-1)/NFAC` 와 거리가중 `SI,SJ` 혼합:
  $$S_I(i,j) = (1-R_J)D_3(i) + R_J\,D_4(i), \quad S_J(i,j) = (1-R_I)D_1(j) + R_I\,D_2(j)$$
  (`tranfn2.f90:116-117`).
- 1차 추정(boundary blending): 정규화 가중 `W1,W2` 로
  $$X_{RH} = [(1-S_I)X_1 + S_I X_2]\,W_1 + [(1-S_J)X_3 + S_J X_4]\,W_2$$
  (`tranfn2.f90:151-154`). 가중 `W1,W2`는 i/n 방향 총 코드길이비 `ATPF` 로부터 정규화 (`tranfn2.f90:124-130`).
- 그 후 셀별 `atpI/atpJ`(코드길이 종횡비) 계산 후 `ITIN` 회 **Laplacian-style smoothing 반복**으로 내부점 재배치 (`tranfn2.f90:179-215`). 각 점은 4-이웃의 가중평균:
  $$X_{i,j} = \frac{w_1 X_{i-1,j} + w_1' X_{i+1,j} + w_2 X_{i,j-1} + w_2' X_{i,j+1}}{w_1+w_1'+w_2+w_2'}$$
  (`tranfn2.f90:200-206`).

반복 횟수는 `m_orthosettings`의 `ITIN`(기본 25) 사용 (`tranfn2.f90:50`, `m_orthosettings.f90:39`).

### 1.3 격자 세분: `refine.f90` / `derefine.f90`

`REFINE(M1,N1,M2,N2,NUM)` 는 기존 격자를 `MFAC`/`NFAC` 배로 보간 세분 (`refine.f90:40`). 새 차원 계산 `MCR = MC - NRM + 1 + NRM*MFAC - 1` (`refine.f90:65-66`), `ISITU` 로 노드분류 후 `GETSPL2`(스플라인 2차계수) → `XYSPLN`(스플라인 보간 세분) 적용 (`refine.f90:76-90`). `DEREFINE`(`derefine.f90:40`)는 역연산(격자 솎기).

---

## 2. 직교화 (Orthogonalization)

곡선격자를 직교(서로 직각으로 만나는 격자선)에 가깝게 만드는 elliptic smoother. 3중 중첩 반복: **ATP(외) → BND(경계) → IN(내부)**.

### 2.1 최상위: `orthogrid.f90`

`ORTHOGRID(M1,N1,M2,N2)` (`dflowfm_rgf/orthogrid.f90:45`):
- `SAVEgrd()` 로 백업, `ISITU()` 로 노드분류 (`orthogrid.f90:87`, `:103`).
- 구면격자(`JSFERIC==1`)면 `MAKEF` 로 위도보정 (`orthogrid.f90:108-110`).
- `GETSPL2` 로 x,y의 i·j 방향 2차 스플라인계수 `XI2,XJ2,YI2,YJ2` 사전계산 (`orthogrid.f90:112-117`) — 경계 재투영에 사용.
- **외부 반복** `do IT=1,ITATP` (`orthogrid.f90:129`): 매 반복마다
  1. `ATPPAR(...)` 로 직교화 계수행렬 `A..E, ATP` 재계산 (`orthogrid.f90:139`),
  2. `FIXDDBOUNDARIES()` 로 domain-decomposition 경계 고정 (`orthogrid.f90:143`),
  3. `ORTSOR(...)` 로 SOR + 경계스무딩 수행 (`orthogrid.f90:148`).
- 첫 반복만 `JDLA=1`(distance reallocation) (`orthogrid.f90:131-133`). 완화계수 `RJAC=0.9` (`orthogrid.f90:125`).

### 2.2 계수행렬: `atppar.f90`

`ATPPAR(X,Y,M1,N1,M2,N2,ATP,A,B,C,D,E)` 가 5점 elliptic 스텐실 계수를 셀 코드길이로부터 만든다 (`dflowfm_rgf/atppar.f90:44`). 헤더 verbatim:

```
!     STUURPARAMETERS (1,MC-1)
!     4 3             (1,NC-1)
!     1 2       D1: (12+43)/2   D2:(14 + 23)/2
!     En vul ATP in celmiddens
```
(`atppar.f90:65-68`)

- 셀 4변 평면거리 `D12,D34,D14,D23`(`PLANEDISTANCE`)로 `A=(D12+D34)/2`(m방향), `B=(D14+D23)/2`(n방향) (`atppar.f90:100-105`).
- `SOMDIST` 로 행/열 합산 후 정규화. **smoothing↔ortho 혼합**: `AF=1-ATPF`, `ATP = ATPF*ATP_ortho + AF*A` (`atppar.f90:134-141`) — `ATPF`(기본 0.975)가 1에 가까울수록 순수 직교화, 0이면 순수 스무딩 (`m_orthosettings.f90:42`).
- 종횡비 `ATP(i,j)=B/A` (`atppar.f90:152`).
- 최종 5점 스텐실: 내부점(`IJC==10`)에만 (`atppar.f90:165-187`)
  $$A=ATP_{i,j-1}+ATP_{i,j},\;B=ATP_{i-1,j-1}+ATP_{i-1,j},\;C=\tfrac1{ATP_{i-1,j}}+\tfrac1{ATP_{i,j}},\;D=\tfrac1{ATP_{i-1,j-1}}+\tfrac1{ATP_{i,j-1}}$$
  $$E=-(A+B+C+D)$$
  (`atppar.f90:179-184`).

### 2.3 SOR 솔버: `sor.f90`

`SOR(A,B,C,D,E,U,RJAC,M1,N1,M2,N2)` — Chebyshev-가속 SOR로 elliptic 격자방정식 1성분(x 또는 y)을 푼다 (`dflowfm_rgf/sor.f90:43`). `MAXITS=ITIN`(기본 25) (`sor.f90:70`).
- 잔차 `RESID = A·U_{i+1,j}+B·U_{i-1,j}+C·U_{i,j+1}+D·U_{i,j-1}+E·U_{i,j}`, 갱신 `U=U-ω·RESID/E`, 내부점(`IJC==10`)만 (`sor.f90:80-82`).
- **Chebyshev ω 가속** (Numerical Recipes 방식): 첫 스텝 `ω=1/(1-½·RJAC²)`, 이후 `ω=1/(1-¼·RJAC²·ω)` (`sor.f90:87-91`).

### 2.4 외부 래퍼: `ortsor.f90`

`ORTSOR(...)` 가 `do I=1,ITBND`(경계반복, 기본 25) 동안 `SOR(...,XR)` + `SOR(...,YR)` + `BNDSMT(...)` 를 호출 (`dflowfm_rgf/ortsor.f90:74-100`). 즉 외부=`ITATP`(2) × 경계=`ITBND`(25) × 내부=`ITIN`(25) 의 3중 반복 구조 (`m_orthosettings.f90:37-39`).

### 2.5 경계 스무딩: `bndsmt.f90`

`BNDSMT(XR,YR,XI2,YI2,XJ2,YJ2,ATP,...)` 가 경계·내부 노드를 스플라인 위로 재투영 (`dflowfm_rgf/bndsmt.f90:45`). 헤더 verbatim:

```
!     RANDPUNTEN OF INTERNE PUNTEN
!     TERUGZETTEN OP DE SPLINE TUSSEN OUDE POSITIE OP RAND (BFAC = 0)
!     EN PROJECTIE OP SPLINE VAN NABIJ PUNT (BFAC = 1)
```
(`bndsmt.f90:86-88`) — `BFAC=0`(`m_gridsettings`)이면 즉시 return(스무딩 안 함) (`bndsmt.f90:99-101`). `BFAC=1`이면 인접 내부점의 스플라인 투영으로 경계점을 끌어당김. 노드코드 `IJC`(11/14=경계 시작, 1/3/5/6=내부 가로/세로) 로 경계 세그먼트 식별 (`bndsmt.f90:111-120`).

---

## 3. 격자 변형 도구

### 3.1 끌어당김/밀어냄: `attractrepulse.f90`

`ATTRACTREPULSE(XH,YH,X,Y,...,JA)` — 격자선을 한 위치로 끌어(JA>0)/밀어(JA<0)내는 인터랙티브 변형 (`dflowfm_rgf/attractrepulse.f90:44`). 영향반경 `RSX = dist(viewport)/6`, 거리감쇠 `FR=(RSX-RN)/RSX`, 변위 `DXY = RFAC*TEKEN*FR*JANU*DXY0`(`RFAC` in `m_gridsettings`) (`attractrepulse.f90:73-110`). 구면이면 `DXY = RD2DG*DXY/RA` (`attractrepulse.f90:111-113`).

### 3.2 polygon→곡선격자: `rest_f90/pol2curvi.f90`

`pol2curvi` 헤더 verbatim (`dflowfm_utils/rest_f90/pol2curvi.f90:33-40`):
```
!> generate curvilinear mesh in polygon, based on three polygon nodes that define two sides 1-2 and 2-3
!>    the third side 3-4 is defined by the polygon nodes by matching the number of nodes with side 1-2
!>    ja4=1: the fourth side is also taken from the polygon...
!>    ja4=0: the fourth side is linearly interpolated between nodes 1 and 4...
```
폴리곤 3노드(2변)로 곡선격자를 만든다. 삼각형 변형 `pol2curvi_tri.f90` 도 있음.

---

## 4. 좌표투영 (Map projections)

### 4.1 디스패처: `mappro.f90`

`MAPPRO(XX,YY,XG,YG,IZONE,NZONE,IHEM,ITYPE,JSFERIC,INIA)` 가 단일점을 투영/역투영 (`dflowfm_rgf/mappro.f90:48`). 초기화 시 `setellipse(3)` = WGS84 (`mappro.f90:67-69`). `ITYPE` 코드(verbatim 인접 주석):
- `0`=ROTATIE/TRANSLATIE, `1`=UTM, `2`=Amersfoort, `3`=RD(Parijs), `4`=MERCATOR, `-1`=AFFINE.
- `JSFERIC==0`(Cartesisch→Spherisch): `TRAROT`/`UTMGEO2`/`RDGEO`/`MERCGEO`/`AFFINE` (`mappro.f90:85-98`).
- `JSFERIC==1`(Spherisch→Cartesisch): `GEOUTM`/`GEORD`/`GEOMERC`/`AFFINE` (`mappro.f90:99-110`).

### 4.2 배치 적용: `mapprojections.f90`

`MAPPROJECTIONS(IT,JA)` 가 격자(`XC,YC`)·net(`XK,YK`)·landboundary·polygon·samples·splines 전체를 일괄 투영하고 `JSFERIC` 토글 (`dflowfm_rgf/mapprojections.f90:43`, 토글 `:190`). 헤더 verbatim `! ITYPE = 1 ! 0 = ROTATIE/TRANSLATIE, 1 = UTM, 2=RD, 3 = PARIJS, 5 = AFFINE` (`mapprojections.f90:74`).

좌표계 변환 보조: `bessel2wgs84.f90`/`wgs842bessel.f90`(네덜란드 Bessel↔WGS84), `geoutm.f90`/`utmgeo2.f90`(UTM), `loc2spher`/`spher2loc`(rest_f90, 국지↔구면).

---

## 5. 스플라인 수치 (Spline machinery)

### 5.1 등간격 스플라인 격자: `makespl.f90`

`MAKESPL(T,X,Y,imax,N,NT,MNFAC,XH,YH,KMAX,TT,H)` 헤더 verbatim (`dflowfm_rgf/makespl.f90:33-45`):
```
!>   generate grid between fixed points on a spline that itself is defined by control points
!>     in:  t(Nt) fixed points on spline
!>          MNfac number of grid intervals between fixed points
!>          H     significant height, where the grid should be equidistant (>0) or disable (<=0)
```
1. `MAKES` 로 x,y 스플라인 + 누적호장(arc-length) `S` 스플라인 생성 (`makespl.f90:68`).
2. `MAKESSQ` 로 고정점 사이를 `MNFAC` 등분 호장좌표 `SSQ` 생성 (`makespl.f90:73`).
3. **단조성 보정**: `SSQ`가 비단조면 인접평균으로 평활(`SSQ(K)=0.5(SSQ(K-1)+SSQ(K+1))`) (`makespl.f90:81-94`).
4. `GETXY` 로 각 호장좌표의 (x,y) 복원 (`makespl.f90:100-102`).

`H>0`(significant height) 이면 곡률적응 메싱(curvature adapted meshing)을 위해 등간격이 되도록 보정 (`makespl.f90:60`).

### 5.2 호장+스플라인: `makes.f90`

`MAKES(X,Y,X2,Y2,T,S,S2,imax,N,NT,H)` — `SPLINXY`(x,y의 2차도함수) → 각 고정점의 누적거리 `GETDIS` → 거리배열의 스플라인 `SPLINE` (`dflowfm_rgf/makes.f90:49-54`). 즉 매개변수 → 물리거리 → 좌표의 2단 스플라인.

관련: `splinxy.f90`/`splintxy.f90`(2D 스플라인), `xyspln.f90`(격자 스플라인 보간), `getspl2.f90`(격자 전체 2차계수), `checkspl.f90`(스플라인 검증).

---

## 6. 격자 I/O (RGF 포맷)

- `reagrid.f90` — RGFGRID `.grd` 격자파일 읽기 (`dflowfm_rgf/reagrid.f90`).
- `wrirgf.f90` — `.grd` 격자파일 쓰기 (`dflowfm_rgf/wrirgf.f90`).
- `readarcinfo.f90`/`wridep.f90` — ArcInfo / depth 파일.
- `gridtonet.f90` — 곡선격자 → 비정형 net 변환 (`dflowfm_rgf/gridtonet.f90`) — RGF와 FM 비정형 커널의 다리.

⚠ 위 I/O 파일들은 헤더·존재만 확인(file 인용은 디렉토리 목록 기준). 내부 포맷 상세는 source-needed.

---

## 7. 핵심 수치 유틸 (`dflowfm_utils/`)

### 7.1 선형대수
- `tridag.f90`: 표준 Thomas 삼중대각 솔버. `bet=b(1); u(1)=d(1)/bet; ...` 전진/후진 소거, pivot 보호 `accur=1e-15` (`dflowfm_utils/tridag.f90:42-62`).
- `rest_f90/ludcmp.f90`: LU 분해 `LUDCMP(A,N,NP,INDX,D,JAPARALLEL)` (Crout, 부분피벗) (`dflowfm_utils/rest_f90/ludcmp.f90:43`).
- 선형 솔버 래퍼(플로우용, 본 노트 범위 밖): `solve_guus.F90`/`solve_petsc.F90`/`solve_parms.F90`/`solve_jacobi.f90`/`saadf.F90`(SAAD ILU) — 비정형 행렬 솔버. 상세는 [[delft3d_dflowfm_kernel_scheme]] / source-needed.

### 7.2 기하 (rest_f90)
- `dlinedis2.f90`: 점→선분 최단거리 `dLINEDIS2(X3,Y3,X1,Y1,X2,Y2,JA,DIS,XN,YN,rl)`. 투영 파라미터 `RL=(X31·X21+Y31·Y21)/R2`, 0≤RL≤1 이면 `JA=1`(수선 내부), 발`(XN,YN)` 계산 (`dflowfm_utils/rest_f90/dlinedis2.f90:35`, 본체 `:51-67`). `jasfer3D` 시 3D 구면 카르테시안으로 정확 계산 (`:69-101`). 변형: `dlinedis3.f90`, `dcross.F90`(선분 교차).
- `m_snappol.f90`: `snappol`(폴리곤→메시 스냅) / `snappnt`(점→flow node 스냅) (`dflowfm_utils/rest_f90/m_snappol.f90:44`, `:266`).
- `m_crspath.f90`: cross-section path(관측단면이 가로지르는 flow link 경로).
- `rmdouble.f90`(중복점 제거), `loc2spher`/`spher2loc`(좌표변환).

### 7.3 샘플/폴리곤 I/O (rest_f90)
- `reasam.f90`(샘플 읽기), `realan.f90`(landboundary), `reapol_nampli.f90`/`reaarc.f90`(폴리곤·ArcInfo), `read_samples_from_geotiff.F90`/`read_samples_from_dem.f90`/`read_samples_from_arcinfo.f90`(DEM·GeoTIFF·ArcInfo 수심 샘플), `wrildb.f90`(landboundary 쓰기).
- `find_crossed_links_kdtree2.f90`: kdtree2 기반 link 교차 검색(폴리곤 클리핑 가속) (`dflowfm_utils/rest_f90/find_crossed_links_kdtree2.f90`).

### 7.4 파일·메시지·시스템 인프라
- `unstruc_files.f90`: 열린 파일 레지스트리. `reg_file_open`/`reg_file_close` 로 파일명 추적 (`dflowfm_utils/unstruc_files.f90:63`, `:91`).
- `unstruc_messages.f90`: 메시지/에러 핸들러 `unstruc_errorhandler(level,message)`, 메시지 버퍼 (`dflowfm_utils/unstruc_messages.f90:35`, `:60`).
- `unstruc_errorhandler.F90`, `unstruc_startup.f90`, `unstruc_ini.f90`(MDU 외 설정), `init_openmp.F90`(OpenMP 스레드 초기화), `mormerge_mpi.F90`(morphology merge MPI — [[delft3d_sediment_morphology]] 연계).
- `m_filez.f90`/`filez.F90`: 저수준 파일 유틸(`NEWFIL` 등, `splrgfr.f90:119`에서 사용).

### 7.5 통계·캘리브레이션
- `statisticsini/newstep/onemorepoint/finalise.f90` + `temporal_statistics.f90`: 시계열 통계(평균/min/max 누적).
- `calibration.f90`/`calibration_init.f90`/`calibration_update.f90`: 캘리브레이션 계수(예: 마찰) 클래스/필드 적용.

### 7.6 GUI/디스플레이 잔여 (미검수)
`unstruc_display.F90`, `unstruc_colors.f90`, `unstruc_opengl.F90`, `unstruc_opengis.f90`, `unstruc_shapefile.F90`, `scherm.F90`, `tekship.f90`, `step_to_screen.f90` 등은 화면출력/GIS 연동으로 GUI 성격 — 존재만 기록, 미검수.

---

## 8. 설정 파라미터 정리

`dflowfm_data/m_orthosettings.f90` (직교화·평활 공통, 곡선격자+비정형 net 겸용):

| 변수 | 기본값 | 의미 | file:line |
|---|---|---|---|
| `ITATP` | 2 | 외부(ATP) 반복 수 | `m_orthosettings.f90:37` |
| `ITBND` | 25 | 경계 반복 수 (ITATP 내부) | `:38` |
| `ITIN` | 25 | 내부 반복 수 (ITBND 내부; SOR/transfinite 평활도 사용) | `:39` |
| `JAPROJECT` | 1 | 노드를 경계로 재투영 (2=전체,1=net경계만,0=안함) | `:41` |
| `ATPF` | 0.975 | 스무딩↔직교화 혼합비 (1=순수 ortho) | `:42` |
| `circumormasscenter` | 1.0 | 1=외심, 0=무게중심 (비정형 net) | `:44` |
| `adapt_method` | 1 | 메시 적응 0=Winslow,1=호장,2=harmonic map | `:46` |
| `ortho_pure` | 0.5 | curvi-like(0)↔pure(1) 직교화 | `:50` |

`dflowfm_data/m_gridsettings.f90` (곡선격자 생성 전용):

| 변수 | 기본값 | 의미 | file:line |
|---|---|---|---|
| `MFAC` | 2000 | m방향 세분계수 | `m_gridsettings.f90:39` |
| `NFAC` | 40 | n방향 세분계수 | `:40` |
| `ITSMO` | 10 | 격자 평활 내부 반복 | `:41` |
| `BFAC` | 1.0 | 경계스무딩 강도(0=안함,1=완전투영) | `:45` |
| `CSMO` | 0.5 | 평활계수 | `:45` |
| `KEEPSTARTDIR` | 1 | 시작방향 유지 | `:47` |
| `pil_rad/pil_x/pil_y` | 0.0 | pillar(원형 교각) 격자 | `:53-55` |

---

## 9. 요약: 곡선격자 파이프라인 한눈에

```
splines (m_splines)
   └─ SPLRGFR (splrgfr.f90)
        ├─ SECTR        : spline 교차·분류 (sectr.f90)
        ├─ MAKESPL      : spline 위 등간격 외곽선 (makespl.f90 → makes.f90)
        └─ TRANFN2      : 블록 내부 transfinite interp (tranfn2.f90)
   → grid (xc,yc in m_grid)
        └─ ORTHOGRID (orthogrid.f90)        [직교화]
             repeat ITATP:
               ATPPAR  : elliptic 계수행렬 (atppar.f90, ATPF 혼합)
               ORTSOR  : repeat ITBND:
                            SOR x, SOR y    : Chebyshev SOR (sor.f90, ITIN)
                            BNDSMT          : 경계 스플라인 투영 (bndsmt.f90)
   → REFINE/DEREFINE (격자 세분/솎기)
   → gridtonet.f90 → 비정형 net (→ FM 플로우 커널)
```

전 과정은 인터랙티브 GUI(`dflowfm_gui/`, 342파일, 미검수)에서 호출되거나 스크립트(net 생성 API)로 구동된다.

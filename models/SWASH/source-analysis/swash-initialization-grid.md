---
title: "SWASH 초기화·격자·밀도/기하 — SwashInit/InitCond/InitSteady/CompGrid/Geometrics/LayerIntfaces/Density/AmbCurrent"
model: SWASH
component: src (initialization / grid / geometry)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashInit.ftn90(기본값 블록 92-552행), SwashInitCond.ftn90(INIT 명령 파서 125-513), SwashInitSteady.ftn90(Chezy 90-238), SwashInitCompGrid.ftn90(KGRPGL/SWDECOMP 94-377), SwashInitCompUgrid.ftn90(offset/allocate 83-164), SwashInputGrid.ftn90(INPGRID 파서 149-406), SwashInputField.ftn90(READINP/INAR2D 111-446), SwashDensity.ftn90(Eckart 식 84-181), SwashGeometrics.ftn90(metric tensor 76-332), SwashLayerIntfaces.ftn90(sigma 76-192), SwashLayUIntfaces.ftn90(unstr 72-118), SwashAmbCurrent.ftn90(contravariant 81-666) file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 초기화·격자·밀도/기하

> 모델 기동 시 기본값 세팅 → 계산격자(구조/비구조) 셋업 → 입력장·초기조건·정상상태 흐름 → 기하 metric·sigma layer interface·밀도(상태방정식)·ambient current 까지의 전처리 체인. (경로: raw/source_code/swash/src/)

이 노트가 다루는 12개 파일은 SWASH의 **전처리(pre-processing) 단계** 전반을 구성한다. 시간적분 루프(SwashComputFlow 등)가 시작되기 전에 호출되어 모든 격자·기하·초기 상태 배열을 확정한다.

---

## 1. 전체 흐름 개관

| 단계 | 파일 | 역할 |
|---|---|---|
| 기본값 세팅 | `SwashInit.ftn90` | 전 common 변수·물리상수·파라미터 디폴트 + output 변수 메타데이터 등록 |
| 입력격자 파싱 | `SwashInputGrid.ftn90` | `INPGRID` 명령 — 입력장의 frame/curv/unstruc 격자 기하 |
| 입력장 읽기 | `SwashInputField.ftn90` | `READINP` 명령 — bottom/current/wind/sal/temp/sed/... 배열 적재 |
| 계산격자(구조) | `SwashInitCompGrid.ftn90` | KGRPGL 인덱스 테이블·도메인 분할·s1/u1/v1 할당 |
| 계산격자(비구조) | `SwashInitCompUgrid.ftn90` | offset/검사·ncells/nfaces 기반 할당 |
| 기하량 | `SwashGeometrics.ftn90` | 공변기저·metric tensor $g_{11},g_{22}$·Jacobian |
| 초기조건 | `SwashInitCond.ftn90` | `INIT` 명령 — CON/ZERO/STEADY/HOTSTART |
| 정상상태 | `SwashInitSteady.ftn90` | Chezy 균일류 초기 유속 |
| layer interface | `SwashLayerIntfaces.ftn90` / `SwashLayUIntfaces.ftn90` | sigma 좌표 층 경계·층 두께 (구조/비구조) |
| 밀도 | `SwashDensity.ftn90` | Eckart 상태방정식 |
| ambient current | `SwashAmbCurrent.ftn90` | 배경류를 contravariant 성분으로 변환·보간 |

모든 서브루틴은 Delft TU(EFM Section) GPL v3 헤더와 `Programmers: The SWASH team` (또는 개별 저자)을 공유한다. `SwashAmbCurrent`만 저자가 `Dirk Rijnsdorp`, 2023 July 신설 (`SwashAmbCurrent.ftn90:32-36`).

---

## 2. SwashInit — 전역 기본값 + 버전

Purpose 주석: `Initializes several variables and arrays` (`SwashInit.ftn90:38-40`).

거대한 단일 subroutine으로, 대부분이 common-block 변수에 디폴트를 대입하는 코드다(전문 전사 생략). 핵심 anchor:

- **버전**: `VERNUM = 12.01` (`SwashInit.ftn90:79`). 이 위키가 v12.01 기준임을 코드가 확정한다.
- **초기화 진입점**: `call OCPINI ( 'swashinit', .true., inerr )` (`:85`) — Ocean Pack 공통 초기화.
- **물리상수**: `grav = 9.813`, `rhoa = 1.205`, `dynvis = 1.e-3`, `vonkar = 0.4` (`:135-139`). 단, `rhow = -999.` 로 두고 주석 `reference density (subject to change)` (`:136`) — 나중에 결정.
- **건습(dry) 임계값**: `epsdry = 5.e-5`, `epshu = 1.e-3`, `epsuf = 1.e-8` (`:121-123`).
- **밀도 파라미터 디폴트**: `idens=0`, `tempw=14.`, `salw=31.`, `rhos=2650.`, `lmixt=.true.` (`:143-147`) — SwashDensity가 쓰는 상수온도/염분.
- **구면좌표**: `kspher=0`(직교), `rearth=2.e7/pi`, `lendeg=2.e7/180.` (`:158-161`) — SwashGeometrics의 위도 보정에 쓰임.
- **계산격자 디폴트**: `optg=1`(직사각), `mxc=0,myc=0`, `oned=.false.`, `kmax=1`, `kpmax=1`, `lsubg=.false.` (`:172-189`).
- **grid offset**: `xoffs=0., yoffs=0., lxoffs=.false.` (`:193-195`) — CompGrid/CompUgrid가 첫 좌표를 기준으로 채운다.
- **repeating grid**: `lreptx=.false., lrepty=.false.` (`:199-200`) — AmbCurrent의 주기 동기화 분기 조건.
- **초기조건 디폴트**: `tkeini=1.e-7`, `epsini=1.e-7`, `restrt=.false.`, `instead=.false.` (`:215-219`) — `instead`는 STEADY 모드 플래그.
- **입력격자 루프**: `do i = 1, numgrd` 로 igtype/xpg/.../`lflgrd(i)=.true.`/`lstag(i)=.false.`/`excfld(i)=-1.e20`/`ifllay(i)=1` 초기화 (`:249-270`).
- **ambient current 디폴트**: `iamb=0, uamb=0., vamb=0., eamb=0.` (`:359-362`).
- **transport 디폴트**: `itrans=0, lsal=0, ltemp=0, lsed=0, ltrans=0` (`:366-370`) — InputField가 SAL/TEMP/SED 읽을 때 증가시킴.
- **이산화 디폴트**: `jhk=1 ! RK3`, `dpsopt=2`, `corrdep=.true.` (`:393-395`).

`:518` 이후 (`properties of output variables`)부터 끝(1728행)까지는 출력량(ovkeyw/ovsnam/ovlnam/ovunit 등) 메타데이터를 ivtype별로 채우는 대형 블록이다. layer-dependent 출력은 `k = 0:kmax` (`:1108`) 와 `k = 1:kmax` (`:1218`) 두 그룹으로 나뉘고, 힘·모멘트(`:1532`), rigid body 운동(`:1606`)까지 등록된다. (개별 ivtype 전사는 분량상 생략 — output 모듈 노트 영역.)

---

## 3. 입력격자·입력장 (INPGRID / READINP)

### 3.1 SwashInputGrid — `INPGRID` 명령

Purpose: `Reads parameters of an input grid` (`SwashInputGrid.ftn90:41-43`). 명령 구문 전체가 주석 박스로 verbatim 기록됨(`:81-147`): BOTtom/WLEVel/CURrent/.../`ACURrent` 등 입력장 종류와 `REGular | CURVilinear STAGgered | UNSTRUCtured` 격자형.

격자형 분기:
- **CURV**: `igtype(igrid1)=2`, 1D/직사각/비구조 computational grid 와는 incompatible (msgerr 4) (`:150-167`). `STAG` 키워드로 `lstag(igrid)=.true.` (staggered curvilinear) (`:170-173`).
- **UNSTRUC**: `igtype=3`, `mxg=nverts, myg=1` (`:183-208`).
- **REG**(기본): `igtype=1`. 회전각 `alpg`를 $[-\pi,\pi]$로 정규화 `alpg = pi2*(alpg/360 - nint(alpg/360))` 후 `cospg/sinpg` 계산 (`:225-228`). 사용자가 준 cell 수를 grid-point 수로 변환(`mxg = mxg+1`) (`:233-246`).

비정상(NONSTAT) 입력장: `igrid` 종류에 따라 nonstationary 금지 검사(bottom 등 일부만 허용) (`:264-291`). 연직 비균일(NONUNIF/VERT): `ifllay(igrid)` 설정, depth-averaged(`kmax==1`)에서 금지, salinity(15)/temp(16)/sed(17)/acur(20,21)만 연직 비균일 허용 (`:294-312`).

직사각 입력격자가 계산격자와 동일하면 `lflgrd(igrid)=.true.` 유지(보간 생략 플래그), 다르면 `.false.` (`:378-392`). 이 플래그는 InitCompGrid의 bottom 보간 분기(`SwashInitCompGrid.ftn90:136-144`)에서 쓰인다.

### 3.2 SwashInputField — `READINP`, INAR2D 적재

Purpose: `Reads and stores actual input field` (`SwashInputField.ftn90:43-45`). 입력장 종류→`igr1` 번호 매핑이 키워드 분기로 결정됨 (`:113-184`):

| 키워드 | igr1 | 적재 배열 |
|---|---|---|
| BOT | 1 | `depth` (`:248`) |
| CUR/VEL | 2(+3) | `uxb`/`uyb` (`:253,365`) |
| FR | 4 | `fric` (`:258`) |
| WI | 5(+6) | `wxi`/`wyi` (`:263,370`) |
| WL | 7 | `wlevl` (`:268`) |
| COOR | 8(+9) | `xcgrid`/`ycgrid` (`:275,377`) |
| PORO/PSIZ/HSTRUC | 10/11/12 | `npor`/`gsiz`/`hpor` |
| PR | 13 | `pres` |
| NPLA | 14 | `npla` |
| SAL/TEMP/SED | 15/16/17 | `sal`/`temp`/`sed` (연직 다층) |
| ACUR | 20(+21) | `avxi`/`avyi` (ambient) (`:333,385`) |
| MWL | 22 | `mwl` (mean water level) |
| CORI | 23 | `corp` |

transport 입력(SAL/TEMP/SED)은 `itrans=1`, `ltrans=ltrans+1`, 해당 인덱스(`lsal/ltemp/lsed`)에 ltrans 부여 (`:151-165`) — 즉 입력 순서대로 constituent 인덱스가 누적된다(Density에서 `rp(n,k,lsal)` 식으로 참조).

실제 데이터 읽기는 `do k = 1, ifllay(igr1)` 루프로 층별 `INAR2D` 호출 후 `SWCOPR`로 복사 (`:233-348`). 연직 다층(`sal/temp/sed/avxi/avyi`)은 `(k-1)*mxg*myg` 오프셋으로 한 배열에 stack (`:308-309`). ADCIRC 격자면 bottom은 fort.14에서 가져오므로 즉시 return (`:226-231`).

---

## 4. 계산격자 셋업

### 4.1 SwashInitCompGrid — 구조격자(직사각/곡선)

Purpose: `Initialises arrays for description of computational grid in case of regular grid; These arrays need to be partitioned, if appropriate` (`SwashInitCompGrid.ftn90:38-41`).

핵심 자료구조 **KGRPGL** — global 도메인의 indirect addressing 인덱스 테이블. 초기값 1(=dummy/dry), 유효 점마다 `mcgrd`를 증가시키며 부여:
```
mcgrd = mcgrd + 1 ; KGRPGL(i,j) = mcgrd        (:148-149)
```
유효성 판정: 격자좌표가 exception값(`excfld(8/9)`)이 아니고(`:100-112`), bottom level(`dep`)이 exception(`excfld(1)`)이 아닐 때(`:146-151`). bottom은 `lflgrd(1)`이면 직접 인덱싱, 아니면 `SVALQI(...,NEAREST)` 보간 (`:136-144`).

곡선격자(`optg==3`) 추가처리:
- 첫 유효점 좌표를 offset(`xoffs/yoffs`)으로 잡고 0으로 reset, 이후 점은 offset 차감 (`:116-129`).
- 가상 경계열 외삽 `xcgrid(mxc,:) = 2*xcgrid(mxc-1,:) - xcgrid(mxc-2,:)` (`:194-198`).
- `call CVCHEK` 곡선격자 검사 (`:204`).
- 도메인 길이/방위 `xclen/yclen`·양의 x축 방향 `alpc = atan2(...)` 계산 (`:227-235`) — 경계 파 스펙트럼 부과에 필요.

**도메인 분할**(분산메모리): `PARLL`이면 `kpart` 옵션으로 `LORB`(orb 분할 여부) 결정 — 2D+다층이면 디폴트 LORB=true (`:240-260`). `call SWDECOMP` 실행 (`:265`). 이후 서브도메인별 부분(`MXF:MXL,MYF:MYL`)을 `kgrpnt`(local 인덱스)에 재할당하며 mcgrd 재계산 (`:276-283`). xcgrid/ycgrid도 global(`XGRDGL/YGRDGL`) 보존 후 local 잘라내기 (`:288-300`).

상태배열 할당: `s1(mcgrd)`, `u1(mcgrd,kmax)`, `v1(mcgrd,kmax)`(2D만; 1D는 v1(0,0) 빈배열) (`:322-342`), 다층이면 depth-averaged `udep/vdep` (`:345-366`). `logcom(6)=.true.`로 할당 완료 표시. 비구조 전용 배열(xcugrd/ycugrd/vmark)은 빈 배열로 (`:370-372`).

### 4.2 SwashInitCompUgrid — 비구조격자

Purpose: `Initialises arrays for description of computational grid in case of unstructured grid` (`SwashInitCompUgrid.ftn90:38-40`). 훨씬 단순:
- 정점(`xcugrd/ycugrd`) offset 적용: 첫 정점을 offset 기준으로(`:83-94`).
- `call SwashCheckGrid` (`:98`).
- 범위(`xcgmin..`)·enclosure 길이(`xclen=xcgmax-xcgmin`) (`:102-116`).
- 할당: `s1(ncells)`, `u1(nfaces,kmax)`, 다층이면 `udep(nfaces)` (`:118-143`). **즉 비구조에서 수위는 cell 중심(ncells), 유속은 face(nfaces)** — finite-volume staggered 배치.
- 직렬 실행이면 `nvertsg=nverts, ncellsg=ncells` (`:147-150`).
- 구조격자 전용 배열(KGRPGL/kgrpnt/XGRDGL/YGRDGL)은 빈 배열로, 편의상 `mcgrd=nverts` (`:154-162`).

---

## 5. SwashGeometrics — metric tensor·Jacobian

Purpose: `Computes geometric quantities based on given grid` (`SwashGeometrics.ftn90:38-40`). 공변 기저벡터 $a_{(1)},a_{(2)}$ 의 성분 dx1,dy1,dx2,dy2 를 구해 metric/Jacobian 산출.

### 5.1 직사각격자 (`optg==1`)

균일 격자라 기저벡터가 상수: 회전각 `cospc/sinpc`로 (`:78-82`)
$$ dx_1 = \Delta x\cos\theta,\ dy_1 = \Delta x\sin\theta,\ dx_2 = -\Delta y\sin\theta,\ dy_2 = \Delta y\cos\theta $$
구면좌표(`kspher>0`)면 `lendeg` 곱 (`:84-90`). u-점·v-점에서 metric:
```
gvu(indx) = sqrt( coslat^2*dx1^2 + dy1^2 )    (:113)
guu(indx) = sqrt( coslat^2*dx2^2 + dy2^2 )    (:114)
gsqsu(indx) = coslat*( dy2*dx1 - dy1*dx2 )    (:115)  ← Jacobian (√g)
```
구면이면 위도 코사인 `coslat = cos(degrad*(0.5*(ycgrid(ix,iy)+ycgrid(ix,iy-1))+yoffs))` (`:105`).

### 5.2 곡선격자 (else 분기)

기저벡터를 인접 좌표 차분으로 추정. 내부 u-점: 중앙차분
```
dx1 = 0.25*( xcgrid(ix+1,iy)+xcgrid(ix+1,iy-1) - xcgrid(ix-1,iy)-xcgrid(ix-1,iy-1) )   (:204)
dx2 = xcgrid(ix,iy) - xcgrid(ix,iy-1)                                                   (:207)
```
경계(ix=1)는 전방차분(`:178-182`). v-점도 대칭적으로 (`:245-298`). 가장자리 행/열은 인접 내부값 복사 (`:229-241, 300-312`).

### 5.3 wl-점 Jacobian

모든 경우 마지막에 wl-점 Jacobian을 u-/v-metric 평균곱으로:
```
gsqs(indx) = 0.5*(gvv(indx)+gvv(indxb)) * 0.5*(guu(indx)+guu(indxl))   (:325-328)
```

---

## 6. 연직 sigma 좌표 — Layer Interfaces

### 6.1 SwashLayerIntfaces (구조격자)

Purpose: `Determines position of the layer interfaces and layer thicknesses at waterlevel and velocity points` (`SwashLayerIntfaces.ftn90:40-42`). Method: 연직을 고정 층 수로 분할, k=0..kmax 가 **자유수면에서 아래로** 계수 (`:44-48`).

알고리즘(wl-점 예):
```
zks(:,0) = -dps(:) + hs(:)          ! 최상층 = 바닥 + 수심 = 자유수면   (:76)
call sigmacoor( zks, hs, mcgrd )    ! sigma 분포로 중간 interface 채움  (:78)
hks(:,k) = zks(:,k-1) - zks(:,k)    ! 층 두께                          (:84)
```
`sigmacoor`는 이 노트 범위 밖(`SwashServices.ftn90:454-595`)이지만, 여기서 호출되어 zk 배열을 sigma 분포로 채운다 — ⚠ 분포식 본체는 미확인(서비스 모듈 노트 영역).

u-점은 두 종류를 계산: (1) 시간외삽 수심 `humn` 기반 — `zkum(:,0)=zkum(:,kmax)+humn` (`:93-95`, 주석 `extrapolated in time; see SwashUpdateDepths`), (2) 통상 수심 `hu/hum` 기반 (`:109-122`). v-점(2D만)도 동일 (`:126-151`).

**subgrid pressure layer**(`lsubg`): 압력층 두께 `hksc(:,kp)`를 velocity 층 두께 `hks(:,k)`를 `npu(kp)`개씩 누적해 구성 (`:155-192`) — 이는 v4.01 `subgrid approach`(`:38-39`, Rijnsdorp·Smit) 지원.

### 6.2 SwashLayUIntfaces (비구조격자)

Purpose 동일하나 `on unstructured mesh` (`SwashLayUIntfaces.ftn90:40`). 2020 April 신설(`:36`). 구조판과 동일 로직이되 `sigmacoor` 인자가 `ncells`(wl) / `nfaces`(velocity) (`:74,91,108-109`). v-점 분기·subgrid 블록 없음(비구조는 face 통일).

---

## 7. SwashDensity — Eckart 상태방정식

Purpose: `Calculates density of water relative to reference density based on temperature, salinity or sediment` (`SwashDensity.ftn90:38-40`). Method: Eckart(1958) 공식 사용 — 출처 주석 verbatim:
> `C. Eckart` / `Properties of water, part II. The equation of state of water and sea water at low temperatures and pressures` / `Amer. J. of Sci., vol. 256, 225-240, 1958` (`SwashDensity.ftn90:46-48`).

격자점 수 `ntot`은 구조면 `mcgrd`, 비구조(`optg==5`)면 `ncells` (`:84-88`).

Eckart 식 (염분+온도 동시 변동 분기, `:105-108`):
$$ P_0 = 5890 + (38 - 0.375\,t)\,t + 3\,s $$
$$ \lambda = 1779.5 + (11.25 - 0.0745\,t)\,t - (3.8 + 0.01\,t)\,s $$
$$ \rho = \frac{P_0}{\lambda + 0.698\,P_0} $$
(t=온도, s=염분; `rp(n,k,lsal)`, `rp(n,k,ltemp)`에서 읽음 — InputField가 매긴 인덱스). 염분만/온도만 변동하는 경우는 상수항을 미리 묶어 최적화 (`:113-153`).

단위 보정·상대화: Eckart는 g/ml라 1000배 후 reference density 차감 — `rho = 1000.*rho - rhow` (`:160-163`).

**퇴적물 혼합**(`lsed>0 .and. lmixt`): 부피농도 `c`로 혼합밀도 (`:165-181`)
$$ \rho = c\,(\rho_s - \rho_w) + \rho\,(1-c) $$
온도·염분 둘 다 없으면 `rho=0.` (`:154-156`). 연산은 모두 `real*8` 더블 정밀도(`:66-74`).

---

## 8. 초기조건 — SwashInitCond

Purpose: `Sets initial state of the flow and turbulence fields` (`SwashInitCond.ftn90:38-40`). `INIT` 명령 파서. 구문 박스 verbatim(`:111-123`):
```
INITial < CON [wlev] [vx] [vy] [tke] [epsilon] | ZERO | STEAdy | HOTStart <MULT|SING> 'fname' >
```

분기:
- **ZERO**: 모든 흐름변수 0 (`:127-139`).
- **STEA**: `instead=.true.` 만 세팅, 실제 계산은 나중에 SwashInitSteady가 (`:141-146`).
- **HOTS/REST**: hotstart 파일 읽기 (`:148-472`). 첫줄이 `SWASH`인지 검사(`:182`), TIME/LOCA/ZK 헤더 파싱, 양자 수(numqua) 검사 — 1D/2D × depth-avg/다층 조합별로 3/4/5/7개 기대 (`:219-233`). 구조격자는 mxcur×mycur 루프로 s1/u1/v1(층별 efac 스케일) 읽음 (`:250-386`), 비구조는 nverts 루프 (`:388-471`). `MULT`(서브도메인별 파일)/`SING`(단일 파일) 모드 (`:157-170`).
- **CON**(기본): 상수 초기값 `WLEV/VX/VY/TKE/EPSILON` 읽어 `s1=wlev, u1=vx, v1=vy` (`:478-492`). 다층이면 udep/vdep도. dry점(인덱스1)은 0으로 (`:494-502`). 비구조(`optg==5`)는 속도를 face 법선성분으로 `u1(iface,:) = nx*vx + ny*vy` (`:504-510`).

---

## 9. 정상상태 흐름 — SwashInitSteady

Purpose: `Initializes velocities based on Chezy formula for uniform flow` (`SwashInitSteady.ftn90:38-40`). Method verbatim: $u = C\sqrt{h\,i}$ (C=Chezy, h=수심, i=수위경사) (`:44-54`). InitCond의 STEA가 `instead`를 켰을 때 호출.

u-점 계산(1D, `:96-123`):
```
slope = ( s1(nm) - s1(nmu) ) / dx                  ! 수위경사   (:103)
cz    = sqrt( grav / cfricu(nm) )                  ! Chezy 환산  (:106)
vel   = sign(1.,slope) * cz * sqrt( hu(nm)*abs(slope) )         (:111)
```
**Froude 제한**: 초임계류 방지 — `froude = |vel|/sqrt(grav*hu)`, `> 0.9999`이면 `vel = (0.9999/froude)*vel` (`:113-119`, 주석 `limited by the Froude criterion so that no super-critical flow will occur` :54). 2D는 u-점(gvu 경사)·v-점(guv 경사) 각각 (`:130-205`). 다층이면 연직 균일 가정으로 `u1(:,k)=udep(:)` 복제 (`:224-238`). 병렬 교환(`SWEXCHG`)·주기경계(`periodic`) 호출 (`:127,213-220`).

---

## 10. SwashAmbCurrent — 배경류 변환·보간

Purpose: `Determines ambient current in water level or velocity points` (`SwashAmbCurrent.ftn90:38-40`). 2023 신설(Rijnsdorp). `iamb` 플래그로 wl-점(`iamb==1`) 또는 velocity-점(`iamb==2`) 분기 (`:81,514`).

세 가지 입력 소스 분기(각 점 종류 안에서):
1. **staggered curv 입력** `lstag(20/21)`: avxf/avyf를 직접/평균 사용 (`:127-175`).
2. **공간변동** `varva`: 공간변동 배경류 `avxf/avyf`.
3. **상수** `uamb/vamb`.

**Cartesian→contravariant 변환**(2D 핵심) — u-점 예 (`:587-588`):
$$ U_{bck} = \frac{u_{amb}\,(y_{c}(m,n)-y_{c}(m,n{-}1)) - v_{amb}\,(x_c(m,n)-x_c(m,n{-}1))}{g_{uu}} $$
즉 covariant 좌표차를 metric `guu`로 나눠 contravariant 성분을 만든다. v-점은 대칭적으로 `gvv` 사용 (`:638-639`). 변동/staggered 경우엔 면→셀중심으로 0.5 평균 추가 보간 (`:189-207` 등). 가상 경계점은 인접 내부값 복사하되 주기격자(`lreptx/lrepty`)면 건너뜀 (`:149-172`). dry점 0, `SWEXCHG`·`periodic` 처리 (`:497-510, 649-662`).

---

## 11. 파일 간 일관성·관찰

- **격자 staggered 배치 확정**: 구조(InitCompGrid `s1(mcgrd)`, `u1(mcgrd,kmax)`) / 비구조(InitCompUgrid `s1(ncells)`, `u1(nfaces,kmax)`) — 수위 cell중심·유속 face 의 Arakawa-C/FV staggered가 코드로 확인됨.
- **sigma 좌표 방향 일관**: LayerIntfaces·LayUIntfaces 모두 `k=0`이 자유수면, 아래로 증가 (`SwashLayerIntfaces.ftn90:46-48`, `SwashLayUIntfaces.ftn90:44-46`)로 동일. `sigmacoor` 호출 인자만 mcgrd↔ncells/nfaces 차이.
- **constituent 인덱스 흐름**: InputField가 `ltrans++` 로 lsal/ltemp/lsed 부여(`SwashInputField.ftn90:151-165`) → Density가 `rp(n,k,lsal)` 등으로 소비(`SwashDensity.ftn90:102-103`). 모순 없음.
- **offset 일관**: 구조(InitCompGrid `:116-129`)·비구조(InitCompUgrid `:83-94`)·InputField COOR(`:271-281`) 모두 `lxoffs` 플래그로 첫 좌표 기준 offset 적용 — 동일 규약.
- ⚠ **미확인**: `sigmacoor`의 sigma 분포식 본체(`SwashServices.ftn90:454-595`)는 이 노트 범위 밖. metric tensor가 SwashGeometrics에서 정의되나 그 소비처(모멘텀 이산화)는 별도 노트 영역. SwashInit `:518` 이후 output-변수 메타데이터 개별 ivtype은 전사하지 않음(분량/범위) → source-needed (output 모듈 노트에서 다룰 것).

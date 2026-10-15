---
title: "SWASH 초기화·격자·밀도/기하 — SwashInit/InitCond/InitSteady/CompGrid/Geometrics/LayerIntfaces/Density/AmbCurrent"
model: SWASH
component: src (initialization / grid / geometry)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashInit.ftn90(기본값 블록 92-552행), SwashInitCond.ftn90(INIT 명령 파서 125-513), SwashInitSteady.ftn90(Chezy 90-238), SwashInitCompGrid.ftn90(KGRPGL/SWDECOMP 94-377), SwashInitCompUgrid.ftn90(offset/allocate 83-164), SwashInputGrid.ftn90(INPGRID 파서 149-406), SwashInputField.ftn90(READINP/INAR2D 111-446), SwashDensity.ftn90(Eckart 식 84-181), SwashGeometrics.ftn90(metric tensor 76-332), SwashLayerIntfaces.ftn90(sigma 76-192), SwashLayUIntfaces.ftn90(unstr 72-118), SwashAmbCurrent.ftn90(contravariant 81-666) file:line 인용; 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
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
- **물리상수**: `grav = 9.813`, `rhoa = 1.205`, `dynvis = 1.e-3`, `vonkar = 0.4` (`src/SwashInit.ftn90:135–139`). [10-15 대조 정정]
- `rhow = -999.`는 후속 결정용 표지다 (`src/SwashInit.ftn90:136`; inputs-setup:SI1-120). [10-15 대조 정정]
- `idens == 0 .and. .not. rhow /= -999.`이면 Eckart 실제 밀도를 계산한다 (`src/SwashCheckPrep.ftn90:894–899`; inputs-setup:SI1-120). [10-15 대조 정정] [10-15 전수 검증 정정]
- `idens≠0`이면 미지정 참조 밀도를 1000으로 정한다 (`src/SwashCheckPrep.ftn90:901–905`; inputs-setup:SI1-120). [10-15 대조 정정]
- RHOWAT를 명시하면 해당 입력을 유지한다 (`src/SwashCheckPrep.ftn90:894–905`; inputs-setup:SI1-120). [10-15 대조 정정]
- **건습(dry) 임계값**: `epsdry = 5.e-5`, `epshu = 1.e-3`, `epsuf = 1.e-8` (`src/SwashInit.ftn90:121–123`). [10-15 대조 정정]
- epshu 최초값은 10⁻³이다 (`src/SwashInit.ftn90:122`; inputs-setup:SI1-503). [10-15 대조 정정]
- DEPMIN만 변경하면 epshu도 함께 변경한다 (`src/SwashReadInput.ftn90:529,553–554`; inputs-setup:SI1-503). [10-15 대조 정정]
- `inewt=0`이면 준비 단계에서 `epshu=epsdry`로 정한다 (`src/SwashCheckPrep.ftn90:1219`; inputs-setup:SI1-503). [10-15 대조 정정]
- **밀도 파라미터 디폴트**: `idens=0`, `tempw=14.`, `salw=31.`, `rhos=2650.`, `lmixt=.true.` (`:143-147`) — SwashDensity가 쓰는 상수온도/염분.
- **문제 좌표**: `kspher=0`은 평면 Cartesian 문제 좌표이다 (`src/SwashReadInput.ftn90:581`; inputs-setup:SI1-708). [10-15 대조 정정]
- `kspher=0`은 계산 격자의 직교성이나 직사각형 여부를 뜻하지 않는다 (`src/SwashReadInput.ftn90:581`; inputs-setup:SI1-708). [10-15 대조 정정]
- **구면좌표**: `rearth=2.e7/pi`, `lendeg=2.e7/180.` (`src/SwashInit.ftn90:158–161`). [10-15 대조 정정]
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

파서의 NONSTAT 허용 입력량은 속도·마찰·바람·수위·대기압·흘수이다 (`src/SwashInputGrid.ftn90:264–273`; `src/SwashReadInput.ftn90:2398–2400`; `src/SwashUpdateData.ftn90:2517–2518`). [10-15 대조 정정] [10-15 전수 검증 정정]
속도·수위의 실제 시간 갱신에는 SI1-515의 SKIPMOM 조건도 적용한다 (`src/SwashCheckPrep.ftn90:342–354`; inputs-setup:SI1-709). [10-15 대조 정정]
BOTTOM·계산 좌표·공극률·입도·구조물 높이·식생 밀도·성분·LABEL·주변 흐름·평균 수위·Coriolis는 금지한다 (`src/SwashInputGrid.ftn90:267–273`; inputs-setup:SI1-709). [10-15 대조 정정]

NONUNIF/VERT는 `ifllay(igrid1)`에 입력층 수를 설정한다 (`src/SwashInputGrid.ftn90:294–299`). `kmax==1`인 계산에서는 이 옵션을 거부한다 (`src/SwashInputGrid.ftn90:295`). 연직 비균일 입력은 염분(15)·수온(16)·퇴적물(17)·주변 흐름(20·21)에 한정한다 (`src/SwashInputGrid.ftn90:296–297`; inputs-setup:SI1-517). [10-15 대조 정정] [10-15 전수 검증 정정]

코드는 원점·각도·점 수가 같은지 검사한다 (`src/SwashInputGrid.ftn90:388`; inputs-setup:SI1-513). [10-15 대조 정정]
격자 간격은 비교하지 않는다 (`src/SwashInputGrid.ftn90:388`; inputs-setup:SI1-513). [10-15 대조 정정]
간격만 다른 격자가 직접 인덱스 복사로 처리될 수 있으므로 E 후보로 유지한다 (`src/SwashCheckPrep.ftn90:2266–2269`; inputs-setup:SI1-513). [10-15 대조 정정]

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

연직 다층은 LAYERS 이름 목록의 파일당 한 층 경로를 사용한다 (`src/SwashInputField.ftn90:394–396`; inputs-setup:SI1-260). [10-15 대조 정정]
직접 fname만 지정한 다층 입력은 첫 층을 읽은 뒤 목록 단위 0을 읽는 결함 후보이다 (`src/SwashInit.ftn90:266`; `src/SwashInputField.ftn90:394–396`; inputs-setup:SI1-260). [10-15 대조 정정] [10-15 전수 검증 정정]

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

**도메인 분할**: OCPINI의 초기 KPART는 1이므로 별도 초기화 파일 지정이 없으면 stripwise다 (`src/ocpids.ftn:111`; guide-syntax-build:SG1-902). [10-15 대조 정정]
`INIVEF.GT.4`인 초기화 파일에서 KPART를 읽는다 (`src/ocpids.ftn:154`; guide-syntax-build:SG1-902). [10-15 대조 정정]
병렬 경로의 `if ( kpart < 0 .or. kpart > 4 ) then`에서만 2D 다층이면 ORB를 자동 선택한다 (`src/SwashInitCompGrid.ftn90:240–259`; guide-syntax-build:SG1-902). [10-15 대조 정정]
`KPART=2`는 ORB다 (`src/SwashInitCompGrid.ftn90:250–251`; guide-syntax-build:SG1-902). [10-15 대조 정정] [10-15 전수 검증 보완]
0은 경고 후 stripwise이고 1·3·4도 stripwise다 (`src/SwashInitCompGrid.ftn90:240–259`; guide-syntax-build:SG1-902). [10-15 대조 정정]
분할 뒤 각 프로세스의 국소 격자 크기를 계산한다 (`src/SwashInitCompGrid.ftn90:265–300`; `src/swanparll.ftn:3542–3543`; theory-unstructured:ST2-422). [10-15 대조 정정]

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
zks(:,0) = -dps(:) + hs(:)          ! 자유수면 경계면 (:76) [10-15 대조 정정]
call sigmacoor( zks, hs, mcgrd )    ! sigma 분포로 중간 interface 채움  (:78)
hks(:,k) = zks(:,k-1) - zks(:,k)    ! 층 두께                          (:84)
```
`zks(:,0)`는 자유수면 경계면이다 (`src/SwashLayerIntfaces.ftn90:76`; theory-framework:ST1-328). [10-15 대조 정정]
최상층은 두 경계면 0·1 사이의 층 1이다 (`src/SwashLayerIntfaces.ftn90:84`; theory-framework:ST1-328). [10-15 대조 정정]
공유 sigmacoor는 가변층에서 수심 비율로 계면을 내린다 (`src/SwashServices.ftn90:531–540`; theory-unstructured:ST2-383). [10-15 대조 정정]
fixlay 분기는 고정층 총두께를 뺀 수심에 가변층 비율을 적용한다 (`src/SwashServices.ftn90:551–571`; theory-unstructured:ST2-383). [10-15 대조 정정]
총수심이 고정층 총두께 이하이면 hlaysh를 사용한다 (`src/SwashServices.ftn90:585`; theory-unstructured:ST2-383). [10-15 대조 정정]
`src/SwashLayUIntfaces.ftn90:74,91,108–109`는 이 공유 서비스를 호출한다 (theory-unstructured:ST2-383). [10-15 대조 정정]
swashuse PDF p.40은 가변층과 고정층을 설명하지만 비구조 고정 두께 층은 지원 범위에서 제외한다 (theory-unstructured:ST2-383). [10-15 대조 정정]

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
공유 sigmacoor의 분포식 근거는 `src/SwashServices.ftn90:531–585`이다 (theory-unstructured:ST2-383). [10-15 대조 정정]

## 문서와 코드 차이 (10-15 대조)

출처: [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md), [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md), [inputs-setup](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md), [inputs-physics-numerics](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md), [guide-syntax-build](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md)의 최종 결론과 원문 인용.

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech, 공개 저장소 `7949227 2026-05-06 "release v12.01"`에서 마지막 변경; 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f 2026-05-26`, 12.01 뒤 `608ffd7`·`9554c98` 포함.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| guide-syntax-build:SG1-590 | swashuse PDF p.156 (edt 50–50): (nhedvec]) | swashuse PDF p.156 (edt 50–50): `(nhedvec])` | `src/ocpmix.ftn:723–726` `NHEDC = 0                                                         30.80` / `IF (LOGC) THEN` / `CALL ININTG ('NHEDVEC', NHEDC, 'UNC', 0)                        30.20` / `ENDIF` | B 문서 오기 | NHEDVEC 선택 필드의 도식은 `([nhedvec])`다. swashuse PDF p.156의 `(nhedvec])`는 여는 대괄호를 빠뜨렸다. swashuse PDF p.47의 도식과 swashuse PDF p.50의 필드 설명은 맞으므로 B는 부록 swashuse PDF p.156에 한정한다. 수치 필드 판독은 8756667(2022-09-03 initial release)부터 같아 판 차이 A가 아니다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| guide-syntax-build:SG1-591 | swashuse PDF p.156 (edt 53–53): FREE \| FORMAT ’form’ \| [idfm] \| UNFORMATTED | swashuse PDF p.156 (edt 53–53): `FREE \| FORMAT ’form’ \| [idfm] \| UNFORMATTED` | `src/ocpmix.ftn:727–751` `CALL INKEYW ('STA', 'FREE')                                       30.06` / `IDFM = 2` / `IF (KEYWIS('FRE')) THEN` / `IDFM = 0` / `ELSE IF (KEYWIS('UNF')) THEN` / `IDFM = -1` / `ELSE IF (KEYWIS('FOR')) THEN` / `!         formatted read` / `CALL ININTG ('IDFM', IDFM, 'NSKP', 2)` / `SELECT CASE(IDFM)                                               40.02` / `CASE(1)                                                         40.02` / `RFORM = '(10X,12F5.0)'                                        40.02` / `CASE(2)                                                         40.02` / `CALL INCSTR ('FORM', RFORM, 'REQ', ' ')                       40.02` / `CASE(5)                                                         40.02` / `RFORM = '(16F5.0)'                                            40.02` / `CASE(6)                                                         40.02` / `RFORM = '(12F6.0)'                                            40.02` / `CASE(8)                                                         40.02` / `RFORM = '(10F8.0)'                                            40.02` / `CASE DEFAULT                                                    40.02` / `CALL MSGERR (2, 'illegal format number')                      40.02` / `WRITE (PRINTF, 50) IDFM                                       40.02` / `50        FORMAT (' -> ', I6)                                           40.02` / `END SELECT                                                      40.02` | B 문서 오기 | 수치 IDFM 앞에도 FORMAT 키워드가 필요하다. swashuse PDF p.156의 평평한 선택지 표기는 IDFM을 독립 대안처럼 보이게 한다. swashuse PDF p.47·50의 FORMAT 설명은 코드와 맞으므로 B는 부록 swashuse PDF p.156 도식에 한정한다. FOR 내부의 IDFM 판독은 8756667(2022-09-03 initial release)부터 같다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| guide-syntax-build:SG1-869 | 입력장 추가 별칭 | swashuse PDF p.41–49의 입력장 설명과 misc/swash.edt:26–53에는 아래 추가 별칭이 없다. | `src/SwashReadInput.ftn90:2358` `else if ( KEYWIS ('CUR') .or. KEYWIS ('VEL') ) then`; `src/SwashReadInput.ftn90:2413` `else if ( KEYWIS ('SHIP') .or. KEYWIS ('VESS') .or. KEYWIS ('WEC') .or. KEYWIS ('FLOAT') .or. KEYWIS ('DRAF') .or. KEYWIS ('PONT') .or. KEYWIS ('PFLOW') ) then`; `src/SwashReadInput.ftn90:2416` `else if ( KEYWIS ('LAB') .or. KEYWIS ('BODY') ) then`; `src/SwashReadInput.ftn90:2419` `else if ( KEYWIS ('ACUR') .or. KEYWIS ('BCUR') .or. KEYWIS ('CCUR') ) then`; `src/SwashInputGrid.ftn90:294` `if ( KEYWIS ('NONUNIF') .or. KEYWIS ('VERT') ) then` | C 문서 누락 | CUR는 VEL도 받는다. DRAF는 SHIP·VESS·WEC·FLOAT·PONT·PFLOW도 받는다. LAB는 BODY도 받는다. ACUR는 BCUR·CCUR도 받는다. NONUNIF는 VERT도 받는다. C는 입력장 기능 자체가 아니라 이 별칭 목록의 누락이다. [10-15 결론 검증 보완] |
| guide-syntax-build:SG1-879 | 층 합과 shadow sigma | swashuse PDF p.40는 PERC 합 100과 가변층 최소 하나를 명시한다. 합의 허용오차와 shadow sigma 구성은 명시하지 않는다. | `src/SwashCheckPrep.ftn90:434–437` `if ( abs(sumh - 1.0) > eps ) then` / `!` / `write (msgstr, '(a,i4,a)') 'the sum of layer thicknesses in percentage is ',nint(sumh * 100.0),' (should be 100)'` / `call msgerr ( 3, trim(msgstr) )`; `src/SwashCheckPrep.ftn90:459` `if ( indlay(i) /= 1 ) depfix = depfix + hlay(i)`; `src/SwashCheckPrep.ftn90:465` `epsfix = 2. * depfix`; `src/SwashCheckPrep.ftn90:471–475` `if ( indlay(i) == 1 ) then` / `hlaysh(i) = hlay(i)/2.` / `else` / `hlaysh(i) = hlay(i)/epsfix` / `endif`; `src/SwashCheckPrep.ftn90:81` `real, parameter                             :: eps = 1.e-3 ! a small criterion number` `src/SwashCheckPrep.ftn90:453–483`의 fixlay 분기와 `hlaysh = hlay`. | C 문서 누락 | PERC 합 검사는 `if ( abs(sumh - 1.0) > eps ) then`이며 `eps = 1.e-3`이다. `fixlay`일 때만 고정 두께 합 depfix와 `epsfix = 2. * depfix`를 계산한다. 이 분기에서 상대층은 `hlaysh(i) = hlay(i)/2.`이고 고정층은 `hlaysh(i) = hlay(i)/epsfix`다. 고정층이 없으면 `hlaysh = hlay`다. C는 허용오차와 shadow 배열 구성에 한정한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| guide-syntax-build:SG1-889 | RHOWAT 자동 계산 | swashuse PDF p.34는 기준 `RHOWAT=1000`과 실제 밀도의 온도·염분 의존성을 설명한다. Eckart 다항식과 -999 표지에 따른 자동 선택은 명시하지 않는다. | `src/SwashCheckPrep.ftn90:894–905` `if ( idens == 0 .and. .not. rhow /= -999. ) then` / `!` / `pf0    =  5890d0  + (  38d0  - 375d-3*dble(tempw))*dble(tempw) +                        3d0*dble(salw)` / `lambda = 17795d-1 + (1125d-2 - 745d-4*dble(tempw))*dble(tempw) - (38d-1 + 1d-2*dble(tempw))*dble(salw)` / `! density based on Eckart is g/ml, hence multiply by 1000 to get g/l` / `rhow   = 1000.*pf0/(lambda+0.698*pf0)` / `!` / `else if ( .not. rhow /= -999. ) then` / `!` / `rhow = 1000.` / `!` / `endif`; `src/SwashCheckPrep.ftn90:918` `kinvis = dynvis / rhow` | C 문서 누락 | `idens == 0 .and. .not. rhow /= -999.`이면 Eckart 다항식으로 실제 rhow를 계산한다. 나머지 미지정 rhow는 1000으로 대입한다. `kinvis = dynvis / rhow`다. C는 밀도의 온도·염분 의존성 자체가 아니라 이 자동 계산식과 선택 조건에 한정한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| guide-syntax-build:SG1-902 | MPI 분할 방식의 기본값 | swashuse PDF p.144는 MPI 영역 분할을 설명한다. KPART 초기값과 ORB·stripwise 선택 조건은 명시하지 않는다. | `src/SwashInitCompGrid.ftn90:240–259` `if ( PARLL ) then` / `if ( kpart < 0 .or. kpart > 4 ) then` / `if ( kpart > 4 ) call msgerr (1, 'incorrect grid partitioning option')` / `if ( .not.oned .and. kmax > 1 ) then` / `LORB = .true.` / `else` / `LORB = .false.` / `endif` / `else if ( kpart == 1 ) then` / `LORB = .false.` / `else if ( kpart == 2 ) then` / `LORB = .true.` / `else if ( kpart > 2 ) then` / `LORB = .false.` / `else` / `LORB = .false.` / `call msgerr (1, 'incorrect grid partitioning option')` / `endif` / `else` / `LORB = .false.`; `src/swanparll.ftn:163` `!MPI      CALL MPI_COMM_RANK ( MPI_COMM_WORLD, INODE, IERR )`; `src/swanparll.ftn:179` `!MPI      CALL MPI_COMM_SIZE ( MPI_COMM_WORLD, NPROC, IERR )` `src/ocpids.ftn:111` `KPART = 1`; `src/ocpids.ftn:154` `IF (INIVEF.GT.4) READ (11, *,   ERR=930, END=930) KPART`; `switch.pl:58`의 MPI 표지 제거. | C 문서 누락 | OCPINI의 초기 KPART는 1이므로 별도 초기화 파일 지정이 없으면 stripwise다. `INIVEF.GT.4`인 초기화 파일에서 KPART를 읽는다. 병렬 경로의 `if ( kpart < 0 .or. kpart > 4 ) then`에서만 2D 다층이면 ORB를 자동 선택한다. `KPART=2`는 ORB다. 0은 경고 후 stripwise이고 1·3·4도 stripwise다. C는 이 선택 규칙의 누락이다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| inputs-physics-numerics:SI2-182 | SUBGRID·압력층 등간격 | swashuse PDF p.90: “vertical is equidistantly divided into a few number of layers for the non-hydrostatic pressure”; “different resolution in the vertical” | `src/SwashReadInput.ftn90:1527`: `lsubg = .true.`; `src/SwashCheckPrep.ftn90:497`: `hlayp = 100./real(kpmax)`; `src/SwashCheckPrep.ftn90:500` `! note: pressure layers are equally distributed over the water depth as much as possible`; `src/SwashCheckPrep.ftn90:537` `if ( nonequi .and. kpmax > 1 ) call msgerr (1,'pressure layers are not equally distributed over the water depth')` | C | SUBGRID는 속도층을 묶어 압력층을 구성한다. 압력층이 정확한 등간격이 아니면 코드가 경고를 낸다. 등간격을 강제하지 않는다. |
| inputs-setup:SI1-120 | SET rhowat | swashuse PDF p.34 “density of water (in kg/m³)”; “Default: [rhowat] = 1000.”; “usually the reference density” | `src/SwashInit.ftn90:136` `rhow   = -999.        ! reference density (subject to change)`; `src/SwashCheckPrep.ftn90:894` `if ( idens == 0 .and. .not. rhow /= -999. ) then`; `src/SwashCheckPrep.ftn90:899` `rhow   = 1000.*pf0/(lambda+0.698*pf0)`; `src/SwashCheckPrep.ftn90:901–903` `else if ( .not. rhow /= -999. ) then`<br>`rhow = 1000.` | B | 경압 외력이 없고 사용자가 밀도를 생략하면 기본 온도 14·염분 31을 Eckart 식에 대입한다. 해석: 그 대입의 산술값은 약 1023.04085 kg/m³이다. 경압 외력이 있고 미지정이면 1000 kg/m³를 사용한다. 문서의 단일 기본값은 조건을 빠뜨렸다. git 이력: `8756667:src/SwashCheckPrep.ftn90:787` `if ( idens == 0 ) then`. 최초 공개판도 일정 밀도 모드에서는 Eckart 식으로 밀도를 계산한다. 5d279d7은 사용자가 준 밀도를 보존하도록 조건을 추가했다. 문서의 단일 기본값 1000과 일치하던 기본 동작의 변경은 아니다. 물 밀도 생략값은 일정 밀도 모드에서 온도·염분식으로 정한다. 경압 모드의 생략값은 1000 kg/m³다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| inputs-setup:SI1-204 | INPGRID NONSTATIONARY의 1D 금지 | swashuse PDF p.45 “NONSTATION ... NOT FOR 1D-MODE.” | `src/SwashInputGrid.ftn90:264–266` `if ( KEYWIS ('NONSTAT') ) then`<br>`if ( nstatm == 0 ) call msgerr (3, 'keyword NONSTAT not allowed in stationary mode')`<br>`nstatm = 1`; `src/SwashUpdateData.ftn90:2503–2504` `if ( ifldyn(5) == 1 ) then`<br>`call SwashUpdateFld ( 5, 6, wxi   , wyi   , coswc, sinwc, wxf   , wyf   , xcgrid, ycgrid, kgrpnt )` | B | 입력 분기와 갱신 분기는 ONED로 금지하지 않는다. 1D에서도 시간 의존 정형 입력을 읽고 갱신하는 경로가 있다. git 이력: `8756667:src/SwashInputGrid.ftn90:252` `if ( KEYWIS ('NONSTAT') ) then`. NONSTAT 분기의 거부 조건은 최초 공개판부터 정상 모드 여부다. ONED 금지를 제거한 이력은 없다. INPGRID NONSTAT는 1D라는 이유로 금지되지 않는다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| inputs-setup:SI1-229 | READINP `fac=0` 금지 | swashuse PDF p.48 “Note that [fac] = 0 is not allowed!” | `src/SwashInputField.ftn90:188` `call INREAL ('FAC', iflfac(igr1), 'STA', 1.)`; `src/ocpmix.ftn:963–965` `DO 39 IY = 1, MYA`<br>`DO 38 IX = 1, MXA`<br>`ARR(IX,IY) = ARR(IX,IY) / VFAC`<br>`src/SwashInputField.ftn90:235–240`은 tarr를 0으로 초기화한 뒤 INAR2D를 호출한다. `src/SwashInputField.ftn90:189–191`은 LABEL의 배율만 1로 강제한다. | E·약함 | 해석: 문서가 금지한 `fac=0`을 일반 입력장에서 사전 거부하지 않는다. INAR2D는 자료 읽기 전에 기존 배열을 VFAC로 나눈다. 정상 읽기는 임시 값을 덮어쓸 수 있다. 유효 입력의 결함으로 확대하지 않고 방어 검사 누락의 E·약함 후보로 한정한다. git 이력: `8756667:src/ocpmix.ftn:969` `ARR(IX,IY,1) = ARR(IX,IY,1) / VFAC`. 후속 `608ffd7`·`9554c98`은 이 핵심 처리를 수정하지 않았다. READINP의 금지값 `fac=0`은 일반 입력장에서 사전 거부되지 않는다. 읽기 전 0 나눗셈에 도달하는 방어 검사 결함 후보로만 유지한다. 판정은 E 유지(약함)이다. ([E1 판정표](../../../_staging/recovery/compare/SWASH-git-verify-E1.md)) [10-15 결론 검증 정정] [10-15 git 이력 판정] |
| inputs-setup:SI1-237 | READINP `idla=5`의 방향 문장·도식 | swashuse PDF p.49 “top to bottom starting in the lower-left-hand corner”; 도식은 “1,1 1,2 ... 1,myc+1”을 적는다. | `src/ocpmix.ftn:990–994` `CASE(5)`<br>`DO IX=1, MXA`<br>`READ (NDSD, *, END=910, ERR=920, IOSTAT=IERR)`<br>`& (ARR(IX,IY), IY=1,MYA)`<br>`ENDDO` | B | 도식과 코드는 아래에서 위로 읽는다. “top to bottom”은 방향 오기이다. 각 지도 열마다 새 READ를 호출한다. git 이력: `8756667:src/ocpmix.ftn:995` `CASE(5)                                                           40.02`. 9d03fff은 INAR2D의 층 차원 K를 제거했다. 각 열에서 IY를 1부터 증가시키는 읽기 방향은 변경 전후에 같다. `IDLA=5`는 각 열의 아래쪽에서 위쪽으로 값을 읽는다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| inputs-setup:SI1-250 | 데이터 부족 오류·echo 조건 | swashuse PDF p.50 “if [itest]>0 ... reproduce the data”; “lay-out ... [idla]=1” | `src/ocpmix.ftn:1109–1112` `CALL MSGERR (2, 'Unexpected end of file while reading '//`<br>`& TRIM(FILENM))`<br>`NDSD = 0`<br>`IDLA = -1`; `src/ocpmix.ftn:1134–1138` `990 IF (ITEST.GE.100 .OR. IDLA.LT.0) THEN`<br>`DO 996 IY=MYA, 1, -1`<br>`WRITE (PRINTF, 994) (ARR(IX,IY), IX=1,MXA)`<br>`994 FORMAT ((1X, 10E12.4))`<br>`996 CONTINUE` | B | EOF·읽기 오류는 IDLA를 음수로 바꾸므로 `ITEST=0`이어도 echo한다. 정상 읽기의 echo 기준은 `ITEST≥100`이다. 배치 방향은 `idla=1`과 같다. git 이력: `8756667:src/ocpmix.ftn:1144` `990  IF (ITEST.GE.100 .OR. IDLA.LT.0) THEN`. 정상 입력의 `ITEST>=100` 조건과 오류 입력의 `IDLA<0` 조건은 최초 공개판부터 같다. 정상 입력 echo는 ITEST가 100 이상일 때 수행한다. 입력 오류는 ITEST와 별도로 echo를 유발한다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| inputs-setup:SI1-259 | LAYERS 파일 교체 시점 | swashuse PDF p.52 “SWASH reads the next file when the previous file end has been encountered.”; swashuse PDF p.55 같은 문장. | `src/SwashInputField.ftn90:394–396` `if ( k < ifllay(igr1) ) then`<br>`close(iflnds(igr1))`<br>`read (iflndf(igr1), '(a)', end=901) filenm`<br>`9d03fff:src/SwashInputField.ftn90:384–386` `if ( k < ifllay(igr1) ) then` / `close(iflnds(igr1))` / `read (iflndf(igr1), '(a)', end=901) filenm`. | A | LAYERS의 EOF 교체 설명은 10.05 이전 코드의 동작이다. `9d03fff 2024-05-07 initial release (v 10.05)`부터 층별 격자값을 읽은 뒤 다음 파일을 연다. 파일마다 한 층을 제공해야 한다. 직접 파일의 다층 읽기 문제는 SI1-260으로 구분한다. git 이력: `a79b2c6:src/ocpmix.ftn:1063` `!     *** End of data file, in case SERIES/LAYERS next file is opened`. 8756667의 LAYERS 문장부터 EOF 교체를 적는다. a79b2c6의 INAR2D는 `END=910`에서 파일을 닫고 다음 층 파일을 읽는다. 9d03fff은 이 처리를 층별 호출 뒤의 명시적 교체로 바꿨다. 12.01 문서는 이전 교체 시점을 유지한다. LAYERS의 EOF 교체 설명은 10.05 이전 코드의 동작이다. 10.05부터는 층별 격자값을 읽은 뒤 다음 파일을 연다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 정정] [10-15 git 이력 판정] |
| inputs-setup:SI1-260 | READTRANS/READAMB 단일 파일의 다층 입력 | swashuse PDF p.52·54 문법은 “’fname1’”과 “LAYers ’fname2’”를 선택지로 둔다. | `src/ocpmix.ftn:697–699` `ELSE`<br>`CALL INCSTR ('FNAME', FILENM, 'REQ', ' ')`<br>`ENDIF`; `src/SwashInit.ftn90:266` `iflndf(i) = 0`; `src/SwashInputField.ftn90:394–396` `if ( k < ifllay(igr1) ) then`<br>`close(iflnds(igr1))`<br>`read (iflndf(igr1), '(a)', end=901) filenm` | E·강함 | 해석: 직접 파일 이름을 쓰면 이름 목록 단위 `iflndf`는 0이다. 첫 층을 읽은 뒤 코드는 데이터 파일을 닫고 단위 0에서 다음 파일 이름을 읽는다. 단일 데이터 파일의 다음 층을 계속 읽지 않는다. LAYERS를 지정한 경로는 유효한 이름 목록 단위를 열므로 이 문제를 피한다. git 이력: `9d03fff:src/SwashInputField.ftn90:386` `read (iflndf(igr1), '(a)', end=901) filenm`. 후속 `608ffd7`·`9554c98`은 이 핵심 처리를 수정하지 않았다. READTRANS·READAMB의 다층 직접 파일 입력은 첫 층 뒤에 파일을 닫는다. 다음 층은 열지 않은 목록 장치에서 파일 이름을 읽으므로 E 후보로 유지한다. 판정은 E 유지(강함)이다. ([E1 판정표](../../../_staging/recovery/compare/SWASH-git-verify-E1.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] [10-15 전수 검증 정정] |
| inputs-setup:SI1-266 | INPAMB 계산층 수 또는 압력층 수 | swashuse PDF p.54 “number of vertical layers ... or the number of pressure layers ... or 1” | `src/SwashInputGrid.ftn90:305–307` `if (ifllay(igrid1) > kmax ) then`<br>`call msgerr (2, 'more than maximum number of layers encountered with ambient current input')`<br>`ifllay(igrid1) = kmax`; `src/SwashCheckPrep.ftn90:312` `if ( ifllay(20) /= kpmax .and. ifllay(20) /= 1 ) call msgerr (3, 'input field of ambient current has incorrect number of layers')` | B | 최종 검사에서 입력층 수는 kpmax 또는 1이어야 한다. SUBGRID에서 kmax와 kpmax가 다르면 kmax층 주변 흐름은 거부한다. 문서의 세 선택지 중 kmax가 항상 허용되는 것은 아니다. git 이력: `9d03fff:src/SwashCheckPrep.ftn90:307` `if ( ifllay(20) /= kpmax .and. ifllay(20) /= 1 ) call msgerr (3, 'input field of ambient current has incorrect number of layers')`. INPAMB를 도입한 9d03fff부터 허용 층 수는 kpmax 또는 1이다. 문서의 kmax 추가 선택지가 구현된 뒤 제거된 이력은 없다. 주변 흐름 입력층 수는 압력층 수 또는 1이어야 한다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| inputs-setup:SI1-503 | SET EPSHU·DEPMIN 연동 | swashuse PDF p.33–35 SET 문법에 EPSHU가 없다. | `src/SwashReadInput.ftn90:529` `chgdry = CHGVAL`; `src/SwashReadInput.ftn90:553–554` `call INREAL ('EPSHU', epshu, 'UNC', 0.)`<br>`if ( .not.CHGVAL .and. chgdry ) epshu = epsdry`; `src/SwashCheckPrep.ftn90:1219` `if ( inewt == 0 ) epshu = epsdry`<br>swashuse PDF p.155 Appendix C와 `misc/swash.edt:9`에는 `[epshu]`가 있다. | C | EPSHU 문법은 부록 C swashuse PDF p.155에 있다. DEPMIN을 바꾸고 EPSHU를 생략하면 `if ( .not.CHGVAL .and. chgdry ) epshu = epsdry`를 적용한다. 준비 단계의 `if ( inewt == 0 ) epshu = epsdry`는 별도의 덮어쓰기이다. C는 이 두 연동 조건의 설명 누락에 한정한다. [10-15 결론 검증 정정] [10-15 전수 검증 정정] |
| inputs-setup:SI1-511 | VERTICAL 등간격 판정 | swashuse PDF p.40은 층 비율을 적지만 부동소수점 판정식을 적지 않는다. | `src/SwashCheckPrep.ftn90:428` `if ( hlay(i)*real(kmax) /= 1. ) nonequi = .true.`; `src/SwashCheckPrep.ftn90:434` `if ( abs(sumh - 1.0) > eps ) then`; `src/SwashCheckPrep.ftn90:441` `if ( .not.bperc ) call msgerr (3, 'at least one layer with variable thickness is required')`<br>swashuse PDF p.40과 swashuse PDF p.127은 적어도 한 가변층이 필요하다고 설명한다. | C | 가변층 필수 조건과 두께 비율 합 100%는 문서에 있다. C는 비율 합의 eps 허용오차와 `hlay(i)*real(kmax) /= 1.`의 정확 비교에 한정한다. 근사 소수로 입력한 등간격 비율은 nonequi를 참으로 만들 수 있다. [10-15 결론 검증 정정] [10-15 전수 검증 정정] |
| inputs-setup:SI1-513 | 입력 격자 동일성의 간격 누락 | swashuse PDF p.20은 계산·입력 격자를 독립적으로 정의한다. swashuse PDF p.45는 dxinp·dyinp를 정의한다. | `src/SwashInputGrid.ftn90:376` `! check whether rectilinear input grid equals computational grid`; `src/SwashInputGrid.ftn90:388` `if ( xpg(igrid1) /= xpc .or. ypg(igrid1) /= ypc .or. alpg(igrid1) /= alpc .or. mxg(igrid1) /= mxc-1 .or. myg(igrid1) /= myc-1 ) lflgrd(igrid1) = .false.`; `src/SwashInit.ftn90:262` `lflgrd(i) = .true.`; `src/SwashCheckPrep.ftn90:2266–2269` `if ( lflgrd(1) ) then`<br>`dep = depth((iygl-1)*mxg(1)+ixgl)`<br>`else`<br>`dep = SVALQI (xp, yp, 1, depth, NEAREST)` | E·강함 | SPRCON은 영역·각도 조건을 검사한다 (`src/SwashCheckPrep.ftn90:948`; `src/swanser.ftn:1881–1932`). 더 큰 입력 간격으로 계산영역을 덮는 경우는 그 검사로 배제하지 않는다. 동일 원점·각도·점 수에서 입력 간격만 다르면 직접 인덱스 복사를 유지한다. 격자 동일성 주석 및 간격을 쓰는 SVALQI 경로와 모순된다. E·강함이다. git 이력: `8756667:src/SwashInputGrid.ftn90:366` `if ( xpg(igrid1) /= xpc .or. ypg(igrid1) /= ypc .or. alpg(igrid1) /= alpc .or. mxg(igrid1) /= mxc-1 .or. myg(igrid1) /= myc-1 ) lflgrd(igrid1) = .false.`. 후속 `608ffd7`·`9554c98`은 이 핵심 처리를 수정하지 않았다. 입력 격자 동일성 검사는 dxinp·dyinp를 비교하지 않는다. 간격만 다른 격자가 직접 인덱스 복사로 처리될 수 있으므로 E 후보로 유지한다. 판정은 E 유지(강함)이다. ([E1 판정표](../../../_staging/recovery/compare/SWASH-git-verify-E1.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] [10-15 전수 검증 정정] |
| inputs-setup:SI1-514 | 입력장 별칭 | swashuse PDF p.41–55은 대표 키워드를 적는다. | `src/SwashReadInput.ftn90:2413` `else if ( KEYWIS ('SHIP') .or. KEYWIS ('VESS') .or. KEYWIS ('WEC') .or. KEYWIS ('FLOAT') .or. KEYWIS ('DRAF') .or. KEYWIS ('PONT') .or. KEYWIS ('PFLOW') ) then`; `src/SwashReadInput.ftn90:2416` `else if ( KEYWIS ('LAB') .or. KEYWIS ('BODY') ) then`; `src/SwashReadInput.ftn90:2419` `else if ( KEYWIS ('ACUR') .or. KEYWIS ('BCUR') .or. KEYWIS ('CCUR') ) then` | C | DRAFT의 일곱 이름과 LABEL/BODY, ACURRENT/BCURRENT/CCURRENT를 같은 인덱스로 받는다. 명령 별칭을 별도 물리 모형으로 세지 않는다. |
| inputs-setup:SI1-515 | 동적 입력 추가 금지 목록 | swashuse PDF p.43은 일곱 입력량의 정상 조건을 적는다. | `src/SwashInputGrid.ftn90:267–273` `if ( igrid1 == 1  .or. igrid1 == 8  .or.                   &`<br>`     igrid1 == 10 .or. igrid1 == 11 .or. igrid1 == 12 .or. &`<br>`     igrid1 == 14 .or.                                     &`<br>`     igrid1 == 15 .or. igrid1 == 16 .or. igrid1 == 17 .or. &`<br>`     igrid1 == 19 .or.                                     &`<br>`     igrid1 == 20 .or. igrid1 == 21 .or. igrid1 == 22 .or. &`<br>`     igrid1 == 23 ) call msgerr (2, 'nonstationary input field not allowed in this case')`<br>swashuse PDF p.23은 성분의 경계 배경 농도를 정상 상태로 가정한다. swashuse PDF p.53은 ACURRENT·MWL을 파랑 운동의 시간 척도에서 일정하게 가정한다.<br>`src/SwashCheckPrep.ftn90:342–354`는 `.not.momskip`일 때 ifldyn(2)·ifldyn(3)·ifldyn(7)을 0으로 되돌린다. | C | 시간 의존 입력 금지는 swashuse PDF p.43의 목록 외에 swashuse PDF p.23의 성분 경계 가정과 swashuse PDF p.53의 주변 흐름·평균 수위 가정에도 나온다. C는 계산 좌표의 금지와 이들 입력량을 함께 거부하는 전체 검사 조건의 설명 누락에 한정한다. 파서의 허용 인덱스는 2·3·4·5·6·7·13·18이다. 대기압의 인덱스 13도 NONSTAT 금지 목록에 없다 (`src/SwashReadInput.ftn90:2398–2400`; `src/SwashInputGrid.ftn90:267–273`). 실제 속도·수위의 시간 갱신은 SKIPMOM 조건도 따른다. [10-15 결론 검증 정정] [10-15 전수 검증 정정] |
| inputs-setup:SI1-516 | 입력 시간 간격과 입력 시간 창의 정합성 경고 | swashuse PDF p.45–46은 시간 창·간격 정의를 적는다. 이 허용오차를 적지 않는다. | `src/SwashInputGrid.ftn90:287–289` `if ( mod(iflend(igrid1)-iflbeg(igrid1),iflint(igrid1)) > 0.01*iflint(igrid1) .and. &`<br>`     mod(iflend(igrid1)-iflbeg(igrid1),iflint(igrid1)) < 0.99*iflint(igrid1) )     &`<br>`  call msgerr (1, '[deltinp] is not a fraction of the period')` | C | 종료−시작을 간격으로 나눈 나머지가 간격의 1% 초과·99% 미만이면 경고한다. COMPUTE도 같은 1%·99% 규칙을 사용한다 (`src/SwashReadInput.ftn90:492–493`). 정확한 정수배만 허용하는 거부식은 아니다. [10-15 결론 검증 정정] [10-15 전수 검증 보완] |
| inputs-setup:SI1-517 | NONUNIFORM 허용량·1층 계산 금지·잘못된 층 수 보정 | swashuse PDF p.51·54은 층 수 선택을 적는다. | `src/SwashInputGrid.ftn90:295–297` `if ( kmax == 1 ) call msgerr (3, 'keyword NONUNIF not allowed in depth-averaged mode')`<br>`if ( igrid1 /= 15 .and. igrid1 /= 16 .and. igrid1 /= 17 .and. igrid1 /= 20 .and. igrid1 /= 21 ) then`<br>`call msgerr (2, 'this input parameter cannot be nonuniform in vertical')`; `src/SwashInputGrid.ftn90:302–303` `call msgerr (1, 'incorrect number of layers, input field now regarded as uniform')`<br>`ifllay(igrid1) = 1` | C | 연직 비균일 입력은 염분·수온·퇴적물·주변 흐름에 한정한다. 1층 계산에서 NONUNIFORM을 거부한다. 성분의 입력층 수가 kmax 또는 1이 아니면 1로 바꾼다. |
| inputs-setup:SI1-522 | LABEL 배율 강제 1 | swashuse PDF p.48은 fac 설명을 READINP 공통으로 준다. | `src/SwashInputField.ftn90:189–192` `if ( igr1 == 19 .and. iflfac(19) /= 1. ) then`<br>`call msgerr (1, 'for labelling rigid bodies, [fac] must be set to 1.0')`<br>`iflfac(19) = 1.`<br>`endif` | C | LABEL에 지정한 fac가 1이 아니면 경고 후 1로 고친다. LABEL에서 `fac=−1` 부호 반전 예를 적용하면 안 된다. |
| inputs-setup:SI1-523 | ADCIRC 바닥 읽기 재지정 | swashuse PDF p.39–40은 Triangle·Easymesh를 설명한다. ADCIRC의 바닥 읽기 선택은 이 명령 설명에 없다. | `src/SwashInputField.ftn90:226–230` `if ( igr1 == 1 .and. grid_generator == meth_adcirc ) then`<br>`call msgerr (1, 'depth will be taken from grid file fort.14 ')`<br>`igtype(1) = 3`<br>`leds(1)   = 2`<br>`return` | C | ADCIRC 격자에서 별도 READ BOTTOM을 요청하면 fort.14의 수심을 사용하고 별도 바닥 읽기를 끝낸다. [10-15 결론 검증 정정] |
| inputs-setup:SI1-524 | INAR2D 오류 sentinel·배율 복원 | swashuse PDF p.50은 오류 출력만 설명한다. | `src/ocpmix.ftn:1109–1112` `CALL MSGERR (2, 'Unexpected end of file while reading '//`<br>`     &                 TRIM(FILENM))`<br>`NDSD = 0`<br>`IDLA = -1`; `src/ocpmix.ftn:1120` `CALL MSGERR (2, 'Error while reading file '//TRIM(FILENM))`; `src/ocpmix.ftn:1123` `IDLA = -2`; `src/ocpmix.ftn:1130` `ARR(IX,IY) = ARR(IX,IY) * VFAC` | C | EOF는 `IDLA=−1`이다. 읽기 오류는 −2이다. 읽기 뒤 배율을 적용하고 음수 IDLA이면 자료를 출력한다. `fac=0` 문제는 SI1-229이다. |
| inputs-setup:SI1-526 | 최초 입력층·누락 다층 자료·파일 바꿈 | swashuse PDF p.52·55의 LAYERS 절차와 차이가 있다. | SI1-259·260의 원문 대조를 적용한다.<br>`src/SwashInputField.ftn90:236–237` `allocate( tarr(mxg(igr1)*myg(igr1)) )` / `tarr = 0.`. | C | 이 행의 C는 층 자료를 읽기 전에 임시 배열 tarr를 0으로 초기화하는 세부 처리에 한정한다. LAYERS의 파일 교체 시점은 SI1-259의 A를 따른다. 직접 파일의 다층 읽기는 SI1-260의 E를 따른다. [10-15 결론 검증 정정] |
| inputs-setup:SI1-529 | STEADY 채택 조건 | swashuse PDF p.55은 Chezy spinup을 설명한다. | `src/SwashCheckPrep.ftn90:405–415` `if ( instead .and. ( inituf .or. initvf ) ) then`<br>`call msgerr (1, 'flow velocities have been initialized, no steady flow condition')`<br>`instead = .false.`<br>`else if ( instead .and. .not.initsf ) then`<br>`call msgerr (1, 'water level should be initialized in case of steady flow condition')`<br>`instead = .false.`<br>`endif`<br>`!`<br>`if ( instead .and. irough == 4 .and. kmax > 1 ) then`<br>`call msgerr (1, 'no steady flow condition in case of logarithmic wall-law')`<br>`instead = .false.` | C | 초기 속도장이 있거나 초기 수위장이 없으면 STEADY를 끈다. 다층 로그 벽법칙도 STEADY를 끈다. |
| inputs-setup:SI1-530 | STEADY Froude 상한 | swashuse PDF p.55은 이 제한을 적지 않는다. | `src/SwashInitSteady.ftn90:157–159` `froude = abs(vel)/sqrt( grav * hu(nm) )`<br>`!`<br>`if ( froude > 0.9999 ) vel = ( 0.9999 / froude ) * vel` | C | 초기 Chezy 속도의 Froude 수가 0.9999를 넘으면 그 값으로 줄인다. 초임계 정상 초기해를 그대로 만든다고 쓰지 않는다. |
| inputs-setup:SI1-708 | `kspher=0`의 의미 | `models/SWASH/source-analysis/swash-initialization-grid.md:54` “`kspher=0`(직교)” | 불일치(B). `src/SwashReadInput.ftn90:581` `kspher = 0`은 CART 선택 경로이다. CURVILINEAR도 Cartesian 문제 좌표를 사용할 수 있다. | B | `kspher=0`은 평면 Cartesian 문제 좌표이다. 계산 격자의 직교성이나 직사각형 여부를 뜻하지 않는다. optg와 kspher를 나누어 적는다. |
| inputs-setup:SI1-709 | NONSTAT 금지·허용 목록의 반전 | `models/SWASH/source-analysis/swash-initialization-grid.md:79` “nonstationary 금지 검사(bottom 등 일부만 허용)” | 불일치(B). `src/SwashInputGrid.ftn90:267–273`의 완전한 연속문은 SI1-515에 인용했다. 첫 조건 `BOTTOM=1`을 금지 목록에 포함한다. `src/SwashReadInput.ftn90:2398–2400`의 대기압 인덱스 13은 이 금지 목록에 없다. | B | 파서의 NONSTAT 허용 입력량은 속도·마찰·바람·수위·대기압·흘수이다. 속도·수위의 실제 시간 갱신에는 SI1-515의 SKIPMOM 조건도 적용한다. BOTTOM·계산 좌표·공극률·입도·구조물 높이·식생 밀도·성분·LABEL·주변 흐름·평균 수위·Coriolis는 금지한다. git 이력: `8756667:src/SwashInputGrid.ftn90:255` `if ( igrid1 == 1  .or. igrid1 == 8  .or.                   &`. BOTTOM의 `igrid1=1`은 최초 공개판부터 NONSTAT 금지 조건에 들어 있다. 9.01·10.05·11.01 patch A는 금지 대상에 새 입력량을 더했다. BOTTOM을 허용했던 판의 설명으로 바꿀 근거는 없다. 파서의 NONSTAT 허용 입력량은 속도·마찰·바람·수위·대기압·흘수이다. 속도·수위의 실제 시간 갱신에는 SI1-515의 SKIPMOM 조건도 적용한다. BOTTOM·계산 좌표·공극률·입도·구조물 높이·식생 밀도·성분·LABEL·주변 흐름·평균 수위·Coriolis는 금지한다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) git 이력: `8756667:src/SwashInputGrid.ftn90:255` `if ( igrid1 == 1  .or. igrid1 == 8  .or.                   &`. BOTTOM의 `igrid1=1`은 최초 공개판부터 NONSTAT 금지 조건에 들어 있다. 9.01·10.05·11.01 patch A는 금지 대상에 새 입력량을 더했다. BOTTOM을 허용했던 판의 설명으로 바꿀 근거는 없다. NONSTAT 허용 입력량은 속도·마찰·바람·수위·대기압·흘수이다. BOTTOM·계산 좌표·공극률·입도·구조물 높이·식생 밀도·성분·LABEL·주변 흐름·평균 수위·Coriolis는 금지한다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 정정] [10-15 git 이력 판정] [10-15 전수 검증 정정] |
| theory-framework:ST1-232 | 번호 없는 공변 기저·계량 정의 | swashtech PDF p.57: `\boldsymbol\xi=(\xi^1,\xi^2)`; `\mathbf e_{(\alpha)}=\mathbf a_{(\alpha)}/\sqrt{g_{\alpha\alpha}}` (no sum); `\mathbf a_{(\alpha)}=\partial\mathbf x/\partial\xi^\alpha`; `g_{\alpha\alpha}=\mathbf a_{(\alpha)}\cdot\mathbf a_{(\alpha)}` | `src/SwashGeometrics.ftn90:204–205` `dx1 = 0.25*( xcgrid(ix+1,iy) + xcgrid(ix+1,iy-1) - xcgrid(ix-1,iy) - xcgrid(ix-1,iy-1) )`<br>`dy1 = 0.25*( ycgrid(ix+1,iy) + ycgrid(ix+1,iy-1) - ycgrid(ix-1,iy) - ycgrid(ix-1,iy-1) )`; `src/SwashGeometrics.ftn90:221` `gvu  (indx) = sqrt( dx1*dx1 + dy1*dy1 )` | F 표기 차이 | 해석: 좌표 차분 `(dx1,dy1)`은 길이 기저 `\mathbf a_{(1)}`의 이산 근사이다. 따라서 `gvu`는 `g_{11}`의 제곱근에 해당한다. 원문의 `\mathbf e_{(1)}=\mathbf a_{(1)}/\sqrt{g_{11}}`은 단위 기저이므로 그 노름을 `gvu`로 쓰면 안 된다. [10-15 결론 검증 정정] |
| theory-framework:ST1-265 | 좌표·기준면·번호 없는 기울기 | swashtech PDF p.63: `x,y,z`는 east·north·vertical; `\hat{\mathbf z}`는 위쪽; `\nabla=\left(\frac\partial{\partial x},\frac\partial{\partial y}\right)^{\mathsf T}`; `d` `positive downwards`, `\zeta` `positive upwards`, 기준 `z=0`. | `src/SwashGeometrics.ftn90:78–82` `dx1 = dx * cospc`<br>`dy1 = dx * sinpc`<br>`!`<br>`dx2 = -dy * sinpc`<br>`dy2 =  dy * cospc`; `src/SwashUpdateDepths.ftn90:113` `hs(nm) = s1(nm) + dps(nm)` | F 표기 차이 | 코드의 두 수평 성분은 격자 좌표 방향이다. 동·북에 정렬된 무회전 Cartesian 격자에서 문서의 성분과 직접 대응한다. 회전 격자는 공변 기저 방향에서 계산하고 성분을 변환한다. 수위·바닥의 양의 방향은 수심 합에 대응한다. [10-15 결론 검증 정정] |
| theory-framework:ST1-269 | 매개변수 기본값의 문서 상태 | swashtech PDF p.63–64: `\nu_h,c_f,c_d,g,\rho_{\mathrm{air}},\rho`의 의미만 제시한다. 이 쪽에는 기본값·범위·권장값이 없다. swashuse PDF p.34는 `[grav] = 9.81`, `[rhowat] = 1000.`, `[rhoair] = 1.205`를 적고 swashuse PDF p.75는 `[cd] = 0.002`를 적는다. | `src/SwashInit.ftn90:135–137` `grav   = 9.813`<br>`rhow   = -999.        ! reference density (subject to change)`<br>`rhoa   = 1.205`; `src/SwashInit.ftn90:293` `pwnd(1) = 0.002` | C 문서 누락 | C의 범위는 swashtech PDF p.63–64의 기본값 설명이다. 사용자 설명서에는 기본값이 있으므로 두 매뉴얼 전체의 누락으로 쓰지 않는다. 코드의 중력 초기값 9.813과 문서 표기는 ST1-343에서 구별한다. 물 밀도의 `-999.`는 미설정 표식이며 실제 확정은 ST1-292에 따른다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-278 | 제4장의 본문 누락 | swashtech PDF p.65: `This chapter is under preparation.` swashuse PDF p.37은 `CURVILINEAR`와 `READGRID COOR`를 설명한다. | `src/SwashGeometrics.ftn90:204–205` `dx1 = 0.25*( xcgrid(ix+1,iy) + xcgrid(ix+1,iy-1) - xcgrid(ix-1,iy) - xcgrid(ix-1,iy-1) )`<br>`dy1 = 0.25*( ycgrid(ix+1,iy) + ycgrid(ix+1,iy-1) - ycgrid(ix-1,iy) - ycgrid(ix-1,iy-1) )`; `src/SwashGeometrics.ftn90:221–223` `gvu  (indx) = sqrt( dx1*dx1 + dy1*dy1 )`<br>`guu  (indx) = sqrt( dx2*dx2 + dy2*dy2 )`<br>`gsqsu(indx) = dy2*dx1 - dy1*dx2` | C 문서 누락 | 곡선 격자의 유속 위치 계량식은 코드에 있다. C의 대상은 준비 중인 swashtech.pdf 제4장의 계량식·절차 설명이다. 사용자 설명서의 곡선 격자 입력 설명과 구별한다. 같은 판 번호만으로 판 차이를 배제하지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-292 | 기준 물 밀도의 확정 | swashtech PDF p.64는 물 밀도 기호를 정의한다. 초기화식 없음. swashuse PDF p.34는 `[rhowat] = 1000.` 뒤에 `this is usually the reference density`와 실제 밀도의 수온·염분 의존성을 설명한다. | `src/SwashInit.ftn90:143–145` `idens  = 0`<br>`tempw  = 14.`<br>`salw   = 31.`; `src/SwashCheckPrep.ftn90:894–899` `if ( idens == 0 .and. .not. rhow /= -999. ) then`<br>`!`<br>`pf0    =  5890d0  + (  38d0  - 375d-3*dble(tempw))*dble(tempw) +                        3d0*dble(salw)`<br>`lambda = 17795d-1 + (1125d-2 - 745d-4*dble(tempw))*dble(tempw) - (38d-1 + 1d-2*dble(tempw))*dble(salw)`<br>`! density based on Eckart is g/ml, hence multiply by 1000 to get g/l`<br>`rhow   = 1000.*pf0/(lambda+0.698*pf0)`; `src/SwashCheckPrep.ftn90:901–905` `else if ( .not. rhow /= -999. ) then`<br>`!`<br>`rhow = 1000.`<br>`!`<br>`endif`; `src/SwashReadInput.ftn90:534–536`은 `RHOWAT`·`TEMP`·`SALINITY`를 읽는다. `src/SwashCheckPrep.ftn90:889` `if ( lsal > 0 .or. ltemp > 0 .or. (lsed > 0 .and. lmixt) ) idens = 1`. | C 문서 누락 | C는 swashtech PDF p.64의 초기화식 설명에 한정한다. 사용자 설명서는 기준 밀도와 실제 밀도를 구별한다. 수송 설정에 따른 `idens` 확정 뒤 미설정 밀도만 처리한다. 일정 밀도 모드에서는 온도·염분식의 실제 밀도를 쓰고 다른 미설정 경로는 기준 밀도 1000을 쓴다. 이미 지정한 `RHOWAT`에는 이 두 대입을 적용하지 않는다. ST1-343과 같은 구분이다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-304 | 좌표 예외값 검사·곡선 격자 오프셋 | swashtech PDF p.65: `This chapter is under preparation.` swashuse PDF p.37–38은 EXCEPTION의 x·y 예외값을 설명한다. | `src/SwashInitCompGrid.ftn90:102–103` `if ( .not.EQREAL(ycgrid(i,j), excfld(9)) ) then`<br>`call msgerr (2, 'incorrect grid coordinates')`; `src/SwashInitCompGrid.ftn90:109–110` `if ( EQREAL(ycgrid(i,j), excfld(9)) ) then`<br>`call msgerr (2, 'incorrect grid coordinates')`; `src/SwashInitCompGrid.ftn90:125–126` `xcgrid(i,j) = real(xcgrid(i,j) - dble(xoffs))`<br>`ycgrid(i,j) = real(ycgrid(i,j) - dble(yoffs))`; 같은 파일 `src/SwashInitCompGrid.ftn90:100` `if ( EQREAL(xcgrid(i,j), excfld(8)) ) then`; `src/SwashInitCompGrid.ftn90:116` `if ( optg == 3 ) then`; `src/SwashInitCompGrid.ftn90:118–121`은 첫 유효 좌표를 `xoffs`·`yoffs`에 저장한다. | C 문서 누락 | C는 기술문서 제4장에 없는 검사와 오프셋 절차이다. 예외값 입력 자체는 사용자 설명서에 있다. x·y 중 하나만 예외값이면 오류를 낸다. 곡선 격자의 첫 유효점을 원점으로 옮기고 나머지 유효점에서 같은 오프셋을 뺀다. [10-15 결론 검증 보완] |
| theory-framework:ST1-305 | 가상 좌표 외삽·격자 검사 | swashtech PDF p.65: `This chapter is under preparation.` | `src/SwashInitCompGrid.ftn90:188` `if ( mcgrd <= 1 ) call msgerr (3, 'no valid grid points found')`; `src/SwashInitCompGrid.ftn90:194–198` `xcgrid(mxc,:) = 2.*xcgrid(mxc-1,:) - xcgrid(mxc-2,:)`<br>`ycgrid(mxc,:) = 2.*ycgrid(mxc-1,:) - ycgrid(mxc-2,:)`<br>`!`<br>`xcgrid(:,myc) = 2.*xcgrid(:,myc-1) - xcgrid(:,myc-2)`<br>`ycgrid(:,myc) = 2.*ycgrid(:,myc-1) - ycgrid(:,myc-2)`; `src/SwashInitCompGrid.ftn90:204` `if ( optg == 3 ) call CVCHEK ( KGRPGL, xcgrid, ycgrid )` | C 문서 누락 | 곡선 격자의 마지막 가상 행·열 좌표를 선형 외삽한다. 곡선 격자 검사를 호출한다. |
| theory-framework:ST1-306 | 위도 계량과 수위점 면적 | swashtech PDF p.42·52는 Hodge의 격자 계량 역할을 설명한다. 기존 swashtech PDF p.31 인용은 벡터값 미분형식의 설명이며 Hodge 계량식의 쪽이 아니다. 이 코드의 위도 보정과 수위점 면적 구성식은 해당 쪽에 없다. | `src/SwashGeometrics.ftn90:105` `coslat = cos(degrad*(0.5*(ycgrid(ix,iy)+ycgrid(ix,iy-1)) + yoffs))`; `src/SwashGeometrics.ftn90:113–115` `gvu  (indx) = sqrt( coslat*coslat*dx1*dx1 + dy1*dy1 )`<br>`guu  (indx) = sqrt( coslat*coslat*dx2*dx2 + dy2*dy2 )`<br>`gsqsu(indx) = coslat * ( dy2*dx1 - dy1*dx2 )`; `src/SwashGeometrics.ftn90:325–328` `dx1 = 0.5 * ( gvv(indx) + gvv(indxb) )`<br>`dy1 = 0.5 * ( guu(indx) + guu(indxl) )`<br>`!`<br>`gsqs(indx) = dx1 * dy1` | C 문서 누락 | C의 범위는 기술문서 swashtech PDF p.42·52의 구체 계량 구성식이다. 인용한 정규 구면 격자 분기는 위도의 cosine을 x방향 계량에 적용한다. 수위점 면적은 맞은편 변 길이 평균의 곱이다. 일반 비직교 사변형의 정확한 면적이라는 결론으로 확대하지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-328 | 자유수면 경계면과 최상층 | `source-analysis/swash-initialization-grid.md:185` `! 최상층 = 바닥 + 수심 = 자유수면` | `src/SwashLayerIntfaces.ftn90:46–48` `!   In the vertical direction the computational domain is divided into a fixed number`<br>`!   of layers of which the k-index has range (0,1,...,kmax) and counting downward from`<br>`!   the free surface.`; `src/SwashLayerIntfaces.ftn90:76` `zks(:,0) = -dps(:) + hs(:)`; `src/SwashLayerIntfaces.ftn90:84` `hks(:,k) = zks(:,k-1) - zks(:,k)` | B 문서 오기 (현재 노트) | `zks(:,0)`는 자유수면 경계면이다. 최상층은 두 경계면 0·1 사이의 층 1이다. 경계면 인덱스와 층 인덱스를 구별한다. `8756667:src/SwashLayerIntfaces.ftn90:46–48,76,84`부터 현재까지 방향·수면 경계·두께 식이 같다. 층 인덱스 변경이 아닌 기존 노트의 표현 오기이다. [git 판정 AD §3](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)의 B를 유지한다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| theory-unstructured:ST2-358 | 물리·마름·미소 유속의 초기값 | swashuse PDF p.33–35는 물리 상수·마름 문턱을 설명한다. swashuse PDF p.73·76·78·83은 각 물리 명령의 활성화를 설명한다. | `src/SwashInit.ftn90:121–123` `epsdry = 5.e-5`, `epshu  = 1.e-3`, `epsuf  = 1.e-8`; `src/SwashInit.ftn90:135–139` `grav   = 9.813`, `rhow   = -999.        ! reference density (subject to change)`, `rhoa   = 1.205`, `dynvis = 1.e-3`, `vonkar = 0.4`; `src/SwashInit.ftn90:151` `ihvisc = 0`; `src/SwashInit.ftn90:291` `iwind   = 0`; `src/SwashInit.ftn90:307` `coriolis = .false.`; `src/SwashInit.ftn90:313` `irough = 0` | C 문서 누락 | `rhow=-999.`는 후속 결정용 표지다. 물의 밀도 기본값으로 인용하지 않는다. 바닥 마찰·바람 응력·코리올리·수평 점성은 이 초기화에서 꺼져 있다. C는 epsuf와 후속 결정용 밀도 표지 등 내부 초기화에 한정한다. 이 초기 플래그를 입력 처리 뒤의 활성 상태로 해석하지 않는다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-382 | 층 방향·계면·세 종류 면 두께 | swashtech PDF p.109는 3차원 장이 비어 있다고 적는다. swashuse PDF p.40은 층 번호가 위에서 아래로 증가한다고 명시한다. | `src/SwashLayUIntfaces.ftn90:44–46` `!   In the vertical direction the computational domain is divided into a fixed number`, `!   of layers of which the k-index has range (0,1,...,kmax) and counting downward from`, `!   the free surface.`; `src/SwashLayUIntfaces.ftn90:72` `zks(:,0) = -dps(:) + hs(:)`; `src/SwashLayUIntfaces.ftn90:80` `hks(:,k) = zks(:,k-1) - zks(:,k)`; `src/SwashLayUIntfaces.ftn90:97` `hkumn(:,k) = zkum(:,k-1) - zkum(:,k)`; `src/SwashLayUIntfaces.ftn90:115–116` `hku (:,k) = zku (:,k-1) - zku (:,k)`, `hkum(:,k) = zkum(:,k-1) - zkum(:,k)` | C 문서 누락 | 계면 `k=0`은 자유수면이다. 층 `k=1`은 최상층이다. 층 `k=kmax`는 최하층이다. 이 방향은 사용설명서와 일치한다. hku는 질량 플럭스용 hu에서 만든다. hkum은 가중 수심 hum에서 만든다. hkumn은 시간 외삽 수심 humn에서 만든다. hu의 중심 선택·고차 보정은 ST2-353·354와 같다. C는 이 세 면 두께를 따로 만드는 구현에 한정한다. [10-15 결론 검증 정정] |
| theory-unstructured:ST2-383 | sigma·고정층·얕은 수심의 대체 sigma | swashuse PDF p.40은 가변층·고정층 입력과 sigma 층을 설명한다. 같은 쪽은 비구조 격자의 고정 두께 층을 지원 범위에서 제외한다. swashtech PDF p.109에는 층 분포식이 없다. | `src/SwashServices.ftn90:531` `if ( .not.fixlay ) then`; `src/SwashServices.ftn90:540` `zk(j+ntot) = zk(j) - h(n) * hlay(k)`; `src/SwashServices.ftn90:551` `if ( h(n) > depfix ) then`; `src/SwashServices.ftn90:557` `if ( indlay(k) == 1 ) then`; `src/SwashServices.ftn90:563` `zk(j+ntot) = zk(j) - (h(n) - depfix) * hlay(k)`; `src/SwashServices.ftn90:571` `zk(j+ntot) = zk(j) - hlay(k)`; `src/SwashServices.ftn90:585` `zk(j+ntot) = zk(j) - h(n) * hlaysh(k)`; `src/SwashReadInput.ftn90:1798–1804`는 M·PERC를 `indl=2`·1로 읽는다. `src/SwashCheckPrep.ftn90:447–450`은 indlay에서 fixlay를 정한다. `src/SwashLayUIntfaces.ftn90:74,91,108–109`는 sigmacoor를 호출한다. | C 문서 누락 | 공유 sigmacoor는 가변층에서 수심 비율로 계면을 내린다. fixlay 분기는 고정층 총두께를 뺀 수심에 가변층 비율을 적용한다. 총수심이 고정층 총두께 이하이면 hlaysh를 사용한다. C는 공유 루틴의 계면식과 얕은 수심 대체식에 한정한다. 이 분기의 존재를 비구조 고정층의 문서상 지원으로 넓혀 쓰지 않는다. [10-15 결론 검증 정정] |
| theory-unstructured:ST2-422 | 구조 격자의 분할·블록 관리 | swashuse PDF p.144는 MPI 영역 분할의 일반 원리를 설명한다. swashtech PDF p.117 및 사용설명서의 해당 설명에는 아래 자동 분할 선택과 블록 크기 계산이 없다. | `src/SwashInitCompGrid.ftn90:240–241`의 `PARLL` 및 `kpart < 0 .or. kpart > 4` 조건 아래 `src/SwashInitCompGrid.ftn90:243–247` `if ( .not.oned .and. kmax > 1 ) then`, `LORB = .true.`, `else`, `LORB = .false.`, `endif`; `src/SwashInitCompGrid.ftn90:265` `call SWDECOMP`; `src/swanparll.ftn:3520` `      IF (.NOT.PARLL) RETURN`; `src/swanparll.ftn:3527` `      CALL SWPARTIT( IPOWN, MXC, MYC )`; `src/swanparll.ftn:3532` `      CALL SWBLADM( IPOWN, MXC, MYC )`; `src/swanparll.ftn:3542–3543` `      MXC = MXL - MXF + 1`, `      MYC = MYL - MYF + 1` | C 문서 누락 | 자동 분할은 2차원 다층에서 ORB를 선택한다. 다른 자동 경우에는 띠 분할을 선택한다. 분할 뒤 각 프로세스의 국소 격자 크기를 계산한다. 이는 구조 격자 경로다. [10-15 결론 검증 보완] [10-15 전수 검증 보완] |

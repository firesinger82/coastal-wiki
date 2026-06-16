---
title: "SWASH 출력 시스템 — dispatch·QuanOutp 물리량·VTK·평균·backup·메모리 정리"
model: SWASH
component: src (output)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashOutput.ftn90 dispatch 루프(:122-257), SwashQuanOutp.ftn90 물리량 분기(oqproc 1~94, :184-3576), SwashElemOutp.ftn90 mesh 출력(:88-122), SwashReqOutQ.ftn90 BLOCK 키워드 목록(:110-231), SwashDecOutQ.ftn90 시간 판정(:113-158), SwashAverOutp.ftn90 시간평균식(:83-194), SwashCoorOutp.ftn90 좌표변환(:114-331), SwashVTKWriteHeader/WriteData/PDataSets.ftn90, SwashBackup.ftn90 hotstart 포맷(:91-307), SwashCleanMem.ftn90 deallocate 목록 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 출력 시스템 — dispatch·QuanOutp 물리량·VTK·평균·backup·메모리 정리

> 출력 요청(TABLE/BLOCK/POINTS 등)을 처리해 물리량을 계산·보간·기록하고, hotstart backup 및 종료 시 메모리 정리를 담당하는 서브시스템. (경로: raw/source_code/swash/src/)

SWASH 출력은 두 축으로 분리된다 — **출력 위치 집합**(point set, `opsdat`)과 **출력 요청**(request, `orqdat`). 요청 하나는 한 위치 집합 + 하나 이상의 출력 quantity를 참조한다. 이 자료구조 설명은 `SwashOutput.ftn90:46-54` Method 주석에 verbatim으로 명시되어 있다.

## 1. 출력 dispatch — SwashOutput

`SwashOutput.ftn90`(268줄)은 모든 출력 요청을 순회하는 dispatcher다. Purpose 주석: `"Processes output requests"`(`SwashOutput.ftn90:40`).

핵심 루프 `reqloop`(`:123-257`)의 단계:

| 단계 | 호출 | file:line |
|---|---|---|
| 출력 quantity 디코드 + 시간 판정 | `SwashDecOutQ` | `SwashOutput.ftn90:133` |
| `logact=.false.`면 skip | `cycle reqloop` | `:134-137` |
| point set 검색 (`FOPS` 연결리스트) | `cuops` 순회 | `:143-153` |
| 출력 point set 디코드 | `SwashDecOutL` | `:161` |
| voq/voqk/ionod 메모리 할당 | `allocate` | `:173-179` |
| 출력점 좌표 계산 | `SwashCoorOutp` | `:189` |
| 물리량 계산 (격자점) | `SwashQuanOutp` | `:197` |
| 물리량 계산 (mesh 요소, `ELEMESH`) | `SwashElemOutp` | `:203` |
| 공간 독립 시계열 (load/runup) | `SwashFlobjOutp`/`SwashRunupHeight` | `:213-217` |
| 실제 기록 dispatch | `SWBLKV`/`SWBLKP`/`SWBLOK`/`SWTABP` | `:228-252` |
| 메모리 해제 | `deallocate` | `:254` |

기록 dispatch는 `rtype`에 따라 분기된다(`:228-252`):

- `rtype(1:3)=='BLK'` → block 출력. 세분: `'BLKV'`(VTK)이면 `SWBLKV`, 병렬+`IMRGE==1`이면 `SWBLKP`, 그 외 `SWBLOK`(`:232-238`).
- `rtype(1:3)=='TAB'` → table 출력 `SWTABP`(`:241-245`).

`voq`는 한 quantity당 1~2열(벡터는 2열), 한 행=한 위치이며, `voqr`이 각 quantity가 voq의 몇 번째 열에 저장됐는지 가리킨다(`SwashOutput.ftn90:99-103` Structure 주석 verbatim). 좌표 보간 여부는 frame/heading(`'F'`/`'H'`)일 때만 `outpar(3)=cuops%opr(6)`, 그 외 0(`:166-170`).

`ELEMESH`(unstructured mesh)와 `NOGRID`(공간 독립)는 별도 경로다(`:193-219`). `nreoq==0`이면 `'no output requested'` 경고 후 return(`:114-117`).

## 2. 출력시간 판정 — SwashDecOutQ

`SwashDecOutQ.ftn90`(345줄) Purpose: `"Decodes output quantities"`(`:40`). 비정상(dynamic) 모드에서 출력 시점을 결정한다.

판정 로직(`:113-140`, Structure 주석 `:85-105`에 의사코드):

- `dif = tfinc - timco`(종료까지 잔여, `:115`).
- **출력 간격 음수**(종료 시점만 출력): `abs(dif) < 0.99*dt` 일 때 `logact=.true.`(`:127-129`).
- **출력 간격 양수**: `.not. real(timco) < real(tnext)` 이면 `logact=.true.`, 다음 출력시각 `outr(1)=tnext+outr(2)`(`:130-132`).
- 그 외 `logact=.false.` 후 즉시 return(`:133-136`).
- 출력 발생 시 VTK 카운터 증가 `ntvtk(outi(2))=ntvtk(outi(2))+1`(`:137`).

정상(stationary) 모드는 무조건 `logact=.true.`(`:138-140`). 디코드 시작 시 `voqr=0`, `oqproc=.false.` 초기화(`:146-147`), Xp/Yp 등 좌표는 항상 처리(`oqproc(1)=.true.`, `:157`). 다중 quantity 시 `ovsvty>4`를 4로 reset(`:151-153`).

## 3. 물리량 계산 — SwashQuanOutp (3577줄, 핵심)

Purpose: `"Calculates requested output quantities in the output points"`(`SwashQuanOutp.ftn90:43`). 출력변수는 고정 정수번호로 식별되며, `oqproc(n)`이 .true.인 quantity만 계산한다.

### 3.1 quantity 그룹 판정

도입부에서 어떤 보조량을 사전 계산할지 그룹 플래그를 세운다:

- `reqzsc`(layer-dependent 스칼라; 연직속도·압력 등) — `oqproc(52..59,82,83,89..94)`(`:193-200`).
- `reqzvl`(layer-dependent 속도/유량) — `oqproc(72..81,84..88)`(`:204-210`).
- `reqvel`(속도/유량) — `oqproc(7..18,31..37,45)` 또는 `reqzvl`(`:214-222`).

`reqvel .and. optg/=5`일 때 수심평균 속도·유량을 사전 계산(`:226`이하). 보조배열 `oparr`/`oparrk`를 0으로 초기화(`:188-189`).

### 3.2 출력 quantity 번호 ↔ 물리량 (대표)

번호는 소스 주석 + BLOCK 키워드 목록(아래 §6)에서 확인. 대표 매핑과 계산 위치:

| # | 물리량 | 계산 file:line | 비고 |
|---|---|---|---|
| 1,2 | Xp, Yp (사용자 좌표) | `SwashDecOutQ:157` 등 | 항상 처리 |
| 3 | distance (곡선 누적거리) | `:2358-2373` | spherical 보정 `lendeg·cos` (`:2365-2367`) |
| 4 | water depth | `:2377-2383` | `SWIPOL` 보간 |
| 5 | bottom level (BOTL) | `:2387-2403` | 비활성점 포함 보간(`epsdry=-99999`) |
| 6 | water level (WATL, $\zeta$) | `:2407-2413` | |
| 7 | velocity magnitude | `:2437-2445` | $\sqrt{u^2+v^2}$ |
| 8 | velocity direction | `:2449-2471` | `atan2`, nautical/Cartesian 변환 `DEGCNV` |
| 9 | flow velocity u,v | `:2417-2433` | 격자→사용자 좌표 회전 `coscq/sincq`(`:2430-2431`) |
| 12 | non-hydrostatic pressure at bottom | `:2489-2499` | `ihydro==0`이면 예외값 |
| 13 | pressure at bottom | `:2503-2511` | |
| 16 | specific discharge q (벡터) | `:2513-2531` | 좌표 회전 동일 |
| 41 | time (TSEC) | `:2354` | `real(timco)-outpar(1)` |
| 51 | layer interface z-level (ZK) | `:2951-2971` | `k=0..kmax` |
| 52 | physical vertical velocity (VZ) | `:2975-2985` | `oparrk(:,k,12)` |
| 53 | relative vertical velocity (VOMEGA) | `:2989-2999` | `oparrk(:,k,11)` |
| 54,55 | TKE, EPS | `:3003-3035` | `iturb==0`이면 예외값 |
| 56 | vertical eddy viscosity | `:3039-3049` | |
| 57,58,59 | mean TKE/EPS/visc | `:3053-3099` | |
| 71 | layer thickness (HK) | `:3103+` | 비활성점 포함 |
| 82 | layer-dependent non-hydrostatic pressure | `:3303-3317` | `ihydro==1/2`만 |
| 83 | layer-dependent pressure | `:3321-3331` | |
| 84,85,86 | mean layer velocity mag/dir/u,v | `:3335-3399` | 86이 벡터, 좌표회전(`:3349-3356`) |
| 87,88 | mean grid-oriented U/V per layer | `:3403-3419` | |
| 89,90,91 | layer salinity/temperature/sediment | `:3423-3491` | |
| 92,93,94 | mean layer sal/temp/sed | `:3495-3533` | |

### 3.3 보간·좌표 처리 메커닉

- **구조격자**(`optg/=5`): `SWIPOL`로 보간(예 `:2379`). 비활성점에서도 값이 필요한 경우(BOTL·ZK·sal 등) 일시적으로 `epsdry=-99999`로 바꿔 모든 점 보간(`:2390-2393`, `:3106-3110`).
- **비구조격자**(`optg==5`): `SwanInterpolateOutput`(예 `:2381`). 비활성 vertex 포함 출력 시 `vert(:)%active=.true.`로 일시 변경 후 복원(`:2396-2401`).
- **속도/유량 좌표 회전**: 격자방향 성분을 사용자 좌표계로 `coscq·u - sincq·v`, `sincq·u + coscq·v`로 회전(`:2430-2431`, `:2528-2531`, `:3353-3354`).
- **방향**: `bnaut`(nautical) 여부로 `atan2` 처리 후 `DEGCNV`로 Cartesian/nautical 변환(`:2456-2465`).

마지막에 좌표 offset 보정(`voq(i,1)+xoffs`, `:3537-3542`)과 병렬 시 자기 subdomain 내부점 마킹(`ionod(i)=INODE`, `:3546-3571`)을 수행한다.

## 4. mesh 요소 출력 — SwashElemOutp

`SwashElemOutp.ftn90`(754줄) Purpose: `"Calculates requested output quantities that are stored in mesh elements"`(`:40`). `ELEMESH` point set 전용으로, 보간 없이 셀 중심값을 직접 대입한다.

- water depth `voq(:,voqr(4))=hs(:)`(`:94`), bottom level `=dps(:)`(`:98`), water level `=s1(:)`(`:102`).
- non-hydrostatic pressure at bottom: `ihydro/=0`이면 `q(:,kmax)`, 아니면 예외값(`:106-112`).
- **bottom pressure** 식(`:116-122`): `ihydro==0`이면 $p_b = 0.01\,\rho_w g\,h_s$, 비정수압이면 $p_b = 0.01\,\rho_w (g\,h_s + q_{kmax})$ — 계수 0.01은 단위 환산(`:118,120`). 정수압 + 비정수압 압력의 합으로 해석됨.
- 발산 연산자(95,96) 출력 시 `chkdiv` 선행 호출(`:90`).
- 수심평균 속도는 면 기반 `hku·u1` 적분 후 `hu`로 정규화(`:136-150`).

## 5. 시간평균 출력 — SwashAverOutp

`SwashAverOutp.ftn90`(195줄) Purpose: `"Computes setup, wave height, mean current, mean constituents and mean turbulence quantities for output purposes"`(`:40`). Method 주석(`:44-46`): 시뮬레이션 최종 구간에서 시간평균하며, steady-state 확립을 위해 충분히 긴 기간을 가정.

`iquan` 인자로 갱신 유형 구분(`:61-64`): 1=표고/속도, 2=transport constituent, 3=turbulence.

| 평균량 | 누적식 | 최종화 file:line |
|---|---|---|
| setup ($\bar\zeta$) | `setup += s1` (dry점 0) | `setup/nwavoutp`, `:117-123` |
| wave height $H_s$ | `etavar += s1²` | $H_s = 4\sqrt{\max(\overline{\zeta^2}/(n-1)-\bar\zeta^2,\,0)}$ `:121` |
| mean current | `mvelu += u1`, `mvelv += v1` | `/ncuroutp`, `:127-147` |
| mean constituents | `mcons += rp` | `/ntraoutp`, `:149-171` |
| mean turbulence | `mtke += rtur(1)`, `meps += rtur(2)` | `/nturoutp`, `:173-193` |

핵심: $H_s$는 표고분산의 제곱근에 4를 곱한 표준 정의(`:121`). 누적은 `dif > t*outp`가 아닐 때(최종 구간)만, 최종화는 `abs(dif) < 0.99*dt`(마지막 스텝)에 1회 수행(`:89,117` 등). 어느 quantity가 평균 대상인지는 ReqOutQ에서 `lwavoutp`/`lcuroutp`/`ltraoutp`/`lturoutp` 플래그로 설정됨(§6 참조).

## 6. BLOCK 키워드 목록 — SwashReqOutQ

`SwashReqOutQ.ftn90`(525줄) Purpose: `"Reading and processing of the output quantities"`(`:42`). BLOCK 명령 주석(`:110-119`)에 전체 출력 quantity 키워드가 verbatim 나열된다:

```
TSEC|XP|YP|DEP|BOTL|WATL|DRAF|VMAG|VDIR|VEL|VKSI|VETA|
PRESS|NHPRES|QMAG|QDIR|DISCH|QKSI|QETA|VORT|WMAG|WDIR|WIND|
FRC|USTAR|UFRIC|ZK|HK|VMAGK|VDIRK|VELK|VKSIK|VETAK|
VZ|VOMEGA|QMAGK|QDIRK|DISCHK|QKSIK|QETAK|PRESSK|NHPRSK|
TKE|EPS|VISC|HS|HRMS|SETUP|MVMAG|MVDIR|MVEL|MVKSI|MVETA|
MVMAGK|MVDIRK|MVELK|MVKSIK|MVETAK|MTKE|MEPS|MVISC|
SAL|TEMP|SED|MSAL|MTEMP|MSED|SALK|TEMPK|SEDK|MSALK|MTEMPK|
MSEDK
```

`svartp`가 키워드→`ivtype` 정수번호 변환(`:199`). BLOCK은 frame/heading/unstructured(`'F'/'H'/'U'`)만 허용(`:127-130`).

**출력 파일 종류 판정**(`:144-163`):
- HEAD/NOHEAD/FIL → `rtype='BLKP'`(헤더有)/`'BLKD'`(헤더無).
- `.MAT`(Matlab) → 헤더 금지(`:154-157`).
- `.VT*`(VTK) → `rtype='BLKV'`, `dfac=1`(`:159-163`).

**평균 quantity 플래그 설정**(`:226-231`): HRMS/SETUP 류(`ivtype==22/23/24`)→`lwavoutp`, 평균 current(`33-37`,`84-88`)→`lcuroutp`, mean constituent(`42-44`,`92-94`)→`ltraoutp`, mean turbulence(`57-59`)→`lturoutp`.

**경고 조건**(`:203-217`): div 연산자는 unstructured만, layer-dependent quantity는 `kmax==1`이면 출력 안함, 격자방향 속도(`10,11,75,76`)는 `optg==5`(unstructured)에서 출력 안함.

> source-needed: `svartp`의 키워드↔ivtype 정확한 매핑표와 `OVKEYW`/`OVSNAM` 정의는 `SwashInit`(미배정 파일)에 있어 본 노트 범위 밖. `SwashOutput.ftn90:52-54` 주석은 "1=Xp, 2=Yp, 6=water level, 7=velocity"임을 명시하며, 위 §3.2 매핑은 QuanOutp의 코드 동작·주석에서 직접 검증함.

## 7. VTK writer (ParaView 출력)

41.95(2022년 7월) 추가된 3개 서브루틴. 모두 Method 주석에 VTK file-format 명세 URL을 인용(`https://vtk.org/wp-content/uploads/2015/04/file-formats.pdf`).

### 7.1 SwashVTKWriteHeader (382줄)
Purpose: `"Writes header to a VTK file"`(`:40`). XML/binary appended 포맷. 그리드 타입을 point set으로 분기:
- frame/heading(`'F'/'H'`) → `StructuredGrid`(`:131`), `WholeExtent`에 글로벌 인덱스 기록(`:134-149`).
- unstructured(`'U'`) → `UnstructuredGrid`(`:153-157`).

파라미터: `datasize=4`(int/real 바이트), `ndim=3`(Paraview 요구), `nov=3`(삼각형 정점 수)(`:72-76`). 헤더에 SWASH 버전·project·run 번호 기록(`:123`).

### 7.2 SwashVTKWriteData (274줄)
Purpose: `"Writes appended data to a VTK file"`(`:40`). quantity별 binary append:
- 스칼라(`ovsvty<3`)는 `nbytes=lenp*datasize`(`:127-129`).
- 데이터는 `real*4`로 기록(`:71-72`), 병렬 시 `ionod(ip+i)==iproc`인 자기 subdomain 점만 기록(`:137`).
- 셀 타입 `ptype=5`(triangle)(`:82`).

### 7.3 SwashVTKPDataSets (379줄)
Purpose: `"Writes parallel VTK file type"`(`:40`). 병렬 실행 시 PVD(시간계열) + 병렬 VTK(`.pvts`/`.pvtu`) 메타파일을 생성해 subdomain별 piece 파일을 링크(`:62-71`). frame은 `iarr(4,0:NPROC-1)`로 subdomain별 격자 인덱스 수집(`:65`).

## 8. Hotstart backup — SwashBackup

`SwashBackup.ftn90`(389줄) Purpose: `"Backups current state of the flow variables to a file"`(`:40`). `HOTFile 'fname'` 명령 처리(`:87`).

**파일 헤더 포맷**(SWASH standard file, `:101`이하):
- 시간 코딩(`nstatm==1`), 좌표계(`kspher==0`→Cartesian `LOCATIONS`, 아니면 `LONLAT`)(`:106-112`).
- 위치 수: 구조격자 `(mxc-1)*(myc-1)`(`:114`), unstructured `nverts`(`:125`). 좌표는 offset 더해 double로 기록(`:118-127`).
- 연직 층(`kmax>1`): `ZK` 스키마, `indlay(k)`+`hlay(k)`(`:131-139`).
- quantity 헤더 개수: 1D/2D × single/multi-layer 조합으로 3/4/5/7(`:141-153`).

**flow 변수 기록**(`:209-296`): 격자점별로 비활성점은 `'NODATA'`(`:220-222`), 활성점은 bottom level `dps`(`:230`), water level `s1`(`:234`), 수심평균/층별 u·v(`:238-291`). 층별 속도는 `efac=max(abs(u1))*1e-5`로 정규화한 정수로 압축 기록(`:252-258`), 전부 0이면 `'ZERO'`(`:253-254`). 병렬 시 파일명에 node 번호 append(`:93-96`).

## 9. 좌표 변환 — SwashCoorOutp

`SwashCoorOutp.ftn90`(340줄) Purpose: `"Calculates grid coordinates of the output points"`(`:40`). point set 타입별 출력점 사용자좌표(xp,yp)와 계산격자 broken 좌표(xc,yc) 산출.

- **Frame(`'F'`)**: 회전각 `alpq`로 `cospq/sinpq`, 격자간격 `dxq=xqlen/(mxq-1)`, 회전된 격자 생성(`:114-153`).
- **Heading(`'H'`)**: 계산좌표 직접 범위 + `EVALF`로 물리좌표 역산(`:155-253`).
- **Curve/Point/NoGrid/Unstructured(`'C'/'P'/'N'/'U'`)**: `xp=x, yp=y` 그대로(`:255-260`).

broken 좌표 변환은 격자 타입 의존(`:269-331`):
- rectilinear(`optg==1`): $x_c = (x_{cp} + x_p\cos + y_p\sin)/dx - M_{XF}+1$(`:273-274`), 1D는 `yc=0`(`:276-277`).
- curvilinear(`optg==3`): `CVMESH` 호출 전후로 글로벌 격자 메타데이터를 임시 교체(`:287-329`).

## 10. 메모리 정리 — SwashCleanMem

`SwashCleanMem.ftn90`(563줄) Purpose: `"Cleans memory"`(`:40`). 종료 시 모든 allocatable 배열을 `if(allocated(...)) deallocate(...)` 패턴으로 해제(예 `:62-128`).

해제 대상은 격자(`kgrpnt,xcgrid,ycgrid,guu/gvv/gsqs...` `:63-73`), 층 스키마(`indlay,hlay,hlaysh` `:74-76`), 경계(`bndval` `:77`), flow 필드 현재값(`depth,wlevl,pres,corp,npor,sal,temp,sed...` `:78-98`), 출력 보조 필드(접미사 `f`: `depf,wlevf,presf,salf...` `:99-118`), 식생(`cdveg,bveg,nveg` `:120-122`), 이전 시간단계(`s0,u0,v0,w0bot...` `:123-128`) 등 다수 모듈(`outp_data,m_genarr,SwashFlowdata,SwashSolvedata,SwashRigBoddata` `:44-52`) 배열에 걸친다.

## 11. 요약 — 출력 데이터 흐름

```
SwashOutput (dispatch loop)
  ├─ SwashDecOutQ   : 시간판정 + oqproc/voqr 결정
  ├─ SwashDecOutL   : point set 디코드
  ├─ SwashCoorOutp  : 출력점 좌표(xp,yp,xc,yc)
  ├─ SwashQuanOutp  : oqproc(1..94) 물리량 → voq/voqk (SWIPOL 보간)
  │    or SwashElemOutp (ELEMESH: 셀값 직접)
  └─ 기록: SWBLOK/SWBLKP/SWBLKV(VTK)/SWTABP
SwashAverOutp : 시간평균(setup/Hs/mean current/constituent/turbulence)
SwashBackup   : hotstart 파일 (HOTFile)
SwashCleanMem : 종료 시 deallocate
```

핵심 설계: (1) **위치-요청 직교 분리**(`opsdat`/`orqdat`)로 한 위치에 다중 quantity·다중 출력형식 지원, (2) **oqproc 플래그 + 정수 quantity 번호**로 ~94종 출력변수를 단일 큰 분기로 처리, (3) 구조격자는 `SWIPOL`·비구조격자는 `SwanInterpolateOutput`로 보간 추상화, (4) VTK는 41.95(2022)에 ParaView 지원으로 추가된 별도 binary-append writer.

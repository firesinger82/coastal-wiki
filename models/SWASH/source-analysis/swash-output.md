---
title: "SWASH 출력 시스템 — dispatch·QuanOutp 물리량·VTK·평균·backup·메모리 정리"
model: SWASH
component: src (output)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashOutput.ftn90 dispatch 루프(:122-257), SwashQuanOutp.ftn90 물리량 분기(oqproc 1~94, :184-3576), SwashElemOutp.ftn90 mesh 출력(:88-122), SwashReqOutQ.ftn90 BLOCK 키워드 목록(:110-231), SwashDecOutQ.ftn90 시간 판정(:113-158), SwashAverOutp.ftn90 시간평균식(:83-194), SwashCoorOutp.ftn90 좌표변환(:114-331), SwashVTKWriteHeader/WriteData/PDataSets.ftn90, SwashBackup.ftn90 hotstart 포맷(:91-307), SwashCleanMem.ftn90 deallocate 목록 file:line 인용; 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
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

양수 출력 간격은 요청 시각 이상인 첫 계산 시각에서 출력한다. (`src/SwashDecOutQ.ftn90:130–132`; [inputs-setup:SI1-054 수정안](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#4-노트-대조와-수정안)) [10-15 대조 정정]
가장 가까운 앞·뒤 시각을 비교해 선택하지 않는다. ([inputs-setup:SI1-054](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#5-차이-결론)) [10-15 대조 정정]

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
| setup | `setup (nm) = setup (nm) + s1(nm)` (`if ( dps(nm) > 0. ) then`) | `setup = setup / nwavoutp`, `src/SwashAverOutp.ftn90:95–119` [10-15 대조 정정] |
| wave height HSIG | `etavar(nm) = etavar(nm) + s1(nm)*s1(nm)` | `hsig = 4. * sqrt( max( etavar / (nwavoutp-1.) - setup*setup, 0. ) )`, `src/SwashAverOutp.ftn90:97,121` [10-15 대조 정정] |
| mean current | `mvelu += u1`, `mvelv += v1` | `/ncuroutp`, `:127-147` |
| mean constituents | `mcons += rp` | `/ntraoutp`, `:149-171` |
| mean turbulence | `mtke += rtur(1)`, `meps += rtur(2)` | `/nturoutp`, `:173-193` |

`etavar`는 수면 높이 제곱의 합이다. (`src/SwashAverOutp.ftn90:97`; [outputs:SO1-289 수정안](../../../_staging/recovery/compare/swash-outputs-vs-code.md#4-노트-대조와-수정안)) [10-15 대조 정정]
현재 파랑 통계는 최종 평균 기간 안에서 `dps>0`인 점만 누적한다. (`src/SwashAverOutp.ftn90:89,95–100`; outputs:SO1-291) [10-15 대조 정정]
최종화는 `if ( abs(dif) < 0.99*dt .and. nwavoutp > 1. ) then`이다. (`src/SwashAverOutp.ftn90:117`; outputs:SO1-291) [10-15 대조 정정]
1회만 수행하게 하는 플래그는 없다. ([outputs:SO1-291 수정안](../../../_staging/recovery/compare/swash-outputs-vs-code.md#4-노트-대조와-수정안)) [10-15 대조 정정]
코드의 분산식은 수면 높이 표준편차의 정의와 다르다. (`src/SwashAverOutp.ftn90:119–121`; `swashuse PDF p.145`; outputs:SO1-290) [10-15 대조 정정]
같은 비영 수면 높이 c를 `N>1`회 누적하면 제곱근 안에 `c²/(N−1)`이 남는다. (outputs:SO1-290) [10-15 대조 정정]
표준 분산은 0이다. (outputs:SO1-290) [10-15 대조 정정]
HSIG 식의 차이는 outputs:SO1-220의 E 코드 결함 후보(강함)이다. ([outputs §5](../../../_staging/recovery/compare/swash-outputs-vs-code.md#5-차이-결론)) [10-15 대조 정정]
평균 대상은 ReqOutQ의 `lwavoutp`/`lcuroutp`/`ltraoutp`/`lturoutp` 플래그로 설정된다. (`src/SwashReqOutQ.ftn90:226–231`; §6 참조) [10-15 대조 정정]

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

출력 키워드와 `ivtype`의 직접 근거는 SwashInit의 개별 대입이다. ([outputs:SO1-292 수정안](../../../_staging/recovery/compare/swash-outputs-vs-code.md#4-노트-대조와-수정안)) [10-15 대조 정정]
`src/SwashInit.ftn90:809–812`는 `ovkeyw(ivtype) = 'HS'` / `ovsnam(ivtype) = 'Hsig'` / `ovlnam(ivtype) = 'Significant wave height'` / `ovunit(ivtype) = uh`를 대입한다. [10-15 대조 정정]
출력량별 키워드·단위 매핑은 [outputs §2.4](../../../_staging/recovery/compare/swash-outputs-vs-code.md#24-p109118-출력-변수-이름단위정의)에 있다. [10-15 대조 정정]

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

`SwashCleanMem.ftn90`는 종료 시 이 루틴에 열거된 배열을 할당 여부에 따라 해제한다. (`src/SwashCleanMem.ftn90:62–128,540–545`). 출력 위치·출력 요청·경계 입력·Fourier 급수·경계점 연결 목록은 `delete` 호출로 정리한다. (`src/SwashCleanMem.ftn90:549–561`; [callflow 직접 호출 표](../../../_staging/recovery/flow/SWASH-callflow.md#swashcleanmem의-직접-호출-5개-호출문)). [10-15 전수 검증 정정]

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

**위치-요청 직교 분리**(`opsdat`/`orqdat`)로 한 위치에 다중 quantity·다중 출력형식을 지원한다. (`src/SwashOutput.ftn90:46–54`) [10-15 대조 정정]
현재 출력 등록 수는 96개이다. (`src/SwashInit.ftn90:524–1693`; [outputs:SO1-293 수정안](../../../_staging/recovery/compare/swash-outputs-vs-code.md#4-노트-대조와-수정안)) [10-15 대조 정정]
`nmovar=120`은 배열 상한이다. (`src/SwashModule1.ftn90:64`) [10-15 대조 정정]
구조격자는 `SWIPOL`로 보간한다. (`src/SwashQuanOutp.ftn90:2379`) [10-15 대조 정정]
비구조격자는 `SwanInterpolateOutput`로 보간한다. (`src/SwashQuanOutp.ftn90:2381`) [10-15 대조 정정]
VTK는 41.95(2022)에 ParaView 지원으로 추가된 별도 binary-append writer이다. (§7) [10-15 대조 정정]

## 문서와 코드 차이 (10-15 대조)

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech, 공개 저장소 `7949227` 2026-05-06 `"release v12.01"`에서 마지막 변경. 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f` 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함.

매뉴얼 인용은 PDF 쪽 번호를 사용한다. 인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.
출처는 [inputs-setup §5](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#5-차이-결론), [outputs §5](../../../_staging/recovery/compare/swash-outputs-vs-code.md#5-차이-결론), [guide-syntax-build §5](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md#5-차이-결론), [callflow §8](../../../_staging/recovery/flow/SWASH-callflow.md#8-차이-결론)의 최종 결론이다.
결론의 절 번호는 해당 보고서의 절 번호이다.
기존 노트 인용의 줄 번호는 대조 보고서에 기록된 번호이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow:RF-016 | 비구조 백업·재시작의 정점 순회 | — | `src/SwashInitCompUgrid.ftn90:119,121` `s1(ncells)` / `u1(nfaces,kmax)`<br>`src/SwashBackup.ftn90:300` `do i = 1, nverts`<br>`src/SwashBackup.ftn90:310` `write (nref, 210) s1(i)`<br>`src/SwashBackup.ftn90:316` `write (nref, 210) u1(i,1)`<br>`src/SwashReadInput.ftn90:2812` `if ( mxc <= 1 .and. optg /= 5 ) then`<br>`src/SwashReadInput.ftn90:2814` `else if ( mcgrd <= 1 .and. nverts <= 0 ) then`<br>`src/SwashInitCond.ftn90:170` `if ( optg == 5 ) npcur = nverts` | E 코드 결함 후보 (강함) | 비구조 백업·재시작은 정점 수로 셀 수위와 면 속도 배열을 순회한다. 일반 삼각망에서는 상태 일부를 빠뜨리거나 배열 범위를 벗어날 수 있다. 단층 u1 입출력은 `kmax == 1` 분기에서 수행한다. 같은 불일치가 최초 공개 소스부터 남아 있으므로 문서판 이후의 변경으로 설명할 수 없다. |
| guide-syntax-build:SG1-870 | 출력 추가 키워드 | `swashuse PDF p.162–163`; `swashuse PDF p.103`; `misc/swash.edt:309–329` | `src/SwashInit.ftn90:833` `ovkeyw(ivtype) = 'XC'`<br>`src/SwashInit.ftn90:845` `ovkeyw(ivtype) = 'YC'`<br>`src/SwashInit.ftn90:1509` `ovkeyw(ivtype) = 'DIVU'`<br>`src/SwashInit.ftn90:1521` `ovkeyw(ivtype) = 'DIVQ'`<br>`src/SwashReqOutL.ftn90:179` `if (KEYWIS('GROUP') .or. KEYWIS ('SUBG')) then`<br>`src/SwashReqOutQ.ftn90:199–218,420–445` `ivtype` / `optg /= 5` | C 문서 누락 | XC·YC·DIVU·DIVQ가 OVKEYW에 등록되어 있다. SUBG는 GROUP과 같은 명령 분기로 진입한다. BLOCK·TABLE은 이 등록 키워드를 판독한다. DIVU·DIVQ는 비정형격자에서만 출력 요청에 등록한다. C는 추가 출력 키워드와 독립 SUBG 명령 별칭에 한정한다. |
| guide-syntax-build:SG1-871 | BLOCK VTK와 프로세스 접미부 | `swashuse PDF p.114` | `src/SwashReqOutQ.ftn90:159–173` `vtk = index ( FILENM, '.VT' ) /= 0 .or. index (FILENM, '.vt' ) /= 0` / `if ( vtk ) then` / `dfac  = 1.` / `rtype = 'BLKV'` / `endif` / `if ( FILENM == ' ' ) then` / `nref = PRINTF` / `else` / `nref = 0` / `!` / `! append node number to FILENM in case of parallel computing` / `if ( parll .and. .not.vtk ) then` / `ilpos = index ( FILENM, ' ' )-1` / `write (FILENM(ilpos+1:ilpos+4),201) inode` | C 문서 누락 | VTK 출력 기능 자체는 p.114에 있다. 코드는 `vtk = index ( FILENM, '.VT' ) /= 0 .or. index (FILENM, '.vt' ) /= 0`으로 경로를 선택한다. VTK를 제외한 병렬 BLOCK 파일명에는 프로세스 번호를 붙인다. C는 확장자 끝 검사보다 넓은 부분 문자열 판정과 이 접미부 분기 조건에 한정한다. |
| guide-syntax-build:SG1-872 | TABLE UNIT 처리와 출력 상한 | `swashuse PDF p.120–122`; 부록 C | `src/SwashReqOutQ.ftn90:458–460` `call INKEYW ('STA', ' ')` / `if ( KEYWIS('UNIT') ) then` / `call msgerr (1, '[unit] is ignored in this version')`<br>`src/SwashModule2.ftn90:64` `integer, parameter               :: max_outp_req = 250         ! maximum number of output requests`<br>`src/SwashReqOutQ.ftn90:139–140` `nreoq = nreoq + 1` / `if ( nreoq > max_outp_req ) call msgerr (2, 'too many output requests')` | C 문서 누락 | TABLE UNIT은 MSGERR 수준 1을 낸 뒤 무시한다. `max_outp_req = 250`이며 요청 수가 이를 넘으면 수준 2를 낸다. C는 이 호환 입력 처리와 상한의 누락이다. |
| inputs-setup:SI1-054 | 출력 시간을 가장 가까운 계산 시간으로 이동 | `swashuse PDF p.20` `the output time is shifted to the nearest computational time level` | `src/SwashDecOutQ.ftn90:130–132` `else if ( outr(2) > 0. .and. .not. real(timco) < real(tnext) ) then` / `outr(1) = tnext + outr(2)` / `logact  = .true.`<br>`8756667:src/SwashDecOutQ.ftn90:129` `else if ( outr(2) > 0. .and. .not. real(timco) < real(tnext) ) then` | B 문서 오기 | 양의 출력 간격은 요청 시간 이상인 첫 계산 단계에서 출력한다. 앞뒤 두 계산 시간의 거리를 비교하지 않는다. 요청 시간을 처음 넘는 단계의 출력 조건은 최초 공개판부터 있다. 가장 가까운 시간으로 선택하던 구현의 삭제는 없다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 전수 검증 보완] |
| outputs:SO1-003 | 이름 중복 시 먼저 정의한 집합 소실 | `swashuse PDF p.101–102` `If one gives one name for two sets of output locations, the first set is lost (first in the sequence in the command file).` | `src/SwashReqOutL.ftn90:166–167` `cops%nextops => opstmp` / `cops => opstmp`<br>`src/swanser.ftn:2780–2782` `CUOPS => FOPS                                                       40.31` / `DO                                                                  40.31` / `IF (CUOPS%PSNAME.EQ.PSNAME) EXIT                                  40.31`<br>`src/SwashOutput.ftn90:143–145` `cuops => FOPS` / `do` / `if ( cuops%psname == psname ) exit`<br>`8756667:src/SwashOutput.ftn90:143–145` `cuops => FOPS` / `if ( cuops%psname == psname ) exit` | B 문서 오기 | 같은 이름의 출력 위치 집합을 여러 번 정의하면 현재 코드는 처음 정의한 집합을 선택한다. |
| outputs:SO1-005 | BLOCK 집합 종류 | `swashuse PDF p.102` `BLOCK write spatial distributions (only for FRAMEs and GROUPs)`<br>`swashuse PDF p.114` `Binary MATLAB files are particularly useful for the computation with unstructured grids.`<br>`swashuse PDF p.102` `only for FRAMEs and GROUPs` | `src/SwashReqOutQ.ftn90:127–129` `if ( pstype /= 'F' .and. pstype /= 'H' .and. pstype /= 'U' ) then` / `call msgerr (2, 'set of output locations is not correct type')` / `goto 800` | B 문서 오기 | BLOCK은 FRAME·GROUP과 비정형 집합 U를 허용한다. |
| outputs:SO1-006 | BLOCK 1차원 금지 | `swashuse PDF p.102` `Command BLOCK cannot be used in 1D-MODE.` | `src/SwashReqOutQ.ftn90:123` `if ( KEYWIS ('BLO') ) then`<br>`src/SwashReqOutQ.ftn90:127` `if ( pstype /= 'F' .and. pstype /= 'H' .and. pstype /= 'U' ) then`<br>`src/swanser.ftn:3263–3267` `IF (ONED) THEN` / `JY1 = 1` / `JY2 = 1` | B 문서 오기 | 현재 BLOCK 판독기는 1차원 모드를 거부하지 않는다. |
| outputs:SO1-008 | FRAME 문법 | `swashuse PDF p.102` `FRAme ’sname’ [xpfr] [ypfr] [alpfr] [xlenfr] [ylenfr] [mxfr] [myfr])` | `src/SwashReqOutL.ftn90:128` `! FRAme   'sname'  [xpfr] [ypfr] [alpfr] [xlenfr] [ylenfr] [mxfr] [myfr]`<br>`8756667:src/SwashReqOutL.ftn90:128` `[myfr]` | B 문서 오기 | FRAME 문법의 마지막 닫는 괄호는 삭제해야 한다. |
| outputs:SO1-023 | GROUP 크기·모서리·각도 PRINT | `swashuse PDF p.103` `the size of the group, the corner coordinates and the angle with the problem coordinate system are written to PRINT file.` | `src/SwashReqOutL.ftn90:235` `if ( ITEST >= 20 .or. intes >= 10 ) write (PRINTF, 201) (opstmp%opr(i), i=1,6)`<br>`src/SwashReqOutL.ftn90:607` `201 format (' Subgrid parms.', 6(1x,e12.4))`<br>`src/SwashReqOutL.ftn90:217` `else if ( optg == 1 ) then` | C 문서 누락 | 규칙 격자 GROUP의 PRINT 진단은 ITEST·INTES 조건을 따른다. `swashuse PDF p.103`은 격자 종류와 출력 수준 조건을 생략한다. git 판정의 B를 C로 좁힌다. 조건부 구현이 있으므로 출력 기능 자체의 오기로 보지 않는다. |
| outputs:SO1-033 | ISOLINE 제한 | `swashuse PDF p.105` `CANNOT BE USED IN 1D-MODE AND IN CASE OF CURVILINEAR GRIDS.` | `src/SwashReqOutL.ftn90:512–516` `if ( oned ) then` / `call msgerr (2, 'illegal keyword (ISO) in combination with 1D computation')` / `goto 800` / `else if ( igtype(1) == 2 .or. igtype(7) == 2 ) then` / `call msgerr (2, 'keyword ISO not supported in case of curvilinear bottom grid')` | C 문서 누락 | ISOLINE은 1D를 거부한다. 곡선형 제한은 바닥·수위 입력 격자에 적용한다. `swashuse PDF p.105`는 곡선형 격자의 대상을 구분하지 않는다. git 판정의 B를 적용 범위 설명 누락 C로 좁힌다. |
| outputs:SO1-046 | ref 기본값 | `swashuse PDF p.107` `starting time of the first computation, except in cases where this is later than the time of the earliest input. In these cases, the time of the earliest input is used.` | `src/SwashInit.ftn90:1708` `outpar(1) = 0.`<br>`src/SwashReadInput.ftn90:659` `call INCTIM (ITMOPT  , 'REF' , rtmp, 'STA', -9.99d2)`<br>`src/SwashReadInput.ftn90:698` `if ( qr(4) /= -999. ) outpar(1) = qr(4)`<br>`8756667:src/SwashInit.ftn90:1629` `outpar(1) = 0.`<br>`src/SwashQuanOutp.ftn90:2354` `if ( oqproc(41) ) voq(:,voqr(41)) = real(timco) - outpar(1)` | B 문서 오기 | REF를 생략하면 현재 코드의 TSEC 기준값은 0이다. |
| outputs:SO1-047 | dur 적용 변수 | `swashuse PDF p.106` `(for output quantities SETUP, HSIG, HRMS, MVEL, MTKE and MSAL)`<br>`swashuse PDF p.108` `QUANTITY MVEL MSALK dur 1 hr`<br>`swashuse PDF p.119` `The mean currents MVEL, MVELK, etc.` / `The mean constituents MSAL, MTEMP and MSED` / `The mean turbulence quantities MTKE, MEPS and MVISC` | `src/SwashReadInput.ftn90:700` `if ( ivtype == 22 .or. ivtype == 23 .or. ivtype == 24 ) then`<br>`src/SwashReadInput.ftn90:704` `if ( ivtype >= 33 .and. ivtype <= 37 ) then`<br>`src/SwashReadInput.ftn90:708` `if ( ivtype == 42 .or. ivtype == 43 .or. ivtype == 44 ) then`<br>`src/SwashReadInput.ftn90:712` `if ( ivtype == 57 .or. ivtype == 58 .or. ivtype == 59 ) then`<br>`src/SwashReadInput.ftn90:716` `if ( ivtype >= 84 .and. ivtype <= 88 ) then`<br>`src/SwashReadInput.ftn90:720` `if ( ivtype == 92 .or. ivtype == 93 .or. ivtype == 94 ) then` | C 문서 누락 | DUR 적용 대상의 누락은 `swashuse PDF p.106` 구문도의 열거에 한정한다. p.108의 MSALK 예문과 p.119의 평균 속도·성분·난류량 설명은 추가 적용 대상을 명시한다. |
| outputs:SO1-061 | WLEV·VX 예문 | `swashuse PDF p.108` `QUANTITY WLEV VX excv=-9.` | `src/SwashInit.ftn90:605` `ovkeyw(ivtype) = 'WATL'`<br>`src/SwashInit.ftn90:653` `ovkeyw(ivtype) = 'VKSI'`<br>`src/swanser.ftn:2908–2909` `IF (KEYWIS (OVKEYW(IVT))) THEN                                    40.00` / `IVTYPE = IVT                                                    40.00`<br>`8756667:src/SwashInit.ftn90:564` `ovkeyw(ivtype) = 'WATL'`<br>`8756667:src/SwashInit.ftn90:612` `ovkeyw(ivtype) = 'VKSI'` | B 문서 오기 | QUANTITY 예문의 출력량 이름은 WATLEV와 VKSI로 적어야 한다. [10-15 전수 검증 보완] |
| outputs:SO1-067 | FRAME 예문 | `swashuse PDF p.109` `QUANTITY VEL VDIR frame` / `to obtain vector components and direction with respect to the frame.` | `src/SwashReadInput.ftn90:744` `outpar(2) = qr(7)`<br>`src/SwashQuanOutp.ftn90:2430` `voq(i,jvx) = coscq*rval1 - sincq*rval2`<br>`src/SwashQuanOutp.ftn90:2459` `dirdeg = (alcq + atan2(rval2,rval1)) * 180./pi`<br>`src/SwashQuanOutp.ftn90:2431` `voq(i,jvy) = sincq*rval1 + coscq*rval2`<br>`src/SwashDecOutL.ftn90:109` `alcq = -alpq`<br>`src/SwashReadInput.ftn90:671–672` `else if ( KEYWIS('FRAME') ) then` / `qr(7) = 1.` | E 코드 결함 후보 (강함) | Cartesian·QUANTITY FRAME의 VDIR은 회전한 VEL에 프레임 회전각을 다시 더한다. 이 경로를 코드 결함 후보로 표시한다. |
| outputs:SO1-069 | field 제한·기본값 | `swashuse PDF p.109` `length of one data field in a table. Minimum is 8 and maximum is 16.` / `Default: field = 12` | `src/SwashModule2.ftn90:71` `integer                          :: fld_table = 15             ! field length for fixed-point table`<br>`src/SwashReadInput.ftn90:364–366` `call ININTG ('FIELD', fld_table, 'STA', 15)` / `if ( fld_table > 16 ) call msgerr (2, '[field] is too large')` / `if ( fld_table < 8  ) call msgerr (2, '[field] is too small')`<br>`src/swanout2.ftn:1590–1595` `FSTR = '(F13.X)'` | B 문서 오기 | FIELD의 코드 기본값은 15이다. 값의 허용 범위는 8–16이다. HEADER의 수치 서식은 F13이다. |
| outputs:SO1-070 | ndec 제한·기본값 | `swashuse PDF p.109` `number of decimals in block` / `Maximum is 9.` / `Default: ndec = 4` | `src/SwashModule2.ftn90:70` `integer                          :: dec_block =  6             ! number of decimals for fixed-point block`<br>`src/SwashReadInput.ftn90:373–374` `call ININTG ('NDEC', dec_block, 'STA', 6)` / `if ( dec_block > 9 ) call msgerr (2, '[ndec] is too large')`<br>`8756667:src/SwashReadInput.ftn90:319` `call ININTG ('NDEC', dec_block, 'STA', 6)` | B 문서 오기 | NDEC의 코드 기본값은 6이다. 상한은 9이다. |
| outputs:SO1-071 | len 제한·기본값 | `swashuse PDF p.109` `number of data on one line of block output. Maximum is 9999.` / `Default: len = 6` | `src/SwashModule2.ftn90:100` `character (len=40)               :: flt_block = '(6e14.6)'     ! floating point block`<br>`src/SwashReadInput.ftn90:375–377` `call ININTG ('LEN', nlen, 'STA', 200)` / `if ( nlen > 9999 ) call msgerr (2, '[len] is too large')` / `write (flt_block, 203) nlen, dec_block+8, dec_block`<br>`8756667:src/SwashReadInput.ftn90:321` `call ININTG ('LEN', nlen, 'STA', 200)` | B 문서 오기 | OUTPUT BLOCK을 생략하면 기본 서식은 줄당 6개를 쓴다. OUTPUT BLOCK에서 LEN을 생략하면 200개를 쓴다. |
| outputs:SO1-074 | BLOCK 헤더 내용·행 수 | `swashuse PDF p.114` `The text of the header indicates run identification (see command PROJECT), time, frame name or group name (’sname’), variable and unit.` / `The number of header lines is 8.` | `src/swanout2.ftn:662–663` `WRITE (NREF, 20) OUT_COMMENT                                      40.13`<br>`src/swanout2.ftn:665–666` `WRITE (NREF, 22) OUT_COMMENT, PROJNR, PSNAME, STRING,             40.13` / `     &                   DFAC, QUNIT                                      40.13`<br>`src/swanout2.ftn:669–670` `IF (NSTATM .GT. 0) THEN` / `WRITE (NREF, 24) OUT_COMMENT, CHTIME                            40.13`<br>`src/swanout2.ftn:675` `WRITE (NREF, 20) OUT_COMMENT                                      40.13`<br>`src/swanout2.ftn:688` `WRITE (NREF, 26) OUT_COMMENT                                    40.13`<br>`src/swanout2.ftn:690–693` `WRITE (NREF, 20) OUT_COMMENT                                    40.13` / `WRITE (NREF, WFORM1) OUT_COMMENT, (II-1,II=IXP1,IXP2)           40.13` / `WRITE (NREF, 99030) OUT_COMMENT                                 40.13` / `99030     FORMAT (A1, 'Y')                                                40.13`<br>`src/swanout2.ftn:672–674` `WRITE (NREF, 20) OUT_COMMENT` | B 문서 오기 | HEADER BLOCK은 정상·비정상 모드 모두 첫 데이터 앞에 9행을 쓴다. `src/swanout2.ftn:662–693`의 WRITE에서 공통 머리말 5행과 첫 열 제목 4행을 센 값이다. 폭 151점을 넘으면 열 제목 4행을 반복한다. git 판정 기록의 ‘비정상 모드에서 한 행 추가’는 ELSE의 빈 행을 빠뜨렸으므로 정정한다. B는 유지한다. |
| outputs:SO1-086 | UNIT 자동 HEADER 서식 | `swashuse PDF p.118` `value is written as a 5 position integer.` / `SWASH takes [unit] such that the largest number occurring in the block can be printed.` | `src/swanout2.ftn:235` `IFAC = INT (10.+LOG10(OVHEXP(IVTYPE))) - 13                 30.20`<br>`src/swanout2.ftn:257` `DFAC = 10.**IFAC`<br>`src/swanout2.ftn:631` `CHARACTER (LEN=21) :: WFORM2 = '(1X,I3,1X, 151(F6.0))'              40.13`<br>`src/swanout2.ftn:683` `WRITE (WFORM2(17:17), '(I1)') DEC_BLOCK                         40.13` | B 문서 오기 | HEADER BLOCK은 기본 F6.0 서식을 쓴다. 자동 배율은 유효한 예상 상한을 먼저 사용한다. |
| outputs:SO1-092 | WATLEV | `swashuse PDF p.115` `water level or surface elevation (in m). Output is in both active and non-active points.` | `src/SwashInit.ftn90:605` `ovkeyw(ivtype) = 'WATL'`<br>`src/SwashInit.ftn90:606` `ovsnam(ivtype) = 'Watlev'`<br>`src/SwashInit.ftn90:608` `ovunit(ivtype) = uh`<br>`src/SwashQuanOutp.ftn90:2411` `call SwanInterpolateOutput ( voq(1,voqr(6)), voq(1,1), voq(1,2), oparr(1,2), mip, kvert, ovexcv(6) )`<br>`src/SwanInterpolateOutput.ftn90:128` `foutp = excval`<br>`src/SwanInterpolateOutput.ftn90:144` `if ( .not.vert(ivert)%active ) cycle pointloop` | C 문서 누락 | 비정형 WATLEV 보간은 비활성 최근접 정점에서 예외값을 남긴다. `swashuse PDF p.115`의 활성·비활성점 출력 설명에는 이 유효값 제한이 없다. 제한 누락 C로 범위를 한정한다. |
| outputs:SO1-100 | NHPRES | `swashuse PDF p.115` `normalised (by density) non-hydrostatic pressure at bottom (in m²/s²).` | `src/SwashInit.ftn90:677` `ovkeyw(ivtype) = 'NHPRES'`<br>`src/SwashInit.ftn90:678` `ovsnam(ivtype) = 'Nhpres'`<br>`src/SwashInit.ftn90:680` `ovunit(ivtype) = uf`<br>`src/SwashQuanOutp.ftn90:2492` `call SWIPOL ( oparr(1,13), ovexcv(12), xc, yc, mip, voq(1,voqr(12)), kgrpnt, oparr(1,1) )`<br>`src/SwashInit.ftn90:111` `uf     = 'N/m2'`<br>`src/SwashQuanOutp.ftn90:2259` `oparr(:,14) = 0.01 * rhow * ( grav * oparr(:,1) + oparr(:,13) )`<br>`src/SwashInit.ftn90:111` `uf     = 'N/m2'`<br>`8756667:src/SwashInit.ftn90:639` `ovunit(ivtype) = uf` | E 코드 결함 후보 (강함) | 비정수압을 켠 NHPRES의 수치는 밀도로 정규화한 압력이다. 헤더의 N/m2는 수치의 m²/s²와 맞지 않으므로 E 후보를 유지한다. 노트 단위의 일치 판정은 SO1-295에서 구분한다. |
| outputs:SO1-115 | SED | `swashuse PDF p.115` `suspended sediment (in kg/m³).` | `src/SwashInit.ftn90:1001` `ovkeyw(ivtype) = 'SED'`<br>`src/SwashInit.ftn90:1002` `ovsnam(ivtype) = 'Sed'`<br>`src/SwashInit.ftn90:1004` `ovunit(ivtype) = ud`<br>`src/SwashQuanOutp.ftn90:2313` `oparr(:,27) = rhos * oparr(:,27)`<br>`src/SwashElemOutp.ftn90:304` `if ( oqproc(39) ) voq(:,voqr(39)) = rp(:,1,lsed)`<br>`src/SwashInitBCUtrans.ftn90:160` `rp(icell,:,lsed) = ( sedf(v(1),:) + sedf(v(2),:) + sedf(v(3),:) ) / 3. / rhos` | E 코드 결함 후보 (강함) | ELEMESH의 SED는 rp에 rhos를 곱하지 않는다. 부유사 수송을 켠 유효 경로에서 kg/m³ 대신 체적 농도를 쓰므로 E 후보를 유지한다. SO1-115·128·140·158은 같은 환산 누락의 출력량별 행이다. |
| outputs:SO1-118 | SETUP | `swashuse PDF p.115` `wave-induced setup (in m).`<br>`swashuse PDF p.119` `averaging the surface elevation` | `src/SwashInit.ftn90:797` `ovkeyw(ivtype) = 'SETUP'`<br>`src/SwashInit.ftn90:798` `ovsnam(ivtype) = 'Setup'`<br>`src/SwashInit.ftn90:800` `ovunit(ivtype) = uh`<br>`src/SwashQuanOutp.ftn90:898` `oparr(indx,17) = setup(indxr)` | C 문서 누락 | SETUP은 `dps>0`인 점에서 기준면에 대한 수면 높이의 표본 평균이다. p.119의 계산 설명은 이 경로와 대응한다. p.115의 wave-induced setup은 정수위 차감 여부를 밝히지 않으므로 git 판정의 B를 기준면 설명 누락 C로 좁힌다. |
| outputs:SO1-119 | HSIG | `swashuse PDF p.116` `significant wave height (in m; for definition, see Appendix A).`<br>`swashuse PDF p.145` `four times the standard deviation` | `src/SwashInit.ftn90:809` `ovkeyw(ivtype) = 'HS'`<br>`src/SwashInit.ftn90:810` `ovsnam(ivtype) = 'Hsig'`<br>`src/SwashInit.ftn90:812` `ovunit(ivtype) = uh`<br>`src/SwashQuanOutp.ftn90:2667` `call SWIPOL ( oparr(1,18), ovexcv(23), xc, yc, mip, voq(1,voqr(23)), kgrpnt, oparr(1,1) )`<br>`src/SwashAverOutp.ftn90:121` `hsig = 4. * sqrt( max( etavar / (nwavoutp-1.) - setup*setup, 0. ) )` | E 코드 결함 후보 (강함) | HSIG는 제곱합만 `N−1`로 나눈 뒤 표본 평균의 제곱을 뺀다. `dps>0`인 점에서 일정한 비영 수위 c와 `N>1`을 대입하면 루트 안은 `c²/(N−1)`이다. 표준편차 0과 다른 결과이므로 E 후보를 유지한다. SO1-220과 같은 문제이다. |
| outputs:SO1-121 | MVMAG | `swashuse PDF p.116` `time-averaged or mean velocity magnitude (in m/s).` | `src/SwashInit.ftn90:929` `ovkeyw(ivtype) = 'MVMAG'`<br>`src/SwashInit.ftn90:930` `ovsnam(ivtype) = 'MVmag'`<br>`src/SwashInit.ftn90:932` `ovunit(ivtype) = uv`<br>`src/SwashQuanOutp.ftn90:2845` `voq(i,voqr(33)) = sqrt(rval1*rval1 + rval2*rval2)` | C 문서 누락 | MVMAG는 시간평균한 속도 벡터의 크기이다. `swashuse PDF p.116·119`에는 크기와 시간평균의 연산 순서가 없다. C는 이 계산 정의의 누락에 한정한다. |
| outputs:SO1-128 | MSED | `swashuse PDF p.116` `time-averaged or mean suspended sediment (in kg/m³).` | `src/SwashInit.ftn90:1061` `ovkeyw(ivtype) = 'MSED'`<br>`src/SwashInit.ftn90:1062` `ovsnam(ivtype) = 'MSed'`<br>`src/SwashInit.ftn90:1064` `ovunit(ivtype) = ud`<br>`src/SwashQuanOutp.ftn90:2319` `oparr(:,30) = rhos * oparr(:,30)`<br>`src/SwashElemOutp.ftn90:425` `if ( oqproc(44) ) voq(:,voqr(44)) = mcons(:,1,lsed)`<br>`src/SwashInitBCUtrans.ftn90:160` `rp(icell,:,lsed) = ( sedf(v(1),:) + sedf(v(2),:) + sedf(v(3),:) ) / 3. / rhos` | E 코드 결함 후보 (강함) | ELEMESH의 MSED는 mcons에 rhos를 곱하지 않는다. 부유사 수송을 켠 유효 경로에서 kg/m³ 대신 체적 농도를 쓰므로 E 후보를 유지한다. SO1-115·128·140·158은 같은 환산 누락의 출력량별 행이다. |
| outputs:SO1-140 | SEDK | `swashuse PDF p.116` `suspended sediment per layer (in kg/m³).` | `src/SwashInit.ftn90:1461` `ovkeyw(ivtype) = 'SEDK'`<br>`src/SwashInit.ftn90:1462` `ovsnam(ivtype) = 'Sedk'`<br>`src/SwashInit.ftn90:1464` `ovunit(ivtype) = ud`<br>`src/SwashQuanOutp.ftn90:2325` `oparrk(:,:,27) = rhos * oparrk(:,:,27)`<br>`src/SwashElemOutp.ftn90:710` `voqk(:,k,voqr(91)) =  rp(:,k,lsed)`<br>`src/SwashInitBCUtrans.ftn90:160` `rp(icell,:,lsed) = ( sedf(v(1),:) + sedf(v(2),:) + sedf(v(3),:) ) / 3. / rhos` | E 코드 결함 후보 (강함) | ELEMESH의 SEDK는 rp에 rhos를 곱하지 않는다. 부유사 수송을 켠 유효 경로에서 kg/m³ 대신 체적 농도를 쓰므로 E 후보를 유지한다. SO1-115·128·140·158은 같은 환산 누락의 출력량별 행이다. |
| outputs:SO1-149 | PRESSK | `swashuse PDF p.116` `pressure per layer (in hPa).` | `src/SwashInit.ftn90:1365` `ovkeyw(ivtype) = 'PRESSK'`<br>`src/SwashInit.ftn90:1366` `ovsnam(ivtype) = 'Pres_k'`<br>`src/SwashInit.ftn90:1368` `ovunit(ivtype) = up`<br>`src/SwashQuanOutp.ftn90:2281` `oparrk(:,k,14) = 0.01 * rhow * ( grav * ( oparr(:,2) - oparrk(:,k,2) ) + oparrk(:,k,13) )`<br>`src/SwashQuanOutp.ftn90:189` `if ( kmax > 1 ) oparrk = 0.`<br>`src/SwashQuanOutp.ftn90:2277` `else if ( ihydro /= 3 ) then`<br>`src/SwashQuanOutp.ftn90:2259` `oparr(:,14) = 0.01 * rhow * ( grav * oparr(:,1) + oparr(:,13) )` | E 코드 결함 후보 (중간) | 다층 속도 격자의 `ihydro=3`에서 PRESSK는 압력 계산을 생략한 보조배열의 0을 출력한다. 미지원 값 처리도 없으므로 E 후보를 중간 강도로 유지한다. |
| outputs:SO1-150 | NHPRSK | `swashuse PDF p.116` `normalised (by density) non-hydrostatic pressure per layer (in m²/s²).` | `src/SwashInit.ftn90:1353` `ovkeyw(ivtype) = 'NHPRSK'`<br>`src/SwashInit.ftn90:1354` `ovsnam(ivtype) = 'Nprs_k'`<br>`src/SwashInit.ftn90:1356` `ovunit(ivtype) = uf`<br>`src/SwashQuanOutp.ftn90:3307` `call SWIPOL ( oparrk(1,k,13), ovexcv(82), xc, yc, mip, voqk(1,k,voqr(82)), kgrpnt, oparr(1,1) )`<br>`src/SwashInit.ftn90:111` `uf     = 'N/m2'`<br>`src/SwashQuanOutp.ftn90:2259` `oparr(:,14) = 0.01 * rhow * ( grav * oparr(:,1) + oparr(:,13) )`<br>`src/SwashInit.ftn90:111` `uf     = 'N/m2'`<br>`8756667:src/SwashInit.ftn90:1315` `ovunit(ivtype) = uf` | E 코드 결함 후보 (강함) | 유효한 `ihydro=1·2`의 NHPRSK는 밀도로 정규화한 압력이다. 헤더의 N/m2는 수치의 m²/s²와 맞지 않으므로 E 후보를 유지한다. `ihydro=3`의 예외값 처리는 `src/SwashQuanOutp.ftn90:3315`이다. |
| outputs:SO1-151 | MVMAGK | `swashuse PDF p.116` `time-averaged or mean velocity magnitude per layer (in m/s).` | `src/SwashInit.ftn90:1377` `ovkeyw(ivtype) = 'MVMAGK'`<br>`src/SwashInit.ftn90:1378` `ovsnam(ivtype) = 'MVmagk'`<br>`src/SwashInit.ftn90:1380` `ovunit(ivtype) = uv`<br>`src/SwashQuanOutp.ftn90:3368` `voqk(i,k,voqr(84)) = sqrt(rval1*rval1 + rval2*rval2)` | C 문서 누락 | 각 층의 MVMAGK는 시간평균한 속도 벡터의 크기이다. `swashuse PDF p.116·119`에는 크기와 시간평균의 연산 순서가 없다. C는 이 계산 정의의 누락에 한정한다. |
| outputs:SO1-158 | MSEDK | `swashuse PDF p.117` `time-averaged or mean suspended sediment per layer (in kg/m³).` | `src/SwashInit.ftn90:1497` `ovkeyw(ivtype) = 'MSEDK'`<br>`src/SwashInit.ftn90:1498` `ovsnam(ivtype) = 'MSedk'`<br>`src/SwashInit.ftn90:1500` `ovunit(ivtype) = ud`<br>`src/SwashQuanOutp.ftn90:2331` `oparrk(:,:,30) = rhos * oparrk(:,:,30)`<br>`src/SwashElemOutp.ftn90:734` `voqk(:,k,voqr(94)) = mcons(:,k,lsed)`<br>`src/SwashInitBCUtrans.ftn90:160` `rp(icell,:,lsed) = ( sedf(v(1),:) + sedf(v(2),:) + sedf(v(3),:) ) / 3. / rhos` | E 코드 결함 후보 (강함) | ELEMESH의 MSEDK는 mcons에 rhos를 곱하지 않는다. 부유사 수송을 켠 유효 경로에서 kg/m³ 대신 체적 농도를 쓰므로 E 후보를 유지한다. SO1-115·128·140·158은 같은 환산 누락의 출력량별 행이다. |
| outputs:SO1-161 | MVISC | `swashuse PDF p.117` `time-averaged or mean vertical eddy viscosity per layer interface (in m²/s).` | `src/SwashInit.ftn90:1207` `ovkeyw(ivtype) = 'MVISC'`<br>`src/SwashInit.ftn90:1208` `ovsnam(ivtype) = 'MVisc'`<br>`src/SwashInit.ftn90:1210` `ovunit(ivtype) = ue`<br>`src/SwashQuanOutp.ftn90:2304` `oparrk(:,:,24) = 0.09 * oparrk(:,:,22) * oparrk(:,:,22) / ( oparrk(:,:,23) + 1.e-8 )`<br>`src/SwashVertVisc.ftn90:72` `vnu3d(:,:) = cmu * rtur(:,:,1) * rtur(:,:,1) / ( rtur(:,:,2) + eps )`<br>`src/SwashQuanOutp.ftn90:2297` `! compute time-averaged vertical eddy viscosity`<br>`src/SwashDecOutQ.ftn90:282` `! for mean eddy viscosity add mean turbulent kinetic energy and mean dissipation rate as output quantities` | C 문서 누락 | 난류 모형을 켠 MVISC는 평균 TKE·평균 EPS로 구성한 점성이다. `src/SwashQuanOutp.ftn90:2301–2302`의 `iturb=0` 분기는 vnu3d를 쓴다. `swashuse PDF p.117·119`에는 이 계산 정의가 없다. 순간 VISC의 산술평균과 구별하는 정의 누락 C로 확정한다. |
| outputs:SO1-167 | BLOCK 선택도와 TABLE 전용 변수 | `swashuse PDF p.113` `TIME` / `FORCEX` / `FORCEY` / `FORCEZ` / `MOMX` / `MOMY` / `MOMZ` / `TRAX` / `TRAY` / `TRAZ` / `ROTX` / `ROTY` / `ROTZ` / `PTOP` / `RUNUP`<br>`swashuse PDF p.117–118` `TABLE only` | `src/SwashReqOutQ.ftn90:131–132` `if ( psname(1:6) == 'NOGRID' ) then` / `call msgerr (2, 'empty set is not allowed')`<br>`src/SwashOutput.ftn90:209–213` `if ( psname(1:6) == 'NOGRID' ) then` / `!` / `! the hydrodynamic loads and/or body motions` / `if ( ifloat /= 0 ) call SwashFlobjOutp ( oqproc, nvoqp, voqr, voq )` | B 문서 오기 | BLOCK 도식 p.113의 TABLE 전용 TIME·부유체 하중·변위·PTO·RUNUP을 구분해야 한다. B 판정은 이 도식으로 한정한다. 본문 p.117–118·120의 TABLE 전용 조건은 코드와 대응한다. |
| outputs:SO1-168 | 벡터가 항상 문제 좌표계라는 문장 | `swashuse PDF p.118` `are always given with respect to the problem coordinate system.` | `src/SwashDecOutL.ftn90:107–109` `if ( EQREAL(outpar(2),1.) ) then` / `! directions will be w.r.t. frame coordinate system` / `alcq = -alpq` | B 문서 오기 | QUANTITY FRAME은 벡터 성분을 프레임 좌표계로 회전한다. |
| outputs:SO1-169 | 부록의 FRAME 자동 예외 | `swashuse PDF p.146` `except in the case of output with BLOCK command in combination with command FRAME` / `x and y relate to the x−axis and y−axis of the output frame.` | `src/SwashInit.ftn90:1713` `outpar(2) = 0.`<br>`src/SwashDecOutL.ftn90:107` `if ( EQREAL(outpar(2),1.) ) then`<br>`src/SwashDecOutL.ftn90:112` `alcq = 0.`<br>`src/SwashReadInput.ftn90:671–672` `qr(7) = 1.`<br>`src/SwashReadInput.ftn90:744` `outpar(2) = qr(7)` | C 문서 누락 | 프레임 좌표계 벡터 출력에는 QUANTITY FRAME 지정이 필요하다. p.108–109는 이 조건을 설명한다. 부록 p.146은 이 선행 조건을 생략하므로 git 판정의 B를 해당 쪽의 조건 누락 C로 좁힌다. |
| outputs:SO1-170 | FRAME 방향의 이중 회전 | `swashuse PDF p.108–109` `directions are counterclockwise relative to the positive x−axis of the frame coordinate system` / `QUANTITY VEL VDIR frame` | `src/SwashDecOutL.ftn90:109` `alcq = -alpq`<br>`src/SwashQuanOutp.ftn90:2430–2431` `voq(i,jvx) = coscq*rval1 - sincq*rval2` / `voq(i,jvy) = sincq*rval1 + coscq*rval2`<br>`src/SwashQuanOutp.ftn90:2459` `dirdeg = (alcq + atan2(rval2,rval1)) * 180./pi` | E 코드 결함 후보 (강함) | Cartesian FRAME의 VDIR은 이미 회전한 VEL에 alcq를 다시 더한다. SO1-067과 같은 E 후보이다. 문제 좌표계 벡터 각도 0°와 프레임 각도 30°를 코드 식에 대입하면 VEL 방향은 330°이고 VDIR은 300°이다. |
| outputs:SO1-196 | TABLE HEADER 내용·행 수·overflow | `swashuse PDF p.121` `output is written in fixed format to file with headers giving name of variable and unit per column.` / `numbers too large to be written will be shown as: ****.` / `Number of header lines is 4.` | `src/swanout2.ftn:1391–1397` `WRITE (NREF, 20) OUT_COMMENT                                  40.13` / `20        FORMAT (A)` / `WRITE (NREF, 43) OUT_COMMENT, PROJNR, PSNAME, TRIM(VERTXT)    40.13` / `43        FORMAT (A1, ' Run:', A4,'  Table:',A8, 10X,                   40.13` / `     &      'SWASH version:', A)                                          40.13`<br>`src/swanout2.ftn:1436` `WRITE (NREF, '(A)') OUTLIN(1:LINKAR-1)`<br>`src/swanout2.ftn:1476–1477` `WRITE (NREF, '(A)') OUTLIN(1:LINKAR-1)` / `WRITE (NREF, 20) OUT_COMMENT                                  40.13`<br>`src/swanout2.ftn:1594` `FSTR = '(F13.X)'` | B 문서 오기 | TABP·TABI HEADER TABLE은 첫 데이터 앞에 7행을 쓴다. |
| outputs:SO1-197 | TABLE NOHEADER·파일명 | `swashuse PDF p.121` `output is written in floating point format to file and has no headers; it is intended primarily for processing by other programs.` / `Default for option HEADER is output to the PRINT file.` / `In case of NOHEADER the filename is required.` | `src/SwashReqOutQ.ftn90:394` `call INCSTR ('FNAME', FILENM, 'STA', ' ')`<br>`src/SwashReqOutQ.ftn90:405` `nref = PRINTF`<br>`src/swanout2.ftn:1591` `FSTR = FLT_TABLE                                          40.13` | B 문서 오기 | TABLE은 NOHEADER에서도 파일명 생략을 허용한다. 이 경우 PRINT 파일에 쓴다. |
| outputs:SO1-219 | Hrms 번호 없는 식 | `swashuse PDF p.145` `RMS wave height, in meters, defined as` / `H_{\mathrm{rms}}=\frac12\sqrt2 H_s` | `src/SwashQuanOutp.ftn90:2293` `oparr(:,19) = 0.5 * sqrt(2.) * oparr(:,18)`<br>`src/SwashElemOutp.ftn90:324` `if ( oqproc(24) ) voq(:,voqr(24)) = 0.5 * sqrt(2.) * hsig(:)` | F 표기 차이 | 수식의 `1/2`와 코드의 0.5는 같은 계수이다. HRMS는 두 출력 경로 모두 Hs에 같은 계수를 곱한다. §5의 F는 표기 차이만 뜻한다. |
| outputs:SO1-220 | Hs 출력의 표준편차 정의 | `swashuse PDF p.145` `computed as four times the standard deviation of the surface elevation over the duration [dur]` / `in the final stage of the simulation` | `src/SwashAverOutp.ftn90:96–97` `setup (nm) = setup (nm) + s1(nm)` / `etavar(nm) = etavar(nm) + s1(nm)*s1(nm)`<br>`src/SwashAverOutp.ftn90:119` `setup = setup / nwavoutp`<br>`src/SwashAverOutp.ftn90:121` `hsig = 4. * sqrt( max( etavar / (nwavoutp-1.) - setup*setup, 0. ) )`<br>`src/SwashModule2.ftn90:195` `real, dimension(:)    , save, allocatable :: etavar            ! variance of the surface elevation` | E 코드 결함 후보 (강함) | HSIG 식의 제곱합 분모는 `N−1`이고 평균 수위의 분모는 N이다. 상수 수위의 표준편차를 0으로 만들지 못하므로 E 후보를 유지한다. SO1-119와 같은 문제이다. |
| outputs:SO1-249 | RAY의 곡선형 입력 격자 거부 | — | `src/SwashReqOutL.ftn90:422–423` `else if ( igtype(1) == 2 .or. igtype(7) == 2 ) then` / `call msgerr (2, 'keyword RAY not supported in case of curvilinear bottom grid')` | C 문서 누락 | RAY는 곡선형 바닥·수위 입력 격자를 거부한다. |
| outputs:SO1-250 | GROUP 별칭·추가 순서 검사 | — | `src/SwashReqOutL.ftn90:179` `if (KEYWIS('GROUP') .or. KEYWIS ('SUBG')) then`<br>`src/SwashReqOutL.ftn90:195` `if ( ix1 < 1 .or. ix2 > MXCGL-1 .or. ix1 > ix2 .or. iy1 < 1 .or. iy2 > MYCGL-1 .or. iy1 > iy2 ) then` | C 문서 누락 | 코드는 최상위 SUBG 별칭도 허용한다. 최저 인덱스가 최고 인덱스보다 크면 오류를 낸다. |
| outputs:SO1-251 | CURVE 분할 수 보정 | — | `src/SwashReqOutL.ftn90:283–285` `if ( intv <= 0 ) then` / `call msgerr (2, '[int] is negative or zero')` / `intv = 1`<br>`src/SwashReqOutL.ftn90:281–282` `call ININTG ('INT',intv,'REP',-1)` / `if ( intv /= -1 ) then` | C 문서 누락 | `intv = -1`은 반복 입력 종료값이다. 그 밖의 0 이하 분할 수는 오류 메시지를 낸 뒤 1로 바꾼다. C는 이 입력 예외 처리에 한정한다. |
| outputs:SO1-252 | RAY 분할 수 보정·한 광선 경고 | — | `src/SwashReqOutL.ftn90:451–453` `if ( intd <= 0 ) then` / `call msgerr (2, '[int] negative or zero')` / `intd = 1`<br>`src/SwashReqOutL.ftn90:489` `if ( mip == 1 ) call msgerr (1,'only one ray is defined')`<br>`src/SwashReqOutL.ftn90:449–450` `120     call ININTG ('INT',intd,'REP',-1)` / `if ( intd /= -1 ) then` | C 문서 누락 | `intd = -1`은 반복 입력 종료값이다. 그 밖의 비양수 분할 수는 오류 메시지를 낸 뒤 1로 바꾼다. 광선 하나만 정의하면 경고한다. |
| outputs:SO1-253 | ISOLINE 첫 교점·교점 없음 | — | `src/swanser.ftn:2667–2668` `SIRAY = 1` / `GOTO 20`<br>`src/SwashReqOutL.ftn90:560–561` `if ( ii == 0 ) then` / `write (PRINTF, 204) dp, xp+xoffs, yp+yoffs, xq+xoffs, yq+yoffs` | C 문서 누락 | 광선 시작 쪽 첫 교점에서 검색을 끝낸다. SIRAY의 가장 가까운 수심 위치 계산은 성공 표시를 바꾸지 않아 ISOLINE 집합에 들어가지 않는다. |
| outputs:SO1-254 | POINTS 빈 집합·파일 오류 | — | `src/SwashReqOutL.ftn90:368` `call msgerr (2, 'error reading point coordinates from file')`<br>`src/SwashReqOutL.ftn90:396` `if ( mip == 0 ) call msgerr (2, 'no output points found')` | C 문서 누락 | 좌표 파일 오류와 빈 점 집합을 검사한다. |
| outputs:SO1-255 | 평균 기간·벡터 기준의 공유 상태 | — | `src/SwashReadInput.ftn90:702` `if ( qr(5) /= -999. ) twavoutp = qr(5)`<br>`src/SwashReadInput.ftn90:706` `if ( qr(5) /= -999. ) tcuroutp = qr(5)`<br>`src/SwashReadInput.ftn90:710` `if ( qr(5) /= -999. ) ttraoutp = qr(5)`<br>`src/SwashReadInput.ftn90:714` `if ( qr(5) /= -999. ) tturoutp = qr(5)`<br>`src/SwashReadInput.ftn90:744` `outpar(2) = qr(7)` | C 문서 누락 | 같은 범주의 출력량은 평균 기간을 공유한다. 모든 방향·벡터는 한 기준 상태를 공유한다. 뒤 명령이 같은 상태를 덮어쓴다. |
| outputs:SO1-258 | 출력 요청 최대 250 | — | `src/SwashModule2.ftn90:64` `integer, parameter               :: max_outp_req = 250         ! maximum number of output requests`<br>`src/SwashReqOutQ.ftn90:140` `if ( nreoq > max_outp_req ) call msgerr (2, 'too many output requests')` | C 문서 누락 | 요청 수 제한은 250이다. |
| outputs:SO1-259 | 한 층 모드에서 층별 요청 제외 | — | `src/SwashReqOutQ.ftn90:206–208` `else if ( ivtype > 50 .and. ivtype < 100 .and. ivtype /= 95 .and. ivtype /= 96 .and. kmax == 1 ) then` / `call msgerr (1, 'this layer-dependent quantity will not be outputted' )` / `write (PRINTF, *) ' -> ', ovsnam(ivtype)` | C 문서 누락 | `kmax=1`은 층별 출력 요청을 경고 후 제외한다. |
| outputs:SO1-260 | 추가 출력 이름 | — | `src/SwashInit.ftn90:833` `ovkeyw(ivtype) = 'XC'`<br>`src/SwashInit.ftn90:845` `ovkeyw(ivtype) = 'YC'`<br>`src/SwashInit.ftn90:1097` `ovkeyw(ivtype) = 'AAAA'`<br>`src/SwashInit.ftn90:1509` `ovkeyw(ivtype) = 'DIVU'`<br>`src/SwashInit.ftn90:1521` `ovkeyw(ivtype) = 'DIVQ'`<br>`src/SwashReqOutQ.ftn90:203` `if ( (ivtype == 95 .or. ivtype == 96) .and. optg /= 5 ) then` | C 문서 누락 | XC·YC는 내부 격자 좌표이다. AAAA는 보조량 이름이다. DIVU·DIVQ는 비정형 연산자 출력이다. 등록만으로 모든 이름의 계산 경로를 보장하지 않는다. |
| outputs:SO1-261 | TABLE의 STAB·IND·FIL 별칭 | — | `src/SwashReqOutQ.ftn90:379` `if ( KEYWIS('NOHEAD') .or. KEYWIS ('FIL') ) then`<br>`src/SwashReqOutQ.ftn90:381–382` `else if ( KEYWIS ('IND') ) then` / `rtype = 'TABI'`<br>`src/SwashReqOutQ.ftn90:385–386` `else if ( KEYWIS ('STAB') ) then` / `rtype = 'TABT'`<br>`src/swanout2.ftn:1571–1574` `IF (RTYPE.EQ.'TABI') THEN` / `WRITE (OUTLIN(1:8), '(I8)') IP` | C 문서 누락 | STAB·IND는 `swashuse PDF p.162`와 misc/swash.edt:320에 이미 있다. C는 p.120 본문 선택도의 두 형식 누락과 FIL 별칭·IND 첫 열의 설명 누락에 한정한다. FIL은 NOHEADER와 같은 형식이다. IND는 점 일련번호를 첫 열에 쓴다. |
| outputs:SO1-262 | MATLAB 헤더 금지·확장자 대소문자 | — | `src/SwashReqOutQ.ftn90:154–155` `if ( index ( FILENM, '.MAT' ) /= 0 .or. index ( FILENM, '.mat' ) /= 0 ) then` / `call msgerr (4, 'no header allowed for Matlab files')` | C 문서 누락 | MATLAB 파일은 NOHEADER가 필요하다. 인식은 .MAT와 .mat 문자열에 한정한다. |
| outputs:SO1-263 | 비정형 ELEMESH 자동 생성 | — | `src/SwashReadInput.ftn90:2570–2572` `opstmp%psname = 'ELEMESH'` / `opstmp%pstype = 'U'` / `opstmp%mip    = ncells`<br>`src/SwashOutput.ftn90:203` `call SwashElemOutp ( oqproc, mip, nvoqp, nvoqk, voqr, voq, voqk )` | C 문서 누락 | 비정형 셀 중심 집합을 별도 생성한다. 변수 계산은 QuanOutp와 다른 경로이다. |
| outputs:SO1-264 | 병렬 텍스트 파일명 | — | `src/SwashReqOutQ.ftn90:171–173` `if ( parll .and. .not.vtk ) then` / `ilpos = index ( FILENM, ' ' )-1` / `write (FILENM(ilpos+1:ilpos+4),201) inode`<br>`src/SwashReqOutQ.ftn90:521` `201 format('-',i3.3)` | C 문서 누락 | 텍스트·MAT 파일명 뒤에도 프로세스 번호를 붙인다. |
| outputs:SO1-265 | 평균·출력의 종료 허용 구간 | — | `src/SwashAverOutp.ftn90:117` `if ( abs(dif) < 0.99*dt .and. nwavoutp > 1. ) then`<br>`src/SwashDecOutQ.ftn90:127` `if ( abs(dif) < 0.99*dt .and. outr(2) < 0. ) then`<br>`src/SwashAverOutp.ftn90:83` `dif = tfinc - timco`<br>`src/SwashAverOutp.ftn90:140` `if ( abs(dif) < 0.99*dt .and. ncuroutp > 0. ) then` | C 문서 누락 | 비정상 계산에서 출력 간격이 미지정인 `outr(2) < 0.` 요청은 `abs(dif) < 0.99*dt`일 때 출력한다. 여기서 `dif = tfinc - timco`이다. 평균 최종화도 같은 시간 허용 구간을 사용하지만 파랑은 표본 수가 1보다 커야 하고 유속은 0보다 커야 한다. 평균 최종화의 중복 수행 방지 플래그는 없다. |
| outputs:SO1-267 | 여러 COMPUTE에서 평균 카운터 유지 | `swashuse PDF p.145` `computed as four times the standard deviation of the surface elevation over the duration [dur]` | `src/SwashInit.ftn90:485–488` `ncuroutp =  0.` / `ntraoutp =  0.` / `nturoutp =  0.` / `nwavoutp =  0.`<br>`src/SwashCheckPrep.ftn90:5773–5774` `setup  = 0.` / `etavar = 0.`<br>`src/SwashCheckPrep.ftn90:5807` `mvelu = 0.`<br>`src/SwashAverOutp.ftn90:142` `mvelu = mvelu / ncuroutp`<br>`src/SwashAverOutp.ftn90:133` `ncuroutp = ncuroutp + 1.`<br>`src/SwashMain.ftn90:126` `call SwashInit ( inerr )`<br>`src/SwashMain.ftn90:135` `repeatloop: do`<br>`src/SwashMain.ftn90:158` `call SwashCheckPrep` | E 코드 결함 후보 (강함) | 반복 COMPUTE는 평균 합을 지우지만 평균 표본 카운터를 재설정하지 않는다. 후속 계산의 평균 분모에 앞 계산의 표본 수가 남으므로 E 후보(강함)를 유지한다. 608ffd7·9554c98은 이 경로를 바꾸지 않았다. |
| outputs:SO1-268 | 평균의 표본 가중치 | — | `src/SwashAverOutp.ftn90:133` `ncuroutp = ncuroutp + 1.`<br>`src/SwashAverOutp.ftn90:135` `mvelu = mvelu + u1`<br>`src/SwashAverOutp.ftn90:142` `mvelu = mvelu / ncuroutp`<br>`src/SwashMain.ftn90:279` `dt = 0.5*dt`<br>`src/SwashMain.ftn90:291` `dt = 2.0*dt` | C 문서 누락 | 평균은 시간 단계당 같은 가중치를 준다. dt가 바뀌면 시간 적분 평균과 표본 평균을 구분해야 한다. |
| outputs:SO1-269 | 파랑 평균의 바닥 수심 조건 | — | `src/SwashAverOutp.ftn90:95–100` `if ( dps(nm) > 0. ) then` / `setup (nm) = setup (nm) + s1(nm)` / `etavar(nm) = etavar(nm) + s1(nm)*s1(nm)` / `else` / `setup (nm) = 0.` / `etavar(nm) = 0.` | C 문서 누락 | 이 조건은 순간 총수심이나 wets가 아니다. 양의 바닥 수심에서만 파랑 통계를 누적한다. |
| outputs:SO1-270 | 출력 좌표의 내부 오프셋 | — | `src/swanser.ftn:159` `XX = REAL(XTMP-DBLE(XOFFS))`<br>`src/swanser.ftn:164` `YY = REAL(YTMP-DBLE(YOFFS))`<br>`src/SwashQuanOutp.ftn90:3539` `if ( .not.EQREAL(xp,ovexcv(1)) ) voq(i,1) = xp + xoffs` | C 문서 누락 | 큰 문제 좌표에서 공통 오프셋을 빼서 내부 실수에 저장한다. XP·YP 출력에서 복원한다. |
| outputs:SO1-272 | HEADER BLOCK의 ndec 적용 위치 | `swashuse PDF p.109` `number of decimals in block` / `Maximum is 9.` | `src/swanout2.ftn:631` `CHARACTER (LEN=21) :: WFORM2 = '(1X,I3,1X, 151(F6.0))'              40.13`<br>`src/swanout2.ftn:683` `WRITE (WFORM2(17:17), '(I1)') DEC_BLOCK                         40.13`<br>`src/SwashModule2.ftn90:70` `integer                          :: dec_block =  6             ! number of decimals for fixed-point block`<br>`src/SwashReadInput.ftn90:377` `write (flt_block, 203) nlen, dec_block+8, dec_block` | C 문서 누락 | NDEC는 HEADER BLOCK에서 열 제목과 수치 필드의 폭을 함께 바꾼다. NOHEADER BLOCK에서는 소수 자릿수를 정한다. 일관된 형식 설계이므로 단일 문자 위치의 코드 결함 후보를 철회한다. C는 `swashuse PDF p.109`의 형식별 의미 설명 누락이다. |
| outputs:SO1-279 | 평균량과 순간량을 섞은 요청 | — | `src/SwashReqOutQ.ftn90:264–266` `orqtmp%oqr(1) = -1.` / `orqtmp%oqr(2) = -1.` / `goto 115`<br>`src/SwashReqOutQ.ftn90:492–493` `orqtmp%oqr(1) = -1.` / `orqtmp%oqr(2) = -1.` | C 문서 누락 | 평균량 하나가 BLOCK·TABLE 요청 전체의 OUTPUT 예약을 취소한다. 순간량도 마지막 출력으로 바뀐다. |
| outputs:SO1-280 | 평균 유속의 깊이 평균 순서 | — | `src/SwashQuanOutp.ftn90:274` `oparr(indx,20) = oparr(indx,20) + hku(indx,k)*mvelu(indx,k)`<br>`src/SwashQuanOutp.ftn90:278` `oparr(indx,20) = oparr(indx,20) / hu(indx)`<br>`src/SwashAverOutp.ftn90:133–142` `mvelu = mvelu + u1`<br>`src/SwashQuanOutp.ftn90:264–278` `kmax == 1` / `if ( hu(indx) > 0. ) then` | C 문서 누락 | 층별 속도를 먼저 시간 평균한다. 다층의 깊이 평균은 출력 시점의 양의 총수심과 층 두께로 계산한다. 따라서 순간 깊이 평균 속도의 시간 평균과 다를 수 있다. |
| outputs:SO1-281 | VTK 벡터의 세 성분 | — | `src/SwashVTKWriteData.ftn90:181` `if ( ios == 0 .and. ionod(ip+i) == iproc ) write(uvtk,iostat=ios) data(ip+i,voqr(ivtype)), data(ip+i,voqr(ivtype)+1), 0.` | C 문서 누락 | 수평 벡터의 세 번째 성분은 0이다. VZ 출력은 별도의 스칼라이다. |
| outputs:SO1-282 | ELEMESH의 변수 계산 범위 | — | `src/SwashElemOutp.ftn90:102` `if ( oqproc(6) ) voq(:,voqr(6)) = s1(:)`<br>`src/SwashOutput.ftn90:173` `allocate (voq(mip*nvoqp))`<br>`src/SwashOutput.ftn90:203` `call SwashElemOutp ( oqproc, mip, nvoqp, nvoqk, voqr, voq, voqk )` | C 문서 누락 | ElemOutp에는 바람·FRC·VORT·DRAFT·TIME·TSEC·TKE·EPS·VISC·MTKE·MEPS·MVISC의 계산 분기가 없다. 요청 판독기는 ELEMESH에 대한 변수별 지원 목록을 검사하지 않는다. C는 문서에 없는 이 집합의 지원 범위에 한정한다. |
| outputs:SO1-283 | TABLE의 UNIT 무시 | — | `src/SwashReqOutQ.ftn90:459–460` `if ( KEYWIS('UNIT') ) then` / `call msgerr (1, '[unit] is ignored in this version')` | C 문서 누락 | UNIT 토큰을 읽으면 무시 경고를 낸다. |
| outputs:SO1-285 | 기능을 끈 변수의 예외값 | — | `src/SwashQuanOutp.ftn90:2497` `voq(:,voqr(12)) = ovexcv(12)`<br>`src/SwashQuanOutp.ftn90:3015` `voqk(:,:,voqr(54)) = ovexcv(54)`<br>`src/SwashQuanOutp.ftn90:3315` `voqk(:,:,voqr(82)) = ovexcv(82)`<br>`src/SwashQuanOutp.ftn90:2489–2498` `ihydro /= 0`<br>`src/SwashQuanOutp.ftn90:3003–3034` `iturb /= 0`<br>`src/SwashQuanOutp.ftn90:3303–3316` `ihydro == 1 .or. ihydro == 2` | C 문서 누락 | QuanOutp에서 NHPRES는 `ihydro=0`이면 예외값이다. TKE·EPS는 `iturb=0`이면 예외값이다. NHPRSK는 `ihydro=1·2` 외에는 예외값이다. C는 `swashuse PDF p.115–116`의 출력 정의 목록에서 빠진 이 조건에 한정한다. |
| outputs:SO1-286 | 층을 생략한 스칼라의 최상층 선택 | — | `src/SwashQuanOutp.ftn90:907–909` `if ( lsal  > 0 ) oparr(indx,25) = rp(indxr,1,lsal )` / `if ( ltemp > 0 ) oparr(indx,26) = rp(indxr,1,ltemp)` / `if ( lsed  > 0 ) oparr(indx,27) = rp(indxr,1,lsed )`<br>`src/SwashQuanOutp.ftn90:915–917` | C 문서 누락 | K 접미사가 없는 SAL·TEMP·SED는 활성 스칼라의 최상층(k=1) 값을 선택한다. 평균 스칼라도 최상층 평균을 선택한다. C는 출력 정의에 없는 수직 선택 위치에 한정한다. |
| outputs:SO1-288 | 계산에 필요한 추가 변수 | — | `src/SwashDecOutQ.ftn90:219` `if ( ivtype == 7 .or. ivtype == 8 ) then`<br>`src/SwashDecOutQ.ftn90:223` `oqproc(9) = .true.`<br>`src/SwashDecOutQ.ftn90:269` `if ( ivtype == 56 ) then`<br>`src/SwashDecOutQ.ftn90:273` `oqproc(54) = .true.`<br>`src/SwashQuanOutp.ftn90:949` `oparrk(indx,0:kmax,17) = vnu3d(indxr,0:kmax)` | C 문서 누락 | 크기·방향 요청은 벡터 성분 계산을 추가한다. VISC·MVISC 요청은 TKE·EPS 또는 평균 TKE·EPS 계산을 추가한다. 실제 VISC 값은 vnu3d에서 읽는다. MVISC의 평균량 재구성은 SO1-161(C)을 참조한다. |
| outputs:SO1-289 | 현재 노트의 HSIG 식 | swash-output.md:138 ``\| wave height $H_s$ \| `etavar += s1²` \| $H_s = 4\sqrt{\max(\overline{\zeta^2}/(n-1)-\bar\zeta^2,\,0)}$ `:121` \|`` | `src/SwashAverOutp.ftn90:97` `etavar(nm) = etavar(nm) + s1(nm)*s1(nm)`<br>`src/SwashAverOutp.ftn90:121` `hsig = 4. * sqrt( max( etavar / (nwavoutp-1.) - setup*setup, 0. ) )`<br>`8756667:src/SwashAverOutp.ftn90:94` `etavar = etavar + s1*s1` | B 문서 오기 | etavar는 수면 높이 제곱의 합이다. 평균으로 적은 노트 식은 제곱합으로 고쳐야 한다. 코드 식은 `hsig = 4. * sqrt( max( etavar / (nwavoutp-1.) - setup*setup, 0. ) )`이다. 표준 분산 정의와의 차이는 SO1-220(E)을 참조한다. |
| outputs:SO1-290 | 현재 노트의 표준 분산 정의 | swash-output.md:143 ``핵심: $H_s$는 표고분산의 제곱근에 4를 곱한 표준 정의(`:121`). 누적은 `dif > t*outp`가 아닐 때(최종 구간)만, 최종화는 `abs(dif) < 0.99*dt`(마지막 스텝)에 1회 수행(`:89,117` 등). 어느 quantity가 평균 대상인지는 ReqOutQ에서 `lwavoutp`/`lcuroutp`/`ltraoutp`/`lturoutp` 플래그로 설정됨(§6 참조).`` | `src/SwashModule2.ftn90:195` `real, dimension(:)    , save, allocatable :: etavar            ! variance of the surface elevation` | B 문서 오기 | 코드의 분산식은 수면 높이 표준편차의 정의와 다르다. 같은 비영 수면 높이 c를 `N>1`회 누적하면 제곱근 안에 `c²/(N−1)`이 남는다. 표준 분산은 0이다. 노트의 표준 정의 단정을 고치고 SO1-220(E)의 결함 후보를 함께 기록한다. |
| outputs:SO1-291 | 현재 노트의 누적·최종화 조건 | swash-output.md:137 ``\| setup ($\bar\zeta$) \| `setup += s1` (dry점 0) \| `setup/nwavoutp`, `:117-123` \|``; swash-output.md:143 ``핵심: $H_s$는 표고분산의 제곱근에 4를 곱한 표준 정의(`:121`). 누적은 `dif > t*outp`가 아닐 때(최종 구간)만, 최종화는 `abs(dif) < 0.99*dt`(마지막 스텝)에 1회 수행(`:89,117` 등). 어느 quantity가 평균 대상인지는 ReqOutQ에서 `lwavoutp`/`lcuroutp`/`ltraoutp`/`lturoutp` 플래그로 설정됨(§6 참조).`` | `src/SwashAverOutp.ftn90:95` `if ( dps(nm) > 0. ) then`<br>`src/SwashAverOutp.ftn90:117` `if ( abs(dif) < 0.99*dt .and. nwavoutp > 1. ) then`<br>`8756667:src/SwashAverOutp.ftn90:98` `nwavoutp > 1.` | B 문서 오기 | 현재 파랑 통계는 최종 평균 기간 안에서 `dps>0`인 점만 누적한다. 노트의 dry점 설명은 b909ee6의 `hs>epsdry` 판정과는 맞지만 현재 조건과 다르다. 최종화는 `if ( abs(dif) < 0.99*dt .and. nwavoutp > 1. ) then`이다. 1회만 수행하게 하는 플래그는 없다. 현재 조건을 빠뜨린 노트의 B 판정은 유지한다. |
| outputs:SO1-292 | 현재 노트의 변수 매핑 | 대조 전 노트는 키워드와 ivtype의 매핑을 본문 범위 밖으로 분류했다. (보고서 §4 SO1-292의 `swash-output.md:171` 인용). | `src/SwashInit.ftn90:809–812` `ovkeyw(ivtype) = 'HS'` / `ovsnam(ivtype) = 'Hsig'` / `ovlnam(ivtype) = 'Significant wave height'` / `ovunit(ivtype) = uh` | B 문서 오기 | 출력 키워드와 ivtype의 직접 근거는 SwashInit의 개별 대입이다. 현재 보고서 §2.4에 그 매핑이 있다. 본문 §6은 이 대입과 보고서 §2.4의 매핑을 인용한다. [10-15 전수 검증 정정] |
| outputs:SO1-293 | 현재 노트의 출력 변수 개수 | swash-output.md:238 ``핵심 설계: (1) **위치-요청 직교 분리**(`opsdat`/`orqdat`)로 한 위치에 다중 quantity·다중 출력형식 지원, (2) **oqproc 플래그 + 정수 quantity 번호**로 ~94종 출력변수를 단일 큰 분기로 처리, (3) 구조격자는 `SWIPOL`·비구조격자는 `SwanInterpolateOutput`로 보간 추상화, (4) VTK는 41.95(2022)에 ParaView 지원으로 추가된 별도 binary-append writer.`` | `src/SwashModule1.ftn90:64` `integer, parameter                         :: nmovar = 120 ! maximum number of output variables`<br>`5d279d7:src/SwashInit.ftn90:1468` `ovkeyw(ivtype) = 'MSEDK'`<br>`5d279d7:src/SwashInit.ftn90:1481` `ivtype = 101`<br>`9b8a012:src/SwashInit.ftn90:1481` `ivtype = 95`<br>`9b8a012:src/SwashInit.ftn90:1482` `ovkeyw(ivtype) = 'DIVU'`<br>`9b8a012:src/SwashInit.ftn90:1493` `ivtype = 96`<br>`9b8a012:src/SwashInit.ftn90:1494` `ovkeyw(ivtype) = 'DIVQ'`<br>`src/SwashInit.ftn90:1509` `ovkeyw(ivtype) = 'DIVU'`<br>`src/SwashInit.ftn90:1521` `ovkeyw(ivtype) = 'DIVQ'` | A 판 차이 | 출력 등록 수 94개는 `5d279d7`(2022-12-27, v9.01) 기준이다. `9b8a012`(2023-10-11, v10.01)에서 DIVU와 DIVQ가 추가되어 현재 등록 수는 96개이다. `nmovar=120`은 배열 상한이다. ([git 판정 AD:SO1-293](../../../_staging/recovery/compare/SWASH-git-verify-AD.md#3-a-후보-판정-표)) |

---
title: "SWASH wetting-drying + breaking + depth update — 마스크 판정·bore-front breaking·총수심 갱신 커널"
model: SWASH
component: src (wetting-drying / wave breaking / depth update)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashDryWet.ftn90(:85-228), SwashUDryWet.ftn90(:82-122), SwashBreakPoint.ftn90(:95-242), SwashUBreakPoint.ftn90(:94-168), SwashRunupHeight.ftn90(:88-154), SwashUpdateDepths.ftn90(:113-805), SwashUpdateUDepths.ftn90(:111-389), SwashUpdDepu.ftn90(:104-461), SwashUpdUDepu.ftn90(:104-313) 의 판정식·임계값·스킴 직접 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH wetting-drying + breaking + depth update

> 침수-건조(wetting/drying) 마스크 판정, bore-front 기반 wave breaking 판정, runup 높이, 그리고 총수심(total depth) 갱신 커널. 경로: raw/source_code/swash/src/

이 노트는 9개 서브루틴을 다룬다. 구조격자(structured) 버전과 비구조격자(unstructured, 접두 `U`) 버전이 쌍을 이룬다.

| 기능 | 구조격자 | 비구조격자 |
|---|---|---|
| wetting/drying 마스크 | `SwashDryWet` | `SwashUDryWet` |
| bore-front breaking | `SwashBreakPoint` | `SwashUBreakPoint` |
| runup 높이 (출력용) | `SwashRunupHeight` (1D만) | — |
| 수심 초기화/갱신 (full) | `SwashUpdateDepths` | `SwashUpdateUDepths` |
| 수심 갱신 (velocity-pt only) | `SwashUpdDepu` | `SwashUpdUDepu` |

## 1. wetting/drying 마스크 판정 (`SwashDryWet`)

Purpose 주석: `"Performs wetting and drying checks in water level and velocity points"` (SwashDryWet.ftn90:41), Method: `"Update mask arrays"` (:43).

### 1.1 핵심 판정: epshu 임계값

velocity-point(u/v)의 wet/dry는 그 점의 수심 `hu`/`hv`가 최소수심 `epshu`를 초과하는지로 결정:

```
if ( hu(nm) > epshu ) then
   wetu(nm) = 1   ! wet
else
   wetu(nm) = 0   ! dry
```
(1D: SwashDryWet.ftn90:85-93; 2D u-점: :132-140; v-점은 `hv > epshu`로 :165-173)

`epshu`는 drying/flooding 최소수심 threshold이며, `SwashUpdateDepths`에서 `epshu = epsdry`로 동기화된다(SwashUpdateDepths.ftn90:186, :429 — "also reset minimal depth at faces"). 즉 **face(velocity-pt)의 dry threshold와 cell(wl-pt)의 dry threshold는 동일 값**.

### 1.2 water-level point 판정: 인접 velocity-point의 OR

wl-point는 인접 velocity-point 중 하나라도 wet이면 wet:

- 1D: `( 1 - wetu(nm) ) * ( 1 - wetu(nmd) ) == 0` → `wets(nm) = 1` (SwashDryWet.ftn90:111-119). 곱이 0 = 둘 중 하나 이상이 wet.
- 2D: 네 인접면(좌우 u, 상하 v)의 곱: `( 1 - wetu(nm) ) * ( 1 - wetu(nmd) ) * ( 1 - wetv(nm) ) * ( 1 - wetv(ndm) ) == 0` → wet (SwashDryWet.ftn90:203-211).

즉 **wl-point가 dry가 되려면 둘러싼 모든 velocity-point가 dry여야 함** (보수적 wetting).

### 1.3 영구 dry 점·병렬·주기경계 처리

- 영구 dry 점(인덱스 1)은 강제로 0: `wetu(1)=0`(:147), `wetv(1)=0`(:180), `wets(1)=0`(:218).
- subdomain 간 마스크 교환: `SWEXCHGI`(:99,151,184,228).
- 반복격자(repeating grid) 동기화: `periodici`(:156,189,222).

### 1.4 비구조격자판 (`SwashUDryWet`)

Purpose: `"Performs wetting and drying checks in cells and faces of triangular mesh"` (SwashUDryWet.ftn90:40).

- face: `hu(iface) > epshu` → `wetu(iface)=1` (SwashUDryWet.ftn90:84-92).
- cell: 셀의 모든 face의 `(1 - wetu(iface))` 곱이 0이면 wet (:100-120). 구조격자와 동일한 OR 논리지만 셀의 임의 개수 face(`cell(icell)%nof`)에 대해 일반화.

## 2. bore-front wave breaking 판정 (`SwashBreakPoint`)

Purpose 주석(verbatim): `"Determines grid points where steep bore-like wave front occurs for wave breaking"` (SwashBreakPoint.ftn90:43).

Method 주석(verbatim): `"Update mask array at those points where the vertical speed of the free surface exceeds a fraction of the wave phase speed. At those points, hydrostatic pressure is assumed and remains so at the front face of the breaking wave."` (:47-49), 이어서 운동량 보존 결합으로 `"a correct amount of energy dissipation on the front face of the breaking wave"` 및 비선형 파 특성(asymmetry, skewness) 보존(:51-53).

### 2.1 판정 변수 — 자유표면 수직속도 vs 천수 위상속도

- 임계 파라미터: `alpha = psurf(1)` (breaking onset), `beta = psurf(2)` (post-breaking 재개시) (SwashBreakPoint.ftn90:95-96, 80-81 주석).
- 천수 위상속도: `rootgh = sqrt( grav * hs(nm) )` ($\sqrt{g\,h_s}$) (:115).
- 자유표면 수직속도: `dsdt = ( s1(nm) - s0(nm) ) / dt` ($\partial\zeta/\partial t \approx (\zeta^{n+1}-\zeta^n)/\Delta t$) (:117).

### 2.2 breaking 판정 분기 (1D, :113-145)

전제: 해당 점이 wet이고 압력점이 아님 — `wets(nm) == 1 .and. presp(nm) == 0` (:113).

| 조건 | 결과 |
|---|---|
| `dsdt > alpha * rootgh` | onset: `brks=1`, `q(nm,:)=0` (비정수압 압력 0 → hydrostatic) (:119-124) |
| `dsdt > beta * rootgh` 이고 인접점이 breaking(`iwrk(nmd/nmu)==1`) | 재개시: `brks=1`, `q=0` (:125-130) |
| `dsdt > 0.` 이고 이미 `brks==1` | breaking 유지: `q=0` (단 brks 갱신 안 함) (:131-134) |
| 그 외 | `brks=0` (비breaking) (:135-138) |

핵심: **breaking point에서 비정수압 압력 q를 0으로 강제 → 그 점은 정수압(shallow-water/bore)으로 전환**. 이것이 Method 주석의 "hydrostatic pressure is assumed"의 구현이다. `alpha`(onset) > `beta`(re-init) 위계로 hysteresis 구현 — 한번 깨진 파의 뒤쪽 점들이 더 낮은 임계로 계속 breaking 상태 전파.

2D판(:172-204)은 동일 논리에 4방향 인접(`iwrk` nmd/nmu/ndm/num)을 OR로 검사(:184). breaking 이전 상태는 루프 시작 전 `iwrk(:,1) = brks(:)`로 보존(:100).

### 2.3 wl-mask 재갱신 — breaking 점은 dry로

루프 후 전 격자에서 `wets(nm)==1 .and. brks(nm)==1` 이면 `wets(nm)=0` (SwashBreakPoint.ftn90:238-242). 즉 **breaking 점은 wetting/drying 마스크 상으로 dry 처리** → 후속 비정수압 계산에서 제외. 주석: `"re-update mask array for wetting and drying at water level points by taking into account the breaking points"` (:236).

기타: 내부 wave generation source 영역(`srcm(nm) /= 0.`)에서는 breaking 비활성화(`brks=0`, :217-225, 주석 "breaking deactivated inside the source region"). 영구 dry점 `brks(1)=0`(:211), 교환(`SWEXCHGI`:229)·주기경계(`periodici`:234).

### 2.4 비구조격자판 (`SwashUBreakPoint`)

동일 onset/re-init 논리(SwashUBreakPoint.ftn90:109-152). 단 전제는 `wets(icell)==1`만(:103 — `presp` 조건 없음). 재개시 분기는 셀의 face들을 돌며 인접 셀(`FACEC1/FACEC2`)이 breaking인지 검사(:115-143). breaking 셀은 `q(icell,:)=0`(:113,136,146), 마지막에 `wets==1 .and. brks==1 → wets=0`(:164-167).

## 3. runup 높이 (`SwashRunupHeight`) — 출력 전용, 1D 한정

Purpose: `"Calculates wave runup height for the purpose of output"` (SwashRunupHeight.ftn90:40). Method: `"Based on the intersection between free surface and bottom level + threshold for runup"` (:44). Note: `"we restrict ourselves to 1D only and wave propagation is pointing eastward!"` (:46).

### 3.1 알고리즘

1. runup threshold `delrp` 사용(:54 use, :112). 동쪽(ml)에서 서쪽(mfu)으로 스캔하며 **최초로 `hs(nm) > delrp`인 점 mr**을 찾음 — 즉 가장 육지쪽(가장 큰 m) wet 점 (:103-117).
2. 병렬 도메인 전체에서 최대 인덱스 선택: 로컬→글로벌 변환 후 `SWREDUCE(...,SWMAX)`(:121-125).
3. 수직 runup level을 선형보간으로 산출 (SwashRunupHeight.ftn90:134):

   $$ rh = s_1(mr) + (\delta_{rp} - h_s(mr))\cdot\frac{s_1(mr{+}1) - s_1(mr)}{h_s(mr{+}1) - h_s(mr)} $$

   즉 자유표면과 (bottom level + threshold) 교차점에서의 수위. `mr`이 유효 범위(`mr > mf .and. mr < mlu`) 밖이면 missing value `ovexcv(115)`(:136-140).
4. 병렬 reduce 최대(:142), 출력량 115번에 저장 `voq(voqr(115)) = rh`(:154).

좌측 경계가 파 입사(`ibl(1)` 2/3/7) 아니면 경고 후 계산 생략(:94-101, "no waves are imposed on west side").

⚠ 비구조격자·2D runup 출력 서브루틴은 본 배정 파일에 없음 — runup 출력은 1D 전용으로 보임(source-needed: 2D/unstructured runup 출력 경로).

## 4. 총수심 갱신 (`SwashUpdateDepths`)

Purpose: `"Initialize / update water depths in both water level and velocity points"` (SwashUpdateDepths.ftn90:42).

### 4.1 wl-point 총수심과 음수심 보정

기본식: `hs(nm) = s1(nm) + dps(nm)` (총수심 = 수위 + 바닥깊이) (SwashUpdateDepths.ftn90:113).

음수심 발생 시(`hs < 0` 이고 Newton 반복 아님) 처리(:115-132):
- `hs < -epsdry` (임계 초과 음수): 경고 출력 후 `s1(nm) = 0.99*epsdry - dps(nm)`, **`epsdry`를 `-1.01*hs`로 키움**(:122-123), `adapted=.true.`.
- 그 외 작은 음수: `s1(nm) = 0.99*epsdry - dps(nm)`만(:127).
- 후 `hs` 재계산(:130).

이는 **적응형 dry threshold**: 수위가 바닥보다 너무 내려가면 epsdry를 동적으로 늘려 안정화. 단 병렬 reduce 후 `epsdry > 0.01`(1cm) 초과 시 치명 오류 — `"INSTABLE: water level is too far below the bottom level!"` + "Please reduce the time step!"(:176-182, 419-425). 마지막에 `epshu = epsdry`로 face threshold 동기화(:186, 429).

floating object(`ifloat /= 0`): `hs = min(dps-flos, hs)`로 상한(:136). Newton 반복(`inewt /= 0`): `hs = max(epsdry, hs)`로 하한(:140).

### 4.2 u/v-point 수심 — 평균·upwind·시간외삽

세 종류 수심을 계산:
1. **평균(averaging)**: `hum(nm) = 0.5*(hs(nm)+hs(nmu))` (SwashUpdateDepths.ftn90:201; v: `hvm`:483).
2. **시간 외삽**: `humn = 1.5*hum - 0.5*humo` (이전값 `humo=hum`) — "extrapolate ... to improve accuracy of momentum-conservative time integration"(:210-212, 467; v:503).
3. **upwind**: 속도 방향에 따라 풍상측 수위 사용(:225-237):

```
if ( u(nm) > 1.0e-5 ) then   hu(nm) = s1(nm)  + dpu(nm)   ! 풍상 = nm
else if ( u(nm) < -1.0e-5 )  hu(nm) = s1(nmu) + dpu(nm)   ! 풍상 = nmu
else                         hu(nm) = max( s1(nm), s1(nmu) ) + dpu(nm)
```

upwind 임계속도는 `±1.0e-5` m/s. `depcds`가 참이면 upwind 대신 평균 사용: `hu = hum`(:272-274). v-point는 동일 논리(:591-603).

### 4.3 고차 보정 (flux limiter, `corrdep`)

`corrdep` 활성 시 내부 u/v점에 MUSCL-류 고차 보정 추가:
- 파라미터 `propsc=pnums(11)`, `kappa=pnums(12)`, `mbound=pnums(13)`, `phieby=pnums(14)`(:282-285).
- 풍상 방향 두 gradient로 `fluxlim(grad1,grad2)` 호출, `hu += 0.5*fluxlim(...)` (u>0: :310-313; u<0: `hu -= 0.5*fluxlim`:322-325).
- **음수심 안전장치**: 보정 전 `s1min + depmin < 0.` 이면 `cycle`로 보정 생략(:308, 320) — 건조부 근처에서 limiter가 음수심 유발 방지.
- `fluxlim`은 외부 함수(선언 :84). ⚠ 본 파일에 정의 없음(source-needed: fluxlim 정의 위치).

### 4.4 inundation depth

전 격자: `hindun(nm) /= 1. .and. hs(nm) > hrunp` 이면 `hindun(nm) = 1.` (SwashUpdateDepths.ftn90:804-806). 즉 **수심이 runup threshold `hrunp`를 한 번이라도 넘으면 침수표시(1) 영구 기록** — maximum inundation 추적용 latch.

## 5. 비구조격자 수심 갱신 (`SwashUpdateUDepths`)

Purpose: `"Initialize / update water depths in both cells and faces"` (SwashUpdateUDepths.ftn90:42).

- cell 총수심·음수심 보정: 구조격자와 동일(`hs(icell)=s1+dps`, epsdry 적응, :113-136).
- face 평균수심: 좌우 셀 선형보간 — `h = finp*hs(icelll) + (1.-finp)*hs(icellr)` (보간계수 `finp=FACELINPF`, :171-180), 경계 셀이면 존재하는 셀값(:182-188). 시간외삽 `humn=1.5*hum-0.5*humo`(:198).
- face upwind: `u(iface) > epsuf` → `s1(icelll)+dpu`, `< -epsuf` → `s1(icellr)+dpu`, 사이는 max(:219-231). 경계 셀 별도 처리(:211-217). upwind 임계는 `epsuf`(구조격자의 1e-5와 달리 명명 상수).
- 고차 보정: **풍상 셀의 most-upwave vertex** 주변 area-weighted 평균 수위·바닥(`wlu`,`du`)로 r-ratio gradient 산출 후 `hu += 0.5*fluxlim`(:247-381, 주석 "for the r-ratio the most upwave vertex of upwind cell is used" :248). 음수심 가드 `s1min+depmin<0 → cycle`(:315,368).
- inundation: `hs(icell) > hrunp → hindun=1.`(:387-389).

## 6. velocity-point 전용 수심 갱신 (`SwashUpdDepu` / `SwashUpdUDepu`)

`SwashUpdDepu` Purpose: `"Update water depths in velocity points"` (SwashUpdDepu.ftn90:40). `SwashUpdateDepths`의 velocity-point 부분만 떼낸 경량판으로, **wl-point 음수심 보정·epsdry 적응을 다시 하지 않는다**(이미 호출 전 완료 전제). u-velocity가 필수 인자, v는 optional(:54-55).

- upwind/평균/고차보정 논리는 §4.2-4.3과 동일 (SwashUpdDepu.ftn90: upwind :111-123, 평균 :138-141, fluxlim :170-200).
- 단 평균 모드에서 `htot = s1(nm)+dps(nm)`을 직접 재계산해 0.5배 평균(`hu = 0.5*(htot+htotu)`, :138-141) — `SwashUpdateDepths`가 미리 계산한 `hs` 대신 즉석 재계산.
- 고차 보정 가드 조건이 `hu(nm) < (dpu(nm) - flou(nm))`로 단순화(floating object 관련, :170) — `SwashUpdateDepths`는 `ifloat==0 .or. hu < dpu-flou`(:301)와 미세하게 다름. ⚠ 파일 간 차이: `SwashUpdDepu`에는 `ifloat==0` OR 분기가 없음(:170 vs SwashUpdateDepths.ftn90:301). 즉 `SwashUpdDepu`는 `ifloat`와 무관히 `flou`를 항상 쓰는데, floating object 미사용 시 `flou=0`이면 결과 동일할 가능성 — 단정 불가(source-needed: flou 기본값).

`SwashUpdUDepu`는 그 비구조격자판 (Purpose: `"Update water depths at cell faces"` :42). face upwind/평균·most-upwave-vertex 고차보정 논리는 `SwashUpdateUDepths`와 동일(SwashUpdUDepu.ftn90:104-313). 차이: 평균 모드에서 `htotl=s1+dps`를 셀별로 재계산해 보간(:156-159).

## 7. 핵심 메커닉 요약

| 메커닉 | 식/임계 | 출처 |
|---|---|---|
| dry threshold (face) | `hu > epshu` (`epshu = epsdry`) | SwashDryWet:85, SwashUpdateDepths:186 |
| 적응형 epsdry | `epsdry = -1.01*hs` (음수심 시), 상한 0.01m | SwashUpdateDepths:123,176 |
| wl-pt wetting | 인접 velocity-pt 중 1개라도 wet → wet (OR) | SwashDryWet:111,203 |
| breaking onset | `dsdt > alpha*sqrt(g*hs)`, `alpha=psurf(1)` | SwashBreakPoint:119 |
| breaking re-init | `dsdt > beta*sqrt(g*hs)` & 인접 breaking, `beta=psurf(2)` | SwashBreakPoint:125,184 |
| breaking 시 비정수압 | `q(nm,:)=0` (hydrostatic 전환) | SwashBreakPoint:123 |
| breaking → dry | `brks==1 → wets=0` | SwashBreakPoint:240 |
| 총수심 | `hs = s1 + dps` | SwashUpdateDepths:113 |
| u-pt upwind 수심 | 풍상측 `s1 + dpu`, 임계 ±1e-5 (unstr: ±epsuf) | SwashUpdateDepths:225, SwashUpdateUDepths:219 |
| 시간외삽 수심 | `humn = 1.5*hum - 0.5*humo` | SwashUpdateDepths:212 |
| 고차보정 가드 | `s1min + depmin < 0 → cycle` (음수심 방지) | SwashUpdateDepths:308 |
| runup level (1D) | 자유표면-바닥 교차 선형보간 (식 §3.1) | SwashRunupHeight:134 |
| inundation latch | `hs > hrunp → hindun=1` | SwashUpdateDepths:805 |

## 8. 미확인/source-needed

- `fluxlim` 함수 정의(스킴 종류: minmod/van Leer 등) — 본 배정 파일 외부.
- `epsuf`(비구조 upwind 임계) 기본값·`epshu`/`epsdry` 기본 초기값 — 입력 처리 모듈.
- 2D/비구조격자 runup **출력** 경로 — `SwashRunupHeight`는 1D 한정(:46,90).
- `SwashUpdDepu`의 고차보정 가드에서 `ifloat==0` 분기 부재(:170 vs SwashUpdateDepths:301)의 동작상 차이 — `flou` 기본값 확인 필요.

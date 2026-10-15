---
title: "SWASH wetting-drying + breaking + depth update — 마스크 판정·bore-front breaking·총수심 갱신 커널"
model: SWASH
component: src (wetting-drying / wave breaking / depth update)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashDryWet.ftn90(:85-228), SwashUDryWet.ftn90(:82-122), SwashBreakPoint.ftn90(:95-242), SwashUBreakPoint.ftn90(:94-168), SwashRunupHeight.ftn90(:88-154), SwashUpdateDepths.ftn90(:113-805), SwashUpdateUDepths.ftn90(:111-389), SwashUpdDepu.ftn90(:104-461), SwashUpdUDepu.ftn90(:104-313) 의 판정식·임계값·스킴 직접 인용. 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
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

일반 경로는 `if ( inewt == 0 ) epshu = epsdry`로 유속 마스크 문턱값을 맞춘다 (`src/SwashCheckPrep.ftn90:1219`; guide-syntax-build:SG1-130). [10-15 대조 정정]
TIMEI METH IMPL NEWTON은 이 대입을 건너뛰므로 별도 `epshu`를 사용한다 (`src/SwashReadInput.ftn90:1878`; guide-syntax-build:SG1-130). [10-15 대조 정정]
`epshu` 초기값은 1.e-3 m다 (`src/SwashInit.ftn90:122`; guide-syntax-build:SG1-130). [10-15 대조 정정]

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
- 초기값은 α=0.6·β=-1·nufac=1.0이다 (`src/SwashInit.ftn90:326–329`). `BREaking` 입력도 같은 생략값을 사용한다 (`src/SwashReadInput.ftn90:916–918`). 제공된 파서는 `isurf = 1`로 설정하므로 `isurf == 2` 분기는 입력으로 선택할 수 없다 (`src/SwashReadInput.ftn90:911–923`). `isurf == 1`의 준비 단계에서 β가 미지정 값 -1이고 수평 BDF가 이미 지정되어 있으면 β=0.15로 바꾼다 (`src/SwashCheckPrep.ftn90:1072–1078`). 그 밖의 미지정 β는 0.3으로 바꾼다 (`src/SwashCheckPrep.ftn90:1080–1082`). β=0.3이고 수평 이류 스킴이 미지정이면 `pnums(6) = 3.`과 `pnums(7) = 1.`로 중앙차분을 선택한다 (`src/SwashCheckPrep.ftn90:1088–1091`). `BREaking` 입력은 `horwinc = .true.`로 설정한다 (`src/SwashReadInput.ftn90:920`). 같은 입력은 `ihvisc == 0`이면 `ihvisc = 4`로 바꾼다 (`src/SwashReadInput.ftn90:921`). 설명서의 β=0.3 표기는 BDF 조건의 생략값 0.15를 적지 않는다 (이 표의 SG1-142·SI2-159). [10-15 전수 검증 정정]
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

swashuse PDF p.118은 RUNUP에 `NOT FOR 2D-MODE.`를 명시한다 (`src/SwashRunupHeight.ftn90:90`의 `if ( oned ) then`). [10-15 대조 정정]

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
- PL-kappa의 식은 `fluxlim = max( 0., min( mbound*r, fac ) ) * b`이다 (`src/SwashServices.ftn90:443`; inputs-physics-numerics:SI2-243). [10-15 대조 정정]

### 4.4 inundation depth

전 격자의 침수 기록 조건은 `if ( hindun(nm) /= 1. .and. hs(nm) > hrunp ) hindun(nm) = 1.`이다 (`src/SwashUpdateDepths.ftn90:805`). [10-15 대조 정정]
HRUN 침수 기록은 한 COMPUTE 구간 안에서 유지된다 (outputs:SO1-299). [10-15 대조 정정]
다음 COMPUTE의 준비 단계는 `hindun`을 0으로 초기화한다 (`src/SwashCheckPrep.ftn90:3108`; outputs:SO1-266·SO1-299). [10-15 대조 정정]

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
- `SwashUpdDepu`의 고차 보정 조건은 `if ( hu(nm) < ( dpu(nm) - flou(nm) ) ) then`이다 (`src/SwashUpdDepu.ftn90:170`). `SwashUpdateDepths`의 대응 조건에는 `ifloat == 0 .or.`가 있다 (`src/SwashUpdateDepths.ftn90:301`). `flou` 초기값은 -9999.이다 (`src/SwashCheckPrep.ftn90:3085`). 해석: 이 초기값이 유지될 때 첫 조건은 `hu(nm) < dpu(nm) + 9999.`이다. [10-15 전수 검증 정정]

`SwashUpdUDepu`는 그 비구조격자판 (Purpose: `"Update water depths at cell faces"` :42). face upwind/평균·most-upwave-vertex 고차보정 논리는 `SwashUpdateUDepths`와 동일(SwashUpdUDepu.ftn90:104-313). 차이: 평균 모드에서 `htotl=s1+dps`를 셀별로 재계산해 보간(:156-159).

## 7. 핵심 메커닉 요약

| 메커닉 | 식/임계 | 출처 |
|---|---|---|
| dry threshold (face) | `hu > epshu` | `src/SwashDryWet.ftn90:85`; `src/SwashCheckPrep.ftn90:1219`은 `if ( inewt == 0 ) epshu = epsdry`를 적용한다. [10-15 대조 정정] |
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
| inundation latch | 한 COMPUTE 구간 안에서 침수 기록을 유지한다. | `src/SwashUpdateDepths.ftn90:805`; `src/SwashCheckPrep.ftn90:3108` [10-15 대조 정정] |

## 8. 입력·출력 연결

- `fluxlim`은 `src/SwashServices.ftn90:387–443`의 제한자 식을 사용한다 (inputs-physics-numerics:SI2-243). [10-15 대조 정정]
- `epsuf` 초기값은 `epsuf  = 1.e-8`이다 (`src/SwashInit.ftn90:123`; theory-unstructured:ST2-358). [10-15 대조 정정]
- `epsdry` 초기값은 `epsdry = 5.e-5`이다 (`src/SwashInit.ftn90:121`; theory-unstructured:ST2-358). [10-15 대조 정정]
- `epshu` 초기값은 `epshu  = 1.e-3`이다 (`src/SwashInit.ftn90:122`; theory-unstructured:ST2-358). [10-15 대조 정정]
- RUNUP은 `if ( oned ) then` 경로에서 계산한다 (`src/SwashRunupHeight.ftn90:90`; swashuse PDF p.118). [10-15 대조 정정]
- `flou`는 준비 단계에서 -9999.로 초기화한다 (`src/SwashCheckPrep.ftn90:3085`). 두 수심 갱신 루틴의 고차 보정 조건은 §6에 정리되어 있다. [10-15 전수 검증 정정]

## 문서와 코드 차이 (10-15 대조)

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경); 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f`(2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

문서 인용의 인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.

근거 보고서: [guide-syntax-build](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md#5-차이-결론), [inputs-physics-numerics](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md#5-차이-결론), [outputs](../../../_staging/recovery/compare/swash-outputs-vs-code.md#5-차이-결론), [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론), [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| guide-syntax-build:SG1-121 | BREAK 중앙차분 자동 선택 | swashuse PDF p.138: `when the command BREAK is employed, SWASH will automatically apply central differences to the horizontal advection terms` | `src/SwashReadInput.ftn90:909–920`의 `KEYWIS ('BRE')` 경로에서 `isurf = 1`. `src/SwashCheckPrep.ftn90:1072` `if ( isurf == 1 ) then`; `src/SwashCheckPrep.ftn90:1088–1091` `if ( .not. psurf(2) /= 0.3 .and. pnums(6) == -1. ) then` / `pnums(6) = 3.` / `pnums(7) = 1.`; `src/SwashCheckPrep.ftn90:1457–1462`의 `if ( linswe ) then`에서는 `pnums(6) = 1.`. | C 문서 누락 | p.138과 p.96의 BREAK→CDS 설명에는 `beta=0.3`, 수평 UMOM 스킴 미지정이라는 조건이 빠져 있다. 명시한 BDF는 이 자동 선택에서 덮어쓰지 않는다. LINEAR 모드는 뒤에서 pnums(6)을 1로 바꾼다. beta 기본값의 별도 예외는 SG1-142를 참조한다. |
| guide-syntax-build:SG1-130 | SET DEPMIN·EPSHU | swashuse PDF p.140: 수심이 문턱값 아래면 방정식을 풀지 않고 유속을 0으로 둔다. `SET DEPMIN` 기본값은 `0.05 mm`다. | `src/SwashInit.ftn90:121` `epsdry = 5.e-5`; `src/SwashDryWet.ftn90:85` `if ( hu(nm) > epshu ) then`; `src/SwashCheckPrep.ftn90:1219` `if ( inewt == 0 ) epshu = epsdry`; `src/SwashInit.ftn90:122` `epshu  = 1.e-3`; `src/SwashReadInput.ftn90:1878` `if ( KEYWIS ('NEWT') ) inewt = 1`. `src/SwashDryWet.ftn90:85–91`은 조건이 거짓이면 `wetu(nm) = 0`으로 둔다. | C 문서 누락 | DEPMIN 기본값 5.e-5 m는 0.05 mm와 같다. 일반 경로는 `if ( inewt == 0 ) epshu = epsdry`로 유속 마스크 문턱값을 맞춘다. TIMEI METH IMPL NEWTON은 이 대입을 건너뛰므로 별도 epshu를 사용한다. epshu 초기값은 1.e-3 m다. 문서 누락은 p.140의 문턱값 선택 조건이다. epshu 구문 자체는 p.155에 있다. |
| guide-syntax-build:SG1-137 | 쇄파 시작 조건 | swashuse PDF p.141: `\partial\zeta/\partial x>\alpha`.동등 조건은 `\partial\zeta/\partial t>\alpha\sqrt{gd}`다. swashuse PDF p.126은 d를 `the (still) water depth`로 정의한다. | `src/SwashBreakPoint.ftn90:115–119` `rootgh = sqrt( grav * hs(nm) )` / `!` / `dsdt = ( s1(nm) - s0(nm) ) / dt` / `!` / `if ( dsdt > alpha * rootgh ) then`; `src/SwashUpdateDepths.ftn90:113` `hs(nm) = s1(nm) + dps(nm)` | B 문서 오기 | 쇄파 시작 조건의 파속은 현재 총수심 `hs=s1+dps`로 계산한다. p.126의 정수위 수심 d를 쓴 p.141의 식은 수위 변동이 있으면 코드와 다르다. p.88의 h 표기는 코드와 맞으므로 B는 p.141에 한정한다. 총수심 사용은 8756667(2022-09-03 initial release)부터 같아 판 차이 A가 아니다. SG1-140과 같은 수심 기호 오류다. |
| guide-syntax-build:SG1-138 | 비정수압 복귀 경계 | swashuse PDF p.141: `\partial\zeta/\partial t<0`이면 파봉이 통과했다고 가정하고 비정수압으로 복귀한다. 같은 문단은 `a point only becomes non-hydrostatic again if the crest of the wave has passed`라고 적는다. | `src/SwashBreakPoint.ftn90:131–137` `else if ( dsdt > 0. .and. brks(nm) == 1 ) then` / `!` / `q(nm,:) = 0.` / `!` / `else` / `!` / `brks(nm) = 0`; `src/SwashBreakPoint.ftn90:113–137,172–196`은 젖은 비가압 점에서 시작·이웃 재시작·기존 표지 유지 조건을 순서대로 검사한다. `src/SwashCheckPrep.ftn90:1057–1082`는 BREAK의 alpha·beta를 양수로 정한다. | C 문서 누락 | 음의 dsdt에서 비정수압으로 복귀한다는 설명은 구현과 맞는다. 다만 준비 검사를 지난 양수 alpha·beta에서 `dsdt=0`이면 시작·이웃 재시작·기존 표지 유지 조건이 모두 거짓이므로 `brks=0`이 된다. C는 p.141의 파봉 통과 설명이 이 등호 경계를 명시하지 않는 점에 한정한다. 비정수압 복귀 기능 전체가 문서에 없다는 뜻은 아니다. |
| guide-syntax-build:SG1-140 | 쇄파 지속 조건 | swashuse PDF p.141: 이웃 x·y점이 정수압이면 `\partial\zeta/\partial t>\beta\sqrt{gd}`를 쓴다. `\beta<\alpha`다. | `src/SwashBreakPoint.ftn90:184` `else if ( dsdt > beta * rootgh .and. (iwrk(nmd,1) == 1 .or. iwrk(nmu,1) == 1 .or. iwrk(ndm,1) == 1 .or. iwrk(num,1) == 1) ) then`; `src/SwashUpdateDepths.ftn90:113` `hs(nm) = s1(nm) + dps(nm)`; `src/SwashBreakPoint.ftn90:100` `iwrk(:,1) = brks(:)`; `src/SwashBreakPoint.ftn90:174` `rootgh = sqrt( grav * hs(nm) )`. | B 문서 오기 | 쇄파 지속 조건은 현재 총수심 hs와 이웃의 이전 쇄파 표지를 사용한다. p.88의 h는 코드와 맞지만 p.141의 정수위 수심 d는 다르다. B는 p.141에 한정한다. 같은 조건은 8756667(2022-09-03 initial release)부터 있으므로 판 차이 A가 아니다. SG1-137과 같은 수심 기호 오류다. `beta<alpha`는 기본값에서 성립하지만 파서가 이 순서를 강제하는 조건은 아니다. |
| guide-syntax-build:SG1-142 | beta 기본값 | swashuse PDF p.142: beta는 `0.3`으로 설정한다. | `src/SwashInit.ftn90:328` `psurf(2) = -1.`; `src/SwashReadInput.ftn90:917` `call INREAL ( 'BETA' , psurf(2), 'STA',-1.)`; `src/SwashCheckPrep.ftn90:1076–1082` `if ( pnums(6) == 3. .and. pnums(7) == -1. .and. psurf(2) == -1. ) then` / `!` / `psurf(2) = 0.15` / `!` / `else if ( psurf(2) == -1. ) then` / `!` / `psurf(2) = 0.3` | B 문서 오기 | BREAK beta를 생략하면 수평 BDF를 명시한 경우 0.15를 쓴다. 다른 기본 경로는 0.3이다. 실제 조건은 `if ( pnums(6) == 3. .and. pnums(7) == -1. .and. psurf(2) == -1. ) then`이다. p.142와 p.88의 무조건적인 0.3 표기는 이 예외와 다르다. 같은 기본값을 다룬 SG1-909의 B와 맞춘다. CDS 자동 선택의 조건 누락은 SG1-121에서 구분한다. |
| guide-syntax-build:SG1-893 | 젖음·마름 범위와 EPSHU | swashuse PDF p.33·130은 DEPMIN 기본값과 적용 권고를 설명한다. 0.01 m 상한 보정과 EPSHU 연동 조건은 명시하지 않는다. | `src/SwashCheckPrep.ftn90:1185–1191` `if ( .not. epsdry > 0. ) then` / `call msgerr (1, 'minimal depth for drying/wetting should not be negative or zero')` / `epsdry = 5.e-5` / `else if ( epsdry > 0.01 ) then` / `call msgerr (1, 'minimal depth for drying/wetting should not be larger than 1 cm')` / `epsdry = 0.01` / `endif`; `src/SwashCheckPrep.ftn90:1219` `if ( inewt == 0 ) epshu = epsdry` | C 문서 누락 | DEPMIN이 비양수이면 5.e-5로 되돌린다. 0.01보다 크면 0.01로 제한한다. `if ( inewt == 0 ) epshu = epsdry`다. C는 기본값 자체가 아니라 입력 보정 범위와 EPSHU 연동에 한정한다. |
| inputs-physics-numerics:SI2-159 | beta 기본값 | swashuse PDF p.88: “Default: [beta] = 0.3” | `src/SwashReadInput.ftn90:917`: `call INREAL ( 'BETA' , psurf(2), 'STA',-1.)`; `src/SwashCheckPrep.ftn90:1076–1082`: `if ( pnums(6) == 3. .and. pnums(7) == -1. .and. psurf(2) == -1. ) then` / `!` / `psurf(2) = 0.15` / `!` / `else if ( psurf(2) == -1. ) then` / `!` / `psurf(2) = 0.3`; `src/SwashCheckPrep.ftn90:1072`: `if ( isurf == 1 ) then`; 같은 파일 1088–1091행은 미정 UMOM과 `beta=0.3`일 때 중앙차분을 선택한다. | C | BREAKING의 beta 생략값은 준비 단계에서 결정한다. 그 시점에 UMOM 수평 BDF가 이미 지정되어 있으면 0.15이다. 나머지 생략값은 0.3이다. SI2-164·241과 같은 조건부 기본값이다. |
| inputs-physics-numerics:SI2-164 | BREAKING·UMOM 결합 기본값 | swashuse PDF p.88에는 운동량 이류 스킴과 beta 기본값을 결합하는 절차가 없다. swashuse PDF p.96은 중앙차분 예외를 설명한다. | `src/SwashCheckPrep.ftn90:1088–1091`: `if ( .not. psurf(2) /= 0.3 .and. pnums(6) == -1. ) then` / `!` / `pnums(6) = 3.` / `pnums(7) = 1.` | C | `beta=0.3`이고 UMOM 수평 스킴이 미정이면 중앙차분을 선택한다. 사용자가 이미 정한 스킴을 무조건 덮어쓰지 않는다. |
| inputs-physics-numerics:SI2-165 | 이전 쇄파 모델의 비활성 분기 | swashuse PDF p.87–88은 두 번째 쇄파 모델 선택지를 제시하지 않는다. | `src/SwashReadInput.ftn90:911`: `!call ININTG ( 'ISURF', isurf, 'STA', 1 )`; `src/SwashReadInput.ftn90:912`: `isurf = 1`; `src/SwashReadInput.ftn90:923`: `else if ( isurf == 2 ) then` | C | `isurf==2` 계산 분기는 파일에 남아 있다. 제공된 파서는 isurf를 항상 1로 설정한다. 주석을 switch.pl로 활성화할 수 없다. 이 분기를 사용자 선택 옵션으로 쓰지 않는다. |
| outputs:SO1-187 | RUNUP 교점 정의 | swashuse PDF p.120: `computed by the intersection between free surface and bottom level.` | `src/SwashRunupHeight.ftn90:112` `if ( hs(nm) > delrp ) then`; `src/SwashRunupHeight.ftn90:134` `rh = s1(nmr) + ( delrp - hs(nmr) ) * ( s1(nmru) - s1(nmr) ) / ( hs(nmru) - hs(nmr) )`; swashuse PDF p.120: `A minimum water depth larger than zero is assumed.`와 `QUANTITY RUNUP delrp`. `src/SwashRunupHeight.ftn90:129`의 `if ( mr > mf .and. mr < mlu ) then` 안에서 134행 보간을 수행한다. | C 문서 누락 | RUNUP의 양의 최소 수심은 swashuse PDF p.120에 명시되어 있다. 누락은 총수심 delrp 위치에서 수면 높이를 선형 보간하는 구체식에 한정한다. 해당 셀 쌍을 찾지 못하면 138행의 예외값을 쓴다. |
| outputs:SO1-191 | HRUN에서 수직 처오름 높이 | swashuse PDF p.119: `with respect to the still water level`; `−1× BOTLEV indicates the runup height.` | `src/SwashElemOutp.ftn90:98` `if ( oqproc(5) ) voq(:,voqr(5)) = dps(:)`; `src/SwashQuanOutp.ftn90:2392` `call SWIPOL ( depf, ovexcv(5), xc, yc, mip, voq(1,voqr(5)), kgrpnt, oparr(1,1) )`; `8756667:src/SwashQuanOutp.ftn90:2108`부터 BOTLEV에 depf를 전달한다. 정수위 차감 경로의 삭제 이력이 아니다. | B 문서 오기 | −BOTLEV는 기준면에 대한 바닥 높이이다. 정수위에 대한 높이는 −BOTLEV−정수위이다. |
| outputs:SO1-257 | 침수·처오름 한계 수심 하한 | 문서는 사용자 값과 기본값만 적는다.; `src/SwashCheckPrep.ftn90:1195` `if ( hrunp /= -999. ) then`, `src/SwashCheckPrep.ftn90:1208` `if ( delrp /= -999. ) then`; `src/SwashCheckPrep.ftn90:1203·1216`의 미지정 기본값도 `epsdry`이다.; 7949227(2026-05-06, release v12.01) 뒤의 608ffd7·9554c98 diff는 이 행의 판정 대상 조건을 변경하지 않았다. [AD §3의 12.01 뒤 변경과 무관한 SO1 목록](../../../_staging/recovery/compare/SWASH-git-verify-AD.md). | `src/SwashCheckPrep.ftn90:1199–1200` `else if ( hrunp < epsdry ) then` / `hrunp = epsdry`; `src/SwashCheckPrep.ftn90:1212–1213` `else if ( delrp < epsdry ) then` / `delrp = epsdry` | C 문서 누락 | 미지정 표시값 -999는 기본값 epsdry로 바꾼다. 그 밖의 지정값이 epsdry보다 작으면 epsdry로 올린다. 그중 비양수 값에는 경고도 낸다. C는 이 하한 보정 방식에 한정한다. |
| outputs:SO1-266 | 여러 COMPUTE에서 HRUN 재초기화 | 문서는 whole simulation의 최대 침수를 설명한다.; 7949227(2026-05-06, release v12.01) 뒤의 608ffd7·9554c98 diff는 이 행의 판정 대상 조건을 변경하지 않았다. [AD §3의 12.01 뒤 변경과 무관한 SO1 목록](../../../_staging/recovery/compare/SWASH-git-verify-AD.md). | `src/SwashMain.ftn90:158` `call SwashCheckPrep`; `src/SwashCheckPrep.ftn90:3108` `hindun = 0.` | C 문서 누락 | 각 COMPUTE 준비 단계가 HRUN 기록을 지운다. 여러 COMPUTE 전체의 최대 침수 마스크로 해석하면 안 된다. |
| outputs:SO1-299 | 현재 노트의 HRUN 기록 구간 | models/SWASH/source-analysis/swash-wetting-drying-runup.md:168 ``전 격자: `hindun(nm) /= 1. .and. hs(nm) > hrunp` 이면 `hindun(nm) = 1.` (src/SwashUpdateDepths.ftn90:804-806). 즉 **수심이 runup threshold `hrunp`를 한 번이라도 넘으면 침수표시(1) 영구 기록** — maximum inundation 추적용 latch.`` | `src/SwashUpdateDepths.ftn90:805` `if ( hindun(nm) /= 1. .and. hs(nm) > hrunp ) hindun(nm) = 1.`; `src/SwashCheckPrep.ftn90:3108` `hindun = 0.`; 7949227(2026-05-06, release v12.01) 뒤의 608ffd7·9554c98 diff는 이 행의 판정 대상 조건을 변경하지 않았다. [AD §3의 12.01 뒤 변경과 무관한 SO1 목록](../../../_staging/recovery/compare/SWASH-git-verify-AD.md). | C 문서 누락 | HRUN 침수 기록은 한 COMPUTE 구간 안에서 유지된다. 다음 COMPUTE의 준비 단계는 hindun을 0으로 초기화한다. |
| theory-framework:ST1-238 | 면 보간과 Hodge의 구별 | swashtech PDF p.58: `a linear map within the dual mesh and thus should not be confused with Hodge star operators.`; `N_e\times N_c`; `The two tildes should not be confused with each other.`; `\widetilde{\tilde\eta^{(0)}}` | `src/SwashUpdateDepths.ftn90:201` `hum(nm) = 0.5 * ( hs(nm) + hs(nmu) )`; `src/SwashUpdateDepths.ftn90:212` `humn = 1.5*hum - 0.5*humo` | F 표기 차이 | 해석: `hum`은 같은 격자 안에서 두 수심을 산술평균한 면 수심이다. `humn`은 그 면 수심의 시간 외삽이다. 이들은 ST1-234의 유속 선적분과 면 적분을 바꾸는 Hodge 길이비와 다른 연산이다. 문서는 구체 공간 보간을 뒤 장으로 미룬다. |
| theory-framework:ST1-283 | 플럭스 수심의 중앙·상류 선택 | swashtech PDF p.58·61은 보존 조건으로 산술평균을 요구한다. 추가 선택 절차는 없다. swashuse PDF p.95는 1차 상류 수심과 고차 보정 `CORRDEP`를 설명한다. | `src/SwashInit.ftn90:395–396` `corrdep    = .true.`<br>`depcds     = .false.`; `src/SwashCheckPrep.ftn90:1370–1373` `if ( ( nint(pnums(11)) == 3 .and. pnums(12) == 1. ) .or. mimetic ) then`<br>`corrdep = .false.`<br>`depcds  = .true.`<br>`endif`; `src/SwashUpdDepu.ftn90:111–123` `if ( u(nm) > 1.0e-5 ) then`<br>`!`<br>`hu(nm) = s1(nm) + dpu(nm)`<br>`!`<br>`else if ( u(nm) < -1.0e-5 ) then`<br>`!`<br>`hu(nm) = s1(nmu) + dpu(nm)`<br>`!`<br>`else`<br>`!`<br>`hu(nm) = max( s1(nm), s1(nmu) ) + dpu(nm)`<br>`!`<br>`endif`; `src/SwashCheckPrep.ftn90:1368` `if ( corrdep ) then`; `src/SwashUpdDepu.ftn90:100` `if ( .not.depcds ) then`; `src/SwashUpdDepu.ftn90:138–141` `htot  = s1(nm ) + dps(nm )`<br>`htotu = s1(nmu) + dps(nmu)`<br>`!`<br>`hu(nm) = 0.5 * ( htot + htotu )`. | C 문서 누락 | C는 swashtech PDF p.58·61에 중앙·상류 선택 절차가 없다는 뜻이다. 사용자 설명서는 상류 수심과 CORRDEP를 설명한다. 준비 검사는 바깥 `corrdep` 조건 아래에서 중앙차분 또는 mimetic 조건을 만나면 `depcds`를 켠다. `SwashUpdDepu`의 비중앙 분기는 유속 부호에 따른 수심을 쓰고 중앙 분기는 산술평균을 쓴다. 산술평균을 가정한 보존 증명은 해당 경로에 한정한다. |
| theory-framework:ST1-284 | 수심 이력 저장과 면 수심 시간 외삽 | swashtech PDF p.58–59은 공간 보간을 설명한다. 이 시간 외삽식은 없다. | `src/SwashUpdateData.ftn90:248–249` `hso = hs`<br>`if ( kmax > 1    ) hkso = hks`; `src/SwashUpdateDepths.ftn90:192` `humo = hum`; `src/SwashUpdateDepths.ftn90:212` `humn = 1.5*hum - 0.5*humo` | C 문서 누락 | 갱신 경로는 전체 수심과 다층 두께의 이전 값을 저장한다. 이류의 질량 가중치에 쓰는 면 수심을 시간에서 외삽한다. 공간 산술평균과 구별한다. |
| theory-framework:ST1-289 | 음수 수심 보정·Newton 하한 | swashtech PDF p.19·63은 수심 정의만 제시한다. 보정 절차 없음. swashuse PDF p.100은 음수 수심을 막기 위한 `NEWTON` 선택을 설명한다. | `src/SwashUpdateDepths.ftn90:115` `if ( hs(nm) < 0. .and. inewt == 0 ) then`; `src/SwashUpdateDepths.ftn90:122–124` `s1(nm)  = 0.99*epsdry - dps(nm)`<br>`epsdry  = -1.01*hs(nm)`<br>`adapted = .true.`; `src/SwashUpdateDepths.ftn90:140` `if ( inewt /= 0 ) hs(nm) = max( epsdry, hs(nm) )`; 같은 파일 `src/SwashUpdateDepths.ftn90:117` `if ( hs(nm) < -epsdry ) then`; `src/SwashUpdateDepths.ftn90:126–128`의 반대 분기도 `s1(nm) = 0.99*epsdry - dps(nm)`을 대입한다. `src/SwashReadInput.ftn90:1878` `if ( KEYWIS ('NEWT') ) inewt = 1`. | C 문서 누락 | C는 기술문서 해당 쪽에 없는 구체 보정식이다. 비Newton의 두 음수 수심 분기는 모두 기존 `epsdry`로 수위를 보정한다. `hs(nm) < -epsdry`인 경우에만 건조 한계도 `-1.01*hs(nm)`으로 바꾸고 `adapted`를 켠다. Newton 경로는 `max( epsdry, hs(nm) )`를 적용한다. NEWTON 기능 자체는 사용자 설명서에 있다. |
| theory-unstructured:ST2-033 | (5.14) 산술 수심을 쓰는 질량 플럭스 | swashtech PDF p.74: `\phi_f^{(n-1)}=\upsilon_f^{(n-1)}\overline{\tilde\eta^{(0)}}_{\tilde e}`; swashuse PDF p.95: `An appropriate approximation is based on first order upwinding instead of the usual interpolation.`; p.96: `the water depth in velocity points is approximated with the MUSCL limiter.` | `src/SwashInit.ftn90:396` `depcds     = .false.`; `src/SwashUpdateUDepths.ftn90:221` `h = s1(icelll) + dpu(iface)`; `src/SwashUpdateUDepths.ftn90:225` `h = s1(icellr) + dpu(iface)`; `src/SwashReadInput.ftn90:1959` `if ( KEYWIS ('DISCRET') ) then`; `src/SwashReadInput.ftn90:1998–2000` `else if ( KEYWIS ('CORR') ) then`, `ieqn = 2`, `corrdep = .true.`; `src/SwashReadInput.ftn90:2024–2026` `if ( KEYWIS('NON') ) then`, `propsc = 3`, `kappa  = 1.`; `src/SwashReadInput.ftn90:2093–2094` `pnums(11) = real(propsc)`, `pnums(12) = kappa`; `src/SwashCheckPrep.ftn90:1368–1373`의 `if ( corrdep ) then`, `if ( ( nint(pnums(11)) == 3 .and. pnums(12) == 1. ) .or. mimetic ) then`, `corrdep = .false.`, `depcds  = .true.`; `src/SwashUpdateUDepths.ftn90:202` `if ( .not.depcds ) then`; `src/SwashUpdateUDepths.ftn90:219` `else if ( u(iface) > epsuf ) then`; `src/SwashUpdateUDepths.ftn90:223` `else if ( u(iface) < -epsuf ) then`; `src/SwashUpdateUDepths.ftn90:229` `h = max( s1(icelll), s1(icellr) ) + dpu(iface)`; `src/SwashUpdateUDepths.ftn90:243` `hu = hum`; `src/SwashUpdateUDepths.ftn90:324` `hu(iface) = hu(iface) + 0.5 * fluxlim(grad1,grad2)` | C 문서 누락 | 해석: 기본 경로는 유속 부호에 따른 상류 수위와 면 바닥 깊이로 면 수심을 만든다. 작은 유속에서는 양쪽 수위의 최댓값을 사용한다. 기본 MUSCL 보정도 더한다. `DISCRET CORRDEP NONE`은 `depcds`를 참으로 바꾸어 `hu = hum`을 선택한다. 이때 `hum`은 길이 가중 평균이므로 일반 삼각망에서 산술 평균과 같지는 않다. 상류법과 MUSCL은 swashuse PDF p.95–96에 있다. C는 swashtech §5.5.3의 산술 수심식과 이 구현 선택의 연결 설명 누락으로 한정한다. ST2-058·106·107도 같은 조건을 따른다. |
| theory-unstructured:ST2-058 | (5.29) 최종 질량 플럭스 | swashtech PDF p.80: `\phi_f^{(n-1)}=\upsilon_f^{(n-1)}\overline{\tilde\eta^{(0)}}_{\tilde e}=S_f\bar h_{\tilde e}u_f=S_f\bar h_fu_f`; swashuse PDF p.95: `An appropriate approximation is based on first order upwinding instead of the usual interpolation.`; p.96: `the water depth in velocity points is approximated with the MUSCL limiter.` | `src/SwashExpDepUflow.ftn90:1598` `qn(iface) = lf * hu(iface) * u1(iface)`; `src/SwashUpdateUDepths.ftn90:221` `h = s1(icelll) + dpu(iface)` | C 문서 누락 | 해석: 기본 `hu`는 상류 수위와 면 바닥 깊이에 MUSCL 보정을 더해 만든다. 저속 분기와 `DISCRET CORRDEP NONE`의 길이 가중 수심 분기는 ST2-033과 같다. 상류 수심과 고차 보정은 swashuse PDF p.95–96에 있다. C는 swashtech §5.6의 산술 평균 플럭스식과 실제 수심 선택의 연결 설명 누락이다. 면 플럭스의 단일값 조건은 유지한다. |
| theory-unstructured:ST2-149 | 모든 면의 조건이 수심 비음수를 보장한다는 주장 | swashtech PDF p.98: `guarantees a non-negative water depth in cell c if the following condition is satisfied for all cell faces f with outgoing mass flux [45]`; `\Delta tS_f\lvert u_f\rvert\le A_c`; swashuse PDF p.140: `ensuring non-negative water depths might lead to a time step restriction which appears to be more restrictive than the usual CFL condition.`; `An example is the case where locally all velocities are directed outward of a grid cell.` | `src/SwashExpDepUflow.ftn90:1600` `qf = qf + rsgn * qn(iface)`; `src/SwashExpDepUflow.ftn90:1610` `s1(icell) = s0(icell) - fh * dt * qf / area` | B 문서 오기 | 해석: swashtech PDF p.98의 면별 상한만으로는 여러 유출 면의 합을 제한하지 못한다. 같은 수심·유입 없음·두 유출 면에서 각각 `\Delta tS_f\lvert u_f\rvert=0.6A_c`이면 총 유출은 `1.2A_ch_c`다. 필요한 충분조건은 유출 플럭스 합의 상한이다. swashuse PDF p.140도 다차원 유출에서는 더 엄격한 시간 간격 조건이 필요할 수 있다고 설명한다. B는 tech p.98의 무조건적 보장 문장에 한정한다. |
| theory-unstructured:ST2-351 | 음수 셀 수심의 사후 보정 | swashtech PDF p.98과 swashuse PDF p.139–140은 비음수 수심 조건을 설명한다. 아래 사후 수위 보정과 epsdry 변경 절차는 적지 않는다. | `src/SwashUpdateUDepths.ftn90:115` `if ( hs(icell) < 0. .and. inewt == 0 ) then`; `src/SwashUpdateUDepths.ftn90:122–124` `s1(icell) = 0.99*epsdry - dps(icell)`, `epsdry  = -1.01*hs(icell)`, `adapted = .true.`; `src/SwashUpdateUDepths.ftn90:136` `if ( inewt /= 0 ) hs(icell) = max( epsdry, hs(icell) )`; `src/SwashUpdateUDepths.ftn90:151–154` `if ( epsdry > 0.01 ) then`, `!`, `call msgerr ( 4, 'INSTABLE: water level is too far below the bottom level!' )`, `call msgerr ( 0, '          Please reduce the time step!' )` | C 문서 누락 | `inewt=0` 경로는 음수 수심에서 수위를 바꾼다. 큰 음수 수심에서는 전역 마름 문턱도 바꾼다. 해석: 이 보정량을 제외한 경계 플럭스만으로 질량 수지를 평가하면 안 된다. |
| theory-unstructured:ST2-352 | 운동량 수심의 시간 외삽 | swashtech PDF p.75·97은 공간 가중 수심을 정의한다. swashuse PDF p.99는 시간 적분을 설명한다. 아래 운동량 분모의 시간 외삽식은 적지 않는다. | `src/SwashUpdateUDepths.ftn90:167` `humo = hum`; `src/SwashUpdateUDepths.ftn90:196` `! extrapolate water depth at midface in time to improve accuracy of momentum-conservative time integration`; `src/SwashUpdateUDepths.ftn90:198` `humn = 1.5*hum - 0.5*humo`; `src/SwashExpDepUflow.ftn90:1038` `contrib = advec(iface) / humn(iface) + ( zgrad + pgrad(iface) + qgrad(iface) - windu(iface) - visc(iface) + corf(iface) ) / hum(iface)` | C 문서 누락 | 이류의 분모는 외삽 수심이다. 다른 명시적 힘의 분모는 현재 가중 수심이다. 두 분모를 같은 배열로 쓰지 않는다. |
| theory-unstructured:ST2-353 | 미소 유속·중심 수심 선택 | swashtech PDF p.98의 상류식은 양·음 유속을 구별한다. swashuse PDF p.94–97은 CORRDEP와 NONE·제한자 선택을 설명한다. | `src/SwashInit.ftn90:396` `depcds     = .false.`; `src/SwashUpdateUDepths.ftn90:219` `else if ( u(iface) > epsuf ) then`; `src/SwashUpdateUDepths.ftn90:223` `else if ( u(iface) < -epsuf ) then`; `src/SwashUpdateUDepths.ftn90:229` `h = max( s1(icelll), s1(icellr) ) + dpu(iface)`; `src/SwashUpdateUDepths.ftn90:243` `hu = hum`; `src/SwashReadInput.ftn90:1998–2000,2024–2026,2092–2094`의 CORRDEP·NONE 선택은 pnums(11)을 3, pnums(12)를 1로 설정한다. `src/SwashCheckPrep.ftn90:1368–1374`는 `if ( ( nint(pnums(11)) == 3 .and. pnums(12) == 1. ) .or. mimetic ) then`에서 `corrdep = .false.`와 `depcds  = .true.`를 설정한다. | C 문서 누락 | 상류 수심 경로의 내부면에서 미소 유속이면 큰 쪽 수위를 사용한다. 경계면은 `src/SwashUpdateUDepths.ftn90:211–217`의 별도 분기다. CORRDEP NONE 또는 mimetic 준비 조건으로 depcds가 참이면 `hu = hum`을 사용한다. C는 이 미소 유속 처리와 길이 가중 수심의 실제 선택 조건에 한정한다. |
| theory-unstructured:ST2-354 | 질량 플럭스 수심의 고차 보정 | swashuse PDF p.95–97·140은 CORRDEP 고차 보정과 기본 MUSCL 제한자를 설명한다. swashtech PDF p.98은 1차 상류 수심만 적는다. | `src/SwashInit.ftn90:395` `corrdep    = .true.`; `src/SwashInit.ftn90:411–413` `pnums(11) = 6.`, `pnums(12) = 0.`, `pnums(13) = 2.`; `src/SwashUpdateUDepths.ftn90:252–255` `propsc = nint(pnums(11))`, `kappa  = pnums(12)`, `mbound = pnums(13)`, `phieby = pnums(14)`; `src/SwashUpdateUDepths.ftn90:315` `if ( s1min + depmin < 0. ) cycle floop`; `src/SwashUpdateUDepths.ftn90:324` `hu(iface) = hu(iface) + 0.5 * fluxlim(grad1,grad2)`; `src/SwashUpdateUDepths.ftn90:377` `hu(iface) = hu(iface) + 0.5 * fluxlim(grad1,grad2)` | C 문서 누락 | 기본 코드는 상류 셀의 반대 꼭짓점에 모인 셀 값을 면적으로 평균한다. 코드는 그 평균으로 만든 경사에 제한자를 적용한다. 국소 최소 수위와 바닥 깊이의 합이 음수이면 보정을 생략한다. C는 비구조 상류 꼭짓점의 면적 가중 stencil과 음수 국소 수심에서의 보정 생략에 한정한다. CORRDEP 선택과 준비 조건은 ST2-353과 같다. |
| theory-unstructured:ST2-381 | 젖은 면·셀의 표지 | swashuse PDF p.33·140은 마름 문턱과 마른 영역의 속도 처리를 설명한다. swashtech PDF p.98 및 사용설명서의 해당 설명에는 젖은 면에서 셀 표지를 집계하는 식이 없다. | `src/SwashUDryWet.ftn90:84–90` `if ( hu(iface) > epshu ) then`, `!`, `wetu(iface) = 1`, `!`, `else`, `!`, `wetu(iface) = 0`; `src/SwashUDryWet.ftn90:108` `ival = ival * ( 1 - wetu(iface) )`; `src/SwashUDryWet.ftn90:112–118` `if ( ival == 0 ) then`, `!`, `wets(icell) = 1`, `!`, `else`, `!`, `wets(icell) = 0` | C 문서 누락 | 코드는 면 수심이 문턱보다 클 때 면을 젖음으로 표시한다. 셀에 젖은 면이 하나라도 있으면 셀을 젖음으로 표시한다. 여기서 면 판정 문턱은 epshu다. 셀 수심 보정의 epsdry와 구별한다. |

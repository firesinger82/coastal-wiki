---
title: "ADCIRC 경계조건 — IBTYPE 카탈로그(elevation/land no-flow/island/specified flux/radiation/internal barrier±pipes/weir 64) + normal flux BC + sponge(absorbing) layer"
topic: adcirc
canonical_source: self
citation_status: verified
last_source_check: 2026-10-11 (recovery 재판독 대조)
has_source_needed: false
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/boundaries.F (675) + normal_flow_boundary.F90 (106) + sponge_layer.F90 (880) 직접 read — IBTYPE 분류(specifiedFluxBoundaryTypes=(2,12,22,32,52):179, flux 3/13/23·4/24/64·5/25, weir 64), sponge SSIGMA_ETA/MNX/MNY + momentum SPNGCOEF(momentum.F VCOEFXX) file:line 인용. Luettich-Westerink ADCIRC."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — IBTYPE 카탈로그·flux BC·sponge 메커니즘 verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
  - models/ADCIRC/source-analysis/adcirc-tidal-forcing.md
  - models/ADCIRC/source-analysis/adcirc-fort-files-reference.md
---

# ADCIRC 경계조건 — IBTYPE / flux / sponge

> `boundaries.F`(675) + `normal_flow_boundary.F90`(106) + `sponge_layer.F90`(880) 직접 read. ADCIRC fort.14 의 **경계 세그먼트 타입(IBTYPE)** 시스템 + normal flux 적용 + **흡수(sponge) 경계**. open(elevation) 조석 BC 는 [[adcirc-tidal-forcing]] 의 body-force 와 별개의 경계 forcing. fort.15 측 NFFR 레코드 구조·QN 합성·gwce.F IBTYPE=32 radiation 이산식·부호 규약(내향 양)은 [[adcirc-nffr-periodic-flux-boundary]] (2026-07-12 신설).

## 1. 두 경계 부류 (boundaries.F)

- **Elevation(open) boundaries** `IBTYPEE`: 조위 지정(fort.15 tidal constituent 또는 fort.19 시계열). `p_nope`/`p_neta` 세그먼트·node 수.
- **Flux/land boundaries** `IBTYPE`: 육지·섬·flux·barrier. `nvell(k)` = 세그먼트별 node 수.

## 2. IBTYPE 카탈로그 (boundaries.F:100-179) ★

| IBTYPE | 종류 | 처리 |
|---|---|---|
| **0 / 10 / 20** | mainland (no normal flow) | 0 free-slip / 10 no-slip / 20 ... tangential 차이 |
| **1 / 11 / 21** | island (no normal flow, 폐곡선) | 〃 |
| **2 / 12 / 22** | **specified normal flux** (+tangential) | `specifiedFluxBoundaryTypes=(2,12,22,32,52)` (:179), fort.15/fort.20 |
| **3 / 13 / 23** | **외부 장벽** | ASCII reader는 `BARLANHT·BARLANCFSP`를 읽는다 (`src/mesh.F:460` `case(3,13,23)`; `src/mesh.F:463` `read(unit=iunit,fmt=*,err=10,end=20,iostat=ios)`; `src/mesh.F:465` `&              externalFluxBoundaries(efCount)%barlanht(j),`; `src/mesh.F:466` `&              externalFluxBoundaries(efCount)%barlancfsp(j)`). |
| **30** | radiation (Flather-type) | 유출 radiation |
| **4 / 24** | **internal barrier**(levee, 단방향 overflow) | weir overflow 식, paired node(`ibconnr` dual) |
| **5 / 25** | internal barrier + **cross pipes**(culvert) | 4/24 + flowthrough pipe |
| **64** | **vertical element wall**(submerged weir, SB) | `ISSUBMERGED64`, 양면 flux |
| **52 / 102 / 112 / 122 / 152** | river / special | mesh reader는 `102·112·122·152`를 경압 river 경계로 분류한다 (`src/mesh.F:1405` `case(102,112,122,152)`; `src/mesh.F:1406` `bndBCRiver=.true.`). `simpleFluxBoundaries` 할당 분기는 `102·112`를 포함하지 않는다 (`src/boundaries.F:353` `case(0,1,2,10,11,12,20,21,22,30,32,52,94,122)`; `src/boundaries.F:354` `allocate(simpleFluxBoundaries(sfCount)%nodes(nvell(i)))`). 확인하지 않음: 읽기 분기만으로 `102·112`의 실행 지원을 확정하지 않았다. |

- v56.2.1의 ASCII fort.14 reader는 `NVDLL` 레코드의 `IBTYPEE`를 읽지 않는다 (`src/mesh.F:418` `read(unit=iunit,fmt=*,err=10,end=20,iostat=ios) nvdll(k)`). 문서는 같은 레코드에 `IBTYPEE`를 적는다 (`docs/technical_reference/input_files/fort14.rst:26` `` :ref:`NVDLL(k) <NVDLL>`, :ref:`IBTYPEE(k) <IBTYPEE>` ``).
- 장벽 높이 검사는 높이가 지형고보다 작을 때 종료한다 (`src/mesh.F:2608` `IF(BARLANHT(JGW).LT.-DP(NBV(JGW))) THEN`; `src/mesh.F:2627` `IF(BARINHT(JGW).LT.-DP(NBV(JGW))) THEN`; `src/mesh.F:2646` `IF(BARINHT(JGW).LT.-DP(NBV(JGW))) THEN`). 내부 장벽의 이 검사는 앞면 `NBV`만 비교한다 (`src/mesh.F:2627` `IF(BARINHT(JGW).LT.-DP(NBV(JGW))) THEN`). 문서는 앞면과 뒷면 양쪽의 지형고 조건을 요구한다 (`docs/technical_reference/parameter_definitions/index.rst:28` `Internal barrier height (positive above the geoid and negative below the geoid) at node NBVV(k,j) and the paired node IBCONN(k,j)). The barrier height must be greater than the bathymetric depth at these nodes, i.e., recalling the different sign convention between the bathymetric depth and the barrier height, BARINHT(k,j) > –DP(NBVV(k,j) and <b >BARINHT(k,j) > –DP(IBCONN(k,j)). If this is not satisfied, the run will terminate.`).
- 모델 reader는 `IBTYPE=4·24·64`의 뒷면 라벨을 dict로 매핑한다 (`src/mesh.F:490` `internalFluxBoundaries(ifCount)%ibconn(j) =`; `src/mesh.F:491` `&             find(node_dict, n2)`). prep의 같은 분기는 뒷면 입력 정수를 그대로 저장한다 (`prep/read_global.F:237` `case(4,24,64)`; `prep/read_global.F:239` `READ(14,*) n1,IBCONNR(K,I),`; `prep/read_global.F:245` `WEIRD(NWEIR) = IBCONNR(K,I)`). 해석: 비연속 라벨의 뒷면 처리가 모델 reader와 다르다 (`src/mesh.F:491` `&             find(node_dict, n2)`; `prep/read_global.F:239` `READ(14,*) n1,IBCONNR(K,I),`). 확인하지 않음: 이 차이의 모델 실행 결과.
- fort.39 reader는 river 경계와 `IDEN=2·3·4`를 요구한다 (`src/cstart.F:961` `IF (BndBCRiver .AND. (IDEN.EQ.2 .OR. IDEN.EQ.3 .OR.`; `src/cstart.F:962` `&    IDEN.EQ.4)) THEN`; `src/cstart.F:963` `OPEN(39,FILE=TRIM(INPUTDIR)//'/'//'fort.39',`). reader는 `RIVBCSTATIM`에 `86400.d0`을 곱한다 (`src/cstart.F:965` `READ(39,*) RIVBCTIMINC, RIVBCSTATIM`; `src/cstart.F:966` `RIVBCTIME1=RIVBCSTATIM*86400.d0`). 해석: 이 입력 시작 시각의 단위는 일이다 (`src/cstart.F:966` `RIVBCTIME1=RIVBCSTATIM*86400.d0`). 문서는 시작 시각을 초로 적는다 (`docs/technical_reference/input_files/fort39.rst:25` `- RIVBCSTATIM is the time (in seconds) when the boundary condition data start, relative to the cold start time`).

- `+100` 변형(102/112/122) = baroclinic river 등 특수. weir(barrier) node 는 paired(`weir`/`weird` dual node, :611-614) — 양쪽 수위차로 overflow.
- `CSII/SIII` = flux 경계 node 의 법선 cos/sin(접선/법선 분해).

## 3. Normal flux BC (normal_flow_boundary.F90, 106)

specified-flux 경계(IBTYPE 2/12/22/32/52)에서 **법선 flux `QN2`** 를 essential 하게 부과. `VelNorm = -QN2/H`(법선 유속). fort.20(시계열) 또는 fort.15 의 flux per unit width.

## 4. Sponge (absorbing) layer (sponge_layer.F90, 880) ★

외향파를 흡수해 **경계 반사 방지**(DW 구현). damping 계수:
- `SSIGMA_ETA`(absorblayer_sigma_eta) = 수위 감쇠 σ / `SSIGMA_MNX`·`SSIGMA_MNY` = 운동량 x/y 감쇠 σ.
- 경계에서 내부로 갈수록 σ 감소(layer 두께). FEM 으로 `∫σφᵢφⱼ dx` 정확 적분(:70).
- **momentum 결합**: [[adcirc-momentum-implementation]] §3 `VCOEFXX = DTO2*(TKM + SPNGCOEF_X)` — sponge 계수가 friction 처럼 운동량 감쇠 항에 추가(`SPNGCOEF_X/Y`). wind 도 sponge 내 무효(momentum.F:740 `absorblayer_sigma_mnx>1e-9 → WSX=0`).
- 용도: 대양 open boundary 에서 outgoing tide/surge 흡수(유한영역 반사 spurious 제거), tsunami·storm-surge radiation.

## 5. 정리

| 경계 | forcing/처리 | 입력 |
|---|---|---|
| elevation(open) | 조위 지정 | fort.15 tidal / fort.19 |
| specified flux | 법선 flux QN2 | fort.15 / fort.20 |
| radiation(3/30) | 외향 유출 | — |
| land/island(0/1) | no normal flow | fort.14 |
| barrier(4/5/24/64) | weir overflow + pipe | fort.14 barrier height |
| sponge | 흡수 damping | fort.13/15 absorbing layer |

## 6. 연결

- [[adcirc-momentum-implementation]] — sponge SPNGCOEF → VCOEFXX 운동량 감쇠 + wind 무효
- [[adcirc-tidal-forcing]] — elevation open-BC 조석 forcing(body-force 와 구분)
- [[adcirc-fort-files-reference]] — fort.14 boundary segment / fort.15 NOPE·NBOU / fort.19·20 시계열
- Luettich & Westerink ADCIRC users manual (IBTYPE 정의)

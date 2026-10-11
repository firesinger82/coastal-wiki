---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/14-fort14-grid-bathymetry-boundaries.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
last_source_check: 2026-10-11 (recovery 재판독 대조)
---
# Fort.14 Grid, Bathymetry, And Boundaries

## Metadata

- date: 2026-04-12
- title: fort.14 as the combined mesh, bathymetry, and boundary artifact
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/technical_reference/input_files/fort14.html

## Why This Matters

This is the key source for understanding why preprocessing is the first bottleneck.

## Core Claims

- `fort.14` is required
- it contains nodal data, element data, open-boundary data, and flow-boundary data

| 항목 | 문서·코드 대조 | 출처와 원문 |
|---|---|---|
| F14-12 IBTYPEE | ASCII 읽기문은 NVDLL만 읽는다. 코드는 같은 레코드의 IBTYPEE를 읽거나 검사하지 않는다. XDMF 경계 형식과 ASCII 형식을 구분해야 한다. | `[file=docs/technical_reference/input_files/fort14.rst line=26]` `` :ref:`NVDLL(k) <NVDLL>`, :ref:`IBTYPEE(k) <IBTYPEE>` ``<br>`[file=docs/technical_reference/parameter_definitions/index.rst line=118]` ` Elevation boundary type, (At present the only allowable value for IBTYPEE is 0). Elevations are specified either in the Model Parameter and Periodic Boundary Condition File for harmonic forcing or in the Non-periodic Elevation Boundary Condition File for time series forcing. `<br>`[file=src/mesh.F line=418]` ` read(unit=iunit,fmt=*,err=10,end=20,iostat=ios) nvdll(k) ` |
| F14-22 외부 장벽 NBVV, BARLANHT, BARLANCFSP: 3,13,23 | 코드는 노드 라벨, 기준면 위로 양수인 장벽 높이, 초임계 유량 계수를 읽는다. 코드는 높이를 읽을 때 단위를 변환하지 않는다. | `[file=docs/technical_reference/input_files/fort14.rst line=37]` `` :ref:`NBVV(k,j) <NBVV>`, :ref:`BARLANHT(k,j) <BARLANHT>`, :ref:`BARLANCFSP(k,j) <BARLANCFSP>`      if IBTYPE(k) = 3, 13, 23 ``<br>`[file=docs/technical_reference/parameter_definitions/index.rst line=33]` ` Coefficient of free surface supercritical flow at external barrier node NBVV(k,j). A typical value is BARLANCFSP(k,j)= 1.0. `<br>`[file=docs/technical_reference/parameter_definitions/index.rst line=38]` ` External barrier height (positive above the geoid and negative below the geoid) at node NBVV(k,j). The barrier height must be greater than the bathymetric depth at this node, i.e., recalling the different sign convention between the bathymetric depth and the barrier height, BARLANHT(k,j) > –DP(NBVV(k,j). If this is not satisfied, the run will terminate. `<br>`[file=src/mesh.F line=460]` ` case(3,13,23) `<br>`[file=src/mesh.F line=463]` ` read(unit=iunit,fmt=*,err=10,end=20,iostat=ios) `<br>`[file=src/mesh.F line=464]` ` &              n1, `<br>`[file=src/mesh.F line=465]` ` &              externalFluxBoundaries(efCount)%barlanht(j), `<br>`[file=src/mesh.F line=466]` ` &              externalFluxBoundaries(efCount)%barlancfsp(j) ` |
| F14-28 장벽 높이의 허용 등호 | 문서는 높이가 지형고보다 반드시 커야 한다고 적는다. 코드는 높이가 지형고보다 작은 경우에만 종료한다. 코드는 두 값이 같은 경우를 허용한다. | `[file=docs/technical_reference/parameter_definitions/index.rst line=38]` ` External barrier height (positive above the geoid and negative below the geoid) at node NBVV(k,j). The barrier height must be greater than the bathymetric depth at this node, i.e., recalling the different sign convention between the bathymetric depth and the barrier height, BARLANHT(k,j) > –DP(NBVV(k,j). If this is not satisfied, the run will terminate. `<br>`[file=docs/technical_reference/parameter_definitions/index.rst line=28]` ` Internal barrier height (positive above the geoid and negative below the geoid) at node NBVV(k,j) and the paired node IBCONN(k,j)). The barrier height must be greater than the bathymetric depth at these nodes, i.e., recalling the different sign convention between the bathymetric depth and the barrier height, BARINHT(k,j) > –DP(NBVV(k,j) and <b >BARINHT(k,j) > –DP(IBCONN(k,j)). If this is not satisfied, the run will terminate. `<br>`[file=src/mesh.F line=2608]` ` IF(BARLANHT(JGW).LT.-DP(NBV(JGW))) THEN `<br>`[file=src/mesh.F line=2627]` ` IF(BARINHT(JGW).LT.-DP(NBV(JGW))) THEN `<br>`[file=src/mesh.F line=2646]` ` IF(BARINHT(JGW).LT.-DP(NBV(JGW))) THEN ` |
| F14-29 내부 장벽 뒷면의 지형고 검사 | 문서는 NBVV와 IBCONN 양쪽의 조건을 요구한다. 이 검사는 NBV 쪽만 비교한다. 해석: 입력 시점에 뒷면 지형고 조건을 독립적으로 보장하지 않는다. | `[file=docs/technical_reference/parameter_definitions/index.rst line=28]` ` Internal barrier height (positive above the geoid and negative below the geoid) at node NBVV(k,j) and the paired node IBCONN(k,j)). The barrier height must be greater than the bathymetric depth at these nodes, i.e., recalling the different sign convention between the bathymetric depth and the barrier height, BARINHT(k,j) > –DP(NBVV(k,j) and <b >BARINHT(k,j) > –DP(IBCONN(k,j)). If this is not satisfied, the run will terminate. `<br>`[file=src/mesh.F line=2627]` ` IF(BARINHT(JGW).LT.-DP(NBV(JGW))) THEN `<br>`[file=src/mesh.F line=2640]` ` CALL terminate(exit_code=ADCIRC_EXIT_FAILURE, message=exeTerm9973) ` |
| F14-30 IBTYPE=102·112·122: 읽기와 할당의 차이 | mesh 읽기 분기는 102·112·122를 갖는다. simpleFluxBoundaries 할당 분기는 이 셋 중 122만 갖는다. 해석: 102·112 지원을 읽기 분기만으로 확정하면 안 된다. 모델을 실행하지 않았다. | `[file=docs/technical_reference/parameter_definitions/index.rst line=113]` ` = 102, 112, or 122 flux specified baroclinic. In order to designate a river boundary as baroclinic, 100 should be added to the IBTYPE that would be appropriate in the barotropic case. For example, to convert a barotropic river boundary (IBTYPE of 22) to a baroclinic river boundary with freshwater inflow, change the IBTYPE to 122. If there is a 1 in the 100s place of the IBTYPE, ADCIRC will then try to read an input file (fort.39) for the salinity and/or temperature boundary condition. The format of the fort.39 file depends on the value of IDEN; see the documentation of the fort.39 file for more details. `<br>`[file=src/mesh.F line=446]` ` case(0,1,2,10,11,12,20,21,22,30,32,52,102,112,122,152) `<br>`[file=src/mesh.F line=1405]` ` case(102,112,122,152) `<br>`[file=src/boundaries.F line=353]` ` case(0,1,2,10,11,12,20,21,22,30,32,52,94,122) `<br>`[file=src/boundaries.F line=354]` ` allocate(simpleFluxBoundaries(sfCount)%nodes(nvell(i))) ` |
| F14-31 prep의 IBTYPE=40·41 노드 레코드 | prep reader에는 40·41의 단일 노드 레코드 읽기가 있다. 모델 mesh.F reader에는 두 case가 없다. F14-21은 모델 reader의 판정이다. 해석: 전처리 입력 수용을 모델 실행 지원으로 바꾸지 않는다. | `[file=docs/technical_reference/parameter_definitions/index.rst line=105]` ` = 40 a zero normal velocity gradient boundary. The GWCE is forced with normal flux, the momentum eqs are sacrificed in favor of setting the velocity at a boundary node equal to the value at a fictitious point inside the domain. The fictitious point lies on the inward directed normal to the boundary a distance equal to the distance from the boundary node to its farthest 'neighbor. This should ensure that the fictitious point does not fall into an element that contains the boundary node. The velocity at the fictitious point is determined by interpolation. `<br>`[file=docs/technical_reference/parameter_definitions/index.rst line=107]` ` = 41 a zero normal velocity gradient boundary. The GWCE is forced with normal flux. The momentum eqs are sacrificed in favor of eqs that set the velocity gradient normal to the boundary equal to zero in the Galerkin sense. `<br>`[file=prep/read_global.F line=224]` ` select case(ITYPE) `<br>`[file=prep/read_global.F line=225]` ` case(0,10,20,30,40,1,11,21,41) `<br>`[file=prep/read_global.F line=227]` ` READ(14,*) n1 `<br>`[file=prep/read_global.F line=228]` ` NBVV(K,I) = find(node_dict,n1) ` |
| F14-32 IBTYPE=4·24·64의 IBCONN 라벨 처리 | 모델 reader는 앞면과 뒷면의 노드 라벨을 dict로 매핑한다. prep의 4·24·64 분기는 뒷면 IBCONNR에 입력 정수를 그대로 저장한다. prep의 5·25 분기는 뒷면도 dict로 매핑한다. 해석: 비연속 라벨에서 4·24·64의 뒷면 해석이 모델 reader와 다르다. 실행 결과는 확인하지 않음. | `[file=docs/technical_reference/parameter_definitions/index.rst line=63]` ` Back face node paired with the front face node, NBVV(k,j), on an internal barrier boundary `<br>`[file=docs/technical_reference/input_files/fort14.rst line=38]` `` :ref:`NBVV(k,j) <NBVV>`, :ref:`IBCONN(k,j) <IBCONN>`, :ref:`BARINHT(k,j) <BARINHT>`, :ref:`BARINCFSB(k,j) <BARINCFSB>`, :ref:`BARINCFSP(k,j) <BARINCFSP>`      if IBTYPE(k) = 4, 24, 64 ``<br>`[file=src/mesh.F line=483]` ` &                      n1, `<br>`[file=src/mesh.F line=484]` ` &                      n2, `<br>`[file=src/mesh.F line=490]` ` internalFluxBoundaries(ifCount)%ibconn(j) = `<br>`[file=src/mesh.F line=491]` ` &             find(node_dict, n2) `<br>`[file=prep/read_global.F line=237]` ` case(4,24,64) `<br>`[file=prep/read_global.F line=239]` ` READ(14,*) n1,IBCONNR(K,I), `<br>`[file=prep/read_global.F line=240]` ` &                    BAR1(K,I),BAR2(K,I),BAR3(K,I) `<br>`[file=prep/read_global.F line=241]` ` NBVV(K,I) = find(node_dict,n1) `<br>`[file=prep/read_global.F line=245]` ` WEIRD(NWEIR) = IBCONNR(K,I) `<br>`[file=prep/read_global.F line=249]` ` READ(14,*) n1,n2, `<br>`[file=prep/read_global.F line=253]` ` IBCONNR(K,I) = find(node_dict,n2) ` |

- it also contains the bathymetric data used by ADCIRC
- therefore mesh generation, bathymetry assignment, and boundary construction are not separable in the final ADCIRC artifact

## Practical Value

- method details: defines the actual object preprocessing must produce
- implementation detail: prevents treating mesh, bathymetry, and boundaries as independent late-stage edits
- validation detail: explains why many setup failures should be debugged at the `fort.14` level first
- limitations: does not tell us which meshing tool or bathymetry source is best

## Relevance Tags

- solver: ADCIRC
- physics: preprocessing
- numerics: mesh construction
- diagnostics: boundary and depth integrity
- failure mode: malformed mesh or boundary encoding

## Transferability

Universal for all ADCIRC projects.

## Extraction Targets

- define the preprocessing object model around `fort.14`
- link bathymetry and boundary work directly to mesh-generation choices

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet

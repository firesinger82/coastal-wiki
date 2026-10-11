---
title: "adcirc bathymetry input foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC 공식 문서(fort.14/fort.13/fort.141 의미·NWS·전처리 도구) 기반. modeling-wiki 마이그레이션(2026-05-23). (2026-06-18 canonical 정화: 개인 로컬 경로·grid 유틸리티 증거 제거, 공개 도구·소스명만 유지.)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 마이그레이션 2026-05-23 → 2026-06-18 정화"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-11 (recovery 재판독 대조)
---

# ADCIRC Bathymetry Input Foundation

Date: 2026-04-12

Purpose:
- organize how bathymetry and topography enter ADCIRC
- distinguish base-mesh depth construction from advanced terrain options

## Core Official Fact

The official docs define `fort.14` as the file that contains:
- the finite element grid
- bathymetric data
- boundary information

That means bathymetry is not a side input.
It is part of the core mesh artifact.

## First Principle

Before discussing parameter tuning, you need a coherent answer to:
- what terrain sources define the bed and land elevations?
- what datum are they in?
- how are they transferred into `DP` at each node in `fort.14`?

If this is unstable, later stability or validation work is built on weak ground.

## Bathymetry Input Layers

### 1. Base Bathymetry In The Mesh

This is the default layer:
- node coordinates and `DP` values are stored in `fort.14`
- initial water depths are derived from the bathymetric depth in `fort.14`

This is the foundation for almost all standard ADCIRC runs.

### 2. Nodal Attributes

Bathymetry-adjacent behavior can also be influenced by nodal attributes in `fort.13`.
Examples include:
- Manning's n
- sea-surface-height related attributes
- initially dry behavior or roughness-related fields

These are not replacements for the base bed elevation, but they often interact with how the terrain behaves dynamically.

### 3. Time-Varying Bathymetry

ADCIRC also supports `fort.141` for time-varying bathymetry.

| 항목 | 문서·코드 대조 | 출처와 원문 |
|---|---|---|
| BATH-01 NDDT 설정 위치·사용 조건 | rst는 fort.14의 NDDT를 적는다. 코드는 fort.15의 TimeBathyControl namelist에서 NDDT를 읽는다. 0·±1·±2를 허용한다. | `[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=6]` ``` The ADCIRC Time Varying Bathymetry Input File (``fort.141``) is used by ADCIRC whenever the :ref:`NDDT <NDDT>` value in the ``fort.14`` is nonzero. There are two variations of this file, depending on the value of :ref:`NDDT <NDDT>`. ```<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=43]` `` - This file is only required when :ref:`NDDT <NDDT>` is nonzero ``<br>`[file=src/read_input.F line=323]` ` NAMELIST /timebathycontrol/ NDDT,BTIMINC,BCHGTIMINC `<br>`[file=src/read_input.F line=422]` ` READ(UNIT = 15,NML = TimeBathyControl,IOSTAT = IOS_NDDT, IOMSG=ios_nml_error_msg) `<br>`[file=src/read_input.F line=2380]` ` IF ( (ABS(NDDT).NE.0).AND.(abs(NDDT).NE.1) `<br>`[file=src/read_input.F line=2381]` ` &                     .AND.(abs(NDDT).NE.2) ) THEN `<br>`[file=src/cstart.F line=122]` ` IF (NDDT.NE.0) then `<br>`[file=src/cstart.F line=134]` ` CALL openFileForRead(141,TRIM(INPUTDIR)//'/'//'fort.141',IOS) ` |
| BATH-02 NDDT=±1: j·depth, NP개 레코드 | 코드는 NP개 레코드를 읽는다. IJK를 직접 배열 인덱스로 쓴다. 노드 라벨 사전을 사용하지 않는다. 수심의 부호와 단위는 fort.14 DP를 따른다. | `[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=11]` `` If :ref:`NDDT <NDDT>` is +/-1, then each bathymetry dataset in the file covers the full domain, and the file format is as follows: ``<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=17]` ` j, depth(j) `<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=24]` ``` - depth(j) has the same meaning as DP in the mesh file (``fort.14``) ```<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=45]` ` - Each dataset must cover all nodes in the domain `<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=46]` ` - The number of records per dataset is fixed (equal to NP) `<br>`[file=src/cstart.F line=125]` ` DP1(:) = DP(:)  !set dp1 to initial depth from fort.14 grid `<br>`[file=src/cstart.F line=126]` ` DP2(:) = DP(:)  !set dp2 to the same values `<br>`[file=src/cstart.F line=148]` ` IF (ABS(NDDT).EQ.1) THEN `<br>`[file=src/cstart.F line=149]` ` DO I=1,NP `<br>`[file=src/cstart.F line=150]` ` READ(141,*) IJK,DP2(IJK) ` |
| BATH-03 NDDT=±2: # 구분자 | 코드는 둘째 열의 #로 데이터셋을 나눈다. 첫째 열 #만으로 구분하지 않는다. | `[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=29]` ``` If :ref:`NDDT <NDDT>` is +/-2, then each dataset in the ``fort.141`` file covers only part of the domain, and the file format is as follows: ```<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=34]` ` "#" `<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=36]` ` j, depth(j) `<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=48]` ` - Each dataset can cover a different subset of nodes `<br>`[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=49]` ` - The separation between datasets is achieved by placing a hash mark ("#") in the second column of a line `<br>`[file=src/globalio.F line=1676]` ` READ(lun,'(A80)') CDUM80 `<br>`[file=src/globalio.F line=1677]` ` IF(CDUM80(2:2).NE.'#') EXIT `<br>`[file=src/globalio.F line=1682]` ` READ(lun,'(A80)',end=172) CDUM80 `<br>`[file=src/globalio.F line=1683]` ` IF(CDUM80(2:2).EQ.'#') EXIT ` |
| BATH-04 NDDT=±2: 고정 형식·-99999 sentinel | 코드는 (I8,E13.5)로 읽는다. 값이 -99999.d0이면 기존 값을 유지한다. 문서 형식은 이 sentinel과 열 폭을 적지 않는다. | `[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=36]` ` j, depth(j) `<br>`[file=src/cstart.F line=156]` ` CALL NDDT2GET(141,DP2(:),-99999.d0) `<br>`[file=src/globalio.F line=1680]` ` READ(CDUM80,'(I8,E13.5)') IJK,tmpval `<br>`[file=src/globalio.F line=1681]` ` if (tmpval.ne.defval) RVAL(IJK) = tmpval  !this allows us to exclude values included for record separation purposes in the parallel version ` |
| BATH-05 시작 프레임·생략 노드 유지·부호별 시간 | 코드는 첫 프레임을 fort.14 수심으로 채운다. 양수 NDDT는 STATIM+BTIMINC를 첫 입력 시각으로 설명한다. 음수 NDDT는 hot start 시각을 기준으로 설명한다. 생략 노드는 현재 수심을 유지한다. | `[file=docs/technical_reference/input_files/time_varying_bathymetry.rst line=48]` ` - Each dataset can cover a different subset of nodes `<br>`[file=src/cstart.F line=125]` ` DP1(:) = DP(:)  !set dp1 to initial depth from fort.14 grid `<br>`[file=src/cstart.F line=126]` ` DP2(:) = DP(:)  !set dp2 to the same values `<br>`[file=src/cstart.F line=128]` ` BTIME1 = STATIM*86400.D0 `<br>`[file=src/cstart.F line=129]` ` BTIME2=BTIME2+BTIMINC  !new ending time for this record `<br>`[file=src/read_input.F line=2398]` ` &    /,9X,'THE UNIT 141 FILE BEGINS AT TIME=STATIM+BTIMINC.', `<br>`[file=src/read_input.F line=2409]` ` &    /,9X,'THE UNIT 141 FILE BEGINS AT THE TIME OF THE HOT START', `<br>`[file=src/read_input.F line=2421]` ` &    /,9X,'THE UNIT 141 FILE BEGINS AT TIME=STATIM+BTIMINC.', `<br>`[file=src/read_input.F line=2432]` ` &    /,9X,'THE UNIT 141 FILE BEGINS AT THE TIME OF THE HOT START', ` |

The docs describe:
- full-domain updates when `NDDT = +/-1`
- limited-area updates when `NDDT = +/-2`

This is an advanced path.
It should not be treated as the default first way to represent terrain changes.

### 4. Subgrid Terrain Representation

SubgridADCIRCUtility는 외부 입력 생성 도구이다. (`[file=docs/tools/subgrid_adcirc_utility.rst line=6]` ` SubgridADCIRCUtility is a Python-based toolkit for creating subgrid input files for subgrid-enabled ADCIRC. It enables the representation of high-resolution terrain and landcover features without requiring extremely fine mesh resolution, improving simulation accuracy while maintaining computational efficiency. `; `[file=docs/tools/subgrid_adcirc_utility.rst line=11]` ` * **Subgrid Lookup Tables**: Generate lookup tables that store subgrid information for ADCIRC `)

| 항목 | 문서·코드 대조 | 출처와 원문 |
|---|---|---|
| SG-01 lookup netCDF: numNode·numPhi·phiSet | 코드는 subgridFilename을 직접 연다. 코드는 두 차원과 수위 집합 phiSet을 읽는다. 이름에 입력 디렉터리를 자동으로 붙이지 않는다. | 주 입력 파일 rst와 위키에서 변수 수준 schema를 찾지 못했다.<br>`[file=src/subgridLookup.F line=193]` ` CALL CHECK_ERR(NF90_OPEN(TRIM(subgridFilename),NF90_NOWRITE,NC_ID)) `<br>`[file=src/subgridLookup.F line=195]` ` CALL CHECK_ERR(NF90_INQ_DIMID(NC_ID,"numNode",NC_VAR)) `<br>`[file=src/subgridLookup.F line=196]` ` CALL CHECK_ERR(NF90_INQUIRE_DIMENSION(NC_ID,NC_VAR,len=numVerts)) `<br>`[file=src/subgridLookup.F line=198]` ` CALL CHECK_ERR(NF90_INQ_DIMID(NC_ID,"numPhi",NC_VAR)) `<br>`[file=src/subgridLookup.F line=199]` ` CALL CHECK_ERR(NF90_INQUIRE_DIMENSION(NC_ID,NC_VAR,len=numPhi)) `<br>`[file=src/subgridLookup.F line=204]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"phiSet",NC_VAR)) `<br>`[file=src/subgridLookup.F line=205]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,setPhi)) ` |
| SG-02 cmfVertex·cfVertex·cadvVertex | level1이면 cmfVertex와 cadvVertex를 읽는다. 그 밖에는 cfVertex를 읽는다. 파일 배열의 크기는 numPhi×numVerts이다. 코드는 전체 노드 번호로 지역 배열에 배치한다. | 주 입력 파일 rst와 위키에서 변수 수준 schema를 찾지 못했다.<br>`[file=src/subgridLookup.F line=229]` ` ALLOCATE(globalVertLookup(numPhi,numVerts)) `<br>`[file=src/subgridLookup.F line=231]` ` IF(level1)THEN `<br>`[file=src/subgridLookup.F line=232]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"cmfVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=233]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,globalVertLookup)) `<br>`[file=src/subgridLookup.F line=240]` ` cmfVertTab(I,:) = globalVertLookup(:,currNode) `<br>`[file=src/subgridLookup.F line=243]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"cfVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=244]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,globalVertLookup)) `<br>`[file=src/subgridLookup.F line=257]` ` IF(level1)THEN `<br>`[file=src/subgridLookup.F line=258]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"cadvVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=259]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,globalVertLookup)) ` |
| SG-03 gridTotWatDepthVertex·wetTotWatDepthVertex·wetFractionVertex·binaryVertexList | 코드는 총수심·젖은 수심·젖은 비율 lookup 배열을 읽는다. 코드는 노드별 binaryVertexList를 읽는다. 변수의 units 메타데이터를 이 읽기 루틴에서 읽지 않는다. | 주 입력 파일 rst와 위키에서 변수 수준 schema를 찾지 못했다.<br>`[file=src/subgridLookup.F line=273]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"gridTotWatDepthVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=274]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,globalVertLookup)) `<br>`[file=src/subgridLookup.F line=287]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"wetTotWatDepthVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=288]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,globalVertLookup)) `<br>`[file=src/subgridLookup.F line=301]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"wetFractionVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=302]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,globalVertLookup)) `<br>`[file=src/subgridLookup.F line=314]` ` ALLOCATE(globalSubVertList(numVerts)) `<br>`[file=src/subgridLookup.F line=316]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"binaryVertexList",NC_VAR)) `<br>`[file=src/subgridLookup.F line=317]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,globalSubVertList)) ` |

subgrid lookup의 phiSet·수심·보정 계수 단위는 확인하지 않음. (`[file=src/subgridLookup.F line=204]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"phiSet",NC_VAR)) `; `[file=src/subgridLookup.F line=205]` ` CALL check_err(NF90_GET_VAR(NC_ID,NC_VAR,setPhi)) `; `[file=src/subgridLookup.F line=232]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"cmfVertex",NC_VAR)) `; `[file=src/subgridLookup.F line=243]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"cfVertex",NC_VAR)) `; `[file=src/subgridLookup.F line=273]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"gridTotWatDepthVertex",NC_VAR)) `; `[file=src/subgridLookup.F line=301]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"wetFractionVertex",NC_VAR)) `)

| 항목 | 문서·코드 대조 | 출처와 원문 |
|---|---|---|
| K74 subgrid | NetCDF schema는 numNode·numPhi·phiSet·gridTotWatDepthVertex·wetTotWatDepthVertex·wetFractionVertex·binaryVertexList를 요구한다. | `[file=src/subgridLookup.F line=195]` ` CALL CHECK_ERR(NF90_INQ_DIMID(NC_ID,"numNode",NC_VAR)) `<br>`[file=src/subgridLookup.F line=198]` ` CALL CHECK_ERR(NF90_INQ_DIMID(NC_ID,"numPhi",NC_VAR)) `<br>`[file=src/subgridLookup.F line=204]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"phiSet",NC_VAR)) `<br>`[file=src/subgridLookup.F line=273]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"gridTotWatDepthVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=287]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"wetTotWatDepthVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=301]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"wetFractionVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=316]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"binaryVertexList",NC_VAR)) ` |
| K75 subgrid | level1이면 cmfVertex와 cadvVertex를 읽는다. 아니면 cfVertex를 읽는다. CMPI에서 abs(nodes_lg)로 전역 노드를 매핑한다. | `[file=src/subgridLookup.F line=231]` ` IF(level1)THEN `<br>`[file=src/subgridLookup.F line=232]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"cmfVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=236]` ` currNode = abs(nodes_lg(I)) `<br>`[file=src/subgridLookup.F line=240]` ` cmfVertTab(I,:) = globalVertLookup(:,currNode) `<br>`[file=src/subgridLookup.F line=243]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"cfVertex",NC_VAR)) `<br>`[file=src/subgridLookup.F line=257]` ` IF(level1)THEN `<br>`[file=src/subgridLookup.F line=258]` ` CALL check_err(NF90_INQ_VARID(NC_ID,"cadvVertex",NC_VAR)) ` |
| K76 subgrid | 수위가 표의 모든 문턱 아래이면 첫 행을 쓴다. 모든 문턱 이상이면 마지막 wet fraction·마찰 계수를 유지하고 수위 초과분을 두 수심에 더한다. | `[file=src/subgridLookup.F line=375]` ` IF(eta2(i).LT.wetFracVertTab(i,j))THEN `<br>`[file=src/subgridLookup.F line=379]` ` IF(numGreater.EQ.numPhi)THEN `<br>`[file=src/subgridLookup.F line=382]` ` wetFracVertETA2(i) = setPhi(1) `<br>`[file=src/subgridLookup.F line=383]` ` gridDepthVertETA2(i) = gridDepthVertTab(i,1) `<br>`[file=src/subgridLookup.F line=384]` ` wetDepthVertETA2(i) = wetDepthVertTab(i,1) `<br>`[file=src/subgridLookup.F line=391]` ` ELSEIF(numGreater.EQ.0)THEN `<br>`[file=src/subgridLookup.F line=394]` ` wetFracVertETA2(i) = setPhi(numPhi) `<br>`[file=src/subgridLookup.F line=395]` ` gridDepthVertETA2(i) = gridDepthVertTab(i,numPhi) `<br>`[file=src/subgridLookup.F line=396]` ` &            + (eta2(i) - wetFracVertTab(i,numPhi)) `<br>`[file=src/subgridLookup.F line=397]` ` wetDepthVertETA2(i) = wetDepthVertTab(i,numPhi) `<br>`[file=src/subgridLookup.F line=398]` ` &            + (eta2(i) - wetFracVertTab(i,numPhi)) `<br>`[file=src/subgridLookup.F line=400]` ` cmfVertETA2(i) = cmfVertTab(i,numPhi) `<br>`[file=src/subgridLookup.F line=401]` ` cadvVertETA2(i) = cadvVertTab(i,numPhi) `<br>`[file=src/subgridLookup.F line=403]` ` cfVertETA2(i) = cfVertTab(i,numPhi) ` |
| K77 subgrid | 표 내부에서는 수위 문턱을 기준으로 wet fraction·두 수심·마찰·이류를 선형 보간한다. | `[file=src/subgridLookup.F line=410]` ` wetFracVertETA2(i) = ((eta2(i) `<br>`[file=src/subgridLookup.F line=411]` ` &            - wetFracVertTab(i,numPhi-numGreater)) `<br>`[file=src/subgridLookup.F line=412]` ` &            /(wetFracVertTab(i,numPhi-numGreater+1) `<br>`[file=src/subgridLookup.F line=413]` ` &            - wetFracVertTab(i,numPhi-numGreater)) `<br>`[file=src/subgridLookup.F line=414]` ` &            *(setPhi(numPhi-numGreater+1) `<br>`[file=src/subgridLookup.F line=415]` ` &            - setPhi(numPhi-numGreater)) `<br>`[file=src/subgridLookup.F line=416]` ` &            + setPhi(numPhi-numGreater)) `<br>`[file=src/subgridLookup.F line=417]` ` gridDepthVertETA2(i) = ((eta2(i) `<br>`[file=src/subgridLookup.F line=424]` ` wetDepthVertETA2(i) = ((eta2(i) `<br>`[file=src/subgridLookup.F line=432]` ` cmfVertETA2(i) = ((eta2(i) `<br>`[file=src/subgridLookup.F line=439]` ` cadvVertETA2(i) = ((eta2(i) ` |
| K78 subgrid | 아래 문턱이 minDepth인 구간은 선형 보간 대신 위 행을 고른다. subgrid 영역 밖은 수심 ETA2+DP와 wet fraction=1을 쓴다. | `[file=src/subgridLookup.F line=405]` ` ELSEIF(wetFracVertTab(i,numPhi-numGreater).NE. `<br>`[file=src/subgridLookup.F line=409]` ` &         minDepth)THEN `<br>`[file=src/subgridLookup.F line=455]` ` ELSE `<br>`[file=src/subgridLookup.F line=458]` ` wetFracVertETA2(i) = setPhi(numPhi-numGreater+1) `<br>`[file=src/subgridLookup.F line=459]` ` gridDepthVertETA2(i) = `<br>`[file=src/subgridLookup.F line=460]` ` &            gridDepthVertTab(i,numPhi-numGreater+1) `<br>`[file=src/subgridLookup.F line=470]` ` ELSE `<br>`[file=src/subgridLookup.F line=473]` ` gridDepthVertETA2(i) = eta2(i) + dp(i) `<br>`[file=src/subgridLookup.F line=474]` ` wetDepthVertETA2(i) = eta2(i) + dp(i) `<br>`[file=src/subgridLookup.F line=475]` ` wetFracVertETA2(i) = 1.d0 ` |

외부 도구의 table 생성 알고리즘은 확인하지 않음. (`[file=docs/tools/subgrid_adcirc_utility.rst line=11]` ` * **Subgrid Lookup Tables**: Generate lookup tables that store subgrid information for ADCIRC `; `[file=src/subgridLookup.F line=193]` ` CALL CHECK_ERR(NF90_OPEN(TRIM(subgridFilename),NF90_NOWRITE,NC_ID)) `)

| 항목 | 문서·코드 대조 | 출처와 원문 |
|---|---|---|
| XDMF-01 격자 파일의 geometry·depth·topology | 코드는 XDMF 선택에서 geometry를 두 좌표 배열로 읽는다. 코드는 depth Attribute를 읽는다. 코드는 세 노드 topology 배열을 읽는다. 코드는 topology의 0 기준 노드 번호에 1을 더한다. XDMF library 내부는 확인하지 않음. | fort14.rst는 ASCII 레코드 형식을 설명한다. 이 XDMF 객체 규격은 설명하지 않는다.<br>`[file=src/mesh.F line=153]` ` select case(meshType) `<br>`[file=src/mesh.F line=154]` ` case(ASCII) `<br>`[file=src/mesh.F line=155]` ` call read14() `<br>`[file=src/mesh.F line=156]` ` case(XDMF) `<br>`[file=src/mesh.F line=157]` ` call readMeshXDMF() `<br>`[file=src/mesh.F line=867]` ` call xdmfRetrieveGeometryType(xdmfFortranObj, geometryType) `<br>`[file=src/mesh.F line=869]` ` case(301) `<br>`[file=src/mesh.F line=870]` ` geometryTypeString = 'XDMF_GEOMETRY_TYPE_XYZ' `<br>`[file=src/mesh.F line=871]` ` case(302) `<br>`[file=src/mesh.F line=872]` ` geometryTypeString = 'XDMF_GEOMETRY_TYPE_XY' `<br>`[file=src/mesh.F line=887]` ` call xdmfRetrieveGeometryValues(xdmfFortranObj, tempCoord, `<br>`[file=src/mesh.F line=888]` ` &    geometryDataType, 2*np, startIndex, arrayStride, valueStride) `<br>`[file=src/mesh.F line=890]` ` slam = tempCoord(1,:) `<br>`[file=src/mesh.F line=891]` ` sfea = tempCoord(2,:) `<br>`[file=src/mesh.F line=907]` ` case("depth") `<br>`[file=src/mesh.F line=908]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, attributeIndex, `<br>`[file=src/mesh.F line=909]` ` &         dp, XDMF_ARRAY_TYPE_FLOAT64, np, startIndex, arrayStride, valueStride) `<br>`[file=src/mesh.F line=943]` ` call xdmfRetrieveTopologyValues(xdmfFortranObj, xdmf_nm, `<br>`[file=src/mesh.F line=944]` ` &    XDMF_ARRAY_TYPE_INT32, numElementValues, startIndex, `<br>`[file=src/mesh.F line=945]` ` &    arrayStride, valueStride) `<br>`[file=src/mesh.F line=952]` ` nm(j,k) = xdmf_nm(k,j) + 1 ` |
| XDMF-02 boundary Set·Information·property·Attribute | 코드는 마지막 Information 값에서 경계 타입을 읽는다. 코드는 Set property 값으로 elevation 경계를 구분한다. 코드는 BARLANHT·BARLANCFSP·IBCONN·BARINHT·BARINCFSB·BARINCFSP·PIPEHT·PIPECOEF·PIPEDIAM Attribute를 읽는다. 읽은 pipe 경계의 짝 노드 번호에 1을 더한다. | fort14.rst의 경계 의미는 ASCII 필드에 적용한다. XDMF 객체 이름·번호 규격은 설명하지 않는다.<br>`[file=src/mesh.F line=1003]` ` call xdmfRetrieveInformation(xdmfFortranObj, numInformations-1, `<br>`[file=src/mesh.F line=1004]` ` &       itemKey, keyLength, itemValue, valueLength) `<br>`[file=src/mesh.F line=1006]` ` read(itemValue,*) boundaryTypes(setIndex) ! value of either ibtype_orig or ibtypee `<br>`[file=src/mesh.F line=1009]` ` call xdmfRetrieveSetSize(xdmfFortranObj, setSize(setIndex), setIndex) `<br>`[file=src/mesh.F line=1016]` ` call xdmfRetrieveSetProperty(xdmfFortranObj, setIndex, `<br>`[file=src/mesh.F line=1017]` ` &           setPropertyIndex, itemKey, keyLength, itemValue, valueLength) `<br>`[file=src/mesh.F line=1020]` ` case("elevation_specified_boundary ") `<br>`[file=src/mesh.F line=1143]` ` call xdmfRetrieveSetValues(xdmfFortranObj, setIndex, `<br>`[file=src/mesh.F line=1144]` ` &          elevationBoundaries(elevCount)%xdmf_nodes, setDataType, `<br>`[file=src/mesh.F line=1181]` ` case("BARLANHT")   ! barrier height at each node `<br>`[file=src/mesh.F line=1182]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1185]` ` case("BARLANCFSP") ! coefficient of free surface super critical flow `<br>`[file=src/mesh.F line=1186]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1211]` ` case("IBCONN")      ! paired (back face) nodes `<br>`[file=src/mesh.F line=1213]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1218]` ` case("BARINHT")     ! barrier height at each node and its paired node `<br>`[file=src/mesh.F line=1219]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1222]` ` case("BARINCFSB")   ! coefficient of free surface sub critical flow `<br>`[file=src/mesh.F line=1223]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1226]` ` case("BARINCFSP")   ! coefficient of free surface super critical flow `<br>`[file=src/mesh.F line=1227]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1278]` ` case("PIPEHT")    ! barrier height at each node and its paired node `<br>`[file=src/mesh.F line=1279]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1283]` ` case("PIPECOEF")   ! coefficient of free surface sub critical flow `<br>`[file=src/mesh.F line=1284]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1288]` ` case("PIPEDIAM")   ! coefficient of free surface super critical flow `<br>`[file=src/mesh.F line=1289]` ` call xdmfRetrieveAttributeValues(xdmfFortranObj, i, `<br>`[file=src/mesh.F line=1301]` ` &             internalFluxBoundariesWithPipes(ifwpCount)%xdmf_ibconn + 1 ` |
| XDMF-03 노드 속성의 units·number_of_values·default_values·배열 | 코드는 depth Attribute를 속성 수에서 제외한다. 코드는 속성 이름 뒤의 units·number_of_values·default_values Information을 읽는다. 코드는 속성 배열을 읽는다. 값의 의미는 2.7·2.14의 동일 속성 정의를 적용한다. | fort13.rst는 ASCII 헤더·기본값·노드 예외 레코드를 설명한다. 이 XDMF Information 키는 설명하지 않는다.<br>`[file=src/nodalattr.F line=625]` ` INQUIRE(FILE=TRIM(naFileName),EXIST=NAFound) `<br>`[file=src/nodalattr.F line=638]` ` call xdmfOpenDomainGrid(xdmfFortranObj, XDMF_GRID_TYPE_UNSTRUCTURED, `<br>`[file=src/nodalattr.F line=639]` ` &   gridIndex, openMaps, openAttributes, openInformations, openSets) `<br>`[file=src/nodalattr.F line=642]` ` nAttr = numAttributes - 1 ! the depth is included so don't count it `<br>`[file=src/nodalattr.F line=650]` ` call xdmfRetrieveAttributeName(xdmfFortranObj, attributeIndex, `<br>`[file=src/nodalattr.F line=651]` ` &       itemName, nameLength) `<br>`[file=src/nodalattr.F line=653]` ` if (trim(itemName).eq.'depth') then `<br>`[file=src/nodalattr.F line=654]` ` cycle `<br>`[file=src/nodalattr.F line=657]` ` na(nattrCount)%attrName = trim(itemName) `<br>`[file=src/nodalattr.F line=733]` ` if (trim(itemKey).eq. trim(na(i)%attrName) // ' number_of_values') then `<br>`[file=src/nodalattr.F line=734]` ` read(itemValue,*) na(i)%numVals `<br>`[file=src/nodalattr.F line=753]` ` if (trim(itemKey).eq. trim(na(i)%attrName)// ' units') then `<br>`[file=src/nodalattr.F line=754]` ` na(i) % units = trim(itemValue) `<br>`[file=src/nodalattr.F line=756]` ` if (trim(itemKey).eq. trim(na(i)%attrName) // ' default_values') then `<br>`[file=src/nodalattr.F line=758]` ` read(itemValue,*) (na(i)%defaultVals(j),j=1,na(i)%numVals) `<br>`[file=src/nodalattr.F line=765]` ` call xdmfRetrieveAttributeName(xdmfFortranObj, attributeIndex, `<br>`[file=src/nodalattr.F line=766]` ` &      itemName, nameLength) ` |

XDMF 라이브러리 내부 형식은 확인하지 않음.


This suggests an important distinction:
- one path improves the base mesh directly
- another path keeps a manageable mesh while representing finer terrain information through subgrid methods

## What The Official Tooling Implies

The official docs indicate:
- `OceanMesh2D` can interpolate bathymetry and topography and work with DEMs
- `SubgridADCIRCUtility` exists for high-resolution terrain and landcover representation without requiring extremely fine mesh resolution

Common DEM/shoreline sources used with `OceanMesh2D` include the `GSHHS` shoreline and global bathymetry grids (e.g. `SRTM15+`, optional `GEBCO`). ADCIRC utility programs such as `bath_interp` / `interp` / `Griddata` / `Gridscope` handle interpolation of those sources onto mesh nodes.

So bathymetry work is not just "find a DEM and assign depths."
It is a pipeline decision:
- direct interpolation into the mesh
- plus optional nodal attributes
- plus optional subgrid enrichment

## What Must Be Controlled

At minimum, the bathymetry workflow must control:
- source datasets
- shoreline and land-water masking
- vertical datum consistency
- interpolation method
- dry land treatment
- relationship between base topography and nodal attributes

## What We Should Record For Every Bathymetry Workflow

- source dataset names
- horizontal resolution
- vertical datum
- date or vintage
- interpolation method into mesh nodes
- land cutoff or shoreline treatment
- any smoothing or editing applied
- whether subgrid processing was used

## What The Docs Do Not Give Us Directly

The official docs are strong on file semantics, but thinner on field-ready bathymetry assembly recipes.

Missing or weakly specified areas include:
- preferred bathymetry source combinations by problem type
- recommended datum harmonization workflow
- practical QC rules for coastal DEM plus bathymetry merging
- a canonical "good enough first bathymetry pipeline" for new users

These are documentation gaps, not to be filled with guesses.

## Current Working Rule

For now, keep the bathymetry branch in this order:
1. define source datasets
2. define datum policy
3. define mesh interpolation path
4. decide whether subgrid is needed
5. only then consider advanced terrain features like `fort.141`

---
title: "SWASH SWAN 공유 비구조 격자·OceanPack 인프라 — SwanGrid* 객체·다중포맷 reader·ocpmod/ocpids"
model: SWASH
component: src (grid-infra / unstructured / OceanPack)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwanGridobjects/Griddata/Compdata 모듈 파생형·파라미터, SwanGridTopology/Vert/Cell/Face 빌더, SwanReadGrid+ADC/Triangle/Easymesh reader, SwanInterpolatePoint/Output·FindPoint·PointinMesh·CreateEdges·Bpntlist 알고리즘, ocpmod(OCPCOMM1-4) 공통변수·ocpids(OCPINI/OCDTIM) 의 Purpose/Method 주석과 핵심 코드를 file:line 인용; 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH SWAN 공유 비구조 격자·OceanPack 인프라

> SWASH는 SWAN과 동일한 `Swan*` 비구조(삼각형) 격자 코드 + OceanPack(`ocp*`) 서비스 루틴을 **소스 그대로 공유**한다. 파일은 헤더만 `SWASH ... non-hydrostatic wave-flow model` 라이선스로 바뀌었고 자료구조·알고리즘은 SWAN과 동일. (경로: raw/source_code/swash/src/)

## 0. SWAN과의 공유 사실 (중요)

배정된 파일군 전체가 SWAN 동명 파일의 사본이다. 모듈/서브루틴 이름이 모두 `Swan` 접두사(`SwanGridobjects`, `SwanReadADCGrid` 등)이며 작성자도 SWAN과 같은 Marcel Zijlema / Nico Booij / Casey Dietrich / Clayton Hiles (SwanReadADCGrid.ftn90:30-33, SwanBpntlist.ftn90:30-35). 따라서 메커닉의 canonical 설명은 SWAN 측 노트(`models/SWAN/source-analysis/swan-grid-readers.md`)와 동일하며, 본 노트는 **S-tier 요약 + SWASH 관점 차이**만 다룬다.

SWASH 관점에서의 차이:
- 라이선스 헤더가 `SWASH (Simulating WAves till SHore); a non-hydrostatic wave-flow model` 로 교체 (예: SwanGridobjects.ftn90:13, ocpmod.ftn:23). SWAN은 같은 자리에 spectral wave model 문구.
- ADCIRC reader가 수심을 직접 저장 — Method 주석 "Bottom topography from file fort.14 will also be stored" (SwanReadADCGrid.ftn90:49), `use m_genarr`로 `DEPTH` 배열 접근 (:55, 저장 :110, :120). 흐름/수심 모델인 SWASH의 격자-수심 통합 입력.
- `SwanInterpolatePoint`는 점을 찾지 못한 경고 메시지의 좌표에 `XOFFS/YOFFS`를 더한다 (`src/SwanInterpolatePoint.ftn90:124–127`). `fullupdated`는 `src/SwanGridobjects.ftn90:181`에 선언되어 있다. 현재 `src/` 전체에서 이 이름의 참조는 해당 선언 한 곳뿐이다. [10-15 전수 검증 정정]

## 1. 자료구조: SwanGridobjects (vert/cell/face 파생형)

`module SwanGridobjects` — "Module containing data structure for unstructured grids ... derived types for grid vertices, cells and faces" (SwanGridobjects.ftn90:42-46).

핵심 파생형(SwanGridobjects.ftn90:153-193):

| type | 주요 필드 | line |
|---|---|---|
| `geomtype` | 공변/반변 기저벡터(`dx1,dx2,dy1,dy2,rdx1..`), 면 방향 `th1,th2`, 행렬식 `det` | :153-160 |
| `facetype` | `atti(MAXFACEATTI=9)`, `attr(MAXFACEATTR=8)` | :162-165 |
| `celltype` | `nov,nof,active`, `geom(MAXCELLVERT)`, `face(MAXCELLFACE)`, `atti(7)`, `attr(5)` | :167-176 |
| `verttype` | `noc,active,fullupdated`, `cell(MAXVERTCELL=10)`, `atti(7)`, `attr(2)` | :178-186 |
| `gridtype` | `vert_grid/cell_grid/face_grid` 포인터, 단일 target `gridobject` | :188-193 |

속성 인덱스는 정수 parameter로 정의 — vertex: `VERTID,VMARKER,VBC,VERTF1/F2,BINDX,BPOL` (:64-74), `VERTX/VERTY` (:78-79); cell: `CELLID,CMARKER,NEXTCELL,CELLRECT,CELLV1..3` (:90-98), `CELLAREA,CELLCX/CY,CELLCCX/CCY`(centroid·circumcenter, :102-106); face: `FACEID,FMARKER,FACEV1/V2,FACEC1/C2,FACECL/CR,FBTYPE` (:112-129), `FACELEN,FACENORMX/Y,FACEMX/MY,FACEDISTC/DISTG,FACELINPF` (:133-145).

면 정렬 규약(verbatim): "FACEC1 < FACEC2 always" 이고 "the first cell lies left of translation vector (second vertex - first vertex)" (SwanGridobjects.ftn90:121-124). 보간계수 `FACELINPF`: `q_face = q_r + attr(FACELINPF)*(q_l - q_r)` (:142-145).

삼각형만 지원: "we restrict ourselves to triangles only!" (SwanGridCell.ftn90:45), `nov = 3` parameter (:78).

## 2. 격자 데이터 모듈

- `SwanGriddata` — "Data with respect to unstructured grid need to be filled by a grid generator" (SwanGriddata.ftn90:44). generator 종류 parameter: `meth_adcirc=1, meth_triangle=2, meth_easy=3` (:54-56). 좌표/연결 배열: `xcugrd,ycugrd`(local), `xcugrdgl,ycugrdgl`(global), `kvertc`(cell→vertex), `kvertf`(face→vertex), `ivertg,vmark` (:70-82), 셀/면/정점 개수 `ncells/nfaces/nverts` + global/boundary 변종 (:62-68).
- `SwanCompdata` — "Module containing data for computation with unstructured grid" (SwanCompdata.ftn90:42). 경계 다각형: `nbpol`, `nbpt(10000)`, `blist`(경계정점 오름차순), `jbcell/jbface`(경계 셀·면 인덱스) (SwanCompdata.ftn90:57-62).

## 3. 토폴로지 빌더 호출 순서

`SwanGridTopology` — "Setups the SWAN grid topology ... Returns information about the grid and the topology" (SwanGridTopology.ftn90:40-45). `gridobject%vert/cell/face_grid` 할당(:70-72) 후:
1. `SwanGridVert(nverts,...)` — 정점 채움 (:80)
2. `SwanGridCell(ncells,...)` — 셀 채움 (:84)
3. `SwanGridFace(nfaces,...)` — 면 채움 (:88)
4. 경계 셀·면 setup (:90 이하)

서브루틴별 Purpose:
- `SwanGridVert` "Fills vertex-based data structure" (SwanGridVert.ftn90:40). 정점 루프에서 `atti(VERTID)=ivert` 등 채움 (:79, :83-90).
- `SwanGridCell` "Fills cell-based data structure ... triangles only!" (SwanGridCell.ftn90:40-45). 셀 면적/centroid/circumcenter(`CELLAREA/CC*`), 공변·반변 기저(`dx1..`) 계산. [10-15 대조 정정]
기본 `ccn`은 참이다. (`src/SwashInit.ftn90:402`; [theory-unstructured:ST2-005](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)) [10-15 대조 정정]
`ccn`이 참인 검사에서 외심이 셀 내부에 없다고 판정하면 `CELLCCX,CELLCCY`에 무게중심을 저장한다. 같은 분기에서 `ncc`를 1 증가시킨다. (`src/SwanGridCell.ftn90:246,284–291`) [10-15 대조 정정] [10-15 전수 검증 정정]
`SET CC`는 이 대체를 끈다. (`src/SwashReadInput.ftn90:524,557`) [10-15 대조 정정]
외심을 무게중심으로 대체하는 동작은 `swashtech PDF p.44·52`에 명시되어 있다. [10-15 대조 정정] [10-15 전수 검증 정정]
- `SwanGridFace` "Fills face-based data structure" (SwanGridFace.ftn90:40). 좌/우 셀(`icelll/icellr`)·정점(`v1,v2`) 식별, 면 법선·길이·circumcenter 거리 계산 (:67-90).
- `SwanCreateEdges` "Generates edge-based data structure ... Faces of triangles are computed from elements" (SwanCreateEdges.ftn90:40-44) — `kvertf`를 elements에서 도출(reader가 면을 안 주는 경우).
- `SwanBpntlist` "Makes list of boundary vertices in ascending order — counterclockwise in case of sea/mainland boundaries — clockwise in case of island boundaries" (SwanBpntlist.ftn90:46-48). 첫 다각형=sea/mainland, 나머지=island (:52-54).

## 4. 다중포맷 격자 reader

디스패처 `SwanReadGrid(basenm,lenfnm)` — "Reads data from either ADCIRC, Triangle or Easymesh" (SwanReadGrid.ftn90:44). `grid_generator==meth_adcirc → SwanReadADCGrid` (:70-74) 분기.

| reader | 입력 파일 | 좌표·연결 저장 | line |
|---|---|---|---|
| `SwanReadADCGrid` | `fort.14` (ADCIRC) | `ncells,nverts` 헤더 → `xcugrd/ycugrd/DEPTH` → `kvertc(3,·)` 삼각형, ADCIRC 경계정보로 `vmark` | ADC:42, :103, :119-122, :132-135, :142-149 |
| `SwanReadTriangleGrid` | `<name>.node` + `<name>.ele` | 정점 좌표 / 삼각형 정점 | Triangle:40-45 |
| `SwanReadEasymeshGrid` | `<name>.n` + `<name>.e` | 정점 좌표 / 삼각형 정점 | Easymesh:40-45 |

ADCIRC reader 특이점:
- 수심을 동시에 읽어 `DEPTH(ii)`에 저장 (`read ... xcugrd(ii),ycugrd(ii),DEPTH(ii)`, ADC:120). SWASH에선 이 수심이 흐름 모델 바닥지형 입력으로 직결.
- 정점·삼각형 번호 비순차 시 경고: "numbering of vertices/triangles is not sequential in grid file fort.14" (ADC:121, :134).
- ADCIRC 41.07(Casey Dietrich) 업데이트로 "use ADCIRC boundary info to mark all boundary vertices" (ADC:38).

## 5. 점 위치·보간 알고리즘

- `SwanFindPoint(x,y,kvert)` — "Finds the closest vertex index of the given point" (SwanFindPoint.ftn90:40). `kvert=-1`이면 미발견 (:54-55). 경계면(`jbface`)까지 상대거리(`reldis`)로 외부 판정.
- `SwanPointinMesh(x,y)` (logical fn) — "draw a vertical line from the point and count the number of crossings with boundary faces; if the number of crossings is odd then the given point is inside the mesh" (SwanPointinMesh.ftn90:44-45) — 표준 ray-casting odd-crossing 판정.
- `SwanInterpolatePoint(foutp,x,y,finp,excval)` — "First, look for closest vertex and next, interpolate given scalar inside triangle where given point is resided" (SwanInterpolatePoint.ftn90:44). 흐름:
  1. `foutp=excval` 초기화 (:116), `SwanFindPoint`로 최근접 정점 (:120), 미발견 시 경고 후 return (:124-127).
  2. 정점값이 exception이면 return; 점이 정점과 일치하면 그 값 반환 (:132, :141-144).
  3. 점 방향 `th=atan2(dyp,dxp)` (:146) → 정점 주변 셀 루프(`vert(ivert)%noc`, :152)에서 면 방향 `th1,th2`(geomtype)와 비교해 점이 든 삼각형 탐색. 경계정점은 허용오차 `eps=PI/360` (:181-182), 내부는 0 (:183-184).
  4. 찾은 삼각형 내에서 scalar 보간(공변/반변 기저 기반 area-weight). `XOFFS/YOFFS` 좌표 보정은 메시지 출력에만 사용 (:125).
- `SwanInterpolateOutput(...,mip,kvert,...)` — "Look for closest vertex and determine triangle ... Determine weighting coefficients for the corresponding vertices; Interpolate output quantity" (SwanInterpolateOutput.ftn90:48-51). 40.90(Nico Booij) "improved interpolation near obstacles", 41.07 optimization (:39-40). 다수 출력점(`mip`) 배치 + 정점 인덱스(`kvert`) 반환형.

## 6. OceanPack 코어

### 6.1 ocpmod.ftn — OCPCOMM1-4 공통변수 모듈
"Common variables used by the Ocean Pack Service Routines and in SWAN" (ocpmod.ftn:50, 동일 문구 :206, :326, :427). 각 모듈 Updates 주석은 40.41(Oct. 04) "taken from the include file OCPCOMM1.INC" — 과거 include 파일(OCPCOMM1-4.INC)을 Fortran module로 전환한 흔적 (ocpmod.ftn:46, 동일 패턴 :202·:322·:423).

| 모듈 | 역할 | 대표 변수 / line |
|---|---|---|
| OCPCOMM1 | 명령어 reading system | `LINELN=180`(:70-71), `KAART/KAR/KEYWRD/ELTYPE`(:110-117), `ELINT/ELREAL/KARNR`(:131-132), `REFDAY`(:140) |
| OCPCOMM2 | 파일명·프로젝트 | `LENFNM=140`(:226-227), `DIRCH1/2`, `FILENM`, `INST`(='Delft University of Technology'), `PROJID`(='SWASH'), `VERTXT`(:253-260) |
| OCPCOMM3 | 출력 프레임 | `MXQ,MYQ`, `DXQ,DYQ`, `VERNUM`(SWASH 버전번호) (:360-361) |
| OCPCOMM4 | 단위번호·테스트·에러 | `INAN/RNAN`(not-a-number, :448-451), `INPUTF=3/PRINTF=4/SCREEN=6`(:463-482), `ITEST/ITRACE/LEVERR/MAXERR/LTRACE`(:486-502) |

SWASH 표시: `PROJID`/`INST` 기본값 문구가 SWASH로 설정(ocpmod.ftn:238-241), `VERNUM`="version number of SWASH"(:358). 즉 동일 OceanPack 코드를 SWASH 브랜딩으로 사용.

SERIES 목록의 첫 이름 읽기는 `(A36)`이다. (`src/ocpmix.ftn:684–690`; [inputs-setup:SI1-081 수정안](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#4-노트-대조와-수정안)) [10-15 대조 정정]
문자·반복·연속 행 규칙은 `swashuse PDF p.149–154`의 부록 B와 연결된다. ([guide-syntax-build:SG1-930 수정안](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md#4-노트-대조와-수정안)) [10-15 대조 정정]

### 6.2 ocpids.ftn — 설치 의존 서비스 루틴
"OCEAN PACK - Installation dependent subroutines" (ocpids.ftn:3). 포함 루틴(grep): `OCPINI`(:7), `OCDTIM`(:345), `DTSTTI`(:442), `DTTIST`(:572).
- `OCPINI(INIFIL,LREAD,INERR)` — "subroutine initialises a number of common variables; opens standard input and output files" (ocpids.ftn:76-77). MPI 분산메모리(40.30) 도입, init 파일에서 디렉토리 구분자 읽음, 40.03 "backslash replaced by CHAR(92) because of problems on Linux" (:66-68). `LTRACE` 등 OCPCOMM4 변수 초기화.
- `OCDTIM`/`DTSTTI`/`DTTIST` — 날짜·시각 코딩 변환(ISO `yyyymmdd.hhmmss` vs SWASH notation, OCPCOMM4 `ITMOPT` 참조, ocpmod.ftn:465-468).

## 7. 요약 (S-tier)

SWASH의 비구조 격자/보간/입출력 인프라는 SWAN 코드를 그대로 재사용한 **삼각형 전용 edge-based 자료구조**(SwanGridobjects 파생형) + 3종 reader(ADCIRC fort.14 / Triangle .node·.ele / Easymesh .n·.e) + closest-vertex→삼각형 area-weight 보간 + ray-casting in-mesh 판정으로 구성된다. OceanPack(`ocpmod` 공통변수 4모듈 + `ocpids` 설치의존 루틴)은 명령파서·파일I/O·시각변환·에러처리의 공통 토대다. SWAN과의 유일한 실질 차이는 (a) 라이선스/브랜딩 헤더, (b) ADCIRC reader의 수심(DEPTH) 동시 적재로 흐름 모델 바닥지형 입력에 연결되는 점이다. 메커닉 상세는 SWAN `swan-grid-readers.md`를 canonical로 참조.

## 문서와 코드 차이 (10-15 대조)

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech, 공개 저장소 `7949227` 2026-05-06 `"release v12.01"`에서 마지막 변경. 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f` 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함.

매뉴얼 인용은 PDF 쪽 번호를 사용한다. 인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.
출처는 [theory-framework §5](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론), [inputs-setup §5](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#5-차이-결론), [outputs §5](../../../_staging/recovery/compare/swash-outputs-vs-code.md#5-차이-결론), [guide-syntax-build §5](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md#5-차이-결론)의 최종 결론이다.
결론의 절 번호는 해당 보고서의 절 번호이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| guide-syntax-build:SG1-867 | ADCIRC 입력격자 | `swashuse PDF p.39·156`의 READgrid UNSTRUC 도식은 TRIAngle·EASYmesh를 열거한다. `swashuse PDF p.58·67·69`는 fort.14의 경계 표지를 언급한다. `misc/swash.edt:42–43`도 TRIAngle·EASYmesh를 열거한다. | `src/SwashReadInput.ftn90:2489–2497` `call INKEYW ('STA', 'TRIA')` / `if ( KEYWIS('ADC') ) then` / `grid_generator = meth_adcirc` / `!` / `! bottom topography will be taken from fort.14, so` / `logcom(3) = .true.` / `igtype(1) = 3` / `leds(1)   = 2` | C 문서 누락 | READ UNSTRUC의 ADC 선택은 `grid_generator = meth_adcirc`로 설정하고 fort.14의 바닥값을 사용한다. C는 ADC라는 격자 입력 선택지의 누락에 한정한다. 다른 쪽의 fort.14 언급까지 없다고 해석하지 않는다. [10-15 전수 검증 보완] |
| inputs-setup:SI1-077 | 두 자리 연도의 절단점 | `swashuse PDF p.25` `between the years 1931 and 2030` / `formats 2-6` | `src/ocpids.ftn:504` `INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`<br>`src/ocpids.ftn:517–521` `IF (DTTIME(1).LT.JUMPYEAR) THEN` / `DTTIME(1) = 2000 + DTTIME(1)` / `ELSE` / `DTTIME(1) = 1900 + DTTIME(1)` / `ENDIF` | B 문서 오기 | 연도를 읽는 옵션 2·3·5·6은 00–29를 2000–2029로 읽고 30–99를 1930–1999로 읽는다. 범위는 1930–2029이다. 옵션 4는 연도를 읽지 않는다. git 이력: `8756667:src/ocpids.ftn:500` `INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`. JUMPYEAR=30과 LT 비교는 최초 공개판부터 같다. H9의 배열 초기화는 연도 절단점을 바꾸지 않는다. 두 자리 연도는 00–29를 2000–2029로 읽는다. 30–99는 1930–1999로 읽는다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] [10-15 전수 검증 보완] |
| inputs-setup:SI1-081 | 파일 이름 최대 길이 | `swashuse PDF p.27` `does not permit file names longer than 36 characters`<br>`swashuse PDF p.32` `36 characters` | `src/ocpmod.ftn:227` `PARAMETER (LENFNM=140)`<br>`src/ocpmod.ftn:254` `CHARACTER (LEN=LENFNM) :: FILEA , FILEB , FILENM`<br>`src/SwashInputField.ftn90:86` `character(LEN=LENFNM)                :: filenm   ! file name` | B 문서 오기 | 공통 파일 이름 저장 길이는 경로를 포함한 140자이다. SERIES 목록 첫 파일 이름만 읽는 `(A36)` 경로는 별도 제한이다. 이를 전체 파일 이름 한도로 일반화하지 않는다. git 이력: `8756667:src/ocpmod.ftn:227` `PARAMETER (LENFNM=140)`. LENFNM=140은 최초 공개판부터 있다. 공통 파일명 길이가 36에서 140으로 바뀐 커밋은 없다. 공통 파일명 저장 길이는 경로를 포함하여 140자다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] [10-15 전수 검증 보완] |
| inputs-setup:SI1-102 | 최대 파일 수·swashinit 변경 | `swashuse PDF p.32` `maximum number of file names is 99` / `change highest unit number of 99 to a higher number` | `src/ocpids.ftn:195` `IUNMAX = 99999`<br>`src/ocpids.ftn:275–277` `FUNLO = 21` / `!/SGI      FUNLO = 103` / `FUNHI = IUNMAX`<br>`src/ocpids.ftn:253` `WRITE (12, 210) IUNMAX, 'highest file ref. number'`  `src/ocpids.ftn:196` `!/SGI        IUNMAX = 199`; `src/ocpids.ftn:135` `READ (11, *,   ERR=930, END=930) IUNMAX`. | B 문서 오기 | 일반 스위치의 기본 최고 파일 단위 번호는 99999이다. 이는 파일 이름 개수와 다른 수량이다. SGI 스위치는 최고 번호 199·최저 동적 번호 103을 쓴다. swashinit의 설정을 읽고 기록하는 경로는 있다. git 이력: `8756667:src/ocpids.ftn:192` `IUNMAX = 99999`. 기본 최고 단위 번호 99999는 최초 공개판부터 있다. 99에서 바뀐 공개 커밋은 없다. 일반 빌드의 기본 최고 파일 단위 번호는 99999다. 이 값은 파일명 개수가 아니다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] [10-15 전수 검증 보완] |
| inputs-setup:SI1-210 | 시간 형식 5의 내용·따옴표 | `swashuse PDF p.45–46` `5 : 87/05/30 15:30:00’` | `src/ocpids.ftn:544` `READ (TIMSTR, '(I2,5(1X,I2))', ERR=98) (DTTIME(II), II=1,6)` | B 문서 오기 | 읽는 값의 순서는 연도·월·일·시·분·초이다. 문서 예시는 닫는 따옴표만 적었다. 공백을 포함한 문자열을 명령에 쓸 때는 앞뒤 따옴표를 갖춰야 한다. git 이력: `8756667:src/ocpids.ftn:539` `READ (TIMSTR, '(I2,5(1X,I2))', ERR=98) (DTTIME(II), II=1,6)       30.11`. 형식 5의 여섯 정수 판독은 최초 공개판부터 같다. H9는 배열을 초기화하지만 이 형식과 따옴표 규칙을 바꾸지 않는다. 형식 5는 연도·월·일·시·분·초를 읽는다. 공백이 들어 있는 명령 문자열에는 양쪽 따옴표가 필요하다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] [10-15 전수 검증 보완] |
| inputs-setup:SI1-504 | SET CC | `swashuse PDF p.155` `CC` | `src/SwashReadInput.ftn90:557` `if ( KEYWIS ('CC') ) ccn = .false.`<br>`src/SwashModule1.ftn90:746` `! indicates whether non-Delaunay (obtuse) cells are corrected or not`<br>`src/SwanGridCell.ftn90:246` `if ( ccn ) then` | C 문서 누락 | CC 문법은 부록 C p.155에 있다. CC는 ccn을 거짓으로 바꾸어 외심 위치 보정 분기를 끈다. C는 이 선택 효과의 설명 누락에 한정한다. |
| inputs-setup:SI1-505 | SET PRINTF·PRTEST | `swashuse PDF p.155` `[printf] [prtest]` | `src/SwashReadInput.ftn90:559–562` `!      the unit numbers PRINTF and PRTEST should be set in swashinit,` / `!      so not documented` / `call ININTG ('PRINTF', PRINTF, 'UNC', 0)` / `call ININTG ('PRTEST', PRTEST, 'UNC', 0)` | C 문서 누락 | PRINTF·PRTEST 문법은 부록 C p.155에 있다. 코드는 두 출력 장치 번호를 바꾼다. C는 p.33–35의 설명 부재와 장치 번호의 의미·변경 효과에 한정한다. 코드의 `so not documented` 주석을 현재 설명서 전체의 누락 근거로 사용하지 않는다. |
| outputs:SO1-205 | itrace 호출 횟수 | `swashuse PDF p.122` `at the first [itrace] entries of each subroutine.` | `src/ocpmix.ftn:1242–1243` `IF (ITRACE.EQ.0) RETURN` / `IF (IENT.GT.ITRACE) RETURN`<br>`src/ocpmix.ftn:1251–1252` `IENT=IENT+1` / `WRITE (PRTEST, 10) SUBNAM`<br>`src/SwashQuanOutp.ftn90:86` `integer, save                         :: ient = 0 ! number of entries in this subroutine`<br>`src/ocpmix.ftn:1212` `!     IF ITRACE>0, a message is printed up to ITRACE times` `src/SwashReadInput.ftn90:2788–2792`는 양의 ITRACE에서 ltrace를 켠다. `8756667:src/ocpmix.ftn:1254,1262–1263`도 검사 뒤 증가·출력 순서이다. 현재 OpenMP 분기의 `src/ocpmix.ftn:1246–1247`도 같은 검사 뒤에 있다. `608ffd7`·`9554c98`은 이 파일을 변경하지 않았다. ([E1 판정표](../../../_staging/recovery/compare/SWASH-git-verify-E1.md)) | E 코드 결함 후보 (강함) | 초기 `IENT=0`에서 양의 ITRACE는 지정 횟수보다 한 번 더 출력을 허용한다. `ITRACE=0`이면 즉시 반환한다. 일반 경로와 OpenMP 경로의 E 후보를 유지한다. [10-15 전수 검증 보완] |
| theory-framework:ST1-161 | 그림 2.4·삼각 격자 계량 | `swashtech PDF p.43` `n=2` / `l_e,A_s,A_v,d_e` / `Note that the dual mesh is not explicitly used, only the volume of the dual mesh elements is stored.` / `N_v,N_e,N_c` | `src/SwanGridFace.ftn90:384–390` `dxl = sqrt( (xcf-xcl)*(xcf-xcl) + (ycf-ycl)*(ycf-ycl) )` / `dxr = sqrt( (xcf-xcr)*(xcf-xcr) + (ycf-ycr)*(ycf-ycr) )` / `dxf = dxl + dxr` / `!` / `if ( dxf /= 0. ) then` / `face(iface)%attr(FACEDISTC) =  1. / dxf` / `face(iface)%attr(FACELINPF) = dxl / dxf` | F 표기 차이 | 그림 2.4의 `d_e`는 인접 셀에 걸친 전체 쌍대 변 길이이다. 내부 면의 코드는 양쪽 셀 중심에서 면 중심까지의 거리를 더해 `dxf`를 만든다. `dxf /= 0.`이면 그 역수를 `FACEDISTC`에 저장한다. 이는 거리 계량을 저장한다는 문서 설명과 대응하는 F 표기 차이이다. 격자 계량의 대응을 확인했으므로 H에서 바꾼다. 무게중심 대체 조건은 ST1-165이다. |
| theory-framework:ST1-209 | 정삼각형의 계량 | `swashtech PDF p.52` `v_1=(-\frac12\sqrt3,0)` / `v_2=(\frac12\sqrt3,0)` / `v_3=(0,\frac32)` / `(0,\frac12)` / `\lvert e_i\rvert=\sqrt3` / `\lvert\tilde e_i\rvert=\frac12` / `\lvert s_1\rvert=\frac34\sqrt3` / `\lvert\tilde s_i\rvert=\frac14\sqrt3` / `i=1,2,3` | `src/SwanGridCell.ftn90:242–244` `fac = ( (x2-x3)*(x3-x1)+(y2-y3)*(y3-y1) )/( (x1-x2)*(y3-y1)-(y1-y2)*(x3-x1) )` / `xc = 0.5 * ( fac*(y1-y2) + x1+x2 )` / `yc = 0.5 * ( fac*(x2-x1) + y1+y2 )` | F 표기 차이 | 해석: 문서의 세 꼭짓점 좌표를 코드 외심식에 대입하면 중심은 `(0, 1/2)`이다. F의 범위는 이 좌표 계산이다. 예제 좌표는 프로그램 기본값이 아니다. |
| theory-framework:ST1-307 | 외심 보정의 선택·기본값 | `swashtech PDF p.52–53`; `swashuse PDF p.155` `CC` | `src/SwashInit.ftn90:402` `ccn        = .true.`<br>`src/SwashReadInput.ftn90:557` `if ( KEYWIS ('CC') ) ccn = .false.`<br>`src/SwanGridCell.ftn90:276–280` `else` / `!` / `numcrs = 1` / `endif`<br>`src/SwanGridCell.ftn90:284` `if ( mod(numcrs,2) == 1 ) then`<br>`src/SwanGridCell.ftn90:288–291` `! current cell is obtuse and will be corrected by replacing circumcenter by centroid` / `ncc = ncc + 1` / `cell(icell)%attr(CELLCCX) = cell(icell)%attr(CELLCX)` / `cell(icell)%attr(CELLCCY) = cell(icell)%attr(CELLCY)`<br>`src/SwanGridCell.ftn90:246` `if ( ccn ) then` | C 문서 누락 | C는 `swashtech PDF p.52–53`에 없는 외심 보정 선택의 설명이다. CC 명령 표기는 사용자 설명서에도 있다. 기본값은 외심의 셀 내부 여부를 검사하고 외부로 판정하면 무게중심으로 대체한다. SET CC는 `ccn`을 꺼 `numcrs = 1` 경로로 보내므로 외심을 유지한다. |
| theory-framework:ST1-308 | 0 중심 거리의 역수 예외 | `swashtech PDF p.52` | `src/SwanGridFace.ftn90:388–394` `if ( dxf /= 0. ) then` / `face(iface)%attr(FACEDISTC) =  1. / dxf` / `face(iface)%attr(FACELINPF) = dxl / dxf` / `else` / `face(iface)%attr(FACEDISTC) = 0.` / `face(iface)%attr(FACELINPF) = 1.` / `endif` | C 문서 누락 | 전체 중심 거리가 0이면 역수 계수를 0으로 둔다. 보간 계수는 1로 둔다. 부분 쌍대 변 하나가 0인 문서 예와 전체 거리 0을 구별한다. |

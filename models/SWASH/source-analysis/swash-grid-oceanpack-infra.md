---
title: "SWASH SWAN 공유 비구조 격자·OceanPack 인프라 — SwanGrid* 객체·다중포맷 reader·ocpmod/ocpids"
model: SWASH
component: src (grid-infra / unstructured / OceanPack)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwanGridobjects/Griddata/Compdata 모듈 파생형·파라미터, SwanGridTopology/Vert/Cell/Face 빌더, SwanReadGrid+ADC/Triangle/Easymesh reader, SwanInterpolatePoint/Output·FindPoint·PointinMesh·CreateEdges·Bpntlist 알고리즘, ocpmod(OCPCOMM1-4) 공통변수·ocpids(OCPINI/OCDTIM) 의 Purpose/Method 주석과 핵심 코드를 file:line 인용"
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
- 보간 시 좌표 오프셋 `XOFFS/YOFFS`(SwashCommdata) 사용 (SwanInterpolatePoint.ftn90:49-50, :125). 자료구조의 spectral 관련 필드(`fullupdated` 등, SwanGridobjects.ftn90:181)는 SWASH에서 거의 미사용(흐름 모델은 spectral space 없음). ⚠ 정확한 미사용 여부는 흐름 솔버 측 코드 추가 검증 필요(source-needed).

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
- `SwanGridCell` "Fills cell-based data structure ... triangles only!" (SwanGridCell.ftn90:40-45). 셀 면적/centroid/circumcenter(`CELLAREA/CC*`), 공변·반변 기저(`dx1..`) 계산. circumcenter 외부 셀 카운트 `ncc` 처리 (:75).
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

### 6.2 ocpids.ftn — 설치 의존 서비스 루틴
"OCEAN PACK - Installation dependent subroutines" (ocpids.ftn:3). 포함 루틴(grep): `OCPINI`(:7), `OCDTIM`(:345), `DTSTTI`(:442), `DTTIST`(:572).
- `OCPINI(INIFIL,LREAD,INERR)` — "subroutine initialises a number of common variables; opens standard input and output files" (ocpids.ftn:76-77). MPI 분산메모리(40.30) 도입, init 파일에서 디렉토리 구분자 읽음, 40.03 "backslash replaced by CHAR(92) because of problems on Linux" (:66-68). `LTRACE` 등 OCPCOMM4 변수 초기화.
- `OCDTIM`/`DTSTTI`/`DTTIST` — 날짜·시각 코딩 변환(ISO `yyyymmdd.hhmmss` vs SWASH notation, OCPCOMM4 `ITMOPT` 참조, ocpmod.ftn:465-468).

## 7. 요약 (S-tier)

SWASH의 비구조 격자/보간/입출력 인프라는 SWAN 코드를 그대로 재사용한 **삼각형 전용 edge-based 자료구조**(SwanGridobjects 파생형) + 3종 reader(ADCIRC fort.14 / Triangle .node·.ele / Easymesh .n·.e) + closest-vertex→삼각형 area-weight 보간 + ray-casting in-mesh 판정으로 구성된다. OceanPack(`ocpmod` 공통변수 4모듈 + `ocpids` 설치의존 루틴)은 명령파서·파일I/O·시각변환·에러처리의 공통 토대다. SWAN과의 유일한 실질 차이는 (a) 라이선스/브랜딩 헤더, (b) ADCIRC reader의 수심(DEPTH) 동시 적재로 흐름 모델 바닥지형 입력에 연결되는 점이다. 메커닉 상세는 SWAN `swan-grid-readers.md`를 canonical로 참조.

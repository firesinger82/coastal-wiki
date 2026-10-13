---
title: "SWAN VTK output (ParaView 호환) — 3 writers verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanVTKPDataSets.ftn90` (308) + `SwanVTKWriteData.ftn90` (207) + `SwanVTKWriteHeader.ftn90` (292) 직접 read — 모두 41.95 (2022-07 Zijlema) 신설. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — 3 file header verbatim"
verification_date: 2026-06-01
last_source_check: "2026-10-13 (recovery 대조 반영)"
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-output-writers-implementation.md
  - models/SWAN/source-analysis/swan-output-formats.md
---

## Scope

이 노트는 SWAN의 VTK 출력 파일 3개를 다룬다. 전체 줄 수는 807줄이다. <!-- count: models/SWAN/raw/source_code/swan/src/SwanVTK*.ftn90 = 3 files, 807 lines --> 이 구현은 VTK XML에 raw appended binary를 기록한다. (`src/SwanVTKWriteHeader.ftn90:277`의 `vtkline = '  <AppendedData encoding="raw">'//lf`; 파일별 줄 수는 아래 Source basis 표.) [10-13 전수 검증 정정]

## Source basis

| File | Lines | Subroutine 인자 | Purpose |
|---|---|---|---|
| `SwanVTKWriteHeader.ftn90` | 292 | `(uvtk, pstype, nvar, ivtyp, mxkf, mxkl, mykf, mykl)` | **Writes header to a VTK file** |
| `SwanVTKWriteData.ftn90` | 207 | `(uvtk, pstype, nvar, ivtyp, voqr, data, lenp, mxk, myk, ionod)` | **Writes appended data to a VTK file** |
| `SwanVTKPDataSets.ftn90` | 308 | `(upvt, pstype, nvar, ivtyp, mxk, myk, vtkfile, upvd, psname, iarr)` | **Writes parallel VTK file type (.pvts/.pvtu)** |

## 1. 41.95 신설 시점 (2022-07)

세 파일의 작성자는 Marcel Zijlema이다. 각 파일의 Updates에는 `41.95, July 2022: New subroutine`이 적혀 있다. (`src/SwanVTKPDataSets.ftn90:32,36`; `src/SwanVTKWriteData.ftn90:32,36`; `src/SwanVTKWriteHeader.ftn90:32,36`.) [10-13 전수 검증 정정]

## 2. 3 subroutine 역할

### 2.1 SwanVTKWriteHeader (header writer)

```fortran
subroutine SwanVTKWriteHeader(uvtk, pstype, nvar, ivtyp, mxkf, mxkl, mykf, mykl)
```

- `uvtk` = VTK file unit
- `pstype` = output point set type (regular / unstructured / parallel)
- `nvar` = output variable 수
- `ivtyp(nvar)` = 변수 타입 (scalar / vector / tensor)
- `mxkf/mxkl, mykf/mykl` = grid index range (first/last)

→ VTK XML header (`<VTKFile type="..." version="0.1">` + `<UnstructuredGrid>` / `<StructuredGrid>`) writeup.

### 2.2 SwanVTKWriteData (data writer)

```fortran
subroutine SwanVTKWriteData(uvtk, pstype, nvar, ivtyp, voqr, data, lenp, mxk, myk, ionod)
```

- `voqr` = variable output request
- `data(lenp, nvar)` = 실제 SWAN output data array
- IONOD는 각 점이 속한 부영역 번호이다. (`src/SwanVTKWriteData.ftn90:68` `integer, dimension(*), intent(in)         :: ionod  ! indicates in which subdomain nodes are located`.)

SWAN writer는 raw appended binary를 기록한다. 이 경로에 base64·zlib 선택 처리는 없다. (`src/SwanVTKWriteHeader.ftn90:277` `vtkline = '  <AppendedData encoding="raw">'//lf`.)

### 2.3 SwanVTKPDataSets (parallel VTK)

```fortran
subroutine SwanVTKPDataSets(upvt, pstype, nvar, ivtyp, mxk, myk, vtkfile, upvd, psname, iarr)
```

- Parallel VTK = **.pvts / .pvtu** (Parallel VTK Structured / Unstructured) — 각 MPI process가 별도 `.vts/.vtu` 작성 + master가 통합 `.pvts/.pvtu` index 작성
- ParaView 가 `.pvts/.pvtu` 열면 모든 process partial file 자동 통합
- `psname` = parallel partition 이름
- `iarr` = partition 정보

→ unSWAN ([swan-unstructured-time-step](swan-unstructured-time-step.md)) MPI 병렬 시 ParaView 시각화 path.

## 3. VTK format 배경

### 3.1 VTK XML format vs Legacy

본 module은 **VTK XML format** (`.vts`, `.vtu`, `.pvts`, `.pvtu`) 사용. ASCII (legacy `.vtk`) 가 아닌 modern XML + binary appended data:
- 빠른 read/write
- ParaView 5.x 표준
- SWAN writer는 raw appended binary를 기록한다. 이 경로에 base64·zlib 선택 처리는 없다. (`src/SwanVTKWriteHeader.ftn90:277` `vtkline = '  <AppendedData encoding="raw">'//lf`.)

### 3.2 SWAN output variable → VTK 매핑

VTK 출력은 BLOCK 파일명의 .vt 또는 .VT 포함 검사로 선택한다. 별도 VTK 명령 키워드는 없다. (`src/swanpre2.ftn:1216–1217`의 `VTK = INDEX( FILENM, '.VT' ).NE.0 .OR.`와 다음 줄 `&          INDEX (FILENM, '.vt' ).NE.0`.) [10-13 전수 검증 보완]
- Scalar: H_s, T_m01, T_p, Depth, Setup, Dissipation 등
- DIR은 각도 스칼라로 기록한다. (`src/swanmain.ftn:1800` `OVSVTY(IVTYPE) = 2`; `src/SwanVTKWriteData.ftn90:124` `if ( ovsvty(ivtype) < 3 ) then        ! scalars`.)
- 벡터는 x·y와 0인 z 성분을 기록한다. (`src/SwanVTKWriteHeader.ftn90:190` `NumberOfComponents="3"`; `src/SwanVTKWriteData.ftn90:144` `if ( ios == 0 .and. ionod(ip+i) == iproc ) write(uvtk,iostat=ios) data(ip+i,voqr(ivtype)), data(ip+i,voqr(ivtype)+1), 0.`.) [10-13 전수 검증 보완]
- Spectral output은 별도 (VTK 직접 미지원, SPECOUT)

## 4. 활용 예

```
SWAN compute
↓
BLOCK 'FRAME1' NOHEADER 'output.vts' LAYOUT 4 HSIGN TPS DIR PDIR WLEN UBOT
↓
SwanVTKWriteHeader → SwanVTKWriteData
↓
ParaView 5.x → output.vts open → contour/streamline/volume rendering
```

unSWAN + MPI 시:
```
process 0..N → output_part_0.vtu .. output_part_N.vtu
master → output.pvtu (SwanVTKPDataSets)
↓
ParaView → output.pvtu → 통합 시각화
```

## 5. Cross-references

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) User §4.6.2 BLOCK + Tech Ch 7 parallel
- [swan-source-coverage-audit](swan-source-coverage-audit.md) §4.1 신규 발견의 VTK 파일 3개. [10-13 전수 검증 정정]
- [swan-output-formats](swan-output-formats.md) — 기존 ASCII/binary block format
- [swan-output-writers-implementation](swan-output-writers-implementation.md) — 기존 writer infrastructure
- [swan-unstructured-time-step](swan-unstructured-time-step.md) — parallel VTK 의 unSWAN+MPI 시 사용
- [swan-parallel-implementation](swan-parallel-implementation.md) — MPI 병렬 + parallel VTK
- Author: Marcel Zijlema (41.95, 2022-07)
- [R6 출력 대조](../../../_staging/recovery/compare/swan-outputs-vs-code.md#26-netcdfmatvtk와-appendix-c) — VTK 파일·배열. [10-13 전수 검증 정정]

## 6. 구현 근거

격자별 .vts/.vtu 선택은 문서와 같다. 병렬 .pvts/.pvtu와 비정상 수집 파일의 세부 동작은 코드 근거이다. (`src/swanout2.ftn:859` `WRITE(FILENM(ILPOS+1:ILPOS+4),35) '.vts'`; `src/swanout2.ftn:860,868–869,879–903`; swanuse PDF 109–110쪽 / 인쇄 101–102쪽.)

실제 물리량 배열은 appended Float32이다. 벡터는 세 성분을 기록한다. (`src/SwanVTKWriteHeader.ftn90:178` `DataArray type="Float32"`; `src/SwanVTKWriteHeader.ftn90:190` `NumberOfComponents="3"`.)

VTK 출력은 BLOCK 파일명의 .vt 또는 .VT 포함 검사로 선택한다. (`src/swanpre2.ftn:1216–1217`의 `VTK = INDEX( FILENM, '.VT' ).NE.0 .OR.`와 다음 줄 `&          INDEX (FILENM, '.vt' ).NE.0`.) [10-13 전수 검증 보완]

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD `43e9bbb` (2026-07-13 patch B). (`src/swanmain.ftn:965` `VERNUM = 41.51`.)

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R6:O-116 | VTK 파일·배열 | swanuse PDF 109–110쪽 / 인쇄 101–102쪽는 `.vtk` 요청, 격자별 `.vts`·`.vtu`, binary XML 및 병렬 부분 영역의 통합 시각화를 설명한다. `.pvts`·`.pvtu`와 비정상 수집 파일은 이 쪽에 명시되지 않는다. | `src/swanout2.ftn:859` `WRITE(FILENM(ILPOS+1:ILPOS+4),35) '.vts'`. 868행은 `.vtu`이다. `src/SwanVTKWriteHeader.ftn90:178`에는 `DataArray type="Float32"`가 있다. 190행에는 `NumberOfComponents="3"`가 있다. `src/swanout2.ftn:860,869`은 병렬 .pvts/.pvtu를 선택한다. 879–903행은 시각별 DataSet을 수집 파일에 기록한다. | C 문서 누락 | 격자별 .vts/.vtu 선택은 문서와 같다. 병렬 .pvts/.pvtu와 비정상 수집 파일의 세부 동작은 코드 근거이다. 실제 물리량 배열은 appended Float32이다. 벡터는 세 성분을 기록한다. C는 swanuse PDF 109–110쪽에 없는 이 파일·배열 세부 사항에 한정한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R6:N-021 | VTK 인수·인코딩 | `models/SWAN/source-analysis/swan-vtk-output.md:58`: `ionod = output mode (ASCII / binary appended)`. 60행: `binary 또는 base64 write`. 82행: `Compressed binary support (zlib)`. | `src/SwanVTKWriteData.ftn90:68` `integer, dimension(*), intent(in)         :: ionod  ! indicates in which subdomain nodes are located`. `src/SwanVTKWriteHeader.ftn90:277` `vtkline = '  <AppendedData encoding="raw">'//lf`. | B 문서 오기 | IONOD는 각 점이 속한 부영역 번호이다. SWAN writer는 raw appended binary를 기록한다. 이 경로에 base64·zlib 선택 처리는 없다. VTK 규격 전체의 기능과 SWAN writer의 기능을 구분한다. |
| R6:N-022 | VTK 요청·DIR 형식 | `models/SWAN/source-analysis/swan-vtk-output.md:86`: `BLOCK / TABLE ... VTK file로 기록`. 88행: `Mean wave direction (DIR + cos/sin)`. 96행: `BLOCK 'FRAME1' VTK 'output.vts' LAYOUT 4 HSIGN TPS DIR PDIR WLEN UBOT`.<br>swanuse PDF 109–110쪽 / 인쇄 101–102쪽는 `.vtk` 요청, 격자별 `.vts`·`.vtu`, binary XML 및 병렬 부분 영역의 통합 시각화를 설명한다. `.pvts`·`.pvtu`와 비정상 수집 파일은 이 쪽에 명시되지 않는다. | `src/swanpre2.ftn:1216–1217`의 `VTK = INDEX( FILENM, '.VT' ).NE.0 .OR.`와 다음 줄 `&          INDEX (FILENM, '.vt' ).NE.0`. `src/swanmain.ftn:1800` `OVSVTY(IVTYPE) = 2`. `src/SwanVTKWriteData.ftn90:124` `if ( ovsvty(ivtype) < 3 ) then        ! scalars`. `src/SwanVTKWriteData.ftn90:144`은 `data(ip+i,voqr(ivtype)), data(ip+i,voqr(ivtype)+1), 0.`을 기록한다. | B 문서 오기 | VTK 출력은 BLOCK 파일명의 .vt 또는 .VT 포함 검사로 선택한다. 별도 VTK 명령 키워드는 없다. 예제는 `BLOCK 'FRAME1' NOHEADER 'output.vts' LAYOUT 4 HSIGN TPS DIR PDIR WLEN UBOT`로 고친다. DIR은 각도 스칼라로 기록한다. 벡터는 x·y와 0인 z 성분을 기록한다. [10-13 전수 검증 보완]

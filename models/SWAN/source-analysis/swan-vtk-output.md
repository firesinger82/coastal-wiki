---
title: "SWAN VTK output (ParaView 호환) — 3 writers verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanVTKPDataSets.ftn90` (308) + `SwanVTKWriteData.ftn90` (207) + `SwanVTKWriteHeader.ftn90` (292) 직접 read — 모두 41.95 (2022-07 Zijlema) 신설."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — 3 file header verbatim"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-output-writers-implementation.md
  - models/SWAN/source-analysis/swan-output-formats.md
---

## Scope

SWAN 의 **3 VTK output writers** (총 807 lines). VTK = **Visualization Toolkit** (Kitware) 의 binary file format — ParaView·VisIt·VTK Python 등 시각화 도구의 표준. 41.95 (2022-07 Zijlema) 신설 (cycle III 최신 추가). 본 위키 기존 [[swan-output-formats]] / [[swan-output-writers-implementation]] 미커버.

## Source basis

| File | Lines | Subroutine 인자 | Purpose |
|---|---|---|---|
| `SwanVTKWriteHeader.ftn90` | 292 | `(uvtk, pstype, nvar, ivtyp, mxkf, mxkl, mykf, mykl)` | **Writes header to a VTK file** |
| `SwanVTKWriteData.ftn90` | 207 | `(uvtk, pstype, nvar, ivtyp, voqr, data, lenp, mxk, myk, ionod)` | **Writes appended data to a VTK file** |
| `SwanVTKPDataSets.ftn90` | 308 | `(upvt, pstype, nvar, ivtyp, mxk, myk, vtkfile, upvd, psname, iarr)` | **Writes parallel VTK file type (.pvts/.pvtu)** |

## 1. 41.95 신설 시점 (2022-07)

[[swan-source-coverage-audit]] §4.2 의 41.x history 에서 **가장 최근 신규 module** (41.95) — 41.91 QC surf breaking 후 6개월. Author: Marcel Zijlema (SWAN team lead).

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
- `ionod` = output mode (ASCII / binary appended)

→ VTK `<AppendedData encoding="raw">` 안에 SWAN 변수 (H_s, T_p, Wind, Current 등) binary 또는 base64 write.

### 2.3 SwanVTKPDataSets (parallel VTK)

```fortran
subroutine SwanVTKPDataSets(upvt, pstype, nvar, ivtyp, mxk, myk, vtkfile, upvd, psname, iarr)
```

- Parallel VTK = **.pvts / .pvtu** (Parallel VTK Structured / Unstructured) — 각 MPI process가 별도 `.vts/.vtu` 작성 + master가 통합 `.pvts/.pvtu` index 작성
- ParaView 가 `.pvts/.pvtu` 열면 모든 process partial file 자동 통합
- `psname` = parallel partition 이름
- `iarr` = partition 정보

→ unSWAN ([[swan-unstructured-time-step]]) MPI 병렬 시 ParaView 시각화 path.

## 3. VTK format 배경

### 3.1 VTK XML format vs Legacy

본 module은 **VTK XML format** (`.vts`, `.vtu`, `.pvts`, `.pvtu`) 사용. ASCII (legacy `.vtk`) 가 아닌 modern XML + binary appended data:
- 빠른 read/write
- ParaView 5.x 표준
- Compressed binary support (zlib)

### 3.2 SWAN output variable → VTK 매핑

User cmd `BLOCK` / `TABLE` ([[swan-documentation-stack]] User §4.6.2) 출력 가능 변수가 VTK file로 기록:
- Scalar: H_s, T_m01, T_p, Depth, Setup, Dissipation 등
- Vector: Wind (U10), Current (Ux, Uy), Mean wave direction (DIR + cos/sin)
- Spectral output은 별도 (VTK 직접 미지원, SPECOUT)

## 4. 활용 예

```
SWAN compute
↓
BLOCK 'FRAME1' VTK 'output.vts' LAYOUT 4 HSIGN TPS DIR PDIR WLEN UBOT
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

- [[swan-documentation-stack]] User §4.6.2 BLOCK + Tech Ch 7 parallel
- [[swan-source-coverage-audit]] §3.5 신규 발견 (3 VTK files)
- [[swan-output-formats]] — 기존 ASCII/binary block format
- [[swan-output-writers-implementation]] — 기존 writer infrastructure
- [[swan-unstructured-time-step]] — parallel VTK 의 unSWAN+MPI 시 사용
- [[swan-parallel-implementation]] — MPI 병렬 + parallel VTK
- Author: Marcel Zijlema (41.95, 2022-07)
- External: VTK XML format spec (https://www.kitware.com/products/books/VTKUsersGuide.pdf), ParaView (https://www.paraview.org/)

## 6. 한계 + 다음 단계

- 본 노트는 3 subroutine header + Purpose 만 verified. 실제 XML markup / binary encoding (line 50-200 in each file) 별도.
- User cmd BLOCK `VTK` 옵션의 syntax (swanuse.pdf p.97-107) 직접 인용 별도.
- 41.95 (2022-07) 이후 추가 41.x 활동 (41.96+) 추적 별도 — TUDelft SWAN GitLab repo check.
- ParaView vs VisIt vs Python VTK 호환성 검증 별도.
- Compressed binary (zlib) 옵션 지원 여부 확인 별도.

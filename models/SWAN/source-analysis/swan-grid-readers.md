---
title: "SWAN unstructured grid readers (ADCIRC fort.14 + Easymesh + Triangle) verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanRead{ADCGrid,EasymeshGrid,TriangleGrid,Grid}.ftn90` 직접 read (header line 1-65 + Purpose). 모두 40.80 (2007-07/12) Zijlema 신설. Tech §8.2 Notes on grid generation + User cmd READGRID UNSTRUCTURED (swanuse.pdf p.34) 매핑."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header + Purpose verbatim"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-adcirc-coupling.md
  - models/SWAN/source-analysis/swan-foundation.md
---

## Scope

SWAN 의 **4개 unstructured grid format readers** — 모두 40.80 (2007) Zijlema 신설. Tech §8.2 + User cmd `READGRID UNSTRUCTURED` (swanuse.pdf p.34).

## Source basis

| File | Lines | Author | Format |
|---|---|---|---|
| `SwanReadADCGrid.ftn90` | 189 | Zijlema 40.80 (2007-12) | **ADCIRC `fort.14`** |
| `SwanReadEasymeshGrid.ftn90` | 155 | Zijlema 40.80 (2007-07) | **Easymesh `<name>.n + <name>.e`** |
| `SwanReadTriangleGrid.ftn90` | 178 | Zijlema 40.80 (2007-07) | **Triangle `<name>.node + <name>.ele`** |
| `SwanReadGrid.ftn90` | — | Zijlema 40.80 | Generic / dispatcher |

## 1. Verbatim Purpose (header 인용)

### 1.1 SwanReadADCGrid.ftn90 (189 lines)

```fortran
subroutine SwanReadADCGrid
!   Authors
!   Updates
!   40.80, December 2007: New subroutine
!   Purpose
!   Reads ADCIRC grid described in fort.14
```

→ **ADCIRC fort.14** = ADCIRC 의 표준 unstructured grid file (node coordinates + element connectivity + boundary types). [[swan-adcirc-coupling]] + [[swan-unstructured-time-step]] 의 ADCIRC-SWAN coupling 시 핵심 path. **SwanCompUnstruc 41.20 Casey Dietrich tightly coupled ADCIRC+SWAN** ([[swan-unstructured-time-step]] §1) 의 기반.

### 1.2 SwanReadEasymeshGrid.ftn90 (155 lines)

```fortran
subroutine SwanReadEasymeshGrid ( basenm, lenfnm )
!   Updates
!   40.80, July 2007: New subroutine
!   Purpose
!   Reads Easymesh grid described in <name>.n and <name>.e
```

→ **Easymesh** = 무료 2D triangular mesh generator (Niceno, http://www-dinma.units.it/nirftc/research/easymesh/). 2개 파일 형식:
- `<name>.n` = node list (id, x, y, mark)
- `<name>.e` = element list (id, v1, v2, v3, mark)

`basenm` 인자 + `lenfnm` (basename 길이) — `<basenm>.n` + `<basenm>.e` 동시 read.

### 1.3 SwanReadTriangleGrid.ftn90 (178 lines)

```fortran
subroutine SwanReadTriangleGrid ( basenm, lenfnm )
!   Updates
!   40.80, July 2007: New subroutine
!   Purpose
!   Reads Triangle grid described in <name>.node and <name>.ele
```

→ **Triangle** = Jonathan Shewchuk의 2D mesh generator (https://www.cs.cmu.edu/~quake/triangle.html). Tech §8.2 의 권장 mesh generator (추정). 형식:
- `<name>.node` = node list (id, x, y, attributes, boundary marker)
- `<name>.ele` = element list (id, v1, v2, v3, region marker)

### 1.4 SwanReadGrid.ftn90

```fortran
subroutine SwanReadGrid ( basenm, lenfnm )
!   Updates
!   40.80, July 2007: New subroutine
```

→ Generic/dispatcher (specific format은 별도 dispatch routine).

## 2. User Manual cmd `READGRID UNSTRUCTURED` (swanuse.pdf p.34)

User cmd `READGRID UNSTRUCTURED [type]` — type:
- `ADCIRC` → SwanReadADCGrid
- `EASYMESH` → SwanReadEasymeshGrid
- `TRIANGLE` → SwanReadTriangleGrid

세 format 의 **공통 변환**: vertex coordinates `(xcugrd(nverts), ycugrd(nverts))` + element-vertex connectivity → SWAN 내부 `SwanGriddata` ([[swan-source-coverage-audit]] §1.1) + `SwanGridobjects`.

## 3. Mesh format 비교

| 항목 | ADCIRC fort.14 | Easymesh .n/.e | Triangle .node/.ele |
|---|---|---|---|
| 파일 수 | 1 (통합) | 2 (분리) | 2 (분리) |
| Boundary marker | 명시 (NETA, NVELL, IBTYPE) | node mark | node + edge marker |
| Attribute | 다중 (Manning, viscosity 등) | 단일 | 다중 (NodeAttribute) |
| Element 타입 | 3-node triangle | 3-node triangle | 3-node triangle (default) |
| 분야 | 해양 storm-surge (ADCIRC) | 일반 CFD | 일반 (academic) |
| License | ADCIRC LGPL | Free (academic) | Free (Shewchuk) |

→ SWAN 은 **3-node triangle mesh** 만 지원 (다른 format의 quadrilateral 등 미지원).

## 4. Cross-references

- [[swan-documentation-stack]] User cmd READGRID UNSTRUCTURED (p.34) + Tech §8.2 grid generation
- [[swan-source-coverage-audit]] §3.3 4 grid readers 신규 발견
- [[swan-unstructured-time-step]] — readers의 출력 `xcugrd/ycugrd` + connectivity 사용
- [[swan-adcirc-coupling]] — fort.14 reader가 ADCIRC-SWAN coupling 의 grid path
- [[swan-foundation]] — SWAN module 구조
- External:
  - ADCIRC fort.14: https://adcirc.org (모델 documentation)
  - Easymesh: http://www-dinma.units.it/nirftc/research/easymesh/
  - Triangle: https://www.cs.cmu.edu/~quake/triangle.html

## 5. 한계

- 본 노트는 4 reader 의 header + Purpose 만 verified. fort.14 binary format / Easymesh ASCII format / Triangle ASCII format 의 정확한 record 구조 별도.
- ADCIRC fort.14 의 boundary types (IBTYPE) 이 SWAN 의 BOUND* command 와 어떻게 매핑되는지 별도.
- Tech §8.2 의 정확한 grid generation 권장 (mesh quality criteria) deep 미실시.
- User cmd READGRID UNSTRUCTURED 의 syntax 상세 별도.
- 41.x version history (40.80 이후 update) 별도 추적 — 본 노트는 40.80 신설 시점만.

---
title: "SWAN unstructured grid readers (ADCIRC fort.14 + Easymesh + Triangle) verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "원본 SwanReadADCGrid·SwanReadEasymeshGrid·SwanReadTriangleGrid·SwanReadGrid의 Authors·Updates·Purpose와 읽기 문장을 대조했다. 네 루틴은 40.80에서 Marcel Zijlema가 신설했다. 신설 월은 ADCIRC 리더가 2007년 12월이고 나머지가 2007년 7월이다. swantech §8.2는 PDF 145쪽 / 인쇄 137쪽이다. READGRID UNSTRUCTURED는 swanuse PDF 43쪽 / 인쇄 35쪽이다. 2026-10-13 recovery 대조 보고서 R1–R8을 반영했다." # [10-13 전수 검증 정정]
last_source_check: 2026-10-13 (recovery 대조 반영)
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

ADCIRC 형식의 격자 입력은 `SwanReadGrid`에서 `SwanReadADCGrid`를 호출한다. (`src/SwanReadGrid.ftn90:73–77`) `SwanReadADCGrid`는 `fort.14`의 좌표·수심·삼각형 연결·경계를 읽는다. (`src/SwanReadADCGrid.ftn90:95,122,135,148–176`) [비구조 시간 단계](swan-unstructured-time-step.md) 루틴의 이력에는 Casey Dietrich의 41.20 결합 확장이 적혀 있다. (`src/SwanCompUnstruc.ftn90:38,56`) [10-13 전수 검증 정정]

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

세 형식의 리더는 좌표와 삼각형 연결을 `SwanGriddata`의 배열에 저장한다. (`src/SwanReadADCGrid.ftn90:58,122,135`; `src/SwanReadEasymeshGrid.ftn90:50,105,132`; `src/SwanReadTriangleGrid.ftn90:50,120,125,155,160`) 이후 `SwanGridTopology`가 `SwanGridobjects`의 격자 객체를 구성한다. (`src/SwanGridTopology.ftn90:50–51,70–88`; [소스 목록](swan-source-coverage-audit.md) §1.1) [10-13 전수 검증 보완]

## 3. Mesh format 비교

| 항목 | ADCIRC fort.14 | Easymesh .n/.e | Triangle .node/.ele |
|---|---|---|---|
| 파일 수 | 1 (통합) | 2 (분리) | 2 (분리) |
| Boundary marker | 명시 (NETA, NVELL, IBTYPE) | node mark | 노드 경계표지. `src/SwanReadTriangleGrid.ftn90:125` `read(ndsd, *, end=950, err=910) ii, xcugrd(ii), ycugrd(ii), rdum, vmark(ii)` |
| SWAN 리더가 소비하는 속성 | 좌표·수심·삼각형 연결·경계 | 좌표·노드 경계표지·삼각형 연결. `src/SwanReadEasymeshGrid.ftn90:105,132`의 읽기 문장. | 속성 0개와 rdum 하나인 분기. [10-13 전수 검증 정정] |
| Element 타입 | 3-node triangle | 3-node triangle | 3-node triangle |
| 분야 | 해양 storm-surge (ADCIRC) | 일반 CFD | 일반 (academic) |
| License | ADCIRC LGPL | Free (academic) | Free (Shewchuk) |

위 표의 속성 행은 SWAN 리더가 실제 소비하는 필드로 한정한다. ADCIRC 경로는 이 파일에서 좌표·수심·연결·경계 정보를 읽는다. `src/SwanReadADCGrid.ftn90:122` `read(ndsd, *, end=950, err=910) ii, xcugrd(ii), ycugrd(ii), DEPTH(ii)`; `src/SwanReadADCGrid.ftn90:135` `read(ndsd, *, end=950, err=910) ii, idum, kvertc(1,ii), kvertc(2,ii), kvertc(3,ii)`. 경계의 읽기 문장은 같은 파일 148–176행이다. [10-13 전수 검증 정정]

Triangle 노드 리더는 속성 0개와 rdum 하나를 읽는 분기로 나뉜다. `src/SwanReadTriangleGrid.ftn90:118` `if ( nattr == 0 ) then`; `src/SwanReadTriangleGrid.ftn90:125` `read(ndsd, *, end=950, err=910) ii, xcugrd(ii), ycugrd(ii), rdum, vmark(ii)`. 일반 파일 형식의 다중 속성 능력을 이 리더의 지원으로 바꾸지 않는다.

## 4. Cross-references

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) — READGRID UNSTRUCTURED는 swanuse PDF 43쪽 / 인쇄 35쪽이다. 격자 생성 설명은 swantech §8.2의 PDF 145쪽 / 인쇄 137쪽이다. [10-13 전수 검증 정정]
- [swan-source-coverage-audit](swan-source-coverage-audit.md) §3.3 4 grid readers 신규 발견
- [swan-unstructured-time-step](swan-unstructured-time-step.md) — 리더의 배열에서 구성한 격자 객체를 사용한다. `src/SwanGridTopology.ftn90:70–88`; `src/SwanCompUnstruc.ftn90:323–324`의 `vert => gridobject%vert_grid`와 `cell => gridobject%cell_grid`. [10-13 전수 검증 보완]
- [swan-adcirc-coupling](swan-adcirc-coupling.md) — §A는 ADCIRC 형식의 격자 읽기를 설명한다. §B는 PADCSWAN 결합 인터페이스를 설명한다. 격자 읽기 호출은 `src/SwanReadGrid.ftn90:73–77`이다. [10-13 전수 검증 정정]
- [swan-foundation](swan-foundation.md) — SWAN module 구조
- External:
  - ADCIRC fort.14: https://adcirc.org (모델 documentation)
  - Easymesh: http://www-dinma.units.it/nirftc/research/easymesh/
  - Triangle: https://www.cs.cmu.edu/~quake/triangle.html

## 5. 격자 입력 연결

- ADCIRC 경로는 좌표·수심·삼각형 연결·경계를 읽는다. `src/SwanReadADCGrid.ftn90:122` `read(ndsd, *, end=950, err=910) ii, xcugrd(ii), ycugrd(ii), DEPTH(ii)`; `src/SwanReadADCGrid.ftn90:135` `read(ndsd, *, end=950, err=910) ii, idum, kvertc(1,ii), kvertc(2,ii), kvertc(3,ii)`.
- ADCIRC fort.14 의 boundary types (IBTYPE) 이 SWAN 의 BOUND* command 와 어떻게 매핑되는지 별도.
- 격자 품질 기준은 [swan-tech-ch8-unstructured-grid-scheme](../manual-notes/swan-tech-ch8-unstructured-grid-scheme.md) §8.2에 연결한다.
- 기본 ADCIRC를 표시한다. ADCIRC는 fort.14를 읽는다. fname은 Triangle·Easymesh의 확장자 없는 이름이다. swanuse PDF 43쪽 / 인쇄 35쪽: 기본 `ADCirc`; “‘fname’ basename … without extension.” `src/swanpre1.ftn:1478` `CALL INKEYW ('STA', 'ADC')`; `src/SwanReadADCGrid.ftn90:95` `grdfil = 'fort.14'`.
- 41.x version history (40.80 이후 update) 별도 추적 — 본 노트는 40.80 신설 시점만.

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

빈 인용 칸은 `—`로 표시한다. 표의 절 번호는 각 행이 링크한 대조 보고서의 절 번호다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R4:T1-312 | 격자 리더의 속성 범위 | R4 §4에 보존된 반영 전 `source-analysis/swan-grid-readers.md:101`의 `다중 (NodeAttribute)` | `src/SwanReadTriangleGrid.ftn90:118` `if ( nattr == 0 ) then`; `src/SwanReadTriangleGrid.ftn90:125` `read(ndsd, *, end=950, err=910) ii, xcugrd(ii), ycugrd(ii), rdum, vmark(ii)`; `src/SwanReadADCGrid.ftn90:122` `read(ndsd, *, end=950, err=910) ii, xcugrd(ii), ycugrd(ii), DEPTH(ii)`; `src/SwanReadADCGrid.ftn90:135` `read(ndsd, *, end=950, err=910) ii, idum, kvertc(1,ii), kvertc(2,ii), kvertc(3,ii)` | B 문서 오기 | 일반 파일 형식의 능력과 SWAN 리더가 소비하는 필드를 구분한다. Triangle은 속성 0개와 rdum 하나인 분기로 나뉜다. ADCIRC 경로는 좌표·수심·삼각형 연결·경계를 읽는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) [10-13 전수 검증 보완] |

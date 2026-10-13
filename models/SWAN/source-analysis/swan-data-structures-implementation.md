---
title: "swan data structures implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-data-structures-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN data structures — AC1/AC2, COMPDA, BSPECS, memory tables

## Scope note

The arrays that hold SWAN's state during a run: action density, spectral grid, geographic grid, working scratch space (`COMPDA`), boundary storage, source-term memo tables, and per-process matrix workspace. With declaration file:line, dimensions, allocation/deallocation points.

## Source basis

Codex deep scan 2026-05-06 of:
- `src/swmod1.ftn`, `src/swmod2.ftn` — module declarations (`M_GENARR`)
- `src/swanmain.ftn` — top-level runtime arrays
- `src/swancom1.ftn` — solver workspace
- `src/SwanGriddata.ftn90` — unstructured-grid module

## A. Action density (`AC1`, `AC2`)

| Array | Declaration | Allocation | Shape | Note |
|-------|-------------|------------|-------|------|
| `AC2` | `[file=src/swmod2.ftn line=1027]` (`M_GENARR`, `SAVE, ALLOCATABLE :: AC2(:,:,:)`) | `[file=src/swanpre1.ftn line=4980]` `ALLOCATE(AC2(MDC,MSC,MCGRD))`; zero at `[file=src/swanpre1.ftn line=4989]` | `(MDC, MSC, MCGRD)` | new/current time level |
| `AC1` | `src/swanmain.ftn:296` | 전체 크기는 `src/swanmain.ftn:500`의 `IF ( NSTATM.EQ.1 .AND. MXITNS.GT.1 .OR. PROPSC.EQ.3 ) THEN`을 따른다. 나머지 경로의 최초 할당은 `src/swanmain.ftn:518`의 `IF(.NOT.ALLOCATED(AC1)) ALLOCATE(AC1(0,0,0))`이다. | 전체 크기 또는 `(0,0,0)` | 이전 시간의 작용밀도 |

Semantics documented in argument lists at `[file=src/swanmain.ftn line=266]`, `[file=src/swanmain.ftn line=6826-6827]`.

AC1의 전체 크기 할당은 인용한 NSTATM·MXITNS·PROPSC 조건을 따른다. 이미 할당된 AC1은 이 ELSE에서 해제하지 않는다. SNEXTI의 시간 복사는 별도의 NSTATC·ITERMX·PROPSC 조건을 따른다. `src/swanmain.ftn:6892`의 `IF (NSTATC.EQ.1) THEN` 안에서 `src/swanmain.ftn:6893–6895`의 `IF (ITERMX.GT.1`<br>`&       .OR. PROPSC.EQ.3`<br>`&                                 ) THEN`을 만족할 때 복사한다. `src/swanmain.ftn:6899`의 원문은 `AC1(IDD,ISS,IXY) = AC2(IDD,ISS,IXY)`이다. [R8:N1-001](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).
```fortran
DO IXY = 1, MCGRD
  DO ISS = 1, MSC
    DO IDD = 1, MDC
      AC1(IDD,ISS,IXY) = AC2(IDD,ISS,IXY)
```

## B. Spectral grid (`SPCSIG`, `SPCDIR`, `DDIR`, `FRINTF`, `FRINTH`)

- Module storage `[file=src/swmod2.ftn line=1029]`: `SPCSIG(:)` shape `(MSC)`, `SPCDIR(:,:)` shape `(MDC,6)`.
- Interface forms used in `swanmain.ftn`: `SPCDIR(MDC,6)`, `SPCSIG(MSC)` at `[file=src/swanmain.ftn line=3642]`, `[file=src/swanmain.ftn line=6830-6831]`.
- `SPCSIG` built geometrically from `SLOW` × `SFAC`; `FRINTF = log(SHIG/SLOW)/(MSC-1)`, `FRINTH = sqrt(SFAC)` at `[file=src/swanpre1.ftn line=4685-4691]`.
- `DDIR` computed at `[file=src/swanpre1.ftn line=1773]` (full circle `2π/MDC`) or `[file=src/swanpre1.ftn line=1789]` (sector).
- `SPCDIR(:,1)` = direction angle (rad); columns 2..6 = `cos`, `sin`, `cos²`, `cos·sin`, `sin²` `[file=src/swanpre1.ftn line=4706]`, `[file=src/swanmain.ftn line=6816-6821]`.
- Field semantics documented at `[file=src/swmod1.ftn line=2030-2037]`.

## C. Geographic grid

| Array | What | Where |
|-------|------|-------|
| `XCGRID(:,:)`, `YCGRID(:,:)` | structured node coordinates | `[file=src/swmod2.ftn line=1025]`, `[file=src/swmod2.ftn line=1028]` |
| `KGRPNT(:,:)` | structured (IX,IY) → wet-point compact index | same module; populated at `[file=src/swanpre1.ftn line=5166-5169]` |
| `MCGRD` | number of wet computational points | `[file=src/swmod1.ftn line=2046]` |
| `vmark`, `nverts`, `ivertg` | unstructured: vertex boundary marker, count, index | `[file=src/SwanGriddata.ftn90 line=65]`, `[file=src/SwanGriddata.ftn90 line=71-72]`; consumed at `[file=src/swanmain.ftn line=146]`, `[file=src/swanmain.ftn line=5053]`, `[file=src/swanmain.ftn line=9101]` |
| `ncells`, `nfaces` | unstructured topology counters (NTRIA equivalent) | `[file=src/SwanGriddata.ftn90 line=62-64]` |

`KGRPNT` indirection is the structured wet-point compaction: `INDX = KGRPNT(IX, IY)` at `[file=src/swanmain.ftn line=7103-7105]`.

## D. Workspace `COMPDA`

`[file=src/swanmain.ftn line=296]` declared, `[file=src/swanmain.ftn line=463]` allocated as `COMPDA(MCGRD, MCMVAR)`.

JDP2 등의 인덱스는 COMPDA 열을 가리킨다. SWOEXD는 JCOMPDA 변수에 이 인덱스를 넣어 공통 출력 보간 코드를 실행한다. `src/swanout1.ftn:1987`의 원문은 `JCOMPDA=JDSXI ! give J-name here, JDSXI/JAICE2/JHICE2`이다. `src/swanout1.ftn:1994`의 원문은 `CALL SWIPOL(COMPDA(1,JCOMPDA),OVEXCV(IVTYPE),XC,YC, MIP,`이다.

| Index | Field | Definition |
|-------|-------|------------|
| `JDP2` | new-time depth | `=8` `[file=src/swanmain.ftn line=1505]` |
| `JVX2` | new-time current X | `=11` `[file=src/swanmain.ftn line=1508]` |
| `JVY2` | new-time current Y | `=12` `[file=src/swanmain.ftn line=1509]` |
| `JWX2` | new-time wind X | `=16` `[file=src/swanmain.ftn line=1513]` |
| `JWY2` | new-time wind Y | `=17` `[file=src/swanmain.ftn line=1514]` |
| `JFRC2` | bottom friction | `[file=src/swanmain.ftn line=1529]`, used at `[file=src/swancom1.ftn line=7266]`, `[file=src/swancom1.ftn line=3581]` |

Layout `(MCGRD, MCMVAR)` confirmed in shape declarations `[file=src/swanmain.ftn line=4746]`. Each field column is the value at every wet point; "new-time" suffix indicates the post-time-update value (vs "1" suffix = old time, used for interpolation).

`WIND10` (10-m wind speed) is **derived in source-term routines** from `JWX2/JWY2` rather than stored as a dedicated `COMPDA` column.

## E. Boundary storage (`BSPECS`, `BGRIDP`)

- `BSPECS` declared `[file=src/swanmain.ftn line=295]` and allocated `(MDC, MSC, NBSPEC, 2)` at `[file=src/swanmain.ftn line=433]`.
- Rank semantics confirmed at `[file=src/swanmain.ftn line=6945]`:
  - rank 1 = direction bin
  - rank 2 = frequency bin
  - rank 3 = boundary spectrum index (`K1`/`K2`)
  - rank 4 = time slot (old/new for nonstat interpolation)

- `BGRIDP` declared `[file=src/swanmain.ftn line=294]`, allocated as `BGRIDP(6 * NBGRPT)` at `[file=src/swanmain.ftn line=435]`.
- Per-boundary-point packing at `[file=src/swanmain.ftn line=4025-4030]`:
  - 6 ints per point: `[INDXGR, type, W1×1000, K1, W2×1000, K2]`
- Runtime decode at `[file=src/swanmain.ftn line=6938-6946]`:
  - `INDXGR = BGRIDP(6i-5)`, `type = BGRIDP(6i-4)`, `W1 = 0.001 * BGRIDP(6i-3)`, `K1 = BGRIDP(6i-2)`, `K2 = BGRIDP(6i)`

## F. Source-term memory tables

- `MEMNL4(MDC, MSC, MCGRD)` — quadruplet DIA workspace; declared `[file=src/swancom1.ftn line=871]`. Allocated full size only when `IQUAD >= 3` at `[file=src/swancom1.ftn line=1030]`; zero-size placeholder otherwise `[file=src/swancom1.ftn line=1042]`, `[file=src/swancom1.ftn line=1046]`.
- `MEMSINB(MDC, MSC, MCGRD)` (paired with `MEMSINA`) — Babanin/DBYB wind input workspace; declared `[file=src/swancom1.ftn line=876]`. Allocated only when `IWIND == 8` at `[file=src/swancom1.ftn line=1100-1104]`; zero-size placeholder otherwise `[file=src/swancom1.ftn line=1115-1116]`.
- Both reset to zero after allocation at `[file=src/swancom1.ftn line=1152]`, `[file=src/swancom1.ftn line=1157]`.
- 활성 MEMNL4와 MEMSINB의 전 배열 초기화는 수렴 반복마다 sweep 묶음 앞에서 수행한다. `src/swancom1.ftn:1487`의 원문은 `DO 450 ITER = 1, ITERMX`이다. `src/swancom1.ftn:1541`의 `IF ( IQUAD .GE. 3 ) THEN` 안에서 `src/swancom1.ftn:1545`의 `MEMNL4(IDC,ISC,IP)=0.`를 수행한다. `src/swancom1.ftn:1581`의 `IF ( IWIND .EQ. 8 ) THEN` 안에서 `src/swancom1.ftn:1586`의 `MEMSINB(IDC,ISC,IP)=0.`를 수행한다.
- Both deallocated at end of `SWCOMP` at `[file=src/swancom1.ftn line=2466]`, `[file=src/swancom1.ftn line=2471]`.

## G. Per-process matrix workspace

`IMATDA, IMATRA, IMATLA, IMATUA, IMAT5L, IMAT6U` — all dimensioned `REAL :: (MDC, MSC)` at `[file=src/swancom1.ftn line=5349-5351]`.

SWSOR 끝의 여섯 배열 초기화를 모든 해법의 공통 후처리로 일반화하지 않는다. 실제 호출되는 SWSIP의 끝은 두 배열을 초기화한다. `src/swancom1.ftn:8931–8932`의 원문은 `IMATDA = 0.` 및 `IMATRA = 0.`이다. SOURCE의 정렬 분기와 SwanTranspAc의 행렬 준비도 각각 구별해서 설명한다. `src/SwanTranspAc.ftn90:117–118`의 원문은 `amat = 0.` 및 `rhs  = 0.`이다. [R8:N1-014](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).

정렬 OpenMP 경로는 SWMATR를 PRIVATE으로 선언한다. 하위 루틴의 IMAT*는 이 작업 배열의 전달된 절편을 읽고 쓴다. `src/swancom1.ftn:1175`의 원문은 `!$OMP+PRIVATE(SWMATR, LSWMAT, ALIMW, GROWW, IDCMIN, IDCMAX)`이다. `src/swancom1.ftn:3644`의 원문은 `CALL SOLPRE(AC2                ,SWMATR(1,1,JAOLD)  ,`이다.

## Working Rules

1. To debug action density at a specific point: `AC2(:, :, KGRPNT(IX, IY))` is the structured access; for unstructured use `AC2(:, :, vertex_index)`.
2. 나머지 경로의 최초 할당은 0 크기이다. 이미 할당된 AC1은 이 ELSE에서 해제하지 않는다. `src/swanmain.ftn:518`의 원문은 `IF(.NOT.ALLOCATED(AC1)) ALLOCATE(AC1(0,0,0))`이다.
3. `COMPDA(:, JDP2)` is the **wet** depth at new time level (after water-level update). `COMPDA(:, JDP1)` is the previous time level (used for time interpolation in source terms).
4. `MEMNL4`/`MEMSINB` are zero-sized when their respective options are off — `IF (ALLOCATED(MEMNL4))` checks won't disambiguate; check `IQUAD` / `IWIND` instead.

## Common Pitfalls

- **Hot-restart spec mismatch**: if MDC, MSC, or MCGRD differ between runs, `AC2` allocation is a different shape. Hot-start file format embeds these dimensions; mismatch = fatal at read.
- **Custom `COMPDA` field index** — adding a new field requires updating both the index constant in `swanmain.ftn:1498-1527` and `MCMVAR` in the allocation. Forgetting one corrupts neighboring fields.
- **OpenMP bug fingerprint**: if you see "matrix corrupted" only with `OMP_NUM_THREADS > 1`, check that any custom code added to the source-term loop didn't use a SHARED variable when it should have been PRIVATE.

## References

### Source files (Codex deep scan, 2026-05-06)

- `src/swmod1.ftn`, `src/swmod2.ftn` — module declarations.
- `src/swanmain.ftn` — runtime arrays, OpenMP region.
- `src/swancom1.ftn` — solver workspace, MEM tables.
- `src/SwanGriddata.ftn90` — unstructured grid module.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 50+ file:line citations |
| Coverage | all primary in-memory data structures and their allocation lifecycle |
| Review status | 2026-10-13 recovery 대조 보고서 R1–R8 반영 |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TC-021 | 정규 격자와 일치하는 스펙트럼 방향의 작은 이동 | — | `src/swanpre1.ftn:4709–4713`: `IF (OPTG.EQ.1) THEN`; `IF (ABS(MODULO(SPCDIR(ID,1)-ALPC+0.25*PI ,0.5*PI)-0.25*PI)`; 다음 행 조건 `.LT. 1.E-6) THEN`; `SPCDIR(ID,1) = OLDDIR + 2.E-6`. | C 문서 누락 | 정규 격자 방향과 거의 일치하는 방향 bin을 $2\times10^{-6}$ rad 이동한다. 등간격 방향 격자의 초기 구성 뒤에 적용하는 예외이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R8:N1-001 | AC1 할당·복사 조건 | `source-analysis/swan-data-structures-implementation.md:32`의 ``only when nonstationary or S&L (`PROPSL=3`)`` 및 `:118`의 ``in stationary `AC1` is unallocated`` | `src/swanmain.ftn:500` `IF ( NSTATM.EQ.1 .AND. MXITNS.GT.1 .OR. PROPSC.EQ.3 ) THEN`; `:502`, `:505`의 전체 크기 할당; `:518` `IF(.NOT.ALLOCATED(AC1)) ALLOCATE(AC1(0,0,0))`. 시간 복사는 `:6892` `IF (NSTATC.EQ.1) THEN` 안의 `:6893–6895` `IF (ITERMX.GT.1`<br>`&       .OR. PROPSC.EQ.3`<br>`&                                 ) THEN`에서 `:6899` `AC1(IDD,ISS,IXY) = AC2(IDD,ISS,IXY)`로 수행한다. | B | AC1의 전체 크기 할당은 인용한 NSTATM·MXITNS·PROPSC 조건을 따른다. 나머지 경로의 최초 할당은 0 크기이다. 이미 할당된 AC1은 이 ELSE에서 해제하지 않는다. SNEXTI의 시간 복사는 별도의 NSTATC·ITERMX·PROPSC 조건을 따른다. 할당부 `:497–498`의 주석도 MXITNS 조건을 생략하므로 실행문과 구분한다. 노트의 PROPSL은 이 조건에서 PROPSC로 고친다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:N1-002 | 기억 배열 초기화의 반복 수준 | `source-analysis/swan-data-structures-implementation.md:104`은 `Both also reset per-wet-point/per-bin during sweep setup`이라고 적으며 초기화 위치를 `:1545`, `:1586`으로 정확히 지목한다. 이 문장에는 매 sweep마다 초기화한다는 명시가 없다 | `src/swancom1.ftn:1487` `DO 450 ITER = 1, ITERMX`. `:1541`의 `IF ( IQUAD .GE. 3 ) THEN` 안에서 `:1545` `MEMNL4(IDC,ISC,IP)=0.`를 수행한다. `:1581`의 `IF ( IWIND .EQ. 8 ) THEN` 안에서 `:1586` `MEMSINB(IDC,ISC,IP)=0.`를 수행한다. 뒤의 sweep 반복은 `:1698` `!WFR        DO 410 SWPDIR = 1, 4` 또는 `:1699` `!JAC        DO 410 ISWP = 0, 3`이다. | F — 시점 표현 | 활성 MEMNL4와 MEMSINB의 전 배열 초기화는 수렴 반복마다 sweep 묶음 앞에서 수행한다. 노트의 “during sweep setup”을 sweep 묶음의 준비로 읽으면 구현과 일치한다. 이를 매 sweep마다라는 주장으로 확대했던 B 판정을 F로 고친다. 노트에는 초기화 시점을 수렴 반복 시작으로 명시한다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:N1-003 | JCOMPDA의 존재 | source-analysis/swan-data-structures-implementation.md:69 ``This codebase doesn't use a literal `JCOMPDA` symbol`` | `src/swanout1.ftn:1987` `JCOMPDA=JDSXI ! give J-name here, JDSXI/JAICE2/JHICE2`; `:1994` `CALL SWIPOL(COMPDA(1,JCOMPDA),OVEXCV(IVTYPE),XC,YC, MIP,`. | B | JDP2 등의 인덱스는 COMPDA 열을 가리킨다. SWOEXD는 JCOMPDA 변수에 이 인덱스를 넣어 공통 출력 보간 코드를 실행한다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:N1-004 | OpenMP 행렬 작업 배열의 소유 | source-analysis/swan-data-structures-implementation.md:113 `each thread/invocation gets its own routine-local copy` | `src/swancom1.ftn:1175` `!$OMP+PRIVATE(SWMATR, LSWMAT, ALIMW, GROWW, IDCMIN, IDCMAX)`; `:3644` `CALL SOLPRE(AC2                ,SWMATR(1,1,JAOLD)  ,`. | B | 정렬 OpenMP 경로는 SWMATR를 PRIVATE으로 선언한다. 하위 루틴의 IMAT*는 이 작업 배열의 전달된 절편을 읽고 쓴다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:N1-014 | 해법의 공통 행렬 초기화라는 주장 | `source-analysis/swan-data-structures-implementation.md:111` `Solver routines explicitly zero all six arrays after use`는 | `src/swancom1.ftn:9441–9446`을 근거로 든다. `src/swancom1.ftn:8938`은 SWSOR 정의이며 `:9441–9446`은 IMATDA·IMATRA·IMATLA·IMATUA·IMAT5L·IMAT6U를 각각 0으로 둔다. 반면 SWSIP의 끝 `:8931–8932`는 `IMATDA = 0.` 및 `IMATRA = 0.`이다. 정렬 실제 호출은 `:3693` SWSIP, `:3709` SOLMT1, `:3726` SOLMAT 또는 `:3656–3678`의 직접 나눗셈이다. `SOURCE`의 `:7291–7294`와 `src/SwanTranspAc.ftn90:117–118`에서도 관련 행렬을 초기화한다. | B | SWSOR 끝의 여섯 배열 초기화를 모든 해법의 공통 후처리로 일반화하지 않는다. 실제 호출되는 SWSIP의 끝은 두 배열을 초기화한다. SOURCE의 정렬 분기와 SwanTranspAc의 행렬 준비도 각각 구별해서 설명한다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |

---
title: "swan command file reference"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-command-file-reference.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영."
last_source_check: 2026-10-13 (recovery 대조 반영)
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN command file (.swn) — commands, parsers, and cross-reference

## Scope note

Every SWAN run is driven by a **command file** (typically `INPUT` or `*.swn`), processed line-by-line by `swanpre1.ftn` and `swanpre2.ftn`. This note maps each top-level command to:
- **purpose** (one sentence),
- **reader subroutine** (`SWREAD`, `SWREOQ`, `SWREPS`, etc.),
- **file:line** of the parsing block,
- **required vs optional** (per a typical run),
- **key sub-keywords / arguments**,
- **manual cross-reference** (swanuse / swantech / online_doc).

Companion to `swan-foundation.md`. Where the foundation note covers *why*, this note covers *what* you write in the command file and *where* SWAN reads it.

## Source basis

- **Codex source scan** of `models/swan/source_code/swan/src/` (33 commands with file:line citations) — 2026-05-06.
- **RAG retrieval** against `manuals` collection filtered to `model=swan` (902 chunks: PDFs `swanuse/swantech/swanimp/swanpgr` + 195 online_doc HTML chapters).

## Command-file structure (typical order)

```
PROJECT 'name' 'nr'
'title1'
'title2'
'title3'
SET LEVEL 0.0 NAUT
MODE NONSTATIONARY TWODIMENSIONAL
COORDINATES SPHERICAL CCM

CGRID REGULAR ... CIRCLE 36 0.04 1.0
INPGRID BOTTOM ... 
READINP BOTTOM ... 'fname'
INPGRID WIND NONSTATIONARY ...
READINP WIND ... SERIES 'fname'

BOUND SHAPESPEC JONSWAP ... PEAK
BOUND SIDE W CONSTANT ... 
INITIAL DEFAULT

GEN3 WESTHUYSEN
WCAP KOMEN
QUADRUPL ...
BREAKING CONSTANT 1.0 0.73
FRICTION JONSWAP CONSTANT 0.038
TRIAD

NUMERICAL ACCUR 0.02 0.02 ... STAT 50
PROPAGATION SORDUP

POINTS 'STATIONS' FILE 'stations.txt'
BLOCK 'COMPGRID' NOHEAD 'fort.18' LAY 4 HSIGN PER DIR
TABLE 'STATIONS' HEADER 'fort.19' HSIGN PER

COMPUTE NONSTATIONARY 20070101.000000 30 MIN 20070103.000000

STOP
```

권고 순서와 선행 자료 의존성을 구분한다. BOUND SHAPE를 생략하면 기본 모양을 사용한다. 뒤에 BOUND SHAPE가 나왔다고 명령 파서 자체가 실패하지는 않는다. `src/swanmain.ftn:1039` `FSHAPE = 2`; `src/swanpre2.ftn:3654` `BSTMP%FSHAPE = FSHAPE`.

## Commands by group

### Group 1 — Setup

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `PROJECT` | Project id/number + 3 title lines | `SWREAD` | `[file=src/swanpre1.ftn line=523]` | optional | `'NAME' 'NR' TITLE1 TITLE2 TITLE3` | `[file=pdf:swan:swanuse]` ch.4 |
| `SET` | Global physical/numerical defaults | `SWREAD` | `[file=src/swanpre1.ftn line=2169]` | optional | `LEVEL`, `DEPMIN`, `MAXMES`, `GRAV`, `RHO`, `CDCAP`, `NAUT`/`CART`, `PWTAIL`, `EXCMARK`, `NSWEEP`, `CURV` | `[file=pdf:swan:swanuse]` |
| `MODE` | Stationary/nonstationary, 1D/2D | `SWREAD` | `[file=src/swanpre1.ftn line=738]` | optional | `STATIONARY`/`NONSTATIONARY`, `ONED`/`TWOD`, `NOUPDAT` | `[file=pdf:swan:swantech]` ch.3.1 |
| `COORDINATES` | Cartesian or spherical | `SWREAD` | `[file=src/swanpre1.ftn line=821]` | optional | `CART`, `SPHE [REARTH]`, projection `QC`/`CCM`, `REPEATING` | `[file=pdf:swan:swanuse]` |

### Group 2 — Grids and input data

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `CGRID` | Computational grid + spectral discretization | `SWREAD` | `[file=src/swanpre1.ftn line=1608]` | **yes** | `REG/CURV/UNSTRUC ...`, `EXC`, spectral `CIR/SEC [DIR1 DIR2] [MDC] [FLOW] [FHIGH] [MSC]` | `[file=website:swan:node11]` Computational grid |
| `INPGRID` | Define input field grid (BOT/CUR/WI/etc.) | `SWREAD` (calls `SINPGR`) | `[file=src/swanpre1.ftn line=1354]` | conditional | field selector `BOT/CUR/VX/VY/FR/WI/WX/WY/WLEV/ASTD/NPLA/TURB/MUDL/AICE/HICE/HSS/TSS/DSS`, grid `REG/CURV/UNSTRUC`, `NONSTAT` | `[file=website:swan:node26]` Input grids and data |
| `READINP` | Read input field data files | `SWREAD` (calls `SREDEP`/`SwanReadGrid`) | `[file=src/swanpre1.ftn line=1453]` | conditional | `UNSTRUC (ADC/TRIA/EASY 'FNAME')` or `[FAC] ('FNAME'/SERIES 'FNAME') [IDLA] FREE/FORMAT/UNFORMATTED` | `[file=website:swan:node26]` |

### Group 3 — Boundary and initial

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `BOUND` | Wave boundary conditions | `SWREAD`/`SWBOUN` | `[file=src/swanpre1.ftn line=1873]`, `[file=src/swanpre2.ftn line=2695]` (SWBOUN body) | conditional | `SHAP`, `JON/BIN/PM/GAUS/TMA`, `WAMN/WW3/NE`, `OPEN/CLOS`, segment/side specs | `[file=website:swan:node27]` Boundary and initial conditions; `[file=pdf:swan:swantech]` ch.4 page 125 |
| `INITIAL` | Initial wave state | `SWREAD`/`INITVA` | `[file=src/swanpre1.ftn line=1309]` | optional | `PAR ...`, `ZERO`, `HOTS/REST` (restart) | `[file=website:swan:node27]` |

### Group 4 — Physics activations

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `WIND` | Wind forcing/source coupling flags | `SWREAD` | `[file=src/swanpre1.ftn line=2773]` | optional | wind-source values paired with GEN choice | `[file=website:swan:node28]` Physics |
| `GEN1` | 1st-generation wind input | `SWREAD` | `[file=src/swanpre1.ftn line=2808]` | optional | `CF10..CFPM` parameters | `[file=pdf:swan:swantech]` ch.2.3 page 21 |
| `GEN2` | 2nd-generation wind input | `SWREAD` | `[file=src/swanpre1.ftn line=2843]` | optional | `CF10..CFPM` parameters | same |
| `GEN3` | 3rd-generation wind input family | `SWREAD` | `[file=src/swanpre1.ftn line=2904]` | optional | `JANS`, `YAN`, `WESTH`, `BAB`, `ST6`, `UP/DOWN`, `VECTAU/SCATAU`, `TRUE10/U10P`, `DRAG (WU/FIT/SWELL)`, `AGROW` | `[file=website:swan:node28]` Physics |
| `WCAP` | Whitecapping dissipation | `SWREAD` | `[file=src/swanpre1.ftn line=2459]` | optional | `KOM`, `JANS`, `LHIG`, `BJ`, `KBJ`, `AB [CDS2 BR] (CUR [CDS3])` | `[file=pdf:swan:swantech]` ch.2.3 |
| `QUADRUPL` | Nonlinear quadruplet (4-wave) | `SWREAD` | `[file=src/swanpre1.ftn line=3286]` | optional | `[IQUAD] [LAMBDA] [CNL4] [CSH1] [CSH2] [CSH3]` | `[file=pdf:swan:swantech]` ch.2.3 |
| `BREAKING` | Surf breaking | `SWREAD` | `[file=src/swanpre1.ftn line=2376]` | optional | `CON`, `VAR/NEL`, `RUE`, `TG`, `BKD`, `ASYM`, `DIR [SPREAD]`, `FREQD [POWER FMIN FMAX]` | `[file=pdf:swan:swantech]` ch.2.3.3 page 29 |
| `FRICTION` | Bottom friction | `SWREAD` | `[file=src/swanpre1.ftn line=2544]` | optional | `JON (CON/VAR)`, `COLL`, `MAD`, `RIP` with method coefficients | `[file=pdf:swan:swantech]` ch.2.3.3 |
| `TRIAD` | Nonlinear triad (3-wave) | `SWREAD` | `[file=src/swanpre1.ftn line=3337]` | optional | `LTA`, `DCTA`, `SPB`, `FTIM`, `COLL/NONC`, `BIPH (ELD/SAPR/WIT)`, `TRA/IC (FG/MS/BR/QU)` | `[file=pdf:swan:swantech]` ch.2.3 |
| `DIFFRACTION` | Diffraction approximation | `SWREAD` | `[file=src/swanpre1.ftn line=2114]` | optional | `[IDIFFR] [SMPAR] [SMNUM] [CGMOD]` | `[file=pdf:swan:swantech]` |

### Group 5 — Numerics

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `PROPAGATION` | Propagation sweep / scheme | `SWREAD` | `[file=src/swanpre1.ftn line=791]` | optional | `BSBT/BTBS`, `GSE [WAVEAGE]`, `FLUXLIM` | `[file=website:swan:node29]` Numerics |
| `NUMERICAL` | Solver stopping/scheme controls | `SWREAD` | `[file=src/swanpre1.ftn line=1939]` | optional | `STOPC/ACCUR ...`, `STAT/NONST`, `DIRIMPL ... DEP/WNUM`, `REFRLIM`, `SIGIMPL/SIGEXPL/FIL`, `CTHETA`, `CSIGMA`, `SETUP` | `[file=website:swan:node29]` |
| `COMPUTE` | Run computation | `SWREAD` | `[file=src/swanpre1.ftn line=875]` | **yes** | `STAT [TIME]` or `[TBEGC] [DELTC] [TENDC]` time unit | `[file=website:swan:node34]` Lock-up |

### Group 6 — Output point/frame definitions

These define **where** outputs are computed but don't write anything by themselves. Output writing requires `BLOCK`, `TABLE`, `SPECOUT`, `NESTOUT` (Group 7) referring to a name defined here.

| Command | Purpose | Reader | file:line | Req? | Key args |
|---------|---------|--------|-----------|------|----------|
| `POINTS` | Named point set | `SWREPS` | `[file=src/swanpre2.ftn line=536]` | optional | `'SNAME'`, repeated `[XP YP]` or `FILE 'FNAME'` |
| `FRAME` | Named rectangular grid | `SWREPS` | `[file=src/swanpre2.ftn line=323]` | optional | `'SNAME' [XPFR YPFR ALPFR XLENFR YLENFR MXFR MYFR]` |
| `GROUP` | Named subgrid (computational index range) | `SWREPS` | `[file=src/swanpre2.ftn line=372]` | optional | `'SNAME' SUBGRID [IX1 IX2 IY1 IY2]` |
| `RAY` | Named ray set | `SWREPS` | `[file=src/swanpre2.ftn line=609]` | optional | `'RNAME' [XP1 YP1 XQ1 YQ1]` with repeated `[INT XP YP XQ YQ]` |
| `ISOLINE` | Isoline points on a ray | `SWREPS` | `[file=src/swanpre2.ftn line=694]` | optional | `'SNAME' 'RNAME' DEPTH/BOTTOM [DEP]` |
| `CURVE` | Polyline output set | `SWREPS` | `[file=src/swanpre2.ftn line=462]` | optional | `'SNAME' [XP1 YP1]` then `[INT XP YP]` |
| `NGRID` | Nested output grid | `SWREPS` | `[file=src/swanpre2.ftn line=794]` | optional | `'SNAME'` + structured `[XPN YPN ALPN XLENN YLENN MXN MYN]` or `UNSTRUC (TRIA/EASY 'FNAME')` |

### Group 7 — Output writers

These reference a name from Group 6 (or use `'COMPGRID'` for the full computational grid) and produce files.

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `BLOCK` | Block/grid output | `SWREOQ` | `[file=src/swanpre2.ftn line=1171]` | optional | `'SNAME'`, `HEADER/NOHEAD`, `'FNAME'`, `LAYOUT [IDLA]`, var list via `SVARTP`, `OUTPUT [TBEG] [DELT]` | `[file=website:swan:node12]` |
| `TABLE` | Tabular output at points | `SWREOQ` | `[file=src/swanpre2.ftn line=1577]` | optional | `'SNAME'`, `HEADER/NOHEADER/INDEXED/SWAN/STAB`, `'FNAME'`, var list, `UNIT`, `OUTPUT [TBEG] [DELT]` | `[file=website:swan:node12]` |
| `SPECOUT` | Spectral output | `SWREOQ` | `[file=src/swanpre2.ftn line=1873]` | optional | `'SNAME'`, `SPEC1D/SPEC2D`, `ABS/REL`, `S/L`, `'FNAME'`, `OUTPUT [TBEG] [DELT]` | `[file=website:swan:node12]` |
| `NESTOUT` | Nesting boundary spectra | `SWREOQ` | `[file=src/swanpre2.ftn line=1984]` | optional | `'SNAME'`, `'FNAME'`, `OUTPUT [TBEG] [DELT]` | `[file=website:swan:node27]` |

### Group 8 — Control

| Command | Purpose | Reader | file:line |
|---------|---------|--------|-----------|
| `STOP` | End command processing | `SWREAD` | `[file=src/swanpre1.ftn line=497]` |
| `$` | Comment to end-of-line | scanner (`INKEYW` path) | (handled by lexer, not a command block) |

## Connectivity / dependency graph

```
                ┌─── PROJECT / SET / MODE / COORD ──┐
                │                                   │
                ▼                                   │
              CGRID  ─── defines computational grid + spectral grid
                │
                ▼
       INPGRID + READINP  ─── for each input field (BOT, WIND, CUR, AICE, HICE, ...)
                │
                ▼
         BOUND / INITIAL  ─── boundary spectra + initial state
                │
                ▼
    GEN1/2/3 + WCAP + QUADRUPL + BREAKING + FRICTION + TRIAD + DIFFRACTION
                │   ─── physical source/sink term selectors
                ▼
       PROPAGATION + NUMERICAL  ─── numerical scheme + stopping
                │
                ▼
      POINTS/FRAME/GROUP/RAY/ISOLINE/CURVE/NGRID  ─── output locations
                │
                ▼
       BLOCK/TABLE/SPECOUT/NESTOUT  ─── output writers
                │
                ▼
              COMPUTE  ─── start the run
                │
                ▼
              STOP
```

Critical orderings:
- `CGRID` must be **before** `INPGRID/READINP/BOUND/INITIAL` (the spatial domain is defined there).
- Physics/numerics commands can appear in any order between setup and `COMPUTE`.
- Output writers require their named target (`POINTS`, `FRAME`, etc.) to be defined earlier in the file.
- A single `.swn` file can contain multiple `COMPUTE` blocks (e.g., stationary then nonstationary or successive time windows) — physics commands between them re-modify the run.

## Decision Guide

| Run type | Required commands | Optional but typical |
|----------|-------------------|----------------------|
| Stationary 2D wave hindcast | PROJECT, MODE STAT, CGRID, INPGRID/READINP BOT, INPGRID/READINP WIND, BOUND, GEN3, NUMERICAL ACCUR, COMPUTE STAT, STOP | WCAP, BREAKING, FRICTION, BLOCK, TABLE |
| Nonstationary storm passage | + MODE NONSTAT, INPGRID WIND NONSTAT, COMPUTE NONSTAT | + INITIAL HOTS for restart, NESTOUT for downstream nesting |
| Nesting from coarse run | (in coarse run) NGRID + NESTOUT | 받는 실행은 `BOUNDNEST1 NEST 'fname'`을 쓴다. `src/swanpre2.ftn:2971` `CALL INCSTR ('FNAME',FILENM,'REQ', ' ')`. |
| 천수 변형이 있는 쇄파대 | 삼파는 TRIAD DCTA·LTA·FTIM·SPB 중 하나로 지정한다. 쇄파 명령은 BREAKING이다. 근거: swanuse PDF 73·75쪽 / 인쇄 65·67쪽. | — | [10-13 전수 검증 정정]

## Working Rules

1. **`SET PWTAIL` matters for stationary convergence** — too steep tail underestimates whitecapping, may prevent convergence.
2. **`NUMERICAL STOPC ...` is the convergence gate for stationary** — default tolerances are loose; tighten for high-quality validation.
3. **`COMPGRID` is a built-in name** for the computational grid — you don't need to define it via `FRAME`/`POINTS`.
4. 주파수와 방향의 스펙트럼 격자는 CGRID에서 지정한다. SET FREQ·SET DIR·SET TIMEFORMAT은 지원하는 명령문이 아니다. `src/swanpre1.ftn:1730` `CALL ININTG('MDC',MDC,'RQI',0)`; `src/swanpre1.ftn:1739` `CALL INREAL('FLOW',FRLOW,'STA',-999.)`; `src/swanpre1.ftn:1740` `CALL INREAL('FHIGH',FRHIG,'STA',-999.)`.
5. ST6는 GEN3 ST6로 지정한다. XNL은 QUADRUPL 51·52·53으로 지정한다. Multiple DIA는 QUADRUPL 4와 별도 MDIA 명령으로 지정한다. `2980d1a:src/swanpre1.ftn:2936` `ELSE IF (KEYWIS('ST6')) THEN`; `43e9bbb:src/swanpre1.ftn:2983` `ELSE IF (KEYWIS('ST6')) THEN`.
6. **Multiple `INPGRID WIND` blocks override each other** — keep one canonical wind input per run.

## Common Pitfalls

- **`CGRID` after `INPGRID`** → SWAN doesn't know the domain when reading inputs. Always order `CGRID` first.
- **`READINP` without preceding `INPGRID`** → "input grid not yet defined" error. Pair them.
- **Mixing structured and unstructured** in the same `INPGRID/READINP` block → fails. Each input field must match the type declared in its `INPGRID`.
- NSTATM≤0이면 COMPUTE의 정상 분기로 간다. 비정상 모드에서는 COMPUTE STAT으로 특정 시각의 정상 계산을 요청할 수 있다. MODE의 모순된 재지정에는 오류가 있다. `src/swanpre1.ftn:879` `IF (NSTATM.LE.0 .OR. KEYWIS('STAT')) THEN`; `src/swanpre1.ftn:881` `IF (NSTATM.GT.0) CALL INCTIM (ITMOPT,'TIME',TINIC,'REQ',0D0)`. MODE 재지정 검사는 `src/swanpre1.ftn:741–751`에 있다. [10-13 전수 검증 보완]
- HOTSTART 시각보다 이전인 시작 시각에는 오류를 내고 현재 시각으로 되돌린다. `src/swanpre1.ftn:899` `IF (TINIC .LT. TIMCO) THEN`. 오류 메시지와 `TINIC = TIMCO` 대입은 `src/swanpre1.ftn:900–901`에 있다. [10-13 전수 검증 보완]
- **`SET LEVEL` left at 0** when modeling a tide-influenced domain — wave-current interaction wrong.
- 현재 JONSWAP CONSTANT 기본값은 0.038 m²/s³다. JONSWAP VARIABLE은 방향 퍼짐에 따라 계수를 정한다. 공간 입력장은 별도 INPGRID FRICTION·READINP FRICTION 경로다. `src/swanmain.ftn:1396` `PBOT(3)   = 0.038`.
- **Output before `COMPUTE`** → the `BLOCK/TABLE/SPECOUT/NESTOUT` records the run state; if placed before `COMPUTE`, you get an empty file. Put output commands BEFORE `COMPUTE` (they're declarative; they fire during/after `COMPUTE`).

## Next expansion

- Per-command complete syntax reference (full BNF for each — currently this note treats sub-keywords at summary level).
- ADCIRC-SWAN unstructured coupling — separate note covering how `BOUND` and `READINP UNSTRUC` interact with the coupled model.
- SWAN command file templates per use case (storm hindcast, swell propagation, surf-zone, ice-covered) — separate `protocols/` notes.
- Comparative reference: SWAN command vs WAVEWATCH III input vs Delft3D-WAVE namelist.

## References

### Source code (Codex scan, 2026-05-06)

- `src/swanpre1.ftn` — main `SWREAD` body, parses Group 1–5 commands.
- `src/swanpre2.ftn` — `SWREOQ` / `SWREPS` for Groups 6–7; `SWBOUN` body for `BOUND` details.
- Full subroutine inventory: `[file=models/swan/manuals/refs/subroutines.md]`.

### Manuals (curated, retrieved 2026-05-06 against `manuals` collection, model=swan)

- `[file=pdf:swan:swanuse]` — User Manual (canonical command reference).
- `[file=pdf:swan:swantech]` — Technical Doc (governing equations, source-term formulations).
- `[file=pdf:swan:swanimp]` — Implementation Manual.
- `[file=pdf:swan:swanpgr]` — Programmer Manual.
- `[file=website:swan:node11]` — Computational grid.
- `[file=website:swan:node12]` — Output grids.
- `[file=website:swan:node13]` — Activation of physical processes (per-process flag matrix).
- `[file=website:swan:node26]` — Input grids and data.
- `[file=website:swan:node27]` — Boundary and initial conditions.
- `[file=website:swan:node28]` — Physics.
- `[file=website:swan:node29]` — Numerics.
- `[file=website:swan:node34]` — Lock-up (stationary convergence).

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 (this session) |
| Generated | 2026-05-06 |
| Source-scan tool | `codex exec --model gpt-5.3-codex` over `models/swan/source_code/swan/src/` |
| RAG retrieval | rag_proxy on `manuals` filtered `model=swan` (902 chunks across pdf+website doc_types) |
| Coverage | 33 top-level commands; sub-keywords at summary level (full BNF deferred to per-command notes) |
| Review status | 2026-10-13 recovery 대조 보고서 R4·R5의 명령 수정안을 반영했다. |
| Companion notes | `swan-foundation.md`, `swan/manuals/refs/subroutines.md` |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

빈 인용 칸은 `—`로 표시한다. 표의 절 번호는 각 행이 링크한 대조 보고서의 절 번호다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R4:T1-037 | 파일 이름 길이 | swanuse PDF 29쪽 / 인쇄 21쪽: “SWAN does not permit file names longer than 36 characters.” swanuse PDF 34쪽 / 인쇄 26쪽: “The maximum length of the file names is 36 characters.” | `src/swmod1.ftn:232` `PARAMETER (LENFNM=140)`; `src/swmod1.ftn:259` `CHARACTER (LEN=LENFNM) :: FILEA , FILEB , FILENM`; `src/ocpcre.ftn:967` `IF (LENCST.GT.LENW) THEN` | B 문서 오기 | 일반 파일 이름 버퍼는 140자이다. 개별 읽기의 더 짧은 제한은 따로 적는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-038 | unit 상한 | swanuse PDF 34쪽 / 인쇄 26쪽: “The maximum number of file names is 99.” “edit the file swaninit to change highest unit number of 99 to a higher number”. swanimp PDF 27 / 인쇄 21 및 웹 `swanimp/node19.html:67`의 swaninit 예시는 `99999`를 highest file ref. number로 제시한다. | `src/ocpids.ftn:190` `IUNMAX = 99999` | B 문서 오기 | 기본 Unix의 unit 상한은 99999이다. 사용자 매뉴얼의 99 표기는 구현 매뉴얼의 예시와도 다르다. 파일 개수 99라는 제한으로 해석하지 않는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-220 | INCLUDE 명령 | — | `src/swanpre1.ftn:543` `IF (KEYWIS ('INCL')) THEN`; `src/swanpre1.ftn:545` `CALL INCSTR ('FILE' , FILENM , 'REQ', ' ')`; `src/swanpre1.ftn:547` `IF (INCLEV.GT.MXINCL) THEN`; `src/swanpre1.ftn:548` `CALL MSGERR (4, 'too many INCLUDE levels')`; `src/swanpre1.ftn:553` `INPUTF = INCNUM(INCLEV)`; `src/swanpre1.ftn:476` `INPUTF = INCNUM(INCLEV)` | C 문서 누락 | INCLUDE는 다른 명령 파일을 읽고 EOF에서 이전 파일로 복귀한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-221 | POOL 호환 처리 | — | `src/swanpre1.ftn:563` `IF (KEYWIS ('POOL')) THEN`; `src/swanpre1.ftn:564` `CALL MSGERR(1,'Keyword POOL is not relevant anymore!')`; `src/swanpre1.ftn:565` `GOTO 100` | C 문서 누락 | POOL은 경고 후 무시한다. 메모리 크기 설정으로 사용하지 않는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-222 | INTEST | — | `src/swanpre1.ftn:629` `CALL ININTG ('INTES' , INTES , 'STA', 30)`; `src/swanmain.ftn:1615` `INTES  = 0`; `src/swanpre1.ftn:4077` `IF (ITEST .GE. 50 .OR. INTES .GE. 5) THEN` | C 문서 누락 | INTEST 명령의 값 생략 기본값은 30이다. 실행 초기값은 0이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-223 | COTEST | — | `src/swanpre1.ftn:641` `CALL ININTG ('COTES' , ICOTES , 'STA', 30)`; `src/swanmain.ftn:1616` `ICOTES = 0`; `src/swanmain.ftn:613` `IF (ICOTES .GT. ITEST) ITEST = ICOTES` | C 문서 누락 | COTEST는 계산 단계의 진단 수준을 설정한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-224 | OUTEST | — | `src/swanpre1.ftn:656` `CALL ININTG ('ITEST' , IOUTES , 'STA', 30)`; `src/swanmain.ftn:1617` `IOUTES = 0`; `src/swanmain.ftn:668` `IF (IOUTES .GT. ITEST) ITEST = IOUTES` | C 문서 누락 | OUTEST가 읽는 변수 이름은 ITEST이다. 출력 단계의 진단 수준을 설정한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-227 | GRID 별칭 | — | `src/swanpre1.ftn:1608` `IF (KEYWIS('CGRID') .OR. KEYWIS('GRID')) THEN` | C 문서 누락 | GRID는 CGRID와 같은 최상위 명령 경로로 간다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-228 | INP GRID·입력장 생략 | — | `src/swanpre1.ftn:1354` `IF (KEYWIS ('INP')) THEN`; `src/swanpre1.ftn:1355` `CALL IGNORE ('GRID')`; `src/swanpre1.ftn:1425` `IGRD = 1`; `src/swanpre1.ftn:1426` `PSNAME = 'BOTTGRID'` | C 문서 누락 | 분리된 INP GRID를 허용한다. 입력장 선택을 생략하면 BOTTOM으로 간다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-232 | BOUND 호환 토큰 | — | `src/swanpre2.ftn:3054` `IF (KEYWIS ('STAT')) THEN`; `src/swanpre2.ftn:3055` `CALL MSGERR (1, 'keyword STAT ignored')`; `src/swanpre2.ftn:3066` `IF (KEYWIS('XY') .OR. KEYWIS ('LOC')) THEN`; `src/swanpre2.ftn:3068` `ELSE IF (KEYWIS('IJ') .OR. KEYWIS ('GRI')) THEN`; `src/swanpre2.ftn:3618` `IF (KEYWIS('UNIF') .OR. KEYWIS('CON') .OR. KEYWIS('PAR')) THEN`; `src/swanpre2.ftn:3666` `ELSE IF (KEYWIS('FILE') .OR. KEYWIS('SPEC')) THEN` | C 문서 누락 | STAT는 무시한다. LOC·GRI·SPEC 별칭과 CONSTANT를 생략한 PAR를 수용한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-233 | INITIAL 호환 토큰 | — | `src/swanpre1.ftn:6166` `CALL IGNORE ('COND')`; `src/swanpre1.ftn:6260` `ELSE IF (KEYWIS('HOTS') .OR. KEYWIS('REST')) THEN`; `src/swanpre1.ftn:6295` `IF (KEYWIS ('UNF') .OR. KEYWIS('BIN')) THEN` | C 문서 누락 | INITIAL 안에서는 COND를 무시한다. REST·BIN은 각각 HOTSTART·UNFORMATTED의 별칭이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-234 | 명령 숫자 반복·문자열 이스케이프 | — | `src/ocpcre.ftn:1784` `IF (ELTYPE.EQ.'INT' .AND. ELINT.GT.0) THEN`; `src/ocpcre.ftn:1785` `NREP = ELINT`; `src/ocpcre.ftn:1818` `IF (KAR.NE.QUOTE) GOTO 88`; `src/ocpcre.ftn:1819` `!         double quote is read as a single quote; continue` | C 문서 누락 | 명령 숫자에 양의 정수 반복 계수를 쓸 수 있다. 문자열 안의 연속 작은따옴표는 작은따옴표 하나로 읽는다. C 판정은 명령 파일의 문법 설명에 한정한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-300 | 노트의 SET FREQ·DIR·TIMEFORMAT | `source-analysis/swan-command-file-reference.md:205–206`의 SET FREQ·DIR·TIMEFORMAT 안내. | `2980d1a:src/swanpre1.ftn:2123–2166`과 `src/swanpre1.ftn:2169–2213`의 SET 분기에는 FREQ·DIR·TIMEFORMAT 선택이 없다. `src/swanpre1.ftn:1730` `CALL ININTG('MDC',MDC,'RQI',0)`; `src/swanpre1.ftn:1739` `CALL INREAL('FLOW',FRLOW,'STA',-999.)`; `src/swanpre1.ftn:1740` `CALL INREAL('FHIGH',FRHIG,'STA',-999.)` | D 문서에만 있음 | SET FREQ·SET DIR·SET TIMEFORMAT은 지원하는 명령문이 아니다. 주파수와 방향의 스펙트럼 격자는 CGRID에서 지정한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) | [10-13 전수 검증 정정]
| R4:T1-302 | 명령 순서의 일괄 고정 | `source-analysis/swan-boundary-implementation.md:211`의 `Reverse breaks the parser.` | `src/swanmain.ftn:1039` `FSHAPE = 2` | B 문서 오기 | 권고 순서와 선행 자료 의존성을 구분한다. BOUND SHAPE 생략 자체가 파서 실패 조건은 아니다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-304 | BOUNDNEST의 문자열 수 | `source-analysis/swan-command-file-reference.md:197`의 `BOUND NEST 'sname' 'fname'` | `src/swanpre2.ftn:2971` `CALL INCSTR ('FNAME',FILENM,'REQ', ' ')` | B 문서 오기 | 받는 실행의 BOUNDNEST1 NEST는 fname 하나를 읽는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R5:PN-154 | 별칭 | — | `src/swanpre1.ftn:793` `IF (KEYWIS ('BSBT') .OR. KEYWIS ('BTBS')) THEN`; `src/swanpre1.ftn:1000` `IF (KEYWIS ('TRANS1') .OR. KEYWIS ('TRFREQ')) THEN`; `src/swanpre1.ftn:1121` `IF (KEYWIS ('FIG') .OR. KEYWIS ('IG')) THEN`; `src/swanpre1.ftn:1325–1326` `IF (KEYWIS('REST') .OR. KEYWIS ('BACK') .OR. KEYWIS('HOTF')`; `src/swanpre1.ftn:2023` `IF (KEYWIS('SIGIM') .OR. KEYWIS ('IMP')) THEN`; `src/swanpre1.ftn:2032` `ELSE IF (KEYWIS('SIGEX') .OR. KEYWIS('EXP')) THEN`; `src/swanpre1.ftn:2382` `ELSE IF (KEYWIS('VAR') .OR. KEYWIS('NEL')) THEN`; `src/swanpre1.ftn:3337` `IF ( KEYWIS ('TRI') .OR. KEYWIS ('NL3') ) THEN`; `src/swanpre1.ftn:3462` `IF (KEYWIS('TRA') .OR. KEYWIS('IC')) THEN`; `src/swanpre1.ftn:3589` `IF ( KEYWIS('SCAT') .OR. KEYWIS('QC') ) THEN`; `src/swanpre1.ftn:3594` `IF ( KEYWIS('K') .OR. KEYWIS('WNUM') ) THEN`; `src/swanpre1.ftn:6744` `IF (KEYWIS ('UNF') .OR. KEYWIS('BIN')) THEN` | C 문서 누락 | 입력기는 §3.2에 열거한 별칭을 같은 처리 분기로 보낸다. 네 매뉴얼과 웹 문서의 검색에서 지원 문법 설명이 없는 별칭은 권장 문법과 구분한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-176 | 지원하지 않는 노트 문법 | `source-analysis/swan-st6-babanin-implementation.md:117`의 `pair with`와 `WCAP ST6`; 124행의 `without`와 `WCAP ST6`. `source-analysis/swan-whitecapping.md:190`의 `GEN3 ST6 BABANIN`, 204행의 `WAVE_BREAKING`. `source-analysis/swan-command-file-reference.md:198`의 `TRIAD ON`, 206행의 `SET TIMEFORMAT`. `source-analysis/swan-time-stepping-implementation.md:138`의 `SET TIMINC`. `manual-notes/swan-tech-ch2-sources-sinks.md:190`의 `QUADRUPL XNL`, 193행의 `QUADRUPL MDIA 6`. | `2980d1a:src/swanpre1.ftn:2936` `ELSE IF (KEYWIS('ST6')) THEN`; `43e9bbb:src/swanpre1.ftn:2983` `ELSE IF (KEYWIS('ST6')) THEN` | D 문서에만 있음 | WCAP ST6·WAVE_BREAKING·TRIAD ON·SET TIMEFORMAT·SET TIMINC·GEN3 ST6 BABANIN·QUADRUPL XNL·QUADRUPL MDIA는 지원 명령문으로 쓰지 않는다. ST6는 GEN3 ST6, 쇄파는 BREAKING, 삼파는 TRIAD DCTA·LTA·FTIM·SPB로 지정한다. XNL은 QUADRUPL 51·52·53, Multiple DIA는 QUADRUPL 4와 별도 MDIA를 사용한다. `2980d1a`(41.45)부터 `43e9bbb`까지 해당 문자열의 이력 검색은 0커밋이며 두 판의 ST6 입력 분기도 GEN3 아래에 있다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |

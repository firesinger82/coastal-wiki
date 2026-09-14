---
title: "adcirc tide forcing implementation"
topic: tides
canonical_source: self
citation_status: verified
has_source_needed: true
source_correction_date: 2026-09-14
source_correction_by: "Codex — scoped source cross-reference"
source_correction_human_approval: not-issued
source_correction_review: "Claude Fable 5.1 — NBFR/첨자/노드/위상/시간/ETRF 변경 원문 대조; 과학적 사람 승인 아님"
source_correction_scope: "NBFR 입력 레코드/첨자와 경계 노드 순서·위상/시간 기준, 전통 분조 경로 ETRF 항. 전체 노트 재검증·실제 실행·수치/물리 검증 아님."
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-tide-forcing-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-09-14: NBFR 입력·노드/분조 순서·위상/시간·ETRF 항의 한정 대조, 본문 한정 대조 범위 참조. 실제 실행·수치/물리 검증 미수행."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC tide forcing — NTIP, fort.15 NBFR, fort.24 SAL


## 2026-09-14 한정 대조 범위

이 보강의 코드 판본은 ADCIRC `6037225ce4573efd3c1f8877a5dc908d01c199a8`이다. 아래 `src/` 인용의 루트는 `models/ADCIRC/raw/source_code/adcirc/`다. **문서 지원·코드 구현** 중 NBFR 입력, 경계 노드 전달, 위상/시간 기준, 전통 분조 경로의 ETRF 항을 대조했다. **실행 확인·수치 검증·물리 검증·개별 입력자료 품질 확인은 수행하지 않았다.** 다른 절과 외부 DB 규약은 이번 검증 범위에 포함하지 않는다. 과거 검증 이력과 이번 정정을 구분하며 이번 정정에 대한 사람 승인은 발급하지 않았다.

## Scope

How tidal forcing enters ADCIRC: `NTIP` for tidal potential (`fort.15`), open-boundary harmonic constituents (`NBFR/EMO/EFA`), `fort.24` self-attraction & loading (SAL). External tide databases like FES2022b/NAO99jb provide the boundary amplitudes/phases that ADCIRC consumes.

## A. NTIP flag

- `NTIP` parsed at `[file=src/read_input.F line=1705-1731]`:
  - `NTIP=0`: tidal potential disabled
  - `NTIP=1`: tidal potential enabled (`CTIP=.TRUE.`)
  - `NTIP=2`: + self-attraction/load tide (SAL)
- SAL data (`SALTAMP/SALTPHA`) only read when `NTIP=2` at `[file=src/read_input.F line=6282-6463]`; otherwise zeroed
- Runtime: `applyTidePotentialForcing` applies tidal potential when `CTIP=true`; SAL added to `TIP2` when `NTIP=2` at `[file=src/timestep.F line=1517-1560]`

## B. Open boundary tide elevations (`fort.15` NBFR block)

- `NBFR` (number of forcing frequencies on open boundaries) parsed at `[file=src/read_input.F line=3410-3436]`
- Per-constituent: frequency `AMIG`, nodal factor `FF`, equilibrium argument `FACE`, plus tag
- Per-frequency per-boundary-node:
  - Amplitude `EMO(I,J)` and phase `EFA(I,J)` at `[file=src/read_input.F line=3450-3456]`, `[file=src/global.F line=387, 1045]`
  - **Note: this codebase uses `EMO/EFA`, not `BCRFA/BCRFP`** (other docs / forks may differ)

### fort.15 NBFR block format
```
NBFR
[for each constituent:]
  BOUNTAG
  AMIG  FF  FACE
[for each constituent:]
  ELEVALPHA
  [for each NETA boundary node:]
    EMO  EFA   ! phase in degrees, converted to rad on read
```
At `[file=src/read_input.F line=3431-3456, 3485-3497]`.

위 블록은 반복 순서를 설명한 도식이다. 첫 첨자는 분조, 둘째는 경계 노드이며, 분조 헤더 묶음 뒤에 별도의 선택 입력 줄을 추가하지 않는다. 공식 [fort.15 형식](https://adcirc.github.io/adcirc/technical_reference/input_files/fort15.html)의 `ALPHAE`가 이 로컬 구현에서는 `ELEVALPHA`다. 각 분조의 값은 `mesh.F:1822–1834`가 `NBDV`에서 구성하는 `NBD` 순서로 대응하며 `read_input.F:3493–3496`에 노드 번호와 함께 기록된다. 실제 수위 적용은 `gwce.F:1644–1649`에서 `EMO(J,I)*FF(J)*RampElev*cos(ARG)`를 `Eta2(NBD(I))`에 더한다.

### Per-timestep synthesis

```fortran
Eta2(NBDI) += EMO * FF * RampElev * cos(AMIG*timeh + FACE - EFA)
```
at `[file=src/gwce.F line=1638-1650]`.

## C. Tide databases (FES2022b, NAO99jb) — ADCIRC consumption

- `[file=src/read_input.F line=3450-3456, 3410-3436]` — ADCIRC reads pre-computed amplitudes/phases at open boundary nodes from `fort.15` block
- **No FES2022b/NAO99jb parser in core source**
- External preprocessing (Python/MATLAB tools) must:
  1. Take database (NetCDF or text)
  2. Interpolate to ADCIRC open boundary nodes
  3. Output amplitudes/phases per constituent in fort.15 NBFR format

So the choice "FES2022b vs NAO99jb" is upstream of ADCIRC — once written into fort.15 the runtime code is identical.

## D. fort.24 (SAL self-attraction loading)

- Reader: `readSelfAttractionAndLoadingFile` at `[file=src/read_input.F line=6282-6463]`
- Reads `fort.24.nc` (NetCDF) or ASCII `fort.24` into `SALTAMP/SALTPHA`
- Phase converted to radians on read

### ASCII fort.24 format
Per constituent:
- Header line
- Constituent name (matched to `TIPOTAG`)
- Per-node: `node_id  amplitude  phase`

At `[file=src/read_input.F line=6429-6455]`.

### Application

SAL adds to effective tide potential:
```
TIP2 += SALTMUL * SALTAMP * cos(ARGT - SALTPHA)
```
at `[file=src/hstart.F line=1529-1532]`, `[file=src/timestep.F line=1547-1555]`.

## E. Tidal potential (NTIP=1)

- Computed in `applyTidePotentialForcing` (or `tidePotential%compute` for full TIP) at `[file=src/timestep.F line=1507-1562]`
- Stored in `TIP2`
- Constituents (M2/S2/K1/O1/etc.) are user-defined via `TIPOTAG` block at `[file=src/read_input.F line=3347-3354]`:
  - `TPK` — tidal potential coefficient
  - `AMIGT` — frequency
  - `ETRF` — Earth-tide reduction factor
  - `FFT` — nodal factor
  - `FACET` — equilibrium argument

So no hardcoded constituents — user decides which to include.

### ETRF (Earth tide reduction factor)

Multiplies `TPK` term at `[file=src/timestep.F line=1501-1503, 1536]`. Standard values 0.69 (M2/S2/N2), 0.736 (K1/O1). ⚠ source-needed(0.69/0.736 표준값의 문헌 출처 미인용).

### Earth potential vs ocean load (SAL)

- Earth tide → `ETRF * TPK` term in `TIP2`
- Ocean load → SAL term (separate, only with NTIP=2)
- Both summed into `TIP2` for the GWCE forcing

## F. Equilibrium tide formula

- Latitude dependence in `L_N` at `[file=src/adcirc.F line=301-307]`:
  - Long-period: `1.5*cos²(φ) - 1`
  - Diurnal: `sin(2φ)`
  - Semidiurnal: `cos²(φ)`
- Species class `NA = 0,1,2` chosen from frequency `AMIGT`, selects `L_N(NA, node)` in potential summation at `[file=src/timestep.F line=1541-1555]`, `[file=src/hstart.F line=1525-1532]`
- Full TIP path uses explicit lunar-solar geometry (P2/P3 terms) at `[file=src/tidalpotential.F90 line=262-279, 289-296]` with precomputed trig fields `m_CSFEA`, `m_S2SFEA`

## G. Nodal corrections + REFTIM

- For tidal potential: nodal factor = `FFT`, argument `(V0+u)` = `FACET` (degrees → radians on read) at `[file=src/read_input.F line=3349, 3371-3383]`
- For open boundary: nodal factor `FF`, equilibrium arg `FACE`, phase lag `EFA`; applied in timestep boundary synthesis at `[file=src/read_input.F line=3433, 3429-3436]`, `[file=src/gwce.F line=1644-1649]`
- `REFTIM` shifts harmonic time base: `TimeH = IT*DTDP + (STATIM - REFTIM)*86400` at `[file=src/timestep.F line=251-259]`, `[file=src/read_input.F line=2541]`
- So `(V0+u)` references are relative to the specified harmonic reference epoch

## Decision Guide — tide forcing 진단

| Issue | Investigation |
|-------|---------------|
| Boundary amplitudes wrong by constant factor | Wrong unit (cm vs m), check fort.15 EMO values |
| Phase off by 90° or 180° | EFA degree/radian conversion or REFTIM mismatch |
| FES2022b vs NAO99jb question | Both produce fort.15 EMO/EFA; choose based on regional accuracy |
| SAL not having effect | NTIP=2 + valid fort.24 + matching `TIPOTAG` constituent names |
| Long-period (Mf, Mm) wrong | NTIP=1 with `TIPOTAG` block missing those constituents |

## Working Rules

1. **`fort.15` NBFR block must match exactly** the constituents in your boundary-extraction tool. NBFR=8 means 8 frequency lines + 8 ELEVALPHA blocks.
2. **Phase in fort.15 is degrees** (converted to radians on read). Don't write radians.
3. **NTIP=2 requires fort.24** with constituent names matching `TIPOTAG`.
4. **`REFTIM` should match boundary forcing reference epoch** — typical is `STATIM=REFTIM=0` or both at simulation start time.
5. **`ETRF(J)=0` makes that constituent’s ETRF-dependent potential coefficient zero in the traditional constituent branch.** Under `CTIP` and `.not.tidePotential%active()`, `TPMUL=RampTip*ETRF(J)*TPK(J)*FFT(J)` multiplies the potential term added to `TIP2` (`src/timestep.F:1517–1556`). This does not mean applying an unreduced full potential. `SALTMUL` is separate; open-boundary `EMO/EFA` synthesis is also separate (`src/gwce.F:1638–1650`). The full-formula `tidePotential%compute` path is a different branch (`src/timestep.F:1520–1521`); its internals are outside this correction.

## Common Pitfalls

- **Using NAO99jb amplitudes with FES2022b phases** — common cross-mix mistake; phases are referenced to different conventions.
- **Wrong NETA in NBFR block** — number of boundary nodes must match fort.14 open boundary listing.
- **Missing `ELEVALPHA` line** between constituents — parser desync, all subsequent boundary amplitudes garbage.
- **NTIP=2 fort.24 with extra constituent** not in `TIPOTAG` — silently dropped, no error.

## References

- `src/read_input.F` — `NTIP` parser, NBFR block reader, `fort.24` SAL reader.
- `src/gwce.F` — boundary synthesis applies harmonic forcing each timestep.
- `src/timestep.F` — `applyTidePotentialForcing`, SAL summation.
- `src/tidalpotential.F90` — full TIP lunar-solar geometry.
- `src/hstart.F` / `src/cstart.F` — SAL initialization for hot/cold restart.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 50+ file:line citations |
| Coverage | NTIP, NBFR fort.15 block, fort.24 SAL, tidal potential, equilibrium formula, REFTIM |
| Review status | `review_required: true` |

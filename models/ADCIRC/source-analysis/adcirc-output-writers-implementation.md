---
title: "adcirc output writers implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-output-writers-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC output writers — fort.6X/7X, harmonic, max-value, NetCDF

## Scope

How ADCIRC writes time-stamped output (fort.61/62/63/64), met output (fort.71-74), harmonic analysis (fort.51-53), 3D station output (fort.41-42), and max-value outputs (maxele/maxvel). Format selection (ASCII vs NetCDF), spool counters, and parallel post-merge.

## A. fort.61/63 (elevation)

- Time-spooling logic: `writeOutput2D` at `[file=src/write_output.F line=1773]` increments per-descriptor spool counter inside time window; writes when `spoolCounter == outputTimeStepIncrement`
- fort.61 stride: `NSPOOLE` at `[file=src/write_output.F line=523, 1811-1823]`
- `initOutput2D` binds fort.61 → `NOUTE` and fort.63 → `NOUTGE` at `[file=src/write_output.F line=504-523, 593-603]`
- Format by `ABS(NOUTE/NOUTGE)`:
  - `1` = ASCII
  - `2` = binary (rejected in v55+)
  - `3` = NetCDF3
  - `5` = NetCDF4
  - `4` = compact ASCII (NOUTE only? check)
  - `7` = XDMF (global only)
- Set in `read_input.F` at `[file=src/read_input.F line=3613-3633, 4124-4152]`
- Writer dispatch by specifier at `[file=src/write_output.F line=4226-4250]` (`ASCII/SPARSE_ASCII/NETCDF3/NETCDF4/XDMF`)

### ASCII headers

- `header61` at `[file=src/globalio.F line=963-977]`
- `header63` at `[file=src/globalio.F line=1011-1024]`
- Format: run strings + numeric line (record count, stride seconds, stride timesteps, item count, FileFmtVersion)

### NetCDF naming

- Base file: `.../fort.61` or `.../fort.63` at `[file=src/write_output.F line=1568-1575, 1691-1693]`
- NetCDF check uses appended `.nc` (so `fort.63.nc` is the actual file on disk)

## B. fort.62/64 (velocity)

- Mirror of elevation structure at `[file=src/write_output.F line=537-563, 710-714]`
- fort.62: `NOUTV/NSPOOLV`, fort.64: `NOUTGV/NSPOOLGV`
- `num_items_per_record = 2` (U,V components) at `[file=src/write_output.F line=548-557, 716-720]`
- Headers `header62` at `[file=src/globalio.F line=987-1001]`, `header64` at `[file=src/globalio.F line=1059-1073]` — encode type=2 for 2-component output

## C. fort.71-74 (met output)

- Station pressure/wind (71/72) controlled by `NOUTM` at `[file=src/write_output.F line=735-748, 775-792]`
- Global pressure/wind (73/74) controlled by `NOUTGW` at `[file=src/write_output.F line=817-823, 906-913]`
- Format gating in read_input.F at `[file=src/read_input.F line=3998-4021, 4356-4384]`: ASCII/NetCDF/XDMF by absolute value
- **Disabled when NWS=0** at `[file=src/write_output.F line=760-762, 804-806, 828-830, 920-922]`
- Pressure and wind kept in separate descriptors/arrays (not combined)

## D. Harmonic analysis output (fort.51-53)

- Init: `initHarmonicParameters` called from `[file=src/adcirc.F line=268]`
- Per-step update: `updateHarmonicAnalysis(IT, TIMEH)` at `[file=src/timestep.F line=1184]`
- Accumulator: `harm.F:632-689` accumulates per-frequency least-squares terms over requested window
- Sub-routines `LSQUPD*` for station/global elevation and velocity
- **End-of-run solve + write**: `solveHarmonicAnalysis` then `writeHarmonicAnalysisOutput` at `[file=src/adcirc.F line=540-541]`
- Writer: `writeOutHarmonicArrays` at `[file=src/write_output.F line=2673]`
  - ASCII output at `[file=src/write_output.F line=2701-2750]`
  - NetCDF output at `[file=src/write_output.F line=2752-2760]`
- `NFREQ` usage: `[file=src/read_input.F line=4421-4452, 4500]`, `[file=src/harm.F line=128, 547-549]`
- **`MUFREQ` not present** — use `NFREQ` only

## E. 3D station output (fort.41-42)

- Controls: `I3DSD` for fort.41 (density/salinity/temp), `I3DSV` for fort.42 (velocity) at `[file=src/global_3dvs.F line=229-264]`
- Init: `initOutput3D` writes 3D headers at `[file=src/write_output.F line=2787-2843]`
- Descriptor setup: `[file=src/write_output.F line=2980-3103]`
- Vertical layer storage: per station with `NFEN` columns, `num_items_per_record = NFEN`
- Layerwise loop `k=1,NFEN` at `[file=src/write_output.F line=3403-3416, 3584-3591, 3623-3630]`

## F. Max-value outputs (maxele.63, maxvel.63)

- Per-step running max: `collectMinMaxData` at `[file=src/timestep.F line=1162]`
- Implementation: `[file=src/write_output.F line=6343-6374]` — updates `ETAMAX`, `UMAX` plus timestamp arrays
- Descriptor init at `[file=src/write_output.F line=1205-1237, 1239-1268]` (both start with `writeFlag=.false.`, `readMaxMin=.true.` for hotstart continuity)
- **End-of-run write only**: `writeOutArrayMinMax` at `[file=src/write_output.F line=1890-1898]` when `it == nt`

So `maxele.63.nc` and `maxvel.63.nc` only get written at the very end of the run.

## G. NetCDF vs ASCII

- Specifier-driven at `[file=src/write_output.F line=4226-4271]`:
  - ASCII / sparse ASCII → text writer
  - NETCDF3 / NETCDF4 → NetCDF writer
- NetCDF init only for NETCDF3/NETCDF4 at `[file=src/write_output.F line=1611-1615]`
- Compile-time `ADCNETCDF` guard required
- File naming: base `file_name` no extension at `[file=src/write_output.F line=1572-1580]`; NetCDF treated as `file_name + '.nc'` at `[file=src/write_output.F line=1691-1693]`

## H. Post-merge (parallel)

- Per-PE files: `PE0000/fort.6X` etc.
- Master mapping from `fort.80` at `[file=prep/post.F line=67-164]` includes:
  - Global/local node maps
  - Station maps
  - Output control / stride fields
- Merge routines per output type:
  - `POST61` at `[file=prep/post.F line=238]`
  - `POST62` at `[file=prep/post.F line=492]`
  - `POST63` at `[file=prep/post.F line=750]`
  - `POST64` at `[file=prep/post.F line=1003]`
  - `POST71` at `[file=prep/post.F line=1858]`
  - `POST72` at `[file=prep/post.F line=2125]`
  - `POST73` at `[file=prep/post.F line=2404]`
  - `POST74` at `[file=prep/post.F line=2660]`

Each reads per-PE files and writes full-domain `fort.6X/7X`.

## Decision Guide — output stride

| Use case | NSPOOLE / NSPOOLGE | Output frequency |
|----------|--------------------|------------------|
| Tidal validation (wide6) | NSPOOLE = 900 (DT=2s → 30min) | per 30 min — current setting |
| Storm surge prediction | NSPOOLE = 360 (15 min) | finer for time-critical |
| Climatology | NSPOOLE = 86400 (1 day) | daily averaging needed externally |
| Disk-saving runs | NSPOOLE = 1800 (1 hour) | rough validation only |

For wide6 (RNDAY=30, DT=2s, NSPOOLGE=900):
- 30 days × 24 h × 2 (per hour) = ~1440 records on global elevation field
- Each record = 475K × 8 bytes = 3.8 MB → total 5.5 GB — matches actual fort.63.nc size

## Working Rules

1. **NetCDF output requires `ADCNETCDF` compile flag** — check build with `ldd padcirc.exe | grep netcdf`. Without it, NETCDF3/4 specifiers fall back silently.
2. **`NOUTE/NOUTGE` sign** controls append (positive = new file) vs not. With NetCDF, hot restart appends; with ASCII, new file each cold start.
3. **Max-value files written ONLY at run end** — if run terminates early (crash, kill), no maxele/maxvel.
4. **Harmonic output is end-of-run** — accumulators are per-step but solve+write happens once.
5. **Per-PE outputs need post-merge** via `adcpost` (separate executable) or `POST61` etc. routines invoked manually.

## Common Pitfalls

- **fort.63 + fort.63.nc both exist** — old format vs new NetCDF; `read_global` may pick the older. Delete one or set NOUT specifier consistently.
- **Hot restart with different `NSPOOLE`** — old file format matched first stride; new stride creates inconsistent records.
- **`NFREQ` mismatch between fort.15 NBFR and fort.15 harmonic block** — silent corruption.
- **Adcprep `--prepall` re-runs every time** — overrides per-PE PE####/fort.6X files. Check before re-running mid-output collection.
- **NetCDF `_FillValue` for dry nodes** — varies by version; downstream tools must handle.
- ▢ User-experience cases — placeholder.

## References

- `src/write_output.F` — main writers (init + writeOutput2D/3D + harmonic + minmax).
- `src/globalio.F` — header functions per output type.
- `src/timestep.F` — `collectMinMaxData`, `updateHarmonicAnalysis` per-step calls.
- `src/harm.F` — accumulator + solve.
- `src/adcirc.F` — end-of-run writeOutHarmonic dispatch.
- `prep/post.F` — POST61-74 merge routines.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 50+ file:line citations |
| Coverage | fort.61-64, 71-74, 51-53, 41-42, max-value, NetCDF, post-merge |
| Review status | `review_required: true` |

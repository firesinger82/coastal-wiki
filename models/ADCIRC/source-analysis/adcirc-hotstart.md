---
title: "adcirc hotstart"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-hotstart.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How ADCIRC reads and writes hot-start state via `IHOT` (cold/binary/NetCDF dispatch), the exact byte-level structure of `fort.67/68` direct-access binary files, what state is preserved (water levels, velocities, wet/dry, harmonic accumulators, 3D state) vs reconstructed (meteorology), how `NHSTAR/NHSINC` controls writes, the relationship between processor-count changes and full-domain ↔ subdomain mapping, and how meteorological forcing re-aligns to `TimeLoc` after restart. Use this when chaining storm hindcasts, debugging restart-induced jumps, or migrating between binary and NetCDF hot-start.

## Source basis

- `read_input.F:1050-1075, 4504-4544` — `IHOT`, `NHSTAR`, `NHSINC` reads.
- `adcirc.F:316-322` — top-level dispatch.
- `hstart.F:47-3048` — main reader, mappers, 3D reader.
- `write_output.F:4429, 4920-5374` — binary writer, full vs local.
- `writer.F:1069`, `vsmy.F:3254, 3531-3778` — dedicated writers, 3D.
- `netcdfio.F90:3866-9188` — NetCDF naming, definitions, read/write.
- `timestep.F:1192-1211` — runtime hot-start trigger.
- `wind.F:2170-2970` — meteorological re-alignment per NWS.

## A. IHOT dispatch

`IHOT` is read from `fort.15` (`read_input.F:1050-1053`).

| `IHOT` | Mode | File | Reader |
|---|---|---|---|
| `0` | Cold start | (none) | `COLDSTART()` (`adcirc.F:316-319`) |
| `17` | ASCII initial | `fort.17` | `HOTSTART()` (`hstart.F:242-253`) |
| `67` | Binary | `fort.67` | `HOTSTART()` (`hstart.F:452-465`) |
| `68` | Binary | `fort.68` | `HOTSTART()` |
| `367/368` | NetCDF3 classic | `fort.67.nc` / `fort.68.nc` | `readNetCDFHotstart*` (`hstart.F:673-690`) |
| `567/568` | NetCDF4/HDF5 | same | same path |

After `IHOT=67`, output flips to unit/file `68`, and vice versa (alternating ping-pong) (`read_input.F:1063-1075`).

## B. fort.67/68 binary structure

Direct-access, `RECL=8` (`hstart.F:485-492`, `write_output.F:4920-4923`).

**Header order** (`write_output.F:4922-4931`):
```
FileFmtVersion, IM, TimeLoc, IT, NPX, NEX, NPX, NEX
```

**2D state** (full-domain `:4935-4967`; local `:5031-5065`):
```
ETA1, ETA2, EtaDisc, UU2, VV2,
[CH1 if applicable], NODECODE, NOFF
```

**Radiation stress** (`:4969-4997`):
- `RSNX1, RSNY1, RSNX2, RSNY2` if `NRS≠0`, zeros otherwise.

**SWAN RS** (`:5000-5028`):
- SWAN arrays if `NRS=3`, zeros otherwise.

**Output spool counters** (`:5131-5154`):
- `NSCOUE, NSCOUV, NSCOUC, NSCOUM, NSCOUGE, NSCOUGV, NSCOUGC, NSCOUGW`.

**Harmonic analysis state** (if active, `:5166-5374`):
- Header/counters, constituent metadata + matrix, load vectors, means/variances.

Reader mirror at `hstart.F:506-668` (header → 2D → counters → 3D → harmonic).

## C. hstart.F entry points

| Routine | Lines |
|---|---|
| `HOTSTART()` (main 2D reader) | `hstart.F:47` |
| `HOTSTART_3D(TimeLoc, ITHS)` (3D init) | `:2061` |
| `readAndMapToSubdomain2D` (real 2D mapper) | `:2827` |
| (integer 2D mapper) | `:2899` |
| (element integer mapper) | `:2973` |
| (3D mapper) | `:3048` |

Write-side **not in `hstart.F`**:
- 2D: `writeHotstart(TimeLoc, IT)` in `write_output.F:4429`.
- Dedicated writer: `writeHotstart_through_HSwriter` in `writer.F:1069`.
- 3D: `HSTART3D_OUT(IT)` in `vsmy.F:3254`.

## D. NetCDF variant

Naming: `fort.67.nc` or `fort.68.nc` based on unit `67/68` (`netcdfio.F90:3866-3871`).

Setup `initNetCDFHotstart` (`:5241`); defines variables (`:5290-5519`):
- `zeta1, zeta2, zetad` — water levels.
- `h1, h2` — depths (computed `H1/H2 = DP + IFNLFA*ETA`).
- `u-vel, v-vel` — velocities.
- `ch1, nodecode, noff` — wet/dry.
- Radiation stress variables.

Read opens `fort.<lun>.nc`, reads `time`, then maps state (`:7904-8216`).
3D NetCDF: `readNetCDFHotstart3D` (`:9188`).

## E. NHSINC / NHSTAR output control

Read together (`read_input.F:4504-4508`):

| `NHSTAR` | Behavior |
|---|---|
| `0` | Disabled |
| `1`, `67`, `68` | Non-portable binary |
| `3`, `367`, `368` | NetCDF3 classic |
| `5`, `567`, `568` | NetCDF4/HDF5 |
| `-1` | Timestamped binary files |

`NHSINC=0` is illegal when `NHSTAR≠0` (`:4542-4544`).

Trigger (`timestep.F:1192-1197`): hot-start fires when `IT` is exact multiple of `NHSINC`, or when `-IHOT==IT` (special end-of-run case).

## F. State preserved

| State | Read | Write |
|---|---|---|
| `ETA1, ETA2, EtaDisc` | `hstart.F:526-536` | `write_output.F:4935-4945` |
| `H1, H2` | NetCDF only; binary recomputes from `DP + IFNLFA*ETA` (`hstart.F:529-533`) | `netcdfio.F90:5357-5380` |
| `UU2, VV2` | `:537-538` | `:4947-4953` |
| `NNODECODE, NODECODE, NOFF` | `:542-545` | `:4961-4967` |
| Harmonic accumulators, means, variances | `:657-668` | `:5166-5374` |
| 3D state (if `C3D`): `DUU/DUV/DVV, UU/VV, BSX/BSY, Q, WZ, q20, l, SigT/Sal/Temp` | `:568-645` | `vsmy.F:3531-3778` |
| **Meteorology** | **NOT stored** — reconstructed via `hotstartMeteorologicalForcing` | — |

Meteorology is **not preserved** — reconstructed at `TimeLoc` from forcing files (`hstart.F:1440-1444`).

## G. Resolution / mesh change

The protocol is **index-based**, not remeshing-based.

- File header carries `NP_G_IN, NE_G_IN, NP_A_IN, NE_A_IN` (`:519-522`).
- Subsequent reads consume arrays using **current run's** `NP_G/NE_G` and **current subdomain maps** (`:2858-2868, 3006-3015`).
- NetCDF maps file variables to current subdomain index lists (`netcdfio.F90:8109-8158`).

So **hot-start across processor-count change is supported** (full-domain → subdomain mapping), but **mesh topology change is NOT** unless node/element indexing is preserved.

## H. Restart with NWS forcing

After dynamic state read, `HOTSTART` repositions time-dependent forcing using `TimeLoc` and `ITHS` (`hstart.F:1442-1444`).

Inside `hotstartMeteorologicalForcing`, time interpolation explicitly reconstructed from `STATIM, WTIMINC, DTDPHS, TimeLoc`.

Per-NWS behavior:

| NWS | Behavior on restart |
|---|---|
| `2` | Fast-forward through forcing records using `TIMEIT = IT*DTDPHS + STATIM*86400`; computes `WTRATIO = (TimeLoc-WTIME1)/WTIMINC` (`wind.F:2170-2192`) |
| `12` (positive) | Wind data treated as cold-start-relative |
| `-12` (negative) | Hot-start-relative `TimeLoc` |
| `13` (NetCDF OWI) | Initialize at `TIMELOC` (`wind.F:2850-2862`) |
| `14` (GRIB2) | `TimeLoc` rounded down to nearest `WTIMINC`; `NWS14INIT` + 2 forcing snaps (`:2936-2970`) |

## Decision Guide

| Need | Setup |
|---|---|
| Standard chained run | `IHOT=67`, `NHSTAR=1`, `NHSINC=86400/DT` (daily) |
| Long hindcast with NetCDF | `IHOT=567`, `NHSTAR=5`, `NHSINC` proportional |
| Storm peak hot-start (specific time) | `NHSTAR=-1` (timestamped), `NHSINC` short around peak |
| Decompose / re-decompose | Allowed if mesh same; `NP_G/NE_G` from header used as full-domain indexing |
| Migrate from binary to NetCDF | One-time read binary, write NetCDF on next hot-start |
| Meteorology continuity | Use **negative** NWS form (e.g., `NWS=-12`, `NWS=-13`) for hot-start-relative timing |
| Coupled ADCIRC+SWAN restart | Both must be at same `TimeLoc`; SWAN hot-file via `SwanHotStartUnit` |

## Working Rules

- Always set `NHSTAR ≠ 0` for production runs — restart capability invaluable.
- Binary `fort.67/68` ping-pong: every hot-start write alternates files. Don't manually delete one mid-run.
- Verify hot-start success: log says "HOTSTART SUCCESSFUL" and prints `IT, TimeLoc`. Mismatch = abort.
- For coupled runs (NRS=3), confirm SWAN spectral hot-file written at compatible time.
- After hot-start, harmonic analysis windows can drift if `NTSTH/NHARFR` settings changed — output `fort.51` immediately after restart to verify.
- NetCDF over binary: easier debugging (ncdump), portable across endianness, slight cost overhead.
- Do **not** edit `STATIM/REFTIM` between hot-starts unless you also update astronomical references.

## Common Pitfalls

- ▢ Hot-start across mesh refinement — node indices misaligned; results garbage.
- ▢ Switching `NTIP` (tidal potential) between cold and hot — harmonic accumulator inconsistency.
- ▢ Switching `NRS` between cold and hot — RS arrays uninitialized.
- ▢ Wrong `IHOT` value (`67` vs `367` confusion) — file format mismatch.
- ▢ Cold-start meteorology with positive `NWS=12` after hot-start — forcing time origin wrong.
- ▢ NetCDF hot-start on Windows / different endianness — generally fine; but binary `fort.67/68` is non-portable, beware cross-platform.
- ▢ Coupled `NRS=3` NetCDF read — possible bug at `netcdfio.F90:8017-8085` (cited in source); test before relying.
- ▢ Setting `NHSTAR=-1` (timestamped) without ensuring filesystem can hold many files for long runs.

## Next expansion

- Hot-start alignment recipe for storm hindcast chains.
- NetCDF hot-start performance vs binary.
- Cross-platform binary hot-start considerations.

## References

- Luettich & Westerink ADCIRC docs (UTexas / UNC).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.

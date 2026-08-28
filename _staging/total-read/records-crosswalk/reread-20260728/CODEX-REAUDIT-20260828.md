# Codex 잔여후보 심층 재감사 (2026-08-28)

> Phase B 에서 caller 가 못 닫은 in-scope pending/MED 23건을 Codex 가 리포지토리 소스 직접 판독으로 결판.
> task-mtcbz7x6 (25m). 결과 `CODEX-REAUDIT-verdicts-20260828.json`.

## 결과: CONFIRM 14 · REFUTE 8 · UNCERTAIN 1

### CONFIRM 14 (→ confirmed_delta 승격, decided_by=Codex, 사람 승인 대기)
- 000·sediment.F·B1 — The positive-flow south-face diffusion uses the north-cell depth pair, while the negative branch uses the south-face pair. F4 feeds the concentration 
- 000·sediment.F·B2 — With px=1, npx is both 0 and px-1, so ELSEIF makes the east-wall F1 assignment unreachable. The analogous py=1 branch explicitly handles both ends, an
- 000·sediment.F·B6 — Cell-centered Zb(Mloc,Nloc) is added as a whole array to x- and y-face arrays whose respective extents are Mloc1 and Nloc1. The intrinsic assignments 
- 001·wavemaker.f90·B9 — For explicit Nfreq=1, the final comparison unconditionally indexes Freq(0), and the equal-dfrequency variants also divide by mfreq-1. The input path v
- 001·mod_input.f90·B0 — A missing key returns with an INTENT(OUT) destination undefined, and unchecked callers immediately branch on that value; the same pattern exists for l
- 004·nesting.F·B1 — Both initialization and EOF leave equal time slots, and the equal-slot branch sets both weights to zero rather than retaining either record. Those wei
- 004·wavemaker.F·B6 — All equal-frequency implementations divide by mfreq-1 before their component loops. The reader supplies 45 only when the key is absent and never rejec
- 004·init.F·B2 — The routine unconditionally clears SLOPE_CTR immediately before both guarded blocks, and there is no intervening assignment or input path. The warning
- 004·io.F·B2 — ROLLER is initialized, so this is not an undefined read, but the force-to-true test runs before ROLLER_EFFECT is parsed. An explicit ROLLER_EFFECT=tru
- 004·mod_vessel.F·B1 — Propeller parameters are assigned only for PR, but the PROPELLER post-read calculations run for every vessel. SL and PA entries therefore read uniniti
- 004·mod_vessel.F·B2 — The parser has geometry branches for PR and SL only, then proceeds to the path record; PA is nevertheless a supported dispatch. GREEN_FUNCTION_SOURCE 
- 004·mod_meteo.F·B0 — Rollover advances only time and position, leaving Pn/Pc/A/B endpoint 1 at the initial record before reading the next endpoint. Subsequent interpolatio
- 004·mod_meteo.F·B1 — Gaussian rollover likewise omits DP/SigmaX/SigmaY/Theta from endpoint 1 while advancing time and position. From the second interval onward, the interp
- 004·mod_tide.F·B3 — Only a missing key gets the default; explicit values are not range-checked. Iwidth=1 reaches the singular denominator, while widths beyond a local dim

### REFUTE 8 (중화가드·edge — 미승격, distinct_unconfirmed 유지)
- 000·convert.f·B1 — convert.f assumes a common record count and clock, but the native producer advances every active station buffer in the same station-output c
- 000·bc.f90·B0 — The only scheme that consumes P/Q as exchanged cell-interface state is hard-disabled by PQ_scheme=.FALSE.; the active scheme uses locally fo
- 000·bc.f90·B1 — All in-tree PHI_COLL callers select VTYPE 1, 2, or 3, whose y-boundary blocks have the periodic guard. No caller selects the unguarded VTYPE
- 000·exchange_gpu0819.F·B6 — PHI_COLL_OUTER_GPU is used for physical-edge reflection only; moment_gpu explicitly recomputes the derivative halo through two ghost layers 
- 001·mod_bathy_correction.f90·B1 — Undefined entries are confined to MASK0=0 cells and Gradx/Grady are not consumed by the correction calculation after being formed. Their onl
- 004·mod_subgrid.F·B1 — For zero or negative ratios, the Fortran allocations have zero extents and the 1:ratio loops execute zero times, leaving pcount=0. The pcoun
- 004·sponge.F·B0 — Nghost is a compile-time 3, and the caller only enters maker/boundary sponge construction for nonnegative widths and positive grid spacing. 
- 004·mod_precipitation.F·B0 — Before the first record time, both zero weights intentionally suppress precipitation; ESTIMATE_DT advances TIME before distribution is calle

### UNCERTAIN 1
- 001·mod_global.f90·B0 — The code incorrectly treats the MPI_COMM_WORLD rank as the comm2d rank and separately builds world-rank mappings. Material failure depends on whether the deployed MPI implementatio (MPI 구현 의존 — 별도 판단)

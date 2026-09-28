---
title: "xbeach output"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach_output.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. **§C.1-C.2 추가 (2026-09-28, SCOPED EDIT)**: runup gauge 추출 경로 직독 — ncoutput.F90:113(rugrowindex 선언 주석)·:915·:925-930·:932-938(rugx is not used)·:957-964(교차 탐색 루프)·:987-989(교차 셀 xz/yz/zs 출력)·:1720(rugrowindex=ypoints), varoutput.F90:182-191, params.F90:1256-1261(nrugauge 0-50·nrugdepth 1-10·rugdepth 기본 0.0)·1398(eps 기본 0.005)·1796-1807(rugdepth<=eps 승격 + 경고). 두 발견은 concepts/swash-zone/06-model-application.md 집필 중 드러났고 절대규칙 #6 에 따라 모델 메커닉을 본 노트로 옮긴 것이다."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
source_correction_date: 2026-09-12
source_correction_by: "Codex"
source_correction_scope: "활성 `ncoutput_module` 공급자와 두 출력 형식에 공통인 `xomaster` 쓰기 조건을 정정"
source_correction_human_approval: not-issued
---

> **2026-09-12 AI 출처 정정**: 활성 `ncoutput_module` 공급자와 두 출력 형식에 공통인 `xomaster` 쓰기 조건을 정정. 기존 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인이 아니다. [원문 구간·SHA와 연결 판정](../../../_staging/total-read/model-audit/XBeach/connectivity/runtime-20260912/evidence.json)을 따르며 원본 솔버는 수정하지 않았다.

## Scope

XBeach output system: `tintg/tintp/tintm` time intervals, `outputformat=fortran/netcdf/debug`, no `outputfreq` keyword (use `tint*` or timing files `tsglobal/tspoints/tsmean`), 21-default global variables list, point output via `npoints/nrugauge/pointvars` with auto-snapping, mean/variance/min/max via `varianceupdate`, NetCDF dimensions/variables/CF-1.4 attributes, hotstart files (NOT `rst.???` — actually `hotstart_<var><NNNNNN>.dat`), morfac time conversion for input/output, and MPI master-gather output (with parallel-NetCDF noted as TODO). Use this when configuring XBeach output for storm hindcasts, debugging point output, or migrating between Fortran/NetCDF formats.

## Source basis

- `params.def:399-430, 305` — output keys.
- `params.F90:1228-1277, 1941-1952, 2131-2524` — parameter parsing, defaults.
- `paramsconst.F90:96-98` — format constants.
- `output.F90:54-169` — dispatch.
- `ncoutput.F90:253-2175` — NetCDF + hotstart.
- `varianceupdate.F90:18-477` — mean/variance.
- `timestep.F90:181-742` — output timing, snap.
- `initialize.F90:1697-1853` — point snap, hotstart read.
- `variables.def:47-198` — variable metadata.
- `varoutput.F90` — compiled legacy output implementation. Its `var_output_init` calls in current `output_init` are commented out (`output.F90:54-80`); it is not the active output provider.
- `postprocess.F90` — `postprocessvar_r2`: 출력 직전 변수별(mnemonic) fill-value/wetz masking 적용 (dry cell fill). 출력 변수 후처리 (2026-06-03).

## A. params.txt output keys

| Key | Purpose | Lines |
|---|---|---|
| `tintg` | Global output interval (replaces `tint`) | `params.def:399-400, params.F90:1228-1232` |
| `tintp` | Point/runup gauge interval | `:401, :1233-1236` |
| `tintm` | Mean/variance/min/max interval | `:403, :1237-1240` |
| `outputformat` | `fortran/netcdf/debug` (constants `0/1/2`) | `paramsconst.F90:96-98, params.F90:1267-1277` |

**No `outputfreq` keyword found** — use `tint*` or timing files `tsglobal, tspoints, tsmean` (`params.def:405-408, timestep.F90:181-285`).

`output_init` selects `fortoutput_init`, `ncoutput_init`, or both (debug with `USENETCDF`). The active provider is `ncoutput_module`, including the Fortran writer. `OUTPUTFORMAT_NETCDF` without `USENETCDF` logs the missing support and halts. Old `var_output_init` calls are commented out. (`output.F90:5-8, 51-80`)

At runtime `output` calls `ncoutput`; its non-`xomaster` return is before **both** the NetCDF and Fortran write branches. Thus `outputformat=fortran` does not make every MPI rank write the same files in this path. (`output.F90:164`; `ncoutput.F90:1118-1164`)

## B. Global output variables

Default 21 mnemonics when `nglobalvar = -1` (`params.F90:2131-2136`):
```
H, zs, zs0, zb, hh, u, v, ue, ve, urms, Fx, Fy,
ccg, ceqsg, ceqbg, Susg, Svsg, E, R, D, DR
```

If `nglobalvar = 999`: outputs all registered mnemonics except small skip list (`xyzs01..04, tideinpz, gw0back, zi, wi`) (`:2137-2165`).

Variable metadata in `variables.def`:
- `zb`: bed level (`:47`).
- `H`: Hrms wave height (`:63`).
- `hh, zs, zs0`: water depth/level/tide-only (`:87-89`).
- `u, v, ue, ve`: cell-centre GLM/Eulerian velocities (`:131-134`).
- `ccg, Susg, Svsg, ceqbg, ceqsg`: sediment (`:148-170`).
- `E, R, D, DR`: wave/roller energy + dissipation (`:119-154`).

## C. Point output

Controlled by `npoints, nrugauge, npointvar, pointvars, xpointsw, ypointsw, stationid, pointtypes` (`params.def:415-430`).

Reader (`params.F90:2219-2305`):
- Allocates combined point/runup arrays.
- Marks types: `0=point, 1=rugauge`.
- Reads positions; stores world coordinates.

Coordinate lines after `npoints` or `nrugauge`:
- Each line: `x y stationid` (or auto-named `pointNNN`/`rugauNNN`) (`:2417-2524`).

Coordinates **snapped to nearest grid indices** in output init (`ncoutput.F90:1697-1731`).

### C.1 ★ runup gauge 는 점이 아니라 **행**이다

`nrugauge` 게이지는 `x y stationid` 로 좌표를 받지만 **추출 루틴은 y 성분만 쓴다.**
게이지는 `rugrowindex` 라는 격자 **행 인덱스** 하나로 환원된다 — 변수 선언 주석이
*"Array with row index where runup gauge can be found"* (`ncoutput.F90:113`), 할당은
`rugrowindex = ypoints(par%npoints+1:)` (`:1720`). Fortran 출력 경로도 동일
(`varoutput.F90:182-191`, 주석 *"Make rugrowindex with row number (per subprocess) with runup gauge"*).

추출 루프는 전역 x 인덱스 **1** 과 `rugrowindex` 를 지역좌표로 변환한 뒤
*"rugy now contains the local y-coordinate / rugx is not used"* 라고 주석으로 못박고(`:937-938`),
그 행의 **전 cross-shore 구간**(`xmin+1 .. xmax`)을 훑어 수심이 임계를 가로지르는 첫 지점을 찾는다
(`:957-964`):

```fortran
do j=xmin+1,xmax
   if ((sl%hh(j,  rugy)<=par%rugdepth(ird)) .and. &
   &   (sl%hh(j-1,rugy)> par%rugdepth(ird)) ) then
      idumhl=j-1
      exit
   endif
enddo
```

- **같은 행에 게이지를 둘 놓으면 같은 결과가 나온다** — 게이지가 고르는 것은 cross-shore 측선이지 지점이 아니다.
- 출력은 교차 **셀**의 `xz`·`yz`·`zs` 를 그대로 낸다(`:987-989`) — **보간 없음**.
  따라서 처오름 해상도가 cross-shore 격자 간격에 직접 묶인다.
- 미검출은 `huge(0.d0)`(`:930`)이고 MPI 에서는 **최솟값 reduce** 로 합쳐진다
  (주석 *"The runup values are collected in xomaster, using xmpi_reduce, taking the minimum values"*, `:925-926`).
- 범위: `nrugauge` 0–50(`params.F90:1257`), 게이지당 출력 벡터 길이 `1 + nrugdepth*3`(`ncoutput.F90:915`).

### C.2 ★ `rugdepth` 는 `eps` 아래로 내려가지 않는다

`nrugdepth`(기본 1, 범위 1–10)개의 처오름 임계를 한 게이지에서 동시에 받을 수 있고
`rugdepth` 기본값은 **0.0**, 범위 0.0–0.1 이다(`params.F90:1260-1261`).

그런데 초기화 단계에서 `nrugauge>0` 이면 `rugdepth <= par%eps` 인 항목이 전부
`(1.0d0 + epsilon(0.d0))*par%eps` 로 **승격**되고 경고 한 줄만 남는다 —
주석 *"fix minimum runup depth"*, 경고 *"Warning: Setting rugdepth to minimum value greater than eps ("*
(`params.F90:1796-1807`). `eps` 는 침수-건조 임계이며 기본 **0.005 m**(범위 0.001–0.1, `params.F90:1398`).

- **기본 설정에서 처오름 임계 = 침수-건조 임계다.** `rugdepth` 를 지정하지 않으면 0.0 이 아니라 `eps` 가 쓰인다.
- **안정성 때문에 `eps` 를 키우면 처오름 정의가 함께 움직인다** — 수치 설정이 물리량 정의를 바꾸는 결합이고,
  로그의 경고 한 줄 말고는 드러나지 않는다.
- 도메인 층 논의는 [concepts/swash-zone/06-model-application.md](../../../concepts/swash-zone/06-model-application.md) §3.

NetCDF point metadata: `pointx, pointy, station_id, xpointindex, ypointindex, pointtypes`. Point data variables: `point_<mnem>` (`:446-528`).

Fortran point output: each station writes `<stationid>.dat` + `pointvars.idx` (`:1786-1804`).

## D. Mean / time-averaged outputs

Enabled by `nmeanvar`, read after that keyword (`params.def:413-414, params.F90:1263-1265, 2310-2320`).

Mean module stores: `mean, variance, min, max`, plus variance helper terms for rank 2/3/4 arrays (`varianceupdate.F90:18-51`).

`makeaverage` called while `par%t` inside mean output window (`output.F90:116-123`).

Accumulation (`varianceupdate.F90:311-388`):
- `mult = par%dt / par%tintm`.
- Rotates variables where needed.
- Handles `thetamean` circular averaging.
- Updates mean/variance/min/max.

Cleared after mean output (`output.F90:166-169`).

NetCDF: 4 variables per mean variable: `<name>_mean, <name>_var, <name>_min, <name>_max`. `cell_methods = "meantime: ..."` (`ncoutput.F90:559-640`).

Fortran: `<mnem>_mean.dat, _var.dat, _min.dat, _max.dat` (`:1806-1950`).

## E. NetCDF structure

Dimensions (`ncoutput.F90:253-305`):
- `nx, ny`, wave angle dims, bed layers, sediment classes.
- Optional: drifter/ship/vegetation/Q3D dims.
- `globaltime, pointtime, meantime`, point name length.

Grid variables `globalx/globaly`: units, long names, standard names, axis, optional projection/rotation (`:319-343`).

Global file attributes: CF-1.4, build metadata (`:345-350`).

Variables defined from mnemonic type/rank; dimensions from `variables.def`; attributes include `coordinates, units, standard_name, long_name, _FillValue` (`:374-440`).

Writes via `nf90_put_var` with rank-specific starts (`:1134-1486`).

## F. Restart / hotstart files

This tree does **NOT implement `rst.???`** — restart called hotstart, files named `hotstart_<var><NNNNNN>.dat` (`ncoutput.F90:2124-2129, initialize.F90:1791-1799`).

Always-included writes: `zs, zb, uu, vv`.

Optional groups (`ncoutput.F90:2052-2113`):
- Groundwater.
- Wave energy `ee/rr, ee_s`.
- Nonhydrostatic `breaking/wb/ws`.
- Sediment `ccg`.
- Turbulence `kturb`.
- Structures.
- `dU/dV, umean/vmean`.

2D real/int files: row-wise over `j=1..ny+1`; each row contains `i=1..nx+1`. 3D loops `k`, then rows (`:2115-2175`). Reading mirrors structure (`initialize.F90:1707-1853`).

## G. Output timing with morfac

When `morfacopt = 1`, input times/intervals converted morphological → hydrodynamic by dividing by `max(morfac, 1)` (`params.F90:1941-1952`).

Timing files `tsglobal, tspoints, tsmean, tshotstart` likewise divided after reading (`timestep.F90:198-317`).

Output timestamps in NetCDF converted **back** to morphological time via `par%t * max(par%morfac, 1)` (`ncoutput.F90:1136-1140, 1303-1306, 1412-1415`).

Time stepper snaps `dt` to next output time (`timestep.F90:652-657`).

## H. Output cost / HPC I/O

MPI path centralizes through `xomaster`:
- Compute ranks wake output master only when `tpar%output` true (`output.F90:130-139`).
- `ncoutput` returns on non-output-master ranks before file writes (`ncoutput.F90:1118-1127`).

Global output: collects every requested global variable from all nodes before writing (`:810-842`). Mean similar (`:864-873`).

**Point output explicit TODO** notes faster if nodes write own points; needs parallel NetCDF or better MPI (`:850-858`).

NetCDF opened+closed at each output call (`:1122-1603`). Fortran direct-access flushes frequently after records (`:1160-1405`).

On network filesystems, main cost: large all-rank gathers to `xomaster`, single-writer serialization, repeated NetCDF open/close, many flushed direct-access files.

## Decision Guide

| Need | Setup |
|---|---|
| Standard storm hindcast | `tintg=600, tintp=60, tintm=3600, outputformat=netcdf` |
| Quick run | `tintg=3600` (hourly) |
| Surf-zone runup detail | `tintp=10` (10s gauge sampling) |
| Storm peak high-frequency | `tintg=60` for 1 hour around peak |
| Long-term morfac | Use `tsglobal` file with sparse times |
| Validation against gauges | `tintp=` matching gauge sample rate |
| Restart capability | `tshotstart` file (or fixed interval) |
| NetCDF for ParaView | `outputformat=netcdf` |
| Fortran legacy tools | `outputformat=fortran` |
| MPI run on cluster | NetCDF output preferred; expect master-bottleneck |

## Working Rules

- `tintg=600` (10 min) is default for storm hindcasts.
- Mean output uses `tintm`; computed over `tintm` window centered at output time.
- Hotstart frequency: ~1 hour for storm hindcasts.
- Point coordinates auto-snap to nearest grid; verify `xpointindex/ypointindex`.
- For Korean coast surveys: `tintp=300` (5 min) at gauges; matches typical observation cadence.
- Output cost on HPC dominated by network I/O; minimize global writes.
- NetCDF preferred over Fortran for analysis (xarray, ncview).

## Common Pitfalls

- ▢ Looking for `outputfreq` keyword — doesn't exist; use `tint*`.
- ▢ Looking for `rst.???` restart — actually `hotstart_<var><NNNNNN>.dat`.
- ▢ Setting `tintg=1` (every second) — disk fills fast.
- ▢ Assuming Fortran output bypasses the MPI output master: both file formats share the `xomaster` guard (`ncoutput.F90:1118-1164`).
- ▢ Mean output without `nmeanvar` — silently no mean output.
- ▢ Forgetting `morfacopt=1` — output times not aligned with input forcing.
- ▢ Hotstart with version mismatch (different XBeach build) — file format incompatible.
- ▢ Comparing global output across MPI ranks — only master writes; per-rank no output.

## References

- XBeach User Manual (Output section).
- CF-1.4 NetCDF conventions.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.

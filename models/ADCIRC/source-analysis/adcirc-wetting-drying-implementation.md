---
title: "adcirc wetting drying implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-wetting-drying-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC wetting/drying — NOLIFA, H0, NODECODE, transitions

## Scope

Code-level walk-through of the wet/dry algorithm: when nodes flip wet→dry, when dry→wet, what thresholds (`H0`, `HABSMIN`, `HOFF`) control them, and how it interacts with bottom friction and momentum equations.

수심 하한(clamp)을 제거해 천해 노드가 다수 활성화되는 메시에서는 wet/dry 거동이 특히 중요해진다.

## A. NOLIFA flag effect

- `IFNLFA = 0` only when `NOLIFA=0`; for `NOLIFA=1` and `NOLIFA=2`: `IFNLFA=1` at `[file=src/adcirc.F line=286-290]`
  → Both `NOLIFA=1` and `=2` use nonlinear depth `H = DP + IFNLFA*ETA`
- **Wet/dry hard-gated to `NOLIFA=2`**: `computeWettingAndDrying` returns immediately if not 2 at `[file=src/wetdry.F line=204-206]`
- `IFNLFA` used in matrix terms (`DPAvg`, `H00`, `H0N*`): `[file=src/gwce.F line=506-507, 1318-1321, 2474, 2571-2573]`
- `NODECODE`/`NOFF` masking active only with `NOLIFA=2`: `[file=src/momentum.F line=312, 783-803]`

So:
| NOLIFA | Wet/dry? | Nonlinear depth (H = DP + ETA)? |
|--------|----------|--------------------------------|
| 0 | No | No |
| 1 | No | Yes (no node state changes) |
| 2 | Yes | Yes |

## B. H0 thresholds

- `H0` parsed by `READ_INPUT()` from fort.15 (referenced at `[file=src/adcirc.F line=227, 239]`)
- Computed during `initializeWettingAndDrying` at `[file=src/wetdry.F line=126-127]`:
  - `HABSMIN = 0.8 * H0` (drying threshold)
  - `HOFF = 1.2 * H0` (re-wetting / element-active threshold)
- D1 (drying) fires when `HTOT <= H0` at `[file=src/wetdry.F line=241-246, 271, 278]`; if `HTOT < HABSMIN`, ETA is clipped upward
- `HOFF` controls element activity (`NOFF`) and re-wetting checks at `[file=src/wetdry.F line=306, 370, 517, 664, 863-864, 1144-1202]`

## C. NODECODE (per-node wet/dry status)

- D1 update per timestep at `[file=src/wetdry.F line=234-285]` — currently wet (`NODECODE=1`) flips to dry when `HTOT <= H0`
- Wet→dry: both `NNODECODE` and `NODECODE` set to 0 immediately at `[file=src/wetdry.F line=274-275, 279-280]`
- Dry→wet (W1) requires:
  - Element has exactly two wet nodes (`NCTOT=2`) at `[file=src/wetdry.F line=354-355]`
  - Both wet nodes at/above `HOFF` at `[file=src/wetdry.F line=370, 517, 664]`
  - Computed velocity exceeds `VELMIN` at `[file=src/wetdry.F line=440-444]` (and symmetric branches at 515+, 662+)
- Final reconciliation: `NODECODE := NNODECODE` at `[file=src/wetdry.F line=1413-1417]` — committed flip point

## D. Velocity reset on dry nodes

- `VELMIN` enforced as activation criterion: `VEL > VELMIN` at `[file=src/wetdry.F line=440, 588, 734]`
- All-nodes-wet branches: `VEL := VELMIN` before `TK` formation at `[file=src/wetdry.F line=881, 946, 1011]` — prevents singularity
- Dry-node zeroing in momentum: `NCI=NODECODE(I)` multiplication at `[file=src/momentum.F line=714, 783-786, 799-803]`. With `NCI=0`, momentum collapses
- Explicit wet/dry-interface zeroing exists only as **commented-out code** at `[file=src/momentum.F line=1134-1137, 1897-1900]`

## E. Dry→wet recovery

- Primary path: 2-wet-node triangle (`NCTOT=2`) at `[file=src/wetdry.F line=354-355]`
- Activation gate: `HTOT >= HOFF (= 1.2*H0)` at `[file=src/wetdry.F line=370, 517, 664]`
- Final velocity check: hydraulic-gradient-derived `VEL > VELMIN` at `[file=src/wetdry.F line=440-444, 588-591, 734-737]`
- Optional all-three-wet activation: when all three element depths exceed `HOFF` at `[file=src/wetdry.F line=863-868, 932-933, 997-998]` (used to avoid stalled reactivation in fully shallow rising elements)

## F. Edge effects (front handling)

- `NODEDRYMIN` and `NODEWETMIN` are NOT in `wetdry.F`/`adcirc.F`/`gwce.F`/`momentum.F`. Search elsewhere for those.
- Wet/dry front via `MJU` (active attached elements) at `[file=src/wetdry.F line=1361-1377, 1387-1390]`:
  - Landlocked wet nodes are dried
  - `MJU` forced to ≥ 1 to keep momentum solve numerically safe
- Mass/flux coupling at fronts: `NCELE = NC1*NC2*NC3*NOFF(IE)` at `[file=src/wetdry.F line=1373]`, `[file=src/gwce.F line=477]`, `[file=src/momentum.F line=312]`
- Spurious oscillation guards:
  - Anti-flooding `NOFF` logic at `[file=src/wetdry.F line=1103-1162]`
  - Single-node connectivity suppression at `[file=src/wetdry.F line=1209-1230]`
  - Nonnegative `DELETA` clamp at `[file=src/wetdry.F line=1242-1289]`
  - Slope-limited gravity (`ALPHAL`) in GWCE at `[file=src/gwce.F line=515-516]`

## G. Friction interaction

- Friction terms (`TK0/TK/TK2`) computed at all nodes without explicit `NODECODE` IF guard at `[file=src/gwce.F line=2477-2482]`
- But friction effect is switched off on dry nodes via momentum's `NCI=NODECODE` multiplication at `[file=src/momentum.F line=714, 751-753, 783-786]`
- During wetting checks, `FRIC` is recomputed (Manning→Cd conversion + lower bound) at `[file=src/wetdry.F line=397-408, 543-553, 690-700]`

## Decision Guide — H0 selection (수심 하한별)

| Bathymetry minimum | Recommended H0 | Why |
|-------------------|----------------|-----|
| ~5m (수심 하한 강제 시) | H0=0.5 → 1.0 (or any) | Wet/dry never fires |
| ~0.5-1m (자연 천해) | **H0=0.05 → 0.1** | Standard ADCIRC default; allows correct shallow flow |
| 음수 가능 (조간대) | H0=0.1, with `NODEDRYMIN`/`NODEWETMIN` tuning | Allows true intertidal dynamics |

수심 하한(5m clamp)을 제거한 메시:
- **Set `H0=0.1`** in fort.15
- Verify `HOFF=0.12` (auto from `1.2*H0`)
- 다수의 천해 노드가 정상적으로 wet/dry에 참여
- Without this, those nodes get treated as permanently dry

## Working Rules

1. **`HABSMIN = 0.8*H0`, `HOFF = 1.2*H0`** are hard-coded ratios. To tighten/loosen wet/dry, change `H0` itself.
2. **`NCELE` masking is multiplicative** — once `NODECODE=0`, that node's contribution to all matrix terms is zero (no special branch).
3. **Re-wetting needs neighbor support** — isolated dry node with rising water can't self-activate; needs at least 2 wet neighbors at `HOFF`.
4. **`VELMIN` is the velocity trigger** for re-wetting — defaults to small (~0.001 m/s); too high prevents re-wetting.
5. **Friction recomputed during wetting checks** — Manning conversion happens twice (assembly + wet check) — slight inefficiency but correct.

## Common Pitfalls

- **`NOLIFA=1` thinking it has wet/dry** → no, only `NOLIFA=2` activates `computeWettingAndDrying`.
- **H0=5.0 with naturally-shallow bathymetry** → all shallow nodes always dry; tide can't propagate.
- **VELMIN=0.5 m/s** (way too high) → re-wetting never triggers; intertidal flats stuck dry.
- **Hot restart with different H0** → wet/dry state from old H0 frozen; mass artifacts.

## References

- `src/wetdry.F` — full wet/dry algorithm.
- `src/adcirc.F` — `IFNLFA` setup.
- `src/gwce.F` — `NCELE` masking in matrix assembly.
- `src/momentum.F` — `NCI` zeroing of dry-node momentum.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 35+ file:line citations |
| Coverage | NOLIFA dispatch, H0/HABSMIN/HOFF, NODECODE transitions, VELMIN, recovery, friction interaction |
| Review status | `review_required: true` |

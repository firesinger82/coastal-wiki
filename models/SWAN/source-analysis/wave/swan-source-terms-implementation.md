---
title: "swan source terms implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-source-terms-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-13 (recovery 대조 반영)
---

# SWAN source/sink terms — code-level implementation

## Scope note

How SWAN's source-term ledger `Stot = Sin + Sds,w + Snl4 + Snl3 + Sds,b + Sds,br` is actually integrated in the source code — which routine implements which formulation, the variable names, the implicit-vs-explicit splitting strategy per term, and the entry into the per-grid-point matrix `(IMATDA, IMATRA)`.

Companion to `swan-propagation-implementation.md` (which covers the propagation matrix). Together they describe the per-iteration solve.

## Source basis

- **Codex deep code analysis** of `models/swan/source_code/swan/src/{swancom1.ftn, swancom2.ftn, swancom3.ftn, swancom4.ftn, SdsBabanin.ftn90}` — 2026-05-06.
- **Manual cross-reference** from swantech ch.2.3 (Sources and sinks, pages 21–52).

## Implicit/explicit splitting principle

Each source term is split between matrix diagonal (`IMATDA`) and RHS (`IMATRA`). The convention:
- **`IMATDA`** = implicit contribution (multiplies the unknown `AC2` after solve)
- **`IMATRA`** = explicit contribution (adds directly to RHS, computed from prior `AC2`)

A common idiom — Patankar's positive-coefficient rule:
```
if S_local > 0:  IMATRA += S_local * AC2     # treat as positive source on RHS
else:            IMATDA += -S_local           # treat as positive sink on diagonal
```
This keeps the diagonal positive (stable for Thomas/SIP) regardless of source-term sign.

## A. Wind input (`Sin`)

원천항 조립 루틴은 `SOURCE`이다. (`src/swancom1.ftn:6823` `SUBROUTINE SOURCE`; `src/swancom1.ftn:7543` `compute nonlinear interactions, starting with triads`) [10-13 전수 검증 보완]

| Formulation | Routine | Routine file:line | Caller |
|-------------|---------|-------------------|--------|
| GEN1 / GEN2 | `WNDPAR` | `[file=src/swancom3.ftn line=30]` | `[file=src/swancom1.ftn line=7443]` |
ST6는 `MEMSINB`에 계산한 바람 입력을 저장한다. 저장 배열의 존재만으로 모든 계산이 반복당 한 번이라고 일반화하지 않는다. (`src/swancom1.ftn:7489` `CALL SWIND_DBYB`; `src/swancom1.ftn:7496` `CALL FILSIN`)
| GEN3 Snyder/Komen | `SWIND3` | `[file=src/swancom3.ftn line=1842]` | `[file=src/swancom1.ftn line=7454]` |
| GEN3 Janssen | `SWIND4` | `[file=src/swancom3.ftn line=2094]` | `[file=src/swancom1.ftn line=7464]` |
| GEN3 Yan / Westhuysen wind branch | `SWIND5` | `[file=src/swancom3.ftn line=2668]` | `[file=src/swancom1.ftn line=7475]` |
| Babanin / ST6 (`SWIND_DBYB`) | `SdsBabanin.ftn90:344` | (`SWIND_DBYB`) | `[file=src/swancom1.ftn line=7489]` |

Inputs each formulation reads (key variables): `WIND10, UFRIC, THETAW, ANYWND, AC2, KWAVE, SPCSIG, CGO, FPM` and parameter array `PWIND(*)`.

### Matrix accumulation per formulation
- `WNDPAR` — both branches: `IMATDA += SWIND_IMP`, `IMATRA += SWIND_EXP` `[file=src/swancom3.ftn line=512-513]`
- `SWIND0` — explicit only: `IMATRA += SWINEA` `[file=src/swancom3.ftn line=1782]`
- `SWIND3` — explicit only: `IMATRA += SWINEB * AC2` `[file=src/swancom3.ftn line=2061]`
- `SWIND4` — explicit only: `IMATRA += SWINEB * AC2` `[file=src/swancom3.ftn line=2623]`
- `SWIND5` — explicit only: `IMATRA += SWINEB * AC2` `[file=src/swancom3.ftn line=2881]`; `IWCAP=7` triggers Yan-coefficient adjustment `[file=src/swancom3.ftn line=2856]`
- ST6 (`SWIND_DBYB`) — explicit, RHS via `FILSIN`: `[file=SdsBabanin.ftn90 line=1584]` then `IMATRA += memsins` `[file=SdsBabanin.ftn90 line=1696]`

So **most GEN3 wind input is purely explicit** (added to RHS), while GEN1/GEN2 (`WNDPAR`) splits between implicit and explicit. Babanin/ST6 uses a memo-table pattern (`MEMSINB`) computed once and replayed per sweep.

## B. Whitecapping (`Sds,w`)

Dispatcher:
- `SWCAP` for `IWCAP <= 7` — `[file=src/swancom1.ftn line=7506]`
- `SWCAP8` for ST6 — `[file=src/swancom1.ftn line=7511]`

| Formulation | Code location |
|-------------|---------------|
| Komen-family coefficient `C_K` | `[file=src/swancom2.ftn line=2485-2491]` (uses `PWCAP(1,2,9,10,11), KM_WAM, ETOT`) |
| Battjes-Janssen WC coefficient `C_BJ` + `QB_WC` | `[file=src/swancom2.ftn line=2503-2511]` (uses `FRABRE, HM, HRMS, PWCAP(7)`) |
| Westhuysen / Alves-Banner saturation `B`, `FBR`, exponent `P` | `[file=src/swancom2.ftn line=2575-2592]` |
| Babanin / ST6 (`SWCAP8`) | `[file=src/swancom2.ftn line=2693]` with core `CALC_SDS` at `[file=src/swancom2.ftn line=2859]` |

### Matrix accumulation
- Implicit on diagonal: `IMATDA += WCAP(IS)` `[file=src/swancom2.ftn line=2645]` (and ST6 at `[file=src/swancom2.ftn line=2896]`)
- Optional explicit compensation (IWCAP 4/5): `IMATRA += WCIMPL * AC2` `[file=src/swancom2.ftn line=2661]`

So whitecapping is **primarily implicit** — gives positive contribution to diagonal which keeps the Thomas/SIP solve stable.

## C. Quadruplet (`Snl4`, DIA)

DIA setup and dispatch:
- λ-triangle setup (`LAMM2/LAMP2`, `DELTH3/DELTH4`, `DAL1/2/3`) in `FAC4WW`: `[file=src/swancom4.ftn line=245-253]`
- Variants `SWSNL1/2/3/4` for `IQUAD = 1/2/3/4`

Stencil and weighting (off-diagonal bins):
- Interaction stencil and AWG/SWG weights: `[file=src/swancom4.ftn line=1020-1037]`, `[file=src/swancom4.ftn line=1109-1127]`

### Variants and matrix split

| `IQUAD` | Method | Matrix split | file:line |
|---------|--------|-------------|-----------|
| 1 | Semi-implicit DIA | `IMATRA += SFNL/SIGPI`, `IMATDA -= DSNL/PI3` | `[file=src/swancom4.ftn line=1138-1139]` |
| 2 / 3 / 4 / 8 | Patankar split via `FILNL3` | positive to `IMATRA`, negative to `IMATDA` | `[file=src/swancom4.ftn line=2774-2779]`; same logic in `SWSNL2` `[file=src/swancom4.ftn line=1539-1544]` |

### Iteration / under-relaxation

- `IQUAD=3`은 `MEMNL4`에 저장한다. 첫 반복에서는 안정화를 위해 각 sweep에서 다시 계산한다. 이후에는 격자점의 첫 방문에서 계산한다. (`src/swancom1.ftn:7637` `IF ( ITER .EQ. 1 ) THEN`; `src/swancom1.ftn:7643`의 `CALL SWSNL3`; `src/swancom1.ftn:7663`의 `CALL FILNL3`)
- `IQUAD=4` MDIA (multiple DIA configurations): loop over `IDIA`, accumulate `MEMNL4` in `SWSNL4` (`IDIA==1` reset else add) — `[file=src/swancom4.ftn line=2328-2332]`, then `FILNL3` `[file=src/swancom1.ftn line=7692]`

## D. Triad (`Snl3`, LTA)

3파 목록에 FTIM/SPB와 공선·비공선 DCTA를 추가한다.

| 모델 | 호출 원문 |
|---|---|
| LTA | `src/swancom1.ftn:7556` `CALL SWLTA` |
| FTIM/SPB | `src/swancom1.ftn:7562` `CALL SWFTIM` |
| 공선 DCTA | `src/swancom1.ftn:7570` `CALL SWDCTA` |
| 비공선 DCTA | `src/swancom1.ftn:7576` `CALL SWDNCTA` |

Biphase usage:
- `SINBPH = SIN(-BIPH)` `[file=src/swancom4.ftn line=3964]`
- Biphase `BIPH` computed in `SINTGRL` `[file=src/swancom1.ftn line=5916-5937]`

Source contributions: `SA, SA3` then composite `STRI` at `[file=src/swancom4.ftn line=4028-4089]`.

### Matrix split

Patankar rule: `STRI > 0 → IMATRA`, else `→ IMATDA` `[file=src/swancom4.ftn line=4095-4102]`.

## E. Bottom friction (`Sds,b`)

Single dispatch routine `SBOT` at `[file=src/swancom2.ftn line=27]`, called from `[file=src/swancom1.ftn line=7338]`.

바닥 마찰 목록에 방향 퍼짐 보정과 잔물결 거칠기 경로를 추가한다. (swanuse PDF 74쪽 / 인쇄 66쪽, PDF 139쪽 / 인쇄 131쪽; `src/swancom2.ftn:386`·`src/swancom2.ftn:418`의 마찰 분기)

| `IBOT` | Method | Coefficient | file:line |
|--------|--------|-------------|-----------|
| 1 | JONSWAP | `CFBOT = PBOT(3) / GRAV²` | `[file=src/swancom2.ftn line=327-334]` |
| 2 | Collins | `CFBOT = CFW * UBOT / GRAV` (CFW from `FRCOEF` if VARFR else `PBOT(2)`) | `[file=src/swancom2.ftn line=340-346]` |
| 3 | Madsen | Newton-solve for `FW`, `CFBOT = UBOT * FW / (sqrt(2) * GRAV)` (roughness `AKN` from `FRCOEF` if VARFR else `PBOT(5)`) | `[file=src/swancom2.ftn line=350-386]` |

현재 JONSWAP CONSTANT 기본값은 0.038 m²/s³다. (`src/swanmain.ftn:1396` `PBOT(3)   = 0.038`)
JONSWAP VARIABLE은 방향 퍼짐에 따라 계수를 정한다. 공간 입력장은 별도 INPGRID FRICTION·READINP FRICTION 경로다. (swanuse PDF 74쪽 / 인쇄 66쪽, PDF 139쪽 / 인쇄 131쪽; `src/swancom2.ftn:408–416`의 `PBOT(6)`·`PBOT(7)` 보간)

### Per-bin dissipation
```
SBOTEO = CFBOT(IS) * (SPCSIG / SINH(KD))²
```
at `[file=src/swancom2.ftn line=520]`.

### Matrix accumulation
Implicit only on diagonal: `IMATDA += SBOTEO` `[file=src/swancom2.ftn line=538]`.

## F. Depth-induced breaking (`Sds,br`)

Battjes-Janssen breaker fraction routine `FRABRE` at `[file=src/swancom2.ftn line=1586]`, with `QBLOC` update at `[file=src/swancom2.ftn line=1763]`.

Surf-breaking source routine `SSURF` at `[file=src/swancom2.ftn line=1779]`, called from `[file=src/swancom1.ftn line=7401]`.

### α and γ application

- `α` (`PSURF(1)`) appears in `WS` formula: `[file=src/swancom2.ftn line=2113-2117]`
- `γ` enters via `HM = GAMBR * DEP2` (max wave height in shallow): `[file=src/swancom1.ftn line=5960]`, `[file=src/swancom1.ftn line=5982]`
- Default for `PSURF(2)` documented: `[file=src/swancom1.ftn line=7072]`

`QB` (fraction of waves currently breaking) computation path:
```
CALL FRABRE(HM, ETOT, QB(KCGRD(1)), KTETA)
```
at `[file=src/swancom1.ftn line=5999]`, then `QB_LOC = QB(KCGRD(1))` at `[file=src/swancom1.ftn line=6011]`.

### Matrix accumulation
Both implicit and explicit:
- `IMATDA += SURFA1`
- `IMATRA += SURFA0 * AC2`

at `[file=src/swancom2.ftn line=2188-2190]`.

## G. Source-term assembly summary

| Term | Implicit (`IMATDA`) | Explicit (`IMATRA`) | file:line |
|------|---------------------|---------------------|-----------|
| Wind GEN1/2 (`WNDPAR`) | `SWIND_IMP` | `SWIND_EXP` | `[file=src/swancom3.ftn line=512-513]` |
| Wind GEN3 (`SWIND0/3/4/5`) | — | `SWINEA / SWINEB * AC2` | `[file=src/swancom3.ftn line=1782, 2061, 2623, 2881]` |
| Wind ST6 (`DBYB`) | — | `memsins` (via `FILSIN`) | `[file=SdsBabanin.ftn90 line=1696]` |
| Whitecapping | `WCAP` | `WCIMPL * AC2` (IWCAP 4/5) | `[file=src/swancom2.ftn line=2645, 2661]` |
| Bottom friction | `SBOTEO` | — | `[file=src/swancom2.ftn line=538]` |
| Depth breaking (`SSURF`) | `SURFA1` | `SURFA0 * AC2` | `[file=src/swancom2.ftn line=2188-2190]` |
| Quadruplet semi-implicit | `-DSNL/PI3` | `SFNL/SIGPI` | `[file=src/swancom4.ftn line=1138-1139]` |
| Quadruplet Patankar | (negative parts) | (positive parts) | `[file=src/swancom4.ftn line=2774-2779]` |
| Triad LTA | (negative `STRI`) | (positive `STRI`) | `[file=src/swancom4.ftn line=4095-4102]` |
| Solver under-relaxation (global) | `+ ALFA*SPCSIG` | `+ ALFA*SPCSIG*AC2` | `[file=src/swancom1.ftn line=6185-6187]` |

## Decision Guide — debugging source-term issues

| Symptom | Likely culprit | Where to look |
|---------|---------------|---------------|
| Hs grows without bound under wind | wind input explicit + no implicit dissipation | confirm `WCAP` is on (`IMATDA += WCAP`); check `PWCAP` values |
| Energy peak too peaky | quadruplet under-resolved or wrong DIA variant | check `IQUAD`; for stiff cases use `IQUAD=2` Patankar |
| Surf-zone Hs collapses too early | breaking γ too low | inspect `PSURF(2)` and `GAMBR` value at points |
| Long swells over-dissipated | bottom friction too high | for swell, switch to `FRICTION COLL` not JONSWAP default |
| Convergence stalls in stationary | solver-level under-relaxation off | check `ALFA` factor at `swancom1.ftn:6185-6187` |
| Triad term wrong sign | biphase computation error | dump `SINBPH` in `SWLTA` and verify against `BIPH` from `SINTGRL` |

## Working Rules

1. 원천항 조립 루틴은 `SOURCE`이다. 이 경로에서는 3파 계산 뒤에 4파 계산을 한다. 바닥·식생·진흙·얼음 등 추가 항도 활성 조건에 따라 먼저 조립한다. (`src/swancom1.ftn:7543` `compute nonlinear interactions, starting with triads`; `src/swancom1.ftn:7556`의 `CALL SWLTA`; `src/swancom1.ftn:7589`의 4파 계산)
2. The matrix split (implicit vs explicit) is a **stability vs accuracy** trade-off. Implicit on diagonal is rock-solid. Explicit on RHS allows positive feedback (wind input) but requires either limiter or implicit dissipation to balance.
3. 저장 배열의 존재만으로 모든 계산이 반복당 한 번이라고 일반화하지 않는다. ST6의 계산 시점은 최초 방향 조건을 따른다. (`src/swancom1.ftn:7424–7427` `IF ( SWPDIR .EQ. 1 .OR.`, `(SWPDIR .EQ. 2 .AND. IX .EQ. 1) .OR.`, `(SWPDIR .EQ. 3 .AND. IY .EQ. 1) .OR.`, `(SWPDIR .EQ. 4 .AND. (IX.EQ.MXC .AND. IY.EQ.1)) )`)
   `IQUAD=3`은 첫 반복에서 각 sweep의 SOURCE 방문마다 계산한다. 이후 반복에서는 인용한 SWPDIR·경계점 조건을 만족할 때 계산한다. (`src/swancom1.ftn:7637` `IF ( ITER .EQ. 1 ) THEN`; `src/swancom1.ftn:7648–7651`의 조건)
4. `IMATDA` should remain positive (stable). If it goes negative, look for: a missing implicit dissipation term, or a Patankar-rule violation in custom code.

## Common Pitfalls

- **GEN3 with all options off** — explicit-only wind input + no whitecapping → unbounded growth + limiter clamping forever. Always pair `GEN3` with `WCAP`.
- JONSWAP VARIABLE은 방향 퍼짐에 따라 계수를 정한다. 공간 입력장은 별도 INPGRID FRICTION·READINP FRICTION 경로다. (swanuse PDF 74쪽 / 인쇄 66쪽, PDF 139쪽 / 인쇄 131쪽)
- **Quadruplet with `IQUAD=1` on a stiff spectrum** — semi-implicit DIA can oscillate. Switch to Patankar `IQUAD=2`.
- **Computing wave biphase outside `SINTGRL`** in custom modifications — the biphase pipeline shares state; bypassing it gives wrong triad sign.

## Next expansion

- [swan-st6-babanin-implementation](../swan-st6-babanin-implementation.md) — ST6 내부식
- [swan-whitecapping](../swan-whitecapping.md) — 백파·너울 소산
- The `SINTGRL` dispatcher itself (it integrates over spectrum to produce ETOT, biphase, QB; central to many terms).

## References

### Source files (Codex deep scan, 2026-05-06)

- `src/swancom1.ftn` — `SOURCE` 원천항 조립 루틴. (`src/swancom1.ftn:6823` `SUBROUTINE SOURCE`; `src/swancom1.ftn:7543` `compute nonlinear interactions, starting with triads`) [10-13 전수 검증 보완]
- `src/swancom2.ftn` — `SBOT` (bottom friction), `SSURF` (breaking), `SWCAP/SWCAP8` (whitecapping), `FRABRE`.
- `src/swancom3.ftn` — wind input family (`WNDPAR`, `SWIND0/3/4/5`).
- `src/swancom4.ftn` — quadruplet (`SWSNL1/2/3/4`, `FAC4WW`, `FILNL3`) and triad (`SWLTA`).
- `src/SdsBabanin.ftn90` — ST6/Babanin wind input + whitecapping.
- Inventory: `[file=models/swan/manuals/refs/subroutines.md]`.

### Manual cross-reference

- `[file=pdf:swan:swantech]` ch.2.3 (Sources and sinks), pages 21–52:
  - 2.3.1 Wind input formulations (Snyder/Komen, Janssen, Yan, ST6).
  - 2.3.2 Whitecapping (Hasselmann, Westhuysen, ST6).
  - 2.3.3 Bottom friction (JONSWAP, Madsen, Collins).
  - 2.3.4 Depth-induced breaking (Battjes-Janssen).
  - 2.3.5 Quadruplet (DIA).
  - 2.3.6 Triad (LTA).
- `[file=website:swan:node13]` — Activation of physical processes (per-process flag matrix).
- `[file=website:swan:node28]` — Physics overview command.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex source scan | 60+ file:line citations across 5 파일(`swancom1`·`swancom2`·`swancom3`·`swancom4`·`swancom5`) |
| Coverage | all source/sink terms — wind, whitecapping, quadruplet, triad, friction, breaking; matrix assembly per term |
| Out of scope (companion notes) | individual ST6/Babanin internals, `SINTGRL` integrator details, saturation-based dissipation specifics |
| Review status | `review_required: true` |


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R5](../../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md) · [R7](../../../../_staging/recovery/compare/swan-implementation-history-vs-code.md) · [R8](../../../../_staging/recovery/flow/SWAN-callflow.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-361 | DIA의 수치 구현: 3.6 · swantech PDF 96쪽 / 인쇄 88쪽, `calculated in every iteration prior to the first sweep`; `stored in internal memory`. | swantech PDF 96쪽 / 인쇄 88쪽, `calculated in every iteration prior to the first sweep`; `stored in internal memory`. | `src/swancom1.ftn:7637` `IF (ITER.EQ.1) THEN`; `src/swancom1.ftn:7643` 의 `CALL SWSNL3`; 7648의 첫 방문 조건; `src/swancom1.ftn:7653` 의 `CALL SWSNL3`; `src/swancom1.ftn:7663` 의 `CALL FILNL3` | C | `IQUAD=3`은 `MEMNL4`에 저장한다. 첫 반복에서는 안정화를 위해 각 스윕에서 다시 계산한다. 이후에는 격자점의 첫 방문에서 계산한다. 모든 격자점에 대해 첫 스윕 전에 일괄 계산한다는 뜻으로 구현을 설명하면 틀린다. |
| R2:SS-362 | DIA의 수치 구현: 3.6 · swantech PDF 96쪽 / 인쇄 88쪽, `two different numerical schemes ... a semi-implicit scheme and a fully explicit scheme`. | swantech PDF 96쪽 / 인쇄 88쪽, `two different numerical schemes ... a semi-implicit scheme and a fully explicit scheme`. | `src/swancom1.ftn:7604` `IF (IQUAD.EQ.1) THEN`; `src/swancom1.ftn:7609` 의 `CALL SWSNL1`; `src/swancom1.ftn:7618` 의 `ELSE IF (IQUAD.EQ.2) THEN`; `src/swancom4.ftn:1544`의 `MAX(1.E-18,AC2(ID,I,KCGRD(1))*SIGPI)`. `src/swancom4.ftn:1539–1546`은 양의 `SFNL`을 우변에 더하고 음의 값을 현재 밀도로 나눠 대각에 더한다 | C | swantech PDF 96쪽 / 인쇄 88쪽의 semi-implicit·fully explicit 선택은 코드의 두 경로에 대응한다. fully explicit 경로도 음의 전달량을 현재 작용 밀도로 나눠 대각에 넣는다. C의 범위는 해당 절에 이 부호별 조립 처리가 생략된 점이다. 명칭만으로 전체 Jacobian 사용 여부나 저자의 의도를 정의하지 않는다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] | [10-13 전수 검증 정정]
| R2:SS-513 | DIA의 여러 사중항을 합하는 MDIA, 최근접 보간, 주파수 격자 밖의 진단 꼬리 | swantech PDF 26쪽 / 인쇄 18쪽은 MDIA를, 38/30은 최근접 보간과 진단 꼬리를 설명한다. swanuse PDF 72–73쪽 / 인쇄 64–65쪽는 `IQUAD` 선택을 설명한다. swanuse PDF 81쪽 / 인쇄 73쪽의 `LIMITER [ursell]`은 Ursell 수 상한에 따른 4파 비활성화를 설명한다. | `src/swancom1.ftn:7592`의 `URSELL(KCGRD(1)).LT.PTRIAD(3)`; `src/swancom1.ftn:7666` 의 `IQUAD.EQ.4`; 7674의 MDIA 반복; `src/swancom1.ftn:7695` 의 `IQUAD.EQ.8`; `src/swancom4.ftn:1447`의 진단 꼬리 대입 | C | MDIA·보간·꼬리·Ursell 제한의 존재를 문서 전체의 누락으로 세지 않는다. C는 swantech 3.6의 두 반복 방식 설명만으로는 이 선택별 호출과 합산 경로를 설명하지 못하는 점에 한정한다. 코드는 `URSELL(KCGRD(1)).LT.PTRIAD(3)` 조건과 선택한 `IQUAD` 경로를 함께 따른다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-508 | JONSWAP 계수를 방향 퍼짐으로 보간하는 `IBOT=4` | swanuse PDF 74쪽 / 인쇄 66쪽은 RIPPLES를 설명한다. 부록 C 139/131은 `JONswap VARiable`·`COLLins [cfw] [cfc]`를 제시한다. 웹 [modifications.htm](../../raw/manuals/website/modifications/modifications.htm):1329–1330은 방향 퍼짐에 의존하는 JONSWAP 변형을 명시한다. | `src/swancom2.ftn:404`의 방향 퍼짐; `src/swancom2.ftn:408–416` 의 `PBOT(6)`·`PBOT(7)` 보간; `src/swancom2.ftn:450` 의 `PHI`; `src/swancom2.ftn:475` 의 `((8.*RIPH**2)/RIPW)`; 491의 Swart 식; `src/swancom2.ftn:526` 의 `IBOT.EQ.2`·`ICUR.EQ.1`·`PBOT(1).GT.0.`; `src/swanmain.ftn:1394`는 `PBOT(1) = 0.0`이다 | C | 방향 퍼짐 보정·연흔 거칠기·흐름 계수 입력의 존재는 다른 문서에 있다. C는 swantech PDF 34–35쪽 / 인쇄 26–27쪽의 기본 마찰식 설명에 보간식과 가동상 계산 세부가 빠진 점이다. 흐름 효과 미고려 서술은 기본 `PBOT(1)=0`에 한정한다. `IBOT.EQ.2`·`ICUR.EQ.1`·`PBOT(1).GT.0.`인 선택 경로는 별도로 적는다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-523 | 진흙층의 파수·군속도 보정과 감쇠 | swanuse PDF 77쪽 / 인쇄 69쪽는 Ng (2000) 기반 `MUD`와 기본 밀도 1300·동점성계수 .0076을 명시한다. 웹 [modifications.htm](../../raw/manuals/website/modifications/modifications.htm):115–119는 점성 감쇠와 분산 관계·파수·군속도 변화를 설명한다. | `src/swanser.ftn:869` `IF ( KND.LT.10. .AND. DM.GT.1.E-5 ) THEN`; `src/swanser.ftn:870` `SBLTM = SQRT(2.*KINVISM/SIG(IS))`; `src/swanser.ftn:1003–1015` 의 `B1`·`B2`·`B3`; `src/swanser.ftn:1024` `DISS=-SBLTM*(BRP+BIP)*WK**2/(SINH(2.*WK*H_WDEPTH)+2.*WK*H_WDEPTH)`; `src/swanser.ftn:1025` `WKDR=WK-BR*WK/(SINH(WK*H_WDEPTH)*COSH(WK*H_WDEPTH)+WK*H_WDEPTH)`; `src/swancom2.ftn:1331` `SMUDWD = 2. * DMW(IS,1) * CGMUD(IS,1)` | C | 진흙 감쇠와 파수·군속도 보정의 존재는 사용자 매뉴얼과 웹 문서에 있다. C는 swantech 2.3에 독립 진흙 절과 인용한 Ng 계산식·`KND.LT.10. .AND. DM.GT.1.E-5` 조건이 없는 점이다. `SMUD`는 $S_N=-2k_i c_{g,mud}N$에 해당하는 소산을 대각에 넣는다. 밀도 $1300\,kg/m^3$와 동점성계수 $.0076\,m^2/s$는 swanuse와 실제 대입(`src/swanmain.ftn:1406–1407`)이 일치한다. `src/swmod1.ftn:2365`의 `.0027`은 대입과 다른 코드 내부 설명이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-540 | 선택적 난류점성 소산 | swanuse PDF 79쪽 / 인쇄 71쪽과 웹 [swanuse/node28.html](../../raw/manuals/website/online_doc/swanuse/node28.html):1957–2013은 TURBULENCE와 CURRENT 입력을 설명한다. | `src/swancom2.ftn:1155` `IF (VISCLOC .GT. 0.) THEN`; `src/swancom2.ftn:1156` `IF (ITURBV.EQ.1) THEN`; `src/swancom2.ftn:1162–1164` 의 `CVISC` 및 `MIN(30.,XKD)` | C | 지정된 2.3의 번호식에는 이 원천항이 없다. 양의 입력 점성과 활성화 조건을 모두 요구한다. 쌍곡함수 인수는 30으로 제한한다. C는 swantech 2.3에 해당 소산식과 쌍곡함수 인수의 30 제한이 없는 점이다. 난류 점성 기능 자체는 사용자 매뉴얼에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-737 | 노트 · source-analysis/wave/swan-source-terms-implementation.md:194 | `source-analysis/wave/swan-source-terms-implementation.md:194` `SBOT → SSURF → SWIND0 → WNDPAR → SWCAP → quadruplets → triads`. | `src/swancom1.ftn:7543` `compute nonlinear interactions, starting with triads`; 7556·7562·7570·7576의 3파 호출 뒤 7589의 4파 계산 | B | 원천항 조립 루틴은 `SOURCE`이다. 이 경로에서는 3파 계산 뒤에 4파 계산을 한다. 바닥·식생·진흙·얼음 등 추가 항도 활성 조건에 따라 먼저 조립한다. |
| R2:SS-738 | 노트 · source-analysis/wave/swan-source-terms-implementation.md:106 | `source-analysis/wave/swan-source-terms-implementation.md:106` `Single routine:` 뒤의 `SWLTA`; 122 `Three formulations`. | `src/swancom1.ftn:7562` `CALL SWFTIM`; `src/swancom1.ftn:7570` `CALL SWDCTA`; `src/swancom1.ftn:7576` `CALL SWDNCTA`; `src/swancom2.ftn:386`·418의 마찰 분기 | C | 3파 목록에 FTIM/SPB와 공선·비공선 DCTA를 추가한다. 바닥 마찰 목록에 방향 퍼짐 보정과 잔물결 거칠기 경로를 추가한다. [10-13 결론 검증 보완] |
| R2:SS-739 | 노트 · source-analysis/wave/swan-source-terms-implementation.md:196 | `source-analysis/wave/swan-source-terms-implementation.md:196` `computed once per iteration and replayed per sweep`. | `src/swancom1.ftn:7637`의 첫 반복 DIA 분기; 7424–7427의 ST6 계산 시점 | C | 저장 배열의 존재만으로 모든 계산이 반복당 한 번이라고 일반화하지 않는다. 배열별 갱신 조건과 첫 반복 예외를 적는다. |
| R5:PN-181 | 마찰 기본값·VARIABLE 뜻 | `source-analysis/swan-command-file-reference.md:216` `FRICTION JONSWAP CONSTANT 0.067`, `= default` | `src/swanmain.ftn:1396` `PBOT(3)   = 0.038` | B | JONSWAP CONSTANT 기본값은 0.038이다. VARIABLE은 방향 퍼짐에 따른 계수 선택이다. 공간 입력장과 구분한다. |
| R7:H-219 | 빠른 DIA | `website/modifications/modifications.htm:219` `A fast version of the DIA approximation for quadruplets is included. Neighbouring interactions are interpolated in a piecewise constant manner instead of linear one. Moreover, the DIA calculation is carried out in the full spectral circle per iteration (instead of a quadrant per iteration). As a result, a significant speed-up in the computation can be obtained. Use of this technique can be realised by setting QUAD IQUAD = 8. This approach has almost no effect on the model results compared to the default method (IQUAD = 2).`; `website/online_doc/swantech/node45.html:52–63`은 매 반복의 첫 sweep 전에 계산한다고 설명한다. | `src/swancom1.ftn:7703` `IF ( ITER .EQ. 1 ) THEN`; `src/swancom1.ftn:7705–7711`은 첫 반복의 매 sweep에서 SWSNL8을 호출한다. 7713–7716행: `ELSE IF ( ITER .GT. 1 .AND. ( SWPDIR .EQ. 1 .OR.` / `     &        ( SWPDIR .EQ. 2 .AND. IX .EQ. 1) .OR.` / `     &        ( SWPDIR .EQ. 3 .AND. IY .EQ. 1) .OR.` / `     &        ( SWPDIR .EQ. 4 .AND. (IX.EQ.MXC .AND. IY.EQ.1)) )) THEN` | C 문서 누락 | IQUAD=8은 전체 방향의 상호작용을 계산한다. `IF ( ITER .EQ. 1 ) THEN` 분기는 매 sweep에서 SWSNL8을 호출한다. 이후 반복은 인용한 SWPDIR·IX·IY 조건에서 갱신한다. C는 수정 이력과 swantech의 반복 설명이 이 첫 반복·경계점 조건을 생략한 부분이다. [10-13 결론 검증 보완] |
| R7:H-755 | triad가 quad·limiter를 끔 | `website/modifications/modifications.htm:755` `The primary task of the limiter is to stabilize the quadruplet wave-wave interactions (as approximated by the DIA). However, in SWAN 30.75, it also but unduly dampened the triad wave-wave interactions. If in SWAN 40.01 these triad interactions are active the quadruplet interactions and the limiter are de-activated. The coefficients of the triad interactions have been given correspondingly new default values.`; `website/modifications/modifications.htm:616,645–654`은 40.31의 triad·quadruplet 동시 활성화와 쇄파 때 limiter 유지를 기록한다. | `src/swancom1.ftn:7630` `ELSE IF ( IQUAD .EQ. 3) THEN`; 이력: `122b595:src/swancom1.ftn:7547` `ELSE IF ( IQUAD .EQ. 3) THEN`; `122b595:src/swancom1.ftn:3742` `CALL PHILIM (AC2, SWMATR(1,1,JAOLD),                        40.31 40.16`; `src/swancom1.ftn:3791–3794`에서 `IF (PNUMS(20).LT.100.) THEN`, `IF (IWIND.NE.4 .OR. NSTATC.NE.1) THEN` 조건으로 PHILIM을 호출한다 | A 판 차이 | 40.01의 triad 활성 시 quadruplet·limiter 비활성화 규칙은 후속 40.31에서 바뀌었다. 41.45 코드 `122b595`(2023-02-28)와 현재 코드 `43e9bbb`(2026-07-13)는 두 상호작용의 계산 경로를 유지한다. 현재 limiter 호출도 별도 조건으로 남아 있다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R8:T1-008 | 정렬 전 방향 DIA의 생산 시점 | swantech PDF 96쪽·인쇄 88쪽: “the interactions are calculated in every iteration prior to the first sweep”. 웹 `website/online_doc/swantech/node45.html:52–62`도 첫 sweep 전 계산과 저장을 설명한다. | `src/swancom1.ftn:7630` `ELSE IF ( IQUAD .EQ. 3) THEN` 안의 `src/swancom1.ftn:7637` `IF ( ITER .EQ. 1 ) THEN`은 `src/swancom1.ftn:7643`에서 SWSNL3를 호출한다. `src/swancom1.ftn:7648–7651`의 다른 조건은 `ELSE IF ( ITER .GT. 1 .AND. ( SWPDIR .EQ. 1 .OR.`<br>`&        ( SWPDIR .EQ. 2 .AND. IX .EQ. 1) .OR.`<br>`&        ( SWPDIR .EQ. 3 .AND. IY .EQ. 1) .OR.`<br>`&        ( SWPDIR .EQ. 4 .AND. (IX.EQ.MXC .AND. IY.EQ.1)) )) THEN`이며 `src/swancom1.ftn:7653`에서 SWSNL3를 호출한다. `src/swancom1.ftn:7639–7641`은 첫 반복 매 sweep 계산을 안정성 조치로 설명한다 | B | 정렬 IQUAD=3은 격자점의 SOURCE 호출 안에서 전 방향 원천항을 계산해 MEMNL4에 저장한다. 첫 반복에서는 각 sweep의 SOURCE 방문마다 계산한다. 이후 반복에서는 인용한 SWPDIR·경계점 조건을 만족할 때 계산한다. 전 영역의 원천항을 첫 sweep 전에 선계산한다는 설명과 다르다. 코드의 `:7634–7635` 주석도 “prior to every iteration”이라고 적지만 실행문은 점별 호출이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |

---
title: "efdc wetdry"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_wetdry.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

## Scope

How EFDC+ identifies wet/dry cells, what the `HDRY`, `HWET` thresholds actually do, how `LMASKDRY` and the face switches `SUB/SVB/SBX/SBY` propagate dry status into the momentum and continuity solves, how the iteration up to 500 closes mass at the front, and how isolated-cell drainage interacts with subgrid-channel coupling. Use this when debugging mass-balance errors, intermittent BC drying (`LOPENBCDRY`), or oscillating wet/dry boundaries.

## Source basis

- `input.f90:269-298, 570-592` — `ISDRY`, `HDRY/HWET` reads, derived `HDRYICE/HDRYWAV`.
- `mod_var_global.f90:60, 841, 1049, 1054` — `LMASKDRY` definition, `ISDRY/HDRY/HWET` doc.
- `calpuv9c.f90` — primary wet/dry algorithm (`:130, 138, 146, 161, 177, 345, 353, 358, 400, 501, 521, 607-631, 641, 724, 752, 804-846, 861, 869, 892-1080, 1156, 1213-1379, 1454-1843`).
- `caluvw.f90:240-270, 939-1052` — velocity reset on dry cells.
- `calexp.f90:750, 1104` — wet-cell list refresh, newly wet damping.
- `Transport/caltran.f90:165-325` — `ISTL` and `LMASKDRY` use in tracer.
- `subchan.f90:12-125` — subgrid channel coupling.
- `Transport/calqvs.f90:787-1899` — withdrawal limits.
- `setopenbc.f90:221, 295-620` — `LOPENBCDRY`.

## A. ISDRY flag

- Read from card C5 (`input.f90:269`) and broadcast (`:272`).
- 음의 ISDRY 입력은 절댓값으로 바뀐다. (`input.f90:292` — `if( ISDRY < 0 )then`; `input.f90:293` — `ISDRY = ABS(ISDRY)`) 이 분기는 IDRYTBP=1을 설정한다. (`input.f90:294` — `IDRYTBP = 1`)
- ISRLID=1이면 코드는 ISDRY=−1을 설정한다. (`input.f90:298` — `if( ISRLID == 1) ISDRY = -1`)
- Definition: `0` = off, `>0` = wetting/drying active (`mod_var_global.f90:841`).

Major gates:
- `CALPUV9C`: face switching, dry checks, mask creation (`:161, 177, 892, 1277, 1455`).
- `SETOPENBC`: open-BC drying behavior (`setopenbc.f90:221, 323`).
- `Transport/calqvs.f90:509, 1748` — source/sink redistribution and withdrawal limits.
- `CALEXP`: wet-list filtering (`calexp.f90:750, 1104`).
- `CALTRAN`: consults `LMASKDRY` and wet lists (`Transport/caltran.f90:167, 228`).

## B. HDRY vs HWET

Read from card C11 (`input.f90:570-592`). Derived: `HDRYICE`, `HDRYWAV`.

- `HDRY` = wet/dry control depth (`mod_var_global.f90:1049`). Drying triggered when `HP < HDRY` or `HP <= HDRY` (`calpuv9c.f90:899, 935`).
- `HWET` = minimum operational depth for QSER withdrawals and structures, **not** the central rewetting threshold (`mod_var_global.f90:1054`).

HWET은 면 깊이 하한에도 쓰인다. (`calpuv9c.f90:1656` — `HU(L) = max(HU(L),HWET)`; `calpuv9c.f90:1768` — `HV(L) = max(HV(L),HWET)`)


Standard wet/dry mode (`ISDRY != 99`) closes all four cell faces when `HP < HDRY` and the cell isn't recovering fast enough (`calpuv9c.f90:905, 912`).

`ISDRY == 99` mode allows rewetting if depth is rising fast enough and adjacent wet faces exist (`:950, 965, 968`). This is the typical choice for tidal flats.

`HWET` use points:
- Minimum withdrawal depth (`Transport/calqvs.f90:787, 862`).
- Hydraulic structure floor (`mod_hydstructure.f90:263`).
- Face-depth floor (`calpuv9c.f90:1656, 1768`).

## C. LMASKDRY (.TRUE. = wet)

- Initialized wet (`ainit.f90:132`).
- Active mask built in `CALPUV9C`:
  1. All local cells set wet first.
  2. A cell with `HP < HDRY` is marked dry **only after** all four faces have been closed for both previous and current face switches (`calpuv9c.f90:1277, 1284, 1292, 1300`).

2TL CALPUV2C도 이전·현재 면 스위치가 닫힌 조건에서 LMASKDRY를 FALSE로 설정한다. (`calpuv9c.f90:1300` — `LMASKDRY(L) = .FALSE.`; `calpuv2c.f90:1213` — `LMASKDRY(L) = .FALSE.`)

- `LWET/LDRY` lists rebuilt from `LMASKDRY` (`:1454, 1462`).

This four-face requirement prevents premature drying: a cell still receiving flow through any face stays wet.

Consultation points:
- CALEXP는 이번 외부 모드의 목록 갱신 전에 목록을 읽는다. (`hdmt2t.f90:619` — `call CALEXP2T`; `hdmt2t.f90:627` — `call CALPUV2C`; `calexp.f90:750` — `if( ISDRY > 0 .and. LADRY > 0 )then`; `calpuv2c.f90:1340` — `LWET(LAWET) = L`; `calpuv2c.f90:1345` — `LDRY(LADRY) = L`; `Transport/caltran.f90:228` — `if( LKSZ(L,K) .or. .not. LMASKDRY(L) ) CYCLE`) 외부 모드는 LMASKDRY와 습윤·건조 목록을 갱신한다. (`Transport/caltran.f90:228` — `if( LKSZ(L,K) .or. .not. LMASKDRY(L) ) CYCLE`) 후속 CALUVW와 수송은 새 목록을 읽는다. (`hdmt2t.f90:619` — `call CALEXP2T`; `hdmt2t.f90:627` — `call CALPUV2C`; `calexp.f90:750` — `if( ISDRY > 0 .and. LADRY > 0 )then`; `calpuv2c.f90:1340` — `LWET(LAWET) = L`; `calpuv2c.f90:1345` — `LDRY(LADRY) = L`; `Transport/caltran.f90:228` — `if( LKSZ(L,K) .or. .not. LMASKDRY(L) ) CYCLE`)
- `CALPUV`: `LMASKDRY` → `LWET, LDRY, LKWET, LLWET` drive subsequent loops (`calpuv9c.f90:1462, 1521, 1843`).
- `CALTRAN`: open-BC tracer skips inactive layers / dry cells via `.not. LMASKDRY(L)` (`Transport/caltran.f90:228, 261, 293, 325`).

## D. ISTL interaction

`ISTL` is the time-step level selector:
- Normal 2TL → `ISTL=2`.
- 3TL → `ISTL=3` for standard step, `ISTL=2` for trapezoidal correction (`mod_var_global.f90:72`).

In `CALPUV9C`:
- `DELT/DELTD2` adjusted by `ISTL` (`:130`).
- Wet/dry transition tests compare `HP` against `H2P` for `ISTL==3` or `H1P` for `ISTL==2` (`:899, 943`).
- Previous-state arrays advanced only on `ISTL==3` (`:501, 521`).

In `CALTRAN`: `ISTL` chooses `H1PK` vs `H2PK` in advective update (`Transport/caltran.f90:165, 179`).

## E. Volume / mass conservation at the front

The pressure equation includes source/sink terms and face-flow divergence using active `SUB/SVB` switches (`calpuv9c.f90:607, 609`).

습윤건조 상태가 바뀌면 외부 모드는 해법을 반복한다. (`calpuv2c.f90:997` — `if( ICORDRY_Global > 0 )then`; `calpuv2c.f90:1001` — `if( NCORDRY < 500  )then`; `calpuv2c.f90:1002` — `GOTO 1000`; `calpuv2c.f90:1015` — `call STOPP('*** NCORDRY > 500 WHEN ISDRY > 0')`) 반복 한도에 도달하면 STOPP를 호출한다. (`calpuv2c.f90:1015` — `call STOPP('*** NCORDRY > 500 WHEN ISDRY > 0')`) 이 반복의 질량 보존은 모델 실행으로 확인하지 않음. (`calpuv2c.f90:1015` — `call STOPP('*** NCORDRY > 500 WHEN ISDRY > 0')`)

**Isolated-cell drainage**: After `NDRYSTP` isolated steps, a cell can be forced to `0.90 * HDRY`; removed volume tracked as `QDWASTE` and accumulated in `VDWASTE` (`:1156, 1213, 1227`). Logged then zeroed unless mass balance output uses it (`:1363, 1379`).

고립 셀 제거량의 전역 질량 보존 영향은 모델 실행으로 확인하지 않음. (`calpuv9c.f90:1156` — `! *** CHECK IF ISOLATED CELL WATER NEEDS TO BE REMOVED`; `calpuv9c.f90:1213` — `! *** SUM VOLUME OF "WASTED" WATER`; `calpuv9c.f90:1227` — `QDWASTE(L) = DELTI*DXYP(L)*(HOLDTMP-HP(L))`)


So: wet/dry pressure iteration is **conservative across active faces**, but isolated-cell drying can **intentionally remove a tracked volume**.

Withdrawal limits:
- Hydraulic controls limit `QCTLT` by `(HP − HDRY) * area / dt` (`Transport/calqvs.f90:1242`).
- General outflows shut off / scale when `HP < HWET` (`Transport/calqvs.f90:1751, 1776`).

## F. Velocity reset on dry cells

Newly dry cells move from `LMASKDRY` to `LDRY` (`calpuv9c.f90:1466`). `CALUVW` then zeros dry-cell momentum / velocity arrays (`caluvw.f90:240, 256, 258, 263, 270`).

If continuity check predicts negative depth in shallow wet/dry cell, `CALUVW` resets local external flows and layer velocities to zero (`:939, 949, 954, 967`); `ISTL==2` branch mirrors (`:1033, 1044, 1052`).

## G. Element-face deactivation

Face switches: `SUB/SBX` (U/east-west), `SVB/SBY` (V/north-south).

- Open BCs that dry: zero current cell + adjacent east/north face switches and external flows (`calpuv9c.f90:827, 829, 837`).
- Normal drying: zero `SUB(L), SUB(LE), SVB(L), SVB(LN)` plus `SBX/SBY` (`:910, 912`).
- Reopening: neighbor water-surface comparison; restore from `SUBO/SVBO/SBXO/SBYO` (`:345, 353, 358, 400`).
- Pressure matrix uses face switches in RHS divergence + coefficients (`:609, 623`).
- Final external face discharges multiplied by `SUB/SVB` (`:724`).
- 3D face masks rebuilt as `SUB3D = SUB * SUB3DO` (`:1351`).

## H. Subgrid channel (SUBCHAN)

Called from `CALPUV9C` and `CALPUV2C` (`subchan.f90:12`):
- `CALPUV9C` initializes previous channel flows with `ISTL` awareness (`calpuv9c.f90:138, 146`), then calls `SUBCHAN` before solving the external pressure system (`:641`).

SUBCHAN은 MDCHH>=1에서 외부 해법 전에 호출한다. (`calpuv9c.f90:642` — `if( MDCHH >= 1 )CALL SUBCHAN(QCHANUT,QCHANVT,IACTIVE,DELT)`; `calpuv2c.f90:598` — `call SUBCHAN(QCHANUT,QCHANVT,IACTIVE,DELT)`; `calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`) 단일 프로세스는 이 조건에서 CONGRADC를 호출한다. (`calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`)


`SUBCHAN` activation:
- Channel active **only if** donor side has previous depth `H1P > HDRY` (`subchan.f90:41, 51, 77, 90`).
- Disabled if either current depth is non-positive.
- Active channels add coupled coefficients to `CC` and source terms to `FP` (`:110, 113`).

After solve:
- Inactive channel flows reset to zero (`calpuv9c.f90:752`).
- Active channel exchanges applied as paired host/channel depth changes — conserving exchange between two cells (`:861, 869`).

## Decision Guide

| Domain feature | Setting |
|---|---|
| Tidal flats with regular wet/dry | `ISDRY=99`, `HDRY=0.05–0.1 m`, `NDRYSTP=10–50` |
| Stable shoreline, no real drying | C7는 NDRYSTP를 명시적으로 읽는다. (`input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`; `input.f90:397` — `NDRYSTP = ABS(NDRYSTP)   ! *** IF > 0, EFDC+ WILL WASTE ISOLATED CELL WATER AFTER NDRYSTP STEPS`; `calpuv2c.f90:1077` — `if( ISDRY > 0 .and. NDRYSTP > 0 )then`; `calpuv2c.f90:1090` — `NTMP = NDRYSTP`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:40` — `\* NDRYSTP: MIN NO. OF TIME STEPS A CELL REMAINS DRY AFTER INTIAL DRYING`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:42` — `\*                   -NDRYSTP FOR ISDRY=-99 TO ACTIVATE WASTING WATER IN DRY CELLS`; EFDC_Manual.pdf, PDF 24쪽·인쇄 20쪽) 코드는 입력의 절댓값을 사용한다. (`input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`; `input.f90:397` — `NDRYSTP = ABS(NDRYSTP)   ! *** IF > 0, EFDC+ WILL WASTE ISOLATED CELL WATER AFTER NDRYSTP STEPS`; `calpuv2c.f90:1077` — `if( ISDRY > 0 .and. NDRYSTP > 0 )then`; `calpuv2c.f90:1090` — `NTMP = NDRYSTP`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:40` — `\* NDRYSTP: MIN NO. OF TIME STEPS A CELL REMAINS DRY AFTER INTIAL DRYING`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:42` — `\*                   -NDRYSTP FOR ISDRY=-99 TO ACTIVATE WASTING WATER IN DRY CELLS`; EFDC_Manual.pdf, PDF 24쪽·인쇄 20쪽) NDRYSTP는 고립 셀의 물을 버리기 전 대기 단계 수다. (`input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`; `input.f90:397` — `NDRYSTP = ABS(NDRYSTP)   ! *** IF > 0, EFDC+ WILL WASTE ISOLATED CELL WATER AFTER NDRYSTP STEPS`; `calpuv2c.f90:1077` — `if( ISDRY > 0 .and. NDRYSTP > 0 )then`; `calpuv2c.f90:1090` — `NTMP = NDRYSTP`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:40` — `\* NDRYSTP: MIN NO. OF TIME STEPS A CELL REMAINS DRY AFTER INTIAL DRYING`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:42` — `\*                   -NDRYSTP FOR ISDRY=-99 TO ACTIVATE WASTING WATER IN DRY CELLS`; EFDC_Manual.pdf, PDF 24쪽·인쇄 20쪽) 확인한 .f90에서 NDRYSTP=50 기본 대입을 찾지 못했다. (`input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`; `input.f90:397` — `NDRYSTP = ABS(NDRYSTP)   ! *** IF > 0, EFDC+ WILL WASTE ISOLATED CELL WATER AFTER NDRYSTP STEPS`; `calpuv2c.f90:1077` — `if( ISDRY > 0 .and. NDRYSTP > 0 )then`; `calpuv2c.f90:1090` — `NTMP = NDRYSTP`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:40` — `\* NDRYSTP: MIN NO. OF TIME STEPS A CELL REMAINS DRY AFTER INTIAL DRYING`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:42` — `\*                   -NDRYSTP FOR ISDRY=-99 TO ACTIVATE WASTING WATER IN DRY CELLS`; EFDC_Manual.pdf, PDF 24쪽·인쇄 20쪽) |
| Rigid-lid (atmospheric pressure forcing only) | `ISDRY=-1` |
| Many isolated puddles producing `VDWASTE` warnings | Increase `NDRYSTP`, raise `HDRY`, or check bathymetry for unrealistic dimples |
| Tide gauge near dry land triggering `LOPENBCDRY` | Move BC further offshore, or accept intermittent BC closure |
| Subgrid channels (e.g., narrow tidal creeks) | `ISCHAN > 0` with `MODCHAN.INP` defining host/channel cell pairs |
| Mass balance closure required | Output `QDWASTE/VDWASTE` to monitor isolated-cell drainage |

## Working Rules

- `HDRY` should be larger than your typical free-surface noise (~3-5x). Too small → constant flicker; too large → too aggressive drying.
- The 500-iteration cap on wet/dry pressure solve is essentially conservation insurance; if you see warnings, the cell is in a numerically pathological state — usually fix bathymetry, not the cap.
- `ISDRY=99` is the production choice for tidal flats. Other modes are mostly legacy.
- `NDRYSTP` should be 10–50 timesteps; too small → spurious drainage of marginal cells; too large → permanent puddles.
- Open-BC drying (`LOPENBCDRY`) is logged in stdout — check log for "OPEN BC DRY" entries when validating tides; missing constituents at a station may mean the BC is silently disabled.
- Subgrid channel (`ISCHAN > 0`) requires donor-side `H1P > HDRY`; if both sides go shallow, the channel snaps off — this is by design but invisible without channel-flow output.

## Common Pitfalls

- HWET은 취수·구조물 조건에 쓰인다. (`calpuv9c.f90:1656` — `HU(L) = max(HU(L),HWET)`; `calpuv9c.f90:1768` — `HV(L) = max(HV(L),HWET)`) HWET은 면 깊이 하한에도 쓰인다. (`calpuv9c.f90:1656` — `HU(L) = max(HU(L),HWET)`; `calpuv9c.f90:1768` — `HV(L) = max(HV(L),HWET)`)
- ▢ Setting `HDRY < HWET` violates the model's assumption (`HWET` should always be >= `HDRY`).
- 사용자는 C7에 NDRYSTP를 입력한다. (`input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`; `input.f90:397` — `NDRYSTP = ABS(NDRYSTP)   ! *** IF > 0, EFDC+ WILL WASTE ISOLATED CELL WATER AFTER NDRYSTP STEPS`; `calpuv2c.f90:1077` — `if( ISDRY > 0 .and. NDRYSTP > 0 )then`; `calpuv2c.f90:1090` — `NTMP = NDRYSTP`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:40` — `\* NDRYSTP: MIN NO. OF TIME STEPS A CELL REMAINS DRY AFTER INTIAL DRYING`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:42` — `\*                   -NDRYSTP FOR ISDRY=-99 TO ACTIVATE WASTING WATER IN DRY CELLS`; EFDC_Manual.pdf, PDF 24쪽·인쇄 20쪽) 코드는 ABS(NDRYSTP)를 사용한다. (`input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`; `input.f90:397` — `NDRYSTP = ABS(NDRYSTP)   ! *** IF > 0, EFDC+ WILL WASTE ISOLATED CELL WATER AFTER NDRYSTP STEPS`; `calpuv2c.f90:1077` — `if( ISDRY > 0 .and. NDRYSTP > 0 )then`; `calpuv2c.f90:1090` — `NTMP = NDRYSTP`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:40` — `\* NDRYSTP: MIN NO. OF TIME STEPS A CELL REMAINS DRY AFTER INTIAL DRYING`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:42` — `\*                   -NDRYSTP FOR ISDRY=-99 TO ACTIVATE WASTING WATER IN DRY CELLS`; EFDC_Manual.pdf, PDF 24쪽·인쇄 20쪽) 고립 셀의 대기 단계가 끝나면 calpuv2c는 수심을 0.9*HDRY까지 줄이는 배수량을 계산한다. (`input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`; `input.f90:397` — `NDRYSTP = ABS(NDRYSTP)   ! *** IF > 0, EFDC+ WILL WASTE ISOLATED CELL WATER AFTER NDRYSTP STEPS`; `calpuv2c.f90:1077` — `if( ISDRY > 0 .and. NDRYSTP > 0 )then`; `calpuv2c.f90:1090` — `NTMP = NDRYSTP`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:40` — `\* NDRYSTP: MIN NO. OF TIME STEPS A CELL REMAINS DRY AFTER INTIAL DRYING`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md:42` — `\*                   -NDRYSTP FOR ISDRY=-99 TO ACTIVATE WASTING WATER IN DRY CELLS`; EFDC_Manual.pdf, PDF 24쪽·인쇄 20쪽)
- ▢ Using `ISDRY=1` (basic) for tidal flats — you'll see hysteresis as cells dry but won't rewet on the flood. Use `ISDRY=99`.
- ▢ Rigid lid (`ISDRY=-1`) with hot-start that had wetting/drying active — face mask states diverge.
- ▢ Subgrid channels with bathymetry where neither side stays wet at low tide — channel flips off silently; expected channel flow not produced.
- 2TL 외부 모드는 ISDRY>0이고 ICORDRY_Global 분기를 통과하지 않을 때 Communicate_PUV1을 호출한다. (`calpuv2c.f90:1019` — `elseif( ISDRY > 0 )then`; `calpuv9c.f90:1097` — `elseif( ISDRY > 0 )then`) 3TL 외부 모드도 같은 조건의 Communicate_PUV1을 호출한다. (`calpuv2c.f90:1019` — `elseif( ISDRY > 0 )then`; `calpuv2c.f90:1028` — `call Communicate_PUV1`; `calpuv9c.f90:1097` — `elseif( ISDRY > 0 )then`; `calpuv9c.f90:1105` — `call Communicate_PUV1`) 부분 영역 경계의 난류·퇴적물 출력 이상은 모델 실행으로 확인하지 않음. (`calpuv2c.f90:1019` — `elseif( ISDRY > 0 )then`; `calpuv2c.f90:1028` — `call Communicate_PUV1`; `calpuv9c.f90:1097` — `elseif( ISDRY > 0 )then`; `calpuv9c.f90:1105` — `call Communicate_PUV1`)

## Next expansion

- Mass-balance audit recipe (sum `QSUME`, `QDWASTE`, `VDWASTE`, integrated face fluxes).
- Subgrid channel sizing (`MODCHAN.INP` parameters) and when to use vs explicit narrow grid.
- ISDRY=99 vs ISDRY=1 quantitative comparison on tidal-flat case.

## References

- Hamrick 1992 (EFDC theoretical baseline).
- Casulli & Cheng 1992 (semi-implicit drying scheme references).
- EFDC+ Theory Documentation (Dynamic Solutions, 2020+).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.

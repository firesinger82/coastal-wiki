---
title: "swan time stepping implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-time-stepping-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN nonstationary time stepping — outer loop, AC1 swap, time-varying inputs

## Scope note

How SWAN advances through time in nonstationary mode: outer time loop wiring, `AC1 ↔ AC2` swap timing, time-varying input updates (wind/current/water level), boundary-spectrum time interpolation, output trigger logic, and CFL warning emission.

Companion to `swan-propagation-implementation.md` (per-iteration solve) and `swan-data-structures-implementation.md` (`AC1`/`AC2` definitions).

## Source basis

Codex deep scan 2026-05-06 of:
- `src/swanmain.ftn` — outer time loop, time advance, output dispatch
- `src/swanpre1.ftn` — `COMPUTE` parser, time-window storage
- `src/swancom5.ftn` — time-term in matrix
- `src/swanout1.ftn` — output triggering

## A. Outer time-step loop

`[file=src/swanmain.ftn line=571]`:
```fortran
DO 500 IT = IT0, MTC
  ...
500 CONTINUE
```

Initial condition:
- `IT0 = 0` for nonstationary (`NSTATC = 1`) — `IT=0` does an initial state update before the first `SWCOMP` call
- `IT0 = 1` for stationary (`NSTATC = 0`) — single iteration block

at `[file=src/swanmain.ftn line=544-562]`.

End-of-step time advance: `TIMCO = TIMCO + DT` for `IT < MTC` at `[file=src/swanmain.ftn line=688-693]`.

## B. COMPUTE parsing → loop wiring

Parser branches `[file=src/swanpre1.ftn line=875-905]`:
- Stationary: `DT = 1.E10`, `RDTIM = 0`, `MTC = 1` — no dynamic stepping at `[file=src/swanpre1.ftn line=888-891]`
- Nonstationary: read `TBEGC, DELTC, TENDC`; compute `DT = DELTC`, `RDTIM = 1./DT`, `MTC = NINT((TFINC-TINIC)/DT)`, `TIMCO = TINIC` at `[file=src/swanpre1.ftn line=903-905]`, `[file=src/swanpre1.ftn line=913-915]`, `[file=src/swanpre1.ftn line=919]`.

Storage in `RCOMPT` at `[file=src/swanpre1.ftn line=925-930]`: `NSTATC, MTC, TFINC, TINIC, DT`.

Runtime pulls: `SWREAD(COMPUT)` fills globals at `[file=src/swanmain.ftn line=394-400]`. The `IT` loop bound at `[file=src/swanmain.ftn line=571]` consumes parsed `MTC`. Per-step `SWCOMP` call at `[file=src/swanmain.ftn line=610]`, `[file=src/swanmain.ftn line=620-627]`.

## C. Time-term contribution in matrix

`[file=src/swancom5.ftn line=2177-2184]` — when `NSTATC=1`, the time term is added in implicit backward-Euler form:
```fortran
IMATRA(...) += ACOLD * RDTIM       ! = AC_old / DT to RHS
IMATDA(...) += RDTIM                ! = 1/DT to diagonal
```

`ACOLD` source at `[file=src/swancom5.ftn line=2179-2181]`:
- `ITERMX == 1`이면 갱신 전 `AC2`를 이전값으로 취한다. 이 선택은 음해법 시간차분을 명시법으로 바꾸는 의미가 아니다. `src/SwanTranspX.ftn90:146,149–150`의 원문은 `acold = ac1(id,is,iv1)`, `rhs (id,is  ) = rhs (id,is  ) + acold*RDTIM`, `amat(id,is,1) = amat(id,is,1) + RDTIM`이다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안).
- `ITERMX > 1` → `ACOLD = AC1(...)` (multi-iter, true old-time)

STRSXY의 시간항 외에 SANDL의 직전 단계 공간항과 SwanTranspX의 시간항도 AC1을 읽는다. `src/swancom5.ftn:2964`의 원문은 `+(0.25*RDX(1)) * (CAX1(ID,IS,2) * AC1(ID,IS,IND2)`이다. `src/SwanTranspX.ftn90:146`의 원문은 `acold = ac1(id,is,iv1)`이다.

## D. Time-varying inputs (wind/current/water level)

Inputs are updated **before** `SWCOMP` each step:
- `SNEXTI` runs first, then `SWCOMP` — at `[file=src/swanmain.ftn line=586-595]`, `[file=src/swanmain.ftn line=7020-7166]`
- Wind via `FLFILE(5,6,...)` — interpolated to `COMPDA(:, JWX2)`, `COMPDA(:, JWY2)` at `[file=src/swanmain.ftn line=7023-7029]`
- Water level via `FLFILE(7,0,...)` — depth fields recomputed from bathymetry + WL at `[file=src/swanmain.ftn line=7093]`
- Current via `FLFILE(2,3,...)` — Froude limiting after at `[file=src/swanmain.ftn line=7161-7166]`

### `FLFILE` time interpolation

`[file=src/swanmain.ftn line=8828-8850]`:
```fortran
W3 = (TIMCO - TIMR1) / (IFLTIM - TIMR1)
W1 = 1 - W3
COMPDA(:, J*2) = W1 * old + W3 * new
```
Vector quantities (wind, current) preserve magnitude with a correction term to avoid losing intensity through interpolation.

## E. Boundary update in nonstationary

- `SNEXTI` calls `RBFILE` for each boundary file every step (master rank), broadcasts `BSPECS` at `[file=src/swanmain.ftn line=6916-6919]`.
- In `RBFILE`, when `TIMCO > TIMF2` → read new spectra, shift prior "new" to "old" at `[file=src/swanmain.ftn line=7724-7754]`.
- Time interpolation weight `W1 = (TIMF2 - TIMCO) / (TIMF2 - TIMF1)`; spectra blend via `SINTRP(W1, 1-W1, old, new, ...)` at `[file=src/swanmain.ftn line=8033-8048]`.
- Spatial interpolation between two stored boundaries on the boundary side uses local `W1`/`W2` from `BGRIDP`; result written into `AC2` at `[file=src/swanmain.ftn line=6941-6946]`.

## F. Output writing per step

- `BLOCK`/`TABLE`/`SPECout` parse `TBEG` + `DELT` into `ORQTMP%OQR(1:2)` at `[file=src/swanpre2.ftn line=1486-1487]`, `[file=src/swanpre2.ftn line=1837-1838]`, `[file=src/swanpre2.ftn line=1961-1962]`.
- `SWOUTP` is called every step at `[file=src/swanmain.ftn line=677-680]`. Per-request gating decides write vs no-write.
- Trigger logic in `SWORDC` `[file=src/swanout1.ftn line=682-704]`:
  - Periodic: `OUTR(2) > 0` and `TIMCO >= TNEXT` → write, advance `OUTR(1) = TNEXT + OUTR(2)`
  - End-only: `OUTR(2) < 0` → write only when `|TFINC - TIMCO| < 0.5 * DT`
- Active dispatch to `SWBLOK`/`SWTABP`/`SWSPEC` at `[file=src/swanout1.ftn line=436-509]`.

**Output stride `DELT` is independent from compute stride `DELTC`** — explicit in trigger code at `[file=src/swanout1.ftn line=693-694]`.

## G. CFL / time-step warnings

`[file=src/swancom5.ftn line=2889-2894]` computes a CFL-like metric for higher-order propagation:
```fortran
MYU = ABS(DT * CGO(1,1) / MIN(DXMYU, DYMYU))
```

`[file=src/swancom5.ftn line=2893-2904]`: if `MYU > 10` and not warned yet, `MSGERR(2, ...)` emits an advisability warning recommending `PROP BSBT` for nonstationary higher-order with large CFL.

User-set `CFL` parameters (in `PNUMS` indices 6 and adjacent) at `[file=src/swanpre1.ftn line=2037,2051,2059]` — these affect explicit-scheme controls, not stability of the implicit BSBT path.

General error handling: `MSGERR` writes to `PRINTF`; halt when `LEVERR > MAXERR` at `[file=src/swanmain.ftn line=523-528]`, `[file=src/swanmain.ftn line=573-578]`.

## Decision Guide

| Symptom | Likely cause | Where to check |
|---------|--------------|----------------|
| Run divergence at large DT | CFL violation w/ higher-order scheme | warning at `swancom5.ftn:2893`; reduce DT or switch to BSBT |
| Time stamps in output skip | output `DELT` < compute `DELTC`, or wall-clock between writes | `SWORDC` trigger at `swanout1.ftn:682-704` |
| Wind interpolation looks step-wise | input `SERIES` interval too large vs `DT` | `FLFILE` weight at `swanmain.ftn:8828-8850` |
| Boundary stays at stale value | `TIMF2 < TIMCO` exhaustion | exhaustion message at `swanmain.ftn:8019` |
| `AC1` "wrong" between iterations | `ITERMX==1` vs `>1` toggles AC1 vs AC2 source | `ACOLD` selection at `swancom5.ftn:2179-2181` |

## Working Rules

1. STRSXY의 시간항 외에 SANDL의 직전 단계 공간항과 SwanTranspX의 시간항도 AC1을 읽는다. `src/swancom5.ftn:2964`의 원문은 `+(0.25*RDX(1)) * (CAX1(ID,IS,2) * AC1(ID,IS,IND2)`이다. `src/SwanTranspX.ftn90:146`의 원문은 `acold = ac1(id,is,iv1)`이다.
2. **Always run `IT=0` first** in nonstationary — it lets initial conditions settle without modifying state from a "before" assumption.
3. **Output `DELT` is decoupled from compute `DELT`** — set finer compute (`DELTC`) for stability + coarser output (`DELT`) for storage.
4. CFL warning at `MYU>10` is **advisory not fatal**. Higher-order can still run; just expect dispersion if you ignore it.

## Common Pitfalls

- 계산 시간 간격은 COMPUTE NONSTAT의 DELTC 입력과 INITVD의 DT 설정으로 설명한다. `src/swanpre1.ftn:903`의 원문은 `CALL INITVD ('DELTC', DT, 'REQ', 0D0)`이다. [R8:N1-013](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).
- HOTSTART 시각보다 이전인 시작 시각에는 오류를 내고 현재 시각으로 되돌린다. 같은 시각만 허용한다고 쓰지 않는다. `src/swanpre1.ftn:897`은 TBEGC 생략 시 TIMCO를 쓴다. `src/swanpre1.ftn:899`의 원문은 `IF (TINIC .LT. TIMCO) THEN`이다. [R5 §4](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#4-노트-대조와-수정안).
- SET TIMINC와 SET TIMEFORMAT은 SWAN 명령으로 안내하지 않는다. `2980d1a:src/swanpre1.ftn:901`, `7ee8981:src/swanpre1.ftn:903`, `43e9bbb:src/swanpre1.ftn:903`의 원문은 `CALL INITVD ('DELTC', DT, 'REQ', 0D0)`이다. [R8:N1-013](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론), [git 판정 D](../../../_staging/recovery/compare/SWAN-git-verify-D.md).

## References

- `src/swanmain.ftn` — outer time loop, FLFILE, output dispatch, error handling.
- `src/swancom5.ftn` — time-term in matrix; CFL warning emission.
- `src/swanpre1.ftn` — `COMPUTE` parser; CFL parameter slots.
- `src/swanout1.ftn` — `SWORDC` output trigger logic.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | time loop, AC1/AC2 swap, FLFILE interp, boundary time interp, output trigger, CFL warning |
| Review status | 2026-10-13 recovery 대조 보고서 R1–R8 반영 |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R4:T1-013 | 입력 시작 전 0 가정 | swanuse PDF 19쪽 / 인쇄 11쪽: “zero values … before” | `src/swanmain.ftn:4965` `IF (JWX3.GT.1) COMPDA(INDX,JWX3) = COMPDA(INDX,JWX2)`. | B 문서 오기 | 첫 입력 시각 전에도 이미 읽은 첫 장이 사용될 수 있다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R5:PN-098 | COMPUTE 시간 처리 | COMPUTE 시간 검사와 반올림. swanuse PDF 120쪽–121쪽 / 인쇄 112쪽–113쪽은 시작·종료·간격을 정의한다. 비정수 시간 간격 처리는 적지 않는다. | `src/swanpre1.ftn:914` `MTC = NINT ((TFINC - TINIC)/DT)`; 915–916행의 `MOD` 조건. | C | 단계 수는 `MTC = NINT ((TFINC - TINIC)/DT)`로 정한다. 경고는 `IF (MOD(TFINC-TINIC,DT).GT.0.01*DT .AND.` / `MOD(TFINC-TINIC,DT).LT.0.99*DT)`일 때만 발생한다. 나누어떨어지지 않는 모든 경우에 경고한다는 원 결론을 고친다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-187 | COMPUTE 모드·시각 | `source-analysis/swan-command-file-reference.md:214` `assumes nonstationary` | `src/swanpre1.ftn:879` `IF (NSTATM.LE.0 .OR. KEYWIS('STAT')) THEN`. | B | 정상 MODE의 COMPUTE는 정상 분기를 선택한다. HOTSTART보다 이전 시작 시각에는 오류를 내고 현재 시각으로 되돌린다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R8:T1-013 | 비정상 시간 간격·반복 권고 | swanuse PDF 121쪽·인쇄 113쪽: “For a nonstationary computation, a time step of at most 10 minutes is advised.” 이어지는 권고는 “For a sufficiently small time step (≤ 10 minutes), no more than 1 iteration per time step is recommended”이다 | `src/swanpre1.ftn:903` `CALL INITVD ('DELTC', DT, 'REQ', 0D0)`; `:1959` `CALL ININTG ('MXITNS' , MXITNS   , 'REQ', 0 )`; `:935` `ITERMX = MXITNS`. 비정렬·정렬 루프는 T1-007의 ITERMX를 쓴다. | H | 사용자 매뉴얼은 비정상 계산에 10분 이하 시간 간격을 권고한다. 시간 단계당 반복을 1회보다 많이 하지 말라는 권고는 충분히 작은 시간 간격(≤ 10 minutes)을 전제로 한다. 이 문장들은 DT 또는 MXITNS의 강제 상한이 아니다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:N1-005 | AC1의 유일한 소비 위치라는 주장 | source-analysis/swan-time-stepping-implementation.md:68 ``This is the **only** place `AC1` is read during the matrix assembly path.``; :131 ``The **time-term in matrix** is the only place `AC1` enters during a time step`` | `src/swancom5.ftn:2964` `+(0.25*RDX(1)) * (CAX1(ID,IS,2) * AC1(ID,IS,IND2)`; `:2965`의 AC1(ID,IS,IND5); `src/SwanTranspX.ftn90:146` `acold = ac1(id,is,iv1)`. | B | STRSXY의 시간항 외에 SANDL의 직전 단계 공간항과 SwanTranspX의 시간항도 AC1을 읽는다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:N1-013 | SET TIMINC·SET TIMEFORMAT | `source-analysis/swan-time-stepping-implementation.md:138`의 `SET TIMINC` 및 `sets the *parsing* time format step`; `:140`의 `SET TIMEFORMAT`. [git 판정 D](../../../_staging/recovery/compare/SWAN-git-verify-D.md)의 결론을 유지한다. `rg -i -uuu 'TIMINC\|TIMEFORMAT' models/SWAN/raw/source_code`는 일치 0건·종료값 1이다. git 저장소 전체의 `git log --all -S TIMINC -- .`, `git log --all -S TIMEFORMAT -- .`, 대소문자 변형의 `-G` 검색도 각 0커밋이다. | `2980d1a:src/swanpre1.ftn:901`, `7ee8981:src/swanpre1.ftn:903`, `43e9bbb:src/swanpre1.ftn:903`은 모두 `CALL INITVD ('DELTC', DT, 'REQ', 0D0)`이다. 현재 SET 분기 `src/swanpre1.ftn:2169–2213`에도 두 명령이 없다. | D — 확정 | SET TIMINC와 SET TIMEFORMAT은 SWAN 명령으로 안내하지 않는다. 계산 시간 간격은 COMPUTE NONSTAT의 DELTC 입력과 INITVD의 DT 설정으로 설명한다. D의 범위는 확인한 전체 소스와 로컬 git 이력이다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) [10-13 전수 검증 보완] |

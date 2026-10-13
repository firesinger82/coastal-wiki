---
title: "swan wind formulations implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 HEAD 대비 추가·수정 28줄을 R2·R7 최종 보고서, 현재 코드, 웹 HTML, swantech PDF 27–29·32·58–60쪽과 swanuse PDF 36·66–67·69쪽에 대조했다." # [10-13 전수 검증 정정]
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-13 (recovery 대조 반영)
---

# SWAN wind input formulations — WNDPAR, SWIND0/3/4/5 (code-level)

## Scope note

Per-formulation deep dive of SWAN's wind-input source terms: `WNDPAR` (GEN1/GEN2), `SWIND0` (linear seed), `SWIND3` (Snyder/Komen GEN3), `SWIND4` (Janssen GEN3), `SWIND5` (Yan / Westhuysen GEN3). The exact formulas as implemented, plus the `AGROW` option's role.

ST6/Babanin is in a separate file (`SdsBabanin.ftn90`) — see `swan-st6-babanin-implementation.md`.

## Source basis

Codex deep scan 2026-05-06 of `models/swan/source_code/swan/src/swancom3.ftn` (wind input family) + `swanpre1.ftn` (parser).

## A. `WNDPAR` (GEN1, GEN2)

- Subroutine: `[file=src/swancom3.ftn line=30]`
- GEN1의 `.0081`은 중간값이다. 천해 하한을 적용한 값이 최종값이다. (`src/swancom3.ftn:408` `ALPM = MIN ( 0.155 , MAX ( ALPMD , ALPM ) )`)
- GEN2 (`IWIND==2`): compute `ETOTW` via `WINDP2`, then `EDML`, then `ALPM = MAX(0.0081, PWIND(5) * (1./EDML)**ABS(PWIND(6)))`

`WINDP1`의 `CFPM` 사용과 `WNDPAR`의 `.13` 재계산을 구별한다. `WNDPAR`의 포화 주파수는 입력 `CFPM` 대신 `.13`을 직접 사용한다. (`src/swancom3.ftn:370` `SIGPK = TWOPI * 0.13 * GRAV / WIND10`; `src/swancom3.ftn:911`의 `PWIND(13)`)

### Per-bin growth/relaxation split

`[file=src/swancom3.ftn line=470-500]`:
- Growth branch: `SWIND_EXP = ADUM + BDUM*AC2CEN`, `SWIND_IMP = 0`
- Relaxation branch: `SWIND_EXP = TAUINV * ALIMW`, `SWIND_IMP = TAUINV`

### Matrix accumulation
`[file=src/swancom3.ftn line=512-517]`:
```
IMATRA += SWIND_EXP    (and to GENC0)
IMATDA += SWIND_IMP    (and to GENC1)
```

So both branches feed both matrix slots — what differs is whether `SWIND_IMP` is zero (growth) or nonzero (relaxation).

## B. `SWIND0` (Cavaleri-Malanotte-Rizzoli linear seed)

- Subroutine: `[file=src/swancom3.ftn line=1526]`
- Formula at `[file=src/swancom3.ftn line=1749-1750, 1766, 1772-1773]`:
  ```
  SWINEA = max(0,
    (PWIND(31) / (g² * 2π) / σ)
    * (UFRIC * max(0, cosΔ))⁴
    * exp(-min(2, FPM/σ)⁴)
  )
  ```
  **Not** proportional to `U10²` (a common literature simplification).

### Activation
- In GEN3-family (`IWIND >= 3`) only when `PWIND(31) > 1e-20` at `[file=src/swancom1.ftn line=7410-7418]`
- This is the optional seed growth from near-zero energy

### Matrix
- Linear input added explicitly: `IMATRA += SWINEA` at `[file=src/swancom3.ftn line=1782]`
- No `IMATDA` contribution (purely explicit)

## C. `SWIND3` (Snyder / Komen)

- Subroutine: `[file=src/swancom3.ftn line=1842]`
- Implemented coefficient at `[file=src/swancom3.ftn line=2043, 2048, 2051-2052, 2058-2059]`:
  ```
  SWINEB = max(0,
    0.25 * PWIND(9) * (28 * UFRIC * (k/σ) * cosΔ - 1) * σ
  )
  ```
- Since `CINV = k/σ = 1/c` (phase speed inverse), this matches the **Komen et al. 1984** form:
  ```
  β = max(0, (ρa/ρw) * 0.25 * (28 * UFRIC * cosΔ / c - 1))
  ```
  with `PWIND(9) = ρa/ρw` and source multiplied by `σ`.

### Matrix
- Explicit only: `IMATRA(ID,IS) += SWINEB * AC2(...)` at `[file=src/swancom3.ftn line=2061]`

So Snyder/Komen contributes purely to RHS (no implicit on diagonal). Stability comes from accompanying `WCAP` (whitecapping) on diagonal.

## D. `SWIND4` (Janssen)

- Subroutine: `[file=src/swancom3.ftn line=2094]`
- More complex than the others — has **iteration** to solve for friction velocity

### Sea-state dependent state

- `USTAR, ZELEN` initialized on early iter/step branches at `[file=src/swancom3.ftn line=2331-2359]`, `[file=src/swancom3.ftn line=2365-2367]`, `[file=src/swancom3.ftn line=2583-2585]`
- Reused and updated from previous iteration

### Wave stress and Newton-Raphson on UFRIC

- Wave stress `TAUW` from spectrum (plus HF tail) at `[file=src/swancom3.ftn line=2368-2526]`
- **Newton-Raphson loop** (up to 20 steps) solving for `TAUTOT` at `[file=src/swancom3.ftn line=2533-2568]`
- Then `UFRIC = sqrt(TAUTOT/RHOA)` at `[file=src/swancom3.ftn line=2570]`

### Janssen-Miles parameter

`[file=src/swancom3.ftn line=2601-2615]`:
```
ZCN = log(g * ZE / c²)
ZARG = κ / ((U*/c + ZALP) * cosΔ)
BETA = F1 * exp(ZLOG) * ZLOG⁴   (if ZLOG < 0)
```

### Final coefficient

`[file=src/swancom3.ftn line=2619]`:
```
SWINEB = (ρa/ρw) * BETA * (U*/c + ZALP)² * cos²Δ * σ
```

### Matrix
- Explicit only: `IMATRA += SWINEB * AC2` at `[file=src/swancom3.ftn line=2623]`

So Janssen has internal Newton-Raphson + state from previous step, but external matrix contribution is the same explicit pattern as Snyder/Komen.

## E. `SWIND5` (Yan / Westhuysen)

- Subroutine: `[file=src/swancom3.ftn line=2668]`

### Yan branch (default, `IWCAP ≠ 7`)

`[file=src/swancom3.ftn line=2849-2853, 2868-2877]`:
- Coefficients: `COF1=0.04, COF2=0.00544, COF3=0.000055, COF4=0.00031`
- `SWINEB = max(0, ((COF1·X² + COF2·X + COF3) * cosΔ - COF4) * σ)`
- where `X = UFRIC*k/σ = U*/c`

### Westhuysen / Alves-Banner branch (`IWCAP == 7`)

`[file=src/swancom3.ftn line=2856-2861]`:
- Coefficients: `COF2=0.00552, COF3=0.000052, COF4=0.000302` (`COF1` unchanged)

So the Westhuysen tuning differs only in lower-order polynomial coefficients (COF2/3/4); the structural form is identical.

### Matrix
- Explicit only: `IMATRA += SWINEB * AC2` at `[file=src/swancom3.ftn line=2881]`

## F. `AGROW` option

- **Not parsed in swancom3.ftn**.
- Parsed by `swanpre1.ftn` at `[file=src/swanpre1.ftn line=3059-3061]` and `[file=src/swanpre1.ftn line=3273-3275]`:
  - `AGROW [A]` sets `PWIND(31)` (default `0.0015` when keyword present without value)
- Documentation tying `PWIND(31)` to `GEN3 AGROW` at `[file=src/swmod1.ftn line=2636-2639]`
AGROW 활성 조건은 GEN3에 공통이다. ST6는 응력 상한을 추가한 별도 선형 입력 루틴을 호출한다. (`src/swancom1.ftn:7417` `IF ( IWIND.NE.8 ) THEN`; `src/swancom1.ftn:7428` `CALL SWIND0_NRL`)
이 루틴은 ST6 선형 입력 응력을 총응력의 1%로 제한한다. (`src/SdsBabanin.ftn90:1517` `IF (TAU_MAGNITUDE.GT.(0.01*TAU_FROM_UFRIC))THEN`; `src/SdsBabanin.ftn90:1518` `REDUCTION=(0.01*TAU_FROM_UFRIC)/TAU_MAGNITUDE`)

## 입력 선택

기본 GEN3 바람·백파 조합은 WESTH이다. (`src/swanpre1.ftn:453` `INTEGER, SAVE :: LWINDM = 5`; `src/swanmain.ftn:1112` `IWCAP  = 7`)

## Working Rules

1. **All GEN3 wind inputs are explicit** (RHS only) — pair with `WCAP` to keep diagonal stable.
2. Janssen 응력을 맞추는 반복은 최대 20회이다. (`src/swancom3.ftn:2533` `DO II = 1, 20`)
3. **Westhuysen and Yan share `SWIND5`** — switching `IWCAP` between 7 and not-7 changes the coefficients within the same routine.
4. **`AGROW` is a global GEN3 modifier** — affects all wind formulations, not specific to one.
5. **`PWIND(31)` is the seed-growth knob** — default 0.0015 when AGROW present without value.

## Common Pitfalls

- **Dropping `WCAP` while keeping `GEN3`** → unbounded growth + limiter clamping forever (already noted in source-terms note).
- **Comparing Janssen vs Komen at first iteration** — Janssen needs prior-state `USTAR`; iterate to convergence first.
- **Confusing `PWIND(9)` (Snyder/Komen ρa/ρw) with `PWIND(31)` (AGROW seed)** — both look like "small constants" in tuning files.
- **Westhuysen with whitecapping other than `IWCAP=7`** — silently uses Yan branch coefficients, not Westhuysen tuning.

## References

- `src/swancom3.ftn` — `WNDPAR`, `SWIND0/3/4/5`.
- `src/swanpre1.ftn` — `AGROW` parser.
- `src/swancom1.ftn` — `SOURCE` dispatcher chooses formulation by `IWIND`.
- `src/swmod1.ftn` — `PWIND(*)` documentation.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | per-formulation formulas as in code, matrix split, AGROW |
| Review status | `review_required: true` |


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-501 | Wu·FIT의 `CDCAP` 제한 | swanuse PDF 36쪽 / 인쇄 28쪽은 `CDCAP`과 기본값 99999를 명시한다. swanuse PDF 67쪽 / 인쇄 59쪽·swanuse PDF 69쪽 / 인쇄 61쪽은 HWANG·FAN·ECMWF를 설명한다. 웹 [swanuse/node23.html](../raw/manuals/website/online_doc/swanuse/node23.html):295–312에도 항력 상한이 있다. | `src/swancom3.ftn:1006`의 `MIN ( CDCAP, CDRAG )`; `src/swancom3.ftn:1007` `IF ( WIND10.GT.50.7 ) THEN`; `src/swancom3.ftn:1008` 의 `UFRIC = 1.9441`; `src/swancom3.ftn:1073` 의 `50.33`; `src/swancom3.ftn:1078` 의 `CALL SURF_ROUGH_FAN`; `src/swancom3.ftn:1082` 의 `CALL SURF_ROUGH_ECMWF` | C | `CDCAP`과 ST6 항력 선택은 사용자 매뉴얼에 있다. C는 swantech PDF 27–28쪽 / 인쇄 19–20쪽의 (2.34)–(2.35)에 고풍속 마찰 속도 제한의 세부가 없는 점으로 좁힌다. `IDRAG.EQ.2`인 FIT 경로는 `IF ( WIND10 .GT. 50.7 ) THEN`에서 `UFRIC = 1.9441`로 둔다(`src/swancom3.ftn:1002–1011`). 50.33은 HWANG 경로의 마찰 속도 상한 분기이다. 이를 Wu·FIT의 상수로 합치지 않는다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 전수 검증 정정] |
| R2:SS-502 | GEN3 선형 입력에서 필터 비 $r=\min(2,FPM/\sigma)$, $\sigma\ge.7FPM$ 조건, $f>1$ Hz에서 추가 $f^{-3}$ 감소 | swantech PDF 28쪽 / 인쇄 20쪽, (2.36) $A={1.5\times10^{-3}\over2\pi g^2}(U_*\max[0,\cos(\theta-\theta_w)])^4H$, $H=\exp\{-(\sigma/\sigma_{PM}^*)^{-4}\}$, $\sigma_{PM}^*={0.13g\over28U_*}2\pi$. | `src/swancom3.ftn:1762` `ARGU = MIN (2., FPM / SIGMA)`; `src/swancom3.ftn:1769` 의 `ANYWND(ID)`와 주파수 조건; `src/swancom3.ftn:1775` `FREQ1 = SIGMA/PI2`; `src/swancom3.ftn:1776–1778` 의 `FREQ1 .GT. 1.`·`FREQ1**(-3)` | C | (2.36)의 필터 외에 하한과 고주파 감소를 적용한다. 1660–1700행 주석은 고주파 절단의 선택 이유를 별도로 설명한다. |
| R2:SS-503 | Janssen 응력에서 진단 꼬리 적분, $\tau_w\le.999\tau$, Newton 최대 20회, 새 총응력이 파랑 응력보다 작거나 같으면 중간값으로 복귀 | swantech PDF 29쪽 / 인쇄 21쪽, (2.38) $B=\beta(\rho_a/\rho_w)(U_*/c_{ph})^2\max[0,\cos(\theta-\theta_w)]^2\sigma$. | `src/swancom3.ftn:2525` `TAUW = MIN ( TAUW , 0.999 * TAUTOT )`; `src/swancom3.ftn:2533` 의 `DO II = 1, 20`; `src/swancom3.ftn:2563` 의 `IF ( TAUNEW .LE. TAUW ) TAUNEW = .5 * (TAUTOT + TAUW)`; `src/swancom3.ftn:2564` 의 `1.E-5` | C | (2.40)–(2.42)의 특이점과 반복을 제한한다. 2444–2506행이 고주파 꼬리의 응력을 더한다. [10-13 전수 검증 정정] |
| R2:SS-504 | Yan 입력의 음의 성장률 제거 | swantech PDF 32쪽 / 인쇄 24쪽, (2.54) $\beta_{fit}=D(u_*/c)^2\cos(\theta-\alpha)+E(u_*/c)\cos(\theta-\alpha)+F\cos(\theta-\alpha)+H$. | `src/swancom3.ftn:2877` `SWINEB = MAX ( 0. , SWINEB * SIGMA )` | C | (2.54)의 맞춤 함수가 음수여도 이 경로는 음의 바람 입력을 내지 않는다. ST6의 음의 입력 선택과 구별한다. |
| R2:SS-527 | GEN1/2의 최소 풍속·항력 일관성 보정·PM 주파수 재계산 | swanuse PDF 66쪽 / 인쇄 58쪽은 `[umin]` 기본값 1.0과 `[cfpm]` 기본값 .13을 제시한다. | `src/swancom3.ftn:910`의 `PWIND(12)`; `src/swancom3.ftn:983–984` 의 `WIND10` 재조정; `src/swancom3.ftn:911` 의 `PWIND(13)`; `src/swancom3.ftn:370` `SIGPK = TWOPI * 0.13 * GRAV / WIND10` | C | 문서의 $U_{10}$ 자리에 항상 원시 입력 풍속이 들어가는 것은 아니다. 기본 최소 풍속은 1 m/s이다. Wu 항력 비의 제곱근으로 풍속을 재조정한다. `WNDPAR`의 포화 주파수는 입력 `CFPM` 대신 `.13`을 직접 사용한다. C는 swantech PDF 58–60쪽 / 인쇄 50–52쪽에 풍속 재조정과 `CFPM` 대신 `.13`으로 재계산하는 세부가 없는 점이다. 최소 풍속과 입력 매개변수의 존재는 사용자 매뉴얼에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-528 | GEN1/2 포화 스펙트럼 지수 제한과 해 갱신 뒤 포화값 제한 | swantech PDF 58쪽 / 인쇄 50쪽, (2.118) $S_{tot}=A+BE$ if $E<E_{lim}$ and $\lvert\theta-\theta_w\rvert<\pi/2$; $(E_{lim}-E)/\tau$ if $E>E_{lim}$ and $\lvert\theta-\theta_w\rvert<\pi/2$; $0$ if $E>E_{lim}$ and $\lvert\theta-\theta_w\rvert>\pi/2$. | `src/swancom3.ftn:417` `ARG2 = MIN ( 2. , SIGPKD / SPCSIG(IS) )`; `src/swancom3.ftn:1499–1503` 의 `ALIMW`와 성장 상태 비교 | C | 저주파 지수 인자를 2로 제한한다. `WINDP3`는 성장·완화 전 상태에 따라 갱신값이 포화값을 통과하지 않도록 제한한다. 식 (2.118)의 source 조립만으로 이 후처리를 설명할 수 없다. |
| R2:SS-711 | 노트 · source-analysis/swan-wind-formulations-implementation.md:28 | `source-analysis/swan-wind-formulations-implementation.md:28` `ALPM = 0.0081`; 31 `same constant used by both`. | `src/swancom3.ftn:408` `ALPM = MIN ( 0.155 , MAX ( ALPMD , ALPM ) )`; 370의 직접 상수 `0.13` | C | GEN1의 `.0081`은 중간값이다. 천해 하한을 적용한 값이 최종값이다. `WINDP1`의 `CFPM` 사용과 `WNDPAR`의 `.13` 재계산을 구별한다. |
| R2:SS-712 | 노트 · source-analysis/swan-wind-formulations-implementation.md:155 | `source-analysis/swan-wind-formulations-implementation.md:155` `it adds the linear seed source through the shared pre-call block`. | `src/swancom1.ftn:7417` `IF ( IWIND.NE.8 ) THEN`; `src/swancom1.ftn:7428` `CALL SWIND0_NRL` | C | AGROW 활성 조건은 GEN3에 공통이다. ST6는 응력 상한을 추가한 별도 선형 입력 루틴을 호출한다. [10-13 결론 검증 보완] |
| R7:S-003 | Janssen 사용 비권고 | `website/settings/settings.htm:43–44` `have not been tested thoroughly. For this reason, it is recommended not to use this source term package.<br>` | `src/swancom1.ftn:7464` `CALL SWIND4  (IDWMIN  ,IDWMAX  ,` | H 코드 대조 대상 아님 | 시험 충실도에 따른 권고이다. Janssen 풍입력 경로는 코드에 남아 있다. [10-13 결론 검증 보완] |

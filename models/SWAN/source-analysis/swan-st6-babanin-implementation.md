---
title: "swan st6 babanin implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 이번 추가·수정 줄을 SWAN 현재 코드의 해당 줄과 조건 분기, swantech·swanuse PDF, R2·R5 최종 결론 및 SWAN-external-sources.md와 대조했다. WW3 인용은 저장된 매뉴얼 PDF 62쪽과 W3SWL6 코드 379–415행을 대조했다." # [10-13 전수 검증 정정]
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-13 (recovery 대조 반영)
---

# SWAN ST6/Babanin submodule — code-level

## Scope note

`SdsBabanin.ftn90` is a single-file submodule that implements the ST6 / Babanin family of source terms (used when `IWIND=8` and `IWCAP=8`). It contains both the wind input (`SWIND_DBYB`) and whitecapping (`CALC_SDS`). This note documents its internal structure, formulas as they appear in code, and integration points with the rest of SWAN.

Companion to `swan-source-terms-implementation.md` (which covers other source terms).

## Source basis

Codex deep scan 2026-05-06 of `models/swan/source_code/swan/src/SdsBabanin.ftn90` (~2700 lines, single module).

## A. Module structure

- Module header: `MODULE SDSBABANIN` at `[file=src/SdsBabanin.ftn90 line=3]`
- Pure procedure container: enters `CONTAINS` at `[file=src/SdsBabanin.ftn90 line=5]` immediately
- No module-scope `TYPE` / derived structures
- No module-scope `PARAMETER` constants — all constants are local to routines (e.g., `BNT` in `CALC_SDS`)
- No `PUBLIC`/`PRIVATE` — default visibility (everything accessible via `USE SDSBABANIN`)

## B. Wind input (`SWIND_DBYB`)

- Subroutine: `[file=src/SdsBabanin.ftn90 line=313]`
- Primary inputs at `[file=src/SdsBabanin.ftn90 line=505-513]`:
  - `SPCSIG, THETAW, KWAVE, AC2, UFRIC, WIND10, SPCDIR, ANYWND, CG`
  - Output arrays: `MEMSINA, MEMSINB`

### Internal computation steps

1. **1D spectral density** `SIGDENS(IS)`: build from `AC2` and `SPCSIG`, scale by `DDIR` at `[file=src/SdsBabanin.ftn90 line=542-549]`
2. **Direction-shape normalization** `KTHETA(IS,ID)`: per-frequency `DMAX`, with empty-bin guard at `[file=src/SdsBabanin.ftn90 line=552-572]`
3. **`ANAR`, `BN`, `SQRTBN`** (saturation precursors): `BN = ANAR * SIGDENS * k³ * Cg` at `[file=src/SdsBabanin.ftn90 line=575-587]`
4. **Wind speed proxy** `TEMP2`: either true `U10` (`TRUE_U10`) or `WNDSCL * UFRIC` at `[file=src/SdsBabanin.ftn90 line=598-602]`
5. **Donelan-Babanin/Yang growth-rate** at `[file=src/SdsBabanin.ftn90 line=621-629]`:
   - `TEMP4 → WPSI → GDONEL → GAMMAD → SWINEB`
   - `SWINEB` is the exponential coefficient (`BETA` in comments — see `[file=src/SdsBabanin.ftn90 line=630-635]`)
6. **`S_IN = SWINEB * AC2 * SPCSIG`**
7. **Linear-term stress** (`MEMSINA`): directional integration `TAUX_linear, TAUY_linear` at `[file=src/SdsBabanin.ftn90 line=643-656]`
8. **Stress-based reduction**: `CALL CALC_LFACTOR` at `[file=src/SdsBabanin.ftn90 line=659-660]`
9. **Final write to `MEMSINB`** at `[file=src/SdsBabanin.ftn90 line=722-726]`:
   - `MEMSINB = S_IN / SPCSIG` (after `RDFSIN(IS)` scaling)

So `SWIND_DBYB` produces a memo table `MEMSINB` that the main solver consumes via `FILSIN`.

## C. Whitecapping (`CALC_SDS`)

- Subroutine: `[file=src/SdsBabanin.ftn90 line=7]`
- Empirical saturation coefficient `BNT = (0.035)²` at `[file=src/SdsBabanin.ftn90 line=168]`
- 백파의 `ANAR`는 1로 고정된다. (`src/SdsBabanin.ftn90:177` `ANAR=1.0`)

### Computation flow

1. **Threshold spectrum** `EDENST(IS) = 2π * BNT / (Cg * k³)` at `[file=src/SdsBabanin.ftn90 line=184-187]`
2. **Exceedance** `DEDENS = max(0, EDENS - EDENST)` at `[file=src/SdsBabanin.ftn90 line=192-195]`
3. **Normalized exceedance** `NDEDENS`: by `EDENST` or `EDENS` depending on `UPWARDS`, clipped nonnegative at `[file=src/SdsBabanin.ftn90 line=207-219]`
4. **Inherent breaking term** `T1(IS) = A1SDS * F * ANAR * NDEDENS^P1SDS` at `[file=src/SdsBabanin.ftn90 line=224-226]`
5. **Induced breaking term** `T2`: cumulative integral of `ADF(II) = ANAR * NDEDENS^P2SDS` at `[file=src/SdsBabanin.ftn90 line=236-248]`
6. **Output** `KDS = T1 + T2` (or `T1` only if `A2SDS ≤ 0`) at `[file=src/SdsBabanin.ftn90 line=256-259]` — passed back to caller

UP이면 $r=D/E_T$이다. DOWN이면 $E_f>0$에서 $r=D/E_f$이고 그 밖은 0이다. (swanuse PDF 67쪽 / 인쇄 59쪽, PDF 69쪽 / 인쇄 61쪽; `src/SdsBabanin.ftn90:208`·`src/SdsBabanin.ftn90:212`의 나눗셈)

There is **no `SDS_TOTAL`** routine in this file (despite being mentioned in some literature). Total-dissipation diagnostics appear only as commented-out NRL local variables.

## D. Negative wind input (decay)

Dedicated block at `[file=src/SdsBabanin.ftn90 line=665-710]`:
- Active only when `ZIEGER` is true at `[file=src/SdsBabanin.ftn90 line=686]`
- Decay-side branch: `TEMP4 = MIN(0.0, UoverC*COSDIF - 1.0)`, `WPSI = TEMP4²` at `[file=src/SdsBabanin.ftn90 line=694-696]`
- Apply by subtracting `SWINEB * AC2 * SPCSIG * RDCOEF` from `S_IN` at `[file=src/SdsBabanin.ftn90 line=702]`

Zieger 선택은 음의 입력 경로의 조건이다. 실제 크기는 `RDCOEF`에 비례한다. 기본값 0이면 이 기여도 0이다. (`src/swanmain.ftn:1383` `RDCOEF = 0.`; `src/SdsBabanin.ftn90:702` `S_IN(ID,IS)= S_IN(ID,IS) - SWINEB*AC2(ID,IS,KCGRD(1))*SPCSIG(IS)*RDCOEF`)

## E. Per-frequency / per-direction integration; A/B split

- Main exponential-term loops: nested `DO IS=1,MSC`, `DO ID=1,MDC` producing `S_IN(ID,IS)` at `[file=src/SdsBabanin.ftn90 line=605-641]`
- Linear-term stress: also nested IS/ID with cos/sin(θ) projection at `[file=src/SdsBabanin.ftn90 line=646-653]`
- Code documentation at `[file=src/SdsBabanin.ftn90 line=712-720]` explicitly: split is `A + B*E`:
  - `B*N` (`MEMSINB`) is the explicit exponential term
  - `MEMSINA` is the linear part (separate routine `SWIND0_NRL`)
- `SWIND0_NRL` writes linear `A/sigma` to `MEMSINA` at `[file=src/SdsBabanin.ftn90 line=1529]`
- `FILSIN` injects whichever memo (`MEMSINA` or `MEMSINB`) into sweep-local `IMATRA`/`GENC0` at `[file=src/SdsBabanin.ftn90 line=1696-1697]`

## F. Calls into rest of SWAN

### Imports
- `SWIND_DBYB` imports `SWCOMM1, SWCOMM3, SWCOMM4, OCPCOMM4` at `[file=src/SdsBabanin.ftn90 line=318-321]`
- `CALC_SDS` imports `SWCOMM1` + selected `SWCOMM3` coefficients (`A1SDS, A2SDS, P1SDS, P2SDS, UPWARDS, GRAV, PI`) at `[file=src/SdsBabanin.ftn90 line=7-10]`

### Consumption from main solver
- `swancom1.ftn:6875` — `SOURCE` routine `USE SdsBabanin`
- `swancom1.ftn:7428-7436` — for `IWIND=8`: linear part via `SWIND0_NRL`, then `FILSIN(MEMSINA, ...)` → `IMATRA/GENC0`
- `swancom1.ftn:7489-7497` — exponential/DBYB part via `SWIND_DBYB`, then `FILSIN(MEMSINB, ...)` → `IMATRA/GENC0`
- `swancom1.ftn:7519-7534` — with `IWCAP=8`, swell-dissipation variants (`SSWELL_ZIEGER`/`_ROGERS`/`_ARDHUIN`) → `IMATDA, DISSC1`
- `swancom2.ftn:2859` — `CALC_SDS` produces `WCAP(IS)` for `SWCAP8` flow

## 입력 선택

`GEN3 ST6`는 ST6 바람 입력과 ST6 백파를 함께 선택한다. (`src/swanpre1.ftn:2987` `LWINDM = 8`; `src/swanpre1.ftn:2991` `IWCAP = 8`)

## Working Rules

1. `GEN3 ST6`는 ST6 바람 입력과 ST6 백파를 함께 선택한다. (`src/swanpre1.ftn:2987` `LWINDM = 8`; `src/swanpre1.ftn:2991` `IWCAP = 8`)
2. **`MEMSINA`/`MEMSINB` are zero-sized** when `IWIND ≠ 8` — don't try to read them in custom code without checking.
3. ST6의 두 소산 계수는 생략할 수 있다. 초기값은 각각 2.8E-6과 3.5E-5다. (`src/swanmain.ftn:1376` `A1SDS       = 2.8E-6`; `src/swanmain.ftn:1377` `A2SDS       = 3.5E-5`; `src/swanpre1.ftn:2992–2993` `CALL INREAL ('A1SDS', A1SDS, 'UNC', 0.)`; `CALL INREAL ('A2SDS', A2SDS, 'UNC', 0.)`) [10-13 전수 검증 보완]
4. ZIEGER는 너울 소산 선택이다. 음의 풍입력 크기는 별도 NEGATINP RDCOEF로 정한다. RDCOEF의 초기값은 0이다. (`src/swanmain.ftn:1383` `RDCOEF      = 0.`; `src/SdsBabanin.ftn90:702` `S_IN(ID,IS)= S_IN(ID,IS) - SWINEB*AC2(ID,IS,KCGRD(1))*SPCSIG(IS)*RDCOEF`)

## Common Pitfalls

- Zieger 선택은 음의 입력 경로의 조건이다. 기본 `RDCOEF=0`에서는 추가 음의 입력이 0이다. (`src/SdsBabanin.ftn90:686` `IF(ZIEGER)THEN`; `src/swanmain.ftn:1383` `RDCOEF = 0.`)
- **Tuning `A1SDS` without measuring** — saturation coefficient is sensitive; published defaults are calibrated for global runs.
- **`TRUE_U10` vs scaled `UFRIC`** — small differences in wind input through `TEMP2` choice affect long-fetch results.
- **Neglecting linear `MEMSINA`** — for very low-energy seed states, the linear term matters; `SWIND0_NRL` must be active.

## References

- `src/SdsBabanin.ftn90` — module body.
- `src/swancom1.ftn` — `SOURCE` dispatcher (`IWIND=8`, `IWCAP=8`), `FILSIN` consumer.
- `src/swancom2.ftn` — `SWCAP8` whitecapping that consumes `CALC_SDS` output.
- `src/swmod*.ftn` — `SWCOMM1/3/4` shared-state holders for ST6 coefficients.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations within SdsBabanin.ftn90 |
| Coverage | module structure, wind input pipeline, whitecapping, negative input, A/B split, integration |
| Review status | `review_required: true` |


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md). 표의 결론은 R2·R5의 AI 해석이다. 기존 노트 인용의 줄 번호는 이번 반영 전 HEAD 기준이다. [10-13 전수 검증 보완]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-734 | 노트 · source-analysis/swan-st6-babanin-implementation.md:67 | `source-analysis/swan-st6-babanin-implementation.md:67`·68의 `ANAR`; `source-analysis/swan-whitecapping.md:128`의 같은 인자. | `src/SdsBabanin.ftn90:177` `ANAR=1.0` | C | 백파의 `ANAR`는 1로 고정된다. 바람 입력에서 계산하는 방향 퍼짐 계수와 같은 작동 방식이라고 설명하지 않는다. [10-13 결론 검증 보완] |
| R2:SS-529 | ST6 백파의 초과 스펙트럼 | swanuse PDF 67쪽 / 인쇄 59쪽·swanuse PDF 69쪽 / 인쇄 61쪽은 기본 `UP`의 $E_T(f)$ 정규화와 `DOWN`의 $E(f)$ 정규화를 설명한다. | `src/SdsBabanin.ftn90:168` `BNT=(0.035**2)`; `src/SdsBabanin.ftn90:177` `ANAR=1.0`; `src/SdsBabanin.ftn90:186` `EDENST(IS)=CTMP1/(CG(IS,1)*KWAVE(IS,1)**3)`; `src/SdsBabanin.ftn90:195` `DEDENS=MAX(0.0,DEDENS)`; 208·212의 나눗셈 | C | `CALC_SDS`는 방향 퍼짐 계수 `ANAR`를 1로 고정한다. 바람 입력의 방향 퍼짐 계수와 구별한다. 기본값은 `UPWARDS = .TRUE.`이다. $E_f$는 Hz당 에너지 밀도이다. C는 swantech PDF 33쪽 / 인쇄 25쪽에 `BNT`·`ANAR=1`과 초과 스펙트럼 계산식의 세부가 없는 점이다. 정규화 선택과 기본 `UP` 자체는 사용자 매뉴얼에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-530 | ST6 백파의 고유·누적 감쇠율 | swanuse PDF 68쪽 / 인쇄 60쪽의 ST6 예제는 `2.8E-6 3.5E-5 4.0 4.0 ... U10PROXY 32.0` 조합을 제시한다. 69/61은 $T_1$·$T_2$와 지수 기본값을 설명한다. | `src/SdsBabanin.ftn90:225` `T1(IS)=A1SDS*F(IS)*ANAR(IS)*NDEDENS(IS)**P1SDS`; `src/SdsBabanin.ftn90:240` `DO II=1,IS`; `src/SdsBabanin.ftn90:246` `CALL INTEGRATE(ASUM,XFF,ADF,IS)`; `src/SdsBabanin.ftn90:247` `T2(IS)=A2SDS*ASUM`; `src/SdsBabanin.ftn90:256` `KDS=(T1+T2)` | C | 적분은 첨두주파수가 아니라 첫 계산 주파수에서 시작한다. 232–234행 주석은 이 선택을 설명한다. $A_2\le0$이면 누적 항은 0이다. 기본 $A_1=2.8\,10^{-6}$, $A_2=3.5\,10^{-5}$, $p_1=p_2=4$이다. 대입은 `src/swanmain.ftn:1376`–1379이다. C는 swantech PDF 33쪽 / 인쇄 25쪽에 실제 적분 시작 주파수와 `A2SDS` 분기 등 계산 세부가 없는 점이다. 계수 조합·두 소산 항의 역할 자체는 사용자 매뉴얼에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-531 | ST6 바람 입력 | swantech PDF 33쪽 / 인쇄 25쪽는 $U=S_{ws}u_*$와 $S_{ws}=32$를 설명한다. swanuse PDF 67쪽 / 인쇄 59쪽도 기본 `U10PROXY=32`와 `TRUE10`을 설명한다. 같은 매뉴얼 69/61의 기본값 줄은 28로 서로 다르다. | `src/SdsBabanin.ftn90:584`의 `1.0/AINV`; `src/SdsBabanin.ftn90:585` 의 `BN`; `src/SdsBabanin.ftn90:621–628` 의 `TEMP4`·`WPSI`·`GDONEL`·`GAMMAD`; `src/SdsBabanin.ftn90:635` 의 `S_IN(ID,IS)=SWINEB*AC2(ID,IS,KCGRD(1))*SPCSIG(IS)` | C | 이 계산은 Donelan–Babanin 계열이다. Yan 다항식 (2.54)와 다르다. 기본 $U=32u_*$이다. `TRUE10`이면 실제 $U_{10}$을 쓴다. `A_\theta`는 최대값으로 정규화한 방향 분포의 적분 역수이다. C는 swantech PDF 33쪽 / 인쇄 25쪽에 인용한 Donelan–Babanin 성장률과 방향 정규화 계산식이 없는 점이다. 풍속 변환의 존재는 문서에 있다. 코드 기본값 32는 swanuse PDF 67쪽 / 인쇄 59쪽와 대응하며 69/61의 28 표기는 구별해 적는다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-532 | ST6 응력 상한과 입력 감소 | swanuse PDF 67쪽 / 인쇄 59쪽·swanuse PDF 69쪽 / 인쇄 61쪽은 기본 VECTAU와 SCATAU의 벡터·스칼라 적분을 설명한다. | `src/SdsBabanin.ftn90:991`–1001의 `tau_visc`; `src/SdsBabanin.ftn90:1324` `AEXP=EXP((1-UOVERC) * REDUC)`; `src/SdsBabanin.ftn90:1327` `LFACTOR(IS)=MIN(1.0,AEXP(IS))`; `src/SdsBabanin.ftn90:1359` `TAU_TOTAL=SQRT(TAU_TOTAL_X**2+TAU_TOTAL_Y**2)`; 1361의 scalar 합; `src/SdsBabanin.ftn90:1098` `DO ITER=1,50`; `src/SdsBabanin.ftn90:1129` `IF((ABS(ERR)/TAU_TOTAL_MAX) < 5.E-04)THEN` | C | 기본 VECTAU는 파랑·점성·선형 입력 응력을 벡터로 합한다. SCATAU 분기는 파랑 응력의 scalar 적분과 점성 응력 크기를 합한다. 이 분기에는 별도 선형 응력 가산이 없다. 응력 상한을 맞추는 반복은 최대 50회이다. 상대 잔차 $.0005$ 미만이면 종료한다. C는 swantech PDF 33쪽 / 인쇄 25쪽에 두 경로의 구체적 응력 합산 항과 입력 감소 반복식·종료 조건이 없는 점이다. 벡터·스칼라 선택 자체는 사용자 매뉴얼에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-533 | ST6 응력 적분의 고주파 확장과 수치 보정 | — | `src/SdsBabanin.ftn90:924`–930의 10 Hz 확장; `src/SdsBabanin.ftn90:952` 의 `0.102`; `src/SdsBabanin.ftn90:956` 의 `S_IN_L(IDIR,IS)=S_IN_L(IDIR,NF_OLD)*(SIGMA_L(NF_OLD)/SIGMA_L(IS))**2`; `src/SdsBabanin.ftn90:1123` `RCHANGE=0.5*(1.0+RCHANGE)`; `src/SdsBabanin.ftn90:1129` `IF((ABS(ERR)/TAU_TOTAL_MAX) < 5.E-04)THEN`. `src/SdsBabanin.ftn90:1136`의 `IF(ISOL==0)THEN` 안에서 1158의 `IF(TAU_TOTAL.NE.TAU_TOTAL)THEN` 뒤 1160의 `STOP`을 실행한다 | C | 응력 계산은 계산 스펙트럼 위쪽에 입력 source의 역제곱 꼬리를 붙인다. 위상속도 역수는 깊은 물 근사 $\sigma/9.8$에 가까운 $.102\sigma$를 사용한다. 반복 중 잔차 부호가 바뀌면 보정폭을 줄인다. 기본 전처리에서 `!NRL` 강제 종료는 살아 있지 않는다. NaN 종료는 별도로 살아 있다. C는 swantech PDF 33쪽 / 인쇄 25쪽에 이 고주파 확장과 반복 보정의 세부가 없는 점이다. NaN 종료는 `ISOL==0` 안의 조건부 경로이다. [10-13 결론 검증 보완] |
| R2:SS-534 | ST6 선형 입력 응력을 총응력의 1%로 제한 | swanuse PDF 68쪽 / 인쇄 60쪽의 ST6 예제에는 `AGROW`가 있다. swantech PDF 33쪽 / 인쇄 25쪽도 SWAN/ST6 선형 입력의 변경을 언급한다. | `src/SdsBabanin.ftn90:1517` `IF (TAU_MAGNITUDE.GT.(0.01*TAU_FROM_UFRIC))THEN`; `src/SdsBabanin.ftn90:1518` `REDUCTION=(0.01*TAU_FROM_UFRIC)/TAU_MAGNITUDE`; `src/SdsBabanin.ftn90:1519` `SWINEA=SWINEA*REDUCTION`; `src/swancom1.ftn:7428` `CALL SWIND0_NRL` | C | ST6도 AGROW를 사용할 수 있다. 그러나 호출 루틴은 `SWIND0`가 아니라 `SWIND0_NRL`이다. 이름의 NRL은 전처리 주석 표시가 아니다. 이 루틴의 계산은 기본 빌드에서도 살아 있다. C는 swantech PDF 33쪽 / 인쇄 25쪽에 총응력의 1% 상한 계산식이 없는 점이다. ST6에서 AGROW를 선택할 수 있다는 사실은 문서에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-535 | Zieger 선택 시 ST6 음의 바람 입력 | swanuse PDF 70–71쪽 / 인쇄 62–63쪽 및 웹 [swanuse/node28.html](../raw/manuals/website/online_doc/swanuse/node28.html):736–748은 ZIEGER와 NEGATINP의 결합·`RDCOEF`·기본값 0을 명시한다. | `src/SdsBabanin.ftn90:686`의 `IF(ZIEGER)THEN`; `src/SdsBabanin.ftn90:695` 의 `MIN(0.0`; `src/SdsBabanin.ftn90:702` 의 `RDCOEF`; `src/SdsBabanin.ftn90:724` `S_IN(ID,IS)= S_IN(ID,IS) * RDFSIN(IS)` | C | 음의 입력은 Zieger 선택과 `RDCOEF`에 종속된다. 기본 `RDCOEF=0`에서는 추가 음의 입력이 0이다. 감소 인자는 마지막에 양·음 입력의 합에 곱한다. Zieger 선택과 `RDCOEF=0`에서의 동작은 사용자 매뉴얼과 일치한다. C는 swantech PDF 33쪽 / 인쇄 25쪽에 감소 인자를 양·음 입력의 합에 마지막으로 곱하는 순서가 없는 점으로 좁힌다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-536 | ST6 너울 소산의 Reynolds 분기 | swanuse PDF 70쪽 / 인쇄 62쪽와 부록 C 138/130은 SSWELL 선택을 설명한다. swanuse PDF 70쪽 / 인쇄 62쪽의 기본 `CDSV=1.2`는 코드와 같다. | `src/SdsBabanin.ftn90:1850` `AORB=2.0*SQRT(ETOT)`; `src/SdsBabanin.ftn90:1852` `RE=4.0*USIGTOP*AORB/NU_AIR`; `src/SdsBabanin.ftn90:1854` `IF(RE > RE_CRIT)THEN`; 1857–1863의 두 `SWDIS`; `src/SdsBabanin.ftn90:2036` `FESWELL = s1*(feGM + (abs(s3) + s2*COSDIF)*UFRIC/USIGTOP)`; `src/SdsBabanin.ftn90:2019–2022`는 `s1=0.8`, `s2=-0.018`, `s3=0.015`, `feGM=0.003`이다 | C | ROGERS는 입력 $f_e$를 쓴다. 기본 ARDHUIN은 $f_e=.8[.003+(.015-.018\cos\Delta\theta)u_*/U_{orb}]$를 쓴다. 기본 $C_{dsv}=1.2$이다. 주석의 물 분자점성 항 $4\nu_wk^2$는 1889–1892행에서 주석 처리되어 실행하지 않는다. `src/swancom1.ftn:7519`의 `IF (IWCAP.EQ.8) THEN`이 이 소산 계열을 제한한다. C는 swantech PDF 33쪽 / 인쇄 25쪽에 Reynolds 분기와 계수 계산식의 세부가 없는 점이다. ARDHUIN 선택과 CDSV 기본값 자체는 사용자 매뉴얼에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-537 | Zieger 너울 소산의 $K=2B_1\sigma\sqrt{B_n}/3$와 기본 $B_1=.00025$ | 대체 문헌: WW3 v5.16 매뉴얼, PDF 62쪽 / 인쇄 54쪽, 식 (2.143) $S_{swl}(k,\theta)=-\frac23 b_1\sigma\sqrt{B_n}N(k,\theta)$, 식 (2.144) $b_1=B_1 2\sqrt E k_p$, 표 2.8의 v4.18 `SWLB1=0.25E-3`. [외부 원문 판정](../../../_staging/recovery/compare/SWAN-external-sources.md) | `src/SdsBabanin.ftn90:2196` `This is from WW3v4 and Zieger et al. (2015) eq. 23.`; `src/SdsBabanin.ftn90:2197–2198` `This does *not* include the steepness-dependent B1` / `WW3v5 and Zieger et al. (2015) eq. 28.`; `src/SdsBabanin.ftn90:2200` `SWDIS(IS) = 2.0*B1Z*SPCSIG(IS)*SQRTBN(IS)/3.0`; `src/swanmain.ftn:1386` `B1Z = 0.00025`. WW3 `W3SWL6`:396–415의 `ANAR = 1.0/( SUM(K,1) * DTH )`, `BN = ANAR * ( ABAND * SIG(1:NK) * DTH ) * WN**3`, `DDIS(IK) = -(2./3.) * B1 * SIG(IK) * SQRT(BN(IK))`. `src/SdsBabanin.ftn90:2189–2191`의 `BN=ANAR(IS)*SIGDENS(IS)*(KWAVE(IS,1)**3)*CG(IS,1)`; 2210의 양의 대각 가산. [외부 원문 판정](../../../_staging/recovery/compare/SWAN-external-sources.md). | F | 판정 기준은 Zieger 논문 자체가 아니라 대체 문헌인 WW3 매뉴얼·코드이다. WW3의 작용 밀도 원천항을 밀도로 나눈 감쇠율은 SWAN의 `SWDIS`와 계수 $2/3$까지 대응한다. 부호 차이는 음의 원천항과 양의 대각 소산 계수의 차이이다. 두 구현은 최대값으로 정규화한 방향 분포의 적분 역수를 사용한다. $E(k)=c_gE(\sigma)$로 바꾸면 $B_n$도 대응한다. SWAN의 고정 계수 `.00025`는 WW3 v4.18 표와 같다. WW3 v5의 경사 의존 $b_1=B_1 2\sqrt E k_p$와는 구별한다. Zieger 식 (23)·(28)이라는 번호는 swantech PDF 33쪽 / 인쇄 25쪽과 코드 주석의 인용 표기이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 외부 원문 판정] |
| R2:SS-733 | 노트 · source-analysis/swan-st6-babanin-implementation.md:117 | `source-analysis/swan-st6-babanin-implementation.md:117` `pair with ` 뒤의 `WCAP ST6`; 124 `GEN3 ST6`만 쓰면 `non-ST6 dissipation`이라는 설명. | `src/swanpre1.ftn:2987` `LWINDM = 8`; `src/swanpre1.ftn:2991` `IWCAP = 8` | B | `GEN3 ST6`는 ST6 바람 입력과 ST6 백파를 함께 선택한다. 별도 백파 명령을 반드시 추가해야 한다는 설명은 삭제한다. |
| R2:SS-735 | 노트 · source-analysis/swan-st6-babanin-implementation.md:120 | `source-analysis/swan-st6-babanin-implementation.md:120` `ZIEGER`가 음의 입력을 활성화한다는 설명. | `src/swanmain.ftn:1383` `RDCOEF = 0.`; `src/SdsBabanin.ftn90:702`의 `*RDCOEF` | C | Zieger 선택은 음의 입력 경로의 조건이다. 실제 크기는 `RDCOEF`에 비례한다. 기본값 0이면 이 기여도 0이다. [10-13 결론 검증 보완] |
| R5:PN-185 | ZIEGER와 음의 풍입력 | `source-analysis/swan-st6-babanin-implementation.md:120` `activates negative wind input` | `src/swanmain.ftn:1383` `RDCOEF      = 0.` | B | ZIEGER는 너울 소산을 고른다. 음의 풍입력 크기는 별도 NEGATINP로 정한다. |

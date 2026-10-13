---
title: "swan whitecapping"
topic: general
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 HEAD 대비 추가·수정 36줄을 R2·R5·R7 최종 보고서, 현재·과거 코드, 웹 HTML, swantech PDF 29–33쪽과 swanuse PDF 67·69·71·138쪽에 대조했다." # [10-13 전수 검증 정정]
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-13 (recovery 대조 반영)
---

## Scope

이 노트는 Komen·Janssen·WESTH·ST6의 백파 선택과 계수를 설명한다. 기본 GEN3 조합은 WESTH이다. `IWCAP`이 1–7이면 `SWCAP`을 호출한다. `IWCAP=8`이면 `SWCAP8`을 호출한다. 두 경로는 백파 소산을 `IMATDA`에 가산한다. 바람·백파 조합 검사는 오류 수준 1의 `MSGERR` 메시지를 낸다. 근거: swanuse PDF 67쪽 / 인쇄 59쪽; `src/swancom1.ftn:7505–7515`; `src/swancom2.ftn:2645–2650,2893–2897`; `src/swanmain.ftn:6419–6445`. [10-13 전수 검증 정정]

**Note**: source-term assembly is in `SOURCE` subroutine of `swancom1.ftn` (no `sources.f` file in this tree).

## Source basis

- `swanmain.ftn:1110-1112, 1340-1491` — defaults, `IGEN=3, IQUAD=2, IWCAP=7`.
- `swanpre1.ftn:2461-3088` — GEN dispatch, parameter parsing.
- `swmod1.ftn:2295-2300, 2728` — `IWCAP` codes.
- `swancom1.ftn:7287-7511` — Sds insertion in source-term assembly.
- `swancom2.ftn:2290-2897` — `SWCAP` (Komen, Janssen, Westhuysen).
- `swancom3.ftn:1907-2860` — wind-input formulas.
- `SdsBabanin.ftn90:44-256` — ST6/Babanin.

## A. GEN dispatch

**Default state** in this version (`swanmain.ftn:1110-1112`):
```
IGEN=3, IQUAD=2, IWCAP=7
```
So default is **Westhuysen / Alves-Banner**, not Komen.

| Command | Effect |
|---|---|
| `GEN1` | First-gen wind, **disables quadruplets and whitecapping** (`swanpre1.ftn:2808-2814`) |
| `GEN2` | Second-gen wind, disables quadruplets and whitecapping (`:2843-2849`) |
| `GEN3 KOM` | `IWIND=3, IWCAP=1` (Komen) (`:3036-3040`) |
| `GEN3 JANS` | `IWIND=4, IWCAP=2` (Janssen / WAM Cycle 4) (`:2908-2912`) |
| `GEN3 WESTH` | `IWIND=5, IWCAP=7` (Yan + Alves-Banner / Westhuysen, default) (`:2935-2940`) |
| `GEN3 ST6` | `IWIND=8, IWCAP=8` (Babanin/Rogers ST6) (`:2983-2991`) |
| `GEN4` | GEN4는 QC 산란을 켠다. 풍입력·사파·백파를 끈다. (`src/swanpre1.ftn:3090` `IQCM  = 1`; `src/swanmain.ftn:6377–6379`의 `IWIND = 0`, `IQUAD = 0`, `IWCAP = 0`) |

## B. Komen (IWCAP=1)

`IWCAP=1` = "standard WAM formulation (Komen et al., 1984)" (`swmod1.ftn:2295-2297`).

Inputs: `CDS2, STPM, POWST, DELTA, POWK` (`swanpre1.ftn:2461-2472`).

Defaults (`swanmain.ftn:1340-1345`):
- `PWCAP(1) = 2.36e-5` (CDS2).
- `PWCAP(2) = 3.02e-3` (STPM).
- `PWCAP(9) = 2` (POWST).
- `PWCAP(10) = 1` (DELTA).
- `PWCAP(11) = 1` (POWK).

Formula (comments):
```
S_wc(σ, θ) = -C_wc · E(σ, θ)
C_K = C1 · [(1−δ) + δ(k/k̄)^n1] · (S̄/S_PM)^n2
```
(`swancom2.ftn:2290-2303`).

Implementation (`:2485-2614`):
```
STP_OV = KM_WAM * sqrt(ETOT)
STP_PM = sqrt(PWCAP(2))
N1 = PWCAP(11), N2 = 2*PWCAP(9)
WCAP(IS) = C_K(IS) * SIGM_10 * (KWAVE(IS,1)/KM_WAM)
```

**`CDSV` is NOT a Komen parameter** — it's used by Babanin/swell physics (`swmod1.ftn:2728`, `swanmain.ftn:1382`).

## C. Janssen / WAM Cycle 4 (IWCAP=2)

`IWCAP=2` = Janssen whitecapping (`swmod1.ftn:2298-2300`).

`GEN3 JANS` reads `CDS1` and `DELTA`, maps into generalized Komen coefficients used by `SWCAP`:
```
PWCAP(1) = PWCAP(3) * (PWCAP(2)^PWCAP(9))
PWCAP(10) = PWCAP(4)
```
(`swanpre1.ftn:2912-2919`).

Defaults: `CFJANS=4.5, DELTA=0.5` (`swanmain.ftn:1350-1351`).

**Consistency check**: WAM Cycle 4 requires Janssen wind input with Janssen whitecapping (`swanmain.ftn:6440-6444`).

## D. Westhuysen / Saturation-based (IWCAP=7, default)

`GEN3 WESTH` uses Yan wind input + Alves-Banner whitecapping (`swanpre1.ftn:2935-2940`).

GEN3 WESTH 또는 WCAP AB를 명시했을 때 CDS2 기본값은 5.0E-5다. 두 명령을 모두 생략한 초기 PWCAP(1)은 2.36E-5다. (`src/swanpre1.ftn:2941` `CALL INREAL ('CDS2',  PWCAP(1),  'STA', 5.0E-5)`; `src/swanmain.ftn:1340` `PWCAP(1)  = 2.36E-5`) WCAP AB의 생략값은 `src/swanpre1.ftn:2511`의 `CALL INREAL ('CDS2',  PWCAP(1),  'STA', 5.0E-5)`에도 지정돼 있다. [10-13 전수 검증 보완]
AB와 XNL을 함께 쓰면 기본 BR는 1.95E-3으로 바뀐다. 판정 조건은 `EQREAL` 호출 그대로 적는다. (`src/swanmain.ftn:6677` `IF (EQREAL(PWCAP(12),1.75E-3)) PWCAP(12) = 1.95E-3`)

In `SWCAP`, this is "Alves and Banner (2003)" (`swancom2.ftn:2536-2538`).

Saturation-based formula (`:2573-2592`):
```
B = (1/2π) · CG · k³ · E(f)                      ! saturation
FBR = 0.5 · (1 + tanh(10·(√(B/BRKD) − 1)))       ! breaking fraction
P = 3 + tanh(25.76·(u*·k/σ − 0.1))               ! exponent
```
WESTH의 비쇄파 배경 소산은 Komen 형태를 사용한다. 이 경로의 $C_{ds}$는 $3.00\,10^{-5}$이다. Komen 기본 $2.36\,10^{-5}$와 구별한다. (`src/swancom2.ftn:2545` `PWCAP1  = 3.00E-5`)

**Requires Yan wind** when `IWCAP=7` (`swanmain.ftn:6426-6428`).

## E. ST6 / Babanin (IWCAP=8)

`GEN3 ST6` sets Babanin/Rogers wind input + whitecapping (`swanpre1.ftn:2983-2991`).

Parameters: `A1SDS, A2SDS, P1SDS, P2SDS` (defaults: `2.8e-6, 3.5e-5, 4, 4`) (`swanpre1.ftn:2992-2995`, `swanmain.ftn:1376-1380`).

Globally initialized: `UPWARDS=.TRUE.` (`swanmain.ftn:1380`).

ST6 wind options (`swanpre1.ftn:3003-3027`):
- `HWANG, FAN, ECMWF` (drag formula).
- `VECTAU, SCATAU` (vector vs scalar tau).
- `TRUE10, U10P` (true 10-m vs proxy).
- Optional `DEB CDFAC`.

`SWCAP8` calls `CALC_SDS` (`swancom2.ftn:2693-2859`).

`CALC_SDS` defines `KDS = Sds/E(f) = T1 + T2` (`SdsBabanin.ftn90:44-53`):
```
T1 = A1SDS * f * ANAR * NDEDENS^P1SDS         (inherent breaking)
T2 = A2SDS * ASUM                              (cumulative)
KDS = T1 + T2
```
(`SdsBabanin.ftn90:225-256`).

백파의 `ANAR`는 1로 고정된다. (`src/SdsBabanin.ftn90:177` `ANAR=1.0`)
UP이면 $r=D/E_T$이다. DOWN이면 $E_f>0$에서 $r=D/E_f$이고 그 밖은 0이다. (swanuse PDF 67쪽 / 인쇄 59쪽, PDF 69쪽 / 인쇄 61쪽; `src/SdsBabanin.ftn90:208`·`src/SdsBabanin.ftn90:212`의 나눗셈) 여기서 $D=\max(E_f-E_T,0)$이다. 근거: `src/SdsBabanin.ftn90:192`의 `DEDENS=EDENS-EDENST`와 195행의 `DEDENS=MAX(0.0,DEDENS)`. [10-13 전수 검증 보완]

## F. CDS2 / wind-input relations

For Komen/Snyder:
- Snyder-Komen wind input combined with Komen dissipation (`swancom3.ftn:1907-1911`).
- Coefficient: `B = max(0, 0.25·ρ_aw·(28U*·cos/(σ/k) − 1))·σ` (`:1918-1927`).
- Implemented as (`:2043-2059`):
```
TEMP1 = 0.25 * PWIND(9)
TEMP2 = 28 * UFRIC
SWINEB = TEMP1 * (TEMP3 * COSDIF − 1)
SWINEB = max(0, SWINEB * sigma)
```

For Westhuysen, Yan coefficients modified when `IWCAP=7` (`:2854-2860`).

## G. Where Sds enters action balance

`SOURCE` subroutine in `swancom1.ftn` initializes `IMATRA, IMATDA` (`:7287-7293`).

Order:
1. Wind input assembled first (`:7410-7480`).
2. Whitecapping called if `IWCAP >= 1` (`:7502-7511`):
   - `IWCAP <= 7` → `SWCAP`.
   - `IWCAP = 8` → `SWCAP8`.

`SWCAP` adds dissipation to matrix diagonal `IMATDA` and output dissipation bucket (`swancom2.ftn:2637-2646`); `SWCAP8` analogous for ST6 (`:2887-2897`).

## H. Defaults / recommendations

Source-code default: **`GEN3 WESTH`** (`IWCAP=7`).

Defaults table:

| Option | Parameters |
|---|---|
| Komen | CDS2=2.36e-5, STPM=3.02e-3, POWST=2, DELTA=1, POWK=1 |
| WESTH | CDS2=5.0e-5, BR=1.75e-3 |
| ST6 | A1SDS=2.8e-6, A2SDS=3.5e-5, P1=P2=4, CDSV=1.2, WNDSCL=32, VECTOR_TAU=T, TRUE_U10=F |

`src/swanpre1.ftn:3031`의 `IF ( IWCAP.EQ.8 .OR. IWIND.EQ.8 ) THEN` 뒤에 `src/swanpre1.ftn:3032`의 `We prefer that you use GEN3 BABANIN.` 메시지가 있다. 조건부 입력 경고는 전체 응용의 성능 권고 근거가 아니다.

## Working Rules

- Default is **Westhuysen**, not Komen — explicitly set `GEN3 KOM` if you want Komen.
- `GEN3 BABANIN`은 이전 입력 형식이다. `GEN3 ST6`는 새 입력 형식이다. (`src/swanpre1.ftn:2943`의 `KEYWIS('BAB')`; `src/swanpre1.ftn:2983`의 `KEYWIS('ST6')`)
- Pair wind input with consistent whitecapping (Janssen-Janssen, Yan-Westhuysen, Babanin-Babanin); SWAN enforces.
- For `GEN1/GEN2`, whitecapping and quadruplets are **disabled**; useful only for first-gen / DIA-free benchmarks.
- GEN4는 QC 산란을 켜면서 여러 물리·수치·좌표 설정을 덮어쓴다. (`src/swanpre1.ftn:3090` `IQCM  = 1`; `src/swanpre1.ftn:3096` `PNUMS(20) = 1.E20`; `src/swanpre1.ftn:3101` `KSPHER = 0`)
- Output Sds dissipation via `BLOCK DISWCAP` for diagnostic.

## Common Pitfalls

- ▢ Setting `GEN3 KOM` thinking it's the default — actual default is `WESTH`.
- ▢ Using `GEN3 KOM` with Janssen wind input — enforced inconsistency, runtime warning.
- ▢ Confusing `CDS2` (whitecapping) with `CDSV` (swell, Babanin physics).
- ▢ Adjusting `A1SDS/A2SDS` in `GEN3 WESTH` run — those are ST6 parameters, ignored.
- ▢ Expecting whitecapping with `GEN1/GEN2` — disabled.
- `GEN3 ST6`는 ST6 바람 입력과 ST6 백파를 함께 선택한다. (`src/swanpre1.ftn:2987` `LWINDM = 8`; `src/swanpre1.ftn:2991` `IWCAP = 8`)

## Next expansion

- Quantitative comparison Komen vs Westhuysen vs ST6 on identical buoy-validation case.
- ST6 wind-input drag formula details (HWANG / FAN / ECMWF).
- WAM Cycle 4 (Janssen) historical context.

## References

- Komen et al. 1984 (whitecapping baseline).
- Janssen 1991 (WAM Cycle 4).
- van der Westhuysen et al. 2007 (saturation-based).
- Babanin & Young 2005 (cumulative dissipation, ST6).
- Rogers et al. 2012 (ST6 implementation in SWAN).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md) · [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-506 | WESTH와 XNL을 결합하면 기본 임계 포화도를 바꾼다 | swanuse PDF 71쪽 / 인쇄 63쪽의 `[br]` 기본값은 `1.75e-3`이다. | `src/swanmain.ftn:6674`–6677의 `IWCAP.EQ.7`·`IQUAD.EQ.51`/52/53 조건 및 `PWCAP(12) = 1.95E-3`; `src/swanmain.ftn:6674–6677`: `IF ( IWCAP.EQ.7 .AND. (IQUAD.EQ.51 .OR. IQUAD.EQ.52 .OR. IQUAD.EQ.53) ) THEN` 안에서 `IF (EQREAL(PWCAP(12),1.75E-3)) PWCAP(12) = 1.95E-3`를 실행한다 | C | WESTH와 XNL의 결합 조건을 만족하면 `EQREAL(PWCAP(12),1.75E-3)`가 참인 값을 `1.95E-3`으로 바꾼다. C는 swantech PDF 31–33쪽 / 인쇄 23–25쪽와 swanuse의 기본값 설명에 이 결합 조건의 재대입이 없는 점이다. 판정 조건은 코드의 `EQREAL` 호출 그대로 적는다. [10-13 결론 검증 보완] |
| R2:SS-538 | 선택적 백파의 BJ·Longuet-Higgins 경로와 암시적 선형화 | swanuse 부록 C 138/130은 `WCAP LHIG`·`BJ`·`KBJ` 선택을 나열한다. | `src/swancom2.ftn:2501`의 `HM = PWCAP(6) / KM01`; `src/swancom2.ftn:2503` 의 `CALL FRABRE(HM, ETOT, QB_WC, 1.)`; `src/swancom2.ftn:2525` 의 `A = -(1./8.) * GRAV**2 / ETOT4`; `src/swancom2.ftn:2531` 의 `C_LH(IS)`; `src/swancom2.ftn:2662` 의 `WCIMPL` | C | 기본 Komen·Janssen·WESTH·ST6 외에 쇄파율을 쓰는 백파와 확률식 백파가 있다. Longuet-Higgins 경로는 $\exp[-g^2/(8m_4)]$와 $\sqrt{m_2}\sigma^2/g$를 사용한다. 선택적 `WCIMPL`은 기본 상대 소산의 대각 가산과 다른 선형화를 적용한다. C는 swantech PDF 29–33쪽 / 인쇄 21–25쪽에 이 선택의 소산식과 `WCIMPL` 선형화 계산이 없는 점이다. 선택지의 존재는 사용자 매뉴얼 부록에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-736 | 노트 · source-analysis/swan-whitecapping.md:190 | `source-analysis/swan-whitecapping.md:190` `GEN3 ST6 BABANIN`; 204 `Not pairing ... incomplete physics`. | `src/swanpre1.ftn:2943`의 `KEYWIS('BAB')`와 2983의 `KEYWIS('ST6')`는 서로 다른 GEN3 분기이다 | B | `GEN3 BABANIN`은 이전 입력 형식이다. `GEN3 ST6`는 새 입력 형식이다. 둘을 연속 하위 키워드로 적지 않는다. |
| R2:SS-740 | 노트 · source-analysis/swan-whitecapping.md:203 | `source-analysis/swan-whitecapping.md:203` `needs ~1 day to spin up`; 180 `Best-tested production`; `source-analysis/swan-st6-babanin-implementation.md:109`–113의 용도별 권고; `source-analysis/swan-wind-formulations-implementation.md:171` `slowest`. | `src/swanpre1.ftn:3031` `IF ( IWCAP.EQ.8 .OR. IWIND.EQ.8 ) THEN` 뒤에 3032의 `We prefer that you use GEN3 BABANIN.` 메시지가 있다 | H | 조건부 입력 경고는 전체 응용의 성능 권고 근거가 아니다. 노트의 1일 spin-up과 상대 속도·정확도 주장은 사례 출처가 없는 성능 서술이다. 이 수치·권고를 노트에서 삭제하는 H 판정을 유지한다. [10-13 결론 검증 정정] |
| R5:PN-021 | AB와 XNL의 BR | swanuse PDF 71쪽 / 인쇄 63쪽 `[br] = 1.75e-3.` | `src/swanmain.ftn:6677` `IF (EQREAL(PWCAP(12),1.75E-3)) PWCAP(12) = 1.95E-3` | C | AB와 XNL을 함께 쓰면 기본 BR는 1.95E-3으로 바뀐다. |
| R5:PN-143 | 암묵적 WESTH 계수 | swanuse PDF 67쪽 / 인쇄 59쪽 `GEN3 WESTH is the default`. | `src/swanmain.ftn:1340` `PWCAP(1)  = 2.36E-5`; `src/swanpre1.ftn:2941`의 STA 값은 `5.0E-5`다 | C | GEN3·WCAP을 모두 생략한 초기 계수와 WESTH를 명시했을 때의 기본 계수는 다르다. |
| R5:PN-146 | GEN4 | `source-analysis/swan-whitecapping.md:183` `uses wave-induced breaking only`. | `src/swanpre1.ftn:3090` `IQCM  = 1`, 3096 `PNUMS(20) = 1.E20`, 3101 `KSPHER = 0` | C | GEN4는 QC 산란을 켜면서 여러 물리·수치·좌표 설정을 덮어쓴다. 쇄파만 켜는 명령이 아니다. |
| R5:PN-186 | 노트의 성능·보정 권고 | `source-analysis/swan-whitecapping.md:203` `needs ~1 day to spin up`; `source-analysis/swan-diffraction-obstacles.md:152` `is essential`. | `src/swanpre1.ftn:3031` `IF ( IWCAP.EQ.8 .OR. IWIND.EQ.8 ) THEN` 뒤에 3032의 `We prefer that you use GEN3 BABANIN.` 메시지가 있다 | H | 성능 우위·약 하루의 준비 시간·필수 평활화·반복 횟수 축소는 적용 권고다. 이를 코드가 강제하는 규칙으로 쓰지 않는다. `src/swanpre1.ftn:3032`의 특정 경고 문구도 보편적 성능 근거는 아니다. [10-13 결론 검증 정정] |
| R7:H-326 | MDIA·CSM 선택 안내 | `website/modifications/modifications.htm:326` `Alternative approximations for two physical processes are available:`; `website/modifications/modifications.htm:1289` `Solved in version 40.72`; 1369행 `patch E`; 1372행 `The so-called CSM formulation for whitecapping is removed.` | `src/swanpre1.ftn:3152` `IF (KEYWIS('MDIA')) THEN                                            40.17`; 이력: `122b595:src/swanpre1.ftn:3105` `IF (KEYWIS('MDIA')) THEN                                            40.17` | D 현재 해당 구현 없음 | 40.20의 MDIA 선택은 현재도 남아 있다. 같은 항목의 CSM 선택은 40.72 patch E에서 제거되었다. 두 선택을 모두 현재 선택지로 안내하지 않는다. `122b595`와 `43e9bbb`의 src에서 `Cumulative Steepness`와 단어 CSM은 검색되지 않는다. 현재 `src/swanpre1.ftn:2508–2511`의 IWCAP=7은 AB 백파식이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R7:H-333 | CSM | `website/modifications/modifications.htm:333` `Cumulative Steepness Method for white-capping.`; `website/modifications/modifications.htm:1289` `Solved in version 40.72`; 1369행 `patch E`; 1372행 `The so-called CSM formulation for whitecapping is removed.` | `src/swanpre1.ftn:2510` `IWCAP = 7                                                       40.53`; 이력: `122b595:src/swanpre1.ftn:2463` `IWCAP = 7                                                       40.53` | D 현재 해당 구현 없음 | CSM은 40.72 patch E에서 제거되었다. 원 보고서의 제거 판 번호 40.51은 40.72 patch E로 고친다. 현재 IWCAP=7은 CSM 선택자가 아니다. `122b595`와 `43e9bbb`의 src에서 `Cumulative Steepness`와 단어 CSM은 검색되지 않는다. 현재 `src/swanpre1.ftn:2508–2511`의 IWCAP=7은 AB 백파식이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R7:H-601 | CSM 정규화 | `website/modifications/modifications.htm:601` `The CSM white-capping formulation contains normalisation. (Already introduced with patch F of the previous version 40.31.)`; `website/modifications/modifications.htm:1289` `Solved in version 40.72`; 1369행 `patch E`; 1372행 `The so-called CSM formulation for whitecapping is removed.` | `src/swanpre1.ftn:2510` `IWCAP = 7                                                       40.53`; 이력: `122b595:src/swanpre1.ftn:2463` `IWCAP = 7                                                       40.53` | D 현재 해당 구현 없음 | 40.41의 CSM 정규화는 현재 기능으로 남아 있지 않다. CSM 제거 판은 40.72 patch E이다. `122b595`와 `43e9bbb`의 src에서 `Cumulative Steepness`와 단어 CSM은 검색되지 않는다. 현재 `src/swanpre1.ftn:2508–2511`의 IWCAP=7은 AB 백파식이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R7:H-813 | 잘못된 물리 선택 오류 처리 | `website/modifications/modifications.htm:813` `Modified the handling of choosing physics for the model. Error messages warn the user regarding erroneous choices in the physics. In previous versions SWAN would automatically correct erroneous choices in the physics, this is now left to the user.` | `src/swanmain.ftn:6373` `IF (IWIND.NE.0 .OR. IQUAD.NE.0 .OR. IWCAP.NE.0) THEN`; 이력: `122b595:src/swanmain.ftn:6278` `IF (IWIND.NE.0 .OR. IQUAD.NE.0 .OR. IWCAP.NE.0) THEN`; `122b595:src/swanmain.ftn:6283` `IQUAD = 0`; `src/swanmain.ftn:6372–6379`의 `IF (IGEN.EQ.4) THEN` 안에서 `IWIND = 0`, `IQUAD = 0`, `IWCAP = 0`을 대입한다 | D 현재 해당 구현 없음 | 현재 GEN4 검사는 심해 물리 선택을 자동으로 0으로 바꾼다. 잘못된 선택의 보정을 전부 사용자에게 맡긴다는 구판 동작은 현재 코드에 없다. 41.45 비교 코드도 같은 자동 보정을 수행한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 git 이력 판정] |

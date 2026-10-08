---
title: "efdc turbulence"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_turbulence.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

## Scope

How EFDC+ runs the original Mellor-Yamada 2.5 closure (CALQQ1 / CALQQ2T + CALAVB), how `ISTOPT(0)` selects Galperin / Kantha-Clayson / Kantha 2003 stability functions, how the modern GOTM_Turbulence module replaces it when `ISGOTM > 0`, and how `q²` and `q²L` boundary conditions are imposed at surface and bottom. Use this when picking a closure, swapping in GOTM, or interpreting `AV/AB/AQ` output. **수평 운동량 확산 (HMD, Smagorinsky)은 본 노트 범위 밖** — [[efdc_dispersion]] 참조.

## Source basis

- `calqq1.f90`, `calqq2t.f90` — `q²` (= QQ) and `q²L` (= QQL) equation assembly and tridiagonal solve.
- `calavb.f90` — vertical viscosity / diffusivity assembly with stability functions.
- `mod_var_global.f90:1004, 1092, 1104, 1106-1108` — array storage definitions.
- `input.f90:643-708` — input cards C12 (background mixing, max), C12A (`ISTOPT`), C12B (`ISGOTM`).
- `hdmt.f90:1274, 1283`; `hdmt2t.f90:533-579, 879-968, 993` — main-loop dispatch and BC setup.
- `GOTM_Turbulence/mod_gotm.f90`, `mod_turbulence.F90` — GOTM integration.

## A. Entry points

| Path | Driver | Calls |
|---|---|---|
| Original MY2.5 (3TL) | `HDMT` | `CALAVB` then `CALQQ1` (`hdmt.f90:1274, 1283`) |
| Original MY2.5 (2TL) | `HDMT2T` | `CALAVB` then `CALQQ2T` (`hdmt2t.f90:533, 577, 993`) |
| GOTM (`ISGOTM > 0`) | `HDMT2T` | `Advance_GOTM(ISTL)` replaces both (`hdmt2t.f90:535-579`) |

`CALQQ1` and `CALQQ2T` solve for:
- `QQ = q²` (turbulent intensity squared).
- `QQL = q²L` (later converted to `DML = QQL/QQ`).

## B. Stability functions (CALAVB)

Stability functions live in **CALAVB**, not in `CALQQ*`. `ISTOPT(0)` selects:

| `ISTOPT(0)` | Family | File:Line |
|---|---|---|
| default (not 2/3) | Galperin et al. | `calavb.f90:44-51` |
| `2` | Kantha-Clayson 1994 | `:53-62` |
| `3` | Kantha 2003 | `:64-73` |

Richardson-number form:
- `RIQ = −GP * HP * DML² * DZIG * (B(k+1) − B(k)) / QQ` (clamped) (`:150-152`).
- `SFAV = SFAV0 * (1 + SFAV1*RIQ) / ((1 + SFAV2*RIQ)*(1 + SFAV3*RIQ))` (`:153`) — momentum stability φ_A (theory Eq 2.15).
- `SFAB = SFAB0 / (1 + SFAB1*RIQ)` (`:154`) — scalar/buoyancy stability ρ_K.

Stability-function constant values (verified 2026-06-03, `calavb.f90:44-73`; `SFAV0=0.392010` common):

| `ISTOPT(0)` | — | — | — | — | — | Table 2.1의 Galperin·Kantha–Clayson·Kantha 수치는 코드의 SFAV·SFAB 상수와 대응한다. (`calavb.f90:45` — `SFAV0= 0.392010`; `calavb.f90:46` — `SFAV1= 7.760050`; `calavb.f90:56` — `SFAV1= 8.679790`; `calavb.f90:57` — `SFAV2 = 30.192000`; `calavb.f90:58` — `SFAV3= 6.127200`; `calavb.f90:60` — `SFAB1 = 30.192000`; `calavb.f90:67` — `SFAV1 = 14.509100`; `calavb.f90:68` — `SFAV2 = 24.388300`; `calavb.f90:69` — `SFAV3= 3.236400`; `calavb.f90:71` — `SFAB1 = 24.388300`; `calavb.f90:47` — `SFAV2 = 34.676440`; `calavb.f90:48` — `SFAV3= 6.127200`; `calavb.f90:49` — `SFAB0= 0.493928`; `calavb.f90:50` — `SFAB1 = 34.676440`; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) 식 2.18·2.19의 R2·R3 정의는 표의 열 이름과 바뀌어 있다. (EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽, 식 2.18; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽, 식 2.19) 점성 분모는 곱의 순서가 결과에 영향을 주지 않는다. (EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) 스칼라 확산은 SFAB1=34.676440을 쓰므로 표의 R3=6.127200을 대입하면 결과가 다르다. (`calavb.f90:50` — `SFAB1 = 34.676440`; `calavb.f90:154` — `SFAB = SFAB0/(1.+SFAB1*RIQ)`; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) RIQ는 밀도 기울기에 음의 부호를 붙인다. (`calavb.f90:150` — `RIQ = -GP*HP(L)*DML(L,K)*DML(L,K)*DZIG(L,K)*(B(L,K+1)-B(L,K))/QQ(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) A0의 두 표현은 제시한 MY 상수에서 완전히 같지 않다. (EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) 기본 분기는 Galperin이며 MY1982 원본 상수의 독립 분기는 없다. (`calavb.f90:46` — `SFAV1= 7.760050`; `calavb.f90:54` — `if( ISTOPT(0) == 2 )then`; `calavb.f90:65` — `if( ISTOPT(0) == 3 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) |
|---|---|---|---|---|---|---|
| 0/1 default | Galperin et al. 1988 | 7.760050 | 34.676440 | 6.127200 | 0.493928 | 34.676440 |
| `2` | Kantha-Clayson 1994 | 8.679790 | 30.192000 | 6.127200 | 0.493928 | 30.192000 |
| `3` | Kantha 2003 | 14.509100 | 24.388300 | 3.236400 | 0.490025 | 24.388300 |

Table 2.1의 Galperin·Kantha–Clayson·Kantha 수치는 코드의 SFAV·SFAB 상수와 대응한다. (`calavb.f90:45` — `SFAV0= 0.392010`; `calavb.f90:46` — `SFAV1= 7.760050`; `calavb.f90:56` — `SFAV1= 8.679790`; `calavb.f90:57` — `SFAV2 = 30.192000`; `calavb.f90:58` — `SFAV3= 6.127200`; `calavb.f90:60` — `SFAB1 = 30.192000`; `calavb.f90:67` — `SFAV1 = 14.509100`; `calavb.f90:68` — `SFAV2 = 24.388300`; `calavb.f90:69` — `SFAV3= 3.236400`; `calavb.f90:71` — `SFAB1 = 24.388300`; `calavb.f90:47` — `SFAV2 = 34.676440`; `calavb.f90:48` — `SFAV3= 6.127200`; `calavb.f90:49` — `SFAB0= 0.493928`; `calavb.f90:50` — `SFAB1 = 34.676440`; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) 식 2.18·2.19의 R2·R3 정의는 표의 열 이름과 바뀌어 있다. (EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽, 식 2.18; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽, 식 2.19) 스칼라 확산은 SFAB1=34.676440을 쓰므로 표의 R3=6.127200을 대입하면 결과가 다르다. (`calavb.f90:50` — `SFAB1 = 34.676440`; `calavb.f90:154` — `SFAB = SFAB0/(1.+SFAB1*RIQ)`; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) RIQ는 밀도 기울기에 음의 부호를 붙인다. (`calavb.f90:150` — `RIQ = -GP*HP(L)*DML(L,K)*DML(L,K)*DZIG(L,K)*(B(L,K+1)-B(L,K))/QQ(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) A0의 두 표현은 제시한 MY 상수에서 완전히 같지 않다. (EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽) 기본 분기는 Galperin이며 MY1982 원본 상수의 독립 분기는 없다. (`calavb.f90:46` — `SFAV1= 7.760050`; `calavb.f90:54` — `if( ISTOPT(0) == 2 )then`; `calavb.f90:65` — `if( ISTOPT(0) == 3 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 27쪽·인쇄 14쪽)

Then:
- `AB = SFAB * DML * HP * sqrt(QQ) + AVBXY` (`:155`).
- `AV = SFAV * DML * HP * sqrt(QQ) + AVOXY` (`:156`).

Both depth-normalized afterward (`:157, 158`). Background `AVOXY/AVBXY` come from card C12 (`input.f90:643-652`: `AVO, ABO, AVMX, ABMX`).

## C. Production and dissipation

- **Buoyancy**: `PQQB = AB * GP * HP * DZIG * (B(k+1) − B(k))` (`calqq2t.f90:274`; 3TL `calqq1.f90:326`).
- **Shear**: `PQQU = AV * DZIGSD4U * (du/dz)²` (`calqq2t.f90:276`); same for `PQQV` (`:277`).
- `q²` RHS: gets `2*PQQ` (consistent with `QQ = q²` while production is TKE-style) (`:278-279`).
- 코드의 q²l 생성은 CTE1·전단+CTE3TMP·부력이다. (`calqq2t.f90:280` — `PQQL = DELT*HP(L)*(CTE3TMP*PQQB + CTE1*(PQQU+PQQV) + CE4VEG*PQQVEGE(L,K) + CE4MHK*PQQMHKE(L,K) + CE4SUP*PQQSUPE(L,K))`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) 문서처럼 E1을 부력항의 E3에도 다시 곱하지 않는다. (`calqq2t.f90:280` — `PQQL = DELT*HP(L)*(CTE3TMP*PQQB + CTE1*(PQQU+PQQV) + CE4VEG*PQQVEGE(L,K) + CE4MHK*PQQMHKE(L,K) + CE4SUP*PQQSUPE(L,K))`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) CTE3TMP는 성층 조건에 따라 달라진다. (`calqq2t.f90:267` — `DELB = B(L,K) - B(L,K+1)`; `calqq2t.f90:268` — `CTE3TMP = CTE3`; `calqq2t.f90:269` — `if( DELB < 0.0 ) CTE3TMP = CTE1`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) CTE2는 입력 코드가 미사용으로 명시한다. (`input.f90:734` — `! *** PMC - CTE2 NOT USED`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) IFPROX는 벽 역거리 제곱을 직접 만든다. (`aaefdc.f90:1523` — `if( IFPROX == 1 ) FPROX(L,K) = 1./(VKC*Z(L,K))**2 + 1./(VKC*(1. - Z(L,K)))**2`; `aaefdc.f90:1525` — `if( IFPROX == 2 ) FPROX(L,K) = (1./(VKC*Z(L,K))**2) + CTE5*(1./(VKC*(1.-Z(L,K)))**2)/(CTE4+0.00001)`; `aaefdc.f90:1527` — `if( IFPROX == 3 ) FPROX(L,K) = 1./(VKC*MIN(Z(L,K),(1. - Z(L,K))))**2`; `aaefdc.f90:1529` — `if( IFPROX == 4 ) FPROX(L,K) = 1./(VKC*(1. - Z(L,K)))**2`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽)

코드는 BETAMHK_P를 음해 난류 소멸계수에 적용한다. (`calqq2t.f90:229` — `TMPQQI = 0.5*BETAMHK_P`; `calqq2t.f90:231` — `PQQMHKI(L,K) = TMPQQI*(FXMHK(L,K)+FXMHK(L,K+1)+FYMHK(L,K)+FYMHK(L,K+1))`; `calqq2t.f90:354` — `+ DELT*HPI(L)*(PQQVEGI(L,1)+PQQMHKI(L,1)+PQQSUPI(L,1))`; EFDC_Theory_Document_Ver_12.pdf, PDF 248쪽·인쇄 235쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 250쪽·인쇄 237쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽) 코드는 BETAMHK_D를 명시 난류 생성원에 적용한다. (`calqq2t.f90:230` — `TMPQQE = 0.5*BETAMHK_D`; `calqq2t.f90:232` — `PQQMHKE(L,K) = TMPQQE*(FXMHK(L,K)*U(L,K)*U(L,K) + FXMHK(L,K+1)*U(L,K+1)*U(L,K+1) &`; `calqq2t.f90:278` — `PQQ  = DELT*( PQQB+PQQU+PQQV+PQQVEGE(L,K)+PQQMHKE(L,K)+PQQSUPE(L,K) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 248쪽·인쇄 235쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 250쪽·인쇄 237쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽)


`CTE3TMP` = `CTE3` if `DELB > 0`, else `CTE1` (stable vs unstable buoyancy switch) (`:267-269`).

**Dissipation** is implicit in the tridiagonal diagonal:
- `q²`: `+ 2*DELT * QQSQR / (CTURBB1 * DML * HP)` (`calqq2t.f90:353`).
- `q²L`: `+ DELT * (QQSQR/(CTURBB1*DML*HP)) * (1 + CTE4*DML²*FPROX)` (`:355`).

`FPROX` = wall proximity function (`aaefdc.f90:1519-1530`).

## D. CALQQ1 (3TL) vs CALQQ2T (2TL) variant

- `CALQQ2T` uses dynamic timestep `DTDYN` when `ISDYNSTP /= 0` (`calqq2t.f90:47-53`); `CALQQ1` switches `DT2/DT` by `ISTL` (`calqq1.f90:50-57`).
- `CALQQ2T` uses current `QQ/QQL` directly in flux assembly (`:130-152`); `CALQQ1` uses `QQ1/QQL1` for `ISTL==2` and `QQ2/QQL2` (doubled) for 3TL (`:137-205`).
- 코드는 BETAMHK_P를 음해 난류 소멸계수에 적용한다. (`calqq2t.f90:229` — `TMPQQI = 0.5*BETAMHK_P`; `calqq2t.f90:231` — `PQQMHKI(L,K) = TMPQQI*(FXMHK(L,K)+FXMHK(L,K+1)+FYMHK(L,K)+FYMHK(L,K+1))`; `calqq2t.f90:354` — `+ DELT*HPI(L)*(PQQVEGI(L,1)+PQQMHKI(L,1)+PQQSUPI(L,1))`; EFDC_Theory_Document_Ver_12.pdf, PDF 248쪽·인쇄 235쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 250쪽·인쇄 237쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽) 코드는 BETAMHK_D를 명시 난류 생성원에 적용한다. (`calqq2t.f90:230` — `TMPQQE = 0.5*BETAMHK_D`; `calqq2t.f90:232` — `PQQMHKE(L,K) = TMPQQE*(FXMHK(L,K)*U(L,K)*U(L,K) + FXMHK(L,K+1)*U(L,K+1)*U(L,K+1) &`; `calqq2t.f90:278` — `PQQ  = DELT*( PQQB+PQQU+PQQV+PQQVEGE(L,K)+PQQMHKE(L,K)+PQQSUPE(L,K) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 248쪽·인쇄 235쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 250쪽·인쇄 237쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽) Theory 식 10.3과 10.26–10.30은 βp를 생성에 적용한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 248쪽·인쇄 235쪽, 식 10.3; EFDC_Theory_Document_Ver_12.pdf, PDF 250쪽·인쇄 237쪽, 식 10.26; EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽, 식 10.30) 같은 식은 βd를 소멸에 적용한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 248쪽·인쇄 235쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 250쪽·인쇄 237쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽) 코드 변수 이름과 문서의 역할을 구별한다. (`calqq2t.f90:229` — `TMPQQI = 0.5*BETAMHK_P`; `calqq2t.f90:230` — `TMPQQE = 0.5*BETAMHK_D`; `calqq2t.f90:231` — `PQQMHKI(L,K) = TMPQQI*(FXMHK(L,K)+FXMHK(L,K+1)+FYMHK(L,K)+FYMHK(L,K+1))`; `calqq2t.f90:232` — `PQQMHKE(L,K) = TMPQQE*(FXMHK(L,K)*U(L,K)*U(L,K) + FXMHK(L,K+1)*U(L,K+1)*U(L,K+1) &`; `calqq2t.f90:278` — `PQQ  = DELT*( PQQB+PQQU+PQQV+PQQVEGE(L,K)+PQQMHKE(L,K)+PQQSUPE(L,K) )`; `calqq2t.f90:354` — `+ DELT*HPI(L)*(PQQVEGI(L,1)+PQQMHKI(L,1)+PQQSUPI(L,1))`; EFDC_Theory_Document_Ver_12.pdf, PDF 248쪽·인쇄 235쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 250쪽·인쇄 237쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽)

There is **no literal `AB ln` symbol** in this source — that nomenclature appears to be from older documentation; the actual variant difference is `CALQQ1` vs `CALQQ2T`.

## E. Storage (AV / AB / AQ / AVMX)

| Symbol | Meaning | Lines |
|---|---|---|
| `AB(LCM,KCM)` | Vertical diffusivity (depth-normalized, m/s — physical m²/s ÷ depth) | `mod_var_global.f90:1092` |
| `AV(LCM,KCM)` | Vertical viscosity (depth-normalized) | `:1105` |
| `AQ(LCM,KCM)` | Diffusivity for `QQ/QQL` | `:1103` |
| `AVOXY` | Spatially varying background `AVO` | `:1106` |
| `AVBXY` | Spatially varying background `ABO` | `:1107` |
| `AVMX` | Maximum `AV` cap from input | `:1003` |

Note: code uses `AVMX`, **not `AVOMX`** (older docs). Maximum limit applies via `AVMX*HPI`, `ABMX*HPI` (`calavb.f90:273-276`).

## F. ISTOPT(0) dispatch

`ISTOPT(0)` is read from card C12A (`input.f90:664-681`). It does **not** select GOTM (that is `ISGOTM`). It selects original-EFDC coefficient behavior inside CALAVB:

- Default Galperin if `!= 2, 3`.
- `==2`: Kantha-Clayson 1994.
- `==3`: Kantha 2003 (also changes `SQLDSQ = 0.377/0.628` for `AQ/QQL` diffusion ratio in `calqq*.f90:109-111`).

## G. GOTM integration (ISGOTM)

`ISGOTM` from card C12B (`input.f90:689-708`).

When `ISGOTM > 0`:
- `Init_GOTM` sets up GOTM turbulence + tridiagonal init (`mod_gotm.f90:17-25`).
- `Advance_GOTM(ISTL)` replaces `CALAVB` (`hdmt2t.f90:535-579`).

Per-step bridge:
1. EFDC buoyancy frequency `NN` and shear frequency `SS` passed in (`mod_gotm.f90:78-156`).
2. Each EFDC water-column copied into 1D GOTM arrays (`:271-288`).
3. `do_turbulence` called (`:290-292`).
4. GOTM `num/nuh` copied back into EFDC `AV/AB` (`:294-299`).

GOTM internal: `do_turbulence` calls production, stability functions, TKE eq, length-scale eq, then Kolmogorov-Prandtl `μ_t = c_μ * sqrt(k) * L` for first-order turbulence (`mod_turbulence.F90:2727-2756`). MY option inside GOTM dispatched by `tke_method == tke_MY` → `q2over2eq` (`:2863-2872`).

This gives access to GOTM's k-ε, k-ω, GLS-family closures while keeping EFDC's hydrodynamics core unchanged.

## H. Surface / bottom BCs for q² and q²L

Original EFDC sets `QQ(L,0)` (bottom) and `QQ(L,KC)` (surface) **before** solving CALQQ2T:

- Non-wave path: bottom from `TBX/TBY`, surface from `TSX/TSY` (`hdmt2t.f90:879-893`).
- Corner-corrected path: modifies bottom stress weighting (`:892-931`).
- Wave path: includes current + wave bottom stress (`:939-964`).

These enter the `q²` tridiagonal RHS at boundaries (`calqq2t.f90:361, 393-399`).

The `q²L` equation does **not** inject explicit Dirichlet values; it relies on vertical diffusion + wall proximity dissipation `FPROX` (`:355, 385, 413`).

For GOTM-MY:
- `q2over2_bc`: log-layer Dirichlet `u_τ² * b1^(2/3) / 2`; Neumann zero (`mod_turbulence.F90:3555-3560`).
- `q2l_bc`: log-layer Dirichlet `2*κ*ki*(zi+z₀)`; Neumann `−2*sqrt(2)*sl*κ²*ki^1.5*(zi+z₀)` (`:3964-3969`).

## Decision Guide

| Goal | Setting |
|---|---|
| Standard estuarine MY2.5 | `ISTOPT(0)=0` (Galperin), `ISGOTM=0` |
| Strong stratification (salt wedge) | `ISTOPT(0)=2` (Kantha-Clayson) |
| Highly stratified shelf | `ISTOPT(0)=3` (Kantha 2003) |
| K-ε / K-ω closure | `ISGOTM=1` with GOTM `tke_method=tke_keps` etc. |
| Wave-dominated nearshore | `ISGOTM=0` MY2.5 with `IS2TIM>=1` (CALQQ2T includes vegetation/MHK terms) |
| Turbulence diagnostic output needed | Output `AV`, `AB` to history (`m²/s` after multiplying by depth) |

## Working Rules

- AVO·ABO·AVMX·ABMX는 C12 입력값이다. (`input.f90:643` — `read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL`) 확인한 원문은 1E−5와 0.5를 공통 기본값으로 고정하지 않는다. (`input.f90:643` — `read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL`) Confluence C12의 수치 행은 카드 예시이다. (`models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_12.md:41` — `|  | 0 | 0.025 | 0.000001 | 1.00E-07 | 0.000001 | 1.00E-07 | 0 | 1 | 0.002 |`) ‘never set to zero’는 확인한 코드 제약으로 입증하지 못했다. (`input.f90:643` — `read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL`) 특정 안정성 효과는 실행 결과가 있어야 확인한다. (`calavb.f90:273` — `AVTMP = AVMX*HPI(L)`; `calavb.f90:275` — `AV(L,K) = min(AV(L,K),AVTMP)`)
- AVO·ABO·AVMX·ABMX는 C12 입력값이다. (`input.f90:643` — `read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL`) 확인한 원문은 1E−5와 0.5를 공통 기본값으로 고정하지 않는다. (`input.f90:643` — `read(1,*,IOSTAT = ISO) AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL`) AVMX 상한은 선택 경로에서 AVMX/H로 적용한다. (`calavb.f90:273` — `AVTMP = AVMX*HPI(L)`; `calavb.f90:275` — `AV(L,K) = min(AV(L,K),AVTMP)`) 특정 안정성 효과는 실행 결과가 있어야 확인한다. (`calavb.f90:273` — `AVTMP = AVMX*HPI(L)`; `calavb.f90:275` — `AV(L,K) = min(AV(L,K),AVTMP)`)
- For GOTM coupling, ensure `gotm_input.nml` is consistent with EFDC vertical resolution; mismatched layer counts crash silently.
- `ISTOPT(0)` change between Galperin/Kantha mid-run is non-trivial — close the run, restart cleanly.
- MY2.5 dissipation is implicit-in-diagonal; explicit dissipation forms in older theory papers don't apply to this code.

## Common Pitfalls

- ▢ Confusing `AV` (depth-normalized, m/s) with physical vertical viscosity (m²/s) — output `AV * HP` for physical units.
- ▢ Looking for `AVOMX` symbol — code uses `AVMX`.
- ▢ Setting `ISGOTM=1` but forgetting `gotm_input.nml` — `Init_GOTM` errors at startup.
- ▢ Expecting "AB ln" symbol from old docs — the actual variant is `CALQQ1` (3TL) vs `CALQQ2T` (2TL); the latter has additional vegetation/structure sink terms in the diagonal.
- ▢ Wall proximity `FPROX` formulation — different forms initialize at `aaefdc.f90:1519-1530`; choice depends on whether you want Mellor's parabolic or alternative form. Verify the active branch matches your case (free-surface vs bottom-bounded).

## Next expansion

- Wave-current bottom stress note for sediment coupling (cross-link to `efdc_sediment.md`).
- GOTM closure choice walk-through (k-ε vs k-ω vs GLS).
- Vegetation drag in `q²L` equation detailed derivation.

## References

- Mellor & Yamada 1982 (MY 2.5 baseline).
- Galperin et al. 1988 (stability functions).
- Kantha & Clayson 1994; Kantha 2003.
- Umlauf & Burchard 2003 (GOTM/GLS framework).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.

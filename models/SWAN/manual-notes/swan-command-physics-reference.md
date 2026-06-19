---
title: "SWAN swanuse §4.5.4 Physics commands reference — GEN/WCAPPING/QUADRUPL/BREAKING/FRICTION/TRIAD/VEGETATION 구문·default verbatim"
topic: swan
canonical_source: external
external_source: "swanuse.pdf (User Manual, SWAN Cycle III version 41.51) §4.5.4 Physics (p.57-83) + node28.md. 각 command 구문·파라미터·default·키워드. swantech 물리(이론)의 user-command 대응."
citation_status: verified
verification_method: "swanuse website_markdown node28.md (Physics, 1577줄) 직접 read: GEN1/2/3(ST6 RBW12 calibration lines)·SSWELL·NEGATINP·WCAPPING·QUADRUPL·BREAKING·FRICTION·TRIAD·VEGETATION 구문+default verbatim. swanuse.pdf §4.5.4 TOC 대조. 나머지(MUD/SICE/TURBULENCE/BRAGG/LIMITER/OBSTACLE/SETUP/DIFFRACTION/SURFBEAT/SCAT/OFF)는 요약."
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — command 구문·default 값 verbatim"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md
  - models/SWAN/manual-notes/swan-tech-ch2-nonlinear-detailed.md
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
---

# SWAN swanuse §4.5.4 Physics commands reference — verified

> swanuse.pdf (User Manual v41.51) §4.5.4 Physics 직접 read. **이론(swantech) ↔ user command(swanuse)** 대응 — 각 물리 command 의 정확 **구문·파라미터·default**. [[swan-documentation-stack]] 가 forward-link 한 command reference (physics 부분). 이론 detail 은 각 `swan-tech-ch2-*` 참조.

## 1. GEN3 — wind input + quadruplet + whitecapping 3rd-gen ★

```
GEN3 < KOMen [cds2] [stpm] | -> WESTHuysen | ST6 [a1sds] [a2sds] [p1sds] [p2sds] ... > (AGROW [a])
```
- **3rd-gen mode** (wind input + quadruplet + whitecapping 동시). triad·friction·breaking 은 **별도 활성**. `U_10 → U_*` wind drag 변환.
- **WESTH = default** (saturation-based whitecapping + Yan 1987 wind, [[swan-tech-ch2-dissipation-detailed]] §2)
- **KOMEN**: WAM Cycle 3 (Komen 1984 exp growth). `cds2=2.36e-5`, `stpm=3.02e-3`
- **JANSSEN**: WAM Cycle 4. `cds1=4.5`, `delta=0.5`
- **ST6** (Rogers 2012 RBW12, [[swan-tech-ch2-dissipation-detailed]] §4): `a1sds`(local diss T1) `a2sds`(cumulative T2) `p1sds=p2sds=4`. 키워드: `UP`(default, E_T norm)/DOWN, wind drag `HWANG`(default)/FAN/ECMWF, `VECTAU`(default)/SCATAU, `U10PROXY [windscaling]`(default, U10=windscaling×U_*, **windscaling 32** — RBW12 28에서 변경)/TRUE10, `DEBIAS [cdfac]`(wind bias 보정 cdfac=mean(τ_obs)/mean(τ_model))
- **AGROW**: linear growth(Cavaleri-Malanotte-Rizzoli 1981) 활성, `a=0.0015`. 미사용 시 nonstationary INIT ZERO 에선 경계/AGROW 없으면 에너지 0 유지

**ST6 권장 calibration lines** (RBW12, [windscaling]별 a1sds/a2sds 상이):
```
GEN3 ST6 4.7E-7 6.6E-6 U10P 28. AGROW      ! windscaling 28
GEN3 ST6 2.8E-6 3.5E-5 U10P 32. AGROW      ! windscaling 32 (mean square slope 개선)
GEN3 ST6 6.5E-6 8.5E-5 ... U10PROXY 35.0 AGROW
```
> ST6 사용 시 **SSWELL 별도 지정 필수**.

## 2. SSWELL — swell dissipation (ST6 짝)

```
SSWELL < -> ARDhuin [cdsv] | ZIEger [b1] >
```
- **ARDHUIN** (Ardhuin 2010, WW3/ST4 non-breaking) `cdsv=1.2` 예
- **ZIEGER** (WW3 v4, steepness-dependent 미포함) — **NEGATINP 와 함께** (negative wind input). 예 `SSWELL ZIEGER 0.00025` + `NEGATINP 0.04`
> [[swan-tech-ch2-dissipation-detailed]] §4 SSWELL ZIEGER/ARDHUIN.

## 3. WCAPPING — whitecapping (GEN3 와 별도 조정)

```
WCAP < KOMEN [cds2] [stpm] [powst] [delta] [powk] | -> AB [cds2] [br] CURrent [cds3] >
```
- **AB = default** (Alves-Banner 2003 / Van der Westhuysen 2007): `cds2=5.0e-5`, `br=1.75e-3`(threshold saturation). `CURRENT` (Van der Westhuysen 2012 enhanced current diss) `cds3=0.8`
- **KOMEN**: `cds2=2.36e-5`, `stpm=3.02e-3`, `powst=2`, **`delta=1`** (40.91A부터 변경, 저주파/mean period 개선; 원래 0=WAM Cycle 3), `powk=1`
> [[swan-tech-ch2-dissipation-detailed]] §1-3 (Eq 2.43-2.58). `OFF WCAP` 비활성.

## 4. QUADRUPL — quadruplet nonlinear

```
QUADrupl [iquad] [lambda] [Cnl4] [Csh1] [Csh2] [Csh3]
```
- **`iquad` = 2 default**: 1=semi-impl DIA/sweep, **2=explicit DIA/sweep**, 3=explicit DIA/iteration (**current 시 권장** — sweep간 freq overlap 비보존 방지), 8=fast(piecewise const interp), 4=Multiple DIA, **51=XNL deep / 52=XNL+WAM depth scaling / 53=XNL finite depth** ([[swan-tech-ch2-nonlinear-detailed]] §A.2)
- `lambda=0.25`, `Cnl4=3e7`, `Csh1=5.5`, `Csh2=0.833333`, `Csh3=-1.25` (DIA, [[swan-tech-ch2-nonlinear-detailed]] §A.1 Eq 2.75-2.79)
> DIA 는 long-crested·freq resolution 10%+ 편차 시 부정확. `OFF QUAD` 비활성.

## 5. BREAKING — depth-induced breaking

```
BREaking < -> CONstant [alpha] [gamma] | BKD [alpha] [gamma0] [a1] [a2] [a3] >
```
- **CONSTANT = default**: `alpha=1.0`, **`gamma=0.73`** (breaker index H_max/d, Battjes-Stive 1985)
- **BKD** (γ scales with bottom slope β + dimensionless depth kd): `alpha=1.0`, `gamma0=0.54`, `a1=7.59`, `a2=-8.06`, `a3=8.09`
> [[swan-tech-ch2-dissipation-detailed]] §6 (Eq 2.64-2.68). command 미사용해도 **default breaking 적용** (끄려면 `OFF BREAKING`).

## 6. FRICTION — bottom friction

```
FRICtion < -> JONswap CONstant [cfjon] | COLLins [cfw] | MADsen [kn] | RIPples [S] [D] >
```
- **JONSWAP = default** (Hasselmann 1973): **`cfjon=0.038`** m²s⁻³ (sandy 권장, wind-sea+swell 공통; **0.067 권장 안 함**, smoother Gulf of Mexico 0.019)
- **COLLINS** (1972): `cfw=0.015`
- **MADSEN** (1988): `kn=0.05` m (roughness length)
- **RIPPLES** (Smith 2011, ripple+sediment 의존): `S=2.65`(specific gravity), `D=0.0001` m(sediment diameter)
> [[swan-tech-ch2-dissipation-detailed]] §5 (Eq 2.59-2.63). cfw/kn 은 INPGRID FRICTION 으로 spatial 가능. **command 미사용 시 friction 무시** (default off).

## 7. TRIAD — triad nonlinear (shallow)

```
TRIad < -> DCTA [trfac] [p] COLL|NONC | LTA [trfac] | FTIM [trfac] | SPB [trfac] [a] > BIPHASE ... TRANSFER ...
```
- **DCTA = default** (Booij 2009): `trfac=4.4`, `p=4/3`(high-freq tail), **`COLL` default**(collinear)/NONC(noncollinear) ([[swan-tech-ch2-nonlinear-detailed]] §B.7)
- **LTA** (extended): `trfac=1.0` (§B.4) / **FTIM** (§B.2): `trfac=1.0` / **SPB** (Becq-Girard 1999, §B.3): `trfac=0.9`, `a=0.95`(K=a·k_loc)
- **BIPHASE**: `ELDEBERKY`(default, Ursell `urcrit=0.63` — Eldeberky 0.2/Doering-Bowen 0.63) / `DEWIT`(2022, bed slope+peak period, `lpar=0` no averaging) (§B.5)
- **TRANSFER** (DCTA 제외): FG(Freilich-Guza1984)/MS(Madsen-Sørensen1993)/BREDMOSE(2005)/**QUADWAVE=default**(Akrish 2024) (§B.6)
> command 미사용 시 **triad 무시**.

## 8. VEGETATION — wave damping (vegetation)

```
VEGEtation [iveg] < [height] [diamtr] [nstems] [drag] >
```
- **`iveg`=1 default** (Suzuki 2011, Dalrymple 1984 cylinder, freq-uniform) / 2 (Jacobsen 2019 freq-dependent canopy, **수직 layering 미지원**)
- 수직 segment 별 `height`/`diamtr`/`nstems`(plants/m²)/`drag` 반복 (rigid plants)
> [[swan-tech-ch2-vegetation-ice-bragg-gen12]] §2.3.5.

## 9. 기타 physics command (요약, default off 또는 별도)

| command | 기능 | 본 위키 |
|---|---|---|
| `NEGATINP [rdcoef]` | negative wind input (swell, ZIEGER 짝) | dissipation §4 |
| `MUD [layer] [rhom] [viscm]` | fluid mud 감쇠 | (없음) |
| `SICE` (R19/D15/M18/R21B) | sea ice 감쇠 (4 methods) | veg-ice-bragg §2.3.6 |
| `TURBULENCE` | turbulent viscosity 감쇠 | (없음) |
| `BRAGG` (CON/FILE) | Bragg scattering (Ardhuin-Herbers 2002) | veg-ice-bragg §2.3.7 |
| `LIMITER [ursell] [qb]` | Ursell·Qb limiter | (없음) |
| `OBSTACLE` (TRANS/REFL/FREEBOARD) | sub-grid obstacle | [[swan-tech-ch2-obstacles-diffraction-setup]] §1-3 |
| `SETUP [supcor]` | wave-induced set-up (open coast) | obstacles-diffraction-setup §5 / [[swan-tech-ch4-5-bc-2d-setup]] |
| `DIFFRACtion [idiffr] [smpar] [smnum]` | phase-decoupled diffraction (Holthuijsen 2003) | obstacles-diffraction-setup §4 |
| `SURFBEAT` | 1D infragravity (Reniers IEM) | [[swan-surfbeat-iem]] |
| `SCAT` | quasi-coherent scattering (Smit-Janssen 2013) | [[swan-quasi-coherent]] / [[swan-tech-ch2-7-qcm-theory]] |
| `OFF <BREAKING\|WCAP\|QUAD\|...>` | 특정 process 비활성 | — |

## 10. 핵심 default 요약표 (실무 tuning)

| command | default | 주요 default 값 |
|---|---|---|
| GEN3 | WESTH | windscaling 32(ST6), AGROW a=0.0015 |
| WCAP | AB | cds2=5e-5, br=1.75e-3 / KOMEN cds2=2.36e-5, **delta=1** |
| QUADRUPL | iquad=2 | lambda=0.25, Cnl4=3e7 |
| BREAKING | CONSTANT | **alpha=1, gamma=0.73** |
| FRICTION | (off; JONSWAP cfjon=0.038 권장) | Collins 0.015 / Madsen kn=0.05 |
| TRIAD | (off; DCTA trfac=4.4 p=4/3) | SPB a=0.95, BIPHASE urcrit=0.63 |

> ★ default 값이 swantech 식의 계수와 일치 (예 KOMEN cds2=2.36e-5 = [[swan-tech-ch2-dissipation-detailed]] Eq 2.44 C_ds WAM Cycle 3; gamma=0.73 = Eq 2.68 Battjes-Stive).

## 11. 한계

- node28(1577줄) 중 MUD/TURBULENCE/LIMITER/OBSTACLE/SETUP/DIFFRACTION/SURFBEAT/SCAT 의 정밀 파라미터·default 는 §9 요약만 — 개별 deep 후속.
- swanuse §4.4 Start-up(PROJECT/SET/MODE/COORDINATES) + §4.5.1-3 grid/input/BC + §4.5.5 NUMERIC + §4.6 output command 미커버 (별도 노트).
- ST6 [a1sds]/[a2sds] 의 windscaling별 calibration 상호의존 — RBW12 원논문([[swan-foundational-papers]]) 참조.

## 12. 연결

- [[swan-documentation-stack]] — 4 docs + 57 command 목록 (본 노트가 physics 부분 deep)
- [[swan-tech-ch2-dissipation-detailed]] — WCAPPING/BREAKING/FRICTION/ST6 이론
- [[swan-tech-ch2-nonlinear-detailed]] — QUADRUPL/TRIAD 이론
- [[swan-tech-ch2-sources-sinks]] — GEN wind input 이론
- [[swan-foundational-papers]] — Rogers2012(ST6)·Becq-Girard1999(SPB)·Akrish2024(QuadWave) 원논문

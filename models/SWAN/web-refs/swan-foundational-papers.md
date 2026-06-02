---
title: "SWAN foundational source papers — swantech 인용 원논문 bibliographic + abstract 정리"
topic: swan
canonical_source: external
external_source: "8 SWAN 원논문 (swantech.pdf v41.51 reference 기반): Booij-Holthuijsen 1987 (GSE), Holthuijsen-Herman-Booij 2003 (diffraction), Van Vledder 2006 (XNL4/WRT), Rogers 2012 + Zieger 2015 (ST6), Smit-Janssen 2013 (QC), Dietrich 2013 (refraction limiter), Akrish 2020 (QC current). Booij-Ris-Holthuijsen 1999 (foundational)은 [[swan-booij-1999-jgr-foundational]] 별도."
citation_status: verified
verification_method: "WebSearch + 저자/저널 landing-page metadata 직접 fetch (2026-06-02). Bibliographic(저자·연도·저널·권·페이지·DOI) verified; 본문은 paywall(ScienceDirect/MDPI/AMS/Cambridge HTTP 403) → abstract/method 요약은 검색 스니펫·저자 사이트(ccht.ccee.ncsu.edu)·landing page 기반. DOI 직접확인: Smit-Janssen(AMS) / Van Vledder(ScienceDirect search) / Dietrich(저자사이트 ccht). DOI PII-derived(미직접확인): Holthuijsen2003·Booij-Holthuijsen1987·Akrish2020 — 표기 시 명시."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — WebSearch + landing-page fetch"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-booij-1999-jgr-foundational.md
  - models/SWAN/manual-notes/swan-tech-ch2-7-qcm-theory.md
  - models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md
  - models/SWAN/source-analysis/swan-xnl4-exact-quadruplet.md
---

# SWAN foundational source papers — 원논문 정리

> swantech.pdf (v41.51)가 인용하는 SWAN 핵심 메커니즘의 **원논문 bibliographic + abstract**. 본 위키 tech-notes 가 모두 swantech reference 기반이므로 원문 출처를 명시 통합. **Bibliographic verified, full-text paywall** (booij-1999 패턴, [[swan-booij-1999-jgr-foundational]]).
>
> **DOI 검증 등급**: ✓直 = landing page/저자 사이트 직접확인 / ◇PII = Elsevier PII 유도(표준이나 미직접확인).

## 1. Booij & Holthuijsen 1987 — Garden-Sprinkler Effect (GSE)

- **Booij N, Holthuijsen LH (1987)**, "Propagation of ocean waves in discrete spectral wave models", *Journal of Computational Physics* **68**(2), 307-326. DOI: 10.1016/0021-9991(87)90060-X ◇PII
- **내용**: 이산 spectral 모델의 finite spectral band 을 개별 wave component 로 처리 → **garden-sprinkler effect**. 2 correction 항(longitudinal=frequency dispersion + lateral=directional dispersion)으로 제거.
- **본 위키**: [[swan-tech-ch3-discretization]] §2 GSE (Eq 3.11-3.13 D_ss/D_nn) + [[swan-gse-correction]] (SwanGSECorr.ftn90).

## 2. Battjes & Janssen 1978 — depth-induced breaking (bore model)

- **Battjes JA, Janssen JPFM (1978)**, "Energy loss and set-up due to breaking of random waves", *Proc. 16th Int. Conf. Coastal Engineering* (ICCE), ASCE, 569-587. DOI: 10.1061/9780872621909.034 ◇
- **내용**: random wave breaking 의 bore 기반 총소산 모델 ($D_{tot}$), breaking fraction $Q_b$. SWAN depth-breaking 표준.
- **본 위키**: [[swan-tech-ch2-dissipation-detailed]] §6 (Eq 2.64-2.68) + [[swan-tech-ch3-breaking-source]] (§3.17 Newton 선형화).

## 3. Holthuijsen, Herman & Booij 2003 — phase-decoupled diffraction

- **Holthuijsen LH, Herman A, Booij N (2003)**, "Phase-decoupled refraction–diffraction for spectral wave models", *Coastal Engineering* **49**(4), 291-305. DOI: 10.1016/S0378-3839(03)00065-6 ◇PII
- **Abstract (요약)**: "Conventional spectral wave models can account for all relevant processes of generation, dissipation and propagation, except diffraction. To accommodate diffraction... a **phase-decoupled refraction–diffraction approximation** is suggested. It is expressed in terms of the **directional turning rate** of the individual wave components in the 2D wave spectrum. The approximation is based on the **mild-slope equation** for refraction–diffraction, omitting phase information."
- **본 위키**: [[swan-tech-ch2-obstacles-diffraction-setup]] §4 (Eq 2.138-2.144 δ diffraction parameter).

## 4. Van Vledder 2006 — XNL4 / WRT exact quadruplet

- **Van Vledder GPh (2006)**, "The WRT method for the computation of non-linear four-wave interactions in discrete spectral wave models", *Coastal Engineering* **53**(2-3), 223-242. DOI: 10.1016/j.coastaleng.2005.10.011 ✓直
- **내용**: Webb-Resio-Tracy(WRT) 정확 Boltzmann quadruplet 적분의 이산 spectral 모델(SWAN/WW3) 구현. DIA 대비 $10^3$-$10^4$배 비용.
- **본 위키**: [[swan-tech-ch2-nonlinear-detailed]] §A.2 (Eq 2.80-2.89) + [[swan-xnl4-exact-quadruplet]] (mod_xnl4v5.ftn90 8989 라인).

## 5. Rogers 2012 + Zieger 2015 — ST6 source term package

- **Rogers WE, Babanin AV, Wang DW (2012)**, "Observation-Consistent Input and Whitecapping Dissipation in a Model for Wind-Generated Surface Waves: Description and Simple Calculations", *J. Atmos. Oceanic Technol.* **29**(9), 1329-1346. DOI: 10.1175/JTECH-D-11-00092.1 ◇
- **Zieger S, Babanin AV, Rogers WE, Young IR (2015)**, "Observation-based source terms in the third-generation wave model WAVEWATCH III: Updates and verification" (ST6), *Ocean Modelling* **96**(1), 2-25. DOI: 10.1016/j.ocemod.2015.07.014 ◇PII
- **내용**: 관측 기반 wind input + whitecapping(local + short-wave modulation) + swell dissipation + wind scaling $S_{ws}u_*$. SWAN ST6 = NRL 2008 도입.
- **참고**: Babanin AV (2011), *Breaking and Dissipation of Ocean Surface Waves*, Cambridge Univ. Press (단행본, ST6 물리 배경).
- **본 위키**: [[swan-tech-ch2-dissipation-detailed]] §4 (ST6, SSWELL ZIEGER/ARDHUIN) + [[swan-st6-babanin-implementation]].

## 6. Smit & Janssen 2013 — Quasi-Coherent (QC) central result ★

- **Smit PB, Janssen TT (2013)**, "The Evolution of Inhomogeneous Wave Statistics through a Variable Medium", *Journal of Physical Oceanography* **43**(8), 1741-1758. DOI: 10.1175/JPO-D-13-046.1 ✓直
- **⚠ 정정**: swantech 및 본 위키 일부 메모가 "JFM"으로 표기했으나 실제는 **JPO**(Journal of Physical Oceanography). (Akrish 2020이 JFM.)
- **Abstract (요약)**: "interaction of ocean waves with variable currents and topography... can result in **inhomogeneous statistics** because of coherent interferences... Stochastic wave models, invariably based on... radiative transfer equation (action balance), do not account for these effects. We develop a **generalization of the radiative transfer equation** that includes coherent interferences... transports the **coupled-mode spectrum (a form of the Wigner distribution)**." swantech §2.7 의 central result(Eq 2.153 = 그들 Eq 15).
- **본 위키**: [[swan-tech-ch2-7-qcm-theory]] (§2.7 Wigner/Weyl/QC) + [[swan-quasi-coherent]] (SwanQCM.ftn90).

## 7. Dietrich 2013 — refraction limiter (unstructured SWAN+ADCIRC)

- **Dietrich JC, Zijlema M, Allier P-E, Holthuijsen LH, Booij N, Meixner JD, Proft JK, Dawson CN, Bender CJ, Naimaster A, Smith JM, Westerink JJ (2013)**, "Limiters for spectral propagation velocities in SWAN", *Ocean Modelling* **70**, 85-102. DOI: 10.1016/j.ocemod.2012.11.005 ✓直
- **내용**: coarse bathymetry 에서 refraction 이 단일 mesh vertex 에 에너지 과집중 → 비물리적. **CFL 기반 spectral propagation(refraction + frequency-shift) velocity limiter**. 저자 명시: "These limiters are **not required for model stability**, but they **improve accuracy** by reducing local errors that would otherwise spread throughout the computational domain."
- **본 위키**: [[swan-tech-ch3-refraction-limiter]] (§3.8 REFRLIM α_θ=0.9, Dietrich2013 거짓 ray 교차) + [[swan-unstructured-time-step]].

## 8. Akrish 2020 — QC with shear currents

- **Akrish G, Smit P, Zijlema M, Reniers A (2020)**, "Modelling statistical wave interferences over shear currents", *Journal of Fluid Mechanics* **891**, A2. DOI: 10.1017/jfm.2020.143 ◇
- **내용**: Smit-Janssen(2013) QC 를 **mean/shear current 포함**으로 확장 (그들 Eq 2.19). swantech §2.7 의 current-포함 QC 근거.
- **본 위키**: [[swan-tech-ch2-7-qcm-theory]] (§2.7) + [[swan-quasi-coherent]].

## 9. 기타 핵심 reference (triad/wind)

| 메커니즘 | 원논문 | 본 위키 |
|---|---|---|
| DIA quadruplet | Hasselmann S et al. 1985, *JPO* 15, 1378-1391 | [[swan-tech-ch2-nonlinear-detailed]] §A.1 |
| LTA triad | Eldeberky 1996 PhD (TU Delft) | [[swan-tech-ch2-nonlinear-detailed]] §B.4 |
| SPB triad | Becq-Girard, Forget, Benoit 1999, *Coastal Eng* 37, 1-24 | §B.3 |
| DCTA triad | Booij, Holthuijsen, Bénit 2009 (ICCE) + Zijlema 2022 | §B.7 |
| QuadWave | Akrish, Rabaud, ... 2024 (Coastal Eng) | §B.6 |
| wind C_D | Zijlema, van Vledder, Holthuijsen 2012, *Coastal Eng* 65, 19-26 | [[swan-tech-ch2-sources-sinks]] |
| Stelling-Leendertse | Stelling, Leendertse 1992 (Estuarine/Coastal Modeling) | [[swan-tech-ch3-discretization]] |

## 10. 한계

- Full-text paywall — abstract/method 요약은 검색 스니펫·landing page·저자 사이트 기반 (정확 인용은 DOI 원문 필요).
- DOI ◇PII 표기(Holthuijsen2003·Booij-Holthuijsen1987·Battjes-Janssen1978·Zieger2015·Rogers2012·Akrish2020)는 PII/패턴 유도 — 인용 전 crossref 직접 확인 권장.
- §9 일부 원논문(Eldeberky 1996 PhD, ICCE proceedings)은 DOI 없음 (bibliographic only).

## 11. 연결

- [[swan-booij-1999-jgr-foundational]] — Booij-Ris-Holthuijsen 1999 JGR (SWAN foundational, 별도 상세)
- [[swan-documentation-stack]] — 4 SWAN PDF docs
- [[swan-recent-research-2024-2026]] — 최근 연구동향 (web-refs)
- [[swan-tech-ch2-7-qcm-theory]] / [[swan-tech-ch3-refraction-limiter]] / [[swan-xnl4-exact-quadruplet]] — 각 원논문 적용

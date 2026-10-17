---
title: "FUNWAVE-TVD 기초 논문 — 지배방정식·수치·GPU·쇄파·벤치마크 계보"
model: FUNWAVE
citation_status: verified
last_source_check: "2026-10-18 (recovery 대조 반영)"
verification_method: "2026-10-18 FUNWAVE recovery 대조 보고서 반영"
source: "서지(권·페이지·DOI)는 WebSearch landing-page 직접 확인(2026-06-15, ascelibrary/sciencedirect/scholar/JAMES) + FUNWAVE 공식 references(fengyanshi.github.io). 코드↔논문 대응은 source-analysis 노트 기준. 보관 3.0·2.1 PDF와 Intro-TN의 보고서 번호는 recovery 대조 보고서의 서지 구분을 반영."
note_date: 2026-06-15
source_scope: FUNWAVE-TVD
---

# FUNWAVE-TVD 기초 논문 계보

> FUNWAVE-TVD 지배방정식·수치기법·모듈의 이론 출처. 코드 구현은 [`../source-analysis/`](../source-analysis/), 공식 사이트·저장소는 [`funwave-official-resources.md`](funwave-official-resources.md).
> Celeris와 **같은 완전비선형 확장 Boussinesq 클래스** — 분산 계보 비교는 [`../../Celeris/web-refs/celeris-coulwave-theory.md`](../../Celeris/web-refs/celeris-coulwave-theory.md).

## 1. 지배방정식 — 완전비선형 확장 Boussinesq (verified)

- **Wei, G., Kirby, J.T., Grilli, S.T., Subramanya, R. (1995)** "A fully nonlinear Boussinesq model for surface waves. Part 1. Highly nonlinear unsteady waves." *J. Fluid Mech.* **294**:71-92. DOI: [10.1017/S0022112095002813](https://doi.org/10.1017/S0022112095002813). — FUNWAVE 지배방정식의 **원형**(Nwogu z_α reference velocity + 완전비선형). → [`../source-analysis/funwave-dispersion-solver.md`](../source-analysis/funwave-dispersion-solver.md).
- **Chen, Q. (2006)** "Fully nonlinear Boussinesq-type equations for waves and currents over porous beds." *J. Engineering Mechanics* **132**(2):220-230. DOI: [10.1061/(ASCE)0733-9399(2006)132:2(220)](https://doi.org/10.1061/(ASCE)0733-9399(2006)132:2(220)). — wave-current + 투수층(porous bed) 확장. FUNWAVE-TVD가 채택한 방정식 형(Shi 2012가 Chen 2006 form을 conservative form으로 재구성).

상류 계보(단층 확장 Boussinesq의 기원): Nwogu 1993(z_α) → [`../../Celeris/web-refs/celeris-coulwave-theory.md`](../../Celeris/web-refs/celeris-coulwave-theory.md) §1.2.

## 2. 수치기법 — TVD finite-volume + adaptive RK (verified)

- **Shi, F., Kirby, J.T., Harris, J.C., Geiman, J.D., Grilli, S.T. (2012)** "A high-order adaptive time-stepping TVD solver for Boussinesq modeling of breaking waves and coastal inundation." *Ocean Modelling* **43-44**:36-51. DOI: [10.1016/j.ocemod.2011.12.004](https://doi.org/10.1016/j.ocemod.2011.12.004). — **FUNWAVE-TVD의 핵심 방법 논문**: Chen 2006 방정식을 well-balanced conservative form으로 재정리 → 고차 Runge-Kutta adaptive time-stepping + **MUSCL-TVD + HLL Riemann** flux + 충격 포착 쇄파 + wetting-drying moving shoreline. → [`../source-analysis/funwave-flux-tvd.md`](../source-analysis/funwave-flux-tvd.md). [10-18 대조 정정]

현재 코드에서 충격 포착 전환의 조건은 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`이다. 이 조건은 `VISCOSITY_BREAKING`을 선택하지 않은 분기에 있다. 이 비는 유속 Froude 수가 아니다. 근거: `FUNWAVE-TVD/src/masks.F:177–188`, [theory-numerics §4 FT1-285](../../../_staging/recovery/compare/funwave-theory-numerics-vs-code.md#4-노트-대조와-수정안). [10-18 대조 정정]

## 3. 쇄파 — eddy viscosity (표준 인용)

- **Kennedy, A.B., Chen, Q., Kirby, J.T., Dalrymple, R.A. (2000)** "Boussinesq modeling of wave transformation, breaking, and runup. I: 1D." *J. Waterway, Port, Coastal, and Ocean Engineering* **126**(1):39-47. — eddy-viscosity 쇄파 모델(∂η/∂t 기준). FUNWAVE의 viscosity breaking 옵션 + Celeris `Pass_Breaking` 공유 계보. → [`../source-analysis/funwave-physics-sources.md`](../source-analysis/funwave-physics-sources.md). (Shi 2012의 shock-capturing 쇄파는 별도; FUNWAVE는 두 방식 모두 지원.)

## 4. GPU 가속 (verified)

- **Yuan, Y., Shi, F., Kirby, J.T., Yu, F. (2020)** "FUNWAVE-GPU: Multiple-GPU Acceleration of a Boussinesq-Type Wave Model." *J. Advances in Modeling Earth Systems (JAMES)*. DOI: [10.1029/2019MS001957](https://doi.org/10.1029/2019MS001957). — CUDA Fortran multi-GPU(4-7× single / >10× multi), 2011 Tohoku 검증. → [`../source-analysis/funwave-gpu-source.md`](../source-analysis/funwave-gpu-source.md)·[`funwave-build-and-blackwell-port.md`](../source-analysis/funwave-build-and-blackwell-port.md).

## 5. 문서·벤치마크 보고서 (Univ. of Delaware CACR)

- 보관 *FUNWAVE-TVD Fully Nonlinear Boussinesq Wave Model Documentation and User's Manual* 3.0 PDF 표지는 **CACR-11-03**과 **Release Dec 2016**을 함께 적는다. 출처: `funwave_tvd_3.0.pdf p.1`. 위키 발췌는 [funwave-tvd-manual.md](../manual-notes/funwave-tvd-manual.md)에 있다. [10-18 대조 정정]
- 2.1 표지는 **CACR-13-XX**다. 출처: `funwave_tvd_2.1_manual.pdf p.1`. [10-18 대조 정정]
- Intro-TN은 Shi 등 (2013) 매뉴얼을 **CACR-11-04**로 인용한다. 출처: `Intro-to-FUNWAVE-CHL-TN.pdf p.24`, [v21-manual §4 FV1-581](../../../_staging/recovery/compare/funwave-v21-manual-vs-code.md#4-노트-대조와-수정안). [10-18 대조 정정]
- **Tehranirad, B., Shi, F., Kirby, J.T., Harris, J.C., Grilli, S.T. (2011)** *Tsunami benchmark results for fully nonlinear Boussinesq wave model FUNWAVE-TVD, Version 1.0.* Report **CACR-11-02**, Univ. of Delaware. — NTHMP 쓰나미 벤치마크 검증.

## 6. 본 위키 cross-ref

- 코드: [`../source-analysis/funwave-source-map.md`](../source-analysis/funwave-source-map.md) (39 .F / 218 subroutine 전수조사)
- 공식 자료: [`funwave-official-resources.md`](funwave-official-resources.md)
- 같은 위상해상 Boussinesq 계열의 GPU 모델은 [Celeris](../../Celeris/)다. COULWAVE 모드는 완전비선형 Boussinesq 방정식 계열에 속한다. 근거: [celeris-coulwave-theory.md](../../Celeris/web-refs/celeris-coulwave-theory.md) §2. [10-18 전수 검증 정정]
- 정온도 정밀 티어: [`../../../concepts/waves/harbor-tranquility-kds64.md`](../../../concepts/waves/harbor-tranquility-kds64.md) §6

## 문서와 코드 차이 (10-18 대조)

문서 판: FUNWAVE-TVD 3.0 문서 "Release Dec 2016"(공개 저장소 PDF 마지막 변경 `fef45a7`, 2018-02-24), 2.1 매뉴얼 `b9c035d`(2016-11-03), Intro-TN 2015-07. 코드 판: 공개 저장소 `github.com/fengyanshi/FUNWAVE-TVD` HEAD `b4c322e`(2025-01-24), `FUNWAVE-TVD/src/main.F:47` `!    VERSION 3.0`.

근거 보고서는 [theory-numerics §4·5](../../../_staging/recovery/compare/funwave-theory-numerics-vs-code.md#4-노트-대조와-수정안)다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| theory-numerics:FT1-285 | 현재 노트 §4 FT1-285 | `05fdbedb:models/FUNWAVE/web-refs/funwave-foundational-papers.md:24`(반영 전 노트 줄) `Froude 임계 초과 시 NLSW 전환 쇄파` | `FUNWAVE-TVD/src/masks.F:177–188` `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`; `FUNWAVE-TVD/src/io.F:2689–2691,2713–2715`; `7b93138:src/masks.F:130–131` | B 문서 오기 | 현재 충격 포착 전환의 조건은 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`이다. 이 비를 유속 Froude 수로 적지 않는다. 이 조건은 VISCOSITY_BREAKING을 선택하지 않은 분기에 있다. FT1-013·125·267과 같은 판정이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] [10-18 표본 정정] |

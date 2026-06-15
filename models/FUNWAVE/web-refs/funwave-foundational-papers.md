---
title: "FUNWAVE-TVD 기초 논문 — 지배방정식·수치·GPU·쇄파·벤치마크 계보"
model: FUNWAVE
citation_status: verified
source: "서지(권·페이지·DOI)는 WebSearch landing-page 직접 확인(2026-06-15, ascelibrary/sciencedirect/scholar/JAMES) + FUNWAVE 공식 references(fengyanshi.github.io). 코드↔논문 대응은 source-analysis 노트 기준. 일부 보고서(CACR)는 번호까지 확인, 본문 미정독."
note_date: 2026-06-15
---

# FUNWAVE-TVD 기초 논문 계보

> FUNWAVE-TVD 지배방정식·수치기법·모듈의 이론 출처. 코드 구현은 [`../source-analysis/`](../source-analysis/), 공식 사이트·저장소는 [`funwave-official-resources.md`](funwave-official-resources.md).
> Celeris와 **같은 완전비선형 확장 Boussinesq 클래스** — 분산 계보 비교는 [`../../Celeris/web-refs/celeris-coulwave-theory.md`](../../Celeris/web-refs/celeris-coulwave-theory.md).

## 1. 지배방정식 — 완전비선형 확장 Boussinesq (verified)

- **Wei, G., Kirby, J.T., Grilli, S.T., Subramanya, R. (1995)** "A fully nonlinear Boussinesq model for surface waves. Part 1. Highly nonlinear unsteady waves." *J. Fluid Mech.* **294**:71-92. DOI: [10.1017/S0022112095002813](https://doi.org/10.1017/S0022112095002813). — FUNWAVE 지배방정식의 **원형**(Nwogu z_α reference velocity + 완전비선형). → [`../source-analysis/funwave-dispersion-solver.md`](../source-analysis/funwave-dispersion-solver.md).
- **Chen, Q. (2006)** "Fully nonlinear Boussinesq-type equations for waves and currents over porous beds." *J. Engineering Mechanics* **132**(2):220-230. DOI: [10.1061/(ASCE)0733-9399(2006)132:2(220)](https://doi.org/10.1061/(ASCE)0733-9399(2006)132:2(220)). — wave-current + 투수층(porous bed) 확장. FUNWAVE-TVD가 채택한 방정식 형(Shi 2012가 Chen 2006 form을 conservative form으로 재구성).

상류 계보(단층 확장 Boussinesq의 기원): Nwogu 1993(z_α) → [`../../Celeris/web-refs/celeris-coulwave-theory.md`](../../Celeris/web-refs/celeris-coulwave-theory.md) §1.2.

## 2. 수치기법 — TVD finite-volume + adaptive RK (verified)

- **Shi, F., Kirby, J.T., Harris, J.C., Geiman, J.D., Grilli, S.T. (2012)** "A high-order adaptive time-stepping TVD solver for Boussinesq modeling of breaking waves and coastal inundation." *Ocean Modelling* **43-44**:36-51. DOI: [10.1016/j.ocemod.2011.12.004](https://doi.org/10.1016/j.ocemod.2011.12.004). — **FUNWAVE-TVD의 핵심 방법 논문**: Chen 2006 방정식을 well-balanced conservative form으로 재정리 → 고차 Runge-Kutta adaptive time-stepping + **MUSCL-TVD + HLL Riemann** flux + Froude 임계 초과 시 NLSW 전환 쇄파 + wetting-drying moving shoreline. → [`../source-analysis/funwave-flux-tvd.md`](../source-analysis/funwave-flux-tvd.md).

## 3. 쇄파 — eddy viscosity (표준 인용)

- **Kennedy, A.B., Chen, Q., Kirby, J.T., Dalrymple, R.A. (2000)** "Boussinesq modeling of wave transformation, breaking, and runup. I: 1D." *J. Waterway, Port, Coastal, and Ocean Engineering* **126**(1):39-47. — eddy-viscosity 쇄파 모델(∂η/∂t 기준). FUNWAVE의 viscosity breaking 옵션 + Celeris `Pass_Breaking` 공유 계보. → [`../source-analysis/funwave-physics-sources.md`](../source-analysis/funwave-physics-sources.md). (Shi 2012의 shock-capturing 쇄파는 별도; FUNWAVE는 두 방식 모두 지원.)

## 4. GPU 가속 (verified)

- **Yuan, Y., Shi, F., Kirby, J.T., Yu, F. (2020)** "FUNWAVE-GPU: Multiple-GPU Acceleration of a Boussinesq-Type Wave Model." *J. Advances in Modeling Earth Systems (JAMES)*. DOI: [10.1029/2019MS001957](https://doi.org/10.1029/2019MS001957). — CUDA Fortran multi-GPU(4-7× single / >10× multi), 2011 Tohoku 검증. → [`../source-analysis/funwave-gpu-source.md`](../source-analysis/funwave-gpu-source.md)·[`funwave-build-and-blackwell-port.md`](../source-analysis/funwave-build-and-blackwell-port.md).

## 5. 문서·벤치마크 보고서 (Univ. of Delaware CACR)

- **Shi, F., Kirby, J.T., Tehranirad, B., Harris, J.C., Grilli, S.T.** *FUNWAVE-TVD Fully Nonlinear Boussinesq Wave Model Documentation and User's Manual* — Report **CACR-11-04**, Center for Applied Coastal Research, Univ. of Delaware. (위키 발췌: [`../manual-notes/funwave-tvd-manual.md`](../manual-notes/funwave-tvd-manual.md); 원본 `raw/manuals/funwave_tvd_3.0.md`.)
- **Tehranirad, B., Shi, F., Kirby, J.T., Harris, J.C., Grilli, S.T. (2011)** *Tsunami benchmark results for fully nonlinear Boussinesq wave model FUNWAVE-TVD, Version 1.0.* Report **CACR-11-02**, Univ. of Delaware. — NTHMP 쓰나미 벤치마크 검증.

## 6. 본 위키 cross-ref

- 코드: [`../source-analysis/funwave-source-map.md`](../source-analysis/funwave-source-map.md) (39 .F / 218 subroutine 전수조사)
- 공식 자료: [`funwave-official-resources.md`](funwave-official-resources.md)
- 같은 위상해상 Boussinesq class(실시간 GPU): [`../../Celeris/`](../../Celeris/) — Celeris COULWAVE 모드 = 동일 완전비선형 식 ([[../../Celeris/web-refs/celeris-coulwave-theory]] §2)
- 정온도 정밀 티어: [`../../../concepts/waves/harbor-tranquility-kds64.md`](../../../concepts/waves/harbor-tranquility-kds64.md) §6

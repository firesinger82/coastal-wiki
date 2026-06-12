---
title: "FUNWAVE 공식 자료·핵심 논문"
model: FUNWAVE
citation_status: verified
source: "GitHub repos + arxiv/journal landing-page (WebFetch/WebSearch 2026-06-12). DOI·권·페이지는 직접 확인분만 verified, 계보 논문 일부는 표준 인용(원문 확인 권장)."
note_date: 2026-06-12
---

# FUNWAVE 공식 자료·핵심 논문

## 1. 공식 사이트·저장소 (verified)

- **문서**: <http://fengyanshi.github.io/build/html/index.html> (FUNWAVE Documentation, USACE version)
- **GitHub (CPU/MPI)**: <https://github.com/fengyanshi/FUNWAVE-TVD> — Fortran ~69%, MATLAB·Python 보조, 7 releases, v3.6 (2021-06), beta
- **GitHub (multi-GPU)**: <https://github.com/dryuanye/FUNWAVE-GPU> — FUNWAVE-TVD v3.3의 CUDA Fortran 다중 GPU 이식

## 2. 핵심 논문

### 2.1 FUNWAVE-TVD (현행 버전) — ✅ verified (Ocean Modelling, search 확인)
- **Shi, F., Kirby, J.T., Harris, J.C., Geiman, J.D., Grilli, S.T. (2012)** "A high-order adaptive time-stepping TVD solver for Boussinesq modeling of breaking waves and coastal inundation." *Ocean Modelling* **43-44**:36-51. (doi:10.1016/j.ocemod.2011.12.004 — 원문 확인 권장)
  - TVD shock-capturing(쇄파=bore), hybrid finite-volume/finite-difference, 고차 adaptive Runge-Kutta time-stepping, MPI, Cartesian+spherical.

### 2.2 완전비선형 Boussinesq 계보 — ◇ 표준 인용 (DOI 확인 권장)
- **Wei, G., Kirby, J.T., Grilli, S.T., Subramanya, R. (1995)** "A fully nonlinear Boussinesq model for surface waves. Part 1. Highly nonlinear unsteady waves." *J. Fluid Mech.* **294**:71-92. (FUNWAVE 지배방정식 원형)
- **Chen, Q. (2006)** "Fully nonlinear Boussinesq-type equations for waves and currents over porous beds." *J. Engineering Mechanics* **132(2)**:220-230. (wave-current, porous bed)
- **Kirby, J.T. et al. (1998)** FUNWAVE 1.0 documentation — Univ. of Delaware Research Report CACR-98-06. (초판)

### 2.3 GPU 가속 — ✅ verified (JAMES, Wiley 확인)
- **Yuan, Y., Shi, F., Kirby, J.T., Yu, F. (2020)** "FUNWAVE-GPU: Multiple-GPU Acceleration of a Boussinesq-Type Wave Model." *Journal of Advances in Modeling Earth Systems (JAMES)*. **doi:10.1029/2019MS001957**.
  - CUDA Fortran + MPI(inter-GPU). on-chip shared memory로 고차 분산미분 global access 감소. batched tridiagonal solver 다중 GPU stream(20-30% 단축).
  - 성능: 36-core HPC 노드 대비 **single-GPU 4-7×, double-GPU >10×**.
  - 검증: 복잡 해안 wave runup 벤치마크 + **2011 Tohoku-oki tsunami** basin-scale.

## 3. 본 위키 cross-ref

- 정체·분류: [`../README.md`](../README.md) — 위상해상 Boussinesq(SWAN 위상평균과 대비)
- 동일 계열: [`../../XBeach/source-analysis/xbeach_nonh.md`](../../XBeach/source-analysis/xbeach_nonh.md) (XBeach-NH Boussinesq-type)

## 4. 미보강 (소스 확보 후)

- GitHub clone → `raw/source_code/` + source-analysis (Boussinesq 항·TVD flux·tridiagonal dispersion solver·sponge·wavemaker)
- 문서 발췌 → manual-notes (입력 input.txt·wavemaker·breaking parameters)

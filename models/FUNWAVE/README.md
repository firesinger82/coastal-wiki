# models/FUNWAVE

> **Canonical source**: 이 디렉토리(`models/FUNWAVE/`)가 FUNWAVE 모델의 구현·메커닉에 대한 진실의 원천. `concepts/waves/06-model-application.md` 등은 여기로의 링크만 가짐.
>
> ⚠️ **현재 상태(2026-06-12 신설)**: source-analysis·manual-notes 미작성 — **본 위키에 소스/메뉴얼 미확보**. README 정체카드 + web-refs(공식 GitHub·논문)는 verified(공개 출처 인용), 내부 알고리즘 file:line 분석은 소스 확보 후.

## 정체 카드

- **이름**: **FUNWAVE-TVD** (Fully Nonlinear Boussinesq Wave Model with Total Variation Diminishing scheme)
- **저자/관리주체**: **Fengyan Shi · James T. Kirby** (University of Delaware, Center for Applied Coastal Research) + Stephan Grilli (URI) 외. (계보: Wei·Kirby 1995 → Kirby et al. FUNWAVE 1.0 1998 → Shi et al. 2012 TVD)
- **라이선스**: open-source (학술; 저장소 LICENSE 확인 권장)
- **공식 문서**: [fengyanshi.github.io/build/html](http://fengyanshi.github.io/build/html/index.html) (USACE version)
- **GitHub**: [fengyanshi/FUNWAVE-TVD](https://github.com/fengyanshi/FUNWAVE-TVD) (Fortran ~69%, MPI; v3.6 2021-06)
- **GPU 버전**: [dryuanye/FUNWAVE-GPU](https://github.com/dryuanye/FUNWAVE-GPU) — FUNWAVE-TVD v3.3의 **multi-GPU(CUDA Fortran + MPI)** 이식 (Yuan et al. 2020 JAMES)
- **소스 위치 (본 위키)**: ❌ 미확보 (`raw/source_code/` 없음 — 향후 GitHub clone 필요)
- **사용 도메인**: 위상해상(phase-resolving) **nearshore Boussinesq** — 쇄파·연안침수(runup)·wave-induced current·harbor·**tsunami**(2011 Tohoku 등)
- **격자**: structured, **Cartesian + spherical** 좌표
- **수치 기법**: 완전비선형 Boussinesq + **TVD shock-capturing**(쇄파를 bore로 처리, hybrid FV/FD), 고차 adaptive time-stepping(Runge-Kutta), MPI 병렬

## 모델 분류 — 위상해상 Boussinesq

SWAN(위상평균 spectral, [`models/SWAN/`](../SWAN/))과 **다른 class**: FUNWAVE는 **개별 파의 위상을 해상**하는 Boussinesq 모델. [`models/XBeach/`](../XBeach/)의 **non-hydrostatic 모드**([[xbeach_nonh]])와 같은 계열(depth-integrated Boussinesq-type). 분산성(dispersion)을 고차 항으로 확보해 SWE보다 깊은 물까지 적용.

## 핵심 논문 (web-refs 상세)

- **FUNWAVE-TVD**: Shi, Kirby, Harris, Geiman, Grilli (2012) *Ocean Modelling* 43-44:36-51 — TVD solver for Boussinesq breaking/inundation
- **완전비선형 Boussinesq 계보**: Wei, Kirby, Grilli, Subramanya (1995) *J. Fluid Mech.* 294:71-92 / Chen (2006) *J. Eng. Mech.* 132(2):220-230 (porous bed, currents)
- **GPU**: Yuan, Shi, Kirby, Yu (2020) *JAMES* doi:10.1029/2019MS001957 — multi-GPU 4-7×(1GPU)·>10×(2GPU) vs 36-core, shared memory 고차 분산미분 + batched tridiagonal solver

→ 상세: [`web-refs/funwave-official-resources.md`](web-refs/funwave-official-resources.md)

## 하위 디렉토리 현황

| 경로 | 상태 | 비고 |
|---|---|---|
| `source-analysis/` | ❌ 미작성 | 소스 미확보 — GitHub clone 후 작성 |
| `manual-notes/` | ❌ 미작성 | fengyanshi.github.io 문서 발췌 후보 |
| `web-refs/` | ✅ 1 verified | funwave-official-resources (GitHub·docs·논문) |

## 본 위키에서의 핵심 활용

- [`concepts/waves/`](../../concepts/waves/) — 위상해상 Boussinesq(SWAN 위상평균과 대비)
- [`models/XBeach/source-analysis/xbeach_nonh.md`](../XBeach/source-analysis/xbeach_nonh.md) — 동일 Boussinesq-type 계열(비교)
- tsunami·runup — 천수 SWE([`models/ADCIRC/`](../ADCIRC/)) 대비 분산성 보존

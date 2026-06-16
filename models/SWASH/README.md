# models/SWASH

> **Canonical source**: 이 디렉토리(`models/SWASH/`)가 SWASH 모델의 구현·메커닉에 대한 진실의 원천. `concepts/swash-zone/04-code-and-tools.md`·`concepts/waves/` 등은 여기로의 링크만 가짐.
>
> ✅ **현재 상태(2026-06-15 신설)**: SWASH 공식 GitLab(gitlab.tudelft.nl/citg/wavemodels/swash) clone(`raw/source_code/swash/`, v12.01, 152 Fortran) + **source-analysis 1 + web-refs 1**(file:line / DOI 인용 verified). 위상해상 비정수압 모델군(FUNWAVE·Celeris) 합류.

## 정체 카드

- **이름**: **SWASH** (Simulating WAves till SHore) — `Swash.ftn90` main program 주석
- **정의**: **non-hydrostatic free-surface wave-flow 모델** — 파·조석·부력·바람 구동 비정상 회전류 + transport. 심해→해빈/항만 파 변형, rapidly varied flow, 밀도류(하구·호소). (repo README introduction)
- **저자/관리주체**: **Marcel Zijlema** 외 SWASH team — **TU Delft**, Faculty of Civil Engineering and Geosciences, **Environmental Fluid Mechanics Section** (`Swash.ftn90`). v1.00 2009-12.
- **라이선스**: **GPL v3** (`raw/source_code/swash/LICENSE`)
- **버전**: **12.01** (repo README badge)
- **공식 사이트**: [swash.sourceforge.io](https://swash.sourceforge.io)
- **GitLab**: [gitlab.tudelft.nl/citg/wavemodels/swash](https://gitlab.tudelft.nl/citg/wavemodels/swash)
- **docs**: [delftwaves.github.io/swash-docs](https://delftwaves.github.io/swash-docs/) · **docker**: delftwaves/swash
- **canonical 논문**: **Zijlema, Stelling, Smit (2011)** *Coastal Engineering* 58(10):992-1012, **doi:10.1016/j.coastaleng.2011.05.015** (repo README DOI badge)
- **소스 위치 (본 위키)**: ✅ `raw/source_code/swash/` (gitignore 로컬, GitLab clone — `src/` 152 Fortran)
- **사용 도메인**: 위상해상 **비정수압 천수**(non-hydrostatic shallow water) — 연안 파 변형·surf zone·**처오름(swash)**·항만 정온·밀도류. SWAN(위상평균)이 못하는 개별 파·shoreline 운동 해상.
- **격자**: structured(curvilinear) + **unstructured**(SWAN grid 공유, `SwanReadADCGrid` = ADCIRC fort.14 reader). multi-layer(z) 또는 depth-averaged.
- **수치 기법**: 비정수압 압력 보정(pressure Poisson) + 천수방정식 finite-difference/volume. **explicit/implicit × depth/layer-averaged** 4×조합 solver. 시초 알고리즘 = **Stelling & Zijlema 2003**(non-hydrostatic free-surface FD).

## 모델 분류 — 위상해상 비정수압 (SWAN 계열 인프라)

- [`models/FUNWAVE/`](../FUNWAVE/)·[`models/Celeris/`](../Celeris/)(Boussinesq) 와 **같은 위상해상 class** 이나, SWASH 차별점 = **비정수압(non-hydrostatic) 다층 천수** 접근(Boussinesq 의 고차 분산항 대신 연직 층분할 + 비정수압 압력으로 분산 표현). 층 수 ↑ 시 깊은 물 분산 정확.
- **SWAN(위상평균)과 같은 TU Delft 그룹** — OCP(Ocean Pack) 인프라·MPI(`SWINITMPI`)·unstructured grid topology(`SwanGrid*`) 공유. SWAN(광역 spectral) → SWASH(항내·swash 위상해상) nesting 자연.
- [`concepts/swash-zone/04-code-and-tools.md §3`](../../concepts/swash-zone/04-code-and-tools.md) 에서 신설 후보로 식별 → 본 디렉토리로 충족.

## 핵심 논문 (web-refs 상세)

- **SWASH 원논문**: Zijlema, M., Stelling, G., Smit, P. (2011) "SWASH: An operational public domain code for simulating wave fields and rapidly varied flows in coastal waters" *Coastal Engineering* **58**(10):992-1012, doi:10.1016/j.coastaleng.2011.05.015
- **수치 시초**: Stelling, G., Zijlema, M. (2003) "An accurate and efficient finite-difference algorithm for non-hydrostatic free-surface flow with application to wave propagation" *Int. J. Numer. Methods Fluids* **43**:1-23
- **쇄파**: Smit, P., Zijlema, M., Stelling, G. (2013) "Depth-induced wave breaking in a non-hydrostatic, near-shore wave model" *Coastal Engineering* **76**:1-16

→ 상세: [`web-refs/swash-official-resources.md`](web-refs/swash-official-resources.md)

## 하위 디렉토리 현황

| 경로 | 상태 | 비고 |
|---|---|---|
| `source-analysis/` | ✅ 1 verified | [swash-architecture-source-map](source-analysis/swash-architecture-source-map.md) — 명명규칙·compute dispatch·SWAN 인프라 공유 |
| `manual-notes/` | (미생성) | swashuse/swashtech/swashimp 매뉴얼 — swash.sourceforge.io online_doc |
| `web-refs/` | ✅ 1 verified | [swash-official-resources](web-refs/swash-official-resources.md) |
| `raw/source_code/swash/` | ✅ clone (gitignore) | v12.01, src 152 Fortran |

## 다음 후보

- source-analysis 심화: `SwashImpDep2DHflow`(비정수압 압력 Poisson solver) line-by-line · `SwashSolvers`(matrix-vector) · `SwashBCtransferfnc`(경계조건/조파)
- manual-notes: swash.sourceforge.io online_doc (User/Tech/Impl) TOC
- 빌드 검증(gfortran/MPI) — FUNWAVE 선례
- concepts/swash-zone/04 §3 cross-link 갱신(미수록→수록)

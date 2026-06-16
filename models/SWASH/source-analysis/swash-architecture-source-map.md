---
title: "SWASH 소스 아키텍처 맵 — main·compute dispatch·flow solver 명명규칙·SWAN 인프라 공유"
model: SWASH
component: src (top-level)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). Swash.ftn90(main 71줄)·SwashComputFlow.ftn90(compute dispatch) call 라인 + 각 flow solver Purpose 주석 verbatim 인용. flow solver 152 Fortran 중 명명규칙 해독은 SwashExp/ImpDep/Lay*.ftn90 Purpose 주석 직접 인용. SWAN 인프라 공유는 src/ 파일명(SwanGrid*·ocp*·swanparll) 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - models/SWASH/README.md
  - models/SWASH/web-refs/swash-official-resources.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
---

# SWASH 소스 아키텍처 맵

> SWASH v12.01 `src/`(152 Fortran)의 골격. main → compute dispatch → flow solver 계층 + SWAN 공유 인프라. 경로: `raw/source_code/swash/src/`.

## 1. main program (`Swash.ftn90`, 71줄)

```
program Swash
  call SWINITMPI        ! MPI 초기화 (SWAN ocean pack 공유)
  call SwashMain        ! SWASH run 본체
  call SWEXITMPI        ! MPI 종료
end program
```

- 자칭: "SWASH (Simulating WAves till SHore); a **non-hydrostatic wave-flow model**" / Purpose: "Program for simulation of wave motion and shallow water flow in coastal waters".
- 저자 v1.00 **Marcel Zijlema, 2009-12** (TU Delft Environmental Fluid Mechanics).
- `SwashMain` → 초기화(`SwashInit` 1728줄)·입력(`SwashReadInput` 2902줄)·시간루프(`SwashComputFlow`)·출력(`SwashQuanOutp`).

## 2. compute dispatch (`SwashComputFlow.ftn90`)

시간스텝마다 **격자차원 × 연직표현 × 시간적분 × 변형** 조합으로 flow solver 호출. 명명규칙 `Swash{Exp|Imp}{Dep|Lay}[P|M]{1DH|2DH|U}flow`:

| 토큰 | 의미 |
|---|---|
| **Exp / Imp** | explicit / **implicit** 시간적분 (비정수압 압력) |
| **Dep / Lay** | **depth-averaged**(1층) / **layer-averaged**(다층 z) |
| **P** | 비정수압 압력 **subgrid 접근**(`SwashImpLayP*` "solved with a subgrid approach") |
| **M** | 운동량보존(momentum-conservative) 변형 (`SwashImpDepM`·`SwashImpLayM`) |
| **1DH / 2DH / U** | 1D-수평 / 2D-수평 / U(연직 단면) |

호출 예 (`SwashComputFlow.ftn90`):

| 라인 | solver | 조건 |
|---|---|---|
| `:86` | `SwashExpDep1DHflow` | 1DH explicit depth-avg |
| `:94` / `:96` | `SwashImpDep1DHflow` / `...M1DHflow` | 1DH implicit (M=운동량) |
| `:111` / `:113` | `SwashExpLay1DHflow` / `...P1DHflow` | 1DH explicit 다층 (P=압력 subgrid) |
| `:146` | `SwashExpDep2DHflow` | 2DH explicit depth-avg |
| `:154` / `:156` | `SwashImpDep2DHflow` / `...M2DHflow` | 2DH implicit |
| `:171-184` | `SwashExp/ImpLay[P]2DHflow` | 2DH 다층 |

각 solver Purpose 주석(verbatim): "Performs the time integration for the **non-hydrostatic, depth-averaged/layer-averaged 2D shallow water equations**" (`SwashExpDep2DHflow`/`SwashExpLay2DHflow`). `SwashImpLayP2DHflow` = "...layer-averaged 2D SWE solved with a **subgrid approach**".

→ Boussinesq(FUNWAVE) 가 고차 분산항으로 분산을 표현하는 데 비해, SWASH 는 **연직 층분할 + 비정수압 압력**(Poisson)으로 분산 표현. 층 수 ↑ → 깊은 물 분산 정확.

## 3. 최대 소스 (flow solver 계열, src 크기순)

| 파일 | 줄 | 역할 |
|---|---|---|
| `SwashExpLayP2DHflow.ftn90` | 9383 | 2DH explicit 다층+압력 |
| `SwashExpLay2DHflow.ftn90` | 7746 | 2DH explicit 다층 |
| `SwashImpLayP2DHflow.ftn90` | 7539 | 2DH implicit 다층+압력(subgrid) |
| `SwashImpLay2DHflow.ftn90` | 7003 | 2DH implicit 다층 |
| `SwashSolvers.ftn90` | 5705 | **선형 solver**(matrix-vector, 압력 Poisson) |
| `SwashCheckPrep.ftn90` | 6006 | 입력 검증·전처리 |
| `SwashBCtransferfnc.ftn90` | 4709 | **경계조건/조파**(boundary transfer) |
| `SwashReadInput.ftn90` | 2902 | 명령 입력 파서 |

## 4. SWAN 인프라 공유 (같은 TU Delft 그룹)

src/ 에 SWAN 파일이 그대로 존재 — SWASH 가 SWAN OCP(Ocean Pack) 재사용:

- `SwanGrid*.ftn90` (SwanGridTopology·GridCell·GridVert·Griddata·Gridobjects) — **unstructured grid topology**
- `SwanReadADCGrid.ftn90` — **ADCIRC fort.14 reader** (SWAN 과 동일, [[../../SWAN/source-analysis/swan-grid-readers]])
- `ocpcre.ftn`·`ocpmix.ftn` — Ocean Pack I/O
- `swanparll.ftn`·`swanser.ftn`·`SWINITMPI` — MPI 병렬

→ SWAN(위상평균) ↔ SWASH(위상해상) 같은 코드베이스 계보. [`web-refs §3`](../web-refs/swash-official-resources.md).

## 5. 미보강 (verified 확장 TODO)

- `SwashImpDep2DHflow`/`SwashImpLayP2DHflow` 비정수압 압력 Poisson 이산화·Keller-box 연직 line-by-line.
- `SwashSolvers` 선형 solver(CG/BiCGSTAB?) 알고리즘.
- `SwashBCtransferfnc` 조파경계(weakly reflective·Riemann) 종류.
- `SwashComputTrans`/`SwashAntiCreep` transport·anti-creep(Z-layer) 식.
- manual-notes: swash.sourceforge.io online_doc(User/Tech/Impl) TOC.

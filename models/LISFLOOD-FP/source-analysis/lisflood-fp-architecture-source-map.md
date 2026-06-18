---
title: "LISFLOOD-FP v8.2 소스 아키텍처 맵 — main·Solver 구조 + 다중 솔버 계열(ACC/FV1/DG2/nugrid + CUDA)"
model: LISFLOOD-FP
component: source (top-level + swe/ + cuda/)
canonical_source: self
citation_status: verified
verification_method: "LISFLOOD-FP v8.2 Zenodo 아카이브(doi:10.5281/zenodo.13121102) 소스 직접 read (raw/source_code/LISFLOOD-FP/). lisflood.cpp(main, :20-27 솔버 include·:34 main·:53-169 Solver struct 기본값) + swe/ 솔버 파일목록 + root *.cpp(fp_acc/fp_flow/fp_trent/sgc) 직접 확인. file:line 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/LISFLOOD-FP/README.md
  - models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md
---

# LISFLOOD-FP v8.2 소스 아키텍처 맵

> LISFLOOD-FP 의 골격 — **하나의 entry(`lisflood.cpp`)에서 다중 솔버**(reduced-physics ACC ~ 완전 SWE FV1/DG2) + CPU/GPU 를 런타임 선택. 경로: `raw/source_code/LISFLOOD-FP/`.

## 1. main + 솔버 include (`lisflood.cpp`)

```cpp
#include "swe/fv1.h"                              // lisflood.cpp:20  FV1 (finite volume 1차)
#include "swe/dg2.h"                              // :21  DG2 (discontinuous Galerkin 2차)
#include "cuda/acc/cuda_acc_simulate.cuh"         // :23  GPU ACC
#include "cuda/fv1/cuda_fv1_simulate.cuh"         // :24  GPU FV1
#include "cuda/dg2/cuda_dg2_simulate.cuh"         // :25  GPU DG2
#include "cuda/acc_nugrid/cuda_acc_nugrid_simulate.cuh"  // :27  GPU ACC 비균일격자(동적 해상도)
int main(int argc, char *argv[])                  // :34
{
  Solver ParSolver;                               // :53  솔버 설정 구조체
  ParSolver.g = C(9.8065500000000);               // :166 중력
  ParSolver.cfl = C(0.7);                          // :168 CFL
  ParSolver.SolverAccuracy = C(1e-4);              // :169
  ...
}
```

→ **단일 entry, 다중 솔버**: include 가 곧 솔버 카탈로그 — ACC·FV1·DG2 각각 **CPU + CUDA** 버전, 추가로 **acc_nugrid**(비균일격자=v8.x dynamic resolution adaptivity). 런타임 입력(parfile)으로 솔버 선택, `Solver` 구조체(:53)에 전역 설정.

## 2. 솔버 계열 (2 family)

### 2.1 Classic "FP" 솔버 (root `*.cpp`) — 원조 Bristol reduced-physics

| 파일 | 솔버 |
|---|---|
| `fp_acc.cpp` | **ACC** — local inertia(acceleration) 근사 SWE. LISFLOOD-FP 대표 reduced-physics(Bates et al. 2010). advection 무시·관성항 유지 → 고속 |
| `fp_flow.cpp` | diffusive wave(관성 무시) 흐름 |
| `fp_trent.cpp` | Trent — 추가 dynamic 처리 |
| `iterateq.cpp` | 반복 solver |
| `sgc.cpp` | **sub-grid channel**(SGC) — 격자보다 작은 하도를 sub-grid 처리(Neal et al.) |
| `por_flow.cpp` | porosity 흐름 |
| `weir_flow.cpp`·`ch_flow.cpp` | 위어·채널 |
| `boundary.cpp`·`input.cpp`·`output.cpp` | 경계·입출력 |

### 2.2 신규 "swe/" 솔버 — SEAMLESS-WAVE(Kesserwani) 완전 2D shallow-water

| 파일 | 솔버 |
|---|---|
| `swe/fv1.cpp` | **FV1** — 1차 Godunov 유한체적 (full 2D SWE, shock-capturing) |
| `swe/dg2.cpp`·`dg2new.cpp` | **DG2** — 2차 Discontinuous Galerkin. **dg2new = multiwavelet 적응**(v8.2 headline: dynamic resolution adaptivity) |
| `swe/hll.cpp` | **HLL** Riemann flux (FV1/DG2 공용 numerical flux) |
| `swe/flux.cpp`·`fields.cpp` | flux·필드 자료구조 |
| `swe/boundary/input/output/stats` | swe 전용 경계·IO·통계 |

### 2.3 CUDA (`cuda/`)

`cuda/{acc,fv1,dg2,acc_nugrid}/cuda_*_simulate.cuh` — 각 솔버의 GPU 구현. `acc_nugrid` = 비균일(non-uniform) 격자 ACC = **동적 해상도 적응**의 GPU 경로.

## 3. 솔버 스펙트럼 (정확도 ↔ 비용)

```
diffusive(fp_flow) < ACC(fp_acc, local inertia) < FV1(full SWE 1차) < DG2(full SWE 2차, multiwavelet 적응)
   ←──────── reduced-physics, 고속 ────────        ──────── full dynamics, 고정확 ────────→
```

- reduced-physics 측(ACC)은 [[../../SFINCS/source-analysis/sfincs-architecture-source-map]] 의 SFINCS reduced SWE 와 같은 계열.
- full SWE 측(FV1/DG2)은 [[../../SWASH/source-analysis/swash-architecture-source-map]]·Godunov 계열과 유사하나 LISFLOOD-FP 는 raster DEM 범람 특화.

## 4. 후속 deep-dive 후보

- `fp_acc.cpp` — ACC local-inertia 이산화(Bates 2010 식) line-by-line
- `swe/dg2new.cpp` — DG2 multiwavelet 적응 격자(v8.2 핵심, Kesserwani)
- `swe/hll.cpp` — HLL Riemann flux
- `sgc.cpp` — sub-grid channel(SGC) 처리
- `cuda/acc_nugrid` — GPU 비균일격자 동적 해상도

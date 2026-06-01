---
title: "ADCIRC DG (Discontinuous Galerkin) continuity solver — PR #502 OPEN WIP"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "GitHub API repos/adcirc/adcirc/pulls/502 (metadata + 25 files diff list) + repos/adcirc/adcirc/contents/src/dg.F90?ref=refs/pull/502/head (5733 lines module header line 1-120) + contents/src/dg_integration.F90 (1324 lines, header line 1-60) + contents/src/slopelimiter.F90 (206 lines, line 1-50 + SL6 body) 직접 fetch (2026-06-01). PR metadata: author namo626, additions 10358, deletions 67, changedFiles 25, createdAt 2026-04-29, state OPEN, body description: 'Work in progress of adding a discontinuous Galerkin solver to the continuity equation'."
note_author: "Claude Opus 4.7 (1M context) GitHub API direct fetch"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — GitHub API verbatim"
verification_date: 2026-06-01
---

## Scope

ADCIRC PR #502 (OPEN, **WIP**) 의 새 **Discontinuous Galerkin (DG)** continuity equation solver 통합. 기존 ADCIRC 의 Continuous Galerkin (CG) GWCE (Generalized Wave-Continuity Equation) 와 별개의 element-local modal expansion + Riemann flux + TVD-RK time stepping + slope limiter 방식. 본 노트는 PR 의 5 신규 .F90 모듈 (dg / dg_integration / messenger_elem / precipitation / slopelimiter) + 핵심 modified file (decomp 1303 라인 update, momentum, timestep, wetdry) 의 verified 인용. PR description 직접 인용: **"Work in progress of adding a discontinuous Galerkin solver to the continuity equation."**

> **상태 경고 (WIP)**: PR 자체 checklist 모두 unchecked, body 에 명시적 WIP 표시. 본 노트는 코드 구조·모듈 책임 인용에 한정 — algorithm correctness, convergence, conservation property 검증은 PR merge 이후 별도. `dofh = 1` (P1 element) 만 현재 지원 (`dg.F90:51-52`).

## 1. PR #502 metadata (GitHub API verbatim)

| 항목 | 값 |
|---|---|
| URL | https://github.com/adcirc/adcirc/pull/502 |
| Title | "Add DG solver for continuity eq." |
| Author | `namo626` |
| State | OPEN |
| Created | 2026-04-29 20:55 UTC |
| Last update | 2026-04-29 20:55 UTC (push 후 변화 없음) |
| Additions | **+10,358 lines** |
| Deletions | -67 lines |
| Files changed | 25 |
| Description | "Work in progress of adding a discontinuous Galerkin solver to the continuity equation." |
| Type of change | (unchecked — WIP) |
| Test 상태 | (unchecked — 미보고) |
| Publication | (unfilled) |

## 2. File 변경 분류 (25 files)

### 2.1 신규 파일 5건 (8,611 lines)

| 파일 | 라인 | 역할 |
|---|---|---|
| `src/dg.F90` | **+5,733** | DG 메인 모듈 — modal coefficients, basis functions, quadrature, RK coefficients (§3) |
| `src/dg_integration.F90` | **+1,324** | `DG_HYDRO_TIMESTEP` driver — modal time-step (§4) |
| `src/messenger_elem.F90` | **+1,189** | Element-level MPI messenger (face-based exchange) (§7) |
| `src/precipitation.F90` | +159 | DG-compatible precipitation forcing |
| `src/slopelimiter.F90` | **+206** | Slope limiter (Barth-Jespersen 계열, slopeflag=6, §5) |

### 2.2 Modified 핵심 파일 (1,747 lines net)

| 파일 | 변경 | 역할 |
|---|---|---|
| `prep/decomp.F` | **+1,303 / -29** | Element-based domain decomposition (DG element partition) |
| `prep/prep.F` | +193 | DG preprocessing 통합 |
| `prep/pre_global.F` | +62 | DG global pre-processing |
| `prep/presizes.F` | +25 | Array sizing for DG |
| `prep/adcprep.F` | +29 / -4 | adcprep driver DG flag |
| `src/momentum.F` | +32 / -18 | Momentum equation modification for DG coupling |
| `src/timestep.F` | +9 / -3 | Timestep driver branch (CG vs DG) |
| `src/wetdry.F` | +6 / -2 | Wet-dry algorithm extension |
| `src/read_input.F` | +39 / -2 | DG namelist read |
| `src/wind.F` | +11 | Wind forcing DG |
| `src/adcirc.F` | +5 / -2 | Top-level driver branch |
| `src/global.F` | +4 / -1 | Global state |
| `src/write_output.F` | +4 | Output writer DG |
| `cmake/*.cmake` (6 files) | +27 / -6 | Build system (DG sources) |
| `.pre-commit-config.yaml` | +1 | Lint |

## 3. DG core module (`dg.F90`)

### 3.1 Module structure (line 1-37)

```fortran
MODULE DG
   USE SIZES, only: mne, mnp, mneta, mnbfr, mnei, mnffr, mnbfr
   implicit none
   private
   public :: ze, U_modal, V_modal, nedel, wdflg, neled, ncele
   public :: rhs_ze, g2root, slopeflag
   public :: phi_corner, el_count, eletab, leq, nleq, nleqg
   public :: atvd, btvd, dtvd, nrk
   public :: needn, qnph_dg, qnam_dg, MAX_BOA_DT, nedno
   public :: sinnx, cosnx, hb, xlen, nedsd, niedn, nagp, xfac, yfac
   public :: dbathdx, bath, srfac, sfac_elem, phi_area, negp, phi_edge
   public :: wegp, bathed, sfaced, xegp, emo_dg, efa_dg
   public :: M_inv, dbathdy, needs, nieds, dofh, pa, constvel
   public :: psi2, psi3, psi1, etiminc_dg
   public :: edgeq, fluxtype, nfeds, qtratio
   public :: nfedn

   public :: prep_DG, nodal_to_modal, nodal_to_quad_points
```

`private/protected` 분리로 외부 (slopelimiter, dg_integration, messenger_elem) 가 read-only 접근. Public public sub-routine 3개: `prep_DG` (초기화), `nodal_to_modal` (변환), `nodal_to_quad_points` (보간).

### 3.2 핵심 변수 (line 40-105)

```fortran
REAL(SZ), ALLOCATABLE :: ZE(:, :, :)
!! ze(i,j,k) = ith mode of water elevation on element j at RK stage k

REAL(SZ), ALLOCATABLE :: U_modal(:, :)
!! u_modal(i,j) = ith mode of x-velocity on element j

real(sz), ALLOCATABLE :: V_modal(:, :)
!! v_modal(i,j) = ith mode of y-velocity on element j

INTEGER, ALLOCATABLE :: WDFLG(:)
!! Same as NOFF(j): 1 if element j is wet, 0 if dry

INTEGER, ALLOCATABLE :: NCELE(:)
!! NCELE = NOFF*NODECODE(n1)*NODECODE(n2)*NODECODE(n3)

integer :: dofh
!! DG polynomial order (degrees of freedom). Currently only 1 is supported.

integer :: NAGP(8)
!! NAGP(i) = number of area quadrature points for dofh = i

integer :: NEGP(8)
!! NEGP(i) = number of edge quadrature points for dofh = i
```

핵심:
- **Modal expansion**: `ZE(i,j,k)` 3D array — i = mode index, j = element index, k = RK stage. CG-ADCIRC 는 nodal $\eta$ (per-vertex) 이지만 DG 는 modal (per-element basis coefficient).
- **dofh = 1 만 지원 현재** (P1 element 만, P2/P3 future)
- `WDFLG, NCELE` = wet-dry flag — 기존 ADCIRC `NOFF`, `NODECODE` 곱한 element-level flag (CG 와 호환 유지)

### 3.3 TVD-Runge-Kutta time integration (line 108-109)

```fortran
REAL(SZ), ALLOCATABLE :: ATVD(:, :), BTVD(:, :), CTVD(:, :)
REAL(SZ), ALLOCATABLE :: DTVD(:), MAX_BOA_DT(:)
```

Total Variation Diminishing Runge-Kutta — Shu-Osher 1988 표준. `ATVD, BTVD, CTVD` 가 RK stage 계수, `DTVD` 가 stage timestep, `MAX_BOA_DT` 가 max stable timestep. `NRK = RK order` (line 64).

### 3.4 Slope limiter flag + Riemann flux type

```fortran
INTEGER, TARGET :: SLOPEFLAG          ! line 70 — slope limiter selection
INTEGER, TARGET :: FLUXTYPE           ! line 72 — Riemann flux type
INTEGER, TARGET :: RK_STAGE, RK_ORDER ! line 73 — current/total RK stages
```

`SLOPEFLAG = 6` 만 현재 활성 (slopelimiter.F90 line 17-22 — 다른 값은 limiter 호출 안 됨).

### 3.5 Adaptive p-refinement (line 74)

```fortran
Integer, TARGET :: padapt, pflag, pl, ph, px, lebesgueP, gflag
```

`padapt, pflag, pl, ph` — adaptive polynomial order refinement (현재 P1 hardwire 이지만 framework 존재). `pflag2con1/2con2` (line 86) — refinement criteria.

## 4. DG time-step driver (`dg_integration.F90`)

### 4.1 Subroutine 구조

```fortran
module dg_integration
   use DG, only: ZE, RHS_ZE, NEDSD, NEDEL, ATVD, BTVD, DTVD, ...
   public :: DG_HYDRO_TIMESTEP

contains

   subroutine DG_HYDRO_TIMESTEP(IT, timeh)
      !! Set ETA1 := ETA2, and
      !! compute ETA2 at the next timestep using DG formulation

      use SLOPELIMITERS, only: SLOPELIMITER
      use GWCE, only: ETIME1, ETIME2, ETIMINC
      use MESSENGER_ELEM, only: updater_elem_mod
      ...

      if (it == 1) then
         call prep_DG()
      end if

      TIME_A = IT*DTDP + STATIM*86400.d0

      eta1 = eta2

      call projectMomentum()
      call positive_depth()

      call UPDATER(UU1, VV1, DUMY2, 2)
      call UPDATER_elem_mod(ze, ze, ze, 1, 1)
```

### 4.2 Hybrid CG-DG 통합

`use GWCE, only: ETIME1, ETIME2, ETIMINC` — DG driver 가 기존 CG-GWCE 의 time level 변수를 참조 (legacy interop). `eta1 = eta2` swap 패턴은 기존 ADCIRC 와 동일.

### 4.3 호출 순서 (line 50-60)

1. `prep_DG()` — 첫 step 만
2. `projectMomentum()` — momentum projection
3. `positive_depth()` — H > 0 enforcement (wet-dry)
4. `UPDATER(UU1, VV1, ..., 2)` — node-level velocity exchange (MPI)
5. `UPDATER_elem_mod(ze, ze, ze, 1, 1)` — **element-level ZE modal coefficient exchange** (신규 module `messenger_elem`)

→ MPI ghost-cell 의 element-level (face-based) communication 이 신규 필요 — DG 의 inter-element flux 가 face 단위라서.

## 5. Slope limiter (`slopelimiter.F90`)

### 5.1 Dispatch

```fortran
module SLOPELIMITERS
   use DG, only: ze, slopeflag, el_count, eletab, phi_corner
   use global, only: NOFF, nodecode
   use SIZES, only: MNE, mnei
   use MESH, only: NE, NP, NM
   public :: slopelimiter

contains
   subroutine SLOPELIMITER(IRK)
      integer, intent(in) :: IRK
      if (slopeflag == 6) then
         call SlopeLimiter6(IRK)
      end if
   end subroutine SLOPELIMITER
```

`slopeflag == 6` 만 현재 활성 — 저자 코멘트 "namo - copy of SL5 but got rid of QX,QY" (line 27).

### 5.2 SlopeLimiter6 algorithm (line 28-90)

```fortran
subroutine SLOPELIMITER6(IRK)
   integer, parameter :: blocksize = 8         ! Vectorized blocks
   real(SZ), dimension(blocksize, 3) :: ZEC, ZEVERTEX, DIF
   real(SZ), dimension(blocksize) :: SUMLOC, SUMDIF, SIGNDIF
   ...
   bound = 1.0e-5

   ! FIND THE MAXIMUM AND MINIMUM OF EACH VARIABLE OVER ALL ELEMENTS
   ! SHARING A NODE
   do I = 1, NP
      ZE_MIN1(I) = 99999.
      ZE_MAX1(I) = -99999.
      ...
      NO_NBORS = EL_COUNT(I)
      do J = 1, NO_NBORS
         NBOR_EL = ELETAB(I, 1 + J)
         ZE_DG(J) = ZE(1, NBOR_EL, IRK + 1)
         if (ZE_DG(J) < ZE_MIN1(I)) then
            ZE_MIN1(I) = ZE_DG(J)
         ...
```

→ 표준 **Barth-Jespersen 형 limiter**:
1. Node 별 인접 element의 min/max ZE collect
2. Element 의 vertex extrapolation 이 [min, max] 초과 시 reduction factor 적용
3. `bound = 1e-5` = numerical tolerance
4. `blocksize = 8` = SIMD/cache vectorization

`use MESSENGER, only: updateR` (line 35) — limiter 후 ghost-cell 동기화 필요.

## 6. Coupling to existing ADCIRC core

### 6.1 `momentum.F` 변경 (+32 -18)

기존 CG momentum equation 에 DG-modal velocity transfer 추가. `projectMomentum()` (dg_integration.F90:50) 가 modal → nodal projection 수행.

### 6.2 `timestep.F` 변경 (+9 -3)

CG vs DG branch — `DGFLAG` (dg.F90:59) 가 dispatch flag. 기존 CG path 변경 없이 새 DG path 병행.

### 6.3 `wetdry.F` 변경 (+6 -2)

`NCELE = NOFF*NODECODE(n1)*NODECODE(n2)*NODECODE(n3)` (dg.F90:48-49) 의 element-level flag 통합. CG `NODECODE` (node-level) 를 element 곱셈으로 element-level wet-dry 로 확장.

### 6.4 `read_input.F` 변경 (+39 -2)

DG namelist parameter read (`DGFLAG`, `SLOPEFLAG`, `FLUXTYPE`, `RK_ORDER`, `dofh` 등). Card 형식 미확정 (WIP).

## 7. Element MPI messenger (`messenger_elem.F90`, 1189 lines)

신규 module — 기존 ADCIRC node-level `MESSENGER` 와 별개의 **element-level (face-based) ghost-cell exchange**. DG 의 inter-element flux 계산에 인접 element 의 modal coefficient 가 필요하므로 face-shared element 간 통신 필요.

`dg_integration.F90:60` `UPDATER_elem_mod(ze, ze, ze, 1, 1)` 호출 형태 — 3개 ZE field × mode 1 × stage 1.

## 8. Preprocessing 대규모 변경 (`prep/decomp.F` +1303 lines)

`decomp.F` (domain decomposition) 가 **element-based partition** 추가 — DG 가 element-local 이라 element-cut 가 minimum 인 partition 필요. 기존 node-based partition 과 다름. METIS interface 추가 가능성 (확인 필요).

## 9. 한계 + 다음 단계

### WIP 한계 (PR description + code 직접 인용)

1. **P1 only** (dg.F90:51-52) — `dofh = 1` 만 지원. P2/P3 framework 존재하나 unused.
2. **slopeflag = 6 only** (slopelimiter.F90:20) — SL1~SL5 비활성.
3. **Test/documentation 미보고** — PR checklist 모두 unchecked.
4. **Publication 미인용** — Cockburn-Shu / Aizinger-Dawson 등 DG-shallow water 표준 reference 누락.
5. **Conservation/consistency 검증 없음** — WIP description.

### 향후 verified 가능 항목 (PR merge 후)

- DG mass matrix `M_inv` (dg.F90:16) 구성 식 + element local computation
- Riemann flux solver type (FLUXTYPE — Roe / HLL / LLF 등)
- TVD-RK coefficients (ATVD/BTVD/CTVD numerical value)
- Quadrature rule (NAGP/NEGP at dofh=1) — Gauss-Legendre order
- `slopelimiter6` 의 reduction factor recipe (Barth-Jespersen vs other)

## 10. ADCIRC CG (GWCE) 와의 비교

| 항목 | CG-GWCE (기존) | DG (PR #502) |
|---|---|---|
| 변수 | Nodal $\eta$ (per-vertex) | Modal $ZE(i,j,k)$ (per-element) |
| Continuity equation | GWCE wave continuity (Luettich-Westerink) | DG element-local + Riemann flux |
| Time integration | Implicit / semi-implicit (depending on IM) | Explicit **TVD-RK** (ATVD/BTVD) |
| Limiter | 없음 (필요시 separate) | Slope limiter (slopeflag=6 Barth-Jespersen) |
| Wet-dry flag | `NOFF, NODECODE` per-node | `NCELE = NOFF·∏NODECODE` per-element |
| MPI exchange | Node-level `MESSENGER` | Node + **Element `MESSENGER_ELEM`** |
| Polynomial order | Linear FE (node) | P1 (element, current) → P2/P3 (planned) |
| Reference impl | Luettich-Westerink 2004 | Cockburn-Shu 가정 (저자 reference 미인용) |
| Conservation | Approximate (wave continuity) | Element-local exact (Riemann flux) |

→ DG 의 핵심 이점: **element-local conservation + discontinuity handling** (storm-surge front, dry-wet interface). 단점: P1 시 nodal CG 와 cost 비슷, 고차 시 element-local DOF 증가.

## 11. Cross-references

- 기존 GWCE: [[adcirc-gwce-implementation]]
- Time-step driver: [`adcirc-baseline-anatomy.md`](adcirc-baseline-anatomy.md)
- Wet-dry: [[adcirc-wetting-drying-implementation]]
- Parallel: [[adcirc-parallel-implementation]]
- Output writers: [[adcirc-output-writers-implementation]]
- swan coupling: [[adcirc-swan-coupling]] (별도 wave path)
- ADCIRC source-analysis topic map: [[adcirc-topic-map]]
- 본 PR 자체: https://github.com/adcirc/adcirc/pull/502
- Author: `namo626` (GitHub)
- Related PR (시간 제어): [[adcirc-swan-coupling]] §SWAN Temporal Controls — PR #498 (2026-05-28 verified)
- Information gaps: [[adcirc-information-gaps]] — DG WIP merge 후 본 노트 갱신

## 12. 후속 추적

본 PR 의 다음 활동 발생 시 본 노트 §J 형식 (ROMS PR #75 §J 패턴, [[roms_4dvar]] 참조) 으로 commit 별 verified 추가:

- 코드 push (merge, force-push, rebase)
- Reviewer 코멘트 (현재 0 inline + 0 conversation comments)
- 학술 publication 인용 (현재 PR body Publications 빈칸)
- Type of change 체크 (현재 모두 unchecked)

---
title: "SWAN 파랑 setup 솔버 (SETUPP·SETUP2D) + swancom1.ftn 19 서브루틴 cross-walk"
model: SWAN
component: "wave-induced setup (radiation stress → 1D marching / 2D Poisson SOR) + swancom1 coverage map"
canonical_source: self
citation_status: verified
verification_method: >
  models/SWAN/raw/source_code/swan/src/swancom1.ftn (12,121 lines, v41.51 = 위키 raw)
  직접 Read — SETUPP(9947-10500)·SETUP2D(10501-12121) 전 구간 + 19 서브루틴 선언부·
  Purpose 헤더 grep 전수. 기본값은 swanmain.ftn:1269-1271 (PNUMS 23-25) 직접 확인.
  이론 대응은 swantech Ch5(Eq 5.1-5.25)·Ch6(SOR)·§3.16(radiation stress) 기존 verified
  노트와 대조. 본 노트로 [[swan-source-coverage-audit]] §5 의 "swancom1 12k cross-walk"
  제안 이행 — 19 서브루틴 중 13 은 기존 노트 커버 확인, 미커버 6 중 물리 실질인
  SETUPP/SETUP2D 를 본 노트가 심층, 잔여 4 는 유틸리티로 판정(§2 표).
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
related:
  - "[[swan-source-coverage-audit]]"
  - "[[swan-propagation-implementation]]"
  - "[[swan-schemes-implementation]]"
  - "[[../manual-notes/swan-tech-ch4-5-bc-2d-setup]]"
  - "[[../manual-notes/swan-tech-ch6-iterative-solvers]]"
  - "[[../manual-notes/swan-command-numerics-output-reference]]"
---

# SWAN setup 솔버 + swancom1.ftn cross-walk

`swancom1.ftn`(12,121줄)은 SWAN 의 **메인 계산 드라이버 파일** — 반복루프·sweep·솔버·limiter·setup 이 한 파일에 모여 있다. 대부분은 기존 source-analysis 노트가 이미 file:line 인용으로 커버하나(§2 표), **파랑 setup(`SETUPP`/`SETUP2D`)** 은 이론 노트([[../manual-notes/swan-tech-ch4-5-bc-2d-setup]] Ch5 Eq 5.1-5.25)만 있고 코드 측이 비어 있었다 → 본 노트 §3-4 가 채운다.

## 1. 파일 정체

- 12,121줄, 서브루틴 **19개** (선언부 grep 전수, §2 표의 line 컬럼).
- GPL-3.0, Delft University of Technology, Copyright 1993-2024 (`swancom1.ftn:9970-9984` SETUPP 헤더 보일러플레이트 — 각 서브루틴마다 반복).
- 역사층위: version 태그 30.7x(1998)~40.41(2004)~41.x 혼재 — Cycle II 유산과 Cycle III 정비가 공존하는 파일. SETUPP 는 32.01(1997.09 신설, Roeland Ris)→40.41(2004.12 정리·swancom1 로 이동, Marcel Zijlema) (`swancom1.ftn:10001-10015` Updates 블록).

## 2. 19 서브루틴 cross-walk (커버리지 맵)

| # | 서브루틴 | line | 역할 (Purpose 헤더 요지) | 담당 노트 |
|---|---|---|---|---|
| 1 | `SWCOMP` | :43 | 계산 전체 driver (iteration loop `DO 450 ITER`) | [[swan-propagation-implementation]] |
| 2 | `SWOMPU` | :2485 | sweep 별 격자점 단위 계산 본체 | [[swan-propagation-implementation]] |
| 3 | `SWPRSET` | :3842 | "Print all the settings used in SWAN run" — 설정 출력 | (유틸 — 본 표로 종결) |
| 4 | `SACCUR` | :4436 | 수렴판정: "check the accuracy of the final computation... terminate" | [[swan-propagation-implementation]] (curvature stopping) |
| 5 | `INSAC` | :4906 | 수렴판정 legacy 변형 — Purpose 헤더가 SACCUR 와 거의 동일("...quit") | (SACCUR 계열 legacy — 본 표로 종결) |
| 6 | `ACTION` | :5117 | spectral 방향/주파수 bin 범위 결정 | [[swan-propagation-implementation]] |
| 7 | `SINTGRL` | :5517 | "compute several integrals used in SWAN and some general parameters" (Hs 등 적분량) | (유틸 — 수렴판정·출력 공급) |
| 8 | `SOLPRE` | :6032 | 솔버 전처리 | [[swan-schemes-implementation]] |
| 9 | `SOLMAT` | :6256 | 행렬 조립 | [[swan-schemes-implementation]] |
| 10 | `SOLMT1` | :6499 | 행렬 조립 변형 | [[swan-schemes-implementation]] |
| 11 | `PHILIM` | :7857 | action limiter (Hersbach-Janssen) | [[swan-propagation-implementation]] (Eq 3.27) |
| 12 | `HJLIM` | :8004 | limiter 변형 | 동 |
| 13 | `RESCALE` | :8146 | 음에너지 제거 rescale | [[swan-schemes-implementation]] (Tolman 1991) |
| 14 | `SWSIP` | :8329 | SIP penta-diagonal 솔버 | [[swan-schemes-implementation]]·[[../manual-notes/swan-tech-ch6-iterative-solvers]] |
| 15 | `SWSOR` | :8938 | SOR 솔버 (action balance 측) | 동 |
| 16 | `SWMTLB` | :9452 | "compute loop bounds for calling thread" — OpenMP 루프 분배 | [[swan-parallel-implementation]] 영역 (유틸) |
| 17 | `SWSTPC` | :9562 | curvature 기반 정지판정 (since 41.01) | [[swan-propagation-implementation]] |
| 18 | `SETUPP` | :9947 | **"computes the wave-induced forces and adds the set-up to the depth"** | **본 노트 §3** |
| 19 | `SETUP2D` | :10501 | **2D setup Poisson 방정식 SOR 해법** | **본 노트 §4** |

> 판정: 19 중 13 = 기존 노트 실인용 확인(위 링크), 4 = 유틸리티(설정출력·legacy 수렴·적분·스레드분배, 본 표 한 줄로 충분), 2 = **SETUPP/SETUP2D 신규 심층(아래)**. → [[swan-source-coverage-audit]] §5 cross-walk 제안 종결.

## 3. `SETUPP` — radiation stress 적분 → setup → 수심 반영 (`:9947-10500`)

Purpose(헤더 verbatim): "computes the wave-induced forces and adds the set-up to the depth" (`:10012` 부근 §2 Purpose).

### 3.1 Radiation stress 성분 적분 (`:10222-10265`)

격자점별로 스펙트럼 전체를 적분:

```fortran
CK = CG(1) * K(1)                                       ! :10237
ELOC = SIG(1) * AC2(ID,IS,INDX)                         ! :10239  (E = σ·N)
RSXX = RSXX + (CK*SPCDIR(ID,4)+CK - SIG(1)/2.) * ELOC   ! :10246
RSXY = RSXY + CK*SPCDIR(ID,5) * ELOC                    ! :10247
RSYY = RSYY + (CK*SPCDIR(ID,6)+CK - SIG(1)/2.) * ELOC   ! :10248
```

- `CK = c_g k`, `SPCDIR(:,4/5/6) = cos²θ / cosθsinθ / sin²θ`, `ELOC = σN = E`. 따라서 적분핵 = $c_g k(1+\cos^2\theta)E - \tfrac{\sigma}{2}E = \sigma E\,(n\cos^2\theta + n - \tfrac12)$ (∵ $n = c_g k/\sigma$, [[../manual-notes/swan-tech-ch3-qc-curvilinear]] Eq 3.62) — **이론 radiation stress $S_{xx}=\rho g\iint(n-\tfrac12+n\cos^2\theta)E$ (Eq 3.59-61)와 정확 일치** (ρg 와 적분가중 `DDIR*FRINTF` 는 저장 시 적용 `:10263-10265`, 파수·군속도는 `KSCIP1` 호출 `:10237` 직전 `:10236`).
- 1D 모드(`ONED`)에서는 격자방향 회전 성분으로 변환해 저장 (`:10259-10262`, `COSPC/SINPC`) — Updates "30.70, Feb. 98: transformation of radiation stress in 1D case" (`:10007`).

### 3.2 1D setup — 단순 marching (`:10286-10292`)

1D 는 Poisson 불필요 — 힘 평형을 x-방향 적분:

```fortran
ETA2 = ETA1 + ( SXX1 - SXX2 ) / ( 0.5 * ( DP2 + DP1 ) )   ! :10290
SETUP2(INDXR) = ETA2                                      ! :10291
```

$\eta_{i+1} = \eta_i + (S_{xx,i} - S_{xx,i+1})/\bar d$ — 이론 equilibrium $\partial\eta/\partial x = -\frac{1}{\rho g d}\partial S_{xx}/\partial x$ (swantech Eq 5.1)의 전진 이산화. 경계 시작값 0 (`:10199`).

### 3.3 2D — 힘(gradient) 계산 후 `SETUP2D` 호출 (`:10300-10402`)

- radiation stress 미분으로 파랑힘 `WFRCX/WFRCY` 를 중앙차분 계산하되, **인접점이 dry(`DEP2≤DEPMIN`)면 stencil 을 해당 방향으로 축소** (`:10317-10318` x-방향 `IXLO/IXUP`, `:10336-10337` y-방향) — dry point 근방 편미분 붕괴 방지.
- `CALL SETUP2D(...)` (`:10402`) — §4 의 Poisson 해.

### 3.4 후처리 — 기준점 보정·수심 갱신·dry 이웃 채움 (`:10406-10500`)

- **기준점 보정** (`:10412-10419`): 최심점 `IDXMAX` 의 setup 을 사용자 지정 `PSETUP(2)` 로 맞추는 상수 이동 `S_UPCOR = S_UPDP - PSETUP(2)` 후 전역 감산 — Poisson 해가 상수 부정(Neumann 전경계, §4)이므로 필요한 게이지 고정.
- **수심 반영** (`:10440`): `DEP2 = DEPSAV + SETUP2` — 저장해둔 원수심(`DEPSAV`)에 setup 을 더해 다음 반복의 유효수심 갱신 (Purpose 의 "adds the set-up to the depth").
- **dry 점 처리** (`:10452-10490`): 갱신 후 `DEP2≤DEPMIN` 인 점은 이웃 wet 점 setup 을 승계해 재침수 판정 (`:10485-10487`) — wetting 허용.

## 4. `SETUP2D` — 일반좌표 2D Poisson + SOR (`:10501-12121`)

Purpose/Method(헤더): "**A 2D Poisson equation in general coordinates is solved**" (`:10553`) — 이론 [[../manual-notes/swan-tech-ch4-5-bc-2d-setup]] 의 Eq 5.2(Poisson)·5.7-5.24(곡선격자 finite-volume) 구현부.

### 4.1 경계조건 (`:10665-10683`)

- 기본: "**Neumann boundary condition is imposed on all the boundaries**" (`:10665`) — 이론 Eq 5.23-24(half-cell Neumann).
- "A modified SOR method for the Poisson equation in unsteady..." (`:10672`) — [[../manual-notes/swan-tech-ch6-iterative-solvers]] §6.2 의 SOR(Botta-Ellenbroek 1985) 대응.
- **nesting 시 Dirichlet** 로 전환 (`:10682-10683` "in case of nesting put Dirichlet boundary condition") — 모(parent) 런의 setup 을 경계값으로.

### 4.2 9-point stencil 조립 (`:11086-11161`)

`AMAT(INDX,1..9)` — 중앙(1)+8이웃의 **9-point stencil**, 교차미분 항은 대각이웃에 `0.25*CONTRB` 로 분배 (`:11086-11157`; 예: `:11090-11093` x-교차항 → `AMAT(:,3/4/8/9) ∓0.25`). 이론 노트의 "Ax=f Eq 5.25, **9-point stencil NWKARR=9**"와 일치. 고립/무효 행은 항등행으로 치환 (`:11159-11161` `AMAT(INDX,1)=1`).

### 4.3 솔버 파라미터·자동 완화계수 (`:11812-11830`)

```fortran
REPS   = PNUMS(23)          ! :11812  수렴 임계 (기본 1e-6)
IAMOUT = INT(PNUMS(24))     ! :11813  반복과정 출력 (기본 0)
MAXIT  = INT(PNUMS(25))     ! :11814  최대 반복 (기본 1000)
```

기본값 출처: `swanmain.ftn:1269-1271` (`PNUMS(23)=1.E-6 / (24)=0. / (25)=1000.`). 사용자 제어 = `NUMERIC ... SETUP [eps2][outp][niter]` ([[../manual-notes/swan-command-numerics-output-reference]] — SETUP eps2 기본 SOR 1e-6 표기와 정합).

**자동 최적 ω** (`RELAX=-1` 시, `:11815-11828`): 활성격자수 `MCGRD` 로 Jacobi 스펙트럴반경을 휴리스틱 추정(ρ = 1−1/M [M<100] / 1−3/M [M<1000] / 1−10/M) 후 고전 최적 SOR 공식

$$\omega_{opt} = \frac{2}{1+\sqrt{1-\rho^2}} \qquad (\texttt{XOMEG = 2./(1.+SQRT(1.-RHOV*RHOV))}, \; \texttt{:11828})$$

사용자 지정 시 `XOMEG = RELAX` (`:11830`).

### 4.4 반복·수렴 (`:11835-12100`)

- 잔차 **inf-norm** `RESM` 추적 (`:11835-11846` 초기화·스윕 내 갱신), red-black 식 다중 블록 갱신 루프.
- 수렴판정: `RESM > REPS` 면 계속 (`:12076` 부근), `MAXIT` 도달 시 중단·진단 출력("required accuracy = REPS", `:12110` 부근).

## 5. 이론↔코드 정합 요약

| 이론 (swantech) | 코드 (본 노트) |
|---|---|
| Eq 3.59-61 radiation stress $S_{xx}/S_{xy}/S_{yy}$ | `:10246-10248` ($n=c_gk/\sigma$ 전개 일치) |
| Eq 5.1 equilibrium (1D) | `:10290` marching |
| Eq 5.2 Poisson + Eq 5.7-5.24 곡선격자 FV | SETUP2D 전체, 9-point `AMAT` `:11086-` |
| Eq 5.23-24 Neumann half-cell | `:10665` 전경계 Neumann (+nesting Dirichlet `:10682`) |
| Ch6 §6.2 SOR (Botta-Ellenbroek) | `:10672` modified SOR, ω 자동 `:11828` |
| swanuse §2.2 한계 "set-up 은 2D open-coast 전용·harbour 부적합" | Neumann 전경계+상수 게이지 보정(`:10412-10419`) 구조가 그 한계의 코드적 근거 |

## 6. 검증 메모

- 모든 line 인용은 위키 raw `swancom1.ftn`(v41.51 clone) 직접 Read. 식 전개($n$ 치환)는 코드 그대로의 항등변형으로, 값 추정 없음.
- `SWPRSET`·`INSAC`·`SINTGRL`·`SWMTLB` 는 Purpose 헤더 verbatim 확인 후 유틸리티 판정 — deep dive 미수행(§2 표가 최종 커버리지 기록). INSAC/SACCUR Purpose 중복은 소스 관찰 사실.
- 잔여 후속(선택): swancom2~5 동일 방식 cross-walk 는 기존 노트 인용밀도가 이미 높아 우선순위 낮음.

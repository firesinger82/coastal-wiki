---
title: "SWAN 파랑 setup 솔버 (SETUPP·SETUP2D) + swancom1.ftn 20 서브루틴 cross-walk" # [10-13 전수 검증 정정]
model: SWAN
component: "wave-induced setup (radiation stress → 1D marching / 2D Poisson SOR) + swancom1 coverage map"
canonical_source: self
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: >
  models/SWAN/raw/source_code/swan/src/swancom1.ftn (12,121 lines, v41.51 = 위키 raw)
  직접 Read — SETUPP(9947-10500)·SETUP2D(10501-12121) 전 구간 + 20 서브루틴 선언부· [10-13 전수 검증 정정]
  Purpose 헤더 grep 전수. 기본값은 src/swanmain.ftn:1269-1271 (PNUMS 23-25) 직접 확인.
  이론 대응은 swantech Ch5(Eq 5.1-5.25)·Ch6(SOR)·§3.16(radiation stress) 기존 verified
  노트와 대조. 본 노트로 [swan-source-coverage-audit](swan-source-coverage-audit.md) §5 의 "swancom1 12k cross-walk"
  제안 이행 — 20 서브루틴 중 14는 기존 노트로 연결한다. 나머지 6개 중 [10-13 전수 검증 정정]
  SETUPP/SETUP2D 를 본 노트가 심층, 잔여 4 는 유틸리티로 판정(§2 표).
  2026-10-13 recovery 대조 보고서 R1–R8 반영
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
related:
  - "[swan-source-coverage-audit](swan-source-coverage-audit.md)"
  - "[swan-propagation-implementation](swan-propagation-implementation.md)"
  - "[swan-schemes-implementation](swan-schemes-implementation.md)"
  - "[swan-tech-ch4-5-bc-2d-setup](../manual-notes/swan-tech-ch4-5-bc-2d-setup.md)"
  - "[swan-tech-ch6-iterative-solvers](../manual-notes/swan-tech-ch6-iterative-solvers.md)"
  - "[swan-command-numerics-output-reference](../manual-notes/swan-command-numerics-output-reference.md)"
---

# SWAN setup 솔버 + swancom1.ftn cross-walk

`swancom1.ftn`(12,121줄)은 SWAN 의 **메인 계산 드라이버 파일** — 반복루프·sweep·솔버·limiter·setup 이 한 파일에 모여 있다. 대부분은 기존 source-analysis 노트가 이미 file:line 인용으로 커버하나(§2 표), **파랑 setup(`SETUPP`/`SETUP2D`)** 은 이론 노트([swan-tech-ch4-5-bc-2d-setup](../manual-notes/swan-tech-ch4-5-bc-2d-setup.md) Ch5 Eq 5.1-5.25)만 있고 코드 측이 비어 있었다 → 본 노트 §3-4 가 채운다.

## 1. 파일 정체

- `src/swancom1.ftn`은 12,121줄이다. `^\s+SUBROUTINE`과 일치하는 선언은 20개이다. SOURCE의 선언은 6823행에 있다. [10-13 전수 검증 정정]
- GPL-3.0-or-later이다. 저작권자는 Delft University of Technology이다. 저작권 연도는 1993–2024이다. (`src/swancom1.ftn:9970–9975`.) [10-13 전수 검증 정정]
- SETUPP의 Updates는 32.01의 신설 시점을 1997년 9월로 적는다. 40.41의 정리 및 SWANCOM1 이동 시점은 2004년 12월이다. Authors는 두 판의 담당자를 각각 Roeland Ris와 Marcel Zijlema로 적는다. (`src/swancom1.ftn:9994–10011`.) [10-13 전수 검증 정정]

## 2. 20 서브루틴 cross-walk (커버리지 맵) [10-13 전수 검증 정정]

| # | 서브루틴 | line | 역할 (Purpose 헤더 요지) | 담당 노트 |
|---|---|---|---|---|
| 1 | `SWCOMP` | :43 | 계산 전체 driver (iteration loop `DO 450 ITER`) | [swan-propagation-implementation](swan-propagation-implementation.md) |
| 2 | `SWOMPU` | :2485 | sweep 별 격자점 단위 계산 본체 | [swan-propagation-implementation](swan-propagation-implementation.md) |
| 3 | `SWPRSET` | :3842 | "Print all the settings used in SWAN run" — 설정 출력 | (유틸 — 본 표로 종결) |
| 4 | `SACCUR` | :4436 | 연속 두 반복의 파고·평균주기 변화에 따른 수렴 판정이다. (`src/swancom1.ftn:4513–4534`.) | [swan-propagation-implementation](swan-propagation-implementation.md)의 SACCUR 절. [10-13 전수 검증 정정] |
| 5 | `INSAC` | :4906 | 수렴판정 legacy 변형 — Purpose 헤더가 SACCUR 와 거의 동일("...quit") | (SACCUR 계열 legacy — 본 표로 종결) |
| 6 | `ACTION` | :5117 | 작용량 수지의 수송·굴절 항을 조립한다. (`src/swancom1.ftn:5212–5213,5381–5495`.) | [swan-propagation-implementation](swan-propagation-implementation.md). [10-13 전수 검증 정정] |
| 7 | `SINTGRL` | :5517 | "compute several integrals used in SWAN and some general parameters" (Hs 등 적분량) | (유틸 — 수렴판정·출력 공급) |
| 8 | `SOLPRE` | :6032 | 솔버 전처리 | [swan-propagation-implementation](swan-propagation-implementation.md)의 SOLPRE 호출 인용. [10-13 전수 검증 정정] |
| 9 | `SOLMAT` | :6256 | 방향 공간의 삼중대각 선형계를 Thomas 알고리즘으로 푼다. (`src/swancom1.ftn:6312–6330`.) | [swan-propagation-implementation](swan-propagation-implementation.md)의 SOLMAT 호출 인용. [10-13 전수 검증 정정] |
| 10 | `SOLMT1` | :6499 | 방향 공간의 주기 경계 결합을 허용하는 삼중대각 선형계를 푼다. 주파수 전파항은 명시적으로 처리한다. (`src/swancom1.ftn:6555–6567`.) | [swan-propagation-implementation](swan-propagation-implementation.md)의 SOLMT1 호출 인용. [10-13 전수 검증 정정] |
| 11 | `PHILIM` | :7857 | Phillips 평형 수준을 기준으로 반복 간 작용량 변화를 제한한다. (`src/swancom1.ftn:7910–7929`.) | [swan-propagation-implementation](swan-propagation-implementation.md)의 PHILIM 절. [10-13 전수 검증 정정] |
| 12 | `HJLIM` | :8004 | limiter 변형 | 동 |
| 13 | `RESCALE` | :8146 | 음의 작용밀도를 같은 주파수의 다른 방향 성분에서 차감하여 0으로 만든다. (`src/swancom1.ftn:8201–8206`.) | [swan-propagation-implementation](swan-propagation-implementation.md)의 RESCALE 호출 인용. [10-13 전수 검증 정정] |
| 14 | `SWSIP` | :8329 | SIP penta-diagonal 솔버 | [swan-propagation-implementation](swan-propagation-implementation.md)의 SWSIP 호출 인용. 이론은 [swan-tech-ch6-iterative-solvers](../manual-notes/swan-tech-ch6-iterative-solvers.md)를 참조한다. [10-13 전수 검증 정정] |
| 15 | `SWSOR` | :8938 | SOR 솔버 (action balance 측) | 동 |
| 16 | `SWMTLB` | :9452 | "compute loop bounds for calling thread" — OpenMP 루프 분배 | [swan-parallel-implementation](swan-parallel-implementation.md) 영역 (유틸) |
| 17 | `SWSTPC` | :9562 | 파고·주기의 상대 변화, 절대 변화와 곡률에 따른 수렴 판정이다. 신설 판은 40.41이다. (`src/swancom1.ftn:9613–9621`.) | [swan-propagation-implementation](swan-propagation-implementation.md). [10-13 전수 검증 정정] |
| 18 | `SETUPP` | :9947 | **"computes the wave-induced forces and adds the set-up to the depth"** | **본 노트 §3** |
| 19 | `SETUP2D` | :10501 | **2D setup Poisson 방정식 SOR 해법** | **본 노트 §4** |
| 20 | `SOURCE` | :6823 | 원천항의 행렬 대각과 우변 기여를 조립한다. (`src/swancom1.ftn:7291–7294,7454–7458`.) | [swan-source-terms-implementation](wave/swan-source-terms-implementation.md). [10-13 전수 검증 보완] |

> 코드의 `^\s+SUBROUTINE` 선언은 20개이다. 위 표에서 기존 노트로 연결한 항목은 14개이다. 유틸리티로 분류한 항목은 4개이다. SETUPP와 SETUP2D는 본 노트의 §3–4에서 다룬다. 기존 표가 빠뜨린 SOURCE의 선언은 `src/swancom1.ftn:6823`에 있다. [swan-source-coverage-audit](swan-source-coverage-audit.md)의 이전 cross-walk 기록과 구분한다. [10-13 전수 검증 정정]

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

코드 저장량을 $R_{ij}=S_{ij}/(\rho g)$로 정의한다. 1D 갱신은 $\eta_{i+1}=\eta_i+(R_{xx,i}-R_{xx,i+1})/\bar d$다. 대응 물리식은 (2.143)이다. 근거: `src/swancom1.ftn:10290` `ETA2 = ETA1 + ( SXX1 - SXX2 ) / ( 0.5 * ( DP2 + DP1 ) )`. 1D 저장은 `src/swancom1.ftn:10259` `SETPDA(INDX,3) = DDIR * FRINTF *`에서 계산 방향으로 투영한 값이다. `src/swancom1.ftn:10263` `SETPDA(INDX,3) = RSXX * DDIR * FRINTF`는 2D 분기(ELSE)의 저장이다. [10-13 표본 정정]

해석: $n=c_g/c$를 쓰면 $CK=\sigma n$이다. $ELOC=\sigma N=E$다. 남은 $\sigma$는 로그 격자 적분의 가중이다. 코드가 저장하는 복사응력은 $R_{ij}=S_{ij}/(\rho g)$이므로 $S_{xx}$ 식과 같다. 기존 보고서가 PDF (2.144)의 인용에 보탠 $S_{xy}$·$S_{yy}$ 식은 이 쪽 원문에 없으므로 제거한다. 근거: `src/swancom1.ftn:10237` `CK = CG(1) * K(1)`; `src/swancom1.ftn:10239` `ELOC = SIG(1) * AC2(ID,IS,INDX)`; `src/swancom1.ftn:10246` `RSXX = RSXX + (CK*SPCDIR(ID,4)+CK - SIG(1)/2.) * ELOC`; `src/swancom1.ftn:10247` `RSXY = RSXY + CK*SPCDIR(ID,5) * ELOC`; `src/swancom1.ftn:10248` `RSYY = RSYY + (CK*SPCDIR(ID,6)+CK - SIG(1)/2.) * ELOC`; `src/swancom1.ftn:10263` `SETPDA(INDX,3) = RSXX * DDIR * FRINTF`.
- 1D 모드(`ONED`)에서는 격자방향 회전 성분으로 변환해 저장 (`:10259-10262`, `COSPC/SINPC`) — Updates "30.70, Feb. 98: transformation of radiation stress in 1D case" (`:10007`).

### 3.2 1D setup — 단순 marching (`:10286-10292`)

1D 는 Poisson 불필요 — 힘 평형을 x-방향 적분:

```fortran
ETA2 = ETA1 + ( SXX1 - SXX2 ) / ( 0.5 * ( DP2 + DP1 ) )   ! :10290
SETUP2(INDXR) = ETA2                                      ! :10291
```

$\eta_{i+1}=\eta_i+(R_{xx,i}-R_{xx,i+1})/\bar d$다. 대응 물리식은 (2.143)이다. 근거: swantech PDF 65쪽 / 인쇄 57쪽; `src/swancom1.ftn:10290` `ETA2 = ETA1 + ( SXX1 - SXX2 ) / ( 0.5 * ( DP2 + DP1 ) )`.

### 3.3 2D — 힘(gradient) 계산 후 `SETUP2D` 호출 (`:10300-10402`)

- radiation stress 미분으로 파랑힘 `WFRCX/WFRCY` 를 중앙차분 계산하되, **인접점이 dry(`DEP2≤DEPMIN`)면 stencil 을 해당 방향으로 축소** (`:10317-10318` x-방향 `IXLO/IXUP`, `:10336-10337` y-방향) — dry point 근방 편미분 붕괴 방지.
- `CALL SETUP2D(...)` (`:10402`) — §4 의 Poisson 해.

### 3.4 후처리 — 기준점 보정·수심 갱신·dry 이웃 채움 (`:10406-10500`)

- **기준점 보정** (`:10412-10419`): 최심점 `IDXMAX` 의 setup 을 사용자 지정 `PSETUP(2)` 로 맞추는 상수 이동 `S_UPCOR = S_UPDP - PSETUP(2)` 후 전역 감산 — Poisson 해가 상수 부정(Neumann 전경계, §4)이므로 필요한 게이지 고정.
- **수심 반영** (`:10440`): `DEP2 = DEPSAV + SETUP2` — 저장해둔 원수심(`DEPSAV`)에 setup 을 더해 다음 반복의 유효수심 갱신 (Purpose 의 "adds the set-up to the depth").
- **dry 점 처리** (`:10452-10490`): 갱신 후 `DEP2≤DEPMIN` 인 점은 이웃 wet 점 setup 을 승계해 재침수 판정 (`:10485-10487`) — wetting 허용.

## 4. `SETUP2D` — 일반좌표 2D Poisson + SOR (`:10501-12121`)

swanuse PDF 86–87·SETUP 절(node28:2971–2982)은 비구조·구면·병렬 실행 제한을 이미 설명한다. 코드는 `IF (PARLL .AND. .NOT.ONED) THEN`에서 오류 수준 4를 내고 반환한다. `IF (OPTG.EQ.5) THEN`에서는 `LSETUP = 0`으로 설정한다. 구면좌표는 `IF (KSPHER.NE.0)`에서 오류 수준 2를 보고한다. C는 swantech 5장에 없는 이 조건별 처리와 `IF ( ICONV.EQ.0 ) THEN` 안의 `CSETUP = .FALSE.`, `IF ( RESM.GT.1.E8 ) SETUP = 0.`에 한정한다. 근거: [R3 대조](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md), CP-025.

Purpose/Method(헤더): "**A 2D Poisson equation in general coordinates is solved**" (`:10553`) — 이론 [swan-tech-ch4-5-bc-2d-setup](../manual-notes/swan-tech-ch4-5-bc-2d-setup.md) 의 Eq 5.2(Poisson)·5.7-5.24(곡선격자 finite-volume) 구현부.

### 4.1 경계조건 (`:10665-10683`)

- 기본: "**Neumann boundary condition is imposed on all the boundaries**" (`:10665`) — 이론 Eq 5.23-24(half-cell Neumann).
- "A modified SOR method for the Poisson equation in unsteady..." (`:10672`) — [swan-tech-ch6-iterative-solvers](../manual-notes/swan-tech-ch6-iterative-solvers.md) §6.2 의 SOR(Botta-Ellenbroek 1985) 대응.
- 중첩 set-up의 Dirichlet 조립 분기는 표준 입력으로 활성화할 수 없다. 부모 모델의 set-up을 중첩 경계에 적용하는 실행 기능으로 안내하지 않는다. 근거: `src/swancom1.ftn:11781` `IF ( LSETUP.EQ.2 ) THEN`; `src/swanpre1.ftn:2094` `LSETUP = 1`; `43e9bbb:src/swanmain.ftn:1197` `! PSETUP(1) is currently unused, but can be used as setup nesting flag`.

### 4.2 9-point stencil 조립 (`:11086-11161`)

`AMAT(INDX,1..9)` — 중앙(1)+8이웃의 **9-point stencil**, 교차미분 항은 대각이웃에 `0.25*CONTRB` 로 분배 (`:11086-11157`; 예: `:11090-11093` x-교차항 → `AMAT(:,3/4/8/9) ∓0.25`). 이론 노트의 "Ax=f Eq 5.25, **9-point stencil NWKARR=9**"와 일치. 고립/무효 행은 항등행으로 치환 (`:11159-11161` `AMAT(INDX,1)=1`).

### 4.3 솔버 파라미터·자동 완화계수 (`:11812-11830`)

```fortran
REPS   = PNUMS(23)          ! :11812  수렴 임계 (기본 1e-6)
IAMOUT = INT(PNUMS(24))     ! :11813  반복과정 출력 (기본 0)
MAXIT  = INT(PNUMS(25))     ! :11814  최대 반복 (기본 1000)
```

기본값 출처: `src/swanmain.ftn:1269-1271` (`PNUMS(23)=1.E-6 / (24)=0. / (25)=1000.`). 사용자 제어 = `NUMERIC ... SETUP [eps2][outp][niter]` ([swan-command-numerics-output-reference](../manual-notes/swan-command-numerics-output-reference.md) — SETUP eps2 기본 SOR 1e-6 표기와 정합).

**자동 최적 ω** (`RELAX=-1` 시, `:11815-11828`): 활성격자수 `MCGRD` 로 Jacobi 스펙트럴반경을 휴리스틱 추정(ρ = 1−1/M [M<100] / 1−3/M [M<1000] / 1−10/M) 후 고전 최적 SOR 공식

$$\omega_{opt} = \frac{2}{1+\sqrt{1-\rho^2}} \qquad (\texttt{XOMEG = 2./(1.+SQRT(1.-RHOV*RHOV))}, \; \texttt{:11828})$$

사용자 지정 시 `XOMEG = RELAX` (`:11830`).

### 4.4 반복·수렴 (`:11835-12100`)

- `RESM`은 한 반복에서 set-up 갱신량의 최댓값이다. 선형계 잔차의 최댓값이 아니다. 코드의 진단 문자열과 실제 계산량을 구분한다. 내부점·변·꼭짓점의 별도 순회를 red-black 갱신으로 부르지 않는다. 근거: `src/swancom1.ftn:11873` `RES = ABS(SETUP(INDX) - SETPI)`; `src/swancom1.ftn:11879` `SETUP(INDX) = SETPI`; `src/swancom1.ftn:12108` `inf-norm of the residual`.
- SOR의 RESM은 해 갱신량 절댓값의 최댓값이다. SIP의 상대 잔차 2-노름과 구분한다. SOR의 기본 EPS2는 1E-6이다. 근거: swanuse PDF 95쪽 / 인쇄 87쪽; `src/swanmain.ftn:1269` `PNUMS(23) = 1.E-6`.

`IF ( MCGRD.LT.100 ) THEN`, `ELSE IF ( MCGRD.LT.1000 ) THEN`, 나머지 분기에서 `RHOV`의 분자는 각각 1, 3, 10이다. `RESM`은 수위 갱신량의 최댓값이다. swanuse PDF 95·NUMERIC 절(node29:554–607)은 SOR의 갱신량 종료식과 `eps2=1.e-6`을 이미 적는다. 최대 반복 기본값 1000도 같은 쪽과 `src/swanmain.ftn:1271`이 일치한다. C는 swantech 5장과 swanuse NUMERIC 절에 없는 `RHOV` 추정과 12076–12087행의 완화계수 전환 조건에 한정한다. 근거: [R3 대조](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md), CP-019.

## 5. 이론↔코드 정합 요약

| 이론 (swantech) | 코드 (본 노트) |
|---|---|
| Eq 3.59-61 radiation stress $S_{xx}/S_{xy}/S_{yy}$ | `:10246-10248` ($n=c_gk/\sigma$ 전개 일치) |
| Eq 2.143 equilibrium (1D) | `src/swancom1.ftn:10290` `ETA2 = ETA1 + ( SXX1 - SXX2 ) / ( 0.5 * ( DP2 + DP1 ) )`; 저장량은 $R_{xx}=S_{xx}/(\rho g)$다. |
| Eq 5.2 Poisson + Eq 5.7-5.24 곡선격자 FV | SETUP2D 전체, 9-point `AMAT` `:11086-` |
| Eq 5.6 Dirichlet 경계 | 중첩 set-up의 Dirichlet 조립 분기는 표준 입력으로 활성화할 수 없다. `src/swancom1.ftn:11781` `IF ( LSETUP.EQ.2 ) THEN`; `src/swanpre1.ftn:2094` `LSETUP = 1`. swantech PDF 128쪽 / 인쇄 120쪽 (5.6). [10-13 전수 검증 정정] |
| Ch6 §6.2 SOR (Botta-Ellenbroek) | `:10672` modified SOR, ω 자동 `:11828` |
| swanuse §2.2 개방 연안 적용 권고 | 개방 연안 적용 권고는 매뉴얼의 물리 가정으로 인용한다. Neumann 조건과 기준값 보정만으로 항만 적용의 정확도 한계를 입증했다고 쓰지 않는다. `src/swancom1.ftn:10413` `S_UPCOR = S_UPDP - PSETUP(2)` |

## 6. 검증 메모

- 모든 line 인용은 위키 raw `swancom1.ftn`(v41.51 clone) 직접 Read. 식 전개($n$ 치환)는 코드 그대로의 항등변형으로, 값 추정 없음.
- `SWPRSET`·`INSAC`·`SINTGRL`·`SWMTLB` 는 Purpose 헤더 verbatim 확인 후 유틸리티 판정 — deep dive 미수행(§2 표가 최종 커버리지 기록). INSAC/SACCUR Purpose 중복은 소스 관찰 사실.
- 잔여 후속(선택): swancom2~5 동일 방식 cross-walk 는 기존 노트 인용밀도가 이미 높아 우선순위 낮음.

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:CP-018 | set-up 기준 수위와 마름점 | — (문서 누락) | set-up 기준 수위와 마름점. `src/swancom1.ftn:10413` `S_UPCOR = S_UPDP - PSETUP(2)`; `src/swancom1.ftn:10419` `SETUP2(INDX) = SETUP2(INDX) - S_UPCOR`; `src/swancom1.ftn:10485` `IF (DEPSAV(INDX) + SETUP2(INDXL) .GT. DEPMIN) THEN`; `src/swancom1.ftn:10486` `SETUP2(INDX) = SETUP2(INDXL)`. | C 문서 누락 | `LSETUP=1`에서 최심점 수위를 `PSETUP(2)`에 맞추도록 젖은 점에 상수를 뺀다. 최심점 선택은 `src/swancom1.ftn:10215–10225`의 전체 계산격자 순회다. swanuse PDF 87·SETUP 절(node28:2986–3015)은 최심점과 SUPCOR 보정을 이미 설명한다. C는 swantech 5장에 없는 보정·수심 갱신·이웃값 재침수 검사의 실행 순서에 한정한다. `IF (DEPSAV(INDX) + SETUP2(INDXL) .GT. DEPMIN) THEN` 뒤 이웃값을 대입하며 영구 마름점은 제외한다. |
| R3:CP-019 | 수정 SOR의 계수와 종료 | — (문서 누락) | 수정 SOR의 계수와 종료. `src/swancom1.ftn:11822` `RHOV = 1. - 1./REAL(MCGRD)`; 11824는 분자가 3이다. 11826은 10이다. 11828 `XOMEG = 2./(1.+SQRT(1.-RHOV*RHOV))`; `src/swancom1.ftn:11873` `RES = ABS(SETUP(INDX) - SETPI)`; `src/swancom1.ftn:12076` `IF ( RESM.GT.REPS ) THEN`; `src/swancom1.ftn:12081` `RESM.GT.10.*RESMI*(XOMEG-1.)**II ) XOM = 1.`. | C 문서 누락 | `IF ( MCGRD.LT.100 ) THEN`, `ELSE IF ( MCGRD.LT.1000 ) THEN`, 나머지 분기에서 `RHOV`의 분자는 각각 1, 3, 10이다. `RESM`은 수위 갱신량의 최댓값이다. swanuse PDF 95·NUMERIC 절(node29:554–607)은 SOR의 갱신량 종료식과 `eps2=1.e-6`을 이미 적는다. 최대 반복 기본값 1000도 같은 쪽과 `src/swanmain.ftn:1271`이 일치한다. C는 swantech 5장과 swanuse NUMERIC 절에 없는 `RHOV` 추정과 12076–12087행의 완화계수 전환 조건에 한정한다. |
| R3:CP-025 | set-up 실행 제한과 실패 처리 | — (문서 누락) | set-up 실행 제한과 실패 처리. `src/swanpre1.ftn:2085` `IF (PARLL .AND. .NOT.ONED) THEN`; `src/swanpre1.ftn:2086` `CALL MSGERR(4,'setup is not supported in parallel run')`; `src/swanpre1.ftn:2089` `IF (OPTG.EQ.5) THEN`; `src/swanpre1.ftn:2091` `LSETUP = 0`; `src/swancom1.ftn:12099` `CSETUP = .FALSE.`; `src/swancom1.ftn:12100` `IF ( RESM.GT.1.E8 ) SETUP = 0.`. | C 문서 누락 | swanuse PDF 86–87·SETUP 절(node28:2971–2982)은 비구조·구면·병렬 실행 제한을 이미 설명한다. 코드는 `IF (PARLL .AND. .NOT.ONED) THEN`에서 오류 수준 4를 내고 반환한다. `IF (OPTG.EQ.5) THEN`에서는 `LSETUP = 0`으로 설정한다. 구면좌표는 `IF (KSPHER.NE.0)`에서 오류 수준 2를 보고한다. C는 swantech 5장에 없는 이 조건별 처리와 `IF ( ICONV.EQ.0 ) THEN` 안의 `CSETUP = .FALSE.`, `IF ( RESM.GT.1.E8 ) SETUP = 0.`에 한정한다. |
| R3:NT-012 | 코드 복사응력의 정규화 | 현재 노트의 수정 전 원문: `source-analysis/swan-setup-solver-swancom1-crosswalk.md:78` `ρg 와 적분가중`과 `는 저장 시 적용`; 90의 `$\eta_{i+1} = \eta_i + (S_{xx,i} - S_{xx,i+1})/\bar d$`. | `src/swancom1.ftn:10237` `CK = CG(1) * K(1)`; `src/swancom1.ftn:10239` `ELOC = SIG(1) * AC2(ID,IS,INDX)`; `src/swancom1.ftn:10246` `RSXX = RSXX + (CK*SPCDIR(ID,4)+CK - SIG(1)/2.) * ELOC`; `src/swancom1.ftn:10247` `RSXY = RSXY + CK*SPCDIR(ID,5) * ELOC`; `src/swancom1.ftn:10248` `RSYY = RSYY + (CK*SPCDIR(ID,6)+CK - SIG(1)/2.) * ELOC`; `src/swancom1.ftn:10263` `SETPDA(INDX,3) = RSXX * DDIR * FRINTF`. | B 문서 오기 | 코드 저장량을 $R_{ij}=S_{ij}/(\rho g)$로 정의한다. 1D 갱신은 $\eta_{i+1}=\eta_i+(R_{xx,i}-R_{xx,i+1})/\bar d$다. 대응 물리식은 (2.143)이다. |
| R3:NT-013 | 중첩 Dirichlet의 실행 가능성 | 현재 노트의 수정 전 원문: `source-analysis/swan-setup-solver-swancom1-crosswalk.md:111` `nesting 시 Dirichlet`; `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:63` `대모델 setup → nested 외경계`. | `src/swancom1.ftn:11781` `IF ( LSETUP.EQ.2 ) THEN`; `src/swanpre1.ftn:2094` `LSETUP = 1`. [SWAN-git-verify-D.md](../../../_staging/recovery/compare/SWAN-git-verify-D.md)의 SU-011. `43e9bbb:src/swanmain.ftn:1197` `! PSETUP(1) is currently unused, but can be used as setup nesting flag`; `src/swancom1.ftn:11781–11802`. | D 문서에만 있음 | 중첩 set-up의 Dirichlet 조립 분기는 표준 입력으로 활성화할 수 없다. 부모 모델의 set-up을 중첩 경계에 적용하는 실행 기능으로 안내하지 않는다. |
| R3:NT-014 | SOR 갱신량과 갱신 순서 | 현재 노트의 수정 전 원문: `source-analysis/swan-setup-solver-swancom1-crosswalk.md:135` `잔차 **inf-norm**`과 `red-black 식 다중 블록 갱신 루프.` | `src/swancom1.ftn:11873`은 `RES = ABS(SETUP(INDX) - SETPI)`다. 11879행에서 즉시 `SETUP(INDX) = SETPI`로 갱신한다. 내부점 순서는 11851–11852행의 IY·IX 순회다. 한편 12108행의 진단 문자열은 `inf-norm of the residual`이라고 부른다. 이 코드 내부 명칭도 실제 갱신량 정의와 다르다. swanuse PDF 95의 SOR 종료식은 갱신량 기준과 일치한다. | B 문서 오기 | `RESM`은 한 반복에서 set-up 갱신량의 최댓값이다. 선형계 잔차의 최댓값이 아니다. 코드의 진단 문자열과 실제 계산량을 구분한다. 내부점·변·꼭짓점의 별도 순회를 red-black 갱신으로 부르지 않는다. |
| R3:NT-015 | set-up 적용 한계의 근거 | 현재 노트의 수정 전 원문: `source-analysis/swan-setup-solver-swancom1-crosswalk.md:147` `구조가 그 한계의 코드적 근거`. | `src/swancom1.ftn:10402` `CALL SETUP2D( SETUP2, XCGRID, YCGRID, SETPDA(1,1), SETPDA(1,2),`; `src/swancom1.ftn:10440` `DEP2(INDX) = DEPSAV(INDX) + SETUP2(INDX)`. | H 코드 대조 대상 아님 | 개방 연안 적용 권고는 매뉴얼의 물리 가정으로 인용한다. Neumann 조건과 기준값 보정만으로 항만 적용의 정확도 한계를 입증했다고 쓰지 않는다. |
| R5:PN-184 | SOR 노름 설명 | 현재 노트의 수정 전 원문: `source-analysis/swan-setup-solver-swancom1-crosswalk.md:135` `잔차 **inf-norm**`. | `src/swancom1.ftn:12056` `RES = ABS(SETUP(INDX) - SETPI)`. | B | SOR의 RESM은 해 갱신량 절댓값의 최댓값이다. SIP의 상대 잔차 2-노름과 구분한다. |

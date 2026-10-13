---
title: "SWAN Surfbeat IEM (Infragravity Energy Model) — SwanIEM.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanIEM.ftn90` 직접 read (1230 lines, line 1-130 module header + grep 4 subroutines). User cmd SURFBEAT (swanuse.pdf p.80) 매핑. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header verbatim"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-quasi-coherent.md
---

## Scope

SwanIEM.ftn90 — SWAN 41.85 (2019-01 Reniers) 신규 module. **1D surfbeat = infragravity wave (IG)** 모델 — 단파(short wave) 그룹의 bound IG + radiation stress 변동 → free IG 변환. User cmd `SURFBEAT` (p.80).

## Source basis

- `SwanIEM.ftn90` (1230 lines)
- User cmd `SURFBEAT` (swanuse.pdf p.80)
- 본 module 의 Tech 문서 §은 미식별 (SWAN Tech swantech.pdf TOC 에 명시 §없음)

## 1. Module header (line 1-2, 32-46 verbatim)

```
! This file contains data and routines for surfbeat (Infragravity Energy Model)
module SwanIEM
!   Authors
!   41.85: Ad Reniers
!   Updates
!   41.85, January 2019: New module
!   Purpose
!   Contains data with respect to 1D surfbeat
```

→ **Reniers** = surfbeat / IG 이론 1차 (Reniers·MacMahan·Thornton·Stanton 2007 시리즈).

## 2. Module data (line 54-71)

```fortran
integer :: nf, nff, nif                ! nf=총 freq, nif=incident freq 수
integer :: nmax                        ! short-wave pair 최대 수
integer, save :: ntf = -9              ! IG frequencies 수 (< 0 first COMPUTE, > 0 second COMPUTE)

integer, allocatable :: iss(:), iwt(:), itt(:)   ! 인덱스 배열

real :: dfiem                          ! incident spectrum frequency resolution (constant)
real :: e_trsh                         ! energy threshold (Emax fraction)
real, allocatable :: E0(:,:)           ! offshore energy density [J/m²], uniformly distributed
real, allocatable :: Ebig(:,:,:)       ! BOUND infragravity wave energy
real, allocatable :: freq(:)           ! uniformly distributed relative frequencies

logical :: sflog                       ! IG freq distribution: linear (false) or log (true)
```

핵심:
- `Ebig` = **bound infragravity wave energy** — Longuet-Higgins·Stewart 1962 group-bound long wave
- `ntf` 의 부호 = COMPUTE 단계 표시 (first → IG 격자 설정, second → 실제 계산)
- `e_trsh` = small-energy threshold (numerical stability)
- `sflog` = uniform vs logarithmic frequency grid

## 3. Subroutine inventory (4 subroutines)

| Line | Subroutine | Purpose |
|---|---|---|
| **78** | `SwanIEMinitig` | IG 격자 초기화 (incident spectrum → bound IG 격자 생성) |
| **324** | `SwanIEMmeanwav(AC2, HSIBC, SPCSIG, KGRPNT, HS)` | Mean wave 통계 (H_s 등) for IG boundary |
| **488** | `SwanIEMncalc` | IG 계산 핵심 (free vs bound 변환?) |
| **679** | `SwanIEMsrfbeat(HS, AC2, DEP2, SPCDIR, SPCSIG, KGRPNT)` | **Surfbeat source term** — main contribution |

### 3.1 SwanIEMinitig (line 78, header verbatim)

> "Initializes several variables and arrays for the computation of reflected waves"

→ 단순 init 라기보다는 reflected wave (= IG 의 free 부분, 해안에서 반사) 격자 준비.

### 3.2 SwanIEMmeanwav (line 324)

인자: `AC2, HSIBC, SPCSIG, KGRPNT, HS`.
- `AC2` = action density
- `HSIBC` = H_s at IG boundary
- `HS` = significant wave height
→ short-wave 통계로부터 IG bound energy 계산을 위한 mean wave 정보 제공.

### 3.3 SwanIEMncalc (line 488)

자세한 인자 없음. 내부 `Ebig` array 갱신 추정.

### 3.4 SwanIEMsrfbeat (line 679)

인자: `HS, AC2, DEP2, SPCDIR, SPCSIG, KGRPNT`.
→ Surfbeat = depth-modulated wave group → 천해 IG amplification. `DEP2` (수심) 변화 시 bound → free 전환.

## 4. Surfbeat physics 배경

**Infragravity wave (IG)** = 0.01 ~ 0.05 Hz (20~100 s 주기) 의 sub-harmonic ocean wave. 주된 형성 mechanism:

1. **Bound IG** (Longuet-Higgins·Stewart 1962): short-wave group 의 radiation stress 변동 → group-bound long wave
2. **Free IG** at shore: bound IG 가 surf zone 에서 단파 breaking 후 free 로 release → coastal IG sea level oscillation
3. **Edge wave / leaky wave**: 해안 반사된 IG

해안공학 응용:
- **Harbor resonance** (oscillation in marinas/harbors)
- **Storm surge cascade with IG** (storm 시 IG 가 mean sea level 추가)
- **Beach groundwater pumping** (IG 가 swash 영역 침투)
- **Coral reef IG flooding** (open ocean 보다 atoll 가 IG 에 더 노출)

## 5. User cmd `SURFBEAT` (swanuse.pdf p.80)

SURFBEAT는 정상 2차원 직사각 격자와 서쪽 입사 경계를 요구한다. DF=0.01, NMAX=50000, EMIN=0.05가 기본값이다. 격자 설정 뒤의 두 번째 COMPUTE가 필요하다. 근거: swanuse PDF 88–89쪽 / 인쇄 80–81쪽; `src/swanpre1.ftn:2144` `CALL INREAL ('DF'  , dfiem , 'STA', 0.01 )`, `src/swanpre1.ftn:2145` `CALL ININTG ('NMAX', nmax  , 'STA', 50000)`, `src/swanpre1.ftn:2146` `CALL INREAL ('EMIN', e_trsh, 'STA', 0.05 )`, `src/swanpre1.ftn:2149` `IF (KEYWIS ('UNIF')) sflog = .FALSE.`, `src/swanpre1.ftn:2150` `IF (KEYWIS ('LOG' )) sflog = .TRUE.`. `src/swanmain.ftn:1214` `sflog = .FALSE.`. `src/SwanIEM.ftn90:172` `df = PI2 * dfiem`, `src/SwanIEM.ftn90:185` `SPCSIG(1) = df`, `src/SwanIEM.ftn90:187` `SPCSIG(is) = SPCSIG(is-1) + df`. `src/swanpre1.ftn:2137` `IF ( OPTG.NE.1 ) THEN`. `src/swanmain.ftn:4108` `IF ( ONED ) THEN`, `src/swanmain.ftn:4114` `IF ( NSTATC.NE.0 .OR. NSTATM.NE.0 ) THEN`, `src/swanmain.ftn:4118` `IF ( NCOMPT.EQ.1 .AND. ntf.LT.0 ) THEN`, `src/swanmain.ftn:4123` `ELSEIF ( NCOMPT.EQ.2 .AND. ntf.GT.0 ) THEN`, `src/swanmain.ftn:4128` `ELSEIF ( NCOMPT.GT.2 ) THEN`, `src/swanmain.ftn:4142` `IF ( ALPC.NE.0.) THEN`, `src/swanmain.ftn:4186` `'location of boundary must be west in case of surfbeat'`.

`do while ( nic > nmax .or. e_trs < e_trsh )`에서 성분을 고른 뒤 `e_trs = e_trs + d_trs`로 문턱을 증가시킨다. 종료 검사값은 마지막 선택 문턱보다 한 증가분 크다. `if ( e_trs > 0.1 ) then` 오류 검사는 루프 종료 뒤 수행한다. 근거: `src/SwanIEM.ftn90:614` `e_trs = 0.01`, `src/SwanIEM.ftn90:616` `do while ( nic > nmax .or. e_trs < e_trsh )`, `src/SwanIEM.ftn90:618` `enl = ( E0 > e_trs*Emax )`, `src/SwanIEM.ftn90:645` `e_trs = e_trs + d_trs`, `src/SwanIEM.ftn90:649` `if ( e_trs > 0.1 ) then`.

## 6. Cross-references

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) — User cmd SURFBEAT (p.80)
- [swan-source-coverage-audit](swan-source-coverage-audit.md) §3.1 신규 발견
- [swan-quasi-coherent](swan-quasi-coherent.md) — QC는 Wigner 분포로 파랑 성분 간 교차상관을 다룬다. 근거: swantech PDF 67–68쪽 / 인쇄 59–60쪽; [R3:QC-002](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론). 41.90과 41.85는 각각 QCM과 IEM의 소스 내부 변경 표기다. 근거: `src/SwanQCM.ftn90:38`의 `!   41.90, June 2021: New module`; `src/SwanIEM.ftn90:38`의 `!   41.85, January 2019: New module`. [10-13 전수 검증 정정]
- [swan-bragg-scattering](swan-bragg-scattering.md) — 또 다른 phase 효과 (산란)
- Author: Ad Reniers (41.85, 2019-01) — Reniers·MacMahan·Thornton·Stanton 학파
- 외부 reference 추정: Reniers et al. 2002 *Coastal Eng*, Reniers·Roelvink·Battjes 2004 *JGR*

## 7. 한계 + 다음 단계

- 본 module 의 Tech 문서 §매핑 부재 (TOC 미수록) → swantech.pdf 본문 검색 후속
- 외부 reference (Reniers 학파) DOI 검증 필요
- `SwanIEMncalc` 의 정확 알고리즘 (488-678 라인) deep dive 별도
- SURFBEAT는 정상 2차원 직사각 격자와 서쪽 입사 경계를 요구한다. 근거: swanuse PDF 88–89쪽 / 인쇄 80–81쪽; `src/swanmain.ftn:4108` `IF ( ONED ) THEN`; `src/swanpre1.ftn:2137` `IF ( OPTG.NE.1 ) THEN`.
- DF=0.01, NMAX=50000, EMIN=0.05가 기본값이다. 근거: swanuse PDF 88–89쪽 / 인쇄 80–81쪽; `src/swanpre1.ftn:2144` `CALL INREAL ('DF'  , dfiem , 'STA', 0.01 )`; `src/swanpre1.ftn:2145` `CALL ININTG ('NMAX', nmax  , 'STA', 50000)`; `src/swanpre1.ftn:2146` `CALL INREAL ('EMIN', e_trsh, 'STA', 0.05 )`.

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R5:PN-072 | SURFBEAT EMIN | SURFBEAT EMIN의 실제 적용. swanuse PDF 89쪽 / 인쇄 81쪽: `energy levels are larger than [emin] × Emax`. | `src/SwanIEM.ftn90:614` `e_trs = 0.01`, `src/SwanIEM.ftn90:616` `do while ( nic > nmax .or. e_trs < e_trsh )`, `src/SwanIEM.ftn90:618` `enl = ( E0 > e_trs*Emax )`, `src/SwanIEM.ftn90:645` `e_trs = e_trs + d_trs`, `src/SwanIEM.ftn90:649` `if ( e_trs > 0.1 ) then`. | C | `do while ( nic > nmax .or. e_trs < e_trsh )`에서 성분을 고른 뒤 `e_trs = e_trs + d_trs`로 문턱을 증가시킨다. 종료 검사값은 마지막 선택 문턱보다 한 증가분 크다. `if ( e_trs > 0.1 ) then` 오류 검사는 루프 종료 뒤 수행한다. |

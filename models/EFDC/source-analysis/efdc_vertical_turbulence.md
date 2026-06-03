---
title: "EFDC+ 연직 난류폐합 — CALAVB Mellor-Yamada 2.5 (Galperin/Kantha-Clayson/Kantha 3 옵션 + ISFAVB 필터·ISLLIM·ISSQL) vs GOTM (ISGOTM, k-ε/MY/GLS)"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calavb.f90 (394 lines) 전체 직접 read + GOTM_Turbulence/mod_turbulence.F90 (4149 lines) 헤더·namelist·옵션 + hdmt2t.f90 (ISGOTM dispatch line 535-537) + mod_scaninp.f90 (ISGOTM 입력 line 212) 직접 확인. SFAV/SFAB 상수 ↔ theory-v12 Ch2 Table 2.1 cross-check. file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — calavb MY2.5 구현 + GOTM 결합 + 이론 Table 2.1 정합"
verification_date: 2026-06-03
related:
  - models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md
  - models/EFDC/source-analysis/efdc_dispersion.md
---

# EFDC+ 연직 난류폐합 — CALAVB (MY2.5) vs GOTM

> `calavb.f90`(394, EFDC+ DSI 2021-24) + `GOTM_Turbulence/mod_turbulence.F90`(4149) 직접 read. EFDC+ 의 **연직 eddy viscosity `AV` / diffusivity `AB`** 산출. **두 경로**: (1) built-in **Mellor-Yamada Level 2.5**(CALAVB, 기본) (2) **GOTM** 결합(`ISGOTM>0`). [[efdc-theory-v12-ch2-hydrodynamics]] §2.1.4 의 이론(Eq 2.14-2.26)을 구현. ※ `AV/AB/AQ` 는 모두 **H 로 나눈 값**으로 저장(코드 주석 line 14).

## 1. CALAVB — Mellor-Yamada 2.5 (Galperin 변형)

### 1.1 핵심 식 (line 150-158, full buoyancy 분기)

```fortran
RIQ  = -GP*HP(L)*DML(L,K)**2*DZIG(L,K)*(B(L,K+1)-B(L,K))/QQ(L,K)   ! Richardson #
RIQ  = max(RIQ,RIQMIN); RIQ = min(RIQ,RIQMAXX)
SFAV = SFAV0*(1.+SFAV1*RIQ)/((1.+SFAV2*RIQ)*(1.+SFAV3*RIQ))         ! momentum φ_A
SFAB = SFAB0/(1.+SFAB1*RIQ)                                         ! buoyancy ρ_K
AB(L,K) = SFAB*DML(L,K)*HP(L)*QQSQR(L,K) + AVBXY(L)                 ! 연직 diffusivity
AV(L,K) = SFAV*DML(L,K)*HP(L)*QQSQR(L,K) + AVOXY(L)                 ! 연직 viscosity
AV = AV*HPI; AB = AB*HPI                                            ! /H 저장
```
- `RIQ` = Richardson number $R_q = \frac{gH l^2}{q^2 H^2}\partial_z b$ (theory **Eq 2.23**). `QQ`=$q^2$ turbulent intensity, `QQSQR`=$q$, `DML`=length scale $l$, `B`=buoyancy, `DZIG`=연직 metric, `GP`=g.
- `SFAV` = momentum stability $\phi_A$ (theory **Eq 2.15**), `SFAB` = scalar stability $\rho_K$.
- `AV = φ_A·l·q + AVOXY`, `AB = ρ_K·l·q + AVBXY` (theory **Eq 2.14·2.20**; AVOXY/AVBXY = background, 2018-10 spatially varying).

### 1.2 ISTOPT(0) — stability function 상수 3 옵션 (line 44-73) ★

| ISTOPT(0) | formulation | SFAV1(R₁⁻¹) | SFAV2(R₂⁻¹) | SFAV3(R₃⁻¹) | SFAB0(K₀) | SFAB1 |
|---|---|---|---|---|---|---|
| **0/1 (default)** | **Galperin et al. 1988** | 7.760050 | 34.676440 | 6.127200 | 0.493928 | 34.676440 |
| **2** | **Kantha & Clayson 1994** | 8.679790 | 30.192000 | 6.127200 | 0.493928 | 30.192000 |
| **3** | **Kantha 2003** | 14.509100 | 24.388300 | 3.236400 | 0.490025 | 24.388300 |

- `SFAV0 = 0.392010` (momentum A₀, 전 옵션 공통), `SFAB1 = SFAV2`(=R₂⁻¹) — buoyancy stability 분모계수.
- 코드 상수 = [[efdc-theory-v12-ch2-hydrodynamics]] **Table 2.1** 와 정합 (Galperin R₁⁻¹=7.760050 ✓ / K-C 8.679790 ✓ / Kantha 14.509100 ✓).
- **★ code ≠ theory 발견**: theory Table 2.1 은 **4 옵션**(Mellor-Yamada 1982 R₁⁻¹=7.846436 포함)을 나열하나, **calavb.f90 은 `ISTOPT(0)==2/3` 만 분기**하고 기본(0·1)은 **Galperin**. 즉 **MY1982 원본 상수(7.846436)는 이 EFDC+ build 에서 선택 불가** — 실질 3 옵션. theory 의 "4 옵션" 은 이론 reference, 구현은 Galperin base.

### 1.3 ISFAVB — 시간 필터 (line 15-17, 100-208)

이전 timestep 값과의 평활 (안정성):
- `0` 필터 없음 (또는 N==1 첫 step)
- `1` 산술평균 `AV = 0.5*(AV_old + AV_new)`
- `2` 기하평균 `AV = SQRT(AV_old·AV_new)`

### 1.4 계산 분기 (line 81-211)

| 조건 | 처리 |
|---|---|
| `ISAVCOMP==0` | **상수 AV** = AVOXY·HPI, AB = AVBXY·HPI (난류 미계산) |
| `BSC ≤ 1e-6` | **중립**(no buoyancy): `SFAV0/SFAB0` 만 (Richardson 무시) |
| else | **full MY2.5** (RIQ 포함, §1.1) |

### 1.5 AQ — q²/q²l 방정식 확산계수 (ISSQL, line 311-387)

`AQ` = TKE(q²)·length(q²l) 수송방정식의 연직 확산계수 (theory **Eq 2.24·2.25**):
- `ISSQL==0` 또는 `ISTOPT(0)≤2`: **momentum 비례** `AQ = 0.205*(AV(K-1)+AV(K))` (theory $A_q=0.2ql$, line 320).
- `ISSQL==1` 또는 `ISTOPT(0)==3 (Kantha)`: **상수형** `AQ = 0.314*(DML·QQSQR) + AVOXY/H` (line 352·374).

### 1.6 Limiter·BC

- `ISLLIM≥1` → `RIQMAXX = RIQMAX` (Galperin 1988 length-scale limit $\sqrt{R_q}<0.53$, line 76). 미설정 시 1e32.
- `RIQMIN = -0.999/SFAB1` (분모 0 방지, line 51).
- open boundary `AB=0` (line 215-220), depth<ZBR bypass(상층값 복사, line 244-262), `ISAVBMX≥1` → max AVMX/ABMX clamp(line 266-281).
- `AVUI/AVVI` = U/V interface 평균 AV 의 역수 (IGRIDV=0 단순평균 / ≠0 SGZ 가중, line 285-309) — 운동량 연직확산 항이 사용.

## 2. GOTM 결합 (ISGOTM>0) — 대안 폐합

`hdmt2t.f90:535-537`:
```fortran
if( ISGOTM > 0 )then
  call Advance_GOTM(ISTL)        ! CALAVB 대신 GOTM 으로 AV/AB/AQ 산출
endif
```
- 입력: `mod_scaninp.f90:212` `read ISGOTM, IFRICTION, ICALNN, ICALSS, CHARNOCK`.
- **GOTM** = General Ocean Turbulence Model (Burchard·Umlauf). 수직 1D column 을 GOTM 으로 복사→난류 update→AV/AB 반환 (mod_turbulence.F90 헤더: "do_turbulence() 가 3-D model 과 GOTM 의 door").

### 2.1 GOTM 옵션 (mod_turbulence.F90 namelist, line 333-396)

| 옵션 | 값 | 의미 |
|---|---|---|
| `tke_method` | 1 local_eq / **2 k-ε style** / 3 MY q²/2 | TKE 방정식 (default **2**) |
| `len_scale_method` | parabolic/triangular/Xing-Davies/Robert-Ouellet/Blackadar/Bougeault-Andre/ISPRAMIX/**diss_eq**/MY q²l/**generic GLS** | 길이척도 (default **8 = dissipation eq**) |
| `stab_method` | (default **3**) | stability functions |

→ GOTM 은 **k-ε, k-ω(GLS), Mellor-Yamada** 등을 모두 지원 — CALAVB(MY2.5 단일)보다 훨씬 넓은 폐합 선택지. 단 EFDC+ 는 GOTM 을 1D-column-coupling 으로 호출하므로 수평 정보는 mean-flow(EFDC) 가 담당.

## 3. CALAVB vs GOTM 비교

| 항목 | CALAVB (built-in) | GOTM (ISGOTM>0) |
|---|---|---|
| 폐합 차수 | Mellor-Yamada **2.5** 고정 | local_eq / **k-ε** / MY / **GLS(k-ω)** 선택 |
| stability fn | Galperin / Kantha-Clayson / Kantha (ISTOPT(0)) | stab_method (Canuto 등 GOTM library) |
| length scale | q²l 수송 + Galperin limit | parabolic~generic-GLS 10 옵션 |
| 코드 규모 | 394 lines | 4149 lines (별도 module) |
| 적용 | 기본·경량 | 고급·연직 정밀(성층·entrainment) |

→ 일반 연안/하구 = CALAVB MY2.5 충분. 강성층·표층 entrainment·내부파 등 연직난류 민감 case = GOTM k-ε/GLS 가치.

## 4. 연결

- [[efdc-theory-v12-ch2-hydrodynamics]] §2.1.4 — 이론(Eq 2.14-2.26, Table 2.1 closure 상수 4모델). 본 노트가 그 **구현**(+ code≠theory MY1982 미선택 발견).
- [[efdc_dispersion]] — 수평 난류(Smagorinsky HMD). 본 노트는 연직(MY2.5/GOTM). AV/AB 는 [[efdc_caldisp_postprocess]] 의 Taylor 전단분산 입력이기도 함.
- AV/AB 산출 → 운동량(연직확산)·scalar transport(salinity/temp/sediment) 연직 mixing 에 사용.

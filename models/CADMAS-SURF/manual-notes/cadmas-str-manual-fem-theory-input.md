---
title: "CADMAS-STR(STR3D) 영문 매뉴얼 — FEM 이론(Biot·Newmark·von Mises/Drucker-Prager·MPC)·NASTRAN 입력 (소스 cross-confirm, MUMPS 플래그 stale 적발)"
model: CADMAS-SURF
component: manual-notes
canonical_source: self
verification_method: "CADMAS-STR 영문 2매뉴얼 pdftotext: Manual(18p, 실은 FEMAP 워크플로) + Program Instructions(113p, 실제 이론 §2 p.3-24·Appendix p.100-110). Newmark-β 범위 0.25≤β<0.5(p.5)·Biot u-p eq⑧⑨⑪⑮(p.10-15)·von Mises/Drucker-Prager MATS1 YF(p.35)·MPC 접촉(p.18-24)·Total-Lagrange(Appendix3 p.103-110)·유체압 surface integral(Appendix1 p.100)·NASTRAN bulk card(p.25-51)·KK(21) solver flag(p.52). 소스 cross-confirm: main.f:45(β=1/3)·yfunc.f·Rd_MATS1.f(YF=4→D-P,α=0.07)·m_mumps·pld_cadmas·send_pos. 적발: p.52 flag legend stale(MUMPS=4 누락, PARDISO 주석처리). printed page+file:line."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-24
related:
  - models/CADMAS-SURF/source-analysis/str3d-fem-core-newmark-elasto-plastic.md
  - models/CADMAS-SURF/source-analysis/str3d-linear-solvers.md
  - models/CADMAS-SURF/source-analysis/str3d-contact-and-fluid-coupling.md
---

# CADMAS-STR(STR3D) 영문 매뉴얼 — FEM 이론·입력

> 2 영문 매뉴얼. ⚠️ **"Manual"(18p)은 이론서가 아니라 FEMAP/NASTRAN 워크플로·운영 가이드**(data.bdf 작성·결합·MPMD 실행·data.neu 후처리). **실제 FEM 이론은 "Program Instructions"(113p) §2 Formulation(p.3-24) + Appendix 1-3(p.100-110)**. [소스 STR3D 3노트](../source-analysis/str3d-fem-core-newmark-elasto-plastic.md)와 cross-confirm.

## 1. FEM 정식화 (Program Instructions §2)

- **지배식**(p.3): `∇·σ+ρg=ρü`, 유효응력 `σ′=σ+p·I`(Biot). 반이산 구조계(p.5 eq④): `[M]{Ü}+{F}−{F^p}={R}`, 강성 증분 `{ΔF}=[K]{ΔU}`, `[K]=∫[B]ᵀ[D][B]dV`(p.6). 감쇠 `C₁[M]{U̇}+C₂{Ḟ}`(질량·강성비례, p.7)
- **시간적분 Newmark-β**(p.5): 3-레벨, **β 범위 0.25≤β<0.5**, 중간력 `{F̃}=β{F}_{n+1}+(1−2β){F}_n+β{F}_{n-1}`. 침투해석 별도 α(0≤α≤1, p.12). → 소스 `main/main.f:45 RR(4)=1/3`(=0.333 ∈ [0.25,0.5) ✅)
- **요소**(p.1·28-33): solid CTETRA/CPENTA/CHEXA(1차+2차)·rod CROD·beam CBAR(직사각 단면). penta 전단=MacNeal PENTA memo
- **구성식**(p.6·35): 선형탄성(MAT1) + **bilinear 탄소성**(MATS1, 경화 H′). 항복 **MATS1 YF: 1=von Mises·4=Drucker-Prager**(p.35), AMAT 0=탄성/1=Mises/2=D-P(p.60). ⚠운영: D-P 마찰각 **0.07 하드고정**(FEMAP 입력 무시, Manual A p.5)·beam은 von Mises만. 인장균열 지원
- **지반 Biot 압밀**(§2.1.2 p.10-14): u-p 완전결합. Darcy `ẇ=k(−∇p+ρ_wg−ρ_wü)`(eq⑧)·질량보존 `∇·ẇ=−∇·u̇−C_fwṗ`(eq⑨)·결합계 `[[A_uu,A_up],[A_pu,A_pp]]`(eq⑮ p.15). monolithic(동시) vs separated(staggered, CG 악조건 시) — KK(1) 0/1(p.52). porous 재료(§2.1.5 p.17)=공극만·침투 미해석·압력은 CADMAS 셀 보간
- **접촉**(§2.2-2.5 p.18-24): **MPC** 변환 `{U}=[λ]{Ũ}`·`K̃=[λ]ᵀ[K][λ]`, master/slave 관입투영(삼각면 p.21·사각 centroid node5 p.22·edge·point). **stick-slip 마찰**(정마찰 μ₀·동마찰 μ_d, p.24). 소스는 arctangent 옵션도(KK(96))
- **유체결합**(Appendix1 p.100): CADMAS→STR 표면압 `∫N_i p n dS` 절점력·STR→CADMAS 변형절점위치 `SEND_POS`. **Total-Lagrange 대변형**(Appendix3 p.103-110, 2nd PK 응력·Green-Lagrange·`[K_L]+[K_NL]`, `PARAM,LGDISP=1`)

## 2. 매뉴얼 ↔ 소스 cross-confirm

| 항목 | 매뉴얼(p) | 소스 | 판정 |
|---|---|---|---|
| Newmark-β | 0.25≤β<0.5(p.5) | `main.f:45 RR(4)=1/3` | ✅ |
| von Mises/D-P | MATS1 YF 1/4(p.35) | `yfunc.f`·`Rd_MATS1.f`(YF=4→IYLD=2, α=0.07) | ✅ (D-P 0.07 확인) |
| Biot 지반 ITYP=6 | "Biot's formula"(p.1·10-14) | `ITYP==6` soil(`geo/npflow.f`·`emassmtx.f`) | ✅ |
| MPC 접촉 | §2.2·2.4(p.18-23) | `MPCCORR`·`CONTACT`·`geo/pcnstri.f` | ✅ |
| solver | KK(21) 1=CG·2=ASE·3=PARDISO(p.52)·"Multi-Frontal"(p.1) | `clsindex_s.f` 1=CG·2=ASE·3=PARDISO(주석)·**4=MUMPS(활성)** | ⚠ **p.52 legend stale** — MUMPS(=4) 누락·PARDISO 주석처리. p.1 "Multi-Frontal"=MUMPS가 실제 direct solver |
| 유체압→절점력 | Appendix1(p.100) | `pld_cadmas.f`(LOADTR/QU) | ✅ |
| 변형위치→CADMAS | p.1·14·97·99 | `send_pos.f`(POS) | ✅ |

## 3. 입력 — NASTRAN bulk data (§3 p.25-51)

Case Control → `BEGIN BULK` → Bulk Data. 카드: 절점 GRID·요소 CTETRA/CPENTA/CHEXA·CROD·CBAR + PSOLID/PROD/PBARL·재료 MAT1(E,ν,ρ,K_water,k,n)·MATS1(H,YF)·구속 SPC1/SPC/SPCD·정하중 FORCE/MOMENT/PLOAD4/GRAV·동하중 DLOAD/TLOAD1/TABLED2·접촉 BCTSET/BCTPARA(μ₀/μ_d)/BSURFS·제어 TSTEP·PARAM(LGDISP/W4/EPSC)·CADMAS,PLOWER2. MID<100 일반·≥100 지반재료. **solver flag KK(21)**(MUMPS는 launch `-S` 옵션·메모리 `-M MB` 기본 8000). 해석유형: direct transient(주)+static 초기조건·기하비선형 KK(2)·재료비선형 KK(80)·지반결합 KK(1)·METIS 분할·MPMD.

## 4. 참고문헌 (inline)

Yagawa-Yoshimura(1995, FEM)·MacNeal(1976, PENTA memo)·Yamada(1995, 소성 [D])·**Bathe(1982, FE Procedures)**(Appendix1·3)·Biot 압밀(명명만, source-needed).

> ⚠ 핵심 적발: **solver flag legend(p.52) stale** — MUMPS(KK21=4)가 실제 활성 direct solver인데 표는 PARDISO(주석처리)만 나열. p.1 "Multi-Frontal"이 정확. "Theory manual"(18p)은 실은 워크플로 가이드.

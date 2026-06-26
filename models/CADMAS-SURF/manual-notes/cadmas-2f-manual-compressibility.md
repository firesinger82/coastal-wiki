---
title: "CADMAS-2F 영문 매뉴얼 — 기상 압축성 부록 (EOS·준압축성 Poisson 소스 cross-confirm, /3D 매뉴얼 95% 중복)"
model: CADMAS-SURF
component: manual-notes
canonical_source: self
verification_method: "CADMAS-2F_Manural_English.pdf(160p, 인쇄 p.463-622) pdftotext 추출. Table 0-1-1(p.467-468)·연속식 eq(2.1) 압축성항(p.471)·EOS eq(2.38)(p.485)·Dρ/Dt eq(2.39)(p.486)·압력선형화 Poisson eq(3.127-3.128)(p.522-523)·입력 OPTION STATE(p.603)/MATE 2열 RHO0(p.585)·참고문헌 CDIT Library(12)(p.621). 소스 cross-confirm: user_eos.f·vf_v1eos.f·vf_vpdrdt.f(EOS·Dρ/Dt·Poisson 계수 정확일치). printed page 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-24
related:
  - models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md
  - models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md
---

# CADMAS-2F 영문 매뉴얼 — 기상 압축성

> 번들 `Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf`(160p, 인쇄 p.463-622, "CADMAS-SURF 3D-2F"). **/3D 매뉴얼의 ~95% 중복** + **기상 압축성 부록**(§2.10·§3.3.12·Overview (1)(b)). [소스 2상 노트](../source-analysis/cadmas-2f-twophase-compressible-gas.md)와 식 단위 cross-confirm.

## 1. 동기 (p.463-464)

기존 /3D-2F 는 **비압축** 2상 → 액체로 둘러싸인 고립 기포가 체적변화 불가 → 케이슨 충격·슬래밍 압력 포착 못함. 본 매뉴얼이 **기상 압축효과** 추가. Table 0-1-1(p.467-468)은 여전히 "incompressible" 명시 — 압축성은 부록으로 적층.

## 2. 기상 압축성 식 (cross-confirm)

별도 운동량집합이 아니라 단상 porous-VOF에 **기상 압축성 소스항 `(1-F)/ρ_G·Dρ_G/Dt`** 1개를 연속식·Poisson에 주입:

- **연속식 eq(2.1)(p.471)**: `∂ₓ(γₓu)+∂_y(γ_yv)+∂_z(γ_zw) = γ_vS_φ − (1−F)/ρ_G·ρ̇_G`
- **VOF-F eq(2.7)(p.472-473)**: 불변. 매뉴얼 명시 *"F 는 비압축 유체상의 이류만; 기상 압축효과는 이 식에 안 나타남. 기상 체적변화 = F이류식과 연속식의 차"* — 결합의 개념적 핵심
- **EOS eq(2.38)(p.485)**: `ρ_G = ρ_G(p)` "user function 으로 주어짐"
- **Dρ_G/Dt eq(2.39)(p.486)**: `ρ̇_G = γ_v∂ρ_G/∂t + ∂ₓ(γₓuρ_G)+...`
- **압력선형화 Poisson eq(3.128)(p.522-523)**: `ρ_G^{n+1}=ρ_Gi+(dρ_G/dP)·(P^{n+1}−P^{(i)})`, SMAC 내부반복 `(i)` + 완화계수 RELAX (SIMPLE형)
- **EOS 등온이상기체**(operation default): 입력 `OPTION STATE`(p.603) `ISTATE=1`+PARAM1=p₀·PARAM2=R·PARAM3=T → ρ_G=(p+p₀)/RT. `ISTATE=0`=비압축

### 매뉴얼 ↔ 소스 대조

| 식 | 매뉴얼(p) | 소스 | 판정 |
|---|---|---|---|
| EOS ρ=ρ(p) 등온이상기체 | (2.38) p.485·STATE p.603 | `user_eos.f` `RHOG=(PP+P0)/(RCONS·TCONS)`·`DRHODP=1/(PP+P0)` | ✅ 정확일치 |
| Dρ/Dt 필드 | (2.39) p.486·(3.127) p.522 | `vf_v1eos.f` `DRHODT=(1−F)(dρ/dt)/ρ` 동일 upwind | ✅ 일치 |
| Poisson 압축성 계수 | (3.128) p.523 | `vf_vpdrdt.f` `AD+=AVLT·DRHODP`·`BB+=AVL·DRHODT` | ✅ 정확일치(행렬계수+RHS) |
| 밀도혼합 ρ=F·ρ_L+(1-F)·ρ_G | **부재** | 2열 RHO0(sharp VOF) | ⚠ 매뉴얼은 sharp-interface, 혼합밀도식 없음 |

> **net**: EOS·Dρ/Dt·Poisson 결합은 매뉴얼↔소스 **정확일치**. 단 "혼합밀도"식은 매뉴얼에 없음 — 모델은 sharp VOF + 2열 RHO0(액=1열·기=2열, 기본 1.0, p.585).

## 3. 적발 — sf_* 구조결합이 매뉴얼에 부재

매뉴얼은 구조물을 **고정 porous body**로만 기술(γ_v·C_D·C_M, eq 2.5-2.6 p.471-472), p.608 *"구조물 위치변경 불가(프로그램 미확인)"* 명시. cut-cell/tetrahedron/FSI/可動床/変形 전문검색 = **0 hit**. → [`sf_*` cut-cell FSI 엔진](../source-analysis/cadmas-2f-structure-coupling-cutcell.md)은 **소스에만 존재, 매뉴얼 부재**(매뉴얼이 해당 기능보다 앞서거나 누락). 문서화 갭으로 기록.

## 4. /3D 매뉴얼 대비 신규분 (얇음)

2상 고유 추가 = §2.10(압축성, eq 2.38-2.39, p.485-486) + §3.3.12(Poisson 선형화, eq 3.127-3.128, p.522-523) + Overview(1)(b)(p.463-464) + 입력키워드(OPTION STATE·DENS_ERROR·MATE 2열 RHO0·배열 RHOG/RHOGO/DRHODP/DRHODT). 그 외 Ch2 분석모델·Ch3 이산화·VOF·k-ε·SMAC·조파·무반사는 [/3D 매뉴얼](cadmas-surf3d-english-manual-governing-equations.md)과 동일(인쇄페이지 463-622 = 더 큰 CDIT 문서의 연속 섹션).

## 5. 참고문헌 (Ch6, p.621-622)

CDIT(2001) "Research and development of numerical wave channel" **CDIT Library (12)** · Sakakiyama-Abe-Kajima(1990, porous) · Hirt-Nichols(1981, VOF) · Torrey et al.(1987, **NASA-VOF3D** LA-11009-MS) · Isobe-Nishimura-Horikawa(1978) · Dean(1965, stream-function) · Gueyffier et al.(1999) · Fujino(1991, BiCGSTAB) 외.

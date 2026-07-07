---
title: "SFINCS 침투(강우손실) source-analysis — sfincs_infiltration.f90 (6법: constant/SCS-CN/Green-Ampt/Horton, SWMM 식) + Green-Ampt 인덱싱 버그"
topic: sfincs-infiltration
canonical_source: self
citation_status: verified
verification_method: "SFINCS raw source 직접 read: source/src/sfincs_infiltration.f90(1039) — Green-Ampt rate+★인덱싱버그(:838 loop nm vs :856 GA_head(np)/GA_sigma(np)) file:line 직접 검증. 소스주석 primary SWMM Reference Manual Eq번호 in-code. [[sfincs_boundaries_forcing]] §5 는 survey(~46줄)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — sfincs_infiltration.f90:828-869 직접 read 검증(GA 버그 확인)"
verification_date: 2026-07-07
related:
  - models/SFINCS/source-analysis/sfincs_boundaries_forcing.md
  - models/SFINCS/source-analysis/sfincs_flow_solver.md
  - models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md
---

# SFINCS 침투(강우손실) — `sfincs_infiltration.f90`

> 소스: [`source/src/sfincs_infiltration.f90`](../raw/source_code/sfincs/source/src/sfincs_infiltration.f90) (1039). 호출 init `sfincs_domain.f90:28`·매스텝 `sfincs_lib.f90:538`.
> **정체**: 격자 강우 → 지중침투 손실 → 지표유출(`netprcp -= qinfmap`). **복합침수(surge+rain)의 육상측 driver**. 6법(constant `con`/spatial `c2d`/SCS-CN `cna`·`cnb`/Green-Ampt `gai`/modified Horton `hor`). [[sfincs_boundaries_forcing]] §5(~46줄 survey)만 존재 — 알고리즘 미커버.

## 0. 구조
| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `initialize_infiltration` | 8-604 | type auto-select(:92-135) + 법별 read/할당/단위변환/recovery 상수 |
| `update_infiltration_map(dt)` | 607-1037 | 매스텝 침투율(inftype 분기, OpenMP/ACC) + 공통 `netprcp-=qinfmap`·`cuminf+=qinfmap·dt` |

분기: con/c2d :630·cna :676·cnb :722·gai :828·hor :912. type 자동선택 = 파일존재(qinf→con·qinffile→c2d·scsfile→cna·sefffile→cnb·psifile→gai·f0file→hor, :92-135).

## 1. SCS-CN (cna/cnb)
```fortran
! cna(old): Qq=(P-0.2S)²/(P+0.8S) ; I=P-Qq ; qinf=(I-cuminf)/dt   ! :693-695 (Ia=0.2S, sfacinf=0.2)
! cnb(new) event 상태기계: 강우 onset 시 scs_P1/F1/S1 reset·scs_rain=1(:747) ; scs_P1+=prcp·dt(:756)
inf_kr = √(ks/25.4)/75                       ! :375 recovery 상수 SWMM Eq4-36 (ks mm/hr→in/hr, /75→day)
if( rain_T1 > 0.06/inf_kr ) scs_Se += inf_kr·Smax·dt/3600 (cap Smax)   ! :800-805 SWMM Eq4-37 회복
```

## 2. Green-Ampt (gai) — SWMM Eq4-27 + ★인덱싱 버그
```fortran
do nm = 1, np                                             ! :838 셀 루프
  if( prcp<ks ) qinfmap(nm)=prcp(nm)                      ! :846-850 소량=강우와 동일
  else qinfmap(nm) = ksfield(nm)*(1 + GA_head(np)*GA_sigma(np)/GA_F(nm))   ! :856 SWMM Eq4-27
  GA_sigma(nm) -= qinfmap·dt/GA_Lu(nm)                    ! :863 deficit
  GA_F(nm) += qinfmap·dt                                  ! :867 누적침투
! GA_Lu = 4·√25.4·√ks (Eq4-33 :488), recovery GA_sigma += inf_kr·sigma_max·dt/3600 (Eq4-35 :884)
```
> ⚠ **Green-Ampt 인덱싱 버그(:856, 직접 확인)**: 루프 `do nm=1,np`(:838)인데 흡입수두·수분부족을 **`GA_head(np)`·`GA_sigma(np)`**(=`np`=마지막 셀/총셀수)로 인덱싱, 나머지(`ksfield(nm)`·`GA_F(nm)`·`qinfmap(nm)`)는 `nm`. → **모든 셀이 마지막 셀의 ψ·σ 를 사용**(공간균일 오류, `np`→`nm` 오타 추정). [[sfincs_boundaries_forcing]]:244 는 이 줄을 verbatim 인용하나 결함 미표기.

## 3. Modified Horton (hor)
```fortran
I = exp(kd·rain_T1/3600) ; f = (fc + (f0-fc)·I)/3600/1000   ! :967,979 지수감쇠
! rain_T1 음의시간 누적(침투중 카운트다운, storm onset 시 0 reset, -dt 과소 방지) :955-963
! 용량제한: Qq=prcp·dt+hh_local ; Horton수요 I=qinf·dt>Qq 면 qinf*=Qq/I   :987-1002
! hh_local = subgrid z_volume/cell_area (geo/proj, :930) or zs-zb(비subgrid :940)
```

## 4. 공통 결합
`netprcp(nm) -= qinfmap(nm)`(전분기 :661/707/813/897/1017) + `cuminf += qinfmap·dt`(store 시). **"물 없으면 침투 없음"** guard(subgrid z_volume≤0 or zs≤zb → qinfmap=0, :645-657·946). NetCDF 입력=quadtree 전용·ASCII=정규격자 전용(:170-189).

## 5. 주요 findings
- **★Green-Ampt 인덱싱 버그**(:856 `np` vs 루프 `nm`) — 확인됨, 공간균일 오류. 기존 노트 미표기.
- **cnb dual-S 부기**(:775 주석 "scs_Se 는 계산 미사용"이나 매 강우스텝 감소, 실제 runoff 는 onset 시 frozen `scs_S1` 이 구동 :749) — survey bullet 누락 subtlety.
- **Horton Qq refactor 미결**(:987 주석 `Qq=prcp·dt+(zs-zb)` vs active `+hh_local`, "MvO: using hh_local?").
- **개발자 doubt marker**(:896 주석처리 `qinffield(nm)=qinfmap(nm) ! Really? Why?`).
- **설계 제약**(header :28,30): "침투는 강우 활성 시만 동작"·"침투법 stacking 미설계" → 강우 없이 침투 쓰려면 0.0 precip 파일 필요(gotcha).

## 6. Primary sources
- **Leijnse, Van Ormondt, Nederhoff, De Dominicis 2021** *Coastal Engineering* 163:103796 — SFINCS reduced-complexity 복합침수(침투=강우손실 항, netprcp→continuity). ★headline(Bates2010 마찰·Baldock 는 flow-solver/SnapWave 소관, 침투 무관).
- **SWMM Reference Manual Vol.I Hydrology**(Rossman-Huber, EPA) — ★in-code 식번호 인용: Eq4-27(GA :856)·4-33(:488)·4-35(:884)·4-36(:372/472)·4-37(:800/880). Green-Ampt·recovery 정본.
- **SCS/NRCS Curve Number**(USDA TR-55) — cna/cnb 기반(Ia=0.2S). **Horton 1933/modified(Bras 1990)** — hor.

## 7. 관련
- [[sfincs_boundaries_forcing]] — §5 침투 survey(본 노트가 알고리즘 심화 + GA 버그 표기)
- [[sfincs_flow_solver]] — netprcp 가 연속식으로(Bates 마찰 reduced-SWE)
- [[sfincs_subgrid_quadtree]] — subgrid z_volume(hh_local 산정)·quadtree(NetCDF 입력)

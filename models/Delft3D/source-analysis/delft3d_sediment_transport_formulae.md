---
title: "Delft3D morphology_kernel — Partheniades-Krone(erosilt) + transport formula gateway(eqtran) + skin friction(compbsskin)"
model: Delft3D
component: utils_gpl/morphology/morphology_kernel
canonical_source: self
citation_status: verified
verification_method: "Delft3D morphology_kernel 소스 직접 read (models/Delft3D/raw/source_code/Delft3D/src/utils_gpl/morphology/packages/morphology_kernel/src/). erosilt.f90(269줄) 전체 + eqtran.f90(834줄) iform dispatch + compbsskin.f90(312줄) Function 직접 인용. 식·파라미터·iform 코드 verbatim. [`delft3d_sediment_morphology.md`](delft3d_sediment_morphology.md)(compute_sediment 커널)가 이 식들을 호출 — erosilt@erosed.f90:1074·eqtran@erosed.f90:1221·compbsskin@erosed.f90:880."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - models/Delft3D/source-analysis/delft3d_sediment_morphology.md
  - models/Delft3D/web-refs/delft3d-official-resources.md
  - concepts/sediment-transport/04-code-and-tools.md
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
---

# Delft3D morphology_kernel — 침식/퇴적 식 본체

> [`delft3d_sediment_morphology.md`](delft3d_sediment_morphology.md)(compute_sediment 커널)가 호출하는 **실제 식 라이브러리**. 경로: `src/utils_gpl/morphology/packages/morphology_kernel/src/`. cohesive=`erosilt`, non-cohesive=`eqtran`(gateway), skin friction=`compbsskin`.

## 1. erosilt.f90 — Partheniades-Krone (cohesive mud, 269줄)

`erosed.f90:1074` 가 mud fraction 마다 호출. **iform** 으로 식 선택:

| iform | 식 |
|---|---|
| **−3** | Default **Partheniades-Krone** (`erosilt.f90:160`) |
| 21 | user-defined DLL (`perf_function_erosilt`, `:204-247`) |
| flmd2l | 2-layer fluid mud (`:145`, entrainment `entr`=par(11)) |

### 1.1 침식 flux (Partheniades, `:183-184`)

```
taum = max(0, taub/tcrero − 1)        ! 무차원 초과전단 (:183)
sour = eropar · taum**powern          ! 침식 entrainment flux [kg/m²/s] (:184)
```

- `taub` = (파 enhanced) bed shear stress [N/m²], `realpar(RP_TAUB)` (`:130`)
- `tcrero` = 침식 임계전단 [N/m²] = par(13)
- `eropar` = 침식률 파라미터 M [kg/m²/s] = par(11)
- `powern` = 지수 = par(18) (표준 Partheniades-Krone = 선형 powern=1)

### 1.2 퇴적 flux (Krone, `:195-203`)

```
sink = max(0, 1 − taub/tcrdep)        ! 무차원 퇴적확률 (:197)
```
- `tcrdep` = 퇴적 임계전단 = par(12). `depeff`(par(17))=−1 이면 위 Krone 식, 아니면 `sink=max(0,min(depeff,1))` (`:202`).
- `wstau = ws(num_layers_grid) · sink` (`:262`) — 침강속도 × 퇴적확률.

### 1.3 Bed-slope 효과 (`:172-181`)

주변 velocity 점 최대경사 `maxslope`>`wetslope` 시 침식 임계전단 **선형 감소**:
```
taucrmin = 0.1 ;  betaslope = 2.0       (:177-178)
tcrero ← 경사 보간 후 max(tcrero, taucrmin)   (:179-180)
```
→ 가파른 사면일수록 더 쉽게 침식(사면 안정).

### 1.4 Fluff layer 침식 (`:188-193`)

```
taum       = max(0, taub − tcrflf)                    (:189)
sour_fluff = min(mflufftot·parfl1, parfl0) · taum     (:190)
```
- `tcrflf`=par(14) fluff 임계전단, `parfl0`=par(15) 0차율, `parfl1`=par(16) 1차율, `mflufftot`=fluff 총질량.

### 1.5 가용량 제한 + 출력 (`:253-268`)

```
sour = fixfac · frac · sour            ! 분율 frac + 공급제한 fixfac (:257, oldmudfrac면 frac 생략 :254)
sour = min(sour, srcmax)               ! 상한 (:264)
sourse  = sour / thick0                ! → erosed sourse(nm,l)  (:267)
sinktot = wstau / thick1               ! → erosed sinkse        (:268)
sourf   = sour_fluff / thick0          (:266)
```

→ EFDC SEDZLJ([[../../EFDC/source-analysis/sediment/efdc_sedzlj]]) 의 Sedflume power-law vs Delft3D 의 **Partheniades-Krone**(`τ/τ_cr−1` 선형) 대비.

## 2. eqtran.f90 — transport formula gateway (non-cohesive sand, 834줄)

`erosed.f90:1221`(3D) / `:1304`(2D) 호출. 헤더 자칭 **"Gateway for all sediment transport formulations"**(`eqtran.f90:2`). `iform` 으로 분기:

| iform | routine | 식 (소스 주석 verbatim) |
|---|---|---|
| **−1** | `tram1` | **van Rijn 1993** (analytical 1984/1993/2004, `:292`) |
| **−2, −4** | `tram2` | **van Rijn 2004** (TRANSPOR2004) |
| 1 | `tranb1` | **Engelund-Hansen** (`:353`) |
| 2 | `tranb2` | **Meyer-Peter-Müller** (`:362`) |
| 3 | `tranb3` | **Ackers-White** (`:371`) |
| 4 | `tranb4` | general bed/total load |
| 5 | `tranb5` | **Bijker** (`:389`) |
| 7 | `tranb7` | van Rijn 1984 계열 |
| 11 | `trab11` | **Soulsby & Van Rijn** (`:470`) |
| 12 | `trab12` | **Soulsby** (`:480`) |
| 13 | `tran9t` | test transport (Wang) **Fredsøe** (`:491`) |
| 14 | `trab14` | generalized **Ashida & Michiue** (`:500`) |
| 15 | DLL | user-defined formula in DLL (`:575-577`) |
| 16 | `trabwc` | **Wilcock & Crowe** (`:509`) |
| 17 | `trabwc2` | Modified **Wilcock & Crowe** (`:518`) |
| 18 | `trabg` | **Gaeuman et al.** (W&C 발전, `:527`) |
| 19 | `trab19` | **van Thiel / Van Rijn (2008)** (`:536`, equi_conc) |
| 20 | `trab20` | **Soulsby / Van Rijn — XBeach adaptations** (`:551`, equi_conc) |
| 22 | `asmita` | **ASMITA** (`:566`, 장기 형태 aggregated) |

- 각 호출은 `sbc_total`/`sus_total`(bed/suspended 합산 여부) 플래그 설정 (예 `:496-497`). iform 19/20/22 는 `equi_conc`(평형농도) 방식(`:538`,`:553`,`:574`).
- 출력: bed load + suspended (reference concentration / suspended transport rate, `:753-827`). suspended 분은 advection-diffusion(`difu`)로, bed load 는 직접 bed 갱신.
- van Rijn(1993/2004) 식만 reference concentration + suspended rate 모두 산출(`:753`,`:802`); 타 식은 bed/total load 위주 → 후처리 개별 가산(`:661`,`:827`).

## 3. compbsskin.f90 — muddy bed skin friction (312줄)

`erosed.f90:880` 호출. **Soulsby (2004)** muddy/silt bed 의 skin-friction τ 계산(`compbsskin.f90:82-83`):

- silt/sand 혼합 bed 의 skin shear stress `taumax` 산출(`:115`).
- 상수: **ar = 0.26, as = 0.22** (Soulsby 원논문, `:90`).
- `kssilt`/`kssand` roughness — 다중 mud fraction 각각 부여 여부는 미해결(`:95` 저자 주석).
- 모델 전역에서 skin friction 계산·사용(`:86`).

→ erosilt 의 `taub` 입력이 이 skin shear. 즉 **total bed shear 가 아니라 skin friction** 으로 cohesive 침식 구동(form drag 제외).

## 4. 본 위키 접점

- [`delft3d_sediment_morphology.md`](delft3d_sediment_morphology.md) — 이 식들의 **호출자**(compute_sediment 커널): erosilt@1074·eqtran@1221·compbsskin@880.
- [`web-refs/delft3d-official-resources.md §3.1`](../web-refs/delft3d-official-resources.md) — Lesser 2004 canonical.
- [`concepts/sediment-transport/04-code-and-tools.md`](../../../concepts/sediment-transport/04-code-and-tools.md) §3 Delft3D-SED.
- [[../../EFDC/source-analysis/sediment/efdc_sedzlj]] — EFDC cohesive(Sedflume) vs Delft3D(Partheniades-Krone) 대비. 둘 다 van Rijn 비점착 식 공유.

## 5. 미보강 (TODO)

- 개별 transport routine(`tram1`/`tram2`/`tranb*`/`trab*`) 식 verbatim — 각 morphology_kernel 파일 별도.
- van Rijn 2004(TRANSPOR2004) reference height `aks`·suspended profile 식 deep.
- `bedcomposition_module` graded sediment 다층 bed 진화.
- compbsskin ar/as·kssilt/kssand 다중 fraction 처리(저자 미해결 주석 `:95`).

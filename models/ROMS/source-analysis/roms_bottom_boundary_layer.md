---
title: "ROMS bottom boundary layer (BBL) — wave-current 저면응력 3 scheme: SSW(Sherwood-Signell-Warner, Madsen94 + moveable ripple roughness) / MB(Meinte Blaas) / SG(Styles-Glenn). bustrc/bustrw/bustrcwmax → sediment·momentum"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/BBL/ 직접 read — bbl.F dispatcher(SSW/MB/SG CPP, 16-21) + ssw_bbl.h(1849, madsen94 PRIVATE, bustrc/bustrw/bustrcwmax, ripple roughness zoBF=ar·rheight²/rlength Grant-Madsen1982 ar=27.7/30 또는 Nielsen1992 0.267) + mb_bbl.h(730)/sg_bbl.h(1149) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 3 BBL scheme·Madsen94 결합응력·ripple roughness verbatim"
verification_date: 2026-06-03
related:
  - models/ROMS/source-analysis/sediment/roms_sediment.md
  - models/ROMS/source-analysis/roms_wec.md
  - models/ROMS/source-analysis/roms_vertical_mixing.md
---

# ROMS bottom boundary layer (BBL) — wave-current 저면응력

> `ROMS/Nonlinear/BBL/` 직접 read. **파+흐름 결합 저면응력(combined wave-current bottom stress)** 계산 모듈 — 단순 quadratic/log drag([[roms_vertical_mixing]] BBL 외 경우) 대신, 파동 궤도운동이 증폭한 bed shear 를 산출. **sediment 침식 임계의 핵심 입력**([[sediment/roms_sediment]]). 파동 입력은 [[roms_wec]]/wave model.

## 1. 3 scheme dispatch (bbl.F:16-21)

```fortran
#if defined SSW_BBL    → ssw_bbl.h   ! Sherwood-Signell-Warner (가장 완전, sediment 권장)
#elif defined MB_BBL   → mb_bbl.h    ! Meinte Blaas
#elif defined SG_BBL   → sg_bbl.h    ! Styles-Glenn 2000
```
- 공통 출력: `bustrc/bvstrc`(current bed stress) · `bustrw/bvstrw`(wave bed stress) · **`bustrcwmax/bvstrcwmax`(max combined wave-current stress)**. 입력: `Ubot/Vbot`(저면 파 궤도속도), `Ur/Vr`(reference 높이 흐름), `Ab`(궤도 excursion), `Tbot`(파주기), `ZoBot`(배경 roughness).

## 2. SSW (Sherwood-Signell-Warner) — madsen94 ★

ssw_bbl.h(1849)가 **Madsen 1994 wave-current BBL**(`madsen94` PRIVATE) 사용:
- 파+흐름이 같은 BBL 을 공유 → 비선형 상호작용. 산출: `ustrc`(current shear velocity) · `ustrw`(wave) · `ustrcwmax`(최대 결합) · apparent roughness `zoa` · wave BL 두께 `dwc`.
- **결합 원리**: 파동이 얇은 BBL 에서 큰 응력 → 흐름이 느끼는 apparent roughness 증가(파가 흐름을 "거칠게"). 최대 결합응력 `τ_cwmax` 이 sediment 침식 구동(순간 peak).

### 2.1 Moveable bed roughness (ssw_bbl.h:487-530)
bottom roughness `z0` = 3 성분 합:
- **skin friction** `z0N`(입경 grain, ~D50/12).
- **bedform/ripple** `zoBF = ar·rheight²/rlength`(:510): `ar=27.7/30`(Grant-Madsen 1982) 또는 `0.267`(Nielsen 1992). ripple height/length 는 ripple predictor(coef_a2=0.442) 또는 `bottom(:,:,irhgt/irlen)`.
- **bedload** `z0BL`(이동층 roughness).
→ moveable bed(파/흐름이 ripple 형성 → roughness 변화 → 응력 feedback). SSW_LOGINT 옵션 시 log-layer 보간.

## 3. MB / SG scheme

- **MB**(Meinte Blaas, mb_bbl.h 730) — Madsen 계열 단순 결합 BBL.
- **SG**(Styles-Glenn 2000, sg_bbl.h 1149) — 성층(stratified) 고려 wave-current BBL(`sg_ab/abokb/chi` 등 Styles-Glenn 파라미터). 외해 성층 BBL 에 적합.

## 4. 결합 — momentum & sediment

- **momentum**: BBL 산출 current 응력 `bustrc/bvstrc` 가 [[roms_baroclinic_3d]]/[[roms_barotropic_2d]] 의 bottom drag 항으로(단순 log/quadratic drag 대체).
- **sediment**([[sediment/roms_sediment]]): **`bustrcwmax`(max wave-current stress)** 가 Shields 임계 초과 판정·erosion flux 구동. 파동이 있으면 평균류만으로는 못 움직일 sediment 도 침식(surfzone/shelf 핵심). ripple roughness ↔ sediment bedform 양방향.
- **wave 입력**: `Ubot/Ab/Tbot` = wave model([[roms_wec]] WEC 또는 외부 SWAN) 의 저면 궤도운동.

## 5. 한계·범위

- 본 노트 = 3 scheme + SSW madsen94/roughness 구조 레벨. madsen94 반복해(iteration)·SG Styles-Glenn 식 line-by-line 은 후속.
- BBL 미정의 시 [[roms_vertical_mixing]] 의 단순 bottom drag(logarithmic/linear/quadratic, Zob).

## 6. 연결

- [[sediment/roms_sediment]] — `bustrcwmax` → Shields 임계·erosion (BBL 의 주 소비자)
- [[roms_wec]] — 저면 파 궤도속도 Ubot/Ab 입력
- [[roms_vertical_mixing]] — BBL 외 단순 bottom drag(Zob log-layer)
- [[roms_baroclinic_3d]] / [[roms_barotropic_2d]] — bottom stress → momentum
- Madsen 1994 / Grant-Madsen 1982 / Nielsen 1992(ripple) / Styles-Glenn 2000 / Sherwood-Signell-Warner / Wiberg-Sherwood

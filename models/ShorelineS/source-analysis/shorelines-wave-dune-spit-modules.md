---
title: "ShorelineS 파랑·사구·스핏/월류·mud 모듈 — 회절 Kd 2공식·Larson 사구침식·overwash 광선법"
model: ShorelineS
component: functions/wave_diffraction*.m, dune_erosion.m, find_overwash_mc.m, transport_mud.m, tide_1d_ana_anycomp.m
canonical_source: self
citation_status: verified
verification_method: "sha 7bf4481ab — wave_diffraction.m 헤더+wave_diffraction_coeff.m 84줄 전문·dune_erosion.m 152줄 헤더+runup 분기·find_overwash_mc.m 206줄 헤더+핵심부·transport_mud.m/tide_1d_ana_anycomp.m 헤더 직접 read. 미정독 잔여(회절 기하 928줄 본문 등)는 §4 disclosed."
note_author: "Claude Fable 5"
note_date: 2026-07-17
related:
  - models/ShorelineS/source-analysis/shorelines-transport-formulations.md
  - models/ShorelineS/source-analysis/shorelines-coastline-change.md
---

# 파랑·사구·스핏·mud 모듈

## 1. 회절·투과 (`wave_diffraction.m` 928줄 + `wave_diffraction_coeff.m`)

- 대상: groyne·이안제·revetment 배후(헤더 :4-8). 선택지 2×2: **Kd 공식 `kdform`='Kamphuis'|'Roelvink'** × **방향처리 `wdform`='Roelvink'|'Dabees'**.
- **Kd 공식**(`wave_diffraction_coeff.m:59-77`):
  - Roelvink형: `kd = 1 − exp(−|(0.5/ω_x)⁴|)`, ω_x=(ω+90)/180 — 매끄러운 지수형(:61-66).
  - Kamphuis형: 구간식 — ω<−86.25° → 0 / [−86.25,0] → `max(0.69+0.008ω, 0)` / (0,40] → `0.71+0.356686·sin ω` / (40,90] → `min(0.83+0.17·sin ω, 1)` (:70-76).
- **방향분산 결합**(:44-57, :79-81): Dabees 모드는 −50°:5°:50° 섹터를 방향분산 확률(`get_dirspr_prob`)로 가중, **에너지(제곱) 재결합** `kd=√(Σ kdi²·prob)`(:80-81); Roelvink 모드는 평균방향 단일성분.
- **투과**(헤더 :22-28): 이안제 3공식 `transmform`='angr'(d'Angremond)|'gent'(Van Gent)|'seabrhall'(Seabrook-Hall) — 마루고·마루폭·사면경사·armour d50 입력.

## 2. 사구 침식·성장 (`dune_erosion.m` 등)

- **Larson 계열 충격식**(헤더 :4-6: "formulation of Larson et al."): 침식은 runup 이 dune foot 을 넘을 때, 계수 cs(+점토층 cstill·xtill·perctill 지원 — till 층 반영).
- **runup 공식 분기**(:82-85+): `runupform` = 'sto' → **Stockdon**: `R = runupfactor·1.1·√(HsL0)·(0.35β+√(0.563β²+0.004)/2)`(:84 verbatim) / 'gho' → Ghonim 계열 / (기타).
- 산출 qs(총 침식)·qss(모래분)·ql(측방)·qw(바람 되돌림) → coastline_change:325 에서 해빈 결합, `dune_growth`(바람 공급)·`dune_flux` 별도.

## 3. 스핏/배리어 월류 (`find_overwash_mc.m` 206줄)

- **광선(transect)법**(헤더 :4-10): 각 해안점에서 파향 방향 transect 를 쏘아 타 해안요소와 교차 검사 → 배리어 배후까지 거리 = 배리어 폭.
- 폭 산정: 법선 방향 `spitwidth` 길이 탐색선(:86-87), 최소거리(:118) → **equilibrium `spitwidth` 미만이면 월류 발동**, 침식분을 배후측 점 2개에 거리가중(`1−d/spitwidth`) 분배(:121-122) — Ashton-Murray(2006) 최소 배리어폭 개념의 벡터판(논문 p.5 Overwash 절 대응).

## 4. mud 해안·조석 (헤더 검수 — deep 후속)

- `transport_mud.m`(200줄): 조석·파랑·바람 **연안 수량수지 기반 농도** → mud 수송·해안선 변화 + 갯벌 Bf/맹그로브 Bm/개척 Bfm 폭 변화율(헤더 :4-8). SWAN 등과 달리 점착성 해안 지형진화를 one-line 레벨에서 내장한 드문 사례.
- `tide_1d_ana_anycomp.m`(92줄): 임의 분조(진폭 eta·위상 phi·연안파수 k·연안경사 ss)의 **해석적 1D 조류 프로파일**(h[nx,nt]·vt[nx,nt]) — TIDEPROF transport 의 유속원(transport.m:208-212).
- ~~미정독 잔여~~ → **종결 라운드(2026-07-18)에서 전량 소진**: 회절 기하 파이프라인·mud 전문·위상 처리 3파일·잔여 C티어 12파일 커버리지 판정 = [shorelines-diffraction-mud-topology](shorelines-diffraction-mud-topology.md).

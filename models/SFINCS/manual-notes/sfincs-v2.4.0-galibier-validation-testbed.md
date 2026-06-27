---
title: "SFINCS v2.4.0 Galibier 테스트베드 검증 카탈로그 — 77 케이스(구현22·검증21·응용34) 3티어 regression/skillbed"
model: SFINCS
component: manual-notes (validation)
canonical_source: self
verification_method: "SFINCS v2.4.0 Galibier 공식 testbed report (Windows, 180p, Deltares 2026-06-15) pdftotext 추출. Status Overview(p.3-4: 77/77 PASS·34 WARNING)·Reader's guide 3티어(p.6)·구현 22(p.7-37)·검증 21(p.38-108)·응용 34(p.108-179). 케이스별 명칭·티어·프로세스·RMSE(이전버전 대비) printed page 인용. ⚠ regression/skillbed(RMSE 대부분 release-vs-prior, 데이터 대비 아님)·cross-model 벤치 없음. 문서제목+page 인용(/mnt/e 경로 미사용)."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-27
related:
  - models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md
  - models/SFINCS/source-analysis/sfincs-architecture-source-map.md
  - models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md
  - models/SFINCS/source-analysis/sfincs_snapwave.md
---

# SFINCS v2.4.0 Galibier 테스트베드 검증 카탈로그

> SFINCS(Super-Fast INundation of CoastS, Deltares 감압물리 compound-flooding) v2.4.0 "Galibier" 공식 **testbed report**(Windows·Docker CPU 2판 각 180p, 2026-06-15 자동생성). 위키 SFINCS [소스 감사](../source-analysis/sfincs-architecture-source-map.md)의 **검증 증거** 보완. 인용: "SFINCS v2.4.0 Galibier testbed report (Windows), p.N".
>
> ⚠️ **성격(caveat)**: 동료심사 검증논문이 아니라 **regression/skillbed 자동리포트** — 각 케이스를 **직전 stable 버전**(v2.3.0 mt.Faber·v2.2.0 col d'Eze)과 비교, 관측데이터는 일부만(p.5). 표의 RMSE 대부분 **release-vs-prior 차이**(near-0 1e-10은 버전差, skill 아님). **cross-model(XBeach/Delft3D-FM) 벤치 없음**. 결론 챕터 없음(Status Overview pp.3-4가 헤드라인).

## 결과 요약 (Status Overview, p.3-4)

- **77/77 시뮬 PASS (100%)**, **34/77 WARNING(44%)** = 추적 출력이 직전 release 대비 2% 임계 초과(failure 아닌 regression 플래그)
- 3티어(p.6): **구현(implementation) 22**(p.7-37) → **검증(verification) 21**(p.38-108) → **응용(application) 34**(p.108-179)

## 티어1 — 구현 (기능 단위, 22, p.7-37)

| 그룹 | 케이스 | 프로세스 |
|---|---|---|
| 격자 | bathtub·bathtub_snapwave(quadtree flood-fill) | quadtree |
| 구조물 | controlled_gates(±0.5m sill 이동게이트)·Drainage_culvert·Drainage_pump(WARN 0.031)·Thin_dam_and_{culvert,weir} | gate/culvert/pump/weir/thin-dam |
| 경계 | downstream_outflow_{with,no}_distance(normal-flow BC, river 1500m) | outflow BC |
| **침투 6** | constant_{uniform,varying}·curvenumber_{constant,recovery}(SCS CN A/B)·greenampt·**horton**(Modified Horton) | infiltration 스킴 6종 |
| **조파(wavemaker)** | IG_plus_incident(WARN 0.086)·onlyIG·onlyincident·fromtimeseries | SnapWave incident+IG 1D flume |
| subgrid | storage_volume_{qt_sbg,sbg}_thd2 | subgrid storage |

## 티어2 — 검증 (해석/실험실, 21, p.38-108)

| 케이스 | 범주 | 검증대상 | p |
|---|---|---|---|
| Bates1D | schematic | 수평바닥 흐름(Leijnse 2018) | 40 |
| **Carriergreenspan**(+advection) | **해석해** | 파처오름 Carrier-Greenspan 무마찰 해석해(Leijnse 2021) | 41·43 |
| **DamBreakWet1D_paper** | **해석해** | 습윤바닥 댐브레이크·이류개선(Stelling 2003·Cui 2013) | 44 |
| EAtest2·EAtest5 | schematic | UK Env. Agency 벤치(egg-box 2000m·현실범람) | 45·47 |
| Globex_A1/A2/A3 | **실험실** | barred beach incident+IG 파고·setup(GLOBEX flume) | 50-56 |
| Lijnbak(+thin·no_neumann) | 실험실/schem | SnapWave 내부 파성장·BC 효과 | 59-64 |
| **Wu_01-07 with_vegetation**·**Wu_08-14 without** | **실험실** | SFINCS-SnapWave vs Wu&Ozeren flume Hm0/Hm0,ig/setup, **식생 유/무** 각 7조건 | 67-108 |

## 티어3 — 응용 (실세계, 34, p.108-179)

핵심 케이스(태풍·복합범람·IG파 reef·조석):
| 케이스 | 강제력 | 도메인 | p |
|---|---|---|---|
| Asheville | Hurricane Helene 2024 강우 두부범람·subgrid(5일, 1475s≈25분) | NC | 111 |
| Harvey_subgrid_500m | Hurricane Harvey 2017 강우(500m subgrid, 13.3s, 6 관측 비교: 5/6 재현·obs9 과소) | Houston | 111 |
| Jacksonville(+advection) | Hurricane Irma 2017 **복합**(fluvial+pluvial+tidal+wind, 914s) | FL | — |
| Charleston | Hurricane Hugo 1989 surge | SC | — |
| Comoros_Kenneth | Cyclone Kenneth 2019 복합 wave-surge(SFINCS-SnapWave·parametric best-track) | Comoros | — |
| Hernani2D(+advection) | Typhoon Haiyan 2013 fringing reef IG파 범람 | 필리핀 | — |
| Duck_SnapWave_IG(+risingWL)·Outerbanks_quadtree·Roi_Namur·Wrightsville | SFINCS-SnapWave IG파 runup(reef flat·quadtree) | NC·Kwajalein | — |
| Dike_breaching_Denmark_1999 | 폭풍 복합 surge + polder/제방 breach | Denmark | — |
| Zeeland_SnapWave | 2013 폭풍 surge+wave, Oosterschelde 가동방파제(drainfile) | NL | ~177 |
| StJohns_river_tide(+subgrid) | 조석전파 >100km(regular vs subgrid 대조) | FL | — |
| Puget_Sound 2009·2020·US_southeastcoast_TC_spherical·Philippines_storm_surge | 조석·구면격자 TC·기압 surge | — | — |
| Hills_and_mountains | 급경사+대량강우 안정성 시험 | synthetic | — |

## 검증 모드 커버리지 (p.3-4·109)

- **격자**: regular(StJohns) / **subgrid**(storage·Harvey·Asheville·Bahamas·StJohns) / **quadtree**(bathtub·Outerbanks·Roi Namur·Bahamas) / **구면**(US SE coast TC)
- **SFINCS-SnapWave 파 결합**(IG 포함): wavemaker·Wu×14·Lijnbak·Duck·Outerbanks·Roi Namur·Comoros·Denmark·Zeeland — [source snapwave](../source-analysis/sfincs_snapwave.md)
- **강우+침투 6스킴**(CN A/B·Green-Ampt·Modified Horton·constant)·**구조물**(게이트·weir·thin dam·culvert·pump·이동방파제)·**이류 on/off 토글**(C-G·dam-break·Hernani·Jacksonville)

## 기준·성능

- **해석해**: Carrier-Greenspan runup·댐브레이크(Stelling 2003). **벤치**: Bates·UK EA·GLOBEX·Wu&Ozeren·Lijnbak. **관측**: Harvey(USGS+115 HWM, 6 시계열만 평가)·Charleston·Bahamas
- **성능("super-fast" 정성근거)**: 다일·대륙규모 복합사건이 분단위 — Asheville 5일 1475s·Harvey 500m subgrid 13.3s·Jacksonville Irma 914s. 단 **명시적 모델대비 속도배수 없음**(감압물리 self-evidence)

> canonical 활용 주의: (a) RMSE = release-vs-prior(skill-vs-data 아님) (b) 진짜 관측비교는 일부만 (c) cross-model 벤치 없음 (d) 일부 기준데이터 "preliminary"(Philippines). 검증 *범위*(케이스 다양성·모드 커버리지)는 신뢰, 정량 skill은 원리포트 케이스별 확인 필요. v2.4.0 변경 → [changelog 노트](sfincs-v2.4.0-galibier-changelog-known-issues.md).

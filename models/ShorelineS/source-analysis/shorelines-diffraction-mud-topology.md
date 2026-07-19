---
title: "ShorelineS 종결 라운드 — 회절 기하 파이프라인(rotfac 0.8 XBeach 보정)·mud 농도수지 전문·위상 처리 3파일·C티어 커버리지 판정"
model: ShorelineS
component: functions/wave_diffraction.m(본문), transport_mud.m(본문), merge_coastlines_mc.m, make_sgrid_mc.m, prepare_grid_groyne.m + 잔여 C티어 12파일
canonical_source: self
citation_status: verified
verification_method: "sha 7bf4481ab — wave_diffraction.m 928줄 섹션 전수(%%) + 핵심부(:105-118 회전상수·:316-385 기하/om·:860-883 평활) 직접 read / transport_mud.m 계산부(:83-199) 전문 / merge_coastlines_mc·make_sgrid_mc·prepare_grid_groyne 섹션 구조+핵심 로직 / 잔여 12파일 헤더 전수 스윕. ※파일 인코딩 ISO-8859+CRLF(grep -a 필요)."
note_author: "Claude Fable 5"
note_date: 2026-07-18
related:
  - models/ShorelineS/source-analysis/shorelines-wave-dune-spit-modules.md
  - models/ShorelineS/source-analysis/shorelines-coastline-change.md
  - models/AUDIT-LEDGER.md
---

# 종결 라운드 — 잔여 소진

## 1. wave_diffraction.m 기하 파이프라인 (928줄 본문)

섹션 순서(%% 마커 전수): 구조물별 회절점(tip) 결정(:162 — 좌/우 tip :203/:227, revetment 은 양끝점만 :241, 원거리 구조물 제거 :290) → 각 transport 점에서 tip 까지 각도 φtip·영향각 ω 계산(:316-340, groyne 은 구조물 방위 기준 별도식) → **방향 회전 om**(:367-374) → **Kd**(:377-384, [wave_diffraction_coeff](shorelines-wave-dune-spit-modules.md) §1) → 수중 breakwater 투과 결합(:386-438) → 영향구역 판정(:440)·타 구조물에 가린 tip 차폐(:476)·모델 밖 구조물은 최근접만(:554) → **구조물 사이 gap 보정**(:599-651) → 측면별 지배 구조물 1개 채택(:652) → 해안이 회절점을 '볼 수 있는지' 차폐 검사(:696-761) → 이안제 한정 극사각 입사 감쇠(:781) → 영향구역 경계 gradient 완화·`diffsmooth` 평활(:860-869) → 출력 `PHItdp−om`(nautical 부호)·`HStdp·min(kd,1)`(:880-883).

- ★**회전계수 보정 실측**(:105-118 + :370-372 주석): `rotfac=0.8` — 주석 verbatim "rotfac (=2 according to Hurst et al, but **0.8 according to comparison with wave-resolving XBeach model**". 방향분산 블렌딩 `alfa=clamp(dirspr−12,0,32)/20`, 경계 오프셋 omegat −20°(장파봉)~−35°(단파봉), 회전 상한 `maxanglerotation`. wdform 이 Dabees/Hurst/Kamphuis 면 omegat=0·rotfac=1(:115-118 — 회전 보정은 Roelvink 방향모드 전용).
- om1/om2 는 영향구역 경계에서 0(연속), om3=0(투과파는 방향 불변 가정, :375).

## 2. transport_mud.m 전문 (:83-199)

1. **연안 유량**: 단면적 `A=0.5·B·d`(:120), 구동력 = 풍응력 `ρa·Cd·U²·sin(φc−φw)` + 파랑 `Fws=ρw·g/32·HS²·sin(2φ)/B`(:122-123) vs 마찰 `ρw·cf·v·max(v,urms)` — v 를 2차방정식 근으로 해석적 해(:124-126, urms=√(g/8d)·HS :119), `Q=A·v`.
2. **정상 농도수지**(:128-156): upwind 이류 + 침강 `w·B` + 맹그로브 흡수 `qmoverC` 를 3중대각으로 조립(Q 부호 4분기), 소스 `r=M·B·max(τ−τcr,0)/τcr + qriv`(:152, τ=cf·ρw·max(vm,urms)² :151), 양끝 무경사 BC(:154-155) → `tridiag` 해(:156) → 음수농도 경고 후 0 클램프(:157-160).
3. **폭 동역학**(:174-193): `QS=upwind C·Q/ρs·spyr` → `dndt_mud=(−dQs/ds−qm+qriv)/d`·맹그로브 `dBm/dt=2qm/dm`·개척 맹그로브 완화 `(Bf−Bfm)/Tfm`·Bf=0 특수분기 2종. 맹그로브 유입 = 조석 프리즘 `P=(0.5Bm+Bfm)(MHW−MSL)` 기반 `qmoverC=700/spyr·P·clamp((Bf−Bfcrit)/Bfcrit,0,1)`(:116-117 — 계수 700 하드코딩).
- 관찰: `HStdp(|φ|>90°)=0.1`(:118) — 모래식(0 처리)과 달리 잔존 0.1 m 부여.

## 3. 위상 처리 3파일

- **merge_coastlines_mc.m**(690줄): 섹션 쌍별(i_mc×j_mc) `get_intersections` 교차 탐지(:138) → cyclic/open·시계방향(`get_clockpoly` — cw=1 해안·cw=0 호수) 판별(:91-98)·폐합 보정·cyclic↔open 스위칭 후 병합. 자기교차(스핏 핀치오프→분리)는 쌍둥이 `merge_coastlines.m:64` 가 단일 섹션 `get_intersections(x,y)` 로 처리.
- **make_sgrid_mc.m**(302줄): regrid 2방법 — METHOD 1(:87) 임계 초과 셀만 분할/병합(저확산·국소 세분 가능·덜 매끄러움), METHOD 2(:169) 전체 재생성(매끄러움·확산↑, 기본값 — FAQ 대조 `S.griddingmethod=2` 기본). cyclic·clockwise 판정(:231-297) 후 x_mc 재삽입.
- **prepare_grid_groyne.m**(408줄): 구조물-해안 교차점 삽입(:106, Ghonim 기여 주석)·교차마다 해안선 분할 + groyne 교차 저장(:122) — PHASE 0 의 본체.

## 4. 잔여 C티어 커버리지 판정 (헤더 전수 스윕, 12파일)

| 파일(줄) | 내용(헤더 verbatim 요지) | 판정 |
|---|---|---|
| wave_refraction(110) | 외해→nearshore 굴절, 옵션 3(CERC 는 외해 직사용) | ✅ 커버(개념 단순·transport 노트 §1 입력 계보와 정합) |
| wave_shoalref(69)·wave_breakingheight(130) | 천수+굴절 파고 변화·TDP→쇄파점 재굴절(Sphimax 가 반복 호출) | ✅ 커버 |
| wave_transmission(100) | 투과 3공식 본체 | ✅ 커버(회절 노트 §1 결합부 확인) |
| transport_bypass(180) | groyne 향 수송 시 우회율 | ✅ 커버(coastline_change §2 분배와 연동) |
| transport_soulsbyvanrijn(83) | Soulsby-van Rijn 모래식(주 trform 분기 밖 보조) | ✅ 커버 |
| dune_growth(91)·dune_flux(203) | 비사(aeolian) 성장·침식/성장 통합 | ✅ 커버(사구 노트 §2 산출항과 정합) |
| move_channel(240)·prepare_delta(88) | 수로 폭 유지 강제(둘레 따라 해측 압출)·delta 구조 준비 | ✅ 커버(개요 수준 — 심층은 사용 시) |
| get_fnourishment_diffusion(43) | shoreface 양빈 확산계수(네덜란드 개방해안 유도) | ✅ 커버 |
| introduce_climatechange(116) | 시점별 기후 보정(SLR 등) | ✅ 커버 |

- S티어(prepare_*/get_* 유틸·plot 7종·save/IO·readkeys 등 ~90파일): 구조·역할 아키텍처 맵 §6 요약으로 충분 — **S요약 판정**. T티어 vendored 0 재확인.

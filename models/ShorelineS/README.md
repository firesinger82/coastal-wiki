# models/ShorelineS

> **Canonical source**: 이 디렉토리(`models/ShorelineS/`)가 ShorelineS 모델의 구현·메커닉에 대한 진실의 원천. 다른 곳(concepts 등)은 여기로의 링크만 가짐.
>
> 🟢 **현재 상태(2026-07-17 신설 + 코어 1차 검수 동일)**: 소스 clone(sha `7bf4481ab`) + 정체카드 + **source-analysis 4노트**(아키텍처 맵·transport 7공식·coastline_change·파랑/사구/스핏 모듈) + **manual-notes 1**(Roelvink 2020 Frontiers 발췌·코드 대조) + web-refs 1 — 전부 verified. 잔여(disclosed): 회절 기하 본문·transport_mud 본문·위상 처리(merge_coastlines_mc 등) deep — [models/AUDIT-LEDGER.md](../AUDIT-LEDGER.md) §14.

## 정체 카드

- **이름**: **ShorelineS** ("free-form coastline simulation program" — repo README.md:2)
- **저자/관리주체**: **J.A. (Dano) Roelvink** (IHE Delft, 2016–현재) 창시, **B.J.A. Huisman** (Deltares, 2017–현재) 확장 + 기여자 다수(Elghandour·Reyns·Ghonim·Mudde·Perry·de Beer·de Bakker·Trouw — `functions/ShorelineS.m:11-22`)
- **저작권**: Copyright (C) 2020 **IHE Delft & Deltares** (`functions/ShorelineS.m:26-27`)
- **라이선스**: 소스 헤더 = **LGPL v2.1 이상**(`functions/ShorelineS.m:38-42` "version 2.1 of the License, or (at your option) any later version"); repo 루트 `LICENSE` 파일 = **LGPL v3 전문**. 두 표기 병존(disclosed) — 실무상 LGPL 계열 free software.
- **공식 소스**: GitHub [danoroelvink/shorelines](https://github.com/danoroelvink/shorelines) · 공식 사이트 www.shorelines.nl (Roelvink et al. 2020 §Data Availability)
- **언어/플랫폼**: **MATLAB** (Octave 호환 분기 존재 — `functions/isoctave.m`, `ShorelineS.m:86-89` isoctave 사용). 컴파일 배포판 `compiled/` 동봉.
- **정체성**: 임의 형상(free-form) 벡터 해안선의 **one-line 해안선 진화 모델** — "computes shoreline changes as a result of gradients in alongshore sediment transport for arbitrary shaped coastlines"(`functions/ShorelineS.m:4-5` verbatim). 해안선 = 자유 이동 grid point 열, 다중 섹션(섬·석호)·스핏 발달·분리/병합 지원. 월~세기 시간스케일.
- **소스 스냅샷(manifest)**: git `7bf4481ab84c635033ef475fa648a1b09cf9f36b`(2025-10-07, depth-1 clone 2026-07-17). 위치: `models/ShorelineS/raw/source_code/shorelines/`(로컬, gitignore) + 외부 드라이브 아카이브 사본(로컬 관리 — 경로는 canonical 비기록, G8b).
- **repo 구조**: `functions/` **136 .m**(generic, 케이스 불변 — repo README.md:4) + `script/` 케이스 예제(groynes·dunes·회절·St-Louis 캘리브 등) + `doc/`(Roelvink 2020 Frontiers 논문 PDF `FMarS2020_Roelvink_etal.pdf`·ICEC2018 논문·FAQ PDF) + `compiled/` + `ShorelineS.ipynb`.

## 모델 분류 — 위키 유일의 해안선 진화(one-line) 클래스

기존 12모델(위상평균/위상해상 파랑·순환·침수)과 다른 축: 유체장을 풀지 않고 **연안표사 수지의 경사**로 해안선 위치를 직접 진화시키는 계보(Pelnard-Considère one-line의 free-form 일반화). 이론 대응 = [textbook/notes/theory-ch14-coastal-morphodynamics.md](../../textbook/notes/theory-ch14-coastal-morphodynamics.md)(one-line·CERC) + [concepts/littoral-drift](../../concepts/littoral-drift/). 시간스케일 대비: XBeach(폭풍 이벤트 2DH) ↔ ShorelineS(월~세기 계획선).

- **transport 공식 4종 선택**: `S.trform` = **CERC / KAMP(Kamphuis) / MILH(Mil-Homens) / VR14(Van Rijn 2014)** (`functions/prepare_transport.m:9,104`) + Soulsby-Van Rijn 별도 구현(`functions/transport_soulsbyvanrijn.m`) + mud coast(`transport_mud.m`)·tide-wave(`transport_tidewave.m`).
- **구조물·개입**: groyne(우회 `transport_bypass.m`·수중 `transport_groynesubmerged.m`)·revetment·투과성 구조 wave_transmission·양빈(nourishment)+shoreface nourishment(`get_fnourishment*.m`)·하천 토사(`get_riverdischarges.m`).
- **프로세스 모듈**: 사구(dune_erosion/flux/growth)·스핏/월류(prepare_spit·find_overwash_mc)·조석(tide_1d_ana_anycomp)·바람·runup·기후변화(SLR, introduce_climatechange)·수로/삼각주(channel·delta)·파랑 회절(wave_diffraction).

## 핵심 논문 (web-refs 상세)

- **기준 논문**: Roelvink, D., Huisman, B., Elghandour, A., Ghonim, M., Reyns, J. (2020) "Efficient Modeling of Complex Sandy Coastal Evolution at Monthly to Century Time Scales" *Frontiers in Marine Science* 7:535, doi:10.3389/fmars.2020.00535 — **repo `doc/FMarS2020_Roelvink_etal.pdf` 동봉**
- 초기 발표: Roelvink et al., ICEC 2018 (repo `doc/ICEC2018_Paper_Roelvink_final_14-8.pdf` 동봉)

→ 상세: [`web-refs/shorelines-official-resources.md`](web-refs/shorelines-official-resources.md)

## 하위 디렉토리 현황

| 경로 | 상태 | 비고 |
|---|---|---|
| `source-analysis/` | ✅ 4 verified | [architecture-map](source-analysis/shorelines-architecture-map.md)(5-phase 루프·분모) · [transport-formulations](source-analysis/shorelines-transport-formulations.md)(★실분기 7종·고각도 Sphimax·적응 dt 확산기준) · [coastline-change](source-analysis/shorelines-coastline-change.md)(staggered FTCS·Bruun SLR·★groyne 자동연장) · [wave-dune-spit-modules](source-analysis/shorelines-wave-dune-spit-modules.md)(회절 Kd 2공식·Larson 사구·overwash 광선법) |
| `manual-notes/` | ✅ 1 verified | [roelvink2020-frontiers](manual-notes/shorelines-roelvink2020-frontiers.md) — Eq.1/Eq.5·고각도·월류 코드 대조. FAQ PDF 발췌 후속 |
| `web-refs/` | ✅ 1 | 공식 repo·사이트·논문 서지 |
| `raw/source_code/shorelines/` | ✅ clone | sha 7bf4481ab, gitignore 로컬 |

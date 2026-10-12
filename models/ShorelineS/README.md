---
last_source_check: "2026-10-12 (recovery 대조 반영)"
verification_method: "2026-10-12 recovery 대조 보고서 R1·R2·R3 반영"
---

# models/ShorelineS

> **Canonical source**: 이 디렉토리(`models/ShorelineS/`)가 ShorelineS 모델의 구현·메커닉에 대한 진실의 원천. 다른 곳(concepts 등)은 여기로의 링크만 가짐.
>
> **핵심 노트 검수(2026-07)** — 2026-10-12 recovery 전수 판독·대조 반영. 근거는 [R1 이론 대조](../../_staging/recovery/compare/ShorelineS-theory-vs-code.md), [R2 입력 대조](../../_staging/recovery/compare/ShorelineS-inputs-vs-code.md), [R3 호출 흐름 대조](../../_staging/recovery/flow/ShorelineS-callflow.md)이다.

## 정체 카드

- **이름**: **ShorelineS** ("free-form coastline simulation program" — repo README.md:2)
- **저자/관리주체**: **J.A. (Dano) Roelvink** (IHE Delft, 2016–현재) 창시, **B.J.A. Huisman** (Deltares, 2017–현재) 확장 + 기여자 다수(Elghandour·Reyns·Ghonim·Mudde·Perry·de Beer·de Bakker·Trouw — `functions/ShorelineS.m:11-22`)
- **저작권**: Copyright (C) 2020 **IHE Delft & Deltares** (`functions/ShorelineS.m:26-27`)
- **라이선스**: 소스 헤더 = **LGPL v2.1 이상**(`functions/ShorelineS.m:38-42` "version 2.1 of the License, or (at your option) any later version"); repo 루트 `LICENSE` 파일 = **LGPL v3 전문**. 두 표기 병존(disclosed) — 실무상 LGPL 계열 free software.
- **공식 소스**: GitHub 저장소는 [danoroelvink/shorelines](web-refs/shorelines-official-resources.md)이다. 2020 논문은 MATLAB 소스 배포 주소로 `www.shorelines.nl`을 기재한다. (Roelvink et al. 2020, PDF 18쪽 / 인쇄 18, §Data Availability Statement) [10-12 전수 검증 정정]
- **언어/플랫폼**: **MATLAB** (Octave 호환 분기 존재 — `functions/isoctave.m`, `ShorelineS.m:86-89` isoctave 사용). 컴파일 배포판 `compiled/` 동봉.
- **정체성**: 임의 형상(free-form) 벡터 해안선의 **one-line 해안선 진화 모델** — "computes shoreline changes as a result of gradients in alongshore sediment transport for arbitrary shaped coastlines"(`functions/ShorelineS.m:4-5` verbatim). 해안선 = 자유 이동 grid point 열, 다중 섹션(섬·석호)·스핏 발달·분리/병합 지원. 월~세기 시간스케일.
- **소스 스냅샷(manifest)**: 원본 저장소 HEAD는 f3ec8638이고, 작업 트리 변경은 없으며, 7bf4481 이후 변경은 doc/ShorelineS_manual_v1.0.pdf 추가 하나이고, 이력은 47커밋(2018-05-24~2026-08-13)이다. ([R1 §1](../../_staging/recovery/compare/ShorelineS-theory-vs-code.md#1-요약); [git 이력 판정 §1](../../_staging/recovery/compare/ShorelineS-git-verify-dtheory.md#1-요약))
- **repo 구조**: `functions/` **136 .m**(generic, 케이스 불변 — repo README.md:4) + `script/` 케이스 예제(groynes·dunes·회절·St-Louis 캘리브 등) + `doc/`(Roelvink 2020 Frontiers 논문 PDF `FMarS2020_Roelvink_etal.pdf`·ICEC2018 논문·FAQ PDF·**공식 매뉴얼 `ShorelineS_manual_v1.0.pdf` 66쪽**) + `compiled/` + `ShorelineS.ipynb`.

## 모델 분류 — 위키 유일의 해안선 진화(one-line) 클래스

연안표사 수지의 경사로 해안선 위치를 직접 진화시키는 one-line 모델이다. TIDEPROF는 1차원 단면에서 조석류와 파랑 구동류를 계산한다. ([R1 §4](../../_staging/recovery/compare/ShorelineS-theory-vs-code.md#4-노트-대조와-수정안)) 이론 대응은 [theory-ch14-coastal-morphodynamics](../../textbook/notes/theory-ch14-coastal-morphodynamics.md)와 [littoral-drift](../../concepts/littoral-drift/)에 연결한다.

- **수송식 선택**: trform 분기는 CERC/CERC1, CERC2, CERC3, KAMP, MILH, VR14, RAY, TIDEPROF다. 실제 주 분기는 8개이다. Soulsby–Van Rijn은 TIDEPROF 경로의 하위 함수이다. CERC와 CERC1은 transport 주식의 별칭이지만 파랑 전처리 전체에서 같은 경로를 쓰지 않는다. ([R2:N11](../../_staging/recovery/compare/ShorelineS-inputs-vs-code.md#4-노트-대조와-수정안); [R3:N18](../../_staging/recovery/flow/ShorelineS-callflow.md#7-노트-수정안과-확인-범위); `functions/transport.m:140` `if strcmpi(upper(TRANSP.trform),'CERC') || strcmpi(upper(TRANSP.trform),'CERC1')`)
- **구조물·개입**: groyne(우회 `transport_bypass.m`·수중 `transport_groynesubmerged.m`)·revetment·투과성 구조 wave_transmission·양빈(nourishment)+shoreface nourishment(`get_fnourishment*.m`)·하천 토사(`get_riverdischarges.m`).
- **프로세스 모듈**: 사구(dune_erosion/flux/growth)·스핏/월류(prepare_spit·find_overwash_mc)·조석(tide_1d_ana_anycomp)·바람·runup·기후변화(SLR, introduce_climatechange)·수로(move_channel)·파랑 회절(wave_diffraction). ([R3 초기화·시간 단계 순서](../../_staging/recovery/flow/ShorelineS-callflow.md#1-초기화-순서)) [10-12 전수 검증 보완]

DELTA 준비 함수는 있다. 현재 ShorelineS.m 시간 루프는 DELTA를 소비하지 않는다. 근거: `functions/ShorelineS.m:72` `[DELTA]   = prepare_delta(S);`. ([R3:N19](../../_staging/recovery/flow/ShorelineS-callflow.md#8-차이-결론))

## 핵심 논문 (web-refs 상세)

- **기준 논문**: Roelvink, D., Huisman, B., Elghandour, A., Ghonim, M., Reyns, J. (2020) "Efficient Modeling of Complex Sandy Coastal Evolution at Monthly to Century Time Scales" *Frontiers in Marine Science* 7:535, doi:10.3389/fmars.2020.00535 — **repo `doc/FMarS2020_Roelvink_etal.pdf` 동봉**
- 초기 발표: Roelvink et al., ICEC 2018 (repo `doc/ICEC2018_Paper_Roelvink_final_14-8.pdf` 동봉)

→ 상세: [`web-refs/shorelines-official-resources.md`](web-refs/shorelines-official-resources.md)

## 하위 디렉토리 현황

| 경로 | 상태 | 비고 |
|---|---|---|
| `source-analysis/` | ✅ 5 verified | [architecture-map](source-analysis/shorelines-architecture-map.md)(5-phase 루프·분모) · [transport-formulations](source-analysis/shorelines-transport-formulations.md)(실분기 8종·고각도 Sphimax·적응 dt 확산기준) · [coastline-change](source-analysis/shorelines-coastline-change.md)(staggered FTCS·Bruun SLR·★groyne 자동연장) · [wave-dune-spit-modules](source-analysis/shorelines-wave-dune-spit-modules.md)(회절 Kd 2공식·Larson 사구·overwash 광선법) · [diffraction-mud-topology](source-analysis/shorelines-diffraction-mud-topology.md)(★rotfac 0.8 XBeach 보정·mud 농도수지 전문·위상 3파일·C 커버리지 판정 — 핵심 노트 검수(2026-07)) |
| `manual-notes/` | ✅ 3 verified | [technical-manual-v1](manual-notes/shorelines-technical-manual-v1.md)(**공식 매뉴얼 66쪽 전수** — 수송 7공식·회절 2종·투과 3식·사구/월류·파라미터 기본값 + ★매뉴얼 내부 불일치 3건을 코드로 판정) · [roelvink2020-frontiers](manual-notes/shorelines-roelvink2020-frontiers.md)(Eq.1/Eq.5·고각도·월류 코드 대조) · [faq-operational](manual-notes/shorelines-faq-operational.md)(ds0 50–100 m·경계 4종·twopoints/maxangle 60°·안정화 노브) |
| `web-refs/` | ✅ 1 | 공식 repo·사이트·논문 서지 |
| `raw/source_code/shorelines/` | ✅ clone | sha f3ec863(2026-09-21 갱신, 검수 시점 7bf4481ab 과 소스 바이트 동일), gitignore 로컬. ⚠ISO-8859+CRLF — `grep -a` 필요 |

## 문서와 코드 차이 (10-12 대조)

결론 문장 출처: [R2 입력 대조](../../_staging/recovery/compare/ShorelineS-inputs-vs-code.md#5-차이-결론), [R3 호출 흐름 대조](../../_staging/recovery/flow/ShorelineS-callflow.md#8-차이-결론).

문서 판: 매뉴얼 v1.0 2024-10-15, FAQ 2023-10-01, 논문 2018·2020. 코드 판: 원본 저장소 HEAD f3ec8638, 코드 파일은 7bf4481 2025-10-07과 같음.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:N11 | README trform 목록 | 매뉴얼 PDF 25쪽 / 인쇄 25 of 66: `CERC1` | `functions/transport.m:140` `if strcmpi(upper(TRANSP.trform),'CERC') \|\| strcmpi(upper(TRANSP.trform),'CERC1')`<br>`functions/transport.m:147` `elseif ~isempty(findstr(lower(TRANSP.trform),'cerc2'))`<br>`functions/transport.m:156` `elseif ~isempty(findstr(lower(TRANSP.trform),'cerc3'))`<br>`functions/transport.m:165` `elseif ~isempty(findstr(lower(TRANSP.trform),'kamp'))`<br>`functions/transport.m:174` `elseif ~isempty(findstr(lower(TRANSP.trform),'milh'))`<br>`functions/transport.m:182` `elseif ~isempty(findstr(lower(TRANSP.trform),'vr14'))`<br>`functions/transport.m:194` `elseif ~isempty(findstr(lower(TRANSP.trform),'ray'))`<br>`functions/transport.m:199` `elseif ~isempty(findstr(lower(TRANSP.trform),'tideprof'))` | C 문서 누락 | trform 분기는 CERC/CERC1, CERC2, CERC3, KAMP, MILH, VR14, RAY, TIDEPROF다. CERC1 경로 차이를 함께 적는다. |
| R3:N18 | README.md:23 | HEAD 기준 변경 전 노트 README.md:23 ``- **transport 공식 4종 선택**: `S.trform` = **CERC / KAMP(Kamphuis) / MILH(Mil-Homens) / VR14(Van Rijn 2014)** (`functions/prepare_transport.m:9,104`) + Soulsby-Van Rijn 별도 구현(`functions/transport_soulsbyvanrijn.m`) + mud coast(`transport_mud.m`)·tide-wave(`transport_tidewave.m`).`` | `functions/transport.m:147` `elseif ~isempty(findstr(lower(TRANSP.trform),'cerc2'))`<br>`functions/transport.m:156` `elseif ~isempty(findstr(lower(TRANSP.trform),'cerc3'))`<br>`functions/transport.m:194` `elseif ~isempty(findstr(lower(TRANSP.trform),'ray'))`<br>`functions/transport.m:199` `elseif ~isempty(findstr(lower(TRANSP.trform),'tideprof'))`<br>`functions/transport.m:208` `[QS(1,i),Slong_mean,Slong,v,vt,vw,Hrms,h] = transport_tidewave(TIDE.eta(i,:),TIDE.detads(i,:),TIDE.phi(i,:),TIDE.ss(i), ...`<br>`functions/transport.m:209` `TIDE.Ttide,TIDE.nT,TIDE.k(i,:),TIDE.cf,TIDE.hmin, ...`<br>`functions/transport.m:210` `Hrms0,Tp,theta0,alpha,gamma, ...`<br>`functions/transport.m:211` `TRANSP.ks,TRANSP.d50,TRANSP.d90,TIDE.hclosure, ...`<br>`functions/transport.m:212` `TIDE.x,TIDE.zb,TRANSP.acal,TRANSP.n);`<br>`functions/transport_tidewave.m:76` `[Slong]=transport_soulsbyvanrijn(h,Tp,k,Hrms,v,ks,hmin,D50,D90,Acal);` | C 문서 누락 | 대표 수송식 소개와 실제 trform 분기 목록을 구분한다. 실제 주 분기는 8개이다. Soulsby–Van Rijn은 TIDEPROF 경로의 하위 함수이다. [10-12 전수 검증 보완]
| R3:N19 | README.md:25 | HEAD 기준 변경 전 노트 README.md:25 `- **프로세스 모듈**: 사구(dune_erosion/flux/growth)·스핏/월류(prepare_spit·find_overwash_mc)·조석(tide_1d_ana_anycomp)·바람·runup·기후변화(SLR, introduce_climatechange)·수로/삼각주(channel·delta)·파랑 회절(wave_diffraction).` | `functions/ShorelineS.m:72` `[DELTA]   = prepare_delta(S);`<br>`functions/ShorelineS.m:245` `[CHANNEL,COAST]=move_channel(CHANNEL,COAST,TIME);`<br>`functions/prepare_delta.m:62` `if S.flooddelta & S.channel`<br>`functions/prepare_delta.m:83` `[DELTA.xflood,DELTA.yflood,DELTA.flooddeficit,DELTA.fcellarea] = prepare_flooddelta(xfloodpol,yfloodpol,S.dxf,S.dxf,S.overdepth);` | D 문서에만 있음 | DELTA 준비 함수는 있다. 현재 ShorelineS.m 시간 루프는 DELTA를 소비하지 않는다. [10-12 전수 검증 보완]

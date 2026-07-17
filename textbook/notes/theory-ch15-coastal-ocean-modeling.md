---
title: "이론 ch15 — 연안 3D 수치모델링 일반론: 정수압 · primitive equations · σ-좌표 · spin-up · 조석 잔류류 (EFDC claim-level 분해)"
topic: numerical-modeling
layer: 1
depends_on:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch05-rans.md
canonical_source: self
citation_status: verified
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch15(EFDC 운용, AI 합성 MDX 무인용) 이식분 — 2026-07-17 claim-level 분해(THEORY-LEDGER 방침: 일반 이론만 ①, EFDC 구현·운용은 models/EFDC 링크·복제 금지). 주 출처 = **stewart-physical-ocean §10.1·§15**(정수압 스케일링·수치모델 일반론·σ-좌표·spin-up·검증 경고) + **sea-level §7:6**(조석 잔류류). ★스케일 정정 1건: 원문 'spin-up 3~7일(조석 최소 5일)' 수치는 코퍼스 무근거(stewart p.271 은 전구 모델 수십 년 스케일의 개념 정의만) — 개념만 이식, 기간 수치는 미이식. σ-좌표 압력경사 오차 = 개념 실재하나 이론 코퍼스 일반 출처 미확정(EFDC/ROMS 매뉴얼 증거는 models 축 존재) — source-needed 1. 미이식(무근거 또는 운용/개인 축): NSE·RMSE 정의+목표치(코퍼스 0건 — p.339 'Nash'는 저자명 오탐)·equifinality(0건)·calibration 튜닝 우선순위 표·Manning n 범위·BC 데이터소스 파이프라인(KHOA/WAMIS/ERA5 — 운용 지침, 절대규칙 #8)·격자 해상도 비용 표·CFL 워크계산·initial shock 세부·한국 적용 사례 표(15.10)·한국 발주 양대 표준 관행·경쟁모델 국적 비교 표·EFDC 계보/역사(15.1·15.12 — models/EFDC README·web-refs 소유)·입력 파일 카드 표(15.5)·후처리 도구 표·비정수압 모델 목록·표사 매개변수 불확실성 상세(ws·τc — ch13·models 축). 34 단언 중 17 부착(50%)·16 삭제/미이식·source-needed 1."
verification_method: "stewart-physical-ocean p.164-165(§10.1 정수압 균형·스케일링 1:10⁶)·p.176(barotropic/baroclinic 분해)·p.269-271(§15.1-15.3 이산화 한계·난류 파라미터화·정수압+Boussinesq 채택·primitive equation·Bryan 1969·spin-up 정의·검증 경고 Post & Votta 2005)·p.272-275(§15.3-15.4 HYCOM isopycnal/hybrid·ROMS terrain-following·연안 모델·POM σ-좌표 Eq.15.1·Mellor-Yamada 1982) + sea-level p.260-263(§7:6 잔류류: Eulerian/Lagrangian·생성 기구·크기·장기 수송) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-17)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-17
related:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch05-rans.md
  - textbook/notes/theory-ch11-spectral-wave-modeling.md
  - textbook/notes/theory-ch12-tides.md
  - textbook/notes/theory-ch02-continuity.md
---

# 연안 3D 수치모델링 일반론 — 정수압 · primitive equations · σ-좌표 · 잔류류

> 4-레이어 **① 이론** 노트 — **claim-level 분해**: ch15 원문(EFDC 운용 챕터)에서 **모델 일반 이론**(근사·좌표계·모델 분류·검증 원리·잔류류 물리)만 이식. EFDC 고유의 지배방정식 구현·수치기법·입력 카드·calibration 운용은 `models/EFDC/`가 canonical — 여기서는 탐색 링크만.
> 근거 의존(①→①): N-S 스케일 분석 [[theory-ch04-navier-stokes]] · RANS 난류 폐합 [[theory-ch05-rans]].
> 탐색 링크(근거 의존 아님): Boussinesq 근사 [[theory-ch02-continuity]] · CFL·implicit [[theory-ch11-spectral-wave-modeling]] §6 · 조석·조화분해 [[theory-ch12-tides]] · `models/EFDC/`.

## 1. 정수압(hydrostatic) 근사

- **정수압 균형** $\dfrac{\partial p}{\partial z}=-\rho g$: 연직 운동량 방정식을 스케일 분석하면(수평 $L\sim10^6$ m·연직 $H\sim10^3$ m·$U\sim0.1$ m/s 급 해양 내부) 연직 가속·이류·Coriolis 항이 모두 $10^{-11}$ 급인데 압력경사·중력 항은 $10$ 급 — **연직에서 유일하게 중요한 균형이 정수압이며 1:10⁶ 까지 정확** (stewart-physical-ocean, p.164-165, §10.1 + scaling box; 근거 [[theory-ch04-navier-stokes]] N-S). 수압은 사실상 그 점 위 물기둥의 무게.
- **실용 해양모델의 표준 근사 세트**: 현실 해양의 자유도를 계산 가능한 수준으로 줄이기 위해 **정수압 + Boussinesq 근사**(때로 연직적분 천수방정식까지)를 채택 (stewart-physical-ocean, p.269, §15.1; Haidvogel & Beckmann 1999 인용). Boussinesq(밀도 변동은 부력항에만)의 정의·근거는 [[theory-ch02-continuity]] §3(탐색; stewart p.125-126 부착분).

## 2. Primitive equation 모델과 모델 분류

- **Primitive equation 모델**: 연속·운동량 방정식(기본형 그대로) + 정수압·Boussinesq + 상태방정식으로 3차원 흐름·열역학을 계산하는 모델 — 최초의 시뮬레이션 모델은 **Bryan (1969)** (GFDL Bryan-Cox 계보) (stewart-physical-ocean, p.270, §15.2).
- **Mechanistic vs simulation 모델**: 과정 연구용 단순화 모델(해석 용이) vs 현실 순환 재현용 복합 모델(해석 곤란) — 목적이 다름 (stewart-physical-ocean, p.270, §15.2).
- **연안(coastal) 모델의 특성**: 해빈~대륙사면 영역, 자유 수면·현실 해안선/지형·하천 유입·대기 강제 포함 — 외해로 깊이 연장되지 않으므로 **셸프 외측 경계에서 외부(광역) 정보가 필요** (stewart-physical-ocean, p.275, §15.4). 예시: POM(Blumberg & Mellor 1987)·Dartmouth 유한요소 모델 (p.275-276).

## 3. 이산화의 본질적 한계 — 난류 파라미터화·수치 오류

- **이산 격자 ≠ 연속계**: 이산계의 동역학은 연속계와 느슨하게만 연결되며 근사가 **가상(spurious) 해**를 만들 수 있음 (stewart-physical-ocean, p.269, §15.1).
- **난류는 직접 계산 불가 → 파라미터화 필연**: 난류 해상에는 mm 격자·ms 시간스텝이 필요(전구 ~$10^{27}$ 격자점 — 실용 모델 대비 **~20 자릿수 부족**, Holloway 1994 'eddy-viscous goo') — 실용 모델은 subgrid 운동을 eddy viscosity 로 뭉갬 (stewart-physical-ocean, p.269, §15.1; 폐합 이론은 [[theory-ch05-rans]] 근거). 연안 모델의 대표 폐합 = **Mellor & Yamada (1982)** (p.275-276, §15.4).
- **코드·검증의 경고**: 수치 코드에는 오류가 있고(컴파일러 버그·round-off 실사례, Lawrence et al. 1999) "**대부분의 모델은 충분히 verification/validation 되지 않았다**(Post & Votta 2005) — 적절한 검증 없이는 모델 출력은 신뢰 불가" (stewart-physical-ocean, p.270, §15.1). 출력은 "a grain of salt" 로 수용 (p.270).

## 4. 연직 좌표계 — σ(지형추종)·z·isopycnal·hybrid

- **σ-좌표(지형추종)**: 수심으로 스케일한 연직좌표 $\sigma=\dfrac{z-\eta}{H+\eta}$ ($\eta$ = 수면, $-H$ = 바닥) — 격자가 수면·바닥에 항상 정합, 수심이 크게 변하는 영역에 적합 (stewart-physical-ocean, p.275, §15.4, Eq. 15.1; POM 문맥). **ROMS = hydrostatic·primitive equation·terrain-following**(stretched 연직좌표) 지역 모델 (p.274, §15.3).
- **z-좌표 vs isopycnal vs hybrid**: z-좌표는 혼합층·천해에 유리하나 내부해양에선 등밀도면 혼합을 표현하기 어려움 — 내부는 밀도좌표(isopycnal)가 자연스럽고, **HYCOM 은 영역별로 두 좌표를 결합한 hybrid** (stewart-physical-ocean, p.272-273, §15.3).
- **σ-좌표 압력경사 오차**: 급한 지형에서 수평 압력경사가 큰 두 항의 작은 차로 계산되어 가상 흐름을 만드는 문제 — 이론 코퍼스 일반 출처 미확정(EFDC·ROMS 매뉴얼 증거는 `models/` 축 존재), 정식·대응책(지형 smoothing·hybrid 전환)은 source-needed. <!-- citation_status: source-needed -->
- **Barotropic/baroclinic 분해**: 연직 유속 구조는 **깊이 무관한 barotropic 성분 + 깊이 변화 baroclinic 성분**으로 분해 가능 — barotropic = 등압면∥등밀도면, baroclinic = 등압면이 등밀도면에 기욺(밀도가 깊이·수평으로 변함) (stewart-physical-ocean, p.176, §10.4). 이 분해가 모델의 external/internal **mode splitting** 수치기법의 물리적 기반 — 분리 시간적분 구현은 `models/EFDC/source-analysis/efdc_external_mode_solver.md`(탐색). 시간스텝의 Courant 제약·implicit 회피 일반론은 [[theory-ch11-spectral-wave-modeling]] §6(탐색; holthuijsen p.305 부착분).

## 5. Spin-up 과 모델 검증 원리

- **Spin-up**: 초기조건(밀도장·플럭스)과 운동방정식이 **서로 일관되지 않아** 모델을 본 계산 전에 미리 적분해 조정 상태로 만드는 과정 — 전구 순환 모델은 수십 년 급 적분 필요 (stewart-physical-ocean, p.271, §15.3). ※원 교재의 '연안 조석 모델 3~7일' 기간 수치는 코퍼스 무근거 — 개념만 이식, 수치는 미이식(운용 경험칙은 `models/EFDC/` 축).
- **검증(validation)의 원리적 한계**: §3 의 경고(불충분 검증·코드 오류·round-off)가 근거 — 모델-관측 불일치가 항상 모델 오류는 아니며 출력 수용에 비판적 태도 필요 (stewart-physical-ocean, p.270, §15.1). ※원 교재의 NSE·RMSE 정의·목표치(NSE≥0.7 등)·equifinality·튜닝 우선순위는 코퍼스 0건 — 미이식(calibration 운용은 `models/EFDC/source-analysis/efdc-calibration-foundation.md` 축). 조석 모델의 분조별 진폭·위상 검증 지표는 조화분해 [[theory-ch12-tides]] §4(탐색) 문맥.

## 6. 조석 잔류류(residual current) — 후처리 핵심 출력의 물리

- **정의**: 관측 유속을 여러 조석 주기로 평균하면 남는 순 흐름 — 고정점 평균 = **Eulerian residual**, 물덩이·부표의 장기 이동 = **Lagrangian residual** (sea-level, p.260, §7:6). 구동원은 밀도경사·바람응력·조석 (p.260).
- **크기와 중요성**: 조류 자체보다 **1~2 자릿수 작지만**(수 cm/s vs ~1 m/s) 지속성 때문에 **수온·염분 등 특성의 장기 분포·수송을 지배** (sea-level, p.260, §7:6) — 퇴적물·오염물 이동 평가에서 잔류류가 핵심 출력인 이유.
- **생성 기구**: (a) 진행 조석파의 비선형성 — 고수위 때 수송 $U_0(D+H_0)$ 과 저수위 때 복귀 $-U_0(D-H_0)$ 가 상쇄되지 않아 파 진행 방향 순 수송 (sea-level, p.260, §7:6); (b) 곶(headland)·섬 주변 — 지형 마찰이 와도를 부여해 만(灣)에 잔류 와류 형성(Portland Bill 관측례), 하수·방사성 폐기물 배출 설계에 직결 (p.261-262); (c) 사퇴(sandbank) 주변 — 마찰 + 지구 자전(potential vorticity 보존, [[theory-ch07-vorticity]] 문맥)으로 북반구 시계방향 순환 (p.262-263).

## 7. EFDC 구현·운용 = `models/EFDC/` (claim-level 분해 경계)

- **지배방정식의 EFDC 구현**(σ-좌표 변환식·mode splitting·난류 폐합 선택): `models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md`·`source-analysis/efdc_hydro_core.md`·`efdc_external_mode_solver.md` (탐색).
- **격자·경계조건·calibration·후처리 운용**: `source-analysis/efdc-grid-system-foundation.md`·`efdc-boundary-condition-foundation.md`·`efdc-calibration-foundation.md`·`efdc_caldisp_postprocess.md`·`manual-notes/efdc-user-manual-r850.md`·`efdc-implementation-guide.md` (탐색).
- **모델 정체·계보·역사**(Hamrick 1992 EPA 보고서·Tetra Tech·DSI EFDC+): `models/EFDC/README.md`·web-refs (탐색) — 이론 노트 비복제.
- 원문 ch15 의 입력 파일 카드 표·BC 데이터소스 파이프라인(KHOA·WAMIS·ERA5)·격자 비용 표·튜닝 표·한국 적용 사례(15.10)는 **운용 지침·개인/시장 관찰**이라 canonical 이론 노트 미이식 (절대규칙 #8; 데이터 소스 안내는 wiki 밖 케이스 축).

## 8. 연결

- [[theory-ch04-navier-stokes]] — N-S·스케일 분석(정수압 유도) (근거 의존)
- [[theory-ch05-rans]] — RANS·난류 폐합(파라미터화 필연·Mellor-Yamada) (근거 의존)
- [[theory-ch02-continuity]] — Boussinesq 근사 (탐색)
- [[theory-ch11-spectral-wave-modeling]] — CFL·implicit·모델 결합 (탐색)
- [[theory-ch12-tides]] — 조석·조화분해(검증 지표 문맥) (탐색)
- [[theory-ch07-vorticity]] — potential vorticity(사퇴 잔류류 기구) (탐색)
- `models/EFDC/` — 구현·운용 canonical (탐색)
- **T트랙 15/15 완주** — 교재 이식(4-레이어 ①) 전 챕터 종결.

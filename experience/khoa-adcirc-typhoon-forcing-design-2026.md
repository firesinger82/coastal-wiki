---
title: "ADCIRC 태풍 강제력 설계 — GAHM(비대칭 파라메트릭) + JMA-MSM 직접장 이원 구성 (KHOA 검증패키지 연계)"
topic: storm-surge
canonical_source: self
citation_status: source-needed
note_author: "Claude Opus 4.8 (1M context) + 사용자 합의"
note_date: 2026-06-20
verification_by: ""
verification_date: ""
experience_evidence:
  repeated_observation: false   # 설계(plan) 단계 — ADCIRC 미구동
  objective_data: true          # 선행연구 3편 + IBTrACS/JMA-MSM 실자료 확보
  reproducible: false           # 강제력 자료원·레시피는 명시, 모델 구동 결과는 미생산
---

# ADCIRC 태풍 강제력 설계

KHOA 관측 EVA([[khoa-design-surge-eva-2026]])의 모델 측 대응 — 자체 ADCIRC로 태풍 해일을 후측하기 위한 **바람·기압 강제력 구성 방침**. 격자·실행 세팅은 별도(ADCIRC 워크스페이스 소관). 검증 타깃·우선순위는 KHOA 산출(`khoa_tide/utide_validation/extensions/30_validation_targets_all`, `32_adcirc_priority.csv`) 재사용.

## 근거 선행연구 3편 (2026-06 사용자 제공)

| # | 출처 | 방법 | 우리 연계 |
|---|---|---|---|
| ① | 김혜인·조완희·문종윤 (2023) *KOSOMES* 29(7):770-778, ㈜해양정보기술 | ERA5(0.25°→0.05° 재격자) + **GAHM(ADCIRC NWS=20)** 비대칭 보텍스 합성. JTWC 4사분면 반경, 2001前은 회귀(Table 2)+Willoughby&Rahn(2004)+Knaff&Harper(2010) | **트랙 A 레시피** |
| ② | 김현정·서승원 (2019) *KSCOE* 31(5):241-252, 군산대 | TCRM 가상태풍 174,689개 → ADCIRC → GEV 100년 해일고 | **JPM 학술 원형**(독립모델 100년값 Table 4) — [[khoa-design-surge-eva-2026]] 토의 삼각검증 |
| ③ | 황태건 외 (2026) *JKWRA* 59(2):115-129, 경상국립대+원자력연+재난안전연 | **JMA-MSM 기상장 → 연성 ADCIRC-SWAN**(마이삭2009·하이선2010). JMA-MSM 안정 재현 / JTWC-BT 파라메트릭은 광역장 누락 → 해일·파랑 과소 | **트랙 B 타당성 입증** |

> 메모 요약: ②는 메인 EVA 논문이 감사하는 가상태풍 방법의 학술 원형(서승원=목포 191cm ADCIRC+SWAN 출처와 동일저자). ③의 'MSM>파라메트릭'은 KHOA ML emulator 점-특징 꼬리붕괴와 동일 물리(점/파라메트릭이 광역장·구조를 못 담음).

## 강제력 이원 구성

| 트랙 | 강제력 | ADCIRC | 비대칭 | 커버리지 | 근거 |
|---|---|---|---|---|---|
| **A. 파라메트릭** | 베스트트랙 → GAHM 보텍스 | NWS=20 (+ASWIP) | 사분면 반경 입력만큼 | **1956+ 전체** | ① |
| **B. 격자장 직접** | JMA-MSM 기상장 | NWS=13/OWI | 완전(격자) | **2006+만** | ③ |

**A=백본**(전 기간·전 태풍 일관), **B=2006+ 고해일 태풍에서 A와 교차검증**. 핵심 비교 = 동일 태풍에 A vs B → 강제력 방식이 해일 재현에 미치는 영향 정량(③의 결론을 KHOA 정점망에서 재현).

### 트랙 A — GAHM 입력 (①)
- **GAHM 비대칭 = 34/50/64kt 등풍속의 4사분면(NE/SE/SW/NW) 반경**이 핵심 입력. 반경이 빈약하면 GAHM도 대칭으로 퇴화.
- **자료원 = JTWC(JMA 아님)**: JTWC가 4사분면 반경을 **2001년부터 직접** 제공(JMA bst는 장축/단축+방향의 타원 2-등풍속이라 변환 필요·열위). ①이 JTWC를 쓴 이유.
- **2001년 이전 보완(①)**: 사분면 반경=Vmax·Rmax·위도 1차 회귀(① Table 2 계수, 회귀 corr 0.59 > Holland 0.45) / Rmax=Willoughby&Rahn(2004) `46.29·exp(−0.0153·Vmax+0.0166·lat)` / Pc=Knaff&Harper(2010) `Vmax=4.4·(1010−Pc)^0.76`. → 1956~2000도 비대칭 가능.
  - **✅ Table 2 전사 완료(2026-06-20)**: `khoa_tide/utide_validation/data/gahm_radius_regression.json`(R34/R50/R64 × NE/SE/SW/NW, `R = a_const + a_lat·lat + a_Vmax·Vmax + a_Rmax·Rmax`, 단위 nm/deg/kt) + 헬퍼 `gahm_radius_fill.py`(자기검증: lat30·Vmax80kt·Rmax15nm → R34 NE143/SW112nm, 단조감소·비대칭 정상). 주의: R34의 NE·SE가 a_const만 상이(원논문 그대로) / W&R는 원전대로 Vmax[m/s]→Rmax[km] 후 nm 변환 / 회귀는 2001–2021 학습이라 **1990–2000 보완용**(IBTrACS 2001+는 실측 우선).
  - **✅ 반경 데이터셋 완성(2026-06-21)**: `build_ibtracs_radii.py` → `extensions/40_ibtracs_korea_radii.{csv,json}`(+`_summary.json`). IBTrACS↔29_ **178/178(이름보유) 매칭**, 16,613 트랙포인트. 반경 **관측 5,742(2001+)·회귀충전 7,678(1990–2000 전량 4,889 포함)·불가 3,193(Vmax결측)**. 충전사슬 Vmax→W&R Rmax→Knaff&Harper Pc→①회귀, **Vmax<등풍속이면 반경=0**(외삽금지). 검증: 볼라벤2012 R34 NE190/SW160nm 비대칭 양호. intl 선행0(`0314`, 45개)은 정식 로더 `gahm_radius_fill.load_korea_radii()`(dtype=str)로 안전 처리(JSON 키도 안전).
- 입력 생성=ASWIP(ADCIRC 부속). 외곽장·배경장 미반영 한계 → 필요시 ERA5 재격자장과 max-합성 보완(①).

### 트랙 B — JMA-MSM 직접장 (③)
- JMA-MSM(psea·u·v, 5km, 1h) → NWS=13(OWI netcdf). 풍속 10m·기압 해면, lat 내림차순 주의.
- 2006+ 한정(MSM 보관 한계). 1990+ ERA5(0.25°)는 핵 과소(RMW 못 풂)라 보조용만 — ①·③ 모두 ERA5 단독 태풍강도 과소를 지적.

## 자산 현황 (2026-06-20)

| 항목 | 상태 |
|---|---|
| **IBTrACS WP 베스트트랙** (A 핵심) | ✅ 확보 — v04r01 CSV(108MB, 1884~2026, 247,502행). `USA_R34/R50/R64_{NE,SE,SW,NW}`·`USA_RMW`·`USA_WIND/PRES` + TOKYO(JMA)·KMA. 결측=공백문자. **반경 가용: 1990–2000 0% / 2001+ ~45%(피크엔 채워짐, 힌남노2022 NE50 vs SW35nm 비대칭 확인)** |
| JMA-MSM 기상장 (B 강제력) | ✅ 457일 보유(2006+ 97태풍) |
| ERA5 기상장 (외곽보강·보조) | ✅ 337/338 태풍 |
| 검증 타깃·우선순위 | ✅ KHOA `30_`,`32_` (자료오류 4정점 제외, 1차 22태풍, Gate-4 RMSE≤30cm) |
| ADCIRC + ASWIP 빌드 | ✅ v56.2.1 (ADCIRC 워크스페이스) |
| ① Table 2 회귀계수 (1990–2000 반경) | ✅ 전사 완료 — `data/gahm_radius_regression.json` + `gahm_radius_fill.py` |
| **정리된 반경 데이터셋** (178태풍, 관측+충전) | ✅ `extensions/40_ibtracs_korea_radii.{csv,json}` |

**상태**: 강제력 자료·레시피 완비 + **GAHM 입력 반경 데이터셋 178태풍 생성 완료**(관측 5,742 + 회귀충전 7,678점). 남은 것 = ASWIP로 fort.22(NWS=20) 생성 + 실제 ADCIRC 구동(별도 워크스페이스).

## 원천 위치
- 설계 상세: `khoa_tide/utide_validation/ADCIRC_FORCING_DESIGN.md`
- 선행연구 PDF: 사용자 제공(`Downloads/`); 서지·발췌는 본 노트 표 및 KHOA 메모 `three-reference-papers-2026-06`.
- IBTrACS: NOAA NCEI v04r01 (`ibtracs.WP.list.v04r01.csv`).

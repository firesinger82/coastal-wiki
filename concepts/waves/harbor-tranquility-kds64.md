---
title: "항만 정온도(harbor tranquility) 설계 표준 — KDS 64 + SWAN 실무"
topic: waves
canonical_source: self
citation_status: verified
source: "KDS 64 10 10·64 40 10 (2024, 해양수산부) 표준값 — 율포항 국가어항 타당성조사 보고서 제4장 수치모형실험 §4.2(2026) PDF 직접 인용 경유. SWAN 설정은 동 보고서 + SWAN-GUI MODEL_ASSUMPTIONS 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-12
---

# 항만 정온도 설계 표준 — KDS 64 + SWAN 실무

> 한국 항만·어항 **정온도(harbor tranquility/agitation) 설계실무**의 객관 표준. 모델 선택 trade-off는 [`06-model-application.md §1.1`](06-model-application.md); 이 노트는 **국가 설계기준(KDS 64) 정량값 + 표준 SWAN 워크플로**.

## 1. 표준 모델 = SWAN (위상평균)

한국 정온도 실무는 **SWAN Model**을 표준으로 사용 (설계파산정 + 항내정온도 모두). SWAN이 고려하는 전파과정: 굴절·천수·**회절(diffraction)**·쇄파·blocking/reflection. 정온도는 SWAN의 **회절 옵션 + 구조물 반사율**로 처리.

- ⚠️ SWAN 회절은 **위상평균 근사**(phase-decoupled, Holthuijsen 2003 — [[swan-tech-ch2-obstacles-diffraction-setup]]). 항만 **공진·다중반사·장주기**엔 정확도 한계 → 정밀 검증은 위상해상 Boussinesq([`../../models/FUNWAVE/`](../../models/FUNWAVE/)·[`../../models/Celeris/`](../../models/Celeris/), §7).
- 표준 SWAN 설정(실무 예): STATIONARY, GEN3 KOMEN, BREAKING α=1.0 γ=0.73, FRICTION JON 0.038, 약최고고조위 수위.

## 2. nesting 격자 (실무 예 — 율포항)

| 영역 | 실거리 | 격자수 | 격자간격 |
|---|---|---|--:|
| 광역 | 46.0 × 55.0 km | 460 × 550 | 100 m |
| 중간역 | 18.0 × 14.0 km | 360 × 280 | 50 m |
| **상세역** | 4.6 × 3.6 km | 460 × 360 | **10 m** |

→ 광역→상세 nesting으로 외해 설계파를 항 입구까지 전달, 상세역(Δ10m)에서 항내 파고 평가.

## 3. 구조물 반사율 (KDS 64 10 10, 2024)

| 구조형식 | 반사율 | 구조형식 | 반사율 |
|---|--:|---|--:|
| 직립벽 (마루 정수면 위) | 0.7~1.0 | 이형소파 블록사면 | 0.3~0.5 |
| 직립벽 (마루 정수면 아래) | 0.5~0.7 | 직립소파 구조물 | 0.3~0.6 |
| 사석사면 (1:2~3) | 0.3~0.6 | 자연해빈 | 0.05~0.2 |

## 4. 항내정온 기준파고 (KDS 64 40 10, 2024)

수역시설 용도별 이용가능 최대파고 (한계파고). 계류시설 전면은 선종·선형·하역특성으로 별도 결정.

| 구분 | 수심 3.0m 미만 | 3.0m 이상 |
|---|--:|--:|
| 항내 묘박·정박 가능 최대 | 0.60 m | 0.70 m |
| 항로 항행 가능 최대 | 0.90 m | 1.20 m |
| 양육·준비 가능 | 0.30 m | 0.40 m |
| 휴식 가능 최대 | 0.40 m | 0.50 m |

## 5. 표준 워크플로

```
심해설계파(빈도별·파향별, 예 50년) ─SWAN nesting(광역→중간→상세)─▶ 항내 파고분포
   → 실험안별(현상태/비교안/채택안) × 주영향 파향 × 반사율(KDS64 10 10)
   → 항내 파고 vs 기준파고(KDS64 40 10) 대조 → 정온확보 구역 판정
```
- 출력: 파향-파고 벡터도 + 파고분포도(정온확보 구역 음영).
- 평면배치 대안을 비교해 **정온확보 가능한 채택안** 도출이 목적.

## 6. Worked example — 율포항 (국가어항, 50년 빈도)

> 율포항 타당성조사 보고서 §4.2 (illustrative; 항-특정값).

- 입사 심해설계파(50년, 파향별 Hs/T): ESE 5.1m/10.0s · SE 5.4m/10.3s · **SSE 11.9m/16.5s** · **S 10.9m/16.5s** · SSW 5.1m/10.5s · SW 5.8m/12.0s (태풍 지배)
- 기준해면: 약최고고조위 DL(+)4.230m
- 결과: 현상태 **S계열 내습시 항내 0.6m 이상**(정온 미확보) → 채택안에서 전 접안시설 정온확보.

## 7. SWAN 표준 vs FUNWAVE/Celeris 정밀 티어

| | SWAN (표준·인허가) | FUNWAVE/Celeris (정밀 검증) |
|---|---|---|
| 회절 | 위상평균 근사 | **위상해상**(정확) |
| 공진·다중반사·장주기 | 약함 | 강함 |
| 위치 | KDS 64 표준, routine 설계 | 공진 민감·SWAN 의심 케이스 검증 |
| 비용 | 빠름 | 느림 → **GPU로 상쇄**([`06-model-application.md §1.1`](06-model-application.md)) |

→ 권장: **SWAN으로 표준 정온도(인허가) + 필요시 FUNWAVE/Celeris 동일 케이스로 정밀 재현·교차검증**.

## 8. 연결

- [`06-model-application.md §1.1`](06-model-application.md) — 정온도 모델 선택 trade-off
- [[swan-tech-ch2-obstacles-diffraction-setup]] — SWAN 회절 근사(Holthuijsen 2003)
- [`../../models/FUNWAVE/`](../../models/FUNWAVE/) · [`../../models/Celeris/`](../../models/Celeris/) — 정밀 티어
- 외부: KDS 64 10 10(구조물 반사율)·KDS 64 40 10(정온 기준파고), 2024 해양수산부

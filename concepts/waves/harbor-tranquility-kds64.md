---
title: "항만 정온도(harbor tranquility) 설계 표준 — KDS 64 + SWAN 실무"
topic: waves
canonical_source: self
citation_status: verified
source: "KDS 64 10 10 §4.3.6(반사율 참고표 4.3-4, Seelig·Ahrens 1981) — KDS 원문 PDF 직접 확인(opendataloader-pdf 변환, 2026-06-13). KDS 64 40 10(하역/계류한계파고 해설표 4.2-3/4·선체동요 참고표 4.2-1) 원문 확인. SWAN 정온도 표준 실무는 한국 항만설계 일반 관행. ※율포항 항-특정 내용은 제거(2026-06-13)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-12
---

# 항만 정온도 설계 표준 — KDS 64 + SWAN 실무

> 한국 항만·어항 **정온도(harbor tranquility/agitation) 설계실무**의 객관 표준. 모델 선택 trade-off는 [`06-model-application.md §1.1`](06-model-application.md); 이 노트는 **국가 설계기준(KDS 64) 정량값 + 표준 SWAN 워크플로**.

## 1. 표준 모델 = SWAN (위상평균)

한국 정온도 실무는 **SWAN Model**을 표준으로 사용 (설계파산정 + 항내정온도 모두). SWAN이 고려하는 전파과정: 굴절·천수·**회절(diffraction)**·쇄파·blocking/reflection. 정온도는 SWAN의 **회절 옵션 + 구조물 반사율**로 처리.

- ⚠️ SWAN 회절은 **위상평균 근사**(phase-decoupled, Holthuijsen 2003 — [[swan-tech-ch2-obstacles-diffraction-setup]]). 항만 **공진·다중반사·장주기**엔 정확도 한계 → 정밀 검증은 위상해상 Boussinesq([`../../models/FUNWAVE/`](../../models/FUNWAVE/)·[`../../models/Celeris/`](../../models/Celeris/), §7).
- 표준 SWAN 설정(실무 예): STATIONARY, GEN3 KOMEN, BREAKING α=1.0 γ=0.73, FRICTION JON 0.038, 약최고고조위 수위.

## 2. nesting 격자 (SWAN 표준)

정온도는 외해→항내 scale가 커서 **광역→중간역→상세역 nesting**으로 구성. 광역에서 외해 설계파를 받아 단계적으로 상세역(항 입구·항내)까지 전달, 상세역(통상 Δ~10m)에서 항내 파고 평가.

| 영역(역할) | 격자간격(통상) |
|---|---|
| 광역 (외해 변형) | ~100 m |
| 중간역 (연안 천수) | ~50 m |
| **상세역 (항내 평가)** | **~10 m** |

## 3. 구조물 반사율 (KDS 64 10 10 참고표 4.3-4, Seelig·Ahrens 1981)

| 구조형식 | 반사율 | 구조형식 | 반사율 |
|---|--:|---|--:|
| 직립벽 (마루 정수면 위) | 0.7~1.0 | 이형소파 블록사면 | 0.3~0.5 |
| 직립벽 (마루 정수면 아래) | 0.5~0.7 | 직립소파 구조물 | 0.3~0.6 |
| 사석사면 (1:2~3) | 0.3~0.6 | 자연해빈 | 0.05~0.2 |

## 4. 항내정온 기준파고 (KDS 64 40 10, 2024 — 원문 1차 확인)

KDS 64 40 10(수역시설) 정온도 평가의 기준파고는 **하역한계파고 + 계류한계파고**로 구분(해설 표 4.2-3) + **선체 동요 권고기준**(참고 표 4.2-1: Surge/Sway/Heave/Yaw/Pitch/Roll, m·°, 선종별). 하역한계파고는 대상선박 선종·선형·하역특성으로 결정(해설 표 4.2-4, 日本港灣協會 1989).

> ⚠️ **정정**: 단순 "묘박 0.6m / 항행 0.9m" 류 수심별 이용가능최대파고 표는 **현행 KDS 64 40 10 본문에 없음**(구판 항만설계기준·어항 관련 추정). 정확 정량값은 [KDS MD 변환본](#) 참조 — opendataloader-pdf 변환 예정.

## 5. 표준 워크플로

```
심해설계파(빈도별·파향별, 예 50년) ─SWAN nesting(광역→중간→상세)─▶ 항내 파고분포
   → 실험안별(현상태/비교안/채택안) × 주영향 파향 × 반사율(KDS64 10 10)
   → 항내 파고 vs 기준파고(KDS64 40 10) 대조 → 정온확보 구역 판정
```
- 출력: 파향-파고 벡터도 + 파고분포도(정온확보 구역 음영).
- 평면배치 대안을 비교해 **정온확보 가능한 채택안** 도출이 목적.

## 6. SWAN 표준 vs FUNWAVE/Celeris 정밀 티어

| | SWAN (표준·인허가) | FUNWAVE/Celeris (정밀 검증) |
|---|---|---|
| 회절 | 위상평균 근사 | **위상해상**(정확) |
| 공진·다중반사·장주기 | 약함 | 강함 |
| 위치 | KDS 64 표준, routine 설계 | 공진 민감·SWAN 의심 케이스 검증 |
| 비용 | 빠름 | 느림 → **GPU로 상쇄**([`06-model-application.md §1.1`](06-model-application.md)) |

→ 권장: **SWAN으로 표준 정온도(인허가) + 필요시 FUNWAVE/Celeris 동일 케이스로 정밀 재현·교차검증**.

## 7. 연결

- [`06-model-application.md §1.1`](06-model-application.md) — 정온도 모델 선택 trade-off
- [[swan-tech-ch2-obstacles-diffraction-setup]] — SWAN 회절 근사(Holthuijsen 2003)
- [`../../models/FUNWAVE/`](../../models/FUNWAVE/) · [`../../models/Celeris/`](../../models/Celeris/) — 정밀 티어
- 외부: KDS 64 10 10(구조물 반사율)·KDS 64 40 10(정온 기준파고), 2024 해양수산부

---
title: "KHOA surge EVA 파이프라인 — 기대 출력·검증 포인트·정량 결과 귀속"
canonical_source: self
citation_status: verified
verification_method: "본 위키 내 cross-reference. 정량 결과·정점별 판정은 experience/khoa-design-surge-eva-2026.md (verified) 귀속. 방법 검증 포인트는 concepts/storm-surge/03-analysis-methods.md·concepts/tides/03-analysis-methods.md 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - examples/khoa-surge-eva-pipeline/README.md
  - experience/khoa-design-surge-eva-2026.md
---

# 기대 출력 · 검증 포인트

> ⚠ 본 예제는 **재현 절차 템플릿**이다. 정점별 정량값(100년 재현값·CI·설계값 판정·기후증폭률)은 모두 [`experience/khoa-design-surge-eva-2026.md`](../../../experience/khoa-design-surge-eva-2026.md) 에 귀속한다. 여기서는 각 단계가 무엇을 산출해야 하는지와 검증 포인트만 기술한다.

## 단계별 기대 출력

| 단계 | 산출물 | 검증 포인트 |
|---|---|---|
| ① fetch | 정점·일자별 조위 시계열(실측·예측) | OpenAPI 1년 retention 경계 — 1년 이전 reqDate 는 NODATA ([`storm-surge/04 §4.1`](../../../concepts/storm-surge/04-code-and-tools.md)) |
| ② utide | 조화상수 $(H_n, g_n)$ + 천문조 예측 $\eta_{tide}(t)$ | KHOA 공시 조화상수와 M₂/S₂/K₁/O₁ cross-check ([`khoa-49-station §4`](../../../experience/khoa-49-station-16yr-utide-2026.md)) |
| ③ separation | 폭풍해일 잔차 $S(t)$ | 잔차에 잔여 조석 신호 없어야 함 ([`storm-surge/03 §1`](../../../concepts/storm-surge/03-analysis-methods.md)) |
| ④ 표본 | AM 표본·POT 표본(디클러스터됨) | $M\ge25$ 권장; POT 피크가 독립 event 인지 ([`storm-surge/03 §3·§4`](../../../concepts/storm-surge/03-analysis-methods.md)) |
| ⑤ EVA | 100년 재현값 $z_{100}$ [95% CI] (Gumbel/GEV/GPD/RFA) | **단일 방법 결론 금지** — 방법 간 수렴/발산 검토 ([`design-surge §2`](../../../experience/khoa-design-surge-eva-2026.md)) |
| ⑥ 감사 | CI 가 설계값 포함 여부·총수위·SSP 재현주기 | 정점별 판정·정량은 experience 귀속 |

## 핵심 검증 교훈 (방법론, experience 귀속)

- **방법 의존성이 결정적**: 동일 잔차라도 Gumbel/GEV/POT/RFA 가 100년값을 크게 벌린다. 단일 방법(특히 단기록 Gumbel-AM 단독)으로 결론내면 오인. 출처 [`experience/khoa-design-surge-eva-2026.md §2`](../../../experience/khoa-design-surge-eva-2026.md).
- **단기록 정점은 RFA 가 실용적**: 단일정점 POT 의 CI 가 매우 넓어, 권역 index-flood(RFA) 가 안정 — 단 권역 동질성(Hosking-Wallis $H$) 진단 필수. 출처 [`design-surge §13`](../../../experience/khoa-design-surge-eva-2026.md).
- **QC 소급이 판정을 바꾼다**: 단일 손상연도 가짜극값이 정점 판정과 권역 성장곡선을 동시에 오염할 수 있다(목포 1957 사례). 동질화 dropped 의 극치분석 소급이 필수 절차. 출처 [`design-surge §11·§13`](../../../experience/khoa-design-surge-eva-2026.md).
- **재현성 시드 규칙**: 부트스트랩은 전역 RNG 대신 정점별 고정 시드(CRC32 등) — 전역 RNG 는 정점 추가 시 타정점 CI 가 MC 노이즈로 뒤집힐 수 있다. 출처 [`design-surge §13`](../../../experience/khoa-design-surge-eva-2026.md).

## 정량 결과 전체

설계값 감사(21항만)·joint tide-surge 총수위 분해·SSP 기후증폭(연례화) 등 모든 정량 결론은 [`experience/khoa-design-surge-eva-2026.md`](../../../experience/khoa-design-surge-eva-2026.md) (§2~§13) 참조.

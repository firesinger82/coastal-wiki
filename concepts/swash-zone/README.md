# concepts/swash-zone — 처오름대 (Swash Zone)

> 쇄파 후 bore 가 해빈 위로 밀려 올라갔다(uprush) 다시 내려오는(backwash) **물이 주기적으로 적셨다 마르는 천이대**. 연안표사·runup·연안구조물 작용의 최전선이며, surf zone 과 dry beach 사이의 경계.

## 정체

- **1차 축**: 도메인 개념(처오름 동역학). swash = surf zone 의 landward 연장, time-varying shoreline.
- 인접: [`concepts/waves`](../waves/)(쇄파·runup) · [`concepts/littoral-drift`](../littoral-drift/)(alongshore transport) · [`concepts/sediment-transport`](../sediment-transport/)(bed-load·suspended) · [`concepts/storm-surge`](../storm-surge/)(범람 wave setup).
- 모델: 위상해상(Boussinesq/Green-Naghdi·SWASH 비정수압·XBeach NH·NLSW)이 swash 해상의 핵심 — [`04-code-and-tools.md`](04-code-and-tools.md).

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **source-needed** | swash 정의·process(uprush/backwash·bore collapse·swash-swash interaction·IG)·runup·sediment·전이된 연구 3건 |
| `04-code-and-tools.md` | ✅ **verified** (2026-06-18) | swash 수치모델 점검 — 모델 swash-handling(SWASH·XBeach·FUNWAVE)을 검수된 source-analysis 로 연결(wetting-drying·breaking·runup·비정수압). NLSW 해·VOF/SPH·한국검증은 source-needed 잔존 |
| `02-theory.md` | ✅ **verified** (2026-06-18) | NLSW swash 해(Shen-Meyer 1963·Antuono 2010, 문헌 cross-ref)·Iribarren/surf similarity scaling·runup 매개변수화(R_u2%·front velocity Eq2-4)·uprush/backwash 비대칭. **교과서 page 인용 verified**: surf similarity ζ=tanβ/√(H0/L0) coastal-processes p.26 §3.3.1 / run-up 속도·계수 coastal-structures p.20-23 §2.3. Hunt1959·Stockdon2006·breaker-type 임계값은 source-needed(교과서 본문 미보유) |
| `03-analysis-methods.md` | (미생성) | wave/shoreline tracking·scalogram·runup 통계(R2%) |
| `05-examples.md` | (미생성) | 한국 해빈 swash·runup 관측 사례 |
| `06-model-application.md` | (미생성) | XBeach/SWASH 적용 워크플로 — `models/` 작성 후 |

## 출처 원칙

본 토픽은 신규(2026-06-15) — research/inbox promote 3건 + publicly-known 모델 canonical 로 시작. 정량 claim 은 abstract 기반 `source-needed`. full PDF read·교과서(Holthuijsen Ch 11·Dean-Dalrymple) 인용 시 `verified` 승격.

# THEORY-LEDGER — 교재 이론 이식 원장 (4-레이어 ①, T 트랙)

> **목적**: 교재 프로젝트 `textbook-ai-data-full`(작성자 로컬 repo — 16챕터, 인용 없는 AI 합성 MDX; 위치는 [plan.md](../plan.md) 4-레이어 섹션 참조)를 `textbook/notes/theory-ch<NN>-<slug>.md` 로 **인용보강 이식**하는 진척·지표 추적. 정책: [plan.md "4-레이어 지식 아키텍처 v2"](../plan.md) · [CONVENTIONS §8.1](../CONVENTIONS.md). 패턴: [models/AUDIT-LEDGER.md](../models/AUDIT-LEDGER.md).
>
> **챕터당 절차(인용접지 파이프라인)**: MDX 이식(컴포넌트 제거) → 원자 단언 분해 → `textbook/md/` FTS5·페이지 대조 → `(source_id, p.N)` 부착 → **미매칭 단언 = 삭제 또는 source-needed 콜아웃** → validator(3종+layer lint) → 지표 기록. 부분 부착 ≠ 파일 verified. frontmatter: `layer: 1` + AI 합성 provenance.
>
> **stop/go 게이트**: T1 파일럿 지표로 장별 scope·페이스 재산정(고정 "세션당 N챕터" 없음). Codex 게이트 ⓐ(T1 후)·ⓒ(~4챕터 배치마다).

## 진척 대시보드

| 챕터 | 주제 | 노트 | 주 출처 후보 | 상태 | 단언 수 | 매칭률 | 소요 |
|---|---|---|---|:--:|--:|--:|--:|
| 00 | Intro (학습 안내) | — | — | **이식 제외** (사이트 안내문, 이론 아님) | - | - | - |
| 00.5 | 수학 도구 (벡터·텐서·RTT) | — | hydraulics-and-hydrology 외 | ⬜ | | | |
| 01 | 보존법칙 (검사체적·RTT) | — | hydraulics-and-hydrology | ⬜ | | | |
| 02 | 연속방정식 | — | hydraulics-and-hydrology | ⬜ | | | |
| 03 | Euler·Bernoulli | — | hydraulics-and-hydrology | ⬜ | | | |
| 04 | Navier-Stokes | — | hydraulics-and-hydrology | ⬜ | | | |
| 05 | RANS·난류 | — | hydraulics-and-hydrology | ⬜ | | | |
| 06 | 경계층 | — | hydraulics-and-hydrology | ⬜ | | | |
| 07 | 와도 동역학 | — | hydraulics-and-hydrology | ⬜ | | | |
| **08** | **선형 파동·분산관계** | [theory-ch08-linear-waves](notes/theory-ch08-linear-waves.md) | water-wave-mechanics(주)·holthuijsen2007 | ✅ **T1 완료**(2026-07-12) | 26 | 92% (24 부착·2 삭제) | ~0.5h |
| 09 | 비선형 파동·스펙트럼 | — | holthuijsen2007·hudspeth2005 | ⬜ | | | |
| 10 | 해안 변형 (shoaling·refraction) | — | coastal-eng-intro-wijetunge·coastal-processes-with-eng-apps | ⬜ | | | |
| 11 | SWAN 모델 | — | ★claim-level 분해 — 일반 이론만 ①, 모델 구현은 models/SWAN 탐색 링크(복제 금지) | ⬜ | | | |
| **12** | **조석** | — | tidal-heights-manual·sea-level·stewart-physical-ocean | **T2 예정** (③ B1 연계) | | | |
| 13 | 퇴적물 이송 (Shields·Rouse) | — | mechanics-of-sediment-transport·marine-sands-manual·van-rijn-1993 | ⬜ | | | |
| 14 | 해안 형태동역학 (Dean·CERC·Bruun) | — | coastal-processes-with-eng-apps·coastal-eng-guidelines | ⬜ | | | |
| 15 | EFDC 운용 | — | ★claim-level 분해 — 일반 이론만 ①, 모델 구현은 models/EFDC 탐색 링크(복제 금지) | ⬜ | | | |

- 매칭률 = (source_id, page) 부착 단언 / 전체 원자 단언. 미매칭 처리(삭제/source-needed) 건수는 노트 frontmatter·본문 콜아웃에.
- 상태: ⬜ 미착수 / 🔄 진행 / ✅ verified / 🟡 source-needed 잔존.

## 게이트 기록

| 게이트 | 일자 | 판정 | 요지 |
|---|---|---|---|
| (설계) Codex 2회차 | 2026-07-12 | MODIFY→반영 | 4-레이어 v2 — plan.md 검증 이력 참조 |

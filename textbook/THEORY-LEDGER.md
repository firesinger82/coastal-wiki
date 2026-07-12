# THEORY-LEDGER — 교재 이론 이식 원장 (4-레이어 ①, T 트랙)

> **목적**: 교재 프로젝트 `textbook-ai-data-full`(작성자 로컬 repo — 16챕터, 인용 없는 AI 합성 MDX; 위치는 [plan.md](../plan.md) 4-레이어 섹션 참조)를 `textbook/notes/theory-ch<NN>-<slug>.md` 로 **인용보강 이식**하는 진척·지표 추적. 정책: [plan.md "4-레이어 지식 아키텍처 v2"](../plan.md) · [CONVENTIONS §8.1](../CONVENTIONS.md). 패턴: [models/AUDIT-LEDGER.md](../models/AUDIT-LEDGER.md).
>
> **챕터당 절차(인용접지 파이프라인)**: MDX 이식(컴포넌트 제거) → 원자 단언 분해 → `textbook/md/` FTS5·페이지 대조 → `(source_id, p.N)` 부착 → **미매칭 단언 = 삭제 또는 source-needed 콜아웃** → validator(3종+layer lint) → 지표 기록. 부분 부착 ≠ 파일 verified. frontmatter: `layer: 1` + AI 합성 provenance.
>
> **완주 분모 = 15챕터**(00.5~15 전부, ch00 Intro 만 제외) — **F-4 사용자 확정 (a) 전부 이식**(2026-07-12; 리뷰어 양측의 (b) 도메인 축소 권고 기각). 챕터 간 유도 의존은 `depends_on` 으로 명시 가능(①→① 허용·순환 금지, CONVENTIONS §8.1).
>
> **stop/go 게이트**: T1 파일럿 지표로 장별 scope·페이스 재산정(고정 "세션당 N챕터" 없음). Codex 게이트 ⓐ(T1 후)·ⓒ(~4챕터 배치마다).
>
> **지표 정의(게이트 ⓐ 확장)**: 단언 수 / 매칭률(부착÷전체) / **anchor 정밀도**(표본 재검증에서 직접 지지 판정 비율 — 광범위 인용·적용문맥 인용은 부적정) / **수식 대조**(전사 오류 0 여부; OCR 소실 페이지는 disclosed) / **residue**(무출처 잔존 단언 수 — verified 는 0 필수) / 소요. 단언별 원장(audit table)은 후속 개선 항목.

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
| **08** | **선형 파동·분산관계** | [theory-ch08-linear-waves](notes/theory-ch08-linear-waves.md) | water-wave-mechanics(주)·holthuijsen2007 | ✅ **T1 완료**(2026-07-12, 게이트 ⓐ MODIFY 반영 재검증) | 26 | 92% (24 부착·2 삭제) · 게이트 후 anchor 정밀화 6곳·residue 2건 해소(쓰나미 p.22-23·Phillips p.173/Hasselmann p.163) → residue 0 | ~0.7h |
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
| **ⓐ T1 파일럿** (Codex 3회차, lint ⓑ 겸) | 2026-07-12 | **MODIFY→필수 6건 반영, T2 진행 가능** | 인용검증: §3 진행파 p.72-77→**p.78 §3.4.4 Eq3.40-42 정정**·선형화 페이지 분리(DFSBC p.73/KFSBC p.74)·바닥 p.63 Eq3.9 / residue 2건(쓰나미 파장·Phillips/Hasselmann) 앵커 확보 / 수식 전사 오류 0(p.78 OCR 소실은 disclosed) / lint: 전용 경로 layer·depends_on **강제**+대상 실존성+`..` 금지+scope guard **HEAD 기준** 전환+escape 감사출력. 후속 개선(비차단): 단언별 audit table·회귀테스트·동일 layer 순환 정책 |

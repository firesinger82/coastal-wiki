---
title: "XBeach 예제와 검증 자료 연결"
canonical_source: self
citation_status: verified
has_source_needed: false
verification_by: "Codex source cross-ref; Claude Sonnet adversarial review"
verification_date: 2026-09-09
verification_method: "Source and referenced-note cross-reference; independent MSI identity/disassembly where applicable"
note_author: "Codex"
note_date: 2026-09-09
---

# XBeach 예제와 검증 자료 연결

공식 예제의 입력 구성·관측 비교와 소스 테스트를 구분해 찾는 연결 문서다. 개별 실행의 성공 여부나 특정 작업 환경에서의 우선순위는 담지 않는다.

| 자료 | 확인할 내용 | 근거 노트 |
|---|---|---|
| DELILAH | 공식 예제의 2D 수리 비교 설정과 관측 자료 | [DELILAH reference](../manual-notes/02-delilah-reference.md) |
| Holland Coast | 공식 예제의 1D 폭풍·사구 침식 구성 | [Holland Coast reference](../manual-notes/03-holland-coast-reference.md) |
| 매뉴얼 예제·계수 | 문서의 버전, 입력 시간, morfac 등 조건 | [Master manual](../manual-notes/xbeach-master-manual.md) |
| 모드별 수치 구현 | stationary·surfbeat·nonh의 분기 및 지원 경로 | [Mode dispatch](xbeach_mode_dispatch.md) |
| 경계 수심 도해 | 파고/수심·상대수심·주기 범위의 설명용 그림 | [경계 도해](xbeach-boundary-limit-figures.md) |

저장소 테스트의 적용 한계는 [승인 소스 보충의 테스트 절](xbeach-source-audit-supplements.md)을, 비교 관측 자료는 위 공식 예제 노트를 따른다.

# 재판독 큐 (2026-07-28, METHOD-AUDIT-20260724.md §2 처분 4항)

EFDC·FUNWAVE·LISFLOOD-FP 의 구조 인덱스 2,248행 중 **비어 있지 않은 텍스트 2,238건 전부**가
LLM 의미 판독 미실시 → 재판독 대상. FUNWAVE 0-byte 10건은 mechanical 예외
(mechanical-exceptions-20260728.txt).

- 형식: `<axis>\t<path>` (path 는 models/ 접두 없는 정규형)
- ★새 LLM 판독은 records-structural/ 의 구조 인덱스를 **보지 않은 상태**에서 작성 (처분 5항).
  구조 인덱스는 완성 후 해시·행수·선언누락·앵커 검증용 대조에만 사용.
- 역할 배정(감사 §4): code=Claude 1차/Codex 맹검, doc=Codex 1차/Grok 맹검, web=Grok 1차/Claude 맹검.

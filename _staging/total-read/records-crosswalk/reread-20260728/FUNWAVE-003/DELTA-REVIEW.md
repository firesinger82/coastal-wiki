# FUNWAVE-003 crosswalk — blinded shard (2026-08-27)

> MERGE-PLAN §2 blinded 단일 subagent. 48파일·319 dispositions·verify PASS.

## subagent 판정
후보쌍 371: SAME 80 · CONFLICT 2 · DIFFERENT 289. findings 401 재질: HIGH 18 · MED 169 · LOW 214.
CONFLICT 2건 모두 .m/.py 스크립트(F07 num2str char-code, F27 '%.4d'%2.5 truncate vs TypeError) → conflict 처분(양쪽 자유 endpoint), 사람 확인 대상이나 스크립트 범위밖.

## dispositions (319)
distinct_unconfirmed 126 · base_only 119 · equivalent 72 (SAME 80→8 병합) · conflict 2 · confirmed_delta 0.

## delta 후보 5 (HIGH 미매칭-audit)
- **in-scope 0** — span 검토 대상 없음.
- **out-of-scope 5**: 전량 .m/.py 벤치·후처리 스크립트(절대규칙 #8). supplement 목적지 없음.
- **confirmed_delta 0**.

전체·상태: `_provenance/delta_candidates.json`.

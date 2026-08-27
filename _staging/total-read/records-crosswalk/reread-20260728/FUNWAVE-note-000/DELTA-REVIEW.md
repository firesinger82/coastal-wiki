# FUNWAVE note-000 crosswalk — blinded shard (2026-08-27)

> MERGE-PLAN §2 blinded 단일 subagent. note(문서) 축 20파일·151 dispositions·verify PASS.
> materiality 기준을 문서용으로 조정(HIGH=문서가 코드와 모순되는 공식/파라미터/인터페이스 오류).

## subagent 판정
후보쌍 15: SAME 14 · CONFLICT 0 · DIFFERENT 1. findings 165 재질: HIGH 5 · MED 135 · LOW 25.

## dispositions (151)
distinct_unconfirmed 91 · base_only 46 · equivalent 14 · confirmed_delta 1 · conflict 0.

## delta 후보 1 (HIGH)
- **confirmed 1**: `funwave-user-manual-full.md` B5 — station 출력 키를 본문 L223 단수 'STATION FILE' 로 서술하나 실제 파서 키는 복수 STATIONS_FILE (io.F:3361 `READ_STRING(...,'STATIONS_FILE',...)`). 예제 L250 은 복수로 맞음. 본문 서술이 사용자 오도. base 미검출. → confirmed_delta(코드 대조 확정).

전체·상태: `_provenance/delta_candidates.json`.

# FUNWAVE-002 crosswalk — blinded shard (2026-08-27)

> MERGE-PLAN §2 blinded 단일 subagent. 49파일·289 dispositions·verify PASS.

## subagent 판정
후보쌍 295: SAME 93 · CONFLICT 0 · DIFFERENT 202. findings 382 재질: HIGH 37 · MED 170 · LOW 175.

## dispositions (289)
distinct_unconfirmed 115 · base_only 92 · equivalent 82 (SAME 93→11 병합) · confirmed_delta 0 · conflict 0.

## delta 후보 6 (HIGH 미매칭-audit)
- **in-scope 1 → refuted**: `mkxyz_shoal_inlet_Uchannel.f` B0 — slope 분기 dep=flat*(-y/width_surf) 가 y>0 서 음수이나 이는 의도된 emergent-beach 경사(L76-78), min(dep,h)+wet/dry mask 로 처리. material delta 아님.
- **out-of-scope 5**: .m/.py 벤치·후처리 스크립트(절대규칙 #8). supplement 목적지 없음.
- **confirmed_delta 0** — 이 shard 는 material delta 없음(span-gate 로 1건 기각).

전체·상태: `_provenance/delta_candidates.json`.

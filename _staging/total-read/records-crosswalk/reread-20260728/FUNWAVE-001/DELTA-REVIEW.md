# FUNWAVE-001 crosswalk — blinded shard (2026-08-27)

> MERGE-PLAN §2 blinded 단일 subagent. 49파일·337 dispositions·verify PASS.
> 파이프라인 동일: `blind_shard.py` → fresh general-purpose subagent → `finalize_shard.py` → span 확정 → `verify_crosswalk.py`.

## subagent 판정
후보쌍 172: SAME 75 · CONFLICT 1 · DIFFERENT 96. findings 412 재질: HIGH 51 · MED 190 · LOW 171.
CONFLICT 1건(F12 [X3,Y1]: Fr 매호출 덮어씀 vs 무-wet-cell 시 stale 잔존) → 한 쪽이 SAME 소비 시 교차주석 보존, 아니면 conflict 처분.

## dispositions (337)
base_only 157 · distinct_unconfirmed 111 · equivalent 69 (SAME 75→6 병합) · confirmed_delta 1 · conflict 0/1(주석).

## delta 후보 20 (HIGH 미매칭-audit)
- **confirmed 1**: `breaker.f90` B1 — DXg/DYg(decl L112) 신규-breaking 분기서만 대입(L152-153), aging/breaking 분기는 미대입인데 xmk/ymk 가 ENDIF 밖 L221-222 무조건 사용. use-before-assign. base 미검출. → confirmed_delta.
- **pending 19**: in-scope Fortran 16 · out-of-scope 4(.m 3 + plot_current.py). in-scope 다수가 use-before-assign/INTENT(OUT)-미정의 계열(fluxes.f90 B0/B1/B2 divide-before-check·dispersive 무조건참조, wavemaker.f90 B4/B6/B9, mod_input.f90 B0, io.f90 B8 등) → supplement 게이트(§3, 누적) 이월.

전체·상태: `_provenance/delta_candidates.json`.

## 인프라 수정
`verify_crosswalk.py` — 레코드 조회를 source_sha256 키에서 **레코드 파일명 키**로 변경. 중복내용 소스(예 wvnum_omvec.m 2경로 동일내용→동일 source_sha256)에서 레코드 충돌로 인한 오탐(bytes 해시 불일치) 해소. EFDC-000·FUNWAVE-000 회귀 PASS.

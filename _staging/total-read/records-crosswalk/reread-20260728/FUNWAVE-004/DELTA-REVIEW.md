# FUNWAVE-004 crosswalk — blinded shard (2026-08-27)

> MERGE-PLAN §2 blinded 단일 subagent. 48파일·478 dispositions·verify PASS.
> ★감사 4분할 병합: audit = FUNWAVE-004(16) + 004a(11) + 004b(11) + 004c(10) = 48 (base 48 정확일치·중복0).
>   파일별 감사 run_id 는 각 crosswalk 에 보존, 매핑은 `_provenance/audit_source_manifest.json`.

## subagent 판정
후보쌍 344: SAME 98 · CONFLICT 0 · DIFFERENT 246. findings 576 재질: HIGH 101 · MED 274 · LOW 201.

## dispositions (478)
base_only 249 · distinct_unconfirmed 136 · equivalent 93 (SAME 98→5 병합) · confirmed_delta 1 · conflict 0.

## delta 후보 31 (HIGH 미매칭-audit) — 최대 산출
- **confirmed 1**: `breaker.F` B1 — DXg/DYg use-before-assign(L238-239 무조건 사용), FUNWAVE-001 breaker.f90 B1 과 동일 결함. span확정.
- **in-scope pending 25** (Fortran 모델소스) — 다수 강후보, supplement 게이트(§3) 우선 대상:
  - use-before-assign/조건정의-무조건사용: fluxes.F B0·fluxes_33v.F B0·init.F B1 (U4xL/V4yL DISPERSION-only 정의 후 무조건 참조, FUNWAVE-000 fluxes.F B0 계열)
  - wavemaker.F B4(Beta_gen 형상 NumFreq×NumDir vs beta_gen(mfreq))·B8(theta/AG [1]만 초기화)·B10(phi1 INTENT(OUT) 비주기 미정의)·B6(mfreq-1 분모 무가드)·B0/B1
  - mod_vessel.F B0(NumVessel 미대입 사용)·B1·B2, mod_meteo.F B0/B1(rollover 시 압력·형상계수 endpoint 미갱신), mod_precipitation.F B0(첫 rainfall 0 소실), mod_tracer.F B1(MPI myid==0 채움→root밖 사용), mod_sediment.F B2(Pd<0 무클램프)/B3(avalanche 누적 아닌 대입), mod_subgrid.F B1·mod_tide.F B3·sponge.F B0(Iwidth-1 분모)·io.F B0/B2
- **out-of-scope 5**: .m/.py 후처리 스크립트(절대규칙 #8).

전체·상태: `_provenance/delta_candidates.json`(review_status·canonical_scope).

## 재현 (감사 병합)
`mkdir merged; cp 004/004a/004b/004c/*.json merged/` → `blind_shard.py <base> merged FUNWAVE-004 <out>`.
검증도 merged 감사 dir 필요(verify 는 단일 audit dir 인자). manifest 로 각 파일 출처 run 추적.

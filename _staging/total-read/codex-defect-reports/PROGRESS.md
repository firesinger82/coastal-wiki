# 전 모델 감사 진행표 (단일 추적, 공정표 MODEL-AUDIT-PLAN-20260831 준거)

> 상태 기호: ⬜미착수 · 🟡진행 · ✅완료(사람게이트 통과). 단계: P0 scope→R1 1차→R2 감사→CW→SUP→V→HG.
> % = 분모(전 언어 소스파일) 대비 판독완료 파일. R1·R2 는 2 독립판독.

| 모델 | 분모(파일) | P0 | R1 | R2 | CW | SUP | V | HG | % | 상태 |
|---|---|---|---|---|---|---|---|---|---|---|
| FUNWAVE | 277 | 🟡 | ✅(코드94) | ✅ | ✅6shard | ✅ | ✅(A:HIGH0) | ✅38승인 | ~34%전체·76%코드 | 🟡(코드 실질완료·스크립트/doc 잔여) |
| EFDC | 557 | ⬜ | 🟡(EFDC-000 6 + 코어37) | 🟡(EFDC-000만) | 🟡EFDC-000 | 🟡 | ✅(HIGH3) | ✅포함 | ~8% | 🟡(코어 부분) |
| ADCIRC | 1,131 | ⬜ | 🟡(코어48) | ⬜ | ⬜ | ⬜ | ✅(HIGH12) | ⬜ | ~4% | 🟡(코어 부분·R2 없음) |
| ROMS | 4,664 | ⬜ | 🟡(코어38) | ⬜ | ⬜ | ⬜ | ✅(HIGH3) | ⬜ | ~1% | 🟡(코어 부분) |
| Delft3D | 24,748 | ⬜ | 🟡(코어34) | ⬜ | ⬜ | ⬜ | ✅(HIGH9) | ⬜ | ~0.1% | 🟡(코어 부분·third-party 미분리) |
| CADMAS-SURF | 1,310 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SFINCS | 241 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| XBeach | 102(승인) | ✅ | ✅(102/102·6shard·H260/M306/L130) | ✅(102/102·blind·H257/M303/L136) | ✅(102파일·908처분·verify PASS) | ⬜ | ⬜ | ⬜ | R1·R2·CW 100% | 🟡(CW 완료·SUP 대기) |
| SWAN | 82 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SWASH | 162 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| LISFLOOD-FP | 868 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (C/CUDA) |
| ShorelineS | 153 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (MATLAB) |
| Celeris | 164 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (WGSL/JS) |

## 완료(✅ 전건 참) 정의
분모 사람승인 + R1·R2 2독립판독 100% + CW PASS + confirmed_delta span재확인 + HIGH 적대검증 + supplement 사람승인.
현재 **어떤 모델도 완료 아님**. FUNWAVE 가 코드축 실질완료(3독립판독·신규HIGH0)로 가장 근접.

## 다음 착수
공정표 1진: **XBeach P0·R1·R2·CW 완료(2026-09-06)**. CW = blinded crosswalk(MERGE-PLAN §2): R1 696 findings ↔ R2 696 findings, 후보쌍 1,241건을 판정 전용 Codex 스레드(keymap·원본레코드·소스 접근 금지)가 SAME/CONFLICT/DIFFERENT 판정 + materiality 부여 → `finalize_shard.py` 처분 → **`verify_crosswalk.py` 6/6 PASS(유실 0·처분 전건·부모해시 정합)**.

| 처분 | 건수 |
|---|---|
| equivalent (양 리더 일치) | 440 |
| conflict (사람 확정 대상) | 2 |
| base_only (R1 단독) | 225 |
| distinct_unconfirmed (R2 단독) | 241 |
| **처분 합계** | **908** (102 파일) |

산출 `model-audit/XBeach/cw/`: `records-r1|r2/`(어댑터 `cw_adapt.py` 변환 레코드)·`blind/<shard>/{blinded_input,keymap,verdicts}.json`·`crosswalk/<shard>/*.crosswalk.json`·`crosswalk/delta_candidates-ALL.json`.

**다음 = SUP supplement**: `delta_candidates-ALL.json` 154건(HIGH 미매칭 R2 단독)의 **원문 span 재확인** → 통과분만 `confirmed_delta` 승격(제안≠확정, MERGE-PLAN §3). 이어 V(확정 HIGH 적대검증)·HG(사람 승인). ★conflict 2건은 사람 확정 대상: `wave_boundary_main.f90`(randomseed allocatable vector vs 비할당 scalar)·`morphevolution.F90`(자기보간 stale vs just-zeroed).

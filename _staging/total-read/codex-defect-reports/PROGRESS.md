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
| XBeach | 102(승인) | ✅ | ✅ | ✅ | ✅ | ✅(manifest 59·verify_supplement PASS) | ✅(407/407) | ✅(firesinger 09-07) | **100%** | ✅ **DONE** |
| SWAN | 82 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SWASH | 162 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| LISFLOOD-FP | 868 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (C/CUDA) |
| ShorelineS | 153 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (MATLAB) |
| Celeris | 164 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (WGSL/JS) |

## 완료(✅ 전건 참) 정의
분모 사람승인 + R1·R2 2독립판독 100% + CW PASS + confirmed_delta span재확인 + HIGH 적대검증 + supplement 사람승인.
**XBeach = 최초 완결 모델(2026-09-07)** — 7단계 전건 충족(분모 사람승인·2독립판독 102/102·CW verify PASS·span 재확인·HIGH 전건 적대검증·supplement 사람승인·리포트/커밋 동기). 나머지 12모델은 미완료.

## 다음 착수
**XBeach 완결(2026-09-07) — 공정표 최초의 DONE 모델.**

완결 게이트 7/7: ①분모 사람승인(102파일/71,568줄) ②R1·R2 2독립판독 각 102/102·71,568줄(real-read·blind 검증) ③`verify_crosswalk.py` 6/6 PASS(유실 0·908처분) ④confirmed_delta span 재확인(라이브 소스 재추출·해시 고정) ⑤확정 HIGH 407건 전건 적대검증 ⑥`verify_supplement_modelaudit.py` **PASS**(supplement 59, 사람승인 영수증 hash-bound, approver=firesinger≠producer) ⑦PROGRESS·리포트·커밋 동기.

산출: `model-audit/XBeach/` — R1/R2 jsonl·`cw/`(records·blind·crosswalk·v)·`XBeach-supplement-manifest.json`·`XBeach-supplement-decisions.json`·`supplement-decisions.json`(HG 패킷).
도구 추가: `cw_adapt.py`·`check_verdicts.py`·`promote_deltas.py`·`check_v.py` + corpus 상수만 바꾼 사본 `build_supplement_manifest_modelaudit.py`·`verify_supplement_modelaudit.py`(diff = EXPECT_CORPUS/provenance 3줄, 검사 로직 무변경).

**이월(완결게이트 조건 아님, 트리거형 처리)**: conflict 2건(wave_boundary_main.f90 randomseed 형·morphevolution.F90 자기보간 stale 여부) · REFUTED 인용 미검증 4건(기각 불인정 = 주장 존치).

**다음 모델 = SFINCS(241파일) P0 scope** — 1진 순서 XBeach→SFINCS→EFDC→ADCIRC.

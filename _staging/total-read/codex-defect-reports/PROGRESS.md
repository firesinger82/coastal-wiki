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
| XBeach | 102(승인) | ✅ | ✅(102/102·6shard·H260/M306/L130) | ✅(102/102·blind·H257/M303/L136) | ✅(102파일·908처분·verify PASS) | ✅(154 span확인→59 확정) | ✅(407/407 적대검증) | ⏳사용자 | 6/7 단계 | 🟡(V 완료·**HG 사용자 승인 대기**) |
| SWAN | 82 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SWASH | 162 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| LISFLOOD-FP | 868 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (C/CUDA) |
| ShorelineS | 153 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (MATLAB) |
| Celeris | 164 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (WGSL/JS) |

## 완료(✅ 전건 참) 정의
분모 사람승인 + R1·R2 2독립판독 100% + CW PASS + confirmed_delta span재확인 + HIGH 적대검증 + supplement 사람승인.
현재 **어떤 모델도 완료 아님**. FUNWAVE 가 코드축 실질완료(3독립판독·신규HIGH0)로 가장 근접.

## 다음 착수
공정표 1진: **XBeach V 적대검증 완료(2026-09-07) — 남은 것은 HG(사용자 승인) 하나.**

V = 독립 skeptic Codex 스레드가 **확정 findings 407건(confirmed_delta 66 + equivalent-HIGH 341)에 REFUTE 시도**(교차파일 중화·#ifdef·초기화 누락·인덱스 base 탐색 지시). caller 가 REFUTED 의 중화 인용문을 원문 verbatim 재대조 → 미검증 4건은 **기각 불인정**.

| V 판정 | 전체 407 | confirmed_delta 66 | equivalent-HIGH 341 |
|---|---|---|---|
| STANDS | 181 | 40 | 141 |
| NARROWED (조건 한정) | 150 | 19 | 131 |
| REFUTED (중화 인용 검증) | 72 | 7 | 65 |
| REFUTED 인용 미검증(불인정) | 4 | 0 | 4 |

적대검증 결과 반영: **confirmed_delta 66 → 59**(REFUTED 7건 rejected 강등, evidence_span 회수). 전 disposition 에 `adversarial` 필드 기록. `verify_crosswalk.py` 6/6 재PASS.

**102파일 최종 처분(908)**: equivalent 440 · base_only 225 · distinct_unconfirmed 156 · **confirmed_delta 59** · rejected 26 · conflict 2.

### HG — 사용자 승인 대기 (producer 자기승인 금지)
결정 패킷 `model-audit/XBeach/supplement-decisions.json` (모든 항목 `decision: PENDING`):
1. **confirmed_delta 59건 승격 승인** (STANDS 40 / NARROWED 19) — supplement 로 canonical 보강할 대상.
2. **conflict 2건 확정** — wave_boundary_main.f90(randomseed 형) · morphevolution.F90(자기보간 stale 여부).
3. **REFUTED 인용 미검증 4건** — 재인용 요구 / 기각 인정 / 보류 중 택일.
승인 후 PROGRESS=DONE·완결게이트 7/7 충족. **승인 전에는 XBeach 미완결.**

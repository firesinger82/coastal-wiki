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
| XBeach | 102(승인) | ✅ | ✅(102/102·6shard·H260/M306/L130) | ✅(102/102·blind·H257/M303/L136) | ✅(102파일·908처분·verify PASS) | ✅(154 span확인·confirmed_delta 66) | ⬜ | ⬜ | R1·R2·CW·SUP 100% | 🟡(SUP 완료·V 대기) |
| SWAN | 82 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SWASH | 162 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| LISFLOOD-FP | 868 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (C/CUDA) |
| ShorelineS | 153 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (MATLAB) |
| Celeris | 164 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (WGSL/JS) |

## 완료(✅ 전건 참) 정의
분모 사람승인 + R1·R2 2독립판독 100% + CW PASS + confirmed_delta span재확인 + HIGH 적대검증 + supplement 사람승인.
현재 **어떤 모델도 완료 아님**. FUNWAVE 가 코드축 실질완료(3독립판독·신규HIGH0)로 가장 근접.

## 다음 착수
공정표 1진: **XBeach P0·R1·R2·CW·SUP 완료(2026-09-06)**.

SUP = delta 후보 154건(HIGH 미매칭 R2 단독)의 **원문 span 재확인**(판정전용 Codex 스레드가 실제 소스 라인 열람 → CONFIRM 시 verbatim 인용 제출) + **caller 독립 인용대조**(인용문이 소스에 그대로 존재하는지·인용 라인 근처인지 재검증, `promote_deltas.py`). 인용대조 실패 9건은 **승격하지 않고** distinct_unconfirmed 로 남겼다(자기신고 인용 불신 원칙).

| SUP 결과 | 건수 |
|---|---|
| CONFIRM → **confirmed_delta 승격** | **66** |
| REFUTE → rejected | 19 |
| UNCERTAIN (파일 단독 판단 불가) | 60 |
| CONFIRM 주장했으나 **인용대조 실패**(미승격) | 9 |

**102파일 최종 처분(908)**: equivalent 440 · base_only 225 · distinct_unconfirmed 156 · **confirmed_delta 66** · rejected 19 · conflict 2. `verify_crosswalk.py` 6/6 재PASS.

**다음 = V 적대검증**: 대상 = confirmed_delta 66 + equivalent 중 HIGH materiality 341 = **407건**을 독립 skeptic 이 REFUTE 시도. 이어 HG(사람 승인, producer 자기승인 금지). ★사람 확정 대기: conflict 2건 + 인용대조 실패 9건(재인용 요구 여부).

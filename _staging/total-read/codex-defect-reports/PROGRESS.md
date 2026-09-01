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
| XBeach | 102(승인) | ✅ | ✅(102/102·6shard·H260/M306/L130) | ✅(102/102·blind·H257/M303/L136) | ⬜ | ⬜ | ⬜ | ⬜ | R1·R2 100% | 🟡(2독립판독 완료·CW 대기) |
| SWAN | 82 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SWASH | 162 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| LISFLOOD-FP | 868 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (C/CUDA) |
| ShorelineS | 153 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (MATLAB) |
| Celeris | 164 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (WGSL/JS) |

## 완료(✅ 전건 참) 정의
분모 사람승인 + R1·R2 2독립판독 100% + CW PASS + confirmed_delta span재확인 + HIGH 적대검증 + supplement 사람승인.
현재 **어떤 모델도 완료 아님**. FUNWAVE 가 코드축 실질완료(3독립판독·신규HIGH0)로 가장 근접.

## 다음 착수
공정표 1진: **XBeach R1+R2 완료(2026-09-01)** — 2 독립판독 성립. R1(reader A, 순방향) 102/102 H260/M306/L130 · R2(reader B, blind·역순, `_staging`/jsonl 접근 금지 프롬프트 + 롤아웃 명령 사후검증 6/6 위반 0) 102/102 H257/M303/L136. 양쪽 모두 롤아웃 nl/sed 범위 = wc -l 전량 real-read PASS. 산출 `model-audit/XBeach/XBeach-00N.jsonl`(R1)·`XBeach-00N-R2.jsonl`(R2)·병합 `XBeach-R1.jsonl`/`XBeach-R2.jsonl` + Codex 로그. 특기(양 리더 공통): wave_boundary_update.f90·wave_boundary_main.f90(분리형 wave-boundary 대체 모듈) compile-time 결함 다수 → 빌드 포함 여부를 CW 에서 분리 집계. **다음 = CW crosswalk**(blind_shard.py → 벤더라벨 제거·A/B 무작위 → equivalent/confirmed_delta → verify_crosswalk.py PASS).

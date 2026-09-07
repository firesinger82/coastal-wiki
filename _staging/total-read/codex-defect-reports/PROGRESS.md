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
| XBeach | **111**(P0 개정) | ✅ | ✅ 111/111 | ✅ 111/111 | ✅ 932처분 PASS | 🟡(manifest 60·**미승인 1**) | ✅ 415/415 | 🟡(59/60) | 판독 100% | 🟡 **DONE 취소** — P0 개정으로 재개 |
| SWAN | 82 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SWASH | 162 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| LISFLOOD-FP | 868 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (C/CUDA) |
| ShorelineS | 153 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (MATLAB) |
| Celeris | 164 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (WGSL/JS) |

## 완료(✅ 전건 참) 정의
분모 사람승인 + R1·R2 2독립판독 100% + CW PASS + confirmed_delta span재확인 + HIGH 적대검증 + supplement 사람승인.
**XBeach 는 2026-09-07 DONE 판정 후 같은 날 P0 개정으로 DONE 취소**(분모 102→111, test 9파일 편입). 신규 confirmed_delta 1건이 미승인이라 `verify_supplement` FAIL. **현재 완결 모델 0.**

## 다음 착수
### ⚠ XBeach DONE 취소 (2026-09-07) — 분모 개정
사용자 지적: **사전 배제 대신 전량 판독 후 사후 판단**. test 9파일(1,731줄)을 EXCLUDE→INCLUDE 로 이동, 분모 **102→111파일 / 73,299줄**. 신규 shard `XBeach-T00` 를 동일 파이프라인으로 전량 처리:
- R1 9/9(H0/M12/L14) · R2 blind 9/9(H0/M12/L12), real-read·blind 검증 PASS
- CW 24처분(equivalent 20·base_only 2·distinct 2) → `verify_crosswalk` PASS (전체 **932처분**)
- SUP: delta 후보 1 → **CONFIRM 1**(인용 원문대조 통과) → confirmed_delta **60**
- V: 8건 적대검증 → STANDS 3·NARROWED 5·REFUTED 0 (신규 delta 생존)
- `verify_supplement_modelaudit.py`: 기계적 검사 전건 PASS, **미승인 1건으로 FAIL**(UNAPPROVED: trunk/test/testgenmodule.F90 B8)

**★배제했으면 놓쳤을 결함 발견**: `testgenmodule.F90` L878 — 배열 `a`/`ia` 를 초기화 없이 할당하고 L910-911 에서 master 가 복사, 입력 초기화(`scattertest` L38-45)는 그 뒤에 수행 → MPI 수집 테스트가 미정의 값으로 동작(적대검증 STANDS).

### HG 재승인 대기 (1건)
`XBeach-supplement-decisions.json` 의 `trunk/test/testgenmodule.F90 B8` = `pending`. 승인 시 supplement 60 전건 PASS → DONE 복귀.

### 잔여 미판독 (P0 재승인 필요)
트리 실측 **456파일**(구 "252 inventory"는 바이너리·산문 미포함 수치). 판독 111 / **미판독 텍스트 171파일·65,693줄** / 바이너리 174.
- 미판독 텍스트: 벤더 65(mpich 40·netcdff90 13·ftnunit 11·pyconfig.h 1) · build 65 · docs 9 · generated 2 · 기타 30
- 결정 필요: ①벤더 65 분모 포함 여부(포함 시 `vendor` 태그 분리집계 권고) ②바이너리 174 처리(sha256 인벤토리 vs 판독)

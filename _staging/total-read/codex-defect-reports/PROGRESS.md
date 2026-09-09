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
| XBeach | **456**(P0 v3 전량) | ✅ | ✅ 281 2독립 + 22 단독 + 153 인벤토리 | ✅ 281/281 | ✅ 1,472처분 PASS | 🟡(delta 103·재승인 대기) | ✅ 571/571 | ⏳사용자 | **미판독 0** | 🟡 판독완주·HG 대기 |
| SWAN | 82 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SWASH | 162 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| LISFLOOD-FP | 868 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (C/CUDA) |
| ShorelineS | 153 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (MATLAB) |
| Celeris | 164 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (WGSL/JS) |

## 완료(✅ 전건 참) 정의
분모 사람승인 + R1·R2 2독립판독 100% + CW PASS + confirmed_delta span재확인 + HIGH 적대검증 + supplement 사람승인.
**XBeach 는 2026-09-07 DONE 판정 후 같은 날 P0 개정으로 DONE 취소**(분모 102→111, test 9파일 편입). 이후 P0 v3(456파일) 확대로 신규 confirmed_delta 43건이 미승인이라 `verify_supplement_modelaudit` FAIL(2026-09-09: 기계적 오류 0, 기존 승인 60건 보존). **현재 완결 모델 0.**

## 다음 착수
### XBeach — 트리 전량 456파일 판독 완주 (2026-09-07), HG 재승인만 남음
사용자 원칙(**전량 판독 → 분류 → 사후 판단**)에 따라 P0 v3 로 분모를 트리 전체로 확대. **미판독 0.**

| 처리 | 파일 | 방식 |
|---|---|---|
| 2독립판독 + CW·SUP·V | **281** | R1/R2 blind → crosswalk → span 확인 → 적대검증 (13 shard) |
| 단독판독 | **22** | 도해 8(시각 판독) · 문서 14(PDF→opendataloader-pdf, Office→docx/OLE 변환 후 판독) |
| 메타데이터 인벤토리 | **153** | 컴파일 산출물(.dll 72·.lib 26·.exe 20·.mod 13·.pyd 10·.jar 8 등) sha256·타입·버전문자열 |
| **합** | **456** | 트리 전량 |

**281파일 처분 1,472건**: equivalent 682 · confirmed_delta **103** · base_only 335 · distinct_unconfirmed 319 · rejected 30 · conflict 3. `verify_crosswalk.py` 13/13 PASS.
**V 적대검증 571건**(407+164): STANDS 305 · NARROWED 178 · REFUTED 78 · 인용미검증 10(기각 불인정).
**신규 그룹 특기**: 벤더(mpich·netCDF·ftnunit) findings 는 `vendor` 태그 분리집계 대상 — XBeach 결함으로 집계 금지. 빌드 스캐폴딩 shard 는 두 리더 편차가 커(B00 HIGH 0 vs 16) CW 에서 distinct 로 다수 잔류.
**문서축 수확**: 매뉴얼·비정수압 보고서에서 인용 가능한 정량 사실 HIGH 207건. 도해 5장은 **모드별 적용한계 판정도**(NH 1층 kh≲1.0-1.1 / NH+ 2층 kh≈3.0-3.5).

**모델 배분**(2026-09-09 사용자 지시): Astra는 가장 높은 추론이 필요한 판단에 한정하고, 일반 판독·정리는 하위 모델을 최대한 활용한다. Claude는 적대적 검토자로 활용한다. 결정론적 복사·해시·집계는 스크립트로 처리한다. ★기존 111파일의 R1·R2 는 `--model` 미지정으로 `gpt-5.6-sol` 에서 수행됨(사후 실사로 확인, 재판독 불요 판정).

### ★ Codex 인수인계서
`model-audit/XBeach/HANDOFF-CODEX.md` (2026-09-09) — 남은 HG 절차 5단계(records-by-run 12개 복사 → 신규 43건 evidence_span 정규화 → manifest 재작성 → 영수증 재생성 → 사용자 승인 → 게이트), 게이트 무결성 원칙, 이번 세션에 밟은 함정 7종(--model/--write 생략·경로 기준·PDF 처리 등), 도구 49개 위치, 이월 5건.

### HG 재승인 대기
분모 확대로 confirmed_delta 60 → **103**(신규 43). **2026-09-09 준비 완료**: records-by-run 12개 디렉터리·340개 레코드 복사, 신규 evidence_span 43건 원본 해시·제출 인용 대조 후 정규화, manifest·영수증 재생성. 기존 60개 영수증의 승인 정보와 해시 전체 보존, 신규 43개 pending. Crosswalk 13/13 PASS; supplement gate `authority=103 approved=60 pending=43 mechanical_fails=0` — 사람 승인 미충족으로 FAIL.

[사용자 승인 목록: 파일·라인·한국어 요약·감사 원문·소스 인용 43건](../model-audit/XBeach/HG-REVIEW-20260909.md). 외부 구성요소 관련 항목은 목록에서 별도 표시하며 전체 vendor 태깅 완료와 구분한다. 승인 전 XBeach 미완결; SFINCS P0는 HG 통과 후 착수한다.


2026-09-09 Claude 적대적 검토 반영: form-feed 이후 9건의 실제 LF 라인과 레거시 게이트 좌표를 분리 명시(게이트 무수정), NARROWED 6건의 적용 조건·근거 공개, 외부 구성요소 31 / 자체 빌드·배포 12로 승인 목록 분류 정정, 생성 makefile 중복·CRLF 바이트 근거·심각도 공개. [검토 원문](../model-audit/XBeach/HG-ADVERSARIAL-20260909.md) · [라인 좌표 대응](../model-audit/XBeach/HG-LINE-MAPPING-20260909.json) · [기계 검증 기록](../model-audit/XBeach/HG-PREPARATION-CHECKS-20260909.json). 기존 60건 보존과 신규 43건 pending 유지.

Claude Sonnet 5의 [한정 재검토](../model-audit/XBeach/HG-ADVERSARIAL-RECHECK-20260909.md)에서 B1·B2 해소 확인. 실제 LF span 43/43 원문 일치, STANDS 37·NARROWED 6 공개. 사람 승인은 별도 대기.

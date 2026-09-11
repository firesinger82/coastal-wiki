# 전 모델 감사 진행표 (단일 추적, 공정표 MODEL-AUDIT-PLAN-20260831 준거)

2026-09-10 다운 후 복구·후속 판독: XBeach 원본 543개·기존 불변 기록 292개·ZIP/JAR member 1,722개 해시 대조 통과. Office 5문서 36페이지와 Jumpshot PDF 61페이지를 보충 판독했고, workbook 수식 1개를 복원했다. MSI 123개 내부 파일을 재추출·검증하고 PE/AR 59개 인터페이스 인덱스를 저장했다. 보충 근거는 27개 원본 경로에 연결했다. 매뉴얼·보고서 9개 경로의 수식·도표 손실과 바이너리 내부 미판독을 유지하며 전체 판독 gate는 NOT_PASSED. [복구 지점](../model-audit/XBeach/connectivity/RESUME.md).

## 2026-09-09 사용자 지정 후속 단계: XBeach → FUNWAVE 연결 분석

전수 판독을 먼저 마친 뒤 파일 사이 계산 흐름을 별도로 검토한다. **XBeach의 파일별 감사·이월·canonical 완료 기록은 유효하지만, 모델 전체 연결 분석은 진행 중이다. FUNWAVE는 판독 누락 재확인·보충이 선행된다.** 기존 표의 DONE/승인 수는 해당 과거 파일별 감사 단계의 상태이며 새 연결 분석 완료나 승인을 뜻하지 않는다.


| 모델 | 판독 전제 | 전수 판독 | 연결 검토 | 검증 | canonical | 신규 HG |
|---|---|---|---|---|---|---|
| XBeach | JAR 내부 자료 누락 확인·보충 중 | 재확인 중, 완료 아님 | 판독 gate까지 확정 보류 | 미착수 | 새 연결 분석 미반영 | 미발급 |
| FUNWAVE | 읽기 전용 인벤토리 준비 | XBeach 완료 후 | XBeach 완료 후 | 미착수 | 새 분석 미반영 | 미발급 |

증거: `_staging/total-read/model-audit/XBeach/connectivity/`, `_staging/total-read/model-audit/FUNWAVE/connectivity-preflight/`. 아래 과거 공정표의 “미판독 0”은 컨테이너 내부 의미 판독까지 입증하지 못하므로 이번 전수 판독 완료 근거로 사용하지 않는다.

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
| XBeach | **456**(P0 v3 전량) | ✅ | ✅ 281 2독립 + 22 단독 + 153 인벤토리 | ✅ 281/281 | ✅ 1,472처분 PASS | ✅ delta 103 PASS | ✅ 571/571 | ✅ 103승인 | **미판독 0** | ✅ DONE 2026-09-09(P0 v3) |
| SWAN | 82 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| SWASH | 162 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ |
| LISFLOOD-FP | 868 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (C/CUDA) |
| ShorelineS | 153 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (MATLAB) |
| Celeris | 164 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0% | ⬜ (WGSL/JS) |

## 완료(✅ 전건 참) 정의
분모 사람승인 + R1·R2 2독립판독 100% + CW PASS + confirmed_delta span재확인 + HIGH 적대검증 + supplement 사람승인.
**현재 완결 모델 1: XBeach(P0 v3, 2026-09-09).** 2026-09-07의 구 분모 DONE은 범위 확대 때문에 취소됐으며, P0 v3 트리 전량 456파일 처리 후 2026-09-09 사용자가 신규 supplement 43건의 감사 기록 편입을 명시 승인했다. 기존 60건과 합쳐 `approved=103 pending=0 mechanical_fails=0`, `verify_supplement_modelaudit` **PASS**. 완료 범위는 아래 P0 v3 처리 방식(281 2독립·22 단독·153 인벤토리)이며 456개 모두의 2독립 의미 판독이나 이월 문제 해결을 뜻하지 않는다.

## 다음 착수
**SFINCS P0 scope** — 사전 배제 없이 트리 전량을 인벤토리화하고 파일별 처리 유형을 분류한다. 기존 241은 이전 소스 집계이므로 전량 분모로 가정하지 않는다. 분모 확정은 별도 사람 게이트를 따른다.

### XBeach — 이월·canonical 후속 정리 완료 (2026-09-09)

사용자 요청으로 이월5종도 정리했다. 원문 대조 후 충돌3·미검증반증10의 최종 판정과 canonical 연결, 456파일/1,472처분 vendor·역할·형태 분류, 문서207건의 판본별 채택·모순보존·변환손상 제외를 마쳤다. 승인 보충103건은 모두 개별 canonical 앵커로 연결했다. `models/XBeach/README.md`, `models/AUDIT-LEDGER.md`, `INDEX.md`는 현재 분모와 노트수(SA37/MN7/web1)를 반영한다. [완료·검토·검증 원장](../model-audit/XBeach/closure/README.md).

MPI2 후속 판정 중 Clone의 초기 DLL 동일성 오판은 MSI File 테이블과 실제 dispatcher 역어셈블리로 교정했다. 과거 반증 원장은 남기고 최종 override가 우선하도록 연결했다. “정리 완료”는 감사와 지식 반영이며 원본 모델의 결함 패치를 뜻하지 않는다.

### XBeach — P0 v3 완료 (2026-09-09)
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

### HG 준비 이력 (승인 전 스냅샷)
분모 확대로 confirmed_delta 60 → **103**(신규 43). **2026-09-09 준비 완료**: records-by-run 12개 디렉터리·340개 레코드 복사, 신규 evidence_span 43건 원본 해시·제출 인용 대조 후 정규화, manifest·영수증 재생성. 기존 60개 영수증의 승인 정보와 해시 전체 보존, 신규 43개 pending. Crosswalk 13/13 PASS; supplement gate `authority=103 approved=60 pending=43 mechanical_fails=0` — 사람 승인 미충족으로 FAIL.

[사용자 승인 목록: 파일·라인·한국어 요약·감사 원문·소스 인용 43건](../model-audit/XBeach/HG-REVIEW-20260909.md). 외부 구성요소 관련 항목은 목록에서 별도 표시하며 전체 vendor 태깅 완료와 구분한다. 이 문서는 승인 직전 스냅샷으로 해시를 고정했으며 수정하지 않는다. 현재 승인 결과는 아래 HG 완료 기록을 따른다.


2026-09-09 Claude 적대적 검토 반영: form-feed 이후 9건의 실제 LF 라인과 레거시 게이트 좌표를 분리 명시(게이트 무수정), NARROWED 6건의 적용 조건·근거 공개, 외부 구성요소 31 / 자체 빌드·배포 12로 승인 목록 분류 정정, 생성 makefile 중복·CRLF 바이트 근거·심각도 공개. [검토 원문](../model-audit/XBeach/HG-ADVERSARIAL-20260909.md) · [라인 좌표 대응](../model-audit/XBeach/HG-LINE-MAPPING-20260909.json) · [기계 검증 기록](../model-audit/XBeach/HG-PREPARATION-CHECKS-20260909.json). 당시 기존 60건 보존과 신규 43건 pending 유지.

Claude Sonnet 5의 [한정 재검토](../model-audit/XBeach/HG-ADVERSARIAL-RECHECK-20260909.md)에서 B1·B2 해소 확인. 실제 LF span 43/43 원문 일치, STANDS 37·NARROWED 6 공개. 이후 아래 명시 승인으로 HG를 마쳤다.

### HG 완료 — 2026-09-09

사용자 `승인` 응답으로 신규 43개 영수증에 `firesinger`, 승인일, 승인 직전 검토 문서 SHA-256을 기록했다. 기존 60개 영수증은 모든 필드 그대로 보존했다. 최종 게이트 **PASS: authority=103 approved=103 pending=0 mechanical_fails=0**. [승인·게이트 실행 기록](../model-audit/XBeach/HG-APPROVAL-20260909.json).

이월 5종(conflict 3·REFUTED 인용 미검증 10·전체 vendor 태깅·문서 정량사실 207·AUDIT-LEDGER 구 감사 표기)은 계속 열려 있다. 이번 승인은 감사 기록 편입이며 canonical 반영·이월 종결을 포함하지 않는다. `models/`와 게이트 코드는 변경하지 않았다.

2026-09-10 비정수압 보고서 시각 보충: 원 PDF 69쪽은 기존 13–68쪽 판독 기록과 신규 1–12·69쪽을 결합해 전 페이지 근거를 연결했다. DOC는 별도 렌더 70쪽의 표시 내용을 확인했으나 수식 참조 공백·묶음 기호 깨짐이 남아 `all-render-pages-inspected-with-unresolved-rendering-fidelity`다. 원시 Equation Native 388개는 인벤토리만 작성했다. 새 페이지 이미지 83개와 DOC 렌더 PDF를 저장했고 구조·SHA 검증 178개 PASS. 전체 판독 gate는 NOT_PASSED, 신규 사람 승인 없음. 상세·다음 단계: [재개 지점](../model-audit/XBeach/connectivity/RESUME.md), [판독 기록](../model-audit/XBeach/connectivity/nonhydro-read/read-receipt.json).

2026-09-10 DOC 수식 복원 후속: 기존 로컬 수식 글꼴을 임시 적용해 관측된 묶음 기호 깨짐을 복원했다. 원본 WordDocument main-text piece에서 MathType 필드 167개(중첩 1개)를 해시·바이트 좌표로 결속하고 outer 166개 중 165개 저장 표시값을 검토 사본에 복원했다. 1개는 원본 캐시도 비어 있다. DOCX의 나머지 ZIP member는 동일 바이트이며 복원 재현·PDF 표시값 출현 횟수를 검증했다. 복원 PDF 71쪽 중 신규 시각 확인은 13·32·33쪽으로 한정, 원시 수식 오브젝트와 전체 자료 판독 gate는 미완료. [복원 근거](../model-audit/XBeach/connectivity/nonhydro-read/field-recovery/receipt.json).

2026-09-11 PDF 판독 보충·복원본 검증: Kingsday 신규 105쪽, Master 신규 108쪽을 시각 확인하고 기존 process chapter 근거와 합쳐 각각 전체 141·145쪽에 결속했다. 원본 오류와 판본 차이는 별도 기록했다. 보고서 복원본의 장 제목→그림 번호 치환 오류는 본문 필드만 고정해 해소했고, 71쪽 전체 본문 판독 및 최종본과의 본문 픽셀 일치를 확인했다. 원본 543개·불변 기록 292개 SHA 유지, 구조 검증 213개 PASS. 두 DOCX 독립 렌더와 보고서 잔여 글리프/원시 수식, 외부 바이너리 내부 판독 범위는 계속 열려 있다. 전체 gate NOT_PASSED·신규 사람 승인 없음. [재개 지점](../model-audit/XBeach/connectivity/RESUME.md), [매뉴얼 판독](../model-audit/XBeach/connectivity/manuals-visual-read/read-receipts.json), [후속 복원 근거](../model-audit/XBeach/connectivity/nonhydro-read/body-field-recovery/receipt.json).

2026-09-11 DOCX 독립 렌더 전제 보완: 직접 변환의 장 제목→그림 번호 치환과 MathType 명령 노출을 확인하고, 원본 OOXML에 저장된 표시값 516개(Kingsday 251·Master 265)를 별도 사본에 복원했다. 각 문서의 원래 빈 필드 4개는 유지했다. 단순 필드 제거로 번호가 사라지는 중간 실패본도 비교 자료로 남겼다. 최종본은 145·148쪽으로 렌더링했으며 이번 시각 판독은 각각 5쪽, 총 10쪽에 한정된다. Master 식 (2.1)의 Writer 본체 누락은 원본 EMF 별도 렌더로 보충했다. ZIP member 1,092개와 OLE 486개의 stream 인벤토리·복원 재현·표시값 출현·원본 543개/불변 292개 보존을 포함해 구조 검증 270개 PASS. DOCX 전체 시각 판독·원시 수식 판독은 계속 열려 있으며 전체 gate NOT_PASSED·신규 사람 승인 없음. [복원/진단 근거](../model-audit/XBeach/connectivity/manuals-docx-read/receipt.json), [재개 지점](../model-audit/XBeach/connectivity/RESUME.md).

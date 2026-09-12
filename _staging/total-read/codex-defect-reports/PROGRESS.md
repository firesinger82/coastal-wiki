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

2026-09-11 DOCX 전체 시각 판독 보충: 기존 10쪽에 Kingsday 신규 140쪽·Master 신규 143쪽을 더해 독립 렌더 전체 145·148쪽의 시각 확인을 연결했다. 신규 PNG 283개와 회전 의사결정도 2개, 관측 기록을 저장했다. Master (2.40)/(2.43)은 본문 누락을 원본 EMF 별도 렌더로 보충했고, Kingsday (2.38)은 원본 WMF도 빈 렌더라 미해결로 남겼다. Kingsday (2.27)/(2.41)/(2.42)의 원본 문단에는 수식 본체가 없음을 문단 XML로 한정 확인했다. 이전 부분 판독 영수증은 보존했다. 원본 543개·불변 기록 292개 SHA 유지, 구조 검증 306개 PASS. 작은 글리프·OLE 원시 수식과 외부 바이너리 내부 범위는 계속 열려 있다. 전체 gate NOT_PASSED·신규 사람 승인 없음. [전체 시각 판독 근거](../model-audit/XBeach/connectivity/manuals-docx-read/full-visual-read/README.md), [재개 지점](../model-audit/XBeach/connectivity/RESUME.md).

2026-09-11 Native 수식 공백 대조: Kingsday (2.38)의 Equation Native 221바이트를 한정 판독해 설정 레코드 뒤 END만 있고 수식 본체가 없음을 확인했다. 같은 MTEF 본문을 가진 공백 문단 오브젝트 4개도 원본에 결속했다. 두 DOCX의 (2.5)–(2.8), B.37/C.37 원본 WMF 10개를 별도 렌더·확인했고 네모 위첨자와 0a 표시는 계속 남는다. 신규 판독은 5개 스트림의 본체 부재 확인이며 나머지 DOCX OLE 481개·보고서 Equation Native 388개는 의미 판독 미완료다. 원본 543개·불변 기록 292개 유지, 절단·미지원/본체 삽입·종료 뒤 데이터 거부 검사를 포함해 구조 검증 362개 PASS. 전체 gate NOT_PASSED·신규 사람 승인 없음. [한정 판독 근거](../model-audit/XBeach/connectivity/manuals-docx-read/native-probe/README.md).

2026-09-11 Native 글리프 한정 판독: 두 DOCX의 (2.5)와 B.37/C.37, 총 4개 수식의 원본 스트림을 구조·문자 단위로 판독했다. 네모 위첨자 위치에는 MTCode 0x223C(∼)가 저장되어 있고, 0a의 a 역시 원본 CHAR 레코드다. 렌더 실패의 정확한 원인과 a의 수학적 의도는 미확정이다. 원본 543개·불변 기록 292개 유지, 선택 수식 원본 재추출·구조/문자 위치 및 절단·변조 검사를 통합했다. DOCX OLE 477개의 구조 판독, 선택 수식의 의미 검증 등은 계속 열려 있으며 전체 gate NOT_PASSED·신규 사람 승인 없음. [문자 판독 근거](../model-audit/XBeach/connectivity/manuals-docx-read/glyph-record-read/README.md).

2026-09-11 Native 판독기 전량 적용 범위 조사: DOCX OLE 486개 중 301개 기계적 수용·185개 거부를 원본 SHA와 오류 좌표로 기록했다. 수용을 의미 판독 완료로 승격하지 않았다. Kingsday p.15의 o는 본문 문자가 없는 원본 목록 문단의 글머리표(numFmt=bullet, lvlText=o)임을 원본 XML과 페이지 이미지로 확인했다. 다음은 거부 항목의 접두부·미지원 옵션/레코드 분류 및 개별 식의 원문/렌더 대조다. 전체 gate NOT_PASSED·신규 사람 승인 없음. [조사 근거](../model-audit/XBeach/connectivity/manuals-docx-read/NATIVE-SURVEY.md).

2026-09-11 Native 접두부 경계 조사: 설정 파서로 유일한 본체 시작 위치를 검증해 offset 218/219/220/228/229를 구분했다. 기존 본체 파서 수정 없이 이전 거부분 60개를 추가 수용, 총 361개 기계적 수용·본문 미지원 122개·접두부 미해결 3개다. 의미 판독 완료로 승격하지 않았다. 기존 원본·영수증 유지, 전체 gate NOT_PASSED·신규 사람 승인 없음. [경계 조사 근거](../model-audit/XBeach/connectivity/manuals-docx-read/NATIVE-PREFIX-SURVEY.md).

2026-09-11 Native 문자 장식 지원: 공식 MTEF5 형식을 대조해 CHAR 장식 목록과 nudge 없는 EMBELL의 한정 판독기를 별도로 추가했다. 80개 추가 수용으로 441개 기계적 수용·본문 미지원 42개·접두부 미해결 3개다. 기존 수용 361개의 구조 출력 동일, 원본 및 과거 영수증 보존. 의미/렌더 검증은 별도이며 전체 gate NOT_PASSED·신규 사람 승인 없음. [장식 판독 근거](../model-audit/XBeach/connectivity/manuals-docx-read/NATIVE-EMBELL-SURVEY.md).

2026-09-11 Native 배치 레코드 지원: 행렬·RGB·SIZE·명시적 RULER의 한정 지원으로 18개 추가 수용, 총 459개 기계적 수용·본문 미지원 24개·접두부 미해결 3개다. 색상 인덱스 0의 의미를 가정하지 않아 12개는 미해결로 남겼다. 기존 441개 출력 동일·원본/과거 기록 보존, 전체 gate NOT_PASSED·신규 사람 승인 없음. [배치 판독 근거](../model-audit/XBeach/connectivity/manuals-docx-read/NATIVE-LAYOUT-SURVEY.md).

2026-09-11 사용자 요청으로 XBeach 마무리 GOAL 활성화. Native 이동 보정의 2/6바이트 및 LINE 간격 판독을 추가해 463개 기계적 수용·미해결 23개, 통합 구조 검증 457개 PASS. 기존 459개 출력과 원본·과거 기록 보존. 전체 판독/연결/canonical/필요 HG는 미완료이며 GOAL active. [전체 추적](../model-audit/XBeach/connectivity/GOAL-STATUS.md), [이동 보정 근거](../model-audit/XBeach/connectivity/manuals-docx-read/NATIVE-NUDGE-SURVEY.md).

2026-09-11 Master 확장 접두부·보고서 Native 조사: Master 3개는 길이 3의 FUTURE payload를 보존한 채 offset 204에서 본문을 판독했으며 payload 의미는 미확정이다. 보고서 DOC의 388개 Native는 386개 구조 판독·2개 본문 인코딩 정의 미지원으로 분류했다. 통합 검증 473개 PASS, 원본·기존 기록 보존. 수학적 의미/렌더 충실도·전체 판독 gate는 여전히 미완료이며 GOAL active. [Master 근거](../model-audit/XBeach/connectivity/manuals-docx-read/NATIVE-FUTURE-PROBE.md), [보고서 근거](../model-audit/XBeach/connectivity/nonhydro-read/NATIVE-SURVEY.md).

2026-09-11 보고서 Native 본문 글꼴 정의 지원: 두 미지원 스트림의 인코딩·글꼴·스타일 정의를 읽어 보고서 388개 전체가 기계적으로 판독된다. 이전 386개 출력 동일, 두 F093 글리프의 시각/의미는 미확정. 통합 검증 485개 PASS, 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/nonhydro-read/NATIVE-FONT-SURVEY.md).

2026-09-11 매뉴얼 색상·정렬 예외 진단: 8개 태그 없는 탭 목록 해석 및 12개 색상 0 미해석 보존으로 20개 조건부 구조를 확보했다. strict 거부는 유지하며 23개(opaque 3 포함)의 해석/렌더 조건은 미해결이다. 전체 486개 구조 대응을 확보했고 통합 검증 530개 PASS. 전체 gate NOT_PASSED·GOAL active. [진단 근거](../model-audit/XBeach/connectivity/manuals-docx-read/NATIVE-CONDITIONAL-PROBE.md).

2026-09-12 조건부 Native 수식 20개의 원본 WMF를 문단·관계 ID에 결속해 전량 렌더/시각 확인했다. 새 네모 글리프는 관측하지 않았지만 세 침투식의 분수 뒤 1 앞 연산자 부재를 Native CHAR와 함께 확인했고 Kingsday 대응식의 +1과 구분했다. 원본 표기를 수정하지 않았으며 조건부 해석/수학적 검증은 미완료. 전체 gate NOT_PASSED·GOAL active. [시각 대조 근거](../model-audit/XBeach/connectivity/manuals-docx-read/conditional-visual-read/README.md).

2026-09-12 침투식 구현 대조: 원본의 연산자 부재를 groundwater.F90의 +1 불포화 침투 관계·실제 양의 근 계산과 대조했다. 임계 셀 가드·암시적 침투층·시간 비율·가용 표층수 제한을 구분했고 원본 문서를 자동 수정하지 않았다. 원문 SHA/구간·대수 검산 포함 통합 564개 PASS. 전체 gate NOT_PASSED·GOAL active. [비교 근거](../model-audit/XBeach/connectivity/INFILTRATION-DOCUMENT-CODE-COMPARISON.md).

2026-09-12 바이트코드 판독 시작: 아카이브 unread 1,284경로를 Java 413종/Python 150종에 결속했다. Java 87,653줄 역어셈블리 자료를 저장하고 launcher 4종의 전체 표시 명령을 직접 읽어 동일 SHA 12경로에 연결했다. Java 409종·Python 150종은 미판독. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/README.md).

2026-09-12 base/io 9종 465줄 직접 판독·54경로 결속. 누적 Java 13/413종(66경로), 나머지 Java 400종/Python 150종 미판독. 문자열 길이·빈 값 반환·제한 읽기 동작 및 Header 호출 구간을 기록했다. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/base-io-read.json).

2026-09-12 SLOG2 헤더·디렉토리 7종 전체 판독: 저장 필드 순서, 버전 검사 분리, map/list 재읽기와 root 갱신 범위를 기록했다. 누적 Java 20/413종·남은 Java 393종/Python 150종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/slog2-header-read.json).

2026-09-12 TreeNodeID 5종 전체 판독: 부모·형제 이동, root/leaf 조건, 두 comparator의 공통 depth 내림차순과 xpos 방향 차이를 기록했다. 누적 Java 25/413종(138경로). 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/slog2-node-read.json).

2026-09-12 TraceName/Permutation/순회기 7종 전체 판독: 확장자 변환, 자리수 열거, 시간 필터 및 복합 객체 순회 흐름을 기록했다. 누적 Java 32/413종, 남은 Java 381종/Python 150종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/slog2-iteration-read.json).

2026-09-12 시간 경계/좌표 11종 전체 판독: 구간의 끝점 포함·교집합·제한적 remove, 4개 비교기의 동률 처리, 좌표 직렬화를 기록했다. 누적 Java 43/413종, 남은 Java 370종/Python 150종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/time-coord-read.json).

2026-09-12 Drawable/비교기/Topology 3종 전체 판독: 동률 처리에 따른 TreeSet 비교 동등 조건, 표시/선택 분기, exclusion 계산을 기록했다. 누적 Java 46/413종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/drawable-order-read.json).

2026-09-12 InfoBox 전체 판독: 누락 범주의 기본 State 생성, 정보 버퍼의 지연 해석과 종료 경로, 직렬화 및 재읽기 상태를 기록했다. 누적 Java 47/413종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/infobox-read.json).

2026-09-12 InfoType/InfoValue 전체 판독: 태그 8종, 타입 포함 IO와 값 전용 IO, wrapper 검사와 알 수 없는 태그 예외를 기록했다. 누적 Java 49/413종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/info-value-read.json).

2026-09-12 NestingStacks/DrawnBox/DrawnBoxSet 전체 판독: 스택 포함 조건과 계수 반환, 1픽셀 비교 규칙 및 행별 저장 구조를 기록했다. 누적 Java 52/413종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/nesting-drawn-read.json).

2026-09-12 SLOG2 객체 버퍼 3종 전체 판독: 34바이트 공통 헤더와 두 목록 IO, 정렬 상태/크기 누계/태그 처리 조건을 기록했다. 누적 Java 55/413종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/drawable-buffer-read.json).

2026-09-12 LineIDMap/Method 전체 판독: 계층 배열 매핑, YCoordMap 변환의 크기 처리, 직렬화와 Method 식별자를 기록했다. 누적 Java 57/413종. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/lineid-method-read.json).

2026-09-12 YCoordMap 전체 판독 및 영수증 기반 누적 집계 추가. Java 58/413종·336경로 판독 근거, Java 355종/Python 150종 미판독. 전체 gate NOT_PASSED·GOAL active. [근거](../model-audit/XBeach/connectivity/bytecode-read/coverage.json).

- XBeach BufForShadows 750줄 판독: 집계 키, 병합 크기, write/empty 상태 의존성을 기록했다. 누적 Java 59종/342개 경로, 잔여 Java 354종·Python 150종. 전체 gate NOT_PASSED.

- XBeach Shadow 1425줄 전체 판독 및 BufForShadows 위임 연결 기록. 누적 Java 60종/348경로, 잔여 Java 353종·Python 150종. 전체 의미 승인 미발급.

- XBeach category weight 계열 10종/909줄 판독. 비율 연산·직렬화·resolve 반환과 Shadow 연결 기록. 누적 Java 70종/408경로, 잔여 Java 343종·Python 150종. 전체 승인 미발급.

- XBeach Primitive 전체 955줄 판독 및 Shadow 복사/집계 연결 기록. 누적 Java 71종/414경로, 잔여 Java 342종·Python 150종. 전체 승인 미발급.

- XBeach Composite/iterator 2종·1049줄 판독. 비중첩 iterator의 인덱스 미증가 경로 기록. 누적 Java 73종/426경로, 잔여 Java 340종·Python 150종. 전체 승인 미발급.

- XBeach output TreeNode 전체 619줄 판독. Composite 분해 및 shadow lifecycle 연결. 누적 Java 74종/430경로, 잔여 Java 339종·Python 150종. 전체 승인 미발급.

- XBeach TreeTrunk/OutputLog 2종·723줄 판독. 정상 출력의 가중치 초기화/병합/shift/저장/empty 연결. 누적 Java 76종/438경로, 잔여 Java 337종·Python 150종. 전체 승인 미발급.

- XBeach Clog2ToSlog2 764줄 판독. 기본 시간 검사 off와 EOF flush/close 연결. 누적 Java 77종/442경로, 잔여 Java 336종·Python 150종. 전체 승인 미발급.

- XBeach ClogToSlog2 전체 750줄 판독. CLOG2와의 YCoordMap 및 decoder 차이 기록. 누적 Java 78종/446경로, 잔여 Java 335종·Python 150종. 전체 승인 미발급.

- XBeach InputAPI/Kind 2종·172줄 판독. 값 동등성과 converter identity 분기 연결. 누적 Java 80종/458경로, 잔여 Java 333종·Python 150종. 전체 승인 미발급.

- XBeach TraceToSlog2 864줄 판독. Composite·filespec·native 경계 기록. 누적 Java 81종/462경로, 잔여 Java 332종·Python 150종. 전체 승인 미발급.

- XBeach trace 입력 래퍼 2종·236줄 판독. Kind identity 연결 및 native 미판독 경계 명시. 누적 Java 83종/466경로, 잔여 Java 330종·Python 150종. 전체 승인 미발급.

2026-09-12 CLOG2 InputLog와 TopologyIterator/YCoordMapIterator 전체 437줄 판독. 정적 Kind 반환 및 topology→content→좌표 맵 전환과 최초 arrow category 특례를 확인했다. ContentIterator 본문과 superclass는 미판독으로 남긴다. 누적 Java 86/413종·472경로, 잔여 Java 327종/Python 150종. 구조 검증은 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 ContentIterator 전체 1,193줄 판독. hasNext가 레코드를 소비하고 next가 저장 객체를 반환하는 계약, Category/Primitive만 생성하는 경로, reflective handler 오류 처리와 미매칭 통계의 중복 집계 가능성을 기록했다. 저수준 레코드·Topo 매칭·ID 맵은 별도 미판독이다. 누적 Java 87/413종·474경로, 잔여 Java 326종/Python 150종. 독립 의미 검증·HG와 구분한다.

2026-09-12 CLOG2 상태/화살표 매칭과 지원 클래스 7종 전체 791줄 판독. 상태 FIFO 매칭, 실패한 종료 이벤트의 예외 전달, 메시지 수신 선행 시 크기 0 저장 경로를 확인했다. 원본은 수정하지 않았다. 누적 Java 94/413종·488경로, 잔여 Java 319종/Python 150종. ID 맵과 저수준 레코드는 별도 미판독이다. 근거: `clog2-matching-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 ID 맵·ID 값·LineID 3종 전체 586줄 판독. 사용 항목 필터와 두 좌표 보기 생성, ID 누락 시 경고 후 null 참조, 전역 크기 기반 ID 계산의 무검사 정수 연산을 확인했다. 누적 Java 97/413종·494경로, 잔여 Java 316종/Python 150종. 저수준 레코드와 preamble 초기화는 별도 미판독이다. 근거: `clog2-idmap-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 RecHeader/RecMsg/RecBare/RecCargo 4종 전체 517줄 판독. 읽기 실패 시 부분/이전 필드 보존과 상위 반환값 미검사, skip 길이 미검사, Cargo의 매회 새 배열 할당을 확인했다. 누적 Java 101/413종·502경로, 잔여 Java 312종/Python 150종. stream/preamble 및 다른 레코드는 별도 미판독이다. 근거: `clog2-record-input-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 InputLog/MixedDataInputStream/Preamble 3종 전체 943줄 판독. preamble 실패 반환값 무시와 전역 ID 설정 누락 가능성, 짧은 블록 EOF 처리, 고정 문자열 NUL 조건을 연결했다. 누적 Java 104/413종·508경로, 잔여 Java 309종/Python 150종. 다른 레코드와 상수는 별도 미판독이다. 근거: `clog2-stream-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Const/RecComm/UUID 3종 전체 352줄 판독. 빈 호환 버전 목록, UUID 내부 읽기 실패에도 RecComm이 48을 반환하는 경로, CommFree와 UUID가 ID 맵 삭제/키에 쓰이지 않는 연결을 확인했다. 누적 Java 107/413종·514경로, 잔여 Java 306종/Python 150종. 근거: `clog2-comm-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 RecColl/RecDefConst/RecSrc/RecTshift 4종 전체 380줄 판독. 본문 converter가 집단통신·상수 이름·소스 위치·시간 이동 body를 건너뛰는 경로와 실제 skip 길이 미검사를 연결했다. 누적 Java 111/413종·522경로, 잔여 Java 302종/Python 150종. 근거: `clog2-skipped-records-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 상태/이벤트/메시지 정의와 ObjDef 4종 전체 552줄 판독. 임시 이벤트 ID 생성, stateID와 Category 번호의 분리, 메시지 형식과 정보 버퍼의 연결을 확인했다. 누적 Java 115/413종·530경로, 잔여 Java 298종/Python 150종. 근거: `clog2-definitions-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Topo_Event/Obj_Event/ColorNameMap 3종 전체 404줄 판독. 단일 좌표 이벤트 생성, 색상 이름 콜론 suffix 생략과 기본색 fallback, null/잘못된 행 처리의 한계를 확인했다. 누적 Java 118/413종·536경로, 잔여 Java 295종/Python 150종. ColorAlpha 내부와 진단 CLI는 별도 미판독이다. 근거: `clog2-event-color-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 ColorAlpha 전체 400줄 판독. 5바이트 저장과 입력 생성자/무동작 readObject의 차이, RGB 제곱합 비교, 216색 중 215개 인덱스 순환 및 전역 fallback 상태를 확인했다. 누적 Java 119/413종·542경로, 잔여 Java 294종/Python 150종. 근거: `color-alpha-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 Category 전체 1,030줄 판독. 색상 입력 생성자 사용, 폭 byte/배열 short 범위 미검사, 형식 문자열 null과 빈 문자열의 차이, 비직렬화 표시 플래그와 shadow 정의를 확인했다. 누적 Java 120/413종·548경로, 잔여 Java 293종/Python 150종. 근거: `category-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Print 진단 CLI 전체 243줄 판독. 출력 카테고리 목록의 shadow 포함, 즉시 Primitive 출력과 사후 정의 출력의 차이, 실제 파일 크기와 누적 바이트 출력의 차이를 기록했다. 누적 Java 121/413종·550경로, 잔여 Java 292종/Python 150종. Print_1pass/Print_2pass는 별도 미판독이다. 근거: `clog2-print-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Print_1pass 전체 1,087줄 판독. 상태 메서드의 RecBare/RecCargo 인자형 불일치로 인한 종료 경로, 현재 stateform만 집계하는 미매칭 통계, 일반 converter와 다른 정의/레코드 처리 범위를 기록했다. 누적 Java 122/413종·552경로, 잔여 Java 291종/Python 150종. 근거: `clog2-print-onepass-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Print_2pass 전체 1,043줄 판독. 첫 상태 정의의 RecBare/RecCargo reflection 불일치, 상태 정의 부재 시 마지막 통계의 null 참조, 두 pass 모두 type0 이후 다음 블록을 읽는 경로를 확인했다. 누적 Java 123/413종·554경로, 잔여 Java 290종/Python 150종. 근거: `clog2-print-twopass-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 하위 CLOG2/TRACE Print 2종 전체 923줄 판독. CLOG2 type0 이후 다음 블록 요청과 레코드 직접 출력, TRACE 선택적 시간 검사·도움말 이전 native load·빈 파일명 검사의 한계를 기록했다. 누적 Java 125/413종·558경로, 잔여 Java 288종/Python 150종. 근거: `lowlevel-print-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 base.topology Event/Line/State 3종 전체 762줄 판독. DrawnBox 선기록, 경계 잘림 차이, 이벤트 초기 반폭/전체 폭 불일치와 상태 Insets 비반영 선택 판정을 기록했다. 누적 Java 128/413종·564경로, 잔여 Java 285종/Python 150종. 근거: `basic-topology-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증이나 독립 의미 승인이 아니다.

2026-09-12 StateBorder 선택기·구현 8종 전체 543줄 판독. 좌우 경계 플래그, 위아래 선의 무조건 호출, 색상 변경 잔류와 XOR 모드 비복원, 알 수 없는 이름의 null 반환을 기록했다. 누적 Java 136/413종·580경로, 잔여 Java 277종/Python 150종. 근거: `state-border-read.json` (XBeach connectivity/bytecode-read). 원본 실행·실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 PreviewEvent 전체 354줄 판독. 중심 시각만 사용하는 표시 생략, 화면 경계 제외, 두 반타원과 세로선, 표시 높이와 타원 선택 높이의 1픽셀 차이를 기록했다. 누적 Java 137/413종·582경로, 잔여 Java 276종/Python 150종. 근거: `preview-event-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 Arrow 전체 619줄 판독. 방향별 화살촉 stroke 적용 차이, NaN 동등 비교의 도달 불가 분기, 같은 픽셀 끝점의 수직 화살촉 처리와 한쪽 경계 검사 한계를 기록했다. 누적 Java 138/413종·584경로, 잔여 Java 275종/Python 150종. 근거: `arrow-render-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 SummaryArrow 전체 423줄 판독. 카테고리별 공통 시작 시간, 객체 수 정수 나눗셈 기반 선 굵기, 밑 0·빈 배열·0시간 길이의 미검사, 굵기를 반영하지 않는 Line 선택 판정을 기록했다. 누적 Java 139/413종·586경로, 잔여 Java 274종/Python 150종. 근거: `summary-arrow-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 SummaryState 전체 889줄 판독. 표시 방식 4종의 시간/행 배치, 준비 단계와 그리기·선택 단계의 가시성 검사 차이, 배경색 객체 동일성 비교, 카테고리 우선 선택과 전체 상자 fallback을 기록했다. 누적 Java 140/413종·588경로, 잔여 Java 273종/Python 150종. 근거: `summary-state-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 CategoryTimeBox 계열 6종 전체 238줄 판독. 비율·색상·가시성의 원본 가중치/카테고리 위임, 네 정렬기의 시간 구간 비참조, null 가중치 미검사를 확인했다. 누적 Java 146/413종·600경로, 잔여 Java 267종/Python 150종. 근거: `category-timebox-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 TimeAveBox 전체 672줄 판독. 비율/개수 가중 합산, 삽입 순서 중첩 계산, 계산 후 timeblock null 처리, 무필터·일회 생성·직접 반환 카테고리 배열을 확인했다. SummaryState 가시성/오래된 표시 구간 문제의 하위 연결 근거를 추가했다. 누적 Java 147/413종·602경로, 잔여 Java 266종/Python 150종. 근거: `timeave-box-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 CategorySummaryF/CategoryWeightF 및 보조·선택 7종 전체 485줄 판독. double 개수 계산과 float 표시, NaN 개수 정렬 및 인덱스 뺄셈 한계, category 참조/캐시 인덱스 연결을 확인했다. category-timebox 기록의 F 정렬기 “이전 판독” 표현은 정수형 CategoryWeight와 혼동한 것으로 정정한다. F 본체는 이번 최초 판독이며 기존 집계에는 포함되지 않았다. 누적 Java 154/413종·616경로, 잔여 Java 259종/Python 150종. 근거: `float-statistics-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 BufForTimeAveBoxes 전체 891줄 판독. 행별 새 상자의 중첩 계산→배열 초기화→배치 순서를 확인해 앞선 캐시/재호출 위험의 정상 초기화 경로 적용 범위를 좁혔다. 행 매핑 누락 미검사와 화살표 우선·HashMap 첫 일치 선택도 기록했다. 누적 Java 155/413종·618경로, 잔여 Java 258종/Python 150종. 근거: `timeave-buffer-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 PreviewState 전체 1,035줄 판독. 표시 6방식의 픽셀 배분·가시성 반영, 그리기에서 갱신한 치수에 의존하는 선택 판정, 누적 방식 x 여백 재검사 부재를 기록했다. 인벤토리 base/ 미판독은 0이지만 전체 gate는 미통과다. 누적 Java 156/413종·620경로, 잔여 Java 257종/Python 150종. 근거: `preview-state-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 SLOG2 BufStub/IteratorOfGroupObjects 2종 전체 267줄 판독. 대리 버퍼의 경고·null/초기값 반환과 toString 캐시 변경, 최초 그룹 준비 및 그룹 전환의 hasNext 의존성을 기록했다. 누적 Java 158/413종·624경로, 잔여 Java 255종/Python 150종. 근거: `input-helpers-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 입력 TreeNode/그림자 순회기 5종 전체 596줄 판독. 생성자의 최초 그룹 준비, 겹치지 않는 버퍼 생략, 음수 자식 수의 null 처리와 직접 반환 배열을 확인했다. 누적 Java 163/413종·634경로, 잔여 Java 250종/Python 150종. 근거: `input-treenode-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 입력 TreeFloor/순회기 3종 전체 571줄 판독. 노드 목록의 얕은 복사와 방향 선택을 연결했다. prune의 내림차순 삭제 방향 불일치에 따른 빈 맵 접근 가능성을 정적 흐름으로 기록했으며 실제 호출 조건은 후속 확인한다. TimeBoundingBox.contains(double)는 양쪽 끝점을 포함함을 직접 재확인했다. 누적 Java 166/413종·640경로, 잔여 Java 247종/Python 150종. 근거: `input-treefloor-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 TreeFloorList/병합 순회기/입력 TreeTrunk 3종 전체 1,848줄 판독. prune 공개 경로와 확대·스크롤 경로가 다름을 확인하여 앞선 조건부 결함의 적용 범위를 제한했다. 층별 병합 조건, static 루트 시간 범위의 인스턴스 간 공유, 자식 읽기 null 처리와 깊이/확대값 검증 부재를 기록했다. 누적 Java 169/413종·646경로, 잔여 Java 244종/Python 150종. 근거: `input-floorlist-trunk-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 SLOG2 InputLog/전체 실객체 순회기 2종 전체 1,089줄 판독. 메타데이터 IO 실패 exit와 트리 노드 실패 null 반환의 차이를 TreeTrunk 호출자에 연결했다. 포인터 null 판정과 시작/종료 끝점의 반개구간 필터를 직접 재확인했으며 잘못된 topology 번호, 빈 leaf 집합, 구간 경계 제외 조건을 기록했다. 누적 Java 171/413종·650경로, 잔여 Java 242종/Python 150종. 근거: `slog-inputlog-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 SLOG2 PrintSerially/PrintRecursively 2종 전체 1,183줄 판독. 옵션 순서 의존성, 숫자 변환 실패 후 계속 진행, NaN 검사 통과, 재귀 출력의 루트 읽기 실패/빈 자료 혼동을 기록했다. 순차 출력의 인접 정렬 표시는 완전성 검증이 아니며 재귀 출력 모드 간 선택 범위도 다르다. 누적 Java 173/413종·654경로, 잔여 Java 240종/Python 150종. 근거: `slog-print-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 SLOG2 Navigator 전체 1,181줄 판독. 출력 모드 변경 시 시간창 갱신 단락 평가, 초기 changedPrintAll 잔존, 첫 숫자 토큰 오류의 catch 내부 배열 접근, EOF 미처리를 확인했다. 현 인벤토리의 SLOG2 input 패키지 판독은 채웠으나 전체 모델 gate는 미통과다. 누적 Java 174/413종·656경로, 잔여 Java 239종/Python 150종. 근거: `slog-navigator-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

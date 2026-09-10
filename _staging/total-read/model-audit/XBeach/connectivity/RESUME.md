# 2026-09-11 재개 지점

현재 작업은 plan.md의 **XBeach 전수 판독 → 연결 분석 → 검증 → canonical → 필요한 신규 HG, 이후 FUNWAVE**다. 연결 후보는 lifecycle/ 및 physics/에 남아 있다. 전체 판독 gate는 **NOT_PASSED**다. 이 문서는 완료 또는 승인 영수증이 아니다.

## 이번에 처리한 범위

- 원본 source_code 456 + manuals 87 = 543개 경로 집합·SHA, closure 불변 기록 292개 SHA 일치.
- ZIP/JAR 9개, member 1,722개 경로·크기·SHA 일치. 저장 상태는 unread 1,284 / read-text 96 / visually-inspected 334 / directory 8이며 중복 경로 수를 고유 content 수와 혼동하지 않는다.
- Office 5문서 36페이지를 렌더링·판독했다. adapted_front 수식, 곡선격자 슬라이드 19장과 WMF 수식 9개, decision tree 초안, 설치 메모, membership archive를 포함한다. members.doc의 VBA 원문은 97개 control 선언과 모듈 속성뿐이며 실행 본문은 없다. 컴파일된 내부 코드까지 판독했다고 하지 않는다.
- Jumpshot PDF 61페이지 전량 시각 보충 판독. 원 Table 3.22에도 SUMMARY_STATE_DISPLAY가 빠져 있다. 예제 C의 마지막 코드는 물리 p.60–61에 있으며 복원했다. 원문 자체의 누락/배치 문제와 변환 손실을 구별했다.
- namespaces.xls의 E1=COUNTA(C2:C102)를 BIFF 토큰에서 복원하고 값 43을 재계산했다. F1=47은 수식이 아닌 RK 상수 레코드다.
- MSI 2개 stream 106개와 cabinet member 123개의 원본 결박·크기·SHA를 재검증했다. 93개 member는 raw 트리와 동일 SHA다. PE/AR 59개는 import/export/resource-directory 인덱스를 저장했다. DLL 의존성 관측을 전체 구현·리소스 판독으로 올리지 않았다.
- `resume-reconciliation.json`에 보충 근거 27개 원본 경로를 연결했다. 근거 미연결 문서는 0개지만 전량 의미 판독 미완료와는 다른 수치다.
- 비정수압 보고서 PDF는 기존 `physics/document-read-premise.json`의 물리 13–68쪽 기록에 이번 1–12·69쪽 판독을 결합해 69쪽 전체의 시각 판독 근거를 연결했다. manuals의 동일 SHA PDF에도 승계했다. 기존 56쪽은 이번에 재판독한 것이 아니며 기존 기록에는 개별 이미지 해시가 없다.
- 보고서 DOC를 별도로 70쪽 PDF로 렌더링하고 전체 표시 내용을 확인했다. 격자·습윤건조·검증 그림·흐름도·부록 표를 확인했지만 수식 참조 공백과 p.14 묶음 기호의 네모 표시가 남아 있다. OLE stream 1,571개(Equation Native 388개)는 해시 목록만 작성했으며 원시 수식 오브젝트 판독은 미완료다. `nonhydro-read/read-receipt.json`과 새 페이지 이미지 83개·DOC 렌더 PDF를 저장했다.

## 다음 작업

1. 두 매뉴얼 DOCX의 독립 렌더 판독을 진행한다. Kingsday PDF는 기존 10–45쪽에 신규 1–9·46–141쪽(105쪽), master PDF는 기존 10–46쪽에 신규 1–9·47–145쪽(108쪽)을 결합해 각각 141·145쪽 전체의 시각 보충 근거를 연결했다. `manuals-visual-read/read-receipts.json`과 신규 이미지 213개 참조. 동일 SHA인 manuals PDF 2경로에만 승계했다. PDF 판독은 DOCX 판독을 대신하지 않는다.
2. 보고서 DOC의 잔여 수식 글리프·388개 Equation Native 충실도를 확인한다. MathType outer 166개 중 165개 저장 표시값 복원은 이전 기록에 보존했다. 이번에는 후속 렌더에서 발견된 그림 번호의 장 제목 치환을 막기 위해 본문 필드 제어 노드 652개만 제거하고 표시값을 고정했다. 머리말·꼬리말을 포함한 나머지 ZIP member는 동일 바이트다. `nonhydro-read/body-field-recovery/receipt.json` 참조. 71쪽 전체 본문을 확인했으며 최종본과 판독 중간본은 모든 페이지 y<1680 RGB가 동일하다. 차이는 쪽 번호 영역뿐이며 별도 확인했다. 최종본 p.11 그림 2-1/2-2도 직접 확인했다. p.15·41·42의 작은 네모 글리프, inline 수식 배치, 원래 빈 필드 1개는 남는다. 저장 목차/참조 쪽 번호는 재페이지화와 일치한다고 보장하지 않으며 물리 페이지 번호로 인용한다.
3. 외부 바이너리의 리소스 payload와 AR 내부 member·JAR bytecode의 처리 범위를 계속 명시한다. `msi-interface-review.json`은 의존성 관측과 추출 인덱스이며 의미 판독 완료가 아니다. 기존 interim interface/resource 범위로 진행하되 전체 gate 예외나 전체 역어셈블리 승인을 발급하지 않는다.
4. 위 전제가 충족된 뒤 연결 후보를 확정한다. FUNWAVE는 읽기 전용 preflight 이외 단계로 넘어가지 않았다.

## 재현 및 검증

저장된 문서 페이지 이미지는 `office-read/`, `jumpshot-pdf-read/`, `nonhydro-read/`, `manuals-visual-read/`에 있어 재부팅 후에도 남는다. 원본을 재생성하거나 수정하지 않는다.

```sh
python3 _staging/total-read/model-audit/XBeach/connectivity/recover_msi.py
python3 _staging/total-read/model-audit/XBeach/connectivity/build_msi_interfaces.py
python3 _staging/total-read/model-audit/XBeach/connectivity/reconcile_resume.py
python3 _staging/total-read/model-audit/XBeach/connectivity/validate_resume_evidence.py
```

필요 도구: Python olefile, cabextract 1.11, objdump. Office 변환은 LibreOffice 24.2.7의 headless PDF/Text export, 페이지 렌더는 pdftoppm scale-to 1600을 사용했다. WMF 수식은 Draw PDF export로 겹침 없이 따로 판독했다. 원문에서 가져온 셸 예제나 VBA를 실행하지 않았다.

수식 필드 복원은 `nonhydro-read/recover_cached_fields.py`로 재현한다. `--converted-docx`와 `--output-docx`를 주면 DOCX 변환본의 동일 순서 필드 명령 166개를 대조하고 검토 사본의 빈 필드만 저장값의 고정 텍스트로 바꾼다. 매크로 실행·원본 수정·수식 번호 재계산은 없다. 글꼴은 PC의 기존 파일을 임시 fontconfig로 사용하며 글꼴 바이너리는 커밋하지 않았다.

후속 본문 필드 고정은 `nonhydro-read/freeze_body_fields.py INPUT.docx OUTPUT.docx`로 재현한다. 검토 중간본과 최종본·각 페이지 이미지를 모두 저장했다. 매뉴얼과 이번 보고서 보충 이미지는 pdftoppm scale-to 1800을 사용했다. 매뉴얼 p.60 의사결정도는 회전해 별도 확인했다.

문서 오류도 판독 근거에 남겼다. Kingsday의 instat 설명과 wbctype 그림, tideloc 설명/표 불일치, Master p.125의 원본 참조 오류·반복된 A.1 표 번호, 두 판본의 bedfriccoef 기본값 차이는 구현 사실로 승격하지 않았다. 전체 PDF 시각 보충은 작은 기호의 완전 전사나 수식의 수학적 검증을 뜻하지 않는다.

validator의 213개 PASS는 구조·원본 SHA·이미지 SHA·입력 집합·필드 복원 재현·중간/최종 본문 픽셀 일치 검증만 뜻한다. 독립 의미 검증이나 사람 승인이 아니다. 이전 사람 승인·crosswalk·closure 기록은 그대로 보존했다.

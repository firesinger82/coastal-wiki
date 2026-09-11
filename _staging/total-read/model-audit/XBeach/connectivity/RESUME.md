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

1. 두 매뉴얼 DOCX의 **복원본 전체 시각 판독**을 이어간다. `manuals-docx-read/receipt.json`의 `display-recovered`가 다음 판독 대상이며 Kingsday 145쪽 중 6·10·18·125·145쪽, Master 148쪽 중 10·18·44·128·148쪽만 이번에 시각 확인했다. 나머지 쪽은 각 variant의 `uninspected_pages`에 명시했다. 직접 변환본과 단순 필드 제거본은 손상 비교 자료이며 최종 판독 사본으로 사용하지 않는다.
   - `recover_display.py`는 원본 DOCX의 MathType 표시 인수와 중첩 SEQ/REF의 저장 결과만 읽어 Kingsday 251개, Master 265개를 복원한다. 각 원본의 빈 인수 4개는 그대로 남는다. 모든 원래 `w:t`·수식 오브젝트·본문 이외 ZIP member 바이트를 보존했다. 문서별 ZIP member 530·562개와 삽입 OLE 238·248개의 stream 해시를 저장했으나 원시 수식 의미 판독은 아니다.
   - 직접 변환 시 장 제목이 그림 번호에 들어가고 숨은 Equation/MERGEFORMAT 명령이 표시된다. 단순 필드 제거는 수식 번호와 참조를 잃는다. 세 단계의 PDF·검토 DOCX·텍스트와 진단 페이지를 저장했다. 최종 표시값 516개는 PDF에서 출현 횟수까지 검사했다.
   - Master 복원본 p.18 식 (2.1)은 본체가 비어 있다. 원본 `word/media/image13.emf`를 별도로 Draw 렌더링해 파랑작용 평형식을 확인했다. `master/equation-2-1/`의 원본 추출·PDF·이미지로 보충했으며 Writer 본문 렌더는 수정하지 않았다. Master p.10의 Figure A.1 참조/2.1 캡션 불일치와 p.128의 원래 참조 오류 2개도 보존했다. 직접 변환의 Error: 문구는 오류 소멸이 아니라 표시 변경이었다.
   - 원 PDF는 Kingsday 기존 10–45쪽+신규 1–9·46–141쪽(105쪽), Master 기존 10–46쪽+신규 1–9·47–145쪽(108쪽)으로 각각 전체 141·145쪽의 시각 보충 근거가 있다. `manuals-visual-read/read-receipts.json`과 신규 이미지 213개 참조. 이 기록은 동일 SHA PDF 경로에만 승계하며 DOCX 판독을 대신하지 않는다.
2. 보고서 DOC의 잔여 수식 글리프·388개 Equation Native 충실도를 확인한다. MathType outer 166개 중 165개 저장 표시값 복원은 이전 기록에 보존했다. 이번에는 후속 렌더에서 발견된 그림 번호의 장 제목 치환을 막기 위해 본문 필드 제어 노드 652개만 제거하고 표시값을 고정했다. 머리말·꼬리말을 포함한 나머지 ZIP member는 동일 바이트다. `nonhydro-read/body-field-recovery/receipt.json` 참조. 71쪽 전체 본문을 확인했으며 최종본과 판독 중간본은 모든 페이지 y<1680 RGB가 동일하다. 차이는 쪽 번호 영역뿐이며 별도 확인했다. 최종본 p.11 그림 2-1/2-2도 직접 확인했다. p.15·41·42의 작은 네모 글리프, inline 수식 배치, 원래 빈 필드 1개는 남는다. 저장 목차/참조 쪽 번호는 재페이지화와 일치한다고 보장하지 않으며 물리 페이지 번호로 인용한다.
3. 외부 바이너리의 리소스 payload와 AR 내부 member·JAR bytecode의 처리 범위를 계속 명시한다. `msi-interface-review.json`은 의존성 관측과 추출 인덱스이며 의미 판독 완료가 아니다. 기존 interim interface/resource 범위로 진행하되 전체 gate 예외나 전체 역어셈블리 승인을 발급하지 않는다.
4. 위 전제가 충족된 뒤 연결 후보를 확정한다. FUNWAVE는 읽기 전용 preflight 이외 단계로 넘어가지 않았다.

## 재현 및 검증

저장된 문서 페이지 이미지는 `office-read/`, `jumpshot-pdf-read/`, `nonhydro-read/`, `manuals-visual-read/`, `manuals-docx-read/`에 있어 재부팅 후에도 남는다. 원본을 재생성하거나 수정하지 않는다.

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

DOCX 표시값 복원은 `manuals-docx-read/recover_display.py SOURCE.docx REVIEW.docx EVIDENCE.json`으로 재현한다. 입력을 원본 DOCX에 결속하며 다른 판본 PDF에서 번호를 가져오지 않는다. 복원본의 나머지 ZIP member가 원본과 같은지, 저장 표시값과 원문 텍스트가 보존되는지, 모든 복원 표시값이 PDF에 남는지 검증한다. 293쪽을 렌더링한 것과 293쪽을 판독한 것은 다르다. 이번 최종본 시각 판독은 명시된 10쪽뿐이다.

validator의 270개 PASS는 구조·원본 SHA·이미지 SHA·입력 집합·필드 복원 재현·PDF 텍스트/쪽 수 결속·기존 보고서 중간/최종 본문 픽셀 일치 검증만 뜻한다. 독립 의미 검증이나 사람 승인이 아니다. 이전 사람 승인·crosswalk·closure 기록은 그대로 보존했다.

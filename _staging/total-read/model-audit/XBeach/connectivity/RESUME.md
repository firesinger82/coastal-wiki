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

1. 두 매뉴얼 DOCX의 복원본은 **145·148쪽 전체 시각 판독 근거를 연결했다**. 기존 5쪽씩에 신규 Kingsday 140쪽·Master 143쪽을 추가했다. `manuals-docx-read/full-visual-read/receipt.json`에 신규 이미지 283개·관측 기록·원본/최종 PDF SHA를 저장했다. 이전 `receipt.json`은 당시의 부분 판독·변환 실패 비교 기록으로 보존하며, 현재 전체 시각 범위는 새 영수증을 따른다. 다음은 **잔여 수식 충실도 확인**이다.
   - Master p.27 (2.40)·p.28 (2.43)의 Writer 본문은 비어 있지만 원본 EMF를 별도 Draw 렌더하여 에너지 평형식과 roller 응력식을 확인했다. Kingsday p.27 (2.38)의 원본 WMF는 빈 화면이며, 후속 Native 판독에서 221바이트 스트림에 설정 레코드와 END만 있고 수식 본체가 없음을 확인했다. Kingsday p.25 (2.27)·p.28 (2.41)/(2.42)의 원본 문단에는 수식 본체가 없고 번호 필드만 있다. 문단 XML과 preview/OLE 추출·관계 ID를 새 영수증에 저장했다. 다른 판본의 수식으로 채우지 않았다.
   - `manuals-docx-read/native-probe/receipt.json`에 같은 MTEF 본문을 가진 5개 스트림의 본체 부재 확인을 저장했다(Kingsday 3·Master 2, 나머지 4개는 공백 문단). 접두부 28바이트는 불투명하게 보존했고 일반 OLE 해독으로 확대하지 않는다. 두 문서 p.19의 (2.5) 네모 위첨자와 B.37/C.37의 0 뒤 a는 원본 WMF 별도 렌더에서도 남는다. (2.5)–(2.8) 및 B.37/C.37 미리보기 10개를 대조했다. 후속 `glyph-record-read/receipt.json`에서 선택한 4개 Native 스트림의 구조·문자를 판독했다. (2.5) 네모 위치에는 MTCode 0x223C(∼), typeface 11, font position 58이 저장되어 있고 B.37/C.37 첫 줄에는 0 다음 소문자 a가 실제 저장되어 있다. 글꼴 문제의 정확한 원인과 a의 수학적 의도는 미확정이다. 후속 `native-survey.json`은 전체 486개에 고정 offset·기존 지원 범위의 판독기를 적용한 기계적 조사다. 301개 수용·185개 거부이며 의미 판독 완료로 승격하지 않는다. Kingsday p.15의 o는 원본 빈 문단 441D49D0의 numId 18/ilvl 1에 지정된 글머리표임을 확인했다(본문 텍스트 노드 없음, numFmt=bullet, lvlText=o). 후속 `native-prefix-survey.json`에서 설정 영역 끝을 검증해 본체 시작 위치 218/219/220/228/229를 구분했다. 기존 본체 판독기는 그대로 두고 60개를 추가 수용해 총 361개 기계적 수용·본문 미지원 122개·접두부 미해결 3개가 됐다. 후속 `native-embell-survey.json`에서 CHAR 장식 목록과 nudge 없는 EMBELL 레코드의 한정 지원으로 80개를 추가 수용했다. 현재 441개 기계적 수용·본문 미지원 42개·Master 접두부 미해결 3개다. 이전 수용 361개의 전체 구조 출력은 동일하다. 후속 `native-layout-survey.json`의 행렬/RGB/크기/정렬 한정 지원으로 18개를 추가 수용해 현재 459개 기계적 수용·본문 미지원 24개·접두부 미해결 3개다. 기존 수용 441개 출력은 동일하다. 후속 `native-nudge-survey.json`에서 이동 보정으로 4개를 추가 수용해 현재 463개 기계적 수용·본문 미지원 20개·접두부 미해결 3개다. 기존 459개 구조 출력은 동일하다. 다음은 색상 인덱스 0(12개), 예상 RULER tag 불일치(8개), Master 접두부(3개)의 확인 및 개별 식의 원문/렌더 대조다. 후속 `native-future-probe.json`에서 Master 세 개의 offset 41 확장 레코드(tag 100, 길이 3, payload 000000)를 보존하고 offset 204에서 본문 구조를 판독했다. 확장 payload 의미는 미해결로 유지한다. 따라서 본문 구조는 466개이며 그중 3개는 opaque prefix 조건부다. 후속 `native-conditional-probe.json`에서 정렬 8개는 태그 없는 탭 목록으로, 색상 12개는 인덱스 0의 의미를 미해석으로 보존하여 조건부 구조 전체를 확보했다. strict 판독은 이 20개를 계속 거부한다. 매뉴얼 전체 486개는 strict 463 + opaque prefix 3 + 조건부 20이며 의미/렌더 완료가 아니다. 후속 `conditional-visual-read/receipt.json`에서 조건부 20개 원본 WMF를 렌더·전량 확인했다. 새 네모 글리프는 관측하지 않았다. Kingsday133/Master143/Master81 침투식의 분수 뒤 1 앞에는 연산자가 보이지 않고 Native CHAR도 없으며, Kingsday70 대응식은 +1을 쓴다. 판본 차이를 그대로 남겼다. 후속 `infiltration-document-code-comparison.json`에서 현재 구현의 +1 불포화 침투 관계와 양의 근을 대조했다. 암시적 침투층·시간 비율·가용 표층수 제한을 구분했고 문서를 자동 수정하지 않았다. 다음은 나머지 매뉴얼/보고서 글리프 및 미판독 컨테이너 자료 검토다. GOAL 활성화로 전체 남은 단계는 GOAL-STATUS.md에서 추적한다. 선택한 4개 역시 전체 수학적 의미 검증 완료가 아니다. 모든 페이지를 보았다는 사실을 모든 글리프와 수학적 내용의 검증으로 해석하지 않는다.
   - `recover_display.py`는 원본 DOCX의 MathType 표시 인수와 중첩 SEQ/REF의 저장 결과만 읽어 Kingsday 251개, Master 265개를 복원한다. 각 원본의 빈 인수 4개는 그대로 남는다. 모든 원래 `w:t`·수식 오브젝트·본문 이외 ZIP member 바이트를 보존했다. 문서별 ZIP member 530·562개와 삽입 OLE 238·248개의 stream 해시를 저장했으나 원시 수식 의미 판독은 아니다.
   - 직접 변환 시 장 제목이 그림 번호에 들어가고 숨은 Equation/MERGEFORMAT 명령이 표시된다. 단순 필드 제거는 수식 번호와 참조를 잃는다. 세 단계의 PDF·검토 DOCX·텍스트와 진단 페이지를 저장했다. 최종 표시값 516개는 PDF에서 출현 횟수까지 검사했다.
   - Master 복원본 p.18 식 (2.1)은 본체가 비어 있다. 원본 `word/media/image13.emf`를 별도로 Draw 렌더링해 파랑작용 평형식을 확인했다. `master/equation-2-1/`의 원본 추출·PDF·이미지로 보충했으며 Writer 본문 렌더는 수정하지 않았다. Master p.10의 Figure A.1 참조/2.1 캡션 불일치와 p.128의 원래 참조 오류 2개도 보존했다. 직접 변환의 Error: 문구는 오류 소멸이 아니라 표시 변경이었다.
   - 원 PDF는 Kingsday 기존 10–45쪽+신규 1–9·46–141쪽(105쪽), Master 기존 10–46쪽+신규 1–9·47–145쪽(108쪽)으로 각각 전체 141·145쪽의 시각 보충 근거가 있다. `manuals-visual-read/read-receipts.json`과 신규 이미지 213개 참조. 이 기록은 동일 SHA PDF 경로에만 승계하며 DOCX 판독을 대신하지 않는다.
2. 보고서 DOC의 잔여 수식 글리프·388개 Equation Native 충실도를 확인한다. 후속 `nonhydro-read/native-survey.json`은 원본 388개 중 386개 본문 기계적 판독, 2개 본문 내 인코딩 정의(tag 19) 미지원 결과다. 후속 `nonhydro-read/native-font-survey.json`에서 본문 인코딩/글꼴/스타일 정의를 지원해 388개 전체가 기계적으로 읽힌다. 이전 386개 출력 동일. 새 두 스트림의 F093/typeface -1/font position 84(Euclid Math Two)는 시각/의미 확인 대상이다. 수학적 의미/렌더 충실도 검증과 구분한다. MathType outer 166개 중 165개 저장 표시값 복원은 이전 기록에 보존했다. 이번에는 후속 렌더에서 발견된 그림 번호의 장 제목 치환을 막기 위해 본문 필드 제어 노드 652개만 제거하고 표시값을 고정했다. 머리말·꼬리말을 포함한 나머지 ZIP member는 동일 바이트다. `nonhydro-read/body-field-recovery/receipt.json` 참조. 71쪽 전체 본문을 확인했으며 최종본과 판독 중간본은 모든 페이지 y<1680 RGB가 동일하다. 차이는 쪽 번호 영역뿐이며 별도 확인했다. 최종본 p.11 그림 2-1/2-2도 직접 확인했다. p.15·41·42의 작은 네모 글리프, inline 수식 배치, 원래 빈 필드 1개는 남는다. 저장 목차/참조 쪽 번호는 재페이지화와 일치한다고 보장하지 않으며 물리 페이지 번호로 인용한다.
3. 외부 바이너리의 리소스 payload와 AR 내부 member·JAR bytecode의 처리 범위를 계속 명시한다. 후속 `bytecode-read/`에서 unread 1,284개 경로를 Java 413종/Python 150종으로 결속하고 Java 87,653줄을 역어셈블리했다. launcher 네 클래스의 전체 표시 명령을 직접 읽어 동일 SHA 12개 경로에 연결했다. Java 400종·Python 150종은 미판독이며 기존 인벤토리를 완료로 바꾸지 않는다. `msi-interface-review.json`은 의존성 관측과 추출 인덱스이며 의미 판독 완료가 아니다. 기존 interim interface/resource 범위로 진행하되 전체 gate 예외나 전체 역어셈블리 승인을 발급하지 않는다.
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

DOCX 표시값 복원은 `manuals-docx-read/recover_display.py SOURCE.docx REVIEW.docx EVIDENCE.json`으로 재현한다. 입력을 원본 DOCX에 결속하며 다른 판본 PDF에서 번호를 가져오지 않는다. 복원본의 나머지 ZIP member가 원본과 같은지, 저장 표시값과 원문 텍스트가 보존되는지, 모든 복원 표시값이 PDF에 남는지 검증한다. 이전 최종본 10쪽 부분 판독에 이번 283쪽을 더해 293쪽 전체 시각 확인을 연결했다. 이전 영수증을 덮어쓰지 않았으며, 새 영수증은 원본 DOCX 및 동일 최종 PDF에 결속된다. Kingsday p.63·Master p.62 의사결정도는 회전해 확인했다.

validator의 585개 PASS는 구조·원본 SHA·이미지 SHA·입력 집합·필드 복원 재현·PDF 텍스트/쪽 수 결속·DOCX 신규 페이지 집합/관측·회전도 픽셀·보충 preview/OLE 및 빈 문단 원본 결속·Native 본체 부재 판독 재현/절단·본체 삽입 거부·기존 보고서 중간/최종 본문 픽셀 일치 검증만 뜻한다. 선택 수식 4개의 문자·중첩 위치·원본 재추출 및 변조/절단 거부 검사도 포함한다. 독립 의미 검증이나 사람 승인이 아니다. 이전 사람 승인·crosswalk·closure 기록은 그대로 보존했다.

2026-09-12 추가: base/io 9종 465줄을 직접 읽고 동일 SHA 54경로에 결속했다. 누적 Java 13/413종(66경로), Python 150종 미판독. [입출력 판독](bytecode-read/base-io-read.json). 전체 gate NOT_PASSED·GOAL active.

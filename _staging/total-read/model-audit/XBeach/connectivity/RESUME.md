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
3. 외부 바이너리의 리소스 payload와 AR 내부 member·JAR bytecode의 처리 범위를 계속 명시한다. 후속 `bytecode-read/`에서 unread 1,284개 경로를 Java 413종/Python 150종으로 결속하고 Java 87,653줄을 역어셈블리했다. launcher 4종·base/io 9종·SLOG2 헤더/디렉토리 7종·TreeNodeID 5종·파일명/열거/순회 7종·시간/좌표 11종·Drawable/Topology 3종·InfoBox·InfoType·InfoValue·중첩/표시 위치 3종·객체 버퍼 3종·LineIDMap/Method/YCoordMap·BufForShadows·Shadow·category weight 계열 10종·Primitive·Composite 2종·output TreeNode/TreeTrunk/OutputLog·Clog2ToSlog2/ClogToSlog2·InputAPI/Kind·TraceToSlog2·trace InputLog/DobjDef·CLOG2 입력 래퍼/순회 3종·ContentIterator·상태/화살표 매칭 7종·ID 맵/LineID 3종·입력 레코드 4종·stream/preamble 3종·Const/RecComm/UUID·생략 레코드 4종·정의/ObjDef 4종·단일 이벤트/색상 3종·ColorAlpha/Category·CLOG2 Print/Print_1pass/Print_2pass·하위 CLOG2/TRACE Print·Event/Line/State·StateBorder 계열 8종·PreviewEvent/Arrow/SummaryArrow/SummaryState·CategoryTimeBox 계열 6종·TimeAveBox·실수 통계/선택 7종·시간 평균 버퍼·PreviewState·입력 보조 2종의 전체 표시 내용을 읽어 동일 SHA 624개 경로에 연결했다. Java 255종·Python 150종은 미판독이며 기존 인벤토리를 완료로 바꾸지 않는다. `msi-interface-review.json`은 의존성 관측과 추출 인덱스이며 의미 판독 완료가 아니다. 기존 interim interface/resource 범위로 진행하되 전체 gate 예외나 전체 역어셈블리 승인을 발급하지 않는다.
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

validator의 834개 PASS는 구조·원본 SHA·이미지 SHA·입력 집합·필드 복원 재현·PDF 텍스트/쪽 수 결속·DOCX 신규 페이지 집합/관측·회전도 픽셀·보충 preview/OLE 및 빈 문단 원본 결속·Native 본체 부재 판독 재현/절단·본체 삽입 거부·기존 보고서 중간/최종 본문 픽셀 일치 검증만 뜻한다. 선택 수식 4개의 문자·중첩 위치·원본 재추출 및 변조/절단 거부 검사도 포함한다. 독립 의미 검증이나 사람 승인이 아니다. 이전 사람 승인·crosswalk·closure 기록은 그대로 보존했다.

2026-09-12 추가: base/io 9종 465줄을 직접 읽고 동일 SHA 54경로에 결속했다. 누적 Java 13/413종(66경로), Python 150종 미판독. [입출력 판독](bytecode-read/base-io-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 후속: SLOG2 헤더·디렉토리 7종 전체 판독. 누적 Java 20/413종, 남은 Java 393종/Python 150종. [근거](bytecode-read/slog2-header-read.json). 전체 gate NOT_PASSED.

2026-09-12 TreeNodeID 본체/정렬/marker 5종 588줄 추가 판독. 누적 Java 25/413종, 남은 Java 388종/Python 150종. [근거](bytecode-read/slog2-node-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 파일명/열거/표시 순회 7종 전체 판독. 누적 Java 32/413종, 남은 Java 381종/Python 150종. [근거](bytecode-read/slog2-iteration-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 시간 경계/좌표 11종 전체 판독. 누적 Java 43/413종, 남은 Java 370종/Python 150종. [근거](bytecode-read/time-coord-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 Drawable/비교기/Topology 3종 전체 판독. 누적 Java 46/413종, 남은 Java 367종/Python 150종. [근거](bytecode-read/drawable-order-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 InfoBox 전체 967줄 판독. 누적 Java 47/413종, 남은 Java 366종/Python 150종. [근거](bytecode-read/infobox-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 InfoType/InfoValue 전체 803줄 판독. 누적 Java 49/413종, 남은 Java 364종/Python 150종. [근거](bytecode-read/info-value-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 중첩/표시 위치 3종 655줄 판독. 누적 Java 52/413종, 남은 Java 361종/Python 150종. [근거](bytecode-read/nesting-drawn-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 객체 버퍼 3종 934줄 판독. 누적 Java 55/413종, 남은 Java 358종/Python 150종. [근거](bytecode-read/drawable-buffer-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 LineIDMap/Method 1099줄 판독. 누적 Java 57/413종, 남은 Java 356종/Python 150종. [근거](bytecode-read/lineid-method-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 YCoordMap 전체 판독 및 bytecode-read/coverage.json 누적 집계. 당시 Java 58/413종·336경로, Java 355종/Python 150종 미판독. 전체 gate NOT_PASSED·GOAL active.

후속 shadow-buffer-read는 750줄 전체를 확인했다. write/empty의 호출 순서와 Shadow 내부 집계 의미는 후속 연결 분석 대상으로 남긴다. 누적 판독 59종은 전체 승인과 구분한다.

2026-09-12 Shadow 1425줄 전체 판독: 객체 수 가중 평균, 기간 비율 재조정, nesting exclusion, 입출력 상태 차이와 preview 위임을 확인했다. 누적 Java 60/413종·348경로, 잔여 Java 353종/Python 150종. Primitive/CategoryWeight 내부와 정상 호출 순서는 후속 확인 대상이다.

2026-09-12 CategoryRatios/Summary/Weight와 comparator·marker 10종, 전체 909줄 판독. 단순 비율 연산, 8/16/20-byte 직렬화와 이미 연결된 category의 resolve=false를 확인했다. 누적 Java 70/413종·408경로, 잔여 Java 343종/Python 150종.

2026-09-12 Primitive 전체 955줄 판독(출력 절단 구간 별도 재판독). 복사/참조 setter, signed-short 직렬화, 배열 입력 생성자의 final index 미설정, Shadow 연결을 기록했다. 누적 Java 71/413종·414경로, 잔여 Java 342종/Python 150종.

2026-09-12 Composite/내부 iterator 전체 1049줄 판독. 비중첩 항목에서 iterator 인덱스가 증가하지 않는 경로를 확인했다. 실제 호출 범위는 후속 분석 대상. 누적 Java 73/413종·426경로, 잔여 Java 340종/Python 150종.

2026-09-12 output TreeNode 619줄 전체 판독. category-null Composite를 primitive로 분해하고 shadow 병합 후 시간 범위를 명시적으로 갱신한다. 누적 Java 74/413종·430경로. 상위 출력 driver의 호출 순서는 후속 확인 대상.

2026-09-12 TreeTrunk/OutputLog 전체 723줄 판독. finalizeLatestTime → merge/shift/write → empty 순서를 확인했다. converter의 입력 순서·flush/close 보장은 후속 대상이다. 누적 Java 76/413종·438경로, 잔여 Java 337종/Python 150종.

2026-09-12 Clog2ToSlog2 전체 764줄 판독. 기본 시간 검사 off, 선택 검사 및 정상 EOF의 flush/map 기록/close 순서를 확인했다. 누적 Java 77/413종·442경로, 잔여 Java 336종/Python 150종. 입력 decoder와 다른 converter는 후속 대상.

2026-09-12 ClogToSlog2 전체 750줄 판독. CLOG2와 달리 YCoordMap 분기가 없고 출력 line map은 identity만 포함한다. 누적 Java 78/413종·446경로, 잔여 Java 335종/Python 150종.

2026-09-12 InputAPI/Kind 전체 172줄 판독. Kind 값 동등성과 converter identity 분기를 구분하고 decoder의 정적 객체 반환 여부를 후속 대상으로 남겼다. 누적 Java 80/413종·458경로, 잔여 Java 333종/Python 150종.

2026-09-12 TraceToSlog2 전체 864줄 판독. Composite/YCoordMap 분기, native TraceInput 로딩, filespec 전달 및 flush/close를 확인했다. 누적 Java 81/413종·462경로, 잔여 Java 332종/Python 150종. Native 구현 승인은 아니다.

2026-09-12 trace InputLog/DobjDef 전체 236줄 판독. 정수 kind를 정적 객체로 변환해 converter identity 조건을 충족하고, 초기 topology 3종을 제공한다. Native 메서드 본문은 이 클래스에 없으며 별도 대상이다. 누적 Java 83/413종·466경로, 잔여 Java 330종/Python 150종.

2026-09-12 CLOG2 InputLog와 TopologyIterator/YCoordMapIterator 전체 437줄 판독. 정적 Kind 반환 및 topology→content→좌표 맵 전환과 최초 arrow category 특례를 확인했다. ContentIterator 본문과 superclass는 미판독으로 남긴다. 누적 Java 86/413종·472경로, 잔여 Java 327종/Python 150종.

2026-09-12 CLOG2 ContentIterator 전체 1,193줄 판독. hasNext가 레코드를 소비하고 next가 저장 객체를 반환하는 계약, Category/Primitive만 생성하는 경로, reflective handler 오류 처리와 미매칭 통계의 중복 집계 가능성을 기록했다. 저수준 레코드·Topo 매칭·ID 맵은 별도 미판독이다. 누적 Java 87/413종·474경로, 잔여 Java 326종/Python 150종.

2026-09-12 CLOG2 상태/화살표 매칭과 지원 클래스 7종 전체 791줄 판독. 상태 FIFO 매칭, 실패한 종료 이벤트의 예외 전달, 메시지 수신 선행 시 크기 0 저장 경로를 확인했다. 원본은 수정하지 않았다. 누적 Java 94/413종·488경로, 잔여 Java 319종/Python 150종. ID 맵과 저수준 레코드는 별도 미판독이다.

2026-09-12 CLOG2 ID 맵·ID 값·LineID 3종 전체 586줄 판독. 사용 항목 필터와 두 좌표 보기 생성, ID 누락 시 경고 후 null 참조, 전역 크기 기반 ID 계산의 무검사 정수 연산을 확인했다. 누적 Java 97/413종·494경로, 잔여 Java 316종/Python 150종. 저수준 레코드와 preamble 초기화는 별도 미판독이다.

2026-09-12 CLOG2 RecHeader/RecMsg/RecBare/RecCargo 4종 전체 517줄 판독. 읽기 실패 시 부분/이전 필드 보존과 상위 반환값 미검사, skip 길이 미검사, Cargo의 매회 새 배열 할당을 확인했다. 누적 Java 101/413종·502경로, 잔여 Java 312종/Python 150종. stream/preamble 및 다른 레코드는 별도 미판독이다.

2026-09-12 CLOG2 InputLog/MixedDataInputStream/Preamble 3종 전체 943줄 판독. preamble 실패 반환값 무시와 전역 ID 설정 누락 가능성, 짧은 블록 EOF 처리, 고정 문자열 NUL 조건을 연결했다. 누적 Java 104/413종·508경로, 잔여 Java 309종/Python 150종. 다른 레코드와 상수는 별도 미판독이다.

2026-09-12 CLOG2 Const/RecComm/UUID 3종 전체 352줄 판독. 빈 호환 버전 목록, UUID 내부 읽기 실패에도 RecComm이 48을 반환하는 경로, CommFree와 UUID가 ID 맵 삭제/키에 쓰이지 않는 연결을 확인했다. 누적 Java 107/413종·514경로, 잔여 Java 306종/Python 150종.

2026-09-12 CLOG2 RecColl/RecDefConst/RecSrc/RecTshift 4종 전체 380줄 판독. 본문 converter가 집단통신·상수 이름·소스 위치·시간 이동 body를 건너뛰는 경로와 실제 skip 길이 미검사를 연결했다. 누적 Java 111/413종·522경로, 잔여 Java 302종/Python 150종.

2026-09-12 CLOG2 상태/이벤트/메시지 정의와 ObjDef 4종 전체 552줄 판독. 임시 이벤트 ID 생성, stateID와 Category 번호의 분리, 메시지 형식과 정보 버퍼의 연결을 확인했다. 누적 Java 115/413종·530경로, 잔여 Java 298종/Python 150종.

2026-09-12 CLOG2 Topo_Event/Obj_Event/ColorNameMap 3종 전체 404줄 판독. 단일 좌표 이벤트 생성, 색상 이름 콜론 suffix 생략과 기본색 fallback, null/잘못된 행 처리의 한계를 확인했다. 누적 Java 118/413종·536경로, 잔여 Java 295종/Python 150종. ColorAlpha 내부와 진단 CLI는 별도 미판독이다.

2026-09-12 ColorAlpha 전체 400줄 판독. 5바이트 저장과 입력 생성자/무동작 readObject의 차이, RGB 제곱합 비교, 216색 중 215개 인덱스 순환 및 전역 fallback 상태를 확인했다. 누적 Java 119/413종·542경로, 잔여 Java 294종/Python 150종.

2026-09-12 Category 전체 1,030줄 판독. 색상 입력 생성자 사용, 폭 byte/배열 short 범위 미검사, 형식 문자열 null과 빈 문자열의 차이, 비직렬화 표시 플래그와 shadow 정의를 확인했다. 누적 Java 120/413종·548경로, 잔여 Java 293종/Python 150종.

2026-09-12 CLOG2 Print 진단 CLI 전체 243줄 판독. 출력 카테고리 목록의 shadow 포함, 즉시 Primitive 출력과 사후 정의 출력의 차이, 실제 파일 크기와 누적 바이트 출력의 차이를 기록했다. 누적 Java 121/413종·550경로, 잔여 Java 292종/Python 150종. Print_1pass/Print_2pass는 별도 미판독이다.

2026-09-12 CLOG2 Print_1pass 전체 1,087줄 판독. 상태 메서드의 RecBare/RecCargo 인자형 불일치로 인한 종료 경로, 현재 stateform만 집계하는 미매칭 통계, 일반 converter와 다른 정의/레코드 처리 범위를 기록했다. 누적 Java 122/413종·552경로, 잔여 Java 291종/Python 150종.

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

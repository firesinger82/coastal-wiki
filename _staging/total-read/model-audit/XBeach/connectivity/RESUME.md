# 2026-09-10 재개 지점

현재 작업은 plan.md의 **XBeach 전수 판독 → 연결 분석 → 검증 → canonical → 필요한 신규 HG, 이후 FUNWAVE**다. 연결 후보는 lifecycle/ 및 physics/에 남아 있다. 전체 판독 gate는 **NOT_PASSED**다. 이 문서는 완료 또는 승인 영수증이 아니다.

## 이번에 처리한 범위

- 원본 source_code 456 + manuals 87 = 543개 경로 집합·SHA, closure 불변 기록 292개 SHA 일치.
- ZIP/JAR 9개, member 1,722개 경로·크기·SHA 일치. 저장 상태는 unread 1,284 / read-text 96 / visually-inspected 334 / directory 8이며 중복 경로 수를 고유 content 수와 혼동하지 않는다.
- Office 5문서 36페이지를 렌더링·판독했다. adapted_front 수식, 곡선격자 슬라이드 19장과 WMF 수식 9개, decision tree 초안, 설치 메모, membership archive를 포함한다. members.doc의 VBA 원문은 97개 control 선언과 모듈 속성뿐이며 실행 본문은 없다. 컴파일된 내부 코드까지 판독했다고 하지 않는다.
- Jumpshot PDF 61페이지 전량 시각 보충 판독. 원 Table 3.22에도 SUMMARY_STATE_DISPLAY가 빠져 있다. 예제 C의 마지막 코드는 물리 p.60–61에 있으며 복원했다. 원문 자체의 누락/배치 문제와 변환 손실을 구별했다.
- namespaces.xls의 E1=COUNTA(C2:C102)를 BIFF 토큰에서 복원하고 값 43을 재계산했다. F1=47은 수식이 아닌 RK 상수 레코드다.
- MSI 2개 stream 106개와 cabinet member 123개의 원본 결박·크기·SHA를 재검증했다. 93개 member는 raw 트리와 동일 SHA다. PE/AR 59개는 import/export/resource-directory 인덱스를 저장했다. DLL 의존성 관측을 전체 구현·리소스 판독으로 올리지 않았다.
- `resume-reconciliation.json`에 보충 근거 27개 원본 경로를 연결했다. 과거 변환본의 수식·도표 손실을 반영해 매뉴얼·보고서 9개 경로를 명시적으로 partial 상태로 보존했다. 근거 미연결 문서는 0개지만 전량 의미 판독 미완료와는 다른 수치다.

## 다음 작업

1. `resume-reconciliation.json`의 `text-read-with-unresolved-equation-or-layout-loss` 9개 경로를 원문 시각 판독으로 보충한다. 고유 저작물 3개, source_code의 DOC(X)/PDF 6표현과 manuals의 동일 PDF 3복제다. PDF 원본은 Kingsday 141p, master 145p, non-hydrostatic draft 69p다. DOC(X)는 각 표현의 수식·도표를 별도로 확인하며 다른 확장자의 같은 제목을 근거로 승계하지 않는다.
2. 외부 바이너리의 리소스 payload와 AR 내부 member·JAR bytecode의 처리 범위를 계속 명시한다. `msi-interface-review.json`은 의존성 관측과 추출 인덱스이며 의미 판독 완료가 아니다. 기존 interim interface/resource 범위로 진행하되 전체 gate 예외나 전체 역어셈블리 승인을 발급하지 않는다.
3. 위 전제가 충족된 뒤 연결 후보를 확정한다. FUNWAVE는 읽기 전용 preflight 이외 단계로 넘어가지 않았다.

## 재현 및 검증

저장된 문서 페이지 이미지는 `office-read/`, `jumpshot-pdf-read/`에 있어 재부팅 후에도 남는다. 원본을 재생성하거나 수정하지 않는다.

```sh
python3 _staging/total-read/model-audit/XBeach/connectivity/recover_msi.py
python3 _staging/total-read/model-audit/XBeach/connectivity/build_msi_interfaces.py
python3 _staging/total-read/model-audit/XBeach/connectivity/reconcile_resume.py
python3 _staging/total-read/model-audit/XBeach/connectivity/validate_resume_evidence.py
```

필요 도구: Python olefile, cabextract 1.11, objdump. Office 변환은 LibreOffice 24.2.7의 headless PDF/Text export, 페이지 렌더는 pdftoppm scale-to 1600을 사용했다. WMF 수식은 Draw PDF export로 겹침 없이 따로 판독했다. 원문에서 가져온 셸 예제나 VBA를 실행하지 않았다.

validator의 PASS는 구조·원본 SHA·이미지 SHA·입력 집합 검증만 뜻한다. 독립 의미 검증이나 사람 승인이 아니다. 이전 사람 승인·crosswalk·closure 기록은 그대로 보존했다.

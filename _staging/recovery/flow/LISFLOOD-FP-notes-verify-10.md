# LISFLOOD-FP 노트 추가·수정 줄 전수 대조 (2026-10-21)

이 기록은 사용자 지정 노트 세 파일의 대상 줄을 원문과 대조한 결과다.
기존 노트의 대상은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄이다.
새 노트 두 파일의 대상은 frontmatter와 빈 줄을 포함한 전체 줄이다.
정정 수와 보완 수는 검증 완료본의 각 표식이 붙은 줄 수로 센다.
한 줄을 여러 문장으로 나눈 경우에는 나눈 뒤의 줄을 센다.
줄 번호는 별도 표시가 없으면 검증 완료 후 노트 기준이다.

## 진행

| 노트 | 대상 줄 수 | 상태 | 정정 수 | 보완 수 |
|---|---:|---|---:|---:|
| `source-analysis/lisflood-fp-architecture-source-map.md` | 107 | 완료 | 10 | 8 |
| `manual-notes/lisflood-fp-docx-manual-differences.md` | 75 | 완료 | 7 | 4 |
| `manual-notes/lisflood-fp-bridge-manual-differences.md` | 71 | 완료 | 1 | 13 |

## 대조 결과

### source-analysis/lisflood-fp-architecture-source-map.md — 완료

작업 시작 시 `git diff -U0 HEAD`의 추가 줄 107줄을 모두 대조했다.
원래 줄 범위는 `2,4,7–8,12–13,17–40,42–43,53,65–66,73–89,94,98–151`이다.
대상 94행의 정확도·비용 순위 표현을 고치면서 인접한 제목·코드 울타리·화살표 4줄(원래 91·93·95·96행)도 함께 고쳤다.
완료본은 159줄이다.

| 대조 구간 | 결과와 근거 |
|---|---|
| frontmatter 6줄 | 제목·component·판 이력·기준일·related를 현재 코드와 `bf804e23` 원분석에 대조했다. 두 related 경로가 존재한다. |
| 본문·제목·빈 줄 | 현재 코드의 main·CPU·CUDA·Metal 분기와 이전 8.0·8.1·8.2 배포본을 열었다. 모든 코드 인용의 조건·식·줄 번호를 확인했다. 빈 줄과 Markdown 구문도 대상에 포함했다. |
| 본문 교체 근거 | 보고서 §4의 LB1-382·LN1-237·LG1-001·LG2-023/035/046/092·LV1-253/279–283/294·LI2-342·LI1-367/373·LT1-413/414를 대조했다. callflow §6의 RF-014/015/017/018도 대조했다. |
| 차이 표 18행 | 배정표와 최종 TSV의 행 ID·분류를 모두 대조했다. 각 conclusion-verify의 마지막 결론 문장과 일치한다. 아래 정정은 원문 칸·참조·표식에 적용했다. E 행은 없다. Claude 최종 조정의 세 E 행과 외부 원문 최종 조정 행은 이 표에 없다. |
| 문서 이미지 | PDF p.1·5·10–12·15–22, DOCX p.1·5·14–15·19–26, bridge DOCX p.1·5를 열었다. 문서 판·수치·표·기능 누락을 이미지로 판정했다. DOCX 쪽은 LibreOffice 변환본 기준이다. |
| 실행 흐름 | 노트에는 mermaid 블록이 없다. 흐름도 링크와 Metal 시작 인용을 callflow §4의 10-21 Claude 수정본·렌더 확인 문단에 대조했다. |
| 경로·제한 문구 | 완료본 Markdown 링크 30개가 실제 파일을 가리킨다. 절대 경로·`~/`·위키 이중 대괄호·사용자가 금지한 미수행/후속 문구가 없다. |

차이 표 행 ID: `LB1-382, LN1-136, LN1-237, RF-001, RF-015, RF-017, LG2-092, LG1-001, LV1-253, LV1-283, LV1-294, LI2-342, LI1-291, LI1-367, LI1-373, LT1-300, LT1-413, LT1-414`.

#### 정정·보완 목록

아래 줄 번호는 `models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md`의 완료본 기준이다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| architecture-source-map.md:77 | 보완 | 지형 detail 코드만 인용 → DOCX p.24의 `limitslopes` 인용 추가 | DOCX p.24의 `Enable the DG2 minmod slope limiter`; `encode_and_thresh_topo.cu:29–54`의 수준별 epsilon·지형 detail 조건. |
| architecture-source-map.md:91 | 정정 | 정확도·비용 스펙트럼 → 물리·수치해법 구분 | PDF p.11은 ACC가 adaptive 확산파보다 계산 시간을 줄일 수 있다고 적는다. 기존 단조 비용 순위의 근거가 되지 않는다. |
| architecture-source-map.md:93 | 정정 | 코드 울타리 → 확산파의 두 가속도 생략 설명 | PDF p.10 표 1·p.11의 `Both local and convective acceleration terms are assumed negligible.` |
| architecture-source-map.md:94 | 정정 | diffusive < ACC < FV1 < DG2 순위 → ACC의 국소 관성 설명 | PDF p.10 표 1·p.11은 acceleration이 이류 가속도만 생략한다고 적는다. |
| architecture-source-map.md:95 | 정정 | 고속·고정확 화살표 → FV1의 1차 Godunov형 유한체적 설명 | DOCX p.5의 `first-order finite volume (FV1)`; p.14의 `Godunov-type finite volume method`. |
| architecture-source-map.md:96 | 정정 | 코드 울타리 → DG2의 2차 불연속 Galerkin 설명 | DOCX p.5·15의 `second-order discontinuous Galerkin`. |
| architecture-source-map.md:118 | 보완 | PDF 표지 판에 쪽 인용 없음 → PDF p.1 추가 | PDF p.1 `Code release 6.1.1`. |
| architecture-source-map.md:119 | 보완 | PDF 날짜에 쪽 인용 없음 → PDF p.1 추가 | PDF p.1 `25th November 2013`. |
| architecture-source-map.md:120 | 정정 | DOCX 판을 5.9로만 설명 → 표지의 삭제·삽입 구분 | DOCX p.1의 6.1.1 삭제선과 8.0.0 삽입선. callflow §5.1. |
| architecture-source-map.md:121 | 정정 | 판 이력 맨 위 5.9 → 삽입된 8.0(2020-07-20) | DOCX p.5의 최상단 `8.0 Jul 20 2020`. RF-001 최종 근거. |
| architecture-source-map.md:122 | 보완 | bridge 표지 판에 쪽 인용 없음 → 변환본 p.1 추가 | bridge DOCX p.1 `Code release 4.3.6`. |
| architecture-source-map.md:123 | 보완 | bridge 날짜에 쪽 인용 없음 → 변환본 p.1 추가 | bridge DOCX p.1 `25th April 2008`. |
| architecture-source-map.md:124 | 정정 | 8.3 DOI 13121119를 적용 관계에 함께 귀속 → 직접 근거가 있는 8.2 DOI·8.3 변경 적용 관계로 정리 | 패키지 `README.md:19–24`는 8.2 DOI 13121102만 적는다. 최종 LB1-408은 이 줄을 8.3 DOI의 근거로 쓰지 말라고 정정한다. |
| architecture-source-map.md:125 | 보완 | 숫자 판과 릴리스 이름 압축 → 체크포인트 숫자 판을 별도 인용 | `VersionHistory.h:16–18`의 8·1·0과 21–22행의 checkpoint 주석. |
| architecture-source-map.md:126 | 보완 | 같은 압축 문장 → 릴리스 이름을 별도 인용 | `VersionHistory.h:23`의 `#define LF_Release "8.3"`. |
| architecture-source-map.md:130 | 정정 | LB1-382의 “배포판 표시는 §1과 같다” → LF_Release 원문 직접 인용 | `VersionHistory.h:23`. 노트 §1에는 해당 배포판 표기 설명이 없었다. |
| architecture-source-map.md:137 | 정정 | LG1-001의 존재하지 않는 §2.7 참조 → Metal 전달 호출 직접 설명 | `metal/metal_integrate.cpp:7–13`의 `run_metal_fv1`과 `lis::metal::fv1::simulate`. |
| architecture-source-map.md:139 | 보완 | LV1-283의 DOCX p.23까지 인용 → p.24 추가 | DOCX p.24가 DG2 `limitslopes`를 설명한다. detail 식 원문은 그대로 유지했다. |

#### 기계 확인 후보 판정

- `CMakeLists.txt:73` 후보는 검사기 오판이다. 현재 원문은 `if (CMAKE_CUDA_COMPILER)`이다. 노트 LG2-092와 일치하므로 유지했다.
- `CMakeLists.txt:77` 후보는 검사기 오판이다. 현재 원문은 `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)`이다. 노트 LG2-092와 일치하므로 유지했다.
- `CMakeLists.txt:178` 후보는 검사기 오판이다. 현재 원문은 `add_subdirectory(cuda/adaptive)`이다. 노트 LG2-092와 일치하므로 유지했다.

이 노트에 미해결 항목은 없다.

### manual-notes/lisflood-fp-docx-manual-differences.md — 완료

작업 시작 시의 전체 75줄을 대조했다.
frontmatter 17줄과 빈 줄을 포함했다.
완료본은 81줄이다.

| 대조 구간 | 결과와 근거 |
|---|---|
| frontmatter·도입부 | DOCX p.1·5와 PDF p.1의 판 표기를 대조했다. 판 설명을 고쳤다. frontmatter의 YAML 구문과 related 두 경로가 유효하다. |
| 차이 표 28행 | note-job-6.tsv·최종 TSV와 모든 행 ID·분류가 일치한다. A 26행과 B 2행이다. E 행은 없다. RF·LV1 최종 결론을 행마다 대조했다. LV1-066의 판독 기록 표기만 현재 기록과 맞게 고쳤다. 판 차이와 수치 결론은 유지했다. |
| 현재 코드 | 인용한 pars.cpp·lisflood.cpp·lisflood.h·fp_acc.cpp·iterateq.cpp·lisflood2/lis2_output.cpp·output.cpp·swe/fv1.cpp·swe/dg2.cpp·swe/output.cpp·swe/dg2/slope_limiter.cpp·rain/rain.tpp를 열었다. 긍정·부정·선택 순서·기본값·단위를 대조했다. |
| 이전 판 | 인용한 v8.0·v8.1·v8.2 파일을 직접 열었다. FV1 수심 임계값 1e-6에서 1e-3으로의 변경, DEM_NO_DATA 1e10에서 1e7로의 변경, limitslopes의 FV2 확대, CUDA 해법 추가를 각각 해당 판에 귀속했다. |
| 문서 이미지 | DOCX p.1·5·13–15·19–26·36–37과 PDF p.1·10–12·15–21·31–32를 열었다. 식·지수·단위·표의 제외 조건을 이미지로 판정했다. DOCX p.22·25·26·37 판독 기록도 대조했다. |
| 본문 64–75행(원래 번호) | RF-002·RF-006 최종 결론을 코드와 대조했다. Metal 연결 대상과 근거 링크를 열었다. 새 노트를 직접 지목한 별도 §4 수정안은 반영 기록 6에 없다. |
| 구조·경로 | mermaid 블록이 없다. 완료본 Markdown 링크 7개와 related 두 경로가 존재한다. 절대 경로·`~/`·위키 이중 대괄호·사용자가 금지한 미수행/후속 문구가 없다. |

차이 표 행 ID: `RF-002, RF-006, LV1-013, LV1-018, LV1-019, LV1-027, LV1-039, LV1-047, LV1-048, LV1-062, LV1-064, LV1-065, LV1-066, LV1-069, LV1-070, LV1-083, LV1-101, LV1-102, LV1-103, LV1-105, LV1-106, LV1-110, LV1-111, LV1-113, LV1-114, LV1-120, LV1-122, LV1-167`.

#### 정정·보완 목록

아래 줄 번호는 `models/LISFLOOD-FP/manual-notes/lisflood-fp-docx-manual-differences.md`의 완료본 기준이다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| docx-manual-differences.md:4 | 정정 | frontmatter의 판 이력 맨 위 5.9 → p.1의 8.0.0 삽입 표지와 p.5의 8.0 삽입 이력 | DOCX p.1·5 쪽 이미지. YAML 주석으로 정정 표식을 붙였다. |
| docx-manual-differences.md:29 | 정정 | DOCX 판을 5.9로만 설명 → 표지의 삭제·삽입 구분 | DOCX p.1의 6.1.1 삭제선과 8.0.0 삽입선. |
| docx-manual-differences.md:30 | 정정 | 판 이력 맨 위 5.9 → 삽입된 8.0(2020-07-20) | DOCX p.5의 최상단 `8.0 Jul 20 2020`. RF-002·RF-006 최종 근거. |
| docx-manual-differences.md:31 | 보완 | PDF 표지 판에 쪽 인용 없음 → PDF p.1 추가 | PDF p.1 `Code release 6.1.1`. |
| docx-manual-differences.md:32 | 보완 | PDF 날짜에 쪽 인용 없음 → PDF p.1 추가 | PDF p.1 `25th November 2013`. |
| docx-manual-differences.md:33 | 정정 | 8.3 DOI 13121119의 귀속 → 8.2 DOI와 8.3 변경 적용 관계 | 패키지 `README.md:19–24`; 최종 LB1-408의 인용 정정. |
| docx-manual-differences.md:34 | 보완 | 내부 숫자 판과 릴리스 이름 압축 → 체크포인트 숫자 판 별도 인용 | `VersionHistory.h:16–22`의 8.1.0과 checkpoint 주석. |
| docx-manual-differences.md:35 | 보완 | 같은 압축 문장 → 릴리스 이름 별도 인용 | `VersionHistory.h:23`의 `#define LF_Release "8.3"`. |
| docx-manual-differences.md:51 | 정정 | LV1-066의 “판독 기록의 1010” → 이미지와 현재 판독 기록 모두 10의 10제곱 | DOCX p.22 이미지와 `read/LISFLOOD-FP/LISFLOOD-FP/LISFLOOD-FP user manual.docx/p019-036.md:18`은 모두 `$10^{10}$`을 적는다. 최종 근거의 기록 상태 설명만 현 상태와 달랐다. v8.0의 1e10과 v8.1의 1e7 결론은 그대로다. |
| docx-manual-differences.md:62 | 정정 | LV1-113의 “최대·최초·누적 침수량” → 최대 수심·최대 수심 시각·최초 침수 시각·누적 침수 시간 | DOCX p.25 `mint_hk` 행의 maxH·maxHtm·initHtm·totalHtm. `iterateq.cpp:198–206`의 시간·수심 배열 대입도 일치한다. |
| docx-manual-differences.md:66 | 정정 | 첫 timestamp는 0 → 첫 timestamp를 0으로 둘 것을 권고 | DOCX p.37 `The first rainfall timestamp should be 0`. 뒤의 sim_time 권고와 같은 의무 강도로 옮겼다. |

이 노트에 사용자가 지정한 기계 확인 후보는 없다.
이 노트에 미해결 항목은 없다.

### manual-notes/lisflood-fp-bridge-manual-differences.md — 완료

작업 시작 시의 전체 71줄을 대조했다.
frontmatter·빈 줄·제목·표 머리글을 포함했다.
완료본은 77줄이다.

| 대조 구간 | 결과와 근거 |
|---|---|
| frontmatter·도입부 | bridge p.1·2와 PDF p.1의 판 표기를 대조했다. frontmatter의 YAML 구문과 related 두 경로가 유효하다. 문서 원문과 AI 결론은 별도 칸에 있다. |
| 차이 표 22행 | final-conclusions.tsv와 최종 LB1a·LB1b의 분류 및 결론 문장을 모두 대조했다. A 8행과 B 14행이다. 문서 이름 풀어쓰기·링크·검증 표식을 제외한 결론 문장이 최종 근거와 같다. E 행은 없다. Claude 최종 조정 3행과 external-sources 끝 절의 조정 행은 이 표에 없다. |
| 문서 이미지 | bridge p.1·2·5·6·8·9·19·21–24·27–30·32–33·35–36·38·41–44·47–50과 PDF p.1·2·34·40–41을 열었다. 식·수량·배열 크기·자료형·날짜를 이미지로 판정했다. 해당 쪽의 판독 기록도 대조했다. |
| 현재 코드 | VersionHistory.h의 판·교량 도입·구조체 도입·htol·출력 통합 이력을 열었다. pars.cpp의 입력 분기와 공통 문자열·수치 파서를 열었다. lisflood.cpp·lisflood.h의 초기값·구조체·자료형·배열 선언을 열었다. input.cpp의 보·격자·시계열 할당과 포인터 연결을 열었다. boundary.cpp의 보간, util.cpp의 SmoothBanks 인수, output.cpp의 outflag 분기를 열었다. ch_flow.cpp:840–847, fp_flow.cpp:157–167, iterateq.cpp:539–540의 식을 대조했다. |
| 이전 판 | v8.0의 pars.cpp:558–562, weir_flow.cpp:138–143, input.cpp:1340–1343·1970–1972, lisflood.h:311–323·381–395·444–448·661–667·708·753–759를 열었다. A 행의 기준은 4.3.6 문서이다. v8.0 자료를 4.3.6 코드로 바꾸어 부르지 않았다. |
| 검색 기록 | 현재·v8.0·v8.1·v8.2 전체 트리에서 touput·tpouput·ch_dyanmic과 따옴표 안 checkfile은 각각 0행이다. 내부 상태명 checkfile은 순서대로 10·6·10·10행이다. 원문 일치 위치를 열람했다. 보고서 S1·S2 및 최종 LB1-099–102의 검색 결과와 같다. |
| 본문 56–71행(원래 번호) | LB1-147·LB1-221·LB1-238의 최종 결론을 대조했다. bridge p.47의 식 [6] 본체는 비어 있다. p.48의 [7]·[8]·[9], p.49의 [10]·[11]·[14], p.50의 [16]은 노트와 같다. 반영 기록 6에서 새 노트를 직접 지목한 별도 §4 수정안은 없다. |
| 구조·경로 | mermaid 블록이 없다. 완료본 Markdown 링크 9개와 related 두 경로가 존재한다. S1·S2 링크는 보고서의 실제 검색 기록 절을 가리킨다. 절대 경로·`~/`·위키 이중 대괄호·사용자가 금지한 미수행/후속 문구가 없다. |

차이 표 행 ID: `LB1-001, LB1-050, LB1-099, LB1-100, LB1-101, LB1-102, LB1-105, LB1-147, LB1-170, LB1-221, LB1-238, LB1-240, LB1-241, LB1-247, LB1-249, LB1-252, LB1-254, LB1-256, LB1-257, LB1-258, LB1-261, LB1-263`.

#### 정정·보완 목록

아래 줄 번호는 `models/LISFLOOD-FP/manual-notes/lisflood-fp-bridge-manual-differences.md`의 완료본 기준이다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| bridge-manual-differences.md:29 | 보완 | bridge 표지 판에 쪽 인용 없음 → 변환본 p.1 추가 | bridge p.1 `Code release 4.3.6`. |
| bridge-manual-differences.md:30 | 보완 | bridge 날짜에 쪽 인용 없음 → 변환본 p.1 추가 | bridge p.1 `25th April 2008`. |
| bridge-manual-differences.md:31 | 보완 | PDF 표지 판에 쪽 인용 없음 → PDF p.1 추가 | PDF p.1 `Code release 6.1.1`. |
| bridge-manual-differences.md:32 | 보완 | PDF 날짜에 쪽 인용 없음 → PDF p.1 추가 | PDF p.1 `25th November 2013`. |
| bridge-manual-differences.md:33 | 정정 | 8.3 DOI 13121119의 귀속 → 8.2 DOI와 8.3 변경 적용 관계 | 패키지 `README.md:19–24`; 최종 LB1-408의 인용 정정. |
| bridge-manual-differences.md:34 | 보완 | 내부 숫자 판과 릴리스 이름 압축 → 체크포인트 숫자 판 별도 인용 | `VersionHistory.h:16–22`의 8.1.0과 checkpoint 주석. |
| bridge-manual-differences.md:35 | 보완 | 같은 압축 문장 → 릴리스 이름 별도 인용 | `VersionHistory.h:23`의 `#define LF_Release "8.3"`. |
| bridge-manual-differences.md:40 | 보완 | LB1-050의 gaugefile 등록만 인용 → 공통 문자열 파서 추가 | `pars.cpp:54–72`는 파일명을 `%255s`로 읽으며 확장자 조건을 두지 않는다. |
| bridge-manual-differences.md:41 | 보완 | LB1-099의 무연결 §5·LB1-084 참조 → 실제 보고서와 최종 근거 링크 | 보고서 §5의 `D 검색 기록 S1·S2`; 최종 LB1a의 LB1-084·099. |
| bridge-manual-differences.md:42 | 보완 | LB1-100의 무연결 S1 참조 → 실제 보고서 절 링크 | 보고서 S1b의 tpouput 0행; 최종 LB1-100. |
| bridge-manual-differences.md:43 | 보완 | LB1-101의 무연결 S1 참조 → 실제 보고서 절 링크 | 보고서 S1c의 ch_dyanmic 0행; 최종 LB1-101. |
| bridge-manual-differences.md:44 | 보완 | LB1-102의 무연결 S2 참조 → 실제 보고서 절 링크 | 보고서 S2의 내부 상태 참조; 최종 LB1-102. |
| bridge-manual-differences.md:52 | 보완 | LB1-247의 출력 함수 선언만 인용 → outflag 설명·처리 본문 추가 | `output.cpp:39–48,96–172`의 일반 출력·면 유량·DEM+H 분기. |
| bridge-manual-differences.md:53 | 보완 | LB1-249의 시계열 함수 호출만 인용 → 입력 배열 할당·읽기 추가 | `input.cpp:1882–1903`의 ndata 크기 할당과 `timeSeries.value[i]`, `timeSeries.time[i]` 읽기. |

이 노트에 사용자가 지정한 기계 확인 후보는 없다.
이 노트에 미해결 항목은 없다.

## 완료 확인

대상 253줄은 architecture 107줄, DOCX 75줄, bridge 71줄의 합이다.
대상 줄을 모두 원문 및 최종 근거와 대조했다.
architecture의 인접 4줄 정리는 해당 노트 결과에 별도로 기록했다.
완료본의 정정 표식은 18줄이다.
완료본의 보완 표식은 25줄이다.
표식이 붙은 43줄과 이 기록의 정정·보완 목록 줄 번호가 모두 일치한다.
차이 표 68행의 분류는 final-conclusions.tsv와 일치한다.
Markdown 상대 링크 46개와 related 경로 6개가 모두 실제 파일을 가리킨다.
세 노트의 YAML 구문과 표 행의 검증 표식 위치가 유효하다.
`git diff --check HEAD -- <대상 노트 3개>`는 종료 코드 0이며 오류 출력이 없다.
기계 확인 후보 3건은 모두 현재 CMakeLists.txt 원문과 일치한다.
미해결 항목은 없다.

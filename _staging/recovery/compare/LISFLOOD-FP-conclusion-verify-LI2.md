# LISFLOOD-FP LI2 차이 결론 재검증

## 1 요약

대상은 `lisflood-files-output-vs-code.md`의 §5에 있는 LI2 136행이다. H 행도 포함한다.

| 최종 결론 | 행 수 |
|---|---:|
| A 판 차이 | 29 |
| B 문서 오기 | 25 |
| C 문서 누락 | 42 |
| D 문서에만 있음 | 1 |
| E 코드 결함 후보 | 19 |
| F 표기 차이 | 0 |
| H 코드 대조 대상 아님 | 19 |
| 일치 | 1 |
| 합계 | 136 |

E 강도는 강함 12행, 중간 6행, 약함 1행이다. 보고서 결론에서 바뀐 행은 18행이다. 유지한 행은 118행이다. 인용을 고친 행은 6행이다. 집계 근거는 아래 행별 표이다.

인용 교정 행은 LI2-011·064·124·137·196·311이다. LI2-011은 수량의 적용 범위를 고쳤다. LI2-064는 면적 제한 조건을 보완했다. LI2-124는 E1의 문서 쪽 인용을 p.15에서 p.16으로 고쳤다. LI2-137은 코드 변수명을 고쳤다. LI2-196은 세 파일과 두 속도 파일의 수량 구분을 고쳤다. LI2-311은 a 분기의 선행 조건을 보완했다. LI2-349의 NULL 포인터 설명은 해석 교정이므로 인용 교정 수에 넣지 않았다.

`바뀜`은 보고서 §5의 분류 또는 명시된 E 강도가 달라진 경우이다. 인용 교정은 보고서와 참고 판정에서 글자·식·수량·조건·쪽 위치를 고친 행을 별도로 센다. 단순한 설명 보강과 근거 추가는 인용 교정으로 세지 않는다.

파일 경로의 기본 위치는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`이다. `v8.0:`은 `_staging/recovery/extract/LISFLOOD-FP/external/v8.0/LISFLOOD-FP-trunk/`이다. `v8.1:`은 같은 external 아래 `v8.1/LISFLOOD-FP-trunk/`이다. `v8.2:`는 같은 external 아래 `v8.2/LISFLOOD-FP/`이다. `v8.3:`은 같은 external 아래 `v8.3/LISFLOOD-FP-8.3/`이다. `패키지:`는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP-8.3-package/`이다.

PDF는 `LISFLOOD-FP user manual.pdf`이다. 쪽 번호는 제공된 `lf-manual-pdf-NNN.png`의 쪽 번호이다. 문서 문장·식·표는 쪽 이미지를 직접 확인했다. PDF p.1은 표지 6.1.1과 2013-11-25를 적는다. p.2는 6.0.4를 적는다. 본문 머리글은 5.9.6이다. 판 판정 파일은 참고 판정으로만 사용한다. 아래 문장은 원문을 재대조한 AI 판정이다. 모델 실행은 하지 않았다.

참고 판정의 AD1은 `LISFLOOD-FP-version-verify-AD1.md`이다. E1은 `LISFLOOD-FP-version-verify-E1.md`이다. 외부 원문 판정은 `LISFLOOD-FP-external-sources.md`의 마지막 절이다. 표본 검증의 LI2-105 판정도 원문과 일치했다.

DEFRA 2003 원문은 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/w/p1.pdf`이다. DEFRA 2006 원문은 같은 scratchpad의 `Flood_risks_to_people_-_Phase_2_The_flood_risks_to_people_methodology_technical_report.pdf`이다. 두 외부 PDF도 해당 쪽을 이미지로 열어 확인했다.

## 2 행별 최종 결론 표

### 2.1 LI2-002–096

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| LI2-002 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.22·34; pars.cpp:164–167; lisflood.cpp:332 | p.34의 `root.op, root.mass, root-0001.wd`가 p.22의 `suffix .res_D`와 모순된다. | resroot는 결과 파일명의 접두부이다. 파일 종류가 확장자를 정한다. |
| LI2-011 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.22; input.cpp:539–552,675–687 | 입력 작성 지침이다. 원문은 상류와 하류의 각 끝에 제한을 둔다. 수량 범위를 보완했다. | 상류·하류의 각 끝에서 영역 밖 벡터점은 하나 이하여야 한다. 각 DEM 셀의 벡터점은 하나 이하여야 한다. 로더의 자동 검사로 설명하지 않는다. |
| LI2-015 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.22–24; input.cpp:394–418,435–447 | p.23 표의 앞 두 행은 Tribs와 자료점 개수이다. 같은 표의 `Line i`와 선택 속성 설명이 자료점 번호를 파일 행 번호와 혼용한다. | 선택 속성은 양 끝 자료점 사이에 적용한다. Tribs·개수 행을 포함한 실제 파일 행 번호와 구분한다. |
| LI2-021 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.24; input.cpp:401,411–418,831 | `infinite stream order`는 수지상 연결의 표현 설명이다. 정수·메모리 무제한이라는 실행 보장이 아니다. | 임의의 수지상 연결을 표현한다는 설명이다. 무한 정수·메모리를 보장한다는 뜻은 아니다. |
| LI2-029 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.25; input.cpp:1645–1651 | 문서가 사용자에게 중복 입력 금지를 지시한다. 자동 검사라는 주장은 없다. | 같은 셀의 점 경계를 중복 작성하지 않는다. 자동 중복 검사나 합산으로 설명하지 않는다. |
| LI2-037 | B 문서 오기 | A 판 차이 (AD1) | B | 아니오 | PDF p.26–27; input.cpp:1920–1931; VersionHistory.h:453–454 | AD1의 A를 채택하지 않는다. 같은 PDF가 days를 열거한다. 2.6.4의 days 추가는 문서 머리글 5.9.6보다 앞선다. | days도 지원한다. minutes 추가는 별도 판 차이이다. |
| LI2-039 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.27; input.cpp:1953–1978,2020–2057,2080–2116; boundary.cpp:283,1422–1429 | NULL 초기화와 무방어 보간이 충돌한다. 누락 경계를 NONE0으로 만드는 반대 경로는 bdy 파일명을 주지 않은 else에만 있다. | 존재하는 bdy에서 참조한 이름을 빠뜨리면 경계 시계열이 NULL로 남는다. 해당 경계의 보간은 NULL을 역참조하는 결함 후보이다. 강도는 강함이다. |
| LI2-040 | C 문서 누락 | - | A | 예 | PDF p.1–2·27; input.cpp:2065–2076 | 문서는 경고의 verbose 조건을 명시했다. 누락이 아니라 과거 설명과 현재 동작의 차이이다. 그 문서 판에서도 틀렸다는 근거는 없다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 미참조 bdy 경고는 `if (timeSeriesUsed == 0)`에서 verbose와 무관하게 출력한다. |
| LI2-044 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.27; input.cpp:1480 | GIS·텍스트 편집기 사용 안내이다. | DEM 편집 도구 사용 안내는 외부 작업 절차로 적는다. |
| LI2-046 | B 문서 오기 | B 문서 오기 (AD1) | A | 예 | PDF p.1–2·27; input.cpp:1007–1055,1065–1076; VersionHistory.h:60,391–394 | AD1의 B를 바꾼다. 공극률 도입 기록은 당시 입력 형식의 오류를 입증하지 않는다. 변경 기록의 부재를 문서 오기의 근거로 쓰지 않는다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 공극률 로더는 같은 파일에서 방법 토큰과 수치 배열을 읽는다. |
| LI2-047 | D 문서에만 있음 | D 문서에만 있음 (AD1) | D | 아니오 | PDF p.27; 현재 input.cpp:1007; v8.0:input.cpp:978; v8.1·v8.2:input.cpp:1007; 네 코드 트리의 rg -i 결과 | 네 트리에서 `rg -i -n --no-ignore --glob '!testing/**' '(write_\|fprintf\|fwrite\|fopen\|ofstream).*por\|por.*(write_\|fprintf\|fwrite\|fopen\|ofstream)'`를 실행했다. 현재·v8.0·v8.1·v8.2의 검색 결과는 8·7·7·7행이다. 공극률 파일 접근은 읽기뿐이다. 같은 옵션의 `porosity\|paerial\|pbound\|porfilename` 검색은 각 104행이다. 전용 출력 writer는 없다. 일반 침수 면적 보정은 별개이다. | 현재·v8.0·v8.1·v8.2 코드에는 문서가 말한 공극률 전용 추가 출력 writer가 없다. 일반 침수 면적 보정과 구분한다. |
| LI2-048 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.27; input.cpp:1023 | 별도 매뉴얼 요청과 성숙도 주장은 실행 코드의 검증 대상이 아니다. | 별도 자료 요청과 방법론의 성숙도 설명을 로더 검증과 구분한다. |
| LI2-053 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.28; lisflood.cpp:130–135 | `average UK gravel bed river`는 계수의 대표성 주장이다. 코드 주석은 대표성을 검증하지 않는다. | 기본 수리기하 관계의 적용 대상 설명을 코드 계수 대조와 구분한다. |
| LI2-055 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.28 | 같은 쪽이 `.pram`의 실제 절 번호를 3.2.13으로 적는다. 4.2.11은 절 번호 오기이다. | pram 형식의 참조 번호를 3.2.13으로 적는다. |
| LI2-058 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.28; sgc.cpp:402–405,424,513–515 | 같은 쪽의 무하도 셀에 대한 `will have no effect`와 `ignored by the model`을 대조했다. region 문장의 `will have any effect`는 부정 누락이다. | 폭이 없는 셀에는 region의 하도 수리기하를 적용하지 않는다. 유효한 region 인덱스 작성 의무는 남는다. |
| LI2-060 | C 문서 누락 | - | C | 아니오 | PDF p.28; input.cpp:2389–2406; sgc.cpp:402–405 | 지역 번호의 순차 작성은 문서에 있다. 첫 필드를 tmp로 버리고 행 인덱스로 저장하는 구현 조건은 없다. | pram 행은 지역 번호 순서로 작성한다. 첫 Region 값으로 행을 재배치하지 않는다. |
| LI2-064 | C 문서 누락 | - | C | 아니오 | PDF p.28; sgc.cpp:429–440; VersionHistory.h:130,153 | 직선 하도의 dx*m 설명에 이웃 연결과 면적 제한 조건이 빠졌다. | 현재 길이는 `Arrptr->SGCc[p0] = m*getmax(chan_length, getmin(dx, dy));`로 정한다. `if (w0 < getmax(dx, dy) && w0*Arrptr->SGCc[p0] > Arrptr->dA[p0])`이면 `Arrptr->SGCc[p0] = Arrptr->dA[p0] / w0;`를 적용한다. |
| LI2-066 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.28–29; input.cpp:2406; sgc.cpp:446 | 같은 문서의 `depth = r*width^p`에 예제의 p와 r을 넣으면 수심 비가 width^0.03이다. 고정 1.1이 아니다. | 예제의 수심 비는 폭의 0.03제곱이다. 고정 10% 증가가 아니다. |
| LI2-069 | E 코드 결함 후보(중간) | E 유지(약함) (E1) | A | 예 | PDF p.1–2·29–30; input.cpp:175–246,254–273,2345–2349; weir_flow.cpp:50–55,97 | E1의 약함도 채택하지 않는다. `Then index the cell it flows from`과 고정 유량 방향이 현재 배치를 지지한다. gauge는 지리적 면 기준이다. 서로 다른 기준만으로 코드 내부 결함을 확정하지 않는다. 당시 문서가 틀렸다는 근거도 없다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 구조물 태그 W·E·N·S는 각각 입력 셀의 동·서·남·북 면에 배치된다. 코드 주석은 기준 셀로 유입하는 방향을 사용한다. |
| LI2-070 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.29–30; input.cpp:165–195 | 같은 x에서 y만 바꾼 두 점의 동·서 면은 같은 면이 될 수 없다. 방향 태그 해석과 독립된 좌표 예제 오류이다. | 동서 이웃의 면을 비교하려면 x 셀 위치가 달라야 한다. y만 바꾼 예제를 사용하지 않는다. |
| LI2-072 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.29; input.cpp:161–163 | 문서는 `typically`로 계수와 modular limit를 권고한다. 로더는 두 값을 입력에서 읽는다. | 1.4와 0.9는 전형값이다. 로더 기본값으로 적지 않는다. |
| LI2-074 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.29–30 | `must be read`는 부록을 읽으라는 사용 지시이다. | 구조물 사용 전에 해당 부록을 읽으라는 의무를 유지한다. 부록 수리식은 이번 범위에 넣지 않는다. |
| LI2-076 | E 코드 결함 후보(중간) | E 유지(중간) (E1) | E(중간) | 아니오 | PDF p.30; input.cpp:225–248; fp_flow.cpp:47,95; weir_flow.cpp:109–136,267 | y 분기의 SGC 방어와 x 분기의 SGC 배열 접근이 모순된다. SGC 전용이라는 지원 제한은 비SGC x 호출을 막는 조건이 아니다. | 교량의 지원 범위는 SGC이다. 고전 CPU x 교량 분기에는 y 분기의 `Statesptr->SGC == ON` 검사가 없다. 비SGC 교량 입력에 대한 방어 누락 후보이다. 강도는 중간이다. |
| LI2-078 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.30; input.cpp:161–163 | `typically 0.8`과 `should be a value of 1.5`는 권고이다. | 교량 계수 0.8과 전이 상한 1.5는 권고값이다. 입력 기본 대입값은 아니다. |
| LI2-079 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.29–30; input.cpp:161–166 | bridge 행 형식에는 DEM 헤더 필드가 없다. 같은 문서의 weir 각주는 X·Y를 대상으로 한다. | bridge 입력의 X·Y는 도 단위이다. DEM 헤더 필드를 bridge 행 필드로 설명하지 않는다. |
| LI2-086 | C 문서 누락 | - | C | 아니오 | PDF p.31; infevap.cpp:51–79 | 문서는 `every model grid cell`이라고만 적는다. 일반 CPU의 하도 마스크와 수심 조건을 보완한다. | 일반 CPU 증발은 `if(Arrptr->ChanMask[i+j*Parptr->xsz]==-1)`과 `if(h0>Solverptr->DepthThresh)`를 만족하는 셀에 적용한다. |
| LI2-088 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.31; output.cpp:79–104 | 문서는 헤더 변경의 활용을 안내한다. 셀값을 그대로 출력하는 코드에서 재투영을 추론하지 않는다. | head는 헤더를 바꾼다. 좌표계 활용 안내를 실제 재투영 기능으로 바꾸지 않는다. |
| LI2-092 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.31; input.cpp:2323,2337–2349; util.cpp:242–259 | 영역 이탈을 막는 주석과 검사 축이 합산 경로와 모순된다. 단면 방향에 따라 축을 전환하는 반대 보정은 없다. | gauge의 N·S 단면은 x 방향으로 합산하지만 y 범위로 길이를 자른다. E·W 단면은 반대 축 오류를 가진다. 강도는 강함이다. |
| LI2-094 | C 문서 누락 | - | C | 아니오 | PDF p.32; infevap.cpp:89–108 | 균일 강우의 NoData 제외 조건이 문서에 없다. | 균일 강우의 일반 CPU Rainfall 경로는 `if (Arrptr->DEM[p0] != Parptr->nodata_elevation)`을 만족하는 셀에 적용한다. |
| LI2-096 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.32 | Sampson et al.의 성능·안정성 주장은 정적 입출력 대조로 재현하지 않는다. | 성능·안정성은 문서의 실험 주장으로 인용한다. 이번 정적 대조에서 재현하지 않았다. |

### 2.2 LI2-097–166

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| LI2-097 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.18·22·32·35; pars.cpp:563–567 | 같은 PDF의 표와 예제가 checkpoint를 사용한다. checkpointing은 기능명과 키워드를 혼동한 오기이다. | 실제 키워드는 checkpoint이다. checkpointing을 입력 키워드로 쓰지 않는다. |
| LI2-100 | B 문서 오기 | A 판 차이 (AD1) | B | 아니오 | PDF p.21·32; input.cpp:1244–1256; VersionHistory.h:119 | AD1의 A를 채택하지 않는다. p.32는 binary_out 결과를 시작 파일로 사용할 수 있다고 적는다. p.21은 그 결과의 double·float 양쪽 정밀도를 명시한다. 고정 double 설명은 같은 문서 안에서 모순된다. | binary 시작 파일의 실수 크기는 NUMERIC_TYPE이다. 같은 문서가 이미 float 출력을 명시하므로 double 고정 설명은 문서 내부 오기이다. |
| LI2-102 | B 문서 오기 | B 문서 오기 (AD1) | A | 예 | PDF p.18·32; pars.cpp:145–162; lisflood.cpp:494–502; VersionHistory.h:192–196 | AD1의 B를 바꾼다. p.18도 startelev filename으로 적는다. 5.2.3의 기능 추가 이력은 당시 플래그의 인수 형식을 입증하지 않는다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 파일명은 startfile 또는 binarystartfile 뒤에 둔다. startelev는 별도 플래그이다. |
| LI2-103 | C 문서 누락 | - | C | 아니오 | PDF p.32; input.cpp:1168–1187 | SGC 기준면과 음수 수심 제한이 문서에 없다. | SGC는 SGCz를 뺀다. 일반 경로는 DEM을 뺀다. 두 경로는 음의 수심을 0으로 제한한다. |
| LI2-105 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.27·33 | 같은 PDF의 실제 절 제목이 3.2.6이다. 표본 검증의 맞음 판정과 같다. | DEM 형식은 3.2.6을 참조한다. |
| LI2-108 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.33; input.cpp:447–450 | 현장 자료 취득과 과거 지형의 적합성 판단은 입력 형식 검사가 아니다. | 자료의 취득 방법과 시대 적합성은 입력 형식 검사와 별도 절차이다. |
| LI2-113 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.33 | 파일 준비 순서와 외부 훈련 자료 사용 안내이다. | 파일 준비 절차와 외부 훈련 자료 안내를 실행 옵션의 순서 규칙으로 옮기지 않는다. |
| LI2-116 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.33; CMakeLists.txt:231–237 | 과거 Mac OS 컴파일 주장을 현재 Metal 빌드 조건으로 입증할 수 없다. | 과거 컴파일 이력은 문서 주장으로 적는다. 8.3의 현재 Metal 추가와 구분한다. |
| LI2-119 | C 문서 누락 | - | A | 예 | PDF p.1–2·34; pars.cpp:895–899; output.cpp:179–182 | 문서가 Windows에서는 무시한다고 명시한다. 현재 일반 ASCII writer에는 운영체제 제외 조건이 없다. 명시된 과거 동작과의 차이를 단순 누락으로 두지 않는다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 일반 ASCII writer는 운영체제와 무관하게 gzip 명령을 요청한다. 호출 범위는 정기 파일에 한정되지 않는다. |
| LI2-121 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.15·34; pars.cpp:54–70,164 | 같은 문서의 resroot name 및 파일명 예제와 대조했다. p.34 옵션 칸에 이름 인수가 빠졌다. | 명령 줄은 -resroot name 형식이다. |
| LI2-123 | E 코드 결함 후보(중간) | E 유지(중간) (E1) | E(중간) | 아니오 | PDF p.25·34; lisflood.cpp:482–486; input.cpp:411–418,831,2032–2046 | 덮어쓰기 주석과 전체 하도망을 순회하는 다른 경로가 모순된다. 실제 대입은 있지만 첫 망의 구간 수까지만 돈다. 내부 루프는 명령 줄 인덱스 i도 재사용한다. | 현재 -nch는 첫 하도망의 구간 수까지만 조도를 덮어쓰는 결함 후보이다. 내부 루프는 명령 줄 순회 인덱스 i도 재사용한다. 강도는 중간이다. |
| LI2-124 | E 코드 결함 후보(중간) | E 유지(약함) (E1) | A | 예 | PDF p.16·34; pars.cpp:176–179; lisflood.cpp:506; input.cpp:929–934; boundary.cpp:289; VersionHistory.h:489–491 | E1의 약함을 채택하지 않는다. 현재 nfp는 fpfric의 별칭이다. 분포 격자를 우선하는 코드와 p.16 설명이 현재 설계를 지지한다. p.34의 명령 줄 덮어쓰기 기능이 과거에도 틀렸다는 증거는 없다. E1의 p.15 인용 위치는 p.16이다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 -nfp는 균일 FPn만 바꾼다. 유효한 분포 Manning 값은 그대로 우선한다. 분포 격자의 NoData에는 FPn을 사용한다. |
| LI2-127 | C 문서 누락 | - | A | 예 | PDF p.34–35; pars.cpp:93–103,563–567,1027–1036 | 문서는 명령 줄 숫자 인수를 금지하고 par의 간격 유지를 명시한다. 현재 공통 파서는 그와 다르다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 -checkpoint는 숫자 인수를 받는다. 숫자가 없으면 기존 간격도 1시간으로 재설정한다. |
| LI2-135 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.19·34; pars.cpp:642–647; lisflood.cpp:171 | 같은 문서 p.19의 cfl value와 p.34의 재설정 설명에 수치 인수가 필요하다. | -cfl value로 입력한다. 0.7은 공통 초기값이다. |
| LI2-136 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.20·34; pars.cpp:651–656; lisflood.cpp:187 | 같은 문서 p.20은 theta value로 적는다. p.34의 인수 생략을 교정한다. | -theta value로 입력한다. 기본값은 1이다. |
| LI2-137 | C 문서 누락 | - | C | 아니오 | PDF p.34; lisflood.cpp:127–128; iterateq.cpp:425–436 | 엄격한 부등식과 연속 10회 조건이 문서에 없다. 보고서 §5의 `fabs(diff)`는 원문 변수명이 아니다. | 일반 CPU는 기본 1800초 간격으로 검사한다. `if (fabs(Parptr->steadyQdiff)<Parptr->steadyQtol)`을 열 번 연속 만족하면 `if (steadyCount == 10) break;`로 종료한다. |
| LI2-138 | C 문서 누락 | - | C | 아니오 | PDF p.34; pars.cpp:259–266 | 허용오차 대입과 정상상태 검사 활성화가 서로 다른 분기이다. | steadytol은 숫자만 설정한다. 정상상태 검사는 steady로 켠다. |
| LI2-139 | C 문서 누락 | - | A | 예 | PDF p.34; pars.cpp:582–588,642–647,1027–1036; VersionHistory.h:34 | 문서의 순서 무관 설명과 현재 순차 파서의 동작이 다르다. FV1 선택의 CFL 재설정은 문서보다 뒤의 해법 추가와 연결된다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 옵션은 왼쪽부터 적용한다. 같은 값을 바꾸는 옵션과 해법·CFL 조합은 순서에 영향을 받는다. |
| LI2-141 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.34–35; iterateq.cpp:329–336 | 문서의 예제 비율 94.94와 뒤 설명의 100이 다르다. 개략값이라는 단서를 붙이지 않은 수치 설명을 교정한다. | 예제 비율은 94.94이다. 100을 쓸 때는 개략값임을 밝힌다. |
| LI2-144 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.35; iterateq.cpp:238 | 성능과 코어 수에 따른 결과 불변성은 실행 실험 주장이다. | 코어 수의 성능·결과 불변성 주장은 별도 실행 검증이 필요하다. 이번에는 실행하지 않았다. |
| LI2-146 | C 문서 누락 | - | A | 예 | PDF p.15·18·35; lisflood.cpp:332,379–380 | p.15는 dirroot의 대상에서 .chkpnt를 명시적으로 제외한다. 과거 디렉터리 계약과 현재 경로 조립의 차이이다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 dirroot가 있으면 기본 체크포인트도 결과 디렉터리에 둔다. |
| LI2-148 | C 문서 누락 | - | C | 아니오 | PDF p.35; lisflood.cpp:123; iterateq.cpp:212,309–320; chkpnt.cpp:223 | 계산시간 간격을 검사하는 실제 호출 위치와 최초 nextcheck 조건이 문서에 없다. | 일반 CPU는 mass 출력 시점에 계산 경과시간을 검사한다. 첫 검사도 저장을 일으킬 수 있다. |
| LI2-151 | B 문서 오기 | A 판 차이 (AD1) | B | 아니오 | PDF p.36; VersionHistory.h:295–298; chkpnt.cpp:93–109,122–133 | AD1의 A를 채택하지 않는다. 4.1.1 이력은 문서 머리글 5.9.6보다 앞서 버전 불일치 파일을 무시한다고 명시한다. | 형식 버전 불일치는 처음부터 시작한다. 모델 버전 불일치는 경고 후 읽는다. 치수 불일치의 종료와 구분한다. |
| LI2-152 | E 코드 결함 후보(중간) | E 유지(중간) (E1) | E(중간) | 아니오 | PDF p.36; VersionHistory.h:19; chkpnt.cpp:143,219,254,283–285; iterateq.cpp:201,217–233 | 구형 파일 호환 조건은 반대 근거이다. 그러나 현재 writer도 checkv=0으로 저장을 생략한다. totalHtm 적산과 누적 손실을 이용하는 재시작 후 계산에 저장값이 이어지지 않는다. | 현재 공통 checkpoint 형식 0은 `if(checkv>1)`의 totalHtm을 저장하지 않는다. `if(checkv>2)`의 누적 침투·증발도 저장하지 않는다. 재시작 통계의 연속성 결함 후보이다. 강도는 중간이다. |
| LI2-157 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.36; lisflood.cpp:603; iterateq.cpp:261 | 같은 문서의 Column 1–12와 실제 출력 인수를 각각 세면 12개이다. | 고전 CPU mass는 12열이다. |
| LI2-159 | C 문서 누락 | - | A | 예 | PDF p.1–2·36; iterateq.cpp:261; swe/output.cpp:14–17 | 문서는 초기 시간 간격을 출력한다고 명시한다. 현재값을 출력하는 코드와 다르다. 과거 writer가 같은 값을 썼다는 근거는 없다. | 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. 현재 Tstep 열은 현재 시간 간격이다. InitTstep의 고정 복사본이 아니다. |
| LI2-161 | C 문서 누락 | - | C | 아니오 | PDF p.36; iterateq.cpp:235–257 | 문서는 침수 면적의 단위만 적는다. 수심 문턱과 공극률·SGC 적용 조건이 없다. | 일반 경로의 침수 면적은 `if (Arrptr->H[ptr] > C(0.01)) FloodArea += dA;`로 계산한다. 공극률 경로는 `dA*Arrptr->paerial[ptr]`를 더한다. SGC 경로는 `if (Arrptr->H[ptr] - Arrptr->SGCbfH[ptr] > Solverptr->DepthThresh)`를 검사한다. |
| LI2-163 | C 문서 누락 | - | C | 아니오 | PDF p.36; iterateq.cpp:261; swe/stats.cpp:48–62,77–116 | 외곽 경계와 점 유량을 더하는 경로를 확인했다. 문서의 downstream exit 설명에는 그 집계 범위가 없다. | Qout는 하도 말단만의 유량으로 일반화하지 않는다. 외곽·점 유출도 집계한다. |
| LI2-164 | C 문서 누락 | - | C | 아니오 | PDF p.36; lisflood.cpp:177; ch_flow.cpp:462–468; cuda/stats.cpp:70 | 1D 말단 갱신과 하도 없는 경로의 차이가 빠졌다. | Hds는 1D 하도 말단 수심이다. 공통 CUDA writer는 0을 쓴다. |
| LI2-166 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.31–32·36; iterateq.cpp:217,261; infevap.cpp:79,120; VersionHistory.h:122 | p.31은 증발을 sink term과 loss로 정의한다. 양의 증발 손실을 더하는 p.36 표기는 그 정의와 모순된다. 현재 writer의 단위는 누적 m³이다. 5.9.9 이력만으로 과거 10³m³ 출력 단위까지 오기였다고 단정하지 않는다. | 마지막 열은 강우에서 침투와 증발을 뺀 누적 m³이다. |

### 2.3 LI2-167–308

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| LI2-167 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.36; VersionHistory.h:34; v8.0:swe/output.cpp:11–26; v8.0:cuda/stats.cpp:40–52; swe/output.cpp:11–26; cuda/stats.cpp:61–74 | v8.0의 FV1·DG2 추가 이후 별도 writer가 지수 표기와 비어 있는 열을 사용한다. | v8.0과 현재 SWE writer는 12열에 지수 표기를 사용한다. 공통 CUDA writer의 기상 누적 열은 0이다. |
| LI2-170 | C 문서 누락 | - | C | 아니오 | PDF p.36; iterateq.cpp:354–366 | 문서는 지정 시각의 격자를 설명한다. 코드는 >= 도달 조건을 사용한다. | overpass는 목표 시각 이상이 된 첫 계산 상태를 기록한다. 해당 조건만으로 정확한 시각 정렬을 보장하지 않는다. |
| LI2-171 | C 문서 누락 | - | C | 아니오 | PDF p.20·36; iterateq.cpp:364–366; output.cpp:148–164 | elevoff 자체는 p.20에도 있다. 수심 임계값 이하를 NoData로 쓰는 세부 조건은 빠져 있다. | elevoff는 overpass 표고도 억제한다. 얕은 셀은 NoData 표고로 쓴다. |
| LI2-178 | C 문서 누락 | - | C | 아니오 | PDF p.36–37; output.cpp:335–351 | 본문은 자료 열을 설명한다. 구간 제목과 debug 추가 열을 모두 설명하지 않는다. | 일반 자료는 11열이다. 구간 제목·열 이름 행과 debug의 추가 두 열을 구분한다. |
| LI2-185 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.37; iterateq.cpp:189–201 | 계산 효율과 정확도에 관한 주장이다. | 최대값 표본 감소는 확인했다. 실제 속도 향상과 오차 크기는 확인하지 않았다. |
| LI2-186 | B 문서 오기 | A 판 차이 (AD1) | B | 아니오 | PDF p.20·37; lisflood2/lis2_output.cpp:478–506 | AD1의 A를 채택하지 않는다. 같은 PDF p.20이 maxdepthonly를 설명하므로 옵션이 없다는 단정은 문서 내부 모순이다. | SGC maxdepthonly는 max를 유지하고 mxe를 억제한다. |
| LI2-189 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.37; iterateq.cpp:196–206 | 같은 절의 최초 시각과 지속시간 정의가 maximum values라는 통칭과 모순된다. | 최초 시각·최대 수심 시각·지속시간을 구분한다. |
| LI2-190 | E 코드 결함 후보(중간) | E 유지(중간) (E1) | E(약함) | 예 | PDF p.21·37–38; iterateq.cpp:189–201; lisflood2/sgm_fast.cpp:3192,3225–3227,3928–3946 | E1과 보고서의 중간을 낮춘다. 문서는 효율을 위한 massint 표본화를 의도적으로 선택한다. 남는 모순은 지속시간 정의와 기본 매 단계 적산에 비해 표본 간격 보정이 없다는 점이다. | mint_hk가 켜지면 `if (Solverptr->t >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)`의 표본 단계에서만 `Arrptr->totalHtm[ptr] += Solverptr->Tstep / C(3600.0);`를 수행한다. 문서는 의도된 표본화를 설명한다. 표본 간격을 가중하지 않는 지속시간 계산의 결함 후보 강도는 약함이다. |
| LI2-191 | B 문서 오기 | A 판 차이 (AD1) | B | 아니오 | PDF p.20·37–38; lisflood2/lis2_output.cpp:478–510 | AD1의 A를 채택하지 않는다. 같은 PDF의 maxdepthonly 설명이 억제 옵션 부재 주장과 모순된다. | SGC maxdepthonly는 inittm·maxtm·totaltm도 억제한다. |
| LI2-195 | B 문서 오기 | A 판 차이 (AD1) | B | 아니오 | PDF p.21·38; pars.cpp:799–802; output.cpp:852,974–975 | AD1의 A를 채택하지 않는다. 같은 PDF p.21이 별도 SGCvoutput을 명시한다. | SGCVx·SGCVy에는 SGCvoutput을 지정한다. |
| LI2-196 | B 문서 오기 | A 판 차이 (AD1) | 일치 | 예 | PDF p.38; output.cpp:829–832,852,974–975 | 보고서의 B와 AD1의 A를 채택하지 않는다. 세 파일은 Qcx·Qcy·Fwidth를 가리킨다. 뒤의 SGCVx·SGCVy는 별도의 속도 설명 절이다. 옵션 오기는 LI2-195에서 판정한다. | 문서의 추가 세 파일은 Qcx·Qcy·Fwidth이다. SGCVx·SGCVy는 별도로 설명한 속도 파일이다. |
| LI2-198 | C 문서 누락 | - | C | 아니오 | PDF p.38; fp_flow.cpp:227–228; output.cpp:432–433 | 문서는 방향별 최대값을 적는다. 절댓값과 출력 면 격자의 연결을 명시하지 않는다. | maxVx·maxVy는 절댓값의 최대이다. 각각 셀 경계 격자로 출력한다. |
| LI2-200 | B 문서 오기 | A 판 차이 (AD1) | B | 아니오 | PDF p.38 식 (3); VersionHistory.h:210; util.cpp:214–217 | AD1의 A를 채택하지 않는다. 절댓값 최대 속도 변경은 5.0.2로 문서 머리글 5.9.6보다 앞선다. | 코드의 셀 속도는 양쪽 면속도 절댓값의 최댓값을 조합한다. 인쇄 식에는 절댓값 기호가 없다. |
| LI2-203 | X 외부 원문 필요 | B (외부 원문 판정) | H | 예 | PDF p.38·43; util.cpp:214–218; DEFRA 2003 FD2317 PDF p.39(인쇄 p.31), 표 5.2; DEFRA 2006 FD2321/TR1 PDF p.16·20(인쇄 p.6·10), §3.2·3.5 | 외부 원문 판정의 B를 채택하지 않는다. 2006 §3.2도 2003의 1.5 식을 재인용한다. 코드 주석은 2006 최종식이라고 특정하지 않는다. 문서와 코드의 수치는 같다. 남는 출처 연도와 debris factor 비교는 외부 문헌 사이 비교이다. | 문서 식 (4)와 코드의 `Haz = Arrptr->H[p0] * (Vc + C(1.5));`는 일치한다. 이는 2003 식에서 debris factor를 더하지 않은 형태이다. 2006 §3.2에도 이 이전 식이 실려 있다. 2006 §3.5의 최종식은 `HR = d x (v + 0.5) + DF`이다. 출처 비교는 H로 분리한다. |
| LI2-204 | B 문서 오기 | B 문서 오기 (AD1) | B | 아니오 | PDF p.38의 본문 및 §5.2.8 제목 | 같은 쪽에 실제 절 번호가 있으므로 참조 번호 오기를 확정한다. | 셀 속도 정의의 절 번호는 5.2.8이다. |
| LI2-205 | C 문서 누락 | - | A | 예 | PDF p.38; iterateq.cpp:158–165,189–190; lisflood2/sgm_fast.cpp:3836–3854,3928–3946 | 문서는 mint_hk가 위험도 최대값도 massint에서 표본화한다고 명시한다. 단순 누락이 아니다. 당시 구현이 틀렸다는 근거는 없다. | 일반 CPU의 hazard 갱신은 mint_hk 밖에서 매 단계 수행한다. 빠른 SGC도 같은 순서이다. 8.0 이전 판(머리글 5.9.6, 표지 6.1.1) 기준, 그 판 코드는 배포본이 없다. |
| LI2-207 | C 문서 누락 | - | C | 아니오 | PDF p.38–39; fp_flow.cpp:208–215; output.cpp:979–981 | 본문은 flow limiter 값을 설명한다. 제한 분기에서 기록되는 부호 있는 유량이라는 배열 의미를 추가한다. | QL은 적응 시간 간격 배열이 아니다. 제한 분기에서 기록한 부호 있는 유량이다. |
| LI2-210 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.39; VersionHistory.h:109; v8.0:lisflood.cpp:724–730; lisflood.cpp:756–768 | 5.9.23의 기본 DEM 출력 변경을 v8.0과 현재 호출 조건에서 확인했다. | 표시 DEM은 5.9.23부터 기본 출력이다. v8.0과 현재 호출은 debug 조건 밖에 있다. 현재 maxdepthonly는 이 출력을 억제한다. |
| LI2-211 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.20·39; VersionHistory.h:109; v8.0:lisflood.cpp:727–730; lisflood.cpp:765–768 | 5.9.23 이력과 v8.0이 하상을 포함한 표시 DEM을 뒷받침한다. | 5.9.23 변경과 v8.0 배포본에서 확인한 SGC 결과 dem은 시각화용 하상고이다. 현재 출력도 SGCz를 사용한다. |
| LI2-216 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.39 | 시각화의 활용 목적이다. | 시각화의 활용 목적을 문서 설명으로 유지한다. |
| LI2-217 | B 문서 오기 | A 판 차이 (AD1) | B | 아니오 | PDF p.21·32·36·39; output.cpp:560–565; VersionHistory.h:197,207 | AD1의 A를 채택하지 않는다. 같은 PDF에 바이너리 입력·출력과 체크포인트가 있으므로 전체를 텍스트라고 한 문장은 내부 모순이다. | ASCII 격자·표와 binary 시작 파일·체크포인트를 구분한다. |
| LI2-218 | H 코드 대조 대상 아님 | - | H | 아니오 | PDF p.39 | FloodView 메뉴와 사용 절차는 모델 코드 대조 대상이 아니다. | p.39의 메뉴·다중 wd 선택 절차는 외부 도구 사용법이다. 뷰어 내부 분석을 모델 완료 조건으로 삼지 않는다. |
| LI2-301 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.26–27; VersionHistory.h:107; v8.0:input.cpp:1891–1893; input.cpp:1920–1922 | 5.9.25 이력과 v8.0 배포본의 분 단위 환산이 일치한다. | 분 단위는 5.9.25에 추가되었다. v8.0과 현재 코드는 minutes와 단수 minute를 모두 지원한다. days를 부정하는 문서 오기와 구분한다. |
| LI2-302 | C 문서 누락 | - | C | 아니오 | PDF p.26–27·31–32; input.cpp:1889–1931 | 문서의 값·시각 표에 없는 로더 검사를 확인했다. | 시각은 엄격히 증가해야 한다. 자료 부족은 중단한다. 알 수 없는 시간 단위는 경고 후 초로 취급한다. |
| LI2-303 | C 문서 누락 | - | C | 아니오 | PDF p.26–27; boundary.cpp:1432–1444 | 선형 보간 설명과 별개인 양 끝 구간의 상수 유지 조건이다. | 첫 시각 전은 첫 값이다. 마지막 시각 이후는 마지막 값이다. |
| LI2-304 | C 문서 누락 | - | C | 아니오 | PDF p.24–26; input.cpp:1584–1642 | 외곽 위치 문자는 대소문자를 구분한다. 종류 토큰은 STRCMPi로 비교한다. | 외곽 위치 문자는 대문자로 쓴다. 외곽 구간은 정렬하고 영역에 자른다. |
| LI2-305 | C 문서 누락 | - | C | 아니오 | PDF p.25; input.cpp:1645–1651,1745–1765 | 해당 점 경계 분기에는 x 상한과 y 범위 검사가 없다. stage 검사와 동일하다고 볼 수 없다. | 점 경계의 영역 검사는 stage의 검사와 다르다. 이 분기는 x 상한과 y 범위를 검사하지 않는다. |
| LI2-306 | C 문서 누락 | - | C | 아니오 | PDF p.22–24; input.cpp:511–516; ch_flow.cpp:675–686 | RATE 관계곡선 처리와 안정성 주석이 입력 표에서 빠져 있다. | 하도 로더는 RATE 관계곡선도 읽는다. 불안정성에 관한 입력 주석을 함께 적는다. |
| LI2-307 | C 문서 누락 | - | C | 아니오 | PDF p.27; input.cpp:1045–1081 | 문서의 방식 이름 외에 배열 순서와 높이층 입력을 확인했다. | PFIX는 면적 배열을 읽는다. PVAR는 높이 설정 뒤 층별 높이와 면적 배열을 읽는다. |
| LI2-308 | C 문서 누락 | - | C | 아니오 | PDF p.27; input.cpp:1083–1146 | 면적 배열과 방향별 경계 배열의 읽기 순서를 확인했다. | PBOUND는 면적 배열과 네 방향 경계 배열을 읽는다. PBVAR는 높이층별 경계 자료를 추가한다. |

### 2.4 LI2-309–338

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| LI2-309 | C 문서 누락 | - | C | 아니오 | PDF p.16·22·32; input.cpp:930–936,1168,1514–1517 | 입력 종류별 NoData의 대체값을 확인했다. | 조도 NoData는 균일 n으로 바꾼다. 시작 수심 NoData는 0으로 바꾼다. DEM NoData는 내부 표고로 바꾼다. |
| LI2-310 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.28; VersionHistory.h:85; v8.0:VersionHistory.h:77; v8.0:sgc.cpp:442–446; sgc.cpp:442–446 | 6.3.5의 하상 보정 기록과 v8.0의 구현이 문서의 단순 차감식 이후 변경을 보여 준다. | 6.3.5의 하상 보정은 v8.0과 현재 코드에 있다. 지정·계산 하상은 `getmin(zf, Arrptr->DEM[p0] - C(0.01))` 등의 분기로 DEM−0.01m 이하가 된다. |
| LI2-311 | C 문서 누락 | - | C | 아니오 | PDF p.28–29; input.cpp:2398–2409; sgc.cpp:442–446 | a는 선택 입력이다. 양수 a 분기는 명시 하상·깊이·면적 모드 뒤에 있다. | 명시 하상·깊이·면적 모드가 선택되지 않고 a가 양수이면 `z0 - r*pow(a, p)`를 사용한다. s 범위 경고는 verbose 조건을 가진다. |
| LI2-312 | C 문서 누락 | - | C | 아니오 | PDF p.28; config.default.cmake:3; lisflood2/sgm_fast.cpp:139–156 | 모델의 단면 계산을 바꾸는 컴파일 조건이다. 외부 빌드 도구 내부가 아니다. | 기본 빠른 SGC 빌드는 비직사각형 수리반경 분기를 제외한다. 입력 Type만으로 실행 단면식을 판정하지 않는다. |
| LI2-313 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | pars.cpp:787–797; lisflood.cpp:253–254; lisflood.h:638–639; sgc.cpp:442–444 | 면적이라는 주석·메시지와 폭으로 나누는 별도 계산 경로가 깊이 플래그 대입과 모순된다. 명시 하상 경로는 영향을 피하지만 대입의 의도를 설명하지 않는다. | SGCA_mode 입력이 면적 플래그 대신 깊이 플래그를 켜는 결함 후보이다. 명시 하상이 먼저 선택되지 않으면 p를 깊이로 사용한다. 강도는 강함이다. |
| LI2-314 | C 문서 누락 | - | C | 아니오 | PDF p.29–30; input.cpp:153–171; weir_flow.cpp:312–319 | 입력 부족·영역 검사와 일부 검사의 부재를 확인했다. Tz=1의 분모 0은 전이 분기에 도달하는 조건에 한정된다. | 부족 행과 영역 밖 기준 셀은 중단한다. 모든 수치 필드와 Tz>1을 검증하지 않는다. |
| LI2-315 | C 문서 누락 | - | C | 아니오 | PDF p.30–31·33; input.cpp:72–82,2332–2335; lisflood.cpp:565–574 | 세 입력의 범위 밖·자료 부족 처리가 서로 다르다. | stage는 영역 밖 점을 비활성화한다. gauge는 좌표를 경계로 옮긴다. opts는 실제 읽은 개수로 줄인다. |
| LI2-316 | C 문서 누락 | - | C | 아니오 | PDF p.32; input.cpp:1169–1187 | startelev와 SGC 조건 안에서 수심·단면 체적을 함께 초기화한다. | 수위 시작 파일을 SGC 수심으로 바꿀 때 단면 체적도 초기화한다. |
| LI2-317 | C 문서 누락 | - | C | 아니오 | PDF p.18·32; pars.cpp:153–154; cuda/io.cpp:63–75; cuda/cuda_simulate.cu:35–41,83–94 | CUDA 시작 로더의 치수 검사와 추가 파일 조건을 기록한다. 바이너리 시작 플래그는 이 분기를 켜지 않는다. | CUDA 시작 격자는 치수를 검사한다. startq2d는 별도 Qx·Qy 파일을 읽는다. 공통 CUDA 시작 로더는 startfile만 검사한다. binarystartfile만 켠 입력은 이 분기를 타지 않는다. |
| LI2-318 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.32; VersionHistory.h:34; v8.0:swe/dg2.cpp:27–35; swe/dg2.cpp:27–35,107–109; swe/dg2/dg2_output.cpp:13–24 | v8.0에 추가한 DG2의 파일 집합을 확인했다. | v8.0에 추가한 DG2는 수심 평균 격자 외에 x·y 기울기 파일을 읽고 쓴다. |
| LI2-319 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.32; VersionHistory.h:39; v8.0:rain/rain.tpp:65–73; rain/rain.tpp:20,65–73 | 6.1 분포 강우 추가와 v8.0 배포본의 단위 변환을 확인했다. | 6.1에 추가한 분포 강우는 v8.0과 현재 코드에서 rainfall_depth의 구간 누적 mm를 강우율 m/s로 바꾼다. ASCII rain의 mm/hour 표와 구분한다. |
| LI2-320 | C 문서 누락 | - | C | 아니오 | PDF p.16·19; infevap.cpp:371; pars.cpp:527–530,880–882,1053–1056 | 높은 경사와 routing_mass_check는 앞쪽 표에 이미 있다. 누락은 dist_routing과 verbose에 종속된 자동 비활성화 조건으로 한정한다. | 높은 경사 조건과 routing_mass_check는 문서에 있다. dist_routing은 별도 선택이다. 자동 비활성화 조건은 `if (Statesptr->routing == ON && Statesptr->acceleration == OFF && Statesptr->SGC == OFF && verbose == ON)`이다. |
| LI2-321 | C 문서 누락 | - | C | 아니오 | PDF p.21; pars.cpp:379–400,990–993; lisflood.cpp:149; lisflood2/file_tool.cpp:728–748 | binary_out과 netcdf_out은 문서에 있다. 표준 확장자·ascii_out·정밀도 선택의 누락으로 한정한다. | standard_extensions_out은 표준 확장자를 선택한다. ascii_out·binary_out·netcdf_out은 별도 형식 플래그이다. output_precision은 소수 자릿수를 정한다. 현재 기본값은 3이다. |
| LI2-322 | C 문서 누락 | - | C | 아니오 | PDF p.21·38; pars.cpp:338–352; swe/output.cpp:68–94 | 일반 voutput과 별도의 최대·관측점 선택을 구분했다. | 최대 유속과 관측점 속도를 따로 요청할 수 있다. velocity와 discharge 파일을 구분한다. |
| LI2-323 | C 문서 누락 | - | C | 아니오 | PDF p.20; pars.cpp:575–579,934–945; iterateq.cpp:177–185 | resettimeinit 자체는 문서에 있다. saveint_max·maxint와 실제 초기화 조건의 누락으로 한정한다. | 최대값을 저장하고 재설정하는 saveint_max·maxint를 별도로 설정할 수 있다. resettimeinit 자체는 문서에 있다. 실제 초기화 조건은 `if ((Statesptr->reset_timeinit == ON) & (Solverptr->t>Parptr->reset_timeinit_time))`이다. |
| LI2-324 | C 문서 누락 | - | C | 아니오 | PDF p.18; pars.cpp:182–195,855–859; lisflood.cpp:126 | startq·ch_start_h·tstart는 앞쪽 표에 있다. startq2d와 출력 시각 재설정이 누락된 부분이다. | startq·ch_start_h·tstart는 문서에 있다. startq2d는 별도 초기 유량 입력이다. tstart는 SaveTotal·MassTotal·maxintTotal도 시작 시각으로 설정한다. |
| LI2-325 | C 문서 누락 | - | C | 아니오 | PDF p.16–21; pars.cpp:232–245,492–496,513–516,948–960 | 일반 manningfile과 구분되는 추가 파일명을 parser 원문에서 확인했다. | Qfile·SGCmanningfile·SGCdirnfile·infilfile·rainfallmask·chanmask·linklist는 별도 입력 파일명을 받는다. |
| LI2-326 | C 문서 누락 | - | C | 아니오 | PDF p.17·28; pars.cpp:745–795,805–813,835–839,874–878; sgc.cpp:443 | 전역 SGCn·SGCr·SGCp·SGCchan·SGCs는 문서에 있다. 나머지 선택과 모드 조건으로 누락 범위를 좁힌다. | 기본 전역 수리기하 매개변수는 문서 p.17에 있다. 추가 선택에는 SGCa·SGC2·SGC_enable·SGCcat_area·SGCd8 등이 있다. SGCbfh_mode는 p를 만제 수심으로 사용한다. |
| LI2-327 | C 문서 누락 | - | C | 아니오 | PDF p.16·19–20; pars.cpp:210–219,410–428,663–683,728–739,863–869 | 보고서 본문은 p.22–39 밖을 검사하지 않았다고 한정한다. 앞쪽 표에 qlimfact·ts_multiple·Roe·1Dfriction·depththresh·momentumthresh·drycheckoff·gravity가 있다. 누락은 별도 Roe_slow 선택에 한정한다. | 열거한 일반 해법·임계값 옵션은 문서 p.16·19–20에 있다. 별도 Roe_slow 키워드는 ghost cell 방식의 Roe 해법을 선택한다. |
| LI2-328 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.19; VersionHistory.h:34; v8.2:pars.cpp:582–635; pars.cpp:582–637 | v8.0의 해법 추가 이후 v8.2에서 해법별 CFL 재설정이 확인된다. | v8.2와 현재 코드의 해법 선택은 CFL을 재설정한다. FV1·HWFV1은 0.5이다. FV2·DG2는 0.33이다. MWDG2는 0.3이다. acc_nugrid는 0.7이다. |
| LI2-329 | C 문서 누락 | - | C | 아니오 | PDF p.16–21; pars.cpp:687–722,973–986 | 전용 해법 검사와 순서 의존성이 고전 옵션 표에 없다. | limitslopes는 `if (Statesptr->dg2 == OFF && Statesptr->mwdg2 == OFF && Statesptr->fv2 == OFF)`이면 중단한다. 해법을 켜기 전에 이 옵션을 읽으면 검사 시점의 상태가 적용된다. |
| LI2-330 | C 문서 누락 | - | C | 아니오 | PDF p.16–21; pars.cpp:294–298,438–474,907–930,1006–1015 | 추가 모델 입력·진단 parser를 확인했다. 외부 VTK 내부로 범위를 넓히지 않는다. | NoData 배수·내부 진단·추가 저장 옵션은 별도 parser 분기로 기록한다. |
| LI2-331 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.38; VersionHistory.h:34; swe/output.cpp:132–141,178–190; swe/stats.cpp:131–140 | v8.0에 추가한 SWE의 셀 중심 단위 폭 유량은 고전 면 체적 유량과 다르다. | v8.0에 추가한 CPU FV1·DG2의 Qx·Qy는 셀 중심 단위 폭 유량이다. 셀 경계 체적 유량과 구분한다. |
| LI2-332 | C 문서 누락 | - | A | 예 | PDF p.20–21·36–38; VersionHistory.h:34; v8.0:swe/fv1.cpp:66,76–79,99; swe/fv1.cpp:39–99; swe/dg2.cpp:57–119; swe/output.cpp:148–165 | 문서의 all models 출력 설명을 이후 추가한 SWE에도 적용하면 달라진다. v8.0의 별도 반복문과 writer로 판 차이를 특정한다. | v8.0에 추가한 CPU FV1·DG2는 최대 수심과 관측점 출력을 처리한다. 두 반복문은 고전 IterateQ의 overpass·profile·hazard·중간 checkpoint·gauge 출력 블록을 호출하지 않는다. |
| LI2-333 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.38; v8.1:cuda/fv2/cuda_fv2_snapshot.cu:30–48; cuda/fv1/cuda_fv1_snapshot.cu:30–48; cuda/fv2/cuda_fv2_snapshot.cu:30–48; cuda/dg2/cuda_dg2_snapshot.cu:36–60; cuda/io.templates.cpp:15–28 | v8.1과 현재 CUDA SWE의 별도 출력 위치·형식을 확인했다. | v8.1과 현재 CUDA SWE snapshot은 DEM과 같은 크기의 셀 중심 ASCII 격자이다. |
| LI2-334 | C 문서 누락 | - | A | 예 | PDF p.38; v8.1:cuda/acc/cuda_acc_snapshot.cu:41–42; v8.1:cuda/acc/cuda_acc_solver.cu:605–606; cuda/acc/cuda_acc_snapshot.cu:41–48; cuda/acc/cuda_acc_solver.cu:605–606 | 문서가 유량을 m³/s로 명시한다. v8.1부터 확인한 CUDA ACC의 m²/s와 다르므로 단순 누락이 아니다. | v8.1과 현재 CUDA ACC snapshot의 Qx·Qy는 셀 경계 단위 폭 유량이다. 고전 CPU의 체적 유량과 단위를 구분한다. |
| LI2-335 | C 문서 누락 | - | A | 예 | PDF p.20–21; v8.0:cuda/fv1/cuda_fv1_snapshot.cu:30–41; cuda/fv1/cuda_fv1_snapshot.cu:30–48; cuda/acc/cuda_acc_snapshot.cu:30–48; cuda/io.templates.cpp:15–28; cuda/fv1/cuda_fv1_simulate.cu:140–199 | 문서는 depthoff와 binary_out을 설명한다. v8.0부터 확인한 별도 CUDA writer가 그 계약을 따르지 않는 판 차이이다. | v8.0부터 확인한 CUDA snapshot은 ASCII wd를 쓴다. 현재 CUDA snapshot 경로에는 depthoff·binary_out·overpass의 일반 CPU 출력 처리가 없다. |
| LI2-336 | C 문서 누락 | - | C | 아니오 | PDF p.37; cuda/fv1/cuda_fv1_simulate.cu:197–199; cuda/fv2/cuda_fv2_simulate.cu:183–184; cuda/dg2/cuda_dg2_simulate.cu:197–198; cuda/cuda_max_field.cu:117–130 | 정의된 시간 통계 writer와 실제 종료 호출을 구분한 추가 설명이다. | CUDA SWE 종료 경로는 MaxField의 max를 쓴다. 정의만 있는 다른 최대 writer와 구분한다. |
| LI2-337 | C 문서 누락 | - | C | 아니오 | PDF p.35–38; cuda/acc/cuda_acc_simulate.cu:290–293,329–343; cuda/acc/cuda_acc_snapshot.cu:52–57; cuda/cuda_simulate.cu:388–406 | 전용 checkpoint 배열 계약과 주석 처리된 mxe 호출을 확인했다. | ACC 전용 checkpoint는 CPU와 같은 배열 계약으로 보장하지 않는다. 종료 시 시간 격자 네 종류를 쓰며 mxe 호출은 주석이다. |
| LI2-338 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.32; input.cpp:1920–1931; rain/Rainfall_uniform.h:60–91; cuda/fv1/cuda_fv1_simulate.cu:149–152 | days는 CPU의 하루 환산과 모순된다. 중간 구간의 t_1만 초로 바꾸는 식은 내부 단위와도 모순된다. seconds와 마지막 구간의 보간 생략은 반대 조건으로 확인했다. | 이 균일 강우 헤더를 호출하는 CUDA 해법은 days를 하루로 환산하지 못한다. `time_now > t_2*time_multiplier`인 전환에서 `t_1 = t_2*time_multiplier;`를 수행한다. 보간식은 `value = value_1 + (value_2 - value_1) / ((t_2 - t_1) * time_multiplier) * (time_now - t_1 * time_multiplier);`이다. 승수가 1이 아닌 중간 구간의 단위가 모순된다. 강도는 강함이다. |

### 2.5 LI2-339–354

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| LI2-339 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.35–37; v8.1:cuda/acc_nugrid/write_mass_data.cu:58–63; cuda/acc_nugrid/write_mass_data.cu:58–63; cuda/acc_nugrid/write_max_maps.cu:47–72; cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:335,709 | v8.1의 비균일 ACC에 별도 출력·재시작 경로가 있다. | v8.1과 현재 비균일 ACC는 자체 mass·최대 격자·체크포인트 writer를 사용한다. |
| LI2-340 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | PDF p.36–38; v8.2:cuda/adaptive/output/write_cumulative_data.cpp:18–28; cuda/adaptive/input/read_plot_params.cpp:10–17; cuda/adaptive/output/write_raster_file.cu:17; cuda/adaptive/output/write_cumulative_data.cpp:18–28 | v8.2의 적응 해법은 고전 writer와 다른 parser·파일명·CSV 형식을 사용한다. | v8.2와 현재 HWFV1·MWDG2는 자체 parser와 cumu CSV를 사용한다. 격자 번호는 네 자리 0 채움이 아니다. |
| LI2-341 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | v8.3:README.md:3–5,35; VersionHistory.h:31–32; metal/fv1/metal_fv1_simulate.mm:1347–1354,1425–1459,1472–1477 | v8.3의 Metal 추가와 공유 SWE 출력 호출을 확인했다. | Metal FV1은 v8.3 추가이다. 공유 SWE 출력 함수를 호출한다. rainfallmask 또는 routing이 켜져 있으면 중단한다. |
| LI2-342 | A 판 차이 | A 판 차이 (AD1) | A | 아니오 | v8.3:README.md:33·35; v8.3:lisflood-8.2-to-8.3.patch:75–89; pars.cpp:965–968 | 패치는 Hold가 0일 때만 질량수지 더하기를 건너뛴다. 단위 변경이 아니다. | metal은 공통 GPU 선택 상태를 켠다. v8.3의 마른 NoData 변경은 `if (Hold == C(0.0)) continue;`로 0인 질량수지 덧셈을 건너뛴다. |
| LI2-343 | E 코드 결함 후보(중간) | E 유지(중간) (E1) | E(중간) | 아니오 | PDF p.32; input.cpp:18–32,1241–1256; output.cpp:532; CMakeLists.txt:211–214 | 바이너리 읽기·쓰기 모드가 충돌한다. 래퍼는 mode를 그대로 fopen에 넘긴다. 본체에 binary 모드 강제 대입이 없다. POSIX에서는 차이가 없으므로 Windows에 한정한다. | Windows binary 시작 로더의 text 모드는 바이트 변환 결함 후보이다. 강도는 중간이다. |
| LI2-344 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.31; output.cpp:79–94,110–144; input.cpp:1482–1491 | 대체 헤더 주석과 셀 중심 분기는 헤더 하나를 전제한다. 면 출력은 대체 6행과 기본 6행을 모두 쓴다. 6행 입력 경로와도 모순된다. | 일반 flux ASCII에서 ascheader와 outflag 1·2를 함께 쓰면 헤더를 12행으로 만드는 결함 후보이다. 강도는 강함이다. |
| LI2-345 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.32·38; output.cpp:110–144,568–596 | 같은 writer의 선언 치수와 기록 개수가 충돌한다. ASCII 경로는 행별로 padding을 제거한다. binary 파일에 padding을 선언하는 표지는 없다. | 일반 binary flux는 선언한 격자 크기와 자료 길이가 다른 결함 후보이다. x 헤더는 `(xsz+1)*ysz`이다. y 헤더는 `xsz*(ysz+1)`이다. 두 분기는 `(Parptr->xsz+1)*(Parptr->ysz+1)`개를 쓴다. 강도는 강함이다. |
| LI2-346 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.34; input.cpp:251–252,279–291 | -v의 진단 의미와 지반 아래 마루를 보정한다는 주석이 수치 대입의 verbose 종속성과 충돌한다. EWeir_Weir 조건은 보에만 한정할 뿐 verbose 의존성을 제거하지 않는다. | 지반 아래 보 마루에서 -v가 보정 여부까지 바꾸는 결함 후보이다. `Arrptr->Weir_hc[i] = getmax(z0, z1);`는 verbose 조건 안에 있다. 강도는 강함이다. |
| LI2-347 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.27; input.cpp:1114–1147; por_flow.cpp:83–92 | zsz×4 할당과 독립된 층·면 반복이 같은 stride 주소와 모순된다. 소비 경로도 겹친 주소를 사용한다. 층·면 공유를 의도한 설명은 없다. | PBVAR의 높이층과 방향 자료가 같은 주소에 겹치는 결함 후보이다. 두 층 이상에서 m=1·k=0과 m=0·k=1이 같은 위치에 기록된다. 강도는 강함이다. |
| LI2-348 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.35–37; iterateq.cpp:203–205,450–477; lisflood.cpp:803–810; chkpnt.cpp:140,251 | 종료 시 표고로 바꾼다는 주석과 재시작의 수심 갱신 경로가 충돌한다. 중간 checkpoint는 변환 전에 기록하므로 제외한다. 반환 전 복구는 없다. | 고전 CPU의 IterateQ 종료 후 최종 checkpoint가 최대 수면고를 최대 수심 배열로 저장하는 결함 후보이다. 변환 조건은 `if (Arrptr->maxH[ptr]>1e-3) Arrptr->maxH[ptr] += Arrptr->DEM[ptr]; else Arrptr->maxH[ptr] = NULLVAL;`이다. 강도는 강함이다. |
| LI2-349 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.35–36; lisflood.h:59–64; config.default.cmake:1–8; lisflood2/lisflood_processing.cpp:1536–1572,2092–2122; utility.cpp:43–50; lisflood2/sgm_fast.cpp:4601–4611; lisflood.cpp:773–775,810; chkpnt.cpp:248–251 | E1의 포인터 정정을 채택한다. 해제 후 포인터가 NULL이 된다. todo 주석과 공통 writer의 유효 배열 전제가 충돌한다. RESULT_CHECK 정의는 해제를 피하지만 기본값은 미정의이다. | 기본 빠른 SGC는 공통 checkpoint 배열을 해제하고 NULL로 만든다. checkpoint가 켜진 최종 writer는 NULL 배열을 사용하는 결함 후보이다. RESULT_CHECK를 정의한 빌드는 이 해제 조건에서 제외된다. 강도는 강함이다. |
| LI2-350 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.21·38; lisflood2/lis2_output.cpp:137–151,402–446; output.cpp:974–976 | y 버퍼 초기화와 출력 인수가 y 복사의 대상 버퍼와 모순된다. 같은 판의 일반 writer는 x·y·셀 치수를 구분한다. maxdepthonly와 SGC 셀 부재는 출력 자체를 생략하는 조건이다. | 빠른 SGC의 SGCV 출력이 활성화되면 y 자료를 tmp_grid1에 덮어쓴다. SGCVy는 0으로 지운 tmp_grid2를 쓰는 결함 후보이다. SGCVx·SGCVc의 행 수도 한 행 많다. 강도는 강함이다. |
| LI2-351 | E 코드 결함 후보(중간) | E 유지(중간) (E1) | E(중간) | 아니오 | PDF p.32; cuda/io.cpp:98–136; cuda/cuda_simulate.cu:35–41; input.cpp:1168–1187; cuda/fv1/cuda_fv1_solver.cu:220–227 | NoData를 0으로 만드는 같은 경로의 의도와 CPU 수심 하한이 무제한 DEM 차감과 충돌한다. startelev OFF는 차감을 피한다. 확인한 후속 건습 분기는 운동량만 0으로 만든다. | CUDA startelev 초기화에서 NoData가 수심으로 바뀌거나 음의 수심이 생기는 결함 후보이다. NoData를 0으로 바꾼 뒤 `H_value = H_value - DEM_value;`를 수행한다. 강도는 중간이다. |
| LI2-352 | E 코드 결함 후보(강함) | E 유지(강함); 8.2 결함, 8.3에서 고침 (E1) | A | 예 | v8.2:cuda/cuda_max_field.cuh:20–21; v8.2:cuda/fv1/cuda_fv1_simulate.cu:98–99; v8.2:cuda/cuda_max_field.cu:21–26,96–106; v8.2:cuda/cuda_geometry.cu:37–43; v8.3:README.md:32; v8.3:lisflood-8.2-to-8.3.patch:98–133; cuda/cuda_max_field.cu:96–98,124–130 | E1의 v8.2 강함과 v8.3 수정 확인은 맞다. 현재 코드에는 문제의 작은 최대 수심 버퍼 분기가 없다. 최종 분류는 현재 결함이 아닌 v8.2→v8.3 판 차이로 바꾼다. | v8.2 CUDA 최대 수심 버퍼 결함은 v8.3에서 수정되었다. 현재 최대 수심 배열은 ghost를 포함한 device 버퍼이다. 출력 때 전체 크기를 host로 복사한다. |
| LI2-353 | E 코드 결함 후보(강함) | E 유지(강함) (E1) | E(강함) | 아니오 | PDF p.16; pars.cpp:300–322,1041–1087 | 조합 금지 문서·자기 주석과 실제 return 순서가 모순된다. 뒤 CheckParams에도 같은 충돌 검사가 없다. 토큰별 상태 덮어쓰기는 중단을 의도한 주석의 근거가 되지 않는다. | adaptoff·acceleration 충돌 검사는 현재 실행 경로에서 호출되지 않음. 해당 토큰은 pars.cpp:300–305 또는 307–314에서 return한다. 상충 검사 분기는 pars.cpp:318–322이다. 이 도달 불가 검사의 결함 후보 강도는 강함이다. |
| LI2-354 | E 코드 결함 후보(중간) | E 유지(중간) (E1) | E(중간) | 아니오 | PDF p.29; input.cpp:161–163; util.cpp:312–340; lisflood2/lisflood_processing.cpp:1210; lisflood2/sgm_fast.cpp:537–546; weir_flow.cpp:79–88 | 문서의 폭 미터 규칙과 같은 판의 도·미터 배열 구분이 생략 폭 대입과 모순된다. 현재 빠른 SGC도 그 폭을 그대로 받는다. 폭 명시와 미터 격자는 영향을 피한다. | latlong에서 구조물 폭을 생략하면 도 단위 Parptr->dx가 폭으로 들어간다. 현재 빠른 SGC의 보 유량도 이 폭을 사용한다. 강도는 중간이다. |

대상 136행: 유지 118, 변경 18

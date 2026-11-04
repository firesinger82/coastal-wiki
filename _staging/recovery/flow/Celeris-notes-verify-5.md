# Celeris 노트 전수 검증 5

## 대상과 진행

- 대상: `models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md`.
- 시작 시 파일은 341줄이다. 순서대로 114줄·114줄·113줄로 나눈다.
- 이 작업의 범위는 시작 시 115–228줄 114줄이다. 행 식별자를 함께 추적한다.
- 상태: 담당 구간 대조 완료.
- 사용자 제공 기계 확인 불일치 후보: 없음.

## 검증 결과

- 대조한 노트 줄: 115–228줄, 총 114줄이다. 첫 행은 CD1-1089이고 마지막 행은 CD1-1274다.
- 정정: 31줄이다. 문서 원문 칸의 누락 설명에서 백틱을 제거했다. 각 결론 칸 끝에 [11-04 전수 검증 정정]을 붙였다.
- 보완: 0줄이다.
- 분류·결론의 내용 변경: 0줄이다. 114행 모두 최종 배정표와 conclusion-verify의 C 문서 누락 분류 및 결론에 일치한다.
- 원문 인용: 1,009개다. Markdown 코드 구간의 바깥쪽 패딩 공백 한 칸을 제외한 인용 문자열이 해당 원문과 일치한다. 내부 공백은 보존해서 검사했다.
- HTML 인용: 817개다. input의 ID와 value 속성 부재를 확인했다. option의 숫자와 표시명도 확인했다.
- 경로와 줄 참조: 중복을 포함하여 2,119개다. 쉼표로 나열한 줄과 범위도 각각 열었다. 참조하는 원문 줄은 파일과 줄 번호의 중복을 제거하면 781줄이다.
- 상대 링크: 114개다. 노트 디렉터리 기준으로 모두 실제 파일을 가리킨다.
- 담당 구간에는 frontmatter, 일반 본문, Mermaid, A 행, E 행, 이전 커밋 인용, 논문 인용이 없다. 따라서 이 구간에는 논문 쪽 이미지·판 차이·흐름도 대조 항목이 없다.
- 담당 구간에는 개인 절대 경로, 홈 축약 경로, 위키 링크 및 사용자가 제거하도록 지정한 한계 문장이 없다.
- 새 차이 파일에 대한 직접 본문 수정안은 없다. 반영 기록 Celeris-notes-apply-3.md와 보고서의 §4를 대조했다. 담당 행은 CD1g·CD1h의 최종 행별 결론으로 판정했다.
- 미해결 항목: 없음.

## 대조 근거

- [최종 분류 배정표](../assign/Celeris-final-conclusions.tsv).
- [CD1g 최종 결론](../compare/Celeris-conclusion-verify-CD1g.md).
- [CD1h 최종 결론](../compare/Celeris-conclusion-verify-CD1h.md).
- [반영 기록 3](Celeris-notes-apply-3.md).
- [반영 기록 4](Celeris-notes-apply-4.md).
- [보고서 §4](../compare/celeris-docs-architecture-vs-code.md#4-노트-대조와-수정안).
- 코드와 저장소 문서의 기준 경로는 models/Celeris/raw/source_code/Celeris-WebGPU/다. 현재 코드 ebca435의 해당 줄을 대조했다.
- 문서 누락의 범위는 README.md, ARCHITECTURE.md, docs/README.md, docs/architecture/CONFIGURATION.md, DATA_AND_TEXTURES.md, REFERENCE_PAPERS.md, SIMULATION_PIPELINE.md, WEBGPU_BINDING_PATTERN.md다. 뒤의 다섯 문서는 docs/architecture/ 아래에 있다. 이 8문서의 내용을 확인했다.
- 입력과 호스트의 연결은 js/main.js:2502–2549, 3497–3518, 3564–3672, 4652–4777, 5125–5157, 5262–5264 안의 노트 지정 줄로 확인했다. HTML value 부재를 JavaScript 기본값 부재로 해석하지 않았다.

## 기계 확인 후보 판정

- 사용자 제공 후보: 없음.
- 자체 표시명 검사 CD1-1197: Bottom Friction Map 뒤의 공백은 원문 HTML과 노트의 직접 인용에 모두 남아 있다. 결론은 표시명만 기술하므로 수정하지 않았다.
- 자체 표시명 검사 CD1-1198: Design Component Map 뒤의 공백은 원문 HTML과 노트의 직접 인용에 모두 남아 있다. 결론은 표시명만 기술하므로 수정하지 않았다.

## 정정 목록

각 줄 번호는 대상 노트의 줄 번호다. 변경 후 문서 원문 칸은 “대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).”이다. 아래 근거 문장은 conclusion-verify의 해당 행 이유 칸 원문이다. 원문 HTML과 최종 결론의 내용은 유지했다.

| 노트:줄 / 행 ID | 변경 전 문서 원문 칸 | 변경 후 | 근거 원문 |
|---|---|---|---|
| celeris-webgpu-infrastructure-differences.md:123 / CD1-1097 | 대상 문서의 해당 항목 원문 없음. 보고서 항목 표기: ` 대상 8문서:HTML 세부 항목 없음 ` ` changeSeaLevel-input / value=없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1097](../compare/Celeris-conclusion-verify-CD1g.md) “정수면 변경량을 받는 모델 입력이다. 대상 문서는 이 입력의 HTML 고정 기본값 유무를 적지 않는다.” 원문 위치: `index.html:707`. |
| celeris-webgpu-infrastructure-differences.md:128 / CD1-1102 | 대상 문서의 해당 항목 원문 없음. 보고서 항목 표기: ` 대상 8문서:HTML 세부 항목 없음 ` ` changeType-select / 1 / Increase/Decrease on Click ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1102](../compare/Celeris-conclusion-verify-CD1g.md) “모델 표면의 증가·감소 또는 값 지정 방식을 고르는 입력이다. 대상 문서는 선택값 1·2의 대응을 적지 않는다.” 원문 위치: `index.html:727`. |
| celeris-webgpu-infrastructure-differences.md:129 / CD1-1103 | 대상 문서의 해당 항목 원문 없음. 보고서 항목 표기: ` 대상 8문서:HTML 세부 항목 없음 ` ` changeType-select / 2 / Set to Value on Click ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1103](../compare/Celeris-conclusion-verify-CD1g.md) “모델 표면의 증가·감소 또는 값 지정 방식을 고르는 입력이다. 대상 문서는 선택값 1·2의 대응을 적지 않는다.” 원문 위치: `index.html:727`. |
| celeris-webgpu-infrastructure-differences.md:130 / CD1-1104 | 대상 문서의 해당 항목 원문 없음. 보고서 항목 표기: ` 대상 8문서:HTML 세부 항목 없음 ` ` changeAmplitude-input / value=없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1104](../compare/Celeris-conclusion-verify-CD1g.md) “모델 표면 수정량·길이척도 입력이다. 대상 문서는 이 입력의 HTML 고정 기본값 유무를 적지 않는다.” 원문 위치: `index.html:737`. |
| celeris-webgpu-infrastructure-differences.md:131 / CD1-1105 | 대상 문서의 해당 항목 원문 없음. 보고서 항목 표기: ` 대상 8문서:HTML 세부 항목 없음 ` ` changeRadius-input / value=없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1105](../compare/Celeris-conclusion-verify-CD1g.md) “모델 표면 수정량·길이척도 입력이다. 대상 문서는 이 입력의 HTML 고정 기본값 유무를 적지 않는다.” 원문 위치: `index.html:745`. |
| celeris-webgpu-infrastructure-differences.md:160 / CD1-1170 | 대상 문서의 해당 항목 원문 없음. 보고서 항목 표기: ` 대상 8문서:HTML 세부 항목 없음 ` ` maxdurationTimeSeries-input / value=없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1170](../compare/Celeris-conclusion-verify-CD1g.md) “시계열 기록·저장 기간을 정하는 입력이다. 대상 문서는 이 입력의 HTML 고정 기본값 유무를 적지 않는다.” 원문 위치: `index.html:1047`. |
| celeris-webgpu-infrastructure-differences.md:195 / CD1-1205 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1205](../compare/Celeris-conclusion-verify-CD1g.md) “2D 모델 자료 출력 간격을 정하는 입력이다. 대상 문서는 이 입력의 HTML 고정 기본값 유무를 적지 않는다.” 원문 위치: `index.html:1260`. |
| celeris-webgpu-infrastructure-differences.md:205 / CD1-1239 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1239](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:206 / CD1-1240 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1240](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:207 / CD1-1241 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1241](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:208 / CD1-1242 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1242](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:209 / CD1-1243 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1243](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:210 / CD1-1244 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1244](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:211 / CD1-1245 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1245](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:212 / CD1-1246 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1246](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:213 / CD1-1247 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1247](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:214 / CD1-1248 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1248](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:215 / CD1-1249 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1249](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:216 / CD1-1250 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1250](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:217 / CD1-1251 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1251](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:218 / CD1-1252 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1252](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:219 / CD1-1253 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1253](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:220 / CD1-1254 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1254](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:221 / CD1-1255 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1255](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:222 / CD1-1256 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1256](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:223 / CD1-1257 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1257](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `index_headless.html:61`. |
| celeris-webgpu-infrastructure-differences.md:224 / CD1-1260 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1260](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `river.html:282`. |
| celeris-webgpu-infrastructure-differences.md:225 / CD1-1261 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1261](../compare/Celeris-conclusion-verify-CD1h.md) “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `river.html:282`. |
| celeris-webgpu-infrastructure-differences.md:226 / CD1-1271 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1271](../compare/Celeris-conclusion-verify-CD1h.md) “Design 선택은 지형 편집의 실행 조건 viewType==1에도 쓰인다. 화면 배치만의 항목이 아니므로 모델 입력 누락 C를 유지한다.” 원문 위치: `river.html:436`. |
| celeris-webgpu-infrastructure-differences.md:227 / CD1-1273 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1273](../compare/Celeris-conclusion-verify-CD1h.md) “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `river.html:461`. |
| celeris-webgpu-infrastructure-differences.md:228 / CD1-1274 | ` 대상 8문서:HTML 세부 항목 없음 ` | 백틱을 제거한 문서 누락 설명으로 정정했다. 결론 끝에 정정 표지를 붙였다. | [CD1-1274](../compare/Celeris-conclusion-verify-CD1h.md) “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `river.html:461`. |

## 줄별 대조 기록

모든 행의 최종 분류와 결론은 일치한다. 참조 수는 인용 앞 경로와 확인한 원문 목록을 함께 센 값이다. 수정 31행은 원문과 설명을 구분하는 표기 정정이다.

| 노트 줄 | 행 ID | 원문 인용 수 | 경로·줄 참조 수 | 결과 |
|---:|---|---:|---:|---|
| 115 | CD1-1089 | 6 | 14 | 일치·수정 없음 |
| 116 | CD1-1090 | 6 | 14 | 일치·수정 없음 |
| 117 | CD1-1091 | 6 | 14 | 일치·수정 없음 |
| 118 | CD1-1092 | 6 | 14 | 일치·수정 없음 |
| 119 | CD1-1093 | 11 | 24 | 일치·수정 없음 |
| 120 | CD1-1094 | 11 | 24 | 일치·수정 없음 |
| 121 | CD1-1095 | 6 | 14 | 일치·수정 없음 |
| 122 | CD1-1096 | 6 | 14 | 일치·수정 없음 |
| 123 | CD1-1097 | 5 | 13 | 누락 설명 표기 정정 |
| 124 | CD1-1098 | 15 | 26 | 일치·수정 없음 |
| 125 | CD1-1099 | 17 | 30 | 일치·수정 없음 |
| 126 | CD1-1100 | 15 | 26 | 일치·수정 없음 |
| 127 | CD1-1101 | 15 | 26 | 일치·수정 없음 |
| 128 | CD1-1102 | 10 | 23 | 누락 설명 표기 정정 |
| 129 | CD1-1103 | 10 | 23 | 누락 설명 표기 정정 |
| 130 | CD1-1104 | 5 | 13 | 누락 설명 표기 정정 |
| 131 | CD1-1105 | 5 | 13 | 누락 설명 표기 정정 |
| 132 | CD1-1142 | 16 | 29 | 일치·수정 없음 |
| 133 | CD1-1143 | 16 | 29 | 일치·수정 없음 |
| 134 | CD1-1144 | 16 | 29 | 일치·수정 없음 |
| 135 | CD1-1145 | 16 | 29 | 일치·수정 없음 |
| 136 | CD1-1146 | 13 | 21 | 일치·수정 없음 |
| 137 | CD1-1147 | 13 | 21 | 일치·수정 없음 |
| 138 | CD1-1148 | 13 | 21 | 일치·수정 없음 |
| 139 | CD1-1149 | 13 | 21 | 일치·수정 없음 |
| 140 | CD1-1150 | 13 | 21 | 일치·수정 없음 |
| 141 | CD1-1151 | 13 | 21 | 일치·수정 없음 |
| 142 | CD1-1152 | 13 | 21 | 일치·수정 없음 |
| 143 | CD1-1153 | 13 | 21 | 일치·수정 없음 |
| 144 | CD1-1154 | 11 | 24 | 일치·수정 없음 |
| 145 | CD1-1155 | 11 | 24 | 일치·수정 없음 |
| 146 | CD1-1156 | 11 | 24 | 일치·수정 없음 |
| 147 | CD1-1157 | 11 | 24 | 일치·수정 없음 |
| 148 | CD1-1158 | 11 | 24 | 일치·수정 없음 |
| 149 | CD1-1159 | 11 | 24 | 일치·수정 없음 |
| 150 | CD1-1160 | 11 | 24 | 일치·수정 없음 |
| 151 | CD1-1161 | 11 | 24 | 일치·수정 없음 |
| 152 | CD1-1162 | 11 | 24 | 일치·수정 없음 |
| 153 | CD1-1163 | 11 | 24 | 일치·수정 없음 |
| 154 | CD1-1164 | 11 | 24 | 일치·수정 없음 |
| 155 | CD1-1165 | 11 | 24 | 일치·수정 없음 |
| 156 | CD1-1166 | 11 | 24 | 일치·수정 없음 |
| 157 | CD1-1167 | 11 | 24 | 일치·수정 없음 |
| 158 | CD1-1168 | 11 | 24 | 일치·수정 없음 |
| 159 | CD1-1169 | 11 | 24 | 일치·수정 없음 |
| 160 | CD1-1170 | 5 | 12 | 누락 설명 표기 정정 |
| 161 | CD1-1171 | 11 | 24 | 일치·수정 없음 |
| 162 | CD1-1172 | 11 | 24 | 일치·수정 없음 |
| 163 | CD1-1173 | 11 | 24 | 일치·수정 없음 |
| 164 | CD1-1174 | 11 | 24 | 일치·수정 없음 |
| 165 | CD1-1175 | 11 | 24 | 일치·수정 없음 |
| 166 | CD1-1176 | 11 | 24 | 일치·수정 없음 |
| 167 | CD1-1177 | 11 | 24 | 일치·수정 없음 |
| 168 | CD1-1178 | 11 | 24 | 일치·수정 없음 |
| 169 | CD1-1179 | 11 | 24 | 일치·수정 없음 |
| 170 | CD1-1180 | 11 | 24 | 일치·수정 없음 |
| 171 | CD1-1181 | 11 | 24 | 일치·수정 없음 |
| 172 | CD1-1182 | 11 | 24 | 일치·수정 없음 |
| 173 | CD1-1183 | 11 | 24 | 일치·수정 없음 |
| 174 | CD1-1184 | 11 | 24 | 일치·수정 없음 |
| 175 | CD1-1185 | 11 | 24 | 일치·수정 없음 |
| 176 | CD1-1186 | 6 | 14 | 일치·수정 없음 |
| 177 | CD1-1187 | 6 | 14 | 일치·수정 없음 |
| 178 | CD1-1188 | 9 | 17 | 일치·수정 없음 |
| 179 | CD1-1189 | 9 | 17 | 일치·수정 없음 |
| 180 | CD1-1190 | 9 | 17 | 일치·수정 없음 |
| 181 | CD1-1191 | 11 | 24 | 일치·수정 없음 |
| 182 | CD1-1192 | 11 | 24 | 일치·수정 없음 |
| 183 | CD1-1193 | 11 | 24 | 일치·수정 없음 |
| 184 | CD1-1194 | 11 | 24 | 일치·수정 없음 |
| 185 | CD1-1195 | 11 | 24 | 일치·수정 없음 |
| 186 | CD1-1196 | 11 | 24 | 일치·수정 없음 |
| 187 | CD1-1197 | 11 | 24 | 일치·수정 없음 |
| 188 | CD1-1198 | 11 | 24 | 일치·수정 없음 |
| 189 | CD1-1199 | 11 | 24 | 일치·수정 없음 |
| 190 | CD1-1200 | 11 | 24 | 일치·수정 없음 |
| 191 | CD1-1201 | 11 | 24 | 일치·수정 없음 |
| 192 | CD1-1202 | 11 | 24 | 일치·수정 없음 |
| 193 | CD1-1203 | 11 | 24 | 일치·수정 없음 |
| 194 | CD1-1204 | 11 | 24 | 일치·수정 없음 |
| 195 | CD1-1205 | 5 | 13 | 누락 설명 표기 정정 |
| 196 | CD1-1206 | 11 | 24 | 일치·수정 없음 |
| 197 | CD1-1207 | 11 | 24 | 일치·수정 없음 |
| 198 | CD1-1208 | 11 | 24 | 일치·수정 없음 |
| 199 | CD1-1209 | 11 | 24 | 일치·수정 없음 |
| 200 | CD1-1210 | 11 | 24 | 일치·수정 없음 |
| 201 | CD1-1211 | 11 | 24 | 일치·수정 없음 |
| 202 | CD1-1212 | 11 | 24 | 일치·수정 없음 |
| 203 | CD1-1213 | 11 | 24 | 일치·수정 없음 |
| 204 | CD1-1225 | 6 | 14 | 일치·수정 없음 |
| 205 | CD1-1239 | 2 | 5 | 누락 설명 표기 정정 |
| 206 | CD1-1240 | 2 | 5 | 누락 설명 표기 정정 |
| 207 | CD1-1241 | 2 | 5 | 누락 설명 표기 정정 |
| 208 | CD1-1242 | 2 | 5 | 누락 설명 표기 정정 |
| 209 | CD1-1243 | 2 | 5 | 누락 설명 표기 정정 |
| 210 | CD1-1244 | 2 | 5 | 누락 설명 표기 정정 |
| 211 | CD1-1245 | 2 | 5 | 누락 설명 표기 정정 |
| 212 | CD1-1246 | 2 | 5 | 누락 설명 표기 정정 |
| 213 | CD1-1247 | 2 | 5 | 누락 설명 표기 정정 |
| 214 | CD1-1248 | 2 | 5 | 누락 설명 표기 정정 |
| 215 | CD1-1249 | 2 | 5 | 누락 설명 표기 정정 |
| 216 | CD1-1250 | 2 | 5 | 누락 설명 표기 정정 |
| 217 | CD1-1251 | 2 | 5 | 누락 설명 표기 정정 |
| 218 | CD1-1252 | 2 | 5 | 누락 설명 표기 정정 |
| 219 | CD1-1253 | 2 | 5 | 누락 설명 표기 정정 |
| 220 | CD1-1254 | 2 | 5 | 누락 설명 표기 정정 |
| 221 | CD1-1255 | 2 | 5 | 누락 설명 표기 정정 |
| 222 | CD1-1256 | 2 | 5 | 누락 설명 표기 정정 |
| 223 | CD1-1257 | 2 | 5 | 누락 설명 표기 정정 |
| 224 | CD1-1260 | 2 | 5 | 누락 설명 표기 정정 |
| 225 | CD1-1261 | 2 | 5 | 누락 설명 표기 정정 |
| 226 | CD1-1271 | 2 | 5 | 누락 설명 표기 정정 |
| 227 | CD1-1273 | 2 | 5 | 누락 설명 표기 정정 |
| 228 | CD1-1274 | 2 | 5 | 누락 설명 표기 정정 |

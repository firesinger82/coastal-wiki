# Celeris 노트 전수 검증 6

## 배정과 진행

- 대상: `models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md`.
- 시작 시 전체 줄 수: 341줄.
- 순서대로 세 몫으로 나누며 앞의 두 몫에 각각 114줄을 배정한다.
- 이 작업의 대상: 시작 시 229–341줄, 113줄이다. 이 범위는 모두 차이 표의 행이다.
- 상태: 완료.
- 기계 확인 불일치 후보: 사용자 제공 후보 없음.

## 완료 결과

- 대상 노트: [celeris-webgpu-infrastructure-differences.md](../../../models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md).
- 대조한 줄 수는 113줄이다. 정정한 줄 수는 31줄이다. 인용을 보완한 줄 수는 7줄이다. 원문 대조 후 유지한 줄 수는 75줄이다.
- 집계 단위는 노트의 물리적인 한 줄이다. 같은 행의 두 위치를 고친 경우에도 한 줄로 센다.
- 수정한 38줄의 결론 칸 끝에 해당 전수 검증 표식을 붙였다.
- 최종 분류는 A 30행, B 11행, C 70행, E 2행이다. 분류의 근거는 배정 TSV와 각 행의 conclusion-verify 파일이다.
- CD1-1305의 E 강도는 중간으로 유지했다. CD2-457의 E 강도는 강함으로 유지했다. CD2-457의 “현재 실행 경로에서 호출되지 않음”을 유지했다.
- 담당 범위에는 frontmatter와 Mermaid 블록이 없다.
- 담당 범위의 상대 링크 114개는 모두 실제 파일을 가리킨다.
- 담당 범위에는 금지된 절대 경로, 홈 축약 경로, 위키 링크, 한계 문장이 없다.
- 미해결 항목은 0개다.

## 대조 근거와 검사

- 현재 파일과 이전 커밋 파일의 인용 위치를 열어 대조했다. 수정 후 경로·줄 참조 1,278개를 다시 검사했다. 이 수는 반복된 참조를 포함한다.
- 줄 번호 뒤의 코드 인용은 해당 원문 범위와 대조했다. Markdown 표의 파이프 이스케이프와 인용 앞뒤 공백을 제외하고 글자를 비교했다.
- 각 행의 분류는 [최종 배정표](../assign/Celeris-final-conclusions.tsv)와 대조했다.
- 각 행의 결론은 연결된 conclusion-verify의 최종 결론과 대조했다. 검증 표식, 논문 쪽 안내 접두어, 백틱, 생략된 파일명의 보충을 정규화한 뒤 불일치는 0행이다.
- A 행의 논문 판과 이전 코드 인용을 대조했다. CD1-1330·1331과 CP3-071의 bb99fee 근거를 확인했다. CP1-072의 32be94a와 CP1-079의 471c581 원문도 확인했다.
- E 행은 최종 결론을 우선했다. CD2-457은 E1의 H 판정 이후 최종 검증에서 E로 재분류된 행이다.
- 논문의 식·숫자·표는 쪽 이미지로 판정했다. 확인한 쪽은 Lynett 2026 PDF p.1–9,12, Tavakkol 2017 PDF p.4–7,10–11, Tavakkol 2020 PDF p.1–14이다.
- [노트 반영 기록 4](Celeris-notes-apply-4.md)의 수정안 10행을 보고서 수정안과 대조했다. 해당 행은 CD1-1327–1333, CP3-117, CP1-139, CP2-173이다.
- [외부 출처 기록](../compare/Celeris-external-sources.md)의 최종 절은 CP3-013·017에 관한 기록이다. 이 두 행은 담당 구간 밖이다.
- 패치 직전에 해당 노트 줄을 다시 읽었다. 각 패치는 한 파일의 한 행에 적용했다.
- 아래 행별 기록의 줄 번호는 작업 시작 시와 완료 시에 동일하다.

## 정정 목록

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:229 (CD1-1275): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:89](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1275: “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `ebca435:river.html:461`; `ebca435:river.html:464`; `ebca435:js/main.js:2504-2512,4760,4768`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:230 (CD1-1276): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:90](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1276: “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `ebca435:river.html:461`; `ebca435:river.html:467`; `ebca435:js/main.js:2504-2512,4760,4768`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:231 (CD1-1277): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:91](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1277: “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `ebca435:river.html:461`; `ebca435:river.html:468`; `ebca435:js/main.js:2504-2512,4760,4768`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:232 (CD1-1278): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:92](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1278: “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `ebca435:river.html:461`; `ebca435:river.html:469`; `ebca435:js/main.js:2504-2512,4760,4768`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:233 (CD1-1279): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:93](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1279: “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `ebca435:river.html:461`; `ebca435:river.html:470`; `ebca435:js/main.js:2504-2512,4760,4768`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:234 (CD1-1280): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:94](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1280: “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `ebca435:river.html:642`; `ebca435:river.html:643`; `ebca435:js/main.js:2504-2512,4760,4768`

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:235 (CD1-1281): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:95](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1281: “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `ebca435:river.html:642`; `ebca435:river.html:645`; `ebca435:js/main.js:2504-2512,4760,4768`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:236 (CD1-1282): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:96](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1282: “지형·마찰·오염원·수면 편집에 전달하는 모델 입력이다. 대상 문서는 HTML 선택값 대응을 열거하지 않는다.” 원문 위치: `ebca435:river.html:642`; `ebca435:river.html:646`; `ebca435:js/main.js:2504-2512,4760,4768`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:237 (CD1-1288): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:105](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1288: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:282`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:238 (CD1-1289): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:106](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1289: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:283`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:239 (CD1-1290): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:107](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1290: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:284`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:240 (CD1-1291): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:108](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1291: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:285`; `ebca435:js/main.js:4763,5262-5264`

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:241 (CD1-1292): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:109](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1292: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:286`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:242 (CD1-1293): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:110](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1293: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:287`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:243 (CD1-1294): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:111](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1294: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:288`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:244 (CD1-1295): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:112](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1295: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:289`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:245 (CD1-1296): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:113](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1296: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:290`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:246 (CD1-1297): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:114](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1297: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:291`; `ebca435:js/main.js:4763,5262-5264`

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:247 (CD1-1298): ` 대상 8문서:HTML 세부 항목 없음 ` → 대상 8문서에 해당 HTML 세부 항목의 문장 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:115](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1298: “예제 선택값을 run_example에 전달하는 입력 대응이다. 사례의 물리 타당성에 대한 판정이 아니다. 대상 문서는 이 대응표를 적지 않는다.” 원문 위치: `ebca435:MC_examples.html:281`; `ebca435:MC_examples.html:292`; `ebca435:js/main.js:4763,5262-5264`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:248 (CD1-1305): ` 대상 문서·현재 코드:호출·조건 교차대조 ` → 대상 문서와 현재 코드의 호출·조건을 교차 대조한 설명(문서 원문 인용 아님).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:125](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1305: “대체 HTML도 같은 main.js를 로드하지만 필수 버튼이 없다. headless의 필수 DOM 보존 주석과 일반 리스너의 존재 검사 경로가 각각 반증이다. 해당 ID를 동적으로 생성하는 경로는 없다. 다른 누락 DOM이 먼저 실행을 중단할 수 있으므로 최초 실패 위치는 확정하지 않는다. 보고서의 강함을 E1과 같이 중간으로 낮춘다.” 원문 위치: `ebca435:index_headless.html:49-59,104-112`; `ebca435:river.html:1468`; `ebca435:index_nots.html:1486`; `ebca435:MC_examples.html:1468`; `ebca435:js/main.js:4830-4845,4850-4853,5242-5246`; `ebca435:index_headless.html:24`; `bb99fee:js/main.js` 중첩 버튼 리스너 추가. `rg -n "refresh-button\|startNestedGridOutput-button\|src=\"js/main.js\"" index_headless.html river.html index_nots.html MC_examples.html index.html js/main.js`: 위 누락 확인.
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:256 (CD1-1387): ` 대상 8문서:구체식·분기 상세 없음 ` → 대상 8문서에 해당 구체식·분기의 상세 설명 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:201](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1387: “대상 문서는 metric의 네 채널과 보호 계산을 적지 않는다. 인용 보정: 이상적인 1/(R cosφ)만 적은 결론에 cos 및 반지름 보호식을 복원한다.” 원문 위치: `ebca435:js/Copy_Data_to_Textures.js:366-381`; `ebca435:js/Copy_Data_to_Textures.js:357-358`.
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:257 (CD1-1392): ` 대상 8문서:구체식·분기 상세 없음 ` → 대상 8문서에 해당 구체식·분기의 상세 설명 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:206](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1392: “대상 문서는 구조물 단면식을 적지 않는다. 원문은 마루 안쪽의 side_distance를 0으로 제한한다. 인용 보정: 보고서가 빠뜨린 max를 복원한다.” 원문 위치: `ebca435:shaders/MouseClickChange.wgsl:86-100`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:258 (CD1-1393): ` 대상 8문서:구체식·분기 상세 없음 ` → 대상 8문서에 해당 구체식·분기의 상세 설명 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:207](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1393: “대상 문서는 수위 입력을 바닥 이동으로 구현하는 조건과 하한을 적지 않는다. 인용 보정: 패널 조건·변화량 임계값·min_val 제한을 복원한다.” 원문 위치: `ebca435:shaders/MouseClickChange.wgsl:150-167`; `ebca435:shaders/MouseClickChange.wgsl:110-124`.
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:259 (CD1-1394): ` 대상 8문서:구체식·분기 상세 없음 ` → 대상 8문서에 해당 구체식·분기의 상세 설명 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:208](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1394: “대상 문서는 평균의 표본 가중치와 절대 와도 사용을 적지 않는다. signed vorticity 평균이 아니라 abs를 누적하는 원문을 확인했다.” 원문 위치: `ebca435:shaders/CalcMeans.wgsl:73-79`

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:260 (CD1-1395): ` 대상 8문서:구체식·분기 상세 없음 ` → 대상 8문서에 해당 구체식·분기의 상세 설명 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:209](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1395: “대상 문서는 최댓값 초기값과 첫 표본 처리 조건을 적지 않는다. 임시 최댓값이 0이고 두 번째 표본부터 비교한다는 원문을 확인했다.” 원문 위치: `ebca435:shaders/CalcMeans.wgsl:81-102`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:261 (CD1-1396): ` 대상 8문서:구체식·분기 상세 없음 ` → 대상 8문서에 해당 구체식·분기의 상세 설명 없음(문서 누락 설명).. 근거: 문서 원문이 아닌 설명의 백틱을 제거하고 설명임을 명시했다. 최종 근거 [Celeris-conclusion-verify-CD1h.md:210](../compare/Celeris-conclusion-verify-CD1h.md)의 CD1-1396: “대상 문서는 파고 환산 계수와 g채널 식을 적지 않는다. g채널은 시간으로 나눈 변화율이 아니라 이전 H_sig에 대한 상대 변화다. 인용 보정: 변화율의 뜻과 0분모 보호 부재를 명확히 적는다.” 원문 위치: `ebca435:shaders/CalcWaveHeight.wgsl:25-42`
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:301 (CP1-075): `<range filename="island">` → `<range filename = "island">`; `<gauges filename="gauges">` → `<gauges filename = "gauges">`. 근거: Tavakkol 2017 PDF p.5 Fig.2에서 range와 gauges의 filename 속성은 등호 양쪽에 공백이 있다.
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:312 (CP1-139): `d8157c80:models/Celeris/d8157c80:models/Celeris/` → `d8157c80:models/Celeris/`. 근거: d8157c80:models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:191의 실제 경로와 원문을 확인했다. 중복된 커밋·경로 접두어를 두 곳에서 제거했다.
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:313 (CP2-004): `; 5절 검색 D2` → `; 검색 근거: [대조 보고서](../../../_staging/recovery/compare/celeris-tavakkol2020-vs-code.md)의 5절 검색 D2`. 근거: 보고서 내부의 5절 검색 D2를 노트 내부 위치처럼 안내하므로 실제 보고서 링크를 붙였다. Celeris-conclusion-verify-CP2.md의 CP2-004가 검색어·검색 결과와 최종 A 판정을 기록한다.
- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:314 (CP2-046): ```js/main.js:4767` `{ input: 'useBreakingModel-select', property: 'useBreakingModel' },``` → ```js/main.js:4749` `{ input: 'west_boundary_type-select', property: 'west_boundary_type' },```. 근거: js/main.js:4749 원문은 { input: 'west_boundary_type-select', property: 'west_boundary_type' }, 이다. Celeris-conclusion-verify-CP2.md:70도 4767행의 쇄파 설정을 4749행의 경계 설정으로 교정하도록 명시한다.

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:324 (CP2-091): `인쇄 Tavakkol 2020 p.122` → `인쇄 p.122`. 근거: Tavakkol 2017 PDF p.6의 인쇄 쪽수는 122이다. Celeris-conclusion-verify-CP2.md:108도 P17 p.6(인쇄 p.122)로 적는다. 2020 연도 표기를 두 곳에서 제거했다.

## 인용 보완 목록

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:318 (CP2-082): `js/main.js:4543–4544` 아래 U1 → `js/main.js:4543` `calc_constants.mouse_current_canvas_indX = Math.round(normalizedX * calc_constants.WIDTH);`<br>`js/main.js:4544` `calc_constants.mouse_current_canvas_indY = Math.round(normalizedY * calc_constants.HEIGHT);`. 근거: js/main.js:4543–4544의 canvas 정규화 좌표→격자 index 계산 원문을 직접 인용했다. 최종 판정은 [Celeris-conclusion-verify-CP2.md:101](../compare/Celeris-conclusion-verify-CP2.md)의 CP2-082와 일치한다.

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:323 (CP2-090): `js/File_Loader.js:43–46` 아래 U3 → `js/File_Loader.js:43` `if (depthValues.length !== calc_constants.WIDTH) {`<br>`js/File_Loader.js:44` `console.error("Bathytopo file at " + filePath + " is not in the correct format.");`<br>`js/File_Loader.js:45` `return null;`<br>`js/File_Loader.js:46` `}`. 근거: js/File_Loader.js:43–46의 WIDTH 불일치 조건과 null 반환 원문을 직접 인용했다. 최종 판정은 [Celeris-conclusion-verify-CP2.md:107](../compare/Celeris-conclusion-verify-CP2.md)의 CP2-090와 일치한다.

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:328 (CP2-127): `js/constants_load_calc.js:23–28` WIDTH=800, HEIGHT=600, dx=1.0, dy=1.0 원문은 CP2-021·114에 인용했다. → `js/constants_load_calc.js:23` `WIDTH: 800,  // Width of the computational domain.`<br>`js/constants_load_calc.js:24` `HEIGHT: 600,  // Height of the computational domain.`<br>`js/constants_load_calc.js:27` `dx: 1.0,  // Cell size in the x direction.`<br>`js/constants_load_calc.js:28` `dy: 1.0,  // Cell size in the y direction.`<br>`js/constants_load_calc.js:31` `Courant_num: 0.15,  // Target Courant number. ~0.25 for P-C, ~0.05 for explicit methods.`<br>`js/constants_load_calc.js:45` `Theta: 2.0,  // Midmod limiter parameter. 1.0 most dissipative(upwind) to 2.0 least dissipative(centered).`;. 근거: js/constants_load_calc.js:23–31,45의 격자·시간 간격·제한자 기본값을 직접 인용했다. 노트에 없는 CP2-021·114 안내를 대체했다. 최종 판정은 [Celeris-conclusion-verify-CP2.md:146](../compare/Celeris-conclusion-verify-CP2.md)의 CP2-127와 일치한다.

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:331 (CP2-145): `shaders/CalcWaveHeight.wgsl:31–42` 아래 C16 → `shaders/CalcWaveHeight.wgsl:31` `let eta = eta_New-eta_mean;`<br>`shaders/CalcWaveHeight.wgsl:33` `sum_eta2 = sum_eta2 + eta * eta;`<br>`shaders/CalcWaveHeight.wgsl:35` `var variance = sum_eta2 / f32(globals.n_time_steps_waveheight);`<br>`shaders/CalcWaveHeight.wgsl:37` `let sigma = sqrt(variance);`<br>`shaders/CalcWaveHeight.wgsl:39` `let H_mean = sigma * 2.829;  // RMS wave height`<br>`shaders/CalcWaveHeight.wgsl:40` `let H_sig = sigma * 4.000;   // sig wave height`<br>`shaders/CalcWaveHeight.wgsl:42` `let new_vals = vec4<f32>(sum_eta2, (H_sig-old_vals.b)/old_vals.b, H_sig, H_mean);`. 근거: shaders/CalcWaveHeight.wgsl:31–42의 eta 차이·제곱 누적·분산·RMS 파고·유의파고 식을 직접 인용했다. 최종 판정은 [Celeris-conclusion-verify-CP2.md:167](../compare/Celeris-conclusion-verify-CP2.md)의 CP2-145와 일치한다.

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:333 (CP2-148): `js/Time_Series.js:108–112` 아래 C17; `js/Time_Series.js:166`의 `Time/Eta/P/Q` header는 CP2-091에 인용했다. → `js/Time_Series.js:108` `if (timeSeriesDataEpoch != calc_constants.timeSeriesDataEpoch) {`<br>`js/Time_Series.js:109` `buffer.unmap();`<br>`js/Time_Series.js:110` `buffer.destroy();`<br>`js/Time_Series.js:111` `return;`<br>`js/Time_Series.js:112` `}`<br>`js/Time_Series.js:166` ``headers += `Time${i+1}\tEta${i+1}\tP${i+1}\tQ${i+1}\t`;``.. 근거: js/Time_Series.js:108–112의 epoch 불일치 조건·버퍼 해제·return과 166행의 header를 직접 인용했다. 최종 판정은 [Celeris-conclusion-verify-CP2.md:170](../compare/Celeris-conclusion-verify-CP2.md)의 CP2-148와 일치한다.

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:334 (CP2-149): `js/constants_load_calc.js:358–370` 아래 C18 → `js/constants_load_calc.js:358` `create_animation: 0, // create animated gif when = 1`<br>`js/constants_load_calc.js:359` `AnimGif_dt: 1.0, // time between animated gif frames`<br>`js/constants_load_calc.js:360` `JPEGstack_dt: 1.0,  // time between images in jpeg stack`<br>`js/constants_load_calc.js:361` `JPEGstack_frames: 10,  // total number of frames to save in jpg stack`<br>`js/constants_load_calc.js:362` `writesurfaces: 0,  //flag for writing 2D data to file`<br>`js/constants_load_calc.js:363` `write_eta: 1, // flag for writing eta surface data to file, write when = 1`<br>`js/constants_load_calc.js:364` `write_P: 0, // flag for writing x flux surface data to file, write when = 1`<br>`js/constants_load_calc.js:365` `write_Q: 0, // flag for writing y flux surface data to file, write when = 1`<br>`js/constants_load_calc.js:366` `write_u: 0, // flag for writing x velocity surface data to file, write when = 1`<br>`js/constants_load_calc.js:367` `write_v: 0, // flag for writing y velocity surface data to file, write when = 1`<br>`js/constants_load_calc.js:368` `write_turb: 0, // flag for writing eddy visc surface data to file, write when = 1`<br>`js/constants_load_calc.js:369` `dt_writesurface: 1.0, // incrememnt to write to file`<br>`js/constants_load_calc.js:370` `fileWritePause: 100, // time (ms) to pause during 2D surface write to not overload write buffer`. 근거: js/constants_load_calc.js:358–370의 GIF·JPEG·면 출력 플래그·주기 원문을 직접 인용했다. 최종 판정은 [Celeris-conclusion-verify-CP2.md:171](../compare/Celeris-conclusion-verify-CP2.md)의 CP2-149와 일치한다.

- models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:337 (CP2-152): `js/File_Loader.js:50–53`의 NaN 검사 U2 → `js/File_Loader.js:50` `if (isNaN(parsedValue)) {`<br>`js/File_Loader.js:51` ``console.error(`Could not parse bathytopo value at [${x}, ${y}] in bathytopo file at ${filePath}`);``<br>`js/File_Loader.js:52` `return null;`<br>`js/File_Loader.js:53` `}`. 근거: js/File_Loader.js:50–53의 NaN 조건과 null 반환 원문을 직접 인용했다. 최종 판정은 [Celeris-conclusion-verify-CP2.md:174](../compare/Celeris-conclusion-verify-CP2.md)의 CP2-152와 일치한다.

## 기계 확인 후보 판정

- 사용자 제공 불일치 후보: 없음.
- 자체 인용 검사: 수정 후 파일·줄 참조와 바로 뒤의 원문 인용에서 불일치가 없다.
- 자체 분류 검사: E 강도를 별도 괄호로 적은 두 행은 배정 TSV의 분류명과 문자열이 다르다. 최종 검증표의 E 강도와 대조하여 두 행 모두 일치로 판정했다.
- 자체 결론 검사: 검증 표식, 논문 쪽 안내, 백틱, 생략된 파일명을 보충한 표기를 정규화하면 불일치가 없다.
- 의미 대조에서 찾은 CP2-046의 잘못된 경계 UI 인용은 314줄에서 정정했다. 4767행의 문자열 자체는 맞지만 해당 행은 쇄파 설정이므로 경계 UI의 근거가 아니다.
- 중복된 과거 경로는 312줄에서 정정했다. Tavakkol 2017의 인쇄 쪽에 붙은 2020 표기는 324줄에서 정정했다.
- 보고서 내부 표식 U1·U2·U3·C16·C17·C18과 노트에 없는 CP2-021·114 안내는 해당 원문 인용으로 보완했다.
- D2 검색 안내는 313줄에서 실제 보고서 링크로 정정했다. 분류는 최종 검증표의 A를 유지했다.

## 전체 대상 줄 대조 기록

줄 번호는 대상 노트 기준이다. 최종 근거 링크 뒤의 행 ID로 해당 결론을 찾을 수 있다.

| 노트 줄 | 행 ID | 최종 분류 | 최종 근거 | 결과 |
|---:|---|---|---|---|
| 229 | CD1-1275 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1275 | 정정 완료 |
| 230 | CD1-1276 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1276 | 정정 완료 |
| 231 | CD1-1277 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1277 | 정정 완료 |
| 232 | CD1-1278 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1278 | 정정 완료 |
| 233 | CD1-1279 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1279 | 정정 완료 |
| 234 | CD1-1280 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1280 | 정정 완료 |
| 235 | CD1-1281 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1281 | 정정 완료 |
| 236 | CD1-1282 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1282 | 정정 완료 |
| 237 | CD1-1288 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1288 | 정정 완료 |
| 238 | CD1-1289 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1289 | 정정 완료 |
| 239 | CD1-1290 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1290 | 정정 완료 |
| 240 | CD1-1291 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1291 | 정정 완료 |
| 241 | CD1-1292 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1292 | 정정 완료 |
| 242 | CD1-1293 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1293 | 정정 완료 |
| 243 | CD1-1294 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1294 | 정정 완료 |
| 244 | CD1-1295 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1295 | 정정 완료 |
| 245 | CD1-1296 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1296 | 정정 완료 |
| 246 | CD1-1297 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1297 | 정정 완료 |
| 247 | CD1-1298 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1298 | 정정 완료 |
| 248 | CD1-1305 | E 코드 결함 후보 (중간) | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1305 | 정정 완료 |
| 249 | CD1-1327 | B 문서 오기 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1327 | 원문 일치·유지 |
| 250 | CD1-1328 | B 문서 오기 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1328 | 원문 일치·유지 |
| 251 | CD1-1329 | B 문서 오기 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1329 | 원문 일치·유지 |
| 252 | CD1-1330 | A 판 차이 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1330 | 원문 일치·유지 |
| 253 | CD1-1331 | A 판 차이 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1331 | 원문 일치·유지 |
| 254 | CD1-1332 | A 판 차이 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1332 | 원문 일치·유지 |
| 255 | CD1-1333 | B 문서 오기 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1333 | 원문 일치·유지 |
| 256 | CD1-1387 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1387 | 정정 완료 |
| 257 | CD1-1392 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1392 | 정정 완료 |
| 258 | CD1-1393 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1393 | 정정 완료 |
| 259 | CD1-1394 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1394 | 정정 완료 |
| 260 | CD1-1395 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1395 | 정정 완료 |
| 261 | CD1-1396 | C 문서 누락 | [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) CD1-1396 | 정정 완료 |
| 262 | CD2-215 | B 문서 오기 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-215 | 원문 일치·유지 |
| 263 | CD2-350 | B 문서 오기 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-350 | 원문 일치·유지 |
| 264 | CD2-410 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-410 | 원문 일치·유지 |
| 265 | CD2-411 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-411 | 원문 일치·유지 |
| 266 | CD2-413 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-413 | 원문 일치·유지 |
| 267 | CD2-416 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-416 | 원문 일치·유지 |
| 268 | CD2-417 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-417 | 원문 일치·유지 |
| 269 | CD2-418 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-418 | 원문 일치·유지 |
| 270 | CD2-419 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-419 | 원문 일치·유지 |
| 271 | CD2-420 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-420 | 원문 일치·유지 |
| 272 | CD2-421 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-421 | 원문 일치·유지 |
| 273 | CD2-423 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-423 | 원문 일치·유지 |
| 274 | CD2-424 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-424 | 원문 일치·유지 |
| 275 | CD2-425 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-425 | 원문 일치·유지 |
| 276 | CD2-426 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-426 | 원문 일치·유지 |
| 277 | CD2-427 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-427 | 원문 일치·유지 |
| 278 | CD2-428 | B 문서 오기 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-428 | 원문 일치·유지 |
| 279 | CD2-429 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-429 | 원문 일치·유지 |
| 280 | CD2-430 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-430 | 원문 일치·유지 |
| 281 | CD2-431 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-431 | 원문 일치·유지 |
| 282 | CD2-432 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-432 | 원문 일치·유지 |
| 283 | CD2-433 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-433 | 원문 일치·유지 |
| 284 | CD2-451 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-451 | 원문 일치·유지 |
| 285 | CD2-452 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-452 | 원문 일치·유지 |
| 286 | CD2-453 | C 문서 누락 | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-453 | 원문 일치·유지 |
| 287 | CD2-457 | E 코드 결함 후보 (강함) | [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) CD2-457 | 원문 일치·유지 |
| 288 | CP3-025 | B 문서 오기 | [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) CP3-025 | 원문 일치·유지 |
| 289 | CP3-071 | A 판 차이 | [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) CP3-071 | 원문 일치·유지 |
| 290 | CP3-082 | C 문서 누락 | [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) CP3-082 | 원문 일치·유지 |
| 291 | CP3-083 | C 문서 누락 | [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) CP3-083 | 원문 일치·유지 |
| 292 | CP3-101 | C 문서 누락 | [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) CP3-101 | 원문 일치·유지 |
| 293 | CP3-105 | C 문서 누락 | [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) CP3-105 | 원문 일치·유지 |
| 294 | CP3-106 | C 문서 누락 | [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) CP3-106 | 원문 일치·유지 |
| 295 | CP3-117 | B 문서 오기 | [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) CP3-117 | 원문 일치·유지 |
| 296 | CP1-068 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-068 | 원문 일치·유지 |
| 297 | CP1-069 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-069 | 원문 일치·유지 |
| 298 | CP1-070 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-070 | 원문 일치·유지 |
| 299 | CP1-071 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-071 | 원문 일치·유지 |
| 300 | CP1-072 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-072 | 원문 일치·유지 |
| 301 | CP1-075 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-075 | 정정 완료 |
| 302 | CP1-076 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-076 | 원문 일치·유지 |
| 303 | CP1-079 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-079 | 원문 일치·유지 |
| 304 | CP1-080 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-080 | 원문 일치·유지 |
| 305 | CP1-083 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-083 | 원문 일치·유지 |
| 306 | CP1-086 | A 판 차이 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-086 | 원문 일치·유지 |
| 307 | CP1-118 | C 문서 누락 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-118 | 원문 일치·유지 |
| 308 | CP1-119 | C 문서 누락 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-119 | 원문 일치·유지 |
| 309 | CP1-133 | C 문서 누락 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-133 | 원문 일치·유지 |
| 310 | CP1-134 | C 문서 누락 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-134 | 원문 일치·유지 |
| 311 | CP1-135 | C 문서 누락 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-135 | 원문 일치·유지 |
| 312 | CP1-139 | B 문서 오기 | [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) CP1-139 | 정정 완료 |
| 313 | CP2-004 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-004 | 정정 완료 |
| 314 | CP2-046 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-046 | 정정 완료 |
| 315 | CP2-049 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-049 | 원문 일치·유지 |
| 316 | CP2-050 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-050 | 원문 일치·유지 |
| 317 | CP2-059 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-059 | 원문 일치·유지 |
| 318 | CP2-082 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-082 | 보완 완료 |
| 319 | CP2-084 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-084 | 원문 일치·유지 |
| 320 | CP2-086 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-086 | 원문 일치·유지 |
| 321 | CP2-087 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-087 | 원문 일치·유지 |
| 322 | CP2-088 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-088 | 원문 일치·유지 |
| 323 | CP2-090 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-090 | 보완 완료 |
| 324 | CP2-091 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-091 | 정정 완료 |
| 325 | CP2-094 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-094 | 원문 일치·유지 |
| 326 | CP2-097 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-097 | 원문 일치·유지 |
| 327 | CP2-098 | A 판 차이 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-098 | 원문 일치·유지 |
| 328 | CP2-127 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-127 | 보완 완료 |
| 329 | CP2-136 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-136 | 원문 일치·유지 |
| 330 | CP2-140 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-140 | 원문 일치·유지 |
| 331 | CP2-145 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-145 | 보완 완료 |
| 332 | CP2-146 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-146 | 원문 일치·유지 |
| 333 | CP2-148 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-148 | 보완 완료 |
| 334 | CP2-149 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-149 | 보완 완료 |
| 335 | CP2-150 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-150 | 원문 일치·유지 |
| 336 | CP2-151 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-151 | 원문 일치·유지 |
| 337 | CP2-152 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-152 | 보완 완료 |
| 338 | CP2-159 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-159 | 원문 일치·유지 |
| 339 | CP2-160 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-160 | 원문 일치·유지 |
| 340 | CP2-162 | C 문서 누락 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-162 | 원문 일치·유지 |
| 341 | CP2-173 | B 문서 오기 | [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) CP2-173 | 원문 일치·유지 |

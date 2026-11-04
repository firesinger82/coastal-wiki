# Celeris 노트 전수 대조 — 작업 4

- 대상: `models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md`.
- 최초 파일은 341줄이다. 순서대로 114줄·114줄·113줄로 나눈 첫 번째 몫인 1–114줄을 대조한다.
- frontmatter·빈 줄·표 머리글을 포함한다. 마지막 대상 행은 최초 114줄의 행 ID로 고정한다.
- 상태: 완료. 최초 1–114줄의 대조를 마쳤다. 마지막 대상은 `docs-architecture:CD1-1088`이다.
- 기계 확인 후보: 사용자 제공 후보 없음.

## 대조 결과

- 대조한 줄 수는 114줄이다. frontmatter·안내·빈 줄·표 머리글은 26줄이다. 차이 표는 88행이다. 이 수는 최초 파일의 1–114줄에서 셌다.
- 정정은 2줄이다. 보완은 1줄이다. 이 수는 담당 범위의 정정·보완 표식을 세었다.
- 차이 표의 최종 분류는 A 2행, B 14행, C 72행이다. 88행 모두 `Celeris-final-conclusions.tsv`의 분류와 일치한다.
- 결론 문장은 연결된 conclusion-verify의 같은 행과 일치한다. RF-018의 문장 앞에는 논문 판을 명시한 구절만 더 있다. 이 구절은 Tavakkol 2017 p.1·p.6과 일치한다.
- 수정 후 경로·줄 번호 인용은 중복 포함 2,142개다. 그 바로 뒤의 원문 인용은 1,619개다. 두 수는 담당 114줄의 백틱 구간을 파싱해 셌다. 지정한 현재·이전 판의 해당 줄을 열어 대조했다. 문자열 불일치는 0개다. 표의 이스케이프된 세로줄과 인용 양끝 공백은 표시 형식으로 처리했다.
- 결론 칸의 코드 식·조건도 같은 행이 인용한 원문과 대조했다. 부호·수량·조건의 불일치는 0개다.
- 경로만 제시한 인용도 해당 원문을 열었다. 호출 순서·입력 조건·파생값·경계 시계열 검사·출력 시간·HTML 속성을 결론과 대조했다.
- 현재 원문 28개 파일과 이전 판 11개 파일·커밋 조합을 열었다. 이 수는 인용 파일과 커밋을 묶어 중복을 제거한 값이다.
- Tavakkol 2017 p.1·p.3·p.6의 지정 쪽 이미지를 열었다. p.3 식 (15)·(18)의 AB3·AM4 계수를 확인했다. p.6의 formatted ASCII 출력 문장을 확인했다.
- A 행 RF-018·RF-025는 `Celeris-version-verify-AD2.md`와 `Celeris-conclusion-verify-CP3RF.md`를 대조했다. `cf9de63`의 이진 Blob 출력과 `bb99fee`의 장치 한도 요청을 해당 커밋 원문으로 확인했다. 반영 전 노트의 날짜와 장치 요청은 `d8157c80` 원문으로 확인했다.
- `Celeris-notes-apply-3.md`·`Celeris-notes-apply-4.md`의 반영 기록을 확인했다. 담당 부분은 새 차이 표다. 기존 본문 삭제·교체를 이 파일에 요구한 수정안은 없다. RF 행은 `Celeris-callflow.md` §6의 수정안과 대조했다.
- 담당 범위의 서로 다른 상대 링크 8개는 모두 실제 대상에 연결된다. 금지 절대 경로·홈 약식 경로·이중 대괄호·사용자가 지정한 한계 문장은 없다. E 행과 mermaid 블록도 없다.
- 문서 원문 칸의 백틱은 실제 문서 원문이다. 한국어 설명을 원문 인용처럼 쓴 항목은 없다.
- 노트 수정은 줄 수를 바꾸지 않았다. 수정 직전에 해당 줄을 다시 읽었다. 담당 밖의 줄은 편집하지 않았다.
- 미해결 항목은 없다.

## 정정 목록

노트 경로는 모두 `models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md`이다. 줄 번호는 최초 파일과 수정 후 파일에서 같다.

1. **12줄 — 정정.** 전: `source_scope: Celeris-WebGPU/docs, Celeris-WebGPU/js, Celeris-WebGPU/shaders`. 후: docs·js·shaders에 scripts·HTML·README.md·ARCHITECTURE.md·transect_version·이전 코드 판·반영 전 노트 판을 명시했다. 근거: 담당 33줄은 `README.md:23`과 `scripts/load_WebGPUCeleris_output.m:14`의 `nt = 496;`을 인용한다. 담당 84–114줄은 HTML 입력 요소를 인용한다. 담당 29–32줄은 반영 전 `d8157c80` 노트를 인용한다. 기존 범위 필드는 이 출처들을 빠뜨렸다. 표식은 YAML 주석으로 붙였다.
2. **35줄, CD1-105 — 정정.** 전: 항목명이 `.`이다. 후: 항목명을 `config.json 병합 순서`로 고쳤다. 근거: `ARCHITECTURE.md:28`의 원문은 ``2. Merge an example or user-provided `config.json`.``이다. 최종 근거 `Celeris-conclusion-verify-CD1a.md`의 CD1-105도 설정 병합 순서를 판정한다. 결론 칸 끝에 정정 표식을 붙였다.
3. **82줄, CD1-958 — 보완.** 전: 외란 초기화 설명에 연결된 코드는 시계열 초기화 처리부 `js/main.js:3475–3518`이다. 후: 외란 버튼이 초기화를 요청하는 `js/main.js:5174`와 `js/main.js:5175` 인용을 코드 칸에 더했다. 원문은 각각 `calc_constants.add_Disturbance = 1;`과 `calc_constants.chartDataUpdate = 1;`이다. `js/main.js:5173–5176`은 두 대입을 같은 외란 버튼 콜백에서 수행한다. 기존 결론 문장은 유지했다. 결론 칸 끝에 보완 표식을 붙였다.

## 기계 확인 후보 판정

- 사용자 제공 후보: 없음.
- 자체 경로·인용 문자열 검사: 최초 인용 1,617개와 수정 후 인용 1,619개 모두 해당 원문에 일치한다. 불일치 후보는 0개다.
- RF-018의 결론 문자열 차이: 논문 판을 명시한 구절이다. p.1·p.6 이미지와 일치하므로 유지했다.
- HTML의 `Oyser` 식별자: `designcomponent_Fric_Oyser-input`은 HTML과 `js/main.js:4718`에 같은 철자로 존재한다. 노트 오기가 아니므로 유지했다.

## 줄별 대조 원장

| 대상 줄 | 대조 내용 | 결과 |
|---|---|---|
| 1–15 | frontmatter의 모델·제목·작성·검증 정보·출처 범위·레이어를 반영 기록과 인용 대상에 대조 | 12줄 출처 범위 정정. 나머지 유지. |
| 16, 18, 20, 22, 24 | 빈 줄 | 유지. |
| 17 | 관련 인프라 노트 상대 링크 | 대상 파일 존재. |
| 19 | 차이 표 절 제목과 날짜 | 반영 기록과 일치. |
| 21 | 코드·문서 판과 논문 목록 | CP3RF의 판독 기준 및 notes-apply-4의 21줄 수정 기록과 일치. |
| 23 | 현재 코드 기준 경로와 이전 코드·노트 판 인용 규칙 | 실제 인용 경로·커밋과 일치. |
| 25–26 | 표 머리글과 구분선 | 6칸 표 구조와 일치. |
| 27 | callflow:RF-002 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 28 | callflow:RF-003 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 29 | callflow:RF-007 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 30 | callflow:RF-011 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 31 | callflow:RF-018 (A 판 차이) | 분류·결론·인용·조건 일치. |
| 32 | callflow:RF-025 (A 판 차이) | 분류·결론·인용·조건 일치. |
| 33 | docs-architecture:CD1-027 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 34 | docs-architecture:CD1-104 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 35 | docs-architecture:CD1-105 (B 문서 오기) | 분류·결론·인용·조건 일치. 항목명 정정. |
| 36 | docs-architecture:CD1-106 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 37 | docs-architecture:CD1-107 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 38 | docs-architecture:CD1-108 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 39 | docs-architecture:CD1-109 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 40 | docs-architecture:CD1-116 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 41 | docs-architecture:CD1-117 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 42 | docs-architecture:CD1-341 (B 문서 오기) | 분류·결론·인용·조건 일치. |
| 43 | docs-architecture:CD1-841 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 44 | docs-architecture:CD1-842 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 45 | docs-architecture:CD1-843 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 46 | docs-architecture:CD1-845 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 47 | docs-architecture:CD1-847 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 48 | docs-architecture:CD1-848 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 49 | docs-architecture:CD1-869 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 50 | docs-architecture:CD1-870 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 51 | docs-architecture:CD1-871 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 52 | docs-architecture:CD1-872 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 53 | docs-architecture:CD1-873 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 54 | docs-architecture:CD1-874 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 55 | docs-architecture:CD1-875 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 56 | docs-architecture:CD1-876 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 57 | docs-architecture:CD1-879 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 58 | docs-architecture:CD1-880 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 59 | docs-architecture:CD1-881 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 60 | docs-architecture:CD1-882 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 61 | docs-architecture:CD1-883 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 62 | docs-architecture:CD1-884 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 63 | docs-architecture:CD1-885 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 64 | docs-architecture:CD1-888 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 65 | docs-architecture:CD1-889 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 66 | docs-architecture:CD1-905 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 67 | docs-architecture:CD1-906 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 68 | docs-architecture:CD1-907 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 69 | docs-architecture:CD1-908 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 70 | docs-architecture:CD1-909 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 71 | docs-architecture:CD1-910 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 72 | docs-architecture:CD1-911 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 73 | docs-architecture:CD1-917 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 74 | docs-architecture:CD1-918 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 75 | docs-architecture:CD1-919 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 76 | docs-architecture:CD1-920 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 77 | docs-architecture:CD1-953 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 78 | docs-architecture:CD1-954 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 79 | docs-architecture:CD1-955 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 80 | docs-architecture:CD1-956 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 81 | docs-architecture:CD1-957 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 82 | docs-architecture:CD1-958 (C 문서 누락) | 분류·결론·인용·조건 일치. 외란 콜백 인용 보완. |
| 83 | docs-architecture:CD1-959 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 84 | docs-architecture:CD1-965 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 85 | docs-architecture:CD1-966 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 86 | docs-architecture:CD1-967 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 87 | docs-architecture:CD1-968 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 88 | docs-architecture:CD1-969 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 89 | docs-architecture:CD1-970 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 90 | docs-architecture:CD1-971 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 91 | docs-architecture:CD1-972 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 92 | docs-architecture:CD1-973 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 93 | docs-architecture:CD1-974 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 94 | docs-architecture:CD1-1067 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 95 | docs-architecture:CD1-1069 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 96 | docs-architecture:CD1-1070 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 97 | docs-architecture:CD1-1071 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 98 | docs-architecture:CD1-1072 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 99 | docs-architecture:CD1-1073 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 100 | docs-architecture:CD1-1074 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 101 | docs-architecture:CD1-1075 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 102 | docs-architecture:CD1-1076 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 103 | docs-architecture:CD1-1077 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 104 | docs-architecture:CD1-1078 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 105 | docs-architecture:CD1-1079 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 106 | docs-architecture:CD1-1080 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 107 | docs-architecture:CD1-1081 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 108 | docs-architecture:CD1-1082 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 109 | docs-architecture:CD1-1083 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 110 | docs-architecture:CD1-1084 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 111 | docs-architecture:CD1-1085 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 112 | docs-architecture:CD1-1086 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 113 | docs-architecture:CD1-1087 (C 문서 누락) | 분류·결론·인용·조건 일치. |
| 114 | docs-architecture:CD1-1088 (C 문서 누락) | 분류·결론·인용·조건 일치. |

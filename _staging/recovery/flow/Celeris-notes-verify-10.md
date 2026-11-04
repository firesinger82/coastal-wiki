# Celeris 노트 전수 대조 10

- 대상: `models/Celeris/source-analysis/celeris-breaking-boundary.md`.
- 상태: 완료.
- 대상 확정: 작업 시작 시 `git diff -U0 HEAD -- models/Celeris/source-analysis/celeris-breaking-boundary.md`의 추가 줄 141개이다.
- 대상 줄: 5–6, 15, 23–24, 27, 69–71, 82–83, 124–127, 148, 155–156, 210, 222–224, 227–345.
- frontmatter와 빈 줄도 대상 수에 포함한다.
- 쓰기 범위는 대상 노트와 이 기록이다.

## 대조 결과

대상 노트의 시작 시점 추가·수정 줄 141개를 모두 대조했다. 이 수는 위에 기록한 `git diff -U0 HEAD`의 추가 줄을 센 값이다. 정정은 69개 줄이다. 인용 보완은 2개 줄이다. 정정·보완 수는 대상 노트의 `[11-04 전수 검증 정정]`·`[11-04 전수 검증 보완]` 표식을 각각 센 값이다. 줄을 추가하거나 삭제하지 않았으므로 아래 줄 번호는 작업 전후에 같다.

차이 표 108개 행의 ID·분류·최종 근거 파일을 `Celeris-note-job-7.tsv`와 `Celeris-final-conclusions.tsv`에 대조했다. 결론 문장을 각 `Celeris-conclusion-verify-*.md` 행과 대조했다. 수식의 표시 구분자와 A 행에 덧붙인 문서 판 설명을 제외하면 결론 문장은 같다. 최종 분류는 A 17개, B 9개, C 78개, E 2개, F 2개이다. 이 수는 대상 노트의 108개 표 행에서 셌다. 이번 검증은 최종 분류와 결론 문장을 바꾸지 않았다.

코드·문서의 인용 범위를 실제 파일에서 열었다. 이전 판의 인용 범위는 지정한 저장소의 `git show`로 열었다. 현재 관련 코드·문서와 `ebca435`의 읽기 전용 diff에는 차이가 없었다. 표에서 경로·줄 뒤에 바로 붙은 인용문 1,201개를 원문 범위와 다시 비교했다. 불일치는 0개이다. 이 비교는 Markdown 표의 `\|` 이스케이프와 인용 양끝의 표시용 공백을 해제했다. 범위 인용 뒤의 연속 코드 조각과 인용 없는 경로·줄의 주장도 해당 원문 및 최종 근거와 대조했다.

논문은 쪽 이미지로 확인했다. Tavakkol 2017은 PDF p.3–6·8의 건습 설명, 식 (25)–(36), Fig.2, 직접 쇄파 부재를 대조했다. Tavakkol 2020은 PDF p.3–4의 경계 목록, 식 (4)·(9), 파속 근사를 대조했다. Lynett 2026은 PDF p.1·3–6의 게재일, 쇄파 설명, 입력·UI 설명을 대조했다. Fotia 학위논문은 로컬 PDF의 p.45–46을 메모리에서 이미지로 렌더했다. 인쇄 p.29–30의 식 (2.26)–(2.28)과 1.2·0.65·0.15·5를 확인했다. CP3-017은 2차 문헌 근거라는 구분을 유지했다.

판 근거는 `Celeris-version-verify-AD1.md`·`AD2.md`와 해당 코드 커밋을 대조했다. CP1-147의 B와 CD1-1400의 A는 각 최종 결론 파일의 판정을 그대로 유지했다. 두 행 모두 현재 값이 5라는 원문과 일치한다. E 행인 CD1-1303·CP2-155는 `Celeris-version-verify-E1.md`와 대조했다. 두 행의 강도는 중간이다. 두 행 모두 해당 경계 설정에서 호출되는 경로이다. 호출되지 않는 경로로 바꿀 근거는 없다.

본문 수정은 각 비교 보고서의 「4 노트 대조와 수정안」과 `Celeris-callflow.md`의 「6 기존 노트 대조와 수정안」·「Claude 렌더 확인 (11-04)」에 대조했다. 본문의 삭제·교체는 쇄파 순서, 도함수 생산자, 무차원 계수, transient 파 수와 종료 함수, near-dry 소비자에 대한 수정안과 일치한다. transect 비교는 CT1-361의 수정안과 일치한다.

노트 전체의 상대 링크 113개는 실제 파일을 가리킨다. 이 수는 Markdown 링크를 센 값이다. 절대 경로, `~/`, 위키 링크 구문, 지정한 한계 문장은 없다. Mermaid 블록은 없다. 모델 실행과 git 쓰기 명령은 사용하지 않았다. 이 작업에서 수정한 파일은 대상 노트와 이 기록이다. 미해결 항목은 없다.

### 본문·형식 줄 대조

| 대상 줄 | 대조 근거와 결과 |
|---|---|
| 5–6 | Celeris-notes-apply-7.md의 frontmatter 반영 기록과 같다. 기존 판독 이력을 유지한다. |
| 15 | main.js:2649,2652–2654,2679의 호출 순서와 같다. 임시 출력 복사는 main.js:2536–2537,2654,2696–2697,2732에서 확인했다. |
| 23 | 366ee34:js/constants_load_calc.js:41–45와 Tavakkol 2017 p.4·8의 판 구분이 같다. |
| 27 | Pass_Breaking.wgsl:55와 Pass3_Bous.wgsl:427의 읽기·쓰기와 같다. |
| 69 | Pass_Breaking.wgsl:93–125에서 h·수면변화율과 dx·dy/dt의 차원이 같다. CP3-113의 무차원 판정과 같다. |
| 71 | CT1-361과 두 판의 점성 상한이 같다. 쇄파 나이의 x 방향 전달 근거를 보완했다. |
| 82 | Pass3_NLSW.wgsl:269·273의 거품 표시와 Pass3_Bous.wgsl:343–364,392의 두 조건을 확인했다. |
| 124,126 | Tavakkol 2020 p.4 식 (9), BoundaryPass.wgsl:104–125, main.js:2694,2729와 같다. E의 중간 강도와 활성 경로를 유지했다. |
| 148 | bb99fee 이전·이후의 BoundaryPass와 현재 175–180행이 파 수 변경 및 선형 종료 함수를 뒷받침한다. |
| 155 | BoundaryPass.wgsl:133–151,448–460과 UI 높이 라벨을 대조했다. CD1-1303의 중간 강도와 같다. |
| 210 | 성분 합산의 수심 조건, 텍스처 데이터 갱신, TMA 성분 캐시를 구분하여 정정했다. |
| 222 | Pass3_Bous.wgsl:159,192, Update_TriDiag_coef.wgsl:34,42, Pass1.wgsl:97–118이 소비자 구분을 뒷받침한다. |
| 224 | BoundaryPass.wgsl:657–720의 독립 건습 판정에 직접 인용을 보완했다. |
| 228,230,232,234,236–237 | 제목·판·경로 기준·표 머리글을 확인했다. ebca435의 날짜는 2026-07-20이다. 234행은 원문과 분석 표제를 구분하도록 정정했다. |
| 24,70,83,125,127,156,223,227,229,231,233,235 | 빈 줄 12개이다. 문장·인용·링크가 없음을 확인했다. |

### 차이 표 줄 대조

아래 각 행은 노트의 문서 원문·코드 원문·결론·판·조건·인용을 함께 대조한 결과이다. 최종 근거 파일의 짧은 이름은 `Celeris-conclusion-verify-` 뒤의 이름이다.

| 노트 줄 | 행 ID | 최종 분류 | 최종 근거 | 처리 |
|---|---|---|---|---|
| 238 | callflow:RF-020 | B 문서 오기 | [CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) | 정정 |
| 239 | docs-architecture:CD1-158 | B 문서 오기 | [CD1a.md](../compare/Celeris-conclusion-verify-CD1a.md) | 일치 |
| 240 | docs-architecture:CD1-856 | C 문서 누락 | [CD1e.md](../compare/Celeris-conclusion-verify-CD1e.md) | 정정 |
| 241 | docs-architecture:CD1-857 | C 문서 누락 | [CD1e.md](../compare/Celeris-conclusion-verify-CD1e.md) | 정정 |
| 242 | docs-architecture:CD1-860 | C 문서 누락 | [CD1e.md](../compare/Celeris-conclusion-verify-CD1e.md) | 정정 |
| 243 | docs-architecture:CD1-861 | C 문서 누락 | [CD1e.md](../compare/Celeris-conclusion-verify-CD1e.md) | 정정 |
| 244 | docs-architecture:CD1-862 | C 문서 누락 | [CD1e.md](../compare/Celeris-conclusion-verify-CD1e.md) | 정정 |
| 245 | docs-architecture:CD1-863 | C 문서 누락 | [CD1e.md](../compare/Celeris-conclusion-verify-CD1e.md) | 정정 |
| 246 | docs-architecture:CD1-912 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 247 | docs-architecture:CD1-913 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 248 | docs-architecture:CD1-914 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 249 | docs-architecture:CD1-915 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 250 | docs-architecture:CD1-916 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 251 | docs-architecture:CD1-922 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 252 | docs-architecture:CD1-923 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 253 | docs-architecture:CD1-924 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 254 | docs-architecture:CD1-937 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 255 | docs-architecture:CD1-938 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 256 | docs-architecture:CD1-939 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 257 | docs-architecture:CD1-940 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 258 | docs-architecture:CD1-941 | A 판 차이 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 259 | docs-architecture:CD1-942 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 260 | docs-architecture:CD1-943 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 261 | docs-architecture:CD1-948 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 262 | docs-architecture:CD1-950 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 263 | docs-architecture:CD1-951 | C 문서 누락 | [CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 정정 |
| 264 | docs-architecture:CD1-1108 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 265 | docs-architecture:CD1-1109 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 266 | docs-architecture:CD1-1110 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 267 | docs-architecture:CD1-1111 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 268 | docs-architecture:CD1-1112 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 269 | docs-architecture:CD1-1113 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 270 | docs-architecture:CD1-1114 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 271 | docs-architecture:CD1-1115 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 272 | docs-architecture:CD1-1116 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 273 | docs-architecture:CD1-1117 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 274 | docs-architecture:CD1-1118 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 275 | docs-architecture:CD1-1120 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 276 | docs-architecture:CD1-1121 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 277 | docs-architecture:CD1-1122 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 278 | docs-architecture:CD1-1123 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 279 | docs-architecture:CD1-1125 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 280 | docs-architecture:CD1-1126 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 281 | docs-architecture:CD1-1127 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 282 | docs-architecture:CD1-1128 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 283 | docs-architecture:CD1-1130 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 284 | docs-architecture:CD1-1131 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 285 | docs-architecture:CD1-1132 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 286 | docs-architecture:CD1-1133 | C 문서 누락 | [CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 정정 |
| 287 | docs-architecture:CD1-1229 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 288 | docs-architecture:CD1-1230 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 289 | docs-architecture:CD1-1231 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 290 | docs-architecture:CD1-1232 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 291 | docs-architecture:CD1-1233 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 292 | docs-architecture:CD1-1234 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 293 | docs-architecture:CD1-1258 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 294 | docs-architecture:CD1-1259 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 295 | docs-architecture:CD1-1283 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 296 | docs-architecture:CD1-1284 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 297 | docs-architecture:CD1-1285 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 298 | docs-architecture:CD1-1286 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 299 | docs-architecture:CD1-1287 | C 문서 누락 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 300 | docs-architecture:CD1-1303 | E 코드 결함 후보 (중간) | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 정정 |
| 301 | docs-architecture:CD1-1342 | B 문서 오기 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 일치 |
| 302 | docs-architecture:CD1-1400 | A 판 차이 | [CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 일치 |
| 303 | docs-source:CD2-412 | C 문서 누락 | [CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 일치 |
| 304 | docs-source:CD2-415 | C 문서 누락 | [CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 일치 |
| 305 | docs-source:CD2-434 | C 문서 누락 | [CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 일치 |
| 306 | docs-source:CD2-435 | C 문서 누락 | [CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 일치 |
| 307 | docs-source:CD2-436 | C 문서 누락 | [CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 일치 |
| 308 | docs-source:CD2-445 | C 문서 누락 | [CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 일치 |
| 309 | docs-source:CD2-446 | C 문서 누락 | [CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 일치 |
| 310 | docs-source:CD2-447 | C 문서 누락 | [CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 일치 |
| 311 | lynett2026:CP3-016 | B 문서 오기 | [CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) | 일치 |
| 312 | lynett2026:CP3-017 | B 문서 오기 | [CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) | 일치 |
| 313 | lynett2026:CP3-089 | C 문서 누락 | [CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) | 일치 |
| 314 | lynett2026:CP3-097 | C 문서 누락 | [CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) | 일치 |
| 315 | lynett2026:CP3-102 | A 판 차이 | [CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) | 일치 |
| 316 | lynett2026:CP3-113 | B 문서 오기 | [CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) | 일치 |
| 317 | tavakkol2017:CP1-048 | A 판 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 318 | tavakkol2017:CP1-049 | A 판 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 319 | tavakkol2017:CP1-050 | A 판 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 320 | tavakkol2017:CP1-052 | F 표기 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 321 | tavakkol2017:CP1-054 | A 판 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 322 | tavakkol2017:CP1-055 | A 판 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 323 | tavakkol2017:CP1-060 | F 표기 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 324 | tavakkol2017:CP1-061 | A 판 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 325 | tavakkol2017:CP1-073 | A 판 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 326 | tavakkol2017:CP1-074 | A 판 차이 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 정정 |
| 327 | tavakkol2017:CP1-116 | C 문서 누락 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 328 | tavakkol2017:CP1-117 | C 문서 누락 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 329 | tavakkol2017:CP1-124 | C 문서 누락 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 330 | tavakkol2017:CP1-131 | C 문서 누락 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 331 | tavakkol2017:CP1-132 | C 문서 누락 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 332 | tavakkol2017:CP1-147 | B 문서 오기 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 333 | tavakkol2017:CP1-148 | B 문서 오기 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 334 | tavakkol2017:CP1-166 | B 문서 오기 | [CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 일치 |
| 335 | tavakkol2020:CP2-026 | A 판 차이 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 일치 |
| 336 | tavakkol2020:CP2-029 | A 판 차이 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 정정 |
| 337 | tavakkol2020:CP2-034 | A 판 차이 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 정정 |
| 338 | tavakkol2020:CP2-040 | A 판 차이 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 정정 |
| 339 | tavakkol2020:CP2-041 | A 판 차이 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 일치 |
| 340 | tavakkol2020:CP2-131 | C 문서 누락 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 일치 |
| 341 | tavakkol2020:CP2-133 | C 문서 누락 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 일치 |
| 342 | tavakkol2020:CP2-135 | C 문서 누락 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 일치 |
| 343 | tavakkol2020:CP2-137 | C 문서 누락 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 일치 |
| 344 | tavakkol2020:CP2-155 | E 코드 결함 후보 (중간) | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 정정 |
| 345 | tavakkol2020:CP2-170 | A 판 차이 | [CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 일치 |

## 정정·보완 목록

위치는 모두 `models/Celeris/source-analysis/celeris-breaking-boundary.md`의 줄 번호이다. 변경 전·후 칸은 바뀐 부분을 적었다. 정정·보완 표식은 본문 줄 끝 또는 표의 결론 문장 칸 끝에 붙였다.

| 노트:줄 | 종류 | 변경 전 | 변경 후 | 근거 원문 |
|---|---|---|---|---|
| celeris-breaking-boundary.md:71 | 보완 | transect 판은 x 방향 쇄파 나이와 응력만 전달한다. | transect 판은 x 방향 쇄파 나이와 응력만 전달한다(`transect_version/shaders/Pass_Breaking.wgsl:58–85,137–148`). | transect_version/shaders/Pass_Breaking.wgsl:85의 `t_here = max(t_here, t1);`과 144행의 `let nu_flux = vec4<f32>(nu_dPdx, 0.0, 0.0, 0.0);`. CT1-361 수정안과 일치한다. |
| celeris-breaking-boundary.md:210 | 정정 | BoundaryPass는 매 스텝 `txWaves`의 `numberOfWaves` 행을 합산(`BoundaryPass.wgsl:197-200`)하므로, JS는 파라미터 변경 시에만 텍스처를 재생성(TMA 결과 캐시, `:22-23,59-72`). transient는 셰이더 `sineWave`에서 파 수 5와 선형 종료 포락선으로 처리한다(`shaders/BoundaryPass.wgsl:175–180`). [11-04 대조 정정] | BoundarySineWave는 `if (d_here > 0.0001)`일 때 `txWaves`의 `numberOfWaves`개 성분을 합산한다(`shaders/BoundaryPass.wgsl:189–202`). JS는 초기화와 `if (calc_constants.html_update > 0)` 분기에서 기존 파 텍스처의 데이터를 갱신한다(`js/main.js:329–334,588,2294,2396`). TMA 생성기는 `if (cacheKey == cachedTmaKey && cachedTmaResult)`이면 캐시 결과의 복사본을 반환한다(`js/Wave_Generator.js:62–80`). transient는 셰이더 `sineWave`에서 파 수 5와 선형 종료 포락선으로 처리한다(`shaders/BoundaryPass.wgsl:175–180`). [11-04 대조 정정] | shaders/BoundaryPass.wgsl:196–199의 수심 조건과 성분 합산. js/main.js:329–334의 copyWaveDataToTexture 호출, 588·2396행의 refreshBoundaryWaveTexture 호출. js/Wave_Generator.js:69–70의 캐시 반환. 기존 ‘파라미터 변경 시에만 텍스처 재생성’은 성분 캐시와 텍스처 데이터 갱신을 혼동한다. |
| celeris-breaking-boundary.md:224 | 보완 | BoundaryPass의 cleanup(§2.8)은 .w와 독립적으로 `delta`·이웃 bathy로 매 스텝 wet/dry를 재판정한다 — 두 메커니즘이 별개임에 유의. | BoundaryPass의 cleanup(§2.8)은 지형 `.w` 표지와 독립적으로 `delta`·이웃 bathy로 wet/dry를 재판정한다(`shaders/BoundaryPass.wgsl:657–720`). | shaders/BoundaryPass.wgsl:658–661은 이웃 표고차와 globals.delta로 문턱을 계산한다. 669–673행은 수심과 문턱을 비교한다. CP1-148 수정안이 분리한 두 메커니즘에 직접 근거를 보탰다. |
| celeris-breaking-boundary.md:234 | 정정 | 문서 원문과 코드 원문은 보고서의 인용이다. | 문서 원문·코드 원문 칸은 원문 인용과 보고서 분석 표제를 구분한다. | Celeris-conclusion-verify-CD1f.md 서문은 문서 칸의 ‘대상 8문서’와 한국어 항목명을 분석 표제로 규정한다. |
| celeris-breaking-boundary.md:238 | 정정 | `Pass2/Pass3가 만든 dU_by_dt` | ``Pass2/Pass3가 만든 `dU_by_dt` `` | d8157c80:models/Celeris/source-analysis/celeris-breaking-boundary.md:24의 원문은 ‘Pass2/Pass3가 만든 `dU_by_dt` 텍스처의 x채널에서 읽음.’이다. 인용 안의 백틱을 복원했다. |
| celeris-breaking-boundary.md:240 | 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` delta의 파생식 ` | `docs/architecture/CONFIGURATION.md:89` delta의 파생식(문서에 해당 계산식 없음). | docs/architecture/CONFIGURATION.md:87–101의 89행은 `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``이다. CD1e 해당 행은 구체식 누락으로 판정한다. |
| celeris-breaking-boundary.md:241 | 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` epsilon의 파생식 ` | `docs/architecture/CONFIGURATION.md:89` epsilon의 파생식(문서에 해당 계산식 없음). | docs/architecture/CONFIGURATION.md:87–101의 89행은 `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``이다. CD1e 해당 행은 구체식 누락으로 판정한다. |
| celeris-breaking-boundary.md:242 | 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` boundary_nx의 파생식 ` | `docs/architecture/CONFIGURATION.md:89` boundary_nx의 파생식(문서에 해당 계산식 없음). | docs/architecture/CONFIGURATION.md:87–101의 89행은 `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``이다. CD1e 해당 행은 구체식 누락으로 판정한다. |
| celeris-breaking-boundary.md:243 | 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` boundary_ny의 파생식 ` | `docs/architecture/CONFIGURATION.md:89` boundary_ny의 파생식(문서에 해당 계산식 없음). | docs/architecture/CONFIGURATION.md:87–101의 89행은 `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``이다. CD1e 해당 행은 구체식 누락으로 판정한다. |
| celeris-breaking-boundary.md:244 | 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` reflect_x의 파생식 ` | `docs/architecture/CONFIGURATION.md:89` reflect_x의 파생식(문서에 해당 계산식 없음). | docs/architecture/CONFIGURATION.md:87–101의 89행은 `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``이다. CD1e 해당 행은 구체식 누락으로 판정한다. |
| celeris-breaking-boundary.md:245 | 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` reflect_y의 파생식 ` | `docs/architecture/CONFIGURATION.md:89` reflect_y의 파생식(문서에 해당 계산식 없음). | docs/architecture/CONFIGURATION.md:87–101의 89행은 `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``이다. CD1e 해당 행은 구체식 누락으로 판정한다. |
| celeris-breaking-boundary.md:246 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 파랑 텍스트 레코드 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:247 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` TMA 생성의 고정 계수 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:248 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` TMA 파고 정규화 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:249 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` TMA 절단 기준 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:250 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 주기 경계 방향 적합 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:251 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 경계 시계열 전후 처리 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:252 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 경계 시계열 시간·공간 보간 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:253 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` type-5 좌표의 기준점 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:254 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` NLSW 쇄파와 분산 모드의 차이 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:255 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 쇄파 시작·종료 임계값 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:256 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 쇄파 시각의 이류 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:257 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` Smagorinsky 항 비활성 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:258 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 스펀지 감쇠의 실제 식 `;<br>Tavakkol 2020 p.4 식 (9) `\lambda(\alpha)=\frac{\gamma(\alpha)}{\gamma(\alpha+c\Delta t)}` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제).;<br>Tavakkol 2020 p.4 식 (9) `\lambda(\alpha)=\frac{\gamma(\alpha)}{\gamma(\alpha+c\Delta t)}` | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:259 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 입사파 위치·진입 ramp ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:260 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 습윤 고립 셀과 수로 끝 억제 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:261 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 지표 침투 생성항 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:262 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 초기 바닥의 고립 섬 제거 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:263 | 정정 | ` 대상 8문서:구체식·검사 없음 ` ` GPU near-dry 재계산의 범위 ` | 대상 8문서에 해당 세부식·검사 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1f.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:264 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 2 / *Transient Pulse (4 waves) ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:265 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 3 / *Solitary Wave ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:266 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / -1 / Custom Spectrum from loaded file ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:267 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 5 / *Time Series from loaded file ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:268 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_H-input / value=없음 ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:269 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_T-input / value=없음 ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:270 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_direction-input / value=없음 ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:271 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` west_boundary_type-select / 0 / Solid Wall ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:272 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` west_boundary_type-select / 1 / Sponge Layer ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:273 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` west_boundary_type-select / 2 / Incident Waves ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:274 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` west_boundary_type-select / 3 / *Periodic Boundary ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:275 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` east_boundary_type-select / 0 / Solid Wall ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:276 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` east_boundary_type-select / 1 / Sponge Layer ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:277 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` east_boundary_type-select / 2 / Incident Waves ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:278 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` east_boundary_type-select / 3 / *Periodic Boundary ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:279 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` south_boundary_type-select / 0 / Solid Wall ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:280 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` south_boundary_type-select / 1 / Sponge Layer ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:281 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` south_boundary_type-select / 2 / Incident Waves ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:282 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` south_boundary_type-select / 3 / *Periodic Boundary ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:283 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` north_boundary_type-select / 0 / Solid Wall ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:284 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` north_boundary_type-select / 1 / Sponge Layer ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:285 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` north_boundary_type-select / 2 / Incident Waves ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:286 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` north_boundary_type-select / 3 / *Periodic Boundary ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1g.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:287 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` useBreakingModel-select / 1 / Breaking Eddy Viscosity Model ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:288 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` useBreakingModel-select / 0 / None; numerical dissipation only ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:289 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` dzdt_I_coef-input / value=없음 ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:290 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` dzdt_F_coef-input / value=없음 ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:291 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` T_star_coef-input / value=없음 ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:292 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` delta_breaking-input / value=없음 ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:293 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 0 / *Sine Wave (single harmonic) ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:294 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 1 / *TMA Spectrum ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:295 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 10 / 10-yr Flood ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:296 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 11 / 50-yr Flood ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:297 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 12 / 100-yr Flood ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:298 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 13 / 200-yr Flood ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:299 | 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` incident_wave_type-select / 14 / 500-yr Flood ` | 대상 8문서에 해당 HTML 세부 항목 설명 없음(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 해당 행. CD1f 서문은 ‘대상 8문서’와 한국어 항목명을 보고서 분석 표제로 명시한다. |
| celeris-breaking-boundary.md:300 | 정정 | ` 대상 문서·현재 코드:호출·조건 교차대조 ` ` 입사 고립파 높이 제어 ` | 입사 고립파 높이 제어에 대한 문서·현재 코드의 호출·조건 교차대조(보고서 분석 표제). | Celeris-conclusion-verify-CD1h.md의 CD1-1303 및 index.html:775, shaders/BoundaryPass.wgsl:140,455–459. 해당 칸은 원문 인용이 아닌 교차대조 표제이다. |
| celeris-breaking-boundary.md:326 | 정정 | Tavakkol 2017 p.5 Fig. 2 서 `type="SineWave" seaLevel=0 widthNum=2`, `amplitude=.01 period=2 theta=0`; 동 `type="Sponge" seaLevel=0 widthNum=20`; 남·북 `type="Solid" seaLevel=0 widthNum=2` | Tavakkol 2017 p.5 Fig. 2 서 `type = "SineWave" seaLevel = 0 widthNum = 2`, `amplitude = .01 period = 2 theta = 0`; 동 `type = "Sponge" seaLevel = 0 widthNum = 20`; 남·북 `type = "Solid" seaLevel = 0 widthNum = 2` | Tavakkol 2017 p.5 Fig.2 쪽 이미지의 속성 대입문에는 등호 양쪽 공백이 있다. |
| celeris-breaking-boundary.md:336 | 정정 | `*_boundary_type`, `incident_wave_type` | `west_boundary_type`, `east_boundary_type`, `south_boundary_type`, `north_boundary_type`, `incident_wave_type` | js/constants_load_calc.js:63–68은 네 방향의 구체적인 필드 이름을 선언한다. *_boundary_type은 원문의 식별자가 아니다. |
| celeris-breaking-boundary.md:337 | 정정 | Tavakkol 2020 p.3 식 (4), §1.2 전사. | Tavakkol 2020 p.3 §3.1.1 식 (4). | Tavakkol 2020 p.3 쪽 이미지의 스펀지 절은 §3.1.1이다. §1.2는 대조 보고서 내부의 전사 절이다. |
| celeris-breaking-boundary.md:338 | 정정 | Tavakkol 2020 p.4 식 (9), §1.2 전사. | Tavakkol 2020 p.4 식 (9). | Tavakkol 2020 p.4 쪽 이미지의 식 (9)는 §3.1.1의 연속 내용이다. 대조 보고서의 §1.2 표기를 제거했다. |
| celeris-breaking-boundary.md:344 | 정정 | `BoundaryWidth - boundary_nx - idx.x`, `BoundaryWidth - boundary_ny - idx.y` | `globals.BoundaryWidth - globals.boundary_nx - idx.x`, `globals.BoundaryWidth - globals.boundary_ny - idx.y` | shaders/BoundaryPass.wgsl:111,123의 원문에는 두 항 모두 globals. 접두어가 있다. E1은 기존 보고서 식을 축약 표기라고 설명한다. |

## 기계 확인 후보 판정

- celeris-breaking-boundary.md:240 — `CONFIGURATION.md:89` 뒤의 `delta의 파생식`은 원문이 아니다. 89행은 파생값의 범주를 소개한다. 백틱을 제거하고 문서에 해당 계산식이 없다는 설명으로 정정했다.
- celeris-breaking-boundary.md:241 — `CONFIGURATION.md:89` 뒤의 `epsilon의 파생식`은 원문이 아니다. 89행은 파생값의 범주를 소개한다. 백틱을 제거하고 문서에 해당 계산식이 없다는 설명으로 정정했다.
- celeris-breaking-boundary.md:242 — `CONFIGURATION.md:89` 뒤의 `boundary_nx의 파생식`은 원문이 아니다. 89행은 파생값의 범주를 소개한다. 백틱을 제거하고 문서에 해당 계산식이 없다는 설명으로 정정했다.
- celeris-breaking-boundary.md:243 — `CONFIGURATION.md:89` 뒤의 `boundary_ny의 파생식`은 원문이 아니다. 89행은 파생값의 범주를 소개한다. 백틱을 제거하고 문서에 해당 계산식이 없다는 설명으로 정정했다.
- celeris-breaking-boundary.md:244 — `CONFIGURATION.md:89` 뒤의 `reflect_x의 파생식`은 원문이 아니다. 89행은 파생값의 범주를 소개한다. 백틱을 제거하고 문서에 해당 계산식이 없다는 설명으로 정정했다.
- celeris-breaking-boundary.md:245 — `CONFIGURATION.md:89` 뒤의 `reflect_y의 파생식`은 원문이 아니다. 89행은 파생값의 범주를 소개한다. 백틱을 제거하고 문서에 해당 계산식이 없다는 설명으로 정정했다.

여섯 후보의 공통 원문은 `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``이다. 뒤의 91–97행은 파생값의 범주를 나열한다. 각 실제 대입식은 `js/constants_load_calc.js:501–502,505–508`에 있다. 코드 인용과 최종 C 분류는 일치하므로 유지했다.

## 완료 확인

대상 141개 줄의 대조를 마쳤다. 정정 목록의 71개 위치는 노트의 정정 69개·보완 2개 표식 위치와 같다. 대상 밖의 기존 줄은 바꾸지 않았다. 지정된 기계 확인 후보 6개를 모두 판정했다. 미해결 항목은 없다.

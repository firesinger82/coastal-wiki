# Celeris 노트 대상 줄 전수 검증 14

- 기준일: 2026-11-04.
- 범위: 사용자 지정 노트 6개. 새 파일 2개는 전체 줄. 기존 파일 4개는 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄.
- 대조 기준: 현재 코드 ebca435, 명시된 이전 판, 논문 쪽 이미지, 최종 결론·수정안·반영 기록.
- 집계 단위: 대조 줄 수는 빈 줄과 frontmatter를 포함한다. 정정·보완 수는 이번 작업에서 바꾼 대상 줄 수다.
- 진행 상태: 완료. 지정된 대상 줄을 모두 대조했다.

## 완료: web-refs/celeris-papers-vs-code.md

- 대조: 39줄(1–39, frontmatter·빈 줄 포함). 정정: 1줄. 보완: 3줄.
- 표 13행의 분류와 결론은 final-conclusions.tsv 및 conclusion-verify-CP1·CP2·CP3RF와 일치한다. A 행은 version-verify-AD1·AD2와 최종 결론의 판 기준을 대조했다. VR 행은 중간 D 판정이 아니라 최종 A 판정을 따른다.
- 논문 쪽 이미지: Tavakkol 2017 p.1–3·7–11, Tavakkol 2020 p.1–2·11–13, Lynett 2026 p.1·4·6. 식 (37)의 부호·구간, h/d 기호, Fig.15의 0.018/0.18, 그림 번호와 표식을 확인했다.
- 코드: README:25·82, MouseClickChange:86–100, AddDisturbance:182–239, Pass3_Bous:117–123, constants_load_calc:27, main:507·2624·4258–4262. 이전 판 69827ba:README:82 및 d778fe7:MouseClickChange:86–100도 열었다. 배 압력·VR 관련 소스 검색 결과를 최종 근거 기록과 대조했다.
- frontmatter의 제목·범위·작성일·작성자·반영 방법은 notes-apply-10과 note-job-10에 부합한다. 본문은 원문과 AI 정리를 구별한다. Mermaid·E 행·금지된 한계 문장은 없다.

정정·보완 목록:

- models/Celeris/web-refs/celeris-papers-vs-code.md:29 — 전: 단일 백틱 안에 역슬래시로 감싼 LICENSE. 후: 이중 백틱 안에 원문의 단일 백틱 LICENSE. 근거: 현재 README.md:82와 69827ba:README.md:82의 원문은 ``This project is licensed under the **MIT License**. See the `LICENSE` file for details.``이다. 결론 칸에 정정 표식을 붙였다.
- models/Celeris/web-refs/celeris-papers-vs-code.md:36 — 전: `5절 검색 D1.`. 후: 2020 대조 보고서 §5.2 검색 D1의 상대 링크. 근거: celeris-tavakkol2020-vs-code.md:1131의 D1 검색 기록. 결론 칸에 보완 표식을 붙였다.
- models/Celeris/web-refs/celeris-papers-vs-code.md:37 — 전: `검색 D1.`. 후: 같은 보고서의 상대 링크. 근거: 같은 D1 기록의 CP2-101 대상 지정. 결론 칸에 보완 표식을 붙였다.
- models/Celeris/web-refs/celeris-papers-vs-code.md:38 — 전: `검색 D1.`. 후: 같은 보고서의 상대 링크. 근거: 같은 D1 기록의 CP2-104 대상 지정 및 main.js:4259의 마우스 분기. 결론 칸에 보완 표식을 붙였다.

기계 확인 후보 판정:

- README.md:82의 `This project is licensed under the **MIT License**. See the \` 후보 — 실제 인용 오류. Markdown 코드 구간 안의 역슬래시는 백틱을 이스케이프하지 않는다. 원문에 없는 역슬래시를 제거하고 이중 백틱으로 고쳤다. 라이선스 결론은 유지했다.

## 완료: source-analysis/celeris-coulwave.md

- 대조: 32줄(5·9·15–16·27·66·70·72·79·167–189). 정정: 2줄. 보완: 0줄.
- 표 13행의 분류·결론을 final-conclusions.tsv와 conclusion-verify-CP1·CP2·CP3RF·CD1f·CD1h·CD2에 대조했다. E 행과 A 행은 없다.
- 모든 파일:줄 인용을 현재 원문과 대조했다. d8157c80의 이전 노트, 67ca57c·984091f·f6fd78b의 지정 줄도 열었다. 문서의 누락 설명과 원문 인용을 구분했다. 코드 인용의 들여쓰기와 표의 파이프 이스케이프는 표시 형식 차이이다.
- 15행은 Tavakkol 2020 p.2–3 이미지 및 CP2-171 수정안과 같다. 27행은 CP1-154·CP3-114·RF-020 수정안과 같다. 66행의 저장 시점은 CD2-470 수정안과 같다. 70·72·79행은 RF-026의 실제 복사원과 같다.
- Tavakkol 2017 p.2–3 및 Lynett 2026 p.3–5 이미지를 열어 모드와 구현 상세의 문서 범위를 대조했다. 총수심 하한·평가 고도·경계 조건·양방향 계수 부호를 원문으로 확인했다. frontmatter의 반영일·범위는 notes-apply-10과 같다. Mermaid·금지된 한계 문장은 없다.

정정 목록:

- models/Celeris/source-analysis/celeris-coulwave.md:66 — 전: `:191–195` 뒤의 축약식 `EzST = E*(eta*S+T)` 등과 `E = dU_by_dt.x`. 후: Pass3B_COULWAVE.wgsl:192–195의 실제 WGSL 대입식 네 개와 :191의 `let E = textureLoad(dU_by_dt, idx, 0).x;`. 근거: 같은 파일의 해당 줄. 저장 시점 결론은 유지했다. 축약식을 원문 인용으로 오인하지 않도록 원문으로 교체했다.
- models/Celeris/source-analysis/celeris-coulwave.md:188 — 전: `shaders/Pass1.wgsl:128–176`. 후: `shaders/Pass1.wgsl:128–171`. 근거: 원본은 172줄이며 함수의 닫는 중괄호는 171행이다. 173–176행은 없다. 최종 근거 파일에서 이어진 범위 오류를 고쳤다. 결론 칸에 정정 표식을 붙였다.
- 기계 확인 후보: 사용자 지정 후보 없음. 자체 검사에서 발견한 파일 끝 초과 인용은 위 188행 정정으로 해소했다.

## 완료: manual-notes/celeris-docs-source-differences.md

- 대조: 26줄(1–26, frontmatter·빈 줄 포함). 정정: 0줄. 보완: 0줄.
- CD2-441·448의 분류·결론·근거는 final-conclusions.tsv 및 conclusion-verify-CD2와 일치한다. note-job-10과 notes-apply-10의 새 노트 배정도 같다.
- 문서 원문: docs/source/shaders/Pass3_NLSW_Spherical_wgsl.md:28–31 및 AddDisturbance_wgsl.md:16–28. 코드 원문: Pass3_NLSW_Spherical.wgsl:205–230, AddDisturbance.wgsl:106–158, main.js:2738–2745. 표시된 인용 63개를 해당 줄에서 대조했다.
- Coriolis 두 운동량 항의 부호를 확인했다. 시간 상한 조건의 `>`와 초기 변화율 억제 조건의 `<`를 확인했다. 이동량의 tanh 식과 시간 단위 dt를 확인했다. C 판정은 문서의 해당 식·조건 누락을 뜻한다.
- frontmatter의 제목·소스 범위·날짜·작성자·반영 방법은 반영 기록과 같다. 표의 문서 칸은 실제 원문이다. Mermaid·A/E 행·금지된 한계 문장은 없다.
- 정정 목록 없음. 기계 확인 후보 없음.

## 완료: web-refs/celeris-coulwave-theory.md

- 대조: 21줄(7–8·42–45·120–122·146–157). 정정: 2줄. 보완: 0줄.
- RF-022·CD2-479의 C 분류와 결론은 conclusion-verify-CP3RF·CD2 및 final-conclusions.tsv와 같다. A/E 행은 없다.
- constants_load_calc.js:36–39, main.js:1540–1571·2662–2685·2795–2815, Pass3A_COULWAVE.wgsl:44, Pass3B_COULWAVE.wgsl:170–200, Pass3_COULWAVE.wgsl:486–488·520–522, Pass3_Bous.wgsl:142–149·181–193을 열었다. 반영 전 노트 d8157c80:116도 열었다.
- 42행은 CD1-1355·1356의 수정안과 같다. 44행은 CP1-158·CP2-178의 수정안과 같다. 121–122행은 CD2-478·479와 RF-022의 수정안에 부합한다. Tavakkol 2020 p.3 식 (2)–(3)을 이미지로 대조했다. 외부 식과의 동일성을 확정하지 않는 문장은 최종 CD2-444의 판정 기준이다. 미완료 작업을 선언하는 문장이 아니다.
- frontmatter의 반영일·방법은 notes-apply-10과 같다. Mermaid는 없다. 남아 있던 과거의 추적 요구는 아래 두 행에서 원문 발췌와 누락 내용의 요약으로 바꿨다.

정정 목록:

- models/Celeris/web-refs/celeris-coulwave-theory.md:156 — 전: `dU_by_dt 생성처 추적 필요.`를 원문처럼 인용. 후: 반영 전 원문의 `` `E = textureLoad(dU_by_dt).x` (`Pass3B:191`) ``만 정확히 발췌하고, 생산처 설명 누락을 원문 요약으로 표시. 근거: d8157c80의 116행은 dU_by_dt 자체를 백틱으로 감싸므로 종전 인용은 원문 글자와 다르다. 결론 칸에 정정 표식을 붙였다.
- models/Celeris/web-refs/celeris-coulwave-theory.md:157 — 전: 반영 전 116행 전체에 포함된 `생성처 추적 필요` 요구를 재수록. 후: 같은 원문 항목의 발췌와 생산처 설명 누락의 요약. 근거: d8157c80:116, Pass3_COULWAVE.wgsl:488·521, 최종 CD2-479. 기존 전체 인용 자체는 정확했다. 사용자 지시 7에 따라 과거의 미완료 요구가 현재 노트에 남지 않도록 정리했다. 결론은 유지했다.
- 자체 기계 후보 판정: 156행은 실제 글자 불일치다. 원문 요약과 실제 발췌를 구분하여 해소했다.

## 완료: web-refs/celeris-lynett-2026.md

- 대조: 28줄(7·14·19·53–54·60·68·70–90). 정정: 0줄. 보완: 0줄.
- 표 9행의 분류·결론을 conclusion-verify-CP1·CP2·CP3RF·CD1h와 대조했다. CP3-003에서 삭제한 한계 문장은 이번 사용자 지시와 notes-apply-10의 반영 방침에 부합한다. A 행 CP3-005는 version-verify-AD2의 이전 구현 판과 같다. E 행은 없다.
- 현재 main.js:1540–1571 및 constants_load_calc.js:36–39를 열었다. 재구성 선택 조건은 main.js:1539도 함께 확인했다. fd57bb7:main.js:32–40과 d8157c80의 지정 노트 줄을 열었다. 인용 문구와 각 경로의 역할이 맞는다.
- Lynett 2026 p.1–5·7–8·10·12의 이미지에서 모드 명칭, 차분 차수, 언어, Fig.3(d)의 067071/061071, 성능 조건의 쪽을 대조했다. Tavakkol 2017 p.1–2와 Tavakkol 2020 p.1–2에서 플랫폼을 대조했다. 쪽별 판독 기록과도 일치한다.
- 19·53–54·60·68·72행은 보고서 §4의 CP3-003·036·054·065·077, CP3-001·002·079, CP3-111, CP1-152, CP2-177, CD1-1357·1358 수정안에 부합한다. frontmatter의 첫 쪽 추출 설명과 후속 대조 반영 설명을 구분했다.
- Mermaid·금지된 한계 문장은 없다. 정정 목록 없음. 기계 확인 후보 없음.

## 완료: web-refs/celeris-official-resources.md

- 대조: 23줄(7–8·17·32–33·35·47–63). 정정: 0줄. 보완: 0줄.
- 표 7행의 분류·결론을 conclusion-verify-CD1c·CD1h·CP1·CP2와 대조했다. A 행의 이전 구현 판과 저장소 이력 설명은 최종 근거와 같다. CP2-007은 version-verify-AD1과도 같다. E 행은 없다.
- README.md:25, REFERENCE_PAPERS.md:18·29, ARCHITECTURE.md:3, main.js:238–254·1537–1543·1564–1571, constants_load_calc.js:36–39를 열었다. d8157c80의 README:14와 공식 자료 노트:15·28을 열었다. fd57bb7:main.js:17과 Pass1.compute:1–28도 열었다. HLSL 셰이더 조각의 존재와 논문 당시 프로그램 전체의 존재를 구분한 최종 판정을 유지했다.
- Tavakkol 2017 p.1–2, Tavakkol 2020 p.1–2·9·11, Lynett 2026 p.1–2·4 이미지에 대조했다. 17행의 언어, 32행의 Base 기능 귀속, 35행의 서지·게재일·방정식 계열·성능 귀속이 원문과 같다.
- 본문은 CP1-151·CP2-176·CP3-111·CD1-1354 수정안 및 CD1-1353·CD2-480 유지안과 같다. frontmatter의 반영일·방법은 notes-apply-10과 같다. Mermaid·금지된 한계 문장은 없다.
- 정정 목록 없음. 기계 확인 후보 없음.

## 최종 집계와 검사

| 노트(models/Celeris/ 기준) | 대조 줄 | 정정 줄 | 보완 줄 | 차이 표 행 |
|---|---:|---:|---:|---:|
| web-refs/celeris-papers-vs-code.md | 39 | 1 | 3 | 13 |
| source-analysis/celeris-coulwave.md | 32 | 2 | 0 | 13 |
| manual-notes/celeris-docs-source-differences.md | 26 | 0 | 0 | 2 |
| web-refs/celeris-lynett-2026.md | 28 | 0 | 0 | 9 |
| web-refs/celeris-official-resources.md | 23 | 0 | 0 | 7 |
| web-refs/celeris-coulwave-theory.md | 21 | 2 | 0 | 2 |
| 합계 | 169 | 5 | 3 | 46 |

- 줄 수는 시작 시 대상 집합에서 셌다. 수정 후에도 대상 집합의 줄 번호와 줄 수가 같다. 표 행 수는 대상 줄의 행 ID에서 셌다.
- 표 46행은 모두 6열이다. 각 행의 분류 및 최종 근거 파일명은 Celeris-final-conclusions.tsv와 일치한다. 이 대상에는 E 행이 없다.
- 상대 링크 54개를 노트 위치에서 해석했다. 모든 대상 파일이 존재한다. 이 수는 대상 줄에서 발견한 링크 출현 수다.
- 대상 줄에는 절대 경로, 홈 축약 경로, 위키 이중 대괄호, Mermaid 블록이 없다. 따라서 그림 대조 대상은 없다.
- 대상 줄의 미완료·후속 작업 문구는 해소했다. 외부 이론식의 동일성을 이름만으로 확정하지 않는다는 문장은 최종 근거의 판정 원칙으로 유지했다.
- 인용 글자 검사는 실제 원문 파일과 이전 판의 지정 줄을 읽어 수행했다. 표의 파이프 이스케이프와 인용 양끝 공백은 Markdown 표현으로 처리했다. 범위 인용·부분 인용·설명문은 문맥으로 따로 판정했다.
- 수정한 8줄에는 지정된 정정 또는 보완 표식을 붙였다. 표 행의 표식은 결론 문장 칸 끝에 있다.
- 대상 노트에 대한 읽기 전용 `git diff --check`가 통과했다. git 쓰기 명령, sudo, 모델 실행을 수행하지 않았다. 쓰기는 대상 노트와 이 DELIVERABLE에 한정했다.
- 사용자 지정 기계 후보 1건과 자체 검사 후보를 모두 판정했다. 미해결 항목은 없다. STOP CONDITION을 충족했다.

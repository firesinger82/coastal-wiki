---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Manual_Testing.md
lines: 86
sha256: c87b32f4c0379f03c795533be3eeb3efa6c1578a225085d4f9dc41836ed62f49
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Manual_Testing.md — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 Manual Testing이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–20 | Test Setup — Jira TEST 프로젝트에 테스트를 만들고 올바른 EFDC+·EE 버전, 모델별 폴더와 테스트별 하위 폴더를 준비하도록 지시한다(12–16). EE에서 테스트 프로젝트를 불러오고 저장해야 한다(17). 각 프로젝트 폴더의 실행 명령 .bat 파일은 선택 사항이다(18). Python 비교 도구(modelcomparer)의 README를 따라 준비하도록 지시한다(19). 연결 대상의 내용을 이번 판독에서 읽지 않았다. |
| 21–40 | Running Models / If Model Crashes — 모델별 각 테스트를 실행하고 결과에 따라 처리하도록 지시한다(23). 모델 충돌(crash)이 나면 명령 프롬프트 화면, 실패 실행의 zip, 관련 Jira Test 항목 링크를 EFDC Jira 버그에 넣도록 지시한다(27–34). 출력이 크면 #output을 zip에서 제외하도록 적는다(28). Test 상태를 Failed로 옮기고 모든 테스트가 충돌 없이 끝난 뒤 모델 비교를 하도록 지시한다(35–39). 로컬 그림 `image-20200506-171702.png`는 TO DO, FAILED, PASSED 열로 나뉜 Jira 테스트 보드이다(37). |
| 41–47 | Model Comparison / 설정 예시의 의미 — 비교 도구 준비가 끝났다는 전제에서 도구 루트 폴더에 config.json을 만들도록 지시한다(43–45). 예시는 각 테스트를 기준 모델(reference model)과 비교하며 3번째 시간 단계부터 한 번에 1개 시간 단계를 비교하고 6번째에서 끝내려는 설정이라고 적는다(46). 원문: `- In the following example config.json, I am comparing each test to a reference model. I am specifying that I want the comparison to start at the 3rd time step, I want to compare 1 time step at a time, and I want to stop the comparison at the 6th time step.` (46). |
| 48–73 | config.json 입력 형식 예시 — REFERENCE와 Single_Domain, IC_Decomp, JC_Decomp의 세 비교 객체를 나열한다(49–71). 각 객체는 comparisonDirectory, sourceDirectory, startIndex: 2, count: 1, endIndex: 5를 갖는다(51–69). JSON 배열·객체 구분과 Windows 경로의 역슬래시 이스케이프를 포함한 예시 줄을 그대로 옮긴다. 이 수치는 비교 예시이며 기본값으로 정의하지 않는다. 원문: `[` (49); `    {` (50); `      "comparisonDirectory": "C:\\models\\Chesapeake_Bay\\REFERENCE",` (51); `      "sourceDirectory": "C:\\models\\Chesapeake_Bay\\Single_Domain",` (52); `      "startIndex": 2,` (53); `      "count": 1,` (54); `      "endIndex": 5` (55); `    },` (56); `    {` (57); `      "comparisonDirectory": "C:\\models\\Chesapeake_Bay\\REFERENCE",` (58); `      "sourceDirectory": "C:\\models\\Chesapeake_Bay\\IC_Decomp",` (59); `      "startIndex": 2,` (60); `      "count": 1,` (61); `      "endIndex": 5` (62); `    },` (63); `    {` (64); `      "comparisonDirectory": "C:\\models\\Chesapeake_Bay\\REFERENCE",` (65); `      "sourceDirectory": "C:\\models\\Chesapeake_Bay\\JC_Decomp",` (66); `      "startIndex": 2,` (67); `      "count": 1,` (68); `      "endIndex": 5` (69); `    }  ` (70); `]` (71). |
| 74–86 | Model Comparison / 실행·결과 처리 — 비교 도구를 실행하고 명령 프롬프트의 색상 문자 처리 때문에 PowerShell을 추천한다(74–76). vel.out 또는 ws.out의 유의한 차이(significant differences)를 보고한다고 적는다(78). 로컬 그림 `image-20200506-175358.png`는 JC_Decomp와 REFERENCE의 시간 단계 비교, Same Timing·Same Domain, `Cell values within 0.001`의 True·False와 유속·수심 차이를 표시한 PowerShell 출력이다(80). 차이가 유의하다고 판단되면 모델 충돌과 같은 절차를 따르고 비교 화면을 포함하도록 지시한다(82). 모델이 끝까지 실행되고 기준 모델과 유의한 차이가 없을 때 Jira Test 상태를 Passed로 옮기도록 지시한다(86). 구분선과 빈 줄을 포함한다(83–85). 원문: `If the differences are considered significant, follow the same procedure as outlined for a model crash. Include a screenshot of the comparison output (like shown above).` (82); `If the models are running to completion, and there are no significant differences between the reference model, then move the Jira Test status to “Passed”. **Finally!**` (86). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 78·80·82행: 본문은 유의한 차이를 판정 조건으로 적는다. 80행 그림은 `Cell values within 0.001`을 표시한다. 본문에는 이 값의 단위와 변수별 판정 기준 설명이 없다.


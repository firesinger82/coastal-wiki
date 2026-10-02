---
file: _staging/recovery/extract/XBeach/office/DecisionTreeXBeach.txt
lines: 158
sha256: 97c846b57ada4aea36a8967bbbb83daf6809de78b776d5ec774d3777a00bf801
reader: codex gpt-6.1-sol
read_date: 2026-10-02
original: models/XBeach/raw/source_code/trunk/doc/misc/DecisionTreeXBeach.docx
---

# DecisionTreeXBeach.txt — 판독 구간 기록

구간은 1행부터 158행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Decision tree XBeach 표제(1). 구상한 트리가 현행 지원 기능보다 넓고 자료 부족으로 모든 조합에 맞춤 조언을 줄 수 없으며, 조합의 중요도·온라인 도구·모델 복잡도·사용자 기술·ICT 환경도 다룬다고 적는다(2–6). 원문: `• Decision tree is more extensive than current functionalities supported by XBeach.` (2), `• Not all combinations will result in a customized advice due to a lack of data.` (3). |
| 7–17 | Input / Forcing (and/or)(7–8). 파랑은 풍파·너울·쓰나미·선박파(9–13), 수위는 조석·폭풍해일(14–16), 바람(17)을 입력 분류로 나열한다. 복수 선택 연결은 제목에 적힌 그대로이다. 원문: `Forcing (and/or)` (8). |
| 18–30 | Configuration (or) / Composition (and/or)(18·23). 지형 구성은 연안방향 균일·장벽섬과 입구·만입 해변·수로와 하천(19–22), 재료/구성 요소는 모래·진흙·점토·산호·자갈·구조물·식생(24–30)을 나열한다. 원문: `Configuration (or)` (18), `Composition (and/or)` (23). |
| 31–50 | Interest (and/or)(31). 지형 변화(32)는 폭풍의 침수·월파·충돌(33–36)과 장기 안정성·회복(37–39)으로 나뉜다. 수리 하중(40)은 파랑의 run-up·overtopping·에너지 소산·구조물·선박(41–46), 흐름의 drifter·수영 안전(47–49), 지하수(50)를 나열한다. 원문: `Interest (and/or)` (31), `▪ Inundation` (34), `▪ Overwash` (35), `▪ Collision` (36), `▪ Run-up` (42), `▪ Overtopping` (43). |
| 51–56 | Scales(51). 시간(52)과 공간(53)을 구분하고 공간 아래에 횡단 방향·연안방향·해상도(54–56)를 나열한다. |
| 57–73 | Output / Model setup(57–58). 모델 설정은 제안 기본값과 보정(59–61), 격자 지침은 제안 구성(62–63), 유효성은 기능 가용성과 시험 여부(64–66), 복잡도는 예산/시간·실행시간·사용자 기술·ICT(67–71)를 나열한다. 72–73행은 빈 줄이다. 실제 매개변수 이름이나 수치 기본값은 적혀 있지 않다. |
| 74–86 | Knowledge Base / Categories / Forcing(74–77). Twitter 메시지형 지식을 네 가지 직교 분류의 hashtag로 태깅하는 데이터베이스 구상(75). 풍파·너울·쓰나미·선박파·조석·폭풍해일·바람을 다시 나열한다(78–86). 원문: `Database with “Twitter messages” tagged with hashtags according to the orthogonal categories “Forcing”, “Composition”, “Configuration” and “Interest”.` (75). |
| 87–99 | Knowledge Base의 Configuration / Composition(87·92). 입력 부분의 네 지형 구성(88–91)과 일곱 재료/구성 요소(93–99)를 반복하여 나열한다. |
| 100–119 | Knowledge Base의 Interest(100). 지형 변화의 폭풍/장기 분류(101–108), 수리 하중의 파랑 하중/흐름/지하수 분류(109–119)를 입력의 관심 항목과 같은 계층으로 나열한다. |
| 120–132 | Types of data(120), 빈 줄(121). 매뉴얼·학술지/학회 논문·석사학위 논문·박사학위 논문·예제 모델·tutorial·Skillbed·전문가 지식·유효성 판단·신규성 점수(122–132)를 자료 유형으로 나열한다. 원문: `• Skillbed` (129), `• Expert knowledge (do’s and don’ts)` (130), `• Validity judgement` (131), `• Novelty score` (132). |
| 133–158 | Database design(133), 빈 줄(134). categories(135–140), labels(141–146), knowledge(147–154), labels2knowledge(155–158)의 필드를 나열한다. 원문 필드명과 각 행을 그대로 아래에 적는다. 원문: `• categories` (135), `◦ id` (136), `◦ parent_id` (137), `◦ type` (138), `◦ name` (139), `◦ status` (140), `• labels` (141), `◦ id` (142), `◦ parent_id` (143), `◦ category_id` (144), `◦ name` (145), `◦ status` (146), `• knowledge` (147), `◦ id` (148), `◦ category_id` (149), `◦ title` (150), `◦ description` (151), `◦ url` (152), `◦ file` (153), `◦ status` (154), `• labels2knowledge` (155), `◦ label_id` (156), `◦ knowledge_id` (157), `◦ status` (158). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 2–3: 문서가 구상한 결정 트리는 현재 XBeach가 지원하는 기능보다 넓다고 명시하며, 자료 부족으로 모든 조합에 맞춤 조언을 줄 수 없다고 명시한다.
- 129: 자료 유형 `Skillbed`의 뜻풀이는 문서 안에 없다.
- 132: `Novelty score`를 자료 유형으로 나열하지만 점수 정의나 척도는 문서 안에 없다.
- 140·146·154·158: 네 데이터베이스 목록 모두 `status` 필드를 포함하지만 상태 값이나 뜻을 정의하지 않는다.

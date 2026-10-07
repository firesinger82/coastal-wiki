---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/External_Forcing_Data/Rating_Curves.md
lines: 14
sha256: 6fe36801d86b491c957c61abfecaaa2f272006dd80bdae3100cf4a0dae19a139
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Rating_Curves.md — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Rating Curves / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–13 | Rating Curves / 수위–유량 관계곡선(rating curve)과 상·하류 의존 조건 — 10행 앞부분은 색상 CSS다. Hydraulic Lookup Table은 External Forcing Data의 일반 양식과 비슷한 기능을 가지며 모든 층 또는 개별 층을 볼 수 있다(10). 구조물 유량이 상류 수위(stage)에만 의존하는 자유 흐름(free flow)은 US Only로 지정한다. 상류와 하류 수위 모두에 의존하는 잠긴 흐름(submerged flow)은 US and DS로 지정한다(12). 조건의 원문: ``The *US Only* option means that flow through the structure depends on the upstream stage only (free flow) while *US and DS* means that flow through the structure depends on both upstream and downstream stages (submerged flow).`` (12). |
| 14–14 | Rating_Curve / 조회 표(lookup table) 화면 — 14행 `EE10_168.png`의 로컬 사본을 열었다. 그림은 `Rating_Curve`, `US Only`, `All Layer`를 선택한 Hydraulic Lookup Table이다. 표 머리글은 `Head`, `Lay_01`이며 단위 표시는 없다. 완전히 보이는 행을 `행 번호: Head, Lay_01` 순서로 옮긴다: ``1: 0, 0``; ``2: 0.0025, 0.00008``; ``3: 0.005, 0.00024``; ``4: 0.0075, 0.00044``; ``5: 0.01, 0.00068``; ``6: 0.0125, 0.00096``; ``7: 0.015, 0.00124``; ``8: 0.0175, 0.00156``; ``9: 0.02, 0.00192``; ``10: 0.0225, 0.00228``; ``11: 0.025, 0.00268``; ``12: 0.0275, 0.00308``; ``13: 0.03, 0.00348``; ``14: 0.0325, 0.00392``; ``15: 0.035, 0.0044``; ``16: 0.0375, 0.00488``; ``17: 0.04, 0.00536``; ``18: 0.0425, 0.00588``; ``19: 0.045, 0.0064``; ``20: 0.0475, 0.00696`` (14행 그림). 다음 행은 화면 하단에서 일부 잘려 있으므로 그 값을 옮기지 않았다. 이 파일 본문은 Head와 Lay_01을 정의하지 않는다(10–12). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10–12·14행 그림: `Head`와 `Lay_01`의 정의와 단위가 본문과 그림에 없다.
- 14행 그림: 20개 자료 행은 완전히 보인다. 그 다음 자료 행은 하단에서 일부 잘려 있다.

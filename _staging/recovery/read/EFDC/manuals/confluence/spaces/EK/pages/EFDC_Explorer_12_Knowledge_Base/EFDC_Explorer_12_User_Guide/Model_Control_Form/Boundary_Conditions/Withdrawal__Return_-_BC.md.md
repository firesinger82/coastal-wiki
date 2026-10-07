---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Boundary_Conditions/Withdrawal__Return_-_BC.md
lines: 24
sha256: 621e729b84864963d7ad71c200a42d9c82f731c3fefb51cd08d9a98f5d8b28fc
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Withdrawal__Return_-_BC.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Withdrawal / Return - BC / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–13 | Withdrawal / Return / 위치와 작동 — EE는 EFDC+의 취수·환류(withdrawal/return) 유량 경계를 지원한다(10). Time Control은 유량과 성분 상승(constituent rises) 시계열 또는 작동 규칙(operational rules)으로 구조물을 운전한다(10). 그룹의 각 셀에 취수 셀과 환류 셀 위치를 직접 지정할 수 있다(12). 원문: ``EE supports the withdrawal/return flow boundary condition of EFDC+. The user interface for the withdrawal/return boundary condition editor is shown in [Withdrawal / Return - BC#Figure 1](#Figure1). As shown in the *Time Control* drop-down menu, EE allows the operation of withdrawal/return structures using time-series of flow (and constituent rises), as well as operation of the structures based on operational rules.`` (10); ``The location of the withdrawal and return cells may be specified directly for each cell in the group in the *Withdrawal Cell* and *Return Cell* frames.`` (12); ``The momentum options for the withdrawal and return cells may be specified in the *Withdrawal Cell Momentum Options* and *Return Cell Momentum Options* frames.`` (12). |
| 14–23 | Withdrawal / Return / 운동량 옵션 — 운동량 플럭스(momentum flux)를 무시하는 기본 옵션과 U·V 셀 면 지정 옵션을 제시한다(14–18). 원문 선택값: ``- Inflow Momentum Flux Ignored (default option)`` (14); ``- Momentum Flux on West U Face`` (15); ``- Momentum Flux on South V Face`` (16); ``- Momentum Flux on East U Face`` (17); ``- Momentum Flux on North V Face`` (18). U·V 면의 양·음 방향과 운동량 폭(momentum width)을 선택할 수 있으며 환류에는 수평각(horizontal angle)도 설정할 수 있다(20). 원문: ``Use the drop-down menu to select momentum flux to be ignored or positive or negative in the U and V faces. The momentum width for both withdrawal and return flows may also be set. In the case of the return flow, the user may also set *Horizontal Angle.*`` (20). 22행 `Withdrawal1.png`의 로컬 사본을 열었다. 그림은 취수·환류 셀, 유량과 농도 상승·하강 설정, 두 셀의 운동량 옵션, Time Control의 세 제어 선택값을 보여 준다(22). 그림의 폭 단위는 `Momentum Width (m)`이고 환류 각도의 단위는 `Horizontal Angle (deg)`이다(22행 그림). |
| 24–24 | Withdrawal / Return / 제어 방식 링크 — 시계열, 취수 셀의 상류 수위(upstream elevation), 취수·환류 셀 사이 고도 차(elevation difference)로 제어할 수 있다고 적는다(24). 적용 대상의 원문: ``Withdrawal/return flow boundary can be controlled by [*Time-Series*](/wiki/spaces/EK/pages/2131132540/Controlled+using+Time+series) or controlled by [*Upstream Elevation*](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2131427332/Controlled+based+on+Water+Elevation) (Water Elevation at Withdrawal cell) or [*Elevation Difference*](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2131427332/Controlled+based+on+Water+Elevation) between Withdrawal and Return cells`` (24). 두 수위 기반 링크는 같은 페이지 ID를 가리킨다(24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·22: Figure 1 링크는 `#Figure1`이다. 이 Markdown 파일에는 해당 ID의 앵커나 Figure 1 캡션이 없다.
- 24: Time-Series 링크의 페이지 ID는 `2131132540`이다. 이번 대상 Controlled using Time Series 파일의 frontmatter ID는 `2133852161`이다(해당 파일 2행). 두 수위 제어 링크의 ID는 `2131427332`이며 이번 대상 Controlled based on Water Elevation 파일의 frontmatter ID는 `2133884929`이다(해당 파일 2행). 링크된 다른 ID 페이지의 본문은 이번 범위에서 읽지 않았다.

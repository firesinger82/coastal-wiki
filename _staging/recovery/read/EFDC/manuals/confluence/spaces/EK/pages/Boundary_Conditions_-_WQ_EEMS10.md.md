---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Boundary_Conditions_-_WQ_EEMS10.md
lines: 21
sha256: c3b37f08d22154020c47958bcd814abe711d9ab716d698941382c7e0555a5430
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Boundary_Conditions_-_WQ_EEMS10.md — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–14 | 문서 정보와 수질 경계조건 — 페이지 메타데이터를 포함한다(1–9). 수질(water quality) 경계조건(boundary condition)을 부하 농도(load concentration)로 정의하는 기능을 소개한다(10). 점오염원 부하 옵션과 설정 화면·캡션을 포함한다(10–13). 그림 직접 확인: `attachments/246546596/10-5-2020_3-59-08_PM.png` — Figure 1(12): Water Quality의 Boundary Conditions 탭을 보여 준다. 점오염원(point source) 농도 시계열 선택값은 창 폭 때문에 끝이 잘려 보인다. Import & Convert WQPSLC.INP (Override)·(Append) 버튼과 `Time Series Data / Water Quality: 1`을 표시한다. |
| 15–18 | Water Quality Point Source Loading Option — 상수 부하·시간 변화 질량 부하·시간 변화 농도 세 옵션을 제시한다(15). 다른 옵션 선택 시 현재 경계조건을 알리고 전환 의사를 묻는다(17). 사용자가 동의하면 선택 옵션으로 변환·저장한다(17). 옵션 이름과 전환 조건을 원문으로 옮긴다(15·17). 원문: `The *Water Quality Point Source Loading Option* provides a drop-down table with the following three options: *Use Constant Point Source Loads, Use Time Variable Point Source MASS Loadings,* and *Use Time Variable Point Source Concentrations.*` (15); `EFDC\_Explorer previously only used the larger mass loading files. The new *Load Concentrations* option provides the user with smaller files and greater control. When the user selects an option different from that previously selected, EFDC\_Explorer informs the user of the current BC and asks whether they want to switch to the new option. If the user responds affirmatively then EFDC\_Explorer will convert and save out the option selected.` (17). |
| 19–19 | Import & Convert / 입력 파일 — Override·Append로 시계열을 덮어쓰거나 추가한다고 설명한다(19). 농도 파일의 단위 표기와 WQPSLC.INP·WQPSL.INP 용도를 원문으로 옮긴다(19). WQPSL.INP는 EFDC가 사용하지 않는 EE 파일이며 흔히 매우 크다고 적는다(19). 원문: `Users can either overwrite or append a new water quality time series by clicking on *Import & Convert WQPSLC.INP* *(Override)* or *Import & Convert WQPSLC.INP* *(Append)* buttons, which is a WQ Point Source concentration file, with a concentration in kg per day. The WQ BC load concentrations rely on two new input files: WQPSLC.INP and WQPSL.INP. Note that WQPSL.INP is an EFDC\_Explorer file not used by EFDC. It is often a very large file.` (19). |
| 20–21 | External Forcing Data / 수직 분포 — 편집 시 수질 매개변수 21개를 표시한다(21). MASS Loadings는 수심 평균(depth-averaged) 값이며 층별 값이 없어 연직 일정하다(21). 농도로 변환하면 층별로 저장하며 처음에는 EE가 계산한 평균이지만 이후 특정 층에 새 값을 할당할 수 있다(21). 원문의 평균·층별 처리 조건을 그대로 옮기고 빈 줄을 포함한다(20–21). 원문: `When the user returns to edit the water quality tables and series in the *External Forcing Data* tab, EFDC\_Explorer displays all 21 WQ parameters. In the *MASS Loadings* option these parameters are depth-averaged and not layered, and so are vertically constant. However, after converting to concentrations loadings, the user is informed that the values have been converted, and now are now stored layer by layer. Initially, these values will be an average as calculated by EFDC\_Explorer, but the user can now specify certain layers and assign new values as required.` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 19: 문서는 WQPSLC.INP를 `concentration file`이라고 부르면서 `a concentration in kg per day`라고 적는다.
- 10: Figure 1 링크는 현재 EK 페이지 ID `246546596` 대신 EEREF 페이지 ID `2380127`을 가리킨다.


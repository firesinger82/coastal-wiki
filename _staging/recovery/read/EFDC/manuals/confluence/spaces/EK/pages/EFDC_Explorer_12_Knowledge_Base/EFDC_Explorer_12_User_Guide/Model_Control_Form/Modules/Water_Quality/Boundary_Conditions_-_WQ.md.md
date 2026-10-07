---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Water_Quality/Boundary_Conditions_-_WQ.md
lines: 21
sha256: 9b0809d18489bb04f9c950c0197b8a72139f966d2c46410c32f2e41c06bdc35c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Boundary_Conditions_-_WQ.md — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Boundary Conditions - WQ — 페이지 메타데이터를 담은 frontmatter이다(1–9). |
| 10–14 | 수질 경계조건(boundary condition) — 질량부하(mass loading) 파일 대신 부하 농도(load concentration)로 정의할 수 있다고 적는다(10). 12행 로컬 그림 `attachments/1034354797/11.png`을 열었다. 그림은 Boundary Conditions 탭의 점오염원 부하(point source loading), WQPSLC.INP 가져오기·변환, 대기 침적(atmospheric deposition), 시계열(time series) 편집을 보여 주는 화면 캡처이다(12–13). |
| 15–18 | 부하 옵션·변환 — 세 가지 선택값은 `The *Water Quality Point Source Loading Option* provides a drop-down table with the following three options: *Use Constant Point Source Loads, Use Time Variable Point Source MASS Loadings,* and *Use Time Variable Point Source Concentrations.*` (15). 기존 옵션과 다른 옵션을 선택했을 때의 확인·변환·저장 조건은 `EFDC+ Explorer previously only used the larger mass-loading files. The new *Load Concentrations* option provides the user with smaller files and greater control. When the user selects an option different from that previously selected, EFDC+ Explorer informs the user of the current BC and asks whether they want to switch to the new option. If the user responds affirmatively then EFDC+ Explorer will convert and save out the option selected.` (17). |
| 19–21 | 농도 파일·수직 배분 — 덮어쓰기·추가 버튼, 파일명·단위·사용 주체는 `Users can either overwrite or append a new water quality time series by clicking on *Import & Convert WQPSLC.INP* *(Override)* or *Import & Convert WQPSLC.INP* *(Append)* buttons, which is a WQ Point Source concentration file, with a concentration in kg per day. The WQ BC load concentrations rely on two new input files: WQPSLC.INP and WQPSL.INP. Note that WQPSL.INP is an EFDC+ Explorer file not used by EFDC. It is often a very large file.` (19). 21개 매개변수 표시, 질량부하의 수심 평균(depth-averaged) 값, 농도 변환 후 층별 저장과 초기 평균값·사용자 지정 조건은 `When the user returns to edit the water quality tables and series in the *External Forcing Data* tab, EFDC+ Explorer displays all 21 WQ parameters. In the *MASS Loadings* option these parameters are depth-averaged and not layered, and so are vertically constant. However, after converting to concentrations loadings, the user is informed that the values have been converted, and now are now stored layer by layer. Initially, these values will be an average as calculated by EFDC+ Explorer, but the user can now specify certain layers and assign new values as required.` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 19행: 점오염원 농도 파일을 설명하는 문구는 `with a concentration in kg per day`이다.


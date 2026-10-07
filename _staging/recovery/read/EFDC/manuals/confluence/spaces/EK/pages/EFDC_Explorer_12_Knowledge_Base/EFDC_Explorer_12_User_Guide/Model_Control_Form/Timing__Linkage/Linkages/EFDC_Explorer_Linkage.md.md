---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Timing__Linkage/Linkages/EFDC_Explorer_Linkage.md
lines: 20
sha256: 7a3976a924c66d7196820927f74f41ef49ad9227fb8661786f3acd477a625eab
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# EFDC_Explorer_Linkage.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — `EFDC+ Explorer Linkage`의 페이지 ID, URL, 버전, 갱신 시각, 계층을 포함한다(1–9). |
| 10–14 | EFDC Model Linkages / 출력 설정 — 결과 후처리 연결 체크박스, 출력 빈도와 간격의 곱, Water Surface 필수 선택을 설명한다(10–14). 매개변수·단위·예시·의무 원문: `- In the EFDC+ Explorer Linkage sub-tab, check *Link EFDC Results to EFDC+ Explorer* checkbox in order to post-process model results ([Figure 1](#Figure1)).` (12) `- The *Linkage Output Frequency* is used to determine how often EFDC will write the output. This is then multiplied by the Output Interval to determine how often various model results will be written. For example, if the *Linkage Output Frequency* is 60 minutes, then an Output interval of 6 will lead to model results being written every 6 hours for that parameter.` (13) `- Which data to output is selected in the *Primary Model Results Linkage Options* frame, with the sub-item checkboxes, such as *Velocities, Water Column*. *Water Surface* must be turned on for EFDC+ Explorer to post-process any of the model results as shown in [Figure 1](#Figure1).` (14) |
| 15–18 | 하위 모델 출력 간격 — 퇴적물 속성작용(sediment diagenesis), 여러 퇴적층(sediment bed layers), 뿌리 식물과 부착조류(Rooted Plant & Epiphyte Model) 출력 간격을 설명한다(15–17). 적용 조건·예시 원문: `- If simulating water quality with the full sediment diagenesis option turned on, EFDC+ Explorer can display the spatial and temporal sediment fluxes and concentrations if the user enables the *Sediment Diagenesis* checkbox. Because the sediment processes are slow, as compared to water column processes, the user has the option to output the diagenesis data at a slower frequency as described above.` (15) `- If simulating sediment transport with the maximum number of bed layers > 1, EFDC+ can write the sediment bed properties by layer. Given that the sediment bed dynamics are generally slow relative to the water column dynamics, the user may want to set the sediment bed layer data output interval to a number greater than 1. For example, if the user is writing the water column data every hour but the user only wants the sediment bed date every day, the user would specify an output interval of 24 to tell EFDC+ to output the sediment data only every 24th water column snapshot.` (16) `- The user may also manually adjust the output interval for the Rooted Plant & Epiphyte Model when applicable.` (17) High-Frequency Dates 설명의 링크를 포함한다(18). |
| 19–20 | Figure 1 — 로컬 그림을 직접 열었다(20). Link EFDC Results to EFDC+ Explorer, Velocities, Water Surface, Water Column 선택 화면이다(20 그림). 예시 값은 `Linkage Output Frequency (min.): 15`, `Sediment Bed Layers (Inorganic Sediments) / Output Interval: 0`, `Rooted Plant & Epiphyte Model / Output Interval: 1`, `Sediment Diagenesis / Output Interval: 12`이다(20 그림). 퇴적층과 속성작용의 Use는 선택되지 않았다(20 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음


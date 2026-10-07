---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-to_Guides_for_Grid/How_to_Export_Grid_to_EFDC.md
lines: 38
sha256: ff66af16042f7c0fda0a24136983a324d817f4d0b68a80aad3ce2273b9fbe069
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# How_to_Export_Grid_to_EFDC.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–13 | 문서 정보와 EFDC 출력 개요 — 페이지 메타데이터를 포함한다(1–9). 선택 격자를 EFDC 입력 파일로 내보내면 EE가 격자에서 별도 모델을 만들지 않고 직접 불러올 수 있다고 설명한다(10). 출력 파일 예시는 `efdc.inp`, `corners.inp`, `dxdy.inp`, `lxly.inp`이다(10). 두 가지 내보내기 방법을 소개한다(12). |
| 14–17 | (1) Using the button from the toolbar — 격자 레이어 선택 후 도구막대 Export To EFDC를 실행한다(16). Save As에서 빈 폴더를 선택하여 저장하면 EFDC 입력 파일을 생성한다(16). 원문: `First, select the grid layer in the Layer Control, then click the Export button from the toolbar. next, select *Export To EFDC* as shown in [How to Export Grid to EFDC#Figure 1](#Figure1). The Save As form will pop up. We need to select an empty folder and then click the *Save* button, as shown in [How to Export Grid to EFDC#Figure 2](#Figure2). As a result, EFDC input files (\*.inp) will be created in that folder.` (16). |
| 18–33 | (2) Using RMC's option — 격자 레이어를 오른쪽 클릭하여 Export.../Export to EFDC를 선택한다(20). Save As에서 빈 폴더를 선택하여 저장한다(20). 두 내보내기 메뉴와 저장 화면의 그림·캡션을 포함한다(22–32). 원문: `First, select the grid layer in the Layer Control, then Right mouse click on that layer, then select *Export.../Export to EFDC*, as shown in [How to Export Grid to EFDC#Figure 3](#Figure3). After that the *Save As* form will pop up, as shown in [How to Export Grid to EFDC#Figure 2](#Figure2), we select an empty folder to save files, then click *Save* button.` (20). 그림 직접 확인: `attachments/2225143866/9.png` — Figure 1(22): 위성 영상 위 항만 격자를 표시하고 도구막대의 Export To EFDC를 빨간 테두리로 강조한다. 그림 직접 확인: `attachments/2225143866/12.png` — Figure 2(26): 빈 폴더를 선택하는 Save As 화면이다. `File name: Select Folder`, `Save as type: EFDC+ Model Folder (*.*)`를 표시한다. 그림 직접 확인: `attachments/2225143866/11.png` — Figure 3(30): 격자 레이어의 Export... 메뉴에서 Export To EFDC를 선택하는 화면. |
| 34–38 | Related articles / Filter by label — 선택한 라벨의 항목이 없다는 안내와 마지막 행을 포함한다(34–38). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·20: `#Figure1`, `#Figure2`, `#Figure3` 링크를 사용하지만 이 Markdown 파일에는 해당 ID를 정의하는 마크업이 없다.
- 26–28: Figure 2의 캡션은 도구막대 사용을 적지만 그림 자체는 빈 폴더를 지정하는 Save As 창을 보여 준다.


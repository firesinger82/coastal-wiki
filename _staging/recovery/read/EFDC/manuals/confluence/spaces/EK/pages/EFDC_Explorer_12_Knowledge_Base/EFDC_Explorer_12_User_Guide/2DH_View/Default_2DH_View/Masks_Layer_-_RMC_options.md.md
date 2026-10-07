---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Default_2DH_View/Masks_Layer_-_RMC_options.md
lines: 42
sha256: 60214dfe5b91ed4df4e16e0102ff0e2ed8897eedfe574867d2672f94ee5519be
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Masks_Layer_-_RMC_options.md — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `title: "Masks Layer - RMC options"` (3)을 포함한다. 페이지 ID, space, URL, 버전, 갱신 시각, 문서 경로와 frontmatter 구분자를 포함한다(1–9). |
| 10–13 | Masks Layer / RMC 메뉴 — Masks 레이어에서 오른쪽 클릭 메뉴를 연다(10). 로컬 그림 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/2090729759/10-28-2021_1-32-20_PM.png`을 열었다(12). 그림 1은 속성·레이어 편집·셀 차단 마스크 편집·확대·제거 메뉴이다(12행 그림). 모델 격자 위의 검은 계단형 선이 마스크를 표시한다(12행 그림). 저면고 범례는 `Bottom Elevation (m)`의 `-4.536`–`-1.500`이다(12행 그림). 빈 줄을 포함한다(11·13). |
| 14–25 | Properties / Edit — Mask Properties에서 이름, 레이어 표시, 범례, 완전·부분 차단 마스크(blocking masks)의 스타일과 색을 설정한다(16). 범례 적용 조건 원문: `Checking this box is only applied when the *Layer Visible* option is checked*.*` (16) `Layer Name`, `Layer Visible`, `Show in Legend`를 설명한다(16). 로컬 그림 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/2090729759/11-1-2021_1-23-54_PM.png`을 열었다(18). 그림 2는 Completely Blocking Masks와 Partially Blocking Masks의 선 스타일·색·폭 설정이다(18행 그림). Edit에서 `Primary Group`, `Parameter`를 바꿔 현재 Masks 레이어를 다른 레이어로 변경한다(22). 로컬 그림 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/2090729759/11-1-2021_1-22-00_PM.png`을 열었다(24). 그림 3은 `Primary Group: Model Grid`, `Parameter: Masks`를 선택한 옵션 창이다(24행 그림). 절 제목과 빈 줄을 포함한다(14–25). |
| 26–35 | Edit Cell Blocking Mask — Vertical Cell Face Blocking에서 마스크를 가진 셀 목록과 셀 인덱스, 초기 조건, 현재 셀의 차단을 표시·편집한다(28–32). 편집 금지 조건 원문: `Initial conditions of the cell, including bottom elevation, water depth, water surface elevation, are shown in the *Initial Conditions* frame, these fields are not editable.` (30) 예제 셀과 면의 조건 원문: `In this case, the cell (L=97) has masks on the west and south faces, so boxes for *Completely Block Mask* of the two faces are checked` (30) 부분 차단 전환·설정의 원문: `In case the user wants to change a mask from completely blocking to partially blocking, the box needs to be unchecked. For example, we will uncheck the box for the west face. Then the *Floating* option can be checked or unchecked, values for *Draft, Bottom Sill* can be entered as shown in [Masks Layer - RMC options#Figure 5](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2090729759#MasksLayer-RMCoptions-Figure5). Click the *Close* button to complete setting the masks for the grid cell.` (32) 34행 URL의 규칙 변환 파일명 두 개는 폴더에 없다. 폴더 목록에서 괄호가 빠진 두 파일을 확인했다. 로컬 그림 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/2090729759/Figure_4_Edit_Cell_Blocking_Masks_1.png`을 열었다(34). 34행 첫 그림은 `I Index: 27`, `J Index: 11`, `L Index: 99` 셀의 `West (U) Face`와 `South (V) Face`가 모두 `Completely Blocked Mask`인 예이다. 초기 조건은 `Bottom Elev. (m): -1.500`, `Depth (m): 1.500`, `WSEL (m): 0.000`이다(34행 첫 그림). 두 면의 `Anchor Elev. (m)`, `Draft (m)`, `Bottom Sill (m)` 값은 모두 `0`이고 비활성화되어 있다(34행 첫 그림). 로컬 그림 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/2090729759/Figure_5_Edit_Cell_Blocking_Masks_2.png`을 열었다(34). 34행 두 번째 그림은 같은 셀의 서쪽 완전 차단을 해제한 예이다. 서쪽 `Floating`을 선택하고 `Draft (m): 4`, `Bottom Sill (m): 1`을 입력한다(34행 두 번째 그림). 서쪽 `Anchor Elev. (m): 0`은 비활성화되어 있다(34행 두 번째 그림). 남쪽 면은 완전 차단 상태이다(34행 두 번째 그림). 두 그림의 확인 버튼은 `OK`, `Cancel`이다(34행 그림). 절 제목과 빈 줄을 포함한다(26–35). |
| 36–42 | Zoom to Layer / Remove — 마스크가 있는 셀로 확대한다(38). Mask 레이어를 Layer Control에서 지운다(42). 절 제목과 빈 줄을 포함한다(36–42). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 30·34행 그림: 본문은 예제 셀을 `L=97`로 적는다. 두 그림은 `I Index: 27`, `J Index: 11`, `L Index: 99`를 표시한다.
- 30·34행 그림: 본문 체크박스 이름은 `Completely Block Mask`이다. 두 그림의 이름은 `Completely Blocked Mask`이다.
- 32·34행 그림: 본문은 완료할 때 `Close` 버튼을 누르라고 적는다. 두 그림에는 `OK`와 `Cancel` 버튼이 보인다.
- 34: 규칙 변환 파일명 `Figure_4_Edit_Cell_Blocking_Masks_(1).png`, `Figure_5_Edit_Cell_Blocking_Masks_(2).png`은 폴더에 없다. 폴더에 있는 `Figure_4_Edit_Cell_Blocking_Masks_1.png`, `Figure_5_Edit_Cell_Blocking_Masks_2.png`을 열어 각각 완전 차단과 부분 차단 화면을 확인했다.

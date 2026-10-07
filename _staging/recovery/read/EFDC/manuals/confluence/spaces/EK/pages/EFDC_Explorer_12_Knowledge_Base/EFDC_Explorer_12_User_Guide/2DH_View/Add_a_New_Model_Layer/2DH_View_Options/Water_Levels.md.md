---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Add_a_New_Model_Layer/2DH_View_Options/Water_Levels.md
lines: 29
sha256: b1316260848a4c91269c2a18b8fdd700830055f4024a2e06e780a2ccd4acbc8b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Water_Levels.md — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `title: "Water Levels"` (3)을 포함한다. 페이지 ID, space, URL, 버전, 갱신 시각, 문서 경로와 frontmatter 구분자를 포함한다(1–9). |
| 10–15 | Water Levels / 메뉴 — 수심(water depth)에서 유도한 매개변수를 제공한다(10). 주된 사용은 `Water Depth`와 수면고(Water Elevation)의 표시이다(10). `Water Level` 옵션을 그림으로 안내한다(10). 로컬 그림 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/259162133/2019-06-26_9-46-59_AM.png`을 열었다(12). 그림 1은 Water Level 그룹의 Parameter 목록을 펼친 화면이다(12행 그림). 캡션과 빈 줄을 포함한다(14–15). |
| 16–26 | 매개변수 표 — 침수 지도(inundation map)의 최소 수심·지속시간과 면적 재계산, FEMA 위험 수준·월류(overtopping)·총수두(total head) 표시, 수심·수면고, 습윤·건조(wet/dry) 표시를 설명한다(18–25). 수식 표현을 원문 형태로 보존한다(19–22). Total Head는 속도를 불러온 경우에만 제공된다(22). Wet/Dry는 `Use Wet` 선택 여부에 따라 건조 수심 또는 습윤 수심을 사용한다(25). 헤더·구분선과 빈 줄을 포함한다(16–26). 각 매개변수·식·적용 조건의 원문 표 행: `\| *Area Extents* \| This option displays an inundation map and computes areas using a specified minimum depth and duration. The user can change the minimum depths and durations and EFDC+ Explorer will recompute the areas and display the results. \|` (18); `\| *Hazard Area Extents* \| This option displays the FEMA velocity hazard level defined as depth \* velocity head (v2/2g). The areas displayed and the areas computed are based on the computed hazard level over a specified minimum. The user can change the minimum level and EFDC+ Explorer will recompute the areas and display the results. \|` (19); `\| *Overtopping Flow* \| This displays the FEMA defined overtopping depth which is defined as: depth \* velocity. \|` (20); `\| *Overtopping Head* \| This displays the FEMA defined overtopping depth which is defined as: depth + velocity head (v2/2g). \|` (21); `\| *Total Head* \| Displays the total head, water surface elevation + velocity head (v2/2g). Only available if the velocities have been loaded. \|` (22); `\| *Water Depth* \| This option displays water depth of the model. \|` (23); `\| *Water Elevation* \| This option displays water surface elevation of the model. \|` (24); `\| *Wet/Dry* \| Provides a two color display for wet cells (blue) and dry (gray). The wet/dry determination is made using the dry depth unless the *Use Wet* option is checked, in which case the wetting depth will be used. The areas and the numbers of wet/dry cells are reported. \|` (25).  |
| 27–29 | 로컬 그림 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/259162133/2019-06-26_10-29-39_AM.png`을 열었다(27). 그림 2는 모델 격자의 수면고를 색으로 표시한다(27행 그림). 범례는 `Water Elevation (m)`이며 양 끝 값은 `6.093`, `6.099`이다(27행 그림). 캡션을 포함한다(29). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 19·21–22: 속도수두(velocity head) 표현은 `v2/2g`이다. 이 파일은 `v2`와 `g`를 별도로 정의하지 않는다.
- 20–21: Overtopping Flow 행과 Overtopping Head 행은 둘 다 `FEMA defined overtopping depth`라고 적는다. 두 행의 정의식은 각각 `depth \* velocity`, `depth + velocity head (v2/2g)`이다.

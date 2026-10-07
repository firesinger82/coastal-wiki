---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Using_CVLGrid_Menu_Options/EFDC_Tools_Menu/Load_EFDC_Grid.md
lines: 22
sha256: 8ccc51e8fa4701fe724460d5ae927bb640739285aa7b83156e0cab70768ed19c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Load_EFDC_Grid.md — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

그림의 설정값은 화면에 표시된 값으로 기록한다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목은 `Load EFDC Grid`이다(3). 문서 ID는 `2818195`이다(2). 공간·원문 URL·버전·갱신 시각·탐색 경로를 기재한다(4–8). YAML 구분선은 1·9행이다. |
| 10–14 | Load EFDC Grid / Figure 1 — 기존 EFDC 모델의 격자를 불러오는 옵션이다(10). 폴더 선택 후 `OK`를 누르면 격자가 불러와진다(10). 그림은 `Select Directory: Open Operation` 창을 보여 준다(12행 그림). `Scale:`의 표시값은 `1`이다. `Don't use the IJ Map to compute nodal coordinates (may result in long import times):`는 체크 해제 상태이다(모두 12행 그림). `Create New`, `Cancel`, `OK` 버튼이 있다(12행 그림). 그림 링크·캡션과 빈 줄을 포함한다(11–14). 원문: `This *Load EFDC Grid* option allows the user to load a grid of an existing EFDC model. This browsing window is shown in [Load EFDC Grid#Figure 1](https://eemodelingsystem.atlassian.net/wiki/spaces/CVLKB/pages/2818195#LoadEFDCGrid-Figure1). After clicking the *OK* button the EFDC Grid is loaded in [Load EFDC Grid#Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/CVLKB/pages/2818195#LoadEFDCGrid-Figure2).` (10). 직접 연 로컬 그림은 `models/EFDC/raw/manuals/confluence/spaces/CVLKB/attachments/2818195/worddav48f5870b22ee0ad4eabf6002b858fce9.png`이다(12행 그림). |
| 15–18 | EFDC Grid Loading Options / Scale — `Scale`은 기존 `LXLY` 파일의 셀 중심(centroid) 좌표 단위를 변환하는 계수이다(17). EFDC+ Explorer의 기본 X, Y 단위는 미터(meters)이다(17). LXLY 좌표가 킬로미터(kilometers)나 마일(miles) 단위이면 모델을 올바르게 표시하기 위해 미터로 변환해야 한다(17). 처음 불러올 때 변환계수를 입력할 수 있다(17). 큰 셀이 겹쳐 뭉친 것처럼 보이는 경우 LXLY 단위 변환 문제가 원인일 가능성이 있다고 설명한다(17). 적절한 계수로 다시 불러오라고 안내한다(17). 절 제목·빈 줄을 포함한다(15–18). 원문: `The "*Scale*" input box allows the user to apply a conversion factor to the centroid units used in the legacy LXLY file. The EFDC+ Explorer default X, Y unit is meters. Many applications use kilometers or miles as the units for the cell centroids provided in the LXLY file. To correctly display the model these cell centroid coordinates must be converted to meters. CVLGrid can perform this function by entering the conversion factor in the *Scale* box when loading the model for the first time. Note: When a model is loaded and then viewed but looks like a cluster of large cells stacked on top of one another, it is likely to be a LXLY units conversion issue. Try reloading the model with an appropriate scale factor.` (17). |
| 19–22 | IJ Map 옵션 / Figure 2 — `Don't use the IJ Map to compute nodal coordinates` 옵션은 CVLGrid가 모든 셀 모서리를 탐색해 노드(node)를 구성하도록 강제한다(19). Figure 2는 불러온 `EFDC_Grid`를 파란 격자로 보여 준다(21행 그림). 넓고 분기한 하부 영역은 가늘고 굽은 상부 구간으로 이어진다(21행 그림). 범례는 `EFDC_Grid`이다. 축척 막대 표기는 `400 Meters`이다. `Layer Control`에는 이름 `EFDC_Grid`와 유형 `Grid`가 표시된다(모두 21행 그림). 좌표축과 방향 화살표는 보이지 않는다(21행 그림). 그림 링크·캡션을 포함한다(21–22). 원문: `The *"Don't use the IJ Map to compute nodal coordinates"* box will force CVLGrid to search through all the cell corners to build the nodes` (19). 직접 연 로컬 그림은 `models/EFDC/raw/manuals/confluence/spaces/CVLKB/attachments/2818195/worddav9b3cdb31a31e79da82969fb77144d351.png`이다(21행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22행 캡션은 `EDFC grid loaded.`라고 적는다. 제목과 본문은 `EFDC`를 사용한다(3·10·17·19행).

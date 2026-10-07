---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Grids_and_Background_Maps/Importing_Multiple_Grids_into_EFDC_Explorer.md
lines: 57
sha256: 589f558574f860a8259cb1bd0c4f9e75a0bb611a3cf45e8a35e97e126411286c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Importing_Multiple_Grids_into_EFDC_Explorer.md — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 메타데이터와 다중 격자(multiple grids) 결합 설명이다(1–17). CSS 색상 지시문이 본문 앞에 남아 있다(10). 외부 격자 생성기로 결합하는 조건은 `While it is possible to join the separate domains using external grid generators one by one, this only works if they are all in the same I, J domain. For example, if users have several domains they must first load one domain then paste this and add more one at a time. In the end, users will have only one grid which they can then import into EE.` (12). 서로 다른 I, J 영역을 따로 가져와 사용자가 연결해야 한다는 조건과 연결 파일 생성 설명은 `If all the grid subdomains are not in the same I, J domain then the sub-domains will have to be brought in separately. This must be done manually by the user. However, EE helps with this process by allowing the user to set the N-S or E-W connection. Once the model is saved EE will generate a MAPPGNS.INP or MAPPGEW.INP file or both of them depending on which type of connectors established.` (14). 예제 파일은 `Part01.cvl`, `Part02.cvl`이다(16). |
| 18–34 | EE10에서 새 모델을 만든 뒤 격자 파일을 가져오는 절차이다(18–34). 본문 단축키는 `Ctrl+O`이다(19). Model 메뉴 그림의 New Model 단축키는 `Ctrl+N`이다(21). 새 모델 아이콘과 도구막대 위치를 보여 준다(19, 21). 가져오기 설정은 `Import Grid from Files`, `Import Grids`, `Multiple grid files`이다(23). Ctrl 키로 여러 파일을 선택한다(27). 파일 선택 그림은 `Grid type`에 `CVLGrid`, `Multiple grid files` 선택, `UTM Zone`에 `0`, `Part01.cvl`과 `Part02.cvl`을 보여 준다(29). 붉은 화살표는 Import Grid 창에서 파일 선택 창으로 향한다(29). 확인 그림은 크기가 다른 녹색 곡선 격자 두 개와 OK 버튼을 보여 준다(33). |
| 35–46 | 2차원 수평 보기(2DH View)와 격자 연결 레이어(layer)를 여는 절차이다(35–46). 설정 이름과 값은 `Primary Group` = `Model Grid`, `Parameter` = `Grid Connections`이다(37, 39). 2DH와 레이어 추가 아이콘을 보여 준다(35, 37). View Options 그림의 붉은 화살표는 도구막대에서 설정 창으로 향한다(39). 파란 격자 그림의 범례는 `Bottom Elevation (m)`, 양 끝 값은 `0.000`과 `0.000`이다(39). Layer Control 그림은 Grid Connections 행과 연필 모양 편집 버튼을 보여 준다(43). |
| 47–57 | 셀(cell)을 오른쪽 클릭하여 연결 종류를 선택하고 다른 격자의 인접 셀을 왼쪽 클릭하는 절차이다(47–57). 메뉴 항목은 `Add N-S Connection`, `Add N-S Connection Group`, `Add E-W Connection`, `Add E-W Connection Group`이다(49). 그림은 첫 항목 선택을 보여 준다(49). 붉은 화살표는 격자 셀에서 연결 메뉴로 향한다(49). 다음 그림의 붉은 선은 격자 사이의 틈을 가로질러 두 셀의 중심 표식을 잇는다(53). 완료 그림의 자홍색 선은 N-S 연결을 표시한다(57). 연결선에는 화살촉이 없다(53, 57). 두 그림의 범례는 `Bottom Elevation (m)`, 양 끝 값은 `0.000`과 `0.000`이다(53, 57). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- CSS 색상 선택자와 스타일 문자열이 본문에 남아 있다(10).
- 새 모델을 여는 본문 단축키는 `Ctrl+O`이지만 메뉴 그림은 `Ctrl+N`을 표시한다(19, 21).
- Figure 1, 2, 3, 5, 7, 9의 링크는 URL 조각을 지정하지만 이 파일에는 해당 조각의 명시적 앵커가 없다(19, 23, 37, 47, 55).

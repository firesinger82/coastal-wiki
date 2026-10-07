---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Get_parameters_from_NetCDF_exported_from_EE.md
lines: 181
sha256: a549707ec34fe1ee4d45aeca2aa22ed5b2aa2f9df9ea41a3b4d00e146d46aa25
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Get_parameters_from_NetCDF_exported_from_EE.md — 판독 구간 기록

구간은 1행부터 181행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 메타데이터와 NetCDF 추출 개요 — 모델 출력이 있을 때 NetCDF로 내보낼 수 있다고 설명하고 별도 내보내기 문서를 연결한다(1–10). Python 스크립트로 주요 매개변수를 추출하는 정보를 제공한다고 적는다(12–14). 16행 로컬 `attachments/2275246081/1.png`를 열었다. 그림은 Export to NetCDF files 화면이다. `Model Grid`, `Initial Bottom Elevation`, `All`, `Water Surface Elevation`, `Flow Velocity`, `Wind`, `Sediments`가 선택됐다. 설정값은 `Start: 3165.000` / `2018-09-01 00:00:00`, `End: 4991.000` / `2023-09-01 00:00:00`, `Time Steps: 1`, `Deflate Level: 2`, `Single File`, `UGrid Format`, `UTM Zone Projection: 16`이다(16). 이 값은 그림의 예시이며 기본값으로 서술하지 않았다. |
| 20–21 | 매개변수 표 머리글 — `**Parameters**` 머리글과 Markdown 표 구분선을 포함한다(20–21). |
| 22–24 | **I index of the model cells** — `Variable name`: `col` (23); `Long name`: `cell column index` (24). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 25–27 | **J index of the model cells** — `Variable name`: `row` (26); `Long name`: `cell row index` (27). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 28–31 | **Bottom elevation** — `Variable name`: `BELV` (29); `Unit`: `m` (30); `Dimensions`: `(time, CELL)  time is the Julian time since the base date of the model.  CELL is the cell index.` (31). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 32–35 | **Water Surface Elevation** — `Variable name`: `WSEL` (33); `Unit`: `m` (34); `Dimensions`: `(time, CELL)` (35). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 36–39 | **Cohesive grain size shear stress** — `Variable name`: `cohesive\_shear` (37); `Unit`: `N/m2` (38); `Dimensions`: `(time, CELL)` (39). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 40–43 | **Sediment bed top layer index** — `Variable name`: `bed\_top` (41); `Unit`: `layer` (42); `Dimensions`: `(time, CELL)` (43). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 44–47 | **Bed sediment thickness** — `Variable name`: `bed\_thickness` (45); `Unit`: `m` (46); `Dimensions`: `(time, CELL, KB)` (47). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 48–51 | **Sediment bed wet density** — `Variable name`: `bed\_wet\_density` (49); `Unit`: `kg/m3` (50); `Dimensions`: `(time, CELL, KB)` (51). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 52–55 | **Bed sediment porosity** — `Variable name`: `bed\_porosity` (53); `Unit`: `-` (54); `Dimensions`: `(time, CELL, KB)` (55). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 56–59 | **Cohesive sediment** — `Variable name`: `cohesive\_sediment` (57); `Unit`: `mg/L` (58); `Dimensions`: `(time, NSED2, CELL, KC)` (59). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 60–63 | **Non-cohesive sediment** — `Variable name`: `noncohesive\_sediment` (61); `Unit`: `mg/L` (62); `Dimensions`: `(time, NSND, CELL, KC)` (63). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 64–67 | **Bed mass cohesive (Top Layer)** — `Variable name`: `bed\_top\_mass\_cohesive` (65); `Unit`: `g/m2` (66); `Dimensions`: `(time, NSED, CELL)` (67). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 68–71 | **Bed mass non-cohesive (Top Layer)** — `Variable name`: `bed\_top\_mass\_noncohesive` (69); `Unit`: `g/m2` (70); `Dimensions`: `(time, NSND, CELL)` (71). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 72–75 | **Sediment mass** — `Variable name`: `bed\_mass` (73); `Unit`: `g/m2` (74); `Dimensions`: `(time, NSXD, CELL, KB)` (75). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 76–79 | **Sediment mass fraction** — `Variable name`: `bed\_mass\_fraction` (77); `Unit`: `-` (78); `Dimensions`: `(time, NSXD, CELL, KB)` (79). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 80–83 | **Average particle size of bed surface** — `Variable name`: `bed\_d50` (81); `Unit`: `microns` (82); `Dimensions`: `(time, CELL)` (83). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 84–87 | **Water temperature** — `Variable name`: `temperature` (85); `Unit`: `degC` (86); `Dimensions`: `(time, CELL, KC)` (87). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 88–91 | **Dye** — `Variable name`: `dye` (89); `Unit`: `mg/L` (90); `Dimensions`: `(time, NDYE, CELL, KC)` (91). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 92–95 | **Refractory particulate organic carbon** — `Variable name`: `RPOC` (93); `Unit`: `mg/L` (94); `Dimensions`: `(time, CELL, KC)` (95). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 96–99 | **Labile particulate organic carbon** — `Variable name`: `LPOC` (97); `Unit`: `mg/L` (98); `Dimensions`: `(time, CELL, KC)` (99). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 100–103 | **Dissolved organic carbon** — `Variable name`: `DOC` (101); `Unit`: `mg/L` (102); `Dimensions`: `(time, CELL, KC)` (103). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 104–107 | **Refractory particulate organic phosphorus** — `Variable name`: `RPOP` (105); `Unit`: `mg/L` (106); `Dimensions`: `(time, CELL, KC)` (107). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 108–111 | **Labile particulate organic phosphorus** — `Variable name`: `LPOP` (109); `Unit`: `mg/L` (110); `Dimensions`: `(time, CELL, KC)` (111). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 112–115 | **Dissolved organic phosphorus** — `Variable name`: `DOP` (113); `Unit`: `mg/L` (114); `Dimensions`: `(time, CELL, KC)` (115). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 116–119 | **Total phosphate** — `Variable name`: `P4D` (117); `Unit`: `mg/L` (118); `Dimensions`: `(time, CELL, KC)` (119). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 120–123 | **Refractory particulate organic nitrogen** — `Variable name`: `RPON` (121); `Unit`: `mg/L` (122); `Dimensions`: `(time, CELL, KC)` (123). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 124–127 | **Labile particulate organic nitrogen** — `Variable name`: `LPON` (125); `Unit`: `mg/L` (126); `Dimensions`: `(time, CELL, KC)` (127). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 128–131 | **Dissolved organic nitrogen** — `Variable name`: `DON` (129); `Unit`: `mg/L` (130); `Dimensions`: `(time, CELL, KC)` (131). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 132–135 | **Ammonia nitrogen** — `Variable name`: `NHX` (133); `Unit`: `mg/L` (134); `Dimensions`: `(time, CELL, KC)` (135). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 136–139 | **Nitrate nitrogen** — `Variable name`: `NOX` (137); `Unit`: `mg/L` (138); `Dimensions`: `(time, CELL, KC)` (139). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 140–143 | **Particulate biogenic silica** — `Variable name`: `SUU` (141); `Unit`: `mg/L` (142); `Dimensions`: `(time, CELL, KC)` (143). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 144–147 | **Available dissolved silica** — `Variable name`: `SAA` (145); `Unit`: `mg/L` (146); `Dimensions`: `(time, CELL, KC)` (147). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 148–151 | **Chemical oxygen demand** — `Variable name`: `COD` (149); `Unit`: `mg/L` (150); `Dimensions`: `(time, CELL, KC)` (151). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 152–155 | **Dissolved oxygen** — `Variable name`: `DOX` (153); `Unit`: `mg/L` (154); `Dimensions`: `(time, CELL, KC)` (155). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 156–159 | **Total active metal** — `Variable name`: `TAM` (157); `Unit`: `mg/L` (158); `Dimensions`: `(time, CELL, KC)` (159). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 160–163 | **Fecal coliform bacteria** — `Variable name`: `FCB` (161); `Unit`: `MPN/100ml` (162); `Dimensions`: `(time, CELL, KC)` (163). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 164–167 | **Phytoplankton** — `Variable name`: `ALG` (165); `Unit`: `mgC/L` (166); `Dimensions`: `(time, NALG, CELL, KC)` (167). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 168–171 | **Total erosion rate in the cell** — `Variable name`: `bed\_erosion\_rate` (169); `Unit`: `g/cm2/s` (170); `Dimensions`: `(time, CELL)` (171). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 172–175 | **Total deposition rate in the cell** — `Variable name`: `bed\_deposition\_rate` (173); `Unit`: `g/cm2/s` (174); `Dimensions`: `(time, CELL)` (175). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 176–179 | **Bed toxics** — `Variable name`: `bed\_toxics` (177); `Unit`: `mg/kg` (178); `Dimensions`: `(time, NTOX, CELL, KB)` (179). 이 항목에 기본값·허용 범위는 명시하지 않는다. |
| 180–181 | 표 뒤 빈 줄과 캡션 — `Table 1. Export to NetCDF files from EFDC+ Explorer.` 캡션을 포함한다(180–181). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12행: Python 스크립트로 매개변수를 추출한다고 소개한다. 이 파일의 1–181행에는 Python 스크립트나 실행 예제가 없다.
- 31·47·59·63·67·75·167·179행 등: `time`과 `CELL`은 31행에서 정의한다. `KB`, `KC`, `NSED2`, `NSED`, `NSND`, `NSXD`, `NDYE`, `NALG`, `NTOX`의 뜻은 이 파일에서 정의하지 않는다.
- 10·14행: Figure 1과 Table 1 링크의 URL fragment를 선언한 로컬 앵커는 본문에 없다. 그림과 표 캡션은 존재한다.

---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Boundary_Conditions/Groundwater_-_BC.md
lines: 23
sha256: d55c18f30d662c9a41947868151468a371f919a6be38aa3e671b12e080202f2e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Groundwater_-_BC.md — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Groundwater - BC / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–16 | Groundwater / 상호작용 옵션 — 색상 CSS 뒤에 지하수(groundwater) 상호작용 옵션을 설명한다(10). 사용자가 옵션 명세와 지하수 매개변수 기능을 확인하려면 EFDC 코드를 검토해야 한다고 적는다(10). 비활성화, 토양 습윤·건조(soil wetting/drying), 지하수 상호작용, 구역별 일정 침투 유출(zoned constant seepage) 옵션을 나열한다(12–15). 원문: `- *Disable*: Disable groundwater interaction;` (12); `- *Soil Wetting/Drying*: Allow soil wetting and drying;` (13); `- *Groundwater Interaction*: Allow groundwater interaction (using GWMAP and GWSER),` (14); `- *Zoned Constant Seepage*: Apply a constant groundwater flux out of the model by zones (using GWSEEP and GWMAP, and available for EFDC+ only).` (15). `Groundwater Interaction`은 `GWMAP`과 `GWSER`를 사용한다(14). `Zoned Constant Seepage`는 모델에서 나가는 일정 지하수 플럭스(flux)를 구역별로 적용하며 `GWSEEP`, `GWMAP`을 사용하고 `EFDC+ only`라고 적는다(15). |
| 17–23 | Groundwater / 클래스 배정과 초기 조건 — Edit Seepage로 지하수 클래스 자료(groundwater class data, Option 3)에 접근한다(17). 시계열 수를 입력한 뒤 표에서 클래스 자료를 지정한다(17). Apply Overlay는 다각형(polygon) 파일 안에 있는 모든 셀을 지정한 지하수 클래스에 배정한다(19). Const IC's의 활성 조건과 지하수 고도(groundwater elevation), 유효 공극률(effective porosity), 건조 셀에서 초과 물의 침투 또는 제거 사용 여부를 설명한다(21). 원문: `*Const IC's* is only enabled when the user select *Soil Wetting/Drying*and *Zoned Constant Seepage.*The user can specify groundwater interactions in this form such as groundwater elevation, effective porosity, or in *Zoned Constant Seepage*case, whether or not to *Use Percolate or Eliminate Excess Water in Dry Cells* ( type in 1 to use, 0 to not use) .` (21). 사용 여부 입력값은 원문의 `type in 1 to use, 0 to not use`이다(21). 23행 `EE10_146.png`의 로컬 사본을 열었다. 그림은 Groundwater 창에서 Zoned Constant Seepage를 선택한 상태와 Const IC's, Edit Seepage, Apply Overlay 버튼을 보여 준다(23). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·23: Figure 1 링크는 원문 페이지의 `#Groundwater-BC-Figure1`을 가리킨다. 이 Markdown 파일에는 해당 ID의 앵커나 Figure 1 캡션이 없다.
- 12–17: 옵션 목록에는 번호가 없다. 17행은 지하수 클래스 자료 접근을 `Option 3`이라고 적으며 이 파일 안에서 그 번호를 목록 항목에 명시적으로 연결하지 않는다.

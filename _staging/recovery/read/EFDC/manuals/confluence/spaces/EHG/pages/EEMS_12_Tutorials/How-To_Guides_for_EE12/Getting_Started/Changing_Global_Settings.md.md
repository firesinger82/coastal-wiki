---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Getting_Started/Changing_Global_Settings.md
lines: 42
sha256: 9154b5d029b5520a74ca38324bb96b9dd6309d9ee771161b40ff25140485eeea
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Changing_Global_Settings.md — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 메타데이터와 전역 설정 진입 — 메타데이터 뒤 CSS 색상 규칙이 본문 첫 문장 앞에 남아 있다(1–10). Tools의 Options에서 기본 정밀도·단위·기타 설정을 바꾼다고 설명한다(10). 12행 로컬 그림을 열었다. 그림 1은 Tools의 Options 메뉴를 강조한다. |
| 16–25 | Options Settings / General — 일반 탭에서 단위계(unit system)와 사용자 인터페이스 언어(language)를 선택한다(16–24). 이름 원문: `1. *General* tab: this option is simply for choosing the *Unit System* and changing *Language* for the graphical user interface.` (20). 22행 로컬 그림을 열었다. 그림 2의 선택값은 `Unit System: Metric`, `Language: English`이며 대안은 `English/US`이다(22행 그림). |
| 26–31 | Formats — Default Precision for Write Operation은 데이터 유형별 출력·표시 정밀도를 지정한다(26). 원문은 표시된 기본값이 대부분의 적용에 적절하나 수로·연구 등 특수한 경우 조정할 가능성이 높다고 적는다(26). 설정은 프로젝트별 `EFDC.EE`에 저장한다(26). 조건·기본값 설명 원문: `2. *Formats* tab: the *Default Precision for Write Operation* settings are for setting the output/display precisions for the indicated data types. The default settings shown are appropriate for most applications. However, for some special cases (e.g. flume studies or other types of research applications) the user will likely have to make adjustments to the defaults. The settings are stored in the project-specific EFDC.EE file.` (26). 28행 로컬 그림을 열었다. 표는 `Elevations & Depths: 3`, `X & Y Locations: 3`, `Time Display (Days): 6`의 Precision 값을 표시한다(28행 그림). |
| 32–37 | Other Settings — 광 소산계수(light extinction coefficient)를 m 단위 Secchi Depth로 바꾸는 계수, 허용 최소 무기 퇴적물 두께, 탄소/건중량 비, 자동 갱신 최대 셀 수를 설명한다(32). 이름·단위·역할 원문: `3. *Other Settings* tab includes the *Secchi Conversion Factor*(to convert light extinction coefficients to a Secchi Depth in meters); the *Minimum Inorganic Sediment Thickness* allowable; *Carbon/Dry Weight Ratio* (ratio of mg of carbon to mg of dry weight to convert POC and algae to the weight of a solid); and the *Maximum Number of Cells to Auto Refresh*.` (32). 34행 로컬 그림을 열었다. 그림 4의 항목은 `Secchi Conversion Factor`, `Minimum Inorganic Sediment Thickness (m)`, `Carbon / Dry Weight (mgC/mg DW)`, `Maximum Number of Cells to Auto Refresh`이다. 입력 칸은 모두 비어 있으며 값·기본값·범위는 읽을 수 없다. |
| 38–42 | Text Editor — ASCII 파일을 편집할 프로그램을 선택한다(38). 40행 로컬 그림을 열었다. 그림 5는 편집기 경로 `C:\Windows\notepad.exe`와 Browse 버튼을 보여 준다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: `[data-colorid=...]` 및 `html[data-color-mode=dark]` CSS 규칙 문자열이 본문 첫 문장 앞에 그대로 남아 있다.

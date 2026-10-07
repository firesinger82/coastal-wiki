---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/Wind_Forcing/Temporally_and_Spatially_Varying_Forcings.md
lines: 26
sha256: bcd0f003c844257946810b220300b099dc4b5b77272fb3d7f0a90f754b675a06
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Temporally_and_Spatially_Varying_Forcings.md — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Temporally and Spatially Varying Forcings / 메타데이터 — 페이지 식별자 `2056257537` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–15 | Time Varying Field / 외부 자료 — CSS 뒤에 전 영역 셀별 시간·공간 가변 바람 강제력을 설명한다(10). 시간 가변장(Time Varying Field, TVF) 형식은 `ASCII and binary formats`, `Appendix B-26` (10)에 따라 외부 자료·모형과 연결한다. 생성 조건 원문은 `at this stage, the creation of TVF data must be done externally.` (10)이다. EE는 읽기·쓰기·보기의 전후처리를 수행할 수 있다고 적는다(10). 로컬 `15.png`를 열었다(12). Wind Speed 선택 목록은 Not Used·From ASCII File·From Binary File을 보여 준다. 빈 줄·Figure 1 캡션을 포함한다. |
| 16–21 | Time Variable Data Field / 활성·옵션 — 형식을 선택한 뒤 Edit로 시간 가변장을 지정한다(16). 비활성 조건의 옵션 원문은 `Enabled` (16)이다. 체크되지 않았으면 바람 시계열 외부 강제력 자료장을 적용한다고 적는다(16). 로컬 `16.png`를 열었다(18). 화면은 `Enabled`가 체크되지 않은 Wind Velocities 폼이며 `Time Begin: 2922`; `Time End: 3287`; `Base Date: 1995-01-01`; `Time Step (min.): 1440.000`; `# Time Steps: 0`; `# Components: 2`; `# Layers: 1`; `Time Scale (sec.): 86400`; `Time Shift: 0`; `Value Scale: 1`; `Value Shift: 0`; `Data Units: m/s`를 표시한다(18, 그림). 두 성분은 Wind X-velocity와 Wind Y-velocity이고 모형 단위는 각각 `m/s`이다. Time Interpolation·Update Option·Area Option 선택 상자는 비활성 상태이다. |
| 22–26 | Field Data Interpolation from Fixed Stations — `PRESFLD` (22) 파일을 만들기 위해 Interpolate로 개별 시계열을 연결한다고 적는다. 연결 목록의 형식 원문은 `4 columns: station ID; X coordinates in UTM, Y coordinate in UTM; and the path of the data series respectively` (22)이다. 개별 파일 형식 원문은 `the number of records, series name, time, and value` (22)이다. 선형 보간(linear interpolation)과 기존 자료 대체 여부를 선택한 뒤 Interpolate를 실행한다(22). 로컬 `17.png`를 열었다(24). 지점 표의 `(ID,X (m),Y (m),Data Path)`은 `(L001,51525.6,2961287,empty); (L002,514785.6,2974097,empty); (L003,531457.9,2986154,empty); (L004,521002.3,2958461,empty)`이다(24, 그림). `# Data Series: 4`; `Time Begin: 2922`; `Time End: 3287`; `Time Step (min.): 1440.000`; `# Time Steps: 366`을 표시한다. 빈 줄·Figure 3 캡션을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·22: 10행은 TVF 자료 생성이 외부에서 이루어져야 한다고 적는다. 22행은 EE의 Interpolate로 PRESFLD 파일을 만드는 절차를 적는다.
- 22: 주제는 바람 강제력인데 생성 파일명을 `PRESFLD`라고 적는다.


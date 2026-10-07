---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/Wind_Forcing/Wind_Drag.md
lines: 12
sha256: 85f2f99d6e36dd8d3684af5c2fdf794e32e03c213cf561ad8fc74f964d1ca012
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Wind_Drag.md — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더인 `models/EFDC/raw/manuals/confluence/spaces/EK/`를 기준으로 적는다.

| 구간 | 내용 |
|---|---|
| 1–9 | Wind Drag / 문서 메타데이터 — 원문 frontmatter는 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 경로를 적는다(1–9). |
| 10–11 | Wind Drag — EEMS는 사용자 정의 바람 항력(wind drag) 관계를 지원한다(10). 사용자는 풍속의 하한·상한으로 관계를 구성한다(10). 원문은 두 관계를 모두 같은 명칭으로 적는다(10). 원문: `EEMS supports a user-defined wind drag relationship.  The wind drag relationship is configured by the user based on the lower and upper bound wind velocities of both the linear wind drag relationship and the linear wind drag relationship. A number of different options are provided including a user-defined relationship.` (10).  |
| 12–12 | Wind Drag / Surface Drag 선택 화면 — 직접 연 로컬 그림 `attachments/2048032781/3.png` (12)은 바람 데이터(Wind Data)의 표면 항력(Surface Drag) 드롭다운을 보여준다. 선택지는 `Original`, `Original Rel U/V`, `Hersbach, 2011 (ECMWF)`, `COARE3.6 Simplified`, `User Defined`이다(12 그림). 사용자 정의 입력 이름은 `Lower Wind Speed (m/s)`, `Upper Wind Speed (m/s)`, `Lower Wind Drag Coeff.`, `Upper Wind Drag Coeff.`이다(12 그림). 그림 표시값은 `Lower Wind Drag Coeff.`의 `1.000E-3`과 `Upper Wind Drag Coeff.`의 `2.500E-3`이다(12 그림). 두 풍속 입력값은 열린 드롭다운이 가린다(12 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 원문은 `both the linear wind drag relationship and the linear wind drag relationship`로 같은 관계 이름을 두 번 적는다.

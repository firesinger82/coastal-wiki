---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Using_CVLGrid_Menu_Options/Display_Options_Menu/DTM_Color_Ramp.md
lines: 23
sha256: 121a9674612cf9041510319adaa54730fb89915edd6af3c65ba0c41cc047d9d8
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# DTM_Color_Ramp.md — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — Confluence 페이지의 식별자, 제목, space, URL, 버전, 갱신 시각, 문서 계층과 frontmatter 경계 표식이다(1–9). |
| 10–14 | DTM Color Ramp — 표고(elevation)별 색상 램프(color ramp)를 설정한다. 적용 조건 원문: `The *DTM Color Ramp* frame deals with elevation and the color gradients to represent different elevations. If the user is only using a 2D polygon then this section is irrelevant. [Figure 1](#DTMColorRamp-Figure1) shows this section for reference.` (10). 2D 폴리곤(polygon)만 사용하는 경우에는 이 절과 관련이 없다고 적는다. Figure 1의 로컬 그림을 직접 열고 확대하여 표시값을 확인했다(12). `Ramp Label`은 `Elevation (m)`이다. `Single Ramp or Upper Range`의 `Blue`는 `9E+15`, `Red`는 `-9E+16`이다. `Lower Range`는 `Use`가 체크되지 않았으며 `Cutoff: 0`, `Bottom: -1`이 비활성으로 표시된다. `Show Color Topo`와 `Auto Ramp to Viewport`는 체크되어 있다. `Elevation Clipping Options`의 `Use`는 체크되지 않았으며 `Low End: 1E+32`, `High End: -1E+32`가 비활성으로 표시된다. `DTM Point Options`에는 `Diameter of DTM Point (in): 0.0075`가 있다(12). 이 값들은 그림 예시값이다. 캡션과 빈 줄을 포함한다(11–14). |
| 15–23 | DTM Color Ramp / 설정 표 — 각 설정의 이름·기능·단위·적용 조건을 원문대로 옮긴다: `*Ramp* *Label*` — `Give the color ramp a name` (17); `*Single* *Ramp* *or* *Upper* *Range*` — `Specifies the range of color from blue to red` (18); `*Lower* *Range*` — `Specifies the lower range of the color ramp` (19); `*Show* *Color* *Topo*` — `Shows the elevation topography in color based on the color ramp.` (20); `*Auto Ramp to Viewport*` — `Change Min, Max, and Average number of View Options "Ortho", "Dx", and "Dy" on Legend when view window changed.` (21); `*Elevation Clipping Options*` — `Specifies the elevation range for clipping` (22); `*DTM Point Options*` — `Allow the user set the diameter of DTM Points in inches` (23). 화면을 바꾸면 `Auto Ramp to Viewport`가 `Ortho`, `Dx`, `Dy` 보기의 범례(legend)에 있는 `Min`, `Max`, `Average`를 바꾼다고 적는다(21). DTM 점 지름의 단위는 `inches`이다(23). 표 머리글·구분선과 빈 줄을 포함한다(15–16). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: 내부 링크 `#DTMColorRamp-Figure1`이 있다. 13행 캡션에는 해당 앵커 정의가 없다.
- 12: `Elevation Clipping Options`의 비활성 표시값은 `Low End: 1E+32`, `High End: -1E+32`이다. 낮은 끝값이 높은 끝값보다 크다. 해당 프레임의 `Use`는 체크되지 않았다.


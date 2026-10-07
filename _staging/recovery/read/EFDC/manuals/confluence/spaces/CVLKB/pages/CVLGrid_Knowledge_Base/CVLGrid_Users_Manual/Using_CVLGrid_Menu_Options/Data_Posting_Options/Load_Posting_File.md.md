---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Using_CVLGrid_Menu_Options/Data_Posting_Options/Load_Posting_File.md
lines: 22
sha256: a3746a32d9f6ee8e8279a6a75ecbc688e2d22a5130144bee8fe7f745eca1e352
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Load_Posting_File.md — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — Confluence 페이지의 식별자, 제목, space, URL, 버전, 갱신 시각, 문서 계층과 frontmatter 경계 표식이다(1–9). |
| 10–14 | Load Posting File / 파일 선택 — 원하는 포스팅(posting) 파일을 파일 선택 창에서 찾는다. 지원 형식은 `File Types` 링크를 참조한다. 포스팅 파일을 선택하면 작업 공간에 불러오기 전에 설정 창이 먼저 표시된다. 해당 설정 설명은 `Options` 링크를 참조한다(10). Figure 1의 로컬 그림을 직접 열었다(12). `Open ASCII File` 창은 선택된 `Posting.dat`를 보여 준다. 보이는 파일 필터의 확장자는 `*.p2d;*.plt;*.dxf;*.dat`이다. 캡션과 빈 줄을 포함한다(11–14). |
| 15–17 | Label import / Figure 2 — 로컬 그림을 직접 열었다(15). 창 제목은 `Label Import`이다. 안내 원문은 `Enter the X&Y Conversion Factor (e.g. 3.281 ft/m):`이다. 입력칸의 예시값은 `1`이다(15). 캡션과 빈 줄을 포함한다(16–17). |
| 18–20 | Data posting options / Figure 3 — 로컬 그림을 직접 열었다(18). `Data Posting Options` 창은 기호(symbol), 라벨(label), 전역 설정(global options)을 보여 준다. 기호의 `Show`와 `Fixed Properties`가 선택되어 있다. 다른 선택지는 `Vary Size`, `Vary Color`이다. 범위 입력칸 표기는 `Range Min: 1E+32`, `Range Mid: 0`, `Range Max: -1E+32`이다. `Default Symbol Properties`, `Reset Range`, `Clip Viewport`, `XY Transform`, `Save Points`, `Label Options` 버튼이 있다. `Label Value`와 전역 `Show`는 체크되어 있다. `As DTM`은 체크되지 않았다(18). 이 값들은 그림에 보이는 상태이다. 캡션과 빈 줄을 포함한다(19–20). |
| 21–22 | 불러온 포스팅 자료 / Figure 4 — 로컬 그림을 직접 열었다(21). 작업 공간에 붉은 기호 여섯 개가 보인다. 라벨은 `CS24`, `CS09`, `CS27`, `CS25`, `CS08`, `CS23`이다. 거리 축척 표기는 `10 Kilometers`이다. 수평·수직 눈금 축은 없다. 캡션을 포함한다(22). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: 내부 링크 `#LoadPostingFile-Figure1`, `#LoadPostingFile-Figure3`, `#LoadPostingFile-Figure4`가 있다. 13·19·22행의 캡션에는 대응하는 앵커 정의가 없다.
- 18: 그림의 범위 입력칸은 `Range Min: 1E+32`, `Range Max: -1E+32`를 표시한다. 표시된 최솟값이 최댓값보다 크다.


---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Data_Format_B-7__GIS_Shapefile.md
lines: 16
sha256: e402126c13721d7c7301570320f2ceed1fdf81c6d82d18466403e44f6f37aefb
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-7__GIS_Shapefile.md — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 페이지 제목은 `"Data Format B-7  GIS Shapefile"` (3)이다. `id: 1588887648` (2), `space: EK` (4), `version: 1` (6), `updated: 2021-11-10T04:10:44.799Z` (7)를 기록한다. 원문 URL (5)과 문서 경로 (8)가 있다. 1·9행은 frontmatter 구분선이다. |
| 10–13 | GIS Shapefile — Shapefile은 비위상 기하(nontopological geometry)와 공간 객체(spatial feature)의 속성(attribute)을 저장한다 (10). 최소 구성은 주 파일(main file), 색인 파일(index file), dBASE 표이다 (10). 주 파일은 꼭짓점(vertex) 좌표 목록으로 도형을 나타내며 직접 접근·가변 레코드 길이 형식이다 (12). 색인 레코드는 대응하는 주 파일 레코드의 시작 기준 오프셋(offset)을 보관한다 (12). dBASE 표는 객체마다 하나의 속성 레코드를 갖는다 (12). 속성 레코드는 주 파일 레코드와 순서가 같아야 하며 도형 레코드와 일대일 관계를 갖는다 (12). 구성·수량 원문: `The Shapefile format stores nontopological geometry and attribute information for spatial features in a data set. A Shapefile consists minimally of the main file, an index file, and a dBASE table.` (10). 형식·순서 의무 원문: `In the main file, the geometry for a feature is stored as a shape comprising a set of vector coordinates. This main file is direct access, variable-record-length file in which each record describes a shape with a list of its vertices. In the index file, each record contains the offset of the corresponding main file record from the beginning of the main file. Attributes are held in a dBASE format file. The dBASE table contains feature attributes with one record per feature. Attribute records in the dBASE file must be in the same order as records in the main file. Each attribute record has a one-to-one relationship with the associated shape record.` (12). 11·13행의 빈 줄을 포함한다. |
| 14–16 | Example — 예시 표제 (14), 빈 줄 (15), 그림 참조 (16)를 포함한다. 로컬 `attachments/1588887648/B-9.png`를 열었다 (16). 속성 표 화면은 `Bot :: Features Total: 2121, Filtered: 2121, Selected: 0`을 표시한다 (16). 열 머리말은 `L`, `I`, `J`, `Bottom Ele`이다 (16). 표의 가시 1–29행 값을 셀별로 전사한다. 그림 표 1행: `L` `878`, `I` `6`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 2행: `L` `877`, `I` `5`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 3행: `L` `876`, `I` `4`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 4행: `L` `875`, `I` `58`, `J` `29`, `Bottom Ele` `-3.065000057` (16); 그림 표 5행: `L` `874`, `I` `57`, `J` `29`, `Bottom Ele` `-3.381999969` (16); 그림 표 6행: `L` `873`, `I` `56`, `J` `29`, `Bottom Ele` `-3.655999899` (16); 그림 표 7행: `L` `872`, `I` `55`, `J` `29`, `Bottom Ele` `-3.772000074` (16); 그림 표 8행: `L` `871`, `I` `54`, `J` `29`, `Bottom Ele` `-3.839999914` (16); 그림 표 9행: `L` `870`, `I` `53`, `J` `29`, `Bottom Ele` `-3.940999985` (16); 그림 표 10행: `L` `869`, `I` `52`, `J` `29`, `Bottom Ele` `-4.074999809` (16); 그림 표 11행: `L` `868`, `I` `51`, `J` `29`, `Bottom Ele` `-4.183000088` (16); 그림 표 12행: `L` `867`, `I` `50`, `J` `29`, `Bottom Ele` `-4.245999813` (16); 그림 표 13행: `L` `866`, `I` `49`, `J` `29`, `Bottom Ele` `-4.298999786` (16); 그림 표 14행: `L` `897`, `I` `25`, `J` `30`, `Bottom Ele` `-3.299999952` (16); 그림 표 15행: `L` `896`, `I` `24`, `J` `30`, `Bottom Ele` `-3.138000011` (16); 그림 표 16행: `L` `895`, `I` `23`, `J` `30`, `Bottom Ele` `-2.961999893` (16); 그림 표 17행: `L` `894`, `I` `22`, `J` `30`, `Bottom Ele` `-2.714999914` (16); 그림 표 18행: `L` `893`, `I` `21`, `J` `30`, `Bottom Ele` `-2.303999901` (16); 그림 표 19행: `L` `892`, `I` `20`, `J` `30`, `Bottom Ele` `-1.715999961` (16); 그림 표 20행: `L` `891`, `I` `19`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 21행: `L` `890`, `I` `18`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 22행: `L` `889`, `I` `17`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 23행: `L` `888`, `I` `16`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 24행: `L` `887`, `I` `15`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 25행: `L` `886`, `I` `14`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 26행: `L` `885`, `I` `13`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 27행: `L` `884`, `I` `12`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 28행: `L` `883`, `I` `11`, `J` `30`, `Bottom Ele` `-1.500000000` (16); 그림 표 29행: `L` `882`, `I` `10`, `J` `30`, `Bottom Ele` `-1.500000000` (16). 화면 밖의 레코드는 전사하지 않았다. |

수식 전사: 0개. 매개변수·입력 필드 이름 전사: 4개 (`L`, `I`, `J`, `Bottom Ele`).
이 집계는 전사한 이름의 종류 수이다. 예시 값은 기본값으로 간주하지 않았다.
참조 그림 1개를 로컬 파일로 직접 열어 확인했다.

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16: 그림의 `L`, `I`, `J`, `Bottom Ele` 열의 정의와 `Bottom Ele` 값의 단위는 본문에 명시되어 있지 않다.

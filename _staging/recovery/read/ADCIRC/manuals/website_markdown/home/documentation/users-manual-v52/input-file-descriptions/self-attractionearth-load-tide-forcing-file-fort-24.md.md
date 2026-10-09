---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/self-attractionearth-load-tide-forcing-file-fort-24.md
lines: 448
sha256: 45875ae170841bc3e638bcad791466e3206e0963f31d31607985e3cbaf4975ef
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# self-attractionearth-load-tide-forcing-file-fort-24.md — 판독 구간 기록

1–448행을 순서대로 읽었다. 아래 구간은 빈 줄·마크업·스크립트를 포함하며 앞 구간의 다음 행부터 이어진다.

| 구간 | 내용 |
| --- | --- |
| 1–12 | 웹 페이지 감시: New Relic 설정과 브라우저 로더(browser loader)가 있다(1–2). 뒤에는 빈 줄이 있다(3–12). |
| 13–77 | 페이지 스타일시트(CSS): 검색 필드(search field)와 경로 탐색(breadcrumbs), 페이지 머리말(header), 본문(body), 전체 컨테이너(container), 태그(tag), 오른쪽 내용 영역의 배치를 지정한다(13–77). |
| 78–150 | 내용 배치 스타일: 한 열 배치, 문단·링크, 경로 탐색, 문맥 메뉴(context navigation), 인용문(blockquote), 소제목, 왼쪽·오른쪽 내용 영역과 탐색 영역의 스타일이 있다(78–150). |
| 151–230 | 탐색 메뉴(navigation menu) 스타일: 메뉴 목록, 하위 메뉴, 포인터가 올라간 항목, 현재 항목, 태그 표시와 이미지 크기의 스타일이 있다(151–230). 배경 그림 두 개를 참조한다(166·202). 두 로컬 그림 파일 없음. 원문: `background:url(images/primary\_nav\_divider.gif) repeat-y scroll right bottom;` (166); `background: #76a3de url(images/primary\_nav\_bg\_repeat\_on.gif) repeat-x top;` (202). |
| 231–241 | 페이지 제목과 메타데이터(metadata): 페이지 제목(232)과 JSON-LD 형식의 웹 페이지·사이트·경로 탐색 정보(237)가 있다. 공개 시각, 수정 시각, 언어와 검색 동작도 포함한다(237). 사이의 빈 줄도 포함한다. |
| 242–269 | 이모지(emoji)와 WordPress 스타일: 이모지 설정·실행 스크립트가 있다(242–246). 이모지 이미지 스타일(249–259)과 자동 생성 버튼·미리 정의된 스타일(262–269)이 있다. |
| 270–303 | 관리·방문 통계·배경 스타일: 빈 줄, 관리자 표시줄 스타일(286–288), Beehive 방문 통계 스크립트(292–298)가 있다. 페이지 배경 그림을 참조한다(300). 해당 로컬 그림 파일 없음. 원문: `body.custom-background { background-color: #ffffff; background-image: url("https://adcirc.org/wp-content/uploads/sites/2255/2013/03/grid\_bkgrd\_lt\_grey1.jpg"); background-position: left top; background-size: auto; background-repeat: repeat-y; background-attachment: scroll; }` (300). |
| 304–361 | 사이트 머리말과 메뉴: ADCIRC 사이트명(306), 공식 사이트 문구(308), 탐색 건너뛰기 링크(310)가 있다. 커뮤니티 메뉴(312–322), 문서·매뉴얼·보고서 메뉴(323–358), 관련 소프트웨어 메뉴(359–361)가 이어진다. |
| 362–401 | 소식·제품 메뉴: 소식과 워크숍 메뉴(362–393), 제품 메뉴(394–399), ASGS 링크(400)가 있다. 사진 링크는 `ADCIRC2018_Group_Photo2.jpg` (368); `2017ADCIRCUGMGroupPhoto.jpg` (370); `160506-A-Y1769-008-A-1.jpg` (374); `adcircBootCampers2016_small_caption.jpg` (375); `2011_ADCIRC_meeting.jpg` (387); `ADCIRC_Workshop2010_GroupPhoto2.png` (389)이다. 각 링크에 대응하는 로컬 그림 파일 없음. |
| 402–403 | 본문 경로 탐색: Home, Documentation, User’s Manual – v52, Input File Descriptions와 현재 문서명이 이어진다(402). 다음 빈 줄도 포함한다(403). |
| 404–409 | 자기 인력·지구 하중 조석(self attraction/earth load tides) 적용과 형식: fort.15의 NTIP=2일 때 사용한다(404·406). 속도 정보가 없는 “tea” 조화 형식(harmonic format)과 같다(408). 분조(constituent) 순서는 fort.15의 조석 퍼텐셜(tidal potential) 항 순서와 같아야 한다(408). 위상(phase)은 도 단위여야 한다(408). 진폭(amplitude)은 중력(gravity) 단위와 호환되는 단위여야 한다(408). 절점 인자(nodal factor)와 평형 인수(equilibrium argument)가 값을 수정한다(408). 원문: `Self attraction/earth load tides are used to force ADCIRC when [NTIP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NTIP)=2 in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15).` (406); `The format of this file is identical to the “tea” harmonic format with no velocity information included. Entries are grouped by constituents and must be in the same order as the tidal potential terms listed in the [Model Parameter and Periodic Boundary Condition File](../model-parameter-and-periodic-boundary-condition-file-fort-15). Phases must be in degrees. Amplitudes must be in units compatible with the units of gravity. These values are modified by the nodal factor and equilibrium argument provided for the tidal potential terms.` (408). |
| 410–429 | 입력 구조와 반복문: 문서의 굵은 변수명, 빈 줄, 반복문, 정의 링크를 설명한다(410). 각 분조에 Alpha line, Constituent frequency, 1, Constituent name 행을 둔다(412–420). 절점 반복문 안에 JN, SALTAMP(k,JN), SALTPHA(k,JN)을 둔다(422–428). 원문: `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (410); `for k=1,[NTIF](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NTIF)` (412); `Alpha line` (414); `Constituent frequency` (416); `1` (418); `Constituent name (e.g., M2)` (420); `for j=1,[NP](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)` (422); `**[JN](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#JN)**, **[SALTAMP(k,JN)](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#SALTAMP)**, **[SALTPHA(k,JN)](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#SALTPHA)**` (424); `end j loop` (426); `end k loop` (428). |
| 430–432 | 주의: 각 분조의 첫 네 행은 파일에 있어야 한다(430·432). ADCIRC는 읽을 때 이 네 행을 건너뛴다(432). 원문: `**Note:**` (430); `The first four lines (Alpha line, Constituent frequency, 1, Constituent name) for each constituent must be present in the file but they are skipped over during the ADCIRC read.` (432). |
| 433–448 | 페이지 후속 스크립트와 빈 줄: 유틸리티 표시 함수(436), 링크 미리 가져오기(prefetch) 설정(438), 쿠키(cookie) 배너 설정과 마크업(441–443), Soliloquy의 no-js 클래스 제거(447), New Relic 페이지 측정 정보(448)가 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·300·368·370·374·375·387·389행: 페이지 배경 그림 참조 세 개와 메뉴의 사진 링크 여섯 개에 대응하는 로컬 그림 파일 없음. 로컬 원문 사본 디렉터리인 models/ADCIRC/raw/manuals에서 해당 그림 파일을 찾지 못했다.

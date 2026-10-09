---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v52/input-file-descriptions/surface-temperature-boundary-values-fort-38/index.md
lines: 456
sha256: 910fdec49f43c11661fc33dfeef7090d92ea56476ae3478b86e88d897a9de911
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

1–456행을 순서대로 읽었다. 아래 구간은 빈 줄·마크업·스크립트를 포함하며 앞 구간의 다음 행부터 이어진다.

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
| 404–407 | 표면 온도 경계값(surface temperature boundary values) 입력의 적용 조건: fort.15의 RES_BC_FLAG가 나열된 값일 때 fort.38을 읽는다(404·406). 문서는 이를 측면 온도 경계 조건(lateral temperature boundary condition)을 사용하는 경우로 설명한다(406). 입력 형식은 표면 열 플럭스(surface heat flux) 매개변수화를 제어하는 BCFLAG_TEMP에 따라 달라진다(406). 원문: `The surface temperature boundary condition input file (fort.38) is read in when the [**RES\_BC\_FLAG**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#RES_BC_FLAG) is set to -3, 3, -4, or 4 in the [fort.15 file](../model-parameter-and-periodic-boundary-condition-file-fort-15/ "Model Parameter and Periodic Boundary Condition File (fort.15)") (i.e., when a lateral temperature boundary condition is being used) and its format depends on the [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#BCFLAG_TEMP) parameter in the fort.15, which controls the surface heat flux parameterization in ADCIRC.` (406). |
| 408–419 | BCFLAG_TEMP=1 형식: 데이터 집합 반복문 안에서 수평 절점(horizontal mesh node)을 반복하여 k와 q_heat(k)를 입력한다(408–418). 원문: `If [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#BCFLAG_TEMP)=1 in the fort.15, the format of the fort.38 is as follows:` (408); `for i=1 to numberOfDataSets` (410); `for k=1 to [**NP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP)` (412); `k, **q\_heat(k)**` (414); `end k loop` (416); `end i loop` (418). |
| 420–429 | BCFLAG_TEMP=2 형식: 각 데이터 집합에서 TMP(K,J)를 J=1,6 및 K=1,NP 범위로 입력한다(420–426). TMP(K,J)는 K번째 수평 절점의 J번째 열 플럭스 성분이다(428). 괄호는 암시적 Fortran 입출력 반복문(implicit Fortran i/o loop)을 나타낸다(428). 원문: `If [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#BCFLAG_TEMP)=2 in the fort.15, the format of the fort.38 is as follows:` (420); `for i=1 to numberOfDataSets` (422); `(K, (**TMP(K,J)**, J=1,6),K=1,[**NP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP))` (424); `end i loop` (426); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (428). |
| 430–439 | BCFLAG_TEMP=3 형식: 각 데이터 집합에서 TMP(K,J)를 J=1,4 및 K=1,NP 범위로 입력한다(430–436). TMP 정의와 암시적 Fortran 입출력 반복문의 괄호를 다시 설명한다(438). 원문: `If [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#BCFLAG_TEMP)=3 in the fort.15, the format of the fort.38 is as follows:` (430); `for i=1 to numberOfDataSets` (432); `(K, (**TMP(K,J)**, J=1,4),K=1,[**NP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP))` (434); `end i loop` (436); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (438). |
| 440–440 | NP의 정의와 추가 참조: 모든 위 형식에서 NP는 수평 격자의 절점 수, 즉 2D 전체 영역(fulldomain)의 절점 수이다(440). 3D 경압 물리와 BCFLAG_TEMP 값의 추가 설명은 fort.15 문서를 참조하도록 안내한다(440). 원문: `In all the above cases, [**NP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#NP) is the number of nodes in the horizontal mesh (i.e., the 2D fulldomain number of nodes). See the [fort.15](../model-parameter-and-periodic-boundary-condition-file-fort-15/) documentation on 3D baroclinic physics (particularly the explanation of various [**BCFLAG\_TEMP**](https://adcirc.org/home/documentation/users-manual-v52/parameter-definitions#BCFLAG_TEMP) values) for more details.` (440). |
| 441–456 | 페이지 후속 스크립트와 빈 줄: 유틸리티 표시 함수(444), 링크 미리 가져오기(prefetch) 설정(446), 쿠키(cookie) 배너 설정과 마크업(449–451), Soliloquy의 no-js 클래스 제거(455), New Relic 페이지 측정 정보(456)가 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 166·202·300·368·370·374·375·387·389행: 페이지 배경 그림 참조 세 개와 메뉴의 사진 링크 여섯 개에 대응하는 로컬 그림 파일 없음. 로컬 원문 사본 디렉터리인 models/ADCIRC/raw/manuals에서 해당 그림 파일을 찾지 못했다.
- 410·422·432행: 데이터 집합 반복 상한인 `numberOfDataSets`의 정의는 이 파일 본문에 없다.
- 414·424·428·434·438·440행: `q\_heat(k)`의 정의와 단위 및 `TMP(K,J)`의 J별 성분명과 단위는 이 파일 본문에 없다. 추가 설명은 fort.15 문서를 참조하도록 안내한다(440).

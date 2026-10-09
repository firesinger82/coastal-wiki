---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/adcirc-architecture/index.md
lines: 423
sha256: a58d9c6cb1d7d6efa847dc939612296f1bd425d741a5722dcdd48de5faf517ef
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# adcirc-architecture/index.md — 판독 구간 기록

구간은 1행부터 423행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 웹사이트 수집 내용 — New Relic 초기 설정과 압축된 브라우저 계측 스크립트가 들어 있다(1–2). 이어지는 빈 줄도 포함한다(3–12). |
| 13–85 | 웹사이트 CSS / 검색·본문 배치 — 검색 필드와 검색 버튼, 제목·본문·링크, 컨테이너·헤더·콘텐츠 영역의 스타일을 정의한다(13–85). 주석도 포함한다. |
| 86–161 | 웹사이트 CSS / 본문·탐색 메뉴 — 콘텐츠 영역·문단·링크·탐색 경로(breadcrumb)·인용문·메뉴의 스타일을 정의한다(86–161). |
| 162–230 | 웹사이트 CSS / 하위 메뉴·그림 배치 — 메뉴 항목의 배경 그림 참조, 하위 메뉴·마우스 반응·현재 페이지 스타일과 그림의 표시 크기 설정을 포함한다(162–230). |
| 231–270 | 페이지 제목·구조화 정보·WordPress 표시 코드 — 페이지 제목과 schema.org의 페이지·탐색 경로·웹사이트 정보를 포함한다(232·235). 이모지(emoji) 지원 검사 스크립트와 이모지·버튼·색상·간격 CSS가 들어 있다(241–268). 빈 줄과 주석도 포함한다. |
| 271–302 | 웹사이트 관리·통계·배경 설정 — 빈 줄, 관리 표시 CSS, Beehive 통계 초기 설정과 배경 그림 URL을 포함한다(271–299). |
| 303–357 | 사이트 공통 탐색 / Community·Documentation — ADCIRC 사이트 제목, Skip Navigation 링크와 개발자·사용자·매뉴얼 V50–v53·컴파일 옵션·예제·보고서·관련 문헌 링크를 나열한다(303–357). |
| 358–400 | 사이트 공통 탐색 / Related software·News·Products·ASGS — 유틸리티·격자 생성기·행사 자료·사진·예보·제품·ASGS 링크를 나열한다(358–399). 마지막 빈 줄도 포함한다(400). |
| 401–408 | ADCIRC Architecture — 탐색 경로와 본문 제목을 포함한다(401·403). 본문은 ADCIRC, ADCPREP, ADCPOST 구조도 링크 3개로 이루어진다(405–407). `ADCIRC-Architecture.png` (405), `ADCPREP-Architecture.png` (406), `ADCPOST-Architecture.png` (407)는 모두 그림 파일 없음. 로컬 사본이 없어 도식의 상자·기호·화살표 방향은 확인하지 못했다. |
| 409–423 | 웹사이트 후처리 — 빈 줄과 화면 유틸리티 호출, 링크 미리 가져오기(prefetch) 설정, 쿠키 안내, jQuery 호출, New Relic 페이지 계측 정보를 포함한다(409–423). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 405행: `ADCIRC-Architecture.png`는 그림 파일 없음. `models/ADCIRC/raw/manuals/`의 파일명 검색과 `website/`·`website_markdown/`의 대응 업로드 폴더 확인에서 로컬 사본을 찾지 못했다.
- 406행: `ADCPREP-Architecture.png`는 그림 파일 없음. 로컬 사본을 찾지 못해 구조도 내용을 열어 보지 못했다.
- 407행: `ADCPOST-Architecture.png`는 그림 파일 없음. 로컬 사본을 찾지 못해 구조도 내용을 열어 보지 못했다.

---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Using_CVLGrid_Menu_Options/Geo-Reference_Background/Setup.md
lines: 16
sha256: fae59ce71edea448ee0fbc573b9f554185cedc317e3916bd2c8bb2b0928ad70c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Setup.md — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

그림의 설정값은 화면에 표시된 값으로 기록한다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목은 `Setup`이다(3). 문서 ID는 `2818230`이다(2). 공간·원문 URL·버전·갱신 시각·탐색 경로를 기재한다(4–8). YAML 구분선은 1·9행이다. |
| 10–11 | Setup — 지리 참조(geo-referenced) 이미지를 만드는 별도 창을 연다(10). 예에서는 Google Earth 같은 외부 지도 도구에서 내보낸 비트맵(bitmap)을 불러오며 그 이미지는 `JPEG`이다(10). 이미지의 두 점에 대한 좌표를 지정한다(10). 본문은 점 위치에서 `RMC`를 사용하고 드롭다운의 점 `1` 또는 `2`를 선택한다고 설명한다(10). 각 점의 대응 좌표를 왼쪽 도구모음의 해당 칸에 입력해야 한다(10). 상세 사용법은 DSI에서 구할 수 있는 별도 문서에 있다고 적는다(10). 원문: `The Setup option opens a separate window that allows the user to create a geo-referenced image. The user is able to load a bitmap image exported from a third party mapping tool such Google Earth (the bitmap image here is JPEG image), for example, and specify the coordinates of two points on the image. Points are specified by RMC on the point location and selecting point 1 or 2 from a drop down menu. The corresponding point coordinates must then be input to the appropriate box in the left toolbar. This window is shown in [Figure 1](#Setup-Figure1) and the file menu is shown in [Figure 2](#Setup-Figure2). Detailed explanation of how to use this tool is provided in a separated document available from DSI.` (10). |
| 12–14 | Figure 1 — `Bitmap Georeferencing` 창에서 위성영상과 기준점(reference point) 표시 `UL WL`을 보여 준다(12행 그림). `Point 1`의 표시값은 `Pixel X:` = `24`, `Pixel Y:` = `25`, `X:` = `583041`, `Y:` = `2331441`이다. `Point 2`의 표시값은 `Pixel X:` = `4778`, `Pixel Y:` = `3187`, `X:` = `590952`, `Y:` = `2326266`이다. `Upper Left Corner`의 표시값은 `X:` = `583001`, `Y:` = `2331480`이다. `Lower Right Corner`의 표시값은 `X:` = `590992`, `Y:` = `2326220`이다(모두 12행 그림). 점마다 `Reset` 버튼이 있다(12행 그림). `Update`, `OK`, `Cancel` 버튼도 보인다(12행 그림). 그림 링크·캡션·빈 줄을 포함한다(12–14). 직접 연 로컬 그림은 `models/EFDC/raw/manuals/confluence/spaces/CVLKB/attachments/2818230/worddava4a0368f8f6b5d395e06418ed20d2b53.png`이다(12행 그림). |
| 15–16 | Figure 2 — 지리 참조 도구의 `File` 메뉴를 보여 준다(15행 그림). 메뉴 항목은 `Load Bitmap File`, `Read Georeference File`, `Save Georeference File`, `Clear Current Georeferences`, `Append DS-INTL GEO`, `Import MapInfo TAB`, `Import Bitmap Using TFW`, `Import World File (JGW)`, `Cancel & Return`이다(15행 그림). 그림 링크와 캡션을 포함한다(15–16). 직접 연 로컬 그림은 `models/EFDC/raw/manuals/confluence/spaces/CVLKB/attachments/2818230/worddavf0d36848a64a5933cee1f5040355d2e9.png`이다(15행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행의 `#Setup-Figure1`, `#Setup-Figure2` 링크 대상에 해당하는 앵커 선언이 이 파일에 없다. 13·16행은 캡션이다.
- 10행의 약어 `RMC`는 이 파일에서 풀어 쓰지 않는다.
- 10행은 DSI에서 구할 수 있는 별도 상세 문서를 언급한다. 문서 제목과 링크는 제공하지 않는다.
- 12행 그림의 `X:`와 `Y:` 좌표에는 단위나 좌표계 이름이 표시되어 있지 않다. 본문 10행도 단위와 좌표계 이름을 명시하지 않는다.

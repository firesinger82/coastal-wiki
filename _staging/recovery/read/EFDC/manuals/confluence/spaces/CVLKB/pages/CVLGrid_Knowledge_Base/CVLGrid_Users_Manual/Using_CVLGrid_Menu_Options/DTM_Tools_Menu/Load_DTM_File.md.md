---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Using_CVLGrid_Menu_Options/DTM_Tools_Menu/Load_DTM_File.md
lines: 49
sha256: 1f91a86f1e04d9310d50a5be025d81572539554f333022c9ef1d1b885cd26dae
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Load_DTM_File.md — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — Confluence 페이지의 식별자, 제목, space, URL, 버전, 갱신 시각, 문서 계층과 frontmatter 경계 표식이다(1–9). |
| 10–17 | Load DTM File / 파일 선택·표시 — `Load DTM File`로 파일 선택 창을 열고 `Open` 뒤 DTM을 불러온다고 적는다. 절차 원문: `Selecting the *Load DTM File* allows the user to load a DTM file. This browsing window is shown in [Figure 1](#LoadDTMFile-Figure1). After clicking on *Open* button, the DTM File is loaded as shown in [Figure 2](#LoadDTMFile-Figure2).` (10). Figure 1의 로컬 그림을 직접 열었다(12). 선택된 파일 예시는 `Soudings Sydney Harbour_Bathymetry.dat`이며 형식 선택은 `Grid XYZ Data & DTM Files`이다(12–13). Figure 2의 로컬 그림을 직접 열었다(15). DTM 점들이 표고에 따른 색으로 표시된다. 표고 범례(legend)는 `Elevation (m)`이다. 파랑 끝값은 `-60.905`, 빨강 끝값은 `2.283`이다. 축척 표기는 `2 Kilometers`이다(15–16). 캡션과 빈 줄을 포함한다(11–17). |
| 18–22 | Pointer Utilities — DTM 파일을 불러오면 옆 메뉴에 `Pointer Utilities`가 나타난다. 적용 조건 원문: `When a DTM file loaded, a tool set of *Pointer Utilities* appears on side menu as shown in [Figure 3](#LoadDTMFile-Figure3). These are described in the following sections.` (18). Figure 3의 로컬 그림을 직접 열었다(20). 선택 항목은 `Post Elev's`, `Edit Elev`, `Digitize Pts`, `None`이며 `None`이 선택되어 있다(20–21). 빈 줄과 캡션을 포함한다(18–22). |
| 23–29 | Post Elevations — `Post Elev's`를 선택한 뒤 RMC하면 특정 점의 좌표와 표고(elevation) Z가 노란 글상자에 표시된다. 조건 원문: `Selecting the *Post Elev's* pointer utility displays the coordinates and elevation value (Z) of a specific point on workspace in the yellow text box by RMC as shown in [Figure 4](#LoadDTMFile-Figure4).` (25). Figure 4의 로컬 그림을 직접 열었다(27). 노란 글상자 표기는 `X: 584570.30`, `Y: 2329841.00`, `Z: 4.33`, `I = 157, J = 623`이다. 지도 위에 표시된 표고 예시는 `4.5`, `4.3`, `3.9`, `4.4`, `4.4`이다. 범례는 `Elevation (m)`이며 파랑 끝값은 `3.356`, 빨강 끝값은 `5.207`이다. 축척은 `666.7 Meters`이다(27). 절 제목·캡션과 빈 줄을 포함한다(23–29). |
| 30–36 | Edit Elevation — 특정 점의 Z를 흰 입력칸에 숫자나 연산자(operator)를 입력하여 수정한다. 설명 원문: `When the *Edit Elevation* function is selected a frame appears which allow the user modify elevation value (Z) of a specific point on workspace by entering a number or using operators on the white box as shown in [Figure 5](#LoadDTMFile-Figure5).` (32). Figure 5의 로컬 그림을 직접 열고 확대하여 값을 확인했다(34). `Elevation Adjustment Factor:` 입력칸의 표시값은 `-1`이다. 이 값은 화면 예시이다. 절 제목·캡션과 빈 줄을 포함한다(30–36). |
| 37–46 | Digitize Points — `Digitize points`에서 연속 RMC로 여러 점을 디지타이즈(digitize)한다. X·Y 값을 기록하여 텍스트 파일에 붙여 넣을 수 있다. 조건 원문: `The *Digitize points* function allows the user digitize a series of points by RMC continuously. The X and Y values are recorded and can be pasted to a text file as shown in [Figure 6](#LoadDTMFile-Figure6) and [Figure 7](#LoadDTMFile-Figure7).` (39). Figure 6·7의 로컬 그림을 각각 직접 열었다(41·44). Figure 6은 초록 X 표식의 점들과 노란 정보 상자를 보여 준다. 상자에는 `Number of Pts: 10`, `X: 585274.900`, `Y: 2328513.000`, `Z: 0.000`이 표시된다. 표고 범례는 `Elevation (m)`이며 끝값은 `2.824`, `5.207`이다. 축척은 `668 Meters`이다(41). Figure 7의 텍스트 창은 쉼표로 구분된 세 열의 좌표 예시를 보여 준다. 보이는 1–9번째 자료 행을 전사한다: `587334.700,  2327845.000,     0.000` (44, 그림의 1행); `587174.700,  2328318.000,     0.000` (44, 그림의 2행); `586972.900,  2328589.000,     0.000` (44, 그림의 3행); `586750.200,  2329118.000,     0.000` (44, 그림의 4행); `586381.400,  2329452.000,     0.000` (44, 그림의 5행); `585824.600,  2329278.000,     0.000` (44, 그림의 6행); `585434.900,  2328944.000,     0.000` (44, 그림의 7행); `585448.900,  2328374.000,     0.000` (44, 그림의 8행); `585692.400,  2328088.000,     0.000` (44, 그림의 9행). 그림의 10행은 빈 줄이다(44). 절 제목·캡션과 빈 줄을 포함한다(37–46). |
| 47–49 | None — `None`을 선택하면 앞서 사용한 포인터 유틸리티(pointer utilities)를 모두 종료한다. 설명 원문: `The *None* option allows the user to end all previous pointer utilities.` (49). 절 제목과 빈 줄을 포함한다(47–49). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·18·25·32·39: `#LoadDTMFile-Figure1`부터 `#LoadDTMFile-Figure7`까지 내부 그림 링크를 사용한다. 13·16·21·28·35·42·45행의 캡션에는 대응하는 앵커 정의가 없다.
- 25·39: 본문은 `RMC`를 사용한다. 이 문서에는 약어의 풀이가 없다.
- 39·44: 본문은 기록되는 값으로 X·Y만 언급한다. 44행의 그림은 각 자료 행에 세 번째 열 `0.000`도 표시한다.
- 41·44: Figure 6의 정보 상자는 `Number of Pts: 10`을 표시한다. Figure 7의 텍스트 창에는 자료 행 9개가 보이고 10행은 빈 줄이다.


---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Menu_and_Toolbar_Items/Vertical_Profile_Plots.md
lines: 42
sha256: d996d95f3244d32cde824def70fad83c19aa8dd84b953ba4231e463ba85953f1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Vertical_Profile_Plots.md — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–21 | 수직 프로파일(Vertical Profile) / 수동 셀 지정 — CSS 색상 마크업 뒤에 셀을 먼저 선택하거나 선택하지 않고 그리는 두 방법을 소개한다(10). New Vertical Profile 또는 도구 모음 아이콘으로 창을 열고 셀 수 `#`, 인덱스 `L` 또는 `I`·`J`, 각 행 마지막 체크 상자를 지정한다(12). 필드 원문은 `Primary Group`, `Parameter`, `Add Water Surface and Bottom Elevation`, `Parameters to Plot`이다(12). 수면과 하상 표고의 표시를 체크로 켜거나 끄고 왼쪽 화살표로 변수를 추가한 뒤 Up·Dn으로 순서를 바꾸고 OK로 그림을 만든다(12). 레이아웃 파일·기본 폴더 원문: `VPLayout.VPL`, `#analysis`, `as default` (14). 실측과 비교하려면 Browse로 자료 파일을 지정한다(16). 비교하지 않을 때의 원문: `If we don't want to model result to data, we should clear the data file path for the *Data File* then click the *Update* button before clicking the *OK* button.` (16). 12행의 프로파일 아이콘과 왼쪽 화살표, 그림 1을 직접 열었다(18–20). 그림의 셀 표는 `No. 1`, `L 1531`, `I 66`, `J 27`, 체크 상태이며 Primary Group은 Water Column, Parameter는 Temperature이다. |
| 22–27 | 그림 2 / 수온과 실측 자료 — 그림을 직접 열었다(24–26). X축은 `Water Temperature (°C)`이며 눈금은 `5`, `10`, `15`, `20`, `25`, `30`이다. Y축은 `Elevation (m)`이며 `235.00`부터 `260.00`까지 `2.50` 간격이다. 빨간 선은 셀 `1531 (I:66,J:27)`의 모델 수온이며 시각은 `2013-08-09 02:30`이다. 노란 원 표식은 `Data: 2013-08-09 03:00:00`이다. 하부에서 약 9°C이고 상부에서 약 23–24°C인 수직 분포를 보여 준다. 이 근삿값은 그림을 눈으로 읽은 값이다. |
| 28–37 | 사전 선택한 여러 셀 — 2DH View에서 다중 선택하면 Selected Cells에 셀 수가 채워지며 파일에서 셀을 불러올 수도 있다(28). 그림 3을 직접 열었다(30–32). 표의 세 행은 `1 1248 60 24`, `2 1905 68 31`, `3 2752 53 41`이며 열은 No.·L·I·J이고 세 행 모두 체크되어 있다. 그림 4를 직접 열었다(34–36). X축은 `Water Temperature (°C)`이며 표시 눈금은 `8.38`, `9.77`, `11.17`, `12.57`, `13.96`, `15.36`, `16.76`, `18.15`, `19.55`, `20.95`이다. Y축 `Elevation (m)`는 `235.00`부터 `260.00`까지 `2.50` 간격이다. 시각 `2013-08-05 10:00`에서 셀 1248은 빨간 선, 1905는 파란 선, 2752는 초록 선이며 각각 위로 갈수록 수온이 커지는 프로파일을 보여 준다. |
| 38–42 | 그래프 설정 — 시계열(time series)과 유사한 그래프 도구를 쓰며 축·제목·범례를 오른쪽 클릭하여 편집한다(38). 범례 오른쪽 클릭은 Line Settings를 열고 기능은 링크된 Series Options의 Data Series와 같다고 적는다(38). 그림 5를 직접 열었다(40–42). 셀별 자료 계열(data series)과 선·표식·축·범례 옵션을 보여 준다. 현재 선택 계열의 화면 값은 `X Range: 8.45117855072021`부터 `22.3442268371582`, `Y Range: 235.362869262695`부터 `258.717895507813`, `Index: 1`, `# of Points: 30`, `Invalid Flag: -999`이다. 선은 Solid·빨강·Width 1.0이고 Show Line은 체크되어 있으며 Show Symbols는 해제되어 있다(40행 그림). 값은 화면 예시 값이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16: 비교하지 않을 때의 문장은 `If we don't want to model result to data`로 적혀 있으며 동사가 빠져 있다. 문구를 수정하지 않고 옮겼다.


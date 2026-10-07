---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Model_Time_Control.md
lines: 24
sha256: 86d79d197ba0f83a6793f8f6adbc85526066274401d817d9564f8a11aad7ecf2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Model_Time_Control.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–19 | 모델 시간 제어(Model Time Control) / 시각 이동 — 긴 CSS 색상 마크업 뒤에 실행 결과의 2DH 후처리 지도를 원하는 시각에 표시하는 방법을 설명한다(10). Timing 스크롤 막대와 처음·마지막 시각 버튼을 사용하며 화살표 또는 PgUp/PgDn으로 한 시간 단계(time step)씩 앞뒤로 이동한다(10). Ctrl-G는 특정 날짜로 이동한다(10). 10행의 처음·마지막 이동 아이콘을 직접 열었다. 그림 1은 주 도구 모음의 Timing 영역을 강조한다(12–14). 그림 2는 Go to Date 창이다(16–18). 두 그림을 직접 열었다. 그림 2의 입력 범위 원문은 `Julian: 0.0000 to 10.0000`, `Calendar: 2018-01-01 00:00 to 2018-01-11 00:00`이다(16행 그림). 이는 해당 모델 화면의 범위이다. |
| 20–24 | Time Control Settings / 시간 기준과 애니메이션 — 달력·시간 형식·애니메이션을 설정한다(20). 다른 변수보다 시간 간격이 작은 시계열은 전역 시간(global time)에서 전부 표시되지 않을 수 있다(20). 옵션별 동작 원문: `The *Time of selected layer* option would let the user see the full-time series for such parameter while *Time of Water Surface* would use the global time.` (20). `Use Global` 체크 해제·체크로 유사한 결과를 얻는다(20). 20행 설정 아이콘과 그림 3을 직접 열었다(22–24). 그림은 Gregorian Date와 Time of Water Surface가 선택된 상태이다. 화면 값은 `Precision: 4`, `Format: yyyy-MM-dd HH:mm`, `Time Tolerance (minutes): 0.0052094`, `Snapshot Skip: 1`, `Frame Delay (sec): 0`이다(22행 그림). 본문은 이 값들을 기본값이라고 명시하지 않는다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·20: `#Figure1`, `#Figure2`, `#Figure3` 링크가 있지만 이 Markdown 파일에는 해당 앵커 정의가 없다.


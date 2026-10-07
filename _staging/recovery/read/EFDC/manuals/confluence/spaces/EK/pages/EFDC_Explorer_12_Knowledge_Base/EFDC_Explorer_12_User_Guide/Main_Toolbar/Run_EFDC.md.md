---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Toolbar/Run_EFDC.md
lines: 22
sha256: e8e38bb9a302a61efb4ff145f7d858a118562a76cbbd36518fa47dd1f31f2fc6
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Run_EFDC.md — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Run EFDC / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–16 | Run EFDC / 실행과 저장 — 색상 CSS와 실행 아이콘 그림을 포함한다(10). 실행 기능은 현재 불러온 프로젝트를 실행 전에 디스크에 먼저 저장하지 않는다(12). 사용자가 변경 내용을 실행에 반영하려면 먼저 프로젝트를 저장해야 한다(12). EFDC Run 창은 실행 직전에 주요 실행 시간 설정을 검토하고 변경하도록 한다(14). 이 창에서 변경하면 EEMS가 EFDC 입력 파일을 자동 저장한다고 적는다(14). 원문: `It does not first save to disk the currently loaded EFDC project prior to running.` (12); `Therefore, if the user has made changes that they desire the run to reflect, the user must first save the project.` (12); `EEMS will save the EFDC input files automatically, if changes are made.` (14). 10행 `Run1.jpg`와 16행 `Run2.jpg`의 로컬 사본을 열었다. 첫 그림은 Main Toolbar의 EFDC 실행 아이콘을 표시한다(10). 둘째 그림은 General 탭에서 다중 스레드, 실행 상태, 후처리 출력 간격과 실행 파일 경로를 설정하는 EFDC+ Run Options 화면이다(16). |
| 17–22 | Run EFDC / 실행 파일 지정 — Run 버튼으로 실행하기 전에 실행 파일 경로를 지정해야 한다(18). 선택한 실행 파일이 없으면 연결된 경로의 배경을 연한 빨강으로 바꾼다고 적는다(18). 원문: `The user must first specify the path to the *EFDC executables* before EE can be used to launch an EFDC run using the Run button.` (18); `If the EFDC executable selected does not exist, EEMS will change the associated path background to light red.` (18). 20행 `Run3.jpg`의 로컬 사본을 열었다. 그림은 실행 옵션 창의 실행 파일 경로 오른쪽 찾아보기 버튼을 `Browse` 말풍선과 화살표로 표시한다(20). Figure 2 캡션과 빈 줄을 포함한다(17–22). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12·14: 12행은 실행 전 현재 프로젝트를 먼저 저장하지 않는다고 적는다. 14행은 실행 설정 창에서 변경하면 EFDC 입력 파일을 자동 저장한다고 적는다. 이 파일은 두 저장 동작의 파일별 범위를 추가로 설명하지 않는다.
- 14·18·22: 본문 링크는 `#Figure1`과 `#Figure2`를 사용한다. 이 Markdown 파일에는 해당 ID의 앵커가 없다. Figure 2 캡션은 22행에 있고 Figure 1 캡션은 없다. 18행 링크 뒤에는 닫는 괄호를 링크한 `[)](#Figure2)`와 추가 닫는 괄호가 있다.

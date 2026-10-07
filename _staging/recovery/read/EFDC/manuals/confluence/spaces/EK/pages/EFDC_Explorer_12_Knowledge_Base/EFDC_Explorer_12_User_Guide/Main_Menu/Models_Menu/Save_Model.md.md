---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Models_Menu/Save_Model.md
lines: 39
sha256: a5a9fb19a121de5cce474bf1295b85145db3ec946e018de3e3a72a295b6912fd
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Save_Model.md — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각, 문서 계층 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–19 | Save Model / Save Options — 현재 프로젝트를 쓰기 작업(Write Operation)으로 저장한다(10). 색상 CSS가 설명 문장 앞에 붙어 있다(10). 저장 선택 세 가지의 이름과 조건을 그대로 옮긴다: `- *Full Write* option provides a complete save of all the input files. In a big model, this option can take longer than the following options.` (12); `- *Write All except Time Series Files option*allows saving all the input files except the time series, and is quicker than *Full Write* option. This option is useful if the user has not made any changes to the time series.` (13); `- If the user has only made changes to the formatting options in EFDC+ Explorer, then *Save Profile* option is useful. This is the quickest option of all three. As the models become bigger and bigger, the user must select the appropriate option to quickly save only relevant changes. The profile is always saved for the other save options also.` (14). 그림 `Savemodel.jpg`는 디렉터리 트리, 입력 파일 목록, Full Write·Write All except Time Series Files·Save Profile File Only (EFDC.EE), EEMS 10·EEMS 8.5 형식 선택을 보여 준다(16). Figure 1 캡션과 빈 줄을 포함한다(11·15–19). |
| 20–24 | 필수 입력 파일 생성 / 새 프로젝트 / EE 파일 — 아카이브 파일만 있을 때의 의무 조건은 `If the user only has the "\*.EFDC" archive file and wants to create a set of files that EFDC needs to run that project, *Full Write* option must be selected to create all the required input files.  ` (20). 새 하위 디렉터리를 만들고 OK를 누르면 `.INP` 파일들을 새 디렉터리로 복사한다고 적는다(21). 모델이 사용하지 않는 라벨과 그래프 서식은 프로젝트 디렉터리의 `EFDC.EE`에 저장된다(23). 수동 복사 조건은 `If the user wants to **manually** **copy** a complete EFDC project data set (together with all the ASCII .INP files or the binary archive file) the user should also copy all of the \*.EE files.` (23). `EFDC.EE`는 ASCII 편집기로 편집할 수 있지만 파일 손상을 주의해야 한다고 적는다(23). |
| 25–31 | 모델 저장 형식 — 두 형식의 열기·실행 조건은 `- The model is saved in EEMS 10 format, which means that the model only can be loaded/opened by EE10 and run with EFDC+ 10.` (27); `- The model is saved in EEMS 8.5 format, which means that the model can be loaded/opened by both EE8.5 and EE10, but can be run with EFDC+ 8 only.` (28). EPA GVC Model 형식으로 저장하려면 `If the user wishes to save the model in EPA GVC Model format rather than EFDC+ model format, then this option should be selected in the *Active Modules* tab *Model Selection* frame on the main EFDC+ Explorer form.` (30). 이 방식은 `EFDC.INP`를 다른 모델에 맞게 재서식화한다(30). 모델을 바꿀 때 모든 매개변수가 원하는 값인지 주의해야 한다고 적는다(30). |
| 32–39 | Cross Platform Note / Note — UNIX에서 PC로 입력 파일을 전송하는 조건과 의무는 `*Many users may want to use EFDC on both a PC and a UNIX based computer. When transferring the input files from the UNIX machine to the PC, the carriage control MUST be reset to the Windows/DOS carriage control.*` (36). EFDC+ Explorer의 Toolbox 또는 UNIX 프로젝트 첫 불러오기에서 Windows/DOS 행 제어로 변환할 수 있다고 적는다(38). 같은 기능을 가진 ASCII 편집기도 사용할 수 있다고 적는다(39). 절 제목, 빈 줄, 강조 마크업을 포함한다(32–39). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: `#Figure1` 링크가 있다. 이 파일의 그림 캡션(18)은 굵은 텍스트이며 `Figure1` 앵커는 정의되어 있지 않다.


---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Getting_Started/Saving_a_Project.md
lines: 34
sha256: b8a4d05e4d72df75dbe231adfaeb106dc59e635c08a0babecd116328a78be1d3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Saving_a_Project.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 메타데이터와 저장 진입 — 현재 프로젝트 변경을 저장하려면 도구모음 디스크 버튼 또는 Model의 Save Model을 선택한다(1–12). 로컬 그림 두 개를 열었다(14·17). 첫 그림은 저장 디스크 아이콘, 둘째 그림은 `Save Model Ctrl+S` 메뉴를 강조한다. |
| 19–30 | Write Operation과 Save Options — 저장 디렉터리·저장할 파일·필요하면 새 폴더를 선택한다(19). 21행 로컬 `EE10_5.png`를 열었다. 그림은 `Full Write`가 선택됐고 `Write All except Time Series Files`, `Save Profile File Only (EFDC.EE)`가 선택되지 않은 저장 창이다. 모든 입력은 Full Write, 형식만 바꾼 경우는 Save Profile File Only를 선택한다고 적는다(23–25). 프로필은 다른 저장 옵션에서도 항상 저장되며 `EFDC.EE`에 경계 그룹·보정 지점 이름 등을 담는다(25–27). `.EFDC` 아카이브만 있을 때 실행에 필요한 입력 파일 세트를 만들려면 Full Write를 선택해야 한다(29). 조건·의무 원문: `        3. For a complete save of all the input files select the *Full Write* option.` (23); `         4. If you have only made changes to the formatting options in EFDC+ Explorer and want those saved, select the *Save Profile File Only* option.  The profile is always saved for the other save options also.` (25); `The *Profile File* is the file EFDC.EE, which contain settings of the model such as  the names of boundary groups, calibration stations, etc...` (27); `         5. If the user only has the “\*.EFDC” archive file and wants to create a set of files that EFDC needs to run that project, the user must select the *Full Write* option to create all the input files required.` (29). |
| 31–34 | Format과 버전 호환 — 두 저장 형식의 호환 조건을 제시한다(31–34). 원문: `- EEMS10 models can only viewed and calculated with EE10 and EFDC+ version 10` (33); `- EEMS8.5 models can be viewed by both EE8.5 or EE10 and run with EFDC+ version 8.5` (34). 21행 그림은 `EEMS 10`을 선택하고 `EEMS 8.5`를 선택하지 않은 상태다. 이 기록은 문서에 적힌 버전 조건을 옮겼다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12·15행: 본문은 현재 프로젝트의 Save Model 동작을 설명한다. 첫 그림 캡션은 `Save Model As button (1).`로 적혀 있다.

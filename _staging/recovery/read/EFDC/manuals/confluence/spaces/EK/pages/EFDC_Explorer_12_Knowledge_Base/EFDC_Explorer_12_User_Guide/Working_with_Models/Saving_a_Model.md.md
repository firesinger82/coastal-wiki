---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Working_with_Models/Saving_a_Model.md
lines: 37
sha256: 5a54849d767bcdb2188804cd1f9a658d2874a226c718290550959abee6af4cf4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Saving_a_Model.md — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 앞부분 메타데이터. `title: "Saving a Model"` (3) 및 페이지 ID, space, URL, 버전, 갱신 시각과 문서 계층을 포함한다(1–9). |
| 10–19 | Step-by-step guide / 저장 명령. 열린 프로젝트의 변경 사항은 도구막대 디스크 아이콘 또는 Model → Save Model로 저장한다(12). 그림 14는 빨간 테두리로 강조한 디스크 아이콘이다. 그림 18은 Model 메뉴의 `Save Model` (18)과 `Ctrl+S` (18)를 강조한 화면이다. Figure 1 캡션을 포함한다(16). |
| 20–25 | Select Directory: Write Operation / Save Options. 저장 디렉터리와 작성할 파일 종류를 선택한다(20). 그림 22는 디렉터리 트리와 저장 옵션 화면이다. `Full Write` (22), `Write All except Time Series Files` (22), `Save Profile File Only (EFDC.EE)` (22)가 보인다. Format은 `EEMS 10` (22)과 `EEMS 8.5` (22)이며 Full Write 및 EEMS 10이 선택되어 있다. Figure 3 캡션을 포함한다(24). |
| 26–33 | 전체 입력·프로필(profile) 저장과 아카이브(archive) 해제. Full Write는 모든 입력 파일을 저장한다. 포맷만 바꾼 경우 프로필만 저장하는 선택 사항을 설명하며 다른 저장 옵션에서도 프로필은 항상 저장된다고 적는다. EFDC.EE는 경계 그룹명과 검보정 지점 등의 설정을 포함한다. *.EFDC 아카이브만 있을 때 실행용 입력 파일을 만들려면 Full Write가 필수이다. 원문: `        3. For a complete save of all the input files select the *Full Write* option.` (26) `         4. If you have only made changes to the formatting options in EFDC+ Explorer and want those saved, select the *Save Profile File Only* option.  The profile is always saved for the other save options also.` (28) `The Profile File is the file EFDC.EE, which contains settings of the model such as the name of boundary groups, calibration stations, etc...` (30) `         5. If the user only has the “\*.EFDC” archive file and wants to create a set of files that EFDC needs to run that project, the user must select the *Full Write* option to create all the input files required.` (32) |
| 34–37 | 두 저장 형식의 호환성. EEMS 10의 보기·계산 가능 버전과 EEMS 8.5의 보기·계산 가능 버전을 구분한다. 제한 조건 원문: `- EEMS 10 can only be viewed and calculated by EFDC+ Explorer and EFDC+ version 10.` (36) `- EEMS 8.5 can be viewed by EFDC+ Explorer version 8.4 or 8.5 or 10 and calculated by EFDC+ version 8.4 or 8.5.` (37) |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음


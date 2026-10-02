---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/build/distribute.bat
lines: 29
sha256: 8095e2951bae4a5e6f3d5e810a4f0a39bd8034cce8acd01ce8c881f87ec79648
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# distribute.bat — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SolutionDir·ConfigurationName·TargetDir·Platform 인수를 읽고 문자열의 큰따옴표를 제거(4–13). 원문: `set SolutionDir=%1` (4). 원문: `set ConfigurationName=%2` (5). 원문: `set TargetDir=%3` (6). 원문: `set Platform=%4` (7). 원문: `set SolutionDir=%SolutionDir:"=%` (10). 원문: `set ConfigurationName=%ConfigurationName:"=%` (11). 원문: `set TargetDir=%TargetDir:"=%` (12). 원문: `set Platform=%Platform:"=%` (13). |
| 15–21 | 배포 목적지와 dynamic·bmi 입력 디렉터리를 platform/configuration에 따라 조립(16–18); echo를 켠다(20). 원문: `set DstDir=%SolutionDir%\dist\%Platform%\%ConfigurationName%` (16). 원문: `set SrcDir1=%SolutionDir%\src\xbeachlibrary\bin\dynamic\%Platform%\%ConfigurationName%` (17). 원문: `set SrcDir2=%SolutionDir%\src\xbeachlibrary\bin\bmi\%Platform%\%ConfigurationName%` (18). |
| 22–29 | 기존 배포 DLL은 각각 존재할 때 삭제(23–24); 목적지 디렉터리가 없을 때 생성(25). 각 입력 DLL이 존재할 때만 Library/BMI 이름으로 복사(28–29). 삭제·디렉터리 생성·각 복사는 서로 독립 조건이다. 원문: `if exist "%DstDir%\XBeach.Library.dll" del "%DstDir%\XBeach.Library.dll" /q /f` (23). 원문: `if exist "%DstDir%\XBeach.BMI.dll" del "%DstDir%\XBeach.BMI.dll" /q /f` (24). 원문: `if not exist "%DstDir%" mkdir "%DstDir%"` (25). 원문: `if exist "%SrcDir1%\xbeachlibrary_dynamic.dll" copy "%SrcDir1%\xbeachlibrary_dynamic.dll" "%DstDir%\XBeach.Library.dll"` (28). 원문: `if exist "%SrcDir2%\xbeachlibrary_bmi.dll" copy "%SrcDir2%\xbeachlibrary_bmi.dll" "%DstDir%\XBeach.BMI.dll"` (29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·12: TargetDir을 읽고 따옴표를 제거하지만 이후 경로 생성·복사에는 사용하지 않는다.
- 23–29: 기존 DLL 삭제는 새 입력 DLL 존재 여부를 검사하는 28–29행보다 먼저 실행한다.

---
file: models/XBeach/raw/source_code/trunk/src/xbeach/build/distribute.bat
lines: 32
sha256: 6e9775ed73ee31a84ab1a1804ccf51e73a093801d89b828e79cff3cd07321c0b
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# distribute.bat — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 명령 표시 off/on(1·15). %1..%4에서 SolutionDir·ConfigurationName·TargetDir·Platform을 받음(4–7), 각 변수의 큰따옴표 제거(10–13); 주석·빈 줄 포함. 인수/따옴표 처리 원문: `set SolutionDir=%1` (4), `set ConfigurationName=%2` (5), `set TargetDir=%3` (6), `set Platform=%4` (7), `set SolutionDir=%SolutionDir:"=%` (10), `set ConfigurationName=%ConfigurationName:"=%` (11), `set TargetDir=%TargetDir:"=%` (12), `set Platform=%Platform:"=%` (13). |
| 17–23 | 출력 디렉터리 존재 조건 `if exist "%SolutionDir%\dist\%Platform%\%ConfigurationName%\" rmdir "%SolutionDir%\dist\%Platform%\%ConfigurationName%\" /q /s` (18). 조건 밖 mkdir(19). static의 해당 Platform/ConfigurationName DLL을 TargetDir로 copy(22). |
| 24–32 | 분기 없이 TargetDir의 *.exe·*.dll을 dist 디렉터리로 복사(25–26), manual PDF(29)와 LICENSE(32) 복사; 주석·빈 줄 포함. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–19: 기존 dist 출력 폴더가 있으면 /q /s로 제거한 뒤 같은 폴더를 만든다.
- 32: 마지막 LICENSE 복사 줄은 개행이 없으며 nl 기준 마지막 번호는 32이다.

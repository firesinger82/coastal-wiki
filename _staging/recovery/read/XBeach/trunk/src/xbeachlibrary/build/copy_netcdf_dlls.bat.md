---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/build/copy_netcdf_dlls.bat
lines: 18
sha256: 4248e3b674b848d224b34dc55b541b885cfa121d7d5d3e41e65cdea259556bdd
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# copy_netcdf_dlls.bat — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 네 인수를 SolutionDir·TargetDir·Platform·Configuration으로 읽으며 echo를 끈다(1·4–7). 원문: `set SolutionDir=%1` (4). 원문: `set TargetDir=%2` (5). 원문: `set Platform=%3` (6). 원문: `set Configuration=%4` (7). |
| 9–18 | 변수 안의 큰따옴표를 제거(10–13)한 뒤 echo를 켠다(15). platform/all의 DLL과 platform/netcdf/configuration의 DLL을 대상 경로에 차례로 복사(17–18); 조건 분기는 없다. 원문: `set SolutionDir=%SolutionDir:"=%` (10). 원문: `set TargetDir=%TargetDir:"=%` (11). 원문: `set Platform=%Platform:"=%` (12). 원문: `set Configuration=%Configuration:"=%` (13). 원문: `copy "%SolutionDir%\lib\%Platform%\all\*.dll" "%TargetDir%"` (17). 원문: `copy "%SolutionDir%\lib\%Platform%\netcdf\%Configuration%\*.dll" "%TargetDir%"` (18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–18: 두 copy 명령 앞에 원본 존재 확인이나 대상 디렉터리 생성, 두 명령 사이에 errorlevel 검사가 없다.

---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood.sln
lines: 74
sha256: ba649135aede6265d4b8fc5c22dda77c978a028977c765d7d4756d4efc16f74d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# lisflood.sln — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–8 | 1행은 바이트 순서 표식(byte order mark)이 있는 빈 내용이다. 솔루션 형식·주석·버전은 `Microsoft Visual Studio Solution File, Format Version 12.00` (2), `# Visual Studio 14` (3), `VisualStudioVersion = 14.0.25420.1` (4), `MinimumVisualStudioVersion = 10.0.40219.1` (5)이다. 3행의 `# Visual Studio 14`는 주석이다. 프로젝트 선언은 `Project("{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}") = "lisflood", "lisflood.vcxproj", "{9E49EBA1-7742-4987-BB55-C07BDF06808E}"` (6)이며 `EndProject` (7), `Global` (8)이 이어진다. |
| 9–29 | `GlobalSection(SolutionConfigurationPlatforms) = preSolution` (9)의 구성 이름과 플랫폼(platform)은 `Debug\|Win32 = Debug\|Win32` (10), `Debug\|x64 = Debug\|x64` (11), `Debug\|x86 = Debug\|x86` (12), `Release_double_all_channel\|Win32 = Release_double_all_channel\|Win32` (13), `Release_double_all_channel\|x64 = Release_double_all_channel\|x64` (14), `Release_double_all_channel\|x86 = Release_double_all_channel\|x86` (15), `Release_double\|Win32 = Release_double\|Win32` (16), `Release_double\|x64 = Release_double\|x64` (17), `Release_double\|x86 = Release_double\|x86` (18), `Release_float_all_channel\|Win32 = Release_float_all_channel\|Win32` (19), `Release_float_all_channel\|x64 = Release_float_all_channel\|x64` (20), `Release_float_all_channel\|x86 = Release_float_all_channel\|x86` (21), `Release_float\|Win32 = Release_float\|Win32` (22), `Release_float\|x64 = Release_float\|x64` (23), `Release_float\|x86 = Release_float\|x86` (24), `ReleaseFloat_win32\|Win32 = ReleaseFloat_win32\|Win32` (25), `ReleaseFloat_win32\|x64 = ReleaseFloat_win32\|x64` (26), `ReleaseFloat_win32\|x86 = ReleaseFloat_win32\|x86` (27)이다. 28행에서 이 절을 닫고 `GlobalSection(ProjectConfigurationPlatforms) = postSolution` (29)을 연다. |
| 30–47 | 시작 시 29행 프로젝트 구성 대응 절 안이다. 첫 `Debug` 구성의 대응은 `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Debug\|Win32.ActiveCfg = Debug\|Win32` (30), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Debug\|Win32.Build.0 = Debug\|Win32` (31), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Debug\|x64.ActiveCfg = Debug\|x64` (32), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Debug\|x64.Build.0 = Debug\|x64` (33), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Debug\|x86.ActiveCfg = Debug\|Win32` (34), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Debug\|x86.Build.0 = Debug\|Win32` (35)이다. 이후 `Release_double_all_channel` (36–41)과 `Release_double` (42–47)은 같은 규칙으로 `Win32`와 `x64`를 각각 같은 이름에 대응한다. 각 `.Build.0`은 바로 앞 `.ActiveCfg`와 같은 값을 사용한다. 다른 플랫폼 대응은 `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Release_double_all_channel\|x86.ActiveCfg = Release_double_all_channel\|Win32` (40), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Release_double\|x86.ActiveCfg = Release_double\|Win32` (46)이며 각 다음 행의 `.Build.0`도 같은 `Win32` 값이다. |
| 48–66 | 시작 시 29행 프로젝트 구성 대응 절 안이다. `Release_float_all_channel` (48–53), `Release_float` (54–59), `ReleaseFloat_win32` (60–65)은 각 `Win32`와 `x64`를 같은 이름의 구성에 대응한다. 각 `.Build.0`은 바로 앞 `.ActiveCfg`와 같은 값을 사용한다. `x86` 대응 원문은 `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Release_float_all_channel\|x86.ActiveCfg = Release_float_all_channel\|Win32` (52), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Release_float\|x86.ActiveCfg = Release_float\|Win32` (58), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.ReleaseFloat_win32\|x86.ActiveCfg = ReleaseFloat_win32\|Win32` (64)이며 각 다음 행의 `.Build.0`도 같은 `Win32` 값이다. 66행에서 구성 대응 절을 닫는다. |
| 67–74 | 솔루션 속성은 `GlobalSection(SolutionProperties) = preSolution` (67), `HideSolutionNode = FALSE` (68)이며 69행에서 닫는다. Subversion 절은 `GlobalSection(SubversionScc) = preSolution` (70), `Svn-Managed = True` (71), `Manager = AnkhSVN - Subversion Support for Visual Studio` (72)이다. `EndGlobalSection` (73), `EndGlobal` (74)로 끝난다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–27·30–65: 솔루션은 `x86` 플랫폼 이름을 포함한다. `x86`의 실제 프로젝트 구성 대응은 모두 `Win32`를 사용한다.

---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood_intel.sln
lines: 31
sha256: 939e7b340370df243abff921f45e3d537251ccb02adfe97e667ffd24039eb2c1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# lisflood_intel.sln — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–8 | 1행은 바이트 순서 표식(byte order mark)이 있는 빈 내용이다. 솔루션 형식·주석·버전은 `Microsoft Visual Studio Solution File, Format Version 12.00` (2), `# Visual Studio 2013` (3), `VisualStudioVersion = 12.0.31101.0` (4), `MinimumVisualStudioVersion = 10.0.40219.1` (5)이다. 3행의 `# Visual Studio 2013`은 주석이다. 프로젝트 선언은 `Project("{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}") = "lisflood_intel", "lisflood_intel.vcxproj", "{9E49EBA1-7742-4987-BB55-C07BDF06808E}"` (6)이다. `EndProject` (7), `Global` (8)이 이어진다. |
| 9–16 | `GlobalSection(SolutionConfigurationPlatforms) = preSolution` (9)의 구성 이름은 `Debug\|x64 = Debug\|x64` (10), `Release_double_all_channel\|x64 = Release_double_all_channel\|x64` (11), `Release_double\|x64 = Release_double\|x64` (12), `Release_float_all_channel\|x64 = Release_float_all_channel\|x64` (13), `Release_float\|x64 = Release_float\|x64` (14)이다. 모두 `x64` 플랫폼이다. 15행에서 구성 절을 닫고 `GlobalSection(ProjectConfigurationPlatforms) = postSolution` (16)을 연다. |
| 17–31 | 시작 시 16행 프로젝트 구성 대응 절 안이다. 첫 구성의 대응은 `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Debug\|x64.ActiveCfg = Debug\|x64` (17), `{9E49EBA1-7742-4987-BB55-C07BDF06808E}.Debug\|x64.Build.0 = Debug\|x64` (18)이다. 나머지 `Release_double_all_channel\|x64` (19–20), `Release_double\|x64` (21–22), `Release_float_all_channel\|x64` (23–24), `Release_float\|x64` (25–26)도 각각 `.ActiveCfg`와 `.Build.0`에 같은 이름의 구성을 지정한다. 27행에서 구성 대응 절을 닫는다. `GlobalSection(SolutionProperties) = preSolution` (28), `HideSolutionNode = FALSE` (29)로 솔루션 속성을 지정하고 30–31행에서 절과 전체를 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

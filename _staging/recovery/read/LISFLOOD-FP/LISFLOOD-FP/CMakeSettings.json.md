---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/CMakeSettings.json
lines: 73
sha256: d024d462a4f994fd3585340cb037b56a8dcfd478c207eb247ea944a1c4f5cf40
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CMakeSettings.json — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–14 | 객체 시작(1)과 주석 `// See https://go.microsoft.com/fwlink/?linkid=834763 for more information about this file.` (2), `"configurations": [` (3) 다음 첫 구성을 연다(4). 구성은 `"name": "msvc-x64-Debug"` (5), `"generator": "Ninja"` (6), `"configurationType": "Debug"` (7), `"inheritEnvironments": [ "msvc_x64_x64" ]` (8)이다. 경로는 `"buildRoot": "${projectDir}\\out\\build\\${name}"` (9), `"installRoot": "${projectDir}\\out\\install\\${name}"` (10)이다. 인수는 `"cmakeCommandArgs": ""` (11), `"buildCommandArgs": "-v"` (12), `"ctestCommandArgs": ""` (13)이다. 14행에서 구성을 닫는다. |
| 15–25 | 두 번째 구성은 `"name": "msvc-x64-Release"` (16), `"configurationType": "Release"` (18)이다. `"generator": "Ninja"` (17), `"inheritEnvironments": [ "msvc_x64_x64" ]` (19), `"buildRoot": "${projectDir}\\out\\build\\${name}"` (20), `"installRoot": "${projectDir}\\out\\install\\${name}"` (21), `"cmakeCommandArgs": ""` (22), `"buildCommandArgs": "-v"` (23), `"ctestCommandArgs": ""` (24)는 첫 구성과 같다. 중괄호·쉼표를 포함한다. |
| 26–48 | 세 번째 구성은 `"name": "intel-x64-Debug"` (27), `"configurationType": "Debug"` (29)이다. 공통 항목은 `"generator": "Ninja"` (28), `"inheritEnvironments": [ "msvc_x64_x64" ]` (30), `"buildRoot": "${projectDir}\\out\\build\\${name}"` (31), `"installRoot": "${projectDir}\\out\\install\\${name}"` (32), `"cmakeCommandArgs": ""` (33), `"buildCommandArgs": "-v"` (34), `"ctestCommandArgs": ""` (35)이다. `"variables": [` (36)에서 `"name": "CMAKE_C_COMPILER"` (38), `"value": "icl.exe"` (39), `"type": "FILEPATH"` (40)와 `"name": "CMAKE_CXX_COMPILER"` (43), `"value": "icl.exe"` (44), `"type": "FILEPATH"` (45)를 지정한다. 나머지는 객체·배열 구분자이다. |
| 49–73 | 네 번째 구성은 `"name": "intel-x64-Release"` (50), `"configurationType": "Release"` (52)이다. `"generator": "Ninja"` (51), `"inheritEnvironments": [ "msvc_x64_x64" ]` (53), `"buildRoot": "${projectDir}\\out\\build\\${name}"` (54), `"installRoot": "${projectDir}\\out\\install\\${name}"` (55), `"cmakeCommandArgs": ""` (56), `"buildCommandArgs": "-v"` (57), `"ctestCommandArgs": ""` (58)를 지정한다. `"variables": [` (59) 안의 `CMAKE_C_COMPILER` (61)와 `CMAKE_CXX_COMPILER` (66)는 각각 `"value": "icl.exe"` (62·67), `"type": "FILEPATH"` (63·68)이다. 70–73행에서 변수 배열·구성·전체 객체를 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

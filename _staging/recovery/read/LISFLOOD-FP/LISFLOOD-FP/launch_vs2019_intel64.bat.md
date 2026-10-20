---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/launch_vs2019_intel64.bat
lines: 2
sha256: eff95f01d31386a35f180695dd68c5e5ff42654a01d5942a2cb94e096f246d0e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# launch_vs2019_intel64.bat — 판독 구간 기록

구간은 1행부터 2행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–2 | Intel 64비트 환경 설정 배치를 `call "C:\Program Files (x86)\IntelSWTools\compilers_and_libraries\windows\bin\ipsxe-comp-vars.bat" intel64 vs2019` (1)로 호출한다. 이어서 `start "VS2019" /B "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe"` (2)로 Visual Studio를 시작한다. `intel64`, `vs2019`, `VS2019`, `/B`와 두 설치 경로는 원문 값이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–2: Intel 환경 설정 배치와 Visual Studio 2019 Community 실행 파일은 `C:\Program Files (x86)` 아래의 고정 경로를 사용한다.

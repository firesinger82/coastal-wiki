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
| 1–16 | echo를 끄고 명령행 인자 `%1..%4`를 각각 `SolutionDir`, `ConfigurationName`, `TargetDir`, `Platform`에 넣는다(1–7). 각 값의 큰따옴표를 제거한 뒤 echo를 켠다(9–15); 빈 줄도 포함한다. |
| 17–23 | `dist\%Platform%\%ConfigurationName%`가 있으면 `rmdir /q /s`로 제거하고 다시 만든다(17–19). `src\xbeachlibrary\bin\static\%Platform%\%ConfigurationName%\*.dll`을 TargetDir로 복사한다(21–22). |
| 24–32 | TargetDir의 모든 exe·dll을 배포 디렉터리로 복사한다(24–26). 고정 경로 `doc\manual\xbeach_manual.pdf`와 루트 `LICENSE`도 같은 곳에 복사한다(28–32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18: 기존 배포 디렉터리를 `/q /s` 옵션으로 제거한 뒤 다시 생성한다.
- 4–32: 인자 개수 검사나 복사·디렉터리 작업 뒤의 errorlevel 검사·실패 분기가 없다.

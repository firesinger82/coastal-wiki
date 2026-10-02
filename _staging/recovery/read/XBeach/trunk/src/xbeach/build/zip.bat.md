---
file: models/XBeach/raw/source_code/trunk/src/xbeach/build/zip.bat
lines: 26
sha256: 291266134d43ca97e8c32d63f44bfc29fbc7fec1143246722d83c40bb5a1a91d
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# zip.bat — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | echo를 끄고 `%1..%3`을 `SolutionDir`, `ConfigurationName`, `Platform`에 넣으며 큰따옴표를 제거하고 echo를 다시 켠다(1–13). |
| 15–22 | 상대경로 `build\7za.exe`를 배포 디렉터리에 복사하고 그 디렉터리로 이동한다(15–18). `7za.exe a "xbeach_%ConfigurationName%_%Platform%.zip" *`로 압축한 뒤 `7za.exe d … 7za.exe`로 압축 안의 도구를 제거한다(20–21). |
| 23–26 | `%SolutionDir%\src\xbeach\`로 이동한 뒤 배포 디렉터리에 복사했던 `7za.exe`를 삭제한다(23–26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16: 압축 도구 원본 경로 `build\7za.exe`는 현재 디렉터리 기준 상대경로다.
- 18·23: 디렉터리 이동에 `cd`를 사용하고 `/d` 옵션은 없다.
- 4–26: 인자 개수나 각 명령의 errorlevel 검사 없이 복사·이동·압축·삭제를 이어 실행한다.

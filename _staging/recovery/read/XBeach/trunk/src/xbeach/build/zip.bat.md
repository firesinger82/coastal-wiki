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
| 1–14 | echo off/on(1·13). %1..%3에서 SolutionDir·ConfigurationName·Platform을 받음(4–6), 각 변수의 큰따옴표 제거(9–11). 인수/따옴표 처리 원문: `set SolutionDir=%1` (4), `set ConfigurationName=%2` (5), `set Platform=%3` (6), `set SolutionDir=%SolutionDir:"=%` (9), `set ConfigurationName=%ConfigurationName:"=%` (10), `set Platform=%Platform:"=%` (11). |
| 15–26 | build\7za.exe를 dist로 copy(16)하고 그 디렉터리로 이동(18). `7za.exe a "xbeach_%ConfigurationName%_%Platform%.zip" *` (20), `7za.exe d "xbeach_%ConfigurationName%_%Platform%.zip" 7za.exe` (21). src\xbeach로 이동(23) 후 dist의 7za.exe 삭제(26). 조건 분기 없음; 주석·빈 줄 포함. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·18·20: 7za.exe를 상대 경로 build에서 복사하며 압축 입력은 작업 디렉터리의 *이다.
- 26: 마지막 삭제 줄은 개행이 없으며 nl 기준 마지막 번호는 26이다.

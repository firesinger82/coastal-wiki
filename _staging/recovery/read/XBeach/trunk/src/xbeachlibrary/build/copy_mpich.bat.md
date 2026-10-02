---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/build/copy_mpich.bat
lines: 33
sha256: 82f148ce3215d81b1b0780af65c5ac55b2d5d660377637d081022c9ae6acd5e5
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# copy_mpich.bat — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | echo off 후 인수 `%1` SolutionDir·`%2` TargetDir·`%3` 플랫폼(win32/x64)을 출력(2–4). 기존 `%2\mpich\`가 있으면 `rmdir ... /s /q`로 제거(7). |
| 9–16 | `C:\Program Files (x86)\` 존재 및 `%3==win32`일 때 64비트 머신의 32비트 빌드 경로(9). 로컬 MPICH2가 있으면 `xcopy ... %2\mpich\ /s` 후 `GOTO:EOF`(11–14). |
| 17–24 | else 블록은 기본 `C:\Program Files\MPICH2\`를 찾아 하위 디렉터리까지 복사하고 종료(18–21). 설치본이 없으면 다음 저장소 포함 파일 경로로 진행. |
| 25–30 | `%3==x64`이면 `%1\lib\x64\mpich\*.*`를 `%2\mpich\`로 `xcopy /s`, 종료(26–29). |
| 31–33 | 나머지 플랫폼은 `%1\lib\win32\mpich\*.*`에서 대상 mpich 폴더로 복사(32–33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·13·20·28·33: 존재 검사/복사 원본은 따옴표를 쓰지만 rmdir 경로와 xcopy 대상 `%2\mpich\`에는 스크립트 자체의 따옴표가 없다.
- 9·26: 플랫폼 비교는 `%3==win32`·`%3==x64`로 고정되어 있으며, 그 외 값은 마지막 win32 복사 경로로 진행한다(32–33).

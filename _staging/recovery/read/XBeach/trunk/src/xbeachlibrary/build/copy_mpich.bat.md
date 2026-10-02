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
| 1–8 | 명령 echo를 끄고 SolutionDir·TargetDir·platform 인수를 출력(1–4). 기존 대상 mpich 디렉터리가 존재할 때만 재귀·강제 삭제 명령을 실행한다(7). 원문: `if exist "%2\mpich\" rmdir %2\mpich\ /s /q` (7). |
| 9–23 | 9행은 Program Files (x86) 존재 검사와 `%3==win32` 검사를 연쇄한다. 안쪽 11행의 로컬 MPICH2 경로가 존재하면 복사하고 `GOTO:EOF`로 종료(13–14). 16행 else는 `%3==win32` 분기에 대응하며 그 안의 18행 기본 설치 경로가 존재할 때 복사·종료(20–21). 원문: `if exist "C:\Program Files (x86)\" if %3==win32 (` (9). 원문: `if exist "c:\Program Files (x86)\MPICH2\" (` (11). 원문: `xcopy "C:\Program Files (x86)\MPICH2\*.*" %2\mpich\ /s` (13). 원문: `GOTO:EOF` (14). 원문: `)` (15). 원문: `) else (` (16). 원문: `if exist "C:\Program Files\MPICH2\" (` (18). 원문: `xcopy "C:\Program Files\MPICH2\*.*" %2\mpich\ /s` (20). 원문: `GOTO:EOF` (21). 원문: `)` (22). 원문: `)` (23). |
| 24–33 | 앞 로컬 설치 복사에서 종료하지 않은 흐름. x64 조건이면 저장소 lib/x64/mpich를 복사하고 종료(26–30); 이후 win32 복사 명령은 그 조건 블록 밖이며 여기까지 도달하면 실행한다(32–33). 원문: `if %3==x64 (` (26). 원문: `xcopy "%1\lib\x64\mpich\*.*" %2\mpich\ /s` (28). 원문: `GOTO:EOF` (29). 원문: `)` (30). 원문: `xcopy "%1\lib\win32\mpich\*.*" %2\mpich\ /s` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·13·20·28·33: 대상 `%2\mpich\` 경로 인수에 따옴표가 없고 소스 경로에는 따옴표가 있다.
- 9·16–23: 기본 Program Files 탐색은 안쪽 platform 조건의 else에 있으며 바깥 Program Files (x86) 존재 조건은 단일 명령의 연쇄 형태다.
- 13–14·20–21·28–29: xcopy 뒤에 성공 여부를 검사하지 않고 `GOTO:EOF`를 실행한다.

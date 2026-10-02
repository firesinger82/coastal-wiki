---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/includes/version/makeversiondat.bat
lines: 20
sha256: 092e389ba2ba06acd9cbab261fb058a437e931bc457c4f67d1d1a600b32e8e8b
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# makeversiondat.bat — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | echo 비활성화(1). 실행파일 기본 경로 `SET exe=C:\Program Files\TortoiseSVN\bin\SubWCRev.exe`(3), 성공 flag `SET ok=0`(4); 빈 줄 포함. |
| 6–11 | `IF NOT DEFINED RevisionNumber (`(6) 안에서 `IF EXIST "%exe%" (`(7)일 때만 `"%exe%" "%cd%" "%cd%\includes\version\version.tpl" "%cd%\includes\version\version.dat"`(8) 실행. 그 안의 `IF ERRORLEVEL 1 (SET ok=0) ELSE (SET ok=1)`(9)로 성공 여부 설정. 11행은 바깥 조건의 ELSE 시작. |
| 12–17 | `RevisionNumber`가 정의된 바깥 ELSE(11)에서 `echo Build_Revision = '%RevisionNumber%' > version.dat`(12), `echo Build_Date     = '%DATE:~3,10% %TIME:~0,8%' >> version.dat`(13), `echo Build_URL      = 'http://svn.oss.deltares.nl/repos/xbeach/trunk/' >> version.dat`(14)로 현재 디렉터리에 파일 생성·추가; ok=1(15), 블록 종료·빈 줄(16–17). |
| 18–20 | 앞 분기 종료 후 독립적으로 `IF %ok%==0 (`(18)이면 `copy "%cd%\includes\version\version.000" "%cd%\includes\version\version.dat"`(19)로 대체 파일 복사. 20행 닫는 괄호까지 포함. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3: SubWCRev 실행파일 위치가 `C:\Program Files\TortoiseSVN\bin\SubWCRev.exe`로 고정되어 있다.
- 8·12–14·19: SubWCRev·fallback은 `includes\version\version.dat`에 쓰지만 `RevisionNumber` 정의 분기는 현재 디렉터리의 `version.dat`에 쓴다.
- 13–14: 날짜·시간 문자열은 고정 substring 위치를 사용하고 Build_URL은 SVN trunk 주소 문자열로 고정되어 있다.

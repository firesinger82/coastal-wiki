---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/build/copy_netcdf_dlls.bat
lines: 18
sha256: 4248e3b674b848d224b34dc55b541b885cfa121d7d5d3e41e65cdea259556bdd
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# copy_netcdf_dlls.bat — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | echo off, 명령행 `%1..%4`를 SolutionDir·TargetDir·Platform·Configuration으로 설정(4–7). 기본값이나 인수 검사 없음. |
| 9–14 | 각 변수에서 `"`를 빈 문자열로 치환해 인수의 따옴표 제거(10–13). |
| 15–18 | echo on 후 `lib\%Platform%\all\*.dll`(17), `lib\%Platform%\netcdf\%Configuration%\*.dll`(18)을 따옴표로 감싼 TargetDir로 순서대로 copy. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–18: 두 copy 명령 전에 원본 존재·대상 디렉터리 생성 검사가 없고, 뒤에 errorlevel 검사도 없다.

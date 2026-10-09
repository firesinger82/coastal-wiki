---
file: models/ADCIRC/raw/source_code/adcirc/util/strip_cr.bat
lines: 2
sha256: effbcf8b8dbbce9a41af910b7ab1e4ee2f241304a5768040d7c5f0cb0a89c9b0
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# strip_cr.bat — 판독 구간 기록

구간은 1행부터 2행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–2 | 실행 명령 원문은 `c:\progra~1\misc_utils\dos2unix.exe adcirc.f cstart.f global.f global_3dvs.f harm.f hstart.f itpackv.f messenger.f read_input.f sizes.f timestep.f vsmy.f wind.f` (1)이다. 고정된 Windows 실행 파일 경로에 나열한 Fortran 파일을 인수로 전달한다. 다음 실행 명령 `pause` (2)는 입력 대기를 요청한다. 조건 분기는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1: dos2unix.exe의 위치와 처리 파일 목록을 명령에 고정한다. 처리 파일은 상대경로이다.
- 1–2: 실행 파일·처리 파일의 존재 여부나 종료 코드를 검사하는 명령은 없다.

---
file: models/ADCIRC/raw/source_code/adcirc/util/add_cr.bat
lines: 2
sha256: 5a96a36d03ec4d8cbf5677bec6aedccdb40502b5f4c442692aeb67029dcbf71e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# add_cr.bat — 판독 구간 기록

구간은 1행부터 2행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–2 | 배치 파일(batch file)의 첫 실행 명령은 `c:\progra~1\misc_utils\unix2dos.exe adcirc.f cstart.f global.f global_3dvs.f harm.f hstart.f itpackv.f messenger.f read_input.f sizes.f timestep.f vsmy.f wind.f` (1). 고정 경로의 unix2dos.exe에 나열된 Fortran 파일명을 인수로 전달한다. 다음 명령은 `pause` (2). 조건 분기와 반복문은 없다. 실행파일 내부는 이 판독 대상에 포함하지 않았다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1: 실행파일 경로는 c:\progra~1\misc_utils\unix2dos.exe로 고정되어 있다. 입력 파일명 목록도 명령 줄에 고정되어 있다.
- 1–2: 첫 명령의 반환 상태를 검사하는 조건문이 없다. 다음 명령은 pause이다.

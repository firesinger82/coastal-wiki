---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_log.f90
lines: 40
sha256: c2f8f8852ab33947eb29045520f8edf48f0259f41c6391a52d6adea52e21385b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_log.f90 — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | `sfincs_log` 모듈 시작(1). 모듈 변수 integer fid·character(256) logstr 선언(3–4). contains(6). 선언의 초기값은 없다. 구분 주석·빈 줄도 포함한다. |
| 8–16 | `open_log()` 시작·implicit none(8–10). 고정 장치 번호 대입은 `fid = 777` (12). `open(unit = fid, file = 'sfincs.log')` (13)으로 로그 파일을 연다. 루틴 종료·구분 주석·빈 줄(14–16). |
| 17–31 | `write_log(str, to_screen)` 시작·implicit none(17–19). str은 character(*) intent(in), to_screen은 integer intent(in)(21–22). `write(fid,'(a)')trim(str)` (24)로 항상 로그 파일에 후행 공백을 제거한 문자열을 쓴다. `if (to_screen==1) then` (26)이면 `write(*,'(a)')trim(str)` (27)로 화면에도 쓴다. 조건·루틴 종료·주석·빈 줄(28–31). |
| 32–40 | `close_log()` 시작·implicit none(32–34). `close(fid)` (36)로 로그 장치를 닫는다. 루틴·모듈 종료와 주석·빈 줄(37–40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–13: 로그 장치 번호는 777로 고정되어 있다. 로그 파일명은 sfincs.log로 고정되어 있다.
- 13·24·27·36: open·write·close에는 iostat 또는 err 인수가 없다. open에는 status·position·action 지정도 없다.
- 24–28: 모든 write_log 호출은 파일에 문자열을 쓴다. 화면 출력 조건은 to_screen==1뿐이다. 화면 출력의 else는 없다.

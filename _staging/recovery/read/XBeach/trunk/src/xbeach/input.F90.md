---
file: models/XBeach/raw/source_code/trunk/src/xbeach/input.F90
lines: 48
sha256: 4ba74d401b7f6319f59fa2bebaa546f1470aca76b74f402cc0372c9a2a8e0b04
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# input.F90 — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | process_input 모듈은 iso_c_binding·libxbeach_module 사용(1–3). readinput은 integer(c_int), arg 길이 100·version 길이 500(7–11). 반환값 0 초기화(13), command_argument_count 호출(15). 원문(readinput 루틴(7행)): `character(len=100) :: arg` (9). 원문(readinput 루틴(7행)): `character(len=500) :: version` (10). 원문(readinput 루틴(7행)): `readinput = 0` (13). 원문(readinput 루틴(7행)): `narguments = command_argument_count()` (15). |
| 16–28 | 구간 첫 행에 열려 있는 범위: readinput 루틴(7행). narguments>0인 분기에서 iarg=1..narguments를 순회해 get_command_argument(19). 그 안 '-V'일 때 getversion(22), 버전 안내 출력(23–25), readinput=1(26). 해당 옵션 if는 27에서 끝나며 28은 바깥 인수 루프 안 빈 줄. 원문(readinput 루틴(7행)): `if (narguments > 0) then` (16). 원문(readinput 루틴(7행) → 16행 if 참 분기): `do iarg=1,narguments` (17). 원문(readinput 루틴(7행) → 16행 if 참 분기 → 17행 do 반복 안): `call get_command_argument(iarg,arg)` (19). 원문(readinput 루틴(7행) → 16행 if 참 분기 → 17행 do 반복 안): `if (arg=='-V') then` (21). 원문(readinput 루틴(7행) → 16행 if 참 분기 → 17행 do 반복 안 → 21행 if 참 분기): `call getversion(version)` (22). 원문(readinput 루틴(7행) → 16행 if 참 분기 → 17행 do 반복 안 → 21행 if 참 분기): `readinput = 1` (26). |
| 29–48 | 구간 첫 행에 열려 있는 범위: readinput 루틴(7행) → 16행 if 참 분기 → 17행 do 반복 안. 첫 행은 16행 narguments 참 분기와 17행 인수 루프 안이며 '-V' if 밖이다. 별도 '-h' 또는 '--help' 조건에서 환영·usage·options 출력(30–41), readinput=1(42). 옵션 if·루프·narguments if 종료(43–45), 함수·모듈 종료 및 빈 줄(46–48). 원문(readinput 루틴(7행) → 16행 if 참 분기 → 17행 do 반복 안): `if (arg.eq.'-h' .or. arg.eq.'--help') then` (29). 원문(readinput 루틴(7행) → 16행 if 참 분기 → 17행 do 반복 안 → 29행 if 참 분기): `readinput = 1` (42). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24: 안내 문자열에 버전 1.23 및 XBeachX release가 하드코딩되어 getversion 결과와 함께 출력된다.
- 29·38–40: -h/--help를 처리하지만 출력 Options 목록에는 -V만 적혀 있다.

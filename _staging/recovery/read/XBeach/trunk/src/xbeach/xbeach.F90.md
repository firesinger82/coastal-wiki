---
file: models/XBeach/raw/source_code/trunk/src/xbeach/xbeach.F90
lines: 33
sha256: 5b8347e6df5b68eceb7127964a6424cd8a14aa463aca949827b1051d45c634d6
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# xbeach.F90 — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | program xbeach에서 libxbeach의 executestep·init·final·outputext, introspection의 getdoubleparameter, iso_c_binding의 c_double, process_input의 readinput, xmpi의 halt_program 가져오기(1–6). implicit none·rc·t/tstop 선언과 빈 줄(7–11). |
| 12–20 | rc 초기화(13) 후 readinput 호출(14). rc=1일 때 halt_program(15–17). 이 if 밖에서 init 호출(19); 주석·빈 줄 포함. 원문(조건 분기 밖): `rc = 0` (13). 원문(조건 분기 밖): `rc = readinput()` (14). 원문(조건 분기 밖): `if (rc.eq.1) then` (15). 원문(15행 if 참 분기): `call halt_program` (16). 원문(조건 분기 밖): `rc = init()` (19). |
| 21–33 | getdoubleparameter로 t·tstop 취득(22–23). t<tstop 반복 안 executestep(25), t 재취득(26), outputext(28). 루프 종료 뒤 final(32), program 종료(33). 원문(조건 분기 밖): `rc = getdoubleparameter("t", t)` (22). 원문(조건 분기 밖): `rc = getdoubleparameter("tstop", tstop)` (23). 원문(조건 분기 밖): `do while (t<tstop)` (24). 원문(24행 do 반복 안): `rc = executestep()` (25). 원문(24행 do 반복 안): `rc = getdoubleparameter("t", t)` (26). 원문(24행 do 반복 안): `rc = outputext()` (28). 원문(조건 분기 밖): `rc = final()` (32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·22–28·32: 각 라이브러리 반환값을 rc에 받지만 readinput의 rc=1 검사 이후에는 rc를 검사하는 문장이 없다.

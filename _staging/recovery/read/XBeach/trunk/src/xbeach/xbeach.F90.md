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
| 1–11 | 주 프로그램 `xbeach`는 실행 라이브러리 `executestep/init/final/outputext`, 매개변수 조회 `getdoubleparameter`, `c_double`, `readinput`, `halt_program`을 가져온다(1–6). `implicit none`, 정수 반환코드 rc와 배정밀도 시간 t·tstop을 선언한다(7–10). |
| 12–20 | `rc=0` 뒤 `readinput()`을 호출한다(12–14). 반환값 1이면 `halt_program`을 호출하고, 이어 `rc=init()`을 수행한다(15–19). |
| 21–33 | `getdoubleparameter("t", t)` 및 `("tstop", tstop)`로 시간을 읽는다(22–23). `t<tstop` 동안 `executestep`, t 재조회, `outputext` 순서로 호출한다(24–29). 루프 종료 후 `final()`을 호출하고 프로그램을 끝낸다(31–33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·22–28·32: 각 함수의 반환코드를 rc에 저장하지만 `readinput` 뒤의 비교(15) 외에는 rc를 검사하는 분기가 없다.
- 23–29: tstop은 루프 전에 한 번만 조회하고 t는 매 timestep 뒤 다시 조회한다.

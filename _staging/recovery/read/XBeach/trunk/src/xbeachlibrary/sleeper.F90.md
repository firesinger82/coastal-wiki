---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/sleeper.F90
lines: 55
sha256: b72c55685d6429c2c93c19d3477e5caf9d8295f2d5d44d2eba5d22cabf9f7a70
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# sleeper.F90 — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 마이크로초 sleep 목적 주석(1–2), `sleeper` 모듈. `#if __GFORTRAN__` (4)에서 iso_c_binding·C 이름 usleep인 서브루틴 인터페이스·`integer(c_int), value :: i` (5–13). `#else` (14)는 implicit none/save만(15–16). private·공개 myusleep·contains(18–21). |
| 22–26 | `#if __GFORTRAN__` (22)의 `myusleep(i)`: integer 입력을 `usleep(i)`에 그대로 전달(23–26). |
| 27–34 | 같은 전처리 선택의 병렬 `#elif __INTEL_COMPILER` (27): `j = i/1000` (31), `j = max(1,j)` (32), `sleepqq(j)` 호출(33). |
| 35–42 | 같은 전처리 선택의 병렬 `#elif __PGI` (35): `j = i/1000` (39), `j = max(1,j)` (40), `sleepqq(j)` (41). |
| 43–55 | 전처리 `#else` (43): fallback의 `j = i/1000000` (48), `j = max(0,j)` (49), `sleep(j)` (51). 50은 비활성 최소 1초 제안 주석. 루틴·전처리·모듈 끝(52–55). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45·48–51: fallback 주석은 전혀 sleep하지 않는다고 쓰지만 실행문은 초 단위로 정수 나눗셈하고 `sleep(j)`를 호출한다.
- 31–33·39–41·48–51: Intel/PGI 분기는 j를 최소 1로 제한하며, fallback은 최소 0으로 제한한다. GNU 분기는 입력 i를 변환하지 않는다.

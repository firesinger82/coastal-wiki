---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/constants.F90
lines: 40
sha256: 43f6465359b2f942cfe3b5a77d7a4b7c085ad0a4d1a92f8a462db6a50588b6b1
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# constants.F90 — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 공통 kind·pi·허수단위 모듈의 문서 머리말, 저작권(2004 WL Delft)·작성자. 19–21은 never used 및 pi/twopi 저장 위치 제안 주석. |
| 23–28 | `constants` 모듈, implicit none·save·private. spkind/dpkind/pi/compi/iFill/sFill/dFill 공개(27). |
| 29–33 | `spkind=kind(1.0)`, `dpkind=kind(1.0d0)`(29–30), `pi=4*atan(1.0_dpkind)`(31), 복소 허수단위 `compi=(0.0_dpkind,1.0_dpkind)`(32), 모두 parameter. |
| 34–40 | 채움값 `iFill=-huge(0)`, `sFill=-huge(0.0)`, `dFill=-dble(huge(0.0))`(35–37). dFill을 sFill보다 작게 만들지 않기 위한 방식이라는 주석(37), 모듈 끝·문서 종료 표시. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37: real*8 dFill은 배정밀도 huge를 직접 취하지 않고 기본 real의 huge를 dble로 변환한 값이다.

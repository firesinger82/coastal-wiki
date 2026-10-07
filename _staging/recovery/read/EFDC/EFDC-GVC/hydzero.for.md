---
file: models/EFDC/raw/source_code/EFDC-GVC/hydzero.for
lines: 49
sha256: aa6af9442b6cb200c879bc98263aed6bb165e8ccd437089c493f806eb18885ce
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# hydzero.for — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 구분 주석과 `SUBROUTINE HYDZERO` 입구(6). 머리말은 이진 유동 배열(binary hydrodynamic array)을 0.0으로 초기화한다고 적고 작성자·버전·수정 날짜를 나열한다(10–24). `EFDC.PAR`·`EFDC.CMN`을 포함한다(29–30). 빈 줄과 구분 주석을 포함한다. |
| 32–44 | 시작 시 6행 `SUBROUTINE HYDZERO` 루틴 안. K=1..KC 바깥 루프와 LL=2..LA 안쪽 루프를 연다(32–33). LL 인덱스의 SELSUM/DEPSUM/VXXSUM/VYYSUM/QXXSUM/QYYSUM 여섯 배열을 0.0으로 설정한다(37–42). 두 루프를 종료한다(43–44). 유동 변수 초기화 주석도 이 구간에 포함한다(35). 원문(조건·루프·계산·호출·파일 처리, 실행 순서): `DO K=1,KC` (32); `DO LL=2,LA` (33); `SELSUM(LL)  = 0.0` (37); `DEPSUM(LL) = 0.0` (38); `VXXSUM(LL) = 0.0` (39); `VYYSUM(LL) = 0.0` (40); `QXXSUM(LL) = 0.0` (41); `QYYSUM(LL) = 0.0` (42); `ENDDO` (43); `ENDDO` (44). |
| 45–49 | 시작 시 6행 `SUBROUTINE HYDZERO` 루틴 안. 루프 밖에서 TIMEHYD=0.0·NHYCNT=0을 설정한다(45–46). 빈 주석·RETURN·END로 루틴을 끝낸다(47–49). 원문(조건·루프·계산·호출·파일 처리, 실행 순서): `TIMEHYD = 0.0` (45); `NHYCNT  = 0` (46); `RETURN` (48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–44: 여섯 초기화 배열의 첨자는 LL 하나이며 K를 포함하지 않는다(37–42). 해당 대입들은 K=1..KC 루프 안에 있다. TIMEHYD/NHYCNT 대입은 이 루프 밖에 있다(45–46).

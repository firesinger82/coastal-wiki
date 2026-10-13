---
file: models/ROMS/raw/source_code/roms/ROMS/Include/tile.h
lines: 38
sha256: 5de99c49e878c5eacbd24b806d7e6bd0ec93c8b780c547419bfd1bdbb3390441
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tile.h — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 저작권·MIT/X 형식 라이선스 머리말(1–8). 자동 지역 배열(automatic private storage arrays)의 수평 범위 IminS·ImaxS·JminS·JmaxS와 배열 하한·상한 LBi·UBi·LBj·UBj·LBij·UBij를 정수로 선언한다(9–10). 11–14행은 범위 설정 주석이다. |
| 15–25 | NESTING 참 분기는 `IminS=BOUNDS(ng)%Istr(tile)-4` (16), `ImaxS=BOUNDS(ng)%Iend(tile)+3` (17), `JminS=BOUNDS(ng)%Jstr(tile)-4` (18), `JmaxS=BOUNDS(ng)%Jend(tile)+3` (19)로 범위를 계산한다. `#else` (20) 분기는 `IminS=BOUNDS(ng)%Istr(tile)-3` (21), `ImaxS=BOUNDS(ng)%Iend(tile)+3` (22), `JminS=BOUNDS(ng)%Jstr(tile)-3` (23), `JmaxS=BOUNDS(ng)%Jend(tile)+3` (24)이다. 전처리 원문: `#ifdef NESTING` (15); `#else` (20); `#endif` (25). |
| 26–38 | I·J 방향 배열 하한과 상한을 BOUNDS(ng)의 tile별 LBi·UBi·LBj·UBj에서 복사한다(29–32). MIN(I,J)·MAX(I,J) 방향이라는 주석 아래 LBij·UBij를 BOUNDS(ng)%LBij·BOUNDS(ng)%UBij에서 복사한다(34–38). 이 구간에는 조건문과 루틴 호출이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–25: NESTING 참 분기와 else 분기의 하한 여유는 각각 4와 3이다. 두 분기의 상한 여유는 모두 3이다.

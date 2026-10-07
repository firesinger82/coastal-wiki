---
file: models/EFDC/raw/source_code/EFDC-GVC/surfplte.for
lines: 33
sha256: e486d7b1786adfa4f6928e85d283482484f04bf70be2b6a4e2feaf5b4ea2095e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# surfplte.for — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 구분 주석(1–5), SUBROUTINE SURFPLTE(6), EFDC-FULL 1.0a·2001-11-01 수정 및 변경 기록 머리말(8–17). 주석은 SUBROUTINE SURFPLT가 자유 수면 고도(free surface elevation) 등고선 파일을 쓴다고 적는다(19–20). 구분·빈 주석(21–23). |
| 24–33 | 시작 시 6행 SURFPLTE 루틴 안. `INCLUDE 'EFDC.PAR'` (24)·`INCLUDE 'EFDC.CMN'` (25), 구분 주석(26–28), INTEGER*4 VER·CHARACTER*80 TITLE 선언(29–30). RETURN·END(32–33). 실행 대입식·조건 분기·입출력·외부 루틴 호출은 없다. 포함 파일 내부는 이 판독 범위에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·19: 루틴 이름은 SURFPLTE이며 기능 주석에는 SURFPLT라고 적혀 있다.
- 24–33: 포함문과 VER·TITLE 선언 뒤 실행문은 RETURN뿐이다. 이 파일에는 주석의 등고선 파일 작성문이 없다.

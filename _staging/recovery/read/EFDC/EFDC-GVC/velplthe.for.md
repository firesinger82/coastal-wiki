---
file: models/EFDC/raw/source_code/EFDC-GVC/velplthe.for
lines: 26
sha256: f3976c21d60dc372353bc63212ccb26acce3232499147cf15b585b1251648a5d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# velplthe.for — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 구분 주석과 `SUBROUTINE VELPLTHE` 입구(1–3). EFDC-FULL 1.0a·2003년 Paul M. Craig 수정 주석(5–12). 설명은 VELPLTH의 수평 순간 유속(instantaneous horizontal velocity) 벡터 파일을 적는다(14–15). EFDC Explorer 형식과 정확히 맞춰 출력을 변경하지 말라는 주석(17–18). 나머지는 구분·빈 주석이다(19–21). |
| 22–26 | 시작 시 3행 VELPLTHE 안. `INCLUDE 'EFDC.PAR'` (22), `INCLUDE 'EFDC.CMN'` (23), 주석(24), RETURN(25), END(26). 이 파일에는 조건·계산 대입·OPEN/WRITE·CALL 문이 없다. 포함 파일 내부는 이 기록의 판독 대상이 아니다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–18·22–26: 주석은 유속 파일과 EFDC Explorer 출력을 설명한다. 실제 루틴 본문은 두 INCLUDE 뒤 RETURN이다. 이 파일에는 출력 실행문이 없다.

---
file: models/EFDC/raw/source_code/EFDC-GVC/skipcomm.for
lines: 36
sha256: a1389fdb029aeeb1f5afd00d29a89fb03b66bb17c4ddb2ec139279a0b2b015d4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# skipcomm.for — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 머리말·SKIPCOMM(IUNIT, CC) 선언·버전·수정일·변경 이력(1–25). 입력 파일의 주석 줄을 건너뛴다는 설명을 포함한다(26–27). |
| 28–36 | 시작 시 6행 SKIPCOMM 루틴 안. IUNIT 정수·1문자 CC·80문자 LINE을 선언한다(28–29). 레이블 100의 목록 지향 입력(list-directed input)은 `100   READ(IUNIT, *, END=999) LINE` (30). 주석 판정 원문은 `      IF(LINE(1:1) .EQ. CC) GOTO 100` (31); `      IF(LINE(1:1) .EQ. 'C') GOTO 100` (32); `      IF(LINE(1:1) .EQ. 'C') GOTO 100` (33). 참이면 100으로 돌아가 다음 레코드를 읽는다. 비주석 레코드에서는 BACKSPACE(IUNIT)으로 되돌린다(34). 파일 끝 레이블 999·RETURN·END를 포함한다(35–36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–33: 대문자 C를 검사하는 문장이 동일하게 두 번 연속 있다.
- 29–33: LINE 길이는 80이다. 소문자 c에 대한 별도 조건은 없으며, CC 인수와 대문자 C만 검사한다.

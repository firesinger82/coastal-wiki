---
file: models/EFDC/raw/source_code/EFDC-GVC/timelog.for
lines: 25
sha256: e8d0b55c6336f4eab90d804ddcdfd840f574d126b705ccdf7676605d56229afe
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# timelog.for — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 구분 주석·EFDC-FULL 1.0a 및 Paul M Craig의 2003-07-21·John Hamrick의 2001-11-01 수정 주석(1–10). SUBROUTINE TIMELOG(N,TIMEDAY)(11), `CHARACTER*8 MRMDATE,MRMTIME*10` (13), 빈 줄(14). |
| 15–25 | 시작 시 11행 TIMELOG 루틴 안. 시간 단계(time step)·시스템 시각을 TIME.LOG에 쓴다는 주석(15·18). DATE·TIME 호출은 주석 처리(16–17). `CALL DATE_AND_TIME(MRMDATE,MRMTIME)` (19), 장치 9에 N·TIMEDAY·MRMDATE·MRMTIME 출력(20). FORMAT은 N=I10·TIMEDAY=F12.4·DATE=A8·TIME=A10(22–23). RETURN·END(24–25). 조건 분기·계산 대입식은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15·19–20: 주석은 TIME.LOG 파일을 언급한다. 이 루틴은 장치 9에 출력하며 이 파일 안에는 해당 장치를 여는 OPEN문이 없다.

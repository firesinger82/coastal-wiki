---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/timelog.f90
lines: 32
sha256: 0408ae0fdf9d55d7228a245555f79fa648e680811345df78ac1b042295c49129
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# timelog.f90 — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | EFDC+·저작권·GPLv2 머리말(1–8), `SUBROUTINE TIMELOG(N,DAYJUL,OUTDIR1,TTDS)` (9). 주석은 모델 시간 단계(time step)와 시스템 시각을 TIME.LOG에 쓴다고 설명한다(11). GLOBAL에서 IK8/NITER만 가져온다(13). N은 integer(IK8), DAYJUL/TTDS는 DOUBLE PRECISION 입력, OUTDIR1은 길이 8 입력 문자열, MRMDATE/MRMTIME은 길이 8/10 문자열(17–20). |
| 22–32 | 시작 시 9행 TIMELOG 안. `call DATE_AND_TIME(MRMDATE,MRMTIME)` (23)으로 시스템 날짜와 시각을 얻는다. `open(9,FILE = OUTDIR1//'TIME.LOG',POSITION = 'APPEND')` (25)으로 파일에 덧붙인다. `write(9,100) NITER, DAYJUL, MRMDATE, MRMTIME, TTDS/3600.` (26)은 반복 번호·모델 일자·시스템 날짜/시각·경과 시간의 시간 단위 변환을 출력한다. close(9)(27). FORMAT은 NITER I12, TIMEDAY F12.4, 날짜 A8, 시각 A10, 경과 시간 F12.5(29). END SUBROUTINE·마지막 빈 줄(31–32). 조건 분기와 반복문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·13·17·26: 인수 N은 선언 이후 참조되지 않는다. 출력 반복 번호는 GLOBAL에서 가져온 NITER이다.

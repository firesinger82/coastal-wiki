---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_21.md
lines: 28
sha256: 299ff29b393e7bd8d2f06a085d307cd7abbab7d5cfa4ecd224c3df69d76101b2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_21.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C21 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 북쪽 개방 경계(open boundary)의 조석(tidal) 주기 강제(periodic forcing)에 따른 수면 표고(surface elevation) 또는 압력(pressure) 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C21 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE ON NORTH OPEN BOUNDARIES ` (10). |
| 14–27 | 북쪽 경계 매개변수 — IPBN 항목은 CARD 18을 참조한다(14). 나머지 매개변수 이름은 콜론 뒤 설명 없이 나열한다(16–24). 원문: ` \* IPBN: SEE CARD 18 ` (14); ` \* JPBN: ` (16); ` \* ISPBN: ` (18); ` \* NPFORN: ` (20); ` \* NPSERN: ` (22); ` \* TPCOORDN: ` (24). |
| 28–28 | C21 입력 형식 — 입력 열 이름만 제시한다(28). 파일은 이 줄에서 끝난다. 원문: ` C21 IPBN  JPBN  ISPBN  NPFORN  NPSERN ` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·18·20·22·24행: `JPBN`, `ISPBN`, `NPFORN`, `NPSERN`, `TPCOORDN` 항목의 콜론 뒤에는 설명이 없다. 14행은 `IPBN: SEE CARD 18`이라고 적는다.
- 24·28행: 설명 항목에는 `TPCOORDN`이 있지만 입력 열 이름에는 `TPCOORDN`이 없다.

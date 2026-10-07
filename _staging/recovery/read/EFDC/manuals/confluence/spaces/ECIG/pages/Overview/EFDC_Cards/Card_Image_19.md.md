---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_19.md
lines: 28
sha256: 5ce5ee7e1037c2cdb63abc0a99a28033e59e75ee06fa2d2da7484752cf316b63
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_19.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–26 | C19 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE ON WEST OPEN BOUNDARIES / 서쪽 경계 항목 — 서쪽 개방 경계(west open boundaries)의 주기 조석 강제력(periodic tidal forcing) 절 제목을 적는다(10). `IPBW`는 Card 18을 보라고 적는다(14). `JPBW`, `ISPBW`, `NPFORW`, `NPSERW`, `TPCOORDW`는 이름과 콜론 뒤에 설명이 없다(16–24). 매개변수 표기 원문: `\* IPBW: SEE CARD 18` (14); `\* JPBW:` (16); `\* ISPBW:` (18); `\* NPFORW:` (20); `\* NPSERW:` (22); `\* TPCOORDW:` (24). 이 파일에 없는 정의를 Card 18에서 가져와 채우지 않았다. 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 27–28 | C19 / 입력 헤더 — 빈 줄과 다섯 필드의 입력 헤더를 포함한다(27–28). 입력 줄 원문: `C19 IPBW  JPBW  ISPBW  NPFORW  NPSERW` (28). 이 파일은 이 헤더에서 끝난다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·16–24행: `IPBW`는 `SEE CARD 18`만 적는다. 다른 다섯 항목은 이름과 콜론 뒤에 정의가 없다.
- 24·28행: 설명 목록의 `TPCOORDW`가 입력 헤더에는 없다.
- 28행: 입력 헤더 뒤에 수치 입력 예시가 없다.


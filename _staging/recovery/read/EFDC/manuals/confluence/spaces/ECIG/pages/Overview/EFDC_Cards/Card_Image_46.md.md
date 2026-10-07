---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_46.md
lines: 49
sha256: 616c920af16195c9044c6f77b4303880c5a6760a80a7b8308e30be977914f7fd
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_46.md — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31195261(2), 제목 Card Image 46(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-11T09:43:29.392Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–26 | C46 BUOYANCY, TEMPERATURE, DYE DATA AND CONCENTRATION BC DATA — 부력(buoyancy), 온도(temperature), 염료(dye) 및 농도 경계 조건(concentration boundary conditions)을 다룬다(10). 부력 영향 계수의 범위·실제 물리 설정값, 기준·초기·평형·등온 온도와 전달계수의 단위를 제시한다(14–18). 초기 퇴적층(sediment bed) 온도의 파일 읽기·초기화 옵션과 사용하지 않는 KBH, 염료의 1차 감쇠 속도를 정의한다(20–26). 원문: `\* BSC: BUOYANCY INFLUENCE COEFFICIENT 0 TO 1, BSC=1. FOR REAL PHYSICS` (14); `\* TEMO: REFERENCE, INITIAL, EQUILIBRUM AND/OR ISOTHERMAL TEMP IN DEG C` (16); `\* HEQT: EQUILIBRUM TEMPERTURE TRANSFER COEFFICIENT M/sec` (18); `\* ISBEDTEMI: 0 READ INITIAL BED TEMPERATURE FROM TEMPB.INP` (20); `\*                     1 INITIALIZE AT START OF COLD RUN` (22); `\* KBH: NOT USED` (24); `\* RKDYE: FIRST ORDER DECAY RATE FOR DYE VARIABLE IN 1/sec` (26). |
| 27–44 | 개방 경계별 농도 경계 조건 개수 — 남·서·동·북 방향의 개방 경계(open boundaries)마다 농도 경계 조건 개수 매개변수를 정의한다(28–42). 원문: `\* NCBS: NUMBER OF CONCENTRATION BOUNDARY CONDITIONS ON SOUTH OPEN` (28); `\*            BOUNDARIES` (30); `\* NCBW: NUMBER OF CONCENTRATION BOUNDARY CONDITIONS ON WEST OPEN` (32); `\* BOUNDARIES` (34); `\* NCBE: NUMBER OF CONCENTRATION BOUNDARY CONDITIONS ON EAST OPEN` (36); `\* BOUNDARIES` (38); `\* NCBN: NUMBER OF CONCENTRATION BOUNDARY CONDITIONS ON NORTH OPEN` (40); `\* BOUNDARIES` (42). |
| 45–49 | C46 입력 표 — 빈 줄·표 마크업과 머리글 및 한 입력 행을 포함한다(45–49). 제시된 수치를 기본값으로 표시하지 않는다. 원문: `\| C46 \| BSC \| TEMO \| HEQT \| ISBEDTEMI \| KBH \| RKDYE \| NCBS \| NCBW \| NCBE \| NCBN \|` (48); `\|  \| 1 \| 10 \| 0.00E+00 \| 0 \| 2 \| 0.00E+00 \| 0 \| 0 \| 9 \| 0 \|` (49). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음


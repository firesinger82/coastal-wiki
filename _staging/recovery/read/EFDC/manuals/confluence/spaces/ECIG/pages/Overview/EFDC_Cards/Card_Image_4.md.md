---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_4.md
lines: 50
sha256: 23e65529ff87a38a262e58a4be4a4dda8e8e483858560a3a655ae4b5b36a0107
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_4.md — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C4 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 장기 질량 수송(longterm mass transport) 적분 전용 스위치 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C4 LONGTERM MASS TRANSPORT INTEGRATION ONLY SWITCHES ` (10). |
| 14–29 | 평균 질량 수송(mean mass transport) 출력 — ISSSMMT=0은 각 평균 기간(averaging period) 뒤에 RESTRAN.OUT을 쓰며 WASP/ICM/RCA 연결(linkage) 목적이다(16–18). 값 1은 마지막 평균 기간 뒤에 쓰며 연구 목적이다(20–22). 값 2는 평균 질량 수송장 계산과 RESTRAN.OUT을 비활성화한다(24). ISLTMT와 ISLTMTS는 미사용이라고 적는다(14·26). 원문: ` \* ISLTMT: NOT USED ` (14); ` \* ISSSMMT: 0 WRITES MEAN MASS TRANSPORT TO RESTRAN.OUT AFTER EACH ` (16); ` \* AVERAGING PERIOD (FOR WASP/ICM/RCA LINKAGE) ` (18); ` \* 1 WRITES MEAN MASS TRANSPORT TO RESTRAN.OUT AFTER LAST ` (20); ` \* AVERAGING PERIOD (FOR RESEARCH PURPOSES) ` (22); ` \* 2 DISABLES MEAN MASS TRANSPORT FIELD CALCULATIONS & RESTRAN.OUT ` (24); ` \* ISLTMTS: NOT USED ` (26). |
| 30–47 | 미사용 항목 — ISIA, RPIA, RSQMIA, ITRMIA, ISAVEC는 미사용이라고 적는다(34–44). 빈 줄과 반복 주석 표식도 포함한다. 원문: ` \* ISIA: NOT USED ` (34); ` \* RPIA: NOT USED ` (38); ` \* RSQMIA: NOT USED ` (40); ` \* ITRMIA: NOT USED ` (42); ` \* ISAVEC: NOT USED ` (44). |
| 48–50 | C4 입력 예시 — 입력 열 이름(48)과 대응 값(50)을 제시한다. 사이 빈 줄도 구간에 포함한다(49). 원문: ` C4 ISLTMT  ISSSMMT  ISLTMTS  ISIA  RPIA  RSQMIA  ITRMIA  ISAVEC ` (48); `         0             2               0           0    1.8      1E-10       0          0 ` (50). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

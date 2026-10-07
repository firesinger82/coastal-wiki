---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_67.md
lines: 54
sha256: 698189eef9f7e0930ac1a4cac77e802a5dd76b1baba63001aaa141557fccfb0b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_67.md — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–26 | C67 DRIFTER DATA / 입자 방출과 추적 — 첫 매개변수 묶음의 부표 입자(particle drifter) 방출·라그랑주 수송(Lagrangian transport) 활성화와 다른 추적 계산 옵션을 설명한다(10·14–18). 입자 수·방출 시간 단계(time step)·추적 파일 출력 간격을 적는다(20–26). 입력 위치 카드와 입력·출력 파일명을 그대로 옮긴다. 주석 표식과 빈 줄을 포함한다(11–26). 원문: `C67 DRIFTER DATA (FIRST 4 PARAMETER FOR SUB DRIFER, SECOND 6 FOR SUB LAGRES)` (10); `\* ISPD: 1 TO ACTIVE SIMULTANEOUS RELEASE AND LAGRANGIAN TRANSPORT OF` (14); `\*              NEUTRALLY BUOYANT PARTICLE DRIFTERS AT LOCATIONS INPUT ON C68` (16); `\*           2 TO ACTIVATE DS-INTERNATIONAL'S LPT DRIFTER COMPUTATIONS (DRIFTER.INP)` (18); `\* NPD:      NUMBER OF PARTICLE DIRIFERS` (20); `\* NPDRT: TIME STEP AT WHICH PARTICLES ARE RELEASED` (22); `\* NWPD:  NUMBER OF TIME STEPS BETWEEN WRITING TO TRACKING FILE` (24); `\*              DRIFTER.OUT` (26). |
| 27–50 | C67 DRIFTER DATA / 평균 속도 — 시간·공간 구간의 라그랑주 평균 속도(Lagrangian mean velocity) 계산 옵션을 제시한다(28–36). 모든 방출 시각에 대한 평균도 계산한다고 적는다(32–34). 두 번째 옵션은 더 높은 차수의 궤적 적분(trajectory integration)을 사용한다고 적는다(36). 영역의 서·동·북·남 경계와 방출 시각 수, 전체·짝수·홀수 수평 속도 벡터 출력 옵션을 정의한다(38–48). 주석 표식과 빈 줄을 포함한다(27–50). 원문: `\* ISLRPD: 1 TO ACTIVATE CALCULATION OF LAGRANGIAN MEAN VELOCITY OVER TIME` (28); `\*                   INTERVAL TREF AND SPATIAL INTERVAL ILRPD1<I<ILRPD2,` (30); `\*                   JLRPD1<J<JLRPD2, 1<K<KC, WITH MLRPDRT RELEASES. ANY AVERGE` (32); `\*                   OVER ALL RELEASE TIMES IS ALSO CALCULATED` (34); `\*               2 SAME BUT USES A HIGER ORDER TRAJECTORY INTEGRATION` (36); `\* ILRPD1     WEST BOUNDARY OF REGION` (38); `\* ILRPD2     EAST BOUNDARY OF REGION` (40); `\* JLRPD1    NORTH BOUNDARY OF REGION` (42); `\* JLRPD2    SOUTH BOUNDARY OF REGION` (44); `\* MLRPDRT NUMBER OF RELEASE TIMES` (46); `\* IPLRPD     1,2,3 WRITE FILES TO PLOT ALL,EVEN,ODD HORIZ LAG VEL VECTORS` (48). |
| 51–54 | C67 입력 예시 — 모든 입력 열 제목과 수치 값 행을 제시한다(52·54). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 빈 줄을 포함한다(51·53). 원문: `C67  ISPD  NPD  NPDRT  NWPD  ISLRPD  ILRPD1  ILRPD2  JLRPD1  JLRPD2  MLRPDRT  IPLRPD` (52); `            0       0        0           12          0            6           47           6           17              12             1` (54). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 30·32행: `TREF`와 `KC`가 시간·공간 구간 설명에 등장하지만 이 파일에는 두 기호의 정의가 없다.


---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_45A.md
lines: 59
sha256: cb9b8ee0b08de2fc60aeb6d56e8d6448fd82d6c007a50c63f9a6399bf07a8c26
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_45A.md — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31752213(2), 제목 Card Image 45A(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-11T08:41:57.883Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–28 | C45A TOXIC CONTAMINANT NON-SEDIMENT BASED ORGANIC CARBON (OC) INTERACTION PARAMETERS / 수주 옵션 — 퇴적물에 기반하지 않는 유기탄소(organic carbon, OC) 상호작용을 다룬다(10). 수주(water column)의 용존 유기탄소(dissolved organic carbon, DOC)와 입자상 유기탄소(particulate organic carbon, POC)의 상수·시간 일정 공간 변동·FPOC 및 함수 지정 옵션을 설명한다(14–28). 기본값 문구·입력 파일·적용 조건 원문: `\* ISTDOCW: 0 CONSTANT DOC IN WATER COLUMN OF STDOCWC (DEFAULT=0.)` (14); `\*                   1 TIME CONSTANT, SPATIALLY VARYING DOC IN WATER COLUMN FROM docw.inp` (16); `\* ISTPOCW: 0 CONSTANT POC IN WATER COLUMN OF STPOCWC (DEFAULT=0.)` (18); `\*                   1 TIME CONSTANT, SPATIALLY VARYING POC IN WATER COLUMN FROM pocw.inp` (20); `\*                   2 TIME CONSTANT, FPOC IN WATER COLUMN, SEE C45C` (22); `\*                   3 TIME CONSTANT, SPATIALLY VARYING FPOC IN WATER COLUMN FORM fpocw.inp` (24); `\*                   4 FUNTIONAL SPECIFICATION OF TIME AND SPATIALLY VARYING` (26); `\*                      FPOC IN WATER COLUMN` (28). |
| 29–44 | 퇴적층 옵션 — 퇴적층(sediment bed)의 DOC·POC 옵션을 제시한다(30–44). FPOC의 시간·공간 변동 함수 지정은 각 적용에서 코드 수정을 요구하며 ADVANCED로 표시한다(42·44). 기본값 문구·입력 파일·적용 조건 원문: `\* ISTDOCB: 0 CONSTANT DOC IN BED OF STDOCBC (DEFAULT=0.)` (30); `\*                  1 TIME CONSTANT, SPATIALLY VARYING DOC IN BED FROM docb.inp` (32); `\* ISTPOCB: 0 CONSTANT POC IN BED OF STPOCBC (DEFAULT=0.)` (34); `\*                  1 TIME CONSTANT, SPATIALLY VARYING POC IN BED FROM pocb.inp` (36); `\*                  2 TIME CONSTANT, FPOC IN BED, SEE C45D` (38); `\*                  3 TIME CONSTANT, SPATIALLY VARYING FPOC IN BED FROM fpocb.inp` (40); `\*                  4 FUNTIONAL SPECIFICATION OF TIME AND SPATIALLY VARYING` (42); `\* FPOC IN BED, REQUIRES CODE MODIFICATION FOR EACH APPLICATION (ADVANCED)` (44). |
| 45–54 | 상수 DOC·POC 매개변수 — 수주·퇴적층의 DOC·POC 상수값을 각각 해당 옵션이 0일 때 사용한다고 정의한다(46–52). 원문: `\* STDOCWC: CONSTANT WATER COLUMN DOC (ISTDOCW=0)` (46); `\* STPOCWC: CONSTANT WATER COLUMN POC (ISTPOCW=0)` (48); `\* STDOCBC: CONSTANT BED DOC (ISTDOCB=0)` (50); `\* STPOCBC: CONSTANT BED POC (ISTPOCB=0)` (52). |
| 55–59 | C45A 입력 표 — 빈 줄·표 마크업과 머리글 및 한 입력 행을 포함한다(55–59). 농도 단위는 이 파일에 명시하지 않는다. 표의 수치를 기본값으로 표시하지 않는다. 원문: `\| C45A \| ISTDOCW \| ISTPOCW \| ISTDOCB \| ISTPOCB \| STDOCWC \| STPOCWC \| STDOCBC \| STPOCBC \|` (58); `\|  \| 1 \| 2 \| 0 \| 2 \| 6 \| 3 \| 10 \| 5 \|` (59). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음


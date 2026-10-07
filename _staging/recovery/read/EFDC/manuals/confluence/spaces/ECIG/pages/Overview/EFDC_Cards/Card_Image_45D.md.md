---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_45D.md
lines: 33
sha256: f64611d6b99d9c6f2f5285353581b52949dd6134d091b888c084fc56c3867bf7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_45D.md — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31785022(2), 제목 Card Image 45D(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-11T09:01:00.867Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–16 | C45D TOXIC CONTAMINANT POC FRACTIONAL DISTRIBUTIONS IN SEDIMENT BED — 퇴적층(sediment bed)의 입자상 유기탄소(particulate organic carbon, POC) 분율 분포를 다룬다(10). ISTRAN(5)가 0이어도 데이터 한 줄을 요구하며 ISTOC(NT)가 1 또는 2일 때 사용한다고 적는다(12·14). 의무·적용 조건 원문: `\* 1 LINE OF DATA REQUIRED EVEN IT ISTRAN(5) IS 0. DATA USED WHEN` (12); `\* ISTOC(NT)=1 OR 2` (14). |
| 17–26 | 분율 매개변수 — 오염물질 번호와 오염물질마다 필요한 데이터 행수·기본값 문구를 제시한다(18·20). SED·SND 부류에 연결된 유기탄소(organic carbon, OC) 분율의 이름과 첨자 범위를 정의한다(22·24). 원문: `\* NTOXN: TOXIC CONTAMINANT NUMBER ID. NSEDC+NSEDN 1 LINE OF DATA` (18); `\* FOR EACH TOXIC CONTAMINANT (DEFAULT = 2)` (20); `\* FPOCSED1-NSED: FRACTION OF OC ASSOCIATED WITH SED CLASSES 1,NSED` (22); `\* FPOCSND1-NSND: FRACTION OF OC ASSOCIATED WITH SND CLASSES 1,NSND` (24). |
| 27–33 | C45D 입력 표 — 빈 줄·표 마크업과 오염물질별 입력 행을 포함한다(27–33). 각 행에 세 분율의 제시값 0.1·0.05·0.05가 있다(31–33). 이 표의 수치를 기본값으로 표시하지 않는다. 머리글·입력 행 원문: `\| C45D \| NTOXN \| FPOCSED1 \| FPOCSND1 \| FPOCSND2 \|  \|` (30); `\|  \| 1 \| 0.1 \| 0.05 \| 0.05 \| \*\* Pesticides \|` (31); `\|  \| 2 \| 0.1 \| 0.05 \| 0.05 \| \*\* Polychrorinated Biphenyls 1336-36-3 \|` (32); `\|  \| 3 \| 0.1 \| 0.05 \| 0.05 \| \*\* Zn \|` (33). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18–20: 데이터 행수 문구에는 `NSEDC+NSEDN 1 LINE OF DATA`가 있다(18). 이 파일에는 `NSEDC`와 `NSEDN`의 별도 정의가 없다.


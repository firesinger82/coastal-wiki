---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_44.md
lines: 51
sha256: e6f66570802bde0308249e9087c10c7b7c7482b38dacc200a5db8c3f1c027841
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_44.md — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31817732(2), 제목 Card Image 44(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-11T07:57:50.128Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–26 | C44 TOXIC SORPTION OPTION, DIFFUSION AND MIXING — 독성물질의 수착(sorption), 확산(diffusion), 혼합(mixing)을 소개한다(10). 오염물질 번호의 기본 데이터 행수와 무기 고형물(inorganic solids), 용존 유기탄소(dissolved organic carbon), 입자상 유기탄소(particulate organic carbon, POC)에 대한 분배(partitioning) 옵션을 설명한다(14–26). 이름·기본 행수·옵션 원문: `\* NTOXN: TOXIC CONTAMINANT NUMBER ID (1 LINE OF DATA BY DEFAULT)` (14); `\* ISTOC: 0 INORGANIC SOLIDS BASED PARTITIONING ONLY (Kd APPROACH)` (16); `\*              1 FOR DISS AND PART ORGANIC CARBON SORPTION, POC IS SPECIFIED` (18); `\*              2 FOR DISS ORGANIC CARBON SORPTION AND POC FRACTIONALLY` (20); `\*                 DISTRIBUTED TO INORGANIC SEDIMENT CLASSES` (22); `\*              3 FOR NO DISS ORGANIC CARBON SORPTION AND POC FRACTIONALLY` (24); `\*                 DISTRIBUTED TO INORGANIC SEDIMENT CLASSES` (26). |
| 27–44 | 퇴적층 확산·혼합 — 퇴적층(sediment bed) 공극수(pore water) 내 확산과 수주(water column)·최상층 공극수 사이 교환을 정의한다(28–36). 양수·음수 DIFTOXS의 서로 다른 해석을 명시한다(34·36). 입자 혼합 계수가 음수이면 구역 파일을 사용한다(38·40). 활성 깊이와 단위도 제시한다(42). 원문: `\* DIFTOX: DIFFUSION COEFF FOR TOXICANT IN SED BED PORE WATER (m^2/s)` (28); `\* DIFTOXS: DIFFUSION COEFF FOR TOXICANT BETWEEN WATER COLUMN AND` (30); `\*                  PORE WATER IN TOP LAYER OF THE BED(m^2/s)` (32); `\*                 > 0.0 INTERPRET AS DIFFUSION COEFFICIENT (m^2/s)` (34); `\*                < 0.0 INTERPRET AS FLUX VELOCITY (m/s)` (36); `\* PDIFTOX: PARTICLE MIXING DIFFUSION COEFF FOR TOXICANT IN SED BED (m^2/s)` (38); `\*                  (if negative use zonal files PARTMIX.INP and PMXMAP.INP)` (40); `\* DPDIFTOX: DEPTH IN BED OVER WHICH PARTICLE MIXING IS ACTIVE (m)` (42). |
| 45–51 | C44 입력 표 — 빈 줄·표 마크업과 오염물질별 입력 행을 포함한다(45–51). 머리글을 보정하지 않고 그대로 옮긴다(48). 제시된 수치의 기본값 표시는 없다. 원문: `\| C44 \| NTOXN \| DIFTOX \| DIFTOXS \| PDIFTOX \| DPDIFTOX \|  \|  \|` (48); `\|  \| 1 \| 2 \| 1.00E-09 \| 2.00E-08 \| 0.00001 \| 0.01 \| ! Pesticides \|` (49); `\|  \| 2 \| 3 \| 1.00E-09 \| 2.00E-08 \| 0.0001 \| 0.01 \| ! Polychrorinated Biphenyls 1336-36-3 \|` (50); `\|  \| 3 \| 0 \| 1.00E-09 \| 1.00E-08 \| 0.000001 \| 0.01 \| ! Zn \|` (51). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16–26·48: 본문은 `ISTOC` 옵션을 정의한다(16–26). 표 머리글에는 `ISTOC` 열 이름이 없으며 마지막 두 열 이름은 비어 있다(48).


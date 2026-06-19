---
title: "EFDC 공식 자료 — DSI·GitHub·핵심 논문 (Hamrick 1992-)·커뮤니티 큐레이션"
topic: efdc-web-refs
canonical_source: self
citation_status: verified
verification_method: "DSI LLC 공식 도메인 (dsi.llc, eemodelingsystem.com) — EFDC_Theory_Document_Ver_12.pdf 표지 publication 정보 직접 인용 + GitHub 공개 repo (dsi-llc/EFDC_Plus) + Acknowledgement (theory v12 p.i) 의 authorship 정보. 핵심 논문 인용은 publicly-known canonical works (Hamrick 1992 EFDC original)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — URL + 공인 논문 인용"
verification_date: 2026-05-24
related:
  - models/EFDC/README.md
  - models/EFDC/manual-notes/efdc-theory-doc-v12.md
---

# EFDC 공식 자료 큐레이션

> [`models/EFDC/README.md`](../README.md) 의 정체 카드 외부 references 확장.

## 1. 공식 사이트 (DSI LLC — 메인 maintainer 2009~)

| 자원 | URL | 활용 |
|---|---|---|
| **DSI EFDC+ Modeling System** | [https://www.dsi-llc.com/efdc-modeling-system/](https://www.dsi-llc.com/efdc-modeling-system/) | 공식 홈 |
| **EE Modeling System** | [https://www.eemodelingsystem.com/](https://www.eemodelingsystem.com/) | EFDC+ GUI + documentation |
| **EFDC+ Documentation Online** | [eemodelingsystem.com/EFDC_Documentation/](https://www.eemodelingsystem.com/EFDC_Documentation/) | r8.5.0 매뉴얼 + Theory v12 online |
| **Theory v12 PDF** | [eemodelingsystem.com/.../EFDC_Theory_Document_Ver_12.pdf](https://www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC_Theory_Document_Ver_12.pdf) | 본 위키 [[../manual-notes/efdc-theory-doc-v12]] verified |

## 2. Code repository

| Repo | 역할 |
|---|---|
| [dsi-llc/EFDC_Plus](https://github.com/dsi-llc/EFDC_Plus) | EFDC+ Stable (DSI 메인) — GPL-3.0 |
| (별도 분기) | EFDC-GVC (사용자 보유, 본 위키 `raw/source_code/EFDC-GVC/`) |
| Legacy (Hamrick) | VIMS EFDC (1992 original, 분기됨) |

## 3. 핵심 논문 — Authorship 계보

### 3.1 Foundation (1992) — Hamrick original

- **Hamrick, J.M. (1992)** "A three-dimensional environmental fluid dynamics computer code: theoretical and computational aspects" *Special Report 317, Virginia Institute of Marine Science (VIMS), College of William and Mary* — **EFDC 시초 doc**
- **Hamrick, J.M. (1996)** "User's manual for the environmental fluid dynamics computer code" *Special Report 331, VIMS*

### 3.2 Eutrophication module — Park

- **Park, K., Kuo, A.Y., Shen, J., Hamrick, J.M. (1995)** "A three-dimensional hydrodynamic-eutrophication model (HEM-3D): description of water quality and sediment process submodels" *Special Report 327, VIMS* — CE-QUAL-ICM kinetics 통합

### 3.3 Sediment dynamics — SEDZLJ (Jones, Ziegler, Lick)

- **Ziegler, C.K., Lick, W. (1986)** "A numerical model of the resuspension, deposition, and transport of fine-grained sediments" *Report UCSB ME-86-3* — SEDZLJ 알고리즘 시초
- **Jones, C.A., Lick, W. (2000)** "Effects of Bed Coarsening on Sediment Transport" — armoring
- **James, S.C., Jones, C.A., Grace, M.D., Roberts, J.D. (2010)** "Advances in sediment transport modelling" — SEDZLJ 통합

### 3.4 Theory document (DSI v12, 2024)

- **DSI LLC (2024)** "EFDC+ Theory, Version 12" *Published by DSI LLC, Edmonds WA* — [PDF](https://www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC_Theory_Document_Ver_12.pdf)
  - 본 위키 verified: [[../manual-notes/efdc-theory-doc-v12]]

### 3.5 Legacy sediment theory

- **Tetra Tech (2002, final rev 2003)** "EFDC Technical Memorandum — Theoretical and Computational Aspects of Sediment and Contaminant Transport in the EFDC Model" *prepared for US EPA Office of Science and Technology* (source_id: efdc-sed-trans-2003)
  - 본 위키 verified: [[../manual-notes/efdc-sediment-theory-2003]]

## 4. 한국 적용

- 한국 해역 EFDC 운영 사례(축산항·서해 하구·인천만 등)는 개인 자료로 canonical 미수록 → 바이블 검증 통과 시 `experience/` 로 카테고리화 (source-needed).
- [[../source-analysis/]] 18 verified 노트는 공식 EFDC source-code 분석 (개인 사례와 무관).

## 5. 운영 자원

| 자원 | 비고 |
|---|---|
| DSI LLC contact | info@dsi.llc, +1 425 728 8440 (Acknowledgement p.i) |
| Address | 110 W. Dayton Street #202, Edmonds WA 98020 USA |
| EFDC+ Training | EFDC_Training_Overview.pdf (본 위키 raw/manuals/pdfs/) |
| Propwash white paper | EFDC+_Propwash_WhitePaper.pdf — DSI 특수 모듈 |
| GitHub Issues | [github.com/dsi-llc/EFDC_Plus/issues](https://github.com/dsi-llc/EFDC_Plus/issues) |

## 6. 본 위키 내 cross-ref

- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — EFDC SedTran-Original (ISTRAN=6/7) vs SEDZLJ unified
- [`models/EFDC/manual-notes/`](../manual-notes/) — 4 verified manual-notes (M-C 1차)
- [`models/EFDC/source-analysis/`](../source-analysis/) — 18 verified 노트 (codex source-code 직접 분석)
- `textbook/sources.yml` 의 `efdc-general` + `efdc-sed-trans-2003` source_id

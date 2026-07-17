---
title: "ShorelineS 공식 리소스 — GitHub·기준 논문(Roelvink 2020)·라이선스"
model: ShorelineS
component: web-refs
canonical_source: self
citation_status: verified
verification_method: "GitHub repo danoroelvink/shorelines depth-1 clone(sha 7bf4481ab, 2026-07-17) 실파일 확인 — LICENSE·ShorelineS.m 헤더·doc/ PDF 파일명·ShorelineS-Publications.txt. 논문 서지는 repo 동봉 PDF(FMarS2020_Roelvink_etal.pdf) + Frontiers 공식 페이지 URL 대조."
note_author: "Claude Fable 5"
note_date: 2026-07-17
related:
  - models/ShorelineS/README.md
  - models/ShorelineS/source-analysis/shorelines-architecture-map.md
---

# ShorelineS 공식 리소스

## 1. 소스·사이트

| 리소스 | 위치 | 비고 |
|---|---|---|
| GitHub (공식) | https://github.com/danoroelvink/shorelines | "ShorelineS free-form coastline simulation program". 검수 스냅샷 sha `7bf4481ab84c635033ef475fa648a1b09cf9f36b`(2025-10-07 커밋) |
| 공식 사이트 | www.shorelines.nl | Roelvink et al. (2020) Data Availability Statement 에 MATLAB 소스 배포처로 명시 |
| 라이선스 | repo `LICENSE` = LGPL v3 전문 / 소스 헤더(`functions/ShorelineS.m:38-42`) = "LGPL v2.1 or later" | 두 표기 병존 — LGPL 계열 확정, 세부 버전 표기 불일치는 disclosed |
| 배포 형태 | `functions/`(generic 136 .m)·`script/`(케이스별)·`compiled/`·`ShorelineS.ipynb` | repo README.md:4 — functions=케이스 불변, scripts=케이스 정보 분리 원칙 |

## 2. 기준 논문 (repo `doc/` 동봉 — 로컬 PDF로 페이지 인용 가능)

1. **Roelvink, D., Huisman, B., Elghandour, A., Ghonim, M., Reyns, J. (2020)** — "Efficient Modeling of Complex Sandy Coastal Evolution at Monthly to Century Time Scales" *Frontiers in Marine Science* **7**:535. doi:10.3389/fmars.2020.00535
   - repo 사본: `doc/FMarS2020_Roelvink_etal.pdf` — 모델 정식화(free-form 해안선·transport·회절·스핏)의 1차 문헌. manual-notes 발췌 대상.
2. **Roelvink et al. (2018)** — ICEC 2018 발표 논문. repo 사본: `doc/ICEC2018_Paper_Roelvink_final_14-8.pdf` — 초기 버전 소개.
3. **FAQ**: `doc/ShorelineS - frequently asked questions.pdf` — 사용 관행 문서(매뉴얼 대용 축).
4. **논문 목록**: repo 루트 `ShorelineS-Publications.txt` — 후속 응용·검증 문헌 리스트(추가 web-refs 후보).

## 3. 저자·기관 (소스 헤더 `functions/ShorelineS.m:10-27` 실측)

- 창시: J.A. Roelvink (IHE Delft, 2016–) / 확장: B.J.A. Huisman (Deltares, 2017–)
- 기여: A.M. Elghandour·J. Reyns (IHE Delft/Deltares)·M.E. Ghonim·C.M. Mudde (TU-Delft)·B. Perry (Flinders)·A. de Beer·A. de Bakker (Deltares)·K. Trouw (Flanders Hydraulics)
- Copyright (C) 2020 IHE Delft & Deltares

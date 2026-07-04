# EFDC+ Acquisition Manifest

**Acquired**: 2026-05-03
**Method**: clone upstream + import canonical PDFs/KB from local

## source_code/

| Repo | Org | Size | Source |
|------|-----|------|--------|
| EFDCPlus_Stable | dsi-llc | 71M | https://github.com/dsi-llc/EFDCPlus_Stable (GPLv2, updated 2026-04-02) |
| EFDC-GVC | dsi-llc | 6M | https://github.com/dsi-llc/EFDC-GVC (Generalized Vertical Coordinate variant) |

Both `--depth 1`. Total source_code/: 77M.

### ★ 버전 provenance 확정 (2026-07-04)

- **EFDCPlus_Stable = `EFDCPlus_12.4`** (릴리스 헤더 `EFDC/aaefdc.f90:22` "RELEASE: EFDCPlus_12.4", DATE 2025-12-29; 솔루션 파일명 `EFDCPlus_MPI_12.sln` 정합). clone HEAD sha **`3ed76b6eb1263921ba99bf23b66bb85c1a5feac1`** (2026-04-02 "update readme"). 12.4 릴리스 피처(헤더 verbatim): MPI Domain Decomposition · Propeller Wash · 신 WQ kinetics(사용자 정의 algal groups+zooplankton) · 3TL 동적 timestep · GOTM · **SIGMA-Zed(SGZ)**. → **위키 EFDC source-analysis 전체 = EFDC+ 12.4 기준.**
- **EFDC-GVC** clone HEAD sha **`68dc93fa04c48a785bbe3136e1784ceca2a7a20f`** (2021-11-10) — **repo 동결 4년+**. DSI README 공식: 레거시 테스트용 as-is 무지원, "recommends that users not use the GVC code for on-going models and make the conversion to EFDC+". → GVC 서브루틴 심층 분석 **불요 판정**(계보·구조·GVC↔SGZ 대조는 [source-analysis/efdc_gvc_legacy.md](source-analysis/efdc_gvc_legacy.md) verified 로 충분; SGZ 현행 구현은 mainline 노트 담당).

## manuals/pdfs/

Imported from `numerical_models/EFDCPlus_Stable/manual/` (canonical DSI distribution; upstream GitHub repo does NOT include manuals).

| File | Size | Type |
|------|------|------|
| EFDC_Manual.pdf | 1.8M | User manual |
| EFDC_Theory_Document_Ver_12.pdf | 15M | Theory |
| EFDC_Implementation_Guide.pdf | 1.8M | Implementation |
| EFDC+_Propwash_WhitePaper.pdf | 31M | Propwash white paper |
| EFDC_Training_Overview.pdf | 4.1M | Training cases |

## manuals/refs/

| File | Size | Type |
|------|------|------|
| EFDC_Parameters_Guide.md | 96K | Parameter reference |
| EFDC_Quick_Reference.md | 4.7K | Quick ref |

## manuals/confluence/

Atlassian Confluence KB export from eemodelingsystem.atlassian.net (manually obtained earlier; site requires auth so cannot re-fetch via API).

Spaces (6 total):
| Space | Description |
|-------|-------------|
| EK | EFDC Knowledge (largest) |
| EHG | EFDC Hydrodynamics Guide |
| ECIG | EFDC Cell Interface Guide |
| CVLKB | Civil KB |
| CVLGRID | Civil Grid |
| ETG | (empty in original export) |

Total Confluence size: 2.1G (includes spaces.zip backup).

## NOT Acquired

- Official site eemodelingsystem.com — HTTP 403 (Cloudflare/anti-bot, would need browser automation)
- efdcplus.com — HTTP 520 (down)

## 수집 메모

- DSI 배포 매뉴얼 5 PDF + Confluence KB 전체 포함. (Training_Overview 는 case-study 성격 포함 — canonical 인용 시 공식 메커닉만 발췌.)

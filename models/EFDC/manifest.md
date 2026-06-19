# EFDC+ Acquisition Manifest

**Acquired**: 2026-05-03
**Method**: clone upstream + import canonical PDFs/KB from local

## source_code/

| Repo | Org | Size | Source |
|------|-----|------|--------|
| EFDCPlus_Stable | dsi-llc | 71M | https://github.com/dsi-llc/EFDCPlus_Stable (GPLv2, updated 2026-04-02) |
| EFDC-GVC | dsi-llc | 6M | https://github.com/dsi-llc/EFDC-GVC (Generalized Vertical Coordinate variant) |

Both `--depth 1`. Total source_code/: 77M.

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

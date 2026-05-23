# ROMS Acquisition Manifest

**Acquired**: 2026-05-03

## source_code/ (7 repos from myroms org)

| Repo | Size | Purpose |
|------|------|---------|
| roms | 34M | Main solver |
| roms_test | 7M | Idealized + realistic test cases (incl. WC13 4D-Var exercises) |
| roms_matlab | 16M | MATLAB processing scripts |
| roms_libs | 2M | External libraries |
| roms-jedi | 2M | C++/Fortran binding to JEDI |
| roms_eccofs | <1M | East Coast Community Ocean Forecast System |
| WRF | 266M | NUOPC/ESMF coupling fork (atmospheric) |

Total: ~506M

## manuals/wiki/ (MediaWiki crawl)

- Source: https://www.myroms.org/wiki
- Statistics: 1030 pages, 300 articles, 6576 edits
- Pages saved: 321 (including redirects)
- Formats: wikitext + html + markdown

## manuals/website/ (myroms.org)

- Source: https://www.myroms.org
- HTML: 838 → 838 markdown (35M)
- Crawl terminated after 838 (was still finding pages)

## Embedded PDFs (in source_code)

- roms_matlab/tidal_ellipse/tidal_ellipse.pdf — algorithm reference
- roms_test/WC13/*/Exercise_*.pdf — 9 4D-Var training exercises (case PDFs)

## NOT acquired

- ROMS Forum content (myroms.org has phpBB forum, requires auth + heavy crawl)

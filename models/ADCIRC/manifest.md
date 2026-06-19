# ADCIRC Acquisition Manifest

**Acquired**: 2026-05-03
**Method**: Hermes skill `acquire-model-source` (prototyped here, see ~/.hermes/skills/numerical-modeling/acquire-model-source/SKILL.md)

## source_code/

| Repo | Org | Size | Source |
|------|-----|------|--------|
| adcirc | adcirc | 89M | https://github.com/adcirc/adcirc |
| adcirc-testsuite | adcirc | 166M | https://github.com/adcirc/adcirc-testsuite |
| gahm | adcirc | 6.2M | https://github.com/adcirc/gahm |
| adcircpy | oceanmodeling | 4.8M | https://github.com/oceanmodeling/adcircpy |
| StormEvents | oceanmodeling | 9.2M | https://github.com/oceanmodeling/StormEvents |
| FigureGen | ccht-ncsu | 2.1M | https://github.com/ccht-ncsu/FigureGen |
| asgs | StormSurgeLive | 297M | https://github.com/StormSurgeLive/asgs |

All cloned with `--depth 1` (latest commit only). Total: ~574M.

## manuals/wiki/

- **Source**: https://wiki.adcirc.org (MediaWiki)
- **Method**: MediaWiki API (`action=parse` per page)
- **Pages enumerated**: 167 (after filtering redirects/special)
- **Pages saved**: 161 (6 skipped due to API errors)
- **Formats**: wikitext (raw), html (parsed), markdown (best-effort regex conversion)
- **Total size**: 2.7M
- **Manifest**: `manuals/wiki/manifest.json` (per-page revid for incremental re-crawl)

## manuals/website/

- **Source**: https://adcirc.org (WordPress)
- **Method**: `wget --mirror` (terminated after 21 min — WordPress taxonomy archive infinite generation)
- **HTML files**: 884
- **Size (raw HTML)**: 188M
- **Size (markdown)**: 47M (`manuals/website_markdown/`, via markdownify)
- **Note**: rest of WP archives skipped — diminishing returns

## manuals/pdfs/

- (not yet acquired — to be downloaded separately when ADCIRC.org PDF user manual URLs are confirmed)

## Skipped (Tier C, available if needed)

- WPringle/ADCIRC_MATLAB
- ccht-ncsu/LPT
- samiiali/adcirpolate
- samiiali/adcirc_interp
- MBilskie/REMOVE_ELEMENTS_BOUNDARY
- MBilskie/GRD2ADC
- sdat2/adcirc-v55.02

## Next Steps

1. Acquire official PDF manuals (User's Manual v53, Theory) from adcirc.org links
2. Run same skill on EFDC, XBeach, SWAN, Delft3D, ROMS
3. Decide what to import from `numerical_models/adcirc/` (legacy, 91GB)
4. Begin RAG ingest of cleaned corpus

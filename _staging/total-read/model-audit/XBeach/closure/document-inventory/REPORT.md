# XBeach document-axis inventory: exact 207

Date: 2026-09-09
Scope: read-only inventory and integration plan; no `models/XBeach/` file was modified.

## Result

The reported **207** is an exact severity-defined population, not the count of all document findings:

- immutable input: `_staging/total-read/model-audit/XBeach/XBeach-X00.jsonl`
- SHA-256: `f668299b20ee4ba722941033aa1b6bad47daa74c00625f743e019adcd6031f19`
- X00 records: 14 converted documents
- all X00 `unresolved`: 286 = **HIGH 207 + MED 49 + LOW 30**
- exact rule: every `unresolved` object whose `severity` is `HIGH`, in X00 artifact order
- frozen rows: `exact-207.jsonl`
- frozen-row SHA-256: `0ca0040d77c978f3ccca16fc5208c51d2aefeb19ee482a9fa4135e2fea4e3a15`

`XBeach-M00` is not part of this population. It is a separate miscellaneous-text shard containing 21 files. M00 R1 contains 59 findings and M00 R2 contains 34; neither is the source of the stated 207.

## Exact source population

All 207 HIGH rows come from six representations of three underlying works:

| Work | Representation | HIGH | Original SHA-256 |
|---|---|---:|---|
| XBeach Technical Reference: Kingsday Release, Deltares 2015, explicitly scoped to v1.22 revision 4567 | `XBeach_manual_kingsday.docx.txt` from `trunk/doc/manual/XBeach_manual_kingsday.docx` | 51 | `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543` |
| same work, PDF representation, 141 physical pages | `XBeach_manual_kingsday.md` from `trunk/doc/manual/XBeach_manual_kingsday.pdf` | 42 | `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4` |
| XBeach Manual, Deltares 2015, 145 physical PDF pages; its §1.2 also labels itself v1.22 revision 4567 | `XBeach_manual_master.docx.txt` from `trunk/doc/manual/XBeach_manual_master.docx` | 34 | `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236` |
| same titled work, PDF representation | `XBeach_manual_master.md` from `trunk/doc/manual/XBeach_manual_master.pdf` | 33 | `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7` |
| *XBeach: Non-hydrostatic model — Validation, verification and model description*, DRAFT, Smit et al., 2010 | `non-hydrostatic_report_draft.doc.txt` from `trunk/doc/reports/non-hydrostatic_report_draft.doc` | 21 | `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec` |
| same report, PDF representation, 69 physical pages | `non-hydrostatic_report_draft.md` from `trunk/doc/reports/non-hydrostatic_report_draft.pdf` | 26 | `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005` |

The DOC(X) and PDF files are separate byte sources. They are never treated as identical merely because they share a title. This matters especially for the two manuals: both claim the same release identifier, yet the extracted contents differ in keyword interface, defaults, boundaries and output descriptions.

The other eight X00 records contribute no HIGH rows. They account for the remaining MED/LOW findings: `DecisionTreeXBeach.docx.txt`, `Parallellization_report.md`, `Tutorial_installing_XBeach_on_Linux_cluster.docx.txt`, `adapted_front_0.doc.txt`, `curvilinear_grid_properties.pptx.txt`, `members.doc.txt`, `namespaces.xls.txt`, and the vendored MPICH Jumpshot `usersguide.md`.

## Page-aware source map

The original X00 PDF Markdown had no page separators. Page-aware extraction was regenerated with the repository's installed parser only:

```text
.venv/bin/opendataloader-pdf
package: opendataloader-pdf 2.4.7
command: .venv/bin/opendataloader-pdf -o <page-aware-dir> -f markdown --markdown-page-separator '<!-- page %page-number% -->' --image-output off <pdfs>
```

| PDF | Pages | Page-aware Markdown SHA-256 | Old-PDF-MD to page-aware token alignment |
|---|---:|---|---:|
| Kingsday | 141 | `85a7f67f00bc05c11e983923c241eeca27eafbf5b6e2f2056a12df8e9fb38341` | 0.997623 |
| master | 145 | `dcd324c99ea961be0ebcd93aa84136b06e765651c98423cd266c13aac20dc4e1` | 0.997602 |
| non-hydrostatic draft | 69 | `0bbbe0be361993f210aa18a9212e4f535e7d9c6562fbbb38259c03ebb90df65a` | 0.990670 |

The compact per-row page map is in `all-207-disposition.jsonl` and `.csv`. Each row records physical PDF pages, printed page numbers when the offset is recoverable, whole-representation alignment, reported-span token coverage, and all page-hit counts.

- 101 rows originate in the PDF Markdown and therefore have direct PDF-representation maps.
- 74 DOC(X)/OLE rows map across formats with at least 0.70 reported-span token coverage.
- 15 DOC(X)/OLE rows have partial cross-format maps and retain that limitation explicitly.
- 17 reordered/table-tail DOC(X) rows have no ordered-token map; their pages are retrieval candidates only and are labeled `cross-format-retrieval-candidate`.

Page alignment establishes provenance and locates the original paragraph. It does **not** validate the reporter's interpretation. Formula corruption, contradictory sentences, units, defaults and applicability still require semantic disposition. Full regenerated Markdown is scratch material; the compact maps and reproduction command are the retained inventory evidence.

Physical-to-printed offsets used after the body starts are Kingsday `printed = physical - 2`, master `printed = physical - 4`, and non-hydrostatic report `printed = physical - 10`. Earlier pages are labeled as front matter rather than assigned invented Arabic page numbers.

## Audit schemas

X00, M00 R1 and M00 R2 share the reader-record schema:

```text
record = {path, lines_read, reader, unresolved[]}
unresolved = {lines, severity, class, finding}
```

The frozen denominator adds immutable provenance: X00 artifact SHA, record and unresolved indices in both zero- and one-based form, stable `XH001`–`XH207` IDs, work ID, representation kind/hash, reported line span, original path/hash and the untouched reported finding.

The disposition schema adds:

- physical and printed page locators plus mapping coverage;
- subject-level canonical group;
- existing-canonical lexical anchors, explicitly marked as locator evidence only;
- proposed canonical routes;
- an explicit final disposition type;
- a cross-format duplicate candidate and confidence score.

## Duplicate structure

The six records are representation pairs, so 207 is not a count of 207 independent scientific claims. Claim granularity differs across the paired readers: one row may combine several facts that the other representation splits across rows.

- 71 mutual cross-format duplicate-candidate pairs were identified.
- Per-row duplicate confidence is high for 75 rows, probable for 97 and unresolved for 35.
- Duplicate links are restricted to representations of the same work. Kingsday and master are never deduplicated merely because both say v1.22 revision 4567.
- No unsupported “unique claim count” is asserted. `all-207-disposition.jsonl` preserves the complete denominator while canonical integration merges rows by source, topic and exact statement.

The pair list is stored in `disposition-summary.json`. It should be used as a review accelerator, not as proof of semantic equivalence.

## Current canonical coverage

Current XBeach canonical material includes 33 source-analysis notes and four manual notes. The relevant coverage is uneven:

- `manual-notes/xbeach-master-manual.md` already covers the master manual's modes, wave action, breaking, flow, groundwater, sediment, morphology, boundaries and many default tables with printed-page citations.
- source-analysis notes cover current implementation mechanisms for mode dispatch, params, waves, boundaries, flow, non-hydrostatic pressure, groundwater, morphology, avalanching, output, vegetation and ships.
- the three earlier catalog/example notes do not provide detailed coverage of this 207-row document population.
- no current canonical note systematically records Kingsday-vs-master drift, internal manual contradictions, DOC-vs-PDF discrepancies, conversion-damaged equations, or the 2010 draft's validation configurations and applicability limits.

Eight high-impact document/code topics covering 26 denominator IDs and 29 ID-topic links have an independent frozen-snapshot adjudication in `closure/manual-code-adjudications.json` (SHA-256 `56075b0e74b75050881292c5a95cca17813b4570457f3585a614d7f34c9f16fa`): `wci`, conditional `nuh` meaning, bed-friction defaults, dilatancy, adaptation time, `posdwn`, `dthetaS_XB`, and `secorder`. `XH100`, `XH135` and `XH147` each retain two adjudications. The all-207 JSONL stores these as `source_code_adjudications[]`, linking every topic to exact source paths, hashes and LF line spans. Those source results do not erase the historical document contradiction and do not reconstruct damaged PDF equations.

The per-row `existing_canonical_anchor_check` records exact technical-token hits. It is intentionally not called semantic coverage: 76 rows have no named technical anchor, and a shared parameter name does not prove that the same value, unit, edition or caveat is already present.

## Disposition of all 207

Every row has one of nine explicit dispositions:

| Disposition | Rows | Canonical treatment |
|---|---:|---|
| Merge with existing canonical as an edition-scoped manual fact | 81 | Merge into the master or Kingsday note after using the mapped original page; preserve units, context and edition. |
| Merge as a draft-scoped fact or limit into the non-hydrostatic report note | 33 | State that the source is a 2010 DRAFT; do not generalize historical switches or MPI limitations. |
| Add a source- and version-scoped manual fact | 10 | Add validation/build/version information absent from current notes. |
| Merge document conflict with frozen-source-snapshot adjudication | 25 | Preserve the document conflict and add the independently evidenced snapshot behavior from `manual-code-adjudications.json`. |
| Document both source statements as an internal conflict; select no value | 31 | Record both claims and their separate page locators. The contradiction itself is the canonical fact. |
| Record as edition or parameter drift | 19 | Preserve both edition spellings/values and avoid claims about present code behavior. |
| Record as a source-scoped unfinished feature or document limit | 4 | Preserve the historical status and source date. |
| Exclude converted value/formula from canonical; retain source warning | 3 | Do not transcribe the damaged equation/table/example as a fact. Record why it is unsafe. |
| Exclude converted formula; keep separate source-code adjudication | 1 | Do not reconstruct the damaged manual equation from code; document snapshot code behavior separately. |

Subject grouping, across all dispositions:

| Canonical group | Rows |
|---|---:|
| non-hydrostatic physics/numerics | 44 |
| morphology/bed composition/avalanching | 23 |
| sediment transport | 23 |
| build/MPI/version | 22 |
| wave boundary/spectra | 13 |
| groundwater | 12 |
| flow/tide/discharge boundaries | 11 |
| flow friction/viscosity | 11 |
| mixed parameter defaults | 11 |
| validation/non-hydrostatic | 10 |
| wave action/breaking/roller/friction | 9 |
| modes/grid/coordinates | 7 |
| vegetation/ships | 6 |
| output | 5 |

The row-level plan is the authoritative all-207 accounting. No subset or “representative” selection replaces it.

## Recommended canonical grouping

Canonical assembly should use four files rather than reproduce 207 audit rows:

1. Update `models/XBeach/manual-notes/xbeach-master-manual.md` with master-PDF facts that survive page checking. Keep its existing role as the current detailed manual note.
2. Add `models/XBeach/manual-notes/xbeach-kingsday-technical-reference.md`, scoped to the Kingsday source and v1.22 revision 4567 values.
3. Add `models/XBeach/manual-notes/xbeach-nonhydrostatic-report-2010.md`, explicitly labeled DRAFT, for theory, applicability, historical implementation and validation configurations.
4. Add `models/XBeach/manual-notes/xbeach-document-discrepancies-and-version-drift.md` for internal contradictions, DOC/PDF differences, cross-edition changes and explicit conversion exclusions. It should present both source statements and must not invent a preferred value.

Source-analysis remains canonical for current implementation behavior. Manual notes may link there after a separate source-code comparison; a historical manual value does not become a current-code default by implication.

## Remaining evidence boundaries

- The 15 partial and 17 retrieval-only DOC-to-PDF page maps require consulting the DOC(X) source as their authority or locating the exact PDF paragraph before citing the PDF.
- The four conversion-risk rows are complete exclusions from fact promotion, not unresolved facts: the conversion is insufficient to support the formula/value.
- Internal-conflict rows are complete document findings when both statements are preserved. Twenty-six high-impact IDs carry 29 separate frozen-source-snapshot links; the remaining conflicts do not imply a claim about current code.
- The non-hydrostatic report is a DRAFT and contains an unfinished validation section; all its switches, defaults and MPI limitations must remain dated source claims.
- Kingsday and master use the same release label but different content and hashes. Their values require separate source IDs or equally explicit bibliographic identities.
- Full semantic source checking must work from the physical page locators. Token alignment and canonical anchor hits alone cannot upgrade any row to `verified`.

## Closure update — 2026-09-09

The page-map counts above describe the initial immutable locator inventory. They remain useful for reproducing the audit, but they are no longer the citation rule for the 32 weak cross-format rows. Final canonical integration uses `document-canonical-mapping.json` as the authoritative per-ID locator:

- all 17 `cross-format-retrieval-candidate` rows now cite the original DOCX document-order paragraph/table-row blocks, source hash and short direct quotations; none claims a PDF page;
- the 15 `cross-format-partial` rows no longer cite their incomplete PDF alignment: nine DOCX rows use original DOCX blocks, while six OLE DOC rows use original-bound text-extract lines, extract/source hashes, short direct quotations and the corresponding printed report section without a physical-page claim;
- these 32 replacements are recorded in `retrieval-docx-evidence.json` and each affected `entries[].source_locator`; the frozen `exact-207.jsonl` and the initial page maps were not rewritten;
- every one of XH001–XH207 has one unique explicit anchor in the four staged manual notes and one mapping entry. The 71 reciprocal same-work representation pairs are only shared review groups. Both findings remain independent, and grouping is not evidence of semantic identity;
- the eight source-code adjudication groups are defined once in the discrepancy note with repo-relative line ranges and source hashes. Individual XH entries link to those definitions instead of repeating the source digest;
- source-locator/provenance verification is exhaustive for 207 rows. Independent semantic rereading was targeted to high-risk samples; the final dispositions otherwise preserve the immutable X00 full-read interpretation. This distinction is stated in each new note and the Master Manual supplement.

Final staged canonical distribution is 34 review groups/53 IDs in Kingsday, 22/35 in Master, 24/32 in the 2010 non-hydrostatic report, and 56/87 in discrepancies: 136 review groups and all 207 IDs. “Review group” is an assembly unit, not a unique scientific-fact count.

## Artifacts

- `exact-207.jsonl` — immutable denominator rows
- `exact-207-manifest.json` — denominator counts and hashes
- `all-207-disposition.jsonl` — full provenance, page map, duplicate candidate, coverage locator and disposition
- `all-207-disposition.csv` — review-friendly flat form
- `disposition-summary.json` — counts, mutual duplicate-pair list and parser provenance
- `source-map.json` — authoritative original/representation hashes and page-aware extraction provenance
- `build_exact207.py` / `build_disposition.py` — deterministic builders
- `retrieval-docx-evidence.json` — original-source evidence for the 32 weak cross-format rows
- `document-canonical-mapping.json` — final XH001–XH207 canonical anchor and source-locator ledger
- `canonical/models/XBeach/manual-notes/` — four complete staged canonical documents
- `build_retrieval_docx_evidence.py` / `build_canonical_drafts.py` — deterministic evidence and document builders

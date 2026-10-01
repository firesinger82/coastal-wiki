# XBeach R2 evidence-packet adapter

Generated 443 packets: unique 440, ambiguous 0, none 3.

| Document | Unique | Ambiguous | None |
|---|---:|---:|---:|
| kingsday | 171 | 0 | 3 |
| master | 179 | 0 | 0 |
| nonhydro | 90 | 0 | 0 |

Run `python3 build_packets.py` from this directory (or use its absolute path). Only this directory is written. The script uses Python standard libraries, preserves existing inputs, and emits no timestamps. The manifest in [association-check.json](association-check.json) binds packet bytes to input and script hashes.

## Mapping rules

- DOCX: zero-based preorder XML ordinal → owning body paragraph → OLE relationship → ShapeID-linked preview. Objects are collected only from the caption paragraph; table-cell context is retained separately. An empty paragraph stays empty.
- DOC: original WordDocument byte offset → sorted outer-field sequence. Original WordDocument/1Table stream hashes and all 167 cached byte-span hashes are checked. All 166 outer command strings match the converted DOCX command sequence. All 1,341 converted/restored body paragraphs retain identical OLE signatures. The corresponding restored paragraph supplies the caption text, object relationship and preview. Opaque container stream hashes supply original DOC stream candidates without interpreting Native payloads.
- Physical pages: accept source occurrence order only when the entire sequence of standalone rendered caption lines exactly equals the source caption sequence. The three checks pass (174/179/90). Inline prose references are excluded. On a failed sequence check the script retains label page candidates and marks an object-bearing packet ambiguous. Image and receipt hashes are checked.
- `unique` means the paragraph object set, preview relationships and render occurrence are uniquely bound. `none` means no OLE/preview in that paragraph; its physical page may still be known. `ambiguous` preserves a page/preview uncertainty. No status asserts readability.
- Preview paths of the form `container!word/media/imageN.emf` identify existing ZIP members; SHA256 is over the uncompressed member. `container_path`, `member`, and `storage` make these paths machine-readable. Existing supplement PNG/PDF/EMF paths are also retained. Nothing is extracted or rendered.
- Contract candidates require the frozen per-caption contract marker and the contract document/label scope. Visual receipts require source hash, label, paragraph ID, page and object relationships. Symbol receipts require document, label, direct paragraph index, OLE member and opaque Native SHA; they concern symbols only. XH candidates require the same source work, explicit label and an eight-token exact prose bridge to source paragraph locators; repeated labels require a unique local bridge. Original-PDF pages remain separate from derivative-render pages. Unmatched XH label mentions are listed in the check file.

Candidate reuse: 14 contract matches, 22 packet–XH finding pairs, six local visual receipts, and three symbol-receipt records (including the explicit stress-tensor definition after (1.1)). Six XH label mentions have no unique verified paragraph bridge and remain listed in the check file. The solitary-wave adjustment-distance prose receipt (`oleObject350`, direct paragraph 414) has no explicit caption label/locator bridge and is retained as unmatched; its neighboring equations are not chosen by proximity.

## Named checks

| Caption ID | Label | Object | Physical render page | Status |
|---|---|---|---:|---|
| master:xml:33272 | (2.110) | oleObject124.bin | 44 | unique |
| master:xml:33803 | (2.110) | oleObject125.bin | 45 | unique |
| master:xml:33982 | (2.110) | oleObject126.bin | 46 | unique |
| nonhydro:word:80632 | (2.9) | oleObject174.bin | 23 | unique |
| nonhydro:word:137756 | (2.9) | oleObject332.bin | 41 | unique |
| kingsday:xml:17124 | (2.27) | none | 25 | none |
| kingsday:xml:19400 | (2.41) | none | 28 | none |
| kingsday:xml:19490 | (2.42) | none | 28 | none |
| master:xml:18476 | (2.40) | oleObject45.bin | 27 | unique |
| kingsday:xml:18997 | (2.38) | oleObject41.bin | 27 | unique |
| kingsday:xml:19304 | (2.40) | oleObject43.bin | 28 | unique |

Kingsday 19400 and 19490 have no objects; neither borrows oleObject43. That object belongs to Kingsday 19304 (2.40), p.28. Kingsday 18997 (2.38) has oleObject41, p.27, and its existing preview receipt records a blank preview. Master 18476 (2.40) has oleObject45, p.27, and the existing supplement records a visible separate preview despite the blank body render. These structural associations do not assign `body_status`.

Master 33272 is on p.44; the following source prose (including porosity, morfac and sediment transport) is retained with paragraph locators even across p.45. No same-page symbol collection is performed. Nonhydro 80632 and 137756 remain distinct despite equal saved field SHA. The solitary-wave receipt attaches only to 137756/oleObject332; the stress-tensor receipt attaches only to its matching (1.1) paragraph and does not resolve that equation as a whole.

## Captions without an object association

- `kingsday:xml:17124` (2.27), p.25: No OLE/preview in the caption paragraph.
- `kingsday:xml:19400` (2.41), p.28: No OLE/preview in the caption paragraph.
- `kingsday:xml:19490` (2.42), p.28: No OLE/preview in the caption paragraph.

All three missing-object cases agree with the existing source-empty-paragraph receipts. There are no page association gaps. Existing judgments remain candidates (`claims_resolved=[]`). Equation transcription, role/implementation judgment, R2 semantic closure and external review remain outside this build.

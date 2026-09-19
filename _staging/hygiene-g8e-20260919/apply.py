"""G8e cleanup — exact-string edits from PLAN.md (rev 1). All-or-nothing: every edit must match its expected count."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PMN = "the practical manual note"
XM = "`XBEACH_MANUAL.md` (XBeach v1.24 practical manual note; not archived in this wiki)"
SB = "confirmed in the source basis above"
A = "models/ADCIRC/manual-notes/"
X = "models/XBeach/"
E = "models/EFDC/source-analysis/"

def D(line):  # delete a whole line
    return (line + "\n", "")

EDITS = {
    # R1 — ADCIRC "not downloaded yet"
    **{f"{A}{n}.md": [D("- local path: not downloaded yet")] for n in (
        "01-docs-hub", "02-getting-started", "03-theory-and-formulation", "04-theory-pdf-v44xx",
        "05-input-files-reference", "06-parameter-definitions", "07-examples-index",
        "08-official-example-problems", "09-support-and-faq", "12-tooling-ecosystem")},
    # R2 — ADCIRC nonexistent raw/code layout (official link: present)
    f"{A}10-github-repo-and-releases.md": [D("- local path: raw/code/adcirc/adcirc")],
    f"{A}11-testsuite.md": [D("- local path: raw/code/adcirc/adcirc-testsuite")],
    f"{A}14-fort14-grid-bathymetry-boundaries.md": [D("- local path: raw/code/adcirc/adcirc/docs/technical_reference/input_files/fort14.rst")],
    f"{A}15-mesh-tools-and-grid-editing.md": [D("- local path: raw/code/adcirc/adcirc/docs/tools/index.rst and related pages")],
    f"{A}16-bathymetry-and-subgrid-paths.md": [D("- local path: raw/code/adcirc/adcirc/docs/technical_reference/input_files and tools pages")],
    f"{A}17-boundary-and-forcing-inputs.md": [D("- local path: raw/code/adcirc/adcirc/docs/user_guide/model_configuration")],
    f"{A}18-nws13-schema-and-local-jma-msm-branch.md": [
        D("- local path: raw/code/adcirc/adcirc/docs/user_guide/model_configuration/meteorological_forcing/nws13.rst"),
        ("- year: active documentation site plus current local practice", "- year: active documentation site")],
    f"{A}13-nws13-and-jma-msm-path.md": [
        ("- link: local synthesis from `nws13.rst`, `fort22.rst`, testsuite `adcirc_katrina-2d-nws13`",
         "- link: synthesis of ADCIRC docs `nws13.rst`, `fort22.rst` and testsuite `adcirc_katrina-2d-nws13`"),
        D("- local path: raw/code/adcirc/adcirc-testsuite/adcirc/adcirc_katrina-2d-nws13"),
        ("- year: active docs plus current local practice", "- year: active docs")],
    "models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md": [
        D("- local path: `raw/code/adcirc/adcirc-testsuite/adcirc/adcirc_quarterannular-2d-netcdf`")],
    # R5 — ADCIRC environment/task state
    f"{A}28-github-oceanmesh-python-repo-review.md": [D("- local machine does not currently have the package installed")],
    f"{A}29-github-ocsmesh-repo-review.md": [
        D("It is already part of the local revalidation track."),
        D("- local scripts still treat it as a reconstruction attempt rather than the accepted baseline"),
        D("- local machine does not currently have the package installed")],
    "models/ADCIRC/source-analysis/adcirc.md": [D("- first controlled DT-sensitivity experiment draft")],
    # R8/R9 — ADCIRC manifest
    "models/ADCIRC/manifest.md": [
        ("- **위치**: 위키 밖 로컬 아카이브 `numerical_models/adcirc/docs-site/` (writer 머신; 상세 색인은 그곳의 `SITE-INDEX.md`)",
         "- **위치**: 위키 repo 밖 보관 (상세 색인 `SITE-INDEX.md` 동봉)"),
        D("3. Decide what to import from `numerical_models/adcirc/` (legacy, 91GB)"),
        D("4. Begin RAG ingest of cleaned corpus")],
    # XBeach manual-notes (R3 R4 R5 R6)
    f"{X}manual-notes/01-local-manual-stack.md": [
        ("모두 local note 인용과 일치). Mixed local  + 외부 공식 URL", "모두 실무 매뉴얼 노트 인용과 일치). Mixed 실무 매뉴얼 노트 + 외부 공식 URL"),
        ("# XBeach Local Manual Stack", "# XBeach Manual Stack"),
        ("- title: XBeach local manual stack", "- title: XBeach manual stack"),
        ("plus local practical note author(s)", "plus practical manual note author(s)"),
        ("and the local note targets XBeach v1.24 Halloween", "and the practical manual note targets XBeach v1.24 Halloween"),
        ("- local path:\n  - numerical_models/xbeach/XBEACH_MANUAL.md\n  - numerical_models/xbeach/src/doc/manual/XBeach_manual_master.pdf\n  - numerical_models/xbeach/src/doc/manual/XBeach_manual_kingsday.pdf",
         "- archived copies:\n  - `XBEACH_MANUAL.md` — not archived in this wiki\n  - `models/XBeach/raw/manuals/pdfs/XBeach_manual_master.pdf`\n  - `models/XBeach/raw/manuals/pdfs/XBeach_manual_kingsday.pdf`"),
        ("- local documentation already frames `surfbeat`", "- the documentation already frames `surfbeat`"),
        ("explicit enough in the local manual note", "explicit enough in the practical manual note"),
        ("confirms local executable/runtime existence and gives practical run setup", "gives practical run setup"),
        ("- limitations: the local note is practical and dense", "- limitations: the practical manual note is practical and dense")],
    **{f"{X}manual-notes/{n}.md": [
        ("모두 local note 인용과 일치). Mixed local  + 외부 공식 URL", "모두 실무 매뉴얼 노트 인용과 일치). Mixed 실무 매뉴얼 노트 + 외부 공식 URL"),
        ("- local path:\n  - numerical_models/xbeach/XBEACH_MANUAL.md\n", "- archived copies:\n  - `XBEACH_MANUAL.md` — not archived in this wiki\n"),
        ("for the XBeach lane in this workspace.", "for the XBeach lane in these notes."),
        ("- the local note characterizes it as:", f"- {PMN} characterizes it as:")]
        for n in ("02-delilah-reference", "03-holland-coast-reference")},
    # R5 — XBeach delilah/holland extras (applied after the dict above via merge below)
    # XBeach source-analysis (R4 R8 R9)
    f"{X}source-analysis/xbeach-parameter-glossary-v1.md": [
        ("- this version is grounded mainly in the confirmed local source stack", "- this version is grounded mainly in the confirmed source stack listed below"),
        ("Primary confirmed local sources:", "Primary confirmed sources:"),
        ("- `numerical_models/xbeach/XBEACH_MANUAL.md`", f"- {XM}"),
        ("Current locally confirmed values:", f"Values {SB}:"),
        ("Locally confirmed values include:", f"Values {SB} include:"),
        ("Locally confirmed examples:", f"Examples {SB}:"),
        ("Locally confirmed example:", f"Example {SB}:"),
        ("Locally confirmed values:", f"Values {SB}:", 3),
        ("Current local interpretation:", "Working interpretation:", 4),
        ("Current local practical default / recommended mode", "Working practical default / recommended mode"),
        ("Current local local-note values:", f"Values in {PMN}:"),
        ("- default local-note value: `n = 0.02`", f"- default value in {PMN}: `n = 0.02`"),
        ("in the local note framing", f"in the framing of {PMN}"),
        ("Current local framing treats `params.txt`", "Working framing treats `params.txt`"),
        ("Current local note explicitly documents:", "The practical manual note explicitly documents:")],
    f"{X}source-analysis/xbeach-morphology-foundation.md": [
        ("- this version is grounded mainly in the confirmed local manual stack and current local example/test context",
         "- this version is grounded mainly in the XBeach manual stack and example/test context listed below"),
        ("- `numerical_models/xbeach/XBEACH_MANUAL.md`", f"- {XM}"),
        ("Current local interpretation:", "Working interpretation:", 4),
        ("Locally confirmed values:", f"Values {SB}:"),
        ("is the practical default in the local note", f"is the practical default in {PMN}"),
        ("Critical practical implication from the local note:", f"Critical practical implication from {PMN}:"),
        ("Current local local-note values:", f"Values in {PMN}:"),
        ("## Example Framing From Local Note", "## Example Framing From the Practical Manual Note"),
        ("already appear in the local note:", f"already appear in {PMN}:")],
    f"{X}source-analysis/wave/xbeach-boundary-and-wave-setup.md": [
        ("- `numerical_models/xbeach/XBEACH_MANUAL.md`", f"- {XM}"),
        ("- source file: `numerical_models/xbeach/src/src/xbeachlibrary/boundaryconditions.F90`",
         "- source file: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90`"),
        ("Current local interpretation:", "Working interpretation:", 4),
        ("Current local practical default:", "Working practical default:"),
        ("The updated local source confirms that boundary logic is mode-sensitive and more varied than the local note alone suggests.",
         f"The source code confirms that boundary logic is mode-sensitive and more varied than {PMN} alone suggests."),
        ("Working interpretation from the local note:", f"Working interpretation from {PMN}:")],
    f"{X}source-analysis/xbeach_q3d.md": [("with the current local source guard", "with the current source guard")],
    f"{X}source-analysis/xbeach.md": [
        ("## Confirmed Local Source Availability\n\nConfirmed local source root:\n- `numerical_models/xbeach`\n\nConfirmed high-value local sources now known:\n"
         "- `src/doc/manual/XBeach_manual_master.pdf`\n- `src/doc/manual/XBeach_manual_kingsday.pdf`\n- `XBEACH_MANUAL.md`\n"
         "- `src/doc/misc/DecisionTreeXBeach.docx`\n- source trees under `src/src/xbeach/` and `src/src/xbeachlibrary/`\n\n"
         "This means XBeach is no longer blocked by total source absence. The next step is controlled ingest.",
         "## Source Availability\n\nArchived source root (vendor mirror):\n- `models/XBeach/raw/source_code/trunk/`\n\nHigh-value sources:\n"
         "- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_master.pdf`\n- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.pdf`\n"
         f"- {XM}\n"
         "- `models/XBeach/raw/source_code/trunk/doc/misc/DecisionTreeXBeach.docx`\n"
         "- source trees under `models/XBeach/raw/source_code/trunk/src/xbeach/` and `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/`")],
    f"{X}web-refs/xbeach-official-resources.md": [D("- (별도 작업) XBeach 의 한국 모래 입경 (D50) calibration")],
    # EFDC
    "models/EFDC/manifest.md": [("Imported from `numerical_models/EFDCPlus_Stable/manual/`", "Imported from the DSI EFDC+ distribution `manual/` directory")],
    f"{E}efdc-grid-system-foundation.md": [
        ("(`numerical_models/EFDCPlus_Stable/EFDC/MPI_*` directories", "(`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_*` directories"),
        ("once a project case forces the issue.", "once a documented case requires it."),
        D("- **Korean estuary case cross-references** — once 2–3 site-specific cases are written, link from this note into the experiment cards.")],
    f"{E}efdc-parameter-glossary-v1.md": [
        ("confirmed through the local EFDC+ manual RAG", "confirmed through retrieved EFDC+ manual passages"),
        ("used to organize future local experiments", "used to organize setup choices"),
        ("Manual-backed from local EFDC+ RAG:", "Manual-backed (retrieved EFDC+ manual passages):"),
        ("Local RAG sources referenced during drafting:", "Manual sources retrieved during drafting:"),
        D("- friction and mixing terms tied to local calibration experiments")],
    f"{E}efdc-calibration-foundation.md": [
        ("- the local EFDC+ manual RAG clearly supports", "- retrieved EFDC+ manual passages clearly support"),
        ("The local EFDC+ manual RAG supports these base facts:", "Retrieved EFDC+ manual passages support these base facts:")],
    f"{E}efdc-boundary-condition-foundation.md": [
        ("- this note is based on the local EFDC+ manual/KB RAG", "- this note is based on retrieved EFDC+ manual/KB passages"),
        ("The local EFDC+ manual RAG clearly supports the following points.", "Retrieved EFDC+ manual passages clearly support the following points.")],
    f"{E}efdc-wetting-drying-foundation.md": [
        ("the local EFDC+ manual RAG did return concrete", "retrieved EFDC+ manual passages did include concrete"),
        ("The local EFDC+ manual RAG explicitly returned the following", "Retrieved EFDC+ manual passages explicitly list the following")],
    f"{E}efdc-current-mismatch-diagnosis.md": [
        D("- local EFDC calibration notes"),
        ("- harbor or estuary case studies close to the active domain", "- published harbor or estuary case studies"),
        D("- repeated current-mismatch experiments recorded under `experiments/`"),
        D("- future failure pattern and playbook notes promoted from those experiments")],
    "models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md": [
        D("- `efdc-sgz-application-cases.md` — 한국 항만·하구 SGZ 적용 경험 (experience/ 후보)")],
    # FUNWAVE (R9)
    "models/FUNWAVE/source-analysis/funwave-build-and-blackwell-port.md": [
        ('verification_method: "본 위키 WSL2(Ubuntu 24.04)에서 직접', 'verification_method: "WSL2(Ubuntu 24.04)에서 직접'),
        ("> 본 위키 머신(WSL2 Ubuntu 24.04, RTX 5070)에서 **직접 clone→build→run** 검증.",
         "> 검증 환경: WSL2 Ubuntu 24.04, RTX 5070(sm_120) — **직접 clone→build→run** 검증.")],
    # concepts (R7)
    "concepts/tides/05-examples.md": [
        ("`experience/`로 승격 조건 ([CONVENTIONS.md §2](../../CONVENTIONS.md), [BOUNDARY.md](../../BOUNDARY.md)):\n"
         "- [ ] 실제 인천 KHOA 시계열 (예: 2024년 시간별) 다운로드·실행\n- [ ] UTide 결과 ↔ §3.2 KHOA 공식값 ±2% 이내 일치 확인\n"
         "- [ ] 약최저저조위 산출값을 KHOA 공식 인천 약최저저조위와 비교\n- [ ] 두 차례 이상 독립 검증 (다른 연도 시계열)\n", "")],
    "concepts/tides/06-model-application.md": [
        ("- 사용자 경험 (검증 통과 시):\n  - `experience/efdc-tidal-forcing-*.md` (미작성, 3조건 통과 시) — EFDC 실제 사용 패턴\n", "")],
}
EDITS[f"{X}manual-notes/02-delilah-reference.md"] += [
    ("- in this workspace, its strongest role is hydrodynamic reference", "- in these notes, its strongest role is hydrodynamic reference"),
    D("- the exact local runnable DELILAH package is not yet attached in this workspace"),
    ("- whether a local runnable reproduction already exists elsewhere in the workspace or online example assets",
     "- whether a runnable reproduction exists among the official online example assets")]
EDITS[f"{X}manual-notes/03-holland-coast-reference.md"] += [
    D("- the exact local runnable Holland Coast package is not yet attached in this workspace"),
    D("- whether local scripts or notebooks can reproduce a profile-comparison plot similar to the manual note")]

new_text, errors, n_edits = {}, [], 0
for rel, edits in EDITS.items():
    text = (ROOT / rel).read_text(encoding="utf-8")
    for e in edits:
        old, new, want = (e + (1,))[:3] if len(e) == 2 else e
        got = text.count(old)
        if got != want:
            errors.append(f"{rel}: expected {want} got {got}: {old[:70]!r}")
            continue
        text = text.replace(old, new); n_edits += 1
    new_text[rel] = text
if errors:
    print("ABORT — nothing written:"); print("\n".join(errors)); raise SystemExit(1)
for rel, text in new_text.items():
    (ROOT / rel).write_text(text, encoding="utf-8")
print(f"applied {n_edits} edits in {len(new_text)} files")

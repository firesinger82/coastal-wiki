#!/usr/bin/env python3
"""Persist the explicitly reviewed 2026-09-10 Office renderings and scope notes."""
import hashlib
import json
from pathlib import Path
import shutil
import zipfile
import olefile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SCRATCH = Path('/tmp/xbeach-resume-office')
OUT = HERE / 'office-read'
SOURCES = {
    'adapted_front_0': ('doc/misc/adapted_front_0.doc', 1),
    'curvilinear grid properties': ('doc/misc/curvilinear grid properties.pptx', 19),
    'DecisionTreeXBeach': ('doc/misc/DecisionTreeXBeach.docx', 5),
    'Tutorial_installing_XBeach_on_Linux_cluster': ('config/Tutorial_installing_XBeach_on_Linux_cluster.docx', 2),
    'members': ('doc/misc/members.doc', 9),
}
NOTES = {
    'adapted_front_0': [
        'Page 1: only the boundary algebra, no explanatory prose, date or applicability statement.',
        'u = u_in + u_out = u_in - sqrt(g*h)/h * eta_out = u_in - sqrt(g*h)/h * (eta-eta_in).',
        'u_in = C_g/h * eta_in; eta_in = u_in*h/C_g.',
        'u = u_in*(1+sqrt(g*h)/C_g) - sqrt(g/h)*eta. This is a transcription, not an assertion of snapshot implementation.',
        'All four Equation Native OLE objects have displayed formula content; native equation serialization was inventoried, not reverse engineered.'
    ],
    'curvilinear grid properties': [
        'Slides 1-10: z/u/v/c staggered locations; dsu/dsz/dsv/dsc, dnu/dnz/dnv/dnc metric segments and dsdnu control-volume area drawn on curved grid.',
        'Slides 11-13: local grid-direction momentum advection, volume continuity, subtraction of u times continuity to obtain sum(Q_in*(u-u_in))/V and bottom stress tau_b,s/(rho*h_um).',
        'Slide 14: average qx/qy at control-volume faces, multiply inward q by dnz/dsc and add Q_in*(u_in-u); embedded image5.wmf resolves overlapped rotation formulas: u_in=u*cos(Delta alpha)+v_u*sin(Delta alpha), or u_v*cos(Delta alpha)+v*sin(Delta alpha).',
        'Slides 15-16: z- and v-centered dsdnz/dsdnv areas.',
        'Slide 17: forward eta differences divided by dsu or dnv at u/v points.',
        'Slide 18: eta difference uses flux differences with velocities at n+1 and depths at n, metric-weighted dnu/dsv, divided by dsdnz.',
        'Slide 19: Cgxu is the adjacent Cgx average, Eu reconstructed from one-sided energy slopes according to Cgxu sign, Fluxx=Cgxu*Eu*dnu.',
        'All 19 slide pages and all 9 separately rendered WMF formulas read; no master-placeholder text promoted to technical content. This is historical diagram evidence, not a source-code path assertion.'
    ],
    'DecisionTreeXBeach': [
        'Pages 1-2: proposal explicitly exceeds currently supported functionality; forcing/configuration/composition/interest dimensions, scales, model setup/validity/complexity outputs.',
        'Pages 3-4: proposed tagged knowledge base, repeated category taxonomy, types of evidence, database field lists.',
        'Pages 4-5: categories/labels/knowledge/labels2knowledge fields are nested lists. Original document.xml has no drawing/pict/object/textbox elements. The flattened old extraction did not prove a missing relationship diagram.',
        'No parameter defaults, tested combinations or working online tool are actually supplied.'
    ],
    'Tutorial_installing_XBeach_on_Linux_cluster': [
        'Page 1: dated 2019-05-28 memo, two-page count, Deltares logo, SVN checkout/workaround and OpenEarthTools xb_write_sh_scripts_xbversions.m step.',
        'Pages 1-2: complete shell example read; Anaconda precedes GCC 4.9.2, HDF5 1.8.14, NetCDF v4.3.2_v4.4.0 and OpenMPI 1.8.3; --with-netcdf --with-mpi and fast-math flags retained as historical settings.',
        'Page 2: --prefix points to /opt/xbeach/..._HEAD but packaging cd points to $SVNPATH/install. No intervening creation/population of that directory is shown. No commands from the document were executed.',
        'Embedded TIFF is the displayed Deltares logo, not an omitted numerical figure.'
    ],
    'members': [
        'Pages 1-8: membership-request archive, requested/intended applications and HTML approval controls. Page 9 blank.',
        'Visual page 4 clips wide table cells; full LibreOffice Text export read through final entry to supplement clipping. Names/contact details are not transcribed into the interpretive report.',
        'Requests span storm erosion, runup, reefs, bathymetry inversion, proposed mud transport, coastal structures and teaching; user intent is not model validation or proof of implemented capability.',
        'Embedded VBA source ThisDocument.cls read separately: attributes and 97 MSForms control declarations, no Sub/Function executable bodies. Compiled VBA internals and external control implementation are not covered.'
    ],
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    records = []
    for name, (relative, count) in SOURCES.items():
        source = ROOT / 'models/XBeach/raw/source_code/trunk' / relative
        pages = sorted((SCRATCH / name).glob('page-*.png'), key=lambda p: int(p.stem.split('-')[-1]))
        assert len(pages) == count
        target = OUT / name
        target.mkdir(exist_ok=True)
        artifacts = []
        for page in pages:
            dst = target / page.name
            shutil.copyfile(page, dst)
            artifacts.append({'path': str(dst.relative_to(ROOT)), 'sha256': sha(dst.read_bytes()),
                              'physical_render_page': int(page.stem.split('-')[-1])})
        container = []
        if zipfile.is_zipfile(source):
            with zipfile.ZipFile(source) as handle:
                for item in handle.infolist():
                    data = handle.read(item)
                    container.append({'path': item.filename, 'bytes': len(data), 'sha256': sha(data)})
        else:
            with olefile.OleFileIO(source) as handle:
                for item in handle.listdir():
                    data = handle.openstream(item).read()
                    container.append({'path': '/'.join(item), 'bytes': len(data), 'sha256': sha(data)})
        records.append({'path': str(source.relative_to(ROOT)), 'sha256': sha(source.read_bytes()),
                        'render_pages': count, 'reader': 'Codex /root, 2026-09-10',
                        'read_status': 'displayed-document-content-read; container-internals-scope-disclosed',
                        'method': 'LibreOffice 24.2.7 PDF export; pdftoppm scale-to 1600; all pages visually inspected. Large sheets used for page review; equations recovered separately where overlap occurred.',
                        'notes': NOTES[name], 'render_evidence': artifacts,
                        'container_members': container,
                        'container_scope': 'Every member hashed; document content/rendered resources read. This is not a claim of semantic review of every XML formatting field or compiled object byte.'})
    formula = OUT / 'curvilinear grid properties' / 'all-formulas.png'
    shutil.copyfile(SCRATCH / 'wmf/all-formulas.png', formula)
    supplementary = [{'path': str(formula.relative_to(ROOT)), 'sha256': sha(formula.read_bytes()),
                      'scope': 'All nine original WMF formula previews; resolves slide 14 overlap.'}]
    for name, textfile in [('members', SCRATCH / 'members.txt')]:
        supplementary.append({'scratch_path': str(textfile), 'sha256': sha(textfile.read_bytes()),
                              'scope': 'Full unclipped body text read; regenerated from original DOC using LibreOffice Text export.'})
    result = {'date': '2026-09-10', 'scope': 'Five Office documents, 36 rendered pages. No whole-model or human approval.',
              'records': records, 'supplementary_evidence': supplementary, 'human_approval_issued': False}
    (OUT / 'read-receipts.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print('Persisted', len(records), 'document records and', sum(r['render_pages'] for r in records), 'page images')


if __name__ == '__main__':
    main()

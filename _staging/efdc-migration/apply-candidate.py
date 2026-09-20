#!/usr/bin/env python3
"""Bounded EFDC candidate migration; canonical files are only read.

All line numbers are those in the original notes. Coordinate operations precede
semantic operations. The ledger records each operation, including overlaps.
"""
import csv
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '_staging/efdc-migration'
CAND = OUT / 'wiki-candidate'
PRE = ROOT / '_staging/efdc-prescan'
OLD = ROOT / 'models/EFDC/raw/source_code/EFDCPlus_Stable'
sys.path.insert(0, str(ROOT / '_staging/model-migration-framework'))
import refparser as rp

ENDPOINT_ONLY = '--endpoint-only' in sys.argv
EXTRA_FINDING = '--extra-finding' in sys.argv
notes = {str(p.relative_to(CAND)): (ROOT / p.relative_to(CAND)).read_text()
         for p in sorted(CAND.rglob('*.md'))}
assert len(notes) == 31
lines = {p: t.splitlines(keepends=True) for p, t in notes.items()}
rows = list(csv.DictReader((OUT / 'line-ref-map.csv').open()))
ledger = []
allowed = set()
coord_checks = []
semantic_spans = []

def record(note, line, category, before, after, evidence, applied='yes'):
    ledger.append(dict(note=note, note_line=line, category=category, applied=applied,
                       evidence=evidence, note_text_before=before.rstrip('\n'),
                       note_text_after=after.rstrip('\n')))

def replace_line(note, line, text, category, evidence):
    before = lines[note][line-1]
    after = text + '\n'
    lines[note][line-1] = after
    allowed.add((note, line))
    record(note, line, category, before, after, evidence)

def change(note, start, end, transform, evidence, report_line=None):
    before = ''.join(lines[note][start-1:end])
    after = transform(before)
    assert before != after, (note, start)
    if not after.endswith('\n'):
        after += '\n'
    lines[note][start-1] = after
    for i in range(start, end):
        lines[note][i] = ''
    allowed.update((note, i) for i in range(start, end+1))
    semantic_spans.append((note, start, end))
    record(note, report_line or start, 'A', before, after, evidence)

def numbers_only(ref, new):
    # Preserve every character except coordinate digits: L, dashes, commas,
    # whitespace, relative paths and bracket syntax are copied verbatim.
    m = rp.BRACKET_RE.fullmatch(ref) or rp.FILE_RE.fullmatch(ref)
    assert m and m.group('lines')
    nums = iter(re.findall(r'\d+', new))
    old_text = m.group('lines')
    assert len(re.findall(r'\d+', old_text)) == len(re.findall(r'\d+', new))
    new_text = re.sub(r'\d+', lambda _: next(nums), old_text)
    return ref[:m.start('lines')] + new_text + ref[m.end('lines'):]

# Baseline receipts cover original notes and all supplied source/input files.
baseline_path = OUT / 'baseline-sha256.json'
baseline_files = [ROOT / p for p in notes]
baseline_files += [ROOT / r['note'] for r in rows]
baseline_files += [OLD / r['source'] for r in rows]
baseline_files += [OUT / n for n in ('codex-task.md', 'line-ref-map.csv', 'final-classification.csv')]
baseline_files += sorted((PRE / 'new').glob('*')) + sorted((PRE / 'patches').glob('*'))
hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in baseline_files if p.is_file()}
if baseline_path.exists():
    previous = json.loads(baseline_path.read_text())
    assert all(hashes.get(p) == h for p, h in previous.items()), 'Read-only baseline changed'
    if previous != hashes:
        baseline_path.write_text(json.dumps(hashes, ensure_ascii=False, indent=2) + '\n')
else:
    assert all((CAND / p).read_text() == t for p, t in notes.items())
    baseline_path.write_text(json.dumps(hashes, ensure_ascii=False, indent=2) + '\n')

# C: independently compare endpoints and complete cited intervals.
for row in rows:
    if row['status'] != 'MOVED':
        continue
    note, ln = row['note'], int(row['note_line'])
    old_src = (OLD / row['source']).read_text().splitlines()
    new_src = (PRE / 'new' / row['source'].replace('/', '__')).read_text().splitlines()
    pairs = list(zip(rp.parse_ranges(row['old']), rp.parse_ranges(row['new'])))
    endpoints = all(old_src[a-1] == new_src[c-1] and old_src[b-1] == new_src[d-1]
                    for (a, b), (c, d) in pairs)
    complete = all(old_src[a-1:b] == new_src[c-1:d] for (a, b), (c, d) in pairs)
    coord_checks.append(dict(note=note, note_line=ln, ref=row['ref'], new=row['new'],
                             endpoints_equal=endpoints, complete_ranges_equal=complete))
    before = lines[note][ln-1]
    assert before.count(row['ref']) == 1, row
    if endpoints and (complete or ENDPOINT_ONLY):
        target = numbers_only(row['ref'], row['new'])
        after = before.replace(row['ref'], target, 1)
        lines[note][ln-1] = after
        allowed.add((note, ln))
        detail = 'complete ranges equal' if complete else 'endpoints equal; interior differs'
        record(note, ln, 'C', before, after, row['source'] + ':' + row['new'] + '; ' + detail)
    else:
        detail = 'UNRESOLVED_SOURCE_REFERENCE: ' + ('range interior differs' if endpoints else 'endpoint differs')
        record(note, ln, 'C', before, before, row['source'] + ':' + row['new'] + '; ' + detail, 'unresolved')

M = 'models/EFDC/'
S = M + 'source-analysis/'
V = S + 'efdc_vertical.md'
T = S + 'efdc_transport_scheme.md'
E = S + 'efdc_baroclinic_eos.md'
I = M + 'manual-notes/efdc-implementation-guide.md'
U = M + 'manual-notes/efdc-user-manual-r850.md'
BC = S + 'efdc_boundary_conditions.md'
SED = S + 'sediment/efdc_sediment.md'

# D: choices confirmed by reading v12.5 code, not by accepting candidate endpoints.
d_targets = {
    (M+'manifest.md', 17): ('EFDC/aaefdc.f90:22', 'release header remains at 22; date at 30'),
    (I, 193): ('input.f90:311', 'C6 read, scalar ISQUICK'),
    (U, 104): ('input.f90:311', 'C6 read, scalar ISQUICK'),
    (BC, 19): ('input.f90:269, 570, 755-778, 884-901, 903-1395, 1445-1470, 2818-3092, 3753-3781, 5801-5836, 5868-5906, 6009-6428', 'C15 closes at 901; surviving MODCHAN read closes at 3781'),
    (BC, 85): ('input.f90:1445-1452', 'C23 read at 1450 inside master block ending at 1452'),
    (T, 28): ('calconc.f90:117-132', 'upwind gate at 117 and LUPU/LUPV assignments at 123-132'),
    (T, 65): ('input.f90:311', 'C6 read, scalar ISQUICK'),
    (V, 24): ('calexp.f90:243-406, 1152, 1169-1222', 'vertical advection unchanged; complete IGRIDV branch ends at 1222'),
    (V, 80): ('calexp.f90:1169', 'IGRIDV == 1 branch'),
    (V, 81): ('calexp.f90:1187', 'IGRIDV > 1 branch'),
    (V, 82): ('calexp.f90:1206-1207', 'else / STANDARD-SIGMA branch'),
    (SED, 205): ('Transport/calconc.f90:198-203', 'ISQUICK dispatch to CALTRAN_QUICKEST or CALTRAN'),
}
for row in rows:
    if row['status'] != 'REANCHOR_REQUIRED':
        continue
    key = (row['note'], int(row['note_line']))
    target, detail = d_targets[key]
    before = lines[key[0]][key[1]-1]
    assert before.count(row['ref']) == 1
    after = before.replace(row['ref'], target, 1)
    lines[key[0]][key[1]-1] = after
    allowed.add(key)
    record(*key, 'D', before, after, row['source'] + ':' + target.split(':', 1)[1] + '; ' + detail)

# A1: version/date only; clone SHA and historical acquisition metadata preserved.
change(M+'manifest.md', 17, 17,
       lambda s: s.replace('12.4', '12.5').replace('DATE 2025-12-29', 'DATE 2026-05-26'),
       'EFDC/aaefdc.f90:22,30')

# A2: retain the manual C5 option listing and IINTPG field; append only specified delta.
def a2(s):
    chunks = s.splitlines(keepends=True)
    chunks[0] = chunks[0].rstrip('\n') + ' v12.5 C5 read에서는 `ISDISP` 슬롯을 `ldum`으로, `ISQQ` 슬롯을 `ICALTB`로 읽고, 13번째 필드 `ISHDMFILTER`를 읽는다. `IINTPG` 입력 필드는 유지된다 (`input.f90:269`).\n'
    chunks[4] = '> ⚠️ **v12.5 소스 드리프트**: v12.5의 C6 read는 `ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)` (`input.f90:311`) — **3번째 슬롯은 scalar `ISQUICK`**, **6·7·8번째 슬롯은 더미(`ldum`)로 읽고 버린다**. `ISQUICK`은 broadcast되며 (`input.f90:316`), 0/1 외 값은 경고 후 0으로 리셋된다 (`input.f90:318-325`).\n'
    return ''.join(chunks)
change(I, 189, 193, a2, 'EFDC/input.f90:269,311,316,318-325', report_line=193)

# A3: retain the historical assertion and add a clearly delimited v12.5 delta.
change(U, 104, 104,
       lambda s: '> - **C6**: 매뉴얼 r850 기준의 3번째 슬롯은 `ISCDCA`; 위 v12.4 소스 드리프트에서는 3·6·7·8번째 슬롯(`ISCDCA` 등)이 `ldum` 더미로 버려졌다. **v12.5 델타**: 3번째 슬롯은 scalar `ISQUICK`이고 6·7·8번째 슬롯은 계속 `ldum`이다 (`input.f90:311`). `ISQUICK`은 broadcast되며 (`input.f90:316`), 0/1 외 값은 경고 후 0으로 리셋된다 (`input.f90:318-325`).\n',
       'EFDC/input.f90:311,316,318-325')

# A4: H1/summary/dispatch only. Frontmatter title remains untouched by contract.
def a4(s):
    s = s.replace('# EFDC+ scalar transport 수치 스킴 — CALTRAN / CALTRAN_AD',
                  '# EFDC+ scalar transport 수치 스킴 — CALTRAN / CALTRAN_AD / QUICKEST·ULTIMATE')
    s = s.replace('**모든 scalar(염분·수온·dye·SFL·toxic·SED·SND·WQ)의 advection 수치 알고리즘** = **1차 donor-cell upwind + Smolarkiewicz MPDATA anti-diffusive corrector**.',
                  '**scalar(염분·수온·dye·SFL·toxic·SED·SND·WQ)의 advection 수치 알고리즘** = **1차 donor-cell upwind + Smolarkiewicz MPDATA anti-diffusive corrector**, v12.5 active WC dispatch에는 **`ISQUICK == 1` QUICKEST/ULTIMATE** 경로가 추가됐다 (`calconc.f90:198-203`).')
    s = s.replace('1. **upwind cell 사전지정** (`calconc.f90:117-132`):',
                  '1. **upwind cell 사전지정** (`calconc.f90:117-132`): `ISQUICK == 0 .or. ISTRAN(4) > 0 .or. (ISTRAN(2) > 0 .and. ISICE == 4)`일 때 수행.')
    s = s.replace('2. `CALTRAN`(IW) — donor-cell upwind 1차 update (모든 active WC).',
                  '2. `ISQUICK == 1`이면 `CALTRAN_QUICKEST`(IW) — QUICKEST/ULTIMATE, 그 외에는 `CALTRAN`(IW) — donor-cell upwind 1차 update (모든 active WC, `calconc.f90:198-203`). 신규 구현: `EFDC/Transport/caltran_quickest.f90:14-33`, `EFDC/Transport/mod_quickest.f90:80-101` (v12.5 좌표).')
    s = s.replace('3. `ISADAC>0` constituent → `CALTRAN_AD`(IW) — anti-diffusive 보정',
                  '3. `ISQUICK == 0`일 때만 `CALTRAN_AD`(IW) 호출 및 `ISADAC` anti-diffusive 보정 (`calconc.f90:228-230, 250`)')
    return s
change(T, 18, 35, a4,
       'EFDC/Transport/calconc.f90:117-132,198-203,228-230,250; EFDC/Transport/caltran_quickest.f90:14-33; EFDC/Transport/mod_quickest.f90:80-101 (full-addition patches)', report_line=28)

# A5: explicit C6 scalar and anti-diffusion gates.
def a5(s):
    s = s.replace('## 4. ISADAC / ISFCT — constituent별 토글', '## 4. ISQUICK / ISADAC / ISFCT — scalar 스킴 선택·constituent별 토글')
    s = s.replace('입력 카드(constituent별, C14 염분 ~ ):', '입력 카드 C6(constituent별; `ISQUICK`은 scalar):')
    s = s.replace('read ISTRAN(NS), ISTOPT(NS), -,', 'read ISTRAN(NS), ISTOPT(NS), ISQUICK,')
    s = s.replace('| **ISADAC(NS)** |', '| **ISQUICK** | scalar: 0 = donor-cell upwind / 1 = QUICKEST·ULTIMATE. Broadcast (`input.f90:316`), 0/1 외 값은 경고 후 0으로 리셋 (`input.f90:318-325`) |\n| **ISADAC(NS)** |')
    s = s.replace('→ **ISADAC=1 + ISFCT=1**', '→ **`ISQUICK == 0`일 때 ISADAC=1 + ISFCT=1**')
    s = s.replace('ISADAC=0 = 순수 upwind', '`ISQUICK == 0`에서 ISADAC=0 = 순수 upwind')
    return s.rstrip('\n') + ' `CALTRAN_AD` 호출은 `ISQUICK == 0`일 때만 발생하고 (`calconc.f90:228-230`), `ISADAC` 반확산 적용도 동일 게이트를 사용한다 (`calconc.f90:250`).\n'
change(T, 65, 77, a5, 'EFDC/input.f90:311,316,318-325; EFDC/Transport/calconc.f90:228-230,250')

# A6 and A7.
change(SED, 205, 205,
       lambda s: 'With `ISQUICK == 1`, CALTRAN_QUICKEST transports every active constituent through `WCV`; otherwise CALTRAN does (`Transport/calconc.f90:198-203`); anti-diffusion is gated by `ISQUICK == 0` at `:228-230, 250`.\n',
       'EFDC/Transport/calconc.f90:198-203,228-230,250')
change(S+'efdc_water_quality.md', 106, 107,
       lambda s: s.replace('mod_diagen.f90:164-277', 'mod_diagen.f90:164-276').replace('Sediment zones, restart controls.', 'Sediment zones.'),
       'EFDC/Eutrophication/mod_diagen.f90:164-276; ISMRST and write_restart_option: 0 case-insensitive occurrences in complete new file')

# A8-10: one record per table row; the first also includes the introductory facts.
pg_evidence = 'EFDC/calexp.f90:1167-1222; EFDC/calexp2t.f90:1246-1305; EFDC/input.f90:269; EFDC/setbcs.f90:447-474'
def a8(s):
    s = s.replace('## E. Sigma-slope pressure-gradient (IINTPG)', '## E. Sigma-slope pressure-gradient (IGRIDV; IINTPG legacy input)')
    s = s.replace('- `IINTPG` read at `input.f90:269`.', '- `IINTPG` is still read at `input.f90:269`, but EFDC+ Stable 12.5 no longer uses it to select buoyancy shear. Its only remaining behavioral consumer is `setbcs.f90:449`: `IINTPG /= 0` disables the external density-gradient cell-face flag treatment for 2-cell-wide channels. In `calexp2t.f90` (2TL), the four `IINTPG` occurrences were also removed (`calexp2t.f90:1246-1305`).')
    s = s.replace('- SGZ branches override first (used when `IGRIDV>0`):', '- Buoyancy shear branches use `IGRIDV`; SGZ branches apply when `IGRIDV>0`:')
    s = s.replace('- Sigma branches (used when `IGRIDV == 0`):', '- v12.5 branches:')
    s = s.replace('| `IINTPG` | Branch | File:Line |', '| `IGRIDV` | Branch | File:Line |')
    s = s.replace('| `0` | Standard density Jacobian | `calexp.f90:1169` |', '| `== 1` | Sigma-Zed buoyancy shears | `calexp.f90:1169` |')
    return s
change(V, 70, 80, a8, pg_evidence, report_line=80)
change(V, 81, 81, lambda s: s.replace('| `1` | Improved sigma-slope correction |', '| `> 1` | Sigma-Zed buoyancy shears |'), pg_evidence)
change(V, 82, 82, lambda s: s.replace('| `2` | Finite-volume formulation |', '| else | STANDARD-SIGMA buoyancy shears |'), pg_evidence)

# A11: the explicit heading update is independently supported, even if its C
# whole-range equality check is unresolved.
def a11(s):
    return '''## 4. 내부모드 buoyancy shear FBBX/FBBY (calexp.f90:1162-1295)

`BSC>1.E-6 .and. KC>1` 게이트(:1167). **EFDC+ Stable 12.5의 buoyancy shear 분기축은 IGRIDV**:
```
IGRIDV==1 : SIGMA-ZED      (:1169)
IGRIDV>1  : SIGMA-ZED      (:1187)
else      : STANDARD-SIGMA (:1206-1207)
```
`IINTPG`는 입력으로 계속 읽히지만 (`input.f90:269`) buoyancy shear 분기에는 더 이상 쓰이지 않는다. `calexp2t.f90`(2TL)에서도 `IINTPG` 출현은 4→0으로 제거됐다 (`calexp2t.f90:1246-1305`). 유일한 동작 소비처는 `setbcs.f90:449`의 `if( IINTPG == 0 )` — 2-cell-wide 수로의 external density gradient cell-face flag 처리이며, `IINTPG /= 0`은 이 처리를 끈다.
'''
change(E, 75, 83, a11, pg_evidence + '; EFDC/calexp.f90:1162-1295')

# B: six specified prose sites, preserving their surrounding claims.
en = ('For EFDC+ Stable 12.5, the `IINTPG` buoyancy-shear branches were removed; '
      'use `IGRIDV>0` (SGZ) for steep bathymetry. `IINTPG /= 0` disables the '
      '2-cell-wide channel external density-gradient cell-face flag treatment at `setbcs.f90:449`.')
replace_line(V, 84, 'There is **no single named "sigma-slope error correction" symbol**; ' + en[0].lower() + en[1:], 'B', pg_evidence)
replace_line(V, 108, '| Steep slope / canyon | `>0` (SGZ) | `0` | EFDC+ Stable 12.5 removed the `IINTPG` buoyancy-shear branches; `IINTPG /= 0` disables the 2-cell-wide channel external density-gradient cell-face flag treatment at `setbcs.f90:449` |', 'B', pg_evidence)
replace_line(V, 118, lines[V][117].rstrip('\n').replace('cure with `IINTPG=2`.', en[0].lower() + en[1:]), 'B', pg_evidence)
replace_line(V, 126, '- ▢ ' + en, 'B', pg_evidence)
replace_line(S+'efdc_hydro_core.md', 99, '| Density-stratified estuary | 3TL + `ISBAL=2` (S+T); ' + en[0].lower() + en[1:] + ' |', 'B', pg_evidence)
sst = 'concepts/sst/06-model-application.md'
replace_line(sst, 75, lines[sst][74].rstrip('\n').replace('만들 수 있어 `IINTPG=1/2` 권장 (efdc_vertical.md §E·Working Rules).',
    '만들 수 있다. **EFDC+ Stable 12.5 기준**으로는 `IINTPG` buoyancy shear 분기가 제거됐으며 급경사 대응은 `IGRIDV>0`(SGZ)을 사용한다. `IINTPG /= 0`은 `setbcs.f90:449`의 2-cell-wide 수로 external density gradient cell-face flag 처리를 끄는 부작용이 있다 (efdc_vertical.md §E·Working Rules).'), 'B', pg_evidence)
if EXTRA_FINDING:
    replace_line(E, 90, '- **EFDC+ Stable 12.5 기준**: `IINTPG` buoyancy shear 분기는 제거됐고 급경사 대응은 `IGRIDV>0`(SGZ)이다. `IINTPG /= 0`은 `setbcs.f90:449`의 2-cell-wide 수로 external density gradient cell-face flag 처리를 끈다.', 'B', pg_evidence)

# No writes until the entire candidate and immutable guards have passed.
final = {p: ''.join(ls) for p, ls in lines.items()}
fm_re = re.compile(r'\A---\n.*?\n---', re.S)
for p, text in final.items():
    fm = fm_re.match(notes[p])
    if fm:
        assert fm_re.match(text).group() == fm.group(), ('frontmatter', p)
    for ln, old_line in enumerate(notes[p].splitlines(keepends=True), 1):
        if old_line != lines[p][ln-1]:
            assert (p, ln) in allowed, ('out-of-scope line', p, ln)
for row in rows:
    if row['status'] == 'IDENTICAL':
        p, ln = row['note'], int(row['note_line'])
        if p not in lines:
            assert row['ref'] in (ROOT / p).read_text().splitlines()[ln-1]
            continue  # Not among the 31 writable copies; original remains untouched.
        spans = [(a, b) for name, a, b in semantic_spans if name == p and a <= ln <= b]
        fragment = ''.join(lines[p][spans[0][0]-1:spans[0][1]]) if spans else lines[p][ln-1]
        assert row['ref'] in fragment, ('IDENTICAL citation changed', row)
assert lines[V][132] == notes[V].splitlines(keepends=True)[132]
assert '`IINTPG`(0=원 internal pressure gradient, 1=Jacobian, 2=finite volume)' in final[I]
for p, text in final.items():
    target = CAND / p
    if target.read_text() == text:
        continue
    # The user-owned copies inherit read-only file modes. Atomic replacement
    # edits only the authorized staging copy, without chmod/chown/unlocking.
    assert not target.is_symlink() and target.stat().st_nlink == 1
    temporary = target.with_name(target.name + '.codex-tmp')
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, target.stat().st_mode & 0o777)
    with os.fdopen(fd, 'w') as f:
        f.write(text)
    temporary.replace(target)
with (OUT / 'apply-report.csv').open('w', newline='') as f:
    fields = ['note', 'note_line', 'category', 'applied', 'evidence', 'note_text_before', 'note_text_after']
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(ledger)
(OUT / 'coordinate-checks.json').write_text(json.dumps(coord_checks, ensure_ascii=False, indent=2) + '\n')
patches = []
for p in sorted(notes):
    result = subprocess.run(['git', 'diff', '--no-index', '--no-ext-diff', '--no-color', '--',
                             p, str((CAND / p).relative_to(ROOT))], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode in (0, 1), result.stderr
    # Normalize the destination prefix only; the body is git diff --no-index output.
    patches.append(result.stdout.replace('b/_staging/efdc-migration/wiki-candidate/', 'b/'))
(OUT / 'wiki-candidate.diff').write_text(''.join(patches))
summary = dict(rows=len(ledger), counts={f'{k[0]}/{k[1]}': v for k, v in Counter((r['category'], r['applied']) for r in ledger).items()},
               changed_notes=sum(notes[p] != final[p] for p in notes), identical_references_preserved=167,
               frontmatter_preserved=True, read_only_baseline_unchanged=True,
               endpoint_only=ENDPOINT_ONLY, extra_finding=EXTRA_FINDING)
(OUT / 'apply-summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))

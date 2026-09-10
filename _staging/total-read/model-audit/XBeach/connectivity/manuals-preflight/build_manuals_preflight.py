#!/usr/bin/env python3
import csv, hashlib, json, mimetypes, subprocess
from collections import Counter, defaultdict
from pathlib import Path

REPO=Path(__file__).resolve().parents[6]
RAW=REPO/'models/XBeach/raw/manuals'; TR=REPO/'_staging/total-read'; OUT=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(p):
 p=str(p).replace('\\','/')
 if p.startswith('XBeach/'): return 'models/'+p
 return p
records={}
for f in (TR/'records').glob('*[xX][bB]each*.jsonl'):
 for line in f.open(errors='replace'):
  try:o=json.loads(line)
  except:continue
  p=norm(o.get('path',''))
  if p.startswith('models/XBeach/raw/manuals/'):
   records[(p,o.get('sha256') or o.get('source_sha256'))]=(o,str(f.relative_to(REPO)))

# Converted full-read representations with original-source SHA provenance.
derived={
 '6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4':('XBeach_manual_kingsday.md','full-text-conversion-read; page-aware mapping exists'),
 '6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7':('XBeach_manual_master.md','full-text-conversion-read; page-aware mapping exists'),
 'd170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005':('non-hydrostatic_report_draft.md','full-text-conversion-read; page-aware mapping exists'),
 'fdbb957018000eb63827cbe0c517e6667b31ae530c017849dd9e6c5e042d8d20':('Parallellization_report.md','INCOMPLETE: prose/plots largely absent; 205 image references not visually read'),
}
files=sorted(p for p in RAW.rglob('*') if p.is_file()); rows=[]; groups=defaultdict(list)
for p in files:
 rel=p.relative_to(REPO).as_posix(); s=sha(p); groups[s].append(rel); o,ef=records.get((rel,s),({},'')); st=o.get('read_status','none')
 d=derived.get(s); conversion='none'; effective=st
 if d:
  conversion=d[1]
  if s!='fdbb957018000eb63827cbe0c517e6667b31ae530c017849dd9e6c5e042d8d20': effective='complete-via-sha-bound-conversion'
  else: effective='incomplete-conversion-image-gap'
 rows.append({'path':rel,'sha256':s,'bytes':p.stat().st_size,'extension':p.suffix.lower() or '[none]','mime':mimetypes.guess_type(p.name)[0] or subprocess.run(['file','--mime-type','-b',str(p)],capture_output=True,text=True).stdout.strip(),'direct_record_status':st,'direct_read_range':o.get('read_range',''),'direct_reader':o.get('reader',''),'direct_evidence_file':ef,'sha_bound_conversion':d[0] if d else '','conversion_scope':conversion,'effective_semantic_status':effective})
for r in rows:
 r['duplicate_count']=len(groups[r['sha256']]); r['duplicate_paths']=' | '.join(groups[r['sha256']]) if len(groups[r['sha256']])>1 else ''
with (OUT/'manuals-read-coverage.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
gaps=[r for r in rows if r['effective_semantic_status'] not in ('complete','complete-via-sha-bound-conversion')]
(OUT/'remaining-incomplete-or-unread.txt').write_text(''.join(r['path']+'\n' for r in gaps))
summary={'files':len(rows),'bytes':sum(r['bytes'] for r in rows),'unique_sha256':len(groups),'exact_sha_record_matches':sum(bool(r['direct_evidence_file']) for r in rows),'direct_complete':sum(r['direct_record_status']=='complete' for r in rows),'direct_partial':sum(r['direct_record_status']=='partial' for r in rows),'direct_failed':sum(r['direct_record_status']=='failed' for r in rows),'complete_via_sha_bound_conversion':sum(r['effective_semantic_status']=='complete-via-sha-bound-conversion' for r in rows),'effective_complete_union':sum(r['effective_semantic_status'] in ('complete','complete-via-sha-bound-conversion') for r in rows),'remaining_incomplete_or_unread':len(gaps),'remaining_statuses':dict(Counter(r['effective_semantic_status'] for r in gaps)),'duplicate_sha_groups':sum(len(v)>1 for v in groups.values()),'paths_in_duplicate_groups':sum(len(v) for v in groups.values() if len(v)>1),'records_sources':sorted(set(r['direct_evidence_file'] for r in rows if r['direct_evidence_file'])),'finding_207_scope':'207 is HIGH unresolved findings from 6 converted representations of 3 works in XBeach-X00; it is not an 87-file read ledger.'}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
validation={'path_set_exact':set(r['path'] for r in rows)==set(p.relative_to(REPO).as_posix() for p in files),'all_sha_rechecked':all(sha(REPO/r['path'])==r['sha256'] for r in rows),'row_count':len(rows)};validation['pass']=all(validation.values())
(OUT/'validation.json').write_text(json.dumps(validation,indent=2)+'\n')

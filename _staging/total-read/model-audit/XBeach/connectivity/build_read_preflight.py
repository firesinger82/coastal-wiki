#!/usr/bin/env python3
"""Reconcile source snapshot reading evidence without promoting metadata to reading."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
OUT=Path(__file__).resolve().parent
AUDIT=OUT.parent
RAW=ROOT/'models/XBeach/raw/source_code'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 inventory=json.loads((AUDIT/'xb-inventory.json').read_text())
 actual={str(p.relative_to(RAW)):p for p in RAW.rglob('*') if p.is_file()}
 assert set(actual)=={r['path'] for r in inventory}
 rows={r['path']:{'path':r['path'],'sha256':sha(actual[r['path']]),'bytes':actual[r['path']].stat().st_size,'status':'unreconciled','evidence':[]} for r in inventory}
 assert all(rows[r['path']]['sha256']==r['sha256'] for r in inventory)
 for p in (AUDIT/'cw/crosswalk').rglob('*.crosswalk.json'):
  cw=json.loads(p.read_text());r=rows[cw['source_path']];assert r['sha256']==cw['source_sha256']
  for side in ('base','audit'):
   rp=AUDIT/'cw/records-by-run'/cw[f'{side}_run_id']/cw[f'{side}_record_file']
   assert sha(rp)==cw[f'{side}_record_sha256_bytes']
   record=json.loads(rp.read_text());assert record['source_sha256']==r['sha256'];assert record['read_status']=='complete'
   raw=actual[r['path']].read_bytes(); lf=raw.count(b'\n'); physical=lf+int(bool(raw) and not raw.endswith(b'\n'))
   assert record.get('lines_or_pages') in (lf,physical), (r['path'],record.get('lines_or_pages'),physical)
   r['physical_lf_lines']=physical
   r['extent_note']='Legacy extent matches physical LF or wc-newline count; unterminated final line additionally inspected by root.'
   if lf!=physical:r['last_line_recheck']=raw.split(b'\n')[-1].decode('utf-8',errors='replace')
   r['evidence'].append({'path':str(rp.relative_to(ROOT)),'sha256':sha(rp),'recorded_extent':record.get('lines_or_pages'),'method':record.get('read_method')})
  r['status']='two-independent-source-reads'
 for line in (AUDIT/'XBeach-I00.jsonl').read_text().splitlines():
  x=json.loads(line);r=rows[x['path']];assert r['sha256']==x['sha256'];r['status']='existing-visual-read';r['evidence'].append({'path':str((AUDIT/'XBeach-I00.jsonl').relative_to(ROOT)),'record':x})
 for x in json.loads((AUDIT/'xb-artifact-inventory.json').read_text()):
  r=rows[x['path']];assert r['sha256']==x['sha256'];r['status']='empty' if r['bytes']==0 else 'artifact-inspection-only';r['evidence'].append({'path':str((AUDIT/'xb-artifact-inventory.json').relative_to(ROOT)),'sha256':sha(AUDIT/'xb-artifact-inventory.json')})
 result={'scope':'source_code456 only; manuals87 reconciled separately. No whole-model read gate claimed.','status_counts':{k:sum(r['status']==k for r in rows.values()) for k in sorted({r['status'] for r in rows.values()})},'files':list(rows.values())}
 (OUT/'source-read-preflight.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result['status_counts']))
if __name__=='__main__':main()

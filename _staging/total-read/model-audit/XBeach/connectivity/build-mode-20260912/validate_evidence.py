"""Validate source sets and receipts; never grant semantic or human approval."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[5]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name):return json.loads((HERE/name).read_text())
def bind(f):assert sha(ROOT/f['path'])==f['sha256'],f['path']
def span(e):
 bind(e);raw=(ROOT/e['path']).read_bytes()
 lines=raw.split(b'\n');count=len(lines)-(1 if raw.endswith(b'\n') else 0)
 assert 1 <= e['line_start'] <= e['line_end'] <= count,('citation outside source',e['path'],e['line_start'],e['line_end'],count)
 assert b'\n'.join(lines[e['line_start']-1:e['line_end']]).decode()==e['quote_exact_utf8'],e['path']
def main():
 d=read('build-map.json');src=ROOT/d['source_root']
 assert {f['path'] for f in d['src_files']}=={str(p.relative_to(src)) for p in (src/'src').rglob('*') if p.is_file()}
 for f in d['src_files']+d['projects']+d['solutions']:assert sha(src/f['path'])==f['sha256'],f['path']
 assert {p['path'] for p in d['projects']}=={str(p.relative_to(src)) for p in (src/'src').rglob('*.vfproj')}
 assert {p['path'] for p in d['solutions']}=={p.name for p in src.glob('*.sln')}
 for p in d['projects']:
  assert len({c['name'] for c in p['configs']})==len(p['configs'])
  assert all(f['resolved_path'] and (src/f['resolved_path']).exists() for f in p['files'])
 for e in d['autotools']['evidence']:span(e)
 c=read('contracts.json')
 assert {m['id'] for m in c['modes']}=={'stationary','surfbeat_directional','surfbeat_single_dir','nonh_one_layer','nonh_two_layer_2dv','nonh_two_layer_3d'}
 for e in c['source_evidence']+[x['source'] for x in c['definitions']]:span(e)
 for f in c['document_sources']+c['visual_evidence']+[c['prior_glyph_receipt']]:bind(f)
 g=read('generation-probe.json');assert g['exit_code']==0
 for f in g['inputs']:bind(f)
 assert {f['name'] for f in g['outputs']}=={f['output'] for f in d['generation']}
 generated={f['name'] for f in g['outputs']}
 assert all(i['include'] in generated for i in d['include_index'] if i['consumer_listed'] and i['include'].endswith('.inc'))
 baseline=json.loads((ROOT/'_staging/total-read/model-audit/XBeach/closure/immutable-baseline.json').read_text())['files']
 for name,h in baseline.items():assert sha(ROOT/name)==h,name
 installed=0
 if (HERE/'install-manifest.json').exists():
  for f in read('install-manifest.json')['files']:
   assert sha(ROOT/f['candidate'])==f['after_sha256'],f['candidate']
   assert sha(ROOT/f['target'])==f['after_sha256'],f['target']
   installed+=1
 if (HERE/'review-response.json').exists():
  r=read('review-response.json')
  for f in r['reviews']+r['reviewed_artifacts']:bind(f)
 result={'status':'PASS','scope':'Source-set, exact-citation, generator, immutable-history and installed-byte checks only','src_files':len(d['src_files']),'model_projects':len(d['projects']),'project_configurations':sum(len(p['configs']) for p in d['projects']),'solutions':len(d['solutions']),'dispatcher_paths':len(c['modes']),'generated_includes':len(g['outputs']),'source_spans':len(c['source_evidence'])+len(c['definitions'])+len(d['autotools']['evidence']),'document_pages':len(c['visual_evidence']),'immutable_files':len(baseline),'installed_files':installed,'human_approval_issued':False}
 (HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()

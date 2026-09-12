"""Bind lifecycle claims and probe receipts to source bytes; not an approval gate."""
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[6]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    errors=[]
    d=json.loads((HERE/'adjudication.json').read_text())
    assert {f['id'] for f in d['findings']}=={f'XB-SC-{i:03}' for i in range(1,13)}
    for e in d['evidence']:
        path=ROOT/e['path'];raw=path.read_bytes()
        quote=b'\n'.join(raw.split(b'\n')[e['line_start']-1:e['line_end']]).decode()
        if sha(path)!=e['sha256'] or quote!=e['quote_exact_utf8']:errors.append(f"citation drift: {e['path']}:{e['line_start']}")
    original=d['original_ledger']
    if sha(ROOT/original['path'])!=original['sha256']:errors.append('historical lifecycle ledger changed')
    baseline=json.loads((ROOT/'_staging/total-read/model-audit/XBeach/closure/immutable-baseline.json').read_text())['files']
    for name,h in baseline.items():
        if sha(ROOT/name)!=h:errors.append(f'immutable history changed: {name}')
    probe=json.loads((HERE/'probe-results.json').read_text())
    for e in probe['source_spans']:
        path=ROOT/e['path'];raw=path.read_bytes()
        fragment=b'\n'.join(raw.split(b'\n')[e['first']-1:e['last']]).decode().replace('\r\n','\n').replace('\r','')
        if sha(path)!=e['sha256'] or hashlib.sha256(fragment.encode()).hexdigest()!=e['extracted_sha256']:errors.append('extracted source drift')
    for r in probe['runs']:
        if sha(HERE/(r['probe']+'.f90'))!=r['program_sha256']:errors.append('compiled probe source drift')
        expected=1 if r['probe']=='error_path_probe' and r['args']==['1'] else 0
        if r['exit_code']!=expected:errors.append('unexpected probe result')
        if expected==1 and (not r['serial_stop_1_observed'] or 'RETURNED=' in r['stdout']):errors.append('fatal path returned')
    installed=0
    manifest=HERE/'install-manifest.json'
    if manifest.exists():
        for f in json.loads(manifest.read_text())['files']:
            if sha(ROOT/f['candidate'])!=f['after_sha256']:errors.append(f"candidate drift: {f['target']}")
            target=ROOT/f['target']
            if not target.exists() or sha(target)!=f['after_sha256']:errors.append(f"target not installed: {f['target']}")
            else:installed+=1
    result={'scope':'source/receipt/install binding only, no semantic or human approval','status':'FAIL' if errors else 'PASS','contracts':len(d['findings']),'source_spans':len(d['evidence']),'source_probe_runs':len(probe['runs']),'immutable_files':len(baseline),'installed_files':installed,'errors':errors}
    (HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
    raise SystemExit(bool(errors))
if __name__=='__main__':main()

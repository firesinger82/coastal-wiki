#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=Path(__file__).resolve().parents[7]
audit=json.loads((HERE/'numeric-audit.json').read_text())
receipts=[json.loads(x) for x in (HERE/'numeric-read-receipts.jsonl').read_text().splitlines() if x]
files=[f for c in audit['cases'].values() for f in c['files'].values()]
checks={
 'file_count_7':len(files)==7,
 'receipt_count_7':len(receipts)==7,
 'token_total_10258554':sum(f['numeric_tokens'] for f in files)==10258554,
 'all_rectangular':all(f['all_rows_same_width'] for f in files),
 'all_finite':all(f['nonfinite_count']==0 for f in files),
 'all_sha_rechecked':all(hashlib.sha256((REPO/f['path']).read_bytes()).hexdigest()==f['sha256'] for f in files),
 'receipt_path_sha_exact':{(r['path'],r['sha256']) for r in receipts}=={(f['path'],f['sha256']) for f in files},
 'figures_present':all((HERE/c['figure']).is_file() and (HERE/c['figure']).stat().st_size>0 for c in audit['cases'].values()),
 'grid_shapes_match_params':all(all(c['params_relation']['bed_x_y_shape_matches_params'].values()) for c in audit['cases'].values()),
 'chezy_active_window_all_50':audit['cases']['Bijleveld_surfbeat_s200']['params_relation']['snapshot_line_reader_consumed_window']['unique_values_count_then_value']==[[73383,50.0]],
}
out={'checks':checks,'pass':all(checks.values())}
(HERE/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

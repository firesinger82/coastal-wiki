"""Check candidate integrity, citation metadata and preservation; no solver run."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'tools' / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def frontmatter(text):
    require(text.startswith('---\n'), 'Missing frontmatter')
    return yaml.safe_load(text.split('---', 2)[1])


if __name__ == '__main__':
    baseline = json.loads((HERE / 'preservation-before.json').read_text())
    manifest = json.loads((HERE / 'install-manifest.json').read_text())
    links = module('quarter_links', 'validate-link-integrity.py')
    hygiene = module('quarter_hygiene', 'validate-canonical-hygiene.py')
    stems = links.all_note_stems()
    report = {'candidates': [], 'actual_model_execution': False}
    for e in manifest:
        candidate = ROOT / e['source']
        old = (ROOT / e['target']).read_text()
        text = candidate.read_text()
        require(digest(candidate) == e['after_sha256'], 'Candidate SHA drift')
        require(digest(ROOT / e['target']) == e['before_sha256'], 'Canonical SHA drift')
        a, b = frontmatter(old), frontmatter(text)
        for key in ['citation_status', 'has_source_needed', 'verification_by', 'verification_date', 'verification_method']:
            require(a.get(key) == b.get(key), f'Historical status changed: {key}')
        require(b['reference_contract_human_approval'] == 'not-issued', 'Human approval fabricated')
        require('pending' not in b['reference_contract_evidence_by'], 'Opus model unchecked')
        require(not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text), 'Control character')
        broken = links.check_file(e['target'], text, stems)
        require(not any(broken), f'Broken target-relative links: {broken}')
        require(not hygiene.find_local_paths(text), 'Personal paths in canonical candidate')
        require(not hygiene.find_placeholders(text), 'Personal case placeholder')
        report['candidates'].append({'target': e['target'], 'sha256': digest(candidate), 'metadata_links_hygiene': 'PASS'})
    prep = (HERE / 'candidate/adcirc-tide-harmonic-prep.md').read_text()
    require(prep.count('<a id="quarterannular-reference-contract"></a>') == 1, 'Section anchor missing/duplicated')
    for receipt in json.loads((HERE / 'local-source-index.json').read_text()):
        require(digest(ROOT / receipt['path']) == receipt['sha256'], 'Source drift')
    for receipt in json.loads((HERE / 'control-metadata.json').read_text()):
        require(digest(ROOT / receipt['path']) == receipt['sha256'], 'Control file drift')
    for path, sha in baseline['interfaces'].items():
        require(digest(ROOT / path) == sha, 'Unrelated interfaces changed')
    require(digest(ROOT / 'plan.md') == baseline['plan_before_sha256'], 'Plan changed before final pointer update')
    report['source_control_unrelated_preservation'] = 'PASS'
    (HERE / 'preflight.json').write_text(json.dumps(report, indent=2) + '\n')
    print('PASS: two candidates, metadata/links/hygiene, source hashes and unrelated work preserved')

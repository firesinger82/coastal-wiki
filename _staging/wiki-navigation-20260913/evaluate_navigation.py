"""Finite navigation comparison; uses frozen questions, never reads vendor trees."""
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
phase = sys.argv[1]
assert phase in {'before', 'candidate'}
spec = HERE / 'questions.json'
assert hashlib.sha256(spec.read_bytes()).hexdigest() == (HERE/'questions.sha256').read_text().split()[0]
questions = json.loads(spec.read_text())
targets = {e['target'] for e in json.loads((HERE/'inputs.json').read_text())['files']}

def read(rel):
    if rel in targets:
        return (HERE/phase/rel).read_text()
    return (ROOT/rel).read_text()

def links(rel):
    content = re.sub(r'```.*?```', '', read(rel), flags=re.S)
    for match in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', content):
        target = match[1].split('#', 1)[0]
        if not target or '://' in target:
            continue
        path = (ROOT/rel).parent / target
        if path.is_dir():
            path = path/'README.md'
        path = path.resolve()
        if path.is_relative_to(ROOT) and path.is_file() and path.suffix == '.md':
            yield str(path.relative_to(ROOT))

def route(start, target):
    queue = collections.deque([[start]])
    seen = {start}
    while queue:
        path = queue.popleft()
        if path[-1] == target:
            return path
        if len(path)-1 >= questions['max_navigation_hops']:
            continue
        # Intermediate nodes are navigation pages only, not arbitrary content.
        if Path(path[-1]).name not in {'README.md', 'INDEX.md'}:
            continue
        for nxt in links(path[-1]):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(path+[nxt])
    return None

results = []
for q in questions['questions']:
    assert hashlib.sha256((ROOT/q['target']).read_bytes()).hexdigest() == q['target_sha256']
    path = route(q['entry'], q['target'])
    # Visibility needs a human/external review; do not infer semantic PASS from tokens.
    snippets = [s for s in read(q['entry']).splitlines() if Path(q['target']).name in s]
    results.append({'id':q['id'], 'category':q['category'], 'path':path,
                    'hops':len(path)-1 if path else None,
                    'direct':q['target'] in set(links(q['entry'])),
                    'target_citation_status':q['expected_citation_status'],
                    'entry_link_lines':snippets,
                    'disclosure_assessment':'requires recorded human/independent-review interpretation'})
output = {'phase':phase, 'questions_sha256':hashlib.sha256(spec.read_bytes()).hexdigest(),
          'results':results, 'direct_links':sum(r['direct'] for r in results),
          'reachable_within_three_nav_hops':sum(r['path'] is not None for r in results),
          'limit':'Direct/route metrics only, not factual accuracy, approval, overall wiki completion or search quality.'}
(HERE/('navigation-'+phase+'.json')).write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='results'},ensure_ascii=False))

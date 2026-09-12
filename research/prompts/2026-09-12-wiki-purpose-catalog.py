"""Index this finite research packet without promoting sources or author claims."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'research/inbox/2026-09-12-wiki-purpose-review'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name, obj): (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
brief = (OUT/'evidence-brief.md').read_text()
papers = []
for section in re.split(r'\n### P', brief)[1:]:
    section = section.split('\n## ')[0]
    head, body = section.split('\n', 1)
    number, title = head.split('. ', 1)
    papers.append({'id': 'P'+number, 'title_in_brief': title,
                   'bibliographic_note': next(s[2:] for s in body.splitlines() if s.startswith('- ')),
                   'urls': list(dict.fromkeys(re.findall(r'\]\((https?://[^)]+)\)', body))),
                   'checked_extent': next(s[2:] for s in body.splitlines() if s.startswith('- 확인 범위:')),
                   'status': 'candidate-literature; author results not independently reproduced'})
assert len(papers)==8
posts = {}
queries = []
for p in sorted(OUT.glob('grok-*.json')):
    result = json.loads(p.read_text())
    assert result.get('success'), p.name
    annotations = result.get('inline_citations', []) + result.get('citations', [])
    cited = {m[1] for a in annotations for m in
             re.finditer(r'https?://(?:www\.)?(?:x|twitter)\.com/[^/\s]+/status/(\d+)',
                         a if isinstance(a,str) else a.get('url',''))}
    for m in re.finditer(r'https?://(?:www\.)?(?:x|twitter)\.com/[^/\s]+/status/(\d+)', result.get('answer','')):
        sid=m[1]
        post=posts.setdefault(sid, {'status_id':sid, 'urls':[], 'mentioned_by':[],
                                    'tool_annotation_in':[], 'direct_browser_text_verified':False})
        if m[0] not in post['urls']: post['urls'].append(m[0])
        if p.name not in post['mentioned_by']: post['mentioned_by'].append(p.name)
        if sid in cited and p.name not in post['tool_annotation_in']: post['tool_annotation_in'].append(p.name)
    queries.append({'file':p.name, 'sha256':sha(p), 'model':result.get('model'),
                    'degraded':result.get('degraded'), 'annotated_status_ids':sorted(cited)})
for post in posts.values():
    post['evidence_status'] = 'Grok-X-tool-citation; paraphrase-not-independently-verified' if post['tool_annotation_in'] else 'Grok-answer-only-candidate; no-matching-tool-annotation'
    post['status_id_derived_date_utc'] = datetime.fromtimestamp(((int(post['status_id']) >> 22)+1288834974657)/1000, timezone.utc).isoformat()
    post['date_limit'] = 'Date derived from status ID; does not establish existence, authorship or content.'
dump('catalog.json', {'collection_date':'2026-09-12', 'papers':papers, 'X_queries':queries,
     'X_posts':sorted(posts.values(), key=lambda x:x['status_id']),
     'counts':{'papers':len(papers),'X_search_responses':len(queries),'X_unique_candidate_status_ids':len(posts),
               'X_with_matching_tool_annotation':sum(bool(p['tool_annotation_in']) for p in posts.values())},
     'limits':['Finite exploratory sample; no prevalence/ranking or universal absence inference',
               'LLM review is an independent provider opinion, not independent empirical replication or human acceptance',
               'No canonical promotion, policy adoption or XBeach completion issued']})
print(json.dumps({'papers':len(papers),'X_unique_candidates':len(posts),
                   'X_tool_annotated':sum(bool(p['tool_annotation_in']) for p in posts.values())}))

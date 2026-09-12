"""User-requested Grok/X collection; public posts only, no canonical writes."""
import concurrent.futures
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'research/inbox/2026-09-12-wiki-purpose-review'
OUT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, '/home/firesinger/.hermes/hermes-agent')
from tools.x_search_tool import x_search_tool
logging.getLogger('tools.x_search_tool').setLevel(logging.CRITICAL)

COMMON = """
Research public X posts about building trustworthy, maintainable LLM-assisted
technical/scientific knowledge wikis. The decision is whether exhaustive reading
of all bundled documents/source code should be a prerequisite to a useful wiki,
or whether scoped question/claim-based verification can work. Seek counterexamples,
not agreement. Use actual X search. Return only posts with exact canonical X
status URLs, author, publication date, a concise paraphrase, any linked original
repository/paper, and whether it is first-hand implementation, proposal, measured
evaluation, criticism, or promotion. Do not invent posts, quotes, measurements,
or imply search results represent all users. No verbatim quote over 20 words per
author. Distinguish author claims from verified facts and your inference.
Do not give popularity rankings. If no matching evidence exists, say so.
"""
QUERIES = [
    ('originals', COMMON + """
Find up to 6 original posts by Andrej Karpathy, Steph Ango/kepano and builders of
LLM wikis or scientific documentation about source curation, ingest/query/lint,
human review, and use-driven growth. Check Karpathy status 2039805659525644595
and follow-up 2040470801506541998 if accessible. Include disagreements and
distinguish exhaustive processing of a selected source from all possible sources.
"""),
    ('failures', COMMON + """
Find up to 7 first-hand reports or critical discussions of LLM wiki failure:
hallucinated synthesis spreading across pages, provenance loss, costly endless
maintenance/audit loops, stale knowledge, overgrown graphs, weak retrieval, or
metrics gamed by easy questions. Prefer concrete incidents or reproducible repos
over product launch posts. Seek arguments FOR deeper systematic source review too.
"""),
    ('evaluation', COMMON + """
Find up to 6 posts linking papers or reproducible evaluations comparing curated
Markdown wikis, RAG/GraphRAG/long-context, source grounding/citation support, and
maintenance cost. Include negative/null results. Report exact paper/repo URLs,
evaluation question and limitations; treat unverified scores as author claims.
Scientific/engineering documentation examples are especially useful.
"""),
]

def collect(item):
    label, query = item
    result = json.loads(x_search_tool(query=query, from_date='2026-01-01', to_date='2026-09-12'))
    result['collected_at_utc'] = datetime.now(timezone.utc).isoformat()
    result['requested_date_range'] = ['2026-01-01', '2026-09-12']
    result['collection_status'] = 'exploratory-public-X-sample-not-independent-verification'
    (OUT / ('grok-' + label + '.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return {'query': label, 'success': result.get('success'), 'model': result.get('model'),
            'degraded': result.get('degraded'), 'citations': len(result.get('citations', [])),
            'inline_citations': len(result.get('inline_citations', [])),
            'error': result.get('error')}

if __name__ == '__main__':
    if sys.argv[1:] == ['--verify']:
        QUERIES = [('verification', COMMON + """
Verify only these three candidate X posts, using the X index and per-post tool
citations: https://x.com/karpathy/status/2041162213160091996 ,
https://x.com/thenightshipper/status/2089638769653883208 ,
https://x.com/mohitmor_ai/status/2043363748174508364 .
For each, state whether the exact post was actually retrieved, give its date and
an evidence-faithful paraphrase. Specifically test whether Karpathy says the wiki
approach skips writing but does not skip reading/thinking; whether Kothari discusses
loss of raw-source provenance; whether Mor discusses token cost of upkeep.
Do not reuse previous summaries as evidence. Do not cite unrelated posts to support
these. No population-level claims or policy recommendation. If inaccessible, mark
that candidate unverified. Every retrieved item must have its own X tool citation.
""")]
    else:
        assert not sys.argv[1:], 'Only --verify is supported'
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for result in pool.map(collect, QUERIES):
            print(json.dumps(result, ensure_ascii=False), flush=True)

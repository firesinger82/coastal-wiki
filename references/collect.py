#!/usr/bin/env python3
"""
coastal-literature-monitoring collection script
Queries arXiv for coastal engineering seed keywords and writes triage-compliant
markdown files to research/inbox/.
"""

import os
import re
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

import feedparser

SEEDS_FILE = Path("research/seeds/keywords.md")
INBOX_DIR = Path("research/inbox")
ARCHIVE_DIR = INBOX_DIR / "_archive"
MAX_RESULTS_PER_SEED = 5
ARXIV_API = "http://export.arxiv.org/api/query"

# --- off-domain relevance filter -------------------------------------------
# Broad seed terms (e.g. "wave", "overwash", "currents") semantically match
# arXiv papers far outside coastal engineering (astrophysics, condensed matter,
# medical imaging, ...). Filter results so the inbox stays domain-scoped.

# Core ocean/coastal physics categories → auto-accept regardless of keywords.
# Kept deliberately narrow: physics.geo-ph (admits seismology), comp-ph, and
# nlin.* are broad enough to leak non-coastal work, so they are keyword-gated
# below instead (a real coastal geo-ph/nonlinear-wave paper still passes on its
# sediment/ocean/wave keywords).
RELEVANT_CATEGORIES = {
    "physics.ao-ph", "physics.flu-dyn",
}
# Clearly off-domain primary fields → hard reject even if a keyword matches.
BLOCKED_CATEGORY_PREFIXES = (
    "astro-ph", "cond-mat", "hep-", "gr-qc", "quant-ph", "nucl-",
    "physics.med-ph", "physics.optics", "physics.atom-ph", "physics.chem-ph",
    "physics.bio-ph", "physics.plasm-ph", "physics.acc-ph", "physics.app-ph",
    "physics.ins-det", "physics.space-ph", "physics.atm-clus", "physics.hist-ph",
    "q-bio", "q-fin", "econ",
)
# Coastal-domain keywords required for dual-use categories (cs.*, eess.*, stat.*,
# math.NA, ...). "wave" appears only in compounds to avoid acoustic/gravitational/
# spin-wave false positives.
DOMAIN_KEYWORDS = (
    "coast", "ocean", "tide", "tidal", "surge", "beach", "nearshore", "estuar",
    "shore", "littoral", "swash", "breakwater", "bathymet", "morphodynam",
    "geomorph", "bed morpholog",
    "sediment", "storm surge", "hurricane", "typhoon", "tsunami", "harbor",
    "harbour", "marine", "sea level", "sea-level", "ice floe", "marginal ice",
    "overtop", "overwash", "run-up", "runup", "wave-current", "wind-wave",
    "wind wave", "ocean wave", "water wave", "surface wave", "wave height",
    "wave model", "storm wave", "infragravity", "rip current", "surf zone",
    "wave transmission", "wave attenuation", "floe", "berm", "inundation",
    "dune", "flood", "delft3d", "adcirc", "swan", "xbeach", "roms", "schism",
)


def is_relevant(paper: dict) -> bool:
    """Drop off-domain arXiv noise from broad seed semantic matches."""
    primary = paper.get("primary_category", "")
    if primary.startswith(BLOCKED_CATEGORY_PREFIXES):
        return False
    if set(paper.get("categories", [])) & RELEVANT_CATEGORIES:
        return True
    text = (paper["title"] + " " + paper["abstract"]).lower()
    return any(kw in text for kw in DOMAIN_KEYWORDS)


def load_seeds(path: Path) -> list[str]:
    """Extract seed keywords from the keywords.md file."""
    if not path.exists():
        return []
    content = path.read_text(encoding="utf-8")
    seeds = []
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("- "):
            seed = line[2:].strip()
            if seed and not seed.startswith("#"):
                seeds.append(seed)
    return seeds


def query_arxiv(seed: str, max_results: int = MAX_RESULTS_PER_SEED) -> list[dict]:
    """Query arXiv API for a given seed keyword."""
    query = f'all:"{seed}"'
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    feed = feedparser.parse(url)
    papers = []
    for entry in feed.entries:
        arxiv_id = entry.id.split("/")[-1]
        title = entry.title.replace("\n", " ").strip()
        abstract = entry.summary.replace("\n", " ").strip()
        published = entry.published if hasattr(entry, "published") else ""
        authors = [a.name for a in entry.authors] if hasattr(entry, "authors") else []
        link = entry.link
        doi = None
        for link_tag in getattr(entry, "links", []):
            if getattr(link_tag, "title", "") == "doi":
                doi = link_tag.href.replace("http://dx.doi.org/", "")
                break
        categories = [t.get("term") for t in getattr(entry, "tags", []) if t.get("term")]
        primary = getattr(entry, "arxiv_primary_category", None)
        if isinstance(primary, dict) and primary.get("term"):
            primary_category = primary["term"]
        else:
            primary_category = categories[0] if categories else ""
        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "abstract": abstract,
            "published": published,
            "authors": authors,
            "link": link,
            "doi": doi,
            "seed": seed,
            "categories": categories,
            "primary_category": primary_category,
        })
    return papers


def make_filename(title: str, arxiv_id: str) -> str:
    """Generate a safe filename for the inbox item."""
    safe = re.sub(r"[^a-zA-Z0-9\-_]", "-", title.lower())[:60].strip("-")
    return f"{safe}-{arxiv_id}.md"


def already_collected(filename: str) -> bool:
    """True if this paper was already collected — present in the active inbox or
    anywhere under inbox/_archive (including YYYY/ subdirs). Prevents the cron
    from re-acquiring papers that were previously triaged/archived/promoted."""
    if (INBOX_DIR / filename).exists():
        return True
    if ARCHIVE_DIR.exists():
        for existing in ARCHIVE_DIR.rglob(filename):
            if existing.is_file():
                return True
    return False


def scihub_url(doi: str | None, arxiv_id: str) -> str:
    """Generate Sci-Hub suggestion URL."""
    if doi:
        return f"https://sci-hub.se/{doi}"
    return f"https://sci-hub.se/{arxiv_id}"


def write_inbox_item(paper: dict) -> Path | None:
    """Write a triage-compliant markdown file to research/inbox/."""
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    filename = make_filename(paper["title"], paper["arxiv_id"])
    filepath = INBOX_DIR / filename

    if already_collected(filename):
        return None  # already in inbox or archived/promoted previously

    authors_str = ", ".join(paper["authors"]) if paper["authors"] else "Unknown"
    published = paper["published"][:10] if paper["published"] else "unknown"
    doi_line = f"doi: {paper['doi']}" if paper["doi"] else ""
    scihub = scihub_url(paper["doi"], paper["arxiv_id"])

    frontmatter = f"""---
title: "{paper['title']}"
source: arxiv
arxiv_id: {paper['arxiv_id']}
seed: {paper['seed']}
authors: {authors_str}
published: {published}
{doi_line}
link: {paper['link']}
arxiv_categories: {", ".join(paper.get('categories', [])) or paper.get('primary_category', '')}
citation_status: draft-unsourced
action: archive
collected: {datetime.now(timezone.utc).isoformat()}
---

"""

    body = f"""## Abstract

{paper['abstract']}

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: {scihub}

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
"""

    filepath.write_text(frontmatter + body, encoding="utf-8")
    return filepath


def main():
    seeds = load_seeds(SEEDS_FILE)
    if not seeds:
        print("No seeds found. Exiting.")
        return

    print(f"Loaded {len(seeds)} seeds from {SEEDS_FILE}")
    new_items = []
    skipped_offdomain = 0

    for seed in seeds:
        print(f"Querying arXiv for: {seed}")
        try:
            papers = query_arxiv(seed)
        except Exception as e:
            print(f"  Error querying {seed}: {e}")
            continue

        for paper in papers:
            if not is_relevant(paper):
                skipped_offdomain += 1
                print(f"  - off-domain ({paper['primary_category']}): {paper['arxiv_id']}")
                continue
            written = write_inbox_item(paper)
            if written:
                new_items.append(written)
                print(f"  + {written.name}")
            else:
                print(f"  = duplicate: {paper['arxiv_id']}")

    print(
        f"\nCollection complete. New items written: {len(new_items)} "
        f"(off-domain skipped: {skipped_offdomain})"
    )


if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)  # run from coastal-wiki root
    main()

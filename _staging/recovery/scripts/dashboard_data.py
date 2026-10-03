# Build dashboard data from reading records and fact tables (no hand-entered numbers).
# Run from repo root: python3 _staging/recovery/scripts/dashboard_data.py > _staging/recovery/dashboard-data.json
import csv, glob, hashlib, json, os, re, subprocess, collections

ROOT = '_staging/recovery'
CATS = ['자체코드', '매뉴얼·문서', '외부라이브러리', '테스트·예제', '부속도구·스크립트', '빌드·설정·기타', '바이너리']
READ = ['LLM판독', '부분판독', '결함감사만', '실패', '기록없음']

def models():
    out = []
    for f in sorted(glob.glob(f'{ROOT}/*-files.tsv')):
        m = os.path.basename(f)[:-len('-files.tsv')]
        rows = list(csv.DictReader(open(f), delimiter='\t'))
        by = collections.defaultdict(collections.Counter)
        for r in rows:
            by[r.get('category') or '미분류'][r['read']] += 1
        out.append({'model': m, 'raw': len(rows),
                    'cats': {c: dict(by[c]) for c in CATS if by[c]}})
    return out

def lines_of(path):
    d = open(path, 'rb').read()
    return d.count(b'\n') + (1 if d and not d.endswith(b'\n') else 0)

def code_records():
    recs = []
    for r in sorted(glob.glob(f'{ROOT}/read/XBeach/trunk/src/**/*.md', recursive=True)):
        t = open(r).read()
        src = re.search(r'^file: (.+)$', t, re.M).group(1).strip()
        n = lines_of(src)
        rngs = [(int(a), int(b)) for a, b in re.findall(r'^\|\s*(\d+)\s*[–-]\s*(\d+)\s*\|', t, re.M)]
        cont = n == 0 or (rngs and rngs[0][0] == 1 and rngs[-1][1] == n and
                          all(rngs[i + 1][0] == rngs[i][1] + 1 for i in range(len(rngs) - 1)))
        sha = hashlib.sha256(open(src, 'rb').read()).hexdigest() in t
        recs.append({'file': src.split('source_code/')[-1], 'lines': n, 'ranges': len(rngs),
                     'covered': bool(cont), 'sha': sha,
                     'quotes': len(re.findall(r'`[^`\n]{6,}`\s*\(\d+', t)) + len(re.findall(r'\(\d+\)\s*`[^`\n]{6,}`', t)),
                     'fixes': len(re.findall(r'검증 (정정|보완)', t)),
                     'facts': len(re.findall(r'^- ', t.split('## 판독 중')[-1], re.M)) if '## 판독 중' in t else 0})
    return recs

def text_doc_records():
    recs = []
    for r in sorted(glob.glob(f'{ROOT}/read/XBeach/**/*.md', recursive=True)):
        if '/trunk/src/' in r or '.pdf/' in r or 'office-compare' in r:
            continue
        t = open(r).read()
        m = re.search(r'^file: (.+)$', t, re.M)
        if not m:
            continue
        src = m.group(1).strip()
        recs.append({'file': src.split('/raw/')[-1].split('/XBeach/')[-1], 'lines': lines_of(src),
                     'ranges': len(re.findall(r'^\|\s*\d+\s*[–-]\s*\d+\s*\|', t, re.M)),
                     'fixes': len(re.findall(r'검증 (정정|보완)', t))})
    return recs

def pdf_pages():
    docs = collections.OrderedDict()
    for r in sorted(glob.glob(f'{ROOT}/read/XBeach/**/p[0-9][0-9][0-9]-[0-9][0-9][0-9].md', recursive=True)):
        t = open(r).read()
        name = os.path.basename(os.path.dirname(r))[:-4]
        total = int(re.search(r'^pages_total: (\d+)', t, re.M).group(1))
        d = docs.setdefault(name, {'name': name, 'total': total, 'pages': {}})
        for m in re.finditer(r'^\|\s*p\.(\d+)[^|]*\|(.*)$', t, re.M):
            p, body = int(m.group(1)), m.group(2)
            if 'fable 재판독: 일치' in body:
                s = 'reread_ok'
            elif 'fable 재판독' in body:
                s = 'reread_fixed'
            elif re.search(r'fable 검증|검증 정정|Claude 정정', body):
                s = 'checked_fixed'
            else:
                s = 'first_pass'
            d['pages'][p] = {'s': s, 'eq': len(re.findall(r'\(식 [^)]+\)|\([A-C]\.\d+\)|\(\d\.\d+\)', body))}
    for d in docs.values():
        d['pages'] = [d['pages'].get(p, {'s': 'missing', 'eq': 0}) for p in range(1, d['total'] + 1)]
    return list(docs.values())

def git_head():
    return subprocess.run(['git', 'log', '-1', '--format=%h %cs'], capture_output=True, text=True).stdout.strip()

print(json.dumps({'generated_from': git_head(), 'models': models(), 'code': code_records(),
                  'textdocs': text_doc_records(), 'pdfs': pdf_pages()}, ensure_ascii=False))

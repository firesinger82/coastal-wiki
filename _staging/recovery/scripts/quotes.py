# one-off: every `code` (N) quote in records must appear (whitespace-insensitive) on source line N (or N..N+3 for continuations)
import re,sys,glob,os
os.chdir('/home/firesinger/coastal-wiki')
recs=sys.argv[1:] or sorted(glob.glob('_staging/recovery/read/XBeach/**/*.md',recursive=True))
T=B=0; IMG=[0]
for r in recs:
    t=open(r).read()
    src=re.search(r'^file: (.+)$',t,re.M).group(1).strip()
    L=open(src,'rb').read().decode('utf-8','replace').replace('\r','').split('\n')
    norm=lambda s: re.sub(r'\s+|&','',re.sub(r'\\([_*|#\[\]()<>`.!-])',r'\1',s)).lower()  # 10-10: Markdown escapes (\_ etc.) ignored
    nl=[norm(x) for x in L]
    # 2026-10-08: union of both pairings (a quote is OK if either pairing matches);
    # reader-written paths (attachments/..., models/...) are not source text and are skipped.
    skip=lambda s: s.startswith(('attachments/','models/','_staging/','/home/'))
    # pair backticks left-to-right over ALL spans (any length) so short spans cannot shift pairing
    spans=[(m.start(),m.end(),m.group(1)) for m in re.finditer(r'`([^`\n]*)`',t)]
    allq={}
    for s,e,raw in spans:
        if len(raw)<6 or skip(raw.strip()): continue
        q=norm(raw)
        if not q: continue
        cands=[]
        m=re.match(r'\s*\((\d+)(?:[–-](\d+))?\)',t[e:e+20])
        if m: cands.append((int(m.group(1)),int(m.group(2) or m.group(1))))
        m=re.search(r'\((\d+)(?:[–-](\d+))?\)\s*$',t[max(0,s-20):s])
        if m: cands.append((int(m.group(1)),int(m.group(2) or m.group(1))))
        cands=[(a,b) for a,b in cands if 1<=a<=len(L)]
        if not cands: continue
        parts=[p for p in re.split(r'…|\.\.\.',q) if p]
        if all('![' in ''.join(L[a-1:b]) for a,b in cands):
            IMG[0]+=1; continue  # cited line is an image: value read from the picture, not checkable against text
        allq[(s,raw)]=any(all(p in ''.join(nl[a-1:min(len(L),max(b,a)+3)]) for p in parts) for a,b in cands)
    tot=len(allq); badl=[(k[1][:60]) for k,ok in allq.items() if not ok]; bad=len(badl); ex=badl
    T+=tot; B+=bad
    if bad: print('QUOTE-MISMATCH',src.split('source_code/')[-1],f'{bad}/{tot}',ex[:3])
print('records',len(recs),'quotes',T,'mismatch',B,'image-derived(skipped)',IMG[0])

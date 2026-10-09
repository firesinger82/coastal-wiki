# one-off: PDF page records — every page row present once; `quote` (p.N) found in extracted text of page N
import re,sys,glob,os,hashlib,json
os.chdir('/home/firesinger/coastal-wiki')
# usage: pdfcheck.py [--jobs FILE] [N ...]   (default jobs = XBeach pdfjobs.json)
args=sys.argv[1:]
JF='_staging/recovery/scripts/pdfjobs.json'
if args[:1]==['--jobs']: JF=args[1]; args=args[2:]
jobs=json.load(open(JF))
sel=[jobs[int(x)-1] for x in args] or jobs
vok=set(tuple(l.rstrip('\n').split('\t')) for l in open('_staging/recovery/scripts/visual-ok.txt') if l.strip())
norm=lambda s: re.sub(r'[^a-z0-9]','',s.lower().replace('ﬁ','fi').replace('ﬂ','fl'))
for j in sel:
    if not os.path.exists(j['out']): print('NO RECORD',j['out']); continue
    t=open(j['out']).read()
    errs=[]
    sha=hashlib.sha256(open(j['path'],'rb').read()).hexdigest()
    if sha not in t: errs.append('sha missing/mismatch')
    rows=[int(x) for x in re.findall(r'^\|\s*p\.(\d+)[^|]*\|',t,re.M)]
    want=list(range(j['a'],j['b']+1))
    if sorted(rows)!=want: errs.append(f'rows {len(rows)} != pages {len(want)}; missing {sorted(set(want)-set(rows))[:8]} dup {[x for x in set(rows) if rows.count(x)>1][:5]}')
    q=tot=0; bad=[]
    if j['ext']:
        ext=open(f"_staging/recovery/extract/{j.get('model','XBeach')}/pdf/{j['ext']}.txt",errors='replace').read()
        ext2=open(f"_staging/recovery/extract/{j.get('model','XBeach')}/pdf-md/{j['ext']}.md",errors='replace').read()
        ext2=re.sub(r'!\[[^\]]*\]\([^)]*\)','',ext2)  # 10-10: image links are not page text (scanned PDFs)
        pages={int(m.group(1)):'' for m in re.finditer(r'<<<PAGE (\d+)>>>',ext)}
        parts=re.split(r'<<<PAGE (\d+)>>>',ext)
        for k in range(1,len(parts),2): pages[int(parts[k])]=norm(parts[k+1])
        parts2=re.split(r'<<<PAGE (\d+)>>>',ext2)
        for k in range(1,len(parts2),2): pages[int(parts2[k])]=pages.get(int(parts2[k]),'')+'|'+norm(parts2[k+1])
        nopq=[]
        for p in want:
            row=re.search(rf'^\|\s*p\.{p}(?!\d)[^|]*\|(.*)$',t,re.M)
            qs=re.findall(r'`([^`]{20,})`\s*\(p\.(\d+)\)',row.group(1)) if row else []
            if not qs and len(pages.get(p,''))>200: nopq.append(p)
            thin=[x for x in want if len(pages.get(x,''))<120]
            for s,pn in qs:
                if len(pages.get(int(pn),'').strip())<120: continue  # extraction empty: quote unverifiable
                tot+=1
                if (j['ext'],pn,s[:50]) in vok: continue
                if norm(s) not in pages.get(int(pn),'') and norm(s) not in pages.get(int(pn)+1,'')+pages.get(int(pn)-1,''): bad.append((pn,s[:50]))
        if nopq: errs.append(f'text pages without quote: {nopq[:10]}')
        if bad: errs.append(f'quote mismatch {len(bad)}/{tot}: {bad[:3]}')
    print(('OK  ' if not errs else 'FAIL'), j['out'].split('XBeach/')[-1], f'pages {len(rows)}', f'quotes {tot}', errs)

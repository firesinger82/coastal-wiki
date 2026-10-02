# one-off: every `code` (N) quote in records must appear (whitespace-insensitive) on source line N (or N..N+3 for continuations)
import re,sys,glob,os
os.chdir('/home/firesinger/coastal-wiki')
recs=sys.argv[1:] or sorted(glob.glob('_staging/recovery/read/XBeach/**/*.md',recursive=True))
T=B=0
for r in recs:
    t=open(r).read()
    src=re.search(r'^file: (.+)$',t,re.M).group(1).strip()
    L=open(src,'rb').read().decode('utf-8','replace').replace('\r','').split('\n')
    norm=lambda s: re.sub(r'\s+|&','',s.replace('\\|','|')).lower()
    nl=[norm(x) for x in L]
    def run(pat,qi,ni,mi):
        tot=bad=0; ex=[]
        for m in re.finditer(pat,t):
            q=norm(m.group(qi)); a=int(m.group(ni)); b=int(m.group(mi) or a)
            if not q or a<1 or a>len(L): continue
            tot+=1
            win=''.join(nl[a-1:min(len(L),max(b,a)+3)])
            parts=[p for p in re.split(r'…|\.\.\.',q) if p]
            if not all(p in win for p in parts): bad+=1; ex.append((a,m.group(qi)[:60]))
        return tot,bad,ex
    r1=run(r'`([^`\n]{6,})`\s*\((\d+)(?:[–-](\d+))?\)',1,2,3)
    r2=run(r'\((\d+)(?:[–-](\d+))?\)\s*`([^`\n]{6,})`',3,1,2)
    tot,bad,ex=min([r1,r2],key=lambda x:(x[1]/max(x[0],1)))
    T+=tot; B+=bad
    if bad: print('QUOTE-MISMATCH',src.split('source_code/')[-1],f'{bad}/{tot}',ex[:3])
print('records',len(recs),'quotes',T,'mismatch',B)

# one-off (10-10, ADCIRC): in a report, every "`path:N` `text`" (or "`path:N`<br>`text`", "— `text`") must have
# `text` on line N..N+3 of that file. path = repo-relative (or unique basename under ROOT). Markdown escapes ignored.
import re,sys,os,glob
os.chdir('/home/firesinger/coastal-wiki')
rep=sys.argv[1]; root=sys.argv[2] if len(sys.argv)>2 else 'models'
idx={}
for p in glob.glob(root+'/**/*',recursive=True):
    if os.path.isfile(p): idx.setdefault(os.path.basename(p),[]).append(p)
cache={}
def lines(p):
    if p not in cache: cache[p]=open(p,'rb').read().decode('utf-8','replace').replace('\r','').split('\n')
    return cache[p]
norm=lambda s: re.sub(r'\s+','',re.sub(r'\\([_*|#\[\]()<>`.!-])',r'\1',re.sub(r'\\+\|','|',s.replace('&lt;','<').replace('&gt;','>').replace('&amp;','&')))).lower()
t=open(rep).read(); ok=bad=amb=0; out=[]
BASES=['','models/ADCIRC/raw/source_code/adcirc/','models/ADCIRC/raw/']  # bare paths like src/wetdry.F:126
pat=r'(?:`([^`\s]+?\.[A-Za-z0-9]+):(\d+)(?:[–-](\d+))?`|(?<![`\w/.\[])((?:src|prep|wind|util|docs|manuals)/[^`\s:]+?\.[A-Za-z0-9]+):(\d+)(?:[–-](\d+))?|\[([^\]\s`]+?\.[A-Za-z0-9]+):(\d+)(?:[–-](\d+))?\]\([^)\s]*\))(?:\s|<br>|—|:)*`([^`\n]+)`'
for m in re.finditer(pat,t):
    if re.search(r'`\s*—\s*$',t[max(0,m.start()-4):m.start()]): continue  # reverse form handled below
    g=m.groups(); path=g[0] or g[3] or g[6]; a=int(g[1] or g[4] or g[7]); b=int(g[2] or g[5] or g[8] or a); code=g[9]
    if re.fullmatch(r"[^`\s]+\.[A-Za-z0-9]+(:\d+)?",code.strip()) and "/" in code: continue  # next token is a path, not a quote
    p=next((B+path for B in BASES if os.path.isfile(B+path)),None)
    if not p:
        ps=idx.get(os.path.basename(path),[])
        if len(ps)!=1: amb+=1; continue
        p=ps[0]
    L=lines(p)
    seg=norm(''.join(L[a-1:max(a,b)+3]))
    parts=[x for x in re.split(r'…|\.\.\.',norm(code)) if x]
    if parts and all(x in seg for x in parts): ok+=1
    else: bad+=1; out.append(f'{path}:{a} `{code[:80]}`')
# reverse form: `name` — path:N
for m in re.finditer(r'`([^`\n]+)`\s*—\s*((?:src|prep|wind|util|docs)/[^`\s:]+?\.[A-Za-z0-9]+):(\d+)',t):
    code,path,a=m.group(1),m.group(2),int(m.group(3))
    p=next((B+path for B in BASES if os.path.isfile(B+path)),None)
    if not p: amb+=1; continue
    if norm(code) in norm(''.join(lines(p)[a-1:a+3])): ok+=1
    else: bad+=1; out.append(f'{path}:{a} `{code[:80]}` (reverse)')
print(f'{os.path.basename(rep)}: ok {ok} mismatch {bad} unresolved {amb}')
for o in out[:int(os.environ.get('SHOW','15'))]: print('  BAD',o)

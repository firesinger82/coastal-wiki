# one-off: in a report, every "`file.ext:N` `code`" pair must have `code` on line N (or N..N+3) of that file (searched under ROOT)
import re,sys,os,glob,html
rep,root=sys.argv[1],sys.argv[2]
idx={}
for p in glob.glob(root+'/**/*',recursive=True):
    if os.path.isfile(p): idx.setdefault(os.path.basename(p),[]).append(p)
norm=lambda s:re.sub(r'\s+','',s)
t=open(rep).read(); ok=bad=amb=0; out=[]
for m in re.finditer(r'`(?:[\w/.-]*/)?([\w.-]+\.(?:f90|F90|for|f|inc|rst|txt)):(\d+)`\s*`([^`]+)`',t):
    f,n,code=m.group(1),int(m.group(2)),m.group(3)
    ps=idx.get(f,[])
    if len(ps)!=1: amb+=1; continue
    L=open(ps[0],errors='replace').read().split('\n')
    seg=''.join(L[n-1:n+3]) if n<=len(L) else ''
    if norm(code) in norm(seg) or norm(code) in norm(L[n-1] if n<=len(L) else ''): ok+=1
    else: bad+=1; out.append(f'{f}:{n} `{code[:70]}`')
for m in re.finditer(r'`(?:[\w/.+-]*/)?([\w.+-]+\.(?:f90|F90|for|f|inc|rst|txt|md)):(\d+)`\s*—\s*`([^`]+)`',t):
    f,n,code=m.group(1),int(m.group(2)),m.group(3)
    ps=idx.get(f,[])
    if len(ps)!=1: amb+=1; continue
    L=open(ps[0],errors='replace').read().split('\n')
    seg=''.join(L[n-1:n+3]) if n<=len(L) else ''
    if norm(code) in norm(seg): ok+=1
    else: bad+=1; out.append(f'{f}:{n} `{code[:70]}`')
for m in re.finditer(r'\[(?:[\w/.-]*/)?([\w.-]+\.(?:f90|F90|inc|rst|txt)):(\d+)\]\([^)]*\)\s*—\s*<code>(.*?)</code>',t):
    f,n,code=m.group(1),int(m.group(2)),html.unescape(m.group(3)).replace('<br>','')
    ps=idx.get(f,[])
    if len(ps)!=1: amb+=1; continue
    L=open(ps[0],errors='replace').read().split('\n')
    seg=''.join(L[n-1:n+3]) if n<=len(L) else ''
    if norm(code) in norm(seg): ok+=1
    else: bad+=1; out.append(f'{f}:{n} `{code[:70]}`')
for m in re.finditer(r'\[[^\]]*?([\w.+-]+\.(?:f90|F90|for|f|inc)):(\d+)\]\([^)]*\)\s*`([^`]+)`',t):
    f,n,code=m.group(1),int(m.group(2)),m.group(3)
    ps=idx.get(f,[])
    if len(ps)!=1: amb+=1; continue
    L=open(ps[0],errors='replace').read().split('\n')
    seg=''.join(L[n-1:n+3]) if n<=len(L) else ''
    if norm(code) in norm(seg): ok+=1
    else: bad+=1; out.append(f'{f}:{n} `{code[:70]}`')
print('cited',ok+bad+amb,'ok',ok,'mismatch',bad,'unresolved',amb)
for o in out[:30]: print('  ',o)

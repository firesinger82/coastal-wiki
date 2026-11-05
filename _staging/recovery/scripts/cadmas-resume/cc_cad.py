# CADMAS: every `SIM/path:N[–M]` followed by `q1`(<br>`q2`)* -> each q must occur in lines N..M+3 (whitespace-insensitive).
import re,sys,os,glob,collections
os.chdir('/home/firesinger/coastal-wiki')
R='models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/'
SIM={'3D':'CADMAS-SURF-3D','3D2F':'CADMAS-SURF-3D2F','STR3D':'STR3D','AGENT':'AGENT'}
idx={k:collections.defaultdict(list) for k in SIM}
for k,v in SIM.items():
    for p in glob.glob(R+v+'/Source code/**/*',recursive=True):
        if os.path.isfile(p): idx[k][os.path.basename(p)].append(p)
cache={}
def lines(p):
    if p not in cache:
        b=open(p,'rb').read()
        for e in ('utf-8','cp932','latin-1'):
            try: s=b.decode(e); break
            except UnicodeDecodeError: pass
        cache[p]=s.replace('\r','').split('\n')
    return cache[p]
norm=lambda s: re.sub(r'\s+','',re.sub(r'\\([_*|#\[\]()<>`.!-])',r'\1',re.sub(r'\\+\|','|',s.replace('&lt;','<').replace('&gt;','>').replace('&amp;','&').replace('&#124;','|')))).lower()
def resolve(sim,path):
    p=R+SIM[sim]+'/Source code/'+path
    if os.path.isfile(p): return p
    ps=idx[sim].get(os.path.basename(path),[])
    return ps[0] if len(ps)==1 else None
tot=collections.Counter(); outs=[]
for rep in sys.argv[1:]:
    t=open(rep).read(); ok=bad=amb=0
    for m in re.finditer(r'`(?:05fdbedb:)?(3D2F|3D|STR3D|AGENT)/([^`\s:]+?\.[A-Za-z0-9]+):([\d–,-]+)`((?:\s*(?:<br>)?\s*`[^`\n]+`)+)',t):
        sim,path,spec,chain=m[1],m[2],m[3],m[4]
        rng=[]
        for x in spec.strip(',').split(','):
            if not x: continue
            u=re.split('[–-]',x); a=int(u[0]); b=int(u[-1] or a); rng.append((a,max(a,b)))
        p=resolve(sim,path)
        if not p: amb+=1; outs.append(f'AMB {rep}: {sim}/{path}'); continue
        segs=[norm(''.join(lines(p)[a-1:b+3])) for a,b in rng]
        for q in re.findall(r'`([^`\n]+)`',chain):
            if re.fullmatch(r'(3D2F|3D|STR3D|AGENT)/\S+:\S+',q): break
            nq=norm(q).strip(';,. ')
            if not nq: continue
            parts=[x for x in re.split(r'…|\.\.\.',norm(q)) if x]
            if all(any(x in s for s in segs) for x in parts): ok+=1
            else: bad+=1; outs.append(f'BAD {os.path.basename(rep)} {sim}/{path}:{spec} `{q[:90]}`')
    tot['ok']+=ok; tot['bad']+=bad; tot['amb']+=amb
    print(f'{os.path.basename(rep)}: ok {ok} mismatch {bad} unresolved {amb}')
print('TOTAL',dict(tot))
open(os.environ.get('OUT','/dev/null'),'w').write('\n'.join(outs)+'\n')

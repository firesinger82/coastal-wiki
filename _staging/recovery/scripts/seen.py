# one-off: check each non-blank source line appeared, as `nl -ba` formatted text, in the Codex session's tool outputs
import json,re,glob,os,sys
log=open(sys.argv[1]).read()
tid=re.search(r'Thread ready \(([0-9a-f-]+)\)',log).group(1)
sess=[p for p in glob.glob(os.path.expanduser('~/.codex/sessions/2026/*/*/*.jsonl')) if tid in p][0]
os.chdir('/home/firesinger/coastal-wiki')
texts=[]; trunc=0
for l in open(sess):
    r=json.loads(l); pl=r.get('payload',{})
    if pl.get('type') in('custom_tool_call_output','function_call_output'):
        o=pl.get('output'); items=[o] if isinstance(o,str) else [it.get('text','') for it in o if isinstance(it,dict)]
        for t in items:
            # unwrap nested JSON (possibly several levels) to plain text
            stack=[t]
            while stack:
                x=stack.pop()
                if isinstance(x,str):
                    try: y=json.loads(x)
                    except Exception: texts.append(x); continue
                    stack.append(y)
                elif isinstance(x,dict): stack.extend(x.values())
                elif isinstance(x,list): stack.extend(x)
blob='\n'.join(texts).replace('\r','')
trunc=blob.count('tokens truncated')
print('session',os.path.basename(sess)[:45],'truncation markers',trunc)
for k in sys.argv[2:]:
    lines=open(k,'rb').read().decode('utf-8','replace').replace('\r','').split('\n')
    if lines and lines[-1]=='': lines=lines[:-1]
    miss=[i+1 for i,s in enumerate(lines) if s.strip() and f"{i+1:6d}\t{s}" not in blob]
    nb=sum(1 for s in lines if s.strip())
    print(('OK  ' if not miss else 'MISS'),k.split('source_code/')[-1],len(lines),'nonblank',nb,'unseen',len(miss),miss[:6])

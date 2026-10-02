# one-off: verify read records cover 1..N contiguously, hash & line count match source
import re,sys,hashlib,os,glob
os.chdir('/home/firesinger/coastal-wiki')
recs=sys.argv[1:] or glob.glob('_staging/recovery/read/XBeach/**/*.md',recursive=True)
bad=0
for r in sorted(recs):
    t=open(r).read()
    fm=dict(re.findall(r'^(\w+): (.+)$',t.split('---')[1],re.M)) if t.startswith('---') else {}
    src=fm.get('file','').strip()
    if not os.path.exists(src): print('FAIL',r,'source missing'); bad+=1; continue
    d=open(src,'rb').read()
    n=d.count(b'\n')+(1 if d and not d.endswith(b'\n') else 0)
    sha=hashlib.sha256(d).hexdigest()
    errs=[]
    if fm.get('sha256','').strip()!=sha: errs.append('sha mismatch')
    if int(fm.get('lines','-1'))!=n: errs.append(f"lines {fm.get('lines')} != {n}")
    rs=[(int(a),int(b)) for a,b in re.findall(r'^\|\s*(\d+)\s*[–-]\s*(\d+)\s*\|',t,re.M)]
    if n>0:
        exp=1
        for a,b in rs:
            if a!=exp: errs.append(f'gap/overlap {exp}->{a}'); 
            if b<a: errs.append(f'bad range {a}-{b}')
            exp=b+1
        if exp-1!=n: errs.append(f'ends at {exp-1} not {n}')
    if errs: bad+=1; print('FAIL',src.split('source_code/')[-1],errs[:4])
    else: print('OK  ',src.split('source_code/')[-1],n,'lines',len(rs),'ranges')
print('records',len(recs),'fail',bad)

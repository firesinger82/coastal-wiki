# usage: python3 dcheck.py MODEL BATCHFILE N CODEX_LOG   — doc/code batch check robust to spaces/'?' in paths
import json,sys,subprocess,os,re,random
M,BF,N,LOG=sys.argv[1],sys.argv[2],int(sys.argv[3]),sys.argv[4]
b=json.load(open(BF))[N-1]
src=[p if isinstance(p,str) else 'models/'+M+'/raw/source_code/'+p[1] for p in b]
rec=['_staging/recovery/read/'+M+'/'+s.split('/raw/')[1].removeprefix('source_code/')+'.md' for s in src]
miss=[r for r in rec if not os.path.exists(r)]
for r in miss: print('MISSING',r)
have=[r for r in rec if os.path.exists(r)]
sd='_staging/recovery/scripts/'
o=subprocess.run(['python3',sd+'check.py']+have,capture_output=True,text=True).stdout.splitlines()
print('\n'.join(l for l in o if not l.startswith('OK')))
o=subprocess.run(['python3',sd+'seen.py',LOG]+[s for s,r in zip(src,rec) if r in have],capture_output=True,text=True).stdout.splitlines()
print('\n'.join(l for l in o if not l.startswith('OK'))[:1500])
print(subprocess.run(['python3',sd+'quotes.py']+have,capture_output=True,text=True).stdout.splitlines()[-1])
random.seed(N)
c=[]
for r in have:
    t=open(r).read(); rs=[x for x in re.findall(r'^\|\s*(\d+)\s*[–-]\s*(\d+)\s*\|',t,re.M) if int(x[1])-int(x[0])>=12]
    if rs: c.append((r.split('/read/')[1][:-3],'–'.join(random.choice(rs))))
random.shuffle(c)
for x in c[:3]: print('sample',*x)

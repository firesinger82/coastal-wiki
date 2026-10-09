#!/bin/bash
# usage: bcheck.sh MODEL BATCHFILE N LOGTAG — coverage/sha, every-line-seen, quotes, sample ranges
S=/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad
cd /home/firesinger/coastal-wiki
P=$(python3 -c "import json;print(' '.join(p for n,p in json.load(open('$2'))[$3-1]))")
F=""; R=""; for p in $P; do F="$F models/$1/raw/source_code/$p"; R="$R _staging/recovery/read/$1/$p.md"; done
for r in $R; do [ -f $r ] || echo "MISSING $r"; done
python3 _staging/recovery/scripts/check.py $R 2>&1 | grep -v "^OK"
python3 _staging/recovery/scripts/seen.py $S/$4.log $F | grep -v "^OK"
python3 _staging/recovery/scripts/quotes.py $R | tail -1
grep -l "분산" $R 2>/dev/null | sed 's/^/HAS-분산 /'
python3 - $R <<'PY'
import re,random,sys
random.seed(int(sum(map(ord,''.join(sys.argv[1:])))))
c=[]
for r in sys.argv[1:]:
    try: t=open(r).read()
    except: continue
    rs=[x for x in re.findall(r'^\|\s*(\d+)\s*[–-]\s*(\d+)\s*\|',t,re.M) if int(x[1])-int(x[0])>=15]
    if rs: c.append((r.split('/read/')[1][:-3], '–'.join(random.choice(rs))))
random.shuffle(c)
for x in c[:3]: print('sample',*x)
PY

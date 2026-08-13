#!/bin/bash
# 전수판독 진척 — 분모는 인벤토리 전수, 축소 없음
TR=~/coastal-wiki/_staging/total-read
total_code=$(cat $TR/shards/inv_code_*.txt 2>/dev/null | wc -l)
total_web=$(cat $TR/shards/inv_web_*.txt 2>/dev/null | wc -l)
rec=$(cat $TR/records/*.jsonl 2>/dev/null | python3 -c "
import sys,json
def norm(p):
    p = p.replace('/home/firesinger/coastal-wiki/','')
    return p[7:] if p.startswith('models/') else p
seen=set()
for l in sys.stdin:
    try:
        r=json.loads(l); seen.add((r.get('model',''), norm(r['path'])))
    except: pass
print(len(seen))")
echo "레코드(canonical model+정규화path): $rec / 분모 code $total_code + web $total_web + doc(PDF 260·기타별도)"
echo "축별 레코드 파일:"; ls $TR/records/ | sed 's/-[0-9a-z]*\.jsonl//' | sort | uniq -c

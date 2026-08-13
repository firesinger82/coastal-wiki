#!/usr/bin/env python3
"""바이너리 파일 기계 기록 + 텍스트 전용 샤드 생성. 판단 없음 — MIME/널바이트 검사만."""
import sys, os, json, hashlib, subprocess, datetime
TR = os.path.expanduser('~/coastal-wiki/_staging/total-read')
BASE = os.path.expanduser('~/coastal-wiki')

def is_text(path):
    try:
        with open(path,'rb') as f: chunk = f.read(8192)
        if b'\x00' in chunk: return False
        if not chunk: return True
        try: chunk.decode('utf-8'); return True
        except UnicodeDecodeError:
            try: chunk.decode('latin-1'); return True  # ISO-8859 소스(ShorelineS 전례)
            except Exception: return False
    except Exception: return False

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda: f.read(1<<20), b''): h.update(b)
    return h.hexdigest()

def main(inv_path, model, cwd_prefix):
    name = os.path.basename(inv_path).replace('inv_','').replace('.txt','')
    out_bin = f'{TR}/records/binauto-{name}.jsonl'
    done = set()
    # 기존 레코드 전체에서 이미 기록된 path 수집(재개)
    recdir=f'{TR}/records'
    for rf in os.listdir(recdir):
        if not rf.endswith('.jsonl'): continue
        for line in open(os.path.join(recdir,rf),encoding='utf-8',errors='replace'):
            try: done.add(json.loads(line)['path'])
            except Exception: pass
    txt_files=[]; nbin=0
    with open(out_bin,'a',encoding='utf-8') as ob:
        for rel in open(inv_path,encoding='utf-8'):
            rel=rel.strip()
            if not rel or rel in done: continue
            full=os.path.join(cwd_prefix, rel)
            if not os.path.isfile(full): continue
            if is_text(full):
                txt_files.append(rel); continue
            try:
                mime=subprocess.run(['file','-b','--mime-type',full],capture_output=True,text=True).stdout.strip()
            except Exception: mime='unknown'
            rec={"axis":inv_path.split('inv_')[1].split('_')[0],"model":model,"path":rel,
                 "sha256":sha256(full),"bytes":os.path.getsize(full),"lines_or_pages":0,
                 "read_status":"failed","fail_reason":f"binary ({mime})","read_range":"",
                 "reader":"mechanical-sweep","read_at":datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                 "content":{"what_it_is":f"binary file, MIME={mime}","entities":[],"constants":[],
                  "params_defined":[],"equations":[],"io":[],"calls":[],"verbatim_spans":[],"unresolved":[]}}
            ob.write(json.dumps(rec,ensure_ascii=False)+'\n'); nbin+=1
    # 텍스트 전용 샤드 재생성
    shard_dir=f'{TR}/shards'
    for old in os.listdir(shard_dir):
        if old.startswith(f'txt_{name}_'): os.remove(os.path.join(shard_dir,old))
    for i in range(0,len(txt_files),40):
        with open(f'{shard_dir}/txt_{name}_{i//40:03d}','w') as sf:
            sf.write('\n'.join(txt_files[i:i+40])+'\n')
    print(f'{name}: binary 자동기록 {nbin}, 잔여 텍스트 {len(txt_files)} → 샤드 {(len(txt_files)+39)//40}')

if __name__=='__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])

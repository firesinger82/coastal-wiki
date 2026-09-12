"""Extract and disassemble unique JVM class bytes; never run archive programs."""
import collections
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
OUT=HERE/'bytecode-read'


def digest(data):return hashlib.sha256(data).hexdigest()
def artifact(p):return {'path':str(p.relative_to(ROOT)),'sha256':digest(p.read_bytes())}


def main():
    inventory=HERE/'archive-content-inventory.json'
    original=json.loads(inventory.read_text())
    groups={}
    for archive in original['archives']:
        path=ROOT/'models/XBeach/raw/source_code'/archive['path']
        assert digest(path.read_bytes())==archive['sha256']
        with zipfile.ZipFile(path) as z:
            for member in archive['members']:
                if member['semantic_status']!='unread':continue
                data=z.read(member['path']);assert digest(data)==member['sha256'] and len(data)==member['bytes']
                item=groups.setdefault(member['sha256'],{'sha256':member['sha256'],'kind':member['kind'],'bytes':len(data),'instances':[],'data':data})
                item['instances'].append({'archive':str(path.relative_to(ROOT)),'member':member['path']})
    OUT.mkdir(exist_ok=True)
    (OUT/'classes').mkdir(exist_ok=True);(OUT/'disassembly').mkdir(exist_ok=True)
    version=subprocess.check_output(['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-version'],text=True).strip()
    def run(item):
        data=item.pop('data')
        if item['kind']!='java-bytecode':
            item['status']='unread-python-bytecode';return item
        cls=OUT/'classes'/(item['sha256']+'.class');cls.write_bytes(data)
        target=OUT/'disassembly'/(item['sha256']+'.txt')
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(cls)]
        result=subprocess.run(args,capture_output=True,text=True,check=True)
        if result.stderr:raise RuntimeError(result.stderr)
        # Exclude the invocation's local filename from generated evidence if present.
        output=result.stdout.replace(str(cls),str(cls.relative_to(ROOT)))
        target.write_text(output)
        item.update(status='disassembled-not-semantically-read',class_file=artifact(cls),disassembly=artifact(target),disassembly_lines=len(output.splitlines()))
        return item
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(run,groups.values()))
    receipt={'date':'2026-09-12','attribution':'AI mechanical extraction/disassembly; original class bytes separately identified',
             'inventory':artifact(inventory),'generator':artifact(Path(__file__)),
             'tool':{'command':'java -m jdk.jdeps/com.sun.tools.javap.Main -c -p -s -constants CLASS_FILE','version':version},
             'instance_count':sum(len(r['instances']) for r in records),'unique_count':len(records),
             'counts':dict(collections.Counter(r['status'] for r in records)),'records':records,
             'limitations':['Disassembly output is preparation for reading; no automatic semantic-read promotion.','Archive classes are not loaded as application entry points or executed.','Python bytecode remains unread.'],
             'whole_model_read_gate':'NOT_PASSED','human_approval_issued':False}
    (OUT/'disassembly-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'instances':receipt['instance_count'],'unique':receipt['unique_count'],'counts':receipt['counts'],'lines':sum(r.get('disassembly_lines',0) for r in records)}))

if __name__=='__main__':main()

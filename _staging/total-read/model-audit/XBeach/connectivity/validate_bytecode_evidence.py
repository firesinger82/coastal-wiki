"""Source/disassembly bindings only, not an independent semantic approval."""
import collections
import hashlib
import json
import subprocess
import zipfile


def validate(root,here):
    r=json.loads((here/'bytecode-read/disassembly-receipt.json').read_text())
    read=json.loads((here/'bytecode-read/launcher-read.json').read_text());checks=[]
    def check(n,v):checks.append({'check':'bytecode-'+n,'pass':bool(v)})
    def digest(b):return hashlib.sha256(b).hexdigest()
    def bound(a):return digest((root/a['path']).read_bytes())==a['sha256']
    check('inputs',bound(r['inventory']) and bound(r['generator']) and bound(read['prior_receipt']))
    inv=json.loads((root/r['inventory']['path']).read_text());expected={}
    for a in inv['archives']:
        path='models/XBeach/raw/source_code/'+a['path']
        with zipfile.ZipFile(root/path) as z:
            for m in a['members']:
                if m['semantic_status']=='unread':
                    raw=z.read(m['path']);expected[(path,m['path'])]=digest(raw)
    actual={(i['archive'],i['member']):x['sha256'] for x in r['records'] for i in x['instances']}
    check('exact-1284-instances',actual==expected and len(actual)==1284 and sum(len(x['instances']) for x in r['records'])==1284)
    check('unique-563',len(r['records'])==len({x['sha256'] for x in r['records']})==563 and collections.Counter(x['kind'] for x in r['records'])=={'java-bytecode':413,'python-bytecode':150})
    check('all-artifacts',all(bound(x['class_file']) and bound(x['disassembly']) and x['class_file']['sha256']==x['sha256'] and len((root/x['disassembly']['path']).read_text().splitlines())==x['disassembly_lines'] for x in r['records'] if x['kind']=='java-bytecode'))
    check('read-four-exact',len(read['records'])==4 and {x['instances'][0]['member'] for x in read['records']}=={'viewer/common/Dialogs.class','viewer/common/RuntimeExecCommand.class','viewer/launcher/Launcher.class','viewer/launcher/Launcher$InputStreamThread.class'})
    for x in read['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-reproduce-read',x['instances']==original['instances'] and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    io=json.loads((here/'bytecode-read/base-io-read.json').read_text())
    expected_io={x['sha256'] for x in r['records'] if x['instances'][0]['member'].startswith('base/io/')}
    check('io-exact-nine',bound(io['prior_receipt']) and len(io['records'])==io['unique_classes_read']==9 and {x['sha256'] for x in io['records']}==expected_io and io['instances_covered']==54)
    for x in io['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-io-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('io-no-approval',io['whole_model_read_gate']=='NOT_PASSED' and io['human_approval_issued'] is False)
    header=json.loads((here/'bytecode-read/slog2-header-read.json').read_text())
    names={'Header','FileBlockPtr','Const','CategoryMap','LineIDMapList','TreeDirValue','TreeDir'}
    check('slog2-header-exact-seven',bound(header['prior_receipt']) and len(header['records'])==header['unique_classes_read']==7 and {x['instances'][0]['member'] for x in header['records']}=={'logformat/slog2/'+n+'.class' for n in names} and header['instances_covered']==sum(len(x['instances']) for x in header['records']))
    for x in header['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-header-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('header-no-approval',header['whole_model_read_gate']=='NOT_PASSED' and header['human_approval_issued'] is False)
    check('no-approval',all(x['whole_model_read_gate']=='NOT_PASSED' and x['human_approval_issued'] is False for x in (r,read)))
    return checks

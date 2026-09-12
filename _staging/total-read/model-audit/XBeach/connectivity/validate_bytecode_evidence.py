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
    node=json.loads((here/'bytecode-read/slog2-node-read.json').read_text())
    expected_nodes={x['sha256'] for x in r['records'] if x['instances'][0]['member'].startswith('logformat/slog2/TreeNodeID')}
    check('node-five-exact',bound(node['prior_receipt']) and len(node['records'])==node['unique_classes_read']==5 and {x['sha256'] for x in node['records']}==expected_nodes and node['instances_covered']==30)
    for x in node['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-node-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('node-no-approval',node['whole_model_read_gate']=='NOT_PASSED' and node['human_approval_issued'] is False)
    iteration=json.loads((here/'bytecode-read/slog2-iteration-read.json').read_text())
    names={'TraceName','Permutation','IteratorOfAllDrawables','IteratorOfForeDrawables','IteratorOfBackDrawables','IteratorOfForePrimitives','IteratorOfBackPrimitives'}
    check('iteration-seven-exact',bound(iteration['prior_receipt']) and len(iteration['records'])==iteration['unique_classes_read']==7 and {x['instances'][0]['member'] for x in iteration['records']}=={'logformat/slog2/'+n+'.class' for n in names} and iteration['instances_covered']==sum(len(x['instances']) for x in iteration['records']))
    for x in iteration['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-iteration-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('iteration-no-approval',iteration['whole_model_read_gate']=='NOT_PASSED' and iteration['human_approval_issued'] is False)
    time_read=json.loads((here/'bytecode-read/time-coord-read.json').read_text())
    expected_time={x['sha256'] for x in r['records'] if x['instances'][0]['member'].startswith(('base/drawable/TimeBoundingBox','base/drawable/Coord'))}
    check('time-coord-eleven-exact',bound(time_read['prior_receipt']) and len(time_read['records'])==time_read['unique_classes_read']==11 and {x['sha256'] for x in time_read['records']}==expected_time and time_read['instances_covered']==sum(len(x['instances']) for x in time_read['records']))
    for x in time_read['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-time-coord-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('time-coord-no-approval',time_read['whole_model_read_gate']=='NOT_PASSED' and time_read['human_approval_issued'] is False)
    drawable=json.loads((here/'bytecode-read/drawable-order-read.json').read_text())
    names={'Drawable','Drawable$Order','Topology'}
    check('drawable-three-exact',bound(drawable['prior_receipt']) and len(drawable['records'])==drawable['unique_classes_read']==3 and {x['instances'][0]['member'] for x in drawable['records']}=={'base/drawable/'+n+'.class' for n in names} and drawable['instances_covered']==18)
    for x in drawable['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-drawable-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('drawable-no-approval',drawable['whole_model_read_gate']=='NOT_PASSED' and drawable['human_approval_issued'] is False)
    info=json.loads((here/'bytecode-read/infobox-read.json').read_text())
    check('infobox-exact',bound(info['prior_receipt']) and len(info['records'])==info['unique_classes_read']==1 and info['records'][0]['instances'][0]['member']=='base/drawable/InfoBox.class' and info['instances_covered']==6)
    for x in info['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('infobox-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('infobox-no-approval',info['whole_model_read_gate']=='NOT_PASSED' and info['human_approval_issued'] is False)
    values=json.loads((here/'bytecode-read/info-value-read.json').read_text())
    check('info-value-exact',bound(values['prior_receipt']) and len(values['records'])==values['unique_classes_read']==2 and {x['instances'][0]['member'] for x in values['records']}=={'base/drawable/InfoType.class','base/drawable/InfoValue.class'} and values['instances_covered']==12)
    for x in values['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-info-value-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('info-value-no-approval',values['whole_model_read_gate']=='NOT_PASSED' and values['human_approval_issued'] is False)
    nesting=json.loads((here/'bytecode-read/nesting-drawn-read.json').read_text())
    names={'NestingStacks','DrawnBox','DrawnBoxSet'}
    check('nesting-three-exact',bound(nesting['prior_receipt']) and len(nesting['records'])==nesting['unique_classes_read']==3 and {x['instances'][0]['member'] for x in nesting['records']}=={'base/drawable/'+n+'.class' for n in names} and nesting['instances_covered']==sum(len(x['instances']) for x in nesting['records']))
    for x in nesting['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-nesting-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('nesting-no-approval',nesting['whole_model_read_gate']=='NOT_PASSED' and nesting['human_approval_issued'] is False)
    check('no-approval',all(x['whole_model_read_gate']=='NOT_PASSED' and x['human_approval_issued'] is False for x in (r,read)))
    return checks

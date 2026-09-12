"""Source/disassembly bindings only, not an independent semantic approval."""
import collections
import importlib.util
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
    buffers=json.loads((here/'bytecode-read/drawable-buffer-read.json').read_text())
    names={'BufForObjects','BufForObjects$Order','BufForDrawables'}
    check('buffers-three-exact',bound(buffers['prior_receipt']) and len(buffers['records'])==buffers['unique_classes_read']==3 and {x['instances'][0]['member'] for x in buffers['records']}=={'logformat/slog2/'+n+'.class' for n in names} and buffers['instances_covered']==18)
    for x in buffers['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-buffer-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('buffers-no-approval',buffers['whole_model_read_gate']=='NOT_PASSED' and buffers['human_approval_issued'] is False)
    lineids=json.loads((here/'bytecode-read/lineid-method-read.json').read_text())
    check('lineids-two-exact',bound(lineids['prior_receipt']) and len(lineids['records'])==lineids['unique_classes_read']==2 and {x['instances'][0]['member'] for x in lineids['records']}=={'logformat/slog2/LineIDMap.class','base/drawable/Method.class'} and lineids['instances_covered']==12)
    for x in lineids['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-lineid-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('lineids-no-approval',lineids['whole_model_read_gate']=='NOT_PASSED' and lineids['human_approval_issued'] is False)
    ycoord=json.loads((here/'bytecode-read/ycoord-read.json').read_text())
    check('ycoord-exact',bound(ycoord['prior_receipt']) and len(ycoord['records'])==ycoord['unique_classes_read']==1 and ycoord['records'][0]['instances'][0]['member']=='base/drawable/YCoordMap.class' and ycoord['instances_covered']==6)
    for x in ycoord['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('ycoord-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('ycoord-no-approval',ycoord['whole_model_read_gate']=='NOT_PASSED' and ycoord['human_approval_issued'] is False)
    shadow_buffer=json.loads((here/'bytecode-read/shadow-buffer-read.json').read_text())
    check('shadow_buffer-exact',bound(shadow_buffer['prior_receipt']) and len(shadow_buffer['records'])==shadow_buffer['unique_classes_read']==1 and shadow_buffer['records'][0]['instances'][0]['member']=='logformat/slog2/BufForShadows.class' and shadow_buffer['instances_covered']==6)
    for x in shadow_buffer['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('shadow_buffer-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('shadow_buffer-no-approval',shadow_buffer['whole_model_read_gate']=='NOT_PASSED' and shadow_buffer['human_approval_issued'] is False)
    shadow=json.loads((here/'bytecode-read/shadow-read.json').read_text())
    check('shadow-exact',bound(shadow['prior_receipt']) and len(shadow['records'])==shadow['unique_classes_read']==1 and shadow['records'][0]['instances'][0]['member']=='base/drawable/Shadow.class' and shadow['instances_covered']==6)
    for x in shadow['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('shadow-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('shadow-no-approval',shadow['whole_model_read_gate']=='NOT_PASSED' and shadow['human_approval_issued'] is False)
    primitive=json.loads((here/'bytecode-read/primitive-read.json').read_text())
    check('primitive-exact',bound(primitive['prior_receipt']) and len(primitive['records'])==primitive['unique_classes_read']==1 and primitive['records'][0]['instances'][0]['member']=='base/drawable/Primitive.class' and primitive['instances_covered']==6)
    for x in primitive['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('primitive-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('primitive-no-approval',primitive['whole_model_read_gate']=='NOT_PASSED' and primitive['human_approval_issued'] is False)
    output_node=json.loads((here/'bytecode-read/output-node-read.json').read_text())
    check('output_node-exact',bound(output_node['prior_receipt']) and len(output_node['records'])==output_node['unique_classes_read']==1 and output_node['records'][0]['instances'][0]['member']=='logformat/slog2/output/TreeNode.class' and output_node['instances_covered']==4)
    for x in output_node['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('output_node-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('output_node-no-approval',output_node['whole_model_read_gate']=='NOT_PASSED' and output_node['human_approval_issued'] is False)
    clog2_converter=json.loads((here/'bytecode-read/clog2-converter-read.json').read_text())
    check('clog2_converter-exact',bound(clog2_converter['prior_receipt']) and len(clog2_converter['records'])==clog2_converter['unique_classes_read']==1 and clog2_converter['records'][0]['instances'][0]['member']=='logformat/slog2/output/Clog2ToSlog2.class' and clog2_converter['instances_covered']==4)
    for x in clog2_converter['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('clog2_converter-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2_converter-no-approval',clog2_converter['whole_model_read_gate']=='NOT_PASSED' and clog2_converter['human_approval_issued'] is False)
    clog_converter=json.loads((here/'bytecode-read/clog-converter-read.json').read_text())
    check('clog_converter-exact',bound(clog_converter['prior_receipt']) and len(clog_converter['records'])==clog_converter['unique_classes_read']==1 and clog_converter['records'][0]['instances'][0]['member']=='logformat/slog2/output/ClogToSlog2.class' and clog_converter['instances_covered']==4)
    for x in clog_converter['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('clog_converter-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog_converter-no-approval',clog_converter['whole_model_read_gate']=='NOT_PASSED' and clog_converter['human_approval_issued'] is False)
    trace_converter=json.loads((here/'bytecode-read/trace-converter-read.json').read_text())
    check('trace_converter-exact',bound(trace_converter['prior_receipt']) and len(trace_converter['records'])==trace_converter['unique_classes_read']==1 and trace_converter['records'][0]['instances'][0]['member']=='logformat/slog2/output/TraceToSlog2.class' and trace_converter['instances_covered']==4)
    for x in trace_converter['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check('trace_converter-reproduce',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('trace_converter-no-approval',trace_converter['whole_model_read_gate']=='NOT_PASSED' and trace_converter['human_approval_issued'] is False)
    weights=json.loads((here/'bytecode-read/category-weight-read.json').read_text())
    expected_weights={x['sha256'] for x in r['records'] if x['instances'][0]['member'].startswith(('base/drawable/CategoryWeight','base/drawable/CategoryRatios','base/drawable/CategorySummary'))}
    check('weights-ten-exact',bound(weights['prior_receipt']) and len(weights['records'])==weights['unique_classes_read']==10 and {x['sha256'] for x in weights['records']}==expected_weights and weights['instances_covered']==60)
    for x in weights['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-weights-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('weights-no-approval',weights['whole_model_read_gate']=='NOT_PASSED' and weights['human_approval_issued'] is False)
    composite=json.loads((here/'bytecode-read/composite-read.json').read_text())
    check('composite-two-exact',bound(composite['prior_receipt']) and len(composite['records'])==composite['unique_classes_read']==2 and {x['instances'][0]['member'] for x in composite['records']}=={'base/drawable/Composite.class','base/drawable/Composite$ItrOfPrimes.class'} and composite['instances_covered']==12)
    for x in composite['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-composite-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('composite-no-approval',composite['whole_model_read_gate']=='NOT_PASSED' and composite['human_approval_issued'] is False)
    output_flow=json.loads((here/'bytecode-read/output-flow-read.json').read_text())
    check('output_flow-two-exact',bound(output_flow['prior_receipt']) and len(output_flow['records'])==output_flow['unique_classes_read']==2 and {x['instances'][0]['member'] for x in output_flow['records']}=={'logformat/slog2/output/TreeTrunk.class','logformat/slog2/output/OutputLog.class'} and output_flow['instances_covered']==8)
    for x in output_flow['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-output_flow-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('output_flow-no-approval',output_flow['whole_model_read_gate']=='NOT_PASSED' and output_flow['human_approval_issued'] is False)
    kinds=json.loads((here/'bytecode-read/input-kind-read.json').read_text())
    check('input-kind-two-exact',bound(kinds['prior_receipt']) and len(kinds['records'])==kinds['unique_classes_read']==2 and {x['instances'][0]['member'] for x in kinds['records']}=={'base/drawable/InputAPI.class','base/drawable/Kind.class'} and kinds['instances_covered']==12)
    for x in kinds['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-input-kind-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('input-kind-no-approval',kinds['whole_model_read_gate']=='NOT_PASSED' and kinds['human_approval_issued'] is False)
    trace_input=json.loads((here/'bytecode-read/trace-input-read.json').read_text())
    check('trace-input-two-exact',bound(trace_input['prior_receipt']) and len(trace_input['records'])==trace_input['unique_classes_read']==2 and {x['instances'][0]['member'] for x in trace_input['records']}=={'logformat/trace/InputLog.class','logformat/trace/DobjDef.class'} and trace_input['instances_covered']==4)
    for x in trace_input['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-trace-input-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('trace-input-no-approval',trace_input['whole_model_read_gate']=='NOT_PASSED' and trace_input['human_approval_issued'] is False)
    clog2_shell=json.loads((here/'bytecode-read/clog2-input-shell-read.json').read_text())
    check('clog2-input-shell-two-exact',bound(clog2_shell['prior_receipt']) and len(clog2_shell['records'])==clog2_shell['unique_classes_read']==3 and {x['instances'][0]['member'] for x in clog2_shell['records']}=={'logformat/clog2TOdrawable/InputLog$TopologyIterator.class', 'logformat/clog2TOdrawable/InputLog$YCoordMapIterator.class', 'logformat/clog2TOdrawable/InputLog.class'} and clog2_shell['instances_covered']==6)
    for x in clog2_shell['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-input-shell-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-input-shell-no-approval',clog2_shell['whole_model_read_gate']=='NOT_PASSED' and clog2_shell['human_approval_issued'] is False)
    clog2_content=json.loads((here/'bytecode-read/clog2-content-read.json').read_text())
    check('clog2-content-one-exact',bound(clog2_content['prior_receipt']) and len(clog2_content['records'])==clog2_content['unique_classes_read']==1 and clog2_content['records'][0]['instances'][0]['member']=='logformat/clog2TOdrawable/InputLog$ContentIterator.class' and clog2_content['instances_covered']==2)
    for x in clog2_content['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-content-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-content-no-approval',clog2_content['whole_model_read_gate']=='NOT_PASSED' and clog2_content['human_approval_issued'] is False)
    clog2_matching=json.loads((here/'bytecode-read/clog2-matching-read.json').read_text())
    check('clog2-matching-seven-exact',bound(clog2_matching['prior_receipt']) and len(clog2_matching['records'])==clog2_matching['unique_classes_read']==7 and sorted(x['instances'][0]['member'] for x in clog2_matching['records'])==['logformat/clog2TOdrawable/NoMatchingEventException.class', 'logformat/clog2TOdrawable/ObjMethod.class', 'logformat/clog2TOdrawable/Obj_Arrow.class', 'logformat/clog2TOdrawable/Obj_State.class', 'logformat/clog2TOdrawable/Topo_Arrow.class', 'logformat/clog2TOdrawable/Topo_State.class', 'logformat/clog2TOdrawable/TwoEventsMatching.class'] and clog2_matching['instances_covered']==14)
    for x in clog2_matching['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-matching-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-matching-no-approval',clog2_matching['whole_model_read_gate']=='NOT_PASSED' and clog2_matching['human_approval_issued'] is False)
    clog2_idmap=json.loads((here/'bytecode-read/clog2-idmap-read.json').read_text())
    check('clog2-idmap-three-exact',bound(clog2_idmap['prior_receipt']) and len(clog2_idmap['records'])==clog2_idmap['unique_classes_read']==3 and sorted(x['instances'][0]['member'] for x in clog2_idmap['records'])==['logformat/clog2/LineID.class', 'logformat/clog2TOdrawable/CommProcThdID.class', 'logformat/clog2TOdrawable/CommProcThdIDMap.class'] and clog2_idmap['instances_covered']==6)
    for x in clog2_idmap['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-idmap-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-idmap-no-approval',clog2_idmap['whole_model_read_gate']=='NOT_PASSED' and clog2_idmap['human_approval_issued'] is False)
    clog2_records=json.loads((here/'bytecode-read/clog2-record-input-read.json').read_text())
    check('clog2-record-input-four-exact',bound(clog2_records['prior_receipt']) and len(clog2_records['records'])==clog2_records['unique_classes_read']==4 and sorted(x['instances'][0]['member'] for x in clog2_records['records'])==['logformat/clog2/RecBare.class', 'logformat/clog2/RecCargo.class', 'logformat/clog2/RecHeader.class', 'logformat/clog2/RecMsg.class'] and clog2_records['instances_covered']==8)
    for x in clog2_records['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-record-input-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-record-input-no-approval',clog2_records['whole_model_read_gate']=='NOT_PASSED' and clog2_records['human_approval_issued'] is False)
    clog2_stream=json.loads((here/'bytecode-read/clog2-stream-read.json').read_text())
    check('clog2-stream-three-exact',bound(clog2_stream['prior_receipt']) and len(clog2_stream['records'])==clog2_stream['unique_classes_read']==3 and sorted(x['instances'][0]['member'] for x in clog2_stream['records'])==['logformat/clog2/InputLog.class', 'logformat/clog2/MixedDataInputStream.class', 'logformat/clog2/Preamble.class'] and clog2_stream['instances_covered']==6)
    for x in clog2_stream['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-stream-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-stream-no-approval',clog2_stream['whole_model_read_gate']=='NOT_PASSED' and clog2_stream['human_approval_issued'] is False)
    clog2_comm=json.loads((here/'bytecode-read/clog2-comm-read.json').read_text())
    check('clog2-comm-three-exact',bound(clog2_comm['prior_receipt']) and len(clog2_comm['records'])==clog2_comm['unique_classes_read']==3 and sorted(x['instances'][0]['member'] for x in clog2_comm['records'])==['logformat/clog2/Const.class', 'logformat/clog2/RecComm.class', 'logformat/clog2/UUID.class'] and clog2_comm['instances_covered']==6)
    for x in clog2_comm['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-comm-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-comm-no-approval',clog2_comm['whole_model_read_gate']=='NOT_PASSED' and clog2_comm['human_approval_issued'] is False)
    clog2_skipped=json.loads((here/'bytecode-read/clog2-skipped-records-read.json').read_text())
    check('clog2-skipped-four-exact',bound(clog2_skipped['prior_receipt']) and len(clog2_skipped['records'])==clog2_skipped['unique_classes_read']==4 and sorted(x['instances'][0]['member'] for x in clog2_skipped['records'])==['logformat/clog2/RecColl.class', 'logformat/clog2/RecDefConst.class', 'logformat/clog2/RecSrc.class', 'logformat/clog2/RecTshift.class'] and clog2_skipped['instances_covered']==8)
    for x in clog2_skipped['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-skipped-records-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-skipped-records-no-approval',clog2_skipped['whole_model_read_gate']=='NOT_PASSED' and clog2_skipped['human_approval_issued'] is False)
    clog2_defs=json.loads((here/'bytecode-read/clog2-definitions-read.json').read_text())
    check('clog2-definitions-four-exact',bound(clog2_defs['prior_receipt']) and len(clog2_defs['records'])==clog2_defs['unique_classes_read']==4 and sorted(x['instances'][0]['member'] for x in clog2_defs['records'])==['logformat/clog2/RecDefEvent.class', 'logformat/clog2/RecDefMsg.class', 'logformat/clog2/RecDefState.class', 'logformat/clog2TOdrawable/ObjDef.class'] and clog2_defs['instances_covered']==8)
    for x in clog2_defs['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-definitions-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-definitions-no-approval',clog2_defs['whole_model_read_gate']=='NOT_PASSED' and clog2_defs['human_approval_issued'] is False)
    clog2_event_color=json.loads((here/'bytecode-read/clog2-event-color-read.json').read_text())
    check('clog2-event-color-three-exact',bound(clog2_event_color['prior_receipt']) and len(clog2_event_color['records'])==clog2_event_color['unique_classes_read']==3 and sorted(x['instances'][0]['member'] for x in clog2_event_color['records'])==['logformat/clog2TOdrawable/ColorNameMap.class', 'logformat/clog2TOdrawable/Obj_Event.class', 'logformat/clog2TOdrawable/Topo_Event.class'] and clog2_event_color['instances_covered']==6)
    for x in clog2_event_color['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-event-color-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2-event-color-no-approval',clog2_event_color['whole_model_read_gate']=='NOT_PASSED' and clog2_event_color['human_approval_issued'] is False)
    color_alpha=json.loads((here/'bytecode-read/color-alpha-read.json').read_text())
    check('color-alpha-one-exact',bound(color_alpha['prior_receipt']) and len(color_alpha['records'])==color_alpha['unique_classes_read']==1 and color_alpha['records'][0]['instances'][0]['member']=='base/drawable/ColorAlpha.class' and color_alpha['instances_covered']==6)
    for x in color_alpha['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-color-alpha-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('color-alpha-no-approval',color_alpha['whole_model_read_gate']=='NOT_PASSED' and color_alpha['human_approval_issued'] is False)
    category=json.loads((here/'bytecode-read/category-read.json').read_text())
    check('category-one-exact',bound(category['prior_receipt']) and len(category['records'])==category['unique_classes_read']==1 and category['records'][0]['instances'][0]['member']=='base/drawable/Category.class' and category['instances_covered']==6)
    for x in category['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-category-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('category-no-approval',category['whole_model_read_gate']=='NOT_PASSED' and category['human_approval_issued'] is False)
    clog2_print=json.loads((here/'bytecode-read/clog2-print-read.json').read_text())
    check('clog2_print-one-exact',bound(clog2_print['prior_receipt']) and len(clog2_print['records'])==clog2_print['unique_classes_read']==1 and clog2_print['records'][0]['instances'][0]['member']=='logformat/clog2TOdrawable/Print.class' and clog2_print['instances_covered']==2)
    for x in clog2_print['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-print-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2_print-no-approval',clog2_print['whole_model_read_gate']=='NOT_PASSED' and clog2_print['human_approval_issued'] is False)
    clog2_onepass=json.loads((here/'bytecode-read/clog2-print-onepass-read.json').read_text())
    check('clog2_onepass-one-exact',bound(clog2_onepass['prior_receipt']) and len(clog2_onepass['records'])==clog2_onepass['unique_classes_read']==1 and clog2_onepass['records'][0]['instances'][0]['member']=='logformat/clog2TOdrawable/Print_1pass.class' and clog2_onepass['instances_covered']==2)
    for x in clog2_onepass['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-print-onepass-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2_onepass-no-approval',clog2_onepass['whole_model_read_gate']=='NOT_PASSED' and clog2_onepass['human_approval_issued'] is False)
    clog2_twopass=json.loads((here/'bytecode-read/clog2-print-twopass-read.json').read_text())
    check('clog2_twopass-one-exact',bound(clog2_twopass['prior_receipt']) and len(clog2_twopass['records'])==clog2_twopass['unique_classes_read']==1 and clog2_twopass['records'][0]['instances'][0]['member']=='logformat/clog2TOdrawable/Print_2pass.class' and clog2_twopass['instances_covered']==2)
    for x in clog2_twopass['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-print-twopass-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2_twopass-no-approval',clog2_twopass['whole_model_read_gate']=='NOT_PASSED' and clog2_twopass['human_approval_issued'] is False)
    lowlevel_print=json.loads((here/'bytecode-read/lowlevel-print-read.json').read_text())
    check('lowlevel-print-two-exact',bound(lowlevel_print['prior_receipt']) and len(lowlevel_print['records'])==lowlevel_print['unique_classes_read']==2 and sorted(x['instances'][0]['member'] for x in lowlevel_print['records'])==['logformat/clog2/Print.class', 'logformat/trace/Print.class'] and lowlevel_print['instances_covered']==4)
    for x in lowlevel_print['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-lowlevel-print-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('lowlevel_print-no-approval',lowlevel_print['whole_model_read_gate']=='NOT_PASSED' and lowlevel_print['human_approval_issued'] is False)
    basic_topology=json.loads((here/'bytecode-read/basic-topology-read.json').read_text())
    check('basic-topology-three-exact',bound(basic_topology['prior_receipt']) and len(basic_topology['records'])==basic_topology['unique_classes_read']==3 and sorted(x['instances'][0]['member'] for x in basic_topology['records'])==['base/topology/Event.class', 'base/topology/Line.class', 'base/topology/State.class'] and basic_topology['instances_covered']==6)
    for x in basic_topology['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-basic-topology-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('basic_topology-no-approval',basic_topology['whole_model_read_gate']=='NOT_PASSED' and basic_topology['human_approval_issued'] is False)
    state_border=json.loads((here/'bytecode-read/state-border-read.json').read_text())
    check('state-border-eight-exact',bound(state_border['prior_receipt']) and len(state_border['records'])==state_border['unique_classes_read']==8 and sorted(x['instances'][0]['member'] for x in state_border['records'])==['base/topology/StateBorder$ColorLoweredBorder.class', 'base/topology/StateBorder$ColorRaisedBorder.class', 'base/topology/StateBorder$ColorXORBorder.class', 'base/topology/StateBorder$EmptyBorder.class', 'base/topology/StateBorder$WhiteLoweredBorder.class', 'base/topology/StateBorder$WhitePlainBorder.class', 'base/topology/StateBorder$WhiteRaisedBorder.class', 'base/topology/StateBorder.class'] and state_border['instances_covered']==16)
    for x in state_border['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-state-border-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('state_border-no-approval',state_border['whole_model_read_gate']=='NOT_PASSED' and state_border['human_approval_issued'] is False)
    preview_event=json.loads((here/'bytecode-read/preview-event-read.json').read_text())
    check('preview-event-one-exact',bound(preview_event['prior_receipt']) and len(preview_event['records'])==preview_event['unique_classes_read']==1 and preview_event['records'][0]['instances'][0]['member']=='base/topology/PreviewEvent.class' and preview_event['instances_covered']==2)
    for x in preview_event['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-preview-event-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('preview_event-no-approval',preview_event['whole_model_read_gate']=='NOT_PASSED' and preview_event['human_approval_issued'] is False)
    arrow_render=json.loads((here/'bytecode-read/arrow-render-read.json').read_text())
    check('arrow-render-one-exact',bound(arrow_render['prior_receipt']) and len(arrow_render['records'])==arrow_render['unique_classes_read']==1 and arrow_render['records'][0]['instances'][0]['member']=='base/topology/Arrow.class' and arrow_render['instances_covered']==2)
    for x in arrow_render['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-arrow-render-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('arrow_render-no-approval',arrow_render['whole_model_read_gate']=='NOT_PASSED' and arrow_render['human_approval_issued'] is False)
    summary_arrow=json.loads((here/'bytecode-read/summary-arrow-read.json').read_text())
    check('summary-arrow-one-exact',bound(summary_arrow['prior_receipt']) and len(summary_arrow['records'])==summary_arrow['unique_classes_read']==1 and summary_arrow['records'][0]['instances'][0]['member']=='base/topology/SummaryArrow.class' and summary_arrow['instances_covered']==2)
    for x in summary_arrow['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-summary-arrow-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('summary_arrow-no-approval',summary_arrow['whole_model_read_gate']=='NOT_PASSED' and summary_arrow['human_approval_issued'] is False)
    summary_state=json.loads((here/'bytecode-read/summary-state-read.json').read_text())
    check('summary-state-one-exact',bound(summary_state['prior_receipt']) and len(summary_state['records'])==summary_state['unique_classes_read']==1 and summary_state['records'][0]['instances'][0]['member']=='base/topology/SummaryState.class' and summary_state['instances_covered']==2)
    for x in summary_state['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-summary-state-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('summary_state-no-approval',summary_state['whole_model_read_gate']=='NOT_PASSED' and summary_state['human_approval_issued'] is False)
    category_timebox=json.loads((here/'bytecode-read/category-timebox-read.json').read_text())
    check('category-timebox-six-exact',bound(category_timebox['prior_receipt']) and len(category_timebox['records'])==category_timebox['unique_classes_read']==6 and sorted(x['instances'][0]['member'] for x in category_timebox['records'])==['base/statistics/CategoryTimeBox$1.class', 'base/statistics/CategoryTimeBox$CountOrder.class', 'base/statistics/CategoryTimeBox$ExclRatioOrder.class', 'base/statistics/CategoryTimeBox$InclRatioOrder.class', 'base/statistics/CategoryTimeBox$IndexOrder.class', 'base/statistics/CategoryTimeBox.class'] and category_timebox['instances_covered']==12)
    for x in category_timebox['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-category-timebox-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('category_timebox-no-approval',category_timebox['whole_model_read_gate']=='NOT_PASSED' and category_timebox['human_approval_issued'] is False)
    timeave_box=json.loads((here/'bytecode-read/timeave-box-read.json').read_text())
    check('timeave-box-one-exact',bound(timeave_box['prior_receipt']) and len(timeave_box['records'])==timeave_box['unique_classes_read']==1 and timeave_box['records'][0]['instances'][0]['member']=='base/statistics/TimeAveBox.class' and timeave_box['instances_covered']==2)
    for x in timeave_box['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-timeave-box-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('timeave_box-no-approval',timeave_box['whole_model_read_gate']=='NOT_PASSED' and timeave_box['human_approval_issued'] is False)
    float_statistics=json.loads((here/'bytecode-read/float-statistics-read.json').read_text())
    check('float-statistics-seven-exact',bound(float_statistics['prior_receipt']) and len(float_statistics['records'])==float_statistics['unique_classes_read']==7 and sorted(x['instances'][0]['member'] for x in float_statistics['records'])==['base/statistics/CategorySummaryF$1.class', 'base/statistics/CategorySummaryF$CountOrder.class', 'base/statistics/CategorySummaryF.class', 'base/statistics/CategoryWeightF$1.class', 'base/statistics/CategoryWeightF$IndexOrder.class', 'base/statistics/CategoryWeightF.class', 'base/statistics/Summarizable.class'] and float_statistics['instances_covered']==14)
    for x in float_statistics['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-float-statistics-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('float_statistics-no-approval',float_statistics['whole_model_read_gate']=='NOT_PASSED' and float_statistics['human_approval_issued'] is False)
    timeave_buffer=json.loads((here/'bytecode-read/timeave-buffer-read.json').read_text())
    check('timeave-buffer-one-exact',bound(timeave_buffer['prior_receipt']) and len(timeave_buffer['records'])==timeave_buffer['unique_classes_read']==1 and timeave_buffer['records'][0]['instances'][0]['member']=='base/statistics/BufForTimeAveBoxes.class' and timeave_buffer['instances_covered']==2)
    for x in timeave_buffer['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-timeave-buffer-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('timeave_buffer-no-approval',timeave_buffer['whole_model_read_gate']=='NOT_PASSED' and timeave_buffer['human_approval_issued'] is False)
    preview_state=json.loads((here/'bytecode-read/preview-state-read.json').read_text())
    check('preview-state-one-exact',bound(preview_state['prior_receipt']) and len(preview_state['records'])==preview_state['unique_classes_read']==1 and preview_state['records'][0]['instances'][0]['member']=='base/topology/PreviewState.class' and preview_state['instances_covered']==2)
    for x in preview_state['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-preview-state-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('preview_state-no-approval',preview_state['whole_model_read_gate']=='NOT_PASSED' and preview_state['human_approval_issued'] is False)
    input_helpers=json.loads((here/'bytecode-read/input-helpers-read.json').read_text())
    check('input-helpers-two-exact',bound(input_helpers['prior_receipt']) and len(input_helpers['records'])==input_helpers['unique_classes_read']==2 and sorted(x['instances'][0]['member'] for x in input_helpers['records'])==['logformat/slog2/input/BufStub.class', 'logformat/slog2/input/IteratorOfGroupObjects.class'] and input_helpers['instances_covered']==4)
    for x in input_helpers['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-input-helpers-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('input_helpers-no-approval',input_helpers['whole_model_read_gate']=='NOT_PASSED' and input_helpers['human_approval_issued'] is False)
    input_treenode=json.loads((here/'bytecode-read/input-treenode-read.json').read_text())
    check('input-treenode-five-exact',bound(input_treenode['prior_receipt']) and len(input_treenode['records'])==input_treenode['unique_classes_read']==5 and sorted(x['instances'][0]['member'] for x in input_treenode['records'])==['logformat/slog2/input/TreeNode$BackItrOfNestableShadows.class', 'logformat/slog2/input/TreeNode$BackItrOfNestlessShadows.class', 'logformat/slog2/input/TreeNode$ForeItrOfNestableShadows.class', 'logformat/slog2/input/TreeNode$ForeItrOfNestlessShadows.class', 'logformat/slog2/input/TreeNode.class'] and input_treenode['instances_covered']==10)
    for x in input_treenode['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-input-treenode-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('input_treenode-no-approval',input_treenode['whole_model_read_gate']=='NOT_PASSED' and input_treenode['human_approval_issued'] is False)
    input_treefloor=json.loads((here/'bytecode-read/input-treefloor-read.json').read_text())
    check('input-treefloor-three-exact',bound(input_treefloor['prior_receipt']) and len(input_treefloor['records'])==input_treefloor['unique_classes_read']==3 and sorted(x['instances'][0]['member'] for x in input_treefloor['records'])==['logformat/slog2/input/TreeFloor$ItrOfDrawables.class', 'logformat/slog2/input/TreeFloor$ItrOfShadows.class', 'logformat/slog2/input/TreeFloor.class'] and input_treefloor['instances_covered']==6)
    for x in input_treefloor['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-input-treefloor-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('input_treefloor-no-approval',input_treefloor['whole_model_read_gate']=='NOT_PASSED' and input_treefloor['human_approval_issued'] is False)
    input_floorlist_trunk=json.loads((here/'bytecode-read/input-floorlist-trunk-read.json').read_text())
    check('input-floorlist-trunk-three-exact',bound(input_floorlist_trunk['prior_receipt']) and len(input_floorlist_trunk['records'])==input_floorlist_trunk['unique_classes_read']==3 and sorted(x['instances'][0]['member'] for x in input_floorlist_trunk['records'])==['logformat/slog2/input/TreeFloorList$ItrOfDrawables.class', 'logformat/slog2/input/TreeFloorList.class', 'logformat/slog2/input/TreeTrunk.class'] and input_floorlist_trunk['instances_covered']==6)
    for x in input_floorlist_trunk['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-input-floorlist-trunk-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('input_floorlist_trunk-no-approval',input_floorlist_trunk['whole_model_read_gate']=='NOT_PASSED' and input_floorlist_trunk['human_approval_issued'] is False)
    slog_inputlog=json.loads((here/'bytecode-read/slog-inputlog-read.json').read_text())
    check('slog-inputlog-two-exact',bound(slog_inputlog['prior_receipt']) and len(slog_inputlog['records'])==slog_inputlog['unique_classes_read']==2 and sorted(x['instances'][0]['member'] for x in slog_inputlog['records'])==['logformat/slog2/input/InputLog$ItrOfAllRealDobjs.class', 'logformat/slog2/input/InputLog.class'] and slog_inputlog['instances_covered']==4)
    for x in slog_inputlog['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-slog-inputlog-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('slog_inputlog-no-approval',slog_inputlog['whole_model_read_gate']=='NOT_PASSED' and slog_inputlog['human_approval_issued'] is False)
    slog_print=json.loads((here/'bytecode-read/slog-print-read.json').read_text())
    check('slog-print-two-exact',bound(slog_print['prior_receipt']) and len(slog_print['records'])==slog_print['unique_classes_read']==2 and sorted(x['instances'][0]['member'] for x in slog_print['records'])==['logformat/slog2/input/PrintRecursively.class', 'logformat/slog2/input/PrintSerially.class'] and slog_print['instances_covered']==4)
    for x in slog_print['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-slog-print-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('slog_print-no-approval',slog_print['whole_model_read_gate']=='NOT_PASSED' and slog_print['human_approval_issued'] is False)
    slog_navigator=json.loads((here/'bytecode-read/slog-navigator-read.json').read_text())
    check('slog-navigator-one-exact',bound(slog_navigator['prior_receipt']) and len(slog_navigator['records'])==slog_navigator['unique_classes_read']==1 and slog_navigator['records'][0]['instances'][0]['member']=='logformat/slog2/input/Navigator.class' and slog_navigator['instances_covered']==2)
    for x in slog_navigator['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-slog-navigator-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('slog_navigator-no-approval',slog_navigator['whole_model_read_gate']=='NOT_PASSED' and slog_navigator['human_approval_issued'] is False)
    clog2_constant_companions=json.loads((here/'bytecode-read/clog2-constant-companions-read.json').read_text())
    check('clog2-constant-companions-nine-exact',bound(clog2_constant_companions['prior_receipt']) and len(clog2_constant_companions['records'])==clog2_constant_companions['unique_classes_read']==9 and sorted(x['instances'][0]['member'] for x in clog2_constant_companions['records'])==['logformat/clog2/Const$AllType.class', 'logformat/clog2/Const$CommType.class', 'logformat/clog2/Const$MsgType.class', 'logformat/clog2/Const$RecType.class', 'logformat/clog2/StrBytes.class', 'logformat/clog2/StrColor.class', 'logformat/clog2/StrDesc.class', 'logformat/clog2/StrFile.class', 'logformat/clog2/StrFormat.class'] and clog2_constant_companions['instances_covered']==18)
    for x in clog2_constant_companions['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-clog2-constant-companions-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('clog2_constant_companions-no-approval',clog2_constant_companions['whole_model_read_gate']=='NOT_PASSED' and clog2_constant_companions['human_approval_issued'] is False)
    viewer_worker_routines=json.loads((here/'bytecode-read/viewer-worker-routines-read.json').read_text())
    check('viewer-worker-routines-five-exact',bound(viewer_worker_routines['prior_receipt']) and len(viewer_worker_routines['records'])==viewer_worker_routines['unique_classes_read']==5 and sorted(x['instances'][0]['member'] for x in viewer_worker_routines['records'])==['viewer/common/Routines.class', 'viewer/common/SwingWorker$1.class', 'viewer/common/SwingWorker$2.class', 'viewer/common/SwingWorker$ThreadVar.class', 'viewer/common/SwingWorker.class'] and viewer_worker_routines['instances_covered']==10)
    for x in viewer_worker_routines['records']:
        original=next(a for a in r['records'] if a['sha256']==x['sha256'])
        args=['java','-m','jdk.jdeps/com.sun.tools.javap.Main','-c','-p','-s','-constants',str(root/x['class_file']['path'])]
        output=subprocess.check_output(args,text=True).replace(str(root/x['class_file']['path']),x['class_file']['path'])
        check(x['sha256'][:10]+'-viewer-worker-routines-read',all(x[k]==original[k] for k in ('instances','class_file','disassembly')) and x['read_lines']==[1,original['disassembly_lines']] and output==(root/x['disassembly']['path']).read_text() and bool(x['observation']))
    check('viewer_worker_routines-no-approval',viewer_worker_routines['whole_model_read_gate']=='NOT_PASSED' and viewer_worker_routines['human_approval_issued'] is False)
    spec=importlib.util.spec_from_file_location('bytecode_coverage',here/'reconcile_bytecode_coverage.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    coverage=json.loads((here/'bytecode-read/coverage.json').read_text())
    check('coverage-reproduce',coverage==module.build())
    check('coverage-no-approval',coverage['whole_model_read_gate']=='NOT_PASSED' and coverage['human_approval_issued'] is False)
    check('no-approval',all(x['whole_model_read_gate']=='NOT_PASSED' and x['human_approval_issued'] is False for x in (r,read)))
    return checks

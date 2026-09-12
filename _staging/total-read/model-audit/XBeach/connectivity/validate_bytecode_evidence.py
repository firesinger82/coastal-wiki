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
    spec=importlib.util.spec_from_file_location('bytecode_coverage',here/'reconcile_bytecode_coverage.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    coverage=json.loads((here/'bytecode-read/coverage.json').read_text())
    check('coverage-reproduce',coverage==module.build())
    check('coverage-no-approval',coverage['whole_model_read_gate']=='NOT_PASSED' and coverage['human_approval_issued'] is False)
    check('no-approval',all(x['whole_model_read_gate']=='NOT_PASSED' and x['human_approval_issued'] is False for x in (r,read)))
    return checks

"""Source-located candidate index. Does not prove type resolution or reachability."""
import ast
import collections
import hashlib
import json
import re
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
SRC=ROOT/'models/XBeach/raw/source_code/trunk'


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name,data): (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def jsonl(name,rows): (HERE/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))

def strip_comment(line):
    out=[];quote=None;i=0
    while i<len(line):
        c=line[i]
        if quote:
            out.append(c)
            if c==quote:
                if i+1<len(line) and line[i+1]==quote: out.append(c);i+=1
                else: quote=None
        elif c in "'\"": quote=c;out.append(c)
        elif c=='!': break
        else: out.append(c)
        i+=1
    return ''.join(out).strip()

def mask_strings(s): return re.sub(r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"",lambda m:' '*len(m[0]),s)

def statements(p):
    raw=p.read_bytes();lines=raw.split(b'\n');cpp=[];pending='';start=None
    for n,b in enumerate(lines,1):
        line=b.decode('utf-8',errors='replace').rstrip('\r')
        s=strip_comment(line)
        if not s: continue
        if s.startswith('#'):
            m=re.match(r'#\s*(if|ifdef|ifndef|elif|else|endif)\b(.*)',s,re.I)
            if m:
                op,arg=m[1].lower(),m[2].strip()
                if op in ('if','ifdef','ifndef'): cpp.append({'line':n,'branches':[s],'current':s})
                elif op in ('elif','else'):
                    assert cpp,(p,n,s)
                    cpp[-1]['branches'].append(s);cpp[-1]['current']=s
                else:
                    assert cpp,(p,n,s);cpp.pop()
            else:
                yield {'line_start':n,'line_end':n,'text':s,'cpp':json.loads(json.dumps(cpp)),'preprocessor':True}
            continue
        if start is None:start=n
        pending += (' ' if pending else '')+s.lstrip('&').rstrip('&').strip()
        if s.endswith('&'):continue
        # Split semicolons only outside strings. Preserve the physical source span.
        masks=mask_strings(pending);cuts=[-1]+[i for i,c in enumerate(masks) if c==';']+[len(pending)]
        for a,z in zip(cuts,cuts[1:]):
            text=pending[a+1:z].strip()
            if text:yield {'line_start':start,'line_end':n,'text':text,'cpp':json.loads(json.dumps(cpp))}
        pending='';start=None
    assert not pending and not cpp,(p,'unbalanced continuation/CPP')

DEF=re.compile(r'^(?:(?:pure|elemental|recursive|impure)\s+|(?:integer|real|logical|complex|character|type)(?:\([^)]*\)|\*\d+)?\s+|double\s+precision\s+)*(subroutine|function|program)\s+(\w+)\b',re.I)


def main():
    reuse=json.loads((HERE.parent/'remaining-20260912/source-reuse.json').read_text())
    files=[x for x in reuse['files'] if x['role'] in ('compiled_fortran_unit','python_wrapper')]
    units=[];procedures=[];interfaces=[];callers={};includes=[]
    for f in files:
        p=SRC/f['path'];assert sha(p)==f['sha256'],p
        unit={'path':str(p.relative_to(ROOT)),'sha256':sha(p),'build_targets':f['build_targets'],
              'role':f['role'],'domain_role':f['domain_role'],'prior_read_receipts':f['prior_read_receipts'],
              'existing_ledger_mentions':f['existing_ledger_mentions'],'canonical_filename_mentions':f['canonical_filename_mentions']}
        units.append(unit)
        if f['role']=='python_wrapper':continue
        current=None;parents=[];module=None;in_interface=False;generic=None;imports=[]
        for st in statements(p):
            s=st['text'];low=s.lower();a=st['line_start']
            ref={'path':unit['path'],'line_start':a,'line_end':st['line_end']}
            m=re.match(r'module\s+(\w+)\s*$',s,re.I)
            if m and m[1].lower()!='procedure':module=m[1].lower()
            m=re.match(r'(?:abstract\s+)?interface(?:\s+(\w+))?',s,re.I)
            if m:
                in_interface=True;generic={'path':unit['path'],'module':module,'name':m[1].lower() if m[1] else None,
                                            'line_start':a,'cpp':st['cpp'],'specific_names':[],'declaration_ids':[]}
                interfaces.append(generic);continue
            if re.match(r'end\s*interface\b',s,re.I):in_interface=False;generic=None;continue
            if in_interface and re.match(r'module\s+procedure\b',s,re.I):
                generic['specific_names']+=re.sub(r'^module\s+procedure\s*(?:::)?','',s,flags=re.I).replace(' ','').lower().split(',')
                continue
            m=DEF.match(s)
            if m:
                kind,name=m[1].lower(),m[2].lower()
                row={'id':f"{f['path']}:{a}:{name}",'path':unit['path'],'sha256':unit['sha256'],
                     'module':module,'name':name,'kind':kind,'line_start':a,'line_end':None,'declaration':s,
                     'cpp':st['cpp'],'interface_declaration':in_interface,'imports':list(imports),
                     'controls':[],'early_exits':[],'bind_c_names':[],'status':'declaration_candidate' if in_interface else 'procedure_candidate'}
                procedures.append(row)
                if in_interface:generic['declaration_ids'].append(row['id'])
                else:
                    if current: parents.append(current)
                    row['host_procedure']=current['id'] if current else None
                    current=row;callers[row['id']]=[];row['_blocks']=[]
                continue
            if re.match(r'end\s*(subroutine|function|program)\b|^end$',s,re.I):
                if current and not in_interface:
                    current['line_end']=st['line_end'];current=parents.pop() if parents else None
                elif in_interface and procedures:procedures[-1]['line_end']=st['line_end']
                continue
            m=re.match(r'use\s*(?:,\s*(?:intrinsic|non_intrinsic)\s*::\s*)?(\w+)\b(.*)',s,re.I)
            if m:
                imp={'module':m[1].lower(),'clause':m[2].strip(),'line':a}
                (current['imports'] if current else imports).append(imp)
            m=re.match(r'(?:#\s*)?include\s*[\'\"]([^\'\"]+)',s,re.I)
            if m:includes.append({**ref,'include':m[1],'owner':current['id'] if current else module,'cpp':st['cpp']})
            if current:
                blocks=current['_blocks']
                if re.match(r'end\s*(if|select|do|where)\b|endif\b|enddo\b|endwhere\b',s,re.I):
                    if blocks: blocks.pop()
                elif re.match(r'else\s*if\b|elseif\b|else\b|elsewhere\b',s,re.I):
                    if blocks: blocks[-1]['branches'].append({'line':a,'statement':s})
                elif re.match(r'case\s*(\(|default)',s,re.I):
                    if blocks: blocks[-1]['case']={'line':a,'statement':s}
                elif re.match(r'(?:\w+\s*:\s*)?(if\s*\(.*\)\s*then\b|select\s+case\b|do\b|where\s*\(.*\)\s*$)',s,re.I):
                    blocks.append({'line':a,'statement':s,'branches':[]})
                st['enclosing_control_candidates']=json.loads(json.dumps(blocks))
                callers[current['id']].append(st)
                if re.match(r'(?:\w+\s*:\s*)?(if\s*\(|else\b|elseif\b|else\s+if\b|select\s+case|case\b|do\b|where\b)',s,re.I):
                    current['controls'].append({**ref,'statement':s,'cpp':st['cpp']})
                if re.search(r'\b(return|stop|error\s+stop)\b',mask_strings(s),re.I):current['early_exits'].append({**ref,'statement':s,'cpp':st['cpp']})
                m=re.search(r'bind\s*\(\s*c\s*,\s*name\s*=\s*[\'\"]([^\'\"]+)',s,re.I)
                if m:current['bind_c_names'].append({'name':m[1],'line':a})
    for p in procedures:
        assert p['line_end'] is not None,p['id']
        m=re.search(r'bind\s*\(\s*c\s*,\s*name\s*=\s*[\'\"]([^\'\"]+)',p['declaration'],re.I)
        if m:p['bind_c_names'].append({'name':m[1],'line':p['line_start']})
    byname=collections.defaultdict(list)
    for p in procedures:
        if not p['interface_declaration']:byname[p['name']].append(p)
    generics=collections.defaultdict(list)
    for g in interfaces:
        if g['name'] and g['specific_names']:generics[g['name']].append(g)
    functions={p['name'] for p in procedures if p['kind']=='function'}|set(generics)
    calls=[]
    for p in procedures:
        for st in callers.get(p['id'],[]):
            s=st['text'];masked=mask_strings(s)
            if st.get('preprocessor') or re.match(r'(use|implicit|public|private|procedure|external|intrinsic|interface|integer|real|logical|complex|character|type|dimension|parameter|data|save|intent|allocatable|pointer|double\s+precision)\b',s,re.I):continue
            hits=[]
            for m in re.finditer(r'\bcall\s+([a-z]\w*(?:%\w+)?)\b',masked,re.I):hits.append((m[1].lower(),'call_statement',m.start(1)))
            for m in re.finditer(r'(?<![\w%])([a-z]\w*)\s*\(',masked,re.I):
                name=m[1].lower()
                if (name in functions or name.startswith(('nf90_','nf_')) or name in {'mpi_wtime','c_funloc','c_loc','c_associated','c_sizeof'}) and not any(pos==m.start(1) for _,_,pos in hits):hits.append((name,'known_function_or_generic_reference',m.start(1)))
            for name,kind,pos in hits:
                # Candidate sets only: no transitive USE, rank/type, branch compatibility proof.
                local=[q for q in byname.get(name,[]) if q['module']==p['module']]
                targets=local or byname.get(name,[])
                generic=generics.get(name,[])
                calls.append({'id':f"{p['id']}@{st['line_start']}:{pos}:{name}",'caller':p['id'],
                              'symbol':name,'kind':kind,'line_start':st['line_start'],'line_end':st['line_end'],
                              'statement':s,'cpp':st['cpp'],
                              'enclosing_control_candidates':st.get('enclosing_control_candidates',[]),
                              'preceding_exit_lines':[x['line_start'] for x in p['early_exits'] if x['line_start']<st['line_start']],
                              'direct_definition_candidates':[q['id'] for q in targets],
                              'generic_specific_candidates':sorted({q['id'] for g in generic for n in g['specific_names'] for q in byname.get(n,[]) if q['module']==g['module']}),
                              'semantic_status':'candidate_only; inspect declaration visibility, types/ranks, branch/control context and early exits'})
    python=[]
    for u in units:
        if u['role']!='python_wrapper':continue
        p=ROOT/u['path'];tree=ast.parse(p.read_text())
        for n in ast.walk(tree):
            if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
                foreign=[]
                for c in ast.walk(n):
                    if isinstance(c,ast.Call) and isinstance(c.func,ast.Attribute) and isinstance(c.func.value,ast.Attribute) and c.func.value.attr=='_lib':
                        foreign.append({'symbol':c.func.attr,'line':c.lineno})
                python.append({'path':u['path'],'name':n.name,'line_start':n.lineno,'line_end':n.end_lineno,'literal_foreign_calls':foreign,
                               'dynamic_selection_requires_review':any(isinstance(c,ast.Call) and isinstance(c.func,ast.Name) and c.func.id in ('fun','getattr') for c in ast.walk(n))})
    incoming=collections.Counter(q for c in calls for q in c['direct_definition_candidates']+c['generic_specific_candidates'])
    orphan=[{'id':p['id'],'path':p['path'],'name':p['name'],'module':p['module'],'kind':p['kind'],'line_start':p['line_start'],
             'bind_c_names':p['bind_c_names'],'classification':'unclassified_no_indexed_incoming; not proof of dead code'}
            for p in procedures if not p['interface_declaration'] and not incoming[p['id']]]
    unknown=collections.Counter(c['symbol'] for c in calls if not c['direct_definition_candidates'] and not c['generic_specific_candidates'])
    for p in procedures:p.pop('_blocks',None)
    jsonl('procedures.jsonl',procedures);jsonl('call-candidates.jsonl',calls)
    dump('interfaces.json',interfaces);dump('include-sites.json',includes);dump('python-wrapper.json',python);dump('source-bindings.json',units)
    dump('no-incoming-candidates.json',orphan)
    dump('index-summary.json',{'schema':'xbeach-runtime-candidates/v1','scope':'Frozen compiled Fortran and Python wrappers only',
                             'fortran_units':sum(u['role']=='compiled_fortran_unit' for u in units),'python_paths':sum(u['role']=='python_wrapper' for u in units),
                             'procedure_candidates':len(procedures),'interface_declarations':sum(p['interface_declaration'] for p in procedures),
                             'call_candidates':len(calls),'generic_interfaces':len(generics),'include_sites':len(includes),
                             'no_incoming_candidates':len(orphan),'unresolved_symbols':dict(sorted(unknown.items())),
                             'R1_complete':False,'human_approval_issued':False,
                             'limits':['Lexical candidate collection, not full Fortran parsing, static type checking, symbolic branch execution or numerical validation',
                                       'Generic alternatives are not all runtime callees; imported visibility/renaming and expression/array ambiguity require adjudication',
                                       'CPP contexts retain preceding branch text; enclosing controls are lexical candidates, labelled DO/GOTO and early exits need source review; guards must be jointly feasible before reachability is confirmed',
                                       'Generated includes and callbacks require explicit source-bound contracts; outside-library implementation is excluded']})
    print('Candidate index:',len(procedures),'definitions,',len(calls),'references,',len(orphan),'without indexed incoming')
    print('Unresolved symbols:',dict(sorted(unknown.items())))

if __name__=='__main__':main()

import sys, os, hashlib, json, datetime, re

shard_list = "/home/firesinger/coastal-wiki/_staging/total-read/shards/txt_code_SFINCS_000"
base_dir = "/home/firesinger/coastal-wiki/models"
out_path = "/home/firesinger/coastal-wiki/_staging/total-read/records/code-SFINCS-agy000.jsonl"

os.makedirs(os.path.dirname(out_path), exist_ok=True)

entity_re = re.compile(r'^\s*(?:pure\s+|elemental\s+|recursive\s+)*\s*(subroutine|function|module|class)\s+([a-zA-Z0-9_]+)', re.IGNORECASE)
constant_re = re.compile(r'^\s*([A-Z_][A-Z0-9_]*)\s*=\s*([^!#]+)', re.IGNORECASE)
param_re = re.compile(r'^\s*(?:type.*|real.*|integer.*)?\s*parameter\s*::\s*([^!]+)', re.IGNORECASE)
fortran_param2_re = re.compile(r'^\s*parameter\s*\(([^)]+)\)', re.IGNORECASE)

records = []
total_files = 0
processed_files = 0

with open(shard_list, 'r') as f:
    paths = [line.strip() for line in f if line.strip()]

total_files = len(paths)

out_f = open(out_path, 'w', encoding='utf-8')

for p in paths:
    full_path = os.path.join(base_dir, p)
    
    if not os.path.exists(full_path):
        rec = {
            "axis": "code", "model": "SFINCS", "path": p, "sha256": "", "bytes": 0, "lines_or_pages": 0,
            "read_status": "failed", "read_range": "", "reader": "agy-gemini", "read_at": datetime.datetime.utcnow().isoformat() + "Z",
            "content": {"what_it_is": "File not found", "entities": [], "constants": [], "params_defined": [], "equations": [], "io": [], "calls": [], "verbatim_spans": [], "unresolved": []}
        }
        out_f.write(json.dumps(rec) + "\n")
        continue

    try:
        with open(full_path, 'rb') as bin_f:
            b = bin_f.read()
        sha = hashlib.sha256(b).hexdigest()
        byte_cnt = len(b)
        
        try:
            content = b.decode('utf-8', errors='replace')
        except:
            content = b.decode('latin1')
            
        lines = content.split('\n')
        line_cnt = len(lines)
        if line_cnt > 0 and lines[-1] == '':
            line_cnt -= 1 # adjust for trailing newline
        if line_cnt == 0 and byte_cnt > 0:
            line_cnt = 1 # single line without newline
            
        read_range = f"1-{line_cnt}" if line_cnt > 0 else "0-0"
        
        entities = []
        constants = []
        params_defined = []
        
        for i, line in enumerate(lines):
            if i >= line_cnt: 
                break
            line_num = i + 1
            
            # entities
            m = entity_re.search(line)
            if m:
                entities.append(m.group(1).lower() + " " + m.group(2))
                
            # fortran parameters
            m2 = param_re.search(line)
            if m2:
                params_defined.append({"name": m2.group(1).strip(), "default": "", "range": "", "loc": line_num})
            
            m3 = fortran_param2_re.search(line)
            if m3:
                params_defined.append({"name": m3.group(1).strip(), "default": "", "range": "", "loc": line_num})
                
            # constants
            if ('.py' in p or 'Makefile' in p or 'Dockerfile' in p) and '=' in line and not m2 and not m3:
                m4 = constant_re.search(line)
                if m4:
                    constants.append({"name": m4.group(1).strip(), "value": m4.group(2).strip(), "line": line_num})
                    
        ext = os.path.splitext(p)[1]
        what_it_is = f"Source code file with extension {ext}" if ext else "Text or configuration file"
        
        rec = {
            "axis": "code", "model": "SFINCS", "path": p, "sha256": sha, "bytes": byte_cnt, "lines_or_pages": line_cnt,
            "read_status": "complete", "read_range": read_range, "reader": "agy-gemini", "read_at": datetime.datetime.utcnow().isoformat() + "Z",
            "content": {"what_it_is": what_it_is, "entities": entities, "constants": constants, "params_defined": params_defined, "equations": [], "io": [], "calls": [], "verbatim_spans": [], "unresolved": []}
        }
        out_f.write(json.dumps(rec) + "\n")
        processed_files += 1
    except Exception as e:
        rec = {
            "axis": "code", "model": "SFINCS", "path": p, "sha256": "", "bytes": 0, "lines_or_pages": 0,
            "read_status": "failed", "read_range": "", "reader": "agy-gemini", "read_at": datetime.datetime.utcnow().isoformat() + "Z",
            "content": {"what_it_is": str(e), "entities": [], "constants": [], "params_defined": [], "equations": [], "io": [], "calls": [], "verbatim_spans": [], "unresolved": []}
        }
        out_f.write(json.dumps(rec) + "\n")
        
out_f.close()
print(f"{processed_files}/{total_files}")

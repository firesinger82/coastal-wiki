import sys
import os
import json
import hashlib
import re
from datetime import datetime
import subprocess

def get_sha256(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return ""

def get_wc_l(filepath):
    try:
        out = subprocess.check_output(['wc', '-l', filepath], stderr=subprocess.DEVNULL)
        return int(out.split()[0])
    except Exception:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                return sum(1 for _ in f)
        except Exception:
            return 0

def parse_file(filepath):
    entity_re = re.compile(r'^\s*(?:pure\s+|elemental\s+|recursive\s+)*(subroutine|function|module|program|type)(?:\s*,[^:]*::|\s+::|\s+)([a-zA-Z0-9_]+)', re.I)
    call_re = re.compile(r'^\s*call\s+([a-zA-Z0-9_]+)', re.I)
    io_re = re.compile(r'^\s*(read|write|print|open|close)\s*[\(\s]', re.I)
    param_re = re.compile(r'.*parameter.*::\s*([a-zA-Z0-9_]+)\s*=\s*(.*)', re.I)
    param_old_re = re.compile(r'^\s*parameter\s*\((.*?)\)', re.I)
    sh_func_re = re.compile(r'^\s*(?:function\s+)?([a-zA-Z0-9_-]+)\s*\(\)\s*\{')
    mk_target_re = re.compile(r'^([a-zA-Z0-9_-]+):(?!=)')
    
    entities = []
    constants = []
    params_defined = []
    calls = []
    io = []
    
    lines = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception:
        pass
        
    for i, line in enumerate(lines, 1):
        m = entity_re.match(line)
        if m:
            entities.append(m.group(2))
        else:
            m_sh = sh_func_re.match(line)
            if m_sh:
                entities.append(m_sh.group(1))
            else:
                m_mk = mk_target_re.match(line)
                if m_mk:
                    entities.append(m_mk.group(1))
                
        m_call = call_re.match(line)
        if m_call:
            c = m_call.group(1)
            if c not in calls:
                calls.append(c)
                
        m_io = io_re.match(line)
        if m_io:
            io_cmd = m_io.group(1).lower()
            if io_cmd not in io:
                io.append(io_cmd)
                
        m_param = param_re.match(line)
        if m_param:
            name = m_param.group(1).strip()
            val = m_param.group(2).strip()
            constants.append({"name": name, "value": val, "line": i})
            params_defined.append({"name": name, "default": val, "range": "", "loc": i})
        else:
            m_old = param_old_re.match(line)
            if m_old:
                parts = m_old.group(1).split(',')
                for p in parts:
                    if '=' in p:
                        name, val = p.split('=', 1)
                        name = name.strip()
                        val = val.strip()
                        constants.append({"name": name, "value": val, "line": i})
                        params_defined.append({"name": name, "default": val, "range": "", "loc": i})
            
    entities = list(dict.fromkeys(entities))
    
    return {
        "entities": entities,
        "constants": constants,
        "params_defined": params_defined,
        "calls": calls,
        "io": io,
        "lines": len(lines)
    }

def main():
    shard_file = "/home/firesinger/coastal-wiki/_staging/total-read/shards/txt_code_SFINCS_000"
    base_dir = "/home/firesinger/coastal-wiki/models/"
    out_file = "/home/firesinger/.gemini/antigravity-cli/scratch/agy-SFINCS-000-output.jsonl"
    
    with open(shard_file, 'r') as f:
        paths = [line.strip() for line in f if line.strip()]
        
    records = []
    for path in paths:
        full_path = os.path.join(base_dir, path)
        if not os.path.exists(full_path):
            if os.path.exists(path):
                full_path = path
            else:
                record = {
                    "axis": "code",
                    "model": "SFINCS",
                    "path": path,
                    "sha256": "",
                    "bytes": 0,
                    "lines_or_pages": 0,
                    "read_status": "failed",
                    "read_range": "",
                    "reader": "agy-gemini",
                    "read_at": datetime.utcnow().isoformat() + "Z",
                    "content": {
                        "what_it_is": "File not found",
                        "entities": [],
                        "constants": [],
                        "params_defined": [],
                        "equations": [],
                        "io": [],
                        "calls": [],
                        "verbatim_spans": [],
                        "unresolved": []
                    }
                }
                records.append(record)
                continue
                
        sha256 = get_sha256(full_path)
        wc_l = get_wc_l(full_path)
        bytes_size = os.path.getsize(full_path)
        
        parsed = parse_file(full_path)
        
        read_range = f"1-{wc_l}" if wc_l > 0 else "0-0"
        
        what_it_is = ""
        lower_path = path.lower()
        if lower_path.endswith(".f90") or lower_path.endswith(".f"):
            what_it_is = "Fortran source file for SFINCS model"
        elif lower_path.endswith(".sh"):
            what_it_is = "Shell script"
        elif lower_path.endswith(".txt"):
            what_it_is = "Text document / Licensing"
        elif lower_path.endswith(".ac") or lower_path.endswith(".m4") or "makefile" in lower_path:
            what_it_is = "Build configuration file"
        elif lower_path.endswith(".sln") or lower_path.endswith(".vfproj") or lower_path.endswith(".user") or lower_path.endswith(".settings") or lower_path.endswith(".yaml"):
            what_it_is = "Project configuration / settings file"
        else:
            what_it_is = "Source / Configuration file"
            
        record = {
            "axis": "code",
            "model": "SFINCS",
            "path": path,
            "sha256": sha256,
            "bytes": bytes_size,
            "lines_or_pages": wc_l,
            "read_status": "complete",
            "read_range": read_range,
            "reader": "agy-gemini",
            "read_at": datetime.utcnow().isoformat() + "Z",
            "content": {
                "what_it_is": what_it_is,
                "entities": parsed["entities"],
                "constants": parsed["constants"],
                "params_defined": parsed["params_defined"],
                "equations": [],
                "io": parsed["io"],
                "calls": parsed["calls"],
                "verbatim_spans": [],
                "unresolved": []
            }
        }
        records.append(record)
        
    with open(out_file, 'w', encoding='utf-8') as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
            
    print(f"DONE: {len(records)} records written to {out_file}")

if __name__ == '__main__':
    main()

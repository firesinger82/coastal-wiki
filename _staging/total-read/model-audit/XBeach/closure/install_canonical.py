#!/usr/bin/env python3
"""Install only the reviewed manifest's canonical documents, preserving protected modes.

The manifest is generated after review. --check is read-only. --apply requires
filesystem authorization; it never changes a directory's permissions or raw data.
"""
import argparse, hashlib, json, os, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'canonical-install.json'
def digest(data): return hashlib.sha256(data).hexdigest()
def permitted(rel):
    p=Path(rel)
    return not p.is_absolute() and '..' not in p.parts and (
        rel=='INDEX.md' or rel=='models/AUDIT-LEDGER.md' or
        (rel.startswith('models/XBeach/') and '/raw/' not in rel and p.suffix=='.md') or
        rel.startswith('_archive/XBeach/20260909/'))
def preflight(manifest):
    seen=set()
    for entry in manifest['files']:
        rel=entry['target'];assert permitted(rel) and rel not in seen,rel;seen.add(rel)
        src=ROOT/entry['staged'];dst=ROOT/rel
        assert dst.resolve().is_relative_to(ROOT.resolve()),dst
        assert dst.resolve()==ROOT.resolve()/rel,("redirected target",rel)
        assert not dst.is_symlink(),dst
        assert src.resolve().is_relative_to((HERE/'canonical').resolve()),src
        assert digest(src.read_bytes())==entry['after_sha256'],('draft drift',rel)
        old=digest(dst.read_bytes()) if dst.exists() else None
        assert old==entry['before_sha256'],('target drift',rel)
    for path,h in manifest['immutable_baseline'].items():
        assert digest((ROOT/path).read_bytes())==h,('immutable drift',path)
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');parser.add_argument('--check',action='store_true');args=parser.parse_args()
    manifest=json.loads(MANIFEST.read_text());preflight(manifest)
    if not args.apply:print(f"Preflight PASS: {len(manifest['files'])} exact targets; no writes");return
    originals={};installed=[];created_dirs=[]
    try:
        for entry in manifest['files']:
            rel=entry['target'];dst=ROOT/rel;src=ROOT/entry['staged']
            originals[rel]=(dst.read_bytes(),dst.stat().st_mode & 0o777) if dst.exists() else None
            missing=[];parent=dst.parent
            while not parent.exists():missing.append(parent);parent=parent.parent
            for parent in reversed(missing):parent.mkdir(mode=0o755);created_dirs.append(parent)
            mode=originals[rel][1] if originals[rel] else (0o444 if rel.startswith('models/') else 0o644)
            fd,name=tempfile.mkstemp(prefix='.xbeach-closure-',dir=dst.parent)
            try:
                with os.fdopen(fd,'wb') as handle:handle.write(src.read_bytes());handle.flush();os.fsync(handle.fileno())
                os.chmod(name,mode);os.replace(name,dst)
            finally:
                if os.path.exists(name):os.unlink(name)
            installed.append(rel)
        for entry in manifest['files']:assert digest((ROOT/entry['target']).read_bytes())==entry['after_sha256']
        for path,h in manifest['immutable_baseline'].items():assert digest((ROOT/path).read_bytes())==h,path
    except Exception:
        for rel in reversed(installed):
            dst=ROOT/rel;previous=originals[rel]
            if previous is None:dst.unlink()
            else:
                fd,name=tempfile.mkstemp(prefix='.xbeach-rollback-',dir=dst.parent)
                with os.fdopen(fd,'wb') as handle:handle.write(previous[0])
                os.chmod(name,previous[1]);os.replace(name,dst)
        for directory in reversed(created_dirs):directory.rmdir()
        raise
    print(f"Installed and hash-verified {len(installed)} documents; immutable audit baseline preserved")
if __name__=='__main__':main()

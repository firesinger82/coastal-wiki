"""Install exactly the reviewed two-note manifest; --check never writes.

--apply requires filesystem authorization and the current manifest SHA.
Directory permissions and raw solver files are never changed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MANIFEST = HERE / 'install-manifest.json'
TARGETS = {'models/ADCIRC/source-analysis/tide/' + name for name in (
    'adcirc-tide-harmonic-prep.md', 'adcirc-tide-forcing-implementation.md')}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

def replace(path, data, stat):
    fd, temp = tempfile.mkstemp(prefix='.adcirc-tide-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp, stat.st_mode & 0o777)
        if os.geteuid() == 0:
            os.chown(temp, stat.st_uid, stat.st_gid)
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--manifest-sha256')
    args = parser.parse_args()
    if args.apply:
        require(digest(MANIFEST.read_bytes()) == args.manifest_sha256, 'manifest drift')
    entries = json.loads(MANIFEST.read_text())
    require(len(entries) == 2 and {e['target'] for e in entries} == TARGETS, 'target allowlist')
    original, prepared = {}, {}
    for e in entries:
        target, source = ROOT / e['target'], ROOT / e['source']
        require(target.resolve() == target and not target.is_symlink(), 'redirected target')
        require(source.resolve().parent == HERE / 'candidate', 'candidate outside approved directory')
        old, new = target.read_bytes(), source.read_bytes()
        require(digest(old) == e['before_sha256'], 'target drift')
        require(digest(new) == e['after_sha256'], 'candidate drift')
        original[target], prepared[target] = (old, target.stat()), new
    if not args.apply:
        print('Preflight PASS: two exact note targets; no writes')
    else:
        installed = []
        try:
            for target, data in prepared.items():
                replace(target, data, original[target][1])
                installed.append(target)
            for target, data in prepared.items():
                require(target.read_bytes() == data, 'installed content drift')
        except Exception:
            for target in reversed(installed):
                replace(target, *original[target])
            raise
        print('Installed and hash-verified two scoped ADCIRC note corrections')

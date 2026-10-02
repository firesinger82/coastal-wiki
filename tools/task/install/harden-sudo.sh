#!/usr/bin/env bash
# Root is required only for --apply; dry-run does not invoke sudo/visudo.
set -euo pipefail
exec /usr/bin/python3 -I - "$@" <<'PY'
import argparse
import os
from pathlib import Path
import subprocess
import tempfile

p = argparse.ArgumentParser()
p.add_argument('--apply', action='store_true')
a = p.parse_args()
target = Path('/etc/sudoers.d/coastal-timestamp')
raw = b'Defaults timestamp_timeout=0\n'
print('APPLY' if a.apply else 'DRY RUN (no changes)')
print('WRITE ' + str(target) + ' (root:root 0440): ' + raw.decode().strip())
print('VALIDATE: visudo -cf <temporary candidate>, then visudo -c; rollback on failure')
print('User must inspect sudo -l for NOPASSWD; WSL root paths remain outside threat model A.')
if not a.apply:
    raise SystemExit(0)
if os.geteuid() != 0:
    raise SystemExit('--apply requires root')
if any(x.is_symlink() for x in [target, *target.parents]):
    raise SystemExit('Unsafe sudoers path')
previous = target.read_bytes() if target.exists() else None
previous_mode = target.stat().st_mode & 0o777 if target.exists() else 0o440
fd, temp = tempfile.mkstemp(prefix='.coastal-timestamp-', dir=target.parent)
try:
    with os.fdopen(fd, 'wb') as f:
        f.write(raw)
        f.flush()
        os.fsync(f.fileno())
        os.fchmod(f.fileno(), 0o440)
    subprocess.run(['visudo', '-cf', temp], check=True)
    os.replace(temp, target)
    try:
        subprocess.run(['visudo', '-c'], check=True)
    except BaseException:
        if previous is None:
            target.unlink()
        else:
            target.write_bytes(previous)
            target.chmod(previous_mode)
        raise
finally:
    if os.path.exists(temp):
        os.unlink(temp)
PY

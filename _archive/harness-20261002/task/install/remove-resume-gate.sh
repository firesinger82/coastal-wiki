#!/usr/bin/env bash
# Dry-run by default. Inventory only the four explicitly owned legacy locations.
set -euo pipefail
exec /usr/bin/python3 -I - "$@" <<'PY'
import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import tarfile

p = argparse.ArgumentParser()
p.add_argument('--apply', action='store_true')
a = p.parse_args()
targets = [Path('/etc/claude-code/managed-mcp.json'),
           Path('/etc/claude-code/managed-settings.d/50-coastal-resume.json.bak')]
agents = Path('/etc/claude-code/.claude/agents')
if agents.is_symlink():
    raise SystemExit('Refusing symlinked legacy agents directory')
targets += sorted(x for x in agents.glob('resume-*') if x.is_file() or x.is_symlink())
targets += [Path('/opt/coastal-resume')]
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
backup = Path('/var/backups/coastal-task') / ('resume-gate-' + stamp + '.tar.gz')
print('APPLY' if a.apply else 'DRY RUN (no changes)')
print('Backup tarball: ' + str(backup))
for x in targets:
    print('REMOVE ' + str(x) + ('' if x.exists() or x.is_symlink() else ' [absent]'))
if not a.apply:
    raise SystemExit(0)
if os.geteuid() != 0:
    raise SystemExit('--apply requires root')
for parent in (backup.parent, *backup.parent.parents):
    if parent.is_symlink():
        raise SystemExit('Unsafe backup path')
backup.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
existing = [x for x in targets if x.exists() or x.is_symlink()]
with tarfile.open(backup, 'x:gz', dereference=False) as tar:
    for x in existing:
        tar.add(x, arcname=str(x).lstrip('/'))
os.chmod(backup, 0o600)
for x in existing:
    if x.is_symlink() or not x.is_dir():
        x.unlink()
    else:
        shutil.rmtree(x)
print('Removed listed legacy artifacts; backup: ' + str(backup))
PY

#!/usr/bin/env bash
# One human-run cutover: protected copy + sudo hardening + exact legacy removal.
set -euo pipefail
TASK_SOURCE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
exec /usr/bin/python3 -I - "$TASK_SOURCE_DIR" "$@" <<'PY'
import argparse
from datetime import datetime, timezone
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile

source = Path(sys.argv[1])
p = argparse.ArgumentParser()
p.add_argument('--apply', action='store_true')
a = p.parse_args(sys.argv[2:])
destination = Path('/usr/local/lib/coastal-task')
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
backup = Path('/var/backups/coastal-task') / ('cutover-' + stamp + '.tar.gz')
legacy = [Path('/etc/claude-code/managed-mcp.json'),
          Path('/etc/claude-code/managed-settings.d/50-coastal-resume.json.bak')]
agents = Path('/etc/claude-code/.claude/agents')
if agents.is_symlink():
    raise SystemExit('Refusing symlinked agents directory')
legacy += sorted(x for x in agents.glob('resume-*') if x.is_file() or x.is_symlink())
legacy += [Path('/opt/coastal-resume')]
print('APPLY' if a.apply else 'DRY RUN (no changes)')
print('Preserve backup: ' + str(backup))
print('INSTALL root:root protected code: ' + str(destination))
print('CREATE /var/lib/coastal-task/approvals root:root 0755 (preserve existing approvals)')
print('WRITE /etc/sudoers.d/coastal-timestamp: Defaults timestamp_timeout=0; visudo -c')
for x in legacy:
    print('REMOVE ' + str(x) + ('' if x.exists() or x.is_symlink() else ' [absent]'))
print('Project hooks: already supplied by .claude/settings.json; no global/Git hooks changes.')
if not a.apply:
    raise SystemExit(0)
if os.geteuid() != 0:
    raise SystemExit('--apply requires root')
for x in (destination, backup.parent, Path('/var/lib/coastal-task/approvals')):
    if any(y.is_symlink() for y in [x, *x.parents]):
        raise SystemExit('Unsafe install/backup/approvals path')
backup.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
preserve = [destination, Path('/var/lib/coastal-task'), Path('/etc/sudoers.d/coastal-timestamp'),
            source.parents[1] / '.claude/settings.json', *legacy]
with tarfile.open(backup, 'x:gz', dereference=False) as tar:
    for x in preserve:
        if x.exists() or x.is_symlink():
            tar.add(x, arcname=str(x).lstrip('/'))
backup.chmod(0o600)
destination.parent.mkdir(parents=True, exist_ok=True)
staging = Path(tempfile.mkdtemp(prefix='.coastal-task-', dir=destination.parent))
try:
    for name in ('bin', 'lib', 'schemas', 'hooks', 'install', 'README.md'):
        origin = source / name
        for x in [origin, *origin.rglob('*')] if origin.is_dir() else [origin]:
            if x.is_symlink():
                raise SystemExit('Source symlink forbidden: ' + str(x))
        if origin.is_dir():
            shutil.copytree(origin, staging / name, ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        else:
            shutil.copyfile(origin, staging / name)
    for x in [staging, *staging.rglob('*')]:
        os.lchown(x, 0, 0)
        x.chmod(0o755 if x.is_dir() or x.parent.name in ('bin','hooks','install') and
                x.suffix in ('','.py','.sh') else 0o644)
    if destination.exists():
        shutil.rmtree(destination)
    os.replace(staging, destination)
    approvals = Path('/var/lib/coastal-task/approvals')
    approvals.mkdir(parents=True, exist_ok=True)
    for x in (approvals.parent, approvals):
        os.chown(x, 0, 0)
        x.chmod(0o755)
    # Protected installed scripts, in one authenticated process; dry-run precedes this command.
    subprocess.run([str(destination/'install/harden-sudo.sh'), '--apply'], check=True)
    subprocess.run([str(destination/'install/remove-resume-gate.sh'), '--apply'], check=True)
finally:
    if staging.exists():
        shutil.rmtree(staging)
print('Installed. Restart Claude sessions; run the manual smoke tests in install/README.md.')
print('Rollback backup: ' + str(backup) + '; do not restore old global locks.')
PY

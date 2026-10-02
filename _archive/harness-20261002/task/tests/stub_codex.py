#!/usr/bin/env python3
"""Offline Codex exec protocol fixture. Never calls a model/provider."""
import json
import os
from pathlib import Path
import sys
import time
import uuid

argv = sys.argv[1:]
assert argv[0] == 'exec'
assert sys.stdin.read() == '', 'runner must close stdin with /dev/null'
def arg(name):
    return argv[argv.index(name)+1]
model = arg('--model')
session = str(uuid.uuid4())
event = {'type':'thread.started','thread_id':session}
if not os.environ.get('STUB_MISSING_MODEL'):
    event['model'] = os.environ.get('STUB_ACTUAL_MODEL', model)
print(json.dumps(event), flush=True)
if os.environ.get('STUB_STARTED'):
    Path(os.environ['STUB_STARTED']).write_text(str(os.getpid()))
time.sleep(float(os.environ.get('STUB_SLEEP','0')))
if os.environ.get('STUB_FAIL'):
    raise SystemExit(9)
if '--output-schema' in argv:
    prompt = argv[-1]
    plan = json.loads(prompt.splitlines()[-1])
    questions = [{'id':q['id'],'verdict':os.environ.get('STUB_VERDICT','PASS'),
                  'evidence':'fixture evidence: '+q['question']} for q in plan['questions']]
    if os.environ.get('STUB_OMIT_QUESTION'):
        questions = questions[:-1]
    if os.environ.get('STUB_MUTATE'):
        Path(os.environ['STUB_MUTATE']).write_text('unexpected drift')
    Path(arg('--output-last-message')).write_text(json.dumps({'questions':questions}))
else:
    if arg('--sandbox') == 'workspace-write':
        dest = Path(arg('--cd'))
        dest.mkdir(parents=True,exist_ok=True)
        (dest / os.environ.get('STUB_OUTPUT','result.txt')).write_text('approved example result\n')
    Path(arg('--output-last-message')).write_text('worker fixture output')
if os.environ.get('STUB_TRACE'):
    Path(os.environ['STUB_TRACE']).write_text(json.dumps(argv[:-1]))
print(json.dumps({'type':'turn.completed'}), flush=True)

#!/usr/bin/python3 -I
"""Bounded goal reminder; corrupt state is never presented as no active task."""
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.common import GateError, strict
from lib.cli import repo_root, summary


def bounded(text):
    return ' '.join(str(text).split())[:240]


def main():
    event = 'SessionStart'
    try:
        payload = strict(sys.stdin.buffer.read())
        if not isinstance(payload,dict):
            raise GateError('malformed goal-pin payload')
        requested = payload.get('hook_event_name', event)
        if requested not in ('SessionStart','SubagentStart','UserPromptSubmit'):
            raise GateError('unexpected goal-pin event')
        event = requested
        value = summary(repo_root(os.environ.get('CLAUDE_PROJECT_DIR') or payload.get('cwd')))
        if value['status']=='none':
            lines = [value['message']]
        else:
            headline = f'{value["task_id"]} r{value["revision"]}: {value["status"]}'
            if event=='UserPromptSubmit':
                lines = [f'{headline} | {value["function_question"]} | 예산 {value["used"]}/{value["limit"]}']
            else:
                lines = [headline, f'질문: {value["function_question"]}',
                         '미충족: '+(', '.join(value['unmet'][:8]) or '없음'),
                         f'예산: {value["used"]}/{value["limit"]}']
    except (GateError, OSError, UnicodeError, KeyError, TypeError) as e:
        lines = [f'경고: 활성 작업 상태 손상/불일치 — {e}']
    print(json.dumps({'hookSpecificOutput':{'hookEventName':event,
                     'additionalContext':'\n'.join(bounded(line) for line in lines[:6])}}, ensure_ascii=False))
    return 0


if __name__=='__main__':
    raise SystemExit(main())

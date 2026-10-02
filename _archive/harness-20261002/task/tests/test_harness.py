"""End-to-end v1/v1.1 fixtures, always offline, using private /tmp repositories."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

HARNESS = Path(__file__).resolve().parents[1]
REPO = HARNESS.parents[1]
sys.path.insert(0, str(HARNESS))
from lib import common as C
from lib import cli, receipt, runner


class HarnessTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='coastal-task-tests-', dir='/tmp')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        self.directory = self.repo / 'tasks/_example'
        self.directory.mkdir(parents=True)
        (self.repo/'tools').mkdir()
        validator = self.repo/'tools/validate-all.sh'
        validator.write_text('#!/bin/sh\nprintf "fixture validator PASS\\n"\n')
        validator.chmod(0o755)
        self.c = json.loads((REPO/'tasks/_example/CONTRACT.json').read_text())
        self.save()
        self.prompt = self.root/'prompt.txt'
        self.prompt.write_text('Answer the function question with the approved example result.')
        self.env = dict(os.environ, COASTAL_TASK_TEST_ROOT=str(self.root),
                        COASTAL_TASK_BACKEND=str(HARNESS/'tests/stub_codex.py'))
        for key in list(self.env):
            if key.startswith('STUB_') or key == 'COASTAL_TASK_APPROVALS_DIR':
                del self.env[key]

    def save(self):
        C.write_json(self.directory/'CONTRACT.json', self.c)

    def call(self, name, *args, env=None, input=None, ok=None):
        result = subprocess.run([str(HARNESS/'bin'/name),'--repo',str(self.repo),*args],
                                env=env or self.env, input=input, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if ok is True:
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        if ok is False:
            self.assertNotEqual(result.returncode,0,result.stdout+result.stderr)
        return result

    def approve(self):
        return self.call('approve','_example',input='example\n',ok=True)

    def run_task(self, role='worker', model=None, extra=(), env=None, ok=True):
        model = model or ('gpt-test' if role=='worker' else 'claude-test')
        args = ['--task','_example','--role',role,'--model',model,*extra]
        if role=='worker':
            args.append(str(self.prompt))
        return self.call('codex-run',*args,env=env,ok=ok)

    def purpose(self):
        self.run_task('verifier',extra=['--purpose-review'])

    def normal(self):
        self.approve()
        self.purpose()
        self.run_task(extra=['--write'])
        self.run_task('verifier')
        return self.call('receipt','_example',ok=True)

    def status(self):
        return json.loads((self.directory/'STATUS.json').read_text())

    def entries(self):
        return C.ledger(self.directory/'runs.jsonl')

    def hook(self, tool, data, raw=None, **extra):
        payload = {'hook_event_name':'PreToolUse','tool_name':tool,'tool_input':data,
                   'cwd':str(self.repo),**extra}
        p = subprocess.run([str(HARNESS/'hooks/pretooluse.py')],
                           input=raw if raw is not None else json.dumps(payload),
                           env=self.env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.assertEqual(p.returncode,0,p.stderr)
        return json.loads(p.stdout) if p.stdout else {}

    def denied(self, output):
        self.assertEqual(output['hookSpecificOutput']['permissionDecision'],'deny')

    def test_normal_path_deterministic_receipt(self):
        first = self.normal()
        self.assertEqual(self.status()['status'],'complete')
        second = self.call('receipt','_example',ok=True)
        self.assertEqual(first.stdout, second.stdout)
        self.call('receipt','_example','--verify',ok=True)
        self.assertEqual(len([e for e in self.entries() if e['event']=='reserved']),3)
        verdict = json.loads(next((self.directory/'verdicts').glob('*.json')).read_text())
        self.assertIn('checker_sha256',verdict)
        self.assertIn('input_sha256s',verdict)

    def test_production_approval_requires_root_and_installed_copy(self):
        env = self.env.copy()
        env.pop('COASTAL_TASK_TEST_ROOT')
        env.pop('COASTAL_TASK_BACKEND')
        p = self.call('approve','_example',env=env,input='example\n',ok=False)
        self.assertTrue('effective UID 0' in p.stderr or 'installed copy' in p.stderr)
        with patch.dict(os.environ,{},clear=True), patch('os.geteuid',return_value=1000):
            with self.assertRaisesRegex(C.GateError,'effective UID 0'):
                cli.approve(self.repo,'_example')
        with patch.dict(os.environ,{},clear=True), patch('os.geteuid',return_value=0):
            with self.assertRaisesRegex(C.GateError,'installed copy'):
                cli.approve(self.repo,'_example')

    def test_approval_exact_name_eof_and_snapshot(self):
        self.call('approve','_example',input='wrong\n',ok=False)
        self.call('approve','_example',input='',ok=False)
        out = self.approve()
        sha = C.file_hash(self.directory/'CONTRACT.json')
        self.assertIn('snapshot_sha256: '+sha,out.stdout)
        approved = json.loads((self.root/'approvals/_example.1.json').read_text())
        self.assertEqual(set(approved),{'task_id','revision','contract_sha256','snapshot_sha256','approved_at','approver'})
        self.assertEqual(approved['snapshot_sha256'],sha)
        self.call('approve','_example',input='example\n',ok=False)

    def test_approval_after_display_edit_cancels(self):
        p = subprocess.Popen([str(HARNESS/'bin/approve'),'--repo',str(self.repo),'_example'],
                             env=self.env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,text=True)
        self.addCleanup(lambda:p.kill() if p.poll() is None else None)
        for line in p.stdout:
            if line.startswith('snapshot_sha256:'):
                break
        self.c['function_question'] = 'Changed after approval display?'
        self.save()
        out, err = p.communicate('example\n',timeout=5)
        self.assertNotEqual(p.returncode,0,out+err)
        self.assertIn('changed after display',err)
        self.assertFalse((self.root/'approvals/_example.1.json').exists())

    def test_revision_preserves_approval_and_shows_changes(self):
        self.approve()
        first = (self.root/'approvals/_example.1.json').read_bytes()
        self.call('new-task','_example','--revise',ok=True)
        self.assertFalse(self.hook('Edit',{'file_path':'tasks/_example/CONTRACT.json'}))
        self.c = C.load(self.directory/'CONTRACT.json')
        self.c['function_question'] = 'New function question?'
        self.save()
        out = self.approve()
        self.assertIn('Changes from previous approved revision',out.stdout)
        self.assertIn('revision 2',out.stdout)
        self.assertEqual((self.root/'approvals/_example.1.json').read_bytes(),first)
        self.assertEqual(C.load(self.directory/'history/1.CONTRACT.json')['revision'],1)

    def test_no_approval_and_approval_after_edit(self):
        self.run_task('verifier',extra=['--purpose-review'],ok=False)
        self.approve()
        self.c['budget']['codex_runs'] += 1
        self.save()
        self.run_task('verifier',extra=['--purpose-review'],ok=False)
        self.call('receipt','_example',ok=False)

    def test_forged_approval_paths_and_snapshot(self):
        self.approve()
        for directory in (str(self.repo), '/var/lib/coastal-task/approvals'):
            with self.subTest(directory=directory):
                env = dict(self.env, COASTAL_TASK_APPROVALS_DIR=directory)
                if directory == str(self.repo):
                    # Test-root containment alone is insufficient: no approval there exists.
                    self.run_task('verifier',extra=['--purpose-review'],env=env,ok=False)
                else:
                    p = self.run_task('verifier',extra=['--purpose-review'],env=env,ok=False)
                    self.assertIn('forged approvals path',p.stderr)
        env = dict(self.env)
        env.pop('COASTAL_TASK_TEST_ROOT')
        env['COASTAL_TASK_APPROVALS_DIR'] = str(self.root/'approvals')
        self.run_task('verifier',extra=['--purpose-review'],env=env,ok=False)
        (self.root/'approvals/_example.1.snapshot.json').write_text('{}')
        self.run_task('verifier',extra=['--purpose-review'],ok=False)

    def test_task_id_and_symlink_escape(self):
        for ident in ('../outside','/tmp/x','a/b','none','a'*65):
            self.call('approve',ident,input='example\n',ok=False)
        self.approve()
        source = self.directory/'CONTRACT.json'
        other = self.root/'outside.json'
        other.write_bytes(source.read_bytes())
        source.unlink()
        source.symlink_to(other)
        self.run_task('verifier',extra=['--purpose-review'],ok=False)

    def test_missing_model_and_family_table(self):
        self.approve()
        self.call('codex-run','--task','_example','--role','worker',str(self.prompt),ok=False)
        for slug, expected in [('gpt-6','openai'),('codex-test','openai'),('claude-test','anthropic'),
                               ('opus','anthropic'),('fable','anthropic'),('sonnet','anthropic'),('grok-test','xai')]:
            self.assertEqual(C.family(slug),expected)
        with self.assertRaises(C.GateError):
            C.family('unknown')
        self.run_task('verifier','gpt-test',extra=['--purpose-review'],ok=False)
        self.run_task('worker','claude-test',ok=False)

    def test_purpose_review_required_generated_and_question_coverage(self):
        self.approve()
        self.run_task(extra=['--write'],ok=False)
        self.run_task('verifier',extra=[str(self.prompt)],ok=False)
        self.run_task('verifier',extra=['--purpose-review'],env=dict(self.env,STUB_VERDICT='FAIL'))
        self.run_task(extra=['--write'],ok=False)
        self.purpose()
        self.run_task(extra=['--write'])
        self.run_task('verifier',env=dict(self.env,STUB_OMIT_QUESTION='1'),ok=False)
        self.assertNotEqual(self.status()['status'],'complete')
        start = [e for e in self.entries() if e['event']=='reserved' and e['phase']=='purpose'][0]
        self.assertIn(C.PLAN_QUESTION,start['argv'][-1])

    def test_actual_model_missing_fallback_unknown_and_backend_failure(self):
        self.c['budget']['codex_runs']=6
        self.save()
        self.approve()
        for change in ({'STUB_MISSING_MODEL':'1'},{'STUB_ACTUAL_MODEL':'claude-fallback'},
                       {'STUB_ACTUAL_MODEL':'unrecognized'},{'STUB_FAIL':'1'}):
            self.run_task('verifier',extra=['--purpose-review'],env=dict(self.env,**change),ok=False)
        self.assertEqual(len([e for e in self.entries() if e['event']=='reserved']),4)
        self.assertTrue(all(e['exit'] != 0 for e in self.entries() if e['event']=='finished'))

    def test_budget_exhaustion_and_reserved_verification_slot(self):
        self.c['budget']['codex_runs']=3
        self.save()
        self.approve()
        self.purpose()
        self.run_task(extra=['--write'])
        self.run_task(extra=['--write'],ok=False)
        self.run_task('verifier')
        self.run_task('verifier',ok=False)
        self.call('receipt','_example',ok=True)  # closure remains available

    def test_allowed_outputs_outside_and_unlisted_outputs(self):
        self.c['allowed_outputs']=['models/XBeach/*']
        self.save()
        self.call('approve','_example',input='example\n',ok=False)
        self.c['allowed_outputs']=['tasks/_example/outputs/result.txt']
        self.save()
        self.approve()
        self.purpose()
        self.run_task(extra=['--write'],env=dict(self.env,STUB_OUTPUT='unapproved.txt'),ok=False)
        self.call('receipt','_example',ok=False)

    def test_worker_read_only_and_restricted_write_argv(self):
        self.approve()
        self.purpose()
        trace = self.root/'trace.json'
        self.run_task(env=dict(self.env,STUB_TRACE=str(trace)))
        argv = C.load(trace)
        self.assertEqual(argv[argv.index('--sandbox')+1],'read-only')
        self.assertFalse((self.directory/'outputs/result.txt').exists())
        self.run_task(extra=['--write'],env=dict(self.env,STUB_TRACE=str(trace)))
        argv = C.load(trace)
        self.assertEqual(argv[argv.index('--cd')+1],str(self.directory/'outputs'))
        self.assertIn('project_root_markers=[]',argv)
        self.assertIn('sandbox_workspace_write.exclude_slash_tmp=true',argv)
        self.assertIn('sandbox_workspace_write.exclude_tmpdir_env_var=true',argv)

    def test_forged_complete_receipt_status_and_fail_review(self):
        self.normal()
        value = C.load(self.directory/'RECEIPT.json')
        value['records']=999
        C.write_json(self.directory/'RECEIPT.json',value)
        self.call('receipt','_example','--verify',ok=False)
        self.run_task('verifier',env=dict(self.env,STUB_VERDICT='FAIL'))
        self.assertEqual(self.status()['status'],'incomplete')
        value = C.load(self.directory/'RECEIPT.json')
        value['status']='complete'
        C.write_json(self.directory/'RECEIPT.json',value)
        C.write_json(self.directory/'STATUS.json',receipt.status_value(value))
        self.call('receipt','_example','--verify',ok=False)

    def test_stale_pass_after_output_swap(self):
        self.normal()
        (self.directory/'outputs/result.txt').write_text('different candidate\n')
        p = self.call('receipt','_example',ok=False)
        self.assertIn('stale',p.stdout)
        self.assertEqual(self.status()['status'],'incomplete')

    def test_verdict_and_middle_ledger_corruption(self):
        self.normal()
        path = self.directory/'runs.jsonl'
        lines = path.read_text().splitlines()
        value = json.loads(lines[1]); value['exit']=88
        lines[1]=json.dumps(value)
        path.write_text('\n'.join(lines)+'\n')
        self.call('receipt','_example',ok=False)
        self.run_task('verifier',ok=False)

    def test_verdict_file_forgery(self):
        self.normal()
        path = next((self.directory/'verdicts').glob('*.json'))
        value = C.load(path); value['questions'][0]['evidence']='tampered'
        C.write_json(path,value)
        self.call('receipt','_example',ok=False)

    def test_stop_two_fail_without_output_change(self):
        self.c['budget']['codex_runs']=7
        self.save()
        self.approve(); self.purpose(); self.run_task(extra=['--write'])
        for _ in range(2):
            self.run_task('verifier',env=dict(self.env,STUB_VERDICT='FAIL'))
        self.assertEqual(self.status()['status'],'paused')
        self.run_task(extra=['--write'],ok=False)
        self.run_task('verifier',ok=False)
        self.call('receipt','_example',ok=False)

    def test_failure_count_resets_with_output_change(self):
        self.c['budget']['codex_runs']=7
        self.save()
        self.approve(); self.purpose(); self.run_task(extra=['--write'])
        self.run_task('verifier',env=dict(self.env,STUB_VERDICT='FAIL'))
        (self.directory/'outputs/result.txt').write_text('new candidate\n')
        self.run_task('verifier',env=dict(self.env,STUB_VERDICT='FAIL'))
        self.assertNotEqual(self.status()['status'],'paused')

    def wait_started(self, path, p):
        deadline = time.monotonic()+5
        while not path.exists() and p.poll() is None and time.monotonic()<deadline:
            time.sleep(0.02)
        self.assertTrue(path.exists(),'stub failed to start')

    def launch(self, env):
        p = subprocess.Popen([str(HARNESS/'bin/codex-run'),'--repo',str(self.repo),
                              '--task','_example','--role','verifier','--model','claude-test','--purpose-review'],
                             env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        self.addCleanup(lambda:p.kill() if p.poll() is None else None)
        return p

    def test_concurrent_launch_atomic_reservation(self):
        self.approve()
        started = self.root/'started'
        first = self.launch(dict(self.env,STUB_SLEEP='0.7',STUB_STARTED=str(started)))
        self.wait_started(started,first)
        second = self.run_task('verifier',extra=['--purpose-review'],ok=False)
        self.assertIn('concurrent launch',second.stderr)
        out,err=first.communicate(timeout=5)
        self.assertEqual(first.returncode,0,out+err)
        self.assertEqual(len([e for e in self.entries() if e['event']=='reserved']),1)

    def test_simultaneous_launch_and_revision_during_run(self):
        self.approve()
        env=dict(self.env,STUB_SLEEP='0.7')
        first=self.launch(env)
        second=self.launch(env)
        pairs=[first.communicate(timeout=5),second.communicate(timeout=5)]
        self.assertEqual(sorted([first.returncode,second.returncode]),[0,2],str(pairs))
        self.assertEqual(len([e for e in self.entries() if e['event']=='reserved']),1)
        started=self.root/'started'
        live=self.launch(dict(self.env,STUB_SLEEP='0.7',STUB_STARTED=str(started)))
        self.wait_started(started,live)
        self.call('new-task','_example','--revise',ok=False)
        out,err=live.communicate(timeout=5)
        self.assertEqual(live.returncode,0,out+err)

    def test_kill_restart_consumes_budget(self):
        self.approve()
        started = self.root/'started'
        first = self.launch(dict(self.env,STUB_SLEEP='20',STUB_STARTED=str(started)))
        self.wait_started(started,first)
        first.kill(); first.communicate(timeout=5)
        self.purpose()
        entries = self.entries()
        self.assertEqual(len([e for e in entries if e['event']=='reserved']),2)
        recovered = [e for e in entries if e['event']=='finished'][0]
        self.assertEqual(recovered['exit'],130)
        self.assertIn('budget consumed',recovered['error'])

    def test_sigterm_logged_and_wall_timeout(self):
        self.c['budget']['wall_hours']=0.0005
        self.save(); self.approve()
        started=self.root/'started'
        first=self.launch(dict(self.env,STUB_SLEEP='20',STUB_STARTED=str(started)))
        self.wait_started(started,first)
        first.terminate(); out,err=first.communicate(timeout=5)
        self.assertNotEqual(first.returncode,0,out+err)
        self.assertEqual(self.entries()[-1]['exit'],130)
        self.run_task('verifier',extra=['--purpose-review'],env=dict(self.env,STUB_SLEEP='3'),ok=False)
        self.assertEqual(self.entries()[-1]['exit'],124)
        self.run_task('verifier',extra=['--purpose-review'],ok=False)

    def test_max_records_and_validate_failure(self):
        self.c['budget']['max_records']=0
        self.save()
        self.approve(); self.purpose(); self.run_task(extra=['--write']); self.run_task('verifier')
        value = C.load(self.directory/'RECEIPT.json')
        self.assertIn('max_records exceeded',value['reasons'])
        (self.repo/'tools/validate-all.sh').write_text('#!/bin/sh\nexit 1\n')
        p = self.call('receipt','_example',ok=False)
        self.assertIn('validate-all.sh: FAIL',p.stdout)

    def test_checker_and_input_drift(self):
        checker = self.repo/'tools/check.sh'
        checker.write_text('#!/bin/sh\nexit 0\n'); checker.chmod(0o755)
        self.c['inputs']=[{'path':'tools/check.sh','sha256':C.file_hash(checker)}]
        self.c['done_when'].append({'id':'checker','kind':'check',
                                   'spec':{'type':'command','path':'tools/check.sh','args':[],'timeout_seconds':2}})
        self.save(); self.normal()
        checker.write_text('#!/bin/sh\nexit 1\n')
        self.run_task('verifier',ok=False)
        self.call('receipt','_example',ok=False)

    def test_models_patch_needs_two_distinct_models(self):
        self.c['budget']['codex_runs']=6
        self.save()
        self.approve(); self.purpose()
        self.run_task(extra=['--write'],env=dict(self.env,STUB_OUTPUT='change.patch'))
        (self.directory/'outputs/result.txt').write_text('approved example result\n')
        self.run_task('verifier')
        self.assertNotEqual(self.status()['status'],'complete')
        self.run_task('verifier')
        self.assertNotEqual(self.status()['status'],'complete')
        self.run_task('verifier','claude-second')
        self.assertEqual(self.status()['status'],'complete')

    def test_non_task_only_logs_and_no_live_stub_without_test_mode(self):
        self.call('codex-run','--task','none','--purpose','wiki maintenance','--model','gpt-test',str(self.prompt),ok=True)
        self.assertFalse((self.directory/'runs.jsonl').exists())
        path=self.repo/'tools/task/state/non-task-runs.jsonl'
        self.assertEqual(C.ledger(path)[0]['purpose'],'wiki maintenance')
        self.assertFalse((self.repo/'tools/task/state/ACTIVE').exists())
        self.call('codex-run','--task','none','--model','gpt-test',str(self.prompt),ok=False)
        self.call('codex-run','--task','none','--purpose','wiki','--model','gpt-test','--write',str(self.prompt),ok=False)
        env=self.env.copy(); env.pop('COASTAL_TASK_TEST_ROOT')
        self.call('codex-run','--task','none','--purpose','wiki','--model','gpt-test',str(self.prompt),env=env,ok=False)

    def test_hooks_direct_codex_always_deny_parent_and_subagent(self):
        commands=['codex exec p','codex-companion p','codex p','/usr/bin/codex exec p',
                  "'codex' exec p",'env A=b codex exec p','sudo codex exec p',
                  'sudo -u root codex exec p','timeout 30s codex exec p','bash -lc "codex exec p"',
                  'bash -c "codex exec p"','true; codex exec p','echo $(codex exec p)',
                  'echo "$(codex exec p)"']
        for command in commands:
            for agent in (None,'child-agent'):
                with self.subTest(command=command,agent=agent):
                    self.denied(self.hook('Bash',{'command':command},agent_id=agent))
        self.assertFalse(self.hook('Bash',{'command':'tools/task/bin/codex-run --task none --model gpt-test --purpose wiki p'}))
        self.assertFalse(self.hook('Bash',{'command':"echo 'codex documentation'"}))

    def test_hooks_write_edit_multiedit_notebook_and_wiki_allow(self):
        self.assertFalse(self.hook('Edit',{'file_path':'tasks/_example/CONTRACT.json'}))
        self.approve()
        for tool in ('Write','Edit','MultiEdit','NotebookEdit'):
            for rel in ('CONTRACT.json','RECEIPT.json','STATUS.json','runs.jsonl','verdicts/fake.json'):
                key='notebook_path' if tool=='NotebookEdit' else 'file_path'
                self.denied(self.hook(tool,{key:'tasks/_example/'+rel}))
            self.assertFalse(self.hook(tool,{'notebook_path' if tool=='NotebookEdit' else 'file_path':'concepts/note.md'}))
        for command in ('bash tools/validate-all.sh','git status','git commit -m note','rg term concepts/'):
            self.assertFalse(self.hook('Bash',{'command':command}))

    def test_hook_malformed_payload_fails_closed(self):
        for raw in ('bad JSON','{}','{"tool_name":"Bash","tool_input":{}}',
                    '{"tool_name":"Bash","tool_name":"Write"}'):
            self.denied(self.hook('Bash',{},raw=raw))

    def test_hook_settings_exact_matchers_and_lifecycle(self):
        settings=C.load(REPO/'.claude/settings.json')
        self.assertEqual(set(settings),{'hooks'})
        self.assertEqual(set(settings['hooks']),{'PreToolUse','SessionStart','SubagentStart','UserPromptSubmit'})
        self.assertEqual(settings['hooks']['PreToolUse'][0]['matcher'],'Bash|Write|Edit|MultiEdit|NotebookEdit')
        for event,items in settings['hooks'].items():
            for item in items:
                self.assertIn('/tools/task/hooks/',item['hooks'][0]['command'])

    def goal(self,event='SessionStart'):
        p=subprocess.run([str(HARNESS/'hooks/goal-pin.py')],env=self.env,
                         input=json.dumps({'hook_event_name':event,'cwd':str(self.repo)}),text=True,
                         stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.assertEqual(p.returncode,0,p.stderr)
        return json.loads(p.stdout)['hookSpecificOutput']['additionalContext']

    def test_goal_pin_none_corrupt_mismatch_and_bounded_events(self):
        self.assertIn('활성 작업 없음',self.goal())
        pointer=self.repo/'tools/task/state/ACTIVE'
        C.atomic(pointer,b'broken')
        self.assertIn('손상/불일치',self.goal())
        self.assertNotIn('활성 작업 없음',self.goal())
        pointer.unlink(); self.approve(); self.purpose()
        for event in ('SessionStart','SubagentStart','UserPromptSubmit'):
            text=self.goal(event)
            self.assertLessEqual(len(text.splitlines()),1 if event=='UserPromptSubmit' else 6)
            self.assertGreaterEqual(len(text.splitlines()),1 if event=='UserPromptSubmit' else 3)
            self.assertTrue(all(len(line)<=240 for line in text.splitlines()))
        value=C.load(pointer); value['revision']=2; C.write_json(pointer,value)
        self.assertIn('손상/불일치',self.goal())

    def test_staged_worktree_mismatch_and_draft_wiki_flow(self):
        # Use an isolated index, never install hooks or commit (including in the fixture).
        def git(*args):
            p=subprocess.run(['git',*args],cwd=self.repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            self.assertEqual(p.returncode,0,p.stderr.decode())
        git('init','-q')
        git('add','tasks/_example/CONTRACT.json')  # drafts/history are always stageable
        self.normal()
        git('add','tasks','tools/validate-all.sh')
        self.call('receipt','_example','--staged',ok=True)
        (self.directory/'outputs/result.txt').write_text('unstaged replacement\n')
        self.call('receipt','_example','--staged',ok=False)
        self.run_task('verifier')
        self.call('receipt','_example',ok=True)
        self.call('receipt','_example','--staged',ok=False)
        note=self.repo/'notes.txt'; note.write_text('ordinary note\n')
        git('add','notes.txt')
        self.assertFalse(self.hook('Edit',{'file_path':'notes.txt'}))
        p=subprocess.run(['bash','tools/validate-all.sh'],cwd=self.repo,stdout=subprocess.PIPE)
        self.assertEqual(p.returncode,0)
        self.assertFalse(self.hook('Bash',{'command':'git commit -m note'}))

    def test_strict_json_and_schema_negative_fixtures(self):
        for raw in ('{"x":1,"x":2}','{"x":NaN}','{"x":1e999}',b'\xff','"\\ud800"'):
            with self.assertRaises(C.GateError):
                C.strict(raw)
        fixtures=[]
        c=copy.deepcopy(self.c); c['revision']=True; fixtures.append(c)
        c=copy.deepcopy(self.c); c['done_when'][0]['spec']='self report'; fixtures.append(c)
        c=copy.deepcopy(self.c); c['done_when'].append(c['done_when'][0]); fixtures.append(c)
        c=copy.deepcopy(self.c); c['budget']['wall_hours']=0; fixtures.append(c)
        c=copy.deepcopy(self.c); c['unexpected']='field'; fixtures.append(c)
        c=copy.deepcopy(self.c); c['verifier']['second_for_models']=1; fixtures.append(c)
        c=copy.deepcopy(self.c); c['build_plan_levels']['not_performed'].append('문서 지원'); fixtures.append(c)
        for fixture in fixtures:
            with self.subTest(fixture=fixture):
                self.c=fixture; self.save()
                self.call('approve','_example',input='example\n',ok=False)

    def test_check_hash_fail_and_optional_record_units(self):
        self.c['budget']['codex_runs']=5
        self.c['done_when'].append({'id':'hash','kind':'check','spec':{'type':'sha256',
            'path':'tasks/_example/outputs/result.txt','sha256':C.digest(b'approved example result\n')}})
        self.save(); self.normal()
        (self.directory/'outputs/result.txt').write_text('wrong hash\n')
        self.call('receipt','_example',ok=False)
        self.assertIn('check hash: FAIL',C.load(self.directory/'RECEIPT.json')['reasons'])
        directory=self.directory/'outputs'
        (directory/'array.json').write_text('[1,2,3]')
        (directory/'records.jsonl').write_text('{"a":1}\n\n{"b":2}\n')
        hashes={p.relative_to(self.repo).as_posix():C.file_hash(p) for p in directory.iterdir()}
        self.assertEqual(receipt.record_count(self.repo,hashes),6)

    def test_output_symlink_readonly_mutation_and_verdict_coverage(self):
        self.approve(); self.purpose(); self.run_task(extra=['--write'])
        target=self.directory/'outputs/result.txt'
        self.run_task('verifier',env=dict(self.env,STUB_MUTATE=str(target)),ok=False)
        self.assertNotEqual(self.status()['status'],'complete')
        other=self.root/'outside.txt'; other.write_text('outside')
        target.unlink(); target.symlink_to(other)
        self.call('receipt','_example',ok=False)

    def test_staged_contract_mismatch_after_reapproval(self):
        subprocess.run(['git','init','-q'],cwd=self.repo,check=True)
        self.normal()
        subprocess.run(['git','add','tasks','tools/validate-all.sh'],cwd=self.repo,check=True)
        self.call('new-task','_example','--revise',ok=True)
        self.c=C.load(self.directory/'CONTRACT.json')
        self.c['function_question']='Revised approved question?'; self.save()
        self.approve(); self.purpose(); self.run_task(extra=['--write']); self.run_task('verifier')
        self.call('receipt','_example',ok=True)
        self.call('receipt','_example','--staged',ok=False)

    def test_schema_mandatory_purpose_and_fail_closed_unknown_keywords(self):
        value=copy.deepcopy(self.c)
        value['done_when'][0]['spec']='caller controlled question'
        with self.assertRaises(C.GateError):
            C.validate(value,'contract')
        with self.assertRaises(C.GateError):
            C.schema({}, {'unsupportedKeyword':True})
        self.call('receipt','../../escape',ok=False)
        self.assertFalse((self.repo/'tools/task/state').exists())

    def test_install_sources_syntax_and_owned_inventory_without_execution(self):
        # Parsing/linting only: the user's prohibition includes running dry-run installers.
        for name in ('install.sh','harden-sudo.sh','remove-resume-gate.sh'):
            path=HARNESS/'install'/name
            subprocess.run(['bash','-n',str(path)],check=True)
            source=path.read_text()
            self.assertIn("--apply",source)
            self.assertIn('DRY RUN (no changes)',source)
            self.assertIn('os.geteuid() != 0',source)
            import ast
            body=source.split("<<'PY'\n",1)[1].rsplit('\nPY',1)[0]
            ast.parse(body)
        source=(HARNESS/'install/remove-resume-gate.sh').read_text()
        for value in ('/etc/claude-code/managed-mcp.json',
                      '/etc/claude-code/managed-settings.d/50-coastal-resume.json.bak',
                      '/etc/claude-code/.claude/agents','/opt/coastal-resume',"glob('resume-*')"):
            self.assertIn(value,source)
        self.assertNotIn("glob('*.bak')",source)

    def test_actual_session_metadata_adapter_without_launch(self):
        sessions=self.root/'codex/sessions/2026/10/02'
        sessions.mkdir(parents=True)
        sid='fixture-session-id'
        path=sessions/('rollout-'+sid+'.jsonl')
        path.write_text(json.dumps({'type':'session_meta','payload':{'id':sid}})+'\n'
                        +json.dumps({'type':'turn_context','payload':{'model':'gpt-test'}})+'\n')
        stdout=json.dumps({'type':'thread.started','thread_id':sid}).encode()
        with patch.dict(os.environ,{'CODEX_HOME':str(self.root/'codex')},clear=True):
            self.assertEqual(runner.execution_identity(stdout),('gpt-test',sid))
            with path.open('a') as f:
                f.write(json.dumps({'type':'turn_context','payload':{'model':'gpt-fallback'}})+'\n')
            with self.assertRaisesRegex(C.GateError,'ambiguous'):
                runner.execution_identity(stdout)

    def test_non_regular_inputs_and_truncated_ledger(self):
        fifo=self.root/'fifo'
        os.mkfifo(fifo)
        with self.assertRaisesRegex(C.GateError,'non-regular'):
            C.read(fifo)
        self.approve(); self.purpose()
        path=self.directory/'runs.jsonl'
        path.write_bytes(path.read_bytes()[:-1])
        self.call('receipt','_example',ok=False)

    def test_recursive_allowed_output_globs(self):
        self.c['allowed_outputs']=['tasks/_example/outputs/**/*.txt']
        self.save(); self.normal()
        nested=self.directory/'outputs/nested'
        nested.mkdir()
        (nested/'evidence.txt').write_text('approved evidence\n')
        self.assertEqual(len(C.outputs(self.repo,self.c)),2)
        self.assertFalse(C.output_match('tasks/_example/outputs/nested/evidence.txt',
                                        'tasks/_example/outputs/*.txt'))
        (nested/'unapproved.md').write_text('not allowed\n')
        with self.assertRaisesRegex(C.GateError,'outside allowed_outputs'):
            C.outputs(self.repo,self.c)


if __name__=='__main__':
    unittest.main()

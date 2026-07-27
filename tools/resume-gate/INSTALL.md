# resume-gate 파일럿 한시 설치·제거

이 절차는 머신 전역 Claude Code managed settings를 설치한다. 설치된 동안
이 PC의 모든 Claude Code 세션이 resume-gate 정책을 적용받으므로, 파일럿은
반드시 **설치 → 파일럿 → 제거**의 한 묶음으로 운용한다. 상시 설치는 하지
않는다.

아래 명령은 문서화된 사용자 실행 절차다. 저장소 산출물 작성·시험 단계에서는
실행하지 않는다.

## 설치

기존 managed 파일이나 `/opt/coastal-resume`를 덮어쓰지 않고 즉시 중단한다.
판정 코드와 고정 입력은 저장소 원 디렉토리 구조를 유지한 채
`/opt/coastal-resume/lib/`에 root 소유 읽기 전용 파일로 설치한다.

```bash
set -euo pipefail

cd /home/firesinger/coastal-wiki

sudo test ! -e /etc/claude-code/managed-settings.d/50-coastal-resume.json
sudo test ! -e /etc/claude-code/managed-mcp.json
sudo test ! -e /etc/claude-code/.claude/agents/resume-coordinator.md
sudo test ! -e /etc/claude-code/.claude/agents/resume-code-reader.md
sudo test ! -e /etc/claude-code/.claude/agents/resume-pdf-reader.md
sudo test ! -e /opt/coastal-resume

sudo install -d -o root -g root -m 0755 \
  /etc/claude-code/managed-settings.d \
  /etc/claude-code/.claude/agents \
  /opt/coastal-resume/bin \
  /opt/coastal-resume/lib/engine \
  /opt/coastal-resume/lib/judge \
  /opt/coastal-resume/lib/validator \
  /opt/coastal-resume/lib/schemas \
  /opt/coastal-resume/lib/fixtures/pilot

sudo install -d -o root -g root -m 0555 \
  /opt/coastal-resume/empty

sudo install -o root -g root -m 0555 \
  tools/resume-gate/bin/resume-submit-mcp \
  /opt/coastal-resume/bin/resume-submit-mcp
sudo install -o root -g root -m 0555 \
  tools/resume-gate/bin/resume-pretool-guard \
  /opt/coastal-resume/bin/resume-pretool-guard
sudo install -o root -g root -m 0555 \
  tools/resume-gate/bin/resume-stop-gate \
  /opt/coastal-resume/bin/resume-stop-gate
sudo install -o root -g root -m 0555 \
  tools/resume-gate/bin/resume-run \
  /opt/coastal-resume/bin/resume-run

sudo install -o root -g root -m 0444 \
  tools/resume-gate/engine/__init__.py \
  /opt/coastal-resume/lib/engine/__init__.py
sudo install -o root -g root -m 0444 \
  tools/resume-gate/engine/core.py \
  /opt/coastal-resume/lib/engine/core.py
sudo install -o root -g root -m 0444 \
  tools/resume-gate/engine/mcp_server.py \
  /opt/coastal-resume/lib/engine/mcp_server.py
sudo install -o root -g root -m 0444 \
  tools/resume-gate/judge/adapter.py \
  /opt/coastal-resume/lib/judge/adapter.py
sudo install -o root -g root -m 0444 \
  tools/resume-gate/judge/prompt.fixed.txt \
  /opt/coastal-resume/lib/judge/prompt.fixed.txt
sudo install -o root -g root -m 0444 \
  tools/resume-gate/validator/validate.py \
  /opt/coastal-resume/lib/validator/validate.py

sudo install -o root -g root -m 0444 \
  tools/resume-gate/schemas/submission.schema.json \
  /opt/coastal-resume/lib/schemas/submission.schema.json
sudo install -o root -g root -m 0444 \
  tools/resume-gate/schemas/manifest.schema.json \
  /opt/coastal-resume/lib/schemas/manifest.schema.json
sudo install -o root -g root -m 0444 \
  tools/resume-gate/schemas/judge.schema.json \
  /opt/coastal-resume/lib/schemas/judge.schema.json
sudo install -o root -g root -m 0444 \
  tools/resume-gate/schemas/decision.schema.json \
  /opt/coastal-resume/lib/schemas/decision.schema.json

sudo install -o root -g root -m 0444 \
  tools/resume-gate/fixtures/pilot/manifest.frozen.json \
  /opt/coastal-resume/lib/fixtures/pilot/manifest.frozen.json
sudo install -o root -g root -m 0444 \
  tools/resume-gate/fixtures/pilot/canary-fabricated-claim.submission.json \
  /opt/coastal-resume/lib/fixtures/pilot/canary-fabricated-claim.submission.json
sudo install -o root -g root -m 0444 \
  tools/resume-gate/fixtures/pilot/parser-negative-duplicate-source.manifest.json \
  /opt/coastal-resume/lib/fixtures/pilot/parser-negative-duplicate-source.manifest.json

sudo install -o root -g root -m 0444 \
  tools/resume-gate/policy/agents/resume-coordinator.md \
  /etc/claude-code/.claude/agents/resume-coordinator.md
sudo install -o root -g root -m 0444 \
  tools/resume-gate/policy/agents/resume-code-reader.md \
  /etc/claude-code/.claude/agents/resume-code-reader.md
sudo install -o root -g root -m 0444 \
  tools/resume-gate/policy/agents/resume-pdf-reader.md \
  /etc/claude-code/.claude/agents/resume-pdf-reader.md
sudo install -o root -g root -m 0444 \
  tools/resume-gate/policy/managed-mcp.json \
  /etc/claude-code/managed-mcp.json

sudo install -o root -g root -m 0444 \
  tools/resume-gate/INSTALL-MANIFEST.sha256 \
  /opt/coastal-resume/INSTALL-MANIFEST.sha256

sudo install -o root -g root -m 0444 \
  tools/resume-gate/policy/50-coastal-resume.json \
  /etc/claude-code/managed-settings.d/50-coastal-resume.json

cd /
sudo sha256sum -c /opt/coastal-resume/INSTALL-MANIFEST.sha256
sudo test -z "$(sudo find /opt/coastal-resume \( ! -user root -o ! -group root -o -perm /022 \) -print -quit)"
```

설치 직후 새 일반 셸에서 다음을 확인한 뒤 파일럿을 시작한다.

```bash
claude /doctor
claude mcp list
```

`claude mcp list`에는 managed `resume-submit`만 보여야 한다. 설치본 wrapper는
`/opt/coastal-resume/lib/engine/mcp_server.py`를 실행하며 저장소 판정 코드
경로로 되돌아가는 fallback이나 환경변수 override가 없다.

## 제거와 원상 확인

파일럿 종료 직후 다음을 실행한다. managed 설정과 managed MCP를 먼저 제거해
머신 전역 제한을 해제하고, 이 절차가 설치한 정확한 파일과 전용 디렉토리만
제거한다.

```bash
set -euo pipefail

sudo rm -f \
  /etc/claude-code/managed-settings.d/50-coastal-resume.json \
  /etc/claude-code/managed-mcp.json

sudo rm -f \
  /etc/claude-code/.claude/agents/resume-coordinator.md \
  /etc/claude-code/.claude/agents/resume-code-reader.md \
  /etc/claude-code/.claude/agents/resume-pdf-reader.md

sudo rm -f \
  /opt/coastal-resume/bin/resume-submit-mcp \
  /opt/coastal-resume/bin/resume-pretool-guard \
  /opt/coastal-resume/bin/resume-stop-gate \
  /opt/coastal-resume/bin/resume-run \
  /opt/coastal-resume/lib/engine/__init__.py \
  /opt/coastal-resume/lib/engine/core.py \
  /opt/coastal-resume/lib/engine/mcp_server.py \
  /opt/coastal-resume/lib/judge/adapter.py \
  /opt/coastal-resume/lib/judge/prompt.fixed.txt \
  /opt/coastal-resume/lib/validator/validate.py \
  /opt/coastal-resume/lib/schemas/submission.schema.json \
  /opt/coastal-resume/lib/schemas/manifest.schema.json \
  /opt/coastal-resume/lib/schemas/judge.schema.json \
  /opt/coastal-resume/lib/schemas/decision.schema.json \
  /opt/coastal-resume/lib/fixtures/pilot/manifest.frozen.json \
  /opt/coastal-resume/lib/fixtures/pilot/canary-fabricated-claim.submission.json \
  /opt/coastal-resume/lib/fixtures/pilot/parser-negative-duplicate-source.manifest.json \
  /opt/coastal-resume/INSTALL-MANIFEST.sha256

sudo rmdir \
  /opt/coastal-resume/lib/fixtures/pilot \
  /opt/coastal-resume/lib/fixtures \
  /opt/coastal-resume/lib/schemas \
  /opt/coastal-resume/lib/validator \
  /opt/coastal-resume/lib/judge \
  /opt/coastal-resume/lib/engine \
  /opt/coastal-resume/lib \
  /opt/coastal-resume/bin \
  /opt/coastal-resume/empty \
  /opt/coastal-resume

sudo test ! -e /etc/claude-code/managed-settings.d/50-coastal-resume.json
sudo test ! -e /etc/claude-code/managed-mcp.json
sudo test ! -e /opt/coastal-resume

claude /doctor
claude mcp list
```

제거 후 `claude mcp list`에는 `resume-submit`이 없어야 하며, `/doctor`에서
resume-gate managed 정책이 남아 있다고 보고하지 않아야 한다.

설치와 제거 어느 쪽에도 `models/`·`corpus/`를 대상으로 하는 `chmod`,
`chown`, 생성, 삭제 또는 내용 변경 명령은 없다. 두 트리의 기존 잠금은
그대로 유지한다.

# RUNS-CHANNEL — 계산결과 → experience 채널 계약

> **목적**: 모델 실행 결과(개인 run)를 위키에 직접 넣지 않고([절대규칙 #8](CLAUDE.md)), 별도 `coastal-runs` repo에 축적한 뒤 **3조건 게이트**를 통과한 것만 위키 `experience/`로 promote하기 위한 양쪽-머신 공유 계약. 계산 머신은 이 문서를 위키 pull로 읽는다.
> **설계 원칙**: repo마다 writer 하나 → divergence 구조적 불가. 위키는 이 PC로 들어오기만(리더 쪽) / 나가기만(writer 쪽), run은 반대 방향.

## 1. 아키텍처 · 머신 역할

```
[coastal-wiki writer PC]  wiki 생산 ──push──▶ GitHub ──pull──▶ [계산 PC] 실행 시 참조
[계산 PC = writer PC 겸 다른 계산 PC]  runs 생산 ──push──▶ GitHub ──pull──▶ [wiki writer PC] 게이트 → experience/
```

| repo | 유일 writer | 다른 머신 |
|---|---|---|
| `coastal-wiki` | **wiki writer PC 1대** | pull 전용(리더) |
| `coastal-runs` | 각 머신이 **자기 `runs/<host>/` 서브트리만** | 서로의 서브트리 미편집 |

- **절대 규칙**: *한 파일을 두 머신이 편집 금지.* 위키=writer PC만, runs=머신별 `<host>` 서브트리(또는 머신별 repo).
- writer PC가 계산도 겸할 수 있음("writer"는 repo 단위 역할). 그 경우에도 `coastal-wiki`와 `coastal-runs`는 **물리적으로 분리된 디렉토리**로 두고, run 출력은 위키 repo에 절대 넣지 않는다(#8).

## 2. 【계산 머신 지시】 `coastal-runs` 생산 규약

계산 머신(들)이 따르는 부분. writer PC는 이 섹션을 읽기만.

### 2.0 신규 계산머신 부트스트랩 (SSOT — README 는 이 절 링크만)

새 계산 머신 1회 세팅 체크리스트. 순서 고정.

1. **접근·환경 확인**: `ssh -T git@github.com` + 두 repo(coastal-wiki·coastal-runs) fetch/push 권한 · `git config user.name/user.email` · `core.autocrlf`(WSL/Linux `input` 권장) · 시간대/NTP 동기(UTC epoch 재현성) · 디스크 여유.
2. **위키 리더 세팅**: `git clone` coastal-wiki → `~/coastal-wiki` → `bash tools/install-hooks.sh --reader` + `git config pull.ff only` → **동작 실측 2건**: (a) 임의 커밋 시도가 pre-commit 에서 거부되는지 (b) `git pull` 후 post-merge 재색인 메시지가 나오는지.
3. **검색 레이어 확인**: `python3 -c "import sqlite3; sqlite3.connect(':memory:').execute(\"CREATE VIRTUAL TABLE t USING fts5(a)\")"` (FTS5 실확인) + MCP smoke — initialize/`wiki_search`/`wiki_manifest` 응답 확인(§2.4 의 `.mcp.json` 경유 또는 stdio 직접).
4. **coastal-runs 세팅**: `git clone` coastal-runs → **`git config pull.rebase true` 실설정**(§2.3 push 규율의 전제 — 미설정 시 조용한 merge 커밋 드리프트) → `bash tools/install-hooks.sh --host-id <id>` 로 훅 설치(**`--host-id` 명시 지정** — hostname 직접 사용 금지, 역할은 `git rev-parse --git-path runs-role` 파일에 기록, 기존 `runs/<id>/` 충돌 검사) → 자기 `runs/<host_id>/`·`observations/<host_id>/` 생성.
5. **계산 프로젝트 배선**: 각 계산 프로젝트에 §2.4 적용(로컬 `.mcp.json` 생성 + CLAUDE.md managed block).
6. **모델 실행환경은 별도**: 모델 실행파일·MPI·컴파일러·DLL 세팅은 이 절의 범위 밖 — "모델별 후속 bootstrap"으로 분리(모델·프로젝트 문서 몫).

### 2.1 repo 구조
```
coastal-runs/
  runs/<host>/<model>/<case>/<YYYY-MM-DD>/
      setup/            # 입력·설정 파일 (fort.15, .inp, .mdf, config …)
      metrics/          # 추출 지표 (peak, RMSE, 시계열 요약 CSV/JSON)
      figures/          # 그림 (png)
      manifest.sha256   # 대용량 원출력(바이너리)의 해시 목록 (파일 자체는 git 밖)
  observations/<host>/<slug>.md   # 관찰 노트 (아래 스키마)
```
- **대용량 바이너리 출력(fort.63, maxele, netcdf …)은 git에 넣지 않는다.** 디스크 보관 + `manifest.sha256`(경로+해시)만 커밋. 재현은 setup/ + sha로.
- run 산출물은 append-only. 기존 run 디렉토리를 나중에 수정하지 않는다.

### 2.2 관찰 노트 스키마 (experience 3조건에 1:1 매핑)
```yaml
---
model: EFDC | ROMS | Delft3D | SWAN | SWASH | ADCIRC | XBeach | SFINCS | custom-ML(<한줄 설명>) | ...  # 물리모델 외 ML emulator·커스텀 코드도 허용 — custom-ML 은 설명 필수 (P0 F1, 2026-07-17)
version: "12.4 (sha 3ed76b6)"        # 모델 버전 — 재현성
case: <케이스명>                       # 예: jpm-rmax-sigma
host: <계산머신 hostname>
date: 2026-07-06
evidence:                             # ★객관 데이터 근거 파일 (repo-상대 경로)
  - runs/<host>/EFDC/<case>/2026-07-06/metrics/peak.csv
repeat_count: 1                       # ★반복 관찰 횟수 — 독립 케이스만 계수. 동일 설정 단순 재실행 = 1회(2026-07-12 Codex). ★autoresearch/최적화 루프 내 N회 실험도 동일 데이터셋이면 1 케이스 — 독립 계수는 다른 기간·정점군·도메인일 때만 (P0 F3, 2026-07-17)
reproducible: true                    # ★setup/+sha로 재현 가능? 결손 시 false + 사유(허위 재현성 금지)
status: draft-observation             # 계산머신은 항상 draft. verified 부여 금지(=writer 몫)
wiki_ref: "coastal-wiki@<sha> models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md §4"  # ★setup 근거로 인용한 위키 노트 — 커밋 sha+경로·절 고정(노트 개정 드리프트 방지, 2026-07-12). ★위키 무인용(탐색적) 셋업은 "none (탐색적 — 근접 canonical: <경로>)" 로 명시 — 공란 금지 (P0 F2, 2026-07-17)
exec:                                 # ★재현성 증거 (manifest.sha256 은 존재 증명일 뿐 — 재생성 정보, 2026-07-12)
  cmd: "<실행 명령>"
  model_sha: "<모델 binary/source sha>"
  env: "<컴파일러·MPI·OS 요지>"
  forcing_version: "<forcing/관측자료 버전·접근 식별자>"
gate:                                 # writer PC 게이트 기록 (계산머신은 비움)
  reviewer: ""                        # 승격 최종 책임 = 사용자
  verdict: ""                         # promote | hold | reject
  date: ""
  reason: ""
wiki_feedback:                        # 선택 — run→wiki 피드백 채널 (Codex 22회차 최소형). 없으면 필드 생략.
  - id: <host_id>-<YYYYMMDD>-<slug>-NNN   # 원장 대조 키 — repo 전역 유일
    type: gap | suspected-error | promote-candidate
    destination: canonical | experience
    target_ref: "coastal-wiki@<sha> <경로> §<절>"   # 대상 문서가 아예 없는 gap 은 "unresolved"
    evidence: [runs/<host>/.../metrics/...]
    note: "<한 줄>"
---

## 관찰
<무엇을 봤나 — 1~3문장. 예: "EFDC v12.4에서 WSER 성분입력(u/v)이 안 먹고 speed/dir만 반영됨.">

## 근거
<evidence 파일의 어느 수치/그림이 이를 뒷받침하나.>

## 재현
<setup/ 어느 파일 + 어떤 실행으로 재현되나.>
```
- **`status`는 계산 머신에서 항상 `draft-observation`.** `verified`·`citation_status: verified`는 절대 부여하지 않는다(객관화 판정 = writer PC의 몫).
- **`wiki_feedback` 규칙**: 계산 머신은 피드백을 *제기*만 한다 — 위키 반영 여부·방식은 writer 게이트(§3.3). 특히 `type: suspected-error` 는 **G8 독립 소스 확인 성공 후에만** 위키 canonical 에 반영(역방향 계약 §3.1 유지 — run 결과 자체는 소스 근거가 아님). id 는 발급 후 불변(원장 대조 키).

### 2.3 push 규율 (단일 repo + 호스트 네임스페이스인 경우)
1. `git pull --rebase` (push 직전)
2. **자기 `runs/<host>/`·`observations/<host>/` 서브트리만** add/commit
3. `git push`
- run 산출물은 비겹침이라 rebase는 항상 clean. 남의 `<host>` 서브트리는 절대 건드리지 않는다.
- (대안: 머신별 `coastal-runs-<host>` repo면 rebase도 불요.)

### 2.4 계산 프로젝트 배선 — wiki 소비 표준 (managed block 원본 = 이 절 1곳)

계산 프로젝트(예: `~/khoa_tide/`, `/mnt/d/SURGE/`)마다 아래 2개를 배선한다.

**(a) 로컬 `.mcp.json` 생성** — 개인 절대경로는 커밋하지 않는다(프로젝트 repo 가 있으면 `.mcp.json` 을 gitignore 하거나 로컬 전용으로 유지). WSL Claude 런타임 기준:

```json
{
  "mcpServers": {
    "coastal-wiki": {
      "command": "bash",
      "args": ["-c", "cd \"${COASTAL_WIKI_ROOT:-$HOME/coastal-wiki}\" && exec python3 tools/llm-wiki-poc/mcp_server.py"]
    }
  }
}
```

**(b) 계산 프로젝트 CLAUDE.md 에 managed block 부착** — 원본은 아래 블록(버전 마커 포함) 하나뿐이며, 각 프로젝트에는 **그대로 복사**한다(문구 개정은 여기서만 → 마커 버전 올리고 재배포 — 드리프트 방지).

```markdown
<!-- coastal-wiki:consumer-block:v1 -->
## coastal-wiki 소비 규칙 (원본: coastal-wiki/RUNS-CHANNEL.md §2.4 — 여기서 직접 수정 금지)
1. 위키 clone(`~/coastal-wiki`)은 **read-only** — 모델 셋업·본문 편집 금지(위키 편집 = writer PC 위키 세션 몫).
2. 세션 시작 시 `git -C ~/coastal-wiki pull --ff-only` + working tree clean 확인(리더 머신).
3. 근거 탐색은 `wiki_search(status="verified")` 부터.
4. 히트의 disclosed-gap 라벨(⚑/✓/?) 확인 후 `wiki_read` 로 해당 절 정독(스니펫만으로 인용 금지).
5. `wiki_manifest` 의 **`fresh=true` 이고 `dirty_working_tree=false`** 인 `git_sha` 만 `wiki_ref` 로 인용.
6. **모델 실행·입력파일 편집은 계산 프로젝트/coastal-runs 에서만** — 위키 세션에서 하지 않는다(세션 역할 경계).
<!-- /coastal-wiki:consumer-block -->
```

## 3. 【라이터 PC 절차】 `coastal-runs` → `experience/` promote 게이트

wiki writer PC(이 PC)만 수행. `coastal-runs`를 **읽기 전용**으로 pull. **pull 직후 `python3 tools/scan-runs-feedback.py` 1회**(§3.3 — 미처리 피드백 유무 확인).

### 3.1 3조건 게이트 (전부 충족 시에만 promote — 2026-07-12 Codex 반영 구체화)
[CLAUDE.md 절대규칙 #2]:
1. **반복 관찰** — **독립 케이스 최소 2건**(동일 설정 단순 재실행은 1회로 계수). 1회성은 대기.
2. **객관 데이터 근거** — `evidence` 파일의 수치/그림이 실재하고 단언을 뒷받침 — **사람이 파일 직접 확인**(자기선언 불충분).
3. **재현 가능** — `reproducible: true` + setup/ + `exec` 필드(명령·model_sha·환경·forcing 버전)로 제3자 재현 가능. 결손분은 복원하지 말고 `false`+사유.
- 미충족 = **버리지 않고 runs repo에 대기**(반복 관찰이 쌓일 때까지). 판정은 `gate:` 필드에 reviewer·verdict·사유 기록 — **최종 승격 책임 = 사용자**.
- **phase 기술적 완료 ≠ 승격**: 계산 phase 는 산출물 체크로 완료 가능, experience 승격은 본 게이트 별도(1회 파일럿이 phase 를 막지 않음).
- **역방향(runs→canonical) 게이트**: run 에서 발견한 버그·미문서 거동은 **소스코드로 독립 확인 성공 시에만** models/ SA 노트 반영(G8). 소스 확인 실패분은 runs/experience 에만.

### 3.2 promote 작성
- 통과분만 `experience/<topic>.md` 정식 작성. `citation_status`는 근거 확인 후 부여(자동 `verified` 금지 — [coastal-promote](CONVENTIONS.md) 패턴).
- **출처 인용 형식**: `coastal-runs@<sha> runs/<host>/<model>/<case>/<date>/` + 구체 근거파일. run 결과의 로컬 절대경로·머신-특정 수치는 canonical(concepts/models/textbook)에 두지 않는다(#8).
- 위키 무결성: experience 노트도 frontmatter·[[wikilink]]·validator 통과.

### 3.3 run→wiki 피드백 처리 (acknowledgment 원장)

§2.2 `wiki_feedback` 항목의 writer 측 처리 절차.

- **원장** = `coastal-wiki/_staging/runs-feedback/ledger.yml` (위키 repo — writer 만 기록). 항목당:
  ```yaml
  - feedback_id: <관찰노트의 wiki_feedback id>
    source_ref: "coastal-runs@<sha> observations/<host>/<slug>.md"
    verdict: accepted | deferred | rejected
    result_ref: "<반영 커밋/문서 경로, deferred/rejected 는 사유 한 줄>"
    date: YYYY-MM-DD
  ```
- **스캐너** `tools/scan-runs-feedback.py --runs-root <coastal-runs 경로>`: coastal-runs 관찰노트의 `wiki_feedback` id 중 **원장에 없는 것만** 출력(무상태 — rg 수동 검색 대체, report-only).
- **원 observation 은 수정하지 않는다** — writer 는 coastal-runs read-only(§1 소유권). 처리 상태의 SSOT 는 원장 하나.
- 반영 규칙: `promote-candidate` → §3.1 3조건 게이트 / `suspected-error` → **G8 독립 소스 확인 후에만** canonical 반영 / `gap` → writer 판단으로 canonical 보강 또는 deferred.

## 4. 재발 방지 (오늘의 divergence 교훈)
- 각 repo에 writer 하나 → 두 머신이 같은 repo 같은 파일을 push할 일이 없음.
- 리더 머신(위키를 pull만 하는 쪽)은 `git config pull.ff only` — 로컬 커밋이 생기면 pull이 조용한 merge 대신 즉시 에러.
- 관련: [CLAUDE.md](CLAUDE.md) 동기화 §, [BOUNDARY.md](BOUNDARY.md), 절대규칙 #5(단일 writer)·#8(위키=케이스 공급원).

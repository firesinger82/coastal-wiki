# 세션 재개 지침 (다음 세션에서 이것부터 읽을 것)

> ★2026-08-27 최신: **code·note 재판독 310/310 완결** + **맹검 감사 269/269 전수 완료**(Codex).
> 병합 설계 확정(오버레이+delta 승격). **다음 = crosswalk 파일럿(EFDC-000)** — 진입점은
> [CROSSWALK-HANDOFF.md](CROSSWALK-HANDOFF.md). 감사·설계 경위 [SESSION-LOG.md](SESSION-LOG.md) 2026-08-26~27,
> [MERGE-PLAN-20260827.md](MERGE-PLAN-20260827.md), [workorders/WO-20260728-amendment-04.md](workorders/WO-20260728-amendment-04.md).

> 상태 스냅샷: **2026-07-28** / semantic 후보 canonical key **22,269 / 71,143 (31.3%)** (중복 640행 미해소 — canonical 선택은 감사 6단계에서)
>
> ⚠️ **처분 실행(2026-07-28, 사용자 승인)**: [METHOD-AUDIT-20260724.md](METHOD-AUDIT-20260724.md) §2 처분안 실행 완료 —
> EFDC·FUNWAVE·LISFLOOD-FP 의 구조 인덱스 3파일 2,248행을 `records-structural/20260724/` 로 **강등·격리**(해시 검증 이동 + manifest.json + 필드 정규화 v2), 비어 있지 않은 텍스트 **2,238건 재판독 큐 복귀**(`reread-queue/`, FUNWAVE 0-byte 10건은 mechanical 예외), 생성기 4개 격리 가드 삽입, SPEC.md 스키마 v2·완결 게이트 추가, status.sh canonical key 집계로 교정.
> **"완결 10모델"은 철회** — 현재 상태는 "10모델 완료 주장 보류, 전 corpus 방법 감사 진행 중"이다. 앞선 7모델(CADMAS-SURF·Celeris·SWAN·XBeach·SFINCS·ShorelineS·SWASH)도 script-산 확정·구조-only 의심 레코드가 섞여 있어(감사 §3 표) **완결 게이트 재통과 전 "재판독 불필요" 지시 금지**.
> 배경·경위는 [SESSION-LOG.md](SESSION-LOG.md), 규격은 [SPEC.md](SPEC.md)(★스키마 v2·완결 게이트 포함), 코퍼스 고정은 [PROVENANCE.md](PROVENANCE.md).

## 지금 하는 일 (한 줄)

사용자 지시: **"판단하지 말고 모든 코드·매뉴얼·웹정보·크롤링분을 전부 읽고 읽은 결과를 저장"**.
분석·중요도 판정은 **판독 완료 후** 별도 단계. 지금은 오직 읽고 기록만 한다.

## 재개 절차

```bash
bash /home/firesinger/coastal-wiki/_staging/total-read/status.sh    # 진척 확인
ls /home/firesinger/coastal-wiki/_staging/total-read/shards/txt_all_*   # 잔여 샤드
```

**중복 방지**: 샤드 투입 전 반드시 기존 레코드의 `path` 와 대조해 이미 판독된 파일은 건너뛴다.
경로 비교 시 `models/` 접두 유무를 **정규화**할 것(벤더마다 표기가 다름 — 이것 때문에 한 번 오판했다).

```python
def norm(p):
    p = p.replace('/home/firesinger/coastal-wiki/','')
    return p[7:] if p.startswith('models/') else p
```

## 잔여 (우선순위 순)

| 순위 | 모델 | 진척 | 잔여 | 비고 |
|---|---|---|---:|---|
| 1 | **ADCIRC** | 3,048/10,687 | 7,639 | `txt_all_ADCIRC_*` (219샤드) |
| 2 | **ROMS** | 2,457/11,661 | 9,204 | `txt_all_ROMS_*` (263샤드). WRF 4,744 포함 |
| 3 | **Delft3D** | 1,154/31,187 | 30,033 | `txt_all_Delft3D_*` (859샤드). 최대 난관 |

| 0 | ✅ **code·note·doc-002 재판독 — 310/310 완결** (2026-08-25) | 310/310 | 0 | 08-11 미처분 건 종결. §5.2 무관용 → 310건 격리 완료(`pending-superseded/20260813-namerule/`). 원인은 프롬프트 v3 29↔31행 자기모순(창작 라벨 0건). **게이트 v5**·**프롬프트 code-v4**(`13b91717…`). **8 shard 전량 완결**(note-000·code-001/002/003/004·doc-002·FUNWAVE-000·EFDC-000). pending 690건 validator v5 결함 0, 각 shard 5종 검증 전건 통과. EFDC `mod_var_global.f90`(07 기각 원인) 재판독 완료로 '완결 10모델' 철회 원인 해소. 후속: 맹검 224표본·완결 게이트 7항(WO §5-§6 외부 게이트). 규격 [WO-20260728-amendment-03.md](workorders/WO-20260728-amendment-03.md), 경위 [SESSION-LOG.md](SESSION-LOG.md) 2026-08-13 |
| 0 | ✅ **doc/FUNWAVE 421 완주** (2026-08-11) | 421/421 | 0 | shard 11개, validator 전수 결함 0, 큐 대조 누락·중복 0. 전량 pending(맹검 미실시). 게이트 **v4**·프롬프트 **doc-v2**(`6cf7a860…`) 체제. 폐기 282건은 `pending-superseded/20260811-{modelid,anchorrule}/` 에 매니페스트와 함께 보존 |
| 4 | **재판독 큐 semantic** (code 679·doc 991·web 145·note 68) | 132/1,883 | 1,751 | §5.1 통과: EFDC-000(6)·FUNWAVE-000(49)·FUNWAVE-001(49) pending / 진행: FUNWAVE-002 17/49·003 11/48·004 미개시 (★07-29 월한도 중단, 사용자 지시: FUNWAVE 까지만 하고 중단). WO+부속서01 체제, ★구조 인덱스 **미열람** 판독. 재개: state/reread-20260728/ 의 002·003 run 이어받기 |

~~완결 10모델~~ → **철회(2026-07-24 진단·07-28 처분)**: 어떤 모델도 완결 아님. 완결 재표기는 SPEC.md 완결 게이트 7조건 전부 통과 후에만. 앞선 7모델의 script-산/구조-only 분류는 METHOD-AUDIT-20260724.md §3 표 참조 (감사 8단계 절차 진행 대상).

### EFDC·FUNWAVE·LISFLOOD-FP 구조 인덱스 생성 경위 (2026-07-24 — ⚠판독 아님, 07-28 강등·격리됨)
- **EFDC** 잔여 182(confluence JSON·f90·md): **결정론적 이미터**(`helpers/rest_efdc_codex_totalread_20260721.py`)로 구조 인덱스 생성 — sha256sum·wc 실측 + 라인앵커 충실 파싱(창작 0). 드라이버 `emit_rest_efdc_final_20260724_9c4e.py`.
- **FUNWAVE** 잔여 974: 같은 이미터를 **MATLAB/Python 엔티티 열거로 확장** + latin-1 폴백(ISO-8859 3건). `emit_funwave_final_20260724_b7d1.py`.
- **LISFLOOD-FP** 잔여 1,092(C/C++/CUDA .h/.cpp/.cu/.cuh 430·데이터·par/asc/bci 645·기타): **C/C++/CUDA 파서 추가**(base 는 .h 를 Fortran 으로 오판 → 오버라이드). 함수/struct/class/enum/namespace/#define 라인앵커 열거. `emit_lisflood_final_20260724_e3a9.py`. 바이너리 36(exe/xls/docx/pdf)는 기(旣) mechanical-sweep 완료·PDF 는 doc-extracted 로 별도 판독됨.
- 공통: 샤드 아닌 **잔여-파일 목록** 구동(NUL-구분 find — 공백 파일명 대응), 기존 레코드 미접촉·중복파일 0. **검증**: 스키마/금지필드/앵커결측 0, 표본(각 12~15) 독립 재실측 전건 일치, 앵커 실재 대조 통과. 미판독은 `.git/` 내부·기스윕 바이너리뿐(범위 외).

## 벤더 배정 (실측 판정 결과 — 바꾸지 말 것. ★단, [SPEC.md](SPEC.md) "역할 배정" 축별 표가 이 일반 표보다 우선: code 1차 Claude/맹검 Codex · doc 1차 Codex/맹검 Grok · web 1차 Grok/맹검 Claude. Claude 독단 완료선언·대량편집 금지)

| 벤더 | 용도 | 호출 |
|---|---|---|
| **Codex** ✅ | 코드·문서·노트 주력 | `node ~/.claude/plugins/cache/openai-codex/codex/1.0.4/scripts/codex-companion.mjs task --background --write "<프롬프트>"` |
| **Claude** ✅ | 코드·노트 | Agent 툴, `model: opus` 지정 |
| **Grok** — | **웹축 전용** | `bash _staging/total-read/run_wave.sh web <모델> <샤드번호...>` |
| ~~Antigravity~~ ❌ | **제외** | sha256 날조 2회 |

## 재판독 완결표 (2026-08-25 — 8 shard 310/310 전량 완결)

★**판독자는 한 번에 1명만 투입한다** (2026-08-13 사용자 지시). 8 shard 전량 순차 완주 완료.
아래 표는 완결 기록. 후속 total-read 대형 3모델(ADCIRC·ROMS·Delft3D)은 상단 "잔여" 표 참조.

| shard | run_id | 수납 | 재개 파일 |
|---|---|---:|---|
| note-FUNWAVE-000 | `…-fable5-20260813T005226Z-b33d4276` | **20/20 완료·검증필** | — |
| code-EFDC-000 | `…-fable5-20260813T012841Z-5799640f` | **6/6 완료·검증필** | — (mod_var_global 07기각 원인 해소) |
| code-FUNWAVE-000 | `…-fable5-20260813T012841Z-2131dcc5` | **49/49 완료·검증필** | — |
| code-FUNWAVE-001 | `…-fable5-20260813T012841Z-2ec7b3b5` | **49/49 완료·검증필** | — |
| code-FUNWAVE-002 | `…-fable5-20260813T012841Z-ff3d40e9` | **49/49 완료·검증필** | — |
| code-FUNWAVE-003 | `…-fable5-20260813T012841Z-7a6fa701` | **48/48 완료·검증필** | — |
| code-FUNWAVE-004 | `…-fable5-20260813T012841Z-cf6786b6` | **48/48 완료·검증필** | — (4배치 이어받기) |
| doc-FUNWAVE-002 | `…-codex-20260813T012841Z-68f0ed11` | **41/41 완료·검증필** | — (input.txt SLP@L31·PLOT_INTV@L48 교정 확인) |

재개 순서 권장: FUNWAVE-000(41파일 11,621행) → EFDC-000(5파일 17,556행, 파일당 3,500행) →
FUNWAVE-004(38파일 28,459행, 최대). 잔여는 전부 Claude 축이라 세션 한도를 나눠 써야 한다.
★중단은 **파일 경계에서**(submit 직후) — ack 후 레코드 없이 끊기면 그 판독분은 통째로 버려지고
`reset_file_state.py` 로 chunk 0 초기화가 필요하다(08-13 에 4회 발생).
**부분 ack 파일은 게이트가 chunk 0 부터 재서빙**한다(부분판독 승계 금지) — 004 의 fluxes_33v.F 해당.
code·note 는 프롬프트 **code-v4**(`13b91717…`, reader `anthropic/claude-fable-5`),
doc 는 **doc-v2**(`6cf7a860…`, reader `openai/gpt-5.6-sol` — rollout 실측값).

## 2026-08-13 이후 필수 (게이트 **v5** · 프롬프트 code-**v4** / doc-v2)

- **code·note 축 프롬프트는 v4 다** — `prompt-code-claude-v4.md` (`13b91717…`) = v3 전문 + 부속서01-code.
  v3 를 그대로 쓰면 안 된다(29↔31행 모순이 게이트 v5 와 양립 불가).
- **게이트 v5**: name 전체 문자열이 앵커 줄에 경계 포함 실재(N1) + 순수 수치 리터럴 name 금지(N2).
  부분문자열 통과(`DT` @ `DTMAX = 1.0`)와 다토큰 업기(`DATA column_1`)를 막는다.
- 이름 없는 수치는 **부속서 A-2** 경로 — `verbatim_spans` 원문 + `what_it_is` 서술, `constants` 빈 배열 허용.
  단 앵커 오류를 항목 삭제로 무마하는 것은 금지(C-2).
- 게이트가 검사하는 필드는 `constants`·`params_defined`·`equations` **뿐**이다.
  `calls`·`io`·`entities`·`verbatim_spans` 앵커는 게이트 미검사 — 자가대조·맹검 소관(B-2).

## 2026-08-11 이후 필수 (게이트 v4 · 프롬프트 doc-v2)

- **트리 잠금**: 세션 사이 `_staging/total-read` 는 root 소유 읽기전용이다. 재개 시
  `sudo chown -R firesinger:firesinger _staging/total-read && sudo chmod -R u+w _staging/total-read`,
  종료 시 `sudo chown -R root:root … && sudo chmod -R a-w …`. 코퍼스 `models/` 는 계속 read-only.
- **model-id 는 자기신고를 믿지 말 것**: 판독자가 계열명(`gpt-5`)을 자기 ID 로 적어 203건을 폐기했다.
  실측은 `grep -o '"model":"[^"]*"' ~/.codex/sessions/<날짜>/rollout-*.jsonl | head -1`.
  프롬프트에 실측 ID 를 박아 주고, 완료 후 `validate_pending_20260811.py --expect-reader` 로 대조한다.
- **검증은 shard 완주마다**: `python3 validate_pending_20260811.py "<run-glob>" --expect-reader <vendor/model>`.
  게이트 submit 을 통과해도 이 검증기가 잡는 결함이 있다(있었다).
- **판독자 중단 시**: 새 init 금지. 같은 run_id 로 이어받기 프롬프트를 투입한다
  (`codex-doc-continue-template.md` 계열). 부분 ack 파일은 게이트가 chunk 0 부터 재서빙한다.

## 프롬프트 필수 문구 (누락하면 규격 위반이 난다)

실제로 이걸 빼먹어서 Claude 초기 레코드 379건에 `read_range` 가 결측됐고, Grok 코드축 200건은 통째로 격리됐다.

```
★path 는 models/ 접두 없이 샤드에 적힌 그대로.
★sha256 은 sha256sum 실측, lines_or_pages 는 wc -l 실측 — 반드시 실제 명령 실행값만.
  추정·생성 금지(다른 벤더가 해시를 창작해 80건 폐기됨).
★read_range 는 실제 읽은 범위. 끝까지 안 읽었으면 complete 금지, partial + 범위 정직 기록.
★entities 는 선언된 subroutine/function/module/class 전부 열거.
★constants·params_defined 는 각각 라인번호 필수.
★판단·중요도 필드(note_worthy·importance·tier·core) 생성 절대 금지.
★헬퍼 스크립트를 만들면 파일명을 유일하게(동시 실행 충돌 방지).
★파일 끝 개행이 없으면 wc -l 이 1 작다 — 실제 행수 기준으로 기록.
```

## 운영상 주의

- **병렬 폭 6~8 유지.** 12까지 올렸다가 서버 rate limit(`not your usage limit`)이 연속 발생했다.
- 하위 에이전트를 재귀 스폰하면 rate limit 이 더 잘 난다 — 재투입 프롬프트에 "직접 순차 판독하라" 명시.
- 바이너리는 LLM 에 보내지 말 것. `binary_sweep.py` 로 해시·MIME 기계 기록(이미 10,786건 처리).
  ```bash
  python3 _staging/total-read/binary_sweep.py _staging/total-read/shards/inv_<축>_<모델>.txt <모델> /home/firesinger/coastal-wiki/models
  ```
- 인벤토리는 **확장자 allowlist 금지**. EFDC 에서 이 방식 때문에 8,884건이 누락됐다(전 파일 나열 후 후분류).

## 검증 (레코드 수령 시마다)

1. 인벤토리 대조 — 미판독 0 인가(경로 정규화 후)
2. `read_range` 결측 / 라인 앵커 결측 / 금지 필드 / JSON 유효성
3. 표본 원본 대조 — 행수·sha256 실측 재계산, 앵커가 그 줄에 실재하는가

★**자기 보고를 믿지 말 것.** 오늘 걸린 것 전부(해시 날조·허위 complete·인용 오귀속)가 대조에서만 나왔다.

## 판독 완료 후 할 일 (아직 안 함)

1. 기존 위키 노트 467건 ↔ 판독 레코드 **역대조** — 노트 주장이 원문과 맞는지
2. 교차 검증(자기 축 자기 감사 금지): code→Codex, doc→Grok, web→Claude
3. `AUDIT-LEDGER.md`·README 의 "전수 검수 완료"·"13/13 종결" 표현 정정
4. upstream 대조(로컬 코퍼스가 원본 전량인지) — 현재 미검증, disclosed

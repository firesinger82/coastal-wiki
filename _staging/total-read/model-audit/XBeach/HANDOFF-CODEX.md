# XBeach 감사 인수인계서 (Claude → Codex)

작성 2026-09-09 · 기준 커밋 `351022e` · 작성자 Claude(Opus 5), 이전 공정 수행자

---

## 1. 지금 상태 한 줄

**XBeach 트리 전량 456파일 판독 완주(미판독 0). 남은 것은 HG(사람 승인) 하나이며, 그 전 준비작업 2건이 미완이다.**

완결 게이트 7항 중 6항 충족. 7항(supplement 사람 승인)이 미충족이라 **XBeach 는 미완결**이다.

| 단계 | 상태 |
|---|---|
| P0 scope (분모 456 전량) | ✅ v3 승인 |
| R1 1차 판독 | ✅ 281 (2독립) + 22 (단독) + 153 (인벤토리) |
| R2 blind 2차 | ✅ 281/281 |
| CW crosswalk | ✅ 처분 1,472 · `verify_crosswalk` 13/13 PASS |
| SUP span 확인 | ✅ confirmed_delta **103** |
| V 적대검증 | ✅ 571건 |
| **HG 사람 승인** | ❌ **미완 — 아래 작업** |

---

## 2. 남은 작업 (순서대로)

### 2-1. records-by-run 12개 디렉터리 복사 (선행 필수)

`build_supplement_manifest_modelaudit.py` 는 레코드를 `records-by-run/<run_id>/<record_file>` 에서 찾는다.
신규 6 shard(B00·B01·D00·M00·V00·V01) × 2 라운드 = **12 run_id 가 아직 없다**.

```bash
cd /home/firesinger/coastal-wiki
python3 - <<'EOF'
import json,glob,os,shutil
CW="_staging/total-read/model-audit/XBeach/cw"
n=0
for f in glob.glob(f"{CW}/crosswalk/*/*.crosswalk.json"):
    j=json.load(open(f)); sh=os.path.basename(os.path.dirname(f))
    for role,rd in (("base","records-r1"),("audit","records-r2")):
        rid=j[f"{role}_run_id"]; rf=j[f"{role}_record_file"]
        od=f"{CW}/records-by-run/{rid}"; os.makedirs(od,exist_ok=True)
        if not os.path.exists(f"{od}/{rf}"):
            shutil.copy2(f"{CW}/{rd}/{sh}/{rf}", f"{od}/{rf}"); n+=1
print("copied",n)
EOF
```

### 2-2. 신규 43건 evidence_span 정규화

기존 60건은 정규화 완료, **신규 43건은 미정규화**(B00 4 · B01 16 · D00 20 · V00 3).

- 현재(미정규화): `{"lines":"L59-L59","quote":"...\r\n","verified_at_lines":"L59-L59","source_sha256":"..."}` — **`path` 키 없음**, lines 에 `L` 접두, quote 는 리포터가 제출한 원문(CRLF 포함)
- 목표(정규화): `path`(= `XBeach/raw/source_code/<source_path>`, `models/` 기준 상대) + `lines`(숫자만, 예 `59-59`) + `quote`(**라이브 소스에서 재추출한 권위 인용문**) + 기존 필드 보존

```bash
cd /home/firesinger/coastal-wiki
python3 - <<'EOF'
import json,glob,re
CW="_staging/total-read/model-audit/XBeach/cw/crosswalk"
n=0
for f in sorted(glob.glob(f"{CW}/*/*.crosswalk.json")):
    j=json.load(open(f)); ch=False
    for d in j["dispositions"]:
        if d["disposition"]!="confirmed_delta": continue
        sp=d["evidence_span"]
        if "path" in sp and re.fullmatch(r"[\d,\- ]+", str(sp.get("lines",""))): continue   # 이미 정규화
        nums=re.findall(r"L?(\d{1,6})", str(sp.get("verified_at_lines") or sp.get("lines","")))
        assert nums, (f, sp)
        a,b=int(nums[0]), int(nums[-1])
        path=f"XBeach/raw/source_code/{j['source_path']}"
        body=open(f"models/{path}",errors="replace").read().splitlines()
        d["evidence_span"]={
            "path":path, "lines":(f"{a}-{b}" if b!=a else str(a)),
            "claimed_lines":sp.get("lines"), "reported_quote":sp.get("quote"),
            "verified_at_lines":sp.get("verified_at_lines"), "source_sha256":sp.get("source_sha256"),
            "quote":"\n".join(body[a-1:b]),
            "quote_source":"live source extract at verified lines (authoritative)"}
        ch=True; n+=1
    if ch: json.dump(j,open(f,"w"),ensure_ascii=False,indent=1)
print("normalized",n)   # 43 이어야 함
EOF
```

정규화 후 **반드시** crosswalk 재검증 (13 shard 전건 PASS 확인):

```bash
cd /home/firesinger/coastal-wiki/_staging/total-read
for t in 000 001 002 003 004 005 T00 B00 B01 D00 M00 V00 V01; do
  python3 verify_crosswalk.py model-audit/XBeach/cw/crosswalk/XBeach-$t \
    model-audit/XBeach/cw/records-r1/XBeach-$t model-audit/XBeach/cw/records-r2/XBeach-$t | tail -1
done
```

### 2-3. supplement manifest 재작성

```bash
cd /home/firesinger/coastal-wiki
T=_staging/total-read
python3 $T/build_supplement_manifest_modelaudit.py \
  $T/model-audit/XBeach/cw/crosswalk \
  $T/model-audit/XBeach/cw/records-by-run \
  models \
  $T/model-audit/XBeach/XBeach-supplement-manifest.json
```
※ 반드시 **리포 루트에서** 실행 — 게이트가 `_staging/` 를 포함한 경로로 컨테인먼트 검사를 한다. `_staging/total-read` 안에서 상대경로로 돌리면 "crosswalk path missing/escapes" 로 전건 FAIL.

### 2-4. 영수증 재생성 — 기존 60 approved 유지, 신규 43 pending

```bash
cd /home/firesinger/coastal-wiki
python3 - <<'EOF'
import json
T="_staging/total-read"
M=json.load(open(f"{T}/model-audit/XBeach/XBeach-supplement-manifest.json"))
old={(d["canonical_source_sha256"],d["audit_id"])
     for d in json.load(open(f"{T}/model-audit/XBeach/XBeach-supplement-decisions.json"))["decisions"]
     if d.get("status")=="approved"}
dec=[]; npend=0
for e in M["entries"]:
    ck=e["canonical_key"]
    for sp in e["supplements"]:
        for aid in sp["member_input_ids"]:
            k=(ck["source_sha256"],aid); ap=k in old
            if not ap: npend+=1
            dec.append({"canonical_source_sha256":ck["source_sha256"],"audit_id":aid,
              "canonical_path":ck["normalized_path"],
              "crosswalk_sha256_bytes":e["crosswalk"]["sha256_bytes"],
              "source_span_hash":sp["source_span_hash"],
              "audit_record_sha256_bytes":sp["audit_record"]["record_sha256_bytes"],
              "evidence_sha256":sorted(x["sha256"] for x in sp["evidence_sources"]),
              "status":"approved" if ap else "pending",
              **({"approver":"firesinger","approved_at":"2026-09-07",
                  "scope":"batch approval of the XBeach packet presented 2026-09-07"} if ap
                 else {"note":"P0 v3(트리 전량 456) 편입으로 생긴 신규 delta — 사용자 승인 대기"})})
D={"schema":"supplement-decisions/v2","corpus":"model-audit-20260831","model":"XBeach",
   "gate":"MERGE-PLAN §3 / 작업규범 #4 — producer 자기승인 금지",
   "decision_count":len(dec),"decisions":dec}
json.dump(D,open(f"{T}/model-audit/XBeach/XBeach-supplement-decisions.json","w"),ensure_ascii=False,indent=1)
print("receipts",len(dec),"| pending",npend)   # 103 / 43 이어야 함
EOF
```

### 2-5. 사용자에게 신규 43건 제시 → 승인 → 게이트

- **Codex 가 임의로 `status:"approved"` 로 바꾸면 안 된다.** 이 게이트의 존재 이유가 producer 자기승인 금지다(CLAUDE.md 작업규범 #4).
- 사용자에게 43건을 파일·라인·주장 요약으로 제시하고 명시 승인을 받은 뒤에만 `approved`/`approver`/`approved_at` 기입.
- 승인 후:

```bash
cd /home/firesinger/coastal-wiki
T=_staging/total-read
python3 $T/verify_supplement_modelaudit.py \
  $T/model-audit/XBeach/XBeach-supplement-manifest.json \
  $T/model-audit/XBeach/cw/records-by-run \
  models \
  $T/model-audit/XBeach/cw/crosswalk \
  $T/model-audit/XBeach/XBeach-supplement-decisions.json
```
`RESULT: PASS` 확인 → PROGRESS.md XBeach 행 DONE 처리 → 커밋·푸시.

---

## 3. 반드시 지킬 것 (게이트 무결성)

1. **`verify_supplement.py` / `verify_crosswalk.py` 원본을 수정하지 말 것.** 기존 게이트는 corpus 를 `reread-20260728` 로 하드코딩하고 있어 XBeach(model-audit 프로그램)에 안 맞는데, **상수만 바꾼 사본**(`*_modelaudit.py`)을 써서 통과시켰다. diff 는 `EXPECT_CORPUS` 1줄 + provenance 3줄이며 검사 로직은 무변경. 같은 방식을 유지할 것.
2. **자기승인 금지.** 승인 상태를 모델이 채우지 않는다.
3. **리포터 인용을 그대로 믿지 말 것.** `promote_deltas.py` 는 Codex 가 제출한 인용문을 원문에 verbatim 대조하고 인용 라인 근접까지 확인한 뒤에만 승격한다. 이번 감사에서 이 게이트가 **인용 미검증 CONFIRM 14건**을 실제로 걸러냈다(SUP 9 + 신규 5). 완화 금지.
4. **적대검증의 REFUTED 도 인용 대조 대상.** 중화 인용문이 원문에 없으면 기각을 인정하지 않는다(현재 그렇게 처리된 10건이 이월 상태).
5. **`models/` 는 root 소유 읽기전용 잠금.** 소스 수정 불가·불필요. `_staging/total-read/` 는 writer 소유라 쓰기 가능.

---

## 4. 이번 세션에서 밟은 함정 (같은 실수 반복 방지)

| 함정 | 내용 |
|---|---|
| **`--model` 생략** | codex-companion 은 생략 시 `~/.codex/config.toml` 기본값(`gpt-6-astra`)이 아니라 **`gpt-5.6-sol`** 로 간다. 기존 111파일 R1·R2 가 sol 로 수행된 것이 사후 실사로 드러났다(재판독 불요 판정). **항상 `--model` 명시.** |
| **`--write` 생략** | task 는 기본 read-only 샌드박스. 파일 출력이 필요하면 `--write` 필수. 없으면 판정을 다 하고도 결과가 유실된다(실제로 CW-005 1회 유실). |
| **경로 기준** | manifest 빌드·게이트는 **리포 루트에서** 실행. `_staging/` 안에서 돌리면 컨테인먼트 검사 전건 FAIL. |
| **PDF 처리** | `pdftotext` 금지, `opendataloader-pdf` 고정. CLI 는 `-o <dir> -f markdown <input>` (`--input/--output` 아님). |
| **출력 형식 편차** | 모델마다 fenced json / bare json / pretty-print 로 갈린다. 추출기가 3형식을 모두 받도록 되어 있다. |
| **real-read 검증 정규식** | `for f in ...; do nl -ba "$f"; done`, `seq` 청크 루프, 인용부호 경로(`nl -ba '...lt~obsolete.m4'`)를 놓쳐 오탐한 적이 있다. 현재 extractor 는 보강됨. |
| **`wc -l` vs 실제 줄 수** | 마지막 줄에 개행이 없으면 `wc -l` 이 1 적게 센다(`trunk/README` 26 vs 25). 판독 오류 아님. |

---

## 5. 도구 (전부 `~/coastal-audit-checkpoint/XBeach/tools/`, 49개)

| 도구 | 용도 |
|---|---|
| `run_r1_model.sh` / `run_r2_model.sh` `<SHARD> <files> <subsystem> [model]` | 1차/2차 blind 판독 |
| `run_cw_astra.sh` / `run_sup_astra.sh` / `run_v_astra.sh` `<SHARD>` | 판정 / span 확인 / 적대검증 |
| `extract_r1_shard.py` / `extract_r2_shard.py` | 롤아웃에서 레코드 추출 + real-read 커버리지 검증 |
| `check_verdicts.py` / `check_v.py` | CW·V 산출물 무결성 게이트 |
| `promote_deltas.py` | 인용 원문대조 후 delta 승격 |
| `cw_adapt.py` | R1/R2 jsonl → crosswalk 레코드 스키마 |
| `final_summary.py` | 전체 집계 |
| `xb-inventory.json` | 456파일 실측 인벤토리(sha256·줄수·텍스트 여부) |

**주의**: 스크립트 상단 `S=` 가 이전 세션의 스크래치패드 경로로 하드코딩돼 있다. 새 세션에서는 그 값만 교체하면 된다.

---

## 6. 이월 항목 (완결 게이트 조건 아님, 별도 판단)

- **conflict 3건** — 두 리더가 같은 위치에 상반된 주장: `wave_boundary_main.f90`(randomseed 가 allocatable 벡터냐 스칼라냐) · `morphevolution.F90`(자기보간 값이 stale 이냐 0-초기화냐) · D00 1건
- **REFUTED 인용 미검증 10건** — 기각 근거 인용문이 원문에 없어 기각 불인정(주장 존치)
- **벤더 findings 분리집계** — V00·V01(mpich·netCDF·ftnunit)의 findings 는 XBeach 결함이 아니다. `vendor` 태그로 분리해야 하며 **아직 태깅 안 됨**
- **문서축 정량사실 207건** — 매뉴얼·비정수압 보고서에서 나온 인용 가능한 값들. 위키 canonical 반영은 별도 판단(절대규칙 #8: 위키는 공급원)
- **AUDIT-LEDGER.md 표기 불일치** — `models/AUDIT-LEDGER.md` 는 XBeach 를 여전히 "종결 2026-07-12"(구 감사 기준)로 적고 있다. 이번 전수 감사와 다른 기준인데 같은 "종결" 표현이라 혼동 소지. `models/` 는 root 잠금이라 수정에 sudo 필요

---

## 7. 다음 모델

XBeach HG 통과 후 → **SFINCS (241파일) P0 scope**. 공정표 1진 순서: XBeach → SFINCS → EFDC(557) → ADCIRC(1,131).

★ P0 는 **사전 배제 없이 트리 전량**을 분모로 잡는다(2026-09-07 사용자 지시: "모든 걸 다 전수로 읽고 분석해서 분류해 놓고 나중에 판단"). XBeach 에서 배제 대상이던 파일들에서 실제 결함 1건(`testgenmodule.F90` L878)과 적용한계 자료(도해 5장)가 나왔다.

참조: 공정표 `_staging/total-read/MODEL-AUDIT-PLAN-20260831.md` · 진행표 `_staging/total-read/codex-defect-reports/PROGRESS.md`

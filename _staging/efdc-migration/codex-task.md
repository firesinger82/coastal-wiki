# CODEX TASK — EFDC 위키 마이그레이션 적용 (v12.3 계열 → v12.5)

```
OBJECTIVE
  _staging/efdc-migration/wiki-candidate/ 안의 노트 31개에 대해
  (A) 의미 수정 11지점, (B) IINTPG 산문 6지점, (C) 좌표 치환 152건,
  (D) 재앵커 12건을 적용하고 통합 diff 와 적용표를 생성한다.

SCOPE
  쓰기 허용:  _staging/efdc-migration/ 하위만.
  읽기 허용:  models/ (읽기 전용), _staging/efdc-prescan/ (new/ 는 v12.5 원본).
  금지:      models/ 하위 수정, chmod/chown/sudo/unlock 시도,
             snapshot·provenance 파일 변경, 지정 밖 문장 수정,
             새 주장·새 인용 추가, 표현만 다듬는 리라이트.

STOP CONDITION
  지정 범위를 벗어난 판단이 필요하면 해당 항목을 UNRESOLVED 로 표시하고
  확대하지 말고 반환한다. 근거가 새 소스에서 확인되지 않으면 적용하지 않는다.

DELIVERABLE
  1. wiki-candidate.diff  — 원본 대비 통합 diff (git diff --no-index 형식)
  2. apply-report.csv     — note, note_line, category(A/B/C/D), applied(yes/no/unresolved),
                            evidence(새 소스 file:line), note_text_before, note_text_after
  3. codex-report.md      — 요약 + UNRESOLVED 목록 + 판단이 갈린 지점
  4. 검사 출력: python3 tools/validate-canonical-hygiene.py (tree 모드),
                python3 _staging/model-migration-framework/test_refparser.py
```

## 입력 파일

| 파일 | 내용 |
|---|---|
| `final-classification.csv` | 78건 최종 분류 (UPDATE_REQUIRED 11 / REVIEW_ONLY 47 / NO_ACTION 20) |
| `line-ref-map.csv` | 참조 331건의 old→new 좌표. `status` = IDENTICAL(167, 무수정) / MOVED(152, 치환) / REANCHOR_REQUIRED(12) |
| `wiki-candidate/` | 수정 대상 노트 31개 사본 (여기만 편집) |
| `../efdc-prescan/new/` | v12.5 원본. 경로 `EFDC/Transport/calconc.f90` → 파일명 `EFDC__Transport__calconc.f90` |
| `../efdc-prescan/patches/` | 파일별 통합 diff |

---

## (A) 의미 수정 11지점

각 지점은 **아래 지정한 사실만** 반영한다. 문장 구조·어조는 기존 노트를 따른다.

### A1. `models/EFDC/manifest.md:17` — 릴리스 문자열
`aaefdc.f90:22` `RELEASE: EFDCPlus_12.5`, `:30` `DATE: 2026-05-26`.
12.4 → 12.5, 날짜 표기도 함께 갱신.

### A2. `manual-notes/efdc-implementation-guide.md:193` — C6 3번째 슬롯
구 서술: 더미(`ldum`)로 버려짐 → 신규: **scalar `ISQUICK`**.
근거 `input.f90:311`(read), `:316`(broadcast), `:318-325`(0/1 외 값은 경고 후 0 으로 리셋).
같은 노트 **:189 C5 카드**도 함께 수정: `ISDISP`→`ldum`, `ISQQ`→`ICALTB`, 13번째 필드 `ISHDMFILTER` 추가
(근거 `input.f90:269`). C5 의 `IINTPG` 는 계속 읽히므로 **필드 자체는 유지**한다.

### A3. `manual-notes/efdc-user-manual-r850.md:104` — C6
같은 사실. 단 이 노트는 r850 매뉴얼 기준이므로 **기존 서술을 폐기하지 말고**
"매뉴얼 r850 기준" 임을 유지한 채 v12.5 델타를 덧붙이는 방식으로 쓴다.

### A4. `source-analysis/efdc_transport_scheme.md:28` — 제목·요약의 스킴 목록
QUICKEST/ULTIMATE 경로 신설. `calconc.f90:117` upwind 게이트,
`:198-203` `ISQUICK == 1` → `CALTRAN_QUICKEST`, else `CALTRAN`.
신규 파일 `EFDC/Transport/caltran_quickest.f90`, `EFDC/Transport/mod_quickest.f90` (NEW FILE RULE: 신규 파일 인용은 v12.5 좌표).

### A5. `source-analysis/efdc_transport_scheme.md:65` — C6 절
A2 와 동일한 `ISQUICK` 사실. 추가로 `calconc.f90:228-230` 의
`CALTRAN_AD` 호출이 `ISQUICK == 0` 일 때만 발생하고, `:250` 의 `ISADAC` 반확산도 동일 게이트임을 반영.

### A6. `source-analysis/sediment/efdc_sediment.md:205` — CALTRAN 수송
"모든 성분이 CALTRAN 으로 수송" → `ISQUICK` 분기 조건부. 근거 `calconc.f90:198-203`.

### A7. `source-analysis/efdc_water_quality.md:106-107` — Inputs
`mod_diagen.f90` 에서 `ISMRST`·`write_restart_option` **완전 삭제**(새 소스 출현 0회).
해당 restart control 항목을 제거하고 남은 입력만 서술.

### A8–A10. `source-analysis/efdc_vertical.md:80, 81, 82` — IINTPG 분기표
표 3행이 가리키는 분기가 `calexp.f90` 에서 **전부 삭제**됐다.
표를 다음 사실로 교체한다.
- v12.5 의 buoyancy shear 분기축은 `IGRIDV` 다: `IGRIDV == 1`, `IGRIDV > 1`, `else`(STANDARD-SIGMA).
  좌표는 새 `calexp.f90` 에서 직접 확인해 인용한다.
- `IINTPG` 는 입력으로 계속 읽히지만(`input.f90:269`) buoyancy shear 분기에는 **더 이상 쓰이지 않는다**.
- 유일한 소비처는 `setbcs.f90:449` `if( IINTPG == 0 )` — 2-cell-wide 수로의
  external density gradient cell-face flag. 즉 `IINTPG /= 0` 은 이 처리를 **끄는** 효과만 낸다.
- `calexp2t.f90`(2TL) 도 동일하게 4→0 으로 제거됐다.

### A11. `source-analysis/efdc_baroclinic_eos.md:75-81` — §4 코드블록
같은 IINTPG 3형식(`:1207/:1225/:1265`)을 코드블록으로 문서화한 부분. A8–A10 과 동일한 사실로 교체.
§4 제목의 범위 인용 `calexp.f90:1162-1352` 도 새 좌표로 갱신.
`:90` findings 의 "IINTPG 0/1/2 3형식" 항목은 (B) 에서 처리.

---

## (B) IINTPG 산문 6지점

인용이 없지만 (A) 와 같은 사실을 직접 단언하는 문장이다.
**삭제하지 말고** 다음 세 요소로 교체한다: (a) v12.5 에서 분기 제거, (b) 급경사 대응은 `IGRIDV>0`(SGZ),
(c) `IINTPG /= 0` 이 `setbcs.f90:449` 를 끄는 부작용.
EFDC-GVC 레거시 트리에는 IINTPG 분기가 남아 있으므로 **"EFDC+ Stable 12.5 기준"** 범위를 문장에 명시한다.

| # | 위치 | 현재 문장 요지 |
|---|---|---|
| B1 | `efdc_vertical.md:84` | "the alternative formulations are selected by `IINTPG`. For steep bathymetry, use `IINTPG=1` or `2`." |
| B2 | `efdc_vertical.md:106` | Decision Guide 표 "Steep slope / canyon → `IINTPG` `1` or `2` / Reduces sigma-coordinate PGF error" |
| B3 | `efdc_vertical.md:118` | Working Rules "…cure with `IINTPG=2`." |
| B4 | `efdc_vertical.md:126` | Pitfalls "Using `IINTPG=2` (finite-volume) with very thin layers near surface…" |
| B5 | `efdc_hydro_core.md:99` | 표 "Density-stratified estuary … set `IINTPG=1` or `2` for steep bathymetry" |
| B6 | `concepts/sst/06-model-application.md:75` | "…`IINTPG=1/2` 권장 (efdc_vertical.md §E·Working Rules)" |

**수정 금지 2곳** (판정 완료, 손대지 않는다):
- `efdc_vertical.md:133` "IINTPG option benchmark on canyon cases" — 백로그 항목, 동작 단언 아님.
- `efdc-implementation-guide.md:189` 의 "C5 에 IINTPG 가 있다" 자체 — 입력 카드는 유지. (A2 의 다른 필드 수정은 적용)

---

## (C) 좌표 치환 152건

`line-ref-map.csv` 의 `status == MOVED` 행만 기계 치환한다.
`old` → `new` 로 바꾸되 **`ref` 열의 원문 표기를 보존**한다 (en dash `–`, `L` 접두, 복수 범위 `a-b,c-d`, 상대경로, `[file= line=]` 형식).

- `status == IDENTICAL` 167건은 **수정 금지**.
- 치환 후 자체 검증: 새 좌표의 줄 내용이 `../efdc-prescan/new/` 의 해당 파일에서
  치환 전 줄 내용과 동일한지 확인. 불일치는 치환을 되돌리고 UNRESOLVED 로 보고.
- 이 152건은 78건 분류 단위보다 넓다. 29건은 분류 후보에 없던 노트에 있으나
  **의미 판정과 무관한 좌표 정비**이므로 포함한다. 문장 내용은 바꾸지 않는다.

## (D) 재앵커 12건

`status == REANCHOR_REQUIRED`. 끝점이 삭제·교체된 블록 안에 있어 기계 매핑이 불가능하다.
`new` 열은 **후보일 뿐 정답이 아니다**. 각 건마다 새 소스를 직접 열어
그 인용이 가리키던 코드가 v12.5 어디에 있는지 확인하고 좌표를 정한다.

- 이 중 `efdc_vertical.md:80,81,82`, `efdc_baroclinic_eos.md:75`, `efdc_transport_scheme.md:28,65`,
  `manifest.md:17`, `efdc-implementation-guide.md:193`, `efdc-user-manual-r850.md:104`,
  `efdc_sediment.md:205` 는 (A) 의미 수정과 같은 지점이다 — 문장을 고치면서 좌표도 함께 정한다.
- `efdc_vertical.md:24`(`calexp.f90:243-406, 1152, 1169-1265`) 와
  `efdc_boundary_conditions.md:19, :85`(`input.f90` 광역 다중 범위) 2노트 3건은
  의미 변경 없이 범위만 재설정한다. 대응 코드를 찾지 못하면 UNRESOLVED_SOURCE_REFERENCE 로 남긴다.

---

## 적용하지 않는 것

- NO_ACTION 20건에 해당하는 문장 — diff 에 나타나면 실패로 본다.
- `citation_status`, `historical_source_provenance`, `current_validated_against` 등 frontmatter 필드.
  (provenance 는 finalization 단계에서 Claude 가 처리)
- `models/` 원본 파일. 작업은 전부 `wiki-candidate/` 사본에서만.

---

# DECISIONS (Claude, Codex 질의 회신)

## D1. 내부 변경 31건 — **152건 전부 적용** (끝점 기준 유지)

Codex 지적대로 `line-ref-map.csv` 의 게이트는 범위 **끝점**만 비교했고, MOVED 152건 중
31건은 범위 **내부** 코드가 달라졌다. 31건을 개별 확인한 결과 전부 좌표 치환이 안전하다.

| 구분 | 건수 | 근거 |
|---|---|---|
| 내부까지 동일 | 121 | 자명 |
| 내부 변경 + 해당 note:line 이 78건 판정 완료 | 30 | REVIEW_ONLY 26 / UPDATE_REQUIRED 2(§A 에서 처리) / 혼재 2. 변경 hunk 를 이미 대조해 "주장 불변" 으로 판정한 지점이다 |
| 내부 변경 + 미판정 | 1 | `concepts/sst/06-model-application.md:75` ← `input.f90:732-754`(C14). Claude 직접 확인: read 목록 11개 필드 동일, 진단 `write` 와 `ISPROPWASH` broadcast 의 **순서만 이동**. 의미 변화 없음 |

**단, 내부 변경은 문장 수정 사유가 아니다.** 31건 모두 좌표만 바꾸고 본문은 건드리지 않는다.

참고: `final-classification.csv` 의 B1 배치 17행은 줄번호가 섹션 경로 문자열에서 잘못 추출돼 있었다.
수정 후 재생성했으므로 **현재 파일을 다시 읽어라**.

## D2. `efdc_baroclinic_eos.md:90` — **교체한다 (B 총 7곳)**

§4(A11)를 IGRIDV 기준으로 고치면서 §5 findings 의 "IINTPG 0/1/2 3형식" 을 남기면
같은 노트 안에서 모순이 생긴다. B1–B6 과 같은 3요소로 교체한다.
B 지점은 총 7곳이 된다.

# EFDC 스냅샷 마이그레이션 — 실행 계획 (v12.3 계열 → v12.5)

상태: PLANNED (미실행). 근거: `_staging/efdc-prescan/` 78건 최종 분류.
이 단계에서 **하지 않는 것**: snapshot 교체, provenance 갱신, DESIGN v2 FINAL 승격, `models/` unlock.

## 0. 실행 방식 — in-place 수정 금지

대상 노트 8개 중 7개가 `models/` 하위(root 소유 `r--r--r--`)다. snapshot 을 아직 교체하지 않으므로,
새 line 번호로 고친 노트를 잠긴 트리에 넣으면 **로컬 소스와 인용 좌표가 불일치**한다.

→ ADCIRC 파일럿과 동일하게 **staging 사본에서 작업**한다.

```
_staging/efdc-migration/
  wiki-candidate/           # 대상 노트 8개 + concepts 1개의 수정본
  wiki-candidate.diff       # 원본 대비 통합 diff (리뷰 단위)
  line-ref-map.csv          # 47건 REVIEW_ONLY 의 old→new 좌표
  codex-task.md             # 아래 §3 계약
  codex-report.md           # Codex 반환 원문
  claude-verification.csv   # §4 체크리스트 판정
```

`models/` 는 잠긴 채로 둔다. 실제 반영은 finalization(별도 승인) 때 snapshot 적용과 **같은 게이트에서** 수행한다.

## 1. 확정된 사실 기반 (새 소스 직접 확인)

| 사실 | 증거 |
|---|---|
| EFDC+ Stable 에서 `IINTPG` **분기 전량 삭제** | pinned: `calexp.f90`(4)·`calexp2t.f90`(4) 만 분기 보유 → v12.5 both 0 |
| 삭제된 것은 buoyancy shear FBBX/FBBY 의 3형식 | `patches/EFDC__calexp.f90.patch`: `elseif( IINTPG == 0/1/2 )` → `else` 단일화 |
| 대체 분기축은 `IGRIDV` | new `calexp.f90`: `IGRIDV == 1` / `IGRIDV > 1` / `else`(STANDARD-SIGMA) |
| `IINTPG` 는 입력으로 계속 읽힘 | new `input.f90:269, 284, 288`; `mod_scaninp.f90`, `mod_var_global.f90` |
| 유일한 새 소비처 | `setbcs.f90:449` `if( IINTPG == 0 )` — 2-cell-wide 수로의 external density gradient cell-face flag |
| C5 카드 필드 변경 | `ISDISP`→`ldum`, `ISQQ`→`ICALTB`, 13번째 `ISHDMFILTER` 추가 |
| `calebi.f90` 는 IINTPG 를 갖지 않음 | pinned 전수 grep — 분기는 calexp 계열에만 존재 |
| EFDC-GVC 레거시 트리는 무변경 | `calexp.for`·`calexpgvc.for`·`calexp2t.for` 의 IINTPG 유지 |

**의미**: v12.5 에서 `IINTPG=1`(JACOBIAN)·`2`(FINITE VOLUME) 는 운동량/부력 경로에 아무 효과가 없다.
0 이 아닌 값은 이제 `setbcs.f90:449` 게이트를 **끄는** 부작용만 낸다. 급경사 sigma PGF 오차 완화 수단은 SGZ(`IGRIDV>0`)로 이동했다.

## 2. 수정 범위

### 2-A. 의미 수정 (UPDATE_REQUIRED 11건 / 노트 8개)

| 노트:줄 | 사유 타입 | 수정 방향 |
|---|---|---|
| `efdc_vertical.md:78-82` | BEHAVIOR_CHANGE | IINTPG 분기표를 IGRIDV 분기표로 교체, IINTPG 는 입력 전용 + setbcs 게이트로 재서술 |
| `efdc_baroclinic_eos.md:75-81` | BEHAVIOR_CHANGE | §4 의 "IINTPG 3형식" 블록을 IGRIDV 분기 + STANDARD 단일화로 교체 |
| `efdc-implementation-guide.md:193` | INPUT_SCHEMA_CHANGE | C5 필드 목록 갱신(ldum/ICALTB/ISHDMFILTER) |
| `efdc-user-manual-r850.md:104` | INPUT_SCHEMA_CHANGE | 동일 카드 서술 정합 |
| `efdc_transport_scheme.md` 제목·요약·:65 | SEMANTIC_CHANGE | C6 ldum→`ISQUICK` scalar 승격, QUICKEST limiter 변경 반영 |
| `efdc_sediment.md:205` | SEMANTIC_CHANGE | calconc 무조건 CALTRAN 호출 전제 수정 |
| `efdc_water_quality.md:106-107` | LINE+SEMANTIC | `mod_diagen.f90` 입력 구간 재서술 |
| `manifest.md:17` | BUGFIX_AFFECTING_DOC | 릴리스 12.4→12.5, DATE 갱신 |

### 2-B. 무인용 산문 재검증 결과 (사용자 지시: 문장 단위 판정)

| # | 위치 | 문장 요지 | 판정 |
|---|---|---|---|
| P1 | `efdc_vertical.md:84` | "formulations are selected by IINTPG. For steep bathymetry, use IINTPG=1 or 2" | **INCLUDE** — 삭제된 분기를 직접 단언 |
| P2 | `efdc_vertical.md:106` | Decision Guide "Steep slope/canyon → IINTPG 1 or 2, Reduces sigma PGF error" | **INCLUDE** — 동일 사실 단언 |
| P3 | `efdc_vertical.md:118` | "cure with `IINTPG=2`" | **INCLUDE** — 제거된 형식 처방 |
| P4 | `efdc_vertical.md:126` | "Using `IINTPG=2` (finite-volume) with very thin layers…" | **INCLUDE** — FINITE VOLUME 존재 전제 |
| P5 | `efdc_hydro_core.md:99` | "set `IINTPG=1` or `2` for steep bathymetry" | **INCLUDE** — 동일 사실 단언 |
| P6 | `concepts/sst/06-model-application.md:75` | "`IINTPG=1/2` 권장" | **INCLUDE** — 동일 사실 단언 |
| — | `efdc_vertical.md:133` | Next expansion "IINTPG option benchmark on canyon cases" | **EXCLUDE** — 동작을 단언하지 않는 백로그 항목. 별도로 무의미해졌음만 보고 |
| — | `efdc-implementation-guide.md:189` | C5 카드에 IINTPG 가 있다 | **EXCLUDE** — 입력 카드는 유지, 단언 여전히 참 (단 2-A 의 필드 갱신 대상) |

P1–P6 의 공통 치환 방향: IINTPG 권고를 **삭제**하지 않고 (a) v12.5 에서 분기가 제거됐다는 사실,
(b) 급경사 대응은 `IGRIDV>0`(SGZ), (c) `IINTPG≠0` 이 `setbcs.f90:449` 를 끄는 부작용 — 세 가지로 교체한다.
GVC 레거시에는 여전히 유효하므로 "EFDC+ Stable 12.5 기준" 범위를 문장에 명시한다.

### 2-C. line-reference 유지보수 (REVIEW_ONLY 47건)

의미 변화 없음. old→new 좌표만 `line-ref-map.csv` 기준으로 기계 치환.
content-identity 검사(치환 후 해당 줄의 토큰이 인용 문구와 일치) 통과분만 반영. 불일치는 UNRESOLVED_SOURCE_REFERENCE 로 남기고 보고.

### 2-D. NO_ACTION 20건 — 무수정. diff 에 등장하면 실패로 본다.

## 3. Codex 위임 계약

```
OBJECTIVE:  _staging/efdc-migration/wiki-candidate/ 에 대상 노트 9개의 수정본과
            통합 diff 를 생성한다. 의미 수정 11건 + 산문 6건은 §2 지정 방향대로,
            line-ref 47건은 line-ref-map.csv 대로 적용한다.
SCOPE:      쓰기 허용 = _staging/efdc-migration/ 하위만.
            읽기 = models/ (읽기 전용), _staging/efdc-prescan/.
            금지 = models/ 하위 수정, unlock 시도, snapshot/provenance 파일 변경,
                   NO_ACTION 20건 수정, 지정 밖 문장 수정, 새 주장 추가.
STOP:       §2 범위를 벗어난 판단이 필요하면 해당 항목을 UNRESOLVED 로 표시하고
            확대하지 말고 반환한다.
DELIVERABLE: wiki-candidate.diff, 항목별 적용표(노트:줄 / 사유타입 / 적용여부 / 근거 file:line),
            tools/validate-canonical-hygiene.py 와 링크 검사 실행 출력.
```

## 4. Claude 사후 검증 체크리스트

1. UPDATE_REQUIRED 11건이 모두 적용됐는가 (누락·과잉 없음)
2. 산문 P1–P6 이 새 동작과 정합하고, P5 제외 판정이 유지됐는가
3. REVIEW_ONLY 47건 line 번호가 새 소스와 일치하는가 (content-identity 재검)
4. 새로 생긴 내부 모순 없음 — IINTPG 서술이 노트 간 일관
5. NO_ACTION 20건 무변경 (diff 부재로 확인)
6. 링크·wikilink·citation 무결성 (`citation_status` 하향 필요 여부 포함)
7. G8b/G8d/G8e 위생 검사 통과
8. 인용 좌표 basis 가 v12.5 임이 노트에 기록됐는가 (`citation_snapshot`)
9. GVC 레거시 적용 범위가 문장에 명시됐는가
10. 파서 게이트 재실행 PASS
11. diff 가 `_staging/efdc-migration/` 밖을 건드리지 않았는가

## 5. 종료 상태

- `MIGRATION_READY_FOR_FINALIZATION` — 1–11 전부 통과. 다음 단계는 별도 승인 하의
  snapshot 적용 + wiki-candidate 반영 + provenance 갱신(동일 게이트).
- `MIGRATION_NEEDS_FIXES` — 수정 가능한 불일치 존재. 항목별로 보고.
- `MIGRATION_BLOCKED` — 소스 증거만으로 판정 불가한 항목 존재. 사용자 결정 필요.

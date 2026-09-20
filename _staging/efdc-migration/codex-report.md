# EFDC 위키 마이그레이션 적용 보고

`codex-task.md` 및 마지막 `DECISIONS` D1/D2를 적용했다. 지정된 `wiki-candidate/` 노트 사본 31개를 수정했다. canonical 원본·snapshot·provenance 파일은 변경하지 않았다.

| 작업 | 적용 | UNRESOLVED |
|---|---:|---:|
| A 의미 수정 | 11 | 0 |
| B IINTPG 산문 | 7 | 0 |
| C MOVED 좌표 | 152 | 0 |
| D 재앵커 | 12 | 0 |
| 합계 | 182 | 0 |

**UNRESOLVED: 없음.** 이 결과는 지정 계약의 사본 적용 결과이며, canonical 설치나 provenance finalization 완료를 뜻하지 않는다.

산출물:

- [wiki-candidate.diff](wiki-candidate.diff): 원본 대비 `git diff --no-index` 출력. 목적지의 staging 접두사만 제거해 `a/<note>` → `b/<note>` 형태로 제공했다. `git apply --check` 통과; 실제 적용은 수행하지 않았다.
- [apply-report.csv](apply-report.csv): 182개 작업의 근거와 변경 전후 텍스트.
- [validate-canonical-hygiene-tree.txt](validate-canonical-hygiene-tree.txt): 사본 31개 tree 검사 출력, exit 0.
- [test-refparser.txt](test-refparser.txt): fixtures 21 + 규칙검사 7, 실패 0, `PARSER_GATE_PASSED`, exit 0.
- 추가 검증 기록: [migration-checks.txt](migration-checks.txt), [coordinate-checks.json](coordinate-checks.json), [baseline-sha256.json](baseline-sha256.json).

## 적용표 읽는 법

`note`와 `note_line`은 **원본 노트 경로·줄 번호**다. CSV는 **C → D → A → B** 순서의 작업 원장이다. `note_text_before`/`note_text_after`는 각 작업 직전·직후 텍스트이며, 같은 위치에 좌표 수정과 의미 수정이 겹치면 별도 행으로 남겼다. 따라서 D 행의 중간 문장은 뒤따르는 A 행에서 의미가 수정된다. 최종 문서는 `wiki-candidate/`와 통합 diff로 확인한다.

A2의 행 번호는 계약 지점 193이고 변경 텍스트는 C5 부수 수정까지 포함한 189–193이다. A4는 제목·요약·dispatch(18–35), A5는 C6 절(65–77), A8은 절 도입부와 첫 표 행(70–80), A11은 75–83을 포함한다. 원장 전체로 최종 사본을 재구성해 실제 파일과 일치함을 검증했다.

## 근거 확인

- 릴리스·날짜: 새 `EFDC/aaefdc.f90:22,30`의 `EFDCPlus_12.5`, `2026-05-26`.
- C5/C6: 새 `EFDC/input.f90:269,311,316,318-325`. C5의 `IINTPG` 필드를 보존했다. C6의 3번째 슬롯은 scalar `ISQUICK`, 6·7·8번째는 `ldum`; 0/1 외 값은 경고 후 0으로 초기화된다. r850 노트는 매뉴얼·이전 소스 설명을 유지하고 v12.5 델타를 덧붙였다.
- 수송: 새 `EFDC/Transport/calconc.f90:117-132,198-203,228-230,250`에서 upwind 사전 계산, QUICKEST/CALTRAN dispatch, 반확산 게이트를 직접 확인했다.
- 신규 파일 2개는 `new/`에 없고 `patches/EFDC__Transport__caltran_quickest.f90.patch`와 `patches/EFDC__Transport__mod_quickest.f90.patch`에 **전체 추가 파일**로 제공돼 있다. 각각 `@@ -0,0 +1,503 @@`, `@@ -0,0 +1,115 @@`와 추가 줄 수를 확인했다. 패치의 새 파일 좌표로 `caltran_quickest.f90:14-33`, `mod_quickest.f90:80-101`을 인용했다. source 파일은 생성하거나 수정하지 않았다.
- Diagenesis: 새 `EFDC/Eutrophication/mod_diagen.f90:164-276`의 입력을 확인했고, 전체 파일에서 대소문자 무관 `ISMRST`·`write_restart_option` 출현이 모두 0회임을 확인했다. Inputs의 restart control 항목만 제거했다.
- Buoyancy shear: 새 `EFDC/calexp.f90:1169,1187,1206-1207`의 `IGRIDV == 1`, `IGRIDV > 1`, `else`를 확인했다. `calexp.f90`·`calexp2t.f90` 모두 `IINTPG` 출현은 이전 4회 → 새 0회다. 2TL 대응 분기는 `calexp2t.f90:1248,1266,1286-1287`. 입력은 `input.f90:269`에 남고, 동작 소비는 `setbcs.f90:447-474`의 2-cell-wide 수로 cell-face flag 처리로 남는다.

## D 재앵커 확정 좌표

아래 위치는 원본 노트 줄 번호다. CSV의 `new` 후보를 그대로 채택하지 않고 대응 코드를 확인했다.

| 노트 | 원본 줄 | 확정 인용 | 선택 근거 |
|---|---:|---|---|
| manifest.md | 17 | `EFDC/aaefdc.f90:22` | 릴리스 헤더 자체가 여전히 22행 |
| efdc-implementation-guide.md | 193 | `input.f90:311` | C6 read |
| efdc-user-manual-r850.md | 104 | `input.f90:311` | C6 read |
| efdc_boundary_conditions.md | 19 | `input.f90:269, 570, 755-778, 884-901, 903-1395, 1445-1470, 2818-3092, 3753-3781, 5801-5836, 5868-5906, 6009-6428` | C15 블록은 901에서 종료; 남은 MODCHAN read 블록은 3781에서 종료 |
| efdc_boundary_conditions.md | 85 | `input.f90:1445-1452` | C23 read는 1450, master 블록 종료는 1452 |
| efdc_transport_scheme.md | 28 | `calconc.f90:117-132` | upwind 게이트와 LUPU/LUPV 할당 포함 |
| efdc_transport_scheme.md | 65 | `input.f90:311` | C6 read |
| efdc_vertical.md | 24 | `calexp.f90:243-406, 1152, 1169-1222` | 연직 이류 구간 불변; IGRIDV 3분기 종료 1222 |
| efdc_vertical.md | 80 | `calexp.f90:1169` | IGRIDV == 1 |
| efdc_vertical.md | 81 | `calexp.f90:1187` | IGRIDV > 1 |
| efdc_vertical.md | 82 | `calexp.f90:1206-1207` | else와 STANDARD-SIGMA 주석 |
| sediment/efdc_sediment.md | 205 | `Transport/calconc.f90:198-203` | ISQUICK dispatch |

## 판단이 갈린 지점과 보존 범위

1. **MOVED 내부 변경 31건:** D1 회신에 따라 끝점 기준으로 152건 모두 적용했다. 152건 모두 양 끝줄의 텍스트가 일치하며, 121건은 범위 전체도 일치한다. C 작업은 전부 좌표 숫자만 바꿨다. A7/A11과 겹치는 두 지점의 의미 수정은 해당 A 작업으로만 기록했다.
2. **B findings:** D2에 따라 `efdc_baroclinic_eos.md:90`도 수정해 B는 7건이다. B2의 지정 문구는 실제 원본 **108행**에 있어 표의 106행 대신 문구로 식별했다.
3. **재생성 입력:** 최신 `final-classification.csv` 78건(UPDATE_REQUIRED 11 / REVIEW_ONLY 47 / NO_ACTION 20)을 다시 읽었다. 수정된 B1-17은 `efdc_dispersion.md:240`이다. `line-ref-map.csv`도 최신 331건을 사용했다.
4. **목록 표기 차이:** 지시서 §D에 함께 언급된 `efdc_baroclinic_eos.md:75`는 실제 CSV에서 MOVED이므로 C 및 A11로 처리했다. D는 CSV의 REANCHOR_REQUIRED 12건이다. D1 회신의 C14 미판정 인용은 `concepts/sst/06-model-application.md:75`라고 적혔으나 실제 CSV 대상은 **`concepts/tides/06-model-application.md:75`**다. C14 read와 끝점을 확인하고 실제 CSV 행에 좌표만 적용했다.
5. **frontmatter·provenance:** 전부 보존했다. A4는 본문 H1·요약을 수정했으며 frontmatter `title`은 금지 범위에 따라 유지했다. manifest의 기존 clone SHA·획득 기록도 유지했다. provenance 정합은 계약대로 후속 finalization 대상이다.
6. **NO_ACTION:** 20건의 문장 내용은 그대로다. 그 문장 안에 포함된 명시적 C/D 대상 인용은 요청대로 좌표만 변경했으며, 좌표를 제외한 텍스트 일치를 검사했다. `efdc_vertical.md:133` 백로그와 implementation guide의 기존 C5 `IINTPG` 설명도 보존했다.
7. **범위 밖 잔존 표기:** 지정되지 않은 bare `:NN` 좌표, 이전 검증 기록·버전 문구, `efdc_vertical.md:15`의 IINTPG 요약 등은 임의로 수정하지 않았다. 예를 들어 `efdc_internal_shear_caluvw.md`의 `calexp.f90:1366`은 CSV대로 `:1309`로 바뀌지만 같은 문장의 bare `:1367`은 CSV 대상이 아니므로 그대로다. 이 보고서는 이러한 범위 밖 항목까지 v12.5로 정합됐다고 주장하지 않는다.

## 검사 실행 방식

`tools/validate-canonical-hygiene.py`는 별도 대상 인자가 없고 import 시 저장소 루트로 이동한다. 원본 검사기를 변경하지 않고 `runpy.run_path`로 로드한 뒤, 작업 디렉터리를 `wiki-candidate/`로 설정해 `main()`을 실행했다. `--staged` 없이 **working-tree 모드**, 검사 대상 Markdown **31개**를 확인했다. 실제 명령과 stdout/stderr는 검사 로그에 있다.

`python3 -B _staging/model-migration-framework/test_refparser.py`도 실행했다. `-B`로 허용 범위 밖 `__pycache__` 생성을 방지했다. 재현용 실행기는 [run-checks.py](run-checks.py)다.

추가 검증에서 IDENTICAL 167건(사본 내 156 / 사본 밖 11), NO_ACTION 산문 20건, 모든 frontmatter, 금지된 B 두 지점 보존을 확인했다. 원본 노트·참조 pinned source·제공된 new source와 patch·입력 CSV의 SHA-256도 보존됐다. staging 사본은 상속된 읽기 전용 파일 모드를 유지하는 원자적 파일 교체로 편집했으며 `chmod`·`chown`·`sudo`·잠금 해제는 사용하지 않았다.

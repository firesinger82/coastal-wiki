# experience 수치 인용 lint 구현 보고서

## 결과 요약

v2 설계 기준으로 구현했다. 기본 모드는 warn(exit 0), `--strict`는 경고가 있으면 exit 1이다. 본문 케이스는 18건 중 16건을 탐지하고 2건을 설계상 한계로 고정 누락했다. frontmatter의 `verification_method`·`sources` experience 참조는 본문과 별도 경고하며 `related`는 경고하지 않는다.

## 생성·변경 파일

- 생성: `tools/validate-experience-numbers.py`
- 생성: `tools/validate-experience-numbers.sh` (실행 권한)
- 생성: `tools/test_validate_experience_numbers.py`
- 생성: `_staging/experience-number-lint/cases.json`
- 생성: `_staging/experience-number-lint/IMPL-REPORT.md`
- 변경: `tools/validate-all.sh` — `validate-experience-numbers.sh`를 VALIDATORS 마지막에 추가

그 밖의 파일과 git state는 변경하지 않았다.

## 단위 테스트

명령: `python3 tools/test_validate_experience_numbers.py`

출력 tail:

```text
Ran 8 tests in 0.038s

OK
```

기존 회귀도 확인했다: `python3 tools/test_validate_layer_deps.py` → `Ran 16 tests ... OK`.

## cases.json 결과

기준 트리: `2ad55e4^`. `detect`/`miss`는 해당 case의 블록이 하나 이상의 경고를 냈는지 기준이다.

| ID | 기대 | 실제 | 결과 |
|---|---|---|---|
| currents-04-174 | detect | detect | OK |
| currents-05-117 | detect | detect | OK |
| sst-01-123 | detect | detect | OK |
| sst-01-125 | detect | detect | OK |
| sst-02-124 | miss | miss | OK |
| sst-02-140 | detect | detect | OK |
| sst-02-177 | miss | miss | OK |
| sst-02-192 | detect | detect | OK |
| sst-02-193 | detect | detect | OK |
| sst-03-164 | detect | detect | OK |
| sst-05-27 | detect | detect | OK |
| sst-06-196 | detect | detect | OK |
| sst-06-197 | detect | detect | OK |
| sst-readme-22 | detect | detect | OK |
| sst-readme-23 | detect | detect | OK |
| storm-surge-06-64 | detect | detect | OK |
| tides-02-412 | detect | detect | OK |
| tides-02-421 | detect | detect | OK |

본문 탐지 16/18, 기대와 다른 결과 0건. frontmatter 별도 2건은 모두 `warn`으로 출력된다.

## 회귀 스냅샷

- `afc08c8^:concepts/storm-surge/01-concept.md`: §3.3의 139–142 블록 정량값을 탐지했다(표시 경고는 3.94 mm/yr, +4 mm, +40 cm 등).
- `0859062^:concepts/storm-surge/05-examples.md`: 232–233의 +7.5 cm, 3.94 mm/yr, +0.30°C를 탐지했다. 234의 전파값은 별도 experience 참조가 없어 자동 귀속하지 않는 한계로 기록했다.

스냅샷은 임시 디렉터리에 archive한 뒤 임시 git index를 만들어 실행했으며, main worktree의 git state는 건드리지 않았다.

## validate-all 시간

동일 환경에서 단일 실행 측정:

- 추가 전 구성(기존 6개 validator): 3.33초
- 추가 후 `bash tools/validate-all.sh`: 3.99초
- 증가: 0.66초 (인수 조건 +1초 이내)

기존 validator의 출력·종료 코드는 변경하지 않았고, 전체 `validate-all.sh`는 exit 0이었다.

## 현재 HEAD 전체 경고

명령: `python3 tools/validate-experience-numbers.py` (whole tree, warn mode)

```text
concepts/sst/05-examples.md:6: [exp-num] frontmatter experience 근거 참조 | verification_method: "Hobday et al. 2016 MHW 알고리즘 (Progress in Oceanography 141:227-238)  monthly variant(OISST v2.1 monthly, 1991-2020 climatology, month-of-year p90, 연속 2+ months) 와 daily 표준(5-day) 의 구현·실행 방법 — tools/sst-cross-check/identify_mhw_{monthly,daily_2024}.py. 실행 결과 수치는 experience/khoa-2024-mhw-extreme.md §2·§2b (2026-09-29 이관, CONVENTIONS §8.1)."
concepts/storm-surge/06-model-application.md:64: [exp-num] khoa-design-surge-eva-2026 | +36 cm | - **Maemi 2003**(마산 최악, source-needed) · **Hinnamnor 2022**(포항 9월 고극조위 누년 +36 cm, verified — 해일 peak 아님) · **Bolaven 2012**(군산외해 ADCP 잔차, verified)
models/ROMS/web-refs/roms-official-resources.md:179: [exp-num] nifs-vertical-sst-trends | 30-40 km, 1-10 km | 1. **동해 의 강한 mesoscale + sub-mesoscale 양쪽 length scale** — Rossby radius (~30-40 km) + sub-mesoscale (1-10 km) → spatially varying correlation 활용 적합
[exp-num] 경고 3건 (mode: full).
```

현재 HEAD 경고는 자동 정정하지 않고 Claude의 한 건씩 판정 대상으로 남겼다. 첫 경고는 frontmatter 검증근거 경고, 둘째는 experience 링크와 같은 블록의 +36 cm, 셋째는 wikilink와 같은 블록의 공간척도 값이다.

## 설계와의 차이·보수적 판단

- `[[README]]`는 v2 지시대로 현재 문서의 로컬 README 우선으로 해석해 experience basename 후보에서 제외했다.
- `related`의 experience 링크는 탐색 링크로 허용하고 경고하지 않았다.
- 수치 토큰이 없는 정량 결론(예: “SST 최대 trend”)과 링크에서 떨어진 값은 자동 의미 판정을 하지 않고 누락으로 남겼다. 이는 설계의 L4 감사 한계에 해당한다.
- 표는 행별 블록으로 검사하고 헤더의 단위만 셀에 상속한다. 행 간 “같음”의 출처 상속은 구현하지 않았다.
- 억제 주석은 사유가 있을 때만 적용하고 빈 사유는 경고한다. 산술 자동 면제는 두지 않았다.

## Claude 검증 (2026-09-29)

- 단위 테스트·layer-deps 회귀·`--strict` 종료 코드(경고 시 1) 재현 확인.
- 현재 HEAD 경고 3건 판정 — **전부 오탐**:
  1. `sst/05:6` frontmatter — 결과 위치 안내 문구. 규칙은 유지하고 노트 문구 수정.
  2. `storm-surge/06:64` (+36 cm, KHOA 출처) / 3. `models/ROMS/web-refs/roms-official-resources.md:179` (Rossby 30–40 km, experience 에 없음) — 형제 항목 귀속이 설계("출처 줄")보다 넓게 구현됨.
- 수정: 형제 귀속은 다음 항목에 검증 표지(검증·확인·근거·출처·전체 분석·`@ sha`)가 있고 "탐색용" 이 없을 때만. 회귀 테스트 `test_sibling_attribution_needs_source_mark` 추가.
- `cases.json` 평가가 재현 불가였음 → `run_cases.py` 추가(기준 리비전 worktree + 현재 validator, 블록 시작행 ±6 허용). 수정 후 16/18, 불일치 0.
- 수정 후 현재 HEAD 경고 0건, validate-all 약 4.0 초.

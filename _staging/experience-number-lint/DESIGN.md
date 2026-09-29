# experience 수치 인용 검사 — 설계 (2026-09-29)

근거 규칙: [CONVENTIONS §8.1](../../CONVENTIONS.md) "experience 수치 인용 금지(2026-09-29 사용자 결정)" — layer ④ 가 아닌 canonical 은 experience 를 참고 링크로 걸 수 있으나 수치·정량 결론을 본문에 옮기지 않는다.

배경: 기존 `validate-layer-deps.py` 는 frontmatter `layer:` 가 있는 파일의 `depends_on` 만 검사한다. 2026-09-29 조사에서 `layer:` 없는 canonical 10파일에 위반 17건 + 재감사 잔여 4건이 있었고 어떤 검사도 잡지 못했다 (`_staging/audit/pending-2026-09-29/survey8-result.json`, `reaudit9-result.json`).

## 범위

- 새 도구 `tools/validate-experience-numbers.py` + 얇은 `.sh` 진입점. `tools/validate-all.sh` VALIDATORS 에 등록.
- 결정적(구조) 검사만. 수치가 experience 에서 왔는지의 **의미 판정은 하지 않는다** — L4 감사 몫(validate-all.sh 머리 주석의 축 분리 유지).
- 기존 validator 동작은 바꾸지 않는다.

## 대상 파일

- `concepts/`·`models/`·`textbook/` 아래 `.md`. `--staged`(pre-commit) 는 staged 파일만, 인자 없으면 트리 전체.
- 제외: frontmatter `layer: 4`, 경로 `concepts/*/NN-applied-*.md`, `*/_template/*`.
- `models/` 는 읽기만 한다(잠금 유지, 도구가 쓰지 않음).

## experience 참조 판정

- 경로 링크: 본문에 `experience/<name>.md` 가 포함(상대 접두 `../../` 등 무관, `@ <sha>`·`#anchor` 허용).
- wikilink: `[[<name>]]`, `[[<name>|…]]`, `[[<name>#…]]` 에서 `<name>` 이 실행 시점 `experience/*.md` basename 집합에 속함.
- frontmatter: `verification_method`·`sources` 값에 experience 경로가 있으면 별도 경고 (`related` 는 탐색 링크로 허용).

## 블록 분할

본문(frontmatter·코드펜스 제외)을 다음 블록으로 나눈다:

1. 표 행 1줄 = 1블록. 단, 표 **위 도입 문단**에 experience 참조가 있으면 표 전체가 그 참조에 묶인다.
2. 목록 항목 1개(들여쓴 이어짐 줄 포함) = 1블록. 목록 **바로 위 도입 문단**(`:` 로 끝나거나 빈 줄 없이 붙은 줄)에 참조가 있으면 목록 전체가 묶인다.
3. 그 외 빈 줄로 나뉜 문단 = 1블록.

(2026-09-29 실례: `storm-surge/01` §3.3 는 도입 줄에 링크, 아래 목록에 수치; `tides/02` 는 표 아래 줄에 링크 — 아래 3의 "표 직후 문단" 도 표에 묶는다.)

3'. 표 **바로 다음 문단**이 experience 참조만 담은 출처 줄(예: "전체 분석: [experience/…]")이면 표 전체가 묶인다.

## 수치 토큰

- 경고 대상: 단위 붙은 수 — `mm`, `cm`, `m`, `km`, `mm/yr`, `cm/yr`, `°C`, `℃`, `%`, `m/s`, `cm/s`, `mb`, `hPa`, `σ`, `/decade`, `/yr`, `/dec`; 배율 `\d+(\.\d+)?\s*[×x배]`; `R²`/`R^2` 뒤 수.
- 제외: 연도·날짜(`YYYY`, `YYYY-MM(-DD)`, `YYYY-YYYY`), `§` 번호, `line N`·`:N` 행 참조, 커밋 해시, 표·그림 번호(`표 3-5`, `그림 7-64`), 버전 문자열, 코드펜스·인라인 코드 안.

## 출력·종료 코드

- 참조가 묶인 블록에 수치 토큰이 있으면 `path:line: [exp-num] <experience 대상> | <수치들> | <블록 앞 80자>`.
- 기본 **warn 모드**: 경고를 출력하고 exit 0. `--strict` 면 경고 1건 이상 시 exit 1. 승격(기본 strict 전환)은 별도 사용자 결정.
- 억제: 블록 안 `<!-- exp-num-ok: <사유> -->` (사유 필수, 빈 사유는 경고). 독립 출처로 뒷받침되는 값에만, 주장 단위로 검토 후 쓴다. 산술 도출값이라도 전제가 experience 에 기대면 억제 대상이 아니다(`currents/04` ±11.25° — 전제 '16방위 = 최근접 22.5° 구간' 이 experience 검증).

## 인수 조건

1. 단위 테스트 `tools/test_validate_experience_numbers.py` — fixture 로 위 블록 규칙 1·2·3·3'·억제·layer-4 제외·날짜/§/행참조 제외를 각각 검증.
2. **재현율**: `git worktree` 로 `2ad55e4^` 를 풀어 트리 전체 실행 시, survey8 위반 17건 중 같은 블록/도입부 묶음에 해당하는 것은 전부 잡는다. 못 잡는 건(링크와 떨어진 수치)은 목록으로 보고 — 설계상 한계로 기록.
3. **현재 HEAD 오탐**: 트리 전체 실행 경고를 전부 나열하고 Claude 가 한 건씩 판정. 진짜 위반은 별도 정정 게이트로, 오탐은 규칙 조정 또는 억제 주석.
4. `validate-all.sh` 전체 실행 시간 증가 1초 이내.
5. 다른 validator 출력·종료 코드 불변.

## 알려진 한계

- 링크와 떨어진 위치에 옮겨진 수치(2026-09-29 재감사 잔여 4건 유형)는 못 잡는다 → L4 감사가 계속 담당.
- experience 링크 없이 수치만 복제한 경우도 못 잡는다 (출처 누락 → 기존 L4 UNSOURCED 판정 몫).

## v2 — 적대 검토 반영 (2026-09-29, `review-result.md`)

v1 기준 추정 재현율 10/18 → 아래 반영 시 16/18. 채택 여부는 Claude 판정.

| # | 지적 | 반영 |
|---|---|---|
| 1 | 분모 오류(본문 18 + frontmatter 2), 누락 허용이 열려 있음 | **채택** — `cases.json` 에 18건 case ID·기대(탐지/누락) 고정, 본문 재현율과 frontmatter 경고 분리 |
| 2 | 표 셀은 단위 없이 수만(`tides/02` 헤더에만 `mm/yr`) | **채택** — 표 헤더 단위를 열에 상속. "같음" 같은 행 간 출처 상속은 **보류**(한계로 기록) |
| 3 | 인접 인용 관계 누락 | **부분 채택** — ⑴ 명시 표지("같은 experience 노트", "전체 분석:", "같음, §N") ⑵ 바로 다음 형제 목록 항목이 experience 출처 줄이면 앞 항목에 귀속 ⑶ "결과:" 문단 뒤 요약 문단. 모두 제목·무관 블록에서 끊음 |
| 4 | 토큰 구멍 | **채택** — 참조 추출을 인라인 코드 제거보다 먼저. 무차원 통계(비·ratio·R²·상관) 뒤 수, `$…$` 수식 안 `= 수 단위`. 제외 우선순위 명시(연도 패턴은 단위가 붙으면 수치로 본다) |
| 5 | `sst/05:190–192` 오탐, 산술 자동 면제 불가 | **채택** — 자동 면제 없음, 주장 단위 억제만. `currents/04` 는 정정 대상으로 되돌림 |
| 6 | basename 매칭 ≠ 링크 해석 | **채택** — wikilink·경로를 실제로 해석(`[[README]]` 는 로컬 우선), 확장자 없는 경로 지원. 면제는 frontmatter `layer: 4` 만(파일명 `NN-applied-*` 만으로 면제하지 않음) |
| 7 | staged 계약·회귀 불완전 | **채택** — `--staged` 는 index 내용(`git show :path`)을 읽고 experience 이름 목록도 index 기준. 부분 staging fixture. 회귀 스냅샷 `afc08c8^:storm-surge/01` 139–142 탐지, `0859062^:storm-surge/05` 232–233 탐지(234 는 전파 한계로 기록) |

### 알려진 한계 (추가)

- 수치 없는 정량 결론("SST 최대 trend", "빈도·강도 모두 증가")은 결정적 검사로 못 잡는다 → L4 감사.
- 표 안 "같음" 행 간 출처 상속.

### 인수 조건 (v2, v1 을 대체)

1. 단위 테스트 — v1 항목 + 표 열 단위 상속, 명시 표지 3종, 형제 목록 귀속, 무차원 통계·`$` 수식, 인라인 코드 속 참조, `[[README]]` 로컬 해석, layer 명시 우선, index 읽기·부분 staging.
2. `cases.json` 18건: 기대 탐지 ≥ 15, 기대와 다른 결과 0 (기대 누락은 사유와 함께 고정).
3. 회귀 스냅샷 2종(위 7).
4. 현재 HEAD 트리 전체 경고 전부 나열 → Claude 판정.
5. `validate-all.sh` 실행 시간 +1초 이내, 다른 validator 불변.

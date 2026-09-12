# Claude Fable 5.1 검토

요청·응답 모델: `claude-fable-5-1` (`modelUsage` 확인). 보조 사용 모델은 원본 JSON 참조.

**판정: 반영 가능.** 8개 candidate와 실제 대상 frontmatter를 대조한 결과 blocker는 없다. 아래는 비차단 관찰 3건과 검토 한계다.

## 확인 결과 (질문 1–7)

1. **README 역할·검색 범위**: 서술한 하위 경로가 모두 실존한다. `experience/`의 failure-patterns·heuristics·playbooks, `data/khoa-analysis`·`sst-global`, `research/`의 inbox·digests·watchlist·prompts·seeds, `tools/`의 llm-wiki-poc·llm-wiki-audit·resume-gate·validate-*, `standards/kds-64` 34개, `textbook/md` 20개, `models/*/raw/source_code`·FUNWAVE `raw/manuals`. 검색 제외·강등 서술은 `tools/llm-wiki-poc/fts5_index.py:19-31`의 ALLOW 집합과 raw DENY, textbook/md RAW_DEMOTE와 일치한다. `references/collect.py:4-17`은 arXiv → research/inbox 수집기가 맞다.
2. **root INDEX 보존**: 테이블 행은 before 72 → candidate 80이며 증가분 8은 새 섹션 헤더 2줄 + 6행이다. 링크 행 60개는 동일하다. waves 구행의 항목은 후보 waves README 상태표에 그대로 남아 있다. 07의 1402.1555·1403.3766, 08의 2511.12711·2606.03231·Doppler/refraction/blocking·SWAN action balance/QC, MPT 74정점, KHOA 284, Holthuijsen이 모두 있다. WW3 SMC Issue #1600은 `04-code-and-tools.md:91` §3.4에 있다. XBeach 구행의 456/281/22/153, 보충103, 충돌3·미검증10·문서207, 40/8/1, 코어118 구별, Q3D·기호 보충은 후보 XBeach README 본문에 유지된다. 정보 소실 없음.
3. **models INDEX**: 13개 진입점 실존, 기존 10개 도메인·격자 셀 동일. 상태 문구를 실제 frontmatter grep으로 대조했다. draft-unsourced는 XBeach 4편뿐이고 source-needed는 models 전체에 없다. has_source_needed true는 ADCIRC 14·SWAN 1·ROMS 1·CADMAS 3, false는 ADCIRC 7·EFDC 1·ROMS 3·CADMAS 3·XBeach 9로 model-state-summary와 표기가 맞는다. 부재를 "미감사"로, false를 "갭 없음 표기"로 구별했고 감사 완료는 AUDIT-LEDGER로 분리했다.
4. **waves·XBeach 탐색**: waves 표의 V·[공시]·[갭없음]·[미감사] 18건 전부 frontmatter와 일치한다. 02·03·ch08·09·11·harbor는 필드 부재, ch10·time-integration만 false. XBeach의 V* 14건은 `source_correction_human_approval: not-issued` 14파일과 정확히 같다. 새 표에 오른 노트 중 false 플래그 파일은 없어 [미감사] 표기가 모두 맞다. D 4편, 승인 미발급, R1–R4 미완은 progress.json의 R1·R2·R4 open과 일치한다. "링크가 근거를 승계하지 않는다"는 문장이 두 파일 모두에 있다.
5. **template·포인터**: CONVENTIONS §8의 README+01 2파일 원칙과 일치한다. plan.md 포인터·AGENTS.md는 "현재 사용자 지시 우선, 자동 실행 아님"을 명시한다.
6. **12문항**: 탐색 측정으로 한정돼 있다. N09/N10의 locator_basis는 "아니오"이며 후보 XBeach README에 승인·전수식 검증 불가 문장이 추가됐다. N11/N12는 기존 링크 회귀만 보고 SST의 sst-stewart 깨진 링크는 out-of-scope-findings에 남겼다.
7. **범위**: 8파일 밖 변경·새 과학 주장·완료 선언 없음.

## 비차단 관찰

- **XBeach README**: 본문이 09-12에 수정했다고 적은 `xbeach_q3d.md`와 `xbeach-nonhydrostatic-report-2010.md`는 frontmatter에 `source_correction_*` 필드가 없어 새 표에서 각각 `V`·표기 없음이다. 범례대로 frontmatter를 그대로 읽은 결과이고 같은 파일의 "연결 분석 보충" 절이 수정 사실을 공개하므로 은폐는 아니다. 다만 대상 노트 frontmatter의 기존 공백이라 P1에서 고칠 수 없다. 원하면 범례 뒤에 "09-12 수정 중 frontmatter 정정 필드가 없는 노트 2편은 V로 표시된다" 한 줄 추가.
- **XBeach README**: manual-notes 8편 중 `02-delilah-reference.md`·`03-holland-coast-reference.md`가 표·본문 어디에도 링크되지 않는다. before에도 없었으므로 회귀는 아니다. 선택 사항으로 "공식 자료·판본" 행에 추가 가능.
- **models INDEX**: 상태 출처가 `_staging`의 2026-09-13 스냅샷 JSON이다. frontmatter가 바뀌면 표가 조용히 stale해진다. 날짜가 명시돼 있어 허용 범위지만 갱신 규칙은 P2 쪽에서 정하는 편이 낫다.

## 검토 한계

- 셸 실행 없이 읽기만 했으므로 install-manifest의 sha256, structural-checks의 canonical 627·불변 292 미변경, evaluate_navigation.py 재실행은 검증하지 못했다. 4/12→12/12 수치는 JSON을 신뢰하되 candidate의 entry_link_lines가 실제 후보 파일에 존재함은 확인했다.
- 작업 트리 plan.md가 이미 수정 상태이므로 before 사본과 현재 파일의 동일성은 별도 확인이 필요하다.
- 링크 대상 실존은 후보에 새로 추가된 링크에 한해 확인했고, 링크 무결성 전수는 pre-commit validator 몫이다.
- 과학적 내용·원문 지지 여부는 이번 검토 대상이 아니다.

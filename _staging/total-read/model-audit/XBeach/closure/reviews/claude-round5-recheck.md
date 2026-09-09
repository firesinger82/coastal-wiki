# Claude Sonnet 최종 수정 재검토

## 검증 결과: 지정된 6개 수정사항 모두 해소 확인, 잔여 블로커 없음

### P1 — ID 오배정 수정 (`manual-code-adjudications.json`)
`items[].finding_ids`를 topic별로 역인덱싱해 확인한 결과, 지정된 6건 모두 정확히 반영됐다:

- `nuh`: XH102 제거, XH100 포함 → `{XH008, XH059, XH100, XH135}`
- `bedfriction`: XH101 제거, XH100 포함 → `{XH009, XH060, XH100, XH135, XH136}`
- `dilatancy`: XH066 제거, XH067 포함 → `{XH013, XH067, XH103, XH141}`
- `adaptation-time`(Ts): XH098 제거 → `{XH063, XH138}` (098은 어디에도 재연결되지 않음)
- `posdwn`: XH069 제거, XH075 포함 → `{XH022, XH075, XH112, XH147}`
- `dthetaS_XB`: XH070 제거, XH078 포함 → `{XH023, XH078, XH113, XH147}`

`exact-207.jsonl`에서 XH098 원문("roelvink2 dissipation … reef fw … eight-harmonic waveform")을 대조하면 실제로 파랑 소산/reef 마찰/파형 항목이며 adaptation-time과 무관하다는 Codex 지적이 맞았고, 지금은 제거되어 있다. XH098/101/102/066/069/070 6개 ID 모두 8개 topic 어디에도 재등장하지 않아, 단순 재배치가 아니라 근본 오류를 없앤 것으로 확인된다.

### finding_bindings의 원문(original text) 보존 여부
`exact-207.jsonl`의 `finding` 필드(원문)를 XH100/135/136/147에서 직접 대조:
- XH100·XH135: Chezy/Manning/ks vs `chezy`/`bedfriccoef` 불일치 **그리고** `nuh=0.1`이 Smagorinsky 계수/차원적 점성 두 가지로 기술된다는 내용이 한 문장 안에 공존하는 복합 주장(compound claim) — `bedfriction`·`nuh` 두 topic 모두와 정당하게 링크됨.
- XH136: 마찰식(`cf=g/C`, Manning 지수)만 다루며 `nuh` 언급 없음 — `bedfriction` 단일 topic만 링크되어 과다연결 없음.
- XH147: posdwn 부호 규약 **그리고** 각도 기준축 두 사실이 한 문장에 있는 복합 주장 — `posdwn`·`dthetaS_XB` 두 topic 모두와 정당하게 링크됨.

지정된 "topic만 명명, 복합 주장 내 나머지 원문은 보존" 원칙이 실제 원문 내용과 일치한다.

### P2 — dictionary 덮어쓰기 방지 (`build_disposition.py`)
`adjudication_by_id = defaultdict(list)`(245행)로 ID→list 구조를 사용하며, 368~394행에서 `adjudication_by_id[item["finding_id"]]` 전체를 순회해 `source_code_adjudications`에 리스트로 채운다(단일 덮어쓰기 아님). output 파일 두 곳에서 직접 확인:
- `all-207-disposition.jsonl`: XH100/XH135/XH147의 `source_code_adjudications`가 각각 2개 원소 리스트(예: XH147 = posdwn 판정 + dthetaS_XB 판정)로 저장됨.
- `all-207-disposition.csv`: `source_code_adjudication_topics` 열이 `nuh;bedfriction`(XH100/135), `bedfriction`(XH136 단독), `posdwn;dthetaS_XB`(XH147)로 정확히 일치하고, `source_code_adjudications_json` 열도 두 판정문 전체를 그대로 보존.

JSONL·CSV 두 산출물이 서로 다른 표현(리스트 객체 vs `;` 구분 문자열+JSON 직렬화)이지만 담긴 근거 리스트는 동일하며, 요청된 "XH100/135/147 각 2 topics" 조건과 정확히 부합한다.

### 최종 canonical 4개 파일(`closure/canonical/models/XBeach/manual-notes/`)
XH098/101/102/066/069/070이 여전히 문서에 등장하지만(D-006, D-023, D-037, M-001, M-009, K-017 review-group 항목), 이는 document-level 발견(finding) 자체의 정당한 소재이지 — 잘못된 source-topic 라벨과의 연결이 아니다. 각 항목 본문을 직접 확인한 결과 nuh/bedfriction/posdwn/dthetaS_XB/adaptation-time 등 topic 이름이 이 항목들 옆에 부당하게 붙어있지 않으며, 순수 문서 불일치 서술(판정: 판본 한정 사실로 채택 등)만 담겨있다. 즉 "관련 없는 topic 링크 잔존" 문제는 애초에 canonical 문서 자체가 아니라 `manual-code-adjudications.json`(소스 측 topic 인덱스)에 있었던 문제였고, 그 인덱스는 위에서 확인한 대로 수정 완료됐다. `master-manual.md` 303행에도 이 수정 사실("cross-format-partial 15건 → DOCX 원본 block/OLE 결박 text-extract로 대체")이 명시돼 있다.

### B1/B2 — source_locator 재작업
`document-canonical-mapping.json`의 `citation_kind` 분포: `cross-format-pdf-page-alignment` 74, `original-docx-block` 26, `original-doc-text-extract` 6, `original-pdf-page` 101 (합계 74+26+6+101=207, 전수 일치). 요청에서 언급한 "DOCX 원본 block 26 + OLE 결박 text 6 = 32"가 정확히 존재하며, `cross-format-partial`이라는 부정확 카테고리는 더 이상 남아있지 않다(대체된 상태).

### "136 review groups ≠ 136 unique facts, 207 independent IDs" 서술
`REPORT.md` 104행에서 "26 denominator IDs, 29 ID-topic links … XH100, XH135, XH147 each retain two adjudications"로 정확히 서술됐고, 176행에서 "136 review groups and all 207 IDs. 'Review group' is an assembly unit, not a unique scientific-fact count"로 명시적으로 구분해 오해 소지를 없앴다(34+22+24+56=136, 53+35+32+87=207 각각 검산 일치).

### validate_closure.py 실행 결과
전 항목 `PASS`: baseline 292, attribution 1472 links, manual-code topics=8/raw-quotes=22, source evidence=60, documents 207/207/207/207 매핑 일치, closure integrity 전 지표 정합. FAIL 없음.

### 결론
지정된 P1(ID 오배정 6건), P2(dictionary 덮어쓰기), 그리고 B1/B2(source_locator 32건 재작업, 136/207 서술 구분) 모두 코드·데이터·prose 3단 교차검증에서 일관되게 수정이 반영되어 있음을 확인했다. 요청 범위 내에서 남은 구체적 블로커는 없다.

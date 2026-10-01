# XBeach R2 — 수식 위치별 근거 결속 계획 v1 (2026-10-01)

사용자 지시(2026-10-01): R1 마무리 후 "XBeach R2로 진행". 범위·종료 조건은 09-12 동결 [remaining.json](../remaining-20260912/remaining.json) R2 와 [equation-scope.json](../remaining-20260912/equation-scope.json) 그대로 — **번호 캡션 위치 443곳**(Kingsday 174 · Master 179 · 비정수압 보고서 90). 443곳은 풀어야 할 식 443개도, 결함·미판독 수도 아니다(README §37). 새 입력·부속 도구 내부(MathType 글꼴 원인 등)·저자 의도 추측 없음.

## 1. 산출물: 위치별 처분표 `R2-dispositions.jsonl`

위치 1곳 = 레코드 1개. `id` 는 equation-scope 의 caption id(같은 번호의 다른 위치는 별개 ID로 보존).

| `disposition` | 조건 | 필수 근거 |
|---|---|---|
| `reuse_contract` | 기존 경계 계약(build-mode-20260912/contracts.json 등 14곳)이 이 위치를 다룬다 | 계약 파일·항목 |
| `reuse_judgment` | 기존 판정(XH001–207 처분·manual-notes 앵커·nonhydro 기호 영수증·침투식 비교)이 이 위치의 의미·구현 관계를 이미 설명 | 판정 ID·앵커 + 이 위치와의 대응 근거 |
| `code_correspondence` | 식의 구현 위치를 소스에서 확인 | 식 내용(시각 판독 근거) + 소스 `file:line` 인용 + 대응 설명(항·계수·부호·조건) |
| `version_difference` | 같은 번호·식이 판본 간 다르거나 구현과 판본이 갈림 | 두 판본 위치·차이 |
| `source_body_missing` | 원본에 식 본체가 없음(빈 수식·빈 필드) | 원본 근거(빈 문단·빈 객체 영수증) |
| `outside_implementation` | 문서상 정식이지만 구현 범위 밖(이론 유도·대안식·미구현 기능) | 문서 문맥 + 소스에 없음의 근거(검색 범위 명시) |
| `unresolved` | 위로 설명 불가 — **미완 유지** | 사유·부족한 근거 |

모든 레코드: `equation_content`(시각 판독: 렌더 페이지/미리보기 이미지 경로 + 판독 내용), `inline_symbols`(인접 inline 기호와 그 의미 연결), `context`(문단 요지), `evidence[]`(path·위치·quote·sha256).

## 2. 실행

1. **근거 꾸러미 생성(결정적)**: 캡션 위치 → 직전 수식 객체(OLE/Native locator·미리보기 이미지) → 렌더 페이지 번호 → 주변 문단 텍스트 → 같은 페이지 inline 기호 객체 → 기존 판정 후보(XH·계약·영수증) 를 묶은 `packets/<id>.json`. 기존 산출물(display-fields·cached-fields·full-visual-read records·document-canonical-mapping)만 사용.
2. **파일럿 30곳**(세 문서·계약 있음/없음·같은 번호 반복 포함, seed 고정) → Codex 가 수식 이미지를 실제로 읽는지(시각 판독 근거가 남는지)·토큰·품질 측정 → 배치 크기 결정.
3. **본 판정**: Codex `gpt-6.1-sol`(토큰 대량) 배치 순차. 매 배치 결정적 검사.
4. **적대 검증**: `gpt-6.1-sol` max(R1과 동일 운영) — `code_correspondence`·`version_difference`·`outside_implementation`·`unresolved` 전건, `reuse_*`·`source_body_missing` 층화 20%. REFUTED/NARROWED 전건 정정·재검증, 같은 규칙 오류는 전체 스윕. 멈춤 규칙은 R1 §5 와 같다.

## 3. 결정적 검사 `check_r2.py`

443 id 전부 1회, disposition 유효·필수 근거 role 존재, evidence path·행/페이지 실재·quote 일치·sha256, 재사용 대상(계약·XH·앵커) 실재, 시각 판독 근거 이미지 경로 실재.

## 4. 완료 조건과 한계

- R2 **처분 기록 완료** = 위 검사·검증 통과.
- R2 **종결**은 `unresolved` 목록과 영향에 대한 **사용자 수용 결정** 후. 모델 의미·구현 관계를 설명 못 한 항목이 남으면 미완(remaining.json done_when).
- 시각 판독은 AI 판독이며 수학적 검증이 아니다. 글꼴 네모·빈 수식의 내부 원인은 조사하지 않는다.
- 결과의 `models/` 반영은 R2 단위 SCOPED EDIT 1회. R3 전체·R4 는 자동 착수 안 함. 사람 승인 발급 없음.

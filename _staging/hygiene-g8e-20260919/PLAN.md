# G8e 작업환경 흔적 정리 — 계획 (2026-09-19)

- 작성: Claude Opus 5 (사용자 명시 승인 — 이번 작업 한정 Fable 5.1 규칙 예외)
- 근거: Jev 전수 스윕(p≥0.9 수동 분류) + `validate-canonical-hygiene.py` G8e WARN 82줄 + `numerical_models/` 상대경로 14줄
- 범위: concepts/·models/ canonical 노트의 **작성자 작업환경 흔적 표현**만. 내용·출처·citation_status 는 바꾸지 않는다.
- 완료 조건: `validate-all.sh` OK · G8e WARN 0 · canonical(비-raw)에서 `numerical_models/` 0 · 링크 무결성 OK · Codex review · 사용자 승인 후 커밋

## 처리 규칙

| ID | 대상 | 처리 | 줄 수(약) |
|---|---|---|---|
| R1 | ADCIRC manual-notes 메타데이터 `- local path: not downloaded yet` | 줄 삭제 (같은 블록 `link:` 가 공식 URL 제공) | 11 |
| R2 | `- local path: raw/code/adcirc/…` (repo 에 없는 옛 로컬 레이아웃) | 줄 삭제. 적용 전 각 파일에 `link:` 존재 확인, 없으면 공식 URL 로 대체 | 9 |
| R3 | XBeach manual-notes `- local path:` 블록(하위 `numerical_models/…` 목록) | repo 에 있는 사본은 repo-상대 경로(`models/XBeach/raw/manuals/pdfs/XBeach_manual_{master,kingsday}.pdf`)로, 없는 것은 R4 표기 | 3 블록 |
| R4 | `XBEACH_MANUAL.md` = 위키 밖 비공식 실무 노트("local note") | 표기를 "XBeach 실무 매뉴얼 노트(`XBEACH_MANUAL.md`, v1.24 Halloween 대상, 위키 미보관)"로 중립화. "Current local interpretation:" → "Interpretation (practical manual note):", "(Current) locally confirmed values:" → "Values documented in the practical manual note:", "Current local practical default" → "Practical default per the practical manual note", "the local note" → "the practical manual note" | ~45 |
| R5 | 작성자 환경 상태·작업 메모 | 줄 삭제: "local runnable … not yet attached in this workspace"(2), "whether local scripts or notebooks can reproduce…", "local machine does not currently have the package installed"(2), "already part of the local revalidation track", "local scripts still treat it as a reconstruction attempt…", ADCIRC `adcirc.md:82` "first controlled DT-sensitivity experiment draft" | 8 |
| R6 | 서술형 "this workspace" | "in this wiki's XBeach notes" / "in these notes" | 3 |
| R7 | 개인 사례 공간 예약(G8d 계열, 정규식 미탐지) | 삭제: `currents/06:174` 한국 적용 사례 체크박스 · `sst/05:247` experience 노트 예약 · `tides/05:338-342` "experience 승격 조건" 체크박스 블록 · `tides/06:207-208` 사용자 경험 예약 · `EFDC ch2:595` SGZ 적용 경험 · `efdc-grid:168` Korean case cross-ref · `efdc-current-mismatch` §Candidate Evidence To Add Later(헤딩+4) · `efdc-parameter-glossary:175` local calibration experiments · XBeach web-refs §5 한국 적용(헤딩+2) | ~20 |
| R8 | `numerical_models/…` 로컬 보관소 상대경로 | repo 에 대응 사본이 있으면 repo-상대로(XBeach PDF·`boundaryconditions.F90` → `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90`, EFDC `MPI_*` → `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_*`), 없으면 중립 서술(EFDC manifest: "DSI EFDC+ 배포본 `manual/`", ADCIRC docs-site: "위키 repo 밖 보관"). `xbeach.md` §"Confirmed Local Source Availability" → §"Source availability" + repo-상대 경로. ADCIRC manifest Next Steps 3번(legacy 91GB import 결정) 삭제 | 14 |
| R9 | 표현만 중립화 | FUNWAVE build 노트 "본 위키 머신(…)" → "검증 환경: WSL2 Ubuntu 24.04, RTX 5070(sm_120)"(빌드 포팅 노트라 환경 사양 자체는 기술 정보로 유지) · ADCIRC 13/18 `year: … plus current local practice` → 뒷부분 삭제 · ADCIRC manifest:45 "(writer 머신; …)" 삭제 · EFDC glossary:21-22 "local EFDC+ manual RAG" → "the EFDC+ manual", "future local experiments" → "setup choices" · `xbeach_q3d:165` "current local source guard" → "current source guard" · XBeach boundary:99 "updated local source" → "the source (`boundaryconditions.F90`)" · morphology:20 "confirmed local manual stack and current local example/test context" → "the XBeach manual stack and example/test context" | ~10 |

## 변경하지 않는 것 (별도 결정 대상으로 기록)

- `concepts/sst/05-examples.md` §4 예제 4(2026-05-23 작성자 실행 결과, 한국 13정점 MHW) 와 §6 item 4 — 절 단위 판단이 필요해 이번 범위 밖. 절대규칙 8 검토 후보.
- XBeach 실무 매뉴얼 노트 기반 해석 목록의 `citation_status: verified` 적정성 — 출처 감사 대상(위키 미보관 비공식 자료). 이번엔 표기만 중립화.
- `01-local-manual-stack.md` 파일명·제목 — 링크 영향이 있어 보류.
- note_author·promote 로그의 모델 서명(Claude Opus 4.7 등) — CONVENTIONS 의 기존 관행.
- 일반 how-to 체크리스트(`adcirc-storm-surge-requirements-checklist.md:32`), 정화 정책 안내문("…experience/ 에 카테고리화 — 본 canonical 미수록"), "(작성 예정) 한국 사례" stub 12건.
- ADCIRC manifest Next Steps 4번(RAG ingest) — 흔적은 아니나 stale. 보고만.

## 후속

- 정리 완료 후 G8e 정규식에 `numerical_models/` 추가(재유입 차단) — 별도 커밋.

## 개정 1 — Codex 적대 검토(MODIFY) 반영 (2026-09-19)

| 지적 | 반영 |
|---|---|
| R1 실제 10줄 | 정정 |
| R2 `link:` 유효성 | `13-nws13`은 `link:`를 "ADCIRC docs `nws13.rst`·`fort22.rst` + testsuite `adcirc_katrina-2d-nws13` 종합"으로 중립화 후 local path 삭제. `adcirc-baseline-anatomy`는 바로 아래 `testsuite name:`이 출처라 local path만 삭제 |
| R3 필드명 | `- local path:` → `- archived copies:`(repo-상대) / `XBEACH_MANUAL.md`는 "위키 미보관" 명시 |
| R4 출처 귀속 강화 금지 | "local note"라고 **원문이 명시한** 곳만 "practical manual note"로. "(Current) locally confirmed values/examples"는 "… confirmed in the source basis above"(혼합 출처 §Source Basis 그대로 가리킴), "Current local interpretation:" → "Working interpretation:"(해석 한정 유지). 문자열별 치환표는 적용 스크립트에 고정 |
| R5 누락 | `02-delilah:74` → "whether a runnable reproduction exists among the official online example assets" |
| R7 과잉 삭제 | `currents/06:174` 유지. `xbeach web-refs:62` 유지(63 "(별도 작업) … calibration"만 삭제). `efdc-current-mismatch` §Candidate Evidence: 개인 실험 3줄만 삭제, case studies 줄은 "published harbor or estuary case studies"로 |
| R9 줄번호·frontmatter | EFDC glossary 22–23 정정. FUNWAVE frontmatter `verification_method`의 "본 위키 WSL2" → "WSL2" |
| 누락: EFDC `local … RAG` 4파일 | "retrieved EFDC+ manual passages"로 중립화(검색 도구 명칭 제거, 대조 수준은 그대로) |
| 누락: XBeach 01:43 runtime | "confirms local executable/runtime existence and" 삭제 |
| 01 제목 | 제목·메타 title을 "XBeach Manual Stack"으로(파일명 유지) |
| ADCIRC manifest RAG TODO | 흔적으로 인정 — Next Steps 3·4번 삭제 |

**별도 결정으로 이관(이번에 수정 안 함)**: ADCIRC `13-nws13`·`18-nws13` 개인 JMA-MSM 운영 기록 분리 / ADCIRC `27–29` 개인 스크립트 기반 도구 평가 / FUNWAVE 개인 실행 결과(FLAT·INI_GAU) / SST §4·§6 item 4 / XBeach 해석 목록 `verified` 출처 감사 / sst `05:247`.

**완료 조건 보강**: G8e 탐지 0건을 별도 명령으로 확인 · R3/R8 비-md 경로 존재 검사 · 정규식 밖 재검색(`RAG`, `numerical_models/`, `this workspace`).

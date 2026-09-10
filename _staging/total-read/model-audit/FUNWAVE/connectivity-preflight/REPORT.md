# FUNWAVE connectivity preflight — 전량 인벤토리와 판독 증거 대조

작성일: 2026-09-09. 이 문서는 연결성 분석 전 준비 원장이다. `models/FUNWAVE/raw/`는 읽기만 했고 canonical·raw·기존 영수증은 수정하지 않았다.

## 판정 기준

- 인벤토리 분모는 사전 제외 없는 raw 아래 모든 regular file이다. 내장 `.git`, 생성물, 사례 데이터·출력, 그림·영상, PDF, archive를 모두 포함한다.
- `exact` 판독 증거는 현재 `path + sha256`가 기존 레코드와 일치하고 `read_status=complete`인 경우다. 최종 코드 레코드는 `comprehension_status=complete`도 요구했다.
- R1은 현재 `fable5` code run, R2는 `codexaudit` code run이다. 둘이 모두 있는 파일만 `two_independent_code_reads_exact=true`다.
- `document_read_exact`는 현재 pending의 doc semantic record다. `legacy_complete_read_exact`는 `records/all-FUNWAVE-*.jsonl`의 과거 complete record다. partial은 complete로 올리지 않았다.
- `mechanical_inspection_exact`는 MIME·수치격자·바이너리 검사일 뿐 의미 판독으로 세지 않았다. 동일 SHA의 다른 경로, 생성 전처리본, GPU/TVD 동명 파일도 서로 판독을 상속하지 않는다.
- canonical 노트가 PDF를 인용하거나 `doc-extracted/` 변환본이 존재해도 raw PDF SHA와 직접 묶인 complete record가 없으면 raw PDF를 exact read로 올리지 않았다.

## 정확한 분모와 현재 증거

raw는 **1,435파일, 454,627,384 bytes**, 고유 SHA-256 **1,197개**다. 두 내장 Git 저장소 메타데이터 59개를 포함한다. Git 스냅샷은 TVD `b4c322e7582035ee19df8e6409a3dfedaff1cb96`, GPU `7f892bad51c1fecdcc8c45ab6694b997684ac143`다.

원자료 뿌리는 `models/FUNWAVE/raw/source_code/FUNWAVE-TVD/`, `models/FUNWAVE/raw/source_code/FUNWAVE-GPU/`, 독립 변환 매뉴얼 `models/FUNWAVE/raw/manuals/funwave_tvd_3.0.md`다. TVD 안의 문서 뿌리는 `doc/`와 benchmarks/simple_cases에 흩어진 PDF·README·입출력 설명이다. 명시적 third-party/vendor 하위 트리는 발견하지 못했지만, 이것을 소유권 판정으로 확대하지 않았으며 모든 파일을 그대로 분모에 보존했다.

| 항목 | 파일 | 해석 |
|---|---:|---|
| 과거 `277` code-extension 분모 | 277 | `.f/.f90/.m/.py` 등 코드 확장자만 센 값. 전체 raw 분모가 아니다. |
| R1 exact + R2 exact + crosswalk exact | 243 | 두 독립 코드 판독과 crosswalk가 모두 현재 SHA에 일치한다. |
| 과거 complete만 있고 R1/R2 쌍이 없는 코드 | 34 | solver/case 29, MATLAB script 5. 최소 1회 의미 판독은 있으나 현재 완료 정의의 2독립 판독은 아니다. |
| doc semantic read exact | 421 | text/data/generated interface 등을 doc axis로 판독한 기록이다. PDF 39개 전수 판독을 뜻하지 않는다. |
| legacy complete exact | 101 | 위 34 code를 포함한 과거 단독 complete 기록이다. |
| 의미 판독 complete 합집합 | 765 | 경로별 중복 제거. code 277은 최소 1회 모두 포함한다. |
| 의미 판독 미증명 | 670 | raw 전체 기준. 이 중 569개는 기계 검사만 존재하며 101개는 complete/기계 검사 어느 쪽도 없다. |
| 문서·매뉴얼 미증명 | 93 | PDF 39 + 문서/build text 54. 정확한 목록은 별도 파일이다. |

따라서 PROGRESS의 `분모 277`, `코드94`, `~34%전체·76%코드`는 하나의 재현 가능한 지표가 아니다. 277은 코드 확장자 분모이고, 현재 최종 증거에는 dual-read code 243개가 있다. `94`를 재현하는 파일 집합이나 현재 SHA 원장은 찾지 못했다. 이는 실제 판독보다 진행표가 뒤처진 상태다. 다만 34개가 2독립 판독을 갖지 않는 실제 gap이고, 전체 raw 1,435개로 넓히면 670개가 의미 판독 미증명이다.

과거 preflight manifest 964행은 raw 944개와 canonical note 20개를 함께 담았다. 현재 raw에서 path+SHA가 일치하는 항목은 944개다. 이 또한 전체 raw 분모가 아니다.

## 중복과 스냅샷

- 동일 SHA 중복은 **180그룹, 418경로**다. 모든 경로는 인벤토리에 남겼고 [`exact-duplicate-groups.csv`](exact-duplicate-groups.csv)에 묶었다.
- `funwave-work/build/pre/*.f90` 34개는 `src/*.F`와 stem이 같은 생성 전처리 counterpart다. 34개 모두 byte-identical은 아니며 별도 SHA와 판독 상태를 유지했다.
- GPU/TVD `src`의 동명 source counterpart는 29쌍이다. 서로 다른 저장소·커밋의 파일이므로 alias로 접지 않았다.
- 두 종류의 비동일 관계는 [`snapshot-alias-ledger.csv`](snapshot-alias-ledger.csv)에 분리했다.

## 실제 남은 판독

- 2독립 코드 판독 보충: [`remaining-legacy277-without-two-independent-reads.txt`](remaining-legacy277-without-two-independent-reads.txt) 34개. solver/case 29개와 script 5개 목록도 각각 분리했다.
- 최소 1회 complete 의미 판독 기준으로 code와 script의 미판독은 0개다. 이 값은 2독립 완료를 뜻하지 않는다.
- 문서·매뉴얼 exact complete 미증명: [`remaining-document-manual-unread.txt`](remaining-document-manual-unread.txt) 93개.
- raw 전체 exact complete 미증명: [`remaining-all-semantic-unread.txt`](remaining-all-semantic-unread.txt) 670개. 이미지·미디어 129, case data/output 158, other text 118, generated build 80, VCS metadata 59, 문서/build text 54, PDF 39, 기타 binary/data 32, archive 1이다.

가용 도구는 `file`, `sha256sum`, `strings`, `readelf`, `objdump`, `nm`, `git`, `tar`, `gzip`, `pdfinfo`, `pdftotext`, `pdftoppm`, `ffprobe`, `python3`이다. 이후 판독 때 text/source는 기존 400-line chunk manifest 방식, PDF는 페이지 고정 `pdfinfo` + `pdftotext -layout`과 필요한 페이지 렌더, archive는 member manifest 후 각 member 해시, object/module/executable은 `file` + strings/symbol table, 이미지·영상은 시각/프레임 판독을 써야 한다. 기계 메타데이터만으로 의미 판독 완료를 선언하면 안 된다.

## 사람 영수증 보존

기존 `supplement-decisions.json`은 **38/38 approved**, approver `firesinger`, 승인일 `2026-08-31`이며 기존 검증기를 현재 원본에 대해 다시 실행해 `authority=38 approved=38 pending=0 mechanical_fails=0`, PASS를 확인했다. 이 38개 중 FUNWAVE 항목은 37개이고, raw source finding은 36개다. 나머지는 FUNWAVE canonical manual note 1개와 EFDC source 1개다. 따라서 PROGRESS의 `HG38승인`은 공유 supplement corpus 전체 수이며 FUNWAVE raw 파일 수가 아니다. 원본 38개는 변경하지 않았고 [`human-receipts-preservation.json`](human-receipts-preservation.json)에 범위만 sidecar로 기록했다.

전체 파일별 SHA·크기·MIME·분류·중복·모든 증거 플래그와 증거 파일 경로는 [`raw-inventory-read-coverage.csv`](raw-inventory-read-coverage.csv)에 있다. 이 preflight는 다음 FUNWAVE 판독 작업의 입력이며 connectivity 결과를 포함하지 않는다.

# XBeach `raw/manuals` 판독 증거 preflight

날짜: 2026-09-09  
범위: `models/XBeach/raw/manuals/`의 일반 파일 87개만 조사했다. `raw/source_code/` 456개와 FUNWAVE 본 판독·연결 분석은 이 작업 범위가 아니다. 원본은 수정하지 않았다.

## 판정 기준과 결과

현재 파일을 다시 SHA-256 해시하고, 과거 판독 원장의 `path`와 `sha256`가 모두 같은 경우에만 직접 증거로 연결했다. 경로만 같거나 제목만 같은 자료는 승계하지 않았다. 87개 모두 현재 경로·SHA와 일치하는 직접 기록이 있다.

| 구분 | 파일 수 | 의미 |
|---|---:|---|
| 직접 `complete` | 74 | 현재 경로·SHA의 과거 기록이 전량 판독을 주장 |
| 직접 `partial` | 7 | 수치 격자의 전 행·열 및 min/max는 파싱했으나 개별 값 전사는 하지 않음 |
| 직접 `failed` | 6 | PDF 4개와 EOT 폰트 2개 |
| SHA 결박 변환본으로 보충 | 3 | 직접 실패 PDF 중 3개는 원본 SHA가 같은 전체 텍스트 변환 및 페이지 대응 증거가 있음 |
| 유효 complete 합집합 | **77** | 직접 74 + 변환본 보충 3 |
| 보수적으로 남긴 파일 | **10** | partial 7 + EOT 2 + 변환 불완전 PDF 1 |

전체 크기는 64,378,412 bytes이며 고유 SHA는 75개다. 3개 중복 SHA 그룹에 15개 경로가 들어간다. JONSWAP 입력은 각각 8개와 5개의 동일 바이트 복제이고, EOT 두 경로도 동일 바이트다. 각 경로는 원장에 독립적으로 남겼으며 중복을 이유로 87개 분모를 줄이지 않았다.

직접 실패였으나 변환본으로 보충한 PDF는 다음 세 개다.

- `pdfs/XBeach_manual_kingsday.pdf` → `XBeach_manual_kingsday.md`
- `pdfs/XBeach_manual_master.pdf` → `XBeach_manual_master.md`
- `reports/non-hydrostatic_report_draft.pdf` → `non-hydrostatic_report_draft.md`

이 승계는 제목 유사성이 아니라 PDF의 정확한 content SHA와 `closure/document-inventory/source-map.json`의 원본 결박 및 page-aware 변환 이력을 근거로 한다. 따라서 CSV에는 직접 상태 `failed`와 파생 상태 `complete-via-sha-bound-conversion`을 모두 보존했다.

## `Parallellization_report.pdf`는 미완료

`reports/Parallellization_report.pdf`의 직접 기록은 `failed`다. `XBeach-X00.jsonl`의 `Parallellization_report.md` 기록은 623줄을 읽었다고 쓰지만, 동시에 변환본에서 보고서 산문의 거의 전부가 빠졌고 205개 이미지 참조를 시각 판독하지 않았으며 speedup 곡선·표와 domain-decomposition 맥락을 잃었다고 명시한다. 그러므로 `lines_read`만으로 PDF 전체 의미 판독을 인정하지 않고 `incomplete-conversion-image-gap`으로 남겼다. 완료하려면 205개 이미지와 각 물리 페이지의 본문·도표를 원 PDF에 대해 시각 검사해야 한다.

## 남은 10개와 판독 범위

정확한 경로 목록은 `remaining-incomplete-or-unread.txt`에 있다.

- 수치 격자 7개: `bed.dep`, `x.grd`, `y.grd`, `chezy.txt`. 과거 기록은 모든 행·열의 형상과 전체 값의 min/max를 기계 파싱했지만 개별 값을 전사하지 않았다고 명시한다. 목적이 byte-level 전량 검증이면 전체 토큰 파싱·개수·비유한값·checksum 증거로 닫을 수 있고, 모든 값을 사람이 의미 판독했다는 기준이면 그대로 partial이다.
- EOT 2개: 같은 SHA의 Font Awesome 바이너리다. 텍스트 의미 판독 대상이 아니므로 글리프/테이블 파서 또는 바이너리 무결성 분류가 필요하다. 현재 원장 상태는 `failed`로 보존했다.
- PDF 1개: 위 Parallelization 보고서다. 원 PDF의 페이지별 시각 판독이 필요하다.

## 207 findings와 전량 판독 증거의 구별

`closure/document-inventory`의 **207**은 87개 manuals 파일 수나 전체 문서 판독 수가 아니다. 불변 `XBeach-X00.jsonl`의 14개 변환 문서에서 나온 unresolved 286건 가운데 HIGH 207건만 고른 finding 분모다. 그 207건 전부는 세 저작물의 여섯 표현(DOC(X) 텍스트와 PDF 변환본)에만 속한다. 나머지 X00 8개 표현은 HIGH 행이 없으며, manuals 트리의 나머지 파일을 포함하지 않는다.

따라서 `exact-207.jsonl`, locator, disposition, canonical anchor의 완결성은 **207개 finding 처리 증거**다. 이것만으로 manuals 87개 전량 판독을 증명할 수 없다. 이 preflight에서는 세 PDF에 대해서만 별도의 정확한 원본 SHA 결박과 전체 텍스트/page-aware 변환 이력을 보충 증거로 사용했다. Parallelization 변환본은 X00에 포함되지만 변환 손실 자체가 기록되어 있어 보충 완료로 올리지 않았다.

## 산출물과 재현

- `manuals-read-coverage.csv`: 87개 전 행의 현재 SHA, 크기, MIME, 직접 기록·범위·reader, 변환본 보충, 중복 경로, 최종 상태
- `remaining-incomplete-or-unread.txt`: 보수적 미완료 10개 정확 경로
- `summary.json`: 계수 및 증거 원장 목록
- `validation.json`: 경로 집합과 87개 SHA 재검사 결과
- `build_manuals_preflight.py`: 원장에서 ledger를 다시 만드는 스크립트

`validation.json`은 현재 raw 경로 집합 일치, 87개 전부의 SHA 재검사, 행 수 87을 확인하며 `pass: true`다.

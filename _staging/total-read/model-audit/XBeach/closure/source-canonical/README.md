# XBeach source-canonical closure

이 디렉토리는 사람 승인된 source supplement 중 `XBeach-000..005`와 `XBeach-T00`의 정확한 60건만 다룬다. 기존 103건 manifest·decision·crosswalk·receipt는 수정하지 않는다.

- `evidence-ledger.json`: `(source_sha256, audit_id)`별 원본 바이트 SHA, 물리 LF 행, raw span SHA, LF 정규화 인용문·SHA, manifest와 최종 crosswalk 판정
- `mapping-ledger.json`: 60건 전량의 canonical 앵커와 기존 관련 노트
- `canonical/models/XBeach/source-analysis/xbeach-source-audit-supplements.md`: 보호 경로 설치 전 canonical 초안(`citation_status: source-needed`)
- `build_source_canonical.py`: 위 세 산출물을 불변 입력에서 다시 만드는 검증 builder

검사 결과: 60/60 source byte SHA 일치, 60/60 LF 행 인용문·manifest quote SHA 일치, 60/60 crosswalk 최종 판정 존재, `STANDS=40`, `NARROWED=20`, concrete canonical anchor=60.

소스는 Fortran 모듈 22개와 test 1개가 CRLF, Python/Mako 3개가 LF이다. 행 번호는 양쪽 모두 LF byte를 기준으로 센다. CRLF source의 `raw_span_sha256`은 CR을 보존하고, `lf_normalized_quote_sha256`만 manifest의 정규화 인용문과 비교한다.

남은 검토 경계: 이 작업은 정적 source/crosswalk 통합이며 compiler·runtime 재현을 새로 수행하지 않았다. 최종 Claude 검토 전에는 `verified`로 승격하지 않는다.

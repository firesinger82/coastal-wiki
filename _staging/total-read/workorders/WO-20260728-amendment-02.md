# WO-20260728 부속서 02 — 수치벌크 mechanical 예외 (2026-08-04 사용자 승인)

부속서 01 과 동일 취급: `numeric-bulk-exceptions-20260804.txt` (sha256 939869dd4556da5c79fabae273a3deef2e1bf61e96c4ade784d39c758fa78bc5, 8건)의
path 는 semantic 판독 대신 mechanical 레코드(records/numbulk-*.jsonl)로 충족. shard 구성·순서
불변, 게이트 v3.4 가 두 예외 목록을 자동 skip. 경위: doc-FUNWAVE-001 의
coupling_file_v2.txt(104,019행·521chunks)가 단일 컨텍스트 완독 불가 + Codex 판독자의 정직한
제출 거부로 적발. semantic 분모 1,883 → **1875**.

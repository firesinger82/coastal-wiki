# WO-20260728 부속서 01 — 수치격자 mechanical 예외 (2026-07-28 사용자 승인)

원 WO 는 동결 유지. 본 부속서는 사용자 승인(2026-07-28 "수치격자 예외 승인")에 따른 변경만 기록한다.

1. `reread-queue/numeric-grid-exceptions-20260728.txt` (sha256
   `c3e330974b3ea1c50cb5d11f8bd516e5e668b27f50f489e2b88691186015a899`, 355건, 전부 doc축)의
   파일은 LLM semantic 재판독 대상에서 제외하고 mechanical 레코드
   (`records/numgrid-{FUNWAVE,LISFLOOD-FP}-20260728.jsonl`)로 충족한다. 판정 기준·필드는 SPEC.md
   "게이트 3항 예외 확장" 절에 고정.
2. doc축 shard 의 validator 판정: shard 구성원 중 본 예외 목록 소속 path 는 semantic 레코드
   대신 위 mechanical 레코드 존재로 충족된 것으로 본다(FUNWAVE 0-byte 10건과 동일 취급).
   shard 분할·이름·순서는 변경하지 않는다.
3. 축별 LLM 판독 분모 갱신: doc 1,346 → **991** (FUNWAVE 701→423, LISFLOOD-FP 645→568).
   전체 semantic 재판독 = **1,883** (code 679 · doc 991 · web 145 · note 68).
4. §6 맹검 표본 크기의 기저는 semantic 레코드 모집단이므로 표본 수는 선택 시점 모집단
   (1,883)에 `ceil(N × 0.10)` 을 재적용해 **189**로 갱신한다. seed·층화·알고리즘은 불변.

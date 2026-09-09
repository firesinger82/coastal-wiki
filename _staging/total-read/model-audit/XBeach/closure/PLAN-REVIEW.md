# 계획 적대 검토 반영

2026-09-09 · Codex gpt-5.6-sol · 스레드 `01a0852c-b1b8-7921-9364-b14dc03cad5e`.

아래는 검토 요약이다. 원 실행은 `/codex:adversarial-review` companion을 사용했다. 최초 판정 needs-attention.

| 지적 | 반영 |
|---|---|
| 13/207 분모 미고정 | 최종 crosswalk 13개를 deferred-inputs.json으로 고정. X00 HIGH 207개를 원본 행/항목 ID·해시와 함께 고정 후 개별 처리 |
| vendor/generated 축 혼동 | component/origin과 생산형태를 분리하고 파일 기반 근거 사용; shard 귀속 금지 |
| 기존 crosswalk 변경 시 HG 해시 무효 | 기존 자료 292개 해시 고정, 후속 resolution/attribution sidecar만 작성 |
| 설치·완료 권한 모호 | 실제 canonical diff와 대상별 사전/사후 해시·백업·rollback을 준비해 보호 경로에 한정 설치. 사용자 명시 요청의 실행 허가와 새 사실 판정의 HG 승인을 구분 |

새 HG 승인 영수증을 발급하지 않는다. 기존 103개 승인 패킷은 역사적 승인 범위 그대로 보존하고 canonical의 근거 검증은 독립 적대 검토·인용 대조·설치 검증으로 기록한다. 검토 권고를 이유로 이미 허가된 canonical 편집을 다시 묻지 않는다.

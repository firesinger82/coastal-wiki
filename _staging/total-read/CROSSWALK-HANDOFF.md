# 재개 핸드오프 — crosswalk 파일럿부터 (다음 세션 진입점)

> 상태: 맹검 감사 269/269 완료·커밋(813b896). 병합 설계 확정·커밋(bb9737e).
> **다음 = crosswalk 실행 미착수.** 설계는 [MERGE-PLAN-20260827.md](MERGE-PLAN-20260827.md).

## 재개 절차
1. 트리 잠금 해제: `sudo chown -R firesinger:firesinger _staging/total-read && sudo chmod -R u+w _staging/total-read`
   (코퍼스 `models/` 는 read-only 유지). 종료 시 재잠금 `sudo chown -R root:root … && sudo chmod -R a-w …`.
2. 설계 MERGE-PLAN-20260827.md 정독(오버레이+delta 승격, 전량 union 폐기).

## 파일럿 = EFDC-000 crosswalk (첫 작업)
- 1차 run: `pending/reread-20260728/reread20260728-code-EFDC-000-fable5-*` (6파일)
- 감사 run: `pending/reread-20260728/reread20260728-code-EFDC-000-codexaudit-*` (6파일)
- 목표: 파일별 1차 unresolved ↔ 감사 unresolved 처분 분류
  (equivalent/confirmed_delta/distinct_unconfirmed/rejected/conflict).
- ★검증 포인트: **DETTMP(aaefdc.f90 L924) 가 confirmed_delta 로** 분류되고, 나머지 겹침이
  equivalent 로 묶이는가. 이게 파이프라인 정합 확인.
- 실행자 편향방지(설계 §2): crosswalk 판정 에이전트에 벤더라벨 제거 + A/B 순서 무작위.
  confirmed_delta 는 제안이 아니라 **원문 span 대조로만 확정**.
- 신설 필요: crosswalk 스키마 + `verify_crosswalk.py`(원본 finding 유실 0·처분 전건 부여).

## 자산 위치
- 감사 레코드 269: `pending/reread-20260728/*codexaudit*/` (커밋됨)
- run 레지스트리: `audit-run-registry/` (1차·감사 run_id)
- 판정 스크립트: `adjudicate_20260826.py`(참고), `audit_select_20260826.py`(표본)
- disposition 로그: `AUDIT-DISPOSITIONS-20260826.md` (shard별 material 후보)
- 확정 delta 현재 1건: EFDC aaefdc.f90 DETTMP 특이점검사 무력화(역수 후 ==0).

## 파일럿 후
shard별 crosswalk 확대 → confirmed_delta supplement 승격 → WO amendment(supplement 게이트)
→ WO §7 canonical 선택 → `/codex:review` 최종. 이후 대형 3모델(ADCIRC/ROMS/Delft3D)은 별건.

## 주의
- 원본 2층(1차·감사 pending) 불가침. 병합은 새 artifact.
- Codex 감사자는 Bash 백그라운드라 완료 자동알림 없음 — 게이트 status 로 확인.
- 세션 크론(session-only)은 무인 야간엔 조용히 멈출 수 있음(2026-08-26/27 13h 공백 실측).
  장기 무인은 `/schedule`(클라우드) 검토.

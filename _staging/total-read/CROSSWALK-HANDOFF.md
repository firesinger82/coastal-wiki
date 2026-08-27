# 재개 핸드오프 — crosswalk (다음 세션 진입점)

> 상태: 맹검 감사 269/269 완료·커밋(813b896). 병합 설계 확정·커밋(bb9737e).
> **✅ 파일럿 EFDC-000 완료(2026-08-27)** — 스키마 [CROSSWALK-SCHEMA.md](CROSSWALK-SCHEMA.md)·검증기 `verify_crosswalk.py`·빌더 `build_crosswalk.py` 신설,
> 출력 `records-crosswalk/reread-20260728/*.crosswalk.json`(6파일·130 dispositions·PASS). DETTMP=confirmed_delta 검증.
> **다음 = 운영 shard 확대(blinded 단일 subagent).** 설계는 [MERGE-PLAN-20260827.md](MERGE-PLAN-20260827.md).

## ✅ 첫 blinded shard = FUNWAVE-000 (code) 완료 (2026-08-27)
- 파이프라인: `blind_shard.py`(라벨제거·seeded A/B무작위·후보쌍) → blinded subagent → `finalize_shard.py`(un-blind 병합) → `verify_crosswalk.py`.
- 49파일·438 dispositions·PASS. distinct_unconfirmed 206·base_only 153·equivalent 78·**confirmed_delta 1**(convert.f B3 OOB, span확정). delta 후보 23(HIGH) 중 1 confirmed·1 refuted(sediment.F B3, span-gate 기각 실증)·21 pending.
- 산출: `records-crosswalk/reread-20260728/FUNWAVE-000/`(+`_provenance/` 에 blinded_input·keymap·verdicts·delta_candidates 동결, `DELTA-REVIEW.md`). 파일럿은 `.../EFDC-000/` 로 네임스페이스 이동.

## ✅ 감사쌍 보유 shard 전량 완료 (2026-08-27) — crosswalk 생성 단계 종료
7 shard 전부 blinded 파이프라인 완주·커밋·verify PASS:
| shard | 축 | 파일 | dispositions | confirmed_delta |
|---|---|---|---|---|
| EFDC-000(파일럿) | code | 6 | 130 | 1 (DETTMP) |
| FUNWAVE-000 | code | 49 | 438 | 1 (convert.f B3) |
| FUNWAVE-001 | code | 49 | 337 | 1 (breaker.f90 B1) |
| FUNWAVE-002 | code | 49 | 289 | 0 |
| FUNWAVE-003 | code | 48 | 319 | 0 |
| FUNWAVE-004 | code | 48 | 478 | 1 (breaker.F B1) |
| FUNWAVE-note-000 | note | 20 | 151 | 1 (manual STATIONS_FILE) |

- 누적: dispositions 2,142 · **confirmed_delta 5**(전량 원문/코드 span 확정, base 미검출) · span-gate 기각 2(sediment.F B3·mkxyz B0).
- 산출: `records-crosswalk/reread-20260728/<SHARD>/`(+`_provenance/`·`DELTA-REVIEW.md`). 스크립트: `blind_shard.py`·`finalize_shard.py`·`verify_crosswalk.py`(레코드파일명 키).

## 다음 작업 = supplement 게이트(§3) — pending HIGH 승격
- 각 shard `_provenance/delta_candidates.json` 의 **in-scope pending HIGH** 를 원문 span 재확인 → confirmed_delta 승격(특히 FUNWAVE-004 25건·001 16건: fluxes/init U4xL·wavemaker Beta_gen/phi1·mod_vessel NumVessel·mod_meteo/precipitation rollover 등).
- 승격분 → canonical supplement(hash 고정·원본 미변경, §3) → WO amendment(§5.3 완결게이트 좁게 개정) → §7 canonical 선택 → `/codex:review`.
- .m/.py 후처리 스크립트 HIGH 는 범위밖(#8) — supplement 목적지 없음.
- 대형 3모델(ADCIRC/ROMS/Delft3D)은 별건(감사 미실시 — 먼저 감사 run 필요).

---
## (완료) 파일럿 = EFDC-000 crosswalk

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

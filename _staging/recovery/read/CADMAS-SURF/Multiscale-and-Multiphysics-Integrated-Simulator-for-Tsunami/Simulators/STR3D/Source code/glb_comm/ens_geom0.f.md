---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/ens_geom0.f
lines: 19
sha256: 0756314b4027faaeae6f45963fdcd344ebe155c14a9c970d8bff7322e0359187
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ens_geom0.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 모듈 M_VAL과 인수 KK(*)·파일명 FLNAME을 선언한다(1–7). ENS_GEOM으로 형상 출력을 위임하고 GRID·IELM을 해제한다(9–12). 원문: `      SUBROUTINE ENS_GEOM0(KK,IFG,FLNAME,NLEN,ICHK)` (1); `      USE M_VAL` (3); `      CHARACTER*256 FLNAME` (5); `      DIMENSION KK(*)` (7); `      CALL ENS_GEOM(KK,IFG,FLNAME,NLEN,ICHK)` (9); `      DEALLOCATE( GRID )` (11); `      DEALLOCATE( IELM )` (12). |
| 14–19 | 시작 시 1행 ens_geom0 루틴 안. ICHK가 2인 분기에서 KK(92)·KK(81)가 각각 양수일 때 IBEL·IPFC를 해제한다(14–17). 루틴을 종료한다(19). 원문: `      IF( ICHK == 2 ) THEN` (14); `        IF( KK(92) > 0 ) DEALLOCATE( IBEL )` (15); `        IF( KK(81) > 0 ) DEALLOCATE( IPFC )` (16); `      ENDIF` (17); `      END` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–16: GRID·IELM 해제는 무조건 실행한다. IBEL·IPFC 해제는 ICHK와 KK 값으로 결정하며 ALLOCATED 검사는 이 파일에 없다.

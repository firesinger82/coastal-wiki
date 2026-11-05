---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/outsol0.f
lines: 33
sha256: 2275dd1ca3528fa84e8a2cc4da6f36724902d2666fd564f810eea99d28fa296c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# outsol0.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | M_VAL·파일 단위 배열과 SIGP·EPSP·PRNSIGP 포인터를 선언한다(3–7). 해석: 세 포인터는 각각 응력·변형률·주응력 데이터에 대응한다. SIGP(6,NNOD)·EPSP(6,NNOD)·PRNSIGP(3,NNOD)를 할당·수집한다(9–15). 원문: `      SUBROUTINE OUTSOL0(NNOD,IFL)` (1); `      USE M_VAL` (3); `      DIMENSION IFL(*)` (5); `      REAL(8),POINTER :: SIGP(:,:),EPSP(:,:),PRNSIGP(:,:)` (7); `      ALLOCATE( SIGP(6,NNOD) )` (9); `      ALLOCATE( EPSP(6,NNOD) )` (10); `      ALLOCATE( PRNSIGP(3,NNOD) )` (11); `      CALL GATHER_NODAL_D(SIGP,6)` (13); `      CALL GATHER_NODAL_D(EPSP,6)` (14); `      CALL GATHER_NODAL_D(PRNSIGP,3)` (15). [11-04 전수 검증 정정] |
| 17–28 | 시작 시 1행 outsol0 루틴 안. ICW=0으로 설정한다(17). 파트 1..NP_ENS(2)에 WTSOL을 호출한다(19–22). NP_ENS(2)·(3)·(4)의 합 다음부터 NP_ENS(6)개 파트에 같은 WTSOL을 다시 호출한다(24–27). 두 호출은 같은 SIGP·EPSP·PRNSIGP 배열을 전달한다. 원문: `      ICW = 0` (17); `      IPS = 1` (19); `      IPE = NP_ENS(2)` (20); `      CALL WTSOL(SIGP,EPSP,PRNSIGP,NNOD,IPS,IPE,NG_ENS,IG_ENS,IFL,ICW)` (22); `      IPS = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + 1` (24); `      IPE = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + NP_ENS(6)` (25); `      CALL WTSOL(SIGP,EPSP,PRNSIGP,NNOD,IPS,IPE,NG_ENS,IG_ENS,IFL,ICW)` (27). [11-04 전수 검증 정정] |
| 29–33 | 시작 시 1행 outsol0 루틴 안. 세 결과 배열을 해제하고 종료한다(29–33). 원문: `      DEALLOCATE( SIGP )` (29); `      DEALLOCATE( EPSP )` (30); `      DEALLOCATE( PRNSIGP )` (31); `      END` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

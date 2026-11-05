---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/outsoil0.f
lines: 18
sha256: 990e0a26b34d70e9807f071943e6d1555a29f4335f304c29f2ea185a653743a6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# outsoil0.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | M_VAL과 VELP 포인터를 선언한다(3–5). VELP(3,NNOD)를 할당하고 GATHER_NODAL_D로 3성분을 수집한다(7–9). 원문: `      SUBROUTINE OUTSOIL0(NNOD,IFL)` (1); `      USE M_VAL` (3); `      REAL(8),POINTER :: VELP(:,:)` (5); `      ALLOCATE( VELP(3,NNOD) )` (7); `      CALL GATHER_NODAL_D(VELP,3)` (9). |
| 11–18 | 시작 시 1행 outsoil0 루틴 안. IPS는 NP_ENS(2)·(3)·(4)의 합에 1을 더한 값이다(11). IPE는 같은 합에 NP_ENS(6)을 더한 값이다(12). 해석: VELP는 간극수 플럭스(pore water flux) 데이터이다. WTSOIL에 결과·범위·파트 절점 목록을 넘기고 배열을 해제한다(14–18). 원문: `      IPS = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + 1` (11); `      IPE = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + NP_ENS(6)` (12); `      CALL WTSOIL(VELP,NNOD,IPS,IPE,NG_ENS,IG_ENS,IFL)` (14); `      DEALLOCATE( VELP )` (16); `      END` (18). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

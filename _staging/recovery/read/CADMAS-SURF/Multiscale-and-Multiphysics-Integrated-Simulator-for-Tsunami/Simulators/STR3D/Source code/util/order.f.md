---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/order.f
lines: 20
sha256: 66bfc0dd63ef1c58044c76adbd6c58cc058e5a7c2db08a5e24203347623f7d31
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# order.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | ORDER의 인수와 IA(*)를 선언한다(1–3). I=1..N에서 IB<IA(I)이면 SHIFTB0(IA,I,N,1)을 호출한 뒤 IB를 삽입하고 표지 10으로 이동한다(5–9). IB=IA(I)이면 즉시 반환한다(10–12). ELSE는 없다. 두 조건이 모두 거짓이면 다음 I를 처리한다. 9행 GOTO의 대상은 17행 표지 10이다. 루프 종료·주석을 포함한다. 원문: `      SUBROUTINE ORDER(N,IA,IB)` (1); `      DIMENSION IA(*)` (3); `      DO I=1,N` (5); `        IF( IB .LT. IA(I) ) THEN` (6); `          CALL SHIFTB0(IA,I,N,1)` (7); `          IA(I)=IB` (8); `          GOTO 10` (9); `        ELSEIF( IB .EQ. IA(I) ) THEN` (10); `          RETURN` (11); `        ENDIF` (12); `      ENDDO` (13). [11-04 전수 검증 보완] |
| 15–20 | 시작 시 1행 ORDER 루틴 안. 앞 루프에서 이동·반환하지 않으면 IA(N+1)에 IB를 덧붙인다(15). 삽입 분기의 표지 10과 합류하여 N을 1 증가시킨다(17). 주석·RETURN·END를 포함한다. 원문: `      IA(N+1)=IB` (15); `   10 N=N+1` (17); `      RETURN` (19); `      END` (20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

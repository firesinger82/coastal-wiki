---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/ex_pload4.f
lines: 36
sha256: 63030e935b0f56e585fef06d32577bbdeedf9d5ec82d0f884cc5fac3248d9802
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ex_pload4.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | EX_PLOAD4의 연속 인수·암시적 형 선언·배열 범위와 집합·항목 수 초기화. 원문: 연속문(1–2): `      SUBROUTINE EX_PLOAD4(NIPL4W,NNPL4W,IPL4W,NPL4W,PLD4W,NIPL4,IPL4` <br> `     &                    ,NPL4,PLD4,LELM,LNOD)`; `      IMPLICIT REAL*8(A-H,O-Z)` (4); 연속문(5–6): `      DIMENSION IPL4(2,NIPL4),NPL4(4,*),PLD4(4,*),IPL4W(2,*),NPL4W(4,*)` <br> `     &         ,PLD4W(4,*),LELM(*),LNOD(*)`; `      IP = 0` (8); `      JP = 0` (9). |
| 11–36 | EX_PLOAD4 루틴 안. ADDSET3로 하중 집합 구간을 얻는다. LELM으로 변환한 요소 번호가 양수인 PLOAD4 항목만 복사한다. 선택한 두 절점 번호는 양수일 때 LNOD로 변환한다. 비어 있지 않은 집합의 끝 위치와 최종 개수를 저장한다. 원문: `      DO I = 1, NIPL4` (11); `        JP0 = JP` (12); `        CALL ADDSET3(JS,JE,IPL4,I)` (13); `        DO J = JS, JE` (14); `          LE = LELM(NPL4(1,J))` (15); `          IF( LE > 0 ) THEN` (16); `            JP = JP + 1` (17); `            NPL4W(1,JP) = LE` (18); `            NPL4W(2:3,JP) = 0` (19); `            IF( NPL4(2,J) > 0 ) NPL4W(2,JP) = LNOD(NPL4(2,J))` (20); `            IF( NPL4(3,J) > 0 ) NPL4W(3,JP) = LNOD(NPL4(3,J))` (21); `            NPL4W(4,JP) = NPL4(4,J)` (22); `            PLD4W(:,JP) = PLD4(:,J)` (23); `          ENDIF` (24); `        ENDDO` (25); `        IF( JP > JP0 ) THEN` (26); `          IP = IP + 1` (27); `          IPL4W(1,IP) = IPL4(1,I)` (28); `          IPL4W(2,IP) = JP` (29); `        ENDIF` (30); `      ENDDO` (31); `      NIPL4W = IP` (33); `      NNPL4W = JP` (34); `      END` (36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/ex_spc1.f
lines: 30
sha256: cbf41587d2936d17af2dd7c40702cf78f8e8be604893e97ad9f132cb9755ee1f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ex_spc1.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | EX_SPC1의 연속 인수·7행 조건 배열 선언과 개수 초기화. 원문: 연속문(1–2): `      SUBROUTINE EX_SPC1(NISP1W,NNSP1W,ISP1W,NSP1W,NISP1,ISP1,NSP1,LNOD` <br> `     &                  ,NNODW)`; `      DIMENSION ISP1(2,NISP1),NSP1(7,*),ISP1W(2,*),NSP1W(7,*),LNOD(*)` (4); `      IP = 0` (6); `      JP = 0` (7). |
| 9–30 | EX_SPC1 루틴 안. ADDSET3로 집합 구간을 얻는다. LNOD 변환 번호가 1부터 NNODW까지인 항목만 뽑는다. 나머지 여섯 행을 복사하고 비어 있지 않은 집합의 끝 위치와 최종 개수를 저장한다. 원문: `      DO I = 1, NISP1` (9); `        JP0 = JP` (10); `        CALL ADDSET3(JS,JE,ISP1,I)` (11); `        DO J = JS, JE` (12); `          LN = LNOD(NSP1(1,J))` (13); `          IF( LN > 0 .AND. LN <= NNODW ) THEN` (14); `            JP = JP + 1` (15); `            NSP1W(1,JP) = LN` (16); `            NSP1W(2:7,JP) = NSP1(2:7,J)` (17); `          ENDIF` (18); `        ENDDO` (19); `        IF( JP > JP0 ) THEN` (20); `          IP = IP + 1` (21); `          ISP1W(1,IP) = ISP1(1,I)` (22); `          ISP1W(2,IP) = JP` (23); `        ENDIF` (24); `      ENDDO` (25); `      NISP1W = IP` (27); `      NNSP1W = JP` (28); `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

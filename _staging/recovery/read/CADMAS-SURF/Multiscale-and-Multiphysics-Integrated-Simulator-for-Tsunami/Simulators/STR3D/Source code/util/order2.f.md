---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/order2.f
lines: 25
sha256: b49ede7abfd9f8d4a054a0201e0aba3efb6eb28ee4ddd4c8c47e284e4ece9fe6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# order2.f — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | ORDER2의 인수와 IA(*)를 선언한다(1–3). I=IS..N에서 IB<IA(I)이면 SHIFTB0(IA,I,N,1)을 호출하고 IB를 삽입한다(5–8). NEXTIS=I+1 뒤 표지 10으로 이동한다(9–10). IB=IA(I)이면 NEXTIS=I+1 뒤 표지 20으로 이동한다(11–14). ELSE는 없다. 두 조건이 모두 거짓이면 다음 I를 처리한다. 10행 GOTO의 대상은 20행 표지 10이다. 13행 GOTO의 대상은 22행 표지 20이다. 루프 종료·주석을 포함한다. 원문: `      SUBROUTINE ORDER2(N,IS,IA,IB)` (1); `      DIMENSION IA(*)` (3); `      DO I=IS,N` (5); `        IF( IB .LT. IA(I) ) THEN` (6); `          CALL SHIFTB0(IA,I,N,1)` (7); `          IA(I)=IB` (8); `          NEXTIS=I+1` (9); `          GOTO 10` (10); `        ELSEIF( IB .EQ. IA(I) ) THEN` (11); `          NEXTIS=I+1` (12); `          GOTO 20` (13); `        ENDIF` (14); `      ENDDO` (15). [11-04 전수 검증 보완] |
| 17–25 | 시작 시 1행 ORDER2 루틴 안. 앞 루프에서 이동하지 않으면 IA(N+1)에 IB를 덧붙이고 NEXTIS=N+2로 둔다(17–18). 표지 10은 N을 1 늘리며 표지 20은 IS에 NEXTIS를 대입한다(20–22). 따라서 중복 분기는 N 증가를 건너뛴다(13·20–22). 주석·RETURN·END를 포함한다. 원문: `      IA(N+1)=IB` (17); `      NEXTIS=N+2` (18); `   10 N=N+1` (20); `   20 IS=NEXTIS` (22); `      RETURN` (24); `      END` (25). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

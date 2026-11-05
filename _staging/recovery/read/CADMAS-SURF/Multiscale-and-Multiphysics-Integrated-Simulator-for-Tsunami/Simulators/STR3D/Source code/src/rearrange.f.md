---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/rearrange.f
lines: 42
sha256: 1c5b8f6d5b984c7bd6c6514d7d464e9438d8746503ab1980b1f393ed890e66f8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rearrange.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | REARRANGE 입구와 배열 선언이다(1–4). LAST(IFR)에서 시작해 IPREV를 따라 이동한다(6–8·34–38). 삽입 위치 JP와 넘겨올 JADD를 정한다(10–17). IDX를 오른쪽으로 밀고 열 번호를 삽입한다(19–32). 마지막 블록이 NSIZ에 도달하면 새 NEXT·IPREV·LAST 연결을 설정한다(23–28). 원문: `      SUBROUTINE REARRANGE(IDX,NSIZ,NIDX,N,IPREV,NEXT,LAST,IFR,IB,JB`<br>`     &                    ,JCOL)` (1–2); `      DIMENSION IDX(NSIZ,*),N(*),IPREV(*),NEXT(*),LAST(*)` (4); `      IP = LAST(IFR)` (6); `      DO` (8); `        IF( IP == IB ) THEN` (10); `          JP = JB` (11); `          JADD = JCOL` (12); `        ELSE` (13); `          JP = 1` (14); `          IPR = IPREV(IP)` (15); `          JADD = IDX(NSIZ,IPR)` (16); `        ENDIF` (17); `        IF( IP == LAST(IFR) ) THEN` (19); `          IF( N(IP) > 0 ) IDX(JP+1:N(IP)+1,IP) = IDX(JP:N(IP),IP)` (20); `          IDX(JP,IP) = JADD` (21); `          N(IP) = N(IP) + 1` (22); `          IF( N(IP) == NSIZ ) THEN` (23); `            NIDX = NIDX + 1` (24); `            NEXT(IP) = NIDX` (25); `            IPREV(NIDX) = IP` (26); `            LAST(IFR) = NIDX` (27); `          ENDIF` (28); `        ELSE` (29); `          IDX(JP+1:NSIZ,IP) = IDX(JP:NSIZ-1,IP)` (30); `          IDX(JP,IP) = JADD` (31); `        ENDIF` (32); `        IF( IP == IB ) THEN` (34); `          EXIT` (35); `        ELSE` (36); `          IP = IPREV(IP)` (37); `        ENDIF` (38); `      ENDDO` (40); `      END` (42) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23–27: 새 블록에 NEXT·IPREV·LAST를 설정한다. 이 분기에는 새 블록의 N(NIDX)를 초기화하는 문장이 없다.

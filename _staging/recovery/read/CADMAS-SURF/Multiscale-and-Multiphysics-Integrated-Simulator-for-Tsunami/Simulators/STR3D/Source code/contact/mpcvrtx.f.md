---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpcvrtx.f
lines: 39
sha256: 6097f0e59c33372580ca0a90e7afa2674fac5e6ae274ed672f281d3f7520d2a1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpcvrtx.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | MPCVRTX는 정점(vertex) 접촉 구속 주소를 만든다. INDOF의 세 방향 중 0이 아닌 값이 있으면 오류를 출력하고 ERRSTP(50,ITO)를 호출한다(6–9). 선언과 주석을 포함한다. 원문: `      SUBROUTINE MPCVRTX(IDEP,IDX,IRH,IS,NS,MA,IVRQ,IELQ,INDOF,ITO)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION IDEP(2,3),IDX(2,3),IRH(2,*),IELQ(4,*),INDOF(3)` (4). `      IF( INDOF(1).NE.0 .OR. INDOF(2).NE.0 .OR. INDOF(3).NE.0 ) THEN` (6). `        WRITE(ITO,'(/X,A)') 'SLAVE POINT IS CONSTRAINED.'` (7). `        CALL ERRSTP(50,ITO)` (8). `      ENDIF` (9). |
| 11–21 | 시작 시 1행 MPCVRTX 루틴 안. IVRQ=0일 때 NS의 각 방향에 MA의 같은 방향 한 항을 배정한다(13–20). 각 IDX의 시작과 끝 주소는 같다(16–17). 원문: `      IF( IVRQ .EQ. 0 ) THEN` (11). `        DO 100 I=1,3` (13). `          IDEP(1,I)=NS` (14). `          IDEP(2,I)=I` (15). `          IDX(1,I)=IS+I-1` (16). `          IDX(2,I)=IS+I-1` (17). `          IRH(1,I)=MA` (18). `          IRH(2,I)=I` (19). `  100   CONTINUE` (20). |
| 22–39 | 시작 시 1행 MPCVRTX 루틴·11행 `IF( IVRQ .EQ. 0 ) THEN`의 ELSE 분기에 진입한다. 이 IF는 37행 `ENDIF`에서 닫힌다. NS의 세 방향 각각에 사각형 네 절점의 같은 방향을 IRH에 기록한다(24–35). IDX는 방향마다 네 항 구간이다(28–29). 분기 종료와 END를 포함한다. 원문: `      ELSE` (22). `        IP=0` (24). `        DO 200 I=1,3` (25). `          IDEP(1,I)=NS` (26). `          IDEP(2,I)=I` (27). `          IDX(1,I)=IS+4*(I-1)` (28). `          IDX(2,I)=IS+4*I-1` (29). `          DO 210 J=1,4` (30). `            IP=IP+1` (31). `            IRH(1,IP)=IELQ(J,IVRQ)` (32). `            IRH(2,IP)=I` (33). `  210     CONTINUE` (34). `  200   CONTINUE` (35). `      ENDIF` (37). `      END` (39). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

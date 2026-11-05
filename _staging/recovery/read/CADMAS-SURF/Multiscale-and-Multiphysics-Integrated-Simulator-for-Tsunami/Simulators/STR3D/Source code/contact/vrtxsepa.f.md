---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/vrtxsepa.f
lines: 39
sha256: cab2200885c23500ae54b23196bd4f1183bc654da4a0ccd16b5458e3a7059cef
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vrtxsepa.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | VRTXSEPA는 IP가 사면체(tetrahedron)의 어느 KN 절점인지에 따라 NOD를 재배열한다(7–26). 어느 절점에도 해당하지 않으면 오류 문구를 출력하고 ERRSTP(90,ITO)를 호출한다(27–30). VOLIN의 LOGICAL 선언과 배열 선언을 포함한다. 원문: `      SUBROUTINE VRTXSEPA(ICHK,IP,F,KN,POS,ITO)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION KN(4),NOD(4),XYZ(3,4),POS(3,*),F(3)` (4). `      LOGICAL VOLIN` (5). `      IF(IP .EQ. KN(1)) THEN` (7). `        NOD(1)=KN(1)` (8). `        NOD(2)=KN(2)` (9). `        NOD(3)=KN(3)` (10). `        NOD(4)=KN(4)` (11). `      ELSEIF(IP .EQ. KN(2)) THEN` (12). `        NOD(1)=KN(2)` (13). `        NOD(2)=KN(3)` (14). `        NOD(3)=KN(1)` (15). `        NOD(4)=KN(4)` (16). `      ELSEIF(IP .EQ. KN(3)) THEN` (17). `        NOD(1)=KN(3)` (18). `        NOD(2)=KN(4)` (19). `        NOD(3)=KN(1)` (20). `        NOD(4)=KN(2)` (21). `      ELSEIF(IP .EQ. KN(4)) THEN` (22). `        NOD(1)=KN(4)` (23). `        NOD(2)=KN(1)` (24). `        NOD(3)=KN(3)` (25). `        NOD(4)=KN(2)` (26). `      ELSE` (27). `        WRITE(ITO,'(/X,A)') 'STOP IN SUB. VRTXSEPA!'` (28). `        CALL ERRSTP(90,ITO)` (29). `      ENDIF` (30). |
| 32–39 | 시작 시 1행 VRTXSEPA 루틴 안. NOD의 네 좌표를 XYZ로 복사하고 VOLIN(XYZ,F,-1.D-10)이 참이면 ICHK=1로 설정한다(32–36). RETURN과 END를 포함한다. 원문: `      DO I=1,4` (32). `        CALL SHIFT1(XYZ(1,I),POS(1,NOD(I)),3)` (33). `      ENDDO` (34). `      IF( VOLIN(XYZ,F,-1.D-10) ) ICHK=1` (36). `      RETURN` (38). `      END` (39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36: VOLIN 결과가 거짓일 때 ICHK를 0으로 바꾸는 대입은 없다.

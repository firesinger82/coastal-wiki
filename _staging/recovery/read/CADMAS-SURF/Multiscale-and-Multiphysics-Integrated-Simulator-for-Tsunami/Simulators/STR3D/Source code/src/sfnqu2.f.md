---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/sfnqu2.f
lines: 49
sha256: cb125afa6a93c44020a1afe36b12303cbecec4093c28a555aa8b80f1523d8f5a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sfnqu2.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | SFNQU2 입구와 입력 좌표·절점 번호·절점 수·출력 형상함수 주석이다(1–7). IMPLICIT·배열 선언 뒤 SFNC(1:4)를 계산한다(9–19). 해석: 이 네 식은 꼭짓점의 쌍선형 함수로 볼 수 있다. 원문: `      SUBROUTINE SFNQU2(SFNC,RINT,SINT,IEJO,NJ)` (1); 주석: `C     SFNC : OUT : SFNC(i) = Ni(ξ,η)` (3); 주석: `C     RINT : IN  : ξ` (4); 주석: `C     SINT : IN  : η` (5); 주석: `C     IEJO : IN  : 節点番号` (6) (절점 번호); 주석: `C     NJ   : IN  : 節点数` (7) (절점 수); `      IMPLICIT REAL*8(A-H,O-Z)` (9); `      DIMENSION SFNC(9),IEJO(8)` (10); `      SP1=1.0D0+RINT` (12); `      SM1=1.0D0-RINT` (13); `      TP1=1.0D0+SINT` (14); `      TM1=1.0D0-SINT` (15); `      SFNC(1)=0.25D0*SP1*TP1` (16); `      SFNC(2)=0.25D0*SM1*TP1` (17); `      SFNC(3)=0.25D0*SM1*TM1` (18); `      SFNC(4)=0.25D0*SP1*TM1` (19) [11-04 전수 검증 정정] |
| 20–49 | 시작 시 SFNQU2 루틴(1) 안이다. NJ>4이면 SFNC(5:8)을 0으로 초기화한다(20–23). IEJO(5:8)의 각 항목이 양수일 때 해당 SFNC 항목에 식을 대입한다(26–29). 이후 SFNC(1:4)를 보정한다(30–33). NJ==9이면 SFNC(9)를 계산하고 SFNC(1:8)을 보정한다(36–46). 해석: SFNC(1:4)·SFNC(5:8)·SFNC(9)를 각각 꼭짓점·모서리·중앙 함수로 볼 수 있다. 원문: `      IF(NJ.GT.4) THEN` (20); `        DO J=5,8` (21); `          SFNC(J)=0.0` (22); `        ENDDO` (23); `        SM2=1.0D0-RINT*RINT` (24); `        TM2=1.0D0-SINT*SINT` (25); `        IF(IEJO(5).GT.0) SFNC(5)=0.5D0*SM2*TP1` (26); `        IF(IEJO(6).GT.0) SFNC(6)=0.5D0*SM1*TM2` (27); `        IF(IEJO(7).GT.0) SFNC(7)=0.5D0*SM2*TM1` (28); `        IF(IEJO(8).GT.0) SFNC(8)=0.5D0*SP1*TM2` (29); `        SFNC(1)=SFNC(1)-0.5D0*SFNC(5)-0.5D0*SFNC(8)` (30); `        SFNC(2)=SFNC(2)-0.5D0*SFNC(6)-0.5D0*SFNC(5)` (31); `        SFNC(3)=SFNC(3)-0.5D0*SFNC(7)-0.5D0*SFNC(6)` (32); `        SFNC(4)=SFNC(4)-0.5D0*SFNC(8)-0.5D0*SFNC(7)` (33); `      END IF` (34); `      IF( NJ .EQ. 9 ) THEN` (36); `        SFNC(9) = SP1*SM1*TP1*TM1` (37); `        SFNC(1) = SFNC(1) + .25D0*SFNC(9)` (38); `        SFNC(2) = SFNC(2) + .25D0*SFNC(9)` (39); `        SFNC(3) = SFNC(3) + .25D0*SFNC(9)` (40); `        SFNC(4) = SFNC(4) + .25D0*SFNC(9)` (41); `        SFNC(5) = SFNC(5) - .50D0*SFNC(9)` (42); `        SFNC(6) = SFNC(6) - .50D0*SFNC(9)` (43); `        SFNC(7) = SFNC(7) - .50D0*SFNC(9)` (44); `        SFNC(8) = SFNC(8) - .50D0*SFNC(9)` (45); `      ENDIF` (46); `      RETURN` (48); `      END` (49) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·20–45: IEJO의 선언 크기는 8이다. NJ==9일 때 중앙 형상함수는 IEJO(9)를 참조하지 않고 계산한다.

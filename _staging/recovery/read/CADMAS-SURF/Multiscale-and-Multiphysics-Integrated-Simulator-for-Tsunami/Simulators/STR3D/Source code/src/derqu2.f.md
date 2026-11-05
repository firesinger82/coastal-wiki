---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/derqu2.f
lines: 81
sha256: f6683e18f588d93d300b37cdfe3bd3d39b6db849b88e025f99fdd3478a7b6073
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# derqu2.f — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | DERQU2의 좌표와 배열을 선언한다. 3행 주석은 PFNC(i,j)를 ∂Nj/∂ξi로 표시한다. 해석: N을 형상함수로 보면 PFNC는 형상함수 미분이다. `節点番号`는 절점 번호(node number), `節点数`는 절점 수(number of nodes)다. C1=0.5와 R·S의 반구간 계수를 계산한다. 원문: `      SUBROUTINE DERQU2(PFNC,RINT,SINT,IEJO,NJ)` (1); 주석 원문 `C     PFNC : OUT : PFNC(i,j) = ∂Nj/∂ξi` (3); 주석 원문 `C     RINT : IN  : ξ (ξ1)` (4); 주석 원문 `C     SINT : IN  : η (ξ2)` (5); 주석 원문 `C     IEJO : IN  : 節点番号` (6); 주석 원문 `C     NJ   : IN  : 節点数` (7); `      IMPLICIT REAL*8(A-H,O-Z)` (9); `      DIMENSION PFNC(2,9),IEJO(8)` (10); `      C1=0.5` (12); `      RP=C1*(1.0D0+RINT)` (13); `      RM=C1*(1.0D0-RINT)` (14); `      SP=C1*(1.0D0+SINT)` (15); `      SM=C1*(1.0D0-SINT)` (16). [11-04 전수 검증 정정] |
| 18–32 | 시작 시 1행 DERQU2 루틴 안. 먼저 4개 절점의 미분을 계산한다. NJ가 4보다 크면 26행 분기에 들어가 5–8번 성분을 0으로 초기화한다. 원문: `      PFNC(1,1)=C1*SP` (18); `      PFNC(1,2)=-PFNC(1,1)` (19); `      PFNC(1,3)=-C1*SM` (20); `      PFNC(1,4)=-PFNC(1,3)` (21); `      PFNC(2,1)=C1*RP` (22); `      PFNC(2,2)=C1*RM` (23); `      PFNC(2,3)=-PFNC(2,2)` (24); `      PFNC(2,4)=-PFNC(2,1)` (25); `      IF(NJ.GT.4) THEN` (26); `        DO I=1,2` (27); `          DO J=5,8` (28); `            PFNC(I,J)=0.0` (29); `          ENDDO` (30); `        ENDDO` (31). |
| 33–53 | 시작 시 26행 `      IF(NJ.GT.4) THEN`의 참 분기 안이다. 이 IF는 52행 `      END IF`에서 닫힌다. IEJO(5:8)의 각 값이 양수일 때 PFNC의 해당 5–8열을 계산한다. 38–41·48–51행은 1–4열에서 해당 5–8열 조합의 절반을 뺀다. 해석: 5–8열은 중간 절점에 해당한다. 원문: `         S2=1.0-SINT*SINT` (33); `        IF(IEJO(5).GT.0) PFNC(1,5)=-2.0D0*RINT*SP  ` (34); `        IF(IEJO(6).GT.0) PFNC(1,6)=-C1*S2` (35); `        IF(IEJO(7).GT.0) PFNC(1,7)=-2.0D0*RINT*SM  ` (36); `        IF(IEJO(8).GT.0) PFNC(1,8)= C1*S2` (37); `        PFNC(1,1)=PFNC(1,1)-C1*(PFNC(1,5)+PFNC(1,8))` (38); `        PFNC(1,2)=PFNC(1,2)-C1*(PFNC(1,6)+PFNC(1,5))` (39); `        PFNC(1,3)=PFNC(1,3)-C1*(PFNC(1,7)+PFNC(1,6))` (40); `        PFNC(1,4)=PFNC(1,4)-C1*(PFNC(1,8)+PFNC(1,7))` (41); `         R2=1.0-RINT*RINT` (43); `        IF(IEJO(5).GT.0) PFNC(2,5)= C1*R2` (44); `        IF(IEJO(6).GT.0) PFNC(2,6)=-2.0D0*SINT*RM  ` (45); `        IF(IEJO(7).GT.0) PFNC(2,7)=-C1*R2` (46); `        IF(IEJO(8).GT.0) PFNC(2,8)=-2.0D0*SINT*RP  ` (47); `        PFNC(2,1)=PFNC(2,1)-C1*(PFNC(2,5)+PFNC(2,8))` (48); `        PFNC(2,2)=PFNC(2,2)-C1*(PFNC(2,6)+PFNC(2,5))` (49); `        PFNC(2,3)=PFNC(2,3)-C1*(PFNC(2,7)+PFNC(2,6))` (50); `        PFNC(2,4)=PFNC(2,4)-C1*(PFNC(2,8)+PFNC(2,7))` (51); `      END IF` (52). [11-04 전수 검증 보완] [11-04 전수 검증 정정] |
| 54–81 | 시작 시 1행 DERQU2 루틴 안. NJ가 9이면 PFNC의 9열을 계산한다. 1–4열에는 9열의 0.25배를 더한다. 5–8열에서는 9열의 0.50배를 뺀다. 해석: 9열은 중앙 절점에 해당한다. 반환문과 루틴 끝을 포함한다. 원문: `      IF( NJ .EQ. 9 ) THEN` (54); `        PFNC(1,9) = -2.*RINT*S2` (56); `        PFNC(1,1) = PFNC(1,1) + .25*PFNC(1,9)` (58); `        PFNC(1,2) = PFNC(1,2) + .25*PFNC(1,9)` (59); `        PFNC(1,3) = PFNC(1,3) + .25*PFNC(1,9)` (60); `        PFNC(1,4) = PFNC(1,4) + .25*PFNC(1,9)` (61); `        PFNC(1,5) = PFNC(1,5) - .50*PFNC(1,9)` (62); `        PFNC(1,6) = PFNC(1,6) - .50*PFNC(1,9)` (63); `        PFNC(1,7) = PFNC(1,7) - .50*PFNC(1,9)` (64); `        PFNC(1,8) = PFNC(1,8) - .50*PFNC(1,9)` (65); `        PFNC(2,9) = -2.*SINT*R2` (67); `        PFNC(2,1) = PFNC(2,1) + .25*PFNC(2,9)` (69); `        PFNC(2,2) = PFNC(2,2) + .25*PFNC(2,9)` (70); `        PFNC(2,3) = PFNC(2,3) + .25*PFNC(2,9)` (71); `        PFNC(2,4) = PFNC(2,4) + .25*PFNC(2,9)` (72); `        PFNC(2,5) = PFNC(2,5) - .50*PFNC(2,9)` (73); `        PFNC(2,6) = PFNC(2,6) - .50*PFNC(2,9)` (74); `        PFNC(2,7) = PFNC(2,7) - .50*PFNC(2,9)` (75); `        PFNC(2,8) = PFNC(2,8) - .50*PFNC(2,9)` (76); `      ENDIF` (78); `      RETURN` (80); `      END` (81). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·18–25·54–78: PFNC의 두 번째 크기는 9다. 9번 성분 대입은 NJ=9 분기에만 있다.

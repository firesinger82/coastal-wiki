---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/crh2edge.f
lines: 103
sha256: d10012f92e2e204cdf20b0c73fe8b7e26a02457d9b0cd40cee79ea7acbea194d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# crh2edge.f — 판독 구간 기록

구간은 1행부터 103행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 루틴·암시적 자료형·배열 차원과단위 행렬 E의 DATA 값을 선언한다(1–8). SHIFT1로 모서리(edge) 양 끝점과 접촉점 좌표를 복사한다(10–12). SUBVEC·DIRCOS로 E1을 구하고 절댓값이 가장 작은 성분의 축을 골라 CROSS2로 E3·E2를 만든다(16–25). D1·D2·D3을 계산하고 LENCD에서 T를 받아 TM을 계산한다(29–36). 원문: `      SUBROUTINE CRH2EDGE(CRH,NS,J1,IG,IEDQ,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XYZ(3,3),POS(3,*),IG(2),E(3,3),V12(3),V(3),CRH(*)` `     &         ,E1(3),E2(3),E3(3),A2(12),A3(12)` (4–5, 하나의 고정형식 연속문); `      DATA E / 1.D0, 0.D0, 0.D0,` `     &         0.D0, 1.D0, 0.D0,` `     &         0.D0, 0.D0, 1.D0 /` (6–8, 하나의 고정형식 연속문); `      CALL SHIFT1(XYZ(1,3),POS(1,NS),3)` (10); `      CALL SHIFT1(XYZ(1,1),POS(1,IG(1)),3)` (11); `      CALL SHIFT1(XYZ(1,2),POS(1,IG(2)),3)` (12); 주석 원문: `C     --- E1,E2,E3 ---` (14); `      CALL SUBVEC(V12,XYZ(1,2),XYZ(1,1),3)` (16); `      CALL DIRCOS(E1,V12,3)` (17); `      J0=1` (19); `      DO 210 J=2,3` (20); `        IF( DABS(E1(J)) .LT. DABS(E1(J0)) ) J0=J` (21); `      CALL CROSS2(E1,E(1,J0),E3)` (24); `      CALL CROSS2(E3,E1,E2)` (25); 주석 원문: `C     --- D1,D2,D3 ---` (27); `      D1=E2(2)*E3(3)-E2(3)*E3(2)` (29); `      D2=E2(3)*E3(1)-E2(1)*E3(3)` (30); `      D3=E2(1)*E3(2)-E2(2)*E3(1)` (31); 주석 원문: `C     --- A2,A3 ---` (33); `      CALL LENCD(T,V,XYZ)` (35); `      TM=1.D0-T` (36). 좌표 복사와 기저 계산의 근거는 같은 STR3D 원문 트리의 `util/shift1.f:16–18`, `util/subvec.f:9–11`, `util/dircos.f:8–15`, `util/cross2.f:9–16`이다. [11-04 전수 검증 보완] |
| 38–79 | 시작 시 1행 CRH2EDGE 루틴 안이다. IEDQ=0이면 N=6으로 두 끝점의 T·TM 가중치를 E2·E3에 곱한다(38–54). ELSE에서는 N=12로 두고 .25D0*T 가중치를 추가 성분에 분배한다(56–76). 두 분기를 닫는다(78). 원문: `      IF( IEDQ .EQ. 0 ) THEN` (38); `        N=6` (40); `        A2(1) = TM*E2(1)` (42); `        A2(2) = TM*E2(2)` (43); `        A2(3) = TM*E2(3)` (44); `        A2(4) = T *E2(1)` (45); `        A2(5) = T *E2(2)` (46); `        A2(6) = T *E2(3)` (47); `        A3(1) = TM*E3(1)` (49); `        A3(2) = TM*E3(2)` (50); `        A3(3) = TM*E3(3)` (51); `        A3(4) = T *E3(1)` (52); `        A3(5) = T *E3(2)` (53); `        A3(6) = T *E3(3)` (54); `      ELSE` (56); `        N=12` (58); `        A2(1) = (TM+.25D0*T)*E2(1)` (60); `        A2(2) = (TM+.25D0*T)*E2(2)` (61); `        A2(3) = (TM+.25D0*T)*E2(3)` (62); `        A2(4) = .25D0*T*E2(1)` (63); `        A2(5) = .25D0*T*E2(2)` (64); `        A2(6) = .25D0*T*E2(3)` (65); `        A2(7:9) = A2(4:6)` (66); `        A2(10:12) = A2(4:6)` (67); `        A3(1) = (TM+.25D0*T)*E3(1)` (69); `        A3(2) = (TM+.25D0*T)*E3(2)` (70); `        A3(3) = (TM+.25D0*T)*E3(3)` (71); `        A3(4) = .25D0*T*E3(1)` (72); `        A3(5) = .25D0*T*E3(2)` (73); `        A3(6) = .25D0*T*E3(3)` (74); `        A3(7:9) = A3(4:6)` (75); `        A3(10:12) = A3(4:6)` (76). |
| 80–103 | 시작 시 1행 CRH2EDGE 루틴 안이다. J1=1·2·그 밖의 경우에 각각 D1·D2·D3을 분모로 사용한다(82–100). 각 분기는 RMULT5로 두 묶음을 구성하고 RMULT1로 전체 2*N+2개 계수를 나누어 CRH를 만든다. RETURN·END로 끝낸다(102–103). 원문: 주석 원문: `C     --- CRH ---` (80); `      IF( J1 .EQ. 1 ) THEN` (82); `        CRH(1)=D2` (83); `        CALL RMULT5(CRH(2),E3(3),A2,-E2(3),A3,N)` (84); `        CRH(N+2)=D3` (85); `        CALL RMULT5(CRH(N+3),-E3(2),A2,E2(2),A3,N)` (86); `        CALL RMULT1(CRH,CRH,1.D0/D1,2*N+2)` (87); `      ELSEIF( J1 .EQ. 2 ) THEN` (88); `        CRH(1)=D3` (89); `        CALL RMULT5(CRH(2),E3(1),A2,-E2(1),A3,N)` (90); `        CRH(N+2)=D1` (91); `        CALL RMULT5(CRH(N+3),-E3(3),A2,E2(3),A3,N)` (92); `        CALL RMULT1(CRH,CRH,1.D0/D2,2*N+2)` (93); `      ELSE` (94); `        CRH(1)=D1` (95); `        CALL RMULT5(CRH(2),E3(2),A2,-E2(2),A3,N)` (96); `        CRH(N+2)=D2` (97); `        CALL RMULT5(CRH(N+3),-E3(1),A2,E2(1),A3,N)` (98); `        CALL RMULT1(CRH,CRH,1.D0/D3,2*N+2)` (99). RMULT1의 전체 계수 스칼라 곱 근거는 같은 STR3D 원문 트리의 `util/rmult1.f:16–18`이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 82–100: 마지막 ELSE는 J1==3 검사 없이 모든 나머지 J1 값을 처리한다.
- 87·93·99: D1·D2·D3의 역수를 사용하기 전에 0 여부를 검사하지 않는다.

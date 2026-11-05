---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/crh2face.f
lines: 54
sha256: 66215ed562a25a2bf5c58d411ff43b08f17dab56ed70f5a1fd227650a1514f55
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# crh2face.f — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 루틴·암시적 자료형·배열을 선언한다(1–4). SHIFT1로 면(face) 세 점과 접촉점 좌표를 복사하고 AREACD를 호출한다(6–11). J2·J3과 다른 성분 J1을 골라 E0을 설정하고 첫 두 CRH를 계산한다(13–23). 원문: `      SUBROUTINE CRH2FACE(CRH,NS,J2,J3,IELC,IFCQ,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XYZ(3,4),POS(3,*),IELC(3),RL(3),E(3),CRH(*)` (4); `      DO 110 J=1,3` (6); `        CALL SHIFT1(XYZ(1,J),POS(1,IELC(J)),3)` (7); `      CALL SHIFT1(XYZ(1,4),POS(1,NS),3)` (9); `      CALL AREACD(RL,E,H,XYZ)` (11); `      DO 200 J=1,3` (13); `        IF( J .NE. J2 .AND. J .NE. J3 ) THEN` (14); `          J1=J` (15); `          GOTO 210` (16); `  210 E0=E(J1)` (20); `      CRH(1)=-E(J2)/E0` (22); `      CRH(2)=-E(J3)/E0` (23). 좌표 복사의 근거는 같은 STR3D 원문 트리의 `util/shift1.f:16–18`이다. [11-04 전수 검증 보완] |
| 25–54 | 시작 시 1행 CRH2FACE 루틴 안이다. IFCQ=0 분기는 3×3개 성분에 RL(K1)*E(K2)/E0을 저장한다(25–33). ELSE 분기는 앞 두 가중치에 .25D0*RL(3)을 더하고 뒤 두 가중치에는 그 항만 써 4×3개를 저장한다(35–50). 분기·루틴을 닫는다(52–54). 원문: `      IF( IFCQ .EQ. 0 ) THEN` (25); `        IP=2` (27); `        DO 130 K1=1,3` (28); `          DO 131 K2=1,3` (29); `            IP=IP+1` (30); `            CRH(IP)=RL(K1)*E(K2)/E0` (31); `      ELSE` (35); `        IP=2` (37); `        DO 140 K1=1,2` (38); `          DO 141 K2=1,3` (39); `            IP=IP+1` (40); `            CRH(IP)=(RL(K1)+.25D0*RL(3))*E(K2)/E0` (41); `        DO 150 K1=3,4` (45); `          DO 151 K2=1,3` (46); `            IP=IP+1` (47); `            CRH(IP)=.25D0*RL(3)*E(K2)/E0` (48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–48: E0을 분모로 사용하며 E0의 0 여부를 검사하는 문장은 없다.

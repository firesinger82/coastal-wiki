---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/npflowd.f
lines: 41
sha256: 7db58479e6cef7cf7182295037a057f560f9367766a0e81d0a279007f2302c27
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# npflowd.f — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | NPFLOWD는 DPG와 FTID를 인수로 받는다. 해석: 압력 증분(pressure increment)에 의한 힘 증분 계산용으로 보인다. 실수 IMPLICIT·배열 선언은 아래와 같다. KK에서 세 요소 범위를 얻고 RR(4)를 BETA에 넣는다. 원문: `      SUBROUTINE NPFLOWD(FTID,KK,RR,GRID,IELM,NM,AMAT,DPG,IDYN,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION KK(*),RR(*),IELM(NM,*),EKUP(1200),EKPP(400),ECPU(1200)` (4); `     &         ,ECPP(400),EMPU(1200),GRID(3,*),AMAT(33,*),ELHM12(1200)` (5); `     &         ,DPG(*),FTID(6,*)` (6); `      NELM = KK(12)` (8); `      NELMC = KK(29)` (9); `      NELMX = KK(32)` (10); `      BETA = RR(4)` (12) [11-04 전수 검증 정정] |
| 14–41 | `I > NELM .AND. I <= NELM + NELMC`인 구간을 건너뛴다. 유형 ITYP=6만 처리한다. 해석: 건너뛰는 구간은 접촉 요소 구간으로 보인다. ND·IMAT·ND3·N12를 구한 뒤 GEOMTX를 호출한다. IDYN=1이면 -BETA*EKUP, ELSEIF IDYN=0이면 -EKUP를 ELHM12에 넣는다. GNPFLWD에 FTID·행렬·DPG·절점 배열을 넘긴다. 원문: `      DO I = 1, NELM + NELMC + NELMX` (14); `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (16); `        ITYP = IELM(2,I)` (18); `        IF( ITYP /= 6 ) CYCLE` (20); `        ND = IELM(3,I)` (22); `        IMAT = IELM(4,I)` (23); `        ND3 = ND * 3` (25); `        N12 = ND3 * ND` (26); `        CALL GEOMTX(EKUP,EKPP,ECPU,ECPP,EMPU,ND,ND3,IELM(8,I),GRID` (28); `     &             ,AMAT(1,IMAT),ITO)` (29); `        IF( IDYN == 1 ) THEN` (31); `          ELHM12(1:N12) = -BETA * EKUP(1:N12)` (32); `        ELSEIF( IDYN == 0 ) THEN` (33); `          ELHM12(1:N12) = -EKUP(1:N12)` (34); `        ENDIF` (35); `        CALL GNPFLWD(FTID,ELHM12,DPG,IELM(8,I),ND)` (37); `      ENDDO` (39); `      END` (41) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4–5: EKUP·ECPU·EMPU·ELHM12 작업 배열은 1200, EKPP·ECPP는 400 원소로 고정한다.
- 31–35: IDYN=1·0 이외에 ELHM12를 대입하는 ELSE는 없다.

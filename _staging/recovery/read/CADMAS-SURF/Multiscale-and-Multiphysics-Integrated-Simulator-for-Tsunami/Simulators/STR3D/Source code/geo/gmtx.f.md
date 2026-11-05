---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gmtx.f
lines: 26
sha256: 25f150d690e511105206a664a6a3b5a990c5dae5ca4a226ef34bcfe405e1f7c8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtx.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | GMTX는 RN과 DNDX를 AXB·ATXB에 전달하여 RKUP·RKPP·CPU·CPP를 구성한다. IMPLICIT·배열 선언은 아래와 같다. 해석: RN은 형상함수(shape function)로 보인다. 해석: DNDX는 공간 미분으로 보인다. 해석: AXB 호출은 RKUP·CPU·CPP의 외적 구성으로 보인다. 해석: ATXB 호출은 RKPP의 미분 내적 구성으로 보인다. 각 곱셈 차원은 호출 인수에 적혀 있다. 원문: `      SUBROUTINE GMTX(RKUP,RKPP,CPU,CPP,RMPU,RN,DNDX,N,N3)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RKUP(N3,N),RKPP(N,N),CPU(N,N3),CPP(N,N),RMPU(N,N3)` (4); `     &         ,RN(N),DNDX(3,N),RN3(3,N3)` (5); `      CALL AXB(RKUP,DNDX,RN,N3,1,N)` (7); `      CALL ATXB(RKPP,DNDX,DNDX,3,N,N)` (9); `      CALL AXB(CPU,RN,DNDX,N,1,N3)` (11); `      CALL AXB(CPP,RN,RN,N,1,N)` (13) [11-04 전수 검증 정정] |
| 15–26 | RN3(3,N3)를 0으로 초기화한다. J=1,N 및 I=1,3에서 `JJ = 3 * ( J - 1)`을 계산한다. `RN3(I,JJ+I) = RN(J)`로 각 J에 대응하는 세 열 중 I번째 열의 I번째 행에 RN(J)를 넣는다. ATXB에 DNDX와 RN3를 넘겨 RMPU를 구성한다. 원문: `      RN3(:,:) = 0.` (15); `      DO J = 1, N` (17); `        JJ = 3 * ( J - 1)` (18); `        DO I = 1, 3` (19); `          RN3(I,JJ+I) = RN(J)` (20); `        ENDDO` (21); `      ENDDO` (22); `      CALL ATXB(RMPU,DNDX,RN3,3,N,N3)` (24); `      END` (26) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

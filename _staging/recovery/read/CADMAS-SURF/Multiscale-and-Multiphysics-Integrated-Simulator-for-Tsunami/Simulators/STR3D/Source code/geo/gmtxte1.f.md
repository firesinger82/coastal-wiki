---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gmtxte1.f
lines: 19
sha256: 923ab3d4043904303703c816166368bc33a63c450ddfd84d9b15444529cf1d7d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtxte1.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | GMTXTE1은 다섯 결합 행렬을 구성한다. 해석: 루틴 이름과 배열 크기는 4절점 사면체(tetrahedron) 요소를 가리키는 것으로 보인다. 실수 IMPLICIT와 배열 범위는 아래와 같다. RN(:)=.25D0으로 두고 DERXTE1을 호출한다. GMTX에 절점 수 4·변위 성분 수 12를 넘긴다. 다섯 결과에 DET/6.D0을 곱한다. 원문: `      SUBROUTINE GMTXTE1(EKUP,EKPP,ECPU,ECPP,EMPU,X,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION EKUP(12,4),EKPP(4,4),ECPU(4,12),ECPP(4,4),EMPU(4,12)` (4); `     &         ,RN(4),X(3,4),DNDX(3,4)` (5); `      RN(:) = .25D0` (7); `      CALL DERXTE1(DNDX,DET,X,ITO)` (9); `      CALL GMTX(EKUP,EKPP,ECPU,ECPP,EMPU,RN,DNDX,4,12)` (11); `      EKUP(:,:) = EKUP(:,:)*DET/6.D0` (13); `      EKPP(:,:) = EKPP(:,:)*DET/6.D0` (14); `      ECPU(:,:) = ECPU(:,:)*DET/6.D0` (15); `      ECPP(:,:) = ECPP(:,:)*DET/6.D0` (16); `      EMPU(:,:) = EMPU(:,:)*DET/6.D0` (17); `      END` (19) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–17: RN 값은 모두 .25D0이며 별도 적분점 루프 없이 한 번 GMTX를 호출한다. 해석: RN은 형상함수 값으로 보인다. [11-04 전수 검증 정정]

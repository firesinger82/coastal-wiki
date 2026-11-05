---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/gmtxte1_s.f
lines: 16
sha256: f70fd3340e4bff764596a1dca43af659c62814b0c5a3cba579dcf62bc3bbc8c8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtxte1_s.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | GMTXTE1_S의 암시적 형·배열 선언. RN의 네 항목을 .25D0로 설정한다. DERXTE1에 DNDX·DET를 전달한다. MATML에 DNDX·RN을 전달하여 EKPP·ECPP를 얻는다. 두 배열에 DET/6.D0를 곱한다. 해석: RN은 형상 함수 값이고 DNDX는 공간 도함수로 읽힌다. 원문: `      SUBROUTINE GMTXTE1_S(EKPP,ECPP,X,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION EKPP(10),ECPP(10),RN(4),X(3,4),DNDX(3,4)` (4); `      RN(:) = .25D0` (6); `      CALL DERXTE1(DNDX,DET,X,ITO)` (8); `      CALL MATML(EKPP,1,DNDX,3,DNDX,2,4,4,3)` (10); `      CALL MATML(ECPP,1,RN,3,RN,2,4,4,1)` (11); `      EKPP(:) = EKPP(:)*DET/6.D0` (13); `      ECPP(:) = ECPP(:)*DET/6.D0` (14); `      END` (16). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

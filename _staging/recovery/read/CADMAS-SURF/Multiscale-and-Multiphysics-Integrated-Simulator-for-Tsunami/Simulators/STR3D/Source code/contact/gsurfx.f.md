---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/gsurfx.f
lines: 14
sha256: 96ea427f16bfc722a2d4133337599004d5f76fb82b7350730d4c6adfe144ba7e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gsurfx.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 루틴·암시적 자료형과 XG(NDIM,NGX)·IELQX(4,NGX) 등 배열 차원을 선언한다(1–4). 모든 사각 면을 순회하며 네 절점 번호를 가져와 MEAN4로 NDIM 성분의 XG를 구한다(6–12). 루틴을 끝낸다(14). 원문: `      SUBROUTINE GSURFX(XG,NDIM,NGX,XX,IELQX)` (1); `      IMPLICIT REAL*8(A-H,O-Z)      ` (3); `      DIMENSION XG(NDIM,NGX),XX(NDIM,*),IG(4),IELQX(4,NGX)` (4); `      DO I = 1, NGX` (6); `        IG(:) = IELQX(:,I)` (8); `        CALL MEAN4(XG(1,I),XX,NDIM,IG,4)` (10). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

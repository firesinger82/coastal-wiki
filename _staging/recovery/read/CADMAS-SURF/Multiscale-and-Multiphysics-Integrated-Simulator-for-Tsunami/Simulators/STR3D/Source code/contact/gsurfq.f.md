---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/gsurfq.f
lines: 16
sha256: 936e0f9a8cb7078a1d38f9b31b063cf3ed60a2c47b3e8218a89d7d85206354c8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gsurfq.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 루틴·암시적 자료형·배열을 선언한다(1–4). I=1..NG를 순회하며 IVRQ=0이면 건너뛴다(6–8). IVRQ가 가리키는 IELQ의 네 절점을 가져와 MEAN4로 NDIM 성분의 XG를 구한다(10–12). 루프·루틴을 끝낸다(14–16). 원문: `      SUBROUTINE GSURFQ(XG,NDIM,NG,XX,IELQ,IVRQ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)      ` (3); `      DIMENSION XG(NDIM,NG),XX(NDIM,*),IELQ(4,*),IVRQ(NG),IG(4)` (4); `      DO I = 1, NG` (6); `        IF( IVRQ(I) == 0 ) CYCLE` (8); `        IG(:) = IELQ(:,IVRQ(I))` (10); `        CALL MEAN4(XG(1,I),XX,NDIM,IG,4)` (12). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8: IVRQ(I)==0인 XG 열은 이 루틴에서 갱신하지 않는다.

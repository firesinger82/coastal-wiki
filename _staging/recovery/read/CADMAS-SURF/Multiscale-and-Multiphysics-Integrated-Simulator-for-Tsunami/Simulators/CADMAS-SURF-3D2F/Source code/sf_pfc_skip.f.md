---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_pfc_skip.f
lines: 23
sha256: f8c89dcffec89f1b1c0f4daa73cd13aa3d494b6126eddc9669a3bfc5cb673247
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_pfc_skip.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | GRID(:,NP(I))를 I=1,N에 대해 합산하여 DBLE(N)으로 나눈 XG를 구한다(7–13). 세 방향 모두 X의 하한 포함·상한 제외 구간 안이면 ISKIP=0, 그 외에는 ISKIP=1로 설정한다(15–21). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_PFC_SKIP(ISKIP,X,N,NP,GRID)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XG(3),X(2,3),NP(N),GRID(3,*)` (5); `      XG(:) = 0.` (7); `      DO I = 1, N` (9); `        XG(:) = XG(:) + GRID(:,NP(I))` (10); `      ENDDO` (11); `      XG(:) = XG(:) / DBLE(N)` (13); `      IF( XG(1) >= X(1,1) .AND. XG(1) < X(2,1) .AND.` (15); `     &    XG(2) >= X(1,2) .AND. XG(2) < X(2,2) .AND.` (16); `     &    XG(3) >= X(1,3) .AND. XG(3) < X(2,3) ) THEN` (17); `        ISKIP = 0` (18); `      ELSE` (19); `        ISKIP = 1` (20); `      ENDIF` (21); `      END` (23). 해석: XG는 N개 절점 좌표의 평균으로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–13: 중심 계산에서 N으로 나눈다. 이 루틴에는 N>0 검사문이 없다.

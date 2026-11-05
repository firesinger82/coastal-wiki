---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_gsfpn.f
lines: 21
sha256: 1b5e7acac43b77270ba9b27baf792ed59a8dfa1eafd231dc8e3b1299df9ae9fb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_gsfpn.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | SF_GSFPN 선언과 배열 범위(1–4). DATA II는 아래 인용한 지표 배열을 정한다(5). 해석: 이 배열은 6절점(node) 요소의 세 사각면 연결을 나타낸다. 세 면과 세 좌표 성분을 순회한다(7–19). 면의 네 절점 좌표를 모아 SF_MEAN1로 평균 좌표 XG를 구한다(9–15). 평균 계산의 근거는 같은 원문 디렉터리의 `sf_mean1.f:18–24`이다. 원문: `      SUBROUTINE SF_GSFPN(XG,XX,NP)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION II(4,3),IG(4),NP(6),XG(3,3),XX(3,*),X(4)` (4)<br>`      DATA II / 1,4,5,2, 2,5,6,3, 3,6,4,1 /` (5)<br>`      DO I = 1, 3` (7)<br>`        IG(:) = NP( II(:,I) )` (9)<br>`        DO J = 1, 3` (11)<br>`          X(:) = XX(J,IG(:))` (13)<br>`          CALL SF_MEAN1(XG(J,I),X,4)` (15)<br>`        ENDDO` (17)<br>`      ENDDO` (19)<br>`      END` (21) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

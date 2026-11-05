---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/gsfpn.f
lines: 15
sha256: f45299e7846cd046761b7ba25d8ffc598ccb01acbd52b675c82916d9054481f2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gsfpn.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 루틴·암시적 자료형·배열과 6절점의 5개 면 연결표를 DATA로 선언한다(1–5). I=1..3에서 연결표의 I+2번째 면, 즉 세 사각 면의 네 절점 번호를 모은다(7–9). MEAN4에 네 절점과 N 성분을 전달하여 XG를 채운다(11). 루프·루틴을 닫는다(13–15). 원문: `      SUBROUTINE GSFPN(XG,XX,NP,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)      ` (3); `      DIMENSION II(4,5),IG(4),NP(6),XG(N,3),XX(N,*)` (4); `      DATA II / 1,2,3,0, 4,6,5,0, 1,4,5,2, 2,5,6,3, 3,6,4,1 /` (5); `      DO I = 1, 3` (7); `        IG(:) = NP( II(:,I+2) )` (9); `        CALL MEAN4(XG(1,I),XX,N,IG,4)` (11). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·7–9: DATA에는 다섯 면이 있지만 실행 루프는 3:5번째 면만 사용한다.

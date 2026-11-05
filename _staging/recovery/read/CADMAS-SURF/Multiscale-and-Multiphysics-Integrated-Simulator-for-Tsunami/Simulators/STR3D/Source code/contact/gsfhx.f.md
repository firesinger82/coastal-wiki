---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/gsfhx.f
lines: 15
sha256: 1068f69c856b29d1916049ccd488fee224450e48d5ccba26b811b4726bd11259
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gsfhx.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 루틴·암시적 자료형·배열과 8절점의 6개 사각 면 연결표를 DATA로 선언한다(1–5). 여섯 면을 순회하며 NP에서 네 절점 번호를 모으고 MEAN4에 네 절점과 N 성분을 전달하여 XG를 채운다(7–13). 루틴을 끝낸다(15). 원문: `      SUBROUTINE GSFHX(XG,XX,NP,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)      ` (3); `      DIMENSION II(4,6),IG(4),NP(8),XG(N,6),XX(N,*)` (4); `      DATA II / 1,2,3,4, 1,5,6,2, 2,6,7,3, 3,7,8,4, 4,8,5,1, 5,8,7,6 /` (5); `      DO I = 1, 6` (7); `        IG(:) = NP( II(:,I) )` (9); `        CALL MEAN4(XG(1,I),XX,N,IG,4)` (11). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

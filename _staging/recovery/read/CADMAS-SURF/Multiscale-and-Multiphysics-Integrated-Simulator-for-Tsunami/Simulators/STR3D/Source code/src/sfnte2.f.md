---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/sfnte2.f
lines: 21
sha256: fed06a1743ce480b55a03b9086cfda567f18a908239a69076cdd48711a984dd4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sfnte2.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | SFNTE2 입구와 체적 좌표·출력 형상함수 주석이다(1–4). IMPLICIT·배열 선언 뒤 H(1:10)을 계산한다(6–18). 해석: 이 식은 열 절점 사면체의 꼭짓점 함수 네 개와 모서리 함수 여섯 개로 볼 수 있다. 원문: `      SUBROUTINE SFNTE2(RL,H)` (1); 주석: `C     RL : IN  : 体積座標` (3) (체적 좌표(volume coordinates)); 주석: `C     H  : OUT : H(i) = Ni` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION H(10),RL(4)` (7); `      H( 1) = RL(1)*(2.*RL(1)-1.) ` (9); `      H( 2) = RL(2)*(2.*RL(2)-1.)` (10); `      H( 3) = RL(3)*(2.*RL(3)-1.)` (11); `      H( 4) = RL(4)*(2.*RL(4)-1.)` (12); `      H( 5) = 4.*RL(1)*RL(2)` (13); `      H( 6) = 4.*RL(2)*RL(3)` (14); `      H( 7) = 4.*RL(1)*RL(3)` (15); `      H( 8) = 4.*RL(1)*RL(4)` (16); `      H( 9) = 4.*RL(2)*RL(4)` (17); `      H(10) = 4.*RL(3)*RL(4)` (18); `      RETURN` (20); `      END` (21) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

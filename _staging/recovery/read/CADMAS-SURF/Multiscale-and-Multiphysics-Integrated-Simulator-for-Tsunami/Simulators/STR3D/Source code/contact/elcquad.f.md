---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/elcquad.f
lines: 23
sha256: b2838410cf4006aec286d644204dee7d8b7cfd61796150a320a6b04bfa788c65
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# elcquad.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 루틴과 배열을 선언한다(1–3). ICSF의 네 절점을 IG에 복사한다(5). 순서가 (1,2)·(2,3)·(3,4)·(4,1)인 각 절점 쌍에 공통 절점 IG5를 붙여 삼각 면 네 개를 만든다(7–21). 루틴을 끝낸다(23). 원문: `      SUBROUTINE ELCQUAD(IELC,ICSF,IG5)` (1); `      DIMENSION IG(4),ICSF(6),IELC(3,4)` (3); `      IG(1:4) = ICSF(3:6)` (5); `      IELC(1,1) = IG(1)` (7); `      IELC(2,1) = IG(2)` (8); `      IELC(3,1) = IG5` (9); `      IELC(1,2) = IG(2)` (11); `      IELC(2,2) = IG(3)` (12); `      IELC(3,2) = IG5` (13); `      IELC(1,3) = IG(3)` (15); `      IELC(2,3) = IG(4)` (16); `      IELC(3,3) = IG5` (17); `      IELC(1,4) = IG(4)` (19); `      IELC(2,4) = IG(1)` (20); `      IELC(3,4) = IG5` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

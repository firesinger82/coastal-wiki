---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mktepn.f
lines: 62
sha256: a77b551ed3f42256d5e130cc57fa01feac88e3a5194484d59ae6ddcf4ec3ae53
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mktepn.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | SF_MKTEPN 선언과 IG(4,11)·JG(6)·KG(3) 범위(1–3). DATA KG는 -1·-2·-3이다(5). KG·JG를 조합해 IG의 1–5열을 설정한다(7–30). 해석: IG는 연결표다. 원문: `      SUBROUTINE SF_MKTEPN(IG,JG)` (1)<br>`      DIMENSION IG(4,11),JG(6),KG(3)` (3)<br>`      DATA KG / -1, -2, -3 /` (5)<br>`      IG(1,1) = KG(1)` (7)<br>`      IG(2,1) = JG(5)` (8)<br>`      IG(3,1) = JG(2)` (9)<br>`      IG(4,1) = KG(2)` (10)<br>`      IG(1,2) = KG(2)` (12)<br>`      IG(2,2) = JG(6)` (13)<br>`      IG(3,2) = JG(3)` (14)<br>`      IG(4,2) = KG(3)` (15)<br>`      IG(1,3) = KG(3)` (17)<br>`      IG(2,3) = JG(4)` (18)<br>`      IG(3,3) = JG(1)` (19)<br>`      IG(4,3) = KG(1)` (20)<br>`      IG(1,4) = KG(1)` (22)<br>`      IG(2,4) = KG(2)` (23)<br>`      IG(3,4) = KG(3)` (24)<br>`      IG(4,4) = JG(6)` (25)<br>`      IG(1,5) = JG(6)` (27)<br>`      IG(2,5) = JG(5)` (28)<br>`      IG(3,5) = JG(4)` (29)<br>`      IG(4,5) = KG(1)` (30) [11-04 전수 검증 정정] |
| 32–62 | 시작 시 1행 SF_MKTEPN 루틴 안. KG·JG를 조합해 나머지 IG의 6–11열을 설정한다(32–60). 별도 분기나 루프는 없다. 원문: `      IG(1,6) = KG(1)` (32)<br>`      IG(2,6) = JG(5)` (33)<br>`      IG(3,6) = KG(2)` (34)<br>`      IG(4,6) = JG(6)` (35)<br>`      IG(1,7) = KG(1)` (37)<br>`      IG(2,7) = KG(3)` (38)<br>`      IG(3,7) = JG(4)` (39)<br>`      IG(4,7) = JG(6)` (40)<br>`      IG(1,8) = KG(1)` (42)<br>`      IG(2,8) = KG(3)` (43)<br>`      IG(3,8) = KG(2)` (44)<br>`      IG(4,8) = JG(3)` (45)<br>`      IG(1,9) = JG(3)` (47)<br>`      IG(2,9) = JG(1)` (48)<br>`      IG(3,9) = JG(2)` (49)<br>`      IG(4,9) = KG(1)` (50)<br>`      IG(1,10) = KG(1)` (52)<br>`      IG(2,10) = JG(1)` (53)<br>`      IG(3,10) = KG(3)` (54)<br>`      IG(4,10) = JG(3)` (55)<br>`      IG(1,11) = KG(1)` (57)<br>`      IG(2,11) = KG(2)` (58)<br>`      IG(3,11) = JG(2)` (59)<br>`      IG(4,11) = JG(3)` (60)<br>`      END` (62) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

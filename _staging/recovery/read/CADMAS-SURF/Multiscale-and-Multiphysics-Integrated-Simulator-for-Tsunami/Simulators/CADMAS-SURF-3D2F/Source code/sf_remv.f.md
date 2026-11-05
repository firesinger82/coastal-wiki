---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_remv.f
lines: 28
sha256: 4d38035c32239d48125ea58f4006e5d5e602a7eef590c328d7ad75552c44f9b7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_remv.f — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | RZ를 DZ와 H의 최솟값으로 정하고 H에서 뺀다(6–8). RZ=DZ이면 GGW=1, 그 외에는 RZ/DZ다(10–14). 기존 GGV를 GGV0에 보관한다(16). GGV를 RZ/DZ와 기존 GGV를 사용하는 18행 식으로 갱신한다. GGF(1:4)는 새 GGV, GGF(5)는 RZ==DZ이면 1이고 그 외에는 기존 GGV, GGF(6)는 1이다(20–26). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_REMV(H,GGW,GGV,GGF,DZ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION GGF(6)` (4); `      RZ = DMIN1(DZ,H)` (6); `      H = H - RZ` (8); `      IF( RZ == DZ ) THEN` (10); `        GGW = 1.D0` (11); `      ELSE` (12); `        GGW = RZ / DZ` (13); `      ENDIF` (14); `      GGV0 = GGV` (16); `      GGV = RZ / DZ + ( 1.D0 - RZ / DZ ) * GGV` (18); `      GGF(1:4) = GGV` (20); `      IF( RZ == DZ ) THEN` (21); `        GGF(5) = 1.D0` (22); `      ELSE` (23); `        GGF(5) = GGV0` (24); `      ENDIF` (25); `      GGF(6) = 1.D0` (26); `      END` (28). 해석: GGV는 공극률로 읽힌다. 해석: RZ/DZ는 제거 비율로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13·18: RZ/DZ를 사용하며 이 루틴에는 DZ=0 검사문이 없다.

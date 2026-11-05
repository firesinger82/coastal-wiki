---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_SPC.f
lines: 14
sha256: e57539b2e8ec1ab8e6c2ade9abef1724c5b11118b015647ee22357fbff8f963b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_SPC.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 80자 CHAR와 IG(2)를 선언한다(3–4). 두 절점 번호를 읽는다(7). 단점 구속(single-point constraint) 항목은 I=1..2에서 첫 0을 만나면 루프를 끝내며 그 전까지 N_SPC를 늘린다(9–12). 원문: `      SUBROUTINE CT_SPC( N_SPC, CHAR )` (1); `      CHARACTER*80 CHAR` (3); `      DIMENSION IG(2)` (4); `      READ(CHAR,'(BN,16X,I8,16X,I8)') IG(:)` (7); `      DO I = 1, 2` (9); `        IF( IG(I) == 0 ) EXIT` (10); `        N_SPC = N_SPC + 1` (11); `      ENDDO` (12); `      END` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

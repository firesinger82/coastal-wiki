---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_MATT1.f
lines: 15
sha256: ddb1d9ae0ba70165981a75aaa290c77e1750d97eb785f48fbf656055e951bfc3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_MATT1.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | RD_MATT1은 80자 CHAR와 J_MATT1(6)을 선언한다(1–4). 카드(card)에서 MID·JE·JNU·JRHO·JA·JGE를 읽는다(6). J_MATT1에는 MID·JE·JNU·JRHO·JGE·JA 순서로 저장한다(8–13). 끝 주석과 END를 포함한다(14–15). 원문: `      SUBROUTINE RD_MATT1( J_MATT1, CHAR )` (1); `      CHARACTER*80 CHAR` (3); `      DIMENSION J_MATT1(6)` (4); `      READ(CHAR,'(BN,8X,2I8,8X,3I8,8X,I8)') MID, JE, JNU, JRHO, JA, JGE` (6); `      J_MATT1(1) = MID` (8); `      J_MATT1(2) = JE` (9); `      J_MATT1(3) = JNU` (10); `      J_MATT1(4) = JRHO` (11); `      J_MATT1(5) = JGE` (12); `      J_MATT1(6) = JA` (13); `      END` (15). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

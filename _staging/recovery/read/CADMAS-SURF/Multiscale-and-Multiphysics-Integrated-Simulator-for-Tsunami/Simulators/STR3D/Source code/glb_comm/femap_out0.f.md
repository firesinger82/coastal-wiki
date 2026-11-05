---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/femap_out0.f
lines: 26
sha256: e6a94228970419376898af096a767e234db5bfcf4e34e17ccbd63d4fce472f42
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# femap_out0.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 암시적 배정밀도(implicit double precision)와 배열을 선언한다(3–4). BLK_S(450)와 BLK_E 사이에서 FMP_OUS0을 호출하여 출력 집합 정보를 쓴다(6–10). 원문: `      SUBROUTINE FEMAP_OUT0(KK,INDG,IFMP)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION KK(*),INDG(*)` (4); `      CALL BLK_S(450,IFMP)` (6); `      CALL FMP_OUS0(IOUT,IFMP)` (8); `      CALL BLK_E(IFMP)` (10). |
| 12–26 | 시작 시 1행 femap_out0 루틴 안. BLK_S(1051) 뒤에 절점·고체·봉·보 결과를 FMP_NODAL0·FMP_SOL0·FMP_ROD0·FMP_BAR0으로 출력한다(12–20). 보 요소 시작 위치 인수는 KK(10)+KK(14)이다(20). KK(25)가 양수일 때 FMP_SOIL0을 호출하고 블록을 닫는다(22–24). 원문: `      CALL BLK_S(1051,IFMP)` (12); `      CALL FMP_NODAL0(IOUT,INDG,KK(8),KK(81),KK(25),IFMP)` (14); `      CALL FMP_SOL0(IOUT,INDG,KK(8),IFMP)` (16); `      CALL FMP_ROD0(IOUT,KK(10),KK(14),IFMP)` (18); `      CALL FMP_BAR0(IOUT,KK(10)+KK(14),KK(16),IFMP)` (20); `      IF( KK(25) > 0 ) CALL FMP_SOIL0(IOUT,INDG,KK(8),IFMP)` (22); `      CALL BLK_E(IFMP)` (24); `      END` (26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

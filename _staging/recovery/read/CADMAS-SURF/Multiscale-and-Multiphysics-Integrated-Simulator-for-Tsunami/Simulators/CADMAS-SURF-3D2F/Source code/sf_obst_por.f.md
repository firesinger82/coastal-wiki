---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_obst_por.f
lines: 24
sha256: eb8baa983c40866894850829a5e9a9f31a0006f22930a4f180ff2cd1cdaba34b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_obst_por.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | GGV0·GGV·NF·DBUF의 선언부다(1–10). 내부 셀에서 NF=-1이면 GGV0를 0으로 설정한다(12–18). VF_P3SRD2 호출 후 GGV0 전체를 GGV로 복사한다(20–22). 12–18행의 루프는 NF=-1인 셀의 GGV0만 0으로 설정한다. 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_OBST_POR(GGV0,GGV,NF,DBUF)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_ANUMBI.h'` (6); `      INCLUDE 'VF_APARAI.h'` (7); `      DIMENSION GGV(NUMI,NUMJ,NUMK),GGV0(NUMI,NUMJ,NUMK)` (9); `     &         ,NF(NUMI,NUMJ,NUMK),DBUF(NUMBUF*MAXBUF)` (10); `      DO K = 2, NUMK - 1` (12); `        DO J = MYJS, MYJE` (13); `          DO I = MYIS, MYIE` (14); `            IF( NF(I,J,K) == -1 ) GGV0(I,J,K) = 0.D0` (15); `          ENDDO` (16); `        ENDDO` (17); `      ENDDO` (18); `      CALL VF_P3SRD2(GGV0,DBUF,0)` (20); `      GGV = GGV0` (22); `      END` (24). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

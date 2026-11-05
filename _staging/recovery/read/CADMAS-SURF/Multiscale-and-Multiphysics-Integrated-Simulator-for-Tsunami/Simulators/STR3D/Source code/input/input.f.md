---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/input.f
lines: 16
sha256: 071d4b792c662bc7450c6c08fefa757d9ffd72b4d31be48e86170261203bb4eb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# input.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | INPUT은 입력 개수 집계 COUNT_DATA(ITI)를 호출하고 장치 ITI를 REWIND한다(6–8). READ_DATA(KK,RR,ITI,ITO) 다음 SET_TABLE(KK,ITO)을 호출한다(10–12). ICK=1인 경우만 DATA_CHECK(KK,RR)를 호출한다(14). 암시적 배정밀도 선언과 KK(*)·RR(*) 범위를 포함한다(3–4). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE INPUT( KK, RR, ICK, ITI, ITO )` (1) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (3) <br> `      DIMENSION KK(*), RR(*)` (4) <br> `      CALL COUNT_DATA( ITI )` (6) <br> `      REWIND(ITI)` (8) <br> `      CALL READ_DATA( KK, RR, ITI, ITO )` (10) <br> `      CALL SET_TABLE( KK, ITO )` (12) <br> `      IF( ICK == 1 ) CALL DATA_CHECK( KK, RR )` (14) <br> `      END` (16) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

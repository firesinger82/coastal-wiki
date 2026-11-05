---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/addset.f
lines: 19
sha256: 10c03bbf24f94feba1ecabd2e0278057d17aa9c8f2339a89710172aec4d45ed1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# addset.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | ADDSET의 인수와 암시적 형, INDEX(2,*)를 선언한다(1–4). 구분선·고정형식 열 위치 주석을 포함한다(5–9). 원문: `      SUBROUTINE ADDSET(I,INDEX,IS,NDATA)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION INDEX(2,*)` (4). |
| 10–19 | 시작 시 1행 ADDSET 루틴 안. 첫 항목이면 이전 끝 IE를 0으로 두고, 나머지는 INDEX의 이전 항목 끝을 가져온다(10–14). 데이터 수 NDATA와 시작 위치 IS를 산출한다(15–16). RETURN·END를 포함한다(18–19). 원문: `      IF(I.EQ.1) THEN` (10); `        IE=0` (11); `      ELSE` (12); `        IE=INDEX(2,I-1)` (13); `      ENDIF` (14); `      NDATA=INDEX(2,I)-IE` (15); `      IS=IE+1` (16); `      RETURN` (18); `      END` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

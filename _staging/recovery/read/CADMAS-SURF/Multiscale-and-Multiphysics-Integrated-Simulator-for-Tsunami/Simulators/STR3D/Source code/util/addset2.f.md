---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/addset2.f
lines: 15
sha256: eb3024c97501400335218c32a3c22619fc119e62f22e9a337c171618c0d14fdc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# addset2.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | ADDSET2와 암시적 형, 가정 크기(assumed-size) INDEX(*)를 선언한다(1–4). 구분 주석을 포함한다(5). 원문: `      SUBROUTINE ADDSET2(I,INDEX,IS,NDATA)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION INDEX(*)` (4). |
| 6–15 | 시작 시 1행 ADDSET2 루틴 안. 첫 항목 여부로 이전 끝 IE를 선택한다(6–10). INDEX(I)와 IE의 차이로 NDATA를 계산하고 IE 다음 위치를 IS로 정한다(11–12). 주석·RETURN·END를 포함한다(13–15). 원문: `      IF(I.EQ.1) THEN` (6); `        IE=0` (7); `      ELSE` (8); `        IE=INDEX(I-1)` (9); `      ENDIF` (10); `      NDATA=INDEX(I)-IE` (11); `      IS=IE+1` (12); `      RETURN` (14); `      END` (15). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

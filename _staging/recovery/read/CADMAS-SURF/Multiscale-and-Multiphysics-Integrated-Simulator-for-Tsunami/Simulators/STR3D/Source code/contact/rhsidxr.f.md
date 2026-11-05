---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/rhsidxr.f
lines: 22
sha256: 42053697828b0f4c80dbecb57107c03ee10813c8720167c9d18ecb7636b05670
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rhsidxr.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | RHSIDXR는 역순 저장된 우변 열 목록을 정방향 행 순서로 복사한다. 인수·배열 선언과 IROW_R(1)=1 초기화를 포함한다(1–5). 원문: `      SUBROUTINE RHSIDXR(NROW,IROW_R,ICOL_R,IROW_R3,ICOL_R3)` (1). `      DIMENSION IROW_R(NROW+1),ICOL_R(*),IROW_R3(NROW+1),ICOL_R3(*)` (3). `      IROW_R(1)=1` (5). |
| 7–22 | 시작 시 1행 RHSIDXR 루틴 안. I=1..NROW에서 II=NROW+1-I를 사용해 역순 행 주소를 얻는다(7–13). SHIFT0으로 해당 열 구간을 복사하고 IROW_R의 다음 주소를 갱신한다(14–19). RETURN과 END를 포함한다. 원문: `      DO 100 I=1,NROW` (7). `        II=NROW+1-I` (9). `        IS=IROW_R3(II)` (11). `        IE=IROW_R3(II+1)-1` (12). `        N=IE-IS+1` (13). `        IP=IROW_R(I)` (14). `        CALL SHIFT0(ICOL_R(IP),ICOL_R3(IS),N)` (15). `        IROW_R(I+1)=IROW_R(I)+N` (17). `  100 CONTINUE` (19). `      RETURN` (21). `      END` (22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_SID.f
lines: 18
sha256: 902fd446e807338b60074253ba419ba979a638887c9f154da4b3a6a12ac4ab46
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_SID.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | ST_SID는 입력 첫 성분의 서로 다른 세트 식별자를 ISID 첫 행에 보존한다(7–16). 이미 등록한 1:NSID에서 일치하면 GOTO 10으로 중복을 건너뛴다(9–11). 새 식별자면 NSID를 늘리고 복사한다(13–14). ISID(2,*)·J_IDX(M,N_IDX) 선언과 주석·루틴 끝을 포함한다(1–18). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_SID( ISID, J_IDX, M, N_IDX )` (1) <br> `      DIMENSION ISID(2,*), J_IDX(M,N_IDX)` (3) <br> `      NSID = 0` (5) <br> `      DO 10 I = 1, N_IDX` (7) <br> `        DO J = 1, NSID` (9) <br> `          IF( J_IDX(1,I) == ISID(1,J) ) GOTO 10` (10) <br> `        ENDDO` (11) <br> `        NSID = NSID + 1` (13) <br> `        ISID(1,NSID) = J_IDX(1,I)` (14) <br> `   10 CONTINUE` (16) <br> `      END` (18) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

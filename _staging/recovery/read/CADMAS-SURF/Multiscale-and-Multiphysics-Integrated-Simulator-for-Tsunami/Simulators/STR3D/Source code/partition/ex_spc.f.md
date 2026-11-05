---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/ex_spc.f
lines: 33
sha256: 7587dd914179dda81d84c5573db5f7c7440e3bc5fb7bddcd4eeb49cc70a4fbf7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ex_spc.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | EX_SPC의 연속 인수·암시적 형 선언·N행 절점 조건 및 6행 값 배열 선언과 개수 초기화. 원문: 연속문(1–2): `      SUBROUTINE EX_SPC(NISPCW,NNSPCW,ISPCW,NSPCW,SPCW,NISPC,ISPC,NSPC` <br> `     &                 ,SPC,LNOD,NNODW,N)`; `      IMPLICIT REAL*8(A-H,O-Z)` (4); 연속문(5–6): `      DIMENSION ISPC(2,NISPC),NSPC(N,*),SPC(6,*),ISPCW(2,*),NSPCW(N,*)` <br> `     &         ,SPCW(6,*),LNOD(*)`; `      IP = 0` (8); `      JP = 0` (9). |
| 11–33 | EX_SPC 루틴 안. ADDSET3로 집합 구간을 얻는다. LNOD 변환 번호가 1부터 NNODW까지인 항목만 뽑고 조건과 값을 복사한다. 비어 있지 않은 집합의 식별자·끝 위치와 최종 개수를 저장한다. 원문: `      DO I = 1, NISPC` (11); `        JP0 = JP` (12); `        CALL ADDSET3(JS,JE,ISPC,I)` (13); `        DO J = JS, JE` (14); `          LN = LNOD(NSPC(1,J))` (15); `          IF( LN > 0 .AND. LN <= NNODW ) THEN` (16); `            JP = JP + 1` (17); `            NSPCW(1,JP) = LN` (18); `            NSPCW(2:,JP) = NSPC(2:,J)` (19); `            SPCW(:,JP) = SPC(:,J)` (20); `          ENDIF` (21); `        ENDDO` (22); `        IF( JP > JP0 ) THEN` (23); `          IP = IP + 1` (24); `          ISPCW(1,IP) = ISPC(1,I)` (25); `          ISPCW(2,IP) = JP` (26); `        ENDIF` (27); `      ENDDO` (28); `      NISPCW = IP` (30); `      NNSPCW = JP` (31); `      END` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

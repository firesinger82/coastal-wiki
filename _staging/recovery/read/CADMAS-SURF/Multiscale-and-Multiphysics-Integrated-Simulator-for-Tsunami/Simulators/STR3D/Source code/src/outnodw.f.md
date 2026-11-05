---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/outnodw.f
lines: 77
sha256: c044feb1d95a2b3327c256c488ae1907377cf0b1e4620a468ab370390713e0cc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# outnodw.f — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | OUTNODW 입구와 배열 선언이다(1–6). NPFC 또는 NICRG 조건에서 변위 헤더를 쓴다(8). `IF( NPFC > 0 ) THEN`(12)에서는 `DO K = 1, NMAT`(14)마다 IP를 증가시킨다(16). 출력 파트 번호는 `N_PART + IP`이다(19). 각 파트에 UG의 세 성분을 기록한다(22–27). 원문: `      SUBROUTINE OUTNODW( UG, PPND, NNOD, NMAT, NPFC, NICRG, NIGSF,`<br>`     &                    N_PART, NG_ENSW, IG_ENSW, IFL )` (1–2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION IFL(*), UG(6,NNOD+NIGSF), NG_ENSW(NMAT+NICRG),`<br>`     &          IG_ENSW(NNOD+NIGSF,NMAT+NICRG), PPND(NNOD)` (5–6); `      IF( NPFC > 0 .OR. NICRG > 0 ) WRITE(IFL(20),'(A)') 'displacement'` (8); `      IP = 0` (10); `      IF( NPFC > 0 ) THEN` (12); `        DO K = 1, NMAT` (14); `          IP = IP + 1` (16); `          WRITE(IFL(20),'(A)') 'part'` (18); `          WRITE(IFL(20),'(I10)') N_PART + IP` (19); `          WRITE(IFL(20),'(A)') 'coordinates'` (20); `          DO J = 1, 3` (22); `            DO I = 1, NG_ENSW(IP)` (23); `              IG = IG_ENSW(I,IP)` (24); `              WRITE(IFL(20),'(1PE12.4)') UG(J,IG)` (25); `            ENDDO` (26); `          ENDDO` (27); `        ENDDO` (29); `      ENDIF` (31) [11-04 전수 검증 정정] |
| 33–53 | 시작 시 OUTNODW 루틴(1) 안이다. NICRG 조건에서는 추가 파트를 순서대로 기록한다(33–52). 원문: `      IF( NICRG > 0 ) THEN` (33); `        DO K = 1, NICRG` (35); `          IP = IP + 1` (37); `          WRITE(IFL(20),'(A)') 'part'` (39); `          WRITE(IFL(20),'(I10)') N_PART + IP` (40); `          WRITE(IFL(20),'(A)') 'coordinates'` (41); `          DO J = 1, 3` (43); `            DO I = 1, NG_ENSW(IP)` (44); `              IG = IG_ENSW(I,IP)` (45); `              WRITE(IFL(20),'(1PE12.4)') UG(J,IG)` (46); `            ENDDO` (47); `          ENDDO` (48); `        ENDDO` (50); `      ENDIF` (52) |
| 54–77 | 시작 시 OUTNODW 루틴(1) 안이다. `IF( NPFC > 0 ) THEN`(54)에서는 `DO K = 1, NMAT`(60)마다 IP를 증가시킨다(62). 출력 파트 번호는 `N_PART + IP`이다(65). 헤더 `'surface pressure'` 아래에 PPND(IG)를 IFL(21)에 기록한다(56·70). 원문: `      IF( NPFC > 0 ) THEN` (54); `        WRITE(IFL(21),'(A)') 'surface pressure'` (56); `        IP = 0` (58); `        DO K = 1, NMAT` (60); `          IP = IP + 1` (62); `          WRITE(IFL(21),'(A)') 'part'` (64); `          WRITE(IFL(21),'(I10)') N_PART + IP` (65); `          WRITE(IFL(21),'(A)') 'coordinates'` (66); `          DO I = 1, NG_ENSW(IP)` (68); `            IG = IG_ENSW(I,IP)` (69); `            WRITE(IFL(21),'(1PE12.4)') PPND(IG)` (70); `          ENDDO` (71); `        ENDDO` (73); `      ENDIF` (75); `      END` (77) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

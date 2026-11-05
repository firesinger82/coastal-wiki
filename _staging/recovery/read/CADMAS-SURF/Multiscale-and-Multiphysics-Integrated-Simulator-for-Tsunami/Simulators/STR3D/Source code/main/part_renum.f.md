---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/part_renum.f
lines: 72
sha256: c398871dbc1db52cf525c39023cfc25aa69f4c38f627d0aa747d9b17580569c9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# part_renum.f — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–72 | PART_RENUM은 두께·재료·봉 단면·보 단면 수의 최대값 MAXP로 IPART(MAXP,6)을 할당한다(6–16). 유형 1·3·4는 IELM(5,I), 유형 2·6은 IELM(4,I)를 부분 분류 속성으로 사용하고 유형 5는 건너뛴다(18–33). 유형 1:6과 속성 1:MAXP를 순회하며 사용된 조합에 연속 부분 번호를 부여한다(35–49). IP_ENS를 0으로 초기화한 뒤 같은 유형 분기로 번호를 매기고 IPART를 해제한다(51–70). 22–29행과 57–64행의 SELECT CASE에는 CASE DEFAULT가 없다. 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE PART_RENUM( N_PART, NP_ENS, IP_ENS, KK, IELM, NM )` (1) <br> `      DIMENSION NP_ENS(6), IP_ENS(*), KK(*), IELM(NM,*)` (3) <br> `      INTEGER, POINTER :: IPART(:,:)` (4) <br> `      NMAT  = KK(11)` (6) <br> `      NELM  = KK(12)` (7) <br> `      NTHK  = KK(13)` (8) <br> `      NRODA = KK(15)` (9) <br> `      NBARD = KK(17)` (10) <br> `      MAXP = MAX0( NTHK, NMAT, NRODA, NBARD )` (12) <br> `      ALLOCATE( IPART(MAXP,6) )` (14) <br> `      IPART(:,:) = 0` (16) <br> `      DO I = 1, NELM` (18) <br> `        ITYP = IELM(2,I)` (20) <br> `        SELECT CASE( ITYP )` (22) <br> `        CASE( 1, 3, 4 )` (23) <br> `          IPROP = IELM(5,I)` (24) <br> `        CASE( 2, 6 )` (25) <br> `          IPROP = IELM(4,I)` (26) <br> `        CASE( 5 )` (27) <br> `          CYCLE` (28) <br> `        END SELECT` (29) <br> `        IPART(IPROP,ITYP) = 1` (31) <br> `      ENDDO` (33) <br> `      IP = 0` (35) <br> `      NP_ENS(:) = 0` (37) <br> `      DO ITYP = 1, 6` (39) <br> `        DO IPROP = 1, MAXP` (40) <br> `          IF( IPART(IPROP,ITYP) == 1 ) THEN` (41) <br> `            IP = IP + 1` (42) <br> `            IPART(IPROP,ITYP) = IP` (43) <br> `            NP_ENS(ITYP) = NP_ENS(ITYP) + 1` (44) <br> `          ENDIF` (45) <br> `        ENDDO` (46) <br> `      ENDDO` (47) <br> `      N_PART = IP` (49) <br> `      IP_ENS(1:NELM) = 0` (51) <br> `      DO I = 1, NELM` (53) <br> `        ITYP = IELM(2,I)` (55) <br> `        SELECT CASE( ITYP )` (57) <br> `        CASE( 1, 3, 4 )` (58) <br> `          IPROP = IELM(5,I)` (59) <br> `        CASE( 2, 6 )` (60) <br> `          IPROP = IELM(4,I)` (61) <br> `        CASE( 5 )` (62) <br> `          CYCLE` (63) <br> `        END SELECT` (64) <br> `        IP_ENS(I) = IPART(IPROP,ITYP)` (66) <br> `      ENDDO` (68) <br> `      DEALLOCATE( IPART )` (70) <br> `      END` (72) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–28·62–63: 유형 5는 두 요소 순회에서 모두 CYCLE로 건너뛰므로 IP_ENS의 초기값 0이 유지된다(51).

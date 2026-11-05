---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/ncgset.f
lines: 81
sha256: 7513155317b534cfdb23e1dc4719e991497bef5a3b4bc753aba78ed2b038ca6e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ncgset.f — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | NCGSET은 NCGMAX·NCGMAXP를 0으로 시작한다(7–10). 유형 1의 ND=3·4·6·8/9는 NCG=42·54·114·126이다(17–29). 유형 2·6의 ND=4·6·8·10·15·20은 45·63·81·90·213·189다(31–46). 유형 6이면 NCGP=NCG/3 및 NCGMAXP 최대값을 계산한다(48–51). 유형 3·5는 NCG=45, 유형 4는 90이며 전 요소에서 최대값을 갱신한다(53–65). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE NCGSET(KK,IELM,NM)` (1) <br> `      USE MPI_PARAM` (3) <br> `      DIMENSION KK(*),IELM(NM,*)` (5) <br> `C-----------------------------------------------------------------------` (6) <br> `      NELM = KK(12)` (7) <br> `      NCGMAX = 0` (9) <br> `      NCGMAXP = 0` (10) <br> `      DO I = 1, NELM` (12) <br> `        ITYP = IELM(2,I)` (14) <br> `        ND = IELM(3,I)` (15) <br> `        SELECT CASE( ITYP )` (17) <br> `        CASE( 1 )` (18) <br> `          SELECT CASE( ND )` (20) <br> `          CASE( 3 )` (21) <br> `            NCG = 42` (22) <br> `          CASE( 4 )` (23) <br> `            NCG = 54` (24) <br> `          CASE( 6 )` (25) <br> `            NCG = 114` (26) <br> `          CASE( 8, 9 )` (27) <br> `            NCG = 126` (28) <br> `          END SELECT` (29) <br> `        CASE( 2, 6 )` (31) <br> `          SELECT CASE( ND )` (33) <br> `          CASE( 4 )` (34) <br> `            NCG = 45` (35) <br> `          CASE( 6 )` (36) <br> `            NCG = 63` (37) <br> `          CASE( 8 )` (38) <br> `            NCG = 81` (39) <br> `          CASE( 10 )` (40) <br> `            NCG = 90` (41) <br> `          CASE( 15 )` (42) <br> `            NCG = 213` (43) <br> `          CASE( 20 )` (44) <br> `            NCG = 189` (45) <br> `          END SELECT` (46) <br> `          IF( ITYP == 6 ) THEN` (48) <br> `            NCGP = NCG / 3` (49) <br> `            NCGMAXP = MAX0( NCGMAXP, NCGP )` (50) <br> `          ENDIF` (51) <br> `        CASE( 3, 5 )` (53) <br> `          NCG = 45` (55) <br> `        CASE( 4 )` (57) <br> `          NCG = 90` (59) <br> `        END SELECT` (61) <br> `        NCGMAX = MAX0( NCGMAX, NCG )` (63) <br> `      ENDDO` (65) |
| 66–81 | 시작 시 NCGSET(1) 안이며 앞 요소 루프 밖이다. MYRANK>0이면 두 최대값을 CG_MPI_ALLREDUCE_I로 집계한다(67–72). KK(24)·KK(25)에 결과를 저장하며 순위 1은 SEND_KK(KK,25)를 호출한다(74–77). KK(1)=0이고 KK(25)>0이면 KK(21)에 10을 더한다(79). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      IF( MYRANK > 0 ) THEN` (67) <br> `        CALL CG_MPI_ALLREDUCE_I(NCGMAX,MAX,1,1)` (68) <br> `        NCGMAX = MAX` (69) <br> `        CALL CG_MPI_ALLREDUCE_I(NCGMAXP,MAX,1,1)` (70) <br> `        NCGMAXP = MAX` (71) <br> `      ENDIF` (72) <br> `      KK(24) = NCGMAX` (74) <br> `      KK(25) = NCGMAXP` (75) <br> `      IF( MYRANK == 1 ) CALL SEND_KK(KK,25)` (77) <br> `      IF( KK(1) == 0 .AND. KK(25) > 0 ) KK(21) = KK(21) + 10` (79) <br> `      END` (81) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–61: SELECT CASE에는 CASE DEFAULT가 없다. 열거되지 않은 유형 또는 절점 수에서 NCG를 설정하는 분기는 없다.

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/pld_cadmas.f
lines: 54
sha256: fabb5bc53e19722b0e3e960522647d3297eee6205432ddd699d9e62ccd388144
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# pld_cadmas.f — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | PLD_CADMAS 입구와 배열 선언이다(1–6). DIR을 0으로 설정한다(8). AFC가 0인 면을 건너뛴다(10–12). `IF( IPND( NOD(J) ) > 0 ) THEN`(20)을 만족하는 항목의 수를 NDP에 센다(21). 해당 PPND의 합을 PA에 누적한다(22). NDP가 0이면 현재 I 반복을 건너뛴다(26–27). 0보다 크고 ND보다 작으면 P(1:ND)에 PA/DBLE(NDP)를 대입한다(28–29). ND와 같으면 개별 PPND를 복사한다(30–31). 이 분기 사슬에는 ELSE가 없다(26–32). 원문: `      SUBROUTINE PLD_CADMAS(FT,FT2,GRID,IELM,NM,NPFC,IPFC,AFC,IPND,PPND`<br>`     &                     ,ITO)` (1–2); `      IMPLICIT REAL*8 (A-H,O-Z)` (4); `      DIMENSION FT(6,*),GRID(3,*),IPFC(10,NPFC),FC(3,8),DIR(3),NOD(8)`<br>`     &         ,P(8),AFC(*),IPND(*),PPND(*),FT2(6,*),IELM(NM,*)` (5–6); `      DIR(:) = 0.` (8); `      DO I = 1, NPFC` (10); `        IF( AFC(I) == 0. ) CYCLE` (12); `        ND = IPFC(2,I)` (14); `        NOD(1:ND) = IPFC(3:2+ND,I)` (15); `        NDP = 0` (17); `        PA = 0.` (18); `        DO J = 1, ND` (19); `          IF( IPND( NOD(J) ) > 0 ) THEN` (20); `            NDP = NDP + 1` (21); `            PA = PA + PPND( NOD(J) )` (22); `          ENDIF` (23); `        ENDDO` (24); `        IF( NDP == 0 ) THEN` (26); `          CYCLE` (27); `        ELSEIF( NDP > 0 .AND. NDP < ND ) THEN` (28); `          P(1:ND) = PA / DBLE(NDP)` (29); `        ELSEIF( NDP == ND ) THEN` (30); `          P(1:ND) = PPND( NOD(1:ND) )` (31); `        END IF` (32) [11-04 전수 검증 정정] |
| 34–54 | 시작 시 PLD_CADMAS 루틴(1)·면 루프(10) 안이다. ND별 LOADTR1·LOADTR2·LOADQU2로 절점 하중을 구한다(34–41). ITYP==6이면 FT에서 빼고 그 외에는 FT2에서 뺀다(43–50). 원문: `        SELECT CASE( ND )` (34); `        CASE( 3 )` (35); `          CALL LOADTR1(GRID,NOD,P,DIR,0,IDUM,DUM,FC,ITO)` (36); `        CASE( 6 )` (37); `          CALL LOADTR2(GRID,NOD,P,DIR,0,IDUM,DUM,FC,ITO)` (38); `        CASE( 4, 8 )` (39); `          CALL LOADQU2(GRID,ND,NOD,P,DIR,0,IDUM,DUM,FC,ITO)` (40); `        END SELECT` (41); `        IE = IPFC(1,I)` (43); `        ITYP = IELM(2,IE)` (44); `        IF( ITYP == 6 ) THEN` (46); `          FT(1:3,NOD(1:ND)) = FT(1:3,NOD(1:ND)) - FC(:,1:ND) * AFC(I)` (47); `        ELSE` (48); `          FT2(1:3,NOD(1:ND)) = FT2(1:3,NOD(1:ND)) - FC(:,1:ND) * AFC(I)` (49); `        ENDIF` (50); `      ENDDO` (52); `      END` (54) 바깥 블록은 `DO I = 1, NPFC`(10)이며 52행의 ENDDO에서 닫힌다. 해석: LOADTR1·LOADTR2·LOADQU2의 FC를 절점 하중으로 보는 설명은 호출 이름에 따른 해석이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34–49: ND 분기는 3·6·4·8을 처리한다. CASE DEFAULT는 없으며, 이후 FC를 사용하는 FT·FT2 갱신은 SELECT CASE 밖에 있다.

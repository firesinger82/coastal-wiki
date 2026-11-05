---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/cgindx2_s.f
lines: 68
sha256: dc653d94c87ca865cd0c6ece41e8c277b11d2f8135348d012211617ffbb9595c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cgindx2_s.f — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | CGINDX2_S의 연속 인수·작업 배열 선언. 연결 작업 표와 연결 목록을 0으로 초기화하고 LAST를 자기 번호로 설정한다. 원문: 연속문(1–3): `      SUBROUTINE CGINDX2_S(NCGSPC,IDCGWK,N,IPREV,NEXT,LAST,IELM,NM,NELM` <br> `     &                    ,NELMC,NELMX,NEQ,NCRMAX,NCGMAX,MIDX,INDOF` <br> `     &                    ,INDMPC,MPCF,IMPC,INDOP,ISLV,ISEEP,ITO)`; 연속문(5–8): `      DIMENSION IDCGWK(NCGMAX,MIDX),N(MIDX),IPREV(MIDX),NEXT(MIDX)` <br> `     &         ,LAST(NEQ),IELM(NM,NELM+NELMC+NELMX),INDOF(6,*)` <br> `     &         ,INDMPC(2,6,*),MPCF(2,*),IDCR(2,NCRMAX),LOCEL(NCRMAX)` <br> `     &         ,INDOP(*)`; `      IDCGWK(:,:) = 0` (10); `      NIDX = NEQ` (12); `      N(:) = 0` (14); `      IPREV(:) = 0` (15); `      NEXT(:) = 0` (16); `      DO I = 1, NEQ` (18); `        LAST(I) = I` (19); `      ENDDO` (20). |
| 22–56 | CGINDX2_S 루틴 안. I=1부터 NELM+NELMC+NELMX까지 반복하되 NELM < I <= NELM+NELMC 구간은 건너뛴다. ISEEP=0에서는 9절점 유형 1을 8절점으로 줄인다. 유형 1·4의 자유도 수는 6, 나머지는 3이다. IDCRSET으로 자유도 목록을 얻는다. ISEEP /= 0이면 ITYP == 6인 경우에만 INDOP를 사용한다. 원문: `      DO I = 1, NELM + NELMC + NELMX` (22); `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (24); `        ITYP = IELM(2,I)` (26); `        ND = IELM(3,I)` (27); `        IF( ISEEP == 0 ) THEN` (29); `          IF( ITYP == 1 .AND. ND == 9 ) ND = 8` (31); `          IF( ITYP == 1 .OR. ITYP == 4 ) THEN` (33); `            NDF = 6` (34); `          ELSE` (35); `            NDF = 3` (36); `          ENDIF` (37); `          CALL IDCRSET(IMPC,IELM(8,I),ND,NDF,INDOF,INDMPC,MPCF,IDCR,NCR)` (39); `          DO J = 1, NCR` (41); `            LOCEL(J) = INDOF( IDCR(2,J), IDCR(1,J) )` (42); `          ENDDO` (43); `        ELSEIF( ITYP == 6 ) THEN` (45); `          NCR = ND` (47); `          LOCEL(1:ND) = INDOP( IELM(8:7+ND,I) )` (49); `        ELSE` (51); `          CYCLE` (53); `        ENDIF` (55). [11-04 전수 검증 정정] |
| 57–68 | 시작 시 `DO I = 1, NELM + NELMC + NELMX` (22, 종료 60) 안. CGINDX1로 요소 연결을 추가한다. 루프 뒤 NEQ와 각 목록 길이를 더해 NCGSPC를 계산한다. 원문: 연속문(57–58): `        CALL CGINDX1(IDCGWK,NCGMAX,MIDX,NIDX,N,IPREV,NEXT,LAST,LOCEL,NCR` <br> `     &              ,ISLV,ITO)`; `      ENDDO` (60); `      NCGSPC = NEQ` (62); `      DO I = 1, NIDX` (64); `        NCGSPC = NCGSPC + N(I)` (65); `      ENDDO` (66); `      END` (68). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

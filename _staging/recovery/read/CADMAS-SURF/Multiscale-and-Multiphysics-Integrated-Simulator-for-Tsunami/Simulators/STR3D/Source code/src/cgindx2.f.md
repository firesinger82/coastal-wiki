---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cgindx2.f
lines: 65
sha256: ed34a8a55a077647e21fa6ec6963207bef569d166d3b38626cec6ac83982ea54
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cgindx2.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | CGINDX2의 인수와 희소 인덱스(sparse index) 작업 배열을 선언한다. IDCGWK·N·IPREV·NEXT를 0으로 초기화하고 NIDX를 NEQ로 설정한다. NEQ개 LAST를 자기 인덱스로 초기화한다. 원문: `      SUBROUTINE CGINDX2(NCGSPC,IDCGWK,N,IPREV,NEXT,LAST,IELM,NM,NELM`<br>`     &                  ,NELMC,NELMX,NEQ,NCRMAX,NCGMAX,MIDX,INDOF,INDMPC`<br>`     &                  ,MPCF,IMPC,INDOP,ISLV,ITO)` (1–3); `      DIMENSION IDCGWK(NCGMAX,MIDX),N(MIDX),IPREV(MIDX),NEXT(MIDX)`<br>`     &         ,LAST(NEQ),IELM(NM,NELM+NELMC+NELMX),INDOF(6,*)`<br>`     &         ,INDMPC(2,6,*),MPCF(2,*),IDCR(2,NCRMAX),LOCEL(NCRMAX)`<br>`     &         ,LOCEP(20),INDOP(*)` (5–8); `      IDCGWK(:,:) = 0` (10); `      NIDX = NEQ` (12); `      N(:) = 0` (14); `      IPREV(:) = 0` (15); `      NEXT(:) = 0` (16); `      DO I = 1, NEQ` (18); `        LAST(I) = I` (19); `      ENDDO` (20). |
| 22–45 | 시작 시 1–3행 CGINDX2 루틴 안. I 루프는 `I > NELM .AND. I <= NELM + NELMC`이면 현재 반복을 건너뛴다. `ITYP == 1 .AND. ND == 9`이면 ND를 8로 바꾼다. ITYP가 1 또는 4이면 NDF를 6으로 둔다. 그 외에는 NDF를 3으로 둔다. 해석: I는 요소 번호이고 ND는 절점 수이며 NDF는 자유도 수이다. IDCRSET으로 IDCR을 얻고 LOCEL을 채운 뒤 CGINDX1을 호출한다. 원문: `      DO I = 1, NELM + NELMC + NELMX` (22); `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (24); `        ITYP = IELM(2,I)` (26); `        ND = IELM(3,I)` (27); `        IF( ITYP == 1 .AND. ND == 9 ) ND = 8` (29); `        IF( ITYP == 1 .OR. ITYP == 4 ) THEN` (31); `          NDF = 6` (32); `        ELSE` (33); `          NDF = 3` (34); `        ENDIF` (35); `        CALL IDCRSET(IMPC,IELM(8,I),ND,NDF,INDOF,INDMPC,MPCF,IDCR,NCR)` (37); `        DO J = 1, NCR` (39); `          LOCEL(J) = INDOF( IDCR(2,J), IDCR(1,J) )` (40); `        ENDDO` (41); `        CALL CGINDX1(IDCGWK,NCGMAX,MIDX,NIDX,N,IPREV,NEXT,LAST,LOCEL,NCR`<br>`     &              ,ISLV,ITO)` (43–44). [11-04 전수 검증 정정] |
| 46–65 | 시작 시 22행 `      DO I = 1, NELM + NELMC + NELMX` 안이다. 이 루프는 53행 `      ENDDO`에서 닫힌다. ITYP가 6일 때만 LOCEP를 구성하여 CGINDX1G를 호출한다. I 루프 종료 뒤 ISLV가 11 이하이면 NEQ부터, 그 외에는 0부터 N(I)를 누적하여 NCGSPC를 산출한다. 루틴 끝을 포함한다. 원문: `        IF( ITYP /= 6 ) CYCLE` (46); `        LOCEP(1:ND) = INDOP( IELM(8:7+ND,I) )` (48); `        CALL CGINDX1G(IDCGWK,NCGMAX,MIDX,NIDX,N,IPREV,NEXT,LAST,LOCEL`<br>`     &               ,NCR,LOCEP,ND,ISLV,ITO)` (50–51); `      ENDDO` (53); `      IF( ISLV <= 11 ) THEN` (55); `        NCGSPC = NEQ` (56); `      ELSE` (57); `        NCGSPC = 0` (58); `      ENDIF` (59); `      DO I = 1, NIDX` (61); `        NCGSPC = NCGSPC + N(I)` (62); `      ENDDO` (63); `      END` (65). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·48: LOCEP의 선언 크기는 20이다. LOCEP 대입 범위는 1:ND이며 이 파일에는 ND<=20 검사가 없다.

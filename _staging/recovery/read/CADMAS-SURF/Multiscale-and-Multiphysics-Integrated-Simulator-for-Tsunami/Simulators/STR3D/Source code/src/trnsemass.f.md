---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/trnsemass.f
lines: 64
sha256: 5efe35884fc3b1348daf4e91b16a368aa0281cf8add7d0d0b2ed36fca47efef2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# trnsemass.f — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | TRNSEMASS 입구와 배열 선언이다(1–4). ND·NDF로 압축 행렬 크기를 계산하고 EMASS를 0으로 초기화한다(6–9). NDF==3에서 LUMP==0은 EMASR(:,1)을 대각에 복사하고, ELSE는 MOD(I,3)==MOD(J,3)인 성분을 복사한다(11–32). 원문: `      SUBROUTINE TRNSEMASS(EMASS,EMASR,ND,NDF,LUMP)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION EMASS(*),EMASR(ND,ND)` (4); `      N1=ND*NDF` (6); `      N2=N1*(N1+1)/2` (7); `      CALL CLEAR1(EMASS,N2)` (9); `      IF( NDF .EQ. 3 ) THEN` (11); `        IF( LUMP .EQ. 0 ) THEN` (13); `          IP=1` (14); `          DO 200 I=1,N1` (15); `            II=(I-1)/3+1` (16); `            EMASS(IP)=EMASR(II,1)` (17); `            IP=IP+(N1-I+1)` (18); `  200     CONTINUE` (19); `        ELSE` (20); `          IP=0` (21); `          DO 100 I=1,N1` (22); `            DO 110 J=I,N1` (23); `              IP=IP+1` (24); `              IF( MOD(I,3) .EQ. MOD(J,3) ) THEN` (25); `                II=(I-1)/3+1` (26); `                JJ=(J-1)/3+1` (27); `                EMASS(IP)=EMASR(II,JJ)` (28); `              ENDIF` (29); `  110       CONTINUE` (30); `  100     CONTINUE` (31); `        ENDIF` (32) 해석: 대각 저장 위치와 방향 자유도라는 설명은 IP 증가식과 MOD 비교에 따른 행렬 저장 해석이다. [11-04 전수 검증 정정] |
| 34–64 | 시작 시 TRNSEMASS 루틴(1)·NDF 분기(11) 안이다. ELSEIF의 NDF==6 분기는 MOD(I,6)가 1부터 3인 항목을 채운다(34–44). LUMP가 0이 아니면 MOD(J,6)도 1부터 3이고 MOD(I,6)와 같아야 한다(50–52). 해석: 선택된 항목을 병진 자유도로 볼 수 있다. LUMP==0과 ELSE의 행렬 주소·복사식은 아래 원문과 같다. 원문: `      ELSEIF( NDF .EQ. 6 ) THEN` (34); `        IF( LUMP .EQ. 0 ) THEN` (36); `          IP=1` (37); `          DO 400 I=1,N1` (38); `            IF( MOD(I,6) .GE. 1 .AND. MOD(I,6) .LE. 3 ) THEN` (39); `              II=(I-1)/6+1` (40); `              EMASS(IP)=EMASR(II,1)` (41); `            ENDIF` (42); `            IP=IP+(N1-I+1)` (43); `  400     CONTINUE` (44); `        ELSE` (45); `          IP=0` (46); `          DO 300 I=1,N1` (47); `            DO 310 J=I,N1` (48); `              IP=IP+1` (49); `              IF( ( MOD(I,6) .GE. 1 .AND. MOD(I,6) .LE. 3 ) .AND.`<br>`     &            ( MOD(J,6) .GE. 1 .AND. MOD(J,6) .LE. 3 ) .AND.`<br>`     &            MOD(I,6) .EQ. MOD(J,6) ) THEN` (50–52); `                II=(I-1)/6+1` (53); `                JJ=(J-1)/6+1` (54); `                EMASS(IP)=EMASR(II,JJ)` (55); `              ENDIF` (56); `  310       CONTINUE` (57); `  300     CONTINUE` (58); `        ENDIF` (59); `      ENDIF` (61); `      RETURN` (63); `      END` (64) 바깥 분기는 `IF( NDF .EQ. 3 ) THEN`(11)에서 시작하며 61행에서 닫힌다. 이 IF/ELSEIF에는 ELSE가 없다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–61: NDF는 3·6 분기만 있다. 그 밖의 값에서는 CLEAR1 이후 EMASS를 채우는 분기가 없다.
- 39–55: NDF==6에서는 MOD(I,6)가 1부터 3인 항목만 복사한다. 그 외 나머지 4·5·0에 해당하는 항목은 CLEAR1 이후 다시 대입하지 않는다. 해석: 이 구분을 병진 성분과 회전 성분으로 볼 수 있다. [11-04 전수 검증 정정]

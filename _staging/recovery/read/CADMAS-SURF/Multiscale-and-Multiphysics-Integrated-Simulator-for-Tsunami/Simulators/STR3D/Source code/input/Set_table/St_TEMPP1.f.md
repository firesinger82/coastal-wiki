---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_TEMPP1.f
lines: 33
sha256: 935fa2703a007a0aaea5d4271257af8762891221def49ec0b4c74cdca72e32d5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_TEMPP1.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | ST_TEMPP1은 서로 다른 입력 세트 식별자를 ITP1에 모은다(8–16). 각 세트의 일치 입력에서 요소 외부 번호 IS:IE를 전개한다(18–31). IELR(K)=0인 요소는 건너뛰고 ITPF와 TMP1의 두 성분을 복사한다(23–28). TMP1 크기는 (2,NELM,NITP1)다(5–6). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_TEMPP1( ITP1, ITPF, TMP1, NITP1, J_TMP1, R_TMP1,` (1) <br> `     &                      N_TMP1, IELR, NELM )` (2) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (4) <br> `      DIMENSION ITP1(NITP1), ITPF(NELM,NITP1), TMP1(2,NELM,NITP1),` (5) <br> `     &          J_TMP1(4,N_TMP1), R_TMP1(2,N_TMP1), IELR(*)` (6) <br> `      N = 0` (8) <br> `      DO 10 I = 1, N_TMP1` (10) <br> `        DO J = 1, N` (11) <br> `          IF( J_TMP1(1,I) == ITP1(J) ) GOTO 10` (12) <br> `        ENDDO` (13) <br> `        N = N + 1` (14) <br> `        ITP1(N) = J_TMP1(1,I)` (15) <br> `   10 CONTINUE` (16) <br> `      DO I = 1, NITP1` (18) <br> `        DO J = 1, N_TMP1` (19) <br> `          IF( J_TMP1(1,J) == ITP1(I) ) THEN` (20) <br> `            IS = J_TMP1(2,J)` (21) <br> `            IE = J_TMP1(3,J)` (22) <br> `            DO K = IS, IE` (23) <br> `              IEL = IELR(K)` (24) <br> `              IF( IEL == 0 ) CYCLE` (25) <br> `              ITPF(IEL,I) = J_TMP1(4,J)` (26) <br> `              TMP1(:,IEL,I) = R_TMP1(:,J)` (27) <br> `            ENDDO` (28) <br> `          ENDIF` (29) <br> `        ENDDO` (30) <br> `      ENDDO` (31) <br> `      END` (33) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

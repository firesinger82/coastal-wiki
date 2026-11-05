---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_SUBCASE.f
lines: 58
sha256: 02077635ea9370b473d6064f7dd210dc138a291eb1533bf5e6d11da1313b9d11
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_SUBCASE.f — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | RD_SUBCASE는 CHAR·ISUB(13)을 선언한다(1–4). 6행 무한 루프(loop)에서 행을 읽는다(8). 10행 조건의 SUBCASE 또는 BEGIN BULK를 만나면 BACKSPACE 후 반환한다(11–12). GET_COMM(IP,IS,IE,CHAR)를 호출한다(15). 17행 조건은 IP가 0인 행을 건너뛴다. 원문: `      SUBROUTINE RD_SUBCASE( ISUB, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      DIMENSION ISUB(13)` (4); `      DO` (6); `        READ(ITI,'(A80)') CHAR` (8); `        IF( CHAR(1:7) == 'SUBCASE' .OR. CHAR(1:10) == 'BEGIN BULK' )THEN` (10); `          BACKSPACE(ITI)` (11); `          RETURN` (12); `        ENDIF` (13); `        CALL GET_COMM( IP, IS, IE, CHAR )` (15); `        IF( IP == 0 ) CYCLE` (17). [11-04 전수 검증 정정] |
| 19–58 | 시작 시 1행 RD_SUBCASE·6행 `DO` 안이며 이 루프는 56행 `ENDDO`에서 닫힌다. ELSE는 없으므로 미인식 문자열은 ISUB를 변경하지 않는다(19–54). 19·22·25·28·31행 조건은 LOAD·SPC·MPC·METHOD·TEMPERATURE(LOAD)를 ISUB(1:5)에 각각 읽는다(20·23·26·29·32). 34–35행 연속 조건의 TEMPERATURE(BOTH) 또는 TEMP는 ISUB(5)에 읽고 ISUB(10)에도 복사한다(36–37). 39·42·45·48·51행 DLOAD·FREQUENCY·NLPARM·TSTEP·BCSET는 각각 ISUB(7)·ISUB(9)·ISUB(11:13)에 저장한다(40·43·46·49·52). 분기·루프·루틴 종료와 주석을 포함한다(54–58). 원문: `        IF( CHAR(IS:IE) == 'LOAD' ) THEN` (19); `          READ(CHAR(IP+1:80),*) ISUB(1)` (20); `        ELSEIF( CHAR(IS:IE) == 'SPC' ) THEN` (22); `          READ(CHAR(IP+1:80),*) ISUB(2)` (23); `        ELSEIF( CHAR(IS:IE) == 'MPC' ) THEN` (25); `          READ(CHAR(IP+1:80),*) ISUB(3)` (26); `        ELSEIF( CHAR(IS:IE) == 'METHOD' ) THEN` (28); `          READ(CHAR(IP+1:80),*) ISUB(4)` (29); `        ELSEIF( CHAR(IS:IE) == 'TEMPERATURE(LOAD)' ) THEN` (31); `          READ(CHAR(IP+1:80),*) ISUB(5)` (32); `        ELSEIF( CHAR(IS:IE) == 'TEMPERATURE(BOTH)' .OR.` / `     &          CHAR(IS:IE) == 'TEMP' ) THEN` (34–35; 하나의 고정형식 연속문); `          READ(CHAR(IP+1:80),*) ISUB(5)` (36); `          ISUB(10) = ISUB(5)` (37); `        ELSEIF( CHAR(IS:IE) == 'DLOAD' ) THEN` (39); `          READ(CHAR(IP+1:80),*) ISUB(7)` (40); `        ELSEIF( CHAR(IS:IE) == 'FREQUENCY' ) THEN` (42); `          READ(CHAR(IP+1:80),*) ISUB(9)` (43); `        ELSEIF( CHAR(IS:IE) == 'NLPARM' ) THEN` (45); `          READ(CHAR(IP+1:80),*) ISUB(11)` (46); `        ELSEIF( CHAR(IS:IE) == 'TSTEP' ) THEN` (48); `          READ(CHAR(IP+1:80),*) ISUB(12)` (49); `        ELSEIF( CHAR(IS:IE) == 'BCSET' ) THEN` (51); `          READ(CHAR(IP+1:80),*) ISUB(13)` (52); `        ENDIF` (54); `      ENDDO` (56); `      END` (58). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·19–52: ISUB(6)·ISUB(8)은 이 루틴에서 대입하지 않는다.
- 8·10: READ에는 END·ERR·IOSTAT 지정이 없다. SUBCASE와 BEGIN BULK 검사는 1열부터의 문자열로 수행한다.

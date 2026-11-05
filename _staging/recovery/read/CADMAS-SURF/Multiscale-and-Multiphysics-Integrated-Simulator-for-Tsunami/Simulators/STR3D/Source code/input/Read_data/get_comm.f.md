---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/get_comm.f
lines: 26
sha256: 134577683389b360c399ce17dc4dddad2f93ec8a1bd2780f982e9562dbc7e6ef
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# get_comm.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | GET_COMM의 80자 CHAR 선언을 포함한다(1–3). 5행 루프(loop)는 '='를 검색한다(6). 발견하면 IP에 열 번호를 저장하고 GOTO 10으로 이동한다(7–8). 검색에 실패하면 IP=0으로 반환한다(12–13). 원문: `      SUBROUTINE GET_COMM( IP, IS, IE, CHAR )` (1); `      CHARACTER*80 CHAR` (3); `      DO I = 1, 80 ` (5); `        IF( CHAR(I:I) == '=' ) THEN` (6); `          IP = I` (7); `          GOTO 10` (8); `        ENDIF` (9); `      ENDDO` (10); `      IP = 0` (12); `      RETURN` (13). |
| 15–26 | 시작 시 1행 GET_COMM 안. 라벨(label) 10의 15행 루프가 '=' 앞의 첫 비공백 문자를 검색한다(16). IS를 저장한 뒤(17), 18행 내부 루프가 공백을 찾으면 EXIT한다(19). IE=J-1로 키(key)의 끝을 계산하고 바깥 루프도 EXIT한다(21–22). 끝 주석·END를 포함한다(25–26). 원문: `   10 DO I = 1, IP - 1` (15); `        IF( CHAR(I:I) /= ' ' ) THEN` (16); `          IS = I` (17); `          DO J = IS + 1, IP - 1` (18); `            IF( CHAR(J:J) == ' ' ) EXIT` (19); `          ENDDO` (20); `          IE = J - 1` (21); `          EXIT` (22); `        ENDIF` (23); `      ENDDO` (24); `      END` (26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–13·15–24: '='를 찾지 못하면 IS·IE를 대입하지 않는다. '=' 앞에 비공백 문자가 없는 경우에도 IS·IE 대입 경로가 없다.

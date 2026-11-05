---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/wt_data.f
lines: 27
sha256: 55e8ca326f7d8c2de2feade6390ea7495a192014173d644e6d55ba05fa07c546
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wt_data.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | WT_DATA는 길이 200의 CHAR1·CHAR2와 쉼표 C를 선언한다. IC=1·IP=0으로 시작한다. 원문: `      SUBROUTINE WT_DATA(CHAR1,IFL)` (1); `      CHARACTER*200 CHAR1,CHAR2` (3); `      CHARACTER*1 C /','/` (4); `      IC = 1` (6); `      IP = 0` (7) |
| 9–27 | 입력 문자열의 1–200 위치를 순서대로 훑는다. 공백이며 IC=0이면 쉼표를 한 번 추가하고 IC=1로 바꾼다. 이미 공백 상태면 CYCLE한다. 비공백은 IP를 증가시켜 해당 문자를 복사하고 IC=0으로 바꾼다. CHAR2(1:IP)를 출력한다. 원문: `      DO I = 1, 200` (9); `        IF( CHAR1(I:I) == ' ' ) THEN` (10); `          IF( IC == 0 ) THEN` (11); `            IP = IP + 1` (12); `            CHAR2(IP:IP) = C` (13); `            IC = 1` (14); `          ELSE` (15); `            CYCLE` (16); `          ENDIF` (17); `        ELSE` (18); `          IP = IP + 1` (19); `          CHAR2(IP:IP) = CHAR1(I:I)` (20); `          IC = 0` (21); `        ENDIF` (22); `      ENDDO` (23); `      WRITE(IFL,'(A)') CHAR2(1:IP)` (25); `      END` (27) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3·9: 처리할 입력 길이는 200자로 고정되어 있다.
- 10–23·25: 공백 경계에서 쉼표를 추가하며 루프 뒤 별도 끝 쉼표 추가문은 없다.

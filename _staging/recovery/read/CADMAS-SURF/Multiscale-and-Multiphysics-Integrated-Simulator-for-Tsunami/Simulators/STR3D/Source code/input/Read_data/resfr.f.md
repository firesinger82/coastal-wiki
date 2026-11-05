---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/resfr.f
lines: 13
sha256: 731186abec15c53c2210aa5d6196e054df0d759b7a46f1a1ed1059c94b2474d1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# resfr.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | RESFR는 8자 CHAR와 IFR(6)을 선언한다(1–4). 플래그(flag) 전체를 0으로 초기화한다(6). 8행 루프(loop)는 CHAR의 각 문자를 I1 형식으로 정수 NO에 읽는다(9). 10행 조건이 참이면 IFR(NO)=1로 설정한다. 루프 종료·주석·END를 포함한다(11–13). 원문: `      SUBROUTINE RESFR( IFR, CHAR )` (1); `      CHARACTER*8 CHAR` (3); `      DIMENSION IFR(6)` (4); `      IFR(:) = 0` (6); `      DO I = 1, 8` (8); `        READ(CHAR(I:I),'(I1)') NO` (9); `        IF( NO > 0 ) IFR(NO) = 1` (10); `      ENDDO` (11); `      END` (13). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·10: IFR의 크기는 6이다. 첨자 NO에 대한 실행 조건은 NO>0이며 NO<=6 검사는 없다.
- 9: 문자별 내부 READ에는 ERR·IOSTAT 지정이 없다.

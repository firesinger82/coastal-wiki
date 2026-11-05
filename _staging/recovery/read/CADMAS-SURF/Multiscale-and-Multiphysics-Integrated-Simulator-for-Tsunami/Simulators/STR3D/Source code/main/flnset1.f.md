---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/flnset1.f
lines: 19
sha256: 9d23ab6e7b41c80382564dfa871196e8b4f6b690511e93d937d272da054b605f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# flnset1.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | FLNSET1은 256자 파일명을 앞에서 검색하여 첫 마침표 직전 위치를 NLEN0로 설정한다(5–10). NLEN0+2부터 첫 공백을 찾고 직전 위치를 NLEN으로 설정한다(12–17). 각 검색은 첫 일치에서 EXIT한다(8·15). 인수·문자열 길이·주석을 포함한다(1–4). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE FLNSET1(FLNAME,NLEN0,NLEN)` (1) <br> `      CHARACTER FLNAME*256` (3) <br> `C----&------------------------------------------------------------------` (4) <br> `      DO I=1,256` (5) <br> `        IF(FLNAME(I:I) .EQ. '.') THEN` (6) <br> `          NLEN0=I-1` (7) <br> `          EXIT` (8) <br> `        ENDIF` (9) <br> `      ENDDO` (10) <br> `      DO I=NLEN0+2,256` (12) <br> `        IF(FLNAME(I:I) .EQ. ' ') THEN` (13) <br> `          NLEN=I-1` (14) <br> `          EXIT` (15) <br> `        ENDIF` (16) <br> `      ENDDO` (17) <br> `      END` (19) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–17: 마침표 또는 뒤 공백을 찾지 못하는 경우 NLEN0·NLEN에 별도 기본값을 대입하는 문장은 없다.

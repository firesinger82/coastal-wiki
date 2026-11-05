---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/ist_trs.f
lines: 38
sha256: e9eac74fd59a327c277ce3dbca9cc6cbf8394f994126ac5be9e724acbc189a58
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ist_trs.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | IST_TRS는 IST == 1이면 즉시 반환한다. ST > 0이고 S > ST이면 IST=1로 바꾸고 GR과 S를 0으로 한 뒤 반환한다. 원문: `      SUBROUTINE IST_TRS(IST,SY,EPSY,S,GR,E,ST,IYLD,HD,EPS)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      IF( IST == 1 ) RETURN` (5)； `      IF( ST > 0. ) THEN` (7)； `        IF( S > ST ) THEN` (8)； `          IST = 1` (9)； `          GR = 0.` (10)； `          S = 0.` (11)； `          RETURN` (12)； `        ENDIF` (13)； `      ENDIF` (14)。 |
| 16–38 | 시작 시 1행 IST_TRS 루틴 안이다. 5행 `IF( IST == 1 ) RETURN`에서 반환하지 않았다. 7행 `IF( ST > 0. ) THEN`과 8행 `IF( S > ST ) THEN`을 모두 만족할 때 실행되는 12행 RETURN도 실행하지 않았다. 16행 IF에는 ELSE가 없다. 17–35행 SELECT CASE에는 CASE DEFAULT가 없다. 19–25행 IF에도 ELSE가 없다. IYLD > 0이면 상태 0·2를 선택한다. 상태 0에서 S > SY이면 상태 2로 전환하여 GR과 S를 계산하고 EPSY·SY를 갱신한다. 상태 2는 S >= SY이면 이력을 갱신하고 ELSE이면 상태 0·GR=E로 바꿔 S를 계산한다. 원문: `      IF( IYLD > 0 ) THEN` (16)； `        SELECT CASE( IST )` (17)； `        CASE( 0 )` (18)； `          IF( S > SY ) THEN` (19)； `            IST = 2` (20)； `            GR = E * HD / ( E + HD )` (21)； `            S = SY + GR * ( EPS - EPSY )` (22)； `            EPSY = EPS` (23)； `            SY = S` (24)； `          ENDIF` (25)； `        CASE( 2 )` (26)； `          IF( S >= SY ) THEN` (27)； `            EPSY = EPS` (28)； `            SY = S` (29)； `          ELSE` (30)； `            IST = 0` (31)； `            GR = E` (32)； `            S = SY + GR * ( EPS - EPSY )` (33)； `          ENDIF` (34)； `        END SELECT` (35)； `      ENDIF` (36)； `      END` (38)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·27: 상태 0의 비교는 S > SY이고 상태 2의 비교는 S >= SY이다.
- 21: GR 식의 분모 E + HD가 0인지 검사하는 조건은 이 파일에 없다.

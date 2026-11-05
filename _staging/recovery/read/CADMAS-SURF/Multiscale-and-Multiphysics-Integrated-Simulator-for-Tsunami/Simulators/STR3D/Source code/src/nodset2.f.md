---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/nodset2.f
lines: 49
sha256: 4070e2d94b0f3fc6145ba9bd92c740b753f80817af8f4578703b417514f0d512
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# nodset2.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 입구와 암시적 형(implicit typing)·배열 선언이다(1–4). KN의 처음 네 항목에서 NODOP를 찾고 계산형 GOTO(computed GOTO)로 대응 블록에 진입한다(10–12). 찾지 못하면 ITO에 `'STOP IN SUB. NODSET2!'`를 쓴다(14). 이어서 ERRSTP(90,ITO)를 호출한다(15). 원문: `      SUBROUTINE NODSET2(KN,NODOP,NOD,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION KN(10),NOD(6)` (4); `      DO 100 I=1,4` (10); `        IF(KN(I).EQ.NODOP) GOTO(201,202,203,204) I` (11); `  100 CONTINUE` (12); `      WRITE(ITO,*) 'STOP IN SUB. NODSET2!'` (14); `      CALL ERRSTP(90,ITO)` (15) 계산형 GOTO의 대상 201·202·203·204는 각각 17·25·33·41행이다. [11-04 전수 검증 보완] |
| 17–32 | 시작 시 NODSET2 루틴(1) 안이다. 레이블 201·202에서 인용한 KN 항목을 NOD(1:6)에 복사하고 반환한다(17–31). 해석: 이 순서를 면의 꼭짓점과 중간 절점의 배열로 볼 수 있다. 원문: `  201 NOD( 1) = KN( 2)` (17); `      NOD( 2) = KN( 4)` (18); `      NOD( 3) = KN( 3)` (19); `      NOD( 4) = KN( 9)` (20); `      NOD( 5) = KN(10)` (21); `      NOD( 6) = KN( 6)` (22); `      RETURN` (23); `  202 NOD( 1) = KN( 1)` (25); `      NOD( 2) = KN( 3)` (26); `      NOD( 3) = KN( 4)` (27); `      NOD( 4) = KN( 7)` (28); `      NOD( 5) = KN(10)` (29); `      NOD( 6) = KN( 8)` (30); `      RETURN` (31) [11-04 전수 검증 정정] |
| 33–49 | 시작 시 NODSET2 루틴(1) 안이다. 레이블 203·204에서 인용한 KN 항목을 NOD(1:6)에 복사하고 반환한다(33–47). 해석: 두 배열은 나머지 두 면의 절점 순서를 나타낼 수 있다. 원문: `  203 NOD( 1) = KN( 1)` (33); `      NOD( 2) = KN( 4)` (34); `      NOD( 3) = KN( 2)` (35); `      NOD( 4) = KN( 8)` (36); `      NOD( 5) = KN( 9)` (37); `      NOD( 6) = KN( 5)` (38); `      RETURN` (39); `  204 NOD( 1) = KN( 1)` (41); `      NOD( 2) = KN( 2)` (42); `      NOD( 3) = KN( 3)` (43); `      NOD( 4) = KN( 5)` (44); `      NOD( 5) = KN( 6)` (45); `      NOD( 6) = KN( 7)` (46); `      RETURN` (47); `      END` (49) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

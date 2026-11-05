---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/ist_updt.f
lines: 40
sha256: d990bca0940ec9ef14fa66802702bff00972874f011c8c79e10af0d23b950054
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ist_updt.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | IST_UPDT의 배열 선언과 요소별 물성 준비 구간이다. KK에서 세 요소 수를 읽는다. NELM보다 크고 NELM+NELMC 이하인 요소는 건너뛴다. 남은 요소의 ITYP·NNP·IMAT와 재료 값을 읽는다. 원문: `      SUBROUTINE IST_UPDT(IST,SY,S,D,KK,MGP,NM,IELM,MAT,AMAT,EPS,ITO)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； 연속문(4–5): `      DIMENSION IELM(NM,*),MAT(2,*),AMAT(33,*),IST(MGP,*),S(6*MGP,*)` (4)； `     &         ,D(21*MGP,*),SY(MGP,*),EPS(6*MGP,*),KK(*)` (5)； `      NELM = KK(12)` (7)； `      NELMC = KK(29)` (8)； `      NELMX = KK(32)` (9)； `      DO I = 1, NELM + NELMC + NELMX` (11)； `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (13)； `        ITYP = IELM(2,I)` (15)； `        NNP  = IELM(3,I)` (16)； `        IMAT = IELM(4,I)` (17)； `        IYLD = MAT(2,IMAT)` (19)； `        E   = AMAT( 1,IMAT)` (21)； `        ANU = AMAT( 2,IMAT)` (22)； `        HD  = AMAT(12,IMAT)` (23)； `        ALP = AMAT(13,IMAT)` (24)； `        ST  = AMAT(14,IMAT)` (25)。 |
| 27–40 | 시작 시 1행 IST_UPDT 루틴과 11행 `DO I = 1, NELM + NELMC + NELMX` 안이다. 바깥 루프는 38행 ENDDO에서 닫힌다. 이 구간은 13행 `IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE`에서 건너뛰지 않은 반복에서 실행된다. ITYP가 2·6이면 IST_SOL을 호출한다. 3이면 IST_TRS에 SY의 두 행을 전달한다. 4이면 IST_BEAM을 호출한다. 선택과 요소 반복을 끝낸다. 원문: `        SELECT CASE( ITYP )` (27)； `        CASE( 2, 6 )` (28)； 연속문(29–30): `          CALL IST_SOL(IST(1,I),SY(1,I),S(1,I),D(1,I),NNP,E,ANU,ST,IYLD` (29)； `     &                ,HD,ALP,ITO)` (30)； `        CASE( 3 )` (31)； 연속문(32–33): `          CALL IST_TRS(IST(1,I),SY(1,I),SY(2,I),S(1,I),D(1,I),E,ST,IYLD` (32)； `     &                ,HD,EPS(1,I))` (33)； `        CASE( 4 )` (34)； `          CALL IST_BEAM(IST(1,I),SY(1,I),S(1,I),D(1,I),E,ANU,ST,IYLD,HD)` (35)； `        END SELECT` (36)； `      ENDDO` (38)； `      END` (40)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–36: ITYP의 SELECT CASE에는 CASE DEFAULT가 없다.
- 32–33: IST_TRS 호출에는 SY(1,I)와 SY(2,I)를 별도 인수로 전달한다.

---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/mergs.f
lines: 25
sha256: 5458060d67e6198e11b8b518d766fe03359b3d45f3a11009ab0f91b64ae5ca77
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mergs.f — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | MERGS의 배열 선언과 절점별 누적 평균(running mean) 계산이다. 대상 절점의 IAVE를 증가시키고 실수 ALP로 바꾼다. SIGG·EPSG의 여섯 성분과 PRNSIGG·PRNEPSG의 세 성분을 갱신한다. VMSIGG(NODE)도 갱신한다. 각 식은 저장값에 ALP-1을 곱하고 새 입력값을 더한 뒤 ALP로 나눈다. 해석: SIGG·EPSG는 응력·변형률 평균이고 PRNSIGG·PRNEPSG는 주응력(principal stress)·주변형률(principal strain) 평균이다. 원문: 연속문(1–2): `      SUBROUTINE MERGS(IAVE,SIGG,EPSG,SIG,EPS,PRNSIGG,PRNEPSG,PRNSIG` (1)； `     &                ,PRNEPS,VMSIGG,VMSIG,KN,ND)` (2)； `      IMPLICIT REAL*8(A-H,O-Z)` (4)； 연속문(5–7): `      DIMENSION KN(ND),IAVE(*),SIGG(6,*),EPSG(6,*),SIG(6,ND),EPS(6,ND)` (5)； `     &         ,PRNSIGG(3,*),PRNEPSG(3,*),PRNSIG(3,ND),PRNEPS(3,ND)` (6)； `     &         ,VMSIGG(*),VMSIG(ND)` (7)； `      DO 100 I=1,ND` (9)； `        NODE=KN(I)` (10)； `        IAVE(NODE)=IAVE(NODE)+1` (11)； `        ALP=DBLE(IAVE(NODE))` (12)； `        DO 200 J=1,6` (13)； `          SIGG(J,NODE)=( SIGG(J,NODE)*(ALP-1.D0) + SIG(J,I) ) / ALP` (14)； `          EPSG(J,NODE)=( EPSG(J,NODE)*(ALP-1.D0) + EPS(J,I) ) / ALP` (15)； `  200   CONTINUE` (16)； `        DO 300 J=1,3` (17)； `          PRNSIGG(J,NODE)=(PRNSIGG(J,NODE)*(ALP-1.D0)+PRNSIG(J,I))/ALP` (18)； `          PRNEPSG(J,NODE)=(PRNEPSG(J,NODE)*(ALP-1.D0)+PRNEPS(J,I))/ALP` (19)； `  300   CONTINUE` (20)； `        VMSIGG(NODE)=( VMSIGG(NODE)*(ALP-1.D0) + VMSIG(I) ) / ALP` (21)； `  100 CONTINUE` (22)； `      RETURN` (24)； `      END` (25)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–21: IAVE를 먼저 1 증가시킨 뒤 평균식의 분모 ALP로 사용한다. IAVE나 누적 배열을 초기화하는 문장은 이 파일에 없다.

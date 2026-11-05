---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/frcadd.f
lines: 12
sha256: a09442a447d762dea00a3bed4e7a27aa998ab4249120ebf5789f071b00585e3b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# frcadd.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | FRCADD의 배열 선언과 I=1..NN 반복이다. NFC(I)를 II에 대입한다. RMULT2에 FT(1,II)·FC(1,I)·SI·3을 전달한다. 해석: II는 대상 절점이고 마지막 인수 3은 처리 성분 수이다. 원문: `      SUBROUTINE FRCADD(NN,FC,NFC,SI,FT)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION FT(6,*),NFC(NN),FC(3,NN)` (4)； `      DO 100 I=1,NN` (6)； `        II=NFC(I)` (7)； `        CALL RMULT2(FT(1,II),FC(1,I),SI,3)` (8)； `  100 CONTINUE` (9)； `      RETURN` (11)； `      END` (12)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·8: FT의 첫 첨자 크기는 6이다. RMULT2 호출의 마지막 인수는 3이다. [11-04 전수 검증 정정]

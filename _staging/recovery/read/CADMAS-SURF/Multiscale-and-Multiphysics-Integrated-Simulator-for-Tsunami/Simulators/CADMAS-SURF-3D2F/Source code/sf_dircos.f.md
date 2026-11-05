---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_dircos.f
lines: 18
sha256: ac2e3593bd6efbfe82093b2b7cb136ec34487cea7aceee9cb106b96c1c29ebc7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_dircos.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SF_DIRCOS 선언과 벡터 정규화(normalization) 관계 주석(1–6). XL=0부터 B의 성분 제곱을 누적하고 제곱근을 구한다(8–12). 두 번째 루프에서 A(I)=B(I)/XL로 방향 코사인(direction cosine)을 반환한다(13–15). 원문: `      SUBROUTINE SF_DIRCOS(A,B,N)` (1)<br>`C     {A}={B}/\|B\|` (3)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (5)<br>`      DIMENSION A(N),B(N)` (6)<br>`      XL=0.` (8)<br>`      DO 100 I=1,N` (9)<br>`        XL=XL+B(I)*B(I)` (10)<br>`  100 CONTINUE` (11)<br>`      XL=DSQRT(XL)` (12)<br>`      DO 200 I=1,N` (13)<br>`        A(I)=B(I)/XL` (14)<br>`  200 CONTINUE` (15)<br>`      RETURN` (17)<br>`      END` (18) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–14: XL의 제곱근을 구한 뒤 0 검사 없이 각 성분을 XL로 나눈다.

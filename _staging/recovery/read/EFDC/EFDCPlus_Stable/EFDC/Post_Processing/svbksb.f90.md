---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Post_Processing/svbksb.f90
lines: 49
sha256: 808037f40c3613d86a52035ea94252d7f593e34027db87a4da9e7eed03622f71
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# svbksb.f90 — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | EFDC+·GPLv2·저작권 머리말(1–8). `SUBROUTINE SVBKSB(U,W,V,M,N,MP,NP,B,X)` (9). Numerical Recipes 출처 주석과 2014년 정수·실수 정밀도 변경 주석(11–14). implicit none, 크기·루프 인덱스, U(MP,NP)·W(NP)·V(NP,NP)·B(MP)·X(NP)·S 선언(15–20). save allocatable TMP 선언(21). `if( .not. allocated(TMP) )then` (23)이면 TMP(N)을 할당하고 0으로 초기화(24–25). |
| 28–38 | 시작 시 9행 SVBKSB 안. J=1..N에서 S=0(28–29). `if( W(J) /= 0. )then` (30)의 I=1..M 루프는 `S = S+U(I,J)*B(I)` (32)을 누적하고 `S = S/W(J)` (34)로 특이값(singular value)을 나눈다. 조건 밖에서 TMP(J)에 S 복사(36). W(J)=0이면 TMP(J)는 0이다. |
| 39–49 | 시작 시 9행 SVBKSB 안. J=1..N에서 S=0, JJ=1..N에 대해 `S = S+V(J,JJ)*TMP(JJ)` (42)을 누적(39–43). X(J)에 S 복사(44). TMP를 해제(46), 루틴 종료·마지막 빈 줄(48–49). 별도 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–34: 특이값 나눗셈의 조건은 W(J)와 0의 정확한 비교이다. 이 루틴에는 작은 비영 특이값을 제외하는 별도 허용오차 조건이 없다.

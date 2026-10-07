---
file: models/EFDC/raw/source_code/EFDC-GVC/lubksb.for
lines: 46
sha256: 48d07cc942741721a2d7f09005c18ddec62c7910b006505987cdf1b107829d20
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# lubksb.for — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 구분 주석과 `SUBROUTINE LUBKSB(A,N,NP,INDX,B)` 입구(1–6). EFDC-FULL 1.0a 및 2001-11-01 수정 주석(8–10), 변경 기록란과 빈 주석(12–20). |
| 21–35 | 시작 시 6행 LUBKSB 루틴 안. A(NP,NP)·INDX(N)·B(N) 선언(21), II=0(22). `DO 12 I=1,N` (23)로 전진 대입(forward substitution). LL=INDX(I), SUM=B(LL), B(LL)=B(I)로 우변(right-hand side)을 순열(permutation)에 따라 교환(24–26). `IF(II.NE.0)THEN` (27)은 `DO 11 J=II,I-1` (28)에서 `SUM=SUM-A(I,J)*B(J)` (29). 병렬 `ELSE IF(SUM.NE.0.)THEN` (31)은 II=I(32)로 첫 0 아닌 우변 위치를 기록한다. 조건 종료(33), B(I)=SUM(34), I 루프 종료 레이블 12(35). |
| 36–46 | 시작 시 6행 LUBKSB 루틴 안. `DO 14 I=N,1,-1` (36)로 후진 대입(back substitution). SUM=B(I)(37). `IF(I.LT.N)THEN` (38)이면 `DO 13 J=I+1,N` (39)에서 `SUM=SUM-A(I,J)*B(J)` (40). 조건 종료(42). `B(I)=SUM/A(I,I)` (43)으로 대각 성분을 나누어 해(solution)를 우변 배열 B에 저장한다. I 루프 종료 레이블 14(44), RETURN·END(45–46). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–26: LL은 INDX(I)에서 가져오며 곧바로 B(LL)를 참조한다. 이 위치에 LL이 1..N 범위인지 검사하는 조건은 없다.
- 43: 후진 대입은 A(I,I)로 나눈다. 이 나눗셈 앞에 대각 성분의 0 또는 작은 절댓값 검사는 없다.
- 21·23·36: A의 선언 크기는 NP×NP이며 두 대입 루프의 상한은 N이다. 이 루틴에는 N<=NP 검사가 없다.


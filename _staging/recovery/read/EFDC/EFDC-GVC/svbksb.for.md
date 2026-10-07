---
file: models/EFDC/raw/source_code/EFDC-GVC/svbksb.for
lines: 45
sha256: 8613f583993bd24811ea07d755317055b650261e66f01dd9875f383e2de6088e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# svbksb.for — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 구분 주석·SVBKSB(U,W,V,M,N,MP,NP,B,X) 입구(1–6). Numerical Recipes·EFDC-FULL 1.0a·2001-11-01 수정 및 변경 기록 주석(8–22). `INCLUDE 'EFDC.PAR'` (23). `PARAMETER (NMAX=100)` (25), U(MP,NP)·W(NP)·V(NP,NP)·B(MP)·X(NP)·TMP(NMAX) 선언(26). 특이값 분해(singular value decomposition)의 배열을 받는다. 포함 파일 내부는 이 판독 범위에 없다. |
| 27–36 | 시작 시 6행 SVBKSB 루틴 안. `DO 12 J=1,N` (27)에서 S=0(28). `IF(W(J).NE.0.)THEN` (29)이면 `DO 11 I=1,M` (30)에서 `S=S+U(I,J)*B(I)` (31), `S=S/W(J)` (33). 조건 종료 뒤 TMP(J)=S(35). W(J)=0이면 초기 S=0이 저장된다. J 루프 종료(36). |
| 37–45 | 시작 시 6행 SVBKSB 루틴 안이며 앞 J 루프 밖. `DO 14 J=1,N` (37)에서 S=0(38), `DO 13 JJ=1,N` (39)에서 `S=S+V(J,JJ)*TMP(JJ)` (40). X(J)=S(42), 루프 종료·RETURN·END(43–45). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–27·35: TMP의 고정 크기는 100이다. TMP(J)의 J 범위는 1..N이며 이 파일에는 N<=100 검사가 없다.
- 29·33: W(J)에 대한 나눗셈 검사는 정확한 0 비교이다. 작은 비영 특이값을 별도로 제한하는 조건은 없다.

---
file: models/EFDC/raw/source_code/EFDC-GVC/cvmulad2.for
lines: 20
sha256: a6eff9418f1b689a321417e7dc637811ddf4163c0bf5b2468fc531239838c49d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cvmulad2.for — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 구분 주석과 `SUBROUTINE CVMULAD2(N,A,B,C,D)` (6) 입구. 길이 N인 A/B/C/D 배열 선언(7). 벡터 곱셈·덧셈(vector multiply-add)이며 AltiVec C 루틴의 Fortran판이라는 주석(9). 구분·빈 주석 포함. |
| 11–20 | 시작 시 6행 CVMULAD2 루틴 안. `LM3=N-3` (11). `DO L=1,LM3,4` (12)는 시작 1·끝 N−3·증분 4이다. 네 원소 갱신은 `A(L  )=B(L  )+C(L  )*D(L  )` (13); `A(L+1)=B(L+1)+C(L+1)*D(L+1)` (14); `A(L+2)=B(L+2)+C(L+2)*D(L+2)` (15); `A(L+3)=B(L+3)+C(L+3)*D(L+3)` (16). END DO·주석·RETURN·END(17–20). 조건 분기·외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–17: 유일한 루프는 L=1..N-3를 증분 4로 진행하고 네 원소를 갱신한다. N을 4로 나눈 나머지 원소를 처리하는 별도 루프나 분기는 없다.


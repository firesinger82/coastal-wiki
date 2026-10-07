---
file: models/EFDC/raw/source_code/EFDC-GVC/fvmulad2.for
lines: 20
sha256: 914a4dad346fb04b201b45f290a2fd9b7b2246523f2bf6d0d64694cca9498d2f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fvmulad2.for — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 구분 주석과 `SUBROUTINE FVMULAD2(N,LC,A,B,C,D)` 선언(1–6). A/B/C/D를 N 크기의 배열로 선언한다(7). Fortran 벡터 곱셈·덧셈(vector multiply-add) 주석(9), 빈 주석(8·10). |
| 11–20 | 시작 시 6행 FVMULAD2 루틴 안. `LM3=LC-3` (11). `DO L=1,LM3,4` (12)에서 4개씩 펼친 식 `A(L  )=B(L  )+C(L  )*D(L  )` (13), `A(L+1)=B(L+1)+C(L+1)*D(L+1)` (14), `A(L+2)=B(L+2)+C(L+2)*D(L+2)` (15), `A(L+3)=B(L+3)+C(L+3)*D(L+3)` (16). 루프 종료·빈 주석·RETURN·END(17–20). 조건 분기와 외부 루틴 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·11–12: N은 배열 크기에 쓰인다. 실행 루프 상한은 N을 참조하지 않고 LC-3을 쓴다.
- 12–20: 루프는 4개 원소씩만 처리한다. LC가 4의 배수가 아닐 때 남은 원소를 별도로 처리하는 루프나 대입은 없다.

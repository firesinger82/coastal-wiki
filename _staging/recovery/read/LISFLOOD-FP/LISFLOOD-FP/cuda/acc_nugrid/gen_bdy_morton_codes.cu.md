---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/gen_bdy_morton_codes.cu
lines: 63
sha256: fa48955ae45ddcdf49a56019eaf207dad2a319d3e503bd8d366db18a6acdef01
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# gen_bdy_morton_codes.cu — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 헤더 포함(1), `lis::cuda::acc_nugrid::gen_bdy_morton_codes` 함수 정의(3–9). `const Boundary&`, `const Pars&`, `const int& direction`을 받는다(5–7). current는 0 초기화(10). `switch (direction)` (12)를 연다. 전처리 조건 분기는 없다. |
| 14–25 | 시작 시 3행 함수·12행 switch 안. `case SOUTH:` (14)는 `for (int i = 0; i < boundary.num_cells(); i++)` (16)에서 `current = boundary.start + i;` (18), `boundary.codes[i] = generate_morton_code(current, 0);` (21)로 y=0인 경계 셀의 모턴 코드(Morton code)를 만든다. y 최댓값을 쓰는 대체식은 주석(20). break로 case를 끝낸다(24–25). |
| 26–37 | 시작 시 3행 함수·12행 switch 안. `case NORTH:` (26)는 `for (int i = 0; i < boundary.num_cells(); i++)` (28)에서 `current = boundary.start + i;` (30), `boundary.codes[i] = generate_morton_code(current, pars.ysz - 1);` (33)로 y=pars.ysz-1인 경계 코드를 만든다. y=0 대체식은 주석(32). break와 case 종료(36–37). |
| 38–48 | 시작 시 3행 함수·12행 switch 안. `case EAST:` (38)는 `for (int i = 0; i < boundary.num_cells(); i++)` (40)에서 `current = boundary.start + i;` (42), `boundary.codes[i] = generate_morton_code(pars.xsz - 1, current);` (44)로 x=pars.xsz-1인 경계 코드를 만든다. break와 case 종료(47–48). |
| 49–63 | 시작 시 3행 함수·12행 switch 안. `case WEST:` (49)는 `for (int i = 0; i < boundary.num_cells(); i++)` (51)에서 `current = boundary.start + i;` (53), `boundary.codes[i] = generate_morton_code(0, current);` (55)로 x=0인 경계 코드를 만든다. break와 case 종료(58–59). `default:` (60)는 break만 실행한다(61). switch와 함수 종료(62–63). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

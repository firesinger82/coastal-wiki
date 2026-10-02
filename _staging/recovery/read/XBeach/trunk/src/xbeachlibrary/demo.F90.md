---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/demo.F90
lines: 109
sha256: babe833e2b1b4e27e0217604053fa9f7de201d158d2959c1f5934ae978ff25d7
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# demo.F90 — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | mnemonic 사용 시범 `program demo`. spacepars·slen·mnemmodule 사용(5–7). `nnames=4`, 이름 배열은 xz/x/cx/nx(12–13). mnemonic 상수로 컴파일러 오타 검사를 받는 대안은 주석(16–18). |
| 20–35 | `space_alloc_scalars(s)` 호출(21), xz(100)·x(120,10)·cx(10,10,10) 할당(25–28). 전체 배열용 space_alloc_arrays와 사전 s/par 값 필요 설명은 주석(30–32). |
| 36–50 | i=1..4에서 `setvar(s,names(i),dble(i))`(38–40), nx 및 xz/x/cx 첫 요소를 출력(44–47). program 종료(49). |
| 51–79 | `setvar(s,name,value)`는 real*8 value를 받음(54–60). `chartoindex(name)` → `indextos(s,index,t)` → 정보 로그·`printvar(t)`(65–69). 포인터 type/rank별 처리가 필요하다는 설명(72–77). |
| 80–93 | type='r'의 rank 0..4별 `t%r0/r1/r2/r3/r4=value`(84–92). 배열 분기는 부분 첨자가 없는 전체 배열 대입이다. |
| 94–109 | type='i'도 rank 0..4별 `t%i0/i1/i2/i3/i4=value`(97–105), real*8 value를 integer 변수로 대입. select와 루틴 종료(106–108), 마지막 빈 줄(109). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 51–53·84–105: 머리 주석은 이름으로 찾은 변수의 첫 요소를 0으로 설정한다고 적지만, 실제 대입은 전달받은 value이며 배열 전체에 적용된다.
- 81·94: case('r') 주석은 integer, case('i') 주석은 real*8이라고 적혀 있어 사용한 r/i 포인터 멤버와 반대이다.
- 60·97–105: value는 real*8로 선언되지만 integer 멤버 대입에 명시적 int/nint 변환 호출은 없다.

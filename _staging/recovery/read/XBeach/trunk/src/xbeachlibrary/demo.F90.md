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
| 1–19 | mnemonic 사용 예제 program과 모듈·변수 선언(4–14). nnames=4, names 배열은 xz·x·cx·nx(12–13); compiler가 오자를 잡는 대안 mnemonic 선언은 주석(16–18). 원문(조건·반복 블록 밖): `integer, parameter :: nnames = 4` (12). `character(slen), dimension(nnames),parameter :: names=(/'xz','x','cx','nx'/)` (13). |
| 20–50 | `space_alloc_scalars` 호출(21), xz(100), x(120,10), cx(10,10,10) 할당(25–28). i=1..nnames에서 `setvar`에 dble(i)를 전달(38–40), 지정 필드의 첫 원소·nx를 출력(44–47), program 종료(49). 원문(조건·반복 블록 밖): `call space_alloc_scalars(s)` (21). `allocate(s%xz(100))` (25). `allocate(s%x(120,10))` (27). `allocate(s%cx(10,10,10))` (28). `do i=1,nnames` (38). 원문(38행 반복 안): `call setvar(s,names(i),dble(i))` (39). `enddo` (40). |
| 51–79 | `setvar`의 목적 주석·입력과 arraytype 선언(51–63). `chartoindex`로 이름을 index로 바꾸고 `indextos`로 정보·포인터를 얻으며 `printvar` 호출(65–69). 이후 엄격한 pointer type/rank 선택 필요성 주석(71–77). 원문(조건·반복 블록 밖): `character(len=*) :: name` (59). `index = chartoindex(name)   !determine index from name` (65). `call indextos(s,index,t)    !get info and pointer` (66). `call printvar(t)` (69). |
| 80–93 | 조건 블록 밖에서 type select를 시작(80). r case(81) 안의 rank select는 0..4별 r0..r4에 value를 대입하고 종료(82–93). 원문(조건·반복 블록 밖): `select case (t%type)` (80). 원문(조건·반복 블록 밖 → 80행 select): `case ('r')      ! type is integer` (81). 원문(80행 select → 81행 case ('r')): `select case (t%rank)` (82). 원문(80행 select → 81행 case ('r') → 82행 select): `case(0)              ! scalar` (83). 원문(80행 select → 81행 case ('r') → 82행 select → 83행 case(0)): `t%r0 = value` (84). 원문(80행 select → 81행 case ('r') → 82행 select): `case(1)              ! (:)` (85). 원문(80행 select → 81행 case ('r') → 82행 select → 85행 case(1)): `t%r1 = value` (86). 원문(80행 select → 81행 case ('r') → 82행 select): `case(2)              ! (:,:)` (87). 원문(80행 select → 81행 case ('r') → 82행 select → 87행 case(2)): `t%r2 = value` (88). 원문(80행 select → 81행 case ('r') → 82행 select): `case(3)              ! (:,:,:)` (89). 원문(80행 select → 81행 case ('r') → 82행 select → 89행 case(3)): `t%r3 = value` (90). 원문(80행 select → 81행 case ('r') → 82행 select): `case(4)              ! (:,:,:,:)` (91). 원문(80행 select → 81행 case ('r') → 82행 select → 91행 case(4)): `t%r4 = value` (92). `end select` (93). |
| 94–109 | 첫 행은 80행 select의 병렬 i case이며 앞 r case 내부가 아니다. i case 안의 rank 0..4별 i0..i4 대입(95–106), type select·subroutine 종료 및 마지막 빈 줄(107–109). 첫 행의 바깥 범위: 조건·반복 블록 밖 → 80행 select. 원문(조건·반복 블록 밖 → 80행 select): `case ('i')     ! type is real*8` (94). 원문(80행 select → 94행 case ('i')): `select case (t%rank)` (95). 원문(80행 select → 94행 case ('i') → 95행 select): `case(0)              ! scalar` (96). 원문(80행 select → 94행 case ('i') → 95행 select → 96행 case(0)): `t%i0 = value` (97). 원문(80행 select → 94행 case ('i') → 95행 select): `case(1)              ! (:)` (98). 원문(80행 select → 94행 case ('i') → 95행 select → 98행 case(1)): `t%i1 = value` (99). 원문(80행 select → 94행 case ('i') → 95행 select): `case(2)              ! (:,:)` (100). 원문(80행 select → 94행 case ('i') → 95행 select → 100행 case(2)): `t%i2 = value` (101). 원문(80행 select → 94행 case ('i') → 95행 select): `case(3)              ! (:,:,:)` (102). 원문(80행 select → 94행 case ('i') → 95행 select → 102행 case(3)): `t%i3 = value` (103). 원문(80행 select → 94행 case ('i') → 95행 select): `case(4)              ! (:,:,:,:)` (104). 원문(80행 select → 94행 case ('i') → 95행 select → 104행 case(4)): `t%i4 = value` (105). `end select` (106). 원문(80행 select → 94행 case ('i')): `end select` (107). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 51–53·84–92·97–105: 주석은 첫 원소를 zero로 설정한다고 쓰지만 실제 대입은 전달받은 value를 scalar 또는 배열 포인터 전체에 넣는다.
- 81·94: r case 주석은 integer, i case 주석은 real*8이라고 쓰며 실제 대상 필드는 각각 r0..r4·i0..i4다.
- 80–107: type/rank select에 case default가 없다.

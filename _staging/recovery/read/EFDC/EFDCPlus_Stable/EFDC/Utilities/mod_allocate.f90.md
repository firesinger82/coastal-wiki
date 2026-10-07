---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/mod_allocate.f90
lines: 277
sha256: ec002485096f896aa1e45b231562c031acd0555f923246f708e968d48ee2ef38
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_allocate.f90 — 판독 구간 기록

구간은 1행부터 277행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | EFDC+·GPLv2 머리말(1–8), 할당과 초기화를 수행한다는 설명·작성자·날짜(9–11). Allocate_Initialize 모듈은 GLOBAL의 RKD·RK4를 사용한다(12–15). 공개 AllocateDSI 인터페이스가 정수 1–3차원, 논리 1–2차원, RK4 실수 1–4차원, RKD 실수 1–4차원 루틴을 묶는다(17–34). contains·빈 줄·구분 주석(35–39). 음수 크기는 해당 차원을 0부터 ABS(size)까지로 정의한다는 주석이다(40–41). |
| 43–57 | AllocateDSI_Integer1 인수·선언(43–46). `if( size1 < 0 )then` (48)은 `allocate(ArrIn(0:abs(size1)))` (49), `else` (50)는 `allocate(ArrIn(size1))` (51). 배열 전체에 iVal을 복사한다(54). 조건·루틴 종료와 빈 줄을 포함한다(52–57). |
| 58–76 | AllocateDSI_Integer2와 2차원 정수 배열 선언(58–61). `if( size1 > 0 .and. size2 > 0 )then` (63)은 `allocate(ArrIn(size1, size2))` (64). `elseif( size1 < 0 .and. size2 > 0 )then` (65)은 `allocate(ArrIn(0:abs(size1), size2))` (66). `elseif( size1 > 0 .and. size2 < 0 )then` (67)은 `allocate(ArrIn(size1, 0:abs(size2)))` (68). `else` (69)는 `allocate(ArrIn(0:abs(size1), 0:abs(size2)))` (70). 배열 전체 iVal 복사·루틴 종료·빈 줄(71–76). |
| 77–98 | AllocateDSI_Integer3와 3차원 정수 배열 선언(77–80). `if( size1 > 0 .and. size2 > 0  .and. size3 > 0 )then` (82)은 `allocate(ArrIn(size1, size2, size3))` (83). `elseif( size1 < 0 .and. size2 > 0 .and. size3 > 0 )then` (84)은 `allocate(ArrIn(0:abs(size1), size2, size3))` (85). `elseif( size1 > 0 .and. size2 < 0 .and. size3 > 0 )then` (86)은 `allocate(ArrIn(size1, 0:abs(size2), size3))` (87). `elseif( size1 > 0 .and. size2 > 0 .and. size3 < 0 )then` (88)은 `allocate(ArrIn(size1, size2, 0:abs(size3)))` (89). `else` (90)는 `allocate(ArrIn(0:abs(size1), 0:abs(size2), 0:abs(size3)))` (91). 전체 iVal 복사·종료·구분 주석(92–98). |
| 99–114 | AllocateDSI_Logical1의 논리 배열·크기·lVal 선언(99–103). `if( size1 < 0 )then` (105)은 `allocate(ArrIn(0:abs(size1)))` (106), `else` (107)는 `allocate(ArrIn(size1))` (108). 전체 lVal 복사·종료·빈 줄(109–114). |
| 115–135 | AllocateDSI_Logical2 선언(115–119). `if( size1 > 0 .and. size2 > 0 )then` (121)은 `allocate(ArrIn(size1, size2))` (122). `elseif( size1 < 0 .and. size2 > 0 )then` (123)은 `allocate(ArrIn(0:abs(size1), size2))` (124). `elseif( size1 > 0 .and. size2 < 0 )then` (125)은 `allocate(ArrIn(size1, 0:abs(size2)))` (126). `else` (127)는 `allocate(ArrIn(0:abs(size1), 0:abs(size2)))` (128). 전체 lval 복사·종료·구분 주석(129–135). |
| 136–151 | AllocateDSI_Real1은 real(RK4) 배열과 기본 real인 val을 받는다(136–140). `if( size1 < 0 )then` (142)은 `allocate(ArrIn(0:abs(size1)))` (143), `else` (144)는 `allocate(ArrIn(size1))` (145). 전체 Val 복사·종료·빈 줄(146–151). |
| 152–171 | AllocateDSI_Real2 선언(152–156). `if( size1 > 0 .and. size2 > 0 )then` (158)은 `allocate(ArrIn(size1, size2))` (159). `elseif( size1 < 0 .and. size2 > 0 )then` (160)은 `allocate(ArrIn(0:abs(size1), size2))` (161). `elseif( size1 > 0 .and. size2 < 0 )then` (162)은 `allocate(ArrIn(size1, 0:abs(size2)))` (163). `else` (164)는 `allocate(ArrIn(0:abs(size1), 0:abs(size2)))` (165). 전체 Val 복사·종료·빈 줄(166–171). |
| 172–193 | AllocateDSI_Real3 선언(172–176). `if( size1 > 0 .and. size2 > 0  .and. size3 > 0 )then` (178)은 `allocate(ArrIn(size1, size2, size3))` (179). `elseif( size1 <= 0 .and. size2 > 0 .and. size3 > 0 )then` (180)은 `allocate(ArrIn(0:abs(size1), size2, size3))` (181). `elseif( size1 > 0 .and. size2 <= 0 .and. size3 > 0 )then` (182)은 `allocate(ArrIn(size1, 0:abs(size2), size3))` (183). `elseif( size1 > 0 .and. size2 > 0 .and. size3 <= 0 )then` (184)은 `allocate(ArrIn(size1, size2, 0:abs(size3)))` (185). `else` (186)는 `allocate(ArrIn(0:abs(size1), 0:abs(size2), 0:abs(size3)))` (187). 전체 Val 복사·종료·빈 줄(188–193). |
| 194–206 | AllocateDSI_Real4와 4차원 real(RK4) 배열 선언(194–198). 조건 없이 `allocate(ArrIn(size1,size2,size3, size4))` (200). 전체 Val 복사(202), 루틴 종료·빈 줄·구분 주석(204–206). |
| 207–222 | AllocateDSI_RKD1은 real(RKD) 배열과 기본 real인 val을 받는다(207–211). `if( size1 < 0 )then` (213)은 `allocate(ArrIn(0:abs(size1)))` (214), `else` (215)는 `allocate(ArrIn(size1))` (216). 전체 Val 복사·종료·빈 줄(217–222). |
| 223–242 | AllocateDSI_RKD2 선언(223–227). `if( size1 > 0 .and. size2 > 0 )then` (229)은 `allocate(ArrIn(size1, size2))` (230). `elseif( size1 < 0 .and. size2 > 0 )then` (231)은 `allocate(ArrIn(0:abs(size1), size2))` (232). `elseif( size1 > 0 .and. size2 < 0 )then` (233)은 `allocate(ArrIn(size1, 0:abs(size2)))` (234). `else` (235)는 `allocate(ArrIn(0:abs(size1), 0:abs(size2)))` (236). 전체 Val 복사·종료·빈 줄(237–242). |
| 243–264 | AllocateDSI_RKD3 선언(243–247). `if( size1 > 0 .and. size2 > 0  .and. size3 > 0 )then` (249)은 `allocate(ArrIn(size1, size2, size3))` (250). `elseif( size1 < 0 .and. size2 > 0 .and. size3 > 0 )then` (251)은 `allocate(ArrIn(0:abs(size1), size2, size3))` (252). `elseif( size1 > 0 .and. size2 < 0 .and. size3 > 0 )then` (253)은 `allocate(ArrIn(size1, 0:abs(size2), size3))` (254). `elseif( size1 > 0 .and. size2 > 0 .and. size3 < 0 )then` (255)은 `allocate(ArrIn(size1, size2, 0:abs(size3)))` (256). `else` (257)는 `allocate(ArrIn(0:abs(size1), 0:abs(size2), 0:abs(size3)))` (258). 전체 Val 복사·종료·빈 줄(259–264). |
| 265–277 | AllocateDSI_RKD4와 4차원 real(RKD) 배열·기본 real val 선언(265–269). 조건 없이 `allocate(ArrIn(size1,size2,size3, size4))` (271). 전체 Val 복사(273), 루틴·모듈 종료와 빈 줄(275–277). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 43–275: 할당 루틴에는 allocated 검사·deallocate·allocate의 stat 인수가 없다.
- 82–91·178–187·249–258: Real3의 단일 비양수 차원 분기는 <=0을 사용한다. Integer3·RKD3의 대응 분기는 <0을 사용한다.
- 63–70·82–91 및 대응 Logical2·Real2·Real3·RKD2·RKD3: 마지막 else는 모든 차원을 0:abs(size)로 할당한다. 이 else에는 여러 비양수 차원이 들어올 수 있고, 양수인 나머지 차원에도 0 하한을 적용한다.
- 40–41·200·271: 음수 크기를 0:ABS(size)로 해석한다는 공통 주석이 있다. 두 4차원 루틴은 크기 부호 분기 없이 크기 인수를 그대로 allocate에 사용한다.
- 209–211·225–227·245–247·267–269: RKD 배열 루틴의 초기값 val은 real(RKD)가 아니라 기본 Real로 선언된다.

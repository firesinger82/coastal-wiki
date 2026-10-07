---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Mod_Map_Global_to_Local.f90
lines: 499
sha256: b6897c94c3a98cf8e8cbcd781c43f302bee575a42d79b4679f0663e993ca07d4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Map_Global_to_Local.f90 — 판독 구간 기록

구간은 1행부터 499행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | EFDC+ 출처·저작권·GPLv2 머리말(1–8). 전역(global) L 배열 LCM_Global을 지역(local) L 배열 LCM으로 매핑한다는 설명과 저자·날짜 주석(9–20). 모듈 시작(21), GLOBAL·Variables_MPI·Broadcast_Routines 사용(23–25), implicit none·Save(27–29). 공개 일반 인터페이스(generic interface) Map_Global_to_Local은 1차원 real(4)·real(8)·integer(4)·logical, 2차원 real(4)·real(8)·integer, 그룹 3차원 real(4)·real(8) 절차를 연결한다(31–45). contains·빈 줄(47–48). |
| 49–94 | 시작 시 21행 Mod_Map_Global_to_Local 모듈 안. `Map_Global_to_Local_RK4(Array)` 시작과 모듈·real(4) allocatable intent(inout) 인수·지역 변수 선언(49–62). `Broadcast_Array(Array, master_id)` 호출(65). ArrayG(LCM_Global)를 할당하고 0으로 초기화한다(68–69). `do LG = 1,LCM_Global` (71)에서 원래 Array를 ArrayG에 복사한다(72). Array를 해제한 뒤 Array(LCM)로 재할당하고 0으로 초기화한다(75–80). `do LG = 1,LCM_Global` (83)에서 L=Map2Local(LG).LL(84). `if( L > 0 )then` (85)이면 Array(L)에 ArrayG(LG)를 복사한다(86). ArrayG 해제·루틴 종료·빈 줄(90–94). |
| 95–141 | 시작 시 21행 모듈 안. `Map_Global_to_Local_RK8(Array)` 시작과 모듈·real(8) allocatable 인수·지역 변수 선언(95–108). `Broadcast_Array(Array, master_id)` 호출(111). ArrayG(LCM_Global)를 할당하고 0으로 초기화한다(114–115). `do LG = 1,LCM_Global` (117)에서 전역 값을 복사한다(118). Array를 해제하여 Array(LCM)로 재할당하고 0으로 초기화한다(121–126). `do LG = 1,LCM_Global` (129)에서 L 조회(130), `if( L > 0 )then` (131)이면 지역 값 복사(132). ArrayG 해제·루틴 종료·빈 줄(136–141). |
| 142–188 | 시작 시 21행 모듈 안. `Map_Global_to_Local_I4(Array)` 시작과 모듈·Integer(4) allocatable 인수·지역 변수 선언(142–155). `Broadcast_Array(Array, master_id)` 호출(158). ArrayG(LCM_Global) 할당과 `ArrayG(:) = 0.` (162). `do LG = 1,LCM_Global` (164)에서 전역 값을 복사한다(165). Array를 해제하여 Array(LCM)로 재할당하고 정수 0으로 초기화한다(168–173). `do LG = 1,LCM_Global` (176)에서 L 조회(177), `if( L > 0 )then` (178)이면 지역 값 복사(179). ArrayG 해제·루틴 종료·빈 줄(183–188). |
| 189–234 | 시작 시 21행 모듈 안. `Map_Global_to_Local_L4(Array)` 시작과 모듈·logical allocatable 인수·지역 변수 선언(189–202). `Broadcast_Array(Array, master_id)` 호출(205). ArrayG(LCM_Global)를 할당하고 .FALSE.로 초기화한다(208–209). `do LG = 1,LCM_Global` (211)에서 전역 값을 복사한다(212). Array를 해제하여 Array(LCM)로 재할당하고 .FALSE.로 초기화한다(215–220). `do LG = 1,LCM_Global` (223)에서 L 조회(224), `if( L > 0 )then` (225)이면 지역 논리값 복사(226). ArrayG 해제·루틴 종료·빈 줄(230–234). |
| 235–285 | 시작 시 21행 모듈 안. `Map_Global_to_Local_R2D(Array,KMAX)` 시작과 KMAX·real(4) 2차원 allocatable 인수·지역 변수 선언(235–249). `Broadcast_Array(Array, master_id)` 호출(252). ArrayG(LCM_Global,KMAX) 할당·0 초기화(255–256). `do K = 1,KMAX` (258), `do LG = 1,LCM_Global` (259)에서 전역 값을 복사한다(260). Array를 해제하여 Array(LCM,KMAX)로 재할당하고 0으로 초기화한다(264–269). `do K = 1,KMAX` (272), `do LG = 1,LCM_Global` (273)에서 L 조회(274), `if( L > 0 )then` (275)이면 Array(L,K)에 ArrayG(LG,K)를 복사한다(276). ArrayG 해제·루틴 종료·빈 줄(281–285). |
| 286–336 | 시작 시 21행 모듈 안. `Map_Global_to_Local_R2D_RK8(Array,KMAX)` 시작과 KMAX·real(8) 2차원 allocatable 인수·지역 변수 선언(286–300). `Broadcast_Array(Array, master_id)` 호출(303). ArrayG(LCM_Global,KMAX) 할당·0 초기화(306–307). `do K = 1,KMAX` (309), `do LG = 1,LCM_Global` (310)에서 전역 값 복사(311). Array를 해제하여 Array(LCM,KMAX)로 재할당하고 0으로 초기화한다(315–320). `do K = 1,KMAX` (323), `do LG = 1,LCM_Global` (324)에서 L 조회(325), `if( L > 0 )then` (326)이면 지역 값 복사(327). ArrayG 해제·루틴 종료·빈 줄(332–336). |
| 337–387 | 시작 시 21행 모듈 안. `Map_Global_to_Local_I2D(Array,KMAX)` 시작과 KMAX·integer 2차원 allocatable 인수·지역 변수 선언(337–351). `Broadcast_Array(Array, master_id)` 호출(354). ArrayG(LCM_Global,KMAX) 할당·정수 0 초기화(357–358). `do K = 1,KMAX` (360), `do LG = 1,LCM_Global` (361)에서 전역 값을 복사한다(362). Array를 해제하여 Array(LCM,KMAX)로 재할당하고 `Array = 0.` (371)로 초기화한다(366–371). `do K = 1,KMAX` (374), `do LG = 1,LCM_Global` (375)에서 L 조회(376), `if( L > 0 )then` (377)이면 지역 값 복사(378). ArrayG 해제·루틴 종료·빈 줄(383–387). |
| 388–441 | 시작 시 21행 모듈 안. `Map_Global_to_Local_GRP(Array,KMAX,NGRP)` 시작과 두 정수 범위·real(4) 3차원 allocatable 인수·지역 변수 선언(388–402). `Broadcast_Array(Array, master_id)` 호출(405). ArrayG(LCM_Global,KMAX,NGRP) 할당·0 초기화(408–409). `do NS = 1,NGRP` (411), `do K = 1,KMAX` (412), `do LG = 1,LCM_Global` (413)에서 전역 값을 복사한다(414). Array를 해제하여 Array(LCM,KMAX,NGRP)로 재할당하고 0으로 초기화한다(419–424). `do NS = 1,NGRP` (427), `do K = 1,KMAX` (428), `do LG = 1,LCM_Global` (429)에서 L 조회(430), `if( L > 0 )then` (431)이면 Array(L,K,NS)에 전역 값을 복사한다(432). ArrayG 해제·루틴 종료(438–441). |
| 442–499 | 시작 시 21행 모듈 안. `Map_Global_to_Local_GRP_RK8(Array,KMAX,NGRP)` 시작과 두 정수 범위·real(8) 3차원 allocatable 인수·지역 변수 선언(442–456). `Broadcast_Array(Array, master_id)` 호출(459). ArrayG(LCM_Global,KMAX,NGRP) 할당·0 초기화(462–463). `do NS = 1,NGRP` (465), `do K = 1,KMAX` (466), `do LG = 1,LCM_Global` (467)에서 전역 값을 복사한다(468). Array를 해제하여 Array(LCM,KMAX,NGRP)로 재할당하고 0으로 초기화한다(473–478). `do NS = 1,NGRP` (481), `do K = 1,KMAX` (482), `do LG = 1,LCM_Global` (483)에서 L 조회(484), `if( L > 0 )then` (485)이면 지역 값을 복사한다(486). ArrayG 해제·루틴·모듈 종료와 마지막 빈 줄(492–499). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 79·85·125·131·172·178·219·225·268·275·319·326·370·377·423·431·477·485: 재할당된 지역 배열의 첫 차원 크기는 LCM이다. 매핑된 L을 사용할 때의 조건은 L>0이며, 이 파일에는 L<=LCM 검사가 없다.
- 151·162·347·371: Integer(4) ArrayG의 초기화와 integer Array의 초기화 중 일부는 실수 리터럴 0.을 사용한다. 같은 정수 절차의 다른 초기화는 정수 리터럴 0을 사용한다(173·358).

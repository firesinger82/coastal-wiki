---
file: models/ROMS/raw/source_code/roms/ROMS/Include/set_bounds_xtr.h
lines: 74
sha256: 0a7a0d2910d5d0dde4f036bf49d28b559bd6a67975cbc8911e0bcd4755625e50
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_bounds_xtr.h — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·경계 할당 설명을 포함한다(1–13). 주석은 inp_par.F가 get_bounds.F의 get_tile을 호출하여 경계를 설정한다고 적는다(9–10). 타일 및 엇갈린 변수 경계 설명·tile=−1의 전역 격자 의미를 적는다(14–20). 기본·B/P/R/T/M/U/V 경계와 ±1/2/3 확장 경계 정수들을 선언한다(21–28). 주석 줄을 포함한다(29). |
| 30–42 | 시작 시 열린 전처리 조건 없음. 현재 ng·tile의 xtr_BOUNDS 구조에서 Istr/IstrB/IstrM/IstrP/IstrR/IstrT/IstrU·Iend/IendB/IendP/IendR/IendT를 같은 이름의 지역 변수로 복사한다(30–41). 경계값을 새로 계산하는 식은 이 블록에 없다. 빈 줄을 포함한다(42). 원문: `Istr   =xtr_BOUNDS(ng) % Istr   (tile)` (30); `IstrB  =xtr_BOUNDS(ng) % IstrB  (tile)` (31); `IstrM  =xtr_BOUNDS(ng) % IstrM  (tile)` (32); `IstrP  =xtr_BOUNDS(ng) % IstrP  (tile)` (33); `IstrR  =xtr_BOUNDS(ng) % IstrR  (tile)` (34); `IstrT  =xtr_BOUNDS(ng) % IstrT  (tile)` (35); `IstrU  =xtr_BOUNDS(ng) % IstrU  (tile)` (36); `Iend   =xtr_BOUNDS(ng) % Iend   (tile)` (37); `IendB  =xtr_BOUNDS(ng) % IendB  (tile)` (38); `IendP  =xtr_BOUNDS(ng) % IendP  (tile)` (39); `IendR  =xtr_BOUNDS(ng) % IendR  (tile)` (40); `IendT  =xtr_BOUNDS(ng) % IendT  (tile)` (41). |
| 43–55 | 시작 시 열린 전처리 조건 없음. 현재 ng·tile의 xtr_BOUNDS 구조에서 Jstr/JstrB/JstrM/JstrP/JstrR/JstrT/JstrV·Jend/JendB/JendP/JendR/JendT를 같은 이름의 지역 변수로 복사한다(43–54). 주석 줄을 포함한다(55). 원문: `Jstr   =xtr_BOUNDS(ng) % Jstr   (tile)` (43); `JstrB  =xtr_BOUNDS(ng) % JstrB  (tile)` (44); `JstrM  =xtr_BOUNDS(ng) % JstrM  (tile)` (45); `JstrP  =xtr_BOUNDS(ng) % JstrP  (tile)` (46); `JstrR  =xtr_BOUNDS(ng) % JstrR  (tile)` (47); `JstrT  =xtr_BOUNDS(ng) % JstrT  (tile)` (48); `JstrV  =xtr_BOUNDS(ng) % JstrV  (tile)` (49); `Jend   =xtr_BOUNDS(ng) % Jend   (tile)` (50); `JendB  =xtr_BOUNDS(ng) % JendB  (tile)` (51); `JendP  =xtr_BOUNDS(ng) % JendP  (tile)` (52); `JendR  =xtr_BOUNDS(ng) % JendR  (tile)` (53); `JendT  =xtr_BOUNDS(ng) % JendT  (tile)` (54). |
| 56–74 | 시작 시 열린 전처리 조건 없음. xtr_BOUNDS의 Istrm3/Istrm2/Istrm1/IstrUm2/IstrUm1·Iendp1/Iendp2/Iendp2i/Iendp3와 대응 J 확장 경계를 지역 변수로 복사한다(56–74). 주석은 각각 시작−3/−2/−1·U/V 시작−2/−1·끝+1/+2/+3·끝+2 interior를 설명한다. 이 파일에는 if·전처리 지시문·루틴 호출이 없다. 원문: `Istrm3 =xtr_BOUNDS(ng) % Istrm3 (tile)            ! Istr-3` (56); `Istrm2 =xtr_BOUNDS(ng) % Istrm2 (tile)            ! Istr-2` (57); `Istrm1 =xtr_BOUNDS(ng) % Istrm1 (tile)            ! Istr-1` (58); `IstrUm2=xtr_BOUNDS(ng) % IstrUm2(tile)            ! IstrU-2` (59); `IstrUm1=xtr_BOUNDS(ng) % IstrUm1(tile)            ! IstrU-1` (60); `Iendp1 =xtr_BOUNDS(ng) % Iendp1 (tile)            ! Iend+1` (61); `Iendp2 =xtr_BOUNDS(ng) % Iendp2 (tile)            ! Iend+2` (62); `Iendp2i=xtr_BOUNDS(ng) % Iendp2i(tile)            ! Iend+2 interior` (63); `Iendp3 =xtr_BOUNDS(ng) % Iendp3 (tile)            ! Iend+3` (64); `Jstrm3 =xtr_BOUNDS(ng) % Jstrm3 (tile)            ! Jstr-3` (66); `Jstrm2 =xtr_BOUNDS(ng) % Jstrm2 (tile)            ! Jstr-2` (67); `Jstrm1 =xtr_BOUNDS(ng) % Jstrm1 (tile)            ! Jstr-1` (68); `JstrVm2=xtr_BOUNDS(ng) % JstrVm2(tile)            ! JstrV-2` (69); `JstrVm1=xtr_BOUNDS(ng) % JstrVm1(tile)            ! JstrV-1` (70); `Jendp1 =xtr_BOUNDS(ng) % Jendp1 (tile)            ! Jend+1` (71); `Jendp2 =xtr_BOUNDS(ng) % Jendp2 (tile)            ! Jend+2` (72); `Jendp2i=xtr_BOUNDS(ng) % Jendp2i(tile)            ! Jend+2 interior` (73); `Jendp3 =xtr_BOUNDS(ng) % Jendp3 (tile)            ! Jend+3` (74). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

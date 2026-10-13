---
file: models/ROMS/raw/source_code/roms/ROMS/Include/set_bounds.h
lines: 74
sha256: 069d21af90d4ad659ad2ed61777feab6b183fc29661f27726298614c30670365
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_bounds.h — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·경계 할당 설명을 포함한다(1–13). 주석은 inp_par.F가 get_bounds.F의 get_tile을 호출하여 경계를 설정한다고 적는다(9–10). 타일 경계와 엇갈린 변수(staggered variable) 경계 설명 및 tile=−1의 전역 격자 의미를 적는다(14–20). 기본·B/P/R/T/M/U/V 경계와 ±1/2/3 확장 경계 정수들을 선언한다(21–28). 주석 줄을 포함한다(29). |
| 30–42 | 시작 시 열린 전처리 조건 없음. 현재 ng·tile의 BOUNDS 구조에서 Istr/IstrB/IstrM/IstrP/IstrR/IstrT/IstrU·Iend/IendB/IendP/IendR/IendT를 같은 이름의 지역 변수로 복사한다(30–41). 경계값을 새로 계산하는 식은 이 블록에 없다. 빈 줄을 포함한다(42). 원문: `Istr   =BOUNDS(ng) % Istr   (tile)` (30); `IstrB  =BOUNDS(ng) % IstrB  (tile)` (31); `IstrM  =BOUNDS(ng) % IstrM  (tile)` (32); `IstrP  =BOUNDS(ng) % IstrP  (tile)` (33); `IstrR  =BOUNDS(ng) % IstrR  (tile)` (34); `IstrT  =BOUNDS(ng) % IstrT  (tile)` (35); `IstrU  =BOUNDS(ng) % IstrU  (tile)` (36); `Iend   =BOUNDS(ng) % Iend   (tile)` (37); `IendB  =BOUNDS(ng) % IendB  (tile)` (38); `IendP  =BOUNDS(ng) % IendP  (tile)` (39); `IendR  =BOUNDS(ng) % IendR  (tile)` (40); `IendT  =BOUNDS(ng) % IendT  (tile)` (41). |
| 43–55 | 시작 시 열린 전처리 조건 없음. 현재 ng·tile의 BOUNDS 구조에서 Jstr/JstrB/JstrM/JstrP/JstrR/JstrT/JstrV·Jend/JendB/JendP/JendR/JendT를 같은 이름의 지역 변수로 복사한다(43–54). 주석 줄을 포함한다(55). 원문: `Jstr   =BOUNDS(ng) % Jstr   (tile)` (43); `JstrB  =BOUNDS(ng) % JstrB  (tile)` (44); `JstrM  =BOUNDS(ng) % JstrM  (tile)` (45); `JstrP  =BOUNDS(ng) % JstrP  (tile)` (46); `JstrR  =BOUNDS(ng) % JstrR  (tile)` (47); `JstrT  =BOUNDS(ng) % JstrT  (tile)` (48); `JstrV  =BOUNDS(ng) % JstrV  (tile)` (49); `Jend   =BOUNDS(ng) % Jend   (tile)` (50); `JendB  =BOUNDS(ng) % JendB  (tile)` (51); `JendP  =BOUNDS(ng) % JendP  (tile)` (52); `JendR  =BOUNDS(ng) % JendR  (tile)` (53); `JendT  =BOUNDS(ng) % JendT  (tile)` (54). |
| 56–74 | 시작 시 열린 전처리 조건 없음. BOUNDS의 Istrm3/Istrm2/Istrm1/IstrUm2/IstrUm1·Iendp1/Iendp2/Iendp2i/Iendp3와 대응 J 확장 경계를 지역 변수로 복사한다(56–74). 주석은 각각 시작−3/−2/−1·U/V 시작−2/−1·끝+1/+2/+3·끝+2 interior를 설명한다. 이 파일에는 if·전처리 지시문·루틴 호출이 없다. 원문: `Istrm3 =BOUNDS(ng) % Istrm3 (tile)            ! Istr-3` (56); `Istrm2 =BOUNDS(ng) % Istrm2 (tile)            ! Istr-2` (57); `Istrm1 =BOUNDS(ng) % Istrm1 (tile)            ! Istr-1` (58); `IstrUm2=BOUNDS(ng) % IstrUm2(tile)            ! IstrU-2` (59); `IstrUm1=BOUNDS(ng) % IstrUm1(tile)            ! IstrU-1` (60); `Iendp1 =BOUNDS(ng) % Iendp1 (tile)            ! Iend+1` (61); `Iendp2 =BOUNDS(ng) % Iendp2 (tile)            ! Iend+2` (62); `Iendp2i=BOUNDS(ng) % Iendp2i(tile)            ! Iend+2 interior` (63); `Iendp3 =BOUNDS(ng) % Iendp3 (tile)            ! Iend+3` (64); `Jstrm3 =BOUNDS(ng) % Jstrm3 (tile)            ! Jstr-3` (66); `Jstrm2 =BOUNDS(ng) % Jstrm2 (tile)            ! Jstr-2` (67); `Jstrm1 =BOUNDS(ng) % Jstrm1 (tile)            ! Jstr-1` (68); `JstrVm2=BOUNDS(ng) % JstrVm2(tile)            ! JstrV-2` (69); `JstrVm1=BOUNDS(ng) % JstrVm1(tile)            ! JstrV-1` (70); `Jendp1 =BOUNDS(ng) % Jendp1 (tile)            ! Jend+1` (71); `Jendp2 =BOUNDS(ng) % Jendp2 (tile)            ! Jend+2` (72); `Jendp2i=BOUNDS(ng) % Jendp2i(tile)            ! Jend+2 interior` (73); `Jendp3 =BOUNDS(ng) % Jendp3 (tile)            ! Jend+3` (74). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

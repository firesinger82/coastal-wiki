---
file: models/ADCIRC/raw/source_code/adcirc/src/internaltide.F90
lines: 249
sha256: 86a0d9c1cf45349bac282d810af5228142acea77d0ca0adcef6a25d6dc76719e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# internaltide.F90 — 판독 구간 기록

구간은 1행부터 249행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | ADCIRC 명칭·1994–2025 저작권·LGPL 3 이상·무보증 머리말(1–19), 구분 주석·빈 줄(20–21). logging_macros.h 포함 및 빈 줄(22–23). |
| 24–51 | INTERNALTIDE 모듈 입구(24). 2023년 3월 CPB 주석은 nodalattr.F의 apply2dinternalwavedrag 가독성을 위해 조석 제거(de-tiding) 속도 계산을 이동했다고 적는다(26–31). mod_logging 사용·implicit none·기본 private(33–37). 이동 평균(moving average)의 표본 저장 UAV/VAV, 평균 속도 UBar/VBar, 필터(filter) 가중치 wts를 real(8) allocatable로 선언한다(39–45). UNTIDE·MunkHPFilter·UBar·VBar 공개(47), contains 및 구분 주석(48–51). |
| 52–88 | 시작 시 24행 INTERNALTIDE 모듈 안. UNTIDE 입구(52). 주석은 현재 속도를 받아 12분 표본의 25시간 지연 평균(lagged average)을 갱신한다고 적는다(54–60). NP·DTDP 사용·implicit none·입력 속도 U_i/V_i·TimeStep(62–66). 상수와 저장 기본값은 `real(8), parameter :: filtL = 25d0*3600d0 ! filter length (s)` (67); `real(8), parameter :: Fs = 12d0*60d0 ! sampling interval (s)` (68); `integer, save :: NS = 1 ! number of samples` (69); `logical, save :: first_call = .true.` (70). 시간 창(window) 인덱스 L/Lm·반복 인덱스·저장 ISTA 선언(71–76). `if (first_call) then` (78)이면 first_call=false(79), `NS = floor(filtL/Fs)` (80), ista=1(81). UAV/VAV를 (NP,NS), UBar/VBar를 NP로 할당하고 모두 0d0로 초기화한다(82–87). 최초 호출 조건 종료(88). |
| 89–118 | 시작 시 24행 INTERNALTIDE 모듈·52행 UNTIDE 루틴 안. `L = floor(dble(TimeStep)*DTDP/Fs)` (90); `Lm = floor(dble(TimeStep - 1)*DTDP/Fs)` (91)로 현재/직전 시간 단계의 12분 창 인덱스를 구한다. `if (L > Lm) then` (92) 안 `if (ISTA > NS) then` (93)이면 `do ii = 1, NP` (94)·`do kk = 1, NS - 1` (95)에서 UAV/VAV의 다음 표본을 앞 칸으로 복사(96–97)하고 마지막 칸에 현재 속도를 저장한다(99–100). `do ii = 1, NP` (102)에서 `UBar(ii) = sum(UAV(ii, 1:NS))/dble(NS)` (103); `VBar(ii) = sum(VAV(ii, 1:NS))/dble(NS)` (104)로 전체 NS 표본의 산술 평균(arithmetic mean)을 구한다. else(106)는 `do ii = 1, NP` (107)에서 현재 속도를 ISTA 칸에 저장(108–109)·`UBar(ii) = sum(UAV(ii, 1:ISTA))/dble(ISTA)` (110); `VBar(ii) = sum(VAV(ii, 1:ISTA))/dble(ISTA)` (111)로 채워진 표본만 평균한다. `ISTA = ISTA + 1` (113). 조건·UNTIDE 종료·구분 주석(114–118). |
| 119–158 | 시작 시 24행 INTERNALTIDE 모듈 안. MunkHPFilter 입구(119). Munk 'Tide Killer' 저역 통과 필터(low-pass filter)의 계수를 사용해 고역 통과 필터(high-pass filter)를 만든다는 주석과 원문 URL(121–125). 주석의 계수 관계는 `!        W^{HP}_0 = 1-W^{LP}_0` (130); `!        W^{HP}_k = -W^{LP}_k   (k not equal to 0)` (131), 적용식은 `!        y_n = \sum_{k=-m}^m W_k * x_{n+k}` (135). 주석은 출력이 현재 시간 단계보다 25시간 지연되고 반일주(semi-diurnal) 주기의 약 두 배라고 적는다(137–140). 작성자·작성 시기(142). NP·DTDP·implicit none·입력 속도/TimeStep 선언(144–148). 상수·저장 기본값은 `real(8), parameter :: filtL = 49d0*3600d0 ! filter length (s)` (149); `real(8), parameter :: T = 60d0*60d0 ! sampling interval (s)` (150); `integer, save :: NS = 1 ! number of samples` (151); `logical, save :: first_call = .true.` (152). 한 시간 창 인덱스·반복 인덱스·저장 ISTA 선언(153–158). |
| 159–191 | 시작 시 24행 INTERNALTIDE 모듈·119행 MunkHPFilter 루틴 안. `if (first_call) then` (160)이면 first_call=false(161), `NS = floor(filtL/T)` (162), ista=1(163). UAV/VAV를 (NP,NS), UBar/VBar를 NP로 할당하고 0d0로 초기화한다(164–169). CalcMunkWeights 호출(170). 최초 조건 종료(171). `L = floor(dble(TimeStep)*DTDP/T)` (173); `Lm = floor(dble(TimeStep - 1)*DTDP/T)` (174)로 현재/직전 시간 단계의 한 시간 창을 구한다. `if (L > Lm) then` (175) 안 `if (ISTA > NS) then` (177)이면 `do ii = 1, NP` (178)에서 `UAV(ii, 1:NS - 1) = UAV(ii, 2:NS)` (179); `VAV(ii, 1:NS - 1) = VAV(ii, 2:NS)` (180)로 표본을 한 칸 당기고 마지막 칸에 현재 속도를 저장한다(181–182). UBar/VBar=0d0(184–185). `do ii = 1, NP` (186)·`do kk = 1, NS` (187) 안 `UBar(ii) = UBar(ii) + wts(kk)*UAV(ii, kk)` (188); `VBar(ii) = VBar(ii) + wts(kk)*VAV(ii, kk)` (189)로 가중합(weighted sum)을 누적한다. 두 루프 종료(190–191). |
| 192–207 | 시작 시 24행 INTERNALTIDE 모듈·119행 MunkHPFilter 루틴·175행 L>Lm 참 분기·177행 ISTA>NS 조건문 안. else(192)는 49시간 자료가 없을 때 지연 평균을 쓴다는 주석(193–194). `do ii = 1, NP` (195)에서 현재 속도를 ISTA 칸에 저장(196–197), `UBar(ii) = U_i(ii) - sum(UAV(ii, 1:ISTA))/dble(ISTA)` (198); `VBar(ii) = V_i(ii) - sum(VAV(ii, 1:ISTA))/dble(ISTA)` (199)로 현재 속도에서 채워진 표본 평균을 뺀다. `ISTA = ISTA + 1` (201). ISTA 조건·시간 창 조건·루틴 종료 및 구분 주석(202–207). |
| 208–249 | 시작 시 24행 INTERNALTIDE 모듈 안. CalcMunkWeights 입구·고역 통과 필터 가중치 준비 주석(208–213), implicit none(214). 한쪽(one-sided) 원본 가중치 LPwts(25), 정규화(normalization) 변수 K·반복 ii 선언(215–218); 고정 표본 수는 `integer, parameter :: NS = 49 ! length of HP filter needed` (216). wts(NS) 할당(221). 원본 저역 통과 계수는 `LPwts = [395287d0, 386839d0, 370094d0, 354118d0, 338603d0, 325633d0, 314959d0, &` (223); `300054d0, 278167d0, 251492d0, 234033d0, 219260d0, 208050d0, 195518d0, &` (224); `180727d0, 165525d0, 146225d0, 122665d0, 101603d0, 85349d0, 72261d0, &` (225); `60772d0, 47028d0, 30073d0, 13307d0]` (226). K=LPwts(1)(228)·`do ii = 2, 25` (229) 안 `K = K + 2d0*LPwts(ii)` (230)로 중심 외 가중치를 두 배 합산한다. `do ii = 1, 25` (233) 안 `LPwts(ii) = LPwts(ii)/K` (234)로 정규화한다. `do ii = 1, 24` (237) 안 `wts(ii) = -LPwts(26 - ii)` (239)와 `wts(ii + 25) = -LPwts(ii + 1)` (241)로 양쪽(two-sided) 고역 통과 계수를 채우며 중심은 `wts(25) = 1 - LPwts(1)` (244). CalcMunkWeights·INTERNALTIDE 종료와 끝 주석(245–249). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40–45·69–70·78–87·151–152·160–170: UNTIDE와 MunkHPFilter는 모듈의 UAV·VAV·UBar·VBar를 공유한다. 두 루틴의 first_call·NS·ISTA는 각각 별도의 저장 지역 변수이다. 두 최초 호출 분기는 같은 공유 배열을 각각 할당하며 ALLOCATED 검사는 없다.
- 54–57·103–111·193–199: UNTIDE의 UBar·VBar는 저장 표본의 평균이다. MunkHPFilter의 표본 부족 분기는 현재 속도에서 저장 표본 평균을 뺀 값을 UBar·VBar에 넣는다. 주석의 지연 평균 표현은 두 루틴에서 서로 다른 대입식을 가리킨다.
- 137–140·149–150·162·181–182·216·244: MunkHPFilter 주석은 25시간 지연을 적는다. 코드는 한 시간 간격의 49개 표본을 쓰고 마지막 표본을 49번째 칸에 둔다. 중심 가중치는 25번째 칸이다. 마지막 칸과 중심 칸의 인덱스 차이는 이 코드에서 24개 표본 간격이다.
- 163·177·192–201: MunkHPFilter의 ISTA는 1에서 시작한다. ISTA가 NS와 같을 때도 표본 부족 else를 실행하고 ISTA를 1 증가시킨다. 가중합 분기는 다음 표본 갱신에서 실행된다.
- 90–115·173–203: 두 루틴의 표본 저장과 UBar·VBar 갱신은 L>Lm 분기 안에만 있다. 두 루틴은 창 인덱스가 여러 칸 증가한 경우에도 현재 속도 표본 하나를 저장한다. L-Lm개 표본을 채우는 별도 반복문은 없다.
- 67–68·149–150·215–226: 필터 길이와 표본 간격은 각각 25시간/12분 및 49시간/한 시간으로 고정되어 있다. CalcMunkWeights의 표본 수 49와 원본 계수 25개는 소스에 직접 정의되어 있다.
- 33–34: mod_logging에서 가져온 DEBUG·ECHO·INFO·WARNING·ERROR·allMessage·logMessage·t_log_scope는 이 파일에서 USE 선언 뒤에 참조되지 않는다.

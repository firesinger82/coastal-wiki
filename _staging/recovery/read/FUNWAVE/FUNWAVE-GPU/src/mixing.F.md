---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/mixing.F
lines: 182
sha256: fa6f15232c208c47066c0106aa08c8429d7c5c03502d8750a75a2dac06a75c7d
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# mixing.F — 판독 구간 기록

구간은 1행부터 182행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | mixing.F·FUNWAVE-TVD 소속·2016년 저작권·Simplified BSD 재배포 조건·무보증 머리말(1–44), 구분 주석(45–46). MIXING_STUFF가 혼합(mixing) 관련 시간 평균(time average)과 평균 수위를 계산한다는 설명·2011년 이력(47–52). 이 파일에는 전처리 조건이나 CUDA·OpenACC·OpenMP 지시가 없다. |
| 53–82 | MIXING_STUFF는 GLOBAL을 사용한다(53–55). Smagorinsky 혼합과 파고 평균이라는 설명 및 Umean·Vmean 사용 여부에 대한 작성자 주석(57–59). `IF( time >= STEADY_TIME )THEN` (60)이면 CALCULATE_MEAN을 호출한다(61–66). 호출 인수는 평균 시간 간격·누적 시간·DT·격자 크기·현재와 이전 수위·속도·평균 및 누적 배열·파고·극값·상향 영점 통과(zero upcrossing) 횟수·내부 격자 범위·수위 편차 제곱 평균·유의파고(significant wave height)이다. 조건·루틴 종료와 빈 줄(67–71). CALCULATE_MEAN의 목적·2011년 이력·추가 평균 처리 이력 주석(72–82). |
| 83–109 | CALCULATE_MEAN의 연속 인수 목록(83–89), 설명 주석(90), PARAM 사용·IMPLICIT NONE (92–93). M·N·Ibeg·Iend·Jbeg·Jend는 입력 정수이고, U·V·ETA·ETA0는 `(M,N)` 입력 배열이다(94–95). T_INTV_mean·DT는 입력, Umean·Vmean·WaveHeightRMS·WaveHeightAve는 출력이며 ETAmean·누적 배열·Emax·Emin·Num_Zero_Up는 입출력이다(96–105). `REAL(SP),INTENT(OUT) :: T_sum` (102). Tmpe·Tmp_0 지역 실수(103), ETA2sum·ETA2mean·SigWaveHeight 입출력 배열 선언과 빈 줄(107–109). |
| 110–136 | 시작 시 83행 CALCULATE_MEAN 안이다. `T_sum=T_sum+DT` (110), `IF(T_sum.GE.T_INTV_mean)THEN` (111). 참 분기에서 `ETA2sum = (Eta-ETAmean)*(Eta-ETAmean)*DT + ETA2sum   !ykchoi` (113), `ETA2mean = ETA2sum/T_sum` (114)를 먼저 계산한다. `Usum=U*DT+Usum` (116), `Vsum=V*DT+Vsum` (117), `ETAsum=ETA*DT+ETAsum` (118), `Umean=Usum/T_sum` (119), `Vmean=Vsum/T_sum` (120), `ETAmean=ETAsum/T_sum` (121). 이전 ETAmean을 수위 편차 계산에 쓰려고 순서를 옮겼다는 설명과 주석 처리된 이전 대입 위치(123–127). `T_sum=T_sum-T_INTV_mean   ! T_sum=ZERO? (ykchoi)` (129) 뒤 `Usum=ZERO` (130), `Vsum=ZERO` (131), `ETAsum=ZERO` (132), `ETA2sum=ZERO     !ykchoi` (133)를 대입한다. `SigWaveHeight = 4.004*SQRT( ETA2mean )  !ykchoi` (135). 이전 위치의 주석식은 `!ETA2sum = (Eta-ETAmean)*(Eta-ETAmean)*DT + ETA2sum` (126)과 `!ETA2mean = ETA2sum/T_sum` (127)이다. 평균 시간 IF의 참 분기는 `ELSE` (152) 앞까지이다. 이 IF는 `ENDIF` (180)에서 닫힌다. [10-17 전수 검증 보완] |
| 137–151 | 시작 시 83행 CALCULATE_MEAN·`IF(T_sum.GE.T_INTV_mean)THEN` (111)의 참 분기 안이다. 이 분기는 `ELSE` (152) 앞까지이다. 이 IF는 `ENDIF` (180)에서 닫힌다. 전체 배열의 `DO J=1,N`·`DO I=1,M` (138–139)에서 `IF(Num_Zero_Up(I,J)>=2)THEN` (140)이면 `WaveHeightAve(I,J)=HavgSum(I,J)/Num_Zero_Up(I,J)` (141), `WaveHeightRMS(I,J)=SQRT(HrmsSum(I,J)/Num_Zero_Up(I,J))` (142)로 평균파고와 제곱평균제곱근(root mean square, RMS) 파고를 계산한다. `!        Num_Zero_Up(I,J)=0` (144), `!        HavgSum(I,J)=ZERO` (145), `!        HrmsSum(I,J)=ZERO` (146)는 주석이다. 조건·두 루프 종료(143·147–148) 뒤 CALL PREVIEW_MEAN (150). [10-17 전수 검증 보완] |
| 152–182 | 시작 시 83행 CALCULATE_MEAN·`IF(T_sum.GE.T_INTV_mean)THEN` (111) 안이며 `ELSE` (152)에서 평균 시간 미도달 분기를 시작한다. `Usum=U*DT+Usum` (154), `Vsum=V*DT+Vsum` (155), `ETAsum=ETA*DT+ETAsum` (156), `ETA2sum = (Eta-ETAmean)*(Eta-ETAmean)*DT + ETA2sum` (158). `DO J=1,N` (161)·`DO I=1,M` (162)에서 `if(Eta(i,j)>Emax(i,j)) Emax(i,j) = Eta(i,j)` (163), `if(Eta(i,j)<Emin(i,j)) Emin(i,j) = Eta(i,j)` (164)로 극값을 갱신한다. `Tmpe = Eta(i,j)-ETAmean(i,j)` (165), `Tmp_0 = Eta0(i,j)-ETAmean(i,j)` (166). `if(Tmpe>Tmp_0.and.Tmpe*Tmp_0<=Zero) then` (167)이면 `Num_Zero_Up(i,j) = Num_Zero_Up(i,j)+1` (168). 그 안 `if(Num_Zero_Up(i,j)>=2) then` (169)이면 `HavgSum(i,j) = HavgSum(i,j)+Emax(i,j)-Emin(i,j)` (170), `HrmsSum(i,j) = HrmsSum(i,j)+(Emax(i,j)-Emin(i,j))**2` (171). 해당 내부 조건 종료 후 같은 영점 통과 조건 안에서 `Emax(i,j) = -1000.` (174), `Emin(i,j) = 1000.` (175)로 다음 파의 극값을 초기화한다. 조건·루프·평균 시간 분기·루틴 종료와 빈 줄(172–182). 횟수 IF는 `endif` (172)에서 닫힌다. 영점 통과 IF는 `endif` (176)에서 닫힌다. 평균 시간 IF는 `ENDIF` (180)에서 닫힌다. [10-17 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 102·110: T_sum은 INTENT(OUT)으로 선언된다. 첫 실행 대입은 우변에서 T_sum을 읽는 T_sum=T_sum+DT이다.
- 97–98·111–158: Umean·Vmean·WaveHeightRMS·WaveHeightAve는 INTENT(OUT)이다. 평균 시간 미도달 분기에는 이 네 배열에 대한 대입이 없다. 평균 시간 도달 분기의 파고 대입도 Num_Zero_Up>=2 조건 안에만 있다.
- 129–133: 평균 시간 도달 시 T_sum에서는 T_INTV_mean만 뺀다. 같은 블록은 누적 배열을 모두 ZERO로 설정한다.
- 140–146·168–171: 파고 분모에는 Num_Zero_Up 전체 횟수를 쓴다. 파고 합산은 횟수 2부터 수행하며, 평균 계산 뒤 횟수·파고 합을 초기화하는 문장은 주석 처리되어 있다.
- 137–175: 극값 갱신과 상향 영점 통과 검사는 평균 시간 미도달 ELSE에만 있다. 평균 시간 도달 참 분기는 저장된 파고 합으로 파고를 계산한다.
- 135·174–175: 유의파고 계수 4.004와 다음 파의 극값 초기값 -1000.·1000.은 이 루틴에 직접 적혀 있다.

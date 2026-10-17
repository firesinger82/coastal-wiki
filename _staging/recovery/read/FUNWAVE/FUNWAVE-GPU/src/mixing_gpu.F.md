---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/mixing_gpu.F
lines: 153
sha256: 3106d40892b5e889fb331c5d5a49e65d834d9c0d8f1b306e31991773e20db9bb
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# mixing_gpu.F — 판독 구간 기록

구간은 1행부터 153행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 혼합(mixing) 관련 시간 평균(time average)과 평균 수위를 계산한다는 설명·2011년 이력·구분 주석(1–8). calculate_mean_module은 cudafor·PARAM의 ZERO와 SP·GLOBAL의 크기·평균 시간·출력 설정과 호스트(host) 배열·mod_cuda의 장치(device) 누적 배열과 실행 배치를 사용한다(9–19). contains·CALCULATE_MEAN 설명·이력·빈 줄(20–32). 이 파일에는 전처리 조건이 없다. |
| 33–60 | 시작 시 9행 모듈 안이다. `attributes(global) subroutine calc_mean_kernel(Mloc,Nloc,T_sum,DT)` (33)의 크기·시간 인수는 VALUE이다(35–36). i·j·DTg 선언(37–38). `i = threadIdx%x + (blockIdx%x-1)*BlockDimX_2D` (40), `j = threadIdx%y + (blockIdx%y-1)*BlockDimY_2D` (41), `DTg = DT` (42). `if (i>=1 .AND. i<=Mloc .AND. j>=1 .AND. j<=Nloc) then` (43) 안에서 `ETA2sum_d(i,j) = (Eta_d(i,j)-ETAmean_d(i,j))*(Eta_d(i,j)-ETAmean_d(i,j))*DTg + ETA2sum_d(i,j)` (44), `ETA2mean_d(i,j) = ETA2sum_d(i,j)/T_sum` (45), `Usum_d(i,j)=U_d(i,j)*DTg+Usum_d(i,j)` (46), `Vsum_d(i,j)=V_d(i,j)*DTg+Vsum_d(i,j)` (47), `ETAsum_d(i,j)=ETA_d(i,j)*DTg+ETAsum_d(i,j)` (48), `Umean_d(i,j)=Usum_d(i,j)/T_sum` (49), `Vmean_d(i,j)=Vsum_d(i,j)/T_sum` (50), `ETAmean_d(i,j)=ETAsum_d(i,j)/T_sum` (51), `SigWaveHeight_d(i,j) = 4.004*SQRT( ETA2mean_d(i,j) )` (52). 그 안 `IF(Num_Zero_Up_d(I,J)>=2)THEN` (53)이면 `WaveHeightAve_d(I,J)=HavgSum_d(I,J)/Num_Zero_Up_d(I,J)` (54), `WaveHeightRMS_d(I,J)=SQRT(HrmsSum_d(I,J)/Num_Zero_Up_d(I,J))` (55)로 평균파고와 제곱평균제곱근(root mean square, RMS) 파고를 계산한다. 조건·커널 종료·빈 줄(56–60). [10-17 전수 검증 보완] |
| 61–95 | 시작 시 9행 모듈 안이다. `attributes(global) subroutine calc_sum_kernel(Mloc,Nloc,DT)` (61), 인수·작업 변수 선언(62–67). `i = threadIdx%x + (blockIdx%x-1)*BlockDimX_2D` (69), `j = threadIdx%y + (blockIdx%y-1)*BlockDimY_2D` (70), `DTg = DT` (71). `if (i>=1 .AND. i<=Mloc .AND. j>=1 .AND. j<=Nloc) then` (72) 안에서 `Usum_d(i,j)=U_d(i,j)*DTg+Usum_d(i,j)` (73), `Vsum_d(i,j)=V_d(i,j)*DTg+Vsum_d(i,j)` (74), `ETAsum_d(i,j)=ETA_d(i,j)*DTg+ETAsum_d(i,j)` (75), `ETA2sum_d(i,j) = (Eta_d(i,j)-ETAmean_d(i,j))*(Eta_d(i,j) &` (76); `-ETAmean_d(i,j))*DTg + ETA2sum_d(i,j)` (77). `if(Eta_d(i,j)>Emax_d(i,j)) Emax_d(i,j) = Eta_d(i,j)` (79), `if(Eta_d(i,j)<Emin_d(i,j)) Emin_d(i,j) = Eta_d(i,j)` (80). `Tmpe = Eta_d(i,j)-ETAmean_d(i,j)` (81), `Tmp_0 = Eta0_d(i,j)-ETAmean_d(i,j)` (82). `if(Tmpe>Tmp_0.and.Tmpe*Tmp_0<=Zero) then` (83)이면 상향 영점 통과(zero upcrossing) 횟수 `Num_Zero_Up_d(i,j) = Num_Zero_Up_d(i,j)+1` (84). 그 안 `if(Num_Zero_Up_d(i,j)>=2) then` (85)이면 `HavgSum_d(i,j) = HavgSum_d(i,j)+Emax_d(i,j)-Emin_d(i,j)` (86), `HrmsSum_d(i,j) = HrmsSum_d(i,j)+(Emax_d(i,j)-Emin_d(i,j))**2` (87). 같은 영점 통과 조건 안에서 `Emax_d(i,j) = -1000.` (90), `Emin_d(i,j) = 1000.` (91)로 다음 파의 극값을 초기화한다. 조건·커널 종료·빈 줄(88–95). 횟수 IF는 `endif` (88)에서 닫힌다. 영점 통과 IF는 `endif` (92)에서 닫힌다. 범위 IF는 `endif` (93)에서 닫힌다. [10-17 전수 검증 보완] |
| 96–114 | 시작 시 9행 모듈 안이다. var_d2h_mean (96–112)은 실행 시 논리 조건에 따라 장치 배열을 호스트 배열에 복사한다. `IF(OUT_Umean)THEN` (98)이면 `Umean = Umean_d` (99), `IF(OUT_Vmean)THEN` (101)이면 `Vmean = Vmean_d` (102), `IF(OUT_ETAmean)THEN` (104)이면 `ETAmean = ETAmean_d` (105)을 복사한다. `IF(OUT_WaveHeight)THEN` (107)이면 `WaveHeightRMS=WaveHeightRMS_d` (108), `WaveHeightAve=WaveHeightAve_d` (109), `SigWaveHeight=SigWaveHeight_d` (110)를 대입한다. SigWaveHeight는 유의파고(significant wave height) 배열이다. 각 조건과 루틴 종료·빈 줄(100–114). 이 출력 설정들은 전처리 조건이 아니다. [10-17 전수 검증 보완] |
| 115–142 | 시작 시 9행 모듈 안이다. CALCULATE_MEAN_GPU 입구와 주석·IMPLICIT NONE (115–118). `tBlock = dim3 (BlockDimX_2D, BlockDimY_2D ,1)` (119), `grid = dim3 ( ceiling ( real ( Mloc ) / BlockDimX_2D ) , &` (120); `ceiling ( real ( Nloc ) / BlockDimY_2D ) , 1)` (121). `T_sum=T_sum+DT` (123). `IF(T_sum.GE.T_INTV_mean)THEN` (125)이면 `call calc_mean_kernel<<<grid, tBlock>>>(Mloc,Nloc,T_sum,DT)` (126). 그 뒤 `T_sum=T_sum-T_INTV_mean` (128), `Usum_d=ZERO` (129), `Vsum_d=ZERO` (130), `ETAsum_d=ZERO` (131), `ETA2sum_d=ZERO` (132)를 대입한다. 장치에서 호스트로 복사한 뒤 미리보기를 호출한다는 주석(134), call var_d2h_mean (135), CALL PREVIEW_MEAN (136). `ELSE` (137)는 `call calc_sum_kernel<<<grid,tBlock>>>(Mloc,Nloc,DT)` (138)를 호출한다. 실행 조건·루틴 종료·빈 줄(139–142). [10-17 전수 검증 보완] |
| 143–153 | 시작 시 9행 모듈 안이다. MIXING_STUFF_GPU 입구·IMPLICIT NONE·목적 주석(143–145). `IF( time >= STEADY_TIME )THEN` (146)이면 CALL CALCULATE_MEAN_GPU (147). 조건·루틴 종료(148–150), 빈 줄(151–152), 모듈 종료(153). 이 파일의 커널 정의와 호출에는 전처리 플래그에 따른 선택이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·40–43·69–72: 가져온 Ibeg·Iend·Jbeg·Jend는 이 파일의 실행문에서 사용되지 않는다. 두 커널의 처리 범위는 1..Mloc·1..Nloc이다.
- 53–55·84–87: 파고 분모는 Num_Zero_Up_d 전체 횟수이다. 파고 합산은 횟수 2부터 수행하며, 이 파일에는 횟수·HavgSum_d·HrmsSum_d를 초기화하는 대입이 없다.
- 125–132: 평균 시간 도달 시 T_sum에서 T_INTV_mean만 뺀다. 같은 분기는 속도·수위·편차 제곱 누적 배열을 ZERO로 설정한다.
- 33–94·125–138: 평균 시간 도달 분기는 calc_mean_kernel을 호출한다. 극값 갱신과 상향 영점 통과 검사는 미도달 분기에서 호출하는 calc_sum_kernel에만 있다.
- 98–110·135–136: 호스트 평균·파고 배열 복사는 각각 OUT 설정 조건 안에 있다. PREVIEW_MEAN 호출에는 이 출력 설정 조건이 붙지 않는다.

# CPU 해법과 GPU 해법 대조 2 — ACC·비균일 격자·MWDG2

분류별 개수: C 28, E 25, F 5, H 26, X 0. 차이 84행. 같음 14행.

## 1 요약

이 보고서는 CPU ACC, CPU SGC, 균일 격자 GPU ACC, 비균일 격자 GPU ACC, GPU HWFV1·MWDG2를 원문 코드로 대조한다.
이 보고서는 모델을 실행하지 않았다.
이 보고서는 수치 정확도와 성능을 검증하지 않았다.
코드 결함 후보는 정적 판독의 결과이다.
이 보고서는 현재 노트를 수정하지 않는다.
§4는 현재 노트에 적용할 수정안을 제시한다.

원문 기준 경로는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`이다.
이하 코드 인용은 이 경로를 생략한다.
`U`는 `cuda/acc/`를 뜻한다.
`N`은 `cuda/acc_nugrid/`를 뜻한다.
`M`은 `cuda/adaptive/`를 뜻한다.
`U/파일:줄`, `N/파일:줄`, `M/파일:줄`은 이 세 디렉터리를 확장한 코드 인용이다.
현재 노트 인용은 저장소 루트를 기준으로 한다.

CPU ACC와 균일 격자 GPU ACC는 같은 q-centred 유량식을 사용한다.
CPU ACC는 `MaskTest`와 routing 조건을 적용한다.
균일 격자 GPU ACC는 이 두 조건을 주석 처리했다.
비균일 격자 GPU ACC는 지형 detail과 사전 지정 위치로 격자를 구성한다.
비균일 격자 GPU ACC는 조도·초기 수심의 계수도 인코딩한다.
비균일 격자 GPU ACC는 조도·초기 수심의 detail을 격자 선택 조건에 넣지 않는다.
비균일 격자 GPU ACC의 시간 루프는 격자를 다시 구성하지 않는다.
MWDG2는 epsilon이 양수이면 매 시간 단계에서 유동 detail을 다시 계산한다.
MWDG2는 ACC와 다른 지배식·HLL 플럭스·Legendre 계수를 사용한다.
근거는 §2의 원문 인용에 둔다.

판정 `같음`은 인용한 계산과 명시한 조건에 한정한다.
판정 `다름`은 차이를 뜻한다.
판정 `X에만`과 `Y에만`은 해당 대조 쌍의 한쪽에만 있는 처리를 뜻한다.
§5는 `같음` 이외의 모든 행에 C·E·F·H·X 중 하나를 부여한다.
같은 식의 변형은 F로 분류한다.
해법별로 명시한 수학 모형·테스트·장치 처리의 차이는 H로 분류한다.
설명되지 않은 계산·옵션 생략은 C로 분류한다.
코드 결함 후보는 반대 근거를 먼저 확인한 뒤 E로 분류한다.

## 2 대조 표

### 2.1 CPU ACC와 균일 격자 GPU ACC

| 행 ID | 계산 항목 | 해법 X — CPU 원문 | 해법 Y — 균일 격자 GPU 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-001 | 수면 경사와 통수심 | `fp_acc.cpp:65` `Sf=-dh/Parptr->dx;`<br>`fp_acc.cpp:66` `hflow=getmax(z0+h0,z1+h1)-getmax(z0,z1);` | `U/cuda_acc_solver.cu:701` `Sf = -dh / cuda::geometry.dx;`<br>`U/cuda_acc_solver.cu:702` `hflow = getmax(z0 + h0, z1 + h1) - getmax(z0, z1);` | 같음 | 두 경로는 수면차에 음의 부호를 붙인다. 두 경로는 높은 수면에서 높은 바닥을 뺀다. y 방향도 `fp_acc.cpp:160-163`, `U/cuda_acc_solver.cu:801-804`에서 같은 계산을 한다. |
| LG2-002 | q-centred 운동량 갱신 | `fp_acc.cpp:88` `Q=((Solverptr->theta*q0+C(0.5)*(1-Solverptr->theta)*(qup+qdown))-(g*dt*hflow*Sf))/(1+g*dt*hflow*fn*fn*fabs(qvect)/(pow(hflow,(C(10.0)/C(3.0)))))*Parptr->dx;` | `U/cuda_acc_solver.cu:723` `Q = ((cuda::solver_params.theta * q0 + C(0.5) * (C(1.0) - cuda::solver_params.theta) * (qup + qdown)) - (g * dt * hflow * Sf)) / (C(1.0) + g * dt * hflow * fn * fn * FABS(qvect) / (POW(hflow, (C(10.0) / C(3.0))))) * cuda::geometry.dx;` | 같음 | 변수 대응 후 식이 같다. y 방향 식은 `fp_acc.cpp:182`, `U/cuda_acc_solver.cu:823`이다. ACC는 이 식으로 면 유량을 구한다. ACC는 HLL 리만 문제를 풀지 않는다. |
| LG2-003 | 역방향 보정 | `fp_acc.cpp:92` `if (Q*dh < C(0.0)){ // version of line above that will compile on windows machine`<br>`fp_acc.cpp:94` `Q=(q0-(g*dt*hflow*Sf))/(1+g*dt*hflow*fn*fn*fabs(qvect)/(pow(hflow,(C(10.0)/C(3.0)))))*Parptr->dx;` | `U/cuda_acc_solver.cu:727` `if (Q * dh < C(0.0)) { // version of line above that will compile on windows machine`<br>`U/cuda_acc_solver.cu:729` `Q = (q0 - (g * dt * hflow * Sf)) / (C(1.0) + g * dt * hflow * fn * fn * FABS(qvect) / (POW(hflow, (C(10.0) / C(3.0))))) * cuda::geometry.dx;` | 같음 | 두 경로는 같은 부호 조건에서 이웃 유량 혼합을 제거한다. y 방향은 `fp_acc.cpp:186-188`, `U/cuda_acc_solver.cu:827-829`이다. |
| LG2-004 | 마찰 벡터 선택 | `fp_acc.cpp:45` `if(Solverptr->fricSolver2D==ON){`<br>`fp_acc.cpp:50-51` `qy_avg=(Arrptr->Qyold[pqy1]+Arrptr->Qyold[pqy2]+Arrptr->Qyold[pqy3]+Arrptr->Qyold[pqy4])/4;`<br>`qvect=sqrt(q0*q0+qy_avg*qy_avg);` | `U/cuda_acc_solver.cu:954` `friction = (physical_params.manning > C(0.0)) \|\| (manning != nullptr);`<br>`U/cuda_acc_solver.cu:686-687` `qy_avg = (U.Qyold[pqy1] + U.Qyold[pqy2] + U.Qyold[pqy3] + U.Qyold[pqy4]) / C(4.0);`<br>`qvect = SQRT(q0 * q0 + qy_avg * qy_avg);` | 다름 | GPU의 `friction`은 마찰 존재 여부이다. CPU의 `fricSolver2D`는 마찰 벡터 선택 옵션이다. GPU는 조도가 있으면 벡터 마찰을 사용한다. CPU는 조도가 있어도 `fricSolver2D==OFF`이면 `fp_acc.cpp:54` `qvect=q0;`를 사용한다. |
| LG2-005 | 공간 조도와 통수심 제한 | `fp_acc.cpp:58` `if(Arrptr->Manningsn!=NULL) fn=C(0.5)*(Arrptr->Manningsn[p0]+Arrptr->Manningsn[p1]);`<br>`fp_acc.cpp:67-68` `hflow=getmax(hflow,0);`<br>`hflow=getmin(hflow,Solverptr->MaxHflow);` | `U/cuda_acc_solver.cu:694` `if (manning != NULL) fn = C(0.5) * (manning[p0] + manning[p1]);`<br>`U/cuda_acc_solver.cu:703-704` `hflow = getmax(hflow, C(0.0));`<br>`hflow = getmin(hflow, cuda::solver_params.MaxHflow);` | 같음 | 두 경로는 인접 조도의 산술평균을 사용한다. 두 경로는 통수심의 하한과 상한을 적용한다. |
| LG2-006 | 채널 마스크와 routing 조건 | `fp_acc.cpp:83` `if(MaskTest(Arrptr->ChanMask[p0],Arrptr->ChanMask[p1]) && hflow>Solverptr->DepthThresh)`<br>`fp_acc.cpp:85` `if (Statesptr->routing==OFF \|\| fabs(Sf)<Parptr->RouteSfThresh) // CCS If routing scheme is enabled, only calc Q where Sf is below threshold value` | `U/cuda_acc_solver.cu:718` `if ( /*MaskTest(U.ChanMask[p0], U.ChanMask[p1]) && */ hflow > cuda::solver_params.DepthThresh)`<br>`U/cuda_acc_solver.cu:720` `//		if (cuda::solver_params.routing == OFF \|\| FABS(Sf) < cuda::solver_params.RouteSfThresh) // CCS If routing scheme is enabled, only calc Q where Sf is below threshold value` | X에만 | GPU는 두 분기를 주석 처리했다. GPU driver도 routing 함수를 호출하지 않는다. GPU의 `MaskTest` 정의가 남아 있다는 사실은 호출을 복구하지 않는다. |
| LG2-007 | 습윤–건조와 경계 인접 이웃 유량 | `fp_acc.cpp:74` `if (i == 0 && qup == 0)`<br>`fp_acc.cpp:78` `if (i == Parptr->xsz - 2 && qdown == 0)`<br>`fp_acc.cpp:83` `if(MaskTest(Arrptr->ChanMask[p0],Arrptr->ChanMask[p1]) && hflow>Solverptr->DepthThresh)` | `U/cuda_acc_solver.cu:709` `if (i == 0 && qup == 0)`<br>`U/cuda_acc_solver.cu:713` `if (i == cuda::geometry.xsz - 2 && qdown == 0)`<br>`U/cuda_acc_solver.cu:879` `if (h0 > cuda::solver_params.DepthThresh \|\| h1 > cuda::solver_params.DepthThresh)` | 같음 | 마스크 차이는 LG2-006에 분리했다. 두 경로는 경계 바깥 유량이 0일 때 중심 유량으로 대체한다. GPU의 통수심 조건은 LG2-006에 인용했다. |
| LG2-008 | CFL 식과 셀별 후보의 이력 | `fp_acc.cpp:271-272` `locT=cfl*Parptr->dx/(sqrt(g*MH));`<br>`Solverptr->Tstep=getmin(Solverptr->Tstep,locT);` | `U/cuda_acc_solver.cu:118-119` `NUMERIC_TYPE dt_ = cuda::solver_params.cfl * cuda::geometry.dx`<br>`/ SQRT(cuda::physical_params.g * H);`<br>`U/cuda_acc_solver.cu:125` `dt[j * cuda::pitch + i] = getmin(dt_, dt[j * cuda::pitch + i]);` | 다름 | 같은 수심에서 CFL 식은 같다. CPU는 매 단계 `InitTstep`에서 다시 최소값을 구한다. GPU의 셀별 배열은 이전 후보와 최소값을 취한다. 실제 배열 초기화·상한은 §2.7에서 호출 쪽과 확인한다. |
| LG2-009 | 이전 단위폭 유량 | `fp_acc.cpp:307` `Arrptr->Qxold[pqptr]=Arrptr->Qx[pqptr]*dxinv;`<br>`fp_acc.cpp:319` `Arrptr->Qyold[pqptr]=Arrptr->Qy[pqptr]*dxinv;` | `U/cuda_acc_solver.cu:606` `Uold.Qxold[pqptr]=Uold.Qx[pqptr]*(C(1.0)/cuda::geometry.dx);`<br>`U/cuda_acc_solver.cu:634` `Uold.Qyold[pqptr]=Uold.Qy[pqptr]*(C(1.0)/cuda::geometry.dx);` | 같음 | 두 경로는 체적 유량을 셀 폭으로 나눈다. |
| LG2-010 | 면 유속과 최대 유속 | `fp_acc.cpp:105-106` `Arrptr->Vx[pq0]=Q/Parptr->dx/hflow;`<br>`Arrptr->maxVx[pq0]=getmax(Arrptr->maxVx[pq0],fabs(Arrptr->Vx[pq0]));` | `U/cuda_acc_solver.cu:740` `U.Vx[pq0] = Q / cuda::geometry.dx / hflow;`<br>`U/cuda_acc_flow.cuh:28-29` `NUMERIC_TYPE* __restrict__ Vx;`<br>`NUMERIC_TYPE* __restrict__ Vy;` | X에만 | 순간 면 유속 식은 같다. GPU는 CPU의 `maxVx`, `maxVy` 누적을 구현하지 않는다. y 방향 CPU 누적은 `fp_acc.cpp:199-200`이다. |
| LG2-011 | 침수 이력 | `iterateq.cpp:199` `Arrptr->initHtm[ptr] = Solverptr->t / C(3600.0);`<br>`iterateq.cpp:201` `Arrptr->totalHtm[ptr] += Solverptr->Tstep / C(3600.0);` | `U/cuda_acc_solver.cu:569` `Uold.initHtm[pqptr] = time / C(3600.0);`<br>`U/cuda_acc_solver.cu:571` `Uold.totalHtm[pqptr] += cuda::dt / C(3600.0);` | 같음 | 두 경로는 습윤 임계값을 넘을 때 시간을 시간 단위로 기록한다. 두 경로는 현재 수심이 기존 최대 수심보다 클 때 최대 시각을 바꾼다. `mint_hk` 조건은 CPU `iterateq.cpp:190`, GPU `U/cuda_acc_simulate.cu:250`이다. |
| LG2-012 | 침수 시작 시각 재설정 | `iterateq.cpp:177` `if ((Statesptr->reset_timeinit == ON) & (Solverptr->t>Parptr->reset_timeinit_time))`<br>`iterateq.cpp:185` `Arrptr->initHtm[ptr] = (NULLVAL);` | `U/cuda_acc_simulate.cu:233` `//if ((Statesptr->reset_timeinit == ON) & (Solverptr->t > Parptr->reset_timeinit_time))` | X에만 | GPU의 재설정 블록은 주석이다. |

CPU ACC의 `CalcMaxH`, `CalcT`, `MaskTestAcc`, `UpdateQs`는 각각 `fp_acc.cpp:208`, `:237`, `:283`, `:292`에서 시작한다.
`MaskTestAcc`는 `fp_acc.cpp:285`의 `if(m1==-1) return(1);`로 채널 셀을 최대 수심 집계에서 제외한다.
GPU ACC의 `FloodplainQx`, `FloodplainQy`는 각각 `U/cuda_acc_solver.cu:852`, `:890`에서 시작한다.
GPU ACC의 `zero_thin_depth_slopes`는 `U/cuda_acc_solver.cu:1066-1070`의 빈 함수이다.
해석: 이 빈 함수는 ACC가 DG2 경사 계수를 갖는다는 근거가 아니다.

### 2.2 CPU SGC의 하위 격자 계산

이 절은 `sgc.cpp`의 계산과 GPU ACC의 계산을 구분한다.
CPU SGC의 기본 실행 진입점은 `lisflood.cpp:775`의 `Fast_MainStart(Fnameptr, &Fps, Statesptr, Parptr, Solverptr, BCptr, Stageptr, CSTypePtr, Arrptr, SGCptr, ChannelSegmentsVecPtr, Damptr, verbosemode); //Damptr added by FEOL`이다.
`iterateq.cpp:120`은 `printf("SGC not processed here\n");`를 실행한다.
`sgc.cpp`의 옛 시간 갱신 함수들은 `lisflood2/sgm_fast.cpp:3458`의 `#ifdef RESULT_CHECK` 안에 있는 `Do_Update_old`가 호출한다.
`SGC_hotstart`와 형상 함수는 이 조건과 별도로 초기화에서 사용한다.
이 보고서는 `lisflood2/`의 최적화된 SGC 전체를 추가 분석 대상으로 삼지 않는다.

| 행 ID | 계산 항목 | 해법 X — CPU SGC 원문 | 해법 Y — ACC 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-013 | 하상·bankfull·사행 길이 | `sgc.cpp:435` `Arrptr->SGCc[p0] = m*getmax(chan_length, getmin(dx, dy)); // make sure channel is at least as long as the shortest cell width then apply meander coefficient m`<br>`sgc.cpp:449` `Arrptr->SGCbfH[p0] = Arrptr->DEM[p0] - Arrptr->SGCz[p0]; // Calculate SGC bank full depth` | `N/update_h.cu:86` `NUMERIC_TYPE cv = H * (dx * dx);` | X에만 | SGC는 셀 내부 채널을 별도 형상으로 표현한다. 비균일 격자 ACC는 계산 셀 크기를 바꾼다. 두 격자 개념은 다르다. `CalcSGCz`는 bedfile·고정 수심·고정 면적·집수면적·폭 기반 수리기하를 `sgc.cpp:442-446`에서 선택한다. |
| LG2-014 | 수심과 체적의 역변환 | `sgc.cpp:204` `v = c*pow(h, C(1.0) / sl + C(1.0));`<br>`sgc.cpp:216` `v = c*pow(h, C(3.0) / C(2.0));` | `sgc.cpp:1671` `h = pow(V / c, sl / (sl + C(1.0)));`<br>`sgc.cpp:1683` `h = pow(V / c, C(2.0) / C(3.0));` | 다름 | 해석: 같은 SGC 내부의 정방향·역방향 표기이다. 지수는 서로 역수이다. 형상 1·3·4·6은 `v=h*c`와 `h=V/c`를 사용한다. 형상 7의 전처리는 `sgc.cpp:495-507`의 주석 블록이다. |
| LG2-015 | 단면적·동수반경·회귀 계수 | `sgc.cpp:134` `(*A) = (*we)*hflow;`<br>`sgc.cpp:241` `R = A / (w + 2 * R); // calculate hydraulic radius`<br>`sgc.cpp:119` `SGCptr->SGCbeta5[i] = SGCptr->SGCbeta1[i] * SGCptr->SGCbetahmin + SGCptr->SGCbeta2[i] * SGCptr->SGCbetahmin*SGCptr->SGCbetahmin;` | `fp_acc.cpp:66` `hflow=getmax(z0+h0,z1+h1)-getmax(z0,z1);` | X에만 | `SGC_wp_prams`, `CalcSGC_A`, `CalcSGC_R`는 채널 형상을 계산한다. GPU ACC에는 이 단면 계산이 없다. SGC 형상 1~7의 면적·동수반경은 `sgc.cpp:131-187`, `:237-297`에 있다. `SGCbeta5`는 회귀식 두 구간의 접속값이다. 외부 회귀계수의 적합도는 이번 코드 대조 대상이 아니다. |
| LG2-016 | SGC 범람원 마찰 분모 | `sgc.cpp:880` `Arrptr->Qxold[pq0] = (q0 - (g*dt*hflow*Sf)) / (1 + g*dt*fn*fn*fabs(q0) / pow(hflow, (C(7.0) / C(3.0))));//*Parptr->dx;` | `fp_acc.cpp:94` `Q=(q0-(g*dt*hflow*Sf))/(1+g*dt*hflow*fn*fn*fabs(qvect)/(pow(hflow,(C(10.0)/C(3.0)))))*Parptr->dx;` | 다름 | 해석: `theta=1`이고 `qvect=q0`일 때 단위폭 유량의 마찰 분모는 같다. `hflow/hflow^(10/3)=1/hflow^(7/3)`이다. 채널 폭 차감은 LG2-019에 분리했다. |
| LG2-017 | 채널 운동량과 합성 유량 | `sgc.cpp:844` `Arrptr->QxSGold[pq0] = (qc - g*A0*dt*Sf) / (1 + dt*g*cn*fabs(qc) / (pow(R, C(4.0) / C(3.0))*A0));`<br>`sgc.cpp:896` `Q = Qc + Q;` | `U/cuda_acc_solver.cu:723`의 범람원 ACC 식(LG2-002). | X에만 | SGC는 작은 단면적 쪽의 `A`, `R`을 선택한다. SGC는 채널 체적 유량과 남은 범람원 폭의 유량을 합한다. SGC는 `sgc.cpp:388`의 `for (i = 0; i<SGCptr->NSGCprams; i++) SGCptr->SGCn[i] = SGCptr->SGCn[i] * SGCptr->SGCn[i];`로 채널 조도를 제곱해 보관한다. |
| LG2-018 | 옛 SGC y 방향 이전 유량 | `sgc.cpp:826` `qc = Arrptr->QxSGold[pq0]; // Get old q in m3/s`<br>`sgc.cpp:844`의 갱신 식(LG2-017). | `sgc.cpp:942` `Qc = Arrptr->QySGold[pq0]; // Get old q in m3/s`<br>`sgc.cpp:961` `Arrptr->QySGold[pq0] = (qc - g*A0*dt*Sf) / (1 + dt*g*cn*fabs(qc) / (pow(R, C(4.0) / C(3.0))*A0));` | 다름 | `CalcFPQySGC`는 `Qc`에 값을 넣은 뒤 별도 지역변수 `qc`를 읽는다. `sgc.cpp:969`의 다른 단면 분기도 같은 `qc`를 읽는다. `RESULT_CHECK` 참조 경로의 결함 후보이다. 기본 SGC 실행 전체의 결함으로 일반화하지 않는다. |
| LG2-019 | 옛 SGC 직사각형 셀 폭 | `sgc.cpp:862` `if (we < Arrptr->dy[p0]) // CCS dy[p0] for cell width relative to flow in x`<br>`sgc.cpp:882` `Q = Arrptr->Qxold[pq0] * (Arrptr->dx[p0] - we);` | `sgc.cpp:979` `if (we < Arrptr->dx[p0]) // CCS use dx[p0] for cell width relative to flow in y`<br>`sgc.cpp:998` `Q = Arrptr->Qyold[pq0] * (Arrptr->dy[p0] - we);` | 다름 | 통과 조건의 횡단 폭과 유량 환산 폭이 다르다. `sgc.cpp:1403`의 `Qfp = (*qoldptr) * (cell_width - w0);`는 경계에서 횡단 폭을 사용한다. 정사각형 셀은 차이를 숨긴다. `RESULT_CHECK` 참조 경로에서 직사각형 셀을 사용하는 경우의 결함 후보이다. |
| LG2-020 | SGC hotstart 역방향 단위 | `sgc.cpp:601` `Arrptr->QxSGold[pq0] = (pow(hflow, (C(5.0) / C(3.0)))*Sf / fn)*getmin(w0, w1);` | `sgc.cpp:612` `Arrptr->QxSGold[pq0] = (-pow(hflow, (C(5.0) / C(3.0)))*Sf / fn);` | 다름 | 역방향 식은 채널 폭을 곱하지 않는다. y 방향도 `sgc.cpp:679`, `:690`에서 같은 비대칭을 갖는다. `sgc.cpp:826`은 이 배열을 `m3/s`로 읽는다. `lisflood.cpp:552`의 `if (SimStates.startq == ON && SimStates.SGC == ON)` 초기화에서 도달한다. |
| LG2-021 | SGC 체적 갱신·원천·경계 | `sgc.cpp:1097` `Arrptr->SGCVol[p0] += dV; // Add dV to Vol. This is now the total volume.`<br>`sgc.cpp:1110` `Arrptr->H[p0] = Arrptr->SGCbfH[p0] + (Arrptr->SGCVol[p0] - Arrptr->SGCbfV[p0]) / Arrptr->dA[p0]; // there is a sub-grid channel but its over bank // Note need to include check for SGCwidth < cell width to make sure out of bank volume is not accounted for in cells with channels wider than a cell` | `iterateq.cpp:540` `(*hptr) += dV / Parptr->dA;`<br>`N/update_h.cu:197` `H += dV / (dx * dx);` | X에만 | SGC는 `SGCdVol`을 체적에 더한다. SGC는 bankfull 전후에 다른 수심 변환을 사용한다. `SGC_BCs`와 `CalcSGC_pointFREE`는 채널·범람원 유량을 합한다. SGC는 `sgc.cpp:1040`, `:1220`에서 위경도 격자의 Q 입력 배율을 구분한다. |
| LG2-022 | SGC 증발·강우·routing | `sgc.cpp:1519` `Parptr->EvapTotalLoss += loc_evap_loss;`<br>`sgc.cpp:1544` `Arrptr->SGCdVol[p0] += V; // add rainfall volume to cell`<br>`sgc.cpp:1645-1646` `Arrptr->SGCdVol[p0] -= flowV; // Remove flow volume from source cell`<br>`Arrptr->SGCdVol[Arrptr->FlowDir[p0]] += flowV; // Add flow volume to recipient cell` | `U/cuda_acc_solver.cu:165` `Hval += cell_rain;`<br>`N/rain_uniform.cu:39` `d_assem_sol.h[idx] += cell_rain;` | X에만 | SGC는 증발의 bankfull 통과 손실을 체적으로 계산한다. SGC routing은 지정 수신 셀로 체적을 옮긴다. GPU ACC의 강우는 수심 증가이다. GPU ACC에는 SGC 형상·SGC routing의 대응 계산이 없다. |

`SGC_UpdateH`는 `sgc.cpp:1098`의 `Arrptr->SGCVol[p0] = getmax(Arrptr->SGCVol[p0], C(0.0)); // if volume has gone negative set to zero, should not happen so will result in mass balance error`로 음의 체적을 자른다.
`SGC_UpdateH`는 HFIX·HVAR를 유량 발산 뒤에 적용한다.
`SGC_UpdateH`는 `sgc.cpp:1182-1198`에서 최대 수심을 다시 구해 앞선 집계와 비교한다.
`CalcSGC_pointFREE`는 `sgc.cpp:1764`의 `*qptr = (*qSGoldptr) + (*qoldptr) * (cell_width - w0);`로 채널·범람원 유량을 합한다.
`SGC_Evaporation`, `SGC_Rainfall`, `SGC_Routing`의 이번 대조는 옛 함수 본문에 한정한다.

### 2.3 균일 격자 ACC와 비균일 격자 ACC

| 행 ID | 계산 항목 | 해법 X — 균일 격자 ACC 원문 | 해법 Y — 비균일 격자 ACC 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-023 | theta와 q-centred 혼합 | `U/cuda_acc_solver.cu:723`의 `theta`, `qup`, `qdown` 포함 식(LG2-002). | `N/compute_q.cu:29` `theta = C(1.0);`<br>`N/compute_q.cu:237` `d_non_uniform_nghbrs.q[idx] = ((theta * q_old) - (g * solver.Tstep * hflow * Sf)) / (C(1.0) + g * solver.Tstep * hflow * Manning * Manning * FABS(qvect) / (POW(hflow, (C(10.0) / C(3.0))))) * length; // Volumetric discharge Q` | X에만 | N은 theta를 고정한다. N은 중심 유량과 같은 방향 이웃 유량을 혼합하지 않는다. theta가 1이면 CPU의 역방향 재계산도 같은 식이므로 별도 보정 분기 생략은 계산을 바꾸지 않는다. |
| LG2-024 | 비균일 격자의 길이와 횡방향 마찰 | `fp_acc.cpp:50`의 네 면 평균(LG2-004).<br>`U/cuda_acc_solver.cu:701` `Sf = -dh / cuda::geometry.dx;` | `N/find_nonuniform_neighbours.cu:62` `d_non_uniform_nghbrs.dx[cumu_nghbr_count] = (nghbr < 0) ? pars.dx * (1 << (solver.L - level)) : pars.dx * (1 << (solver.L - d_nghbr_assem_sol.levels[nghbr]));`<br>`N/compute_q.cu:216` `q_opp_avg = q_opp / d_non_uniform_nghbrs.dx_sum[idx];`<br>`N/compute_q.cu:228` `Sf = -dh / length; // (C(0.5)* (dx_owner + dx_nghbr));` | 다름 | N은 인접 셀 폭을 `length`로 사용한다. N은 횡방향 체적 유량의 합을 폭의 합으로 나눈다. 같은 크기의 셀에서는 네 면 평균으로 환원된다. 다른 크기의 셀에서 중심 간 거리로 바꾸는 대안은 `N/compute_q.cu:229`의 주석이다. 선택 이유는 적혀 있지 않다. |
| LG2-025 | 최대 통수심 설정 | `fp_acc.cpp:68` `hflow=getmin(hflow,Solverptr->MaxHflow);`<br>`U/cuda_acc_solver.cu:704` `hflow = getmin(hflow, cuda::solver_params.MaxHflow);` | `N/compute_q.cu:232-233` `MaxHflow = C(10.0);`<br>`hflow = FMIN(hflow, MaxHflow);` | 다름 | N은 전달받은 Solver의 `MaxHflow`를 사용하지 않는다. 기본값 10에서는 결과가 같을 수 있다. 설정값이 다르면 결과가 달라진다. |
| LG2-026 | 비균일 격자 CFL와 꼬리 스레드 | `fp_acc.cpp:271` `locT=cfl*Parptr->dx/(sqrt(g*MH));` | `N/calculate_dt.cu:19` `if (idx < d_assem_sol.length)`<br>`N/calculate_dt.cu:29` `NUMERIC_TYPE h = d_assem_sol.h[idx];`<br>`N/calculate_dt.cu:42` `dt_loc = solver.cfl * dx / SQRT(solver.g * h);` | 다름 | 지역 셀 크기를 사용하는 CFL 식은 균일 격자식의 확장이다. 길이 검사는 초기값 대입만 감싼다. 뒤의 배열 읽기·쓰기는 모든 스레드가 수행한다. `N/cuda_acc_nugrid_simulate.cu:285`의 올림 블록 수와 결합하면 끝 블록의 초과 스레드가 유효 길이 밖을 접근한다. 할당 용량 안의 비활성 부분과 실제 할당 밖을 구분해야 한다. |
| LG2-027 | 수심 발산·건조 유량 제한 | `iterateq.cpp:539-541` `dV = Solverptr->Tstep*(*qxptr0 - *(qxptr0 + 1) + *qyptr0 - *qyptr1);`<br>`(*hptr) += dV / Parptr->dA;`<br>`if (*hptr<C(0.0)) *hptr = C(0.0);` | `N/update_h.cu:104` `NUMERIC_TYPE WDweight = -cv / dV; // C(0.5) for improved drying stability`<br>`N/update_h.cu:196-198` `dV = solver.Tstep * q;`<br>`H += dV / (dx * dx);`<br>`if (H < C(0.0)) H = C(0.0);` | 다름 | N은 가변 개수의 이웃 면 유량을 합한다. N은 별도의 `drychecking` 옵션 없이 수심이 임계값을 넘고 체적이 음수가 될 때 유출 유량을 줄인다. CPU의 선택식 DryCheck와 GPU U의 결합식은 §2.6에서 구분한다. |
| LG2-028 | 질량 출력에 넘기는 값 | `iterateq.cpp:222` `Solverptr->Verror = BCptr->VolInMT - BCptr->VolOutMT - (Solverptr->vol2 + loss - Solverptr->vol1);` | `N/cuda_acc_nugrid_simulate.cu:633-642`는 `write_mass_data`의 열 인자에 `C(0.0),`를 열 번 전달한다. | 다름 | N은 면적·체적·유입·유출·질량오차를 계산해 전달하지 않는다. §2.8은 함수 선언과 출력 열을 대조한다. 이 파일의 `.mass`를 계산된 질량수지로 읽을 수 없다. |

### 2.4 다해상도 분석 — N과 M의 같은 연산 대조

이 절은 비균일 격자 ACC의 지형 인코딩과 adaptive의 다해상도 인코딩을 직접 대조한다.
`maskFilterHaar.h`라는 파일명만으로 N을 Haar 해법으로 판단하지 않았다.
N의 Haar 상수는 `N/maskFilterHaar.h:5-8`에서 주석 처리되어 있다.
N의 실행 식은 `HH`, `GA`, `GB`, `GC` 행렬을 사용한다.
M의 HWFV1만 `M/mra/encode_scale.cuh:12`의 Haar 평균식을 사용한다.

| 행 ID | 계산 항목 | 해법 X — N 원문 | 해법 Y — M 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-029 | scale coefficient의 0.5 계수 | `N/maskFilterHaar.h:31` `#define HH0_11 C(0.5) * ( C(1.0) / C(2.0) )`<br>`N/encode_scale.cuh:54-57`은 아래 전체 식을 사용한다. | `M/mra/Filters.h:10` `#define HH0_11 ( C(1.0) / C(2.0) )`<br>`M/mra/encode_scale.cuh:18-21`은 아래 전체 식을 사용한다. | 다름 | N은 필터 상수에 0.5를 넣는다. M은 합산 뒤 2로 나눈다. `11↔0`, `21↔1x`, `12↔1y`의 세 scale 식은 항과 자식 순서가 같다. |
| LG2-030 | detail의 0.5 계수 | `N/maskFilterHaar.h:79` `#define GA0_11 C(0.5) * ( -SQRT( C(14.0) ) / C(14.0) )`<br>`N/encode_details.cuh:169-172`은 아래 전체 식을 사용한다. | `M/mra/Filters.h:58` `#define GA0_11 ( -sqrt( C(14.0) ) / C(14.0) )`<br>`M/mra/encode_details.cuh:80-83`은 아래 전체 식을 사용한다. | 다름 | alpha·beta·gamma의 각 0·1x·1y 식은 같은 변환이다. 같은 0.5를 다른 위치에 둔다. |
| LG2-031 | Haar 인코딩·디코딩 | N은 `N/encode_scale.cuh:15-18`의 Haar 함수를 주석 처리했다. | `M/mra/encode_scale.cuh:12` `return C(0.5) * (H0 * (H0 * u.child_0 + H1 * u.child_2) + H1 * (H0 * u.child_1 + H1 * u.child_3));`<br>`M/mra/decode_scale_children.cuh:40` `return ( H0 * (H0 * u + G0 * sub_detail.alpha) + G0 * (H0 * sub_detail.beta + G0 * sub_detail.gamma) ) * C(2.0);` | Y에만 | M의 HWFV1은 Haar 변환을 사용한다. 네 자식의 scale은 산술평균으로 환원된다. `decode_0/1/2/3`는 부모와 세 detail로 네 자식을 복원한다. |
| LG2-032 | 지형 정규화 분모 | `N/get_max_scale_coefficients.cu:108-115`의 `cub::DeviceReduce::Max`는 `d_assem_sol.z0`를 입력으로 받는다.<br>`N/get_max_scale_coefficients.cu:124` `maxes.z = FMAX( *h_max_out, C(1.0) );` | `M/mra/get_max_from_array.cu:14` `// custom functor for maximum of absolute value`<br>`M/mra/get_max_from_array.cu:57` `real max_from_array = max( *h_max_out, C(1.0) );` | 다름 | N은 부호 있는 최대값을 사용한다. M은 절댓값 최대값을 사용한다. 두 경로는 분모를 최소 1로 제한한다. 음의 지형이 지배적이면 같은 epsilon이 같은 정규화 기준을 뜻하지 않는다. |
| LG2-033 | qy 정규화 배열 | `M/mra/get_max_scale_coeffs.cu:22` `maxes.qx  = get_max_from_array(d_assem_sol.qx0, d_assem_sol.length);` | `M/mra/get_max_scale_coeffs.cu:23` `maxes.qy  = get_max_from_array(d_assem_sol.qx0, d_assem_sol.length);`<br>`M/classes/Detail.h:46` `real qy_norm  =  qy.get_max() / maxes.qy;` | 다름 | M은 qy detail의 분모를 qx 배열에서 구한다. qy 배열은 별도로 존재한다. `tol_q=0`은 이 배열 대입을 바꾸지 않는다. |
| LG2-034 | 조도·초기 수심 detail의 사용 | `N/encode_and_thresh_topo.cu:132` `d_scale_coeffs.n0[parent_idx] = encode_scale_11(n0_children, n1x_children, n1y_children);`<br>`N/encode_and_thresh_topo.cu:187` `d_scale_coeffs.h[parent_idx] = encode_scale_11(h0_children, h1x_children, h1y_children);`<br>`N/encode_and_thresh_topo.cu:193` `if ((z_details.get_max() / maxes.z) >= epsilon_local) {` | `M/classes/Detail.h:44-47` `real eta_norm = eta.get_max() / maxes.eta;`<br>`real qx_norm  =  qx.get_max() / maxes.qx;`<br>`real qy_norm  =  qy.get_max() / maxes.qy;`<br>`real z_norm   =   z.get_max() / maxes.z;` | 다름 | N은 n·h의 detail을 저장해도 지형 detail만 significant 판정에 사용한다. M은 eta·qx·qy 유동 detail로 활성 격자를 바꾼다. M의 유동 인코딩은 지형 자식에 0을 넣고 지형을 별도 preflag로 유지한다. |
| LG2-035 | 격자 갱신 시점과 지역 임계값 | `N/preflag_topo.cu:17` `NUMERIC_TYPE epsilon_local = eps / ( 1 << (lev - level) );`<br>`N/cuda_acc_nugrid_simulate.cu:217` `preflag_topo /// flag cells with significant topography detail` | `M/mra/encode_and_thresh_flow.cu:46` `real epsilon_local = solver_params.epsilon / ( 1 << (solver_params.L - level) );`<br>`M/cuda_adaptive_simulate.cu:479` `if (solver_params.epsilon > C(0.0) \|\| first_t_step)` | 다름 | 지역 임계값의 식은 같다. N은 초기화에서만 격자를 구성한다. M은 시간 루프에서 유동 detail을 재계산한다. M에서 epsilon이 0이면 첫 단계 이후 격자 재구성 블록을 건너뛴다. |
| LG2-036 | 트리 정규화 | `N/reg_new.cu:52` `if (child_details.has_sig_detail()) d_sig_details[parent_idx] = SIGNIFICANT;`<br>`N/reg_new.cu:79` `if ( child_details.has_sig_detail() ) d_sig_details[g_idx] = SIGNIFICANT;` | `M/mra/regularisation.cu:54` `if (child_details.has_sig_detail()) d_sig_details[parent_idx] = SIGNIFICANT;`<br>`M/mra/regularisation.cu:81` `if ( child_details.has_sig_detail() ) d_sig_details[h_idx] = SIGNIFICANT;` | 같음 | 한 자식이라도 significant이면 부모를 significant로 만든다. 두 경로의 wrapper는 높은 레벨부터 내려간다. 이 처리는 이웃 셀의 2:1 균형 조건과 다르다. |
| LG2-037 | 경계·점 원천·관측점 preflag | `N/preflag_details.cu:22-24` `MortonCode child_idx = gauge_points.codes[i] / 4; // to get Morton code one level below`<br>`h_preflagged_details[starting_idx + child_idx] = true;` | `M/mra/preflag_details.cu:26-28` `MortonCode child_idx = stage_points.codes[i] / 4; // to get Morton code one level below`<br>`h_preflagged_details[starting_idx + child_idx] = true;` | 같음 | 두 경로는 finest 셀의 부모 detail을 표시한다. 두 경로는 네 경계와 점 원천에도 같은 `/4` 연산을 적용한다. |
| LG2-038 | 추가 significance·디코딩·벽 preflag | N driver는 `N/cuda_acc_nugrid_simulate.cu:231-282`에서 정규화·트리 순회·압축을 수행한다. | `M/mra/extra_significance.cu:35-38` `real eps_local_block     = solver_params.epsilon / ( 1 << (solver_params.L - lvl) );`<br>`real eps_extra_sig_block = eps_local_block * pow(C(2.0), M_BAR + 1);`<br>`bool is_extra_sig = (norm_detail >= eps_extra_sig_block);`<br>`M/mra/extra_significance.cuh:4` `#define M_BAR C(1.5)` | Y에만 | M은 예측 refinement와 역변환을 수행한다. `M/mra/decoding_all.cu:12-60`은 추가 significance 뒤 디코딩을 실행한다. `refine_high_wall`은 북·동 가장자리 띠만 preflag한다. 함수명만으로 네 벽 전체 처리라고 쓰면 안 된다. |
| LG2-039 | grading의 레벨별 좌표 범위 | `M/mra/encode_and_thresh_topo.cu:18` `int num_threads = 1 << (2 * level);` | `M/mra/encode_and_thresh_topo.cu:96` `if ( (i > 0 && i < sim_params.xsz) && (j > 0 && j < sim_params.ysz) ) {`<br>`M/mra/encode_and_thresh_topo.cu:99` `Coordinate i_e = i + 1;`<br>`M/mra/encode_and_thresh_topo.cu:114` `d_preflagged_details[curr_lvl_idx + e_idx] = SIGNIFICANT;` | 다름 | grading은 MWDG2 지형 preflag에서만 실행한다. 좌표는 해당 level의 Morton 좌표이다. 검사 상한은 finest `xsz`, `ysz`이다. 마지막 열·행에서 같은 level 밖의 이웃을 표시할 수 있다. |
| LG2-040 | 활성 leaf 순회 | `N/traverse_tree_of_sig_details.cu:57` `bool is_child = ( ( fine_code >> ( 2 * (lev - level) ) ) == current_code);`<br>`N/traverse_tree_of_sig_details.cu:63` `if (!is_sig)` | `M/mra/traverse_tree_of_sig_details.cu:43` `MortonCode curr_code = ( fine_code >> ( 2 * (solver_params.L - level) ) );`<br>`M/mra/traverse_tree_of_sig_details.cu:51` `if (!is_sig)` | 다름 | 두 경로는 finest Morton code의 접두 비트로 조상을 찾는다. 두 경로는 첫 insignificant 조상에서 멈춘다. N은 스택을 사용한다. M은 경로의 접두 비트를 직접 계산한다. |
| LG2-041 | 압축 flag | `N/get_compaction_flags.cu:20` `d_compaction_flags.north_east[idx] = !(current == right);`<br>`N/get_compaction_flags.cu:31` `d_compaction_flags.south_west[idx] = !(current == left);` | `M/neighbours/get_compaction_flags.cu:21` `d_compaction_flags.north_east[idx] = !(current == right);`<br>`M/neighbours/get_compaction_flags.cu:32` `d_compaction_flags.south_west[idx] = !(current == left);` | 같음 | 연속된 같은 활성 셀의 마지막 항목과 첫 항목을 각각 표시한다. 양 끝은 1로 설정한다. |
| LG2-042 | 압축한 필드와 호출 인자 | `N/compaction.cu:111` `if (startfile) {`<br>`N/compaction.cu:116-118` `d_buf_sol.h,`<br>`d_compaction_flags.north_east,`<br>`d_sol.h,` | `M/neighbours/compaction.cu:134-137` `d_buf_neighbours.south.act_idcs,`<br>`d_compaction_flags.south_west,`<br>`d_neighbours.south.act_idcs,` | 다름 | N은 초기 수심·지형·조도 계수를 선택한다. M은 활성 인덱스·레벨·이웃 인덱스를 선택한 뒤 계수를 트리에서 읽는다. M이 수심 선택 코드를 주석 처리한 사실만으로 수심 누락이라고 판단하지 않았다. |
| LG2-043 | Morton 비트 순서와 계층 시작 인덱스 | `N/generate_morton_code.cuh:20` `return dilate(x) \| (dilate(y) << 1);`<br>`N/get_lvl_idx.cuh:27` `return ( ( 1 << (2 * level) ) - 1 ) / 3;` | `M/zorder/generate_morton_code.cuh:15` `return dilate(x) \| (dilate(y) << 1);`<br>`M/utilities/get_lvl_idx.cuh:22` `return ( ( 1 << (2 * level) ) - 1 ) / 3;` | 같음 | x 비트와 y 비트의 위치가 같다. 두 `dilate`는 16비트를 남긴다. 두 `compact`는 같은 역연산을 수행한다. |
| LG2-044 | 정렬과 역정렬 | `N/sort_finest_scale_coefficients_z_order.cu:49` `// sorting the Morton codes is equivalent to ordering the scale coefficients according to` | `M/zorder/sort_finest_scale_coeffs_z_order.cu:16-18` `const int sorted_idx = d_rev_z_order[idx];`<br>`d_assem_sol.h0[idx]  = d_buf_assem_sol.h0[sorted_idx];` | 같음 | N은 CUB SortPairs를 각 필드에 적용한다. M은 정렬 순열을 한 번 구해 각 필드에 적용한다. `reverse_z_order_*`, `rev_z_order_*`, `sort_nghbr_assem_sol_row_major`는 같은 순열을 역으로 적용한다. 수치 값을 평균하거나 재보간하지 않는다. |
| LG2-045 | 작은 L의 고정 블록 가정 | `N/get_reg_tree.cu:30` `index_1D curr_lvl_idx = get_lvl_idx(LVL_SINGLE_BLOCK);`<br>`N/BLOCK_VAR_MACROS.cuh:13` `#define LVL_SINGLE_BLOCK 4` | `M/mra/get_reg_tree.cu:27` `int num_threads  = 1 << (2 * LVL_SINGLE_BLOCK);`<br>`M/utilities/BLOCK_VAR_MACROS.cuh:13` `#define LVL_SINGLE_BLOCK 4` | 다름 | 실제 L과 무관하게 level 4의 detail을 읽는다. detail 배열 길이는 `get_lvl_idx(L)`이다. 기본 블록 크기에서 L≤4이면 level 4 detail이 할당 범위 밖이다. M의 single-block 디코딩·추가 significance도 고정 레벨 루프를 사용한다. 입력 검증에서 이 하한을 강제하지 않는다. |

LG2-029의 N 전체 식은 `N/encode_scale.cuh:54-57`이다.

```cpp
return HH0_11 * u0.child_0 + HH0_12 * u1x.child_0 + HH0_13 * u1y.child_0 +
       HH1_11 * u0.child_2 + HH1_12 * u1x.child_2 + HH1_13 * u1y.child_2 +
       HH2_11 * u0.child_1 + HH2_12 * u1x.child_1 + HH2_13 * u1y.child_1 +
       HH3_11 * u0.child_3 + HH3_12 * u1x.child_3 + HH3_13 * u1y.child_3;
```

LG2-029의 M 전체 식은 `M/mra/encode_scale.cuh:18-21`이다.

```cpp
return (HH0_11 * u._0.child_0 + HH0_12 * u._1x.child_0 + HH0_13 * u._1y.child_0 +
        HH1_11 * u._0.child_2 + HH1_12 * u._1x.child_2 + HH1_13 * u._1y.child_2 +
        HH2_11 * u._0.child_1 + HH2_12 * u._1x.child_1 + HH2_13 * u._1y.child_1 +
        HH3_11 * u._0.child_3 + HH3_12 * u._1x.child_3 + HH3_13 * u._1y.child_3) / C(2.0);
```

LG2-030의 N 전체 식은 `N/encode_details.cuh:169-172`이다.

```cpp
return GA0_11 * u0.child_0 + GA0_12 * u1x.child_0 + GA0_13 * u1y.child_0 +
       GA1_11 * u0.child_2 + GA1_12 * u1x.child_2 + GA1_13 * u1y.child_2 +
       GA2_11 * u0.child_1 + GA2_12 * u1x.child_1 + GA2_13 * u1y.child_1 +
       GA3_11 * u0.child_3 + GA3_12 * u1x.child_3 + GA3_13 * u1y.child_3 ;
```

LG2-030의 M 전체 식은 `M/mra/encode_details.cuh:80-83`이다.

```cpp
return (GA0_11 * u._0.child_0 + GA0_12 * u._1x.child_0 + GA0_13 * u._1y.child_0 +
        GA1_11 * u._0.child_2 + GA1_12 * u._1x.child_2 + GA1_13 * u._1y.child_2 +
        GA2_11 * u._0.child_1 + GA2_12 * u._1x.child_1 + GA2_13 * u._1y.child_1 +
        GA3_11 * u._0.child_3 + GA3_12 * u._1x.child_3 + GA3_13 * u._1y.child_3) / C(2.0);
```

정적 대수 확인은 주석을 제외한 필터 정의를 읽었다.
확인한 필터 정의는 N 144개와 M 144개이다.
두 파일의 `HH·GA·GB·GC` 4군, 자식 4개, 행 3개, 열 3개를 세어 이 수를 얻었다.
모든 N 필터 값은 대응 M 필터 값의 절반이었다.
세 scale 함수와 아홉 detail 함수의 12항은 모두 같은 모드·자식 순서였다.
이 확인은 코드를 컴파일하거나 모델을 실행하지 않았다.

M의 MW 디코더는 `M/mra/decode_scale_children.cuh:70-73`에서 전치 필터와 2배를 사용한다.

```cpp
return (HH0_11 * u0  + HH0_21 * u1x  + HH0_31 * u1y  +
        GA0_11 * da0 + GA0_21 * da1x + GA0_31 * da1y +
        GB0_11 * db0 + GB0_21 * db1x + GB0_31 * db1y +
        GC0_11 * dg0 + GC0_21 * dg1x + GC0_31 * dg1y) * C(2.0);
```

해석: 인코딩 행렬을 `T/2`로 쓰면 디코딩 행렬은 `2*Tᵀ`이다.
필터 상수로 구성한 12×12 행렬의 `T*Tᵀ-I` 최대 절댓값은 Python double 정적 계산에서 `2.220446049250313e-16`이었다.
이 수는 모델 오차가 아니다.
이 수는 필터 상수의 직교성에 대한 부동소수점 대수 확인값이다.
`decode_0/1/2/3`의 자식 순서와 MW의 열 인덱스는 인코딩의 `0,2,1,3` 필터 배치와 대응한다.
`decode_scale_coeffs`는 eta·qx·qy의 각 모드에 같은 디코더를 적용한다.
`decoding`과 `store_scale_coeffs`는 유동 계수를 갱신하고 기존 지형 계수를 보존한다.

LG2-031의 Haar 함수는 M 내부에서 인코더·디코더를 대조했다.
scale 식은 `M/mra/encode_scale.cuh:12`이다.

```cpp
return C(0.5) * (H0 * (H0 * u.child_0 + H1 * u.child_2) + H1 * (H0 * u.child_1 + H1 * u.child_3));
```

alpha·beta·gamma 식은 `M/mra/encode_details.cuh:62`, `:68`, `:74`이다.

```cpp
return C(0.5) * ( H0 * (G0 * u.child_0 + G1 * u.child_2) + H1 * (G0 * u.child_1 + G1 * u.child_3) );
return C(0.5) * ( G0 * (H0 * u.child_0 + H1 * u.child_2) + G1 * (H0 * u.child_1 + H1 * u.child_3) );
return C(0.5) * ( G0 * (G0 * u.child_0 + G1 * u.child_2) + G1 * (G0 * u.child_1 + G1 * u.child_3) );
```

자식 0의 역변환은 `M/mra/decode_scale_children.cuh:40`이다.

```cpp
return ( H0 * (H0 * u + G0 * sub_detail.alpha) + G0 * (H0 * sub_detail.beta + G0 * sub_detail.gamma) ) * C(2.0);
```

자식 1·2·3은 같은 파일 `:52`, `:46`, `:58`에서 대응 H1·G1 부호를 사용한다.
호출 쪽 `:30-33`은 decode_0·decode_1·decode_2·decode_3을 같은 자식 순서로 반환한다.
네 인코딩 식과 네 디코딩 식에서 구성한 4×4 행렬의 역변환 잔차 최대 절댓값은 Python double 정적 대수 확인에서 `4.440892098500626e-16`이었다.
이 확인은 모델 실행이 아니다.

### 2.5 adaptive의 유동 연산자와 이웃

| 행 ID | 계산 항목 | 해법 X 원문 | 해법 Y 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-046 | 지배식의 운동량 이류 | ACC `fp_acc.cpp:88`의 식은 LG2-002에 인용했다. | M `M/classes/FlowVector.h:63` `return { qx, qx * qx / h + g * h * h / C(2.0), qx * qy / h };`<br>`:80` `return { qy, qx * qy / h, qy * qy / h + g * h * h / C(2.0) };` | Y에만 | M의 SWE 플럭스는 운동량 이류를 포함한다. ACC는 국소 관성 유량식을 사용한다. HWFV1과 MWDG2의 해법 선택은 `M/classes/SolverParams.h:38-46`이다. |
| LG2-047 | 재구성과 정수압 절단 | U `U/cuda_acc_solver.cu:702` `hflow = getmax(z0 + h0, z1 + h1) - getmax(z0, z1);` | M `M/classes/FlowVector.h:32` `return max(C(0.0), eta - z_intermediate);`<br>`:44-45` `real qx_star = h_star * get_speed(qx, tol_h);`<br>`real qy_star = h_star * get_speed(qy, tol_h);`<br>`M/operators/eval_loc_face_val_dg2.cuh:14` `return s._0 * basis._0 + s._1x * basis._1x + s._1y * basis._1y;` | 다름 | HWFV1은 상수 상태를 재구성한다. MWDG2는 평균과 두 Legendre 경사로 면 상태를 평가한다. ACC의 이웃 q 혼합은 Legendre 재구성이 아니다. `get_x/y_face_coord`, `get_x/y_face_unit`, `get_leg_basis`는 MWDG2 면 좌표를 같은 기준으로 변환한다. |
| LG2-048 | 리만 플럭스와 방향 회전 | ACC `fp_acc.cpp:88`은 LG2-002의 직접 유량식이다. | M `M/operators/flux_HLL.cuh:40-41` `const real s_neg = (h_neg < solver_params.tol_h) ? u_pos - C(2.0) * a_pos : min(u_neg - a_neg, u_star - a_star);`<br>`const real s_pos = (h_pos < solver_params.tol_h) ? u_neg + C(2.0) * a_neg : max(u_pos + a_pos, u_star + a_star);`<br>`:80` `F.qy = ( s_neg < C(0.0) && s_mid >= C(0.0) ) ? F.h * v_neg : F.h * v_pos;` | Y에만 | M은 파속 부호에 따라 좌측·중간·우측 플럭스를 선택한다. 횡방향 운동량은 중간 파속으로 상류 상태를 선택한다. `flux_HLL_y`는 상태를 회전한 뒤 x 함수를 호출한다. 전체 중간 플럭스는 아래에 인용했다. |
| LG2-049 | 바닥 경사 원천 항 | ACC `fp_acc.cpp:65` `Sf=-dh/Parptr->dx;` | M `M/operators/get_bed_src.cuh:24` `return g * C(0.5) * (h_star_w_pos + h_star_e_neg) * (z_star_e - z_star_w) / dx_loc;`<br>`:68-69` `Sbx.qx._0  = -C(2.0) * sqrt(C(3.0)) * g * h0x_star * z1x_star / dx_loc;`<br>`Sbx.qx._1x = -C(2.0) * sqrt(C(3.0)) * g * h1x_star * z1x_star / dx_loc;` | 다름 | ACC는 수면 경사를 유량식에 넣는다. HWFV1은 바닥 원천 항을 운동량 갱신에서 뺀다. MWDG2는 음의 부호를 포함한 계수 원천 항을 더한다. MWDG2의 y 식은 `:95-96`에서 같은 모드를 사용한다. 부호만 떼어 서로 모순이라고 판정하지 않는다. |
| LG2-050 | 마찰 적분 | ACC `fp_acc.cpp:88`의 분모는 LG2-002에 인용했다. | M `M/operators/apply_friction.cuh:41` `real Cf = g * n * n / pow( h, C(1.0) / C(3.0) );`<br>`:48` `real D_x = C(1.0) + dt * Cf / h * (C(2.0) * ux * ux + uy * uy) / speed;`<br>`:51` `qx += dt * Sf_x / D_x;` | 다름 | M은 마찰을 별도 단계에서 적분한다. HWFV1은 셀 평균과 이웃 평균을 처리한다. MWDG2는 평균과 네 Gauss 상태를 처리한 뒤 경사를 복원한다. `M/operators/friction_implicit.cu:211-263`이 이 호출과 복원이다. 전체 마찰식은 아래에 인용했다. |
| LG2-051 | 공간 조도 입력 | U `U/cuda_acc_solver.cu:694` `if (manning != NULL) fn = C(0.5) * (manning[p0] + manning[p1]);`<br>N `N/compute_q.cu:136` `Manning = C(0.5) * (n_owner + n_nghbr);` | M `M/classes/SimulationParams.h:58` `this->manning = read_keyword_real(input_filename, "fpfric", 6);` | X에만 | M의 활성 마찰 호출은 단일 `sim_params.manning`을 전달한다. M은 U·N의 공간 조도 래스터를 읽거나 인코딩하지 않는다. N은 조도의 scale coefficient를 격자에 맞추어 보관한다. |
| LG2-052 | 건조 상태의 유량과 수심 | N `N/update_h.cu:198` `if (H < C(0.0)) H = C(0.0);` | M `M/operators/dg2_update.cu:336` `const bool below_depth = (h0 < solver_params.tol_h);`<br>`:340-346`은 qx·qy의 여섯 모드를 0으로 만든다.<br>M `M/operators/flux_HLL.cuh:18` `if (U_neg.h < solver_params.tol_h && U_pos.h < solver_params.tol_h) return FlowVector();` | 다름 | M의 갱신 후 건조 처리는 운동량을 0으로 만든다. 이 블록은 수심 평균을 0으로 자르지 않는다. HWFV1도 `M/operators/fv1_update.cu:218-225`에서 유량을 0으로 만든다. 이 차이만으로 실제 음의 수심 발생을 주장하지 않는다. |
| LG2-053 | 제한 함수와 적용 위치 | ACC `fp_acc.cpp:88`은 q-centred 식이다. | M `M/operators/limit_slopes.cu:23` `if (level == solver_params.L)`<br>`:216-217` `const bool above_h_min_limiter_x = ( C(0.05) * max_h < min( coeffs.h._0, min(coeffs_e.h._0, coeffs_w.h._0) ) );`<br>`const bool above_h_min_limiter_y = ( C(0.05) * max_h < min( coeffs.h._0, min(coeffs_n.h._0, coeffs_s.h._0) ) );` | Y에만 | `get_limited_slopes`는 면 불연속 지표가 `tol_Krivo`에 도달하면 minmod를 적용한다. `limit_slopes`는 가장 세밀한 수준의 습윤 stencil에만 제한한 경사를 넣는다. 수심 경사는 제한한 eta 경사에서 지형 경사를 뺀다. ACC에는 이 경사 제한 함수가 없다. |
| LG2-054 | 시간 적분과 단계 사이 인코딩 | U `U/cuda_acc_simulate.cu:192` `solve->FloodplainQ();`는 한 번의 ACC 유량 갱신이다. | M `M/operators/dg2_update.cu:314` `coeffs += dt * (Lx + Ly);`<br>`:326` `h0   = (rkdg2) ? C(0.5) * (coeffs.h._0   + h0  ) : coeffs.h._0  ;` | Y에만 | MWDG2는 두 RK 단계를 사용한다. 나머지 여덟 모드도 `:327-334`에서 같은 평균을 취한다. 두 단계 사이 `M/cuda_adaptive_simulate.cu:710-727`의 `for_nghbrs=true` 인코딩은 이웃 계수를 갱신한다. 이 호출은 detail과 격자 선택을 다시 계산하지 않는다. HWFV1은 한 번의 FV 갱신이다. |
| LG2-055 | 파속과 CFL | ACC `fp_acc.cpp:271` `locT=cfl*Parptr->dx/(sqrt(g*MH));` | M `M/operators/dg2_update.cu:354-355` `real dt_x = solver_params.CFL * dx_loc / ( abs(ux) + sqrt(sim_params.g * h0) );`<br>`real dt_y = solver_params.CFL * dy_loc / ( abs(uy) + sqrt(sim_params.g * h0) );`<br>`:357` `d_dt_CFL[idx] = min(dt_x, dt_y);` | 다름 | SWE는 이류 속도와 중력 파속을 더한다. ACC는 중력 파속만 쓴다. M의 `get_dt_CFL`은 활성 셀 배열의 최소값을 취한다. M의 첫 dt는 `M/cuda_adaptive_simulate.cu:184`의 `real dt = C(0.001);`이다. 셀별 초기 후보는 `initial_tstep`이다. |
| LG2-056 | 허용값과 CFL 옵션 | CPU `lisflood.cpp:174` `ParSolver.DepthThresh = C(1e-3);`는 기본값이다. CPU는 매개변수 파서를 공유한다. | M `M/classes/SolverParams.h:15-17` `real tol_h         = C(1e-3);`<br>`real tol_q         = C(0.0);`<br>`real tol_s         = C(1e-9);`<br>`:41` `this->CFL         = C(0.5);`<br>`:46` `this->CFL         = C(0.3);` | 다름 | M 생성자는 이 세 허용값을 파일에서 읽지 않는다. M 생성자는 해법별 CFL 상수를 지정한다. CPU의 CFL·건조 임계값 옵션이 M에 전달된다고 적을 수 없다. `tol_Krivo`는 `:60`에서 별도로 읽는다. |
| LG2-057 | 비균일 이웃의 표현 | N `N/find_nonuniform_neighbours.cu:59` `if (!already_in_list \|\| (bc_bound && at_border))`<br>`:62` `d_non_uniform_nghbrs.dx[cumu_nghbr_count] = (nghbr < 0) ? pars.dx * (1 << (solver.L - level)) : pars.dx * (1 << (solver.L - d_nghbr_assem_sol.levels[nghbr]));` | M `M/neighbours/find_neighbours.cu:113` `d_neighbours.north.act_idcs[idx] = min(lvl_idx_local, lvl_idx_north) + ( code_north >> (2 * lvl_diff_north) );`<br>`:118` `d_neighbours.north.levels[idx] = min(lvl_local, lvl_north);` | 다름 | N은 셀 변을 따라 서로 다른 이웃과 각 면 길이를 열거한다. M은 방향마다 자기 수준과 이웃 수준 중 낮은 수준의 계수를 참조한다. M의 네 방향 분기와 모서리 분기도 같은 규칙이다. N의 면 목록을 M의 이웃 한 개와 동일 자료구조로 보지 않는다. |
| LG2-058 | 이웃 수 집계와 채우기의 경계 | N `N/count_neighbours.cu:41` `bool at_border = (y_ne == (pars.ysz - 1));`<br>`:63` `bool at_border = (x_ne == (pars.xsz - 1));` | N `N/find_nonuniform_neighbours.cu:45` `bool at_border = ( y_ne == (pars.ysz - 1) \|\| ( y_ne == (mesh_dim - 1) ) );`<br>`:74` `bool at_border = ( x_ne == (pars.xsz - 1) \|\| ( x_ne == (mesh_dim - 1) ) );` | 다름 | 같은 이웃 목록의 count와 fill 조건이 다르다. `pars.xsz/ysz`보다 큰 정방형 padding의 바깥 북·동 셀에서 count는 배열 밖 이웃을 참조할 수 있다. fill은 그 위치를 경계로 처리한다. 실제 영역과 정방형이 같으면 이 차이는 드러나지 않는다. |
| LG2-061 | 중력 상수 | CPU `lisflood.cpp:169` `ParSolver.g = C(9.8065500000000);` | M `M/classes/SimulationParams.h:18` `real g = C(9.80665);` | 다름 | U·N은 공통 CPU Solver의 g를 전달받는다. M은 별도 상수를 사용한다. 이 차이를 설명하는 판 주석은 없다. |

LG2-048의 중간 질량·종방향 운동량 플럭스는 `M/operators/flux_HLL.cuh:65-78`이다.

```cpp
F.h =
    ( s_pos * F_neg.h - s_neg * F_pos.h + s_neg * s_pos * (h_pos - h_neg) )
    /
    (s_pos - s_neg);

F.qx =
    ( s_pos * F_neg.qx - s_neg * F_pos.qx + s_neg * s_pos * (U_pos.qx - U_neg.qx) )
    /
    (s_pos - s_neg);

const real s_mid =
    ( s_neg * h_pos * (u_pos - s_pos) - s_pos * h_neg * (u_neg - s_neg) )
    /
    ( h_pos * (u_pos - s_pos) - h_neg * (u_neg - s_neg) );
```

LG2-050의 마찰 원천 항·분모·증분은 `M/operators/apply_friction.cuh:45-52`이다.

```cpp
real Sf_x = -Cf * ux * speed;
real Sf_y = -Cf * uy * speed;

real D_x = C(1.0) + dt * Cf / h * (C(2.0) * ux * ux + uy * uy) / speed;
real D_y = C(1.0) + dt * Cf / h * (C(2.0) * uy * uy + ux * ux) / speed;

qx += dt * Sf_x / D_x;
qy += dt * Sf_y / D_y;
```

`apply_friction`은 `M/operators/apply_friction.cuh:20-38`에서 작은 수심과 작은 두 속도를 먼저 처리한다.
이 두 분기는 0으로 나누는 마찰식을 실행하지 않는다.
`FlowVector`, `PlanarCoefficients`, `FlowCoeffs`, `ChildScaleCoeffsHW/MW`의 산술 연산자는 각 성분에 같은 스칼라 연산을 적용한다.
이 산술 보조 함수는 별도 지배식을 추가하지 않는다.

LG2-053의 불연속 지표 한 방향은 `M/operators/get_limited_slopes.cuh:57-58`이다.

```cpp
const real DS_e = ( norm_x > C(1e-12) ) ? jump_e / (C(0.5) * dx_finest * norm_x) : C(0.0);
const real DS_w = ( norm_x > C(1e-12) ) ? jump_w / (C(0.5) * dx_finest * norm_x) : C(0.0);
```

같은 파일 `:63-68`의 x 경사 선택은 다음과 같다.

```cpp
const real u1x_limited = (max(DS_e, DS_w) < tol_Krivo) ? u._1x : minmod
(
    u._1x,
    (u._0 - u_w._0),
    (u_e._0 - u._0)
);
```

y 방향 `:60-61`, `:70-75`는 north·south와 dy_finest를 사용한다.
minmod는 `M/operators/minmod.cuh:15`의 `if ( ( a * b > C(0.0) ) && ( a * c > C(0.0) ) )`를 검사한다.
부호가 같으면 `:19`의 `return min( abs(a), min( abs(b), abs(c) ) ) * sign_a;`를 사용한다.
부호가 다르면 0을 반환한다.

### 2.6 초기화·건조 보정·경계·점 원천

| 행 ID | 계산 항목 | 해법 X 원문 | 해법 Y 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-059 | 최초 H·이전 유량·최대 수심 | N `N/init_q.cu:13` `d_non_uniform_nghbrs.q[idx] = C(0.0);`<br>`input.cpp:1414-1415` `Arrptr->Qxold = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));`<br>`Arrptr->Qyold = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` | U `U/cuda_acc_flow.cu:22-23` `flow.Qxold = cuda::GhostRaster::allocate_pinned_Q(geometry);`<br>`flow.Qyold = cuda::GhostRaster::allocate_pinned_Q(geometry);`<br>`:69-70` `cuda::GhostRaster::copy_Q(dst.Qxold, src.Qxold, geometry);`<br>`U/cuda_acc_simulate.cu:66` `nullify_max(U.maxHtm, U.initHtm, U.totalHtm, geometry, pitch, offset, verbose);` | 다름 | U의 할당 함수는 0으로 초기화하지 않는다. startfile이 꺼지면 initialise_H도 H를 설정하지 않는다. U driver는 `initialise_discharge`를 호출하지 않는다. 최초 ACC 식은 아직 설정하지 않은 Qxold·Qyold를 읽는다. `nullify_max`의 인자에는 `U.maxH`가 없다. 체크포인트는 maxH를 복원할 수 있다. 체크포인트는 Qold를 복원하지 않는다. |
| LG2-060 | 건조 보정 유량의 공유 | CPU `util.cpp:48-51` `if (*q1 < 0) *q1 *= WDweight;`<br>`if (*q2 > 0) *q2 *= WDweight;`<br>`if (*q3 < 0) *q3 *= WDweight;`<br>`if (*q4 > 0) *q4 *= WDweight;` | 공통 GPU `cuda/cuda_boundary.cu:237` `NUMERIC_TYPE qxptr0 = Qx[i + j * (cuda::geometry.xsz + 1)];`<br>`:252` `if (qxptr0 < C(0.0)) qxptr0 *= WDweight;`<br>`:259-261`은 지역 복사본으로 dV·H를 갱신한다. | 다름 | CPU는 공유 면 배열을 바꾼다. GPU는 네 지역 복사본만 바꾼다. 이웃 셀과 이후 Qold 갱신은 보정 전 배열을 읽는다. 이 차이는 `drycheck`가 켜지고 `cv+dV<0`일 때 발생한다. 8.3 nodata 패치는 이 배열을 수정하지 않는다. |
| LG2-062 | 면 QFIX 경계 | CPU `boundary.cpp:414` `case QFIX4:`<br>`:416` `*qptr = -BCptr->BC_Val[BCi] * sign*Parptr->dx;`<br>N `N/compute_q.cu:190` `else if (boundary_type == QFIX \|\| boundary_type == QVAR)` | U `U/cuda_acc_solver.cu:274` `case QVAR5:`<br>`:277` `qptr = -sign*h0*cuda::geometry.dx;` | X에만 | U의 네 면 switch에는 QVAR만 있다. `rg -n 'QFIX\|QVAR' U/cuda_acc_solver.cu`는 QFIX를 찾지 못한다. 경계 복사 `cuda/cuda_boundary.cu:556`은 `BC_Ident`를 그대로 전송한다. QFIX를 QVAR로 바꾸는 보정 경로는 없다. |
| LG2-063 | 마른 셀에 HFIX·HVAR 유입 | CPU `boundary.cpp:190` `if (true)//Arrptr->H[p0]>Solverptr->DepthThresh)`<br>`:192` `hflow = getmax(Arrptr->H[p0], BCptr->BC_Val[BCi] - Arrptr->DEM[p0]);`<br>N `N/compute_q.cu:171` `hflow = getmax(h_owner, boundary_value - z_owner);` | U `U/cuda_acc_solver.cu:253` `if (U.H[p0] > cuda::solver_params.DepthThresh)`<br>`:256` `hflow = getmax(U.H[p0], h0 - DEM[p0]);` | 다름 | U는 셀 자체가 먼저 젖어야 경계 수면을 읽는다. CPU와 N은 높은 경계 수면으로 마른 셀을 젖게 할 수 있다. U의 나머지 세 면도 같은 내부 수심 조건이다. |
| LG2-064 | Q 경계의 유속 분모 | N `N/compute_q.cu:23` `NUMERIC_TYPE dh, Sf, hflow, MaxHflow, theta, length, Manning, g;`<br>`:192` `d_non_uniform_nghbrs.q[idx] = -boundary_value * sign * length; // no need for q_source as we need discharge not h` | N `N/compute_q.cu:197` `d_non_uniform_nghbrs.v[idx] = d_non_uniform_nghbrs.q[idx] / length / hflow;` | 다름 | QFIX·QVAR 분기는 지역 변수 hflow를 설정하지 않는다. 비영 유량이면 같은 호출이 그 변수를 유속 분모로 읽는다. FREE와 H 경계 분기는 각각 `:154`, `:171`에서 hflow를 설정한다. 이 후보는 경계 유속과 그 집계에 해당한다. Q 자체의 지정식은 별개이다. |
| LG2-065 | adaptive Q 경계의 수심 덮어쓰기 | CPU `boundary.cpp:416`은 지정 면 유량을 설정한다. N `N/compute_q.cu:192`는 `// no need for q_source as we need discharge not h`라고 적는다. | M `M/neighbours/add_ghost_cells.cu:160-161` `d_assem_sol.h0[idx]        = boundaries.north.q_src(dt, dx_finest);`<br>`d_neighbours.north.h0[idx] = d_assem_sol.h0[idx];`<br>`M/classes/Boundary.h:83` `real q_src(const real& dt, const real& dx) { return inlet * dt / dx; }` | 다름 | M은 기존 셀 수심을 유량 증분으로 덮어쓴다. M은 이 분기에서 지정 유량을 법선 운동량에 넣지 않는다. 동·남·서 면도 같은 대입이다. M의 점 Q 원천은 증분을 `+=`로 더한다. 따라서 점 원천과 같은 증분 처리라고도 설명할 수 없다. |
| LG2-066 | FREE·벽·수위 경계의 수치 상태 | N `N/compute_q.cu:155` `Sf = boundary_value; // 0.02; //BCptr->BC_Val[BCi]; // MKS must check this`<br>U `U/cuda_acc_solver.cu:239-240`은 마찰을 포함한 외향 유량을 계산한다. | M `M/neighbours/add_ghost_cells.cu:139` `d_neighbours.north.h0[idx]  = pow( (d_assem_sol.qy0[idx] * d_assem_sol.qy0[idx]) / sim_params.g, C(1.0) / C(3.0) );`<br>`:150` `d_assem_sol.h0[idx]        = max(C(0.0), boundaries.north.inlet - d_assem_sol.z0[idx]);` | 다름 | ACC의 FREE는 외향 관성 유량식이다. M의 FREE는 지정한 ghost 수심과 복사한 운동량으로 HLL을 푼다. M의 H 경계는 셀 수심도 강제로 설정한다. 기본 벽은 ghost 법선 유량을 0으로 만든다. U는 FREE 경사 미지정 시 인접 지형차를 사용한다. N은 전달한 경사값을 그대로 사용한다. |
| LG2-067 | 한 변의 경계 구간 수 | CPU→U `cuda/cuda_boundary.cu:553` `dst.BC_count = src.numBCs;`<br>`:556` `cuda::copy(dst.BC_type, src.BC_Ident, src.numBCs*sizeof(ESourceType));` | N `N/Boundary.h:275` `while (filedir != bcidir)`<br>M `M/classes/Boundary.h:322` `while (filedir != bcidir)` | 다름 | CPU·U는 경계 셀마다 종류를 보관한다. N·M의 Boundary 객체는 방향마다 처음 찾은 한 구간을 보관한다. `bound`는 그 start·end 한 쌍을 검사한다. 같은 방향의 여러 구간을 모두 지원한다고 적을 수 없다. |
| LG2-068 | 경계·점 원천 시계열의 끝과 건너뛰기 | CPU `boundary.cpp:1440` `if (t >= times[count - 1])`<br>`:1444` `return values[count - 1];`<br>`:1455` `for (int i = timeSeries->prev_index + 1; i < count; i++)` | N `N/Boundary.h:453` `if ( (row - 1) < timeseries_len )`<br>`:456` `NUMERIC_TYPE t_2 = time_data[row + 1];`<br>M `M/classes/Boundary.h:478`, `M/classes/PointSources.h:429`도 같은 조건이다. | 다름 | N·M은 마지막 행에서도 row+1을 읽을 수 있다. 읽기 함수는 길이 1을 거부하지 않는다. row 증가는 while이 아닌 if 한 번이다. 여러 구간을 건너뛰면 현재 구간을 찾지 못한다. N의 활성 점 원천은 `N/PointSources.h:193`의 CPU 보간기를 사용한다. N의 사용하지 않는 옛 `update_source`를 활성 경로의 근거로 삼지 않는다. |
| LG2-069 | 점 Q 원천의 수심 증분 | CPU `iterateq.cpp:500` `Arrptr->H[BCptr->xpi[ps_index] + BCptr->ypi[ps_index] * Parptr->xsz] += BCptr->PS_Val[ps_index] * Parptr->dx*Solverptr->Tstep / Parptr->dA;`<br>GPU 공통 `cuda/cuda_boundary.cu:155`는 같은 폭·면적 변환이다. | N `N/PointSources.h:205` `NUMERIC_TYPE q_src(const NUMERIC_TYPE& dt, const NUMERIC_TYPE& dx, const int idx) { return this->d_srcs[idx] * dt / dx; }`<br>M `M/classes/PointSources.h:126` `return this->d_srcs[idx] * dt / dx;` | 같음 | 정방형 셀에서 q·dx·dt/dx²와 q·dt/dx는 같다. 셀 유량 업데이트와 점 원천의 적용 순서는 해법마다 다르다. LG2-065의 면 경계 덮어쓰기는 이 일치에 포함하지 않는다. |
| LG2-070 | adaptive 최초 H 원천의 지형 인덱스 | M `M/mra/insert_point_srcs.cu:16` `HierarchyIndex h_idx = point_sources.d_codes[idx];`<br>`:22` `d_assem_sol.h0[h_idx] = point_sources.d_srcs[idx] - d_assem_sol.z0[idx];` | N `N/update_h.cu:279` `H = point_sources.d_srcs[i] - d_assem_sol.z0[idx];`<br>M의 반복 삽입 `M/mra/reinsert_point_srcs.cu:23` `d_scale_coeffs.eta0[h_idx] = point_sources.d_srcs[idx];` | 다름 | M의 최초 함수는 점 번호 idx로 지형을 읽는다. 쓰기 위치는 Morton 코드 h_idx이다. 두 번호가 다르면 잘못된 지형을 뺀다. 이 호출은 finest 계수 복사 뒤에 있다. 다음 시간 루프는 scale 계수에 원천을 다시 넣는다. 직접 유동 오염 범위는 제한되지만 최초 최대값 정규화는 이 배열을 읽는다. |
| LG2-071 | 시계열 평가 시각 | CPU `boundary.cpp:422` `h0 = InterpolateTimeSeries(BCptr->BC_TimeSeries[BCi], Solverptr->t);`<br>U `U/cuda_acc_simulate.cu:194` `cuda::Boundary::update_time_series(solver.t);` | M `M/cuda_adaptive_simulate.cu:424` `current_time += dt;`<br>`:462` `point_sources.update_all_srcs(current_time);`<br>`:604` `boundaries.update_all_inlets(input_filename, current_time);` | 다름 | CPU·U·N은 단계 시작 시각을 사용한다. M은 먼저 시각을 증가시킨다. M의 두 RK 경계 호출은 같은 갱신한 경계값을 사용한다. 이 시간 표본 차이를 자동으로 같은 시계열 적용이라고 정리하지 않는다. |
| LG2-072 | 침투·증발·구조물·porosity·routing | CPU `iterateq.cpp:153-156`의 침투·증발·강우·routing 호출과 `:530-535`의 porosity 면적 갱신이 있다. | U `U/cuda_acc_simulate.cu:178-230`, N `N/cuda_acc_nugrid_simulate.cu:541-621`, M `M/cuda_adaptive_simulate.cu:422-798`에는 대응 침투·증발·구조물·porosity·routing 갱신 호출이 없다. | X에만 | GPU ACC·adaptive가 CPU의 이 옵션을 전부 구현한다는 근거가 없다. SGC의 형상·채널 경계·채널 증발·채널 routing은 LG2-013~022에서 분리했다. |

LG2-068의 N 경계 보간 전체 조건·대입은 `N/Boundary.h:453-470`이다.

```cpp
if ( (row - 1) < timeseries_len )
{
    NUMERIC_TYPE t_1 = time_data[row];
    NUMERIC_TYPE t_2 = time_data[row + 1];

    if (time_now > t_2)
    {
        row++;

        t_1 = time_data[row];
        t_2 = time_data[row + 1];
    }

    NUMERIC_TYPE inlet_1 = inlet_data[row];
    NUMERIC_TYPE inlet_2 = inlet_data[row + 1];

    inlet = inlet_1 + (inlet_2 - inlet_1) / (t_2 - t_1) * (time_now - t_1);
}
```

M의 `M/classes/Boundary.h:478-494`와 `M/classes/PointSources.h:429-445`는 자료형·시각 변수·대입 대상을 바꾼 같은 보간 구조이다.
각 reader는 초·분·시간을 초로 한 번 변환한다.
그 변환은 배열 끝 검사 결함을 보정하지 않는다.
U의 활성 보간기는 `cuda/cuda_boundary.cu:11-36`의 `linear_interpolate`이다.
이 함수는 최초값·최종값과 내부 구간을 별도로 처리한다.

M의 Monai·Oregon 경계는 일반 H 경계의 별도 분기이다.
`M/neighbours/add_ghost_cells.cu:450-480`은 이 두 분기를 서쪽에만 적용한다.
`is_monai`와 `is_oregon`은 DEM 파일 이름의 접두어로 결정한다.
`non_reflective_wave`는 Newton 반복으로 경계 상태를 구한다.
Oregon 분기는 `:476`의 `real s = C(0.6) * exp( -C(0.25) * ( current_time - C(14.75) ) * ( current_time - C(14.75) ) );`로 wavemaker 속도를 구한다.
이 실험별 경계와 그 외부 실험의 재현성은 LG2-094의 H 범위로 구분한다.

LG2-094의 Newton 갱신은 `M/operators/non_reflective_wave.cuh:49-50`의 `dp = f0 / df;`와 `p1 = p0 - dp;`이다.
이 함수는 같은 파일 `:34`의 `while ( (k <= max_k) && cond == 0 )`로 반복한다.
같은 파일 `:28`은 `int k = 0, max_k = 100, cond = 0;`을 지정한다.
같은 파일 `:56-74`는 상대 증분·함숫값의 허용차를 검사한다.
출력 상태 식은 같은 파일 `:86-91`이다.

```cpp
real beta_minus = ur - C(2.0) * cr;
real beta_plus  = C(2.0) * sqrt(g * (h_inlet + C(0.13535))) + h_inlet * sqrt(g / C(0.13535));

// this is "hb" in MKS Fortran code
real h_out = C(1.0) / C(16.0) / g * (beta_plus - beta_minus) * (beta_plus - beta_minus);
real u_out = C(0.5) * (beta_plus + beta_minus);
```

### 2.7 강우와 시간 간격의 호출 순서

| 행 ID | 계산 항목 | 해법 X 원문 | 해법 Y 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-073 | NetCDF 누적 강우의 단위 | CPU `rain/rain.tpp:65` `if (read_file_netCDF(&netcdf_, t / C(3600.0) /* s to hr */))`<br>`:67` `netcdf_.dt *= C(3600.0); // hr to s`<br>`:72-73` `netcdf_.data[i] /= netcdf_.dt;`<br>`netcdf_.data[i] /= C(1000.0); // mm to m` | U `U/cuda_acc_simulate.cu:55-56`, N `N/cuda_acc_nugrid_simulate.cu:163`은 같은 DynamicRain 템플릿을 생성한다.<br>U `cuda/cuda_rain.cu:110` `Hval += rate_at_cell_ACC(rain_data, i, j) * cuda::dt;`<br>N `N/rain.cu:76` `d_assem_sol.h[idx] += rate_at_cell(rain_data, i, j, dx, pars, xsz_rain, tly_rain, dx_rain, dy_rain) * solver.Tstep;` | 같음 | 공통 reader는 누적 mm를 m/s로 바꾼다. 각 갱신은 강우율에 dt를 곱한다. 실제로 어느 dt를 쓰는지는 LG2-077에 분리했다. |
| LG2-074 | 균일 강우 시계열의 시간 단위 | CPU `infevap.cpp:96` `rain_rate=InterpolateTimeSeries(Arrptr->rain,Solverptr->t);//constant rate across whole floodplain`<br>N 경계 reader `N/Boundary.h:440` `time_data[i] *= time_multiplier;` | 공통 `rain/Rainfall_uniform.h:74` `t_1 = t_2*time_multiplier;`<br>`:90` `value = value_1 + (value_2 - value_1) / ((t_2 - t_1) * time_multiplier) * (time_now - t_1 * time_multiplier);`<br>N `N/RainfallUniform.h:79`, `:95`에 같은 식이 있다. | 다름 | 구간을 전진한 호출은 t_1만 초로 바꾼다. 보간식은 t_1에 배수를 다시 곱한다. t_2는 원래 단위로 남는다. 초 단위에서는 배수가 1이다. 분·시간 단위에서는 혼합 단위가 된다. 구간 전진도 if 한 번이므로 여러 구간을 건너뛰는 경우를 처리하지 않는다. |
| LG2-075 | 공간 강우의 배열 범위 | `rain/rain.h:53-54` `* The rainfall rate (m/s) at cell (i, j).`<br>`* If the cell is outside the rainfall domain, the rainfall rate is zero.` | CPU `rain/rain.tpp:118` `if (tile_i < geometry_.xsz && tile_j >= 0)`<br>`:120` `return netcdf_.data[tile_j*geometry_.xsz + tile_i];`<br>N `N/rain.cu:33` `if (tile_i < xsz_rain && tile_j >= 0)`<br>U `cuda/cuda_rain.cu:79`의 `if (tile_i < cuda::rain_geometry.xsz && tile_j >= 0)`도 같은 두 조건만 검사한다. | 다름 | 세 경로 모두 tile_j의 상한을 검사하지 않는다. 모델 영역이 강우 배열의 아래로 나가면 0 대신 범위 밖을 읽을 수 있다. `rate_at_cell_SGC`도 `rain/rain.tpp:146`에 같은 검사를 둔다. 원점·타일 크기 확인 함수는 배열 상한 검사 자체를 대신하지 않는다. |
| LG2-076 | `_NETCDF=0`의 활성 상태 | `rain/rain.tpp:17` `enabled_ = (strlen(filename) > 0);` | `rain/rain_stub.tpp:5-11`의 생성자는 `{}`이다.<br>`rain/rain.h:95` `return enabled_;`<br>`:114` `bool enabled_;` | 다름 | stub 생성자는 enabled_를 설정하지 않는다. U·N driver는 매 단계 `rain.enabled()`를 호출한다. `_NETCDF=0`이면 활성 상태 읽기가 미정 값에 의존한다. stub의 update_H가 빈 함수라는 사실은 GPU driver의 enabled 읽기를 없애지 않는다. 기본 CMake 설정 `_NETCDF=1`에서는 이 stub을 사용하지 않는다. |
| LG2-077 | 강우에 곱하는 단계 dt | CPU `iterateq.cpp:146`의 FloodplainQ 뒤 `:157`의 dynamicRain.update_H를 호출한다.<br>`rain/rain.tpp:178` `NUMERIC_TYPE inc = rate_at_cell(Parptr, i, j) * Solverptr->Tstep;` | U `U/cuda_acc_simulate.cu:184-185`는 동적 강우를 적용한다.<br>`:190` `dynamic_dt.update_dt_ACC();`<br>N `N/cuda_acc_nugrid_simulate.cu:563-564`는 `solver.Tstep`으로 균일 강우를 적용한다.<br>`:578` `solver.Tstep = get_dt_CFL(d_dt_CFL, d_assem_sol.length);` | 다름 | U 동적 강우는 이전 cuda::dt를 사용한다. U의 최초 cuda::dt는 0이다. N의 동적·균일 강우도 CFL 갱신 전 dt를 사용한다. 유동 갱신과 시각 증가는 새 dt를 사용한다. 두 dt가 다르면 강우 체적과 경과 시간이 맞지 않는다. U의 균일 강우는 CFL 갱신 뒤에 있다. |
| LG2-078 | 강우의 질량 장부 | CPU `rain/rain.tpp:180` `total_rain_mass += inc*Parptr->dA;`<br>`:184` `Parptr->RainTotalLoss += total_rain_mass;`<br>`infevap.cpp:124` `Parptr->RainTotalLoss+=loc_rainfall_total; // Update domain mass balance` | U `cuda/cuda_rain.cu:110`은 H만 갱신한다.<br>N `N/rain_uniform.cu:41` `//        loc_rainfall_total += cell_rain * Parptr->dA; // mass balance for local cell (cumulative)` | X에만 | GPU ACC의 강우 갱신은 CPU의 RainTotalLoss를 누적하지 않는다. N의 해당 누적 행은 주석이다. GPU의 질량 출력 열은 LG2-028·081에서 확인한다. |
| LG2-079 | SGC 강우 캐시 갱신 조건 | `rain/rain.tpp:206` `if (update_time_SGC(curr_time)); // if the file had to be read update rain_grid` | `rain/rain.tpp:207-230`의 블록은 if 뒤 빈 문장 다음에 있다.<br>`:227` `rain_grid[grid_cell_index] = rate_at_cell_SGC(i, j,row_dx, row_dy, tly)*cell_area_col[j];` | 다름 | 세미콜론 때문에 캐시 블록은 매 호출 실행된다. 강우 파일을 읽었을 때만 갱신한다는 주석과 실행 횟수가 다르다. 이 함수는 강우율×셀 면적을 저장한다. 이 함수는 여기서 H에 강우를 두 번 더하지 않는다. 이 행은 캐시·성능 처리의 H로 분류한다. |
| LG2-080 | adaptive 강우 입력 | U `U/cuda_acc_simulate.cu:181-186`, `:205-210`과 N `N/cuda_acc_nugrid_simulate.cu:551-565`는 강우를 적용한다. | M `M/cuda_adaptive_simulate.cu:422-798`은 점 원천·경계·마찰·SWE·CFL을 갱신한다. | X에만 | M의 활성 시간 루프에는 균일 강우와 DynamicRain 호출이 없다. U·N의 강우 지원을 M에 확장해서 적을 수 없다. |
| LG2-095 | 비균일 격자 강우의 남북 인덱스 | N `N/read_raster_file.cpp:39` `fscanf( fp, "%" NUM_FMT, &raster_array[(nrows - 1 - j) * mesh_dim + i] );`<br>N `N/rain.cu:69` `int j = compact(code >> 1);` | N `N/rain.cu:30-31` `NUMERIC_TYPE top_gap = pars.tly - tly_rain;`<br>`int tile_j = (j - top_gap/ dx) * dx / dy_rain;` | 다름 | N의 j는 남쪽에서 증가한다. 강우 배열의 j는 북쪽 첫 행에서 증가한다. N의 강우식은 이 방향을 뒤집지 않는다. 같은 원점·같은 셀 크기에서도 남북 대칭이 아닌 강우는 뒤집힌 행을 참조한다. 공간 강우 배열의 방향은 `rain/rain.tpp:26-29`의 y 간격·tly 정의와 함께 확인했다. |
| LG2-096 | 음의 균일 강우 | CPU `infevap.cpp:113-118`은 음의 수심을 검사하고 H를 0으로 만든다. | N `N/rain_uniform.cu:33-37`의 음의 수심 처리는 주석이다.<br>`:39` `d_assem_sol.h[idx] += cell_rain;`<br>U `U/cuda_acc_solver.cu:165` `Hval += cell_rain;` | 다름 | GPU 균일 강우는 CPU의 직후 수심 제한을 생략한다. N은 뒤의 update_h에서 다시 0으로 자른다. U도 뒤의 공통 update_H에서 다시 0으로 자른다. 이 후속 보정 때문에 최종 수심이 반드시 음수라고 결론내리지 않는다. |

LG2-008의 GPU 후보 배열은 `cuda/cuda_solver.templates.cu:68`의 `dt_field = cuda::GhostRaster::allocate_device_H(geometry);`에서 할당한다.
할당 경로는 `cuda/cuda_geometry.cu:51-52`에서 `malloc_device`를 호출한다.
`cuda/cuda_util.cu:63`의 원문은 `checkCudaErrors(cudaMalloc(&ptr, size));`이다.
이 경로는 dt_field를 초기화하지 않는다.
습윤 셀의 첫 읽기 조건은 `U/cuda_acc_solver.cu:121`의 `if (FABS(dt[j * cuda::pitch + i] - C(0.0)) < C(1e-6)) {`이다.
그 조건이 참이면 `:122`의 `dt[j * cuda::pitch + i] = cuda::solver_params.max_dt;`를 실행한다.
그 조건이 거짓이면 LG2-008의 이전 값과 최소값을 취한다.
해석: 0으로 초기화한다고 가정해도 최초 습윤 셀의 CFL 후보는 그 호출에서 버려진다.
건조 셀은 `:132`에서 max_dt를 저장한다.
이미 한 번 젖은 셀은 건조 분기를 거치지 않는 동안 과거 최소 dt를 계속 유지한다.
CPU는 `iterateq.cpp:144`에서 단계마다 초기 상한으로 되돌린다.
이 후보는 단순한 CUB 최소값 표기 차이가 아니다.

`DynamicTimestepACC::update_dt_ACC`는 `cuda/cuda_solver.templates.cu:90-92`에서 항상 셀별 계산과 최소값 축약을 실행한다.
이 함수는 생성자가 보관한 `adaptive`를 검사하지 않는다.
CPU ACC도 `CalcT`에서 항상 ACC CFL을 계산한다.
따라서 공통 FV/DG 시간 간격 클래스의 옵션 의미를 ACC에 그대로 적용하지 않는다.

DynamicRain의 원점 검사 원문은 `rain/rain.tpp:40-41`이다.

```cpp
return FABS(Parptr->blx - geometry_.blx) < epsilon &&
    FABS(Parptr->bly - geometry_.bly) < epsilon;
```

타일 크기 검사는 같은 파일 `:50-54`이다.

```cpp
NUMERIC_TYPE dx_ratio = geometry_.dx / Parptr->dx;
NUMERIC_TYPE dy_ratio = geometry_.dy / Parptr->dy;

return FABS(round(dx_ratio) - dx_ratio) <= epsilon &&
        FABS(round(dy_ratio) - dy_ratio) <= epsilon;
```

epsilon은 같은 파일 `:5`의 `static const NUMERIC_TYPE epsilon = C(1e-12);`이다.
이 보조 함수는 원점·정수 타일 비율의 계약 검사이다.
이 보조 함수는 LG2-075의 셀별 y 상한을 검사하지 않는다.
N의 강우 방향 대조에는 reader의 `lisflood2/file_tool.cpp:359` 원문 `// assume data are ordered left-to-right, top-to-bottom`도 사용했다.

### 2.8 질량 집계와 출력 값

| 행 ID | 계산 항목 | 해법 X 원문 | 해법 Y 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-081 | 면 경계·강우를 포함한 질량 장부 | CPU `iterateq.cpp:167`은 BoundaryFlux를 호출한다.<br>`:222` `Solverptr->Verror = BCptr->VolInMT - BCptr->VolOutMT - (Solverptr->vol2 + loss - Solverptr->vol1);` | U `U/cuda_acc_solver.cu:1053` `void lis::cuda::acc::Solver::FloodplainQ()`<br>`:987-1002`의 update_flow_variables는 mass_stats를 사용하지 않는다.<br>`cuda/stats.cpp:74` `C(0.0) /*Parptr->RainTotalLoss - (Parptr->InfilTotalLoss + Parptr->EvapTotalLoss)*/` | 다름 | U의 H 합계는 계산한 체적이다. U의 면 유량·강우는 MassStats에 더해지지 않는다. U의 점 원천과 nodata 배수는 별도 통계 경로를 사용한다. 따라서 U의 전체 질량 오차 열을 CPU와 같은 수지라고 해석할 수 없다. N은 LG2-028처럼 체적·면적·수지 열에 0을 전달한다. |
| LG2-082 | GPU 질량 오차의 시간 분모 | U `U/cuda_acc_simulate.cu:212` `stats_collector.accumulate_mass();`<br>`:219` `stats_collector.accumulate_mass();` | `cuda/cuda_stats.cu:83` `cumulative_time += cuda::dt;`<br>`:118` `(net_source_flux - volume_change)/time` | 다름 | 한 단계에서 두 원천 묶음을 따로 누적한다. 두 호출이 각각 경과 시간을 더한다. 질량량 누적은 묶음별로 가능하지만 경과 시간은 두 배가 된다. 같은 잔차의 Qerror 분모가 실제 누적 시간과 다르다. |
| LG2-083 | N의 최대 수심·침수 시간 표본 | CPU `iterateq.cpp:190` `if (Solverptr->t >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)`<br>U `U/cuda_acc_simulate.cu:250`은 같은 선택 조건이다. | N `N/cuda_acc_nugrid_simulate.cu:624` `if (solver.t >= pars.MassTotal)` 안의 `:660`에서 update_max를 호출한다.<br>N `N/update_max.cu:23` `totalHtm[idx] += solver.Tstep / C(3600.0);` | 다름 | N은 mint_hk가 꺼져도 MassInt 표본에서만 최대값을 갱신한다. 침수 시간에는 표본 단계의 마지막 dt만 더한다. 중간 단계의 최대 수심과 젖은 시간은 이 호출로 누적되지 않는다. CPU도 mint_hk를 켜면 표본 갱신을 선택한다. 따라서 이 행은 N의 옵션 생략 C로 분류한다. |
| LG2-084 | M의 누적 수리 진단 | U `U/cuda_acc_snapshot.cu:54-57`은 inittm·totaltm·max·maxtm을 쓴다.<br>CPU는 `iterateq.cpp:214-255`에서 체적·수지·침수 면적을 집계한다. | M `M/output/write_cumulative_data.cpp:28` `if (first_t_step) fprintf(cumulative_input, "simtime,runtime_mra,runtime_solver,runtime_total,dt,reduction\n");` | X에만 | M의 cumulative 파일은 계산 시간과 격자 감소율을 저장한다. 이 파일은 질량 수지 장부가 아니다. M 시간 루프는 U의 네 누적 수리 래스터를 계산하지 않는다. |
| LG2-085 | `.Qx/.Qy`의 단위 | CPU `output.cpp:803-804`는 `Arrptr->Qx`, `Arrptr->Qy`를 저장한다.<br>CPU `fp_acc.cpp:307` `Arrptr->Qxold[pqptr]=Arrptr->Qx[pqptr]*dxinv;` | U `U/cuda_acc_snapshot.cu:41-42` `writer_HU = write_async(U.Qxold, ".Qx", 1, call_gzip);`<br>`writer_HV = write_async(U.Qyold, ".Qy", 2, call_gzip);`<br>U `U/cuda_acc_solver.cu:606` `Uold.Qxold[pqptr]=Uold.Qx[pqptr]*(C(1.0)/cuda::geometry.dx);` | 다름 | CPU ACC의 저장값은 체적 유량이다. U의 같은 확장자는 단위폭 유량을 저장한다. 두 값은 dx를 곱해야 대응한다. dx가 1이면 수치가 같아 이 차이가 가려진다. M의 qx·qy는 SWE 상태의 단위폭 유량이다. M의 별도 소문자 qx·qy 출력을 CPU ACC의 면 Q와 혼동하지 않는다. |
| LG2-086 | M의 raster·stage 공간 평가 | M `M/output/write_all_raster_maps_dg2.cu:117` `real h_loc_face_val = eval_loc_face_val_dg2(coeffs.h, leg_basis);`<br>`:140` `vx[idx] = (h_loc_face_val > solver_params.tol_h) ? qx_loc_face_val / h_loc_face_val : C(0.0);` | M `M/output/project_assem_sol.cu:73-75` `d_assem_sol.h0[idx]  = d_scale_coeffs.eta0[act_idx] - d_scale_coeffs.z0[act_idx];`<br>`d_assem_sol.qx0[idx] = d_scale_coeffs.qx0[act_idx];`<br>`d_assem_sol.qy0[idx] = d_scale_coeffs.qy0[act_idx];` | 다름 | MWDG2 raster는 leaf 내부의 세밀한 셀 중심에서 세 모드를 평가한다. stage용 projection은 선택한 leaf의 평균만 복제한다. stage 유속은 그 평균 q를 평균 h로 나눈다. 따라서 같은 위치의 stage와 DG2 raster가 반드시 같은 값은 아니다. HWFV1에서는 경사 모드가 없다. |
| LG2-087 | M stage 헤더의 좌표 원점 | N `N/write_gauge_point_data.cu:193-194` `NUMERIC_TYPE x_centre = pars.blx + x * pars.dx + pars.dx / C(2.0);`<br>`NUMERIC_TYPE y_centre = pars.bly + y * pars.dx + pars.dx / C(2.0);` | M `M/output/write_stage_point_data.cu:72-73` `i * dx_finest + dx_finest / C(2.0),`<br>`j * dy_finest + dy_finest / C(2.0),` | 다름 | M stage 헤더는 xmin·ymin을 더하지 않는다. M의 StagePoints reader는 절대 좌표에서 원점을 빼서 인덱스를 만든다. M VTK 좌표는 `M/output/write_soln_vtk.cu:94-101`에서 원점을 다시 더한다. 원점이 0이 아니면 stage 헤더가 입력·VTK의 좌표와 다르다. 이 후보는 stage 값의 배열 위치가 아니라 헤더 좌표에 해당한다. |
| LG2-088 | 초기 수면고의 수심 변환 | U 공통 `cuda/cuda_simulate.cu:38-40` `if (states.startelev == ON)`<br>`{`<br>`StartFile::subtract_dem(H, DEM, geometry, pitch, offset);` | N `N/get_modal_values.cu:64-67`의 startelev 조건·subtract_dem은 주석이다.<br>`:62` `read_raster_file(h_raster_filename, h_raster, mesh_dim, C(0.0));` | X에만 | N은 startfile 값을 그대로 수심으로 읽는다. N의 `startelev` 옵션은 이 경로에서 적용되지 않는다. M의 실제 지형 입력은 HWFV1 상수 또는 MWDG2 nodal projection으로 따로 처리한다. |
| LG2-089 | N 정기 raster 출력 호출 | U `U/cuda_acc_snapshot.cu:32` `writer_H = write_async(U.H, ".wd", 0, call_gzip);` | N `N/cuda_acc_nugrid_simulate.cu:743` `//    		write_raster_maps`<br>`:730-751`의 projection·출력 호출은 주석이다. | X에만 | N은 정기 출력 시 VTK 분기를 실행할 수 있다. N은 최대값 raster와 stage·velocity를 별도로 쓴다. `write_raster_maps` 함수가 존재해도 정기 `.wd` 호출이 활성이라는 뜻은 아니다. |
| LG2-090 | 상태 저장과 장치 자료 이동 | N `N/write_chkpnt.cu:75-76` `fwrite(h, sizeof(NUMERIC_TYPE), d_assem_sol.length, check_fp);`<br>`fwrite(q, sizeof(NUMERIC_TYPE), d_non_uniform_nghbrs.length, check_fp);` | N `N/read_chkpnt.cu:194-195` `copy_cuda(d_assem_sol.h, h, bytes_sol);`<br>`copy_cuda(d_non_uniform_nghbrs.q, q, bytes_dis);` | 다름 | N 체크포인트는 구성된 leaf의 H·면 Q·선택적 조도·최대값 배열을 저장·복원한다. 차원·판 검사와 시간·출력 간격도 복원한다. U의 공통 체크포인트와 M의 장치 복사도 상태 전송이다. 이 행은 해법 식의 차이로 판정하지 않는 H이다. 최초 U Qold 미복원은 LG2-059에 분리했다. |
| LG2-098 | 최초 질량 수지의 기준 체적 | CPU `iterateq.cpp:29` `Solverptr->vol1 = DomainVol(Statesptr, Parptr, ChannelSegments, Arrptr, ChannelSegmentsVecPtr);` | `cuda/cuda_stats.cuh:35` `NUMERIC_TYPE previous_volume = C(0.0);`<br>`cuda/cuda_stats.cu:93` `NUMERIC_TYPE volume_change = current_volume - previous_volume;` | 다름 | U는 루프 전에 초기 H의 체적을 previous_volume에 넣지 않는다. 최초 create_entry는 U driver `:267`의 출력 단계에 있다. 시작 수심이 비영이면 최초 체적 변화가 초기 체적까지 포함한다. 유효한 체크포인트는 `cuda/cuda_simulate.cu:311`에서 previous_volume을 복원한다. |

CPU 비-SGC 침수 면적의 문턱은 `iterateq.cpp:254`의 `if (Arrptr->H[ptr] > C(0.01)) FloodArea += dA; // standard area calculation`이다.
GPU StatsCollector의 histogram 경계는 `cuda/cuda_stats.cu:45`의 `histogram_levels[1] = DepthThresh;`를 사용한다.
이 면적 정의 차이는 LG2-081의 진단 항목 차이에 포함한다.
정방형 GPU의 체적은 `cuda/cuda_stats.cu:157`의 `return h_volume * geometry.dx * geometry.dy;`이다.
CPU는 latlong·porosity·SGC 선택에 따라 면적과 체적의 정의를 바꾼다.
그 옵션 차이는 LG2-013·021·072에 포함한다.

N의 scalar velocity는 `N/update_h.cu:189-194`에서 방향별 면 유속 평균의 최대 절댓값을 두 방향으로 합성한다.
CPU stage scalar velocity는 `iterateq.cpp:286`에서 각 방향의 양쪽 면 최대 절댓값을 합성한다.
N VTK는 이 scalar v를 저장한다.
N 조도 VTK는 n0도 저장한다.
M VTK는 leaf 평균 h·qx·qy·z와 dt를 저장한다.
M DG2 raster는 평균과 경사로 재구성한다.
이 출력 위치·집계 차이는 LG2-086의 C에 포함한다.

LG2-085의 출력 보정 경로도 확인했다.
`cuda/cuda_snapshot.templates.cu:96-97`은 field를 공통 Snapshot에 그대로 전달한다.
실제 x 면 출력 원문은 `cuda/io.templates.cpp:45-46`이다.

```cpp
fprintf(file, "%.*" NUM_FMT "\t", precision,
    array[j * (pitch + 1) + i + offset]);
```

y 면 출력은 같은 파일 `:63-64`의 같은 배열 접근이다.
이 출력기는 단위폭 유량에 dx를 다시 곱하지 않는다.

### 2.9 테스트 초기 조건·빌드 조건·계산 외 처리

| 행 ID | 계산 항목 | 해법 X 원문 | 해법 Y 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG2-091 | CUDA 보조 함수와 성능 계산 | `cuda/common/helper_cuda.h:785-786` `uint64_t compute_perf = (uint64_t)deviceProp.multiProcessorCount *`<br>`sm_per_multiproc * deviceProp.clockRate;` | `cuda/common/helper_string.h:194` `value = atoi(&string_argv[length + auto_inc]);` | 다름 | common은 오류 검사·장치 선택·문자열 파싱을 제공한다. common의 코어 수·클록 곱은 장치 선택 점수이다. 이 값은 수리 플럭스나 CFL이 아니다. `helper_functions.h`는 이 helper를 묶는다. 모델 완료 조건에 SDK 내부 검증을 추가하지 않는다. |
| LG2-092 | 실제 빌드와 실행 분기 | `CMakeLists.txt:73` `if (CMAKE_CUDA_COMPILER)`<br>`:77` `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)`<br>`:178` `add_subdirectory(cuda/adaptive)` | `lisflood.cpp:437` `else if (Statesptr->acceleration == ON)`<br>`:442` `else if (Statesptr->acc_nugrid == ON)`<br>`:447` `else if (Statesptr->mwdg2 == ON \|\| Statesptr->hwfv1 == ON)` | 다름 | CUDA 빌드 안에서 서로 다른 실행 분기를 선택한다. adaptive는 `:450`의 `simulation.run(argc, argv);`로 파일을 다시 파싱한다. `:457`의 `return 0;` 때문에 CPU 초기화로 이어지지 않는다. 동일 전역 구조체가 존재한다는 사실로 CPU 옵션의 전달을 추정하지 않는다. |
| LG2-093 | 내장 테스트와 초기화 | M `M/input/read_test_case.cpp:33` `const int max_test_case = 23;`<br>`M/tests/h_init.cuh:70` `case 23: // radial dam break` | CPU·U·N의 이 보고서 대상 시간 루프에는 이 23종 synthetic selector가 없다. | X에만 | M의 주석 목록은 22번에서 끝난다. 실제 선택 범위는 0~23이다. 0은 실제 지형 입력이다. 초기 조건의 식은 아래 표에 따로 대조했다. 내장 테스트가 존재한다는 사실은 테스트 통과 결과가 아니다. |
| LG2-094 | 실험별 비반사·wavemaker 경계 | M `M/neighbours/add_ghost_cells.cu:450` `if (sim_params.is_monai)`<br>`:471` `else if (sim_params.is_oregon)` | U·N의 FREE·H·Q 경계에는 이 두 실험 이름에 따른 분기가 없다. | X에만 | M은 비반사 상태 반복과 Gaussian wavemaker를 별도로 구현한다. 해당 실험의 외부 논문·자료와 계수가 같은지는 이 코드 쌍의 비교 대상이 아니다. 이 행은 H이다. |
| LG2-097 | 미사용 계산 보조 경로 | N `read_all_bdy_conds.cu`, `read_bdy_conds.cu`, `read_point_srcs.cu`와 옛 `PointSources::update_source`는 별도 정의이다. | 현재 N driver는 `Boundary`·`PointSources` 객체와 CPU `LoadBCs/LoadBCVar`를 사용한다.<br>M은 활성 `encode_scale_coeffs.cuh`·`decode_scale_coeffs.cuh`를 사용한다. | 다름 | 옛 parser·계수 wrapper의 존재를 활성 동작으로 합치지 않는다. `M/mra/encode_scale_coefficients.cuh`, `decode_scale_coefficients.cuh`, `store_scale_coefficients.cuh`의 옛 자료형 wrapper는 활성 include·호출 경로와 분리했다. U의 zero_ghost_cells는 정의되어도 driver가 호출하지 않는다. 이 행은 H이다. |

기본 매크로 조합은 `config.default.cmake:1-8`이다.

```cmake
set(_NETCDF 1)
add_compile_definitions(_NUMERIC_MODE=1)
add_compile_definitions(_ONLY_RECT=1)
add_compile_definitions(_PROFILE_MODE=0)
add_compile_definitions(_DISABLE_WET_DRY=0)
add_compile_definitions(_CALCULATE_Q_MODE=1)
add_compile_definitions(_SGM_BY_BLOCKS=0)
add_compile_definitions(_BALANCE_TYPE=0)
```

`_NUMERIC_MODE`는 CPU NUMERIC_TYPE과 M real의 float·double 선택에 관여한다.
`_NETCDF`는 실제 강우 구현과 stub을 선택한다.
`CUDA`는 GPU entry와 CUDA 자료형을 활성화한다.
`RESULT_CHECK`는 `sgc.cpp:726-1768`의 옛 갱신 함수들을 활성화한다.
기본 설정은 `lisflood.h:60`, `:64`의 RESULT_CHECK 정의를 주석으로 둔다.
`_ONLY_RECT`, `_CALCULATE_Q_MODE`, `_DISABLE_WET_DRY`, `_BALANCE_TYPE`, `_PROFILE_MODE`는 대상 ACC·N·M 계산 함수의 식을 선택하는 분기가 아니다.
대상 계산 구현에서 위 이름을 직접 검색한 결과는 `RESULT_CHECK`, `_NETCDF`, M의 `_NUMERIC_MODE` 분기뿐이었다.
따라서 이 매크로로 LG2-018·020·033·060·064·068의 차이를 설명할 수 없다.
LG2-019는 사각 셀일 때만 드러난다.
기본 정방형 셀에서는 두 폭이 같아 그 후보가 가려진다.

다음 표는 LG2-093의 모든 지형·수심 초기화 함수를 다룬다.
원문은 `M/tests/`와 `M/classes/Depths1D.h`이다.
테스트 이름과 외부 이론의 정확성은 H이다.

| 선택 번호 | 지형 계산과 원문 | 초기 수심 계산과 원문 | 내부 호출 확인 |
|---|---|---|---|
| 1·2 | `M/tests/topo.cuh:23-31`은 x 또는 y를 `topo_c_prop_1D`에 전달한다. `M/tests/topo_c_prop_1D.cuh:20-41`은 삼각·포물선·평탄 블록 구간을 선택한 뒤 `return C(10.0) * z_int;`를 실행한다. | `M/tests/h_init_c_property.cuh:18-20` `real h = eta_west - z_int;` / `return h;` | Depths1D의 양쪽 수면은 `M/classes/Depths1D.h:15-16`의 `C(6.0)`이다. |
| 3·4 | 1·2와 같은 지형 함수이다. | 같은 수심 함수이다. Depths1D `:19-20`은 양쪽에 `C(2.0)`을 지정한다. | `M/tests/h_init_c_property.cuh:22`의 `return (h < 0) ? 0 : h;`는 앞 return 뒤에 있다. 이 절은 음의 초기값을 자른다고 적지 않는다. |
| 5·6 | topo의 default는 `M/tests/topo.cuh:19`의 `real z_int = C(0.0);`를 유지한다. | `M/tests/h_init_overtopping.cuh:15` `return (x_or_y_int <= 25) ? max(C(0.0), bcs.hl - z_int) : max(C(0.0), bcs.hr - z_int);` | `M/tests/h_init.cuh:32-44`가 x·y 인자를 나눈다. Depths1D는 6·2이다. |
| 7·8·9·10 | 같은 평탄 지형이다. | 같은 overtopping 함수이다. Depths1D `:30-31`은 6·0이다. | 9·10은 SimulationParams에서 조도를 0.02로 설정한다. |
| 11·12·13·14 | `M/tests/topo.cuh:33-39`는 c-property 지형을 사용한다. | 같은 overtopping 함수이다. Depths1D는 11·12에서 6·2, 13·14에서 6·0이다. | 수심은 각 쪽 수면에서 그 위치의 지형을 뺀 뒤 0으로 자른다. |
| 15·16 | `M/tests/topo_triangle.cuh:14` `real slope = C(0.4) / C(3.0);`<br>`:20` `z_int = ( x_or_y_int - C(25.5) ) * slope;`<br>`:24` `z_int = C(0.4) - ( x_or_y_int - C(28.5) ) * slope;` | `M/tests/h_init.cuh:47` `h_int = ( x_int < C(15.5) ) ? C(0.75) : C(0.0);`<br>`:50` `h_int = ( y_int < C(15.5) ) ? C(0.75) : C(0.0);` | 지형의 두 구간은 `M/tests/topo_triangle.cuh:18`, `:22`의 조건을 사용한다. x·y 방향만 바뀐다. |
| 17·18 | `M/tests/topo_parabolic_bowl.cuh:13` `return C(0.01) * x_or_y_int * x_or_y_int;` | `M/tests/h_init_parabolic_bowl.cuh:15` `const real eta = C(0.2) * x_or_y_int + C(10.0);`<br>`:17` `return max(C(0.0), eta - z_int);` | `M/tests/topo.cuh:47-54`, `M/tests/h_init.cuh:52-56`의 x·y 선택이 대응한다. Depths1D의 case 17 주석은 이 함수의 수심 인자가 아니다. |
| 19 | `M/tests/topo_three_cones.cuh:19-40`은 세 중심·반경에서 선형 원뿔을 구해 최대값과 0을 취한다. `:34-36`은 `real zb_1 = (rm_1 - r_1) / 8;` / `real zb_2 = (rm_2 - r_2) / 8;` / `real zb_3 = C(0.3) * (rm_3 - r_3);`이다. | `M/tests/h_init.cuh:59` `h_int = C(1.0) - z_int;` | 20도 같은 지형 함수를 사용한다. |
| 20 | 19와 같은 세 원뿔이다. | `M/tests/h_init.cuh:62` `h_int = ( x_int < C(16.0) ) ? max( (C(1.875) - z_int), C(0.0) ) : C(0.0);` | SimulationParams는 조도 0.018을 지정한다. |
| 21 | `M/tests/topo_diff.cuh:17-23`은 높이·기울기가 다른 세 원뿔의 최대값을 취한다. 초기 z_int는 0이다. | `M/tests/h_init.cuh:65` `h_int = C(1.95) - z_int;` | `M/tests/topo.cuh:61-63`이 이 함수를 선택한다. |
| 22 | `M/tests/topo_non_diff.cuh:17-29`는 y 구간과 세 x 구간에서 높이 0.86·1.78·2.30을 선택한다. | `M/tests/h_init.cuh:68` `h_int = C(1.78) - z_int;` | `M/tests/h_init_three_blocks.cuh:13`의 별도 helper는 같은 수면차를 반환하지만 현재 selector는 inline 식을 사용한다. |
| 23 | topo default의 평탄 지형이다. | `M/tests/h_init_radial.cuh:14` `const real r = sqrt(x_int * x_int + y_int * y_int);`<br>`:16` `return ( r < C(2.5) ) ? C(2.5) : C(0.5);` | `M/tests/h_init.cuh:70-71`이 helper를 호출한다. |

`h_init_three_peaks.cuh`는 `C(1.95)-z_int`를 반환하는 별도 helper이다.
현재 selector의 case 21은 같은 수면차를 직접 계산한다.
`h_init_c_property`의 뒤쪽 두 return은 실행되지 않는다.
해석: 부호가 있는 수심 초기값은 일정 수면의 다항식 표현을 유지하는 선택일 수 있다.
이 보고서는 그 선택을 외부 테스트 정의와 대조하지 않았다.
이 사실을 실제 유동 계산의 음의 수심 결함으로 확대하지 않는다.

초기 노드 좌표는 `M/mra/init_nodal_values.cu:53-54`의 `const real x_int = sim_params.xmin + dx_finest * x_idx;`와 `const real y_int = sim_params.ymin + dy_finest * y_idx;`이다.
이 함수는 각 좌표에 topo와 h_init를 적용한다.
이 함수는 `:74-75`에서 두 초기 유량을 0으로 둔다.
`get_nodal_values`는 이 초기화를 호출한다.
`get_modal_values`는 modal_projections를 호출한다.
평균 투영은 `M/mra/modal_projections.cu:71`의 `d_assem_sol.h0[idx]  = C(0.25) * (h_NW  + h_NE  + h_SE  + h_SW );`이다.
x 경사 투영은 `:78`의 `d_assem_sol.h1x[idx]  = (h_NE  - h_NW  + h_SE  - h_SW ) / ( C(4.0) * sqrt( C(3.0) ) );`이다.
y 경사 투영은 `:83`의 `d_assem_sol.h1y[idx]  = (h_NE  - h_SE  + h_NW  - h_SW ) / ( C(4.0) * sqrt( C(3.0) ) );`이다.
qx·qy·z는 `:72-86`에서 같은 평균·경사 식을 사용한다.
해석: 상수 입력의 두 경사는 0이다.
해석: 선형 입력의 평균은 셀 중심값이다.
HWFV1은 평균만 사용한다.
MWDG2는 평균과 두 경사를 사용한다.

### 2.10 계산 루틴의 범위 확인

다음 표는 대상 구현의 계산 루틴을 앞 절의 항목에 연결한다.
같은 이름의 선언 헤더는 구현과 한 묶음이다.
자료형의 할당·복사·해제와 출력 문자열 보조 함수는 LG2-090·091·097의 H이다.
범위 밖 해법의 본체를 이 목록에 추가하지 않는다.

| 원문 경로·루틴 | 확인한 계산 또는 호출 | 이 보고서의 위치 |
|---|---|---|
| `fp_acc.cpp:18-326` — CalcFPQxAcc·CalcFPQyAcc·CalcMaxH·CalcT·MaskTestAcc·UpdateQs | 두 방향 유량·마찰·최대 수심·CFL·유량 이력 | §2.1 전체 |
| `iterateq.cpp:6-478` — IterateQ | 채널 호출 간격·유량→경계→원천→H 순서·시간 증가·최대값·수지·면적·stage·virtual gauge·checkpoint·정기/overpass 출력·정상상태 종료 | §2.1·2.6~2.8. `:428-431`은 Qin−Qout 허용차를 연속 열 번 만족하면 종료한다. 이 CPU 종료 옵션은 LG2-072에 포함한다. |
| `iterateq.cpp:482-587` — UpdateH | 점 Q 원천→면 유량 발산→음의 H 제한→점 H 강제 | LG2-060·069·072. PorArea 선택은 CPU 전용이다. |
| `sgc.cpp:18-559` — SGC_wp_prams·CalcSGC_A·CalcSGC_UpV·CalcSGC_R·CalcSGCz | 회귀계수·일곱 단면·면적/폭·동수반경·체적·bankfull·사행·levee·mask | LG2-013~017. 형상별 전처리와 switch의 활성 분기를 구분했다. |
| `sgc.cpp:563-724` — SGC_hotstart | x·y 정상류 초기 유량과 폭 | LG2-020 |
| `sgc.cpp:729-1029` — SGC_FloodplainQ·CalcFPQxSGC·CalcFPQySGC | 채널·범람원 합산·weir 호출·면 유속 | LG2-016~019. RESULT_CHECK 전용이다. |
| `sgc.cpp:1031-1431` — SGC_UpdateH·SGC_BCs | 체적 보존 변수·점/면 H/Q/FREE·방향별 cell_length/cell_width | LG2-021. 경계는 `:1289-1297`에서 N/S와 E/W의 길이·폭을 바꾼다. |
| `sgc.cpp:1436-1768` — SGC_Evaporation·SGC_Rainfall·SGC_Routing·CalcSGC_UpH·CalcSGC_pointFREE | 채널 수면적을 반영한 증발·강우 체적·D4 체적 이동·역변환·외향 합산 유량 | LG2-014·021·022 |
| `lisflood.h` — Solver·Pars·States·Arrays·SGCprams·NUMERIC_TYPE | 옵션·단위·기본 매크로·정밀도·상수 선언 | §1·2.9. 기본값의 실제 대입은 lisflood.cpp로 확인했다. |
| `rain/rain.cpp`, `rain.h`, `rain.tpp`, `rain_stub.tpp`, `Rainfall_uniform.h` | 생성·시간 갱신·원점/타일 검사·CPU/SGC 셀 매핑·H/강우 격자 갱신·단위 변환·stub | LG2-073~079·096 |
| U `U/cuda_acc_solver.cu:50-94` — zero_ghost_cells_N/S/E/W | 네 방향 H ghost 초기화 정의 | LG2-097. 활성 ACC driver는 이 wrapper를 호출하지 않는다. |
| U `U/cuda_acc_solver.cu:99-169` — update_dt_per_element·update_uniform_rain_func | 셀 CFL 후보·균일 강우 | LG2-008·077·096 |
| U `U/cuda_acc_solver.cu:171-544` — update_ghost_cells | 네 방향 NONE/FREE/HFIX/HVAR/QVAR 면 유량 | LG2-062·063·066 |
| U `U/cuda_acc_solver.cu:546-649` — update_max_field_ACC·update_flow_variables_x/y·MaskTest | 최대값·침수 시간·Qold 변환·미사용 mask | LG2-006·009·011·012·059 |
| U `U/cuda_acc_solver.cu:651-923` — CalcFPQxAcc_·CalcFPQyAcc_·FloodplainQx/y | 두 방향 ACC 식과 습윤 검사 | LG2-001~007·010 |
| U `U/cuda_acc_solver.cu:930-1070` — Solver 생성자·각 launch wrapper | Flow 복사·마찰 선택·계산 호출·빈 slope 함수 | LG2-004·059·081·097 |
| U `cuda_acc_simulate.cu`, `cuda_acc_flow.cu`, `cuda_acc_max_field.cu`, `cuda_acc_snapshot.cu` | 시간 루프·배열 초기 상태·최대값 reduction 정의·출력 선택 | LG2-008·059·073~085·090. `MaxH::update`의 CUB 최대값은 CPU CalcMaxH의 활성 대체 호출이 아니다. |
| U `Rainfall_uniform.h` | 공통 reader와 같은 보간 정의 | LG2-074. 활성 driver의 include는 공통 `rain/Rainfall_uniform.h`이다. |
| N `get_modal_values.cu`, `read_raster_file.cpp`, `copy_finest_coefficients.cu`, `init_h.cu`, `init_q.cu`, `init_max.cu` | DEM·1x/1y·조도·시작 수심·nodata/padding·finest 저장·초기값 | LG2-034·059·088·095. 초기 q·v는 0이다. |
| N `encode_scale.cuh`, `encode_details.cuh`, `maskFilterHaar.h`, `SubDetail.h`, `SubDetails.h` | scale 3개·detail 9개·필터·detail 최대 절댓값 | LG2-029~034 |
| N `preflag_topo.cu`, `encode_and_thresh_topo.cu`, `get_max_scale_coefficients.cu` | 수준별 threshold·지형/조도/초기 H 인코딩·정규화 분모 | LG2-032·034·035 |
| N `preflag_details.cu`, `gen_bdy_morton_codes.cu`, GaugePoints·Boundary·PointSources의 코드 생성 | 경계·gauge·점 원천의 finest parent 강제 | LG2-037·067~070 |
| N `reg_new.cu`, `get_reg_tree.cu`, `traverse_tree_of_sig_details.cu` | 조상 significant OR·트리 하강·조도 유무별 leaf 추출 | LG2-036·040·045 |
| N `get_compaction_flags.cu`, `compaction.cu` | NE/SW run 경계·Flagged 선택·선택 개수 | LG2-041·042 |
| N `dilate.cuh`, `compact.cuh`, `generate_morton_code.cuh`, `generate_all_morton_codes.cu`, `get_lvl_idx.cuh`, `get_level.cu`, `is_child.cuh` | 비트 삽입/추출·Morton 결합·수준 시작 인덱스·계층/자식 판정 | LG2-043·044. index 자료형의 비트 폭과 shift를 구분했다. |
| N `sort_finest_scale_coefficients_z_order.cu`, `reverse_z_order_act_idcs.cu`, `reverse_z_order_assembled_solution.cu`, `sort_nghbr_assem_sol_row_major.cu` | 같은 순열로 필드·인덱스 정렬·역정렬 | LG2-043·044 |
| N `count_neighbours.cu`, `init_neighbours.cu`, `find_nonuniform_neighbours.cu` | 이웃 개수→누적 scan→이웃 인덱스·길이·방향 | LG2-024·057·058 |
| N `count_interfaces_per_neighbours.cu`, `init_interfaces.cu`, `find_interfaces.cu`, `load_interface_q_vol.cu`, `load_neighbour_h.cu` | 횡방향 면 개수·scan·소유자/이웃 flags·폭 합·이전 Q·H/z/n 적재 | LG2-024·051·057 |
| N `calculate_dt.cu`, `get_dt_CFL.cu`, `compute_q.cu`, `update_h.cu` | ACC·CFL·체적 발산·유출 제한·음의 H 절단·방향별 유속·점 원천 | LG2-023~027·058·064·069 |
| N `rain.cu`, `rain_uniform.cu`, `RainfallUniform.h` | 동적/균일 강우·nodata 배수·보간 | LG2-074~078·095·096. nodata 배수는 H를 0으로 만들고 별도 질량 장부를 누적하지 않는다. |
| N `project_assem_sol.cu`, `reinsert_assem_sol.cu`, `update_max.cu` | leaf 계수 재삽입→finest 복제→역정렬·최대값 누적 | LG2-040·044·083·086 |
| N `write_gauge_point_data.cu`, `write_mass_data.cu`, `write_max_maps.cu`, `write_raster_maps.cu`, `write_soln_vtk.cu` | H·scalar v·0인 수지 열·최대 raster·정기 raster 정의·leaf VTK와 조도 VTK | LG2-028·083·086·087·089 |
| N `read_chkpnt.cu`, `write_chkpnt.cu` | state와 시간·기하 정보의 저장·복원 | LG2-090 |
| N의 `read_num_*`, `read_*bdy*`, `read_point_srcs.cu`, `read_gauge_points.cu` | 구간 좌표→셀 수·원천 종류·Morton 위치 파싱 | LG2-037·067·097. 활성 객체와 독립 reader를 구분했다. |
| M `input/read_and_project_modes_fv1.cu`, `read_and_project_modes_dg2.cu`, `read_raster_file.cpp`, `read_cell_size.cpp` | 실제 DEM·H·선택적 Q 입력·노드 배열·modal projection·벽 padding | LG2-047·088·093 |
| M `input/read_keyword_*`, `read_command_line_params.cpp`, `read_test_case.cpp`, `read_bound_conds.cpp`, `read_sim_params.cpp`, `read_solver_params.cpp`, `read_plot_params.cpp`, `read_save_interval.cpp` | 매개변수·단위·CLI 덮어쓰기·구간/저장시각 파싱 | LG2-056·067·071·092·093·097. 활성 생성자의 읽기 목록과 옛 구조체 reader를 혼동하지 않았다. |
| M `mra/init_nodal_values.cu`, `get_nodal_values.cu`, `modal_projections.cu`, `get_modal_values.cu`, `tests/*` | 23종 테스트의 모든 지형·수심 helper·노드→평균/경사 | LG2-093과 §2.9의 함수별 표 |
| M `mra/Filters.h`, `encode_scale.cuh`, `encode_scale_coeffs.cuh`, `encode_details.cuh`, `Detail.h`, `SubDetail.h`, `SubDetails.h` | HW 평균/detail·MW scale/detail·성분별 정규화 최대값 | LG2-029~034 |
| M `mra/init_eta_temp.cu`, `get_max_from_array.cu`, `get_max_scale_coeffs.cu` | eta=H+z 임시 배열·absmax·분모 하한·qx/qy 입력 | LG2-032·033 |
| M `mra/init_sig_details.cu`, `zero_details.cu`, `preflag_details.cu`, `refine_high_wall.cu`, `preflag_topo.cu`, `encode_and_thresh_topo.cu` | flow detail 0화·지형 detail 유지·지형/경계/점/북·동 벽 preflag·grading | LG2-034·037~039 |
| M `mra/encode_and_thresh_flow.cu`, `encoding_all.cu` | HW/MW·일반/단일 block·전체 인코딩/이웃 전용 인코딩 | LG2-034·035·045·054. 분기별 호출 인자가 같은 변환 함수에 연결된다. |
| M `mra/regularisation.cu`, `get_reg_tree.cu`, `extra_significance.cu`, `decoding_all.cu` | 조상 OR·예측 refine·디코딩 순서 | LG2-036·038·045 |
| M `mra/decode_scale_children.cuh`, `decode_scale_coeffs.cuh`, `decoding.cu`, load/store/get_child helper | 평균/detail→자식 계수·지형 보존·모드/자식 번호 | LG2-029·030·038. load/store는 eta·qx·qy 세 변수의 각 모드에 대응한다. |
| M `mra/traverse_tree_of_sig_details.cu`, `reinsert_assem_sol.cu`, `insert_point_srcs.cu`, `reinsert_point_srcs.cu` | leaf 경로·H+z→eta·점 원천 최초/반복 삽입 | LG2-040·069·070 |
| M `zorder/*` | dilate/compact·Morton·행/열·좌표·순열 생성·필드 gather·역정렬·finest 저장 | LG2-043·044·047·087 |
| M `neighbours/find_neighbours.cu`, `get_compaction_flags.cu`, `compaction.cu`, `load_soln_and_nghbr_coeffs.cu` | 방향별 조상 이웃·NE/SW 선택·계층 계수→H/q/z 적재 | LG2-040~042·057 |
| M `neighbours/add_ghost_cells.cu`, Boundary·Boundaries·PointSources·StagePoints | 벽/실험/실제 경계·원천 시계열·공간 인덱스 | LG2-065~071·087·094 |
| M `operators/flux_HLL.cuh`, `get_bed_src.cuh`, `fv1_update.cu`, `dg2_update.cu` | 재구성·HLL·바닥 원천·FV/RK2·CFL 후보 | LG2-046~049·052·054·055 |
| M `operators/get_x/y_face_coord.cuh`, `get_x/y_face_unit.cuh`, `get_leg_basis.cuh`, `eval_loc_face_val_dg2.cuh` | 물리 면 좌표→이웃 셀 단위좌표→Legendre 면값 | LG2-047 |
| M `operators/apply_friction.cuh`, `friction_implicit.cu` | implicit 마찰·Gauss 상태·경사 복원 | LG2-050·051 |
| M `operators/minmod.cuh`, `get_limited_slopes.cuh`, `limit_slopes.cu` | 부호 검사·Krivo 지표·minmod·수면 경사 제한 | LG2-053 |
| M `operators/copy_to_buf_assem_sol.cu`, `get_dt_CFL.cu`, `non_reflective_wave.cuh` | RK 버퍼·전역 최소 dt·실험별 Newton 경계 상태 | LG2-054·055·090·094 |
| M `output/project_assem_sol.cu`, `write_all_raster_maps*.cu`, `write_stage_point_data.cu`, `write_soln_vtk.cu`, `write_c_prop_data.cu` | 평균 stage projection·DG2 모드 평가·HWFV1 상수 raster·VTK·c-property 자료 덤프 | LG2-084·086·087·093 |
| M `output/write_cumulative_data.cpp`, `write_mesh_info.cpp`, `write_raster_file.cu`, `write_*_to_file.cu`, `append_reals_to_file.cu` | 압축률·시간/격자 크기 기록·남북 행 뒤집기·진단 배열 저장 | LG2-084·090·091 |
| N·M `classes`/자료형·`cuda_utils`·allocator·`get_num_blocks`·BLOCK_VAR_MACROS와 `cuda/common/*` | 저장 공간·복사·오류/장치 검사·ceil launch 크기·정밀도 선택 | LG2-026·045·090~092·097. 부속 SDK 내부를 추가 해법으로 분석하지 않았다. |

`get_max_scale_coefficients`와 `get_max_scale_coeffs`의 이름은 서로 다르다.
이 보고서는 그 차이를 계산식 차이의 근거로 삼지 않는다.
필터·모드·호출 인자와 실제 배열을 기준으로 LG2-029~034를 판정했다.

## 3 코드에만 있는 처리

이 절은 한쪽 경로에만 있는 기능·옵션을 모은다.
인용 원문과 조건은 연결한 LG2 행에 둔다.
`있음`은 활성 호출까지 확인한 경우이다.

| 처리·옵션 | CPU ACC·SGC | 균일 GPU ACC | 비균일 GPU ACC | adaptive | 근거 행 |
|---|---|---|---|---|---|
| q-centred theta·역방향 보정 | ACC에 있음 | 있음 | theta=1 고정 | SWE 연산자 사용 | LG2-002·003·023·046 |
| 1D/2D 마찰 벡터 선택 | ACC에 있음 | 조도 존재 여부로 벡터 선택 | 횡방향 면 Q로 벡터 계산 | 별도 implicit 마찰 | LG2-004·024·050 |
| 공간 조도 | 있음 | 있음 | n0 인코딩·선택 있음 | 단일 fpfric | LG2-005·034·051 |
| ChanMask·routing·porosity·침투·증발 | 있음 | 대응 갱신 없음 | 대응 갱신 없음 | 대응 갱신 없음 | LG2-006·072 |
| SGC 단면·bankfull·사행·위경도 채널 폭 | SGC에 있음 | 없음 | 없음 | 없음 | LG2-013~022 |
| 유량 재시작 초기화 | CPU 초기화·선택적 hotstart | Qold 초기화 후보 | 면 Q를 0으로 초기화·체크포인트 복원 | 선택적 startq2d 읽기 | LG2-020·059·088·090 |
| HLL·Legendre·경사 제한·RK2 | 이번 CPU ACC에는 없음 | 없음 | 없음 | HWFV1/MWDG2별 있음 | LG2-046~055 |
| 지형의 다해상도 압축 | 없음 | 없음 | 초기 1회 | 지형 preflag + 유동 적응 | LG2-029~045 |
| extra significance·decode | 없음 | 없음 | 활성 시간 루프에 없음 | 있음 | LG2-038 |
| 경계·점·관측 preflag | 없음 | 없음 | 있음 | 있음 | LG2-037 |
| 북·동 벽 인접대 refine_wall | 없음 | 없음 | 없음 | 실제 지형에서 선택적 적용 | LG2-038 |
| topo grading | 없음 | 없음 | 없음 | MWDG2 topo 분기만 있음 | LG2-039 |
| 한 변의 복수 경계 구간 | 셀별 설정 | 셀별 설정 | 첫 구간만 읽음 | 첫 구간만 읽음 | LG2-067 |
| QFIX 면 경계 | 있음 | switch 없음 | 있음 | 수심 덮어쓰기 후보 | LG2-062·065 |
| NetCDF·균일 강우 | 있음 | 있음 | 있음 | 시간 루프 호출 없음 | LG2-073~080 |
| maxVx·maxVy·reset_timeinit | 있음 | 없음 | 대응 옵션 없음 | 대응 누적 없음 | LG2-010·012·083·084 |
| 최대 수심·침수 시간 | 매 단계 또는 선택적 MassInt | 같은 선택 조건 | MassInt에서만 | 대응 누적 없음 | LG2-011·083·084 |
| virtual gauge·overpass·steadycheck | CPU driver에 있음 | 같은 CPU 후처리로 이어지지 않음 | 같은 CPU 후처리로 이어지지 않음 | 별도 출력 경로 | LG2-072·092 |
| VTK leaf 출력 | 이 CPU ACC 경로에는 없음 | 없음 | H·z·scalar v·선택적 n | h·qx·qy·z·dt | LG2-086·089 |
| 23종 synthetic 초기 조건·실험별 파랑 경계 | 없음 | 없음 | 없음 | 있음 | LG2-093·094 |

수치 옵션이 구조체에 남아 있다는 사실과 해법이 그 옵션을 적용한다는 사실은 다르다.
예를 들어 U의 solver_params에는 routing과 RouteSfThresh가 있다.
U의 실제 유량 조건은 LG2-006처럼 주석이다.
예를 들어 N에는 write_raster_maps가 있다.
N의 정기 호출은 LG2-089처럼 주석이다.
예를 들어 M에는 초기 수심의 음수 절단 return이 있다.
그 return은 LG2-093처럼 앞 return 뒤에 있다.

이 보고서는 실행하지 않은 함수의 결과를 활성 해법의 결과로 보고하지 않는다.

## 4 노트 대조와 수정안

이 절의 인용 경로는 저장소 루트 기준이다.
이 절은 제안문만 작성한다.
현재 노트 파일은 변경하지 않았다.

### 4.1 모델 README와 아키텍처

`models/LISFLOOD-FP/README.md:11` 원문:

> - **버전**: **v8.2** (2024-07-29). **8.x 특징 = GPU multiwavelet DG2 + dynamic resolution adaptivity**(비균일격자 acc_nugrid).

수정안: 현재 위키 원자료는 공식 8.2에 공식 8.3 패치를 적용한 코드이다. `cuda/adaptive/`는 HWFV1·MWDG2의 동적 해상도 경로이다. `cuda/acc_nugrid/`는 초기 지형 detail로 비균일 격자를 구성하는 ACC 경로이다. N의 시간 루프는 격자를 갱신하지 않는다.

근거: LG2-035·092. `VersionHistory.h:23`의 원문은 `#define LF_Release "8.3"`이다. 배포 설명 `LISFLOOD-FP-8.3-package/README.md:3-5`는 다음과 같다.

> LISFLOOD-FP 8.2 with faster, reproducible CUDA solvers and a new GPU back end
> for Apple computers (Metal, FV1 solver). The numerical method of 8.2 is
> unchanged.

숫자 헤더 8.1.0과 출력 release 8.3은 서로 다른 용도이다. `VersionHistory.h:21-22`는 체크포인트 때문에 숫자를 유지했다고 적는다. 이 판 식별은 LG2-092의 범위 설명이다. 같은 판 CPU/GPU 차이를 판 차이 A로 분류하지 않는다.

`models/LISFLOOD-FP/README.md:29` 원문:

> | `cuda/` | **GPU(CUDA)** 버전: acc·fv1·fv2·dg2·acc_nugrid(Haar 적응 ACC)·**adaptive(★멀티웨이블릿 HWFV1/MWDG2)** |

수정안: acc_nugrid는 MW 필터로 지형을 인코딩하는 비균일 격자 ACC이다. adaptive는 Haar HWFV1과 multiwavelet MWDG2를 모두 포함한다. 근거: LG2-029~031·035.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:68` 원문:

> `cuda/{acc,fv1,dg2,acc_nugrid}/cuda_*_simulate.cuh` — 각 솔버의 GPU 구현. `acc_nugrid` = 비균일(non-uniform) 격자 ACC = **동적 해상도 적응**의 GPU 경로.

수정안: 균일 ACC와 비균일 ACC는 국소 관성 유량식을 사용한다. acc_nugrid는 초기 격자를 유지한다. adaptive의 HWFV1·MWDG2는 시간 루프에서 유동 detail에 따라 격자를 갱신한다. 같은 노트 `:28`, `:39`, `:86`의 acc_nugrid 동적 해상도 표기도 같은 기준으로 바꾼다. 근거: LG2-023·035·046·092.

### 4.2 CUDA 노트

`models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:17` 원문:

> LISFLOOD-FP 의 GPU 경로(`cuda/`)는 천수방정식(SWE)을 **FV1(1차 유한체적 HLL Godunov)** 으로 푸는 정식 2D 솔버다. CPU 의 ACC(국소 관성) 솔버와 달리, GPU 경로는 보존형 SWE 를 HLL Riemann flux 로 직접 적분한다. 솔버 패밀리는 4종으로 분기한다:

수정안: 이 노트의 FV1 경로는 보존형 SWE를 HLL 플럭스로 적분한다. CUDA ACC와 acc_nugrid는 국소 관성 유량식을 사용한다. adaptive의 HWFV1·MWDG2도 별도 실행 분기이다. GPU 전체를 FV1·HLL 하나로 설명하지 않는다. 근거: LG2-002·023·046·048·092.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:142` 원문:

> `DynamicTimestepACC` 는 ghost 없는 `elements_H` 크기로 동일 동작(ACC 경로, `:42-71`, `:87-97`).

수정안: DynamicTimestepACC는 elements_H 크기의 dt_field를 별도로 할당한다. 활성 update_dt_ACC는 adaptive 값을 검사하지 않는다. 습윤 셀의 후보는 이전 dt_field와 최소값을 취한다. dt_field의 최초 초기화는 확인되지 않는다. 최초값과 후보 유지 방식은 LG2-008의 결함 후보이다. 근거: LG2-008·055.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:174` 원문:

> `update_H` 커널 (`cuda_boundary.cu:219-265`, ACC 경로): flux 발산으로 $\Delta V=\Delta t(q_{x0}-q_{x1}+q_{y0}-q_{y1})$, 음수 깊이 방지 `WDweight` 부분 flux 스케일링(`drycheck`) (`:247-257`) 후 $H\mathrel{+}=\Delta V/\Delta x^2$, 음수는 0 클램프 (`:259-261`).

수정안: GPU ACC update_H는 네 면 유량을 지역 변수로 복사한다. drycheck는 이 복사본의 외향 유량을 줄인다. 함수는 보정 유량을 공유 Qx·Qy에 저장하지 않는다. 이웃 셀과 Qold 갱신에 보정이 전달되지 않는 결함 후보를 구분한다. 근거: LG2-060.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:213` 원문:

> `cuda/acc_nugrid/` 는 ACC 솔버를 **Haar wavelet 기반 적응 격자**로 확장한 별도 파이프라인이다 (`cuda_acc_nugrid_simulate.cu`). 일반 FV1 의 균일 raster 와 달리:

`models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:215` 원문:

> - **scale/detail 계수** wavelet 분해 후 `preflag_topo`/`encode_and_thresh_topo` 로 유의(detail) 임계화하여 활성 셀만 유지 — 동적 해상도 (`get_max_scale_coefficients.cuh`, `traverse_tree_of_sig_details.cu`).

수정안: acc_nugrid의 활성 scale/detail 함수는 HH·GA·GB·GC 3×3 필터를 사용한다. Haar 대안은 주석이다. 지형 detail과 경계·원천·관측 preflag가 초기 격자를 정한다. 조도·시작 수심 detail은 계산되지만 threshold의 최대값에는 들어가지 않는다. 시간 루프는 구성한 격자에서 compute_q와 update_h를 반복한다. 근거: LG2-029~035·037.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:229` 원문:

> - 4개 솔버 패밀리(fv1/dg2/acc/acc_nugrid)가 동일 HLL/boundary/ghostraster 인프라 공유, acc_nugrid 는 Morton+wavelet 동적해상도 별도 파이프라인.

수정안: CUDA 해법은 일부 장치 보조 함수를 공유한다. ACC는 HLL을 호출하지 않는다. ACC의 면 경계는 fv1/dg2의 ghost 상태 함수와 다르다. acc_nugrid와 adaptive는 이웃·경계·출력도 별도로 구현한다. 근거: LG2-046~048·057·062~068·081~089·091.

### 4.3 adaptive 노트

`models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:24` 원문:

> - 자식 번호는 논문 Fig 2 대비 **상하 flip**(원점 top-left, `:101-114`).

수정안: driver의 모식도 주석과 실제 물리 좌표를 구분한다. 실제 노드는 xmin·ymin에서 증가한다. Morton 코드는 x 비트와 y 비트를 교차한다. 실제 지형 reader는 ASCII 북쪽 행을 남쪽 기준 배열로 뒤집는다. 모식도 주석만으로 물리 원점을 top-left라고 쓰지 않는다. 근거: LG2-043·093과 `M/mra/init_nodal_values.cu:53-54`.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:45` 원문:

> 경계·point source·stage 셀 및 (`refine_wall` 시) 벽 인접대는 **영구 preflag** — 항상 finest 유지(`mra/preflag_details.cu:24-88`, `refine_high_wall.cu`).

수정안: 지정 경계·점 원천·관측 셀은 preflag를 갖는다. 실제 지형에서 refine_wall은 북쪽과 동쪽 인접대만 추가한다. 이 처리를 네 방향 전체 벽의 refine이라고 쓰지 않는다. 근거: LG2-037·038. topo grading의 좌표 상한 후보는 별도로 LG2-039에 연결한다.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:48` 원문:

> - **★`maxes.qy` copy-paste 버그**: detail 정규화 분모 qy 최대값을 **`qx0` 배열로 계산**(`mra/get_max_scale_coeffs.cu:23` — `maxes.qy = get_max_from_array(d_assem_sol.qx0, …)`). max|qx|≫max|qy| 인 흐름에서 qy detail 이 과소 정규화 → y-방향 특징 **과소-refine** 가능. v8.2 Zenodo 정본 기준 미수정.

수정안: maxes.qy는 qx0 배열의 최대값을 읽는다. qy detail의 분모와 입력 배열이 불일치한다. 8.3 적용본도 이 행을 그대로 둔다. 분모 하한 1에 걸리지 않고 max|qx|가 max|qy|보다 크면 qy detail의 정규화값이 작아질 수 있다. 이 보고서는 실제 격자 오차를 실행으로 검증하지 않았다. 근거: LG2-033. v8.2와 해당 파일의 byte 비교도 같았다.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:49` 원문:

> - **정규화 분모 하한 1.0 클램프**: `max(*h_max_out, C(1.0))`(`mra/get_max_from_array.cu:56`) — max|q|<1, max|z|<1 인 **실험실 스케일에서 상대 임계가 사실상 절대 임계로 전환**(스케일 비불변). 소규모 벤치마크에서 ε 재보정 필요.

수정안: M은 absmax와 1 중 큰 값을 정규화 분모로 쓴다. N의 z 분모는 signed max와 1 중 큰 값이다. M의 해당 return은 get_max_from_array.cu:57이다. 이 코드 판독만으로 특정 실험의 epsilon 재보정을 의무로 권고하지 않는다. 근거: LG2-032·034. 실험 권고의 타당성은 H이다.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:55` 원문:

> - **별도 미니앱 성격**: `simulation.run(argc, argv)` 가 parfile 을 **자체 키워드로 재파싱**(`max_ref_lvl`·`epsilon`·`hwfv1/mwdg2`·`grading`·`limitslopes`·`tol_Krivo`·`refine_wall`·`ref_thickness`·`startq2d`, `SolverParams.h:33-72`) — 본체 파서(input.cpp)의 State 를 사실상 무시. 합성 테스트 22종 내장(`cuda_adaptive_simulate.cu:59-87`), `monai.dem`·`oregon-seaside-0p02m.dem` 파일명 하드코딩 특례(`SimulationParams.h:58-59`).

수정안: adaptive는 별도 생성자로 매개변수를 읽는다. 실제 synthetic selector는 1~23이다. test_case 0은 실제 지형 입력이다. Monai·Oregon 분기는 파일 이름을 검사한다. 실제 검사 행은 SimulationParams.h:59-60이다. 근거: LG2-056·092~094.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:64` 원문:

> - [[lisflood-fp-cuda-gpu]] — GPU 공통 인프라·acc_nugrid(Haar 적응 ACC, 본 노트와 별개 파이프라인)

수정안: 관련 링크 설명을 “GPU 공통 인프라·acc_nugrid의 초기 지형 기반 비균일 ACC”로 바꾼다. N의 활성 MW scale/detail과 M의 MW scale/detail은 계수 배치를 대조할 수 있다. N의 필터에 들어간 0.5와 M의 식 끝 `/ C(2.0)`는 같은 정규화이다. 근거: LG2-029~031·035.

추가안: adaptive 노트에 LG2-039·045·065·068·070·087의 조건부 결함 후보를 추가한다. 경계 Q 수심 덮어쓰기와 qy 정규화 입력 오류는 별도 항목으로 쓴다. stage 출력은 leaf 평균을 복제한다는 사실을 추가한다. 근거: LG2-033·065·086.

### 4.4 CPU ACC·SGC·외력 노트

`models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:20` 원문:

> | **SGC** (Sub-Grid Channel, Neal) | `sgc.cpp`, `weir_flow.cpp`(bridge) | 격자 내부 sub-grid 단면 | 같은 2D 셀에 하도+범람원 공존 | 현행 주력 |

수정안: SGC 형상·초기화는 sgc.cpp에 있다. 기본 시간 루프는 lisflood2의 Fast_MainStart로 진입한다. sgc.cpp의 옛 유량·H·BC 갱신은 RESULT_CHECK 참조 경로이다. 같은 노트 :72의 RESULT_CHECK 설명은 유지한다. 근거: §2.2의 entry 인용과 LG2-018·019·092.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:52` 원문:

> (`sgc.cpp:114-117`). 무차원 깊이 `hp = 2h/wbf` (반폭 기준, `:246`)에 대해 임계 `SGCbetahmin`(=0.05, lisflood.h:478) 아래는 β1·β2, 위는 β3·β4를 쓰고 `SGCbeta5`(임계점 wetted-perimeter 분율 `:119`)로 이어붙인다 (`:248-260`).

수정안: SGCbetahmin의 실제 초기 대입은 `lisflood.cpp:278`의 `SGCchanprams.SGCbetahmin = C(0.2);`이다. lisflood.h:478은 값 없는 필드 선언이다. sgc.cpp:250·256·258의 0.05 주석과 실제 대입값을 구분한다. beta 구간의 실제 조건은 `sgc.cpp:248`의 `if (hp <= SGCptr->SGCbetahmin)`이다. 이 수정은 LG2-015의 형상 설명에 포함한다. 외부 회귀계수 자체의 옳고 그름을 판정한 수정이 아니다.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:106` 원문:

> - **hotstart** `SGC_hotstart` (`:563-724`): 수면으로부터 초기 Q를 정상류 망닝식 `q = h^(5/3)·Sf/fn·min(w0,w1)` 로 추정 (SGC `:601`, FP `:629`). Sf는 `√(dh/dx)` (kinematic 형태).

수정안: 정방향 SGC hotstart는 최소 채널 폭을 곱한다. 역방향 x·y 식은 그 폭을 곱하지 않는다. 단위와 방향 대칭에 어긋나는 결함 후보이다. 이 함수는 startq와 SGC가 켜진 초기화에서 호출된다. 근거: LG2-020. 옛 y 방향 qc 미설정과 사각 셀 폭 후보는 RESULT_CHECK 범위를 명시해 별도로 추가한다. 근거: LG2-018·019.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow.md:126` 원문:

> - `MH<DepthThresh` 면 `Tstep=InitTstep` (:276). h가 분모이므로 마른 격자 회피(주석 :250).

수정안: `fp_acc.cpp:250`의 실제 조건은 `if(MH>Solverptr->DepthThresh)`이다. 해석: 이 else는 최대 수심이 건조 임계값 이하인 경우이다. 코드 조건을 그대로 인용해 등호를 빠뜨리지 않는다. CPU의 단계별 초기 상한 복원과 U의 dt_field 후보 이력 차이를 덧붙인다. 근거: LG2-008.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:145` 원문:

> 라우팅 OFF일 때만 호출(주석 infevap.cpp:88-89). 도메인 균일 시변율(`InterpolateTimeSeries(rain,t)`), NODATA 표고 셀 제외(`DEM != nodata_elevation`, infevap.cpp:108), `RainTotalLoss` 적산. OpenMP 병렬(infevap.cpp:99). rain 파일은 mm/hr → m/s 환산(input.cpp LoadRain). evap·rain 시계열은 첫 줄 skip(`LoadTimeSeries(..., ON)`).

수정안: 이 문장의 적용 범위를 CPU Rainfall로 명시한다. CPU DynamicRain도 실제 단계 dt와 셀 면적으로 강우 체적을 누적한다. U·N 강우의 dt 순서와 질량 장부는 별개이다. GPU 균일 강우 reader의 분·시간 구간 전진 결함 후보를 덧붙인다. 근거: LG2-073~078·096.

`models/LISFLOOD-FP/source-analysis/lisflood-fp-lisflood2-driver.md:100` 원문:

> 2. **overlapped single** (`#pragma omp single nowait`, `:3678`): reduction 변수 0화, point source TimeSeries 선보간, `SGC2_BCs`(경계 Q+sub-grid vol, `:3714`), evap/rain deltaH 계산.

판정: 이 설명은 기본 Fast_MainStart 경로의 설명이다. 이 문장을 sgc.cpp의 RESULT_CHECK 갱신과 합치지 않는다. 수정안은 channel-sgc의 entry 구분을 이 노트에 연결하는 것이다. 이번 보고서는 lisflood2의 모든 최적화 수식을 다시 감사하지 않았다.

추가안: CUDA 노트의 출력 절에 LG2-028·081~089를 추가한다. `.mass` 파일의 존재와 질량 수지의 완전성은 별도 사실로 쓴다. `.Qx/.Qy`는 배열 이름과 단위를 함께 쓴다. stage 평균값과 raster의 DG2 평가값도 구분한다.

## 5 차이 결론

분류별 개수: C 28, E 25, F 5, H 26, X 0. 차이 행은 84개이다. 같음 행은 14개이다.

분류는 §2의 고유 행 ID를 기준으로 한다.
하나의 행에 하나의 결론만 부여했다.
C는 설명되지 않은 계산·옵션·진단의 차이이다.
E는 정적 코드 결함 후보이다.
F는 대응 조건에서 같은 식·연산을 다른 표기로 쓴 경우이다.
H는 서로 같은 계산의 이식 결과로 판정할 대상이 없는 해법 모형·테스트 정의·상태 전송·장치 처리이다.
H도 §2의 계산 항목 대조와 루틴 목록에는 포함했다.
외부 논문 식을 읽어야만 결정할 값은 이 보고서의 내부 식 대조에 남지 않았다.
외부 실험의 재현성·성능·회귀계수의 적합도는 H이다.

E 판정 전에 기본 매크로·호출 순서·후속 보정·비활성 경로·8.3 패치를 확인했다.
RESULT_CHECK의 옛 SGC 후보와 기본 활성 초기화 후보를 구분했다.
정방형 셀·0인 좌표 원점·초 단위 시계열처럼 차이를 가리는 조건을 각 행에 적었다.
8.3 패치 `LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:79`, `:87`은 `if (Hold == C(0.0)) continue; // dry: nothing to add to the mass balance`를 추가한다.
그 패치는 nodata 질량 카운터 호출을 건너뛴다.
그 패치는 LG2-060의 유량 복사본이나 LG2-008의 dt_field를 고치지 않는다.
같은 패치 `:56`, `:68`은 adaptive의 sync 이름을 sync_device로 바꾼다.
이 이름 변경은 MRA 필터·인덱스·경계식을 바꾸지 않는다.
후보 관련 원문 파일과 Zenodo v8.2 압축 해제본의 byte 대조는 같은 파일임을 확인했다.
공통 cuda_boundary.cu는 nodata 패치 때문에 다르다.
그 파일의 update_H 계산 블록은 패치 대상이 아니다.
따라서 아래 E는 8.3에서 고쳤다고 보고하는 8.2 결함이 아니다.

문서 설명 검색은 원본 README.md·INSTALL.md·VersionHistory.h와 매뉴얼 세 텍스트 추출본을 대상으로 했다.
`rg -i 'acc_nugrid|mwdg2|hwfv1|Haar|compaction'`은 세 매뉴얼 추출본에서 일치 행을 찾지 못했다.
원본 README.md:64는 FV1·DG2 CUDA 빌드를 설명한다.
VersionHistory.h:45는 CPU의 1Dfriction 선택을 설명한다.
이 두 설명은 GPU ACC의 해당 옵션 생략을 설명하지 않는다.
C 행은 표의 차이를 설명하는 별도 지원 제한을 찾지 못한 경우이다.
기존 위키 노트의 추정은 원본 코드의 의도 변경 주석으로 취급하지 않았다.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| LG2-004 | 1D/2D 마찰 선택 | C | CPU `fp_acc.cpp:45` `if(Solverptr->fricSolver2D==ON){`. U `U/cuda_acc_solver.cu:954` `friction = (physical_params.manning > C(0.0)) \|\| (manning != nullptr);`. | U는 CPU fricSolver2D 옵션 대신 조도 존재 여부로 벡터 마찰을 선택한다. |
| LG2-006 | mask·routing | C | U `U/cuda_acc_solver.cu:718` `if ( /*MaskTest(U.ChanMask[p0], U.ChanMask[p1]) && */ hflow > cuda::solver_params.DepthThresh)`. CPU 조건은 `fp_acc.cpp:83-85`에 있다. | U는 CPU의 채널 마스크와 routing 유량 조건을 적용하지 않는다. |
| LG2-008 | dt_field 초기화·이력 | E · 강함 | 반대 근거: 건조 셀은 max_dt로 다시 설정한다. CPU `iterateq.cpp:144` `if (Solverptr->t>C(0.0)) Solverptr->Tstep = Solverptr->InitTstep;`. U `U/cuda_acc_solver.cu:125` `dt[j * cuda::pitch + i] = getmin(dt_, dt[j * cuda::pitch + i]);`. 할당 `cuda/cuda_util.cu:63`은 `checkCudaErrors(cudaMalloc(&ptr, size));`이다. 최초 읽기 전 초기화와 매 단계 상한 복원이 없다. | U dt_field의 최초 읽기와 과거 최소값 유지 방식은 CPU CFL 갱신과 다른 결함 후보이다. |
| LG2-010 | 최대 유속 | C | CPU `fp_acc.cpp:106` `Arrptr->maxVx[pq0]=getmax(Arrptr->maxVx[pq0],fabs(Arrptr->Vx[pq0]));`. U `U/cuda_acc_flow.cuh:28-29`는 Vx·Vy만 선언한다. | U는 순간 면 유속을 계산하지만 CPU의 최대 면 유속을 누적하지 않는다. |
| LG2-012 | initHtm 재설정 | C | CPU `iterateq.cpp:177` `if ((Statesptr->reset_timeinit == ON) & (Solverptr->t>Parptr->reset_timeinit_time))`. U `U/cuda_acc_simulate.cu:233`은 같은 조건을 주석으로 둔다. | U는 reset_timeinit 블록을 실행하지 않는다. |
| LG2-013 | SGC 내부 채널 형상 | H | `sgc.cpp:449` `Arrptr->SGCbfH[p0] = Arrptr->DEM[p0] - Arrptr->SGCz[p0]; // Calculate SGC bank full depth`. N `N/update_h.cu:86` `NUMERIC_TYPE cv = H * (dx * dx);`. | SGC의 셀 내부 채널과 N의 비균일 계산 셀은 다른 격자 개념이다. |
| LG2-014 | SGC 체적 역변환 | F | `sgc.cpp:204` `v = c*pow(h, C(1.0) / sl + C(1.0));`. `:1671` `h = pow(V / c, sl / (sl + C(1.0)));`. | SGC 수심·체적 변환의 지수는 서로 역수이다. |
| LG2-015 | SGC 단면·반경·beta | H | `sgc.cpp:241` `R = A / (w + 2 * R); // calculate hydraulic radius`. 실제 접속 임계값은 `lisflood.cpp:278`의 `SGCchanprams.SGCbetahmin = C(0.2);`이다. | SGC 형상 함수는 ACC 통수심과 다른 채널 모형 계산이다. |
| LG2-016 | h의 마찰 지수 | F | `sgc.cpp:880`의 전체 식과 `fp_acc.cpp:94`의 전체 식은 §2.2에 인용했다. `hflow/hflow^(10/3)=1/hflow^(7/3)`은 해석용 식 변형이다. | theta=1·qvect=q0 조건에서 두 마찰 분모는 같은 식이다. |
| LG2-017 | 채널·범람원 합산 | H | `sgc.cpp:896` `Q = Qc + Q;`. 채널 갱신의 A·R은 `sgc.cpp:844`의 전체 식에 있다. | SGC는 채널 유량과 남은 범람원 폭의 유량을 합한다. |
| LG2-018 | 옛 SGC y qc | E · 강함 | 반대 근거: `sgc.cpp:726` `#ifdef RESULT_CHECK`. x는 `:826` `qc = Arrptr->QxSGold[pq0]; // Get old q in m3/s`. y는 `:942` `Qc = Arrptr->QySGold[pq0]; // Get old q in m3/s`. `:961`, `:969`는 설정하지 않은 별도 qc를 읽는다. | RESULT_CHECK의 옛 y SGC 유량식은 qc 미설정 결함 후보이다. |
| LG2-019 | 옛 SGC 사각 셀 폭 | E · 강함 | 반대 근거: 정방형에서는 dx=dy이고 기본 빌드는 RESULT_CHECK를 끈다. `sgc.cpp:862` `if (we < Arrptr->dy[p0]) // CCS dy[p0] for cell width relative to flow in x`. `:882` `Q = Arrptr->Qxold[pq0] * (Arrptr->dx[p0] - we);`. 경계 `:1403` `Qfp = (*qoldptr) * (cell_width - w0);`. | 옛 SGC는 사각 셀에서 횡단 폭 검사와 유량 환산 폭이 달라지는 결함 후보이다. |
| LG2-020 | SGC 역방향 hotstart 폭 | E · 강함 | 반대 근거: startq와 SGC를 함께 켤 때만 호출한다. `sgc.cpp:601`은 최소 폭을 곱한다. `:612` `Arrptr->QxSGold[pq0] = (-pow(hflow, (C(5.0) / C(3.0)))*Sf / fn);`. y도 `:679`, `:690`에서 비대칭이다. `:826`의 원문 단위는 `// Get old q in m3/s`이다. | SGC 역방향 hotstart는 체적 유량에 필요한 채널 폭을 생략한 결함 후보이다. |
| LG2-021 | SGC 체적·경계 | H | `sgc.cpp:1097` `Arrptr->SGCVol[p0] += dV; // Add dV to Vol. This is now the total volume.`. N `N/update_h.cu:197` `H += dV / (dx * dx);`. | SGC는 bankfull 형상에 따른 체적 역변환과 채널 경계를 사용한다. |
| LG2-022 | SGC 원천·routing | H | `sgc.cpp:1544` `Arrptr->SGCdVol[p0] += V; // add rainfall volume to cell`. `:1645-1646`의 두 체적 이동 행은 §2.2에 인용했다. | SGC 원천은 채널 형상의 체적 장부에서 처리한다. |
| LG2-023 | theta 옵션 | C | N `N/compute_q.cu:29` `theta = C(1.0);`. U `U/cuda_acc_solver.cu:723`은 theta·qup·qdown을 사용한다. | N은 q-centred theta를 1로 고정한다. |
| LG2-024 | 비균일 거리·횡방향 평균 | C | N `N/compute_q.cu:216` `q_opp_avg = q_opp / d_non_uniform_nghbrs.dx_sum[idx];`. `:228` `Sf = -dh / length; // (C(0.5)* (dx_owner + dx_nghbr));`. | N은 이웃 셀 폭을 경사 길이로 쓰고 횡방향 체적 유량을 폭 합으로 나눈다. |
| LG2-025 | 통수심 상한 옵션 | C | N `N/compute_q.cu:232-233` `MaxHflow = C(10.0);` / `hflow = FMIN(hflow, MaxHflow);`. CPU `fp_acc.cpp:68`은 Solverptr->MaxHflow를 사용한다. | N은 MaxHflow 옵션 대신 10을 사용한다. |
| LG2-026 | CFL 초과 스레드 | E · 중간 | 반대 근거: 배열 용량이 활성 길이보다 클 수 있고 reduction은 활성 길이만 사용한다. N `N/calculate_dt.cu:19` `if (idx < d_assem_sol.length)`는 `:22` 초기 대입만 감싼다. `:29` `NUMERIC_TYPE h = d_assem_sol.h[idx];`는 조건 밖이다. 호출 `N/cuda_acc_nugrid_simulate.cu:285`는 올림 블록 수이다. | N CFL 커널은 활성 길이 밖 스레드의 배열 읽기를 막지 않는 결함 후보이다. |
| LG2-027 | 건조 보정 옵션 | C | CPU `iterateq.cpp:150` `if (Statesptr->drychecking == ON) DryCheck(Parptr, Solverptr, Arrptr);`. N `N/update_h.cu:104` `NUMERIC_TYPE WDweight = -cv / dV; // C(0.5) for improved drying stability`. | N은 drychecking 선택과 별도로 유출 체적 제한을 실행한다. |
| LG2-028 | 0인 질량 출력 인자 | C | N `N/cuda_acc_nugrid_simulate.cu:633-642`는 열 인자를 모두 0으로 전달한다. `N/write_mass_data.cu:11-20`의 인자 이름은 FArea·vol2·Qin·Hds·Qout·Qerror·Verror·강우·침투·증발이다. | N의 mass 파일 수리 열은 계산 결과가 아니라 0인 호출 인자이다. |
| LG2-029 | scale 정규화 | F | N `N/maskFilterHaar.h:31` `#define HH0_11 C(0.5) * ( C(1.0) / C(2.0) )`. M `M/mra/Filters.h:10` `#define HH0_11 ( C(1.0) / C(2.0) )`. M의 합산 뒤 나눗셈까지 §2.4에서 대조했다. | N 필터의 0.5와 M 식 끝의 2로 나누기는 같은 scale 정규화이다. |
| LG2-030 | detail 정규화 | F | N `N/encode_details.cuh:169-172`와 M `M/mra/encode_details.cuh:80-83`의 전체 식은 §2.4에 있다. 대응 필터 값과 자식·모드의 12항이 같다. | N과 M의 아홉 MW detail 식은 같은 변환이다. |
| LG2-031 | Haar 분기 | H | M `M/mra/Filters.h:5` `#define H0  C(1.0) / sqrt( C(2.0) )`. N `N/encode_scale.cuh:15-50`의 Haar 대안은 주석이다. | Haar는 M의 HWFV1 분기이며 N의 활성 인코딩 이름이 아니다. |
| LG2-032 | signed max·absmax | C | N `N/get_max_scale_coefficients.cu:108-115`은 z0에 CUB Max를 적용한다. `:124` `maxes.z = FMAX( *h_max_out, C(1.0) );`. M `M/mra/get_max_from_array.cu:57` `real max_from_array = max( *h_max_out, C(1.0) );`의 입력은 abs iterator이다. | N의 지형 정규화와 M의 지형 정규화는 음수 지형에서 다를 수 있다. |
| LG2-033 | maxes.qy 입력 | E · 강함 | 반대 근거: 두 최대값이 같거나 하한 1에 걸리면 차이가 가려진다. M `M/mra/get_max_scale_coeffs.cu:23` `maxes.qy  = get_max_from_array(d_assem_sol.qx0, d_assem_sol.length);`. `M/classes/Detail.h:46` `real qy_norm  =  qy.get_max() / maxes.qy;`. qx 대입도 `:22`에서 qx0을 사용한다. | M의 qy detail 분모는 qy0 대신 qx0을 읽는 결함 후보이다. |
| LG2-034 | n·H detail 선택 | C | N `N/encode_and_thresh_topo.cu:193` `if ((z_details.get_max() / maxes.z) >= epsilon_local) {`. n·h scale 저장은 같은 파일 `:132`, `:187`이다. M detail은 eta·qx·qy를 정규화한다. | N의 n·H detail은 격자 threshold에 반영되지 않는다. |
| LG2-035 | 초기 격자와 동적 격자 | C | N `N/cuda_acc_nugrid_simulate.cu:217` `preflag_topo /// flag cells with significant topography detail`은 루프 밖이다. M `M/cuda_adaptive_simulate.cu:479` `if (solver_params.epsilon > C(0.0) \|\| first_t_step)`는 루프 안이다. | N은 초기 비균일 격자를 유지하고 M은 유동 detail로 격자를 갱신한다. |
| LG2-038 | 예측 refine·decode·벽 | H | M `M/mra/extra_significance.cuh:4` `#define M_BAR C(1.5)`. 추가 임계 식 전체는 §2.4에 있다. N 시간 루프에는 역변환이 없다. | M의 추가 significance와 decode는 adaptive 다해상도 알고리즘의 별도 단계이다. |
| LG2-039 | grading 상한 | E · 강함 | 반대 근거: grading이 켜진 MWDG2 지형 분기만 해당한다. M `M/mra/encode_and_thresh_topo.cu:96` `if ( (i > 0 && i < sim_params.xsz) && (j > 0 && j < sim_params.ysz) ) {`. `:99` `Coordinate i_e = i + 1;`. `:114`는 curr_lvl_idx에 e_idx를 더한다. level 좌표와 finest 상한이 다르다. | M topo grading은 현재 수준 바깥의 이웃을 표시할 수 있는 결함 후보이다. |
| LG2-040 | leaf 순회 표기 | F | N `N/traverse_tree_of_sig_details.cu:57`의 접두 비트 검사와 M `M/mra/traverse_tree_of_sig_details.cu:43`의 접두 비트 추출은 §2.4에 인용했다. | 두 순회는 첫 insignificant 조상을 같은 Morton 경로에서 찾는다. |
| LG2-042 | compaction 필드 | H | N `N/compaction.cu:111` `if (startfile) {`. M `M/neighbours/compaction.cu:134-137`은 south 인덱스와 south_west flag를 전달한다. 실제 필드·flag 인자 묶음은 §2.4에 있다. | N은 초기 계수를 선택하고 M은 선택한 인덱스로 트리 계수를 다시 읽는다. |
| LG2-045 | 작은 L | E · 강함 | 반대 근거: 기본 block 매크로가 정한 수준보다 충분히 큰 L에서는 이 후보가 드러나지 않는다. N `N/BLOCK_VAR_MACROS.cuh:13` `#define LVL_SINGLE_BLOCK 4`. M `M/mra/get_reg_tree.cu:27` `int num_threads  = 1 << (2 * LVL_SINGLE_BLOCK);`. 실제 detail 길이는 get_lvl_idx(L)이다. N·M wrapper 모두 L을 clamp하지 않는다. | 기본 block 설정의 L≤4는 고정 level 4 detail 접근과 맞지 않는 결함 후보이다. |
| LG2-046 | SWE 운동량 이류 | H | M `M/classes/FlowVector.h:63` `return { qx, qx * qx / h + g * h * h / C(2.0), qx * qy / h };`. ACC 전체 식은 LG2-002에 인용했다. | M의 보존형 SWE와 ACC 국소 관성식은 서로 다른 지배식 근사이다. |
| LG2-047 | 재구성·면 평가 | H | M `M/classes/FlowVector.h:32` `return max(C(0.0), eta - z_intermediate);`. `M/operators/eval_loc_face_val_dg2.cuh:14` `return s._0 * basis._0 + s._1x * basis._1x + s._1y * basis._1y;`. | MWDG2는 세 Legendre 모드로 면값을 재구성한다. |
| LG2-048 | HLL | H | M `M/operators/flux_HLL.cuh:80` `F.qy = ( s_neg < C(0.0) && s_mid >= C(0.0) ) ? F.h * v_neg : F.h * v_pos;`. 전체 중간 플럭스는 §2.5에 있다. | M은 HLL 플럭스를 사용하며 ACC는 직접 관성 유량식을 사용한다. |
| LG2-049 | 바닥 원천 | H | M `M/operators/get_bed_src.cuh:24` `return g * C(0.5) * (h_star_w_pos + h_star_e_neg) * (z_star_e - z_star_w) / dx_loc;`. DG 모드 원천은 같은 파일 `:68-69`, `:95-96`이다. | FV와 DG의 원천 항 부호는 각 갱신식의 더하기·빼기와 함께 읽어야 한다. |
| LG2-050 | 별도 implicit 마찰 | H | M `M/operators/apply_friction.cuh:48` `real D_x = C(1.0) + dt * Cf / h * (C(2.0) * ux * ux + uy * uy) / speed;`. 원천·분모·증분 전체는 §2.5에 있다. | M은 평균·Gauss 상태의 별도 마찰 적분을 사용한다. |
| LG2-051 | M 공간 조도 생략 | C | M `M/classes/SimulationParams.h:58` `this->manning = read_keyword_real(input_filename, "fpfric", 6);`. N `N/compute_q.cu:136` `Manning = C(0.5) * (n_owner + n_nghbr);`. | M의 활성 마찰은 단일 fpfric이며 U·N의 공간 조도 입력을 적용하지 않는다. |
| LG2-052 | 건조 운동량 처리 | H | M `M/operators/dg2_update.cu:336` `const bool below_depth = (h0 < solver_params.tol_h);`. N `N/update_h.cu:198` `if (H < C(0.0)) H = C(0.0);`. | M은 건조 평균의 운동량 모드를 0으로 만들며 ACC와 같은 H 절단 블록은 사용하지 않는다. |
| LG2-053 | slope limiter | H | M `M/operators/limit_slopes.cu:23` `if (level == solver_params.L)`. `:216-217`의 전체 습윤 조건은 §2.5에 있다. | MWDG2의 선택적 제한 함수는 finest 수준의 습윤 stencil에만 적용된다. |
| LG2-054 | RK2 | H | M `M/operators/dg2_update.cu:326` `h0   = (rkdg2) ? C(0.5) * (coeffs.h._0   + h0  ) : coeffs.h._0  ;`. | MWDG2는 두 RK 단계와 이웃용 중간 인코딩을 사용한다. |
| LG2-055 | SWE CFL | H | M `M/operators/dg2_update.cu:354` `real dt_x = solver_params.CFL * dx_loc / ( abs(ux) + sqrt(sim_params.g * h0) );`. CPU `fp_acc.cpp:271` `locT=cfl*Parptr->dx/(sqrt(g*MH));`. | SWE CFL은 이류 속도를 포함하고 ACC CFL은 중력 파속을 사용한다. |
| LG2-056 | M 허용값·CFL 옵션 | C | M `M/classes/SolverParams.h:15-17`의 기본 허용값과 `:41`, `:46`의 CFL 대입은 §2.5에 인용했다. `:33-70`의 생성자에는 이 허용값을 읽는 호출이 없다. | M은 tol_h·tol_q·tol_s와 해법별 CFL을 고정한다. |
| LG2-057 | 이웃 표현 | H | M `M/neighbours/find_neighbours.cu:118` `d_neighbours.north.levels[idx] = min(lvl_local, lvl_north);`. N `N/find_nonuniform_neighbours.cu:59` `if (!already_in_list \|\| (bc_bound && at_border))`. | N의 가변 면 목록과 M의 방향별 조상 계수는 다른 이웃 표현이다. |
| LG2-058 | 이웃 count·fill 상한 | E · 강함 | 반대 근거: 실제 영역이 정방형 전체와 같으면 두 조건이 같아진다. N `N/count_neighbours.cu:41` `bool at_border = (y_ne == (pars.ysz - 1));`. `N/find_nonuniform_neighbours.cu:45` `bool at_border = ( y_ne == (pars.ysz - 1) \|\| ( y_ne == (mesh_dim - 1) ) );`. padding의 북·동 바깥은 count에서 유효 이웃 인덱스가 아니다. | N의 count·fill 경계 불일치는 padding 영역의 범위 밖 읽기 후보이다. |
| LG2-059 | 최초 H·Qold·maxH | E · 강함 | 반대 근거: startfile은 H를 읽고 checkpoint는 H·Q·maxH를 복원한다. CPU `input.cpp:1414` `Arrptr->Qxold = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));`. U `U/cuda_acc_flow.cu:69` `cuda::GhostRaster::copy_Q(dst.Qxold, src.Qxold, geometry);`. U의 할당은 `cuda/cuda_util.cu:53` `checkCudaErrors(cudaMallocHost(&ptr, size));`이다. Qold 초기 대입과 비-startfile H 대입이 없다. | U는 설정하지 않은 최초 H·Qold·maxH를 사용할 수 있는 결함 후보이다. |
| LG2-060 | 지역 건조 유량 | E · 강함 | 반대 근거: drycheck가 꺼지거나 cv+dV가 음수가 아니면 이 차이는 없다. GPU `cuda/cuda_boundary.cu:237`은 Qx를 값으로 복사한다. `:252` `if (qxptr0 < C(0.0)) qxptr0 *= WDweight;`. CPU `util.cpp:48` `if (*q1 < 0) *q1 *= WDweight;`는 공유 배열을 바꾼다. U Qold 갱신은 `U/cuda_acc_solver.cu:606`에서 원래 Qx를 읽는다. | GPU ACC의 지역 유출 보정이 이웃과 Qold에 전달되지 않는 결함 후보이다. |
| LG2-061 | g 상수 | C | CPU `lisflood.cpp:169` `ParSolver.g = C(9.8065500000000);`. M `M/classes/SimulationParams.h:18` `real       g         = C(9.80665);`. | M은 CPU·U·N과 다른 중력 상수를 사용한다. |
| LG2-062 | U QFIX 경계 생략 | C | CPU `boundary.cpp:414` `case QFIX4:`. U `U/cuda_acc_solver.cu:274` `case QVAR5:`. 공통 복사는 `cuda/cuda_boundary.cu:556`에서 BC_Ident를 그대로 전달한다. | U 면 경계 switch는 QFIX를 처리하지 않는다. |
| LG2-063 | U 마른 H 경계 | E · 강함 | 반대 근거: 셀이 이미 젖었으면 이 후보 조건을 피한다. CPU `boundary.cpp:190` `if (true)//Arrptr->H[p0]>Solverptr->DepthThresh)`. U `U/cuda_acc_solver.cu:253` `if (U.H[p0] > cuda::solver_params.DepthThresh)`. N `N/compute_q.cu:171` `hflow = getmax(h_owner, boundary_value - z_owner);`. | U H 경계는 마른 셀을 높은 경계 수면으로 젖게 하지 못하는 결함 후보이다. |
| LG2-064 | N Q 경계 유속 | E · 강함 | 반대 근거: Q가 0이면 v=0 분기로 빠진다. N `N/compute_q.cu:23`의 hflow는 초기화 없는 지역 변수이다. `:192`는 Q만 설정한다. `:197` `d_non_uniform_nghbrs.v[idx] = d_non_uniform_nghbrs.q[idx] / length / hflow;`. FREE/H 분기의 hflow 대입은 `:154`, `:171`이다. | N의 비영 Q 경계 유속은 설정하지 않은 hflow로 나누는 결함 후보이다. |
| LG2-065 | M Q 경계 덮어쓰기 | E · 강함 | 반대 근거: 경계가 finest·bound·border이고 test_case=0일 때만 해당한다. M `M/neighbours/add_ghost_cells.cu:160` `d_assem_sol.h0[idx]        = boundaries.north.q_src(dt, dx_finest);`. 점 원천은 `M/mra/reinsert_point_srcs.cu:27` `d_scale_coeffs.eta0[h_idx] += point_sources.q_src(dt, dx_finest, idx);`. N `N/compute_q.cu:192`의 주석은 경계에 discharge가 필요하다고 적는다. | M Q 경계는 기존 수심을 증분으로 덮어쓰는 결함 후보이다. |
| LG2-066 | FREE·H·벽 수치 상태 | H | M `M/neighbours/add_ghost_cells.cu:139`의 전체 critical-depth 식은 §2.6에 있다. N `N/compute_q.cu:155` `Sf = boundary_value; // 0.02; //BCptr->BC_Val[BCi]; // MKS must check this`. | M의 HLL ghost 경계와 ACC의 관성 면 유량 경계는 같은 경계식이 아니다. |
| LG2-067 | 방향별 첫 경계 구간 | C | N `N/Boundary.h:275`과 M `M/classes/Boundary.h:322`의 원문은 `while (filedir != bcidir)`이다. M `M/classes/Boundary.h:77` `bool bound(const Coordinate& coordinate) const { return (coordinate >= start && coordinate <= end); }`. | N·M은 방향마다 처음 찾은 start·end 한 구간을 적용한다. |
| LG2-068 | 시계열 row 경계 | E · 강함 | 반대 근거: 현재 row가 내부 구간에 있고 한 구간만 전진하면 정상 보간할 수 있다. N `N/Boundary.h:453` `if ( (row - 1) < timeseries_len )` 뒤 `:456`은 row+1을 읽는다. M Boundary·PointSources에도 같은 패턴이 있다. CPU `boundary.cpp:1440` `if (t >= times[count - 1])`는 최종값을 먼저 처리한다. | N 경계와 M 경계·점 원천의 row 검사와 단일 전진은 배열 끝·큰 시간 점프 결함 후보이다. |
| LG2-070 | M 초기 원천 지형 인덱스 | E · 중간 | 반대 근거: 첫 finest 복사 뒤의 호출이고 시간 루프가 scale 계수에 원천을 다시 넣는다. M `M/mra/insert_point_srcs.cu:16` `HierarchyIndex h_idx = point_sources.d_codes[idx];`. `:22` `d_assem_sol.h0[h_idx] = point_sources.d_srcs[idx] - d_assem_sol.z0[idx];`. 초기 maxes는 driver `:397`에서 이 배열을 읽는다. | M 최초 H 원천은 점 번호와 Morton 위치를 혼용하는 결함 후보이다. |
| LG2-071 | 시계열 표본 시각 | C | M `M/cuda_adaptive_simulate.cu:424` `current_time += dt;`. `:604` `boundaries.update_all_inlets(input_filename, current_time);`. U `U/cuda_acc_simulate.cu:194` `cuda::Boundary::update_time_series(solver.t);`는 시간 증가 전이다. | M은 단계 끝 시각에서 경계·점 원천 시계열을 평가한다. |
| LG2-072 | CPU 전용 원천·옵션 | C | `iterateq.cpp:153` `if (Statesptr->calc_infiltration == ON) FPInfiltration(Parptr, Solverptr, Arrptr);`. `:156`은 routing을 호출한다. `:301`은 CalcVirtualGauge를 호출한다. GPU entry는 `lisflood.cpp:457`의 `return 0;`으로 CPU driver를 벗어난다. | GPU ACC·adaptive는 CPU 원천·routing·porosity·종료/후처리 옵션 전체를 구현하지 않는다. |
| LG2-074 | 균일 강우 시간 단위 | E · 강함 | 반대 근거: seconds이면 time_multiplier=1이다. `rain/Rainfall_uniform.h:74` `t_1 = t_2*time_multiplier;`. `:90`의 전체 보간식은 §2.7에 있다. 보간식은 t_1과 t_2의 차이에 배수를 곱하고 t_1에도 배수를 다시 곱한다. N `N/RainfallUniform.h:79`, `:95`가 같은 패턴이다. 경계 reader는 모든 time_data를 한 번만 변환한다. | GPU 균일 강우 reader는 구간 전진 시 분·시간을 혼합해 보간하는 결함 후보이다. |
| LG2-075 | 강우 배열 아래 범위 | E · 강함 | 반대 근거: 강우 도메인이 모델 전체를 덮으면 이 조건이 발생하지 않는다. `rain/rain.h:54` `* If the cell is outside the rainfall domain, the rainfall rate is zero.`. `rain/rain.tpp:118` `if (tile_i < geometry_.xsz && tile_j >= 0)` 뒤 data[tile_j*xsz+tile_i]를 읽는다. GPU도 같은 상한 누락이다. | CPU·GPU 공간 강우는 tile_j 상한을 검사하지 않는 결함 후보이다. |
| LG2-076 | NetCDF stub 초기 상태 | E · 강함 | 반대 근거: 기본 `_NETCDF=1`은 실제 생성자를 사용한다. `_NETCDF=0`은 `rain/rain_stub.tpp:11`의 `{}` 생성자이다. `rain/rain.h:114` `bool enabled_;`에 초기값이 없고 `:95`는 `return enabled_;`이다. 실제 생성자는 `rain/rain.tpp:17`에서 값을 지정한다. | NetCDF를 끈 GPU ACC 빌드는 설정하지 않은 enabled_를 읽는 결함 후보이다. |
| LG2-077 | 강우 dt 순서 | E · 강함 | 반대 근거: 이전 dt와 새 dt가 같으면 N의 시간량 차이가 가려진다. U 균일 강우는 새 dt를 쓴다. N `N/cuda_acc_nugrid_simulate.cu:564`는 강우에 solver.Tstep을 전달하고 `:578`에서 새 dt를 정한다. CPU `iterateq.cpp:152` `// Infiltration, evaporation and rainfall routines after time step update (TJF)`와 U 동적 강우의 `cuda/cuda_rain.cu:110`을 함께 확인했다. | U 동적 강우와 N 강우는 유동·시각 증가에 사용할 새 dt보다 먼저 이전 dt로 적분하는 결함 후보이다. |
| LG2-078 | 강우 질량 누적 | C | CPU `rain/rain.tpp:184` `Parptr->RainTotalLoss += total_rain_mass;`. N `N/rain_uniform.cu:41`의 mass 누적은 주석이다. U 동적 강우는 H만 더한다. | GPU ACC 강우 갱신은 CPU RainTotalLoss 장부를 누적하지 않는다. |
| LG2-079 | SGC 강우 캐시 | H | `rain/rain.tpp:206` `if (update_time_SGC(curr_time)); // if the file had to be read update rain_grid`. | 세미콜론 때문에 캐시 계산은 매 호출 실행되지만 이 행만으로 강우를 두 번 적용한다고 볼 수 없다. |
| LG2-080 | M 강우 호출 생략 | C | U `U/cuda_acc_simulate.cu:205` `if (states.rainfall == ON) {`. N `N/cuda_acc_nugrid_simulate.cu:559`도 같은 강우 분기를 둔다. M 시간 루프는 이 분기를 호출하지 않는다. | adaptive의 활성 시간 루프에는 균일·동적 강우 갱신이 없다. |
| LG2-081 | 질량 수지 정의 | C | CPU `iterateq.cpp:222`의 전체 Verror 식은 §2.8에 있다. GPU `cuda/stats.cpp:74` `C(0.0) /*Parptr->RainTotalLoss - (Parptr->InfilTotalLoss + Parptr->EvapTotalLoss)*/`. U FloodplainQ는 MassStats를 받지 않는다. | U의 체적 합계와 불완전한 원천 장부를 CPU 전체 질량 수지와 구분한다. |
| LG2-082 | 질량 오차 경과 시간 | E · 강함 | 반대 근거: 두 원천 묶음을 분리 누적하는 것은 가능하다. U `U/cuda_acc_simulate.cu:212`, `:219`는 모두 `stats_collector.accumulate_mass();`이다. 각 호출은 `cuda/cuda_stats.cu:83`의 `cumulative_time += cuda::dt;`를 실행한다. `:118`은 잔차를 이 시간으로 나눈다. | U는 한 단계 경과 시간을 두 번 누적해 Qerror 분모를 두 배로 만드는 결함 후보이다. |
| LG2-083 | N 누적 표본 | C | CPU `iterateq.cpp:190`은 MassTotal 또는 mint_hk==OFF를 검사한다. N `N/cuda_acc_nugrid_simulate.cu:624` `if (solver.t >= pars.MassTotal)` 안에서만 최대값을 갱신한다. N `N/update_max.cu:23` `totalHtm[idx] += solver.Tstep / C(3600.0);`. | N은 mint_hk를 끈 매 단계 누적을 제공하지 않고 MassInt 표본의 dt만 더한다. |
| LG2-084 | M 수리 누적 진단 생략 | C | M `M/output/write_cumulative_data.cpp:28`의 헤더는 `simtime,runtime_mra,runtime_solver,runtime_total,dt,reduction`이다. U `U/cuda_acc_snapshot.cu:56` `write_max(U.maxH, ".max", 0);`. | M cumulative 파일은 성능·격자 정보이며 mass·최대값·침수 시간 장부가 아니다. |
| LG2-085 | Q 파일 단위 | E · 중간 | 반대 근거: SWE의 단위폭 유량 출력 관례를 재사용했을 수 있고 dx=1이면 값이 같다. U `U/cuda_acc_snapshot.cu:41` `writer_HU = write_async(U.Qxold, ".Qx", 1, call_gzip);`. `U/cuda_acc_solver.cu:606`은 Qxold=Qx/dx이다. CPU `output.cpp:803`은 Qx 배열을 같은 확장자에 쓴다. | U의 `.Qx/.Qy`는 CPU ACC의 체적 유량과 단위가 다른 출력 결함 후보이다. |
| LG2-086 | 평균 stage·DG2 raster·scalar v | C | M `M/output/project_assem_sol.cu:73` `d_assem_sol.h0[idx]  = d_scale_coeffs.eta0[act_idx] - d_scale_coeffs.z0[act_idx];`. M DG2 raster의 Legendre 면 평가는 `M/output/write_all_raster_maps_dg2.cu:117`이다. N scalar v와 CPU stage v의 집계 식은 §2.8에 있다. | M stage는 leaf 평균이며 DG2 raster는 위치별 모드 평가값이다. |
| LG2-087 | stage 좌표 원점 | E · 중간 | 반대 근거: xmin=ymin=0인 synthetic 영역은 차이를 가린다. M `M/classes/StagePoints.h:133` `Coordinate x = (x_stage - sim_params.xmin) / cell_size;`. 출력 `M/output/write_stage_point_data.cu:72`는 `i * dx_finest + dx_finest / C(2.0),`이다. 같은 M의 VTK `N/write_soln_vtk.cu:94`는 xmin을 다시 더한다. | M stage 헤더 좌표는 실제 좌표 원점을 빠뜨린 결함 후보이다. |
| LG2-088 | N startelev 생략 | C | U 공통 `cuda/cuda_simulate.cu:40` `StartFile::subtract_dem(H, DEM, geometry, pitch, offset);`. N `N/get_modal_values.cu:64-67`의 대응 블록은 주석이다. | N의 시작 raster는 startelev 변환 없이 수심으로 읽힌다. |
| LG2-089 | N 정기 raster 생략 | C | N `N/cuda_acc_nugrid_simulate.cu:730-751`의 정기 projection·write_raster_maps가 주석이다. 활성 선택은 `:753` `if (states.save_vtk == ON) {`이다. | N은 정기 raster 함수 정의와 별개로 그 호출을 비활성화했다. |
| LG2-090 | checkpoint·copy | H | N `N/write_chkpnt.cu:76` `fwrite(q, sizeof(NUMERIC_TYPE), d_non_uniform_nghbrs.length, check_fp);`. `N/read_chkpnt.cu:195` `copy_cuda(d_non_uniform_nghbrs.q, q, bytes_dis);`. | 상태 전송은 수리식의 차이로 분류하지 않는다. |
| LG2-091 | CUDA SDK·장치 성능 점수 | H | `cuda/common/helper_cuda.h:785-786`의 compute_perf 곱은 §2.9에 전체 인용했다. | common의 장치 선택·파싱·오류 검사는 수리 계산이 아니다. |
| LG2-092 | 빌드·entry·8.3 판 식별 | H | `CMakeLists.txt:77` `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)`. `lisflood.cpp:450` `simulation.run(argc, argv);`. `VersionHistory.h:23` `#define LF_Release "8.3"`. | CUDA 해법별 entry와 별도 adaptive 파서를 기준으로 옵션 적용 범위를 정한다. |
| LG2-093 | 테스트 정의·좌표 | H | M `M/input/read_test_case.cpp:33` `const int max_test_case = 23;`. `M/mra/init_nodal_values.cu:54` `const real y_int = sim_params.ymin + dy_finest * y_idx;`. | 실제 synthetic selector는 23종이며 좌표는 ymin에서 증가한다. |
| LG2-094 | Monai·Oregon 특례 | H | M `M/neighbours/add_ghost_cells.cu:450` `if (sim_params.is_monai)`. `:471` `else if (sim_params.is_oregon)`. | M은 파일 이름으로 선택하는 실험별 서쪽 경계 함수를 갖는다. |
| LG2-095 | N 강우 남북 방향 | E · 강함 | 반대 근거: 남북 대칭 강우는 방향 차이를 가린다. `lisflood2/file_tool.cpp:359` `// assume data are ordered left-to-right, top-to-bottom`. N `N/read_raster_file.cpp:39`는 DEM 행을 뒤집는다. N `N/rain.cu:31` `int tile_j = (j - top_gap/ dx) * dx / dy_rain;`는 Morton의 남쪽 j를 뒤집지 않는다. | N 동적 강우는 북쪽 첫 행 배열을 남쪽 Morton 좌표로 참조하는 결함 후보이다. |
| LG2-096 | 음의 강우 직후 보정 생략 | C | CPU `infevap.cpp:114` `if(h0<0)`은 수심을 0으로 자른다. N `N/rain_uniform.cu:33-37`은 주석이며 U `U/cuda_acc_solver.cu:165` `Hval += cell_rain;`은 바로 더한다. 후속 H 갱신은 다시 0으로 자른다. | GPU 균일 강우는 CPU의 강우 직후 음수 제한을 생략한다. |
| LG2-097 | 미사용 wrapper·reader | H | U `U/cuda_acc_solver.cu:1066-1070`은 빈 zero_thin_depth_slopes 정의이다. N 활성 점 시계열은 `N/PointSources.h:193` `this->h_srcs[i] = InterpolateTimeSeries(h_src.PS_TimeSeries[i], time_now);`이다. | 사용하지 않는 옛 wrapper와 활성 해법 호출을 구분한다. |
| LG2-098 | 최초 기준 체적 | E · 강함 | 반대 근거: 초기 체적이 0이면 차이가 없고 유효한 체크포인트는 기준 체적을 복원한다. CPU `iterateq.cpp:29`는 DomainVol로 초기 vol1을 구한다. `cuda/cuda_stats.cuh:35` `NUMERIC_TYPE previous_volume = C(0.0);`. `cuda/cuda_stats.cu:93`은 현재 체적에서 이 값을 뺀다. U driver에는 루프 전 체적 대입이 없다. | U는 비영 초기 수심의 체적을 첫 질량 오차에 포함하는 결함 후보이다. |

분류별 개수: C 28, E 25, F 5, H 26, X 0. 열지 못한 파일: 없음.

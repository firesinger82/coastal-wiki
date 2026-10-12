---
file: models/ShorelineS/raw/source_code/shorelines/functions/transport_tidewave.m
lines: 88
sha256: 85da348c8f72586b9c22d7495589e1f03d00af8adf925c37d1c76ad32f62dc49
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# transport_tidewave.m — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | 함수 시그니처(1), 조석·파랑 수송 목적(4), eta·detads·phi·surfslope·Ttide·nT·ktide·cf·hmin·파랑·입경·단면 입력과 8개 출력 설명(6–36), 저작권·LGPL·무보증·빈 줄(38–65). Ttide=745*60과 nT=24는 입력 주석의 예시이며 실행 기본값 대입은 없다. 원문: `function [Slongtot,Slong_mean,Slong,v,vt,vw,Hrms,h]=transport_tidewave(eta,detads,phi,surfslope,Ttide,nT,ktide,cf,hmin,Hrms0,Tp,theta0,alpha,gamma,ks,D50,D90,hclosure,x,zb,Acal,n)` (1). |
| 66–77 | 시작 시 1행 함수 안. tide_1d_ana_anycomp 호출에서 네 번째 인수 0을 넘겨 수심 h와 조석 속도 vt를 얻는다(67). wave_cur_1D로 조석 중 파고 감소와 파랑 유도 속도 vw를 계산한다(70). vt+vw를 총 속도로 하고 transport_soulsbyvanrijn을 호출하여 Slong을 얻는다(73–76). 원문: `[h,vt] = tide_1d_ana_anycomp(eta,detads,phi,0,surfslope,Ttide,nT,ktide,cf,hmin,x,zb);` (67), `[Hrms,Dw,Urms,k,C,Cg,theta,Fy,vw] = wave_cur_1D(Hrms0,Tp,theta0,alpha,gamma,cf,x,h,n);` (70), `v=vt+vw;` (73), `[Slong]=transport_soulsbyvanrijn(h,Tp,k,Hrms,v,ks,hmin,D50,D90,Acal);` (76). |
| 78–88 | 시작 시 1행 함수 안. h==hmin 또는 h>hclosure인 수송을 0으로 설정한다(79–80). 시간 차원 평균 Slong_mean과 hmean을 구하고 첫 두 x의 간격으로 전체 수송을 적분한다(81–85). 함수 끝과 빈 줄(87–88). 원문: `Slong(h==hmin)=0;` (79), `Slong(h>hclosure)=0;` (80), `Slong_mean=mean(Slong,2);` (81), `hmean=mean(h,2);` (82), `Slongtot=sum(Slong_mean)*(x(2)-x(1));` (85). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70·82: wave_cur_1D 출력 Dw·Urms·C·Cg·theta·Fy와 계산한 hmean은 이후 이 파일에서 참조되지 않는다.
- 79: 건조점 수송 제거 조건은 h<hmin이 아니라 h==hmin이다.
- 85: 횡단 적분은 x(2)−x(1) 하나를 모든 점에 사용한다.
- 1·6–26: 함수 인수 Acal·n은 시그니처와 호출에 있으나 입력 설명에는 별도 항목이 없다.

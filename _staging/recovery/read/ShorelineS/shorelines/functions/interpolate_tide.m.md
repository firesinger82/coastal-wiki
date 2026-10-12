---
file: models/ShorelineS/raw/source_code/shorelines/functions/interpolate_tide.m
lines: 88
sha256: f56dc1ca182e6b962844d2345330c36455765168e41cd1bfacb8913f167fac4e
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# interpolate_tide.m — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 함수 시그니처(1). M2·M4 조석(tide)의 진폭(amplitude), 연안 방향 진폭 기울기, 위상(phase), 파수(wave number), 평균 수면 기울기를 조석 지원점에서 해안선으로 보간한다는 입출력 주석(4–25). 좌표는 m, 위상은 deg, 파수는 rad/m이다(8–13). 원문: `function [TIDE]=interpolate_tide(TIDE,COAST)` (1). [10-12 전수 검증 정정] |
| 27–54 | 시작 시 1행 interpolate_tide 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(27–54). |
| 55–71 | 시작 시 1행 interpolate_tide 함수 안. TIDE가 비어 있지 않을 때만 처리한다(55). eta·detads·k의 두 성분과 ss를 var1에, phi의 두 성분을 var2에 넣는다(57–65). 지원점과 COAST.xq·yq를 가져와 weighted_distance로 get_interpolation_on_grid를 호출한다(66–71). 원문: `if ~isempty(TIDE)` (55), `var1.eta1    =   TIDE.eta_stat(:,1);` (57), `var1.eta2    =   TIDE.eta_stat(:,2);` (58), `var1.detads1 =   TIDE.detads_stat(:,1);` (59), `var1.detads2 =   TIDE.detads_stat(:,2);` (60), `var1.k1      =   TIDE.k_stat(:,1);` (61), `var1.k2      =   TIDE.k_stat(:,2);` (62), `var1.ss      =   TIDE.ss_stat;` (63), `var2.phi1    =   TIDE.phi_stat(:,1);` (64), `var2.phi2    =   TIDE.phi_stat(:,2);` (65), `xtide        =   TIDE.x_stat;` (66), `ytide        =   TIDE.y_stat;` (67), `xq           =   COAST.xq;` (68), `yq           =   COAST.yq;` (69), `method       =   'weighted_distance';` (70), `[var1i,var2i,idGRID]=get_interpolation_on_grid(method,xq,yq,xtide,ytide,var1,var2);` (71). |
| 72–88 | 시작 시 1행 interpolate_tide 함수·55행 TIDE 비어 있지 않음 분기 안. 보간된 진폭·진폭 기울기·파수를 각각 두 열로 구성한다(72–77). ss와 두 위상을 받아 TIDE.eta·detads·k·ss·phi를 갱신한다(78–85). 조건 종료·빈 줄·함수 종료(86–88). 원문: `eta(:,1)    = var1i.eta1;` (72), `eta(:,2)    = var1i.eta2;` (73), `detads(:,1) = var1i.detads1;` (74), `detads(:,2) = var1i.detads2;` (75), `k(:,1)      = var1i.k1;` (76), `k(:,2)      = var1i.k2;` (77), `ss          = var1i.ss;` (78), `phi(:,1)    = var2i.phi1;` (79), `phi(:,2)    = var2i.phi2;` (80), `TIDE.eta    = eta;` (81), `TIDE.detads = detads;` (82), `TIDE.k      = k;` (83), `TIDE.ss     = ss;` (84), `TIDE.phi    = phi;` (85). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 71: get_interpolation_on_grid의 idGRID 출력은 이후 이 함수에서 사용하지 않는다.
- 55–86: TIDE가 빈 경우 필드를 만드는 별도 분기는 없다.

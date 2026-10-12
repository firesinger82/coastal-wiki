---
file: models/ShorelineS/raw/source_code/shorelines/functions/dune_growth.m
lines: 92
sha256: a5452d4d2e6a448bca9d39b96bfbc3c9ee8810b98a73ce1c32990a57e65df0a5
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# dune_growth.m — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–63 | 함수 시그니처 `function [qw,uc,us,mwe,qwe,Bdry,FL]=dune_growth(uwindi,duneaw,rhos,rhoa,por,g,d50,d50r,z,k,kw,R,SWLi,dfelev,wberm,phic,phiwndi,segmaw)` (1). 풍성 수송(aeolian transport)에 의한 사구(dune) 성장 목적·입출력 단위·계수 설명(4–35). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(36–63). |
| 64–77 | 점 수 length(phic)(64). 임계 마찰속도(critical shear velocity)·배열 확장·거칠기 높이·마찰속도(shear velocity) `uc=duneaw*sqrt((rhos-rhoa)*g*d50/rhoa);                                     % wind critical shear velocity (m/s)` (67); `uc=uc.*ones(1,n);` (68); `z0=d50/30;                                                                  % Larson 2016` (69); `us=k.*uwindi./log(z/z0);                                                    % wind shear velocity (m/s)` (71). 대체 거칠기 식은 주석 처리(70). 잠재 풍성 수송률 `mwe=kw*sqrt(d50r/d50)*rhoa*us.^2.*max(us-uc,0)/g;` (75). mov 검사·0 설정은 주석 처리(74·76). 추가 원문: `n=length(phic);` (64). [10-12 전수 검증 보완] |
| 78–88 | 연간 초 수·공극률(porosity)을 반영한 평형 수송률 `spyr     = 3600*24*365;` (79); `qwe=spyr*mwe/rhos/(1-por);                                                  % adapted by Anouk` (80). 마른 해빈(dry beach) 폭 `Bdry=max((1-(R+SWLi)./dfelev),0).*wberm;` (83). 해안 법선 방향과 풍향 차이의 코사인 하한 0·취송 거리(fetch length) `cosphiwndloc=max(cosd(phic-phiwndi),0);` (86); `FL = max(Bdry./cosphiwndloc,0);` (87). [10-12 전수 검증 정정] |
| 89–92 | 취송 거리를 반영한 수송률·해안 법선 성분 `qw0=qwe.*(1-(exp(-segmaw.*FL)));` (90); `qw=qw0.*cosphiwndloc;` (91). 함수 종료(92). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·1: 출력 주석에는 wberm이 있지만 함수 출력 목록에는 wberm이 없다.
- 86–91: cosphiwndloc의 하한은 0이다. FL은 cosphiwndloc로 나누며 분모의 양수 하한을 별도로 두는 문장은 없다.

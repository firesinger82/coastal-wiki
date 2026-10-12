---
file: models/ShorelineS/raw/source_code/shorelines/functions/transport_soulsbyvanrijn.m
lines: 83
sha256: faaae2622e6ecd32fe40cbb0980e460b14fc9eba2edf2795fbc928634280c9fd
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# transport_soulsbyvanrijn.m — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | 함수 시그니처(1), Soulsby–van Rijn 모래 수송 목적(4), h·T·k·H·v·ks·hmin·입경 입력 및 연간 Slong 출력 설명(6–18), 저작권·LGPL·무보증·빈 줄(20–47). 구조체 입력과 인수 기본값 대입은 없다. 원문: `function [Slong]=transport_soulsbyvanrijn(h,T,k,H,v,ks,hmin,D50,D90,Acal)` (1). |
| 48–68 | 시작 시 1행 함수 안. g=9.81·delta=1.65·rho=1025·nu=1.e-6·kappa=0.39를 설정하고 거칠기(roughness) z0와 무차원 입경 Dstar를 계산한다(48–51). dry를 h<hmin으로 정하고 수심 하한을 적용한다(52–53). 파랑 Urms를 계산하며 D50<=0.5e-3 분기와 else에서 임계 속도 Ucr를 달리 정한다(54–59). 마찰 cf·유효 속력 umod·2.4승 ksi, 소류사(bedload) 및 부유사(suspended load) 계수와 수송을 계산한다(60–68). 원문: `g=9.81;delta=1.65;rho=1025;nu=1.e-6;kappa=0.39;` (48), `z0=ks/30;` (49), `Dstar=(g*delta/nu^2)^(1/3)*D50;` (51), `dry=h<hmin;` (52), `h=max(h,hmin);` (53), `Urms=1/sqrt(2)*pi*H./T./sinh(k.*h);` (54), `if D50<=0.5e-3` (55), `Ucr=0.19*D50^0.1*log10(4*h/D90);` (56), `else` (57), `Ucr=8.5*D50^0.6*log10(4*h/D90);` (58), `cf=(kappa./(log(h/z0)-1)).^2;` (60), `umod=sqrt(v.^2+0.018./cf.*Urms.^2);` (61), `ksi=(umod-Ucr).^2.4;` (62), `ksi(umod<Ucr)=0;` (63), `Asb=0.005*h.*(D50./h/delta/g/D50).^1.2;` (64), `Ass=0.012*D50*Dstar^(-0.6)/(delta*g*D50)^1.2;` (65), `Sby=Acal*Asb.*v.*ksi;` (66), `Ssy=Acal*Ass.*v.*ksi;` (67), `Stoty=Sby+Ssy;` (68). |
| 69–83 | 시작 시 1행 함수 안. dry 인덱스에서 파랑·임계 속도·수송 관련 배열을 0으로 설정한다(70–81). Stoty에 연간 초를 곱하여 Slong으로 반환하고 함수를 끝낸다(82–83). 원문: `Urms(dry)=0;` (70), `Ucr(dry)=0;` (71), `Cd(dry)=0;` (72), `ksi(dry)=0;` (73), `Asb(dry)=0;` (74), `Ass(dry)=0;` (75), `Sbx(dry)=0;` (76), `Sby(dry)=0;` (77), `Ssx(dry)=0;` (78), `Ssy(dry)=0;` (79), `Stotx(dry)=0;` (80), `Stoty(dry)=0;` (81), `Slong=Stoty*3600*24*365;` (82). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48: rho=1025는 대입 이후 이 파일에서 참조되지 않는다.
- 72·76·78·80: Cd·Sbx·Ssx·Stotx는 dry 인덱스에 0을 넣는 문장에서 처음 등장한다. 이 변수의 계산식은 앞 블록에 없다.
- 62–63: ksi=(umod-Ucr).^2.4를 먼저 계산하고 umod<Ucr인 인덱스를 다음 행에서 0으로 바꾼다.
- 14–15·51·55–58: 입력 주석의 입경 단위는 um이다. 실행식은 입력 D50·D90를 그대로 사용하며 D50를 0.5e-3과 비교한다. 단위 변환문은 이 파일에 없다.

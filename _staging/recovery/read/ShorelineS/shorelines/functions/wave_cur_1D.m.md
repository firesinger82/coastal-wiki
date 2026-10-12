---
file: models/ShorelineS/raw/source_code/shorelines/functions/wave_cur_1D.m
lines: 97
sha256: 97e3b93b0097addd958654ec7df44671de3fbe855aa51ad3c497facd5d4dcaec
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# wave_cur_1D.m — 판독 구간 기록

구간은 1행부터 97행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | 함수 시그니처(1), 여러 수위에서 1차원 단면의 Snell 법칙(Snell's law)·파랑 에너지 수지(wave energy balance)·파랑 유도 흐름 계산 목적(4–5), 인수와 9개 출력 설명(7–26), 저작권·LGPL·무보증·빈 줄(28–55). 인수 기본값 설정문은 없다. 원문: `function [H,Dw,Urms,k,C,Cg,theta,Fy,vw] = wave_cur_1D(H0,T,theta0,alpha,gamma,cf,x,h,n)` (1). |
| 56–75 | 시작 시 1행 함수 안. g=9.81·rho=1025·eps=1e-6을 설정한다(56–58). n이 비어 있지 않으면 수심에 따른 cf를 계산한다(59–61). dx는 첫 두 x의 차이이다(62). get_disper로 분산(dispersion) 관계를 풀고 Hmax·Emax를 계산한다(65–67). try에서 첫 위치 파속 대비 asind로 파향을 구하고 catch에서는 theta0를 그대로 사용한다(70–74). 원문: `g=9.81;` (56), `rho=1025;` (57), `eps=1e-6;` (58), `if ~isempty(n)` (59), `cf=9.81*(n^2)./h.^(1/3);` (60), `dx=x(2)-x(1);` (62), `[k,C,Cg]=get_disper(h,T);` (65), `Hmax=0.88./k.*tanh(gamma*k.*h/0.88);` (66), `Emax=0.125*rho*g*Hmax.^2;` (67), `try` (70), `theta=asind(sind(theta0).*C./C(1,:));` (71), `catch` (72), `theta=theta0;` (73). |
| 76–86 | 시작 시 1행 함수 안. E·beta를 0으로 초기화하고 첫 위치 에너지에 eps 하한을 적용한다(76–78). 1:length(x)−1 루프에서 beta와 다음 E를 한 번 계산한 뒤 두 점 에너지 합으로 beta·E를 다시 계산한다(79–83). E 상한은 0.125*rho*g*(gamma*h)^2, 하한은 eps이다(84). 원문: `E=zeros(size(h));` (76), `beta=zeros(size(h));` (77), `E(1,:)=max(1/8*rho*g.*H0.^2,eps);` (78), `for i=1:length(x)-1` (79), `beta(i,:)=2*alpha./T*dx.*exp(-Emax(i,:)./abs(E(i,:)));` (80), `E(i+1,:)=(E(i,:).*Cg(i,:).*cosd(theta(i,:))-beta(i,:).*Emax(i,:))./(Cg(i+1,:).*cosd(theta(i+1,:))+beta(i,:));` (81), `beta(i,:)=2*alpha./T*dx.*exp(-Emax(i,:)./abs(E(i,:)+E(i+1,:))*2);` (82), `E(i+1,:)=(E(i,:).*Cg(i,:).*cosd(theta(i,:))-beta(i,:).*Emax(i,:))./(Cg(i+1,:).*cosd(theta(i+1,:))+beta(i,:));` (83), `E(i+1,:)=max(min(E(i+1,:),0.125*rho*g*(gamma*h(i+1,:)).^2),eps);` (84). |
| 87–97 | 시작 시 1행 함수 안이며 에너지 루프 밖. E에서 H를 구하고 beta와 Emax+E로 소산(dissipation) Dw, 파랑 힘 Fy를 계산한다(87–89). min(H/T,1)을 사용한 Urms와 이차식 계수 aa·bb·cc로 vw를 계산한다(90–92). NaN Urms·vw를 0으로 바꾸며 대체 vw 식 두 개는 주석이다(93–96). 함수가 끝난다(97). 원문: `H=sqrt(8*E/rho/g);` (87), `Dw=beta/dx.*(Emax+E);` (88), `Fy=Dw./C.*sind(theta);` (89), `Urms=1/sqrt(2)*pi*min(H./T,1)./sinh(k.*h);` (90), `aa=1./Urms.^2;bb=1.16^2;cc=-(Fy/rho./cf./Urms).^2;` (91), `vw=sqrt((-bb+sqrt(bb.^2-4*aa.*cc))/2./aa).*sign(theta);` (92), `Urms(isnan(Urms))=0;` (93), `vw(isnan(vw))=0;` (94). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 79–85·88: beta는 1:length(x)−1 행만 갱신한다. 마지막 행은 초기값 0을 유지하고 Dw 식은 전체 beta를 사용한다.
- 90–94: Urms의 NaN 대체는 aa·cc·vw 계산 뒤에 실행된다. Inf를 별도로 바꾸는 문장은 없다.
- 62: 모든 횡단 계산에 쓰는 dx는 x(2)−x(1) 한 값이다.
- 1·7–15·59–60: 인수 n은 시그니처와 cf 계산에 있으나 입력 설명에 별도 항목은 없다.

---
file: models/ShorelineS/raw/source_code/shorelines/functions/tide_1d_ana_anycomp.m
lines: 92
sha256: e4f3d532164c6f8a5d97afbacdeddae1fea7c39aa427682cbe05814cde9b00bb
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# tide_1d_ana_anycomp.m — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | 함수 시그니처는 `function [h,vt,surfslope]=tide_1d_ana_anycomp(eta,detads,phi,vmean,surfslope,Ttide,nT,k,cf,hmin,x,zb)` (1). 주석은 횡단면(cross-shore profile)의 조석(tide)·평균 속도 해석해(analytical solution), 성분 진폭·연안방향 기울기·위상·파수·마찰·최소 수심·시간점 수와 수심·속도 행렬 출력을 설명한다(2–22). S 구조체 입력과 S 필드 기본값은 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(23–50). |
| 51–68 | `g=9.81;` (51), `deg2rad=pi/180;` (52), `ncomp=length(eta);` (53), `phi=phi*deg2rad;` (54), `omega(1)=2*pi/Ttide;` (55). `for i=2:ncomp` (56)에서 `omega(i)=i*omega(1);` (57). `dT=Ttide/nT;` (59), `t=[dT:dT:Ttide];` (60), `etat=zeros(size(t));` (61). `for i=1:ncomp` (62)에서 `etat=etat+eta(i)*cos(omega(i)*t-phi(i));` (63). `tt=repmat(t,length(x),1);` (65), `h=etat-zb';` (66), `h=max(h,hmin);` (67), `hmean=mean(h,2);` (68)로 조석 수위와 제한 수심·평균 수심을 만든다. |
| 69–81 | 진폭 기울기 보정은 `amp=sqrt(sum(k.^2.*eta.^2+detads.^2));` (70). 마찰 관련 진폭·계수 해석식은 `aa=(3*pi/8*cf/omega(1)./hmean).^2;bb=1;cc=-(g*amp/omega(1))^2;` (73), `vamp=max(sqrt((-bb+sqrt(bb^2-4*aa*cc))/2./aa),eps);` (74), `labda=3*pi/8*cf*vamp;` (75). `for i=1:ncomp` (77)에서 `ph(:,:,i)=labda./hmean/omega(i);` (78), `a(:,:,i)= g/omega(i).*(        1./(1+ph(:,:,i).^2)*k(i)*eta(i)-ph(:,:,i)./(1+ph(:,:,i).^2)*detads(i));` (79), `b(:,:,i)=-g/omega(i).*(ph(:,:,i)./(1+ph(:,:,i).^2)*k(i)*eta(i)+        1./(1+ph(:,:,i).^2)*detads(i));` (80)를 계산한다. 주석·빈 줄·루프 종료를 포함한다. |
| 82–92 | `vt=zeros(size(h));` (83). `for i=1:ncomp` (84)에서 `vt=vt +a(:,:,i).*cos(omega(i)*tt-phi(:,i))+b(:,:,i).*sin(omega(i)*tt-phi(:,i));` (85). 대체 수면 경사 보정식은 주석이다(87). `if length(x)==1` (88)이면 `surfslope=-vmean*labda/g/hmean;` (89). 최종식은 `vt=vt-mean(vt,2)-g*hmean*surfslope./labda;` (91). 조건·함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 51: 중력 가속도 g는 9.81로 고정 대입한다.
- 55–58: 성분 각진동수는 omega(1)의 정수배로 설정한다. 각 성분의 주기를 따로 입력받는 인수는 없다.
- 59–60: 조석 시간축은 dT부터 시작하며 0을 포함하지 않는 범위식이다.
- 63·85: 수위 합성은 phi(i)를 참조한다. 속도 합성은 phi(:,i)를 참조한다.
- 73–75·91: vamp 식은 aa로 나누며 최종 속도식은 labda로 나눈다. 해당 분모가 0인지 검사하는 조건은 없다. eps 제한은 vamp의 제곱근 계산 뒤 max에 적용한다.
- 88–91: vmean은 length(x)==1일 때 surfslope 계산에만 사용한다. 그 밖의 길이에서는 입력 surfslope를 최종식에 사용한다.

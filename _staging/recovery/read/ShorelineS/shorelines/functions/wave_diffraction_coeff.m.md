---
file: models/ShorelineS/raw/source_code/shorelines/functions/wave_diffraction_coeff.m
lines: 84
sha256: 954c48277a77b71a2d6c30fb4d9032f9a93d9e98fb17577764f41962433f3ed1
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# wave_diffraction_coeff.m — 판독 구간 기록

구간은 1행부터 84행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 함수 시그니처(1), 회절(diffraction) 파고 저감 목적(4), omega·kdform·wdform·방향 퍼짐(directional spreading) dspr 입력과 kd 출력 설명(6–13), 저작권·LGPL·무보증·빈 줄(15–42). dspr는 주석상 선택 인수이나 기본값 대입은 없다. 원문: `function [kd]=wave_diffraction_coeff(omega,kdform,wdform,dspr)` (1). |
| 43–58 | 시작 시 1행 함수 안. kd를 빈 배열로 시작하고 omega의 각 행을 처리한다(44–45). wdform이 Roelvink이면 방향 0 하나와 확률 1을 사용한다(48–51). else는 −50:5:50 방향 구간을 omega와 합치고 get_dirspr_prob 결과를 확률 합으로 정규화한다(52–56). 원문: `kd=[];` (44), `for j=1:size(omega,1)` (45), `if strcmpi(wdform,'Roelvink')` (48), `dirout=[0];` (49), `omr=omega(j,:);` (50), `prob=1;` (51), `else` (52), `dirout=[-50:5:50];` (53), `omr=repmat(dirout(:),[1,length(omega(j,:))])+repmat(omega(j,:),[length(dirout),1]);` (54), `prob=get_dirspr_prob(dspr,dirout);` (55), `prob=prob/sum(prob);` (56). |
| 59–79 | 시작 시 1행 함수·45행 j 루프 안. kdform=='Roelvink'이면 fac1=0.5·pwr=4와 om_x=(omr+90)/180의 지수식을 사용하고 omr<−90에서 kdi=1로 둔다(60–66). Kamphuis elseif는 omk=−omr, 기본 kdi=1로 시작하여 −86.25·0·40·90 경계의 선형·사인식을 적용한다(68–77). 72–73행 대체식은 주석이다. 원문: `if kdform=='Roelvink'` (60), `fac1=0.5;` (62), `pwr=4;` (63), `om_x=(omr+90)/180;` (64), `kdi=1-exp(-abs((fac1./om_x).^pwr));` (65), `kdi(omr<-90)=1;` (66), `elseif kdform=='Kamphuis'` (68), `omk=-omr;   % Note: we define omega positive towards shadow zone` (70), `kdi=ones(size(omk));` (71), `kdi(omk < -86.25 ) = 0;` (74), `kdi(omk <= 0 & omk >=-86.25) = max(0.69+0.008*omk(omk <= 0 & omk >=-86.25),0);` (75), `kdi(omk > 0 & omk <= 40) = 0.71+0.356686*sind(omk(omk >  0 & omk <= 40));` (76), `kdi(omk > 40 & omk <= 90) = min(0.83+0.17*sind(omk(omk > 40 & omk <= 90)),1);` (77). |
| 80–84 | 시작 시 1행 함수·45행 j 루프 안이며 kdform 선택문 밖. 방향별 kdi 제곱에 확률을 곱하고 합의 제곱근으로 kd를 계산한다(81–82). 루프와 함수가 끝난다(83–84). 원문: `kdiprob=kdi.^2.*repmat(prob(:),[1,size(kdi,2)]);` (81), `kd(j,:)=(sum(kdiprob,1)).^0.5;` (82). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·1: 입력 주석 필드 이름은 dpsr이고 함수 인수 이름은 dspr이다.
- 60·68: kdform 비교는 문자 배열 ==를 사용한다. wdform 비교는 strcmpi를 사용한다(48).
- 60–78·81: kdform 선택문에는 두 이름만 있고 else가 없다. kdi를 사용하는 식은 선택문 밖에 있다.
- 1·10·55: dspr를 선택 인수라고 설명하지만 nargin 검사나 기본값 설정은 없다. Roelvink가 아닌 wdform 분기에서 dspr를 참조한다.
- 53: Roelvink가 아닌 wdform의 방향 구간은 −50:5:50으로 고정한다.

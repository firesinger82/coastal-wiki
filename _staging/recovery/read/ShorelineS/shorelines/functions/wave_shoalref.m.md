---
file: models/ShorelineS/raw/source_code/shorelines/functions/wave_shoalref.m
lines: 69
sha256: 8d3ae5b65fcb1ddc1409ddbd9893f63f59326206fa9383641172dff5467fdf8d
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# wave_shoalref.m — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | 함수 시그니처(1), 천수(shoaling)와 굴절(refraction)에 따른 파고·쇄파수심 변화 목적(4–5), hbr·tper·gamma·hstdp·ctdp·ntdp·sinPHIw·cosPHIw 입력과 5개 출력 설명(7–22), 저작권·LGPL·무보증·빈 줄(24–51). 인수 기본값 설정은 없다. 원문: `function [hbrnew,dPHIbr,err,cbr,nbr]=wave_shoalref(hbr,tper,gamma,hstdp,ctdp,ntdp,sinPHIw,cosPHIw)` (1). |
| 52–65 | 시작 시 1행 함수 안. get_disper로 가정 수심의 파속(celerity) cbr·nbr를 얻는다(52). Snell 사인 인수 절대값이 1 미만이면 asind로 각도를 구한다(53–54). 에너지 유속 인수가 양수이고 각도 코사인 절대값이 1e-3보다 크면 파고 변환식을 사용한다(55–56). 내부 else와 바깥 else는 acosd(cosPHIw) 각도와 기존 hstdp를 사용한다(58–64). 원문: `[~,cbr,~,nbr]=get_disper(hbr,tper);` (52), `if abs(cbr./ctdp.*sinPHIw)<1` (53), `dPHIbr=asind(cbr./ctdp.*sinPHIw);` (54), `if (nbr.*cbr.*cosd(dPHIbr))>0 && abs(cosd(dPHIbr))>1e-3` (55), `hstdpbr=hstdp.*sqrt(ntdp.*ctdp.*cosPHIw./(nbr.*cbr.*cosd(dPHIbr)));` (56), `else` (58), `dPHIbr=acosd(cosPHIw); % take the input wave angle as representative for the relative incidence angle at breaking` (59), `hstdpbr=hstdp;  % not so relevant case where the wave approaches very obliquely, or depth is 0, likely very small TP of hstdp` (60), `else` (62), `dPHIbr=acosd(cosPHIw); % take the input wave angle as representative for the relative incidence angle at breaking` (63), `hstdpbr=hstdp;` (64). |
| 66–69 | 시작 시 1행 함수 안이며 각도·파고 분기 밖. hstdpbr/gamma를 새 쇄파수심으로 하고 err=hbrnew−hbr를 반환한다(67–68). 함수가 끝난다(69). 원문: `hbrnew=hstdpbr/gamma;` (67), `err=hbrnew-hbr;` (68). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 53·55·59·63: 정상 분기는 sinPHIw를 포함한 asind를 사용한다. 두 대체 각도는 cosPHIw만 포함한 acosd를 사용한다.
- 20·68: 출력 주석은 err를 relative change라고 적고 단위는 m이다. 실행식은 수심의 차 hbrnew−hbr이다.
- 52·67: cbr·nbr는 입력 hbr에서 계산한다. 새 hbrnew 대입 뒤 재계산하는 호출은 없다.

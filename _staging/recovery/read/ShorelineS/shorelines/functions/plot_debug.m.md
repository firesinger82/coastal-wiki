---
file: models/ShorelineS/raw/source_code/shorelines/functions/plot_debug.m
lines: 131
sha256: f7149e8a820d34b39d18dddb070f6038b1b05280f54ae0c5d85cbab2991ff22f
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# plot_debug.m — 판독 구간 기록

구간은 1행부터 131행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 함수 시그니처(1). 디버그(debug) 그림을 만드는 설명(4). use_debug 주석 범위는 0–5이다(7). 입력 해안 좌표·수송점·파랑·수송량·차폐 지표와 세 debug 수송량 필드의 의미를 적는다(8–31). 원문: `function plot_debug(use_debug,COAST,WAVE,TRANSP,im3,ip3)` (1). |
| 33–60 | 시작 시 1행 plot_debug 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(33–60). |
| 61–80 | 시작 시 1행 plot_debug 함수 안. use_debug==1이면 현재 그림을 보관하고 112번 그림에 plot_figureproperties(1220,920,30)를 적용한다(61–65). 인접 해안 좌표 평균으로 x2·y2를 만든다(67–68). 첫 2×2 패널에 dPHItdp를 scatter로 표시하고 색 범위를 0..360으로 둔다(71–76). try로 im3 위치를 덧그린다(77). 축 범위 대안은 주석(78–79). 원문: `if use_debug==1` (61), `fc9=gcf;` (63), `figure(112);` (64), `clf;plot_figureproperties(gcf,1220,920,30);` (65), `x2=(COAST.x(1:end-1)+COAST.x(2:end))/2;` (67), `y2=(COAST.y(1:end-1)+COAST.y(2:end))/2;` (68), `subplot(2,2,1);` (71), `plot(COAST.x,COAST.y);hold on;` (72), `title('WAVE.dPHItdp [?]');` (73), `scatter(x2,y2,10,WAVE.dPHItdp);` (74), `set(gca,'clim',[0,360]);` (75), `colorbar;` (76), `try;plot(COAST.x(im3(2:end,1)),COAST.y(im3(2:end,1)),'ko');end` (77). |
| 81–113 | 시작 시 1행 plot_debug 함수·61행 use_debug==1 분기 안. 나머지 세 2×2 패널에서 TRANSP.debug.QS2·QS0·QS1을 scatter로 표시한다(82–109). 각 패널에 colorbar를 붙인다(86·98·108). try 안에서 im3 또는 ip3 위치를 표시한다(87·99·109). 축 범위·차폐 변경 대안은 주석(88–91·100–101·110–112). 원문: `subplot(2,2,2);` (82), `plot(COAST.x,COAST.y);hold on;` (83), `title('TRANSP.debug.QS2');` (84), `scatter(x2,y2,10,TRANSP.debug.QS2);` (85), `colorbar;` (86), `try;plot(COAST.x(im3(2:end,1)),COAST.y(im3(2:end,1)),'ks');end;` (87), `subplot(2,2,3);` (94), `plot(COAST.x,COAST.y);hold on;` (95), `title('TRANSP.debug.QS0');` (96), `scatter(x2,y2,10,TRANSP.debug.QS0);` (97), `colorbar;` (98), `try;plot(x2(im3),y2(im3),'ks');end` (99), `subplot(2,2,4);` (104), `plot(COAST.x,COAST.y);hold on;` (105), `title('TRANSP.debug.QS1');` (106), `scatter(x2,y2,10,TRANSP.debug.QS1);` (107), `colorbar;` (108), `try;plot(x2(ip3),y2(ip3),'k+');end` (109). |
| 114–117 | 시작 시 1행 plot_debug 함수·61행 디버그 유형 분기 안. 유형 1 경로는 원래 그림 fc9로 돌아간다(114). 116행 elseif는 유형 3이며 수송량·yq·한계수심/쇄파 파고·두 파향을 4×1 패널로 그린다(117). 원문: `figure(fc9);` (114), `elseif use_debug==3` (116), `figure;subplot(4,1,1);plot(TRANSP.QS);grid on;subplot(4,1,2);plot(COAST.yq);grid on;subplot(4,1,3);plot(WAVE.HStdp);hold on;plot(WAVE.HSbr,'r');grid on;subplot(4,1,4);plot(WAVE.PHItdp);hold on;plot(WAVE.PHIbr,'r');grid on` (117). |
| 118–123 | 시작 시 1행 plot_debug 함수·61행 디버그 유형 분기 안. 유형 4는 전체 수송점의 QS_mc를 scatter로 표시한다(118–120). 각 점 루프에서 수송량 text를 넣는다(121–123). 원문: `elseif use_debug==4` (118), `hold on;` (119), `hsc=scatter(COAST.xq_mc,COAST.yq_mc,5,TRANSP.QS_mc);` (120), `for kk=1:length(TRANSP.QS_mc)` (121), `hpp=text(COAST.xq_mc(kk),COAST.yq_mc(kk),num2str(TRANSP.QS_mc(kk),'%1.0f'));` (122). |
| 124–131 | 시작 시 1행 plot_debug 함수·61행 디버그 유형 분기 안. 유형 5는 대칭(symmetry) 비교이다(124–127). 수송량과 역순 부호 반전값, 270에서 쇄파 방향을 뺀 값과 역순 부호 반전값, 원래·y 부호 반전 해안을 3×1 패널로 그린다(127). 차폐점과 수송점도 표시한다. 다른 대칭 비교식은 주석(126·128). 유형 분기·함수 종료(130–131). 원문: `elseif use_debug==5` (124), `figure(88);clf;subplot(3,1,1);plot(TRANSP.QS_mc);hold on;plot(fliplr([1:length(TRANSP.QS_mc)]),-TRANSP.QS_mc,'r--');xi=[1:length(TRANSP.QS_mc)];plot(xi(TRANSP.shadowS_mc),TRANSP.QS_mc(TRANSP.shadowS_mc),'ko');subplot(3,1,2);plot(270-WAVE.PHIbr_mc);hold on;plot(fliplr([1:length(WAVE.PHIbr_mc)]),-(270-WAVE.PHIbr_mc),'r--');subplot(3,1,3);plot(COAST.x_mc,COAST.y_mc);hold on;plot(COAST.x_mc,-COAST.y_mc,'r--');plot(COAST.xq_mc,COAST.yq_mc,'g*');plot(COAST.xq_mc(TRANSP.shadowS_mc),COAST.yq_mc(TRANSP.shadowS_mc),'ko')` (127). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·61–130: 입력 주석은 use_debug 범위를 0–5로 적는다. 실행 분기는 1·3·4·5만 있으며 2 또는 그 외 값의 else는 없다.
- 77·87·99·109: 이 네 try 문장에는 catch 절이 없다.
- 127: 유형 5 파향 대칭 표시는 270-WAVE.PHIbr_mc를 사용한다.

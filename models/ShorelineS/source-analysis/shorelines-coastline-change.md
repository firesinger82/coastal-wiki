---
title: "ShorelineS coastline_change.m — one-line 이산화(staggered FTCS)·Bruun SLR·groyne 부착/자동연장·사구/mud 결합"
model: ShorelineS
component: functions/coastline_change.m
canonical_source: self
citation_status: verified
verification_method: "sha 7bf4481ab — coastline_change.m 440줄 전문 직접 read. 이산식·결합항 라인 인용, Roelvink et al. 2020 Eq.1·Eq.5 와 대조(manual-notes 참조). 2026-10-12 recovery 대조 보고서 R1·R2·R3 반영"
last_source_check: "2026-10-12 (recovery 대조 반영)"
note_author: "Claude Fable 5"
note_date: 2026-07-17
related:
  - models/ShorelineS/source-analysis/shorelines-transport-formulations.md
  - models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md
---

# coastline_change.m — 해안선 갱신 코어

> PHASE 2 의 본체(440줄). 논문 Eq.1(질량보존)·Eq.5(staggered explicit)의 코드 실체.

## 1. one-line 이산화 (`:301-318`, `:356-391`)

- 길이 하한이 작동하지 않는 내부점에서 ds=L_i/2이다. (functions/coastline_change.m:314 `COAST.ds(i)=hypot(COAST.x(ip1)-COAST.x(im1),COAST.y(ip1)-COAST.y(im1))/2;`; functions/coastline_change.m:315 `COAST.ds(i)=max(COAST.ds(i),eps);`)
- functions/coastline_change.m:316 `COAST.dSds(i)=(TRANSP.QS(ip1q)-TRANSP.QS(im1q))/COAST.ds(i);`
- functions/coastline_change.m:317 `COAST.dndt(i)=-COAST.dSds(i)/COAST.h0(i);`
- **위치 갱신**: `dn=(dndt+dndtnour−SLRo/tanbeta)·dt`(:365) — 양빈(육상 rate_density + shoreface FNOUR.q_tot, :319) 가산·**SLR 은 Bruun형 후퇴항 `−SLR/tanβ`**. 이동은 국소 법선 방향(접선 회전 :380-381), 옵션 `preserveorientation` 은 초기 방위 고정(:367-372), 단부는 PHIcxy0 방위(:373-378). cyclic 섹션은 끝점 평균 봉합(:392-399).
- 수치 보호: ds 하한 eps=1e-3(:315), 빈 섹션 sentinel −1e10(:412-417).

## 2. groyne 경계 처리 (`:141-296`)

- **우회(bypass) 방향 판정**(:142-156): 양측 QS 발산→0 / 동부호→최대측 채택 / 수렴→합산.
- **차폐구간 분배**(:179-217): bypass 량을 그림자 구간에 **삼각분포^pwr**(`bypassdistpwr`)로 가산 — pwr>1 이면 구조물 인접 퇴적 집중.
- **해안선-구조물 부착**(:220-295): 해안선 끝점을 groyne 둘레 경로 shard 위 보간점으로 핀(:289-290). 끝점 침식 dn 은 국소 수지+양빈+SLR 로 산출(:244-249, mud 는 가산 :246-248).
- ★**구조물 자동 연장**(:255-286): 침식이 groyne 육측 끝을 넘으면 **구조물 다리를 육지쪽으로 연장**(epsgroyne=1 m 여유)하고 STRUC 좌표를 갱신 — 사용자 통보는 모델단 없음(런 후 구조물 길이가 입력과 다를 수 있음, 검수 관찰). 인접 배치 오류 시 ds0 대체 + 경고(:235).

## 3. 프로세스 결합 (`:321-354`)

- **사구**(DUNE.used, :322-337): `dndt += (qss−qw)/h0`(:325 — 사구침식 모래분 qss 는 해빈 공급, 바람 되돌림 qw 차감), berm 폭 wberm 별도 부기(:327-332, 하한 1 m)·사구 기저/정상고 _mc 동기.
- MUD.used는 S.mud로 정한다. (functions/prepare_mudcoast.m:81 `MUD.used   = S.mud;                                                                     % mud transport option`)
- mud 해안선 변화율의 가산·대체 분기는 소스에 있다. (functions/coastline_change.m:247 `COAST.dndt(p1)=COAST.dndt(p1)+COAST.dndt_mud(p1);`; functions/coastline_change.m:342 `COAST.dndt=COAST.dndt_mud;`)
- 이 경로의 get_segmentdata는 dndt_mud_mc와 다른 이름을 읽는다. (functions/get_segmentdata.m:134 `[ COAST.dndt_mud ] = get_one_polygon( COAST.dndt_mudmc,i_mc);`; [R3:V01 코드 결함 후보](shorelines-architecture-map.md#코드-결함-후보-정적-판독))
- 점착성 해안은 갯벌·맹그로브·개척 폭을 별도 갱신한다. Bfm의 실제 갱신율은 dBfmdt-dBmdt이다. (functions/coastline_change.m:345 `COAST.Bfm=COAST.Bfm+(COAST.dBfmdt-COAST.dBmdt)*TIME.dt;`; functions/coastline_change.m:344 `COAST.Bf=COAST.Bf+COAST.dBfdt*TIME.dt;`; functions/coastline_change.m:346 `COAST.Bm=COAST.Bm+COAST.dBmdt*TIME.dt;`) [10-12 전수 검증 보완]

## 4. 논문 대조 (Roelvink et al. 2020)

| 논문 | 코드 |
|---|---|
| 논문 2020 PDF 3쪽 / 인쇄 3, 식 (1): $\frac{\partial n}{\partial t}=-\frac1{D_c}\frac{\partial Q_s}{\partial s}-\frac{RSLR}{\tan\beta}+\frac1{D_c}\sum q_i$ | functions/coastline_change.m:365 `dn=(COAST.dndt(i)+COAST.dndtnour(i)-CC.SLRo/COAST.tanbeta)*TIME.dt;` |
| 논문 2020 PDF 6쪽 / 인쇄 6, 식 (5): $\Delta n_i^j=-\frac1{D_c}\frac{2(Q_{s,i}^j-Q_{s,i-1}^j)}{L_i}\Delta t$ | functions/coastline_change.m:314 `COAST.ds(i)=hypot(COAST.x(ip1)-COAST.x(im1),COAST.y(ip1)-COAST.y(im1))/2;`<br>functions/coastline_change.m:315 `COAST.ds(i)=max(COAST.ds(i),eps);`<br>길이 하한이 작동하지 않는 내부점에서 ds=L_i/2이다. [10-12 전수 검증 보완] |
| 논문 2020 PDF 6쪽 / 인쇄 6, 고각도 전이 | functions/get_upwindcorrection.m:168 `if cw*dPHIcr(kk,i)>0 && ~TRANSP.idrevq(i) ... % only when the wave angle is larger than the critical wave angle`<br>전이점 upwind의 근거는 get_upwindcorrection.m:168~185이다. |

## 문서와 코드 차이 (10-12 대조)

문서 판: 매뉴얼 v1.0 2024-10-15, FAQ 2023-10-01, 논문 2018·2020. 코드 판: 원본 저장소 HEAD f3ec8638, 코드 파일은 7bf4481 2025-10-07과 같음.

문서 쪽 차이는 [manual-notes/shorelines-technical-manual-v1.md](../manual-notes/shorelines-technical-manual-v1.md#문서와-코드-차이-10-12-대조), [manual-notes/shorelines-faq-operational.md](../manual-notes/shorelines-faq-operational.md#문서와-코드-차이-10-12-대조), [manual-notes/shorelines-roelvink2020-frontiers.md](../manual-notes/shorelines-roelvink2020-frontiers.md#문서와-코드-차이-10-12-대조)의 표 참조.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:K001 | 중심 길이 하한과 끝점 방향 | — | functions/coastline_change.m:125 `eps=1e-3;`<br>functions/coastline_change.m:314 `COAST.ds(i)=hypot(COAST.x(ip1)-COAST.x(im1),COAST.y(ip1)-COAST.y(im1))/2;`<br>functions/coastline_change.m:315 `COAST.ds(i)=max(COAST.ds(i),eps);`<br>functions/coastline_change.m:367 `if COAST.preserveorientation==1`<br>functions/coastline_change.m:371 `COAST.dx(i)= dn*sind(COAST.PHIcxy0(i)); % no minus sign here`<br>functions/coastline_change.m:372 `COAST.dy(i)= dn*cosd(COAST.PHIcxy0(i));`<br>functions/coastline_change.m:373 `elseif i==1`<br>functions/coastline_change.m:374 `COAST.dx(i)= dn*sind(COAST.PHIcxy0(1)); % no minus sign here`<br>functions/coastline_change.m:375 `COAST.dy(i)= dn*cosd(COAST.PHIcxy0(1));`<br>functions/coastline_change.m:376 `elseif i==n`<br>functions/coastline_change.m:377 `COAST.dx(i)= dn*sind(COAST.PHIcxy0(end)); % no minus sign here`<br>functions/coastline_change.m:378 `COAST.dy(i)= dn*cosd(COAST.PHIcxy0(end));`<br>functions/coastline_change.m:392 `if COAST.cyclic`<br>functions/coastline_change.m:393 `x1=(COAST.x(n)+COAST.x(1))/2;`<br>functions/coastline_change.m:394 `y1=(COAST.y(n)+COAST.y(1))/2;`<br>functions/coastline_change.m:395 `COAST.x(1)=x1;`<br>functions/coastline_change.m:396 `COAST.y(1)=y1;`<br>functions/coastline_change.m:397 `COAST.x(n)=x1;`<br>functions/coastline_change.m:398 `COAST.y(n)=y1;` | C 문서 누락 | 중심 차분의 일치 범위는 내부점이며, 짧은 중심 길이와 고정·순환 끝점은 별도 처리를 쓴다. |
| R1:K029 | 공간 가변 격자와 재보간 위치 | — | functions/get_gridsize.m:42 `if isscalar(ds0)`<br>functions/get_gridsize.m:43 `ds0i=repmat(ds0,[1,length(x)]);`<br>functions/get_gridsize.m:48 `ds0i=get_interpolation_on_grid('weighted_distance',x,y,xg,yg,ds1);`<br>functions/get_gridsize.m:50 `ds0i_center=0.5*(ds0i(1:end-1)+ds0i(2:end));`<br>functions/make_sgrid_mc.m:114 `if max(ds./ds0imean>2)==1 \|\| max(ds./ds0imean<0.5)==1`<br>functions/make_sgrid_mc.m:144 `sn=round(sn0(ii)+sn0rest);`<br>functions/make_sgrid_mc.m:179 `if max(ds)>2*ds0 \|\| TIME.it==0`<br>functions/make_sgrid_mc.m:187 `ns=ceil(s0(end)/ds0);`<br>functions/make_sgrid_mc.m:188 `ds1=s0(end)/ns;`<br>functions/make_sgrid_mc.m:199 `if ds2<ds0/sqrt2 && snew(end)>=ds0/sqrt2`<br>functions/make_sgrid_mc.m:204 `elseif i==2 && ds2<ds0/4 && length(snew)>2`<br>functions/make_sgrid_mc.m:206 `elseif ds2<ds0/4`<br>functions/make_sgrid_mc.m:211 `elseif ds2>ds0*sqrt2`<br>functions/make_sgrid_mc.m:221 `snew(2:end-1)=COAST.smoothfac*snew(1:end-2)+(1.-2*COAST.smoothfac)*snew(2:end-1)+COAST.smoothfac*snew(3:end);`<br>functions/make_sgrid_mc.m:224 `x=interp1(s,x,snew);` | C 문서 누락 | 공간 가변 격자는 거리 가중 목표 크기와 양쪽 평균을 사용하며 재생성은 누적거리 좌표에서 수행한다. |
| R1:K042 | 돌제의 양측 우회 합성과 접점 이동 | — | functions/coastline_change.m:126 `epsgroyne=1;`<br>functions/coastline_change.m:144 `if GROYNE.QS(ig,1)<=0 & GROYNE.QS(ig,2)>=0`<br>functions/coastline_change.m:146 `GROYNE.QS(ig,:)=0;`<br>functions/coastline_change.m:147 `elseif (GROYNE.QS(ig,1)>=0 & GROYNE.QS(ig,2)>=0) \|\| (GROYNE.QS(ig,1)<=0 & GROYNE.QS(ig,2)<=0)`<br>functions/coastline_change.m:149 `[QSm,imx]=max(abs(GROYNE.QS(ig,:)));`<br>functions/coastline_change.m:150 `GROYNE.QS(ig,:)=GROYNE.QS(ig,imx);`<br>functions/coastline_change.m:151 `else % GROYNE.QS(ig,1)>=0 & GROYNE.QS(ig,2)<=0`<br>functions/coastline_change.m:153 `GROYNE.QS(ig,:)=sum(GROYNE.QS(ig,:),2);`<br>functions/coastline_change.m:239 `dnratio=1.5./(1-cosd(min(GROYNE.PHIdn(idgroyne,segmentside),180)));`<br>functions/coastline_change.m:240 `dnratio=1; %min(dnratio,1);`<br>functions/coastline_change.m:244 `COAST.dSds(p1)=(TRANSP.QS(pq2)-TRANSP.QS(pq1))/(COAST.ds(p1)/2);`<br>functions/coastline_change.m:245 `COAST.dndt(p1)=-COAST.dSds(p1)/COAST.h0(p1);                          % dndt in [m/yr] = alongshore gradient in sediment transport in [m3/yr/m] divided by 'active height' [m]`<br>functions/coastline_change.m:249 `dn=dnratio*(COAST.dndt(p1)+NOUR.growth*NOUR.rate_density(p1)/COAST.h0(p1)-CC.SLRo/COAST.tanbeta+FNOUR.q_tot(p1)/COAST.h0(p1))*TIME.dt;      % dndt in [m/yr] + nourishment in [m3/m/yr] divided by the active height [m]`<br>functions/coastline_change.m:253 `shard_tip=shard(GROYNE.tipindx(idgroyne,segmentside));`<br>functions/coastline_change.m:255 `if segmentside==2`<br>functions/coastline_change.m:256 `if max(GROYNE.s(idgroyne,segmentside)-dn,shard_tip)>max(shard)`<br>functions/coastline_change.m:257 `% extend structure if needed -> so the leg will be extended in landward direction`<br>functions/coastline_change.m:269 `GROYNE.s(idgroyne,segmentside)=min(max(GROYNE.s(idgroyne,segmentside)-dn,shard_tip),max(shard)-eps);`<br>functions/coastline_change.m:272 `if min(GROYNE.s(idgroyne,segmentside)+dn,shard_tip)<min(shard)`<br>functions/coastline_change.m:274 `sxt=min(GROYNE.s(idgroyne,segmentside)+dn,shard_tip)-min(shard)-epsgroyne;`<br>functions/coastline_change.m:277 `dxt=-sxt*dx/((dx.^2+dy.^2).^0.5);`<br>functions/coastline_change.m:278 `dyt=-sxt*dy/((dx.^2+dy.^2).^0.5);`<br>functions/coastline_change.m:285 `GROYNE.s(idgroyne,segmentside)=max(min(GROYNE.s(idgroyne,segmentside)+dn,shard_tip),min(shard)+eps);`<br>functions/coastline_change.m:289 `GROYNE.x(idgroyne,segmentside)=interp1(shard,xhard,GROYNE.s(idgroyne,segmentside));` | C 문서 누락 | 돌제 접점은 양측 우회 합성과 반 셀 구배 및 선단 제한·육측 다리 연장으로 별도 이동한다. |
| R2:U06 | S.xmc0 | — | functions/prepare_coastline.m:118 `COAST.x_mc0=S.xmc0;`<br>functions/prepare_coastline.m:113 `elseif ~isempty(S.xmc)`<br>functions/prepare_coastline.m:117 `try`<br>functions/prepare_coastline.m:119 `COAST.y_mc0=S.ymc0;`<br>functions/prepare_coastline.m:120 `catch`<br>functions/prepare_coastline.m:121 `COAST.x_mc0=S.xmc;`<br>functions/prepare_coastline.m:122 `COAST.y_mc0=S.ymc;` | C 문서 누락 | xmc0는 직접 좌표 입력 경로의 별도 초기 x 좌표다. |
| R2:U07 | S.ymc0 | — | functions/prepare_coastline.m:119 `COAST.y_mc0=S.ymc0;` | C 문서 누락 | ymc0는 xmc0와 함께 주는 초기 y 좌표다. |
| R2:K16 | 권고 격자 간격 | FAQ PDF 1쪽 / 인쇄 쪽 없음: `Typical grid cell size (S.ds0) of 50-100 m` | — | H 코드 대조 대상 아님 | 50–100 m는 FAQ의 전형 격자 간격이다. 코드의 필수 허용 범위로 쓰지 않는다. |

출처: [R1 §4·§5](../../../_staging/recovery/compare/ShorelineS-theory-vs-code.md#5-차이-결론), [R2 §4·§5](../../../_staging/recovery/compare/ShorelineS-inputs-vs-code.md#5-차이-결론), [R3 §7·§8](../../../_staging/recovery/flow/ShorelineS-callflow.md#8-차이-결론).

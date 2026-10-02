---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_secondorder.F90
lines: 1063
sha256: 33d588f751f2faffb02b0c97854a0a975f67ab7851492d7927c8ff68d545b3de
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# flow_secondorder.F90 — 판독 구간 기록

구간은 1행부터 1063행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | 모듈 머리말·2009년 작성 이력(1–11), `flow_secondorder_module`은 save·private(13–17), `nh_pars.inc` 포함(21). 할당형 작업 배열 `wrk1/2`와 용도 주석(26–33), `initialized=.false.`(35). advUV·advW·con·minmod·huhv 공개(37–41), contains(47). |
| 49–84 | `flow_secondorder_init`: McCormack 자원 초기화라는 주석(59), `spacepars` 인자(66–71). 두 작업 배열을 `(nx+1,ny+1)`로 할당·0 초기화하고 initialized=true(74–80). |
| 85–156 | `flow_secondorder_advUV`의 이력·의도·인자·지역 변수. 1차 Euler 예측 `s%uu/vv`와 단계 시작 `uu_old/vv_old`로 slope-limited 보정한다는 주석(113–115). 옛 속도 배열 크기는 nx+1·ny+1(124–125), 수심 제한·기울기·유량·계수 선언(130–151). |
| 157–204 | 첫 진입이면 init 호출(158–160). 기본 imin=2·imax=nx·jmin=2·jmax=ny, top/left이면 최소 3, bot/right이면 최대 nx−1/ny−1(163–189). ny>0이면 j 루프 2..ny, 1D이면 1..1(192–202). |
| 205–242 | z점 `qx*du` 보정: jmin1d..jmax1d·i=2..nx(207–209), wrk1=0 및 인접 인덱스 제한(211–215). `mindepth=minval(zs)-maxval(zb)`(216), `qx=.5*(qx(i)+qx(iw))*cos(alfau(i)-alfau(iw))`(218). mindepth>eps일 때 qx>0·i>imin이면 새/옛 속도 차 두 기울기의 minmod에 `0.5*dsu(iw)*qx`를 곱함(224–226); 음의 qx·i<imax+1이면 반대 시각 차와 음의 계수 사용(230–232). |
| 243–283 | ny>0일 때 c점 `qy*du`: j=2..ny·i=2..nx−1(245–249), wrk2=0, 인접 2×확장 구간의 mindepth(251–255). qy는 두 qy 평균×alfau 방향차 cos(259); 양·음 qy와 j 경계 조건에 따라 `±0.5*dnv*minmod(delta1,delta2)*qy`(261–271). `wrk2(:,1)=0`(280). |
| 284–308 | U 보정: 2D에서 uu 유효 범위, `fac=dt/hum*dsdnui`(287–291), `uu -= fac*(dnz(i+1)*wrk1(i+1)-dnz(i)*wrk1(i)+dsc(j)*wrk2(j)-dsc(j−1)*wrk2(j−1))`(292–293). 1D는 `uu(i,1)-=dt/hum*(wrk1(i+1)-wrk1(i))/dsu`(301–303). |
| 309–344 | V 보정은 ny>2일 때(310). j=2..ny·i=2..nx에서 wrk1=0, 확장 j 범위의 mindepth(312–321), `qy=.5*(qy(j)+qy(jn))*cos(alfav(j)-alfav(jn))*dsz`(323). 수심 조건 및 유량 부호·j 경계에 따라 `±0.5*dnv*minmod* qy`(325–337). |
| 345–387 | V의 x방향 보정: j=2..ny−1·i=2..nx, wrk2=0(345–349), 인접 범위 수심 검사·`qx=.5*(qx(j+1)+qx(j))*cos(alfav(i)-alfav(i+1))*dsc`(350–357). `qx>Umin` 또는 `<−Umin`에 따라 ds u의 j=1 값을 사용한 기울기·보정(359–366). `wrk2(1,:)=0`(371). `fac=dt/hvm*dsdnvi`, `vv-=fac*(wrk2(i)-wrk2(i−1)+wrk1(j+1)-wrk1(j))`(374–379), 루틴 끝(386). |
| 388–450 | `flow_secondorder_advW`: 비정수압 모듈과 함께 W 이류 2차 보정이라는 주석(406–407). spaceparams·parameters·xmpi 사용(413–415). inout w·입력 w_old·정수 마스크 mskZ는 nx+1×ny+1(424–426), 인덱스·계수·수심·기울기·유량 선언(431–444). |
| 451–487 | advW 기본 imin/jmin=1, imax=nx·jmax=ny, 물리 경계이면 최소 2·최대 nx−1/ny−1(452–478). 아직 초기화되지 않았으면 init 호출(481–486). |
| 488–535 | 2D W의 s방향 유량: 전체 wrk1=0, j=2..ny·i=1..nx, mskZ=0이면 cycle(488–501). `rfac=real(mskZ(ie)*mskZ(iee)*mskZ(iw))`, `qx=s%qx*dnu*rfac`(509–512). mindepth>eps, 유량 부호와 imin/imax 조건으로 새 w와 옛 w의 기울기 두 개를 minmod 제한하여 `±0.5*dsu*minmod*qx`(514–526). |
| 536–579 | 2D W의 n방향 유량: 전체 wrk2=0, j=1..ny·i=2..nx, 비활성 마스크 cycle(539–544). jn=min(j+1,jmax+1)·jnn=min(j+2,jmax+1)·js=max(j−1,1)(548–550). 마스크 곱과 `qy=s%qy*dsv*rfac`(552–555), 수심·유량 부호·j 경계별 `±0.5*dnv*minmod*qy`(557–569). |
| 580–618 | top/bot에서 wrk1의 1/nx행, left/right에서 wrk2의 1/ny열 0(581–600). zs 유효 범위에서 mskZ=0이면 건너뛰고 `w-=dt*dsdnzi*(wrk1(i)+wrk2(j)-wrk1(i−1)-wrk2(j−1))/hh`(606–612), 1D 분기 시작(618). |
| 619–657 | 1D W: j=1·i=2..nx, 비활성 마스크 cycle 후 현재 wrk1=0(622–627). ie/iee 최대 nx·iw 최소 1, 이웃 마스크 곱(629–633), `qx=s%qx*rfac`(636). mindepth>eps와 qx>0·i>2 또는 qx<0·i<nx−1에서 ds u 기울기와 `±0.5*dsu*minmod*qx`(638–650). |
| 658–685 | top/bot의 wrk1 경계 0(659–668). zs 유효 i 범위에서 마스크가 활성인 점만 `w(i,1)-=dt/hh*(wrk1(i)-wrk1(i−1))/dsz`(672–676), 분기·루틴 끝(680–682). |
| 686–735 | `flow_secondorder_con`의 연속방정식 보정 설명(700), s·par·옛 수위 zs_old 인자(705–713), 인접 인덱스·1D 루프 범위·수심·기울기 선언(719–731). |
| 736–773 | ny>0이면 j=2..ny, 아니면 j=1(736–742); 첫 진입 init 호출(746–748). x유량 보정 i=2..nx−1, wrk1=0·인접 인덱스·수심 검사(751–758). uu>umin·i>2이면 `wrk1=uu*0.5*dsu(i,1)*minmod`(759–762); uu<−umin·i<nx−1이면 앞쪽 옛 수위 기울기와 음의 계수(763–766). wrk1의 1·nx행 0(771–772). |
| 774–801 | ny>2이면 y유량 보정 j=2..ny−1·i=2..nx(775–777), 수심 검사(778–783). vv의 ±Umin 및 j 조건별 옛/새 수위 기울기 사용(784–791); 두 부호 분기 모두 `wrk2=vv*0.5*dnv(1,j)*minmod` 형태(787·791). 1·ny열 0(796–797); ny≤2는 전체 wrk2=0(798–800). |
| 802–827 | 수위 보정: 2D zs 유효 범위에서 `zs-=dt*((wrk1(i)-wrk1(i−1))/dsz(i,1)+(wrk2(j)-wrk2(j−1))/dnz(1,j))`(803–807), 1D는 x항만(810–812). 유량 유효 범위에서 qx에 wrk1, 2D qy에 wrk2를 추가(817–821). 루틴 끝(824). |
| 828–903 | `flow_secondorder_huhv`: 수위 2차 보정이라는 목적 주석(842), spaceparams·parameters·xmpi 및 s·par 인자(847–854), zs_old 선언은 주석(856). 기본 imin/jmin=1·imax=nx·jmax=ny, 물리 경계이면 최소 2·최대 nx−1/ny−1(876–902). |
| 904–939 | 2D hu 보정: uu 유효 범위(908–910), 인접 인덱스와 `mindepth=minval(zs)-maxval(zb)`(912–916). mindepth>eps·uu>umin·i>imin이면 `hu+=0.5*dsu(i,1)*minmod`(920–924), uu<−umin·i<imax이면 `hu-=0.5*dsu(i,1)*minmod`(926–930). 기울기는 현재 zs만 사용. |
| 940–970 | 2D hv 보정: vv 유효 j/i 범위(940–946), ie/iee/iw는 여기서 j 이웃 인덱스(942–944). 수심 조건(948–950), vv>umin·j>jmin이면 `hv+=0.5*dnv(i,j)*minmod`(952–956), 음의 vv·j<jmax이면 hv에서 같은 형태를 뺌(958–962). |
| 971–1005 | 1D huhv는 j=1, uu 유효 i 범위에서 인접 수심 검사(974–982). uu 부호·imin/imax 조건별 `hu +=/− 0.5*dsu(i,1)*minmod(delta1,delta2)`(984–994). hv 수정은 이 분기에 없다. 분기·루틴 끝(1001–1003). |
| 1006–1047 | pure 실수 함수 `minmod` 선언(1006). TVD 제한자이며 연속 기울기 부호가 반대면 보정을 0으로 한다는 설명(1020–1029), 부작용 없는 pure에 관한 주석(1031–1032). 입력 delta1·delta2 선언(1043–1044). |
| 1048–1063 | `delta1*delta2<=0`이면 0 반환·return(1048–1051). delta1>0이면 두 값의 min, <0이면 max, 그 외 0(1053–1059). 함수·모듈 끝(1060–1063). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 359–366: advUV의 V x방향 보정은 모든 j에서 `s%dsu(...,1)`을 사용한다.
- 760–766·785–791·806–807: con의 2D 보정도 `dsu(...,1)`·`dnv(1,...)`·`dsz(...,1)`·`dnz(1,...)`을 사용한다.
- 763–766·788–791: con의 음의 x유량 보정에는 선행 음수가 있으나 음의 y유량 보정에는 없다.
- 625–627: advW 1D에서 mskZ=0인 점은 wrk1을 0으로 대입하기 전에 cycle한다. 2D 경로에는 전체 wrk1 초기화(496)가 있으나 1D 분기에는 해당 전체 초기화가 없다.
- 435–438·548–550: advW의 jn/js 선언 주석은 각각 j+1/j−1이며 실제 대입도 그 방향이다. advUV의 jn/js 선언(136·138)은 각각 j−1/j+1이다.

---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90
lines: 1102
sha256: 50742b601cc8feccd513cf742ca772b6021f1d4f5ffe074c4e8ffc90907dd2b2
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# flow_timestep.F90 — 판독 구간 기록

구간은 1행부터 1102행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | `flow_timestep_module`은 private·save, `flow` 공개(1–7). 저작권·LGPL 2.1 머리말(8–33). parameters·spaceparamsdef·xmpi·경계조건·2차 보정·비정수압·바닥거칠기·수직구조·강우·dFill 의존 선언(34–44). |
| 46–73 | flow 인자 s·par(48–49), 저장형 옛 속도/수위·보간 속도·기울기·파향 배열 선언(53–58·67). `fcvisc=0.1d0`, `facdel=5.d0`, `facdf=1.d0`, `swglm=0`(68·71), 응력·가속도·인덱스 선언(59–71). |
| 74–123 | vsu 미할당 시 작업 배열을 nx+1×ny+1로 할당(74–86). secorder=1 또는 NONH면 vv_old·uu_old·zs_old 할당 및 현재 값 복사(88–92). 보간 속도·이류·점성·셀 중심 속도 등을 0으로(94–117), `fc=2*wearth*sin(lat)`(118). `bedroughness_init` 호출과 sglobal 초기화에 쓰지 말라는 주석(120–121). |
| 124–150 | ny=0이면 j1=1, 그 외 2(125–129); 수직 유량 경계 `discharge_boundary_v` 호출(132). uu 유효 범위에서 `dzsdx=(zs(i+1)+ph(i+1)-zs(i)-ph(i))/dsu`(137–139); ny>0일 때 vv 범위에서 같은 y방향 차/dnv(143–146). |
| 151–180 | 점성용 `dudx=(uu(i)-uu(i−1))/dsz`(153–155), top 경계 0(159–161). ny>2면 `dvdy=(vv(j)-vv(j−1))/dnz`·left 경계 0(162–171), 아니면 전체 dvdy=0(172–174). `bedroughness_update` 호출(177). |
| 181–212 | U의 x이류: ududx=0, 왼쪽 유입 `qin=.5*(qx(i)+qx(i−1))`(185–186), 각도 회전 `uin=uu(i−1)*cos(dalfa)+vu(i−1)*sin(dalfa)`(188–189). 속도차>eps_sd이면 평균 속도×속도차×dnz×dsdnui(192), 아니면 qin/hum×속도차×같은 기하계수(195). 오른쪽은 qin=−.5*(qx(i)+qx(i+1)), 회전한 이웃값 및 에너지 분기 앞의 음수(198–207). |
| 213–245 | par%ny>0에서 U의 y이류 vdudy 초기화(213–215). 아래/위 유입 qin은 이웃 qy 평균 및 그 음수(216·228), uin은 alfau 방향차로 회전(218–219·230–231). vv 차>eps_sd이면 평균 vv를 사용한 에너지 항(220–222·232–234), 그 외 qin/hum의 운동량 항(225·237); dsc·dsdnui로 계량. else는 이미 0이라는 주석만(242–244). |
| 246–289 | right 여부·ny로 지역 jmax를 정함(249–255), 전체 vdvdy=0(256). par%ny>0에서 vv 유효 범위를 반복(258–260), 유입 qy 평균과 음수(261·273), `vin=vv(이웃)*cos(dalfa)-uv(이웃)*sin(dalfa)`(264·276). vv 차>eps_sd는 평균 vv 에너지 항, 그 외 qin/hvm 항; dsz·dsdnvi 사용(265–282). |
| 290–315 | ny>0의 물리 측면 경계 vdvdy: left는 j=1에서 위쪽 qin=−.5*(qy(1)+qy(2))만 반영(292–299), right는 j=ny에서 아래쪽 qin=.5*(qy(ny)+qy(ny−1))만 반영(303–310). 둘 다 qin>0에서 회전한 vin과 qin/hvm·dsz·dsdnvi 사용. |
| 316–364 | 전체 udvdx=0(316). 2D에서 vv 유효 범위, x 양쪽 qx 평균·방향 회전 vin(319–324·333–336), uu 차>eps_sd일 때 평균 uu 에너지 항(325–327·337–339), 그 외 qin/hvm 운동량 항(330·342), dnc·dsdnvi 사용. 1D는 qin=qx(i−1,1)·−qx(i,1)로 같은 회전·운동량 항만 적용(348–359). |
| 365–406 | viscosity=0이면 nuh·viscu=0(366–368). 그 외 smag=1이면 `visc_smagorinsky`, 아니면 nuh=par%nuh(372–377). swave=1·smag=0이면 `nuh=max(nuh,nuhfac*hh*(DR/rho)^(1/3))`(380–387). swave=0·NONH의 nhbreaker 1은 breaking≠0에서 breakviscfac 배, 2는 breaking=1에서 `(nuh*breakvisclen*hh)^2*sqrt(dudx^2+dvdy^2)` 추가(388–397); 3·default는 주석만(398–404). |
| 407–451 | U 점성 x항: 인접 `nuh*hh*Δuu/dsz` 응력 차에 `2/(dsz(i)+dsz(i+1))/hum`(408–413). smag=1이면 전체 viscu 두 배(417–435); 변동 점성 응력식과 상수 점성식 주석(419–432). y항은 네 셀 nuh 평균, hvm 평균·Δuu/dnc의 차를 hum으로 나누고 인접 wetu 곱으로 제한(437–448). |
| 452–470 | smag=1의 U 교차응력: nuh 네 점 평균(458–459), hvm 평균×Δvv/dsc(461–462), 차/dnz/hum 및 네 wetv 마스크 곱으로 viscu에 추가(463–464). endif 주석에는 ny>0도 적혀 있으나 if 조건은 smag만(452·467). |
| 471–495 | V 점성 y항: viscv 전체 0(471), 인접 `nuh*hh*Δvv/dnz` 차를 hvm·평균 dnz로 나누고 wetv 곱(472–478). ny>0이면 left의 열1을 열2로, right의 열ny를 열ny−1로 복사(482–488). smag=1이면 전체 viscv 두 배(492–494). |
| 496–531 | `s%nuh=par%nuhv*s%nuh`로 배열 자체를 배율 변경(496). V x항은 네 점 nuh·두 점 hum 평균×Δvv/dsc의 차/hvm, 이웃 wetv 곱(497–508). smag=1은 Δuu/dnc 교차응력 차/dsz/hvm을 추가하며 마스크는 wetu 세 개와 wetv 하나(512–525). 점성 분기 끝(530). |
| 532–558 | 바닥 마찰: wetu=1에서 `taubx=cfu*rho*ueu*sqrt((1.16*urms)^2+vmageu^2)+taubx_add`, 그 외 0(534–539). 절댓값을 `100*g*rho*hu`로 제한(543–545). y도 cfv·vev·vmagev·tauby_add·hv로 같은 계산·제한(549–557). |
| 559–592 | U Euler 단계: 젖은 uu 범위에서 `dudt=ududx+vdudy-viscu+g*dzsdx+taubx/(rho*hu)+Fvegu/(rho*hu)-lwave*Fx/(rho*hum)-fc*vu-rhoa*Cd*windsu*sqrt(windsu^2+windnv^2)/(rho*hum)`(561–570). ±maxfacg*g로 제한한 뒤 `uu-=dt*dudt`, 마른 점 0(571–579). ny>0의 물리 left/right에서 uu 측면 열을 내부 열로 복사(583–590). |
| 593–629 | V Euler 단계: 젖은 점 `dvdt=udvdx+vdvdy-viscv+g*dzsdy+tauby/(rho*hv)+Fvegv/(rho*hv)-lwave*Fy/(rho*hvm)+fc*uv-rhoa*Cd*windnv*sqrt(windsu^2+windnv^2)/(rho*hvm)`(595–606). ±maxfacg*g 제한·vv 갱신, 마른 점 0(607–615). left는 `flow_lat_bc(...,par%right,1,2,...)`, right는 `(...,par%left,ny,ny−1,...)`(621–627). |
| 630–659 | USEMPI에서 uu·vv shift(630–633). NONH이면 `nonh_cor(...,0,uu_old,vv_old)` 예측 후 shift(635–643). secorder=1이면 `flow_secondorder_advUV` 및 shift(645–652). NONH 압력 보상 `nonh_cor(...,1,...)` 호출, 내부 MPI shift라는 주석(654–658). |
| 660–683 | 연속식용 hu를 전체 격자에서 upwind 재계산(661–662). uu>umin이면 oldhu=1의 hh(i), 아니면 zs(i)−양쪽 바닥 max(664–669). uu<−umin이면 다음 셀 수위/수심 사용(670–675). 작은 속도는 양쪽 최대 수위−최대 바닥과 eps의 max(676–678). 끝에 전체 hu≥0 제한(682). |
| 684–713 | hv도 전체 격자에서 vv 부호·oldhu로 현재/다음 j 셀 수위 또는 hh 선택(684–698); 작은 속도는 양쪽 최대 수위−최대 바닥을 eps 이상으로(699–701), hv≥0(704). secorder=1에서 `flow_secondorder_huhv` 호출(706–712). |
| 714–732 | `qx=uu*hu`, `qy=vv*hv`(715·719), 출력용 `qmag=sqrt(qx^2+qy^2)`(721–722). `discharge_boundary_h` 호출(726), rainfall=1이면 `rainfall_update` 호출(729–731). |
| 733–765 | 2D zs 유효 범위에서 `dzsdt=−(qx(i)*dnu(i)-qx(i−1)*dnu(i−1)+qy(j)*dsv(j)-qy(j−1)*dsv(j−1))*dsdnzi-infil+rainfallrate`, `zs+=dzsdt*dt`(735–744). 1D는 x유량만(745–752). secorder 분기의 `flow_secondorder_con` 호출은 주석이며 2014년 감쇠 때문에 제거했다는 설명(754–759). USEMPI zs shift(762–764). |
| 766–800 | secorder 또는 NONH면 vv_old·uu_old·zs_old를 갱신(767–771). 셀 중심 u는 인접 uu 평균, top은 uu(1), bot은 u(nx) 복사(776–783). 2D v는 인접 vv 평균, 측면 복사 및 nx+1행에 nx행 복사(785–794); 1D v=vv(795–797). |
| 801–854 | `sinthm/costhm=sin/cos(thetamean-alfaz)`(802–803). U점의 V속도 vu는 2D 네 vv 평균·1D 두 vv 평균, 측면 복사 및 wetu 마스크(806–821). V/U Stokes 성분 vsu/usu는 두 x이웃 ust에 sin/cos를 곱한 평균(824–825·833–834·840–841·849–850), 측면 복사·wetu 적용(826–831·837·842–847·853). |
| 855–877 | `veu=vu-vsu`, `ueu=uu-usu`(856–858). sedtrans=0이면 vmagu, 항상 vmageu를 두 성분 제곱합 제곱근으로 계산(860–864). 셀 중심 ue는 ueu 평균 및 첫 행 복사(867–868). 셀 중심 ve는 이 시점의 vev 평균 또는 1D vev 복사(871–876). |
| 878–924 | V점 U속도 uv: 2D 네 uu 평균·1D 두 uu 평균(879–880·887), right 외곽 열 복사·wetv 적용(883–892). V점 Stokes vsv/usv는 두 y이웃 ust×sin/cos 평균(895–896·911–912), 측면 열 복사; 1D는 ust×sin/cos(904·920). 둘 다 wetv 적용(908·923); 채워야 할 경계에 관한 주석(889–891·906·922). |
| 925–955 | `vev=vv-vsv`, `uev=uv-usv`(926–928). sedtrans=0이면 vmagv, 항상 vmagev 계산(930–934). hold에 옛 hh 복사, `hh=max(zs-zb,eps)`, `zs1=zs-zs0`(938–941). wetz=1에서 maxzs>dFill+1이면 최대/최소 수위 누적, 아니면 둘 다 현재 zs로 초기화(943–950); zswet은 젖은 점 zs, 마른 점 dFill(951–954). |
| 956–989 | nz>1·form≠VANRIJN1993에서 전체 격자 루프(957–959). 젖은 셀 `ks=12*hh/10**(sqrt(g/cfu)/18)` 및 바람 응력 계산(960–964), `vsm_u_XB`에 Euler 속도·수심·파랑·응력·계수·수직 배열을 전달(966–972). 마른 셀은 uz·vz·ustz·nutz·ue_sed·ve_sed 0(973–979). 해당 조건이 아니면 ue_sed=ue·ve_sed=ve(983–985), flow 끝(988). |
| 990–1046 | `visc_smagorinsky` 의존·이력·선언. 설명식 `nuh=C^2*dx*dy*Tau`, `Tau=sqrt(2)*sqrt((du/dx)^2+(dv/dy)^2+.5*(du/dy+dv/dx)^2)`(1015–1017); C≈0.15는 par%nuh로 지정한다는 주석(1022). s·par 인자, 네 기울기·Tau·셀 면적 l 선언(1027–1039), MPI 인덱스 확인 주석(1046). |
| 1047–1064 | ny>2: zs 유효 범위에서 dudx·dvdy 차분과 두 이웃 평균 dudy·dvdx(1048–1053). `Tau=sqrt(2*dudx^2+2*dvdy^2+(dvdx+dudy)^2)`, `l=1/dsdnzi`(1054–1055). `nuh=par%nuh^2*l*Tau*real(wetu(i)*wetu(i−1)*wetv(j)*wetv(j−1),8)`(1061). 쇄파 점성과의 관계에 관한 주석·대안식은 비실행(1056–1060). |
| 1065–1087 | ny≤2: j=max(ny,1)·유효 i 범위(1067–1069), x방향 dudx·dvdx와 `Tau=sqrt(2*dudx^2+dvdx^2)`(1071–1073). dy>−1이면 `l=dsz*dy`, 아니면 dsz²(1075–1079). `nuh=par%nuh^2*l*Tau*real(wetu(i)*wetu(i−1),8)`(1083). |
| 1088–1102 | USEMPI nuh shift(1088–1090), ny>0의 left/right 외곽 열 복사(1092–1095), top/bot 외곽 행 복사(1097–1098). Smagorinsky 루틴·모듈 끝(1100–1102). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 249–255·259: 지역 jmax를 대입하지만 바로 뒤 vdvdy 루프의 끝은 jmax_vv이다. 지역 jmax는 이 파일의 나머지 실행문에서도 사용하지 않는다.
- 366–368·471·600: viscosity=0 분기는 nuh·viscu만 0으로 대입한다. 매 단계 전체 viscv=0은 viscosity의 else 내부(471)에 있으며 V 운동량식은 viscv를 사용한다(600).
- 452·467: U 교차응력의 실행 조건은 smag==1만이고 endif 주석에는 `smag ==1 and s%ny>0`이 적혀 있다.
- 496: V의 x방향 점성항 전에 nuhv를 작업 계수에만 곱하지 않고 s%nuh 배열 전체에 곱해 저장한다.
- 525: V 교차응력 마스크는 `wetu(i,jp1)*wetu(i,j)*wetu(i−1,jp1)*wetv(i−1,j)`로 마지막 인자만 wetv이다.
- 754–759·770: 2차 연속식 보정 호출은 주석 처리되어 있지만 zs_old에는 단계 끝 수위를 계속 복사한다. 이 파일 안에서 zs_old를 사용하는 실행 호출은 없다.
- 872–875·926: 셀 중심 ve는 vev의 이번 단계 재계산(926)보다 먼저 계산된다.
- 68·71·966–972: 수직구조 호출 계수 fcvisc=0.1·facdel=5·facdf=1·swglm=0은 지역 선언에 하드코딩되어 있다.

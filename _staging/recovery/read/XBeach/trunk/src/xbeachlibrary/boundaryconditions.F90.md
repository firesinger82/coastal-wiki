---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90
lines: 2324
sha256: 0cbaa20cd8dd147005ec6b01d13ec05ac46bb98d181e0a7fec1025cd9fe30b71
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# boundaryconditions.F90 — 판독 구간 기록

구간은 1행부터 2324행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `boundaryconditions` 모듈. `slen`·`pi` 사용, `save`·`private`, 공개 루틴은 `flow_lat_bc`, `wave_bc`, `flow_bc`, 두 discharge 루틴(7). |
| 9–50 | `wave_bc(sg,sl,par)` 시작, 저작권·LGPL 머리말(10–35), 보간·분산·스펙트럼 경계·로그·MPI 모듈 의존성. MPI일 때 `space_distribute` 사용(46–48). |
| 51–94 | 경계 파일의 시간·레코드·배열을 `save`로 보존. `bccreated=.false.`는 선언 시 초기화(88). 기본 포인터 `s=>sl`, 비MPI는 `s=>sg`(90–93). |
| 95–125 | 최초 `fac1` 미할당 시 경계 배열 할당. `L0=g*Trep**2/2/px`, `L=L0`, `wbw=2*px/Trep`(106–112). 매 호출 `startbcf=.false.`, 최초 생성 때만 참·`bcendtime=huge(0.0d0)`·`newstatbc=1`(117–125). |
| 126–166 | TS_1: unit 7의 `bc/gen.ezs`에서 `*` 머리말을 건너뛰고 `nt`, `tE,dum,dataE`를 읽음(130–153); MPI broadcast, `Emean=sum(dataE)/nt`, `dispersion(par,s,s%hh)`(164–165). |
| 167–205 | TS_2: 같은 파일에서 `tE,databi,dataE`를 읽고 세 값 broadcast(189–197). 파일 닫기 후 `Emean=sum(dataE)/nt`·`dispersion`(203–204). |
| 206–237 | stationary JONS_TABLE: `Hm0,Trep,dir0,dum1,spreadpar,bcendtime,dum2` 읽기(209). `Hrms=Hm0/sqrt(2)`, `m=int(2*spreadpar)`, morfacopt=1이면 종료시간을 `max(morfac,1)`로 나눔. `theta0=1.5*px-dir0*atan(1)/45`, −px..px로 감쌈(216–222). `sigt=2*px/Trep`, 평균 `sigm`, `dispersion`(232–236). |
| 238–275 | 비stationary PARAMETRIC/JONS_TABLE·SWAN·VARDENS는 master에서 `spectral_wave_bc`(241·244·247). REUSE는 `curline=1`(250). TS_NONH는 master에 ny+1, 나머지에 1개 길이 U/V/Z/W/dU/dV 배열을 할당하고 `velocity_Boundary('boun_U.bcf',...)`(271–272). |
| 276–303 | 비스펙트럼 방향분포 `dist=cos(theta-theta0)**m`, cos<0이면 0(279–283). TS 계열 `Hrms=sqrt(8*Emean/(rho*g))`. `E0=rhog8*Hrms**2`, 합>0일 때 `factor=dist/sum(dist)/dtheta`, 아니면 0; `e01=max(factor*E0,0)`, `Llong=Tlong*cg(1,1)`(286–297). |
| 304–350 | `t>=bcendtime`이면 경계 갱신. stationary JONS_TABLE은 종료시간이 t를 넘을 때까지 다음 조건을 읽음(314–336); `taper=0`(321), 기간을 morfac에 따라 누적. 각주파수·`sigm` 갱신 후 `dispersion`(346–350). |
| 351–400 | 새 stationary 조건의 방향분포·`e01` 재계산(352–366). 스펙트럼 계열은 unit 71/72를 닫고 `spectral_wave_bc` 후 `startbcf=.true.`. REUSE도 닫고 참으로 설정, `t<=tstop-dt`일 때만 `curline++`(387–394). MPI에서 startbcf broadcast(397). |
| 401–423 | stationary 현재 단계: PARAMS/JONS_TABLE만 처리. 새 조건이면 `ee=0`; `taper>tiny(0)`일 때 `e01*min(t/taper,1)`, 아니면 e01 그대로(408–417). `bi(1)=0`, `ui(1,:)=0`(418–419). |
| 424–438 | surfbeat 이색파: PARAMS·`Tlong/=-123`·top 조건(426). `ee=e01*0.5*(1+cos(2*px*(t/Tlong-공간위상/Llong)))*min(t/taper,1)`(428–431). `bi=-(2*cg/c-0.5)*(em-ei)/(cg**2-g*hh)/rho`(434), `ui=cg*bi/ht*cos(theta0-alfaz)*lwave*(order-1)`(436). |
| 439–455 | surfbeat TS_1: 평균 격자각과 theta0 차<1e-3이면 현재 t, 아니면 공간 지연시간을 0 이상으로 제한해 `linear_interp`(441–446). `ee=e01*E1/max(Emean,0.000001)*taper계수`, 이색파와 같은 bi 식, `ui=cg*bi/ht*cos(theta0-alfaz)`(448–453). |
| 456–475 | surfbeat TS_2: E와 사용자가 준 bi를 같은 시간으로 보간(460–466). `freewave==1`이면 `ui=sqrt(g/ht)*bi`, 아니면 `cg*bi/ht*cos(theta0-alfaz)*min(t/taper,1)`(469–473). |
| 476–515 | surfbeat 스펙트럼 계열의 최초/새 파일: `ebcflist.bcf`·`qbcflist.bcf`, single_dir+REUSE 때 `esbcflist.bcf`를 열고 curline까지 메타데이터 읽음(482–503). 마지막 경우 `reclen=wordsize*(sg%ny+1)*sg%ntheta_s`, 단일방향 스펙트럼 첫 레코드 `sg%ee_s` 읽기(506–513). |
| 516–554 | 시간·주기·파고·방향·E 파일명을 broadcast, single_dir 배열 분배(517–531). 목록을 닫고 `sigt`·`sigm`·분산 갱신(540–544). master가 E는 `(ny+1)*ntheta`, q는 `(ny+1)*4` 단위 직접접근 파일을 unit 71/72로 열음(547–551). |
| 555–596 | master 전역 q/E 배열, 다른 rank 주소용 길이 1 배열, 로컬 ny+1 배열 할당(556–570). E/q의 레코드 1·2를 읽고 `ier+ier2` 검사(572–580); 분배 또는 대입. `old=floor(t/dtbcfile+1)`, `recpos=1`(594–595). |
| 597–654 | `new=floor(t/dtbcfile+1)`이 old와 다르면 레코드 위치 전진. 여러 단계 건너뛰면 두 시간 레코드를 모두 읽어 분배(602–625); 비MPI 대입은 `q1=gq2; q2=gq2`(629–630). 한 단계면 이전의 2를 1로 옮겨 새 2만 읽음(633–650). 마지막 `old=new`(653). |
| 655–668 | `ht=zs0-zb`, `tnew=dble(new)*dtbcfile`; E·q 선형 시간보간(655–660). `ui=(qx*cos(alfau)+qy*sin(alfau))/ht*taper계수`, `vi=(-qx*sin(alfau)+qy*cos(alfau))/ht*taper계수`(662–663), E도 taper 적용(664). |
| 669–708 | NONH PARAMS: `iteratedispersion`으로 L 갱신, `kbw=2*px/L`, `arms=Hrms/2`(672–678). order=1은 정현 수위와 선형 속도, order=2는 `zi=arms*(cos(kxmwt)+kbw*arms*(3-tanhkhwb**2)/(4*tanhkhwb**3)*cos(2*kxmwt))`, `ui=(wbw/kbw)/hh*zi*cos(theta0-alfaz)`(693–696). order=3은 주석뿐(697–700). 2층 모델이면 dUi/dVi=0, `nonh_init_wcoef` 호출(702–707). |
| 709–755 | NONH 스펙트럼 첫 파일: `nhbcflist.bcf`에서 시작·끝 시간·Trep·Hrms·파일명 읽기(713–720), U 등 배열 할당. `nh_reuse.bcf`만 `bcst=bcstarttime`을 더하도록 `velocity_Boundary(...,force_init=.true.)` 호출(741–753). |
| 756–793 | NONH 첫 스펙트럼의 여섯 배열 분배/대입, 설정 flag·bcendtime broadcast(757–776). 미지정 U/V/dU/dV는 0, Z/W는 내부 `zs(2,:)`·`ws(2,:)`(778–790); V 입력 존재를 `isSet_Vbc=0/1`로 기록. `nonh_init_wcoef`(792). |
| 794–845 | NONH 스펙트럼 일반 단계의 `velocity_Boundary`, reuse만 bcst 지정(798–806). 분배와 flag broadcast 또는 대입 후 첫 단계와 같은 미지정 값 처리(809–844); 이 분기에는 `nonh_init_wcoef` 호출 없음. |
| 846–867 | 임시 U/V/dU/dV 배열을 로컬 ny+1로 할당·복사(847–857). 격자 회전 `ui=tempu*cos(alfau)+tempv*sin(alfau)`, `vi=-tempu*sin(alfau)+tempv*cos(alfau)`, dUi도 회전(859–861). taper는 ui·zi·wi·dUi에 적용(863–866). |
| 868–916 | NONH TS_NONH는 `boun_U.bcf` 읽기. MPI는 배열·U/Z/W/dU/dV flag 분배(874–884). 비MPI만 Q 입력을 `uig/s%hu`로 속도화하며 2층 차유량 식 `duig=((1-2*nhlay)*uig+duig)/(2*nhlay*hu*(1-nhlay))`(886–898). 미지정 값 및 `isSet_Vbc` 처리(900–912). |
| 917–929 | wave_bc 마무리: `ee(1,:,:)=swave*ee(1,:,:)`; `nonhspectrum<=0`이면 전체 `ui=lwave*(order-1)*ui`(919–922). 유동 경계 절 머리말. |
| 930–962 | `flow_bc` 선언. `tide_boundary_timestep`, `linear_interp`, 공간 파라미터 및 조건부 MPI 의존성. 수심·Riemann 변수 beta·경계 평균·hybrid 조석 통계와 계수를 save로 보존(949–959). |
| 963–1008 | 최초 ht 등 할당; instant/hybrid만 zs0old 할당(979–983). `zsmean`은 front와 nx 수위로, hotstart=0이면 umean/vmean은 현재 속도로 초기화(986–992). hybrid `hybf1=hybf2=0`, 평균시간 `3*cats*Trep`, 임계값 0.10/0.90, 극값 ±huge·평균 0(996–1007). |
| 1009–1045 | ny=0이면 j1=1, 아니면 2(1011–1015). epsi<0·swave=1·hybrid 때 평균시간까지 front/back 극값과 dnz 가중 평균을 누적. min 갱신은 이전 min 대신 `hybmaxzs`·`hybmaxzs0`를 인수로 사용(1023·1025·1036·1038). `hybtavgtot+=dt`(1044). |
| 1046–1096 | hybrid 상대오차 `abs(meanzs-meanzs0)/min(huge(0),max(maxzs-minzs,maxzs0-minzs0))`(1049·1063). <0.1이면 계수 0, >0.9면 1, 사이에는 `0.5-0.5*cos((err-ll)*px/(hl-ll))`. 통계·시간 재초기화(1075–1085), MPI_MAX로 계수 동기화(1090–1091). |
| 1097–1135 | instant/hybrid: 이전 zs0·모서리 수위 저장 후 `tide_boundary_timestep`(1099–1105). wetz=1·zb<zs0이며 front 또는 back까지 젖은 연결이 있을 때만 dzs0 반영(1113–1114), 증가/감소를 네 모서리 조석 변화 극값으로 제한(1118–1122). `ccg*=max(zs-zb,eps)/max(zs+dzs0-zb,eps)`, cmax 제한 후 zs 증가(1123–1127). 다른 조석형도 tide 호출(1133). |
| 1136–1183 | epsi<0이면 factime: velocity는 `dt/(cats*Trep)`, hybrid는 hybf1배, 다른 형은 0.1배; swave=0이면 `dt/60`. epsi>=0이면 그 값(1138–1154). velocity/hybrid·factime>0만 front u/v를 경계 길이 가중 합 및 MPI_SUM으로 평균해 `factime*현재+(1-factime)*이전` 갱신; 그 외 평균속도 0(1158–1181). |
| 1184–1201 | MPI에서 입사 ui/vi/zi/wi를 양쪽 Y방향으로 `xmpi_shift`(1187–1195). `wbctype/=OFF`이며 top rank에서 front 장파 경계 실행(1198–1201). |
| 1202–1221 | FRONT_ABS_1D: freewave면 `uu=2*ui-sqrt(g/hh)*(zs(2)-zs0(2))+umean`, 아니면 입사 계수 `1+sqrt(g*hh)/cg`(1206–1209). vv·zs·nonh ws는 인접값. WAVEFLUME은 velocity 조석 때 zsmean을 factime으로 갱신하고 반사 수위차 기준을 zsmean으로 사용(1215–1221). |
| 1222–1249 | FRONT_ABS_2D: `ht=max(zs0-zb,eps)`, `beta=uu-2*sqrt(g*hum)`(1223–1224). u점 x기울기, ny>0에서 Y 중앙기울기(1233–1234), 1D면 Y항 0. `bn=-(uu-sqrt(g*hum))*dbetadx-vu*dbetady+sqrt(g*hum)*dvdy+g*dhdx+Fx/(hum*rho)-cfu*sqrt(uu**2+vu**2)*uu/hum`(1242–1247). |
| 1250–1282 | `thetai=atan(vi/(ui+1e-16))`, `betanp1=beta+bn*dt`, 반사각 초기값 `-(theta0-alfaz)`(1251–1257). 최대 50회, freewave는 sqrt(gh), 그 외 cg로 입사 항을 보정해 ur 산출(1263–1271). `vert=vu-vmean-vi`, 새 각=atan(vert/(ur+1e-16)), ±pi/2 보정·각차<0.001이면 종료(1275–1280). |
| 1283–1301 | ARC=0이면 `uu=(order-1)*ui+umean`, zs 복사. 그 외 ur까지 더하고 Riemann 수위값의 `1.5*첫값-0.5*두번째값` 외삽(1288–1292); 고차식은 주석(1294–1296). vv 및 nonh ws는 인접값(1300–1301). |
| 1302–1342 | FRONT_WALL: uu=0·zs 인접값(1305–1306). FRONT_NONH_1D는 ARC=0일 때 지정 ui/vi·`zi+zs0`·wi, ARC 사용 때 `uu=ui-sqrt(g/hh)*(zs(2)-zi-zs0(2))+umean`, zs/ws 인접값(1310–1336). 2층은 dU=dui. V 입력 없으면 vv 인접값(1338–1340). |
| 1343–1366 | front의 좌우 모서리 속도는 인접값, 수위는 dzs0dn*dnv 보정 및 zb 하한(1345–1352). back 준비에서 hybrid factime을 `hybf2*dt/(cats*Trep)`로 바꿈(1363–1365). |
| 1367–1393 | back u/v도 nx 경계의 dnu/dnv 가중 합과 MPI_SUM 후 factime 평균(1370–1387). 비활성 조건이면 `umean(nx,:)=vmean(nx,:)=0`(1389–1392). |
| 1394–1425 | back wall은 uu(nx)=0·zs(nx+1)=zs(nx). ABS_1D는 `sqrt(g/hh)*(zs-max(zb,zs0))+umean`(1400). ABS_2D는 ht 하한 eps, `beta=uu+2*sqrt(g*hum)`(1403–1405). wetu=1 셀에서 기울기·힘·마찰로 bn 계산(1408–1422); Y기울기는 j±1을 사용(1410·1413). |
| 1426–1455 | 젖은 back 셀에서 `betanp1=beta(2)+bn*dt`, alpha 초기 theta0, 최대 50회 반사각 반복·오차<0.001 종료(1428–1445). `uu=ur+umean`, zs(nx+1)는 1.5/−0.5 외삽(1448–1451). |
| 1456–1486 | back 바깥 u/v 인접값 복사, 좌우 모서리 수위 보정은 `dzs0dn(1,...)`·`dnv(1,...)`·`zb(1,...)` 사용(1462·1467). 측면 조석 경계는 i별 `zs(i,1)=max(zs(i,2)-dzs0dn(i,1)*dnv(i,1),zb(i,1))`, 오른쪽은 더함(1477·1480). |
| 1487–1496 | 비정상 풍속(`windlen>1`)만 x/y 시계열을 `LINEAR_INTERP`로 현재시간 보간(1489–1490); 격자각 alfau·alfav에 따라 windsu·windnv 회전(1491–1493). flow_bc 끝. |
| 1497–1522 | `flow_lat_bc` 함수는 nx+1 길이 vbc 반환. 초기 t<=dt일 때만 save Coriolis `fc=2*wearth*sin(lat)`(1514). ny=0이면 wall만 0, 나머지는 기존 vv 그대로(1516–1521). |
| 1523–1545 | 2D LR_WALL은 vbc=0. LR_NEUMANN_V의 수위기울기 보정 유도식은 주석(1528–1544), 실제 식은 `vbc(:)=vv(:,jn)`(1545). |
| 1546–1571 | LR_NO_ADVEC: wetv 셀 `advterm=udvdxb+vdvdyb-viscvb+fc*uv`(1551). vv 부호에 맞춰 max/min/0로 제한해 감소 방향 항만 유지(1552–1558). `vbc=vv-dt*(advterm+g*dzsdy+tauby/(rho*hvm)-lwave*Fy/(rho*hvm)-바람항)`(1559–1563). 마른 셀 0, 양끝은 이웃값*wetv. |
| 1572–1607 | LR_NEUMANN은 제한 없이 이류·점성·압력·마찰·파력·fc*uv·풍력으로 vbc 갱신(1577–1582). LR_ABS_1D는 `sqrt(g/hh(i,jn))*(zs(i,jn)-max(zb(i,jn),zs0(i,jn)))*(jbc-jn)`, 경계 zs를 이웃으로 복사(1594–1595). 두 형 모두 마른 셀 0·양끝 이웃값*wetv; select에 default 없음(1603). |
| 1608–1651 | `discharge_boundary_h`: 선 유량 경계의 전역→로컬 shift는 MPI일 때 is/js−1, 아니면 0(1628–1634). 로컬 zs 유효범위를 물리 경계 rank에서 1칸 확장(1635–1650). |
| 1652–1682 | pntdisch=0만 `linear_interp`로 qnow 계산(1654–1657). 두 끝점 좌표를 shift해 하나라도 로컬 유효범위이면 indomain(1670–1673). 좌표는 m=1..nx, n=1..ny로 제한(1675–1678), A=0. |
| 1683–1717 | n1=n2 선: 측면 물리경계면 q 부호·hv를 유입 방향으로 조정(1686–1697). `A=sum(hv**1.5*dsv)`·MPI_SUM(1700–1704). `CONST=qnow/max(A,eps)`, `vv=CONST*sqrt(hv)`, `qy=CONST*sqrt(hv)*hv`(1713–1715). |
| 1718–1756 | m1=m2 선은 front/back 물리경계에서 부호·hu 조정(1721–1732). `A=sum(hu**1.5*dnu)`·MPI_SUM, `uu=CONST*sqrt(hu)`, `qx=CONST*sqrt(hu)*hu`(1735–1750). 두 축이 모두 다른 선에 대한 분기는 없음(1752). |
| 1757–1803 | `discharge_boundary_v`: pntdisch=1 지점 유량을 보간(1785–1787), shift 후 m/n을 1..nx/ny로 제한(1793–1794). 질량 추가 `zs(m1l,n1l)+=qnow*dt*dsdnzi(m1l,n1l)`(1797). 이 루틴에는 indomain 검사 없음. |
| 1804–1845 | 내부 `velocity_Boundary`는 비정수압 경계 시계열 판독 루틴(1816–1817). `nh_pars.inc` 포함(1833); nyg+1 길이 U/V/Z/W/dU/dV 출력, 일곱 isSet flag는 intent(out), 선택 인수 force_init·bcst(1837–1843). |
| 1846–1901 | 파일명 ''·unit iUnit_U, lVarU/lIsEof/lNH_boun_U=false·initialize=true(1847–1853). 변수 헤더 인덱스 iZ/iU/iV/idU/idV/iQ/idQ/iW/iT는 save·초깃값 0(1860–1868); 각 변수의 두 시간 배열 및 `t0=t1=0` 보존(1877–1896). |
| 1902–1960 | master만 실행. 선택 bcst 없으면 0, force_init 없으면 false; 파일 변경/강제초기화이면 initialize=true(1903–1918). 새 파일 존재·열림 여부 확인 후 열린 경우 unit_U 닫기, 기존 배열 해제(1926–1947). 존재하면 읽기 전용 순차 파일 열기, 없으면 로그·halt·return(1949–1957). |
| 1961–2013 | 첫 문자열 lowercase 후 scalar/vector로 lVarU 설정, 다른 문자열 분기는 비어 있음(1966–1973). nvar·2글자 header 배열 읽음(1976–1985). z/zs,t,u,v,w,dU,dV,q,dq 변형에 맞춰 인덱스 지정; q는 iQ와 iU, dq는 idQ와 idU 함께 지정(1988–2010). |
| 2014–2055 | 각 헤더 인덱스>0일 때 nyg+1 길이 old/new 배열을 할당하고 0 초기화; stat 오류면 Halt_program(2015–2053). |
| 2056–2085 | `tmp(nyg+1,nvar-1)`에 `velocity_Boundary_read`로 두 시간층 판독, 시간에 bcstarttime 추가(2058–2059·2076–2077); 각 열은 헤더 인덱스−1(2060–2065·2078–2083). 첫 판독 EOF면 t1=t0·new=old(2067–2074). tmp 해제(2085). |
| 2086–2144 | 초기화 출력은 각 변수 `값0+(값1-값0)*(t-t0)/(t1-t0)`(2087–2126); 존재하면 isSet 참, 없으면 값 0·flag 거짓. Q flag는 iQ>0 여부(2133–2138). 여기서 바로 return(2142). |
| 2145–2184 | 일반 단계에서 EOF가 아니면 `t>=t0 .and. t<t1`일 때까지 시간층을 옮기며 다음 행 판독·bcst 추가(2151–2167). EOF 도달 때 존재하는 변수의 마지막 값과 Q flag만 설정하고 return(2171–2183). |
| 2185–2239 | 일반 단계 보간도 `(t-t0)/(t1-t0)` 사용; U/V/Z/W/dU/dV별 존재 flag 및 미지정 0 갱신(2186–2228), Q 여부(2231–2237). |
| 2240–2257 | 이미 EOF인 경우 존재한 변수의 마지막 값을 유지(2242–2247), Q flag만 새로 설정(2248–2252). master 조건 및 velocity_Boundary 끝. |
| 2258–2302 | `velocity_Boundary_read` 선언·주석. `nh_pars.inc`, 시간·vector는 intent(inout), iseof는 intent(out), scalar는 nvar−1 길이(2281–2296). |
| 2303–2324 | iseof=false 후 vector면 `read ... t,vector`, scalar면 `t,scalar`를 읽고 모든 y점에 scalar 열값 복제(2303–2311). EOF 외 iostat 오류는 파일명 조회·`report_file_read_error`(2314–2316); EOF는 label 9000에서 iseof=true(2320). 루틴·모듈 끝(2322–2324). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 320–321: 주석은 새 조건의 taper 시간을 1초로 설정한다고 적지만 실행문은 `par%taper=0.d0`이다.
- 612–630: 여러 경계 시간단계를 건너뛴 비MPI 분기에서 gq1도 읽지만 `q1=gq2`, `q2=gq2`로 대입한다. MPI 분기는 gq1을 q1로 분배한다(625).
- 697–700: order=3 NONH PARAMS 분기의 수위·속도 식은 모두 주석이다.
- 854–866: 스펙트럼 NONH 경계 회전은 ui·vi·dUi에만 실행되고 dVi 회전문은 없다. taper 적용 목록도 ui·zi·wi·dUi이며 vi·dVi는 없다.
- 874–908: TS_NONH MPI 분기는 isSet_V를 broadcast하지 않지만 이후 isSet_V를 검사한다. Q→속도 변환은 비MPI 분기에만 있다(886–891).
- 1023·1025·1036·1038: hybrid 최소값 갱신의 첫 인수는 이전 최소값이 아니라 갱신된 최대값이다.
- 1462·1467: back 모서리 수위 계산에서 조석기울기·격자간격·바닥의 i 인덱스는 nx+1이 아니라 1이다.
- 1511·1514: save 변수 fc는 `t<=dt` 조건에서만 값을 설정한다. LR_NO_ADVEC의 식에는 fc가 포함되지만 뒤 주석은 Coriolis가 없다고 적는다(1551·1564).
- 1793–1797: 점 유량 루틴은 shift된 위치를 로컬 범위로 제한한 뒤 질량을 더하며, 선 유량 루틴의 indomain 검사는 없다(1670–1673).
- 1860–1868·1922–2012: save 헤더 인덱스의 초기값은 선언 시 0이며, 새 파일 초기화 블록에 이 인덱스들을 0으로 되돌리는 실행문은 없다.
- 1868·1994·2058–2065·2306–2308: iT를 헤더에서 찾지만 입력 판독은 시간을 첫 값으로 읽고 다른 열은 헤더 인덱스−1로 접근한다. iT를 판독 위치에 사용하는 실행문은 없다.
- 2067–2087: 첫 판독 EOF 때 t1=t0로 만든 뒤 초기화 보간식에서 `(t1-t0)`로 나눈다. 이 블록에 분모 0 검사문은 없다.
- 1841·2171–2183·2240–2252: isSet_U/V/Z/W/dU/dV는 intent(out)인데 EOF 반환·유지 경로는 이 여섯 flag에 대입하지 않고 isSet_Q만 대입한다.

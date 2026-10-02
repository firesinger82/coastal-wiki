---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/bedroughness.F90
lines: 737
sha256: 508ccef2919d203a716f831f4ffd80a57068562eab747a00a94da802a840dfef
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# bedroughness.F90 — 판독 구간 기록

구간은 1행부터 737행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 2007년 기관·저자·연락처 및 LGPL 2.1 이상 재배포·수정 조건과 무보증 문구의 주석 머리말(1–26). |
| 27–50 | `bedroughness_module`은 `implicit none`, `save`, `private`(27–31). 조도 kru/krv와 입도별 조도, 속도·침투 보정·이전 속도·가속도·Shields 작업 배열, 길이 2의 `dtold`, delta/rhogdelta, 식생 마스크 isveggie, 초기 Manning 계수 nman0를 선언한다(32–42). `nmanmin=-123`(44), 공개 루틴은 `bedroughness_init/update`(45–46); 빈 줄과 contains(47–50). |
| 51–77 | `bedroughness_init(s,par)`에서 parameters/spacepars/paramsconst를 사용하고 par는 intent(in)이다(51–60). include 문 두 개는 주석(62–63). 추가 바닥응력 taubx_add/tauby_add를 0으로 둔다(65–66). bedfriction이 Chezy이면 `cfu=cfv=g/bedfriccoef**2`(68–72), CF이면 두 계수에 bedfriccoef를 그대로 대입한다(73–75). Manning 분기 시작(76–77). |
| 78–103 | Manning에서 dynamrough=1이면 nman0와 isveggie를 `(nx+1,ny+1)`로 할당하고 nman0에 초기 계수를 저장한다(78–81). `nmanmin=minval(bedfriccoef)`, 최소값보다 큰 셀을 식생 True, 나머지를 False로 둔다(82–87). 젖은 u/v점은 `cf=g*n**2/h**(1.d0/3)`를 계산하고 maxcf 상한·mincf 하한을 적용한다(90–100). 마른 점은 maxcf로 설정한다(94–96·101–103). |
| 104–131 | 입도 기반 White-Colebrook 초기화는 kru/krv를 `(nx+1,ny+1)`로 할당한다(104–106). ngd=1이면 모두 `3*D90top`(108–110). 그 외 u점은 `1.5*(D90top(i,j)+D90top(i+1,j))`, 끝 x열은 앞 열 복사(113–118). ny=0이면 v점은 `3*D90top`; 그 외 `1.5*(D90top(i,j)+D90top(i,j+1))`(y방향 이웃 두 값의 합×1.5, 126)이고 마지막 y열을 복사한다(120–130). [10-02 검증 정정: '평균×1.5' → '합×1.5'] |
| 132–169 | 입도 기반 젖은 u/v점에서 `cf=g/(18*log10(12*max(h,kr)/kr))**2`를 계산하고 maxcf·mincf로 제한하며, 마른 점은 maxcf다(132–145). 직접 White-Colebrook 분기는 kru/krv를 할당하고 bedfriccoef를 조도로 대입한다(146–150). 같은 식과 상·하한/건조 처리를 적용한다(151–164). select와 초기화 루틴을 끝내고 빈 줄을 포함한다(165–169). |
| 170–195 | 빈 줄 뒤 `bedroughness_update` 선언·사용 모듈·형과 인덱스 선언(172–182). bedfriction 선택에서 Chezy·CF는 초기화한 상수 조도를 유지하며 별도 실행문이 없다(186–191). Manning 분기에 Chezy 변환과 `cf=g*n**2/h**(1/3)` 설명 주석이 있다(192–195). |
| 196–219 | dynamrough=1일 때 하나의 where 분기로 계수를 갱신한다(196–206). 식생이고 sedero>0이면 `n=nmin+min(max((dstem-sedero)/dstem,0),1)*(n0-nmin)`(198–199). 식생이고 sedero<-droot이면 최소값으로 두고 식생 플래그를 False로 변경한다(200–202). 그 외 전체 셀은 `n=nmin+min(max((droot+sedero)/droot,0),1)*(n0-nmin)`(203–205). 젖은 u/v점의 Manning cf를 수심으로 다시 계산하고 maxcf 상한만 적용; 마른 점은 maxcf(208–219). |
| 220–247 | 입도 기반 조도 갱신은 ngd>1일 때만 수행한다(220–221). 젖은 u점에 이웃 D90 합×1.5를 대입하고 마지막 x열을 복사한다(223–230). ny=0이면 젖은 v점에 `3*D90top`; 그 외 젖은 v점에 y이웃 합×1.5를 대입하고 마지막 y열을 복사한다(232–246). |
| 248–274 | 입도 기반 White-Colebrook cf를 젖은 u/v점에서 다시 계산한다(248–259). u는 상한 `0.1d0`(250), v는 par%maxcf(256), 마른 점은 둘 다 par%maxcf. 직접 White-Colebrook 분기에서도 같은 로그식을 계산하되 u/v 모두 maxcf 상한을 쓴다(260–272). 이들 갱신 분기에는 초기화의 mincf 하한이 없고 select가 끝난다(273–274). |
| 275–304 | 추가 바닥응력을 0으로 초기화한다(275–277). friction_acceleration이 CF_ACC_NIELSEN이면 `acceleration_boundary_layer_effect_Nielsen`, CF_ACC_MCCALL이면 `acceleration_boundary_layer_effect`를 호출한다(279–284). friction_turbulence=1이면 난류 보정(286–290), friction_infiltration=1이면 침투 보정 루틴을 호출한다(292–296). 끝에 cfu/cfv를 `min(cf,1.d0)`로 제한하고 갱신 루틴을 끝낸다(299–304). |
| 305–345 | `infiltration_boundary_layer_effect`의 모듈·형·인덱스와 상수 `epsVentilation=1`, `maxEnhancement1=3`, `maxEnhancement2=0.1` 선언(305–317). facbl이 미할당이면 facbl/blphi/infilb/Ubed/Ventilation 배열을 `(nx+1,ny+1)`로 할당한다(320–327). 주석은 Butt/Russell/Turner(2001), Conley/Inman(1994)의 침투에 따른 경계층 변화와 cf/응력 비를 설명하며, surf-beat에서는 추가응력의 urms 성분을 생략한다고 적는다(330–344). |
| 346–381 | u점에서 젖은 셀은 `infilb=0.5*(infil(i,j)+infil(i+1,j))`, 마르면 0, 끝 x열은 앞 열 복사(346–356). 젖은 점은 `Ubed=abs(vmageu)`, `Ventilation=-infilb/max(Ubed,1.d-6)`을 ±1로 제한하고 `blphi=0.9/2/cfu*Ventilation`을 계산한다(357–363). infilb≥0이면 blphi≤-1d-4로 두고 `facbl=blphi/(exp(blphi)-1)`을 최대 3으로 제한; 그 외 blphi≥1d-4, facbl은 최소 0.1(365–373). cf 자체 수정은 주석(374–375); `facbl=min(facbl,1/cfu)` 후 `taubx_add+=(facbl-1)*cfu*rho*ueu*vmageu`(377–378). |
| 382–422 | ny>0이면 젖은 v점의 infilb를 y방향 이웃 평균, 마르면 0으로 두고 마지막 y열은 `s%infil(:,s%ny)`로 채운다(382–393). ny=0이면 셀 중심 infil 전체를 쓴다(394–397). 젖은 v점에서 `Ubed=abs(vmagev)`, Ventilation ±1, `blphi=0.9/2/cfv*Ventilation`, infilb 부호에 따른 ±1d-4 회피와 facbl 상한 3·하한 0.1을 u와 동일하게 적용한다(398–414). cf 수정은 주석(415–416); `facbl=min(facbl,1/cfv)`, `tauby_add+=(facbl-1)*cfv*rho*vev*vmagev`(417–418). 루틴 끝과 빈 줄(420–422). |
| 423–460 | McCall 경로 `acceleration_boundary_layer_effect`의 모듈·형·평활 시간과 저장 배열 Fi 선언(423–435). dudtsmooth가 미할당이면 가속도 2개·이전 속도 4개·평활 속도 4개·Fi를 `(nx+1,ny+1)`로 할당한다(438–450). 이전·평활 속도는 모두 0, dtold의 두 원소는 par%dt로 초기화한다(451–459). dudtsmooth/dvdtsmooth/Fi 값 대입은 이 초기화 블록에 없다. |
| 461–500 | 주석은 ueu/veu가 직전 단계 값이므로 한 단계 더 이전의 값과 dtold(1)을 이용해 시간 미분을 만들고, 두 단계 동안 가속도 변화가 작으며 현재 젖음 마스크를 사용할 수 있다고 가정한다(462–475). `Tsmooth=Trep/20`, `factime=min(dtold(1)/Tsmooth,1)`(476–477). 젖은 u점의 `ueuf=(1-factime)*ueuf+factime*ueu`, `dudtsmooth=(ueuf-ueuold)/dtold(1)`(479–483); 가속도를 ±100*g로 제한한다(486–490). `taubx_add+=ci*rho*min(D50top,hu)*dudtsmooth`(491). 마르면 ueuf·veuf를 0으로 두고 이전 값 ueuold·veuold를 현재 평활값으로 저장한다(492–499). |
| 501–531 | ny=0이고 양쪽 경계가 LR_WALL이거나 swave=0이면 v추가응력을 건드리지 않는다(501–506). 그 외 젖은 v점에 vevf 평활·`dvdtsmooth=(vevf-vevold)/dtold(1)`·±100*g 제한·`tauby_add+=ci*rho*min(D50top,hv)*dvdtsmooth`를 적용한다(507–515). 마르면 vevf·uevf를 0으로 두고 uevold·vevold를 저장한다(516–524). `dtold(1)=dtold(2)`, `dtold(2)=dt`로 이력을 이동한 뒤 루틴 끝(526–531). |
| 532–568 | Nielsen 가속도 루틴은 parameters/spacepars/constants의 pi/paramsconst를 사용하고 omegap·Tsmooth·factime·iomegap 및 저장 변수 phirad를 선언한다(532–544). dudtsmooth가 미할당이면 u/v 가속도·동방향 이전속도·평활속도만 할당하고 초기속도 0·dtold=dt로 둔다(547–566); 교차속도 배열 할당·초기화는 주석이다. 이 최초 할당 분기에서 `phirad=phit/180*px`를 정한다(567–568). |
| 569–602 | `omegap=2*px/Trep`, `iomegap=1/omegap`(570–571). 시간차와 마스크 가정 주석은 McCall 경로와 같다(572–585). `Tsmooth=Trep/20`, `factime=min(dtold(1)/Tsmooth,1)`(586–587). 벡터 가속도 대안은 주석(589–593); 젖은 u점은 동방향 ueuf 평활 및 차분으로 dudtsmooth를 계산하고, 마른 점은 ueuf·dudtsmooth를 0으로 둔다(594–601). |
| 603–627 | ny=0이고 양쪽 벽 또는 swave=0인 조건에서는 dvdtsmooth=0(603–607). 그 외 젖은 v점은 vevf 평활과 차분을 수행하며 마르면 vevf·dvdtsmooth=0(609–619); 교차속도 가속도식은 주석(612–614·617). ueuold=ueuf, vevold=vevf를 저장하고 dtold 이력을 이동한다(621–627); 교차속도 저장은 주석이다. |
| 628–665 | 주석은 Nielsen 전체응력에서 통상응력을 빼는 식, urms 생략 및 phi=0·가속도=0의 정상 조건에서 일관되도록 속도 성분을 처리하는 전개를 설명한다(628–645). 젖은 u점은 `taubx_add+=cfu*rho*((cos(phirad)**2-1)*ueu*vmageu+2*cos(phirad)*ueu*sin(phirad)*iomegap*dudtsmooth+(sin(phirad)*iomegap*dudtsmooth)**2*sign(1.d0,ueu))`(646–651). ny=0·양쪽 벽/무단파 조건이면 v응력은 그대로; 아니면 젖은 v점에서 cfu/ueu/vmageu/dudtsmooth 대신 cfv/vev/vmagev/dvdtsmooth의 같은 식을 추가한다(652–661). 루틴 끝과 빈 줄(662–665). |
| 666–689 | `turbulence_boundary_layer_effect`는 parameters/spacepars, 저장 allocatable kbl과 인덱스를 선언한다(666–676). 주석은 Reniers et al.(2004)을 따르는 `ubed_turb=sqrt(ubed**2+gamma*kb)`, 전체응력과 통상응력 차 `cf*rho*gamma*kb`를 설명한다(678–684). kbl이 미할당이면 `(nx+1,ny+1)`로 할당한다(686–688). |
| 690–708 | 젖은 u점의 kbl은 `0.5*(kb(i,j)+kb(i+1,j))`, 마른 점은 0; 마지막 x열은 앞 열 복사(690–700). wetu=1이고 kbl>0인 셀에서 `taubx_add+=cfu*rho*gamma_turb*kbl*sign(1.d0,ue)`(701–703). cf를 직접 증폭하던 두 대안식은 주석(705–707). |
| 709–737 | ny>0이면 젖은 v점 kbl은 y이웃 kb 평균, 마르면 0이고 마지막 y열을 복사한다(709–720). ny=0이면 셀 중심 kb 전체를 쓴다(721–724). wetv=1·kbl>0인 셀에서 `tauby_add+=cfv*rho*gamma_turb*kbl*sign(1.d0,ve)`(725–727). 과거 cf 증폭식은 주석(729–731), 루틴 끝·빈 줄·모듈 끝을 포함한다(732–737). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 90–103·208–219: Manning 초기화는 maxcf와 mincf를 모두 적용하지만 갱신은 maxcf 상한만 적용한다. White-Colebrook 초기화·갱신에서도 mincf 적용 여부가 다르다(132–164·248–272).
- 249–256: 입도 기반 White-Colebrook 갱신의 u 상한은 고정 `0.1d0`, v 상한은 `par%maxcf`다.
- 200–205: 큰 침식 후 isveggie를 False로 바꾸지만, 다음 갱신의 마지막 elsewhere는 isveggie 조건 없이 nman0·sedero 식을 모든 남은 셀에 적용한다.
- 299–300: 추가응력 보정 루틴을 모두 호출한 뒤 cfu/cfv에 별도의 고정 상한 1을 적용한다.
- 292–295·374–378·415–418: 호출부 주석은 침투가 cfu/cfv 증가로 응력을 높인다고 하지만, 루틴의 직접 cf 수정은 주석이고 실행문은 taubx_add/tauby_add를 갱신한다.
- 356·393: 침투 u점의 끝열은 보간한 infilb 앞 열을 복사한다. v점의 끝열은 infilb가 아니라 원래 s%infil의 마지막 내부 열을 대입한다.
- 438–460·547–568: 두 가속도 루틴이 같은 dudtsmooth 할당 여부를 초기화 조건으로 사용한다. Nielsen 초기화에서는 교차속도 배열을 할당하지 않고, McCall 초기화에서는 이를 할당한다. 설정 변경 시의 처리 분기는 이 파일에 없다.
- 544·547–570: 저장 phirad는 Nielsen 최초 할당 블록에서만 설정된다. omegap는 호출마다 다시 계산한다.
- 486–490·510–514·595–618: McCall 경로는 가속도를 ±100*g로 제한하며 Nielsen 경로에는 같은 제한이 없다.
- 491·515·703·727: 가속도 추가응력은 min(D50top,hu/hv)를 쓰고, 난류 추가응력 부호는 ue/ve를 쓴다. Nielsen과 침투 추가응력은 ueu/vev를 쓴다(378·418·647–658).
- 32–40·435·450: kru50/krv50/kru90/krv90, urms_upd/u2_upd, shieldsu/shieldsv, delta/rhogdelta는 이 파일에서 선언 이후 사용하지 않는다. Fi는 선언·할당만 한다.
- 536: 가져온 상수 pi는 Nielsen 루틴의 실행식에 없으며 위상·각주파수 식은 par%px를 사용한다(567·570).
- 51–169·172–303: bedfriction select에 case default 분기가 없다.

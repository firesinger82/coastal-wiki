---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/beachwizard.F90
lines: 806
sha256: 94039fd11198d6c41102e44687abe0bedfa8def6536a3b9d6a9b0a72928deb32
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# beachwizard.F90 — 판독 구간 기록

구간은 1행부터 806행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | `beachwizard_module`은 `implicit none`, `save`, `private`이고 `bwinit/assim/assim_update`를 공개한다(1–5). `beachwiz` 형에 최대 1000시각×8소스의 분 단위 시각·유효기간·파일명·오차파일명(8–14), 네 종류 파일명 포인터(15–22), 기본 0인 소스별 `status/statuserr`와 시간 인덱스·읽기 플래그를 선언한다(23–34). `ntimesnew`, `nflagsigpr`, `nflagsetobs`도 0으로 초기화된다(9–11). |
| 35–78 | 관측 원격격자 포인터 `fobs1/fobs1err/disobs/zbobs1/shobs1`(35–39), 모델격자 관측값·계산 파속·파수·잔차·동화량 및 표준편차 배열(41–55)을 선언한다. 일부 dobs/shobs/zbobs/sig2prior 선언은 주석(40·45–46·56). 지도 원점·격자 간격·각도(degree)·관측 주기 `tradar`·격자 크기·기본 오차 스칼라를 선언한다(57–70). 형을 끝내고 모듈 저장 객체 `bw`를 선언한 뒤 `contains`(73–78). |
| 79–104 | `bwinit(s)`는 `spacepars`와 `xmaster`를 사용하고 master가 아니면 즉시 반환한다(80–89). 항상 참인 `if(.true.)`에서 `dobs/zbobs/sig2prior/shobs/bwalpha/dcmdo/dassim/cobs`를 모두 `(1:nx+1,1:ny+1)`로 할당한다(91–100). 이 블록에는 값 초기화가 없다. 빈 줄과 루틴 끝을 포함한다(101–104). |
| 105–147 | `assim(s,par)`의 매개변수·공간 형, 80자 infofile·소스 번호·인덱스·파일존재 플래그·읽기 함수 external 및 작업 배열을 선언한다(105–133). 파수 근사 다항식 계수는 `a1=5.060219360721177D-01`, `a2=2.663457535068147D-01`, `a3=1.108728659243231D-01`, `a4=4.197392043833136D-02`, `a5=8.670877524768146D-03`, `a6=4.890806291366061D-03`, `b1=1.727544632667079D-01`, `b2=1.191224998569728D-01`, `b3=4.165097693766726D-02`, `b4=8.674993032204639D-03`(135–144). |
| 148–182 | `bw%fobs`가 미할당이면 관측·파속·파수·잔차·동화·오차 배열 13개를 `(nx+1,ny+1)`로 할당한다(148–166); s의 일부 배열 할당은 주석이다. 호출별 지역 `h1/hh/ome2/num/rk/E/Hrms/den`을 같은 크기로 할당한다(168–177). `bw%dcmdo/ccmco/scmso`를 0으로 초기화한다(179–181). |
| 183–229 | 최초 관측 초기화(`nflagsetobs==0`)에서는 `s%dobs`, `bw%cobs`, `s%shobs`, `s%zbobs`를 -999로 두고 플래그를 1로 만든다(183–192). 최초 prior 설정에서는 `sigpr.dep`가 있으면 unit 444로 `(nx+1)×(ny+1)` 분산을 읽고 없으면 `s%sig2prior=1**2`(194–205). `bwdefaults.inp`가 있으면 sigD/C/Z/Sdef를 차례로 읽어 해당 오차 배열에도 대입(207–218); 없으면 sigCdef=1, sigDdef=20, sigZdef=sigSdef=0.5의 스칼라만 설정한다(219–224). 플래그를 1로 두고, open 오류 목적지는 `999 continue`(225–229). |
| 230–253 | `imageinfoimap`이 있으면 소스 1로 `assim_rd`를 호출한다(232–236). status=1이면 `in=1..nx, im=1..ny`에서 `wetu>0`이고 `dobs>-5`인 셀의 소산 잔차를 `Dr-dobs`로 둔다(237–245). statuserr=0이면 `h1=max(hh+delta*H,hmin)`을 계산하고 sigD를 sigDdef로 설정한다(246–251); 수심에 따른 오차 조절식은 주석(248). |
| 254–292 | `imageinfozb`는 소스 2로 읽고 오차 status=0이면 sigZ=sigZdef(254–262). `imageinfocx`는 소스 3(264–268). status=1이면 전체 `(nx+1,ny+1)`에서 `om=2*3.1415/tradar`, `ome2=om**2*hh/g`, `num=1+ome2*(a1+ome2*(a2+ome2*(a3+ome2*(a4+ome2*(a5+ome2*a6)))))`, `den=1+ome2*(b1+ome2*(b2+ome2*(b3+ome2*(b4+ome2*a6))))`, `rk=sqrt(ome2*num/den)/hh`(270–279). `Hrms=max(0.01d0,sqrt(8*max(0.01d0,E)/rho/g))`, `ccom=sqrt(g/rk*tanh(rk*hh+Hrms))`(280–281); 젖고 cobs>-990이면 ccmco=ccom-cobs(282–284). 오차 없음이면 sigC=sigCdef(288–290). |
| 293–340 | `imageinfokabs`는 소스 4로 읽는다(293–297). status=1이면 272–281행과 같은 om·ome2·num·den·rk·Hrms·ccom 계산을 수행한다(298–310). 관측 파수를 파속으로 바꾸는 식은 `cobs=om/max(kobs,0.01d0)`이고 kobs<-990이면 cobs=-999; 젖고 kobs>-990이면 ccmco=ccom-cobs(311–317). statuserr=1이면 rk를 다시 계산해 `sigC=om/rk*(sigK/(rk+sigK))`(321–336); statuserr=0이면 sigCdef를 쓴다(337–339). |
| 341–374 | `imageinfoibathy`가 있으면 소스 5로 `assim_rd`를 호출한다(342–346). status=1이면 `1..nx,1..ny`에서 `abs(shobs)<=5`일 때 `scmso=zb-shobs`(349–356); `hh+shobs` 대안은 주석(352). 내부 셀 `2..nx,2..ny`의 3×3 이웃 평균 `/9.`을 같은 배열에 즉시 대입하는 스무딩을 두 번 한다(359–367). 오차 없음이면 sigS=sigSdef(370–372). |
| 375–382 | 출력용 `s%dcmdo=bw%dcmdo` 대입(375–377), `comp_depchg(bw,s,par)` 호출(379), assim 끝과 빈 줄(381–382). |
| 383–423 | `assim_rd`는 bw·s·par·infofile·srcnr를 받고 parameters/spacepars를 사용한다(383–396). 지도 좌표 회전·보간용 실수와 네 가중치, 격자 인덱스·파일 플래그·할당해제 상태 변수 등을 선언한다(398–418). 420행 이하에는 실제 시간 기준에 관한 주석과 빈 줄이 있다. |
| 424–450 | `ntimesnew(srcnr)==0`이면 infofile 존재를 확인한다(424–428). unit 31로 지도 수를 읽고 각 지도 시각·값파일·오차파일·유효기간을 읽어 표준출력에도 쓴다(430–440). 남은 시각 슬롯 `ntimesnew+1:1000`을 `1.e10`으로 채운다(441). 파일이 없으면 고정 메시지로 stop(444–446). 시각 인덱스는 1, 마지막 읽은 인덱스는 0으로 둔다(447–448). |
| 451–470 | 호출마다 `status(srcnr)=0`(452). `par%t<60*첫 지도 시각`이면 읽기를 수행하지 않는다(455–459). 그렇지 않으면 다음 지도 시각 이상인 동안 인덱스를 1씩 증가시키며 label 10으로 돌아간다(460–463). 현재 지도 시작 이후 시간이 `60*timvalnew` 이하이고 그 인덱스가 마지막 읽은 인덱스와 다를 때 새 지도 읽기를 시작한다(466–470). |
| 471–523 | 값 지도 파일이 있으면 unit 31에서 xll·yll·dx·dy·nx·ny·angle을 차례로 읽는다(473–482). `associated(fobs1)`이면 해제하고 `(bw%nx,bw%ny)`로 할당하여 y행별 값을 읽은 뒤 파일을 닫고 읽은 인덱스를 갱신한다(484–490). 파일이 없으면 999로 이동(491–493). 오차파일 헤더·배열 읽기와 `statuserr` 설정 전체는 주석이다(494–523). |
| 524–569 | `degrad=atan(1.)/45`, 회전계수 cos/sin, 허용 좌표 끝 `(nx-2)*dx`, `(ny-2)*dy`를 계산한다(524–528). 전체 모델격자에서 fobs를 -999로 두고 xz/yz에서 지도 원점을 뺀 좌표를 `x1=xs*cs+ys*sn`, `y1=-xs*sn+ys*cs`로 회전한다(530–538). 좌표를 dx..x1max·dy..y1max로 제한하고 지도 인덱스 및 이웃을 2..nx-1·2..ny-1로 제한한다(539–546). `a=mod(x1,dx)/dx`, `b=mod(y1,dy)/dy`; `(1-b)*(1-a)`, `(1-b)*a`, `b*(1-a)`, `b*a` 가중치로 네 점의 fobs1을 합산한다(547–557). 젖음 마스크와 오차 보간은 주석이다(534·553·559–566). |
| 570–588 | 소스 1→s%dobs, 2→s%zbobs, 3→bw%cobs, 4→bw%cobs, 5→s%shobs에 보간값을 복사한다(570–574). 새 지도 읽기 분기를 닫고 유효기간 내이면 status=1(576–578). 기간이 지났으면 bw%fobs만 0으로 두고, 오류 목적지 `999 continue`와 루틴 끝이 이어진다(580–588). |
| 589–604 | `assim_update`는 parameters와 spacepars를 사용한다(589–593). bchwiz=1과 bchwiz=2의 두 분기는 모두 `s%zb=s%zb-bw%dassim`을 수행한다(595–603). dzbdt와 dt*morfac에 관한 설명은 주석이다(597–598). |
| 605–643 | `comp_depchg`의 형·인덱스·최대파고·최대제곱미분·정규화 계수·동화 횟수와 errD/C/S, Hb·kh·gambal·Ga·미분·수심·관측분산·Hrms·alphafac·h2 배열을 선언한다(605–643). alpha 배열 선언은 주석(637). |
| 644–689 | errD가 미할당이면 작업 배열 모두 `(nx+1,ny+1)`로 할당한다(644–662). `Hrms=max(H,0.01d0)`, `h2=0`(665–667). `j=2..ny, i=2..nx+1`에서 역방향으로 `disfac=dsc/(0.5*(L1(index)+L1(max(index-1,1))))`를 계산해 남은 상대거리 `1-backdis`로 제한하고 `h2+=disfac*hh`를 누적한다(668–684). 첫/끝 y열은 인접 열을 복사(685–686). `h1=max(hh+delta*Hrms,hmin)`, `kh=min(10.0,k*h1)`(687–688). |
| 690–715 | 주석은 Van Dongeren et al.(2008)의 식 번호를 따른다고 한다(690–691). `gambal=0.29+0.76*kh`, `Hb=0.88/k*tanh(gambal*kh/0.88)`, `Ga=(Hb/Hrms)**2`, `Hrmsmax=maxval(Hrms)`(694–697). `dDdGa=-0.25*rho*g/Trep*Hrms**2*Ga*exp(-Ga)`, `dGadHb=2*Hb/Hrms**2`(699–700). `dHbdh=(0.29+2*0.76*kh)*(1-kh/(sinh(kh)*cosh(kh)+kh))/cosh((0.29*kh+0.76*kh**2)/0.88)**2 + 0.88*tanh((0.29*kh+0.76*kh**2)/0.88)/(sinh(kh)*cosh(kh)+kh)`(702–704). `dDdh=dDdGa*dGadHb*dHbdh`, `mxdDdh=maxval(dDdh**2)`(706–709); 오차 수정식은 주석(712–713). |
| 716–750 | sigD를 관측 소산 최댓값의 15%인 `0.15*maxval(dobs)`로 덮어쓴다(716). 공간변화 오차식은 주석(718–722). `alp_as=0.005`, `errD=(dcmdo**2+sigD**2)/(dDdh**2+alp_as*mxdDdh+1.e-16)`(724–725); dobs<-990이면 999(727–731). errC는 모두 999이고 관측 결측 확인도 999로 대입하며, 파속 오차 공식은 주석이다(733–739). cobs를 출력용 s%cobs로 복사(741–742). `errS=(scmso**2+sigS**2)/1.d0`, shobs<-990이면 999(744–749). |
| 751–773 | `Nassim=tstop/dt`(753), `sig2obs=1/(1/errD+1/errS)`, `bwalpha=sig2prior/(sig2prior+Nassim*sig2obs)`(755–756). 얕은 수심용 bwalpha 조절은 주석(757). 전체 셀에서 `alphafac=cosh(sdist/100-0.65*t*sdist(nx+1,im)/tstop/100-2)**(-10)`(761–765). 각 y열의 최대 alphafac 위치 ind를 구해 `1:ind`는 1로 바꾼다(767–770). bwalpha에 곱하는 대안은 주석이다(772). |
| 774–789 | 소산에 따른 동화량은 `dassim=-bwalpha*tanh((h1/0.85)**5)*(dDdh-sqrt(alp_as*mxdDdh))/(dDdh**2+alp_as*mxdDdh)*dcmdo*alphafac`(774). 파속 기여 대안은 주석(775–776). 전체 셀에서 양수면 `min(dassim,0.1*h1)`, 음수면 `max(dassim,-0.1*h1)`, 그 외는 0으로 제한한다(778–788). |
| 790–806 | 제한 후 `dassim+=bwalpha*scmso`로 해안선 보정을 더한다(791); 다른 보정식은 주석(792). 출력용 `s%dassim=bw%dassim`(794–795). dobs>-990인 셀에서만 `sig2prior=bwalpha*tanh((h1/0.85)**5)*Nassim*sig2obs`로 갱신한다(797–802); h2를 쓰는 식은 주석(800). 루틴·모듈을 끝낸다(804–806). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35–39·484: `fobs1` 등 포인터 선언에 `=> null()`이 없고, 이 파일에는 첫 `associated(bw%fobs1)` 검사 전의 명시적 nullify가 없다.
- 153·185–190·311–316·570–574: kobs는 할당되지만 최초 관측 초기화에 포함되지 않는다. 소스 4 지도도 cobs에 대입하며, 뒤의 파속 환산은 kobs를 읽는다. 이 파일에는 kobs 값 대입이 없다.
- 24·494–523: statuserr 기본값은 0이고 오차파일 읽기·statuserr 변경 코드는 모두 주석이다. 실행 코드에는 statuserr=1 대입이 없다.
- 207–224·744: defaults 파일이 없는 분기에서는 오차 스칼라만 설정한다. sigS 배열은 소스 5 infofile이 존재할 때 설정되지만(342–372), comp_depchg는 파일 존재 여부와 별도 조건 없이 sigS를 읽는다.
- 215·249·716: sigD에 기본 오차를 대입하는 코드가 있지만 comp_depchg에서 `0.15*maxval(dobs)`로 다시 덮어쓴다.
- 238–239·349–350: 소산·해안선 잔차 루프는 nx·ny까지다. 파속 계산·지도 보간·지형보정 루프는 nx+1·ny+1까지다(270–271·530–531·761–762).
- 430–441·460–463: 지도 수를 읽은 뒤 1000 이하인지 검사하지 않는다. 시각 진행은 `itimnew+1`을 조회하며 별도의 지도 수 상한 비교가 없다.
- 532–557: fobs를 -999로 설정한 뒤 모든 셀에서 네 점 보간값으로 덮어쓴다. 주석의 젖음 검사 외에 결측 지도값을 제외하는 실행 분기는 없다.
- 359–367: 3×3 해안선 잔차 스무딩은 별도 버퍼 없이 같은 배열을 순서대로 갱신한다.
- 581·570–578: 지도 유효기간이 지난 분기는 공용 fobs만 0으로 두며, 이전에 복사된 dobs·zbobs·cobs·shobs 배열은 이 분기에서 지우지 않는다.
- 595–603: bchwiz=1과 2의 지형 갱신식이 동일하다.
- 668–686: h2 계산의 y 내부 루프는 `2..ny`이고 경계 복사는 `h2(:,1)=h2(:,2)`와 `h2(:,ny+1)=h2(:,ny)`다. 이 블록에는 ny=0에 대한 분기가 없다.
- 733–755: errC는 999로 설정되고 합성 관측분산 식에는 errD·errS만 쓰인다. ccmco·sigC도 최종 dassim 식(774·791)에는 나타나지 않는다.
- 753: 동화 횟수의 실행식은 tstop/dt이며 주석에는 tstop/wavint로 변경했다는 문구가 있다.
- 725·774: errD 분모에는 `+1.e-16`이 있지만 dassim의 `dDdh**2+alp_as*mxdDdh` 분모에는 해당 상수가 없다.
- 778–791: ±0.1*h1 제한은 소산 보정에 적용되고, 해안선 보정은 그 뒤 더한다. 그 이후 같은 제한을 다시 적용하는 코드는 없다.
- 120–121·133·168–174·620·696: readkey_dbl/readkey_int는 선언만, 지역 hh/E는 선언·할당만, Hrmsmax는 계산만 하며 이후 실행식에 쓰이지 않는다. h2도 계산 후 실제 보정식에는 쓰이지 않고 800행 주석식에만 나타난다.

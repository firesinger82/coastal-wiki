---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/roelvink.F90
lines: 320
sha256: ebaf7cb8be5ad72921f5105bb429c62fa110475de07e255f4865fc5177df7c3f
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# roelvink.F90 — 판독 구간 기록

구간은 1행부터 320행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | private 모듈·공개 `roelvink,baldock,janssen_battjes` 선언(1–5), 저작권·LGPL(6–31). 각 generic 인터페이스에 1D/2D 루틴 연결(33–46), contains(48). |
| 49–76 | `roelvink_1D` 선언 및 저장 allocatable 배열(50–63). `if (.not. (allocated(kmr))) then` (65)이면 ny+1 크기 kmr,arg,H,hr 할당(66–69). H=파고, hr=hhw(73–74); `kmr = min(max(s%k(i,:), 0.01d0), 100.d0)` (75). |
| 77–96 | `if (par%break /= BREAK_ROELVINK_DALY) then` (77), 그 안의 `if (par%wci==1) then` (78): `arg = -( H / (par%gamma*tanh(kmr*hr)/kmr))**par%n` (79), else `arg = -( H / (par%gamma*hr              ))**par%n` (81). 78 조건 밖이면서 77 then 안의 `s%Qb(i,:) = min(1.d0 - exp(max(arg,-100.d0)), 1.d0)` (84). 77의 else(85)는 j 루프의 `if (s%wete(i,j)==1) then` (87), 그 안 `if (H(j) > par%gamma *hr(j)) then` (88)이면 Qb=1, `elseif (H(j) < par%gamma2*hr(j)) then` (90)이면 Qb=0(89,91), 그 외 기존 Qb 유지(92). |
| 97–115 | 앞 쇄파 조건 밖 기본 소산 `s%D(i,:) = s%Qb(i,:) * 2.d0 * par%alpha * s%E(i,:)` (97). `if (par%break == BREAK_ROELVINK1) then` (99), `if (par%wci==1) then` (100)이면 `s%D(i,:) = s%D(i,:) * s%sigm(i,:)/2.d0/par%px;` (101), else `s%D(i,:) = s%D(i,:) / par%Trep` (103). 99의 병렬 `elseif (par%break == BREAK_ROELVINK2 .or. par%break == BREAK_ROELVINK_DALY) then` (105)에서 `if (par%wci==1) then` (107)이면 `s%D(i,:) = s%D(i,:) * s%sigm(i,:)/2.d0/par%px * H/s%hh(i,:);` (108), else `s%D(i,:) = s%D(i,:) / par%Trep * H/s%hh(i,:)` (110). 종료(114). |
| 116–142 | `roelvink_2D`와 외부 루프 메모리 overhead 관련 주석(116–120), 선언(122–132). `if (.not. (allocated(kmr))) then` (134)이면 nx+1,ny+1 크기 kmr,arg 할당(135–136). `kmr = min(max(s%k, 0.01d0), 100.d0)` (141). |
| 143–164 | `if (par%break /= BREAK_ROELVINK_DALY) then` (143) 안의 `if (par%wci==1) then` (144): `arg = -( s%H / (par%gamma*tanh(kmr*s%hhw)/kmr))**par%n` (145), else `arg = -( s%H / (par%gamma*s%hhw              ))**par%n` (147). 144 조건 밖·143 then 안에서 `s%Qb(imin_ee:imax_ee,jmin_ee:jmax_ee) = min(1.d0 - exp(max(arg(imin_ee:imax_ee,jmin_ee:jmax_ee),-100.d0)), 1.d0)` (150). 143의 else는 ee 범위 루프(152–153), `if (s%wete(i,j)==1) then` (154)이고 `if (s%H(i,j) > par%gamma *s%hhw(i,j)) then` (155)이면 Qb=1(156), 병렬 `elseif (s%H(i,j) < par%gamma2*s%hhw(i,j)) then` (157)이면 Qb=0(158), 나머지는 유지(159). |
| 165–184 | 앞 조건 밖 `s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) = s%Qb(imin_ee:imax_ee,jmin_ee:jmax_ee) * 2.d0 * par%alpha * s%E(imin_ee:imax_ee,jmin_ee:jmax_ee)` (165). `if (par%break == BREAK_ROELVINK1) then` (167) 안의 `if (par%wci==1) then` (168)이면 `s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) = s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) * s%sigm(imin_ee:imax_ee,jmin_ee:jmax_ee)/2.d0/par%px;` (169), else `s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) = s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) / par%Trep` (171). 167의 병렬 `elseif (par%break == BREAK_ROELVINK2 .or. par%break == BREAK_ROELVINK_DALY) then` (173) 안의 `if (par%wci==1) then` (175)이면 `s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) = s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) * s%sigm(imin_ee:imax_ee,jmin_ee:jmax_ee)/2.d0/par%px * s%H(imin_ee:imax_ee,jmin_ee:jmax_ee)/s%hh(imin_ee:imax_ee,jmin_ee:jmax_ee)` (176), else `s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) = s%D(imin_ee:imax_ee,jmin_ee:jmax_ee) / par%Trep * s%H(imin_ee:imax_ee,jmin_ee:jmax_ee)/s%hh(imin_ee:imax_ee,jmin_ee:jmax_ee)` (178). 183에서 루틴 끝. |
| 185–210 | `baldock_1D` 인수·배열 선언(185–197). `if (.not. (allocated(kh))) then` (199)이면 kh,f,k,H,Hb,R,gamma 각각 ny+1로 할당(200–206). Baldock et al.(1998) 주석(209). |
| 211–234 | k 복사(211). `if (par%wci==1) then` (212)이면 `f = s%sigm(i,:) / 2.d0 / par%px` (213), else `f = 1.d0 / par%Trep` (215). 조건 밖 `kh  = s%k(i,:) * s%hhw(i,:)` (218). 별도 `if (par%wci==1) then` (220)이면 `gamma = 0.76d0*kh + 0.29d0` (221, 주석 Ruessink et al.1998), else `gamma = par%gamma` (223). 조건 밖 H 복사(226), `Hb  = tanh(gamma*kh/0.88d0)*(0.88d0/max(k,1d-10))` (227), `R   = Hb/max(H,0.00001d0)` (228), `s%Qb(i,:)   = exp(-R**2)` (230), `s%D (i,:)   = 0.25d0 * par%alpha * f * par%rho * par%g * (Hb**2+H**2) * s%Qb(i,:)` (231). |
| 235–252 | `baldock_2D` 선언(235–245), i=1:nx+1에서 `baldock_1D(par,s,i)` 호출(247–249), 종료. |
| 253–281 | `janssen_battjes_1D` 선언·`math_tools`의 xerf 의존(253–267). `if (.not. (allocated(kh))) then` (269)이면 kh,f,k,H,Hb,R 각각 ny+1 할당(270–275). Janssen and Battjes(2007) 주석(278), B=alpha(280). |
| 282–301 | k 복사(282). `if (par%wci==1) then` (283)이면 `f = s%sigm(i,:) / 2.d0 / par%px` (284), else `f = 1.d0 / par%Trep` (286). 조건 밖 `kh  = s%k(i,:) * s%hhw(i,:)` (289), H 복사(291), `Hb  = tanh(par%gamma*kh/0.88d0)*(0.88d0/k)` (292), `R   = Hb/max(H,0.00001d0)` (293). `s%Qb(i,:)   = 1 + 4/(3*sqrt(par%px)) * (R**3 + 1.5d0*R) * exp(-R**2) - xerf(R)` (295), `xerf` 사용; 이전 식은 주석(296–297). `s%D (i,:)   = 3*sqrt(par%px)/16      * B * f * par%rho * par%g * H**3/s%hh(i,:) * s%Qb(i,:)` (298), 종료. |
| 302–320 | `janssen_battjes_2D` 선언(302–312), i=1:nx+1에서 `janssen_battjes_1D(par,s,i)` (314–316). 루틴·모듈 끝(318–320). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 65–70·134–137·199–207·269–276: 저장 배열은 할당 여부만 보고 최초 할당한다. 이미 할당된 배열의 격자 크기 변경을 검사하거나 재할당하는 코드는 없다.
- 87–93·154–160: Daly 분기에서 마른 셀 또는 두 임계값 사이/임계값과 같은 파고는 Qb 대입을 하지 않는다.
- 227·292: Baldock의 Hb 분모는 `max(k,1d-10)`이고 Janssen–Battjes의 Hb 분모는 k 그대로다.
- 150·165–178·247–249·314–316: Roelvink 2D의 Qb/D 갱신은 ee 인덱스 범위이며, 다른 두 2D wrapper는 i=1:nx+1 전체에서 1D 루틴을 호출한다.

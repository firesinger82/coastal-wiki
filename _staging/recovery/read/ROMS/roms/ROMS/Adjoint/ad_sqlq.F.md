---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_sqlq.F
lines: 303
sha256: fe3ea9593d4e7dbdacc43d2a25aa850cc5b4f60b5fedb707d92e7cfe6ab37206
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_sqlq.F — 판독 구간 기록

구간은 1행부터 303행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. 전처리 조건은 `#if (defined SENSITIVITY_4DVAR \|\| defined TL_RBL4DVAR \|\| \` (3), `     defined TL_R4DVAR)        && defined MINRES` (4)이다. 이 조건 안에서 ad_sqlq(innLoop,a,ad_a,tau,ad_tau,y,ad_y)를 선언한다(6). 정방 행렬 A의 LQ 분해(LQ factorization)의 수반(adjoint)을 수행하고 여섯 실수 인수 모두 반환 시 덮어쓴다는 주석(15–18). mod_kinds·implicit none(22–24), 입력 정수 innLoop와 intent(inout) 정방 행렬 a·ad_a, 길이 innLoop의 tau·ad_tau·y·ad_y(28–32), 정수·실수 작업 변수 및 as(innLoop,innLoop)·arow(innLoop) 선언(36–42), 구분 주석(44–47). |
| 48–83 | 시작 시 3–4행 전처리 조건·6행 ad_sqlq 안. ad_znorm·ad_zbeta·ad_zaii·ad_ztemp 및 ad_y·arow를 0으로 초기화한다(48–55). 두 루프로 a를 as에 복사한다(59–63). 역순 `DO ii=innLoop-1,1,-1` (65) 안에서 `ad_zaii=ad_zaii+ad_a(ii,ii)` (68), ad_a(ii,ii)=0(69). a를 as로 복원한다(73–77). `iflag=1` (79), kk=ii·m=innLoop(80–81)로 설정하고 `call reclqbs (iflag, kk, m, a, tau, y)` (82)를 호출한다. 대응 접선 선형(tangent linear) 대입은 `!^` 주석이다(66–67). |
| 84–121 | 시작 시 3–4행 전처리 조건·6행 ad_sqlq·65행 ii 역순 루프 안. `IF (tau(ii).ne.0.0_r8) THEN` (84) 안에서 `jj=ii-1` (85). j=1..innLoop-jj·i=1..innLoop-ii 루프(86·88)에서 `ztemp=-tau(ii)*a(ii,j+jj)` (87), `ad_ztemp=ad_ztemp+y(i)*ad_a(ii+i,j+jj)` (92), `ad_y(i)=ad_y(i)+ztemp*ad_a(ii+i,j+jj)` (93). i 루프 뒤 `ad_tau(ii)=ad_tau(ii)-a(ii,j+jj)*ad_ztemp` (97), `ad_a(ii,j+jj)=ad_a(ii,j+jj)-tau(ii)*ad_ztemp` (98), ad_ztemp=0(99). 다음 j·i 루프(102·104)는 `ztemp=a(ii,j+jj)` 복사(103), `ad_ztemp=ad_ztemp+a(ii+i,j+jj)*ad_y(i)` (108), `ad_a(ii+i,j+jj)=ad_a(ii+i,j+jj)+ztemp*ad_y(i)` (109), i 루프 뒤 `ad_a(ii,j+jj)=ad_a(ii,j+jj)+ad_ztemp` (113), ad_ztemp=0(114). ad_y 전체를 0으로 설정한다(117–120). END IF(121). 접선 선형 대응식은 주석이다(89–91·95–96·105–107·111–112·118). |
| 122–156 | 시작 시 3–4행 전처리 조건·6행 ad_sqlq·65행 ii 역순 루프 안이며 84행 조건 밖. ad_a(ii,ii)=0(124), `ad_a(ii,ii)=ad_a(ii,ii)+ad_zaii` (127), ad_zaii=0(128), `ad_zbeta=ad_zbeta+ad_a(ii,ii)` (131), ad_a(ii,ii)=0(132).a를 as로 복원한다(136–140). `iflag=2` (142), kk=ii·m=innLoop(143–144), reclqbs 재호출(145). znorm=0(147) 뒤 j=ii+1..innLoop 루프(148–150)에서 `znorm=znorm+a(ii,j)*a(ii,j)` (149). `znorm=SQRT(znorm)` (151), `zbeta=SQRT(znorm*znorm+a(ii,ii)*a(ii,ii))` (152), zbetas=zbeta 복사(153), `zbeta=-SIGN(zbeta,a(ii,ii))` (154), `tau(ii)=(zbeta-a(ii,ii))/zbeta` (155). 접선 선형 대응 대입은 주석이다(122–123·125–126·129–130). |
| 157–197 | 시작 시 3–4행 전처리 조건·6행 ad_sqlq·65행 ii 역순 루프 안. j=ii+1..innLoop 루프(157–167)에서 arow(j)=a(ii,j) 복사(158), `a(ii,j)=a(ii,j)/(a(ii,ii)-zbeta)` (159), `adfac=ad_a(ii,j)/(a(ii,ii)-zbeta)` (163), `ad_zbeta=ad_zbeta+a(ii,j)*adfac` (164), `ad_a(ii,ii)=ad_a(ii,ii)-a(ii,j)*adfac` (165), ad_a(ii,j )=adfac(166). 루프 밖 `adfac=ad_tau(ii)/zbeta` (170), `ad_zbeta=ad_zbeta+adfac-tau(ii)*adfac` (171), `ad_a(ii,ii)=ad_a(ii,ii)-adfac` (172), ad_tau(ii)=0(173), `ad_zbeta=-SIGN(1.0_r8,zbetas)*SIGN(1.0_r8,a(ii,ii))*ad_zbeta` (176). `IF (zbetas.NE.0.0_r8) THEN` (177)에서는 `adfac=ad_zbeta/zbetas` (180), `ad_znorm=ad_znorm+znorm*adfac` (181), `ad_a(ii,ii)=ad_a(ii,ii)+a(ii,ii)*adfac` (182), ad_zbeta=0(183). ELSE(184)도 ad_zbeta=0(187). `IF (znorm.NE.0.0_r8) THEN` (189)에서는 `ad_znorm=0.5_r8*ad_znorm/znorm` (192), ELSE(193)는 ad_znorm=0(196). END IF(197). 대응 접선 선형 식은 `!^` 주석이다(160–162·168–169·174–175·178–179·185–186·190–191·194–195). |
| 198–215 | 시작 시 3–4행 전처리 조건·6행 ad_sqlq·65행 ii 역순 루프 안. j=ii+1..innLoop 루프(198–202)에서 `ad_a(ii,j)=ad_a(ii,j)+2.0_r8*arow(j)*ad_znorm` (201). 접선 선형 식은 주석이다(199–200·203–204). ad_znorm=0(205) 뒤 ii 역순 루프 종료(206). i=1..innLoop에서 ad_tau를 모두 0으로 설정한다(207–211). RETURN·루틴 종료(213–214), 빈 줄(215). |
| 216–247 | 시작 시 3–4행 전처리 조건 안. reclqbs(iflag,kk,innLoop,a,tau,y) 루틴(216)은 LQ 분해의 중간 배열을 재계산한다는 주석(220–221)을 둔다. mod_kinds·implicit none(225–227), 입력 정수 innLoop·iflag·kk와 intent(inout) a·tau·y(231–233), 지역 변수(237–238), 주석(240–243). i=1..innLoop 루프에서 tau 전체를 0으로 설정한다(244–246). |
| 248–272 | 시작 시 3–4행 전처리 조건·216행 reclqbs 안. `DO ii=1,kk` (248)에서 기본 반사자(elementary reflector) H(ii)로 A(ii,ii+1:innLoop)를 제거한다는 주석(250). znorm=0(252), j=ii+1..innLoop 루프(253–255)에서 `znorm=znorm+a(ii,j)*a(ii,j)` (254). `znorm=SQRT(znorm)` (256), `zbeta=SQRT(znorm*znorm+a(ii,ii)*a(ii,ii))` (257), `zbeta=-SIGN(zbeta,a(ii,ii))` (258), `tau(ii)=(zbeta-a(ii,ii))/zbeta` (259). `IF ((iflag.eq.2).and.(ii.eq.kk)) RETURN` (261)으로 조기 반환한다. 다음 j 루프(263–265)에서 `a(ii,j)=a(ii,j)/(a(ii,ii)-zbeta)` (264), 대각 원소에 zbeta 복사(266). 우측 반사자 적용 주석(268), zaii에 대각 원소 저장(270), `a(ii,ii)=1.0_r8` (271). |
| 273–303 | 시작 시 3–4행 전처리 조건·216행 reclqbs·248행 ii 루프 안. `IF (tau(ii).ne.0.0_r8) THEN` (273)에서 y 전체=0(274–276), `jj=ii-1` (277). j=1..innLoop-jj·i=1..innLoop-ii 루프(278·280)에서 `ztemp=a(ii,j+jj)` 복사(279), `y(i)=y(i)+ztemp*a(ii+i,j+jj)` (281). `IF ((iflag.eq.1).and.(ii.eq.kk)) RETURN` (285). 이어 같은 j·i 범위의 루프(287·289)에서 `ztemp=-tau(ii)*a(ii,j+jj)` (288), `a(ii+i,j+jj)=a(ii+i,j+jj)+y(i)*ztemp` (290). 조건 종료(293) 뒤 a(ii,ii)=zaii 복원(294), ii 루프 종료(295), RETURN·루틴 종료(297–298). `#else` (299)는 3–4행 조건 불성립 분기이며 인수 없는 ad_sqlq가 RETURN만 수행한다(300–302). `#endif` (303). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 152–180·257–264: tau 재계산은 zbeta로 나누고 행 정규화는 a(ii,ii)-zbeta로 나눈다. 이 대입 앞에 해당 분모의 0 여부를 검사하는 분기는 없다. 177행의 zbetas 검사와 189행의 znorm 검사는 뒤에 있다.
- 32·52–55·207–211: ad_y와 ad_tau는 intent(inout)이다. ad_y 전체는 루틴 시작에서 0으로 설정한다. ad_tau 전체는 역순 루프가 끝난 뒤 0으로 설정한다.
- 261·273·285: iflag=2의 최종 ii 조기 반환은 tau 조건 밖에 있다. iflag=1의 최종 ii 조기 반환은 tau(ii).ne.0.0_r8 조건 안에 있다.

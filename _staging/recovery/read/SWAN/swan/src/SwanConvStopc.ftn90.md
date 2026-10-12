---
file: models/SWAN/raw/source_code/swan/src/SwanConvStopc.ftn90
lines: 272
sha256: b94cb5bd2fd819b059324fecd12ff3b0fd26f62500844e5f2ec0ea4df3586b97
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanConvStopc.ftn90 — 판독 구간 기록

구간은 1행부터 272행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–64 | `SwanConvStopc` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–42). 파고와 평균주기의 반복곡선 곡률(curvature)로 수렴을 점검한다는 목적(44–46). QC 모형(QC modelling)에서는 파고의 절대·상대 변화만 쓰며 산란(scattering)·쇄파(surf breaking)로 파고가 급변할 수 있다는 방법 주석(48–52). 통신·병렬·격자 모듈과 `implicit none`(56–63). 방법 주석은 산란 및/또는 쇄파에 따른 파고의 내재적인 급변 때문에 곡률 기준이 위험하다고 명시한다(51–52). [10-13 전수 검증 보완] |
| 65–122 | 시작 시 1행 루틴 안. 시험점 배열, `intent(inout)` 정확도 `accur`, 입력 작용밀도·주파수, 출력 차이 배열, 현재·이전 반복의 파고·평균주기 및 두 반복 간 차이 배열을 선언한다(67–79). 곡률·허용오차·모멘트·카운터·플래그·꼭짓점 포인터 선언(83–111). `ient = 0` 초기값(84). 공통 블록 `convstopc`에 `npacc,nwetp`를 둔다(115). 구조·소스 안내 주석(117–122). `accur`는 요구 정확도를 달성한 활성 꼭짓점의 백분율이다(69). `hsdifc`와 `tmdifc`의 선언 주석은 현재 반복과 전전 반복 사이의 차이를 가리킨다(74,77). [10-13 전수 검증 보완] |
| 123–163 | 시작 시 1행 루틴 안. 추적 조건·호출은 `if (ltrace) call strace (ient,'SwanConvStopc')` (123)이다. 꼭짓점 객체 연결(127). 카운터 초기값은 `npacc = 0.`(129), `nwetp = 0.`(130)이다. 차이 배열 초기값은 `deltm = 0.`(132), `delhs = 0.`(133)이다. 헤더 초기값은 `lhead = .true.`(135)이다. `do ivert = 1, nverts`(139)의 활성 조건은 `if ( vert(ivert)%active ) then` (141)이다. 시험점 조건은 `if ( NPTST > 0 ) then` (146), `do j = 1, NPTST`(147) 안의 `if ( ivert /= xytst(j) ) cycle` (148)이다. 시험점 플래그 초기값은 `tstfl = .false.`(145)이다. 일치 시 `tstfl = .true.`(149)로 둔다. 시험점 루프는 150행에서 닫힌다. 시험점 조건은 151행에서 닫힌다. 활성 수 증가식은 `nwetp = nwetp + 1.` (155)이다. 이전 두 반복의 값 보관 및 하한 설정식은 `hsprev0       = max( 1.e-20, hsprev(ivert) )` (159); `hsprev(ivert) = max( 1.e-20, hscurr(ivert) )` (160); `tmprev0       = max( 1.e-20, tmprev(ivert) )` (161); `tmprev(ivert) = max( 1.e-20, tmcurr(ivert) )` (162)이다. [10-13 전수 검증 보완] |
| 164–199 | 시작 시 1행 루틴·139행 꼭짓점 루프·141행 활성 참 분기 안. `m0 = 0.`(166), `m1 = 0.`(167)으로 초기화하고 `do is = 1, MSC`, `do id = 1, MDC`(168–169)에서 `fact = spcsig(is)**2 * ac2(id,is,ivert)` (170); `m0 = m0 + fact` (171); `m1 = m1 + fact * spcsig(is)` (172)로 누적한다. 적분 계수 적용식은 `m0 = m0 * FRINTF * DDIR` (175); `m1 = m1 * FRINTF * DDIR` (176)이다. `if ( m0 > 0. ) then` (178)이면 `hscurr(ivert) = max ( 1.e-20, 4.*sqrt(m0) )` (179)이다. 앞 조건이 거짓일 때의 후속 분기 `elseif ( IQCM /= 0 .and. m0 < 0. ) then` (180)이면 `hscurr(ivert) = -1.` (181); `nwetp = nwetp - 1.` (182)이다. `else` (183) 분기는 `hscurr(ivert) = 1.e-20` (184)이다. 평균주기 조건은 `if ( m1 > 0. ) then` (186)이며 참 분기는 `tmcurr(ivert) = max ( 1.e-20, PI2*(m0/m1) )` (187), `else` (188) 분기는 `tmcurr(ivert) = 1.e-20` (189)이다. 절대차 식은 `hsabs = abs ( hscurr(ivert) - hsprev(ivert) )` (194); `tmabs = abs ( tmcurr(ivert) - tmprev(ivert) )` (195)이다. `delhs(ivert) = hsabs`(197), `deltm(ivert) = tmabs`(198)로 차이를 복사한다. 방향 루프는 173행에서 닫힌다. 주파수 루프는 174행에서 닫힌다. 파고 분기 사슬은 185행에서 닫힌다. 평균주기 분기는 190행에서 닫힌다. [10-13 전수 검증 정정] [10-13 전수 검증 보완] |
| 200–239 | 시작 시 1행 루틴·139행 꼭짓점 루프·141행 활성 참 분기 안. `hsdif0        = hsdifc(ivert)`(202), `tmdif0        = tmdifc(ivert)`(208)로 이전 차이를 보관한다. 파고 곡률 계산식은 `hsdifc(ivert) = 0.5*( hscurr(ivert) - hsprev0 )` (203); `hscurv        = abs ( hsdifc(ivert) - hsdif0 )` (204), 평균주기 곡률 계산식은 `tmdifc(ivert) = 0.5*( tmcurr(ivert) - tmprev0 )` (209); `tmcurv        = abs ( tmdifc(ivert) - tmdif0 )` (210)이다. 허용오차 식은 `hsrel  = PNUMS( 1) * hscurr(ivert)` (214); `curvah = PNUMS(15) * hscurr(ivert)` (215), `tmrel  = PNUMS( 1) * tmcurr(ivert)` (219); `curvat = PNUMS(16) * tmcurr(ivert)` (220)이다. `if ( IQCM == 0 ) then` (222)이면 수렴 논리식 `lconv = ( hsabs <= PNUMS(2) .or. (hsabs <= hsrel .and. hscurv <= curvah) ) .and. &` (224); `( tmcurv <= curvat .and. tmabs <= max(tmrel,PNUMS(3)) )` (225)를 쓴다. `else` (227) 분기에서는 `if ( hscurr(ivert) /= -1. .and. hsprev(ivert) /= 1.e-20 ) then` (229)일 때 `lconv = hsabs <= max(hsrel,PNUMS(2))` (231)로 파고 변화만 검사한다. 내부 `else` (233) 분기는 `lconv = .false.`를 설정한다(235). 229행 조건은 237행에서 닫힌다. 222행 조건은 239행에서 닫힌다. 바깥 활성 조건은 256행에서 닫힌다. 바깥 꼭짓점 루프는 258행에서 닫힌다. [10-13 전수 검증 보완] |
| 240–258 | 시작 시 1행 루틴·139행 꼭짓점 루프·141행 활성 참 분기 안. 수렴 수 누적은 `if ( lconv ) npacc = npacc + 1.` (243)이다. 시험점 출력 조건은 `if ( tstfl .and. IQCM==0 ) then` (245), 헤더 출력 조건은 `if (lhead) write(PRINTF,11)` (246)이다. 출력문은 `write (PRINTF,12) ivert, hsabs, hsabs/hscurr(ivert), hscurv/hscurr(ivert), tmabs, tmabs/tmcurr(ivert), tmcurv/tmcurr(ivert)`(247)이다. 같은 분기에서 `lhead = .false.`(248)로 둔다. 출력 분기는 249행에서 닫힌다. 활성 조건의 `else` (251) 분기는 `hscurr(ivert) = 1.e-20` (253); `tmcurr(ivert) = 1.e-20` (254)로 현재 값을 설정한다. 조건·꼭짓점 루프 종료(256–258). [10-13 전수 검증 보완] |
| 259–272 | 시작 시 1행 루틴 안이며 꼭짓점 루프 밖. 활성 수와 수렴 수에 대해 `SWREDUCE(...,SWREAL,SWSUM)`을 호출한다(262–263). 요구 정확도를 달성한 활성 꼭짓점의 백분율 조건·식은 `if ( nwetp > 0. ) accur = ceiling(npacc*10000./nwetp)/100.` (267)이다. 출력 형식 11·12와 루틴 종료(269–272). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 178–198·203–235: `IQCM/=0`이며 `m0<0`이면 파고를 -1로 두고 활성 수에서 1을 뺀다. 그 뒤 차이·곡률 계산을 계속한다. 229행 조건은 파고가 -1이면 수렴을 거짓으로 둔다.
- 69·267: `accur`는 `intent(inout)`이다. `nwetp>0`이 아니면 이 루틴은 `accur`에 새 값을 대입하지 않는다.
- 203·209: 두 반복 간 차이 계산의 계수는 0.5로 고정되어 있다. 곡률 허용오차는 현재 파고와 현재 평균주기로 계산한다(214–220).

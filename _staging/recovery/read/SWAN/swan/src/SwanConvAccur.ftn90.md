---
file: models/SWAN/raw/source_code/swan/src/SwanConvAccur.ftn90
lines: 241
sha256: 2a3218fd337674bb05a0018b82be15f663069bece946859d8f43f9a5a169a5f1
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanConvAccur.ftn90 — 판독 구간 기록

구간은 1행부터 241행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | `SwanConvAccur` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–38). 적분 매개변수(integral parameter)의 정확도로 수렴(convergence)을 점검한다는 목적(40–42). 통신·병렬·격자 모듈과 `implicit none`(46–53). 빈 주석(54). |
| 55–104 | 시작 시 1행 루틴 안. 시험점(test point) `xytst`, 정확도 달성 꼭짓점 비율 `accur`, 입력 작용밀도·주파수, 출력 파고·평균주기(mean period) 차이, 현재 파고·평균주기 배열을 선언한다(57–65). 적분 모멘트(moment), 절대차·상대 및 전체 허용오차, 활성 꼭짓점 수, 시험점 플래그, 꼭짓점 포인터를 선언한다(69–94). `ient = 0` 초기값(70). 공통 블록(common block) `convaccur`에 `npacc,nwetp,hsmean,tmmean`을 둔다(97). 구조·소스 안내 주석(99–104). `accur`의 단위는 백분율이다(59). [10-13 전수 검증 보완] |
| 105–148 | 시작 시 1행 루틴 안. 추적 조건은 `if (ltrace) call strace (ient,'SwanConvAccur')` (105)이다. 꼭짓점 포인터 연결(109). 카운터 초기값은 `npacc = 0.`(111), `nwetp = 0.`(112)이다. 평균 초기값은 `hsmean = 0.`(114), `tmmean = 0.`(115)이다. 차이 배열 초기값은 `deltm = 0.`(117), `delhs = 0.`(118)이다. 헤더 플래그 초기값은 `lhead = .true.`(120)이다. `hsmean = 0.`(124), `tmmean = 0.`(125)으로 평균을 다시 초기화한다. `do ivert = 1, nverts`(127)와 `if ( vert(ivert)%active ) then` (129) 안에서 `nwetp = nwetp + 1.` (131), `hsmean = hsmean + hscurr(ivert)` (133); `tmmean = tmmean + tmcurr(ivert)` (134)로 활성 꼭짓점 수와 이전 반복의 공간 합을 누적한다. `SWREDUCE`를 각각 `SWSUM`으로 호출한다(142–144). 평균식은 `hsmean = hsmean/nwetp` (146); `tmmean = tmmean/nwetp` (147)이다. 주석·빈 줄 포함. 활성 조건은 136행에서 닫힌다. 꼭짓점 루프는 138행에서 닫힌다. [10-13 전수 검증 보완] |
| 149–194 | 시작 시 1행 루틴 안. `do ivert = 1, nverts`(151)의 활성 조건은 `if ( vert(ivert)%active ) then` (153)이다. 시험점 검사 조건은 `if ( NPTST > 0 ) then` (158), `do j = 1, NPTST`(159) 안의 `if ( ivert /= xytst(j) ) cycle` (160)이다. 시험점 플래그 초기값은 `tstfl = .false.`(157)이다. 일치 시 `tstfl = .true.`(161)로 둔다. 시험점 루프는 162행에서 닫힌다. 시험점 검사 조건은 163행에서 닫힌다. 이전 값 하한은 `hsprev = max( 1.e-20, hscurr(ivert) )` (167); `tmprev = max( 1.e-20, tmcurr(ivert) )` (168)이다. `do is = 1, MSC`와 `do id = 1, MDC`(174–175)의 모멘트 누적식은 `fact = spcsig(is)**2 * ac2(id,is,ivert)` (176); `m0 = m0 + fact` (177); `m1 = m1 + fact * spcsig(is)` (178)이다. 적분 계수 적용식은 `m0 = m0 * FRINTF * DDIR` (181); `m1 = m1 * FRINTF * DDIR` (182)이다. `if ( m0 > 0. ) then` (184)의 참 분기는 `hscurr(ivert) = max ( 1.e-20, 4.*sqrt(m0) )` (185), `else` (186) 분기는 `hscurr(ivert) = 1.e-20` (187)이다. `if ( m1 > 0. ) then` (189)의 참 분기는 `tmcurr(ivert) = max ( 1.e-20, PI2*(m0/m1) )` (190), `else` (191) 분기는 `tmcurr(ivert) = 1.e-20` (192)이다. 조건 종료·주석(193–194). 모멘트 초기값은 `m0 = 0.`(172), `m1 = 0.`(173)이다. 방향 루프는 179행에서 닫힌다. 주파수 루프는 180행에서 닫힌다. `m0` 조건은 188행에서 닫힌다. `m1` 조건은 193행에서 닫힌다. 바깥 활성 조건은 226행에서 닫힌다. 바깥 꼭짓점 루프는 228행에서 닫힌다. [10-13 전수 검증 보완] |
| 195–228 | 시작 시 1행 루틴·151행 꼭짓점 루프·153행 활성 참 분기 안. 절대차 식은 `hsabs = abs ( hscurr(ivert) - hsprev )` (197); `tmabs = abs ( tmcurr(ivert) - tmprev )` (198)이다. `delhs(ivert) = hsabs`(200), `deltm(ivert) = tmabs`(201)로 절대차를 복사한다. 허용오차 식은 `hsrel  = PNUMS( 1) * hsprev` (205); `hsoval = PNUMS(15) * hsmean` (206), `tmrel  = PNUMS( 1) * tmprev` (208); `tmoval = PNUMS(16) * tmmean` (209)이다. 정확도 달성 계수 조건·누적식은 `if ( hsabs <= max(hsrel,hsoval) .and. tmabs <= max(tmrel,tmoval) ) npacc = npacc + 1.` (213)이다. 출력 조건은 `if (tstfl) then` (215), 헤더 출력 조건은 `if (lhead) write(PRINTF,11)` (216)이다. 시험점 출력은 `write (PRINTF,12) ivert, hsabs/hsprev, hsabs/hsmean, tmabs/tmprev, tmabs/tmmean`(217)이다. 같은 분기에서 `lhead = .false.`(218)로 둔다. 시험점 출력 분기는 219행에서 닫힌다. 활성 조건의 `else` (221) 분기는 `hscurr(ivert) = 1.e-20` (223); `tmcurr(ivert) = 1.e-20` (224)로 현재 파고·평균주기를 설정한다. 조건·꼭짓점 루프 종료(226–228). [10-13 전수 검증 보완] |
| 229–241 | 시작 시 1행 루틴 안이며 꼭짓점 루프 밖. `SWREDUCE(npacc,1,SWREAL,SWSUM)`을 호출한다(232). 활성 꼭짓점 중 요구 정확도를 달성한 꼭짓점의 백분율 계산 조건·식은 `if ( nwetp > 0. ) accur = ceiling(npacc*10000./nwetp)/100.` (236)이다. 11·12번 출력 형식(format), 주석, 루틴 종료(238–241). [10-13 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 146–147: 공간 평균은 `nwetp`로 나눈다. 이 대입 앞에는 `nwetp>0` 조건이 없다.
- 59·236: `accur`는 `intent(out)`이다. `nwetp>0`일 때만 `accur`에 대입하는 문장이 있다.
- 80·114–125: `hsmean`과 `tmmean`은 114–115행에서 0으로 설정된다. 두 변수는 124–125행에서 다시 0으로 설정된다. 변수 이름과 달리 두 평균은 면적 가중치 없이 활성 꼭짓점 수로 나눈다(133–147).

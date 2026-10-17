# FUNWAVE 외부 원문 조회 (2026-10-18)

조회: sonnet 웹 조회(Claude 하위 작업). 판정 대상: `compare/funwave-theory-numerics-vs-code.md` E 행 중 `Beta_2` 배수에서 나온 행(FT1-021·024·028·029·031·034·208–227 등). git 판정(`FUNWAVE-git-verify-E1.md`)은 이 행들을 모두 E 유지(강함)로 두었다.

## 코드

- `FUNWAVE-TVD/src/init.F:662` `! kennedy equation`
- `FUNWAVE-TVD/src/init.F:663` `Beta_1=Beta_ref+1.0_SP`
- `FUNWAVE-TVD/src/init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP` (값 0.04). `# if defined (CARTESIAN)` (656) 안이다. 이 줄은 공개 저장소 최초 커밋 cab9425 2016-03-02 "first add to repository"의 `cab9425:init.F:497`에 이미 있다. b9c035d 2016-11-03은 파일을 `src/`로 옮긴 커밋이다(`git log -S`가 경로 이동 때문에 b9c035d를 처음으로 보여 준다). [10-18 Claude 정정]
- `FUNWAVE-TVD/src/dispersion.F:312` `ken1 = ( 1.0_SP/6.0_SP - Beta_1 + Beta_1*Beta_1 )*rh*reta*Beta_2   &`, `:313` `+ ( 1.0_SP/2.0_SP*Beta_1*Beta_1 - 1.0_SP/6.0_SP )*reta*reta*Beta_2*Beta_2`, `:314` `ken2 = ( Beta_1 - 1.0_SP/2.0_SP )*reta*Beta_2`. 수면 높이 eta에 비례하는 항마다 Beta_2를 곱한다.

## 외부 원문

| 출처 | 확인한 문장(원문) | 판정에 쓴 사실 |
|---|---|---|
| Kennedy et al., ICCE 2000 학회판, https://www1.udel.edu/kirby/papers/kennedy-etal-icce00.pdf (쪽 이미지로 읽음) | "The resulting redundancy was removed by specifying β = β1 = β2"; "the result γ = 17/200 is obtained, where γ = β(1 + (ζ1+ζ2)/2)"; "(A = 0.425, B = 1/5 ...)" | 기준 높이는 z_α1 = ζ1·h + β1·η, z_α2 = ζ2·h + β2·η이다. η 계수는 β이고 γ = 17/200으로 맞춘다. B = 1/5는 선형 천수 계수이며 η에 곱하는 배수가 아니다. (1/5)^2 배수는 없다. |
| FUNWAVE-TVD 2.1 매뉴얼(CACR-11-04), https://www1.udel.edu/kirby/papers/shi-etal-cacr-11-04-version2.1.pdf | "We retain dimensional forms below"; "z_α = ζh + βη (4) ... as in Kennedy et al (2001)"; "z_α = −h + βH = (β − 1)h + βη = ζh + (1 + ζ)η (14)" | 식은 차원식이다. 무차원 순서 매개변수(δ², μ²)의 수치가 식에 남지 않는다. |
| GitHub 이슈 #46 "What is the use of beta_2?" (2021-04-01), https://github.com/fengyanshi/FUNWAVE-TVD/issues/46 | "I have read the manual and the paper of Kenney, but I cannot find the beta_2 in any references." | 공개 저장소 사용자가 같은 질문을 했다. 조회 시점에 답이 없고 열린 상태다. |
| GitHub master `src/init.F`, https://raw.githubusercontent.com/fengyanshi/FUNWAVE-TVD/master/src/init.F | `! kennedy equation` / `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP` | 공개 최신 코드도 같다. |

접근하지 못한 원문: Kennedy et al. (2001) Wave Motion 33, 225–243 본문, Shi et al. (2012) Ocean Modelling 43–44, 36–51 본문(둘 다 유료). 위 학회판과 매뉴얼이 같은 저자의 같은 정식화를 적는다.

## 결론

- `Beta_2` 배수의 근거는 조회한 문헌 어디에도 없다. 같은 판 문서(3.0 부록 A 식 (109)–(120), 본문 식 (7))에도 없다. 코드 주석 `! kennedy equation`은 Kennedy 정식화를 가리키지만 그 정식화의 η 계수는 β이다.
- E(코드 결함 후보) 유지. 강도는 강함(같은 판 문서와 문헌 정식화 둘과 모순, 반대 근거는 주석 한 줄뿐이며 그 주석이 가리키는 문헌에 배수가 없다).
- `Beta_2` 배수에서 나온 E 행들은 원인이 하나다. 노트에는 원인 하나로 묶어 적고, 행마다 같은 원인임을 밝힌다.
- 이 판정은 정적 판독과 문헌 대조이며 모델을 실행해 영향을 재지 않았다.

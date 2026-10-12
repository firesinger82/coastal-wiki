---
file: models/SWAN/raw/source_code/swan/src/SwanDispParm.ftn90
lines: 111
sha256: 9a8cfe43220c1dc327491a59ad695bb0caebc9413090dfc5e45736a336723d46
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanDispParm.ftn90 — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | `SwanDispParm` 입구(1). 기관·GPL 3 이상·무보증·작성자·진흙 바닥(muddy bottom) 도입 이력(3–38). 계산 스텐실 꼭짓점의 분산(dispersion) 매개변수인 파수·군속도를 계산한다는 목적(40–43). 통신·격자·계산 데이터 모듈 사용과 `implicit none`(47–53). |
| 55–81 | 시작 시 1행 루틴 안. 출력 군속도 `cgo`, 진흙 소산률(mud dissipation rate) `dmw`, 파수 `kwave`의 크기는 `(MSC,ICMAX)`이다. 입력은 꼭짓점 수심·진흙 두께(mud thickness)와 상대 주파수이다(57–62). 스텐실·주파수·꼭짓점 순회 변수, 지역 수심·진흙 두께, 군속도/위상속도 비와 그 수심 미분 선언(66–74). `ient = 0` 초기값(67). 구조·소스 안내 주석(76–81). [10-13 전수 검증 보완] |
| 82–111 | 시작 시 1행 루틴 안. 추적 조건·호출은 `if (ltrace) call strace (ient,'SwanDispParm')` (82)이다. `do ic = 1, ICMAX`(84)에서 `ivert  = vs(ic)`(86)로 꼭짓점 번호를 읽는다. `deploc = dep2(ivert)`(87)로 수심을 읽는다. 진흙 두께 선택 조건은 `if (VARMUD) then` (89)이다. 참이면 `dm = mudl2(ivert)`(90)로 둔다. `else`(91)이면 `dm = PMUD(1)`(92)로 둔다. 진흙 두께 조건은 93행에서 닫힌다. 수심 조건은 `if ( deploc > DEPMIN ) then` (95)이다. 참이면 `KSCIP1`을 호출하고(97), 추가 진흙 분산 호출 조건은 `if ( IMUD == 1 ) call KSCIP2 (MSC, spcsig, deploc, kwave(1,ic), cgo(1,ic), n, nd, dmw(1,ic), dm)` (98)이다. 수심 조건의 `else` (100) 분기는 `do is = 1, MSC`(102)에서 `kwave(is,ic) = -1.`(103), `cgo  (is,ic) =  0.`(104), `dmw  (is,ic) =  0.`(105)을 설정한다. 주파수 루프는 106행에서 닫힌다. 조건·루프·루틴 종료(108–111). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 59·95–105: 수심이 `DEPMIN`보다 크고 `IMUD/=1`이면 `dmw`를 계산하는 호출이나 대입문이 이 루틴에 없다. 수심 조건의 else에서는 `dmw=0`을 설정한다.
- 73–74·97–98: `n`과 `nd`는 두 분산 계산 루틴의 인수로 전달된다. 이 파일에는 호출 뒤 두 배열을 사용하는 계산식이 없다.

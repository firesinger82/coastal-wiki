---
file: models/SWAN/raw/source_code/swan/src/SwanTranspX.ftn90
lines: 161
sha256: 1214cb32a7495f378f7d47ff3f59a160eaecdb0245703bd58ccab884c66c15f4
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanTranspX.ftn90 — 판독 구간 기록

구간은 1행부터 161행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | SwanTranspX 인수 목록(1–3). 기관·GPL 3 이상·무보증 머리말(5–29), 저자·2007–2008년 이력(32–39). 최저 차수 풍상 차분법(lowest order upwind scheme)으로 x-y 공간 수송(transport)을 계산한다는 목적(41–43). |
| 45–80 | 시작 시 1행 SwanTranspX 루틴 안. ocpcomm4·swcomm2·swcomm3·swcomm4·SwanGriddata·SwanCompdata 사용(47–52), implicit none(54). 입력 주파수 범위와 주파수별 방향 범위(58–62), 이전·현재 파작용 밀도(action density) ac1/ac2, 입출력 행렬(matrix) amat 선언(64–66). 1번 계수는 `(l  ,m  )` 중심이다(67). 2번과 3번 계수는 각각 `(l-1,m  )`과 `(l+1,m  )` 주파수 인접점이다(68–69). 4번과 5번 계수는 각각 `(l  ,m-1)`과 `(l  ,m+1)` 방향 인접점이다(70–71). 입력 cax/cay·전달 저감 obredf·반변 기저 벡터(contravariant base vector) rdx/rdy, 입출력 우변(right-hand side) rhs, 출력 수송 항 trac0/trac1 선언(72–79). 기저 성분 주석은 `rdx(b) = a^(b)_1` (75)과 `rdy(b) = a^(b)_2` (76)이다. [10-13 전수 검증 보완] |
| 81–108 | 시작 시 1행 루틴 안. 방향·주파수 인덱스, 계산 스텐실(computational stencil)의 iv1/iv2/iv3, `integer, save :: ient = 0 ! number of entries in this subroutine` (85), acold·asum·fac1/fac2·rsum 선언(83–95). 구조·소스 주석(97–101), `if (ltrace) call strace (ient,'SwanTranspX')` (103). 스텐실 인덱스는 `iv1 = vs(1)` (105), `iv2 = vs(2)` (106), `iv3 = vs(3)` (107)으로 복사한다. [10-13 전수 검증 보완] |
| 109–120 | 시작 시 1행 루틴 안. `if ( KSPHER == 0 ) then` (109)이면 `fac1 = 1.` (111)과 `fac2 = 1.` (112). `else` (114)는 구면좌표(spherical coordinates) 계수 `fac1 = COSLAT(2)/COSLAT(1)` (116); `fac2 = COSLAT(3)/COSLAT(1)` (117). 조건 종료(119). [10-13 전수 검증 보완] |
| 121–140 | 시작 시 1행 루틴 안. is=isslow..isstop(121), iddum=idcmin(is)..idcmax(is)(123), `id = mod ( iddum - 1 + MDC , MDC ) + 1` (124)로 방향 인덱스 순환. 행렬 기여는 `asum = (rdx(1)+rdx(2))*cax(id,is,1) + (rdy(1)+rdy(2))*cay(id,is,1)` (128), 우변 기여는 `rsum = (rdx(1)*cax(id,is,2) + rdy(1)*cay(id,is,2)*fac1)*obredf(id,is,1)*ac2(id,is,iv2) + &` (130); `(rdx(2)*cax(id,is,3) + rdy(2)*cay(id,is,3)*fac2)*obredf(id,is,2)*ac2(id,is,iv3)` (131). 수송 속도·기저 벡터·위도비·obredf·파상류 두 정점의 ac2를 사용한다. 조립은 `amat(id,is,1) = amat(id,is,1) + asum` (135); `rhs (id,is  ) = rhs (id,is  ) + rsum` (136), 출력 수송 항 누적은 `trac0(id,is,1) = trac0(id,is,1) - rsum` (138); `trac1(id,is,1) = trac1(id,is,1) + asum` (139). |
| 141–161 | 시작 시 1행 루틴·121행 is 루프·123행 iddum 루프 안. `if ( NSTATC == 1 ) then` (141)의 `if ( ITERMX == 1 ) then` (143)이면 `acold = ac2(id,is,iv1)` (144)로 현재 중심 값을 고른다, `else` (145)이면 `acold = ac1(id,is,iv1)` (146)로 이전 중심 값을 고른다. 시간항 추가는 `amat(id,is,1) = amat(id,is,1) + RDTIM` (149); `rhs (id,is  ) = rhs (id,is  ) + acold*RDTIM` (150), 출력 수송 항 시간 기여는 `trac0(id,is,1) = trac0(id,is,1) - acold*RDTIM` (152); `trac1(id,is,1) = trac1(id,is,1) + RDTIM` (153). 조건·방향·주파수 루프 종료(155·157·159), 루틴 종료(161). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 78–79·138–139·152–153: trac0/trac1은 intent(out)이다. 이 루틴의 대입은 기존 trac0/trac1 값에 항을 더하거나 빼는 형태이다. 루틴 안에는 두 배열을 먼저 초기화하는 실행문이 없다.
- 116–117·130–131: 구면 계수 fac1/fac2는 rsum에서 cay 항에만 곱한다. cax 항에는 해당 계수가 곱해지지 않는다.
- 116–117: fac1/fac2의 분모는 COSLAT(1)이다. 이 루틴에는 해당 값에 대한 0 검사문이 없다.

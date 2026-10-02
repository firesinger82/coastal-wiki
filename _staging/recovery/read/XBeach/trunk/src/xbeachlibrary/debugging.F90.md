---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/debugging.F90
lines: 634
sha256: 9efa26098d26ef96e2fdd29accd380e7cbc388ade28786ee31ec7cff1b4f54ee
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# debugging.F90 — 판독 구간 기록

구간은 1행부터 634행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | `debugging_module`. 2행의 `#if 0` 안에 본체를 둠; 전면 재작성 필요 주석(3). MPI용 compare 오버로드는 integer 2D·real 2D/3D(7–11), printsum은 real/integer 각각 rank 0..4(14–25). contains(27). |
| 29–50 | USEMPI 조건부 절. 분산 격자 이웃과 겹치는 `a(:,2)=al(:,ny+1)`, `a(2,:)=at(nx+1,:)`를 비교하며 양끝은 예외라는 설명(31–46). |
| 51–101 | `space_consistency`: mnem='ALL'이면 1..numvars, 아니면 `chartoindex`의 한 항목(61–67). `indextos` 후 real rank 2/3·integer rank 2만 `compare` 호출(69–95); 나머지 rank 호출은 주석. |
| 102–126 | `comparer2`: real 2D·선택 verbose, 임계 `eps=1.0d-60`(110), tideinpz는 즉시 return(119–122). m/n=size, c(m,2)·r(2,n) 임시 배열 할당(123–126). |
| 127–163 | 첫 두 열 저장 후 `xmpi_shift(SHIFT_Y_R,1,2)`(128–130). 내부 행과 전체 행의 절대차 합을 dif(1/2)에 넣고 MPI_SUM allreduce(134–138). master 로그·eps 초과 표시, verbose='verbose'이고 `sum(difmax)>eps`(149)일 때만 c·x 둘 중 하나가 0이 아닌 (i,j) 항목 출력(147–159). [10-02 검증 정정: 149행 조건 누락 보완] 원본 첫 두 열 복원(162). |
| 164–185 | 마지막 두 열 저장·`SHIFT_Y_L,3,4`·내부/전체 절대차 합·원본 복원(165–174). `xmpi_reduce(...,MPI_SUM)`, master에 차이·eps 경고 출력(176–183). |
| 186–206 | 첫 두 행 저장·`SHIFT_X_D,1,2`(187–189), 내부/전체 열 절대차 합·복원(193–195), MPI_SUM reduce와 master 로그(197–204). |
| 207–228 | 마지막 두 행도 `SHIFT_X_U,3,4`로 같은 비교·복원(208–216), MPI_SUM reduce·master 경고 로그(218–225). comparer2 종료. |
| 229–250 | `comparei2`: integer 2D, eps=0, c/r은 1D(232–242). 이중 경계 방식에 맞춰 수정하지 않았다는 메시지 출력 후 무조건 return(244–245). 뒤 verbose 미구현 출력(247–249)은 이 return 뒤에 있음. |
| 251–287 | return 뒤의 integer 비교 코드: m/n 크기·c/r 할당, 첫/마지막 열을 저장하고 문자열 `':1'`/`':n'`으로 `xmpi_shift`(251–273). 내부/전체 절대차 합·원본 복원·MPI_SUM reduce·master eps 경고(258–286). |
| 288–322 | integer 첫/마지막 행은 `'1:'`/`'m:'` shift(289·306), 내부/전체 절대차 합·원본 복원·MPI_SUM·master 로그(291–319). comparei2 종료. |
| 323–345 | `comparer3`: real 3D, eps=1e-60·m/n/l·2D c/r(326–335). 출력 메시지는 `comparei2 not adapted...`이며 무조건 return(337–338). 뒤에는 verbose 미구현 출력과 크기 계산(339–344). |
| 346–381 | return 뒤 real 3D 첫/마지막 y슬라이스 비교. c(m,l)·r(n,l) 할당, 문자열 shift·내부/전체 절대차 합·복원·MPI_SUM reduce·master 경고(346–379). |
| 382–418 | real 3D 첫/마지막 x슬라이스도 문자열 shift(383·400), 절대차 합·복원·reduce·로그(385–413). comparer3와 USEMPI 절 종료(415–417). |
| 419–440 | real `printsum0`는 scalar를 unit f에 id·이름과 출력(425). `printsum1`은 pointer associated면 sum·shape, 아니면 'Not allocated'(434–438). |
| 441–467 | real rank 2/3 pointer도 associated 검사 후 sum·shape 또는 'Not allocated'를 출력(447–451·461–465). |
| 468–489 | real rank4 pointer의 sum·shape 출력(474–478). integer scalar `printsumi0`는 값 그대로 출력(487). |
| 490–516 | integer rank1/2 pointer는 associated 확인 후 sum·shape 또는 'Not allocated'(496–500·509–513). |
| 517–542 | integer rank3도 pointer·associated(522–527), rank4는 allocatable·allocated로 검사(535–540); 모두 sum·shape/미할당 문자열 출력. |
| 543–565 | `printssums(s,str)`: MPI rank>0이면 return, 비MPI id=0(554–561). unit 번호 `f=100+4*numvars+id+1`(563), 시작 로그(565). |
| 566–608 | 모든 변수에 `indextos`, rank 0..4 및 type='i'/그 외에 맞는 printsum 오버로드 호출(566–600). MPI에서는 is/js/lm/ln도 출력(602–605). |
| 609–634 | `printssumso`는 표준출력에 xz/yz/zs/u/v/ue/ve/H/urms/zb/hh/Fx/Fy/E/R/D의 sum 출력(616–631). 루틴 종료, `#if 0` 닫기(633), 모듈 종료(634). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2·633: 인터페이스·contains·모든 루틴이 `#if 0`에 둘러싸여 있으며 전처리 조건상 제외된다.
- 244–245·337–338: comparei2와 comparer3는 안내 출력 후 무조건 return하므로 그 뒤 비교문에 도달하지 않는다. comparer3의 안내 문자열도 comparei2라고 되어 있다.
- 110·330: real 비교 경고 임계값은 두 루틴 모두 `1.0d-60`으로 고정되어 있다.
- 433–474·495–535: real 배열과 integer rank1..3은 pointer·associated인데 integer rank4만 allocatable·allocated이다.
- 563–565: printssums는 계산한 unit f에 write하며 이 루틴 안에는 명시적 open/close가 없다.

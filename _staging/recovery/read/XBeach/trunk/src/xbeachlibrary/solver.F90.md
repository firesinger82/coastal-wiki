---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/solver.F90
lines: 514
sha256: be97d575b3d32f1e0788b713123d0e0630997c2142e2d2990eab10201f9f90f7
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# solver.F90 — 판독 구간 기록

구간은 1행부터 514행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 모듈 머리·변경 이력·`solver_module`·MPI 관련 주석(1–22), `nh_pars.inc` 포함(25). `logical                  :: initialized = .false.` (30), itmea/itmin/itmax/ittot/itcal/itnconv는 0(32–37). 초기 설정 `real(kind=rKind)         :: reps  = 0.005_rKind` (39), `real(kind=rKind)         :: alpha = 0.94_rKind` (40), `integer(kind=iKind)      :: maxit = 30` (41). |
| 43–70 | allocatable residual(2차원)·work(3차원)(44–45), 공개 `solver_init,solver_free,solver_solvemat,solver_tridiag,solver_sip` (53–57), contains 및 구분 주석. |
| 71–108 | `solver_init` 선언·목적/이력 주석·의존 모듈·par,nx,ny 입력(71–104), 구현 구분 머리말(106–108). |
| 109–129 | reps=solver_acc, alpha=solver_urelax, maxit=solver_maxit를 인수에서 받음(109–111). `if     (par%solver == SOLVER_SIPP) then` (114)이면 work(5,1:nx+1,1:ny+1)·residual(1:nx+1,1:ny+1) 할당 및 0 초기화(115–116); 병렬 `elseif (par%solver == SOLVER_TRIDIAGG) then` (117)은 같은 work만 할당·0(118). 조건 종료 뒤 initialized=true(121), 루틴 끝·빈 줄·다음 머리말. |
| 130–144 | `solver_free` (130): `if (allocated(residual)) deallocate(residual)` (133), `if (allocated(work))     deallocate(work)` (134). 루틴 끝·빈 줄·다음 구분 머리말. |
| 145–185 | `solver_solvemat` 선언·이력/목적·의존성·인수(145–176): amat(5,nx+1,ny+1), rhs 및 inout x(nx+1,ny+1), par. it 지역변수·구분 머리말(180–184). |
| 186–202 | `if (.not. initialized) call solver_init(nx,ny,par)` (186). `if     (par%solver == SOLVER_SIPP) then` (188) 안에서 `itcal = itcal+1` (190), residual=0(191), `solver_sip` 호출(193). `ittot  = ittot+it` (195), `itmin  = min(it,itmin)` (196), `itmax  = max(it,itmax)` (197), `itmea  = ittot/itcal` (198). 같은 SIP 분기 안의 `if (it>=par%solver_maxit) then` (199)이면 `itnconv = itnconv+1` (200). |
| 203–219 | 188 if의 병렬 `elseif (par%solver == SOLVER_TRIDIAGG) then` 분기(203)에서 시작. 그 안 `USEMPI`는 rhs의 `xmpi_shift_zs` (206), it=1:3에서 amat(it,:,:)의 `xmpi_shift_zs` (207–209). 이 분기에서 `solver_tridiag(amat,rhs,x,work,nx,ny)` (211), 이후 `USEMPI`는 x의 `xmpi_shift_zs` (213). 분기·루틴 종료(216–218). |
| 220–272 | `solver_tridiag` 선언(222), Thomas 알고리즘·1-DH 적용·rhs/matrix 보존 주석(236–244). nx,ny 및 선택 논리 `fixshallow`, 입력 amat/rhs·inout x·1차원 cmat(252–259), i/jindex/fac/lfixshallow 선언(264–267), 구현 머리말. |
| 273–290 | `if (ny>0) then` (273)이면 jindex=2(274), else=1(276). 별도 `if (present(fixshallow)) then` (279)이면 인수 사용(280), else `lfixshallow = .false.` (282). `fac    = amat(1,1,jindex)` (285), `if (abs(fac)<tiny(0.d0) .and. lfixshallow) then` (286)이면 `fac = sign(tiny(0.d0),fac)` (287). 조건 밖 `x(1,jindex) = rhs(1,jindex)/fac` (289). |
| 291–308 | 전진소거 i=2:nx+1(292): `cmat(i)  = amat(3,i-1,jindex)/fac` (293), `fac      = amat(1,i,jindex)-amat(2,i,jindex)*cmat(i)` (294). `if (abs(fac)<tiny(0.d0) .and. lfixshallow) then` (295)이면 `fac = sign(tiny(0.d0),fac)` (296), 그 조건 밖·루프 안 `x(i,jindex) = (rhs(i,jindex)-amat(2,i,jindex)*x(i-1,jindex))/fac` (298). 전진 루프 종료 후 역대입 i=nx:1:-1(302)의 `x(i,jindex) = x(i,jindex)-cmat(i+1)*x(i+1,jindex)` (303). 루틴 끝·다음 머리말. |
| 309–364 | `solver_sip` 선언·Marcel Zijlema 이력·Stone SIP로 단층 Poisson을 푼다는 주석(309–323). xmpi 의존, 출력 it·nx/ny·amat/rhs/x/cmat/res 선언(328–340). `logical             :: iconv = .false.` (344), 지역 변수(345–354), `real(kind=rKind),parameter :: small=1.e-15_rKind` (360), `USEMPI`에서 `logical, parameter         :: dompi = .true.` (362). |
| 365–403 | 입출력·호출·오류 메시지 없음 주석 및 SIP 설명. Stone(1968) 서지(388–391), 원 행렬과 동일 sparsity의 incomplete LU·alpha 범위 0≤alpha≤1, 약 0.92 권장 및 0.95 초과 관련 주석·alpha=0은 ILU(393–397), 반복 전진/역대입 설명(399–400). 이는 코드 주석의 설명이다. |
| 404–424 | 기본 인덱스 imin=2, imax=nx, jmin=2, jmax=ny(404–407). `USEMPI`·`if (dompi) then` (409) 안에서 imin/jmin=3(410–411), `imax = nx-1` (412), `jmax = ny-1` (413). 그 안에서 `if (xmpi_istop)   imin = 2` (415), `if (xmpi_isbot)   imax = nx` (416), `if (xmpi_isleft)  jmin = 2` (417), `if (xmpi_isright) jmax = ny` (418). 전처리/조건 밖 it=0·iconv=false(422–423). |
| 425–446 | L/U 구성·bnorm=0(425–427), jmin:jmax·imin:imax 루프(428–429). `p1          = alpha*cmat(5,i-1,j)` (430), `p2          = alpha*cmat(3,i,j-1)` (431), `cmat(2,i,j) = amat(2,i,j)/(1.+p1)` (432), `cmat(4,i,j) = amat(4,i,j)/(1.+p2)` (433), `p1 =  p1*cmat(2,i,j)` (434), `p2 =  p2*cmat(4,i,j)` (435). `p3 =  amat(1,i,j) + p1 + p2        &` / `- cmat(2,i,j)*cmat(3,i-1,j)    &` / `- cmat(4,i,j)*cmat(5,i,j-1)    &` / `+ small` (436–439), `cmat(1,i,j) = 1./p3` (440), `cmat(3,i,j) = (amat(3,i,j)-p2)*cmat(1,i,j)` (441), `cmat(5,i,j) = (amat(5,i,j)-p1)*cmat(1,i,j)` (442), `bnorm = bnorm + rhs(i,j)*rhs(i,j)` (443). |
| 447–466 | `USEMPI`·`if (dompi) then` (449)이면 `xmpi_allreduce(bnorm,mpi_sum)` (450). 조건 밖 `bnorm = sqrt(bnorm)` (454), `epslin = reps*bnorm` (456), `ueps   = 1000.*tiny(0.)*bnorm` (457), `if ( epslin < ueps .and. bnorm > 0. ) then` (458)이면 epslin=ueps(459). 이 조건 밖 iconv=false(465). |
| 467–485 | `do while ( .not. iconv .and. it < maxit )` (467) 시작, `it    = it + 1` (469), rnorm=0(470). jmin:jmax·imin:imax 루프(472–473)의 `res(i,j)  = rhs(i,j)-amat(1,i,j)*x(i,j) &` / `-amat(2,i,j)*x(i-1,j)          &` / `-amat(3,i,j)*x(i+1,j)          &` / `-amat(4,i,j)*x(i,j-1)          &` / `-amat(5,i,j)*x(i,j+1)` (474–478). `rnorm     = rnorm + res(i,j)*res(i,j)` (480), 전진대입 `res(i,j)  = (res(i,j) - cmat(2,i,j)*res(i-1,j)   &` / `- cmat(4,i,j)*res(i,j-1))* &` / `cmat(1,i,j)` (481–483). 셀 루프 끝(484–485). |
| 486–500 | 467 반복 안·전진 셀 루프 밖. `USEMPI`·`if (dompi) then` (488)이면 `xmpi_allreduce(rnorm,mpi_sum)` (489). 조건 밖 `rnorm=sqrt(rnorm)` (493). 역대입 j=ny:2:-1·i=nx:2:-1(495–496): `res(i,j) = res(i,j) - cmat(3,i,j)*res(i+1,j) - cmat(5,i,j)*res(i,j+1)` (497), `x(i,j)   = x(i,j) + res(i,j)` (498). |
| 501–514 | 467 반복 안·역대입 셀 루프 밖. `USEMPI`·`if (dompi) then` (503)에서 `xmpi_shift_zs(x)` (504). 조건 밖 `iconv = rnorm .lt. epslin` (508). 510에서 while 끝, 루틴·모듈 종료(512–514). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30·121·133–136·186: solver_free는 배열을 해제하지만 initialized를 false로 되돌리지 않는다. 자동 초기화 조건은 `.not. initialized`이다.
- 33·196: itmin은 0으로 초기화되고 이후 `min(it,itmin)`으로 갱신된다. 첫 호출을 따로 처리하는 코드는 없다.
- 114–121: 두 solver 선택 외 값에는 자원 할당 분기가 없지만 initialized=true는 선택 조건 밖에서 실행된다.
- 115·118·211·259: work는 3차원으로 할당되지만 solver_tridiag 호출에서 cmat 인수로 전달되며, 그 dummy 선언은 nx+1 길이 1차원이다. 이 파일에 배열 일부를 선택하는 실제 인수 표현은 없다.
- 279–298·211: 작은 fac 보정은 선택 인수 fixshallow가 참일 때만 한다. solver_solvemat의 tridiag 호출은 그 선택 인수를 전달하지 않는다.
- 428–429·472–473·495–496: 인수분해/전진 루프는 MPI에서 조정한 imin/imax/jmin/jmax를 사용하지만 역대입은 nx:2·ny:2를 그대로 사용한다.
- 456–460·508: 수렴 판정은 엄격한 `<` 비교다. bnorm=0이면 epslin과 ueps가 둘 다 0이며, `bnorm > 0.` 보정 조건은 참이 되지 않는다.

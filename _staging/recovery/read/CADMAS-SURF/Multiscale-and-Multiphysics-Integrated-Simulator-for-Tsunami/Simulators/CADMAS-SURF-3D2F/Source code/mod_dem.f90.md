---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/mod_dem.f90
lines: 39
sha256: f9d53388c32bb6516653f5c195446ecdcd8918afdabbb44a03bf4ed205ca7673
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mod_dem.f90 — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | HiDEM 결합(coupling) 모듈의 IMPLICIT NONE·결합 여부·프로세스/대표 순위(rank)·시간 간격·체적 공극률(porosity) 하한·전체 영역·분할 수 변수를 선언한다. 주석의 ihidem=0/비영 의미는 초기값 대입이 아니다. 원문: `module mod_dem` (1); `  implicit none` (3); `  integer :: ihidem     ! 構造物破壊解析プログラムHiDEMとの連成` (5) (구조물 파괴 해석 프로그램 HiDEM과 결합); `                        !      ==0:連成しない` (6) (0: 결합하지 않음); `                        !      /=0:連成する` (7) (비영: 결합함); `  integer :: nsize_dem  ! dem担当PE数` (9) (DEM 담당 처리 요소(processing element, PE) 수); `  integer :: nprwld     ! comm_2fc_demのプロセス数` (11) (comm_2fc_dem 프로세스 수); `  integer :: myrwld     ! comm_2fc_demでのランク` (12) (comm_2fc_dem에서 순위); `  integer :: ihidm      ! HiDEM の中での0番PEの comm_2fc_dem でのランク` (14) (HiDEM의 0번 PE가 comm_2fc_dem에서 가지는 순위); `                        ! HiDEM と代表通信を行うときの HiDEM側のランク` (15) (HiDEM과 대표 통신 시 HiDEM 쪽 순위); `  integer :: icadm      ! HiDEMと代表通信を行うCADMASのランク(comm_2fc_dem)` (16) (HiDEM과 대표 통신하는 CADMAS의 comm_2fc_dem 순위); `  integer :: icadm2     ! HiDEMと代表通信を行うCADMASのランク(COMCAD内)` (17) (HiDEM과 대표 통신하는 CADMAS의 COMCAD 내부 순위); `  real(8) :: dtcadm     ! cadmasの時間刻み幅` (19) (CADMAS 시간 간격(time step)); `  real(8) :: glcadm     ! cadmasの体積多孔率の下限値` (20) (CADMAS 체적 공극률(porosity) 하한); `  real(8) :: xhidem(6)  ! DEM全体の解析範囲` (22) (DEM 전체 해석 범위); `  integer :: jcadm(6)   ! HiDEM解析領域のCADMASでの位置（インデックス）` (23) (HiDEM 해석 영역의 CADMAS 인덱스 위치); `  integer :: ncadm(3)   ! HiDEM解析領域のCADMASでの分割数` (24) (HiDEM 해석 영역의 CADMAS 분할 수) |
| 26–39 | 시작 시 1행 mod_dem 모듈 안이다. 결합 순위 대응과 DEM별 하위 격자(subgrid) 범위의 동적 배열(allocatable array)을 선언하고 모듈을 끝낸다. 주석은 양수와 음수에 PE 번호+1을 부호화한다고 설명한다. 할당·초기화·통신 실행문은 없다. 원문: `  integer,allocatable :: nrank_2fc_dem(:)  ! comm_2fc_dem のsizeで定義` (27) (comm_2fc_dem 크기로 정의); `                                       ! >0 dem担当PEでDEMの中での+(PE番号+1)` (28) (양수: DEM 담당 PE이며 DEM 안에서 +(PE번호+1)); `                                       ! <0 2fc担当PEで2FCの中での-(PE番号+1)` (29) (음수: 2FC 담당 PE이며 2FC 안에서 -(PE번호+1)); `  integer,allocatable :: nrank_dem(:)      ! (0:nsize_dem-1) --> (0:nprwld-1)` (30); `  real(8),allocatable :: xhidem_sub(:,:)   ! (6,0:nsize_dem-1)` (32); `                          ! DEMの各PEが担当するsubgridを包括する範囲の座標値` (33) (DEM의 각 PE가 담당하는 하위 격자(subgrid)를 포괄하는 범위 좌표); `  integer,allocatable :: jcadm_sub(:,:)    ! (6,0:nsize_dem-1)` (34); `                          ! xhidem_sub の範囲のindex(local)` (35) (xhidem_sub 범위의 지역 인덱스); `  integer,allocatable :: ncadm_sub(:,:)    ! (3,0:nsize_dem-1)` (36); `                          ! xhidem_sub の範囲の分割数` (37) (xhidem_sub 범위 분할 수); `end module mod_dem` (39) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

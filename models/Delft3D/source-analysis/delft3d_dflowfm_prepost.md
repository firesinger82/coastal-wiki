---
title: "Delft3D D-Flow FM 전·후처리 — network/flow geometry 구축 (flow_geominit·net node coding·partition)"
model: Delft3D
component: dflowfm/prepost (network·geometry·flowgeom admin)
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/dflowfm/.../dflowfm_kernel/prepost/). flow_geominit.f90 의 두 phase 구조·findcells/find1dcells 호출·flow link admin(ln/kcu/ln2lne·lncn)·node link admin(nd%ln) / makenetnodescoding.f90 의 NB 코딩 / partition_from_commandline.f90·partition_write_domains.f90 의 METIS·idomain·도메인 파일 기록 / makecell.f90·find1dcells.f90·setbobs.f90·update_geom.f90 를 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_overview.md
  - models/Delft3D/source-analysis/delft3d_dimr_coupling.md
  - models/Delft3D/README.md
---

# Delft3D D-Flow FM 전·후처리 — network/flow geometry 구축

> 비구조(unstructured) 망(net)으로부터 흐름 기하(flow geometry: cell·link·node admin)를 만드는 prepost 서브시스템. 경로: `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/prepost/` (344 파일). 중심 루틴은 `flow_geominit` (1603 라인). 계산 커널은 [[delft3d_dflowfm_kernel_scheme]], MDU 입력은 [[delft3d_dflowfm_mdu_input]], 도메인 분할 결합은 [[delft3d_dimr_coupling]] 참조.

## 0. 두 자료구조 레이어: net (net) vs flow geometry

D-Flow FM 은 **두 개의 분리된 격자 admin** 을 유지한다.

| 레이어 | 핵심 배열 | 의미 |
|---|---|---|
| **net** (`m_netw`/`network_data`) | `xk,yk,zk` (net node), `kn(3,L)` (net link: 노드1·노드2·종류), `lne(2,L)`·`lnn(L)` (link 이웃 cell), `netcell(n)%nod/%lin` (net cell) | 사용자가 준 위상(topology). net node = corner, net link = edge |
| **flow geometry** (`m_flowgeom`) | `xz,yz` (flow node=cell center), `ln(2,L)` (flow link: 셀1·셀2), `kcu(L)` (link 종류), `lncn(2,L)` (link 양끝 corner), `nd(k)%ln` (node→link) | 실제 FV 이산화 단위. flow node = cell, flow link = face |

핵심 카운터: `numk`(net node 수), `numl`/`numl1d`(net link/1D), `nump`(2D cell), `nump1d2d`(1D+2D cell), `ndx2d`/`ndxi`/`ndx`(flow node: 2D / 내부 / +경계), `lnx1d`/`lnxi`/`lnx`(flow link: 1D / 내부 / +경계). 대응은 `flow_geominit.f90:308-310` — `NDX2D = NUMP`, `NDX = NUMP1d2d`, `LNX1D = NUML1D`.

## 1. flow_geominit — 중심 조립 루틴

`flow_geominit.f90:70` `subroutine flow_geominit(iphase)`. 주석: `! initialise flow geometry`. 인자 `iphase` = "phase in geominit, 0 (all), 1 (first) or 2 (second)" (`:130`). 두 단계로 나뉜다 (MPI partition init 때문):

- **phase 1** (`iphase==0|1`): net→cell 탐색, flow link/node admin 구축, 1차 metric. 끝은 `:896` `if (iphase == 1) then ... return`.
- **phase 2** (`iphase==2` 진입 시 `:202-204` `goto 9002`): label `9002 continue` (`:789`) 부터. 최종 metric(dx, normal, corner weight 등) 완성.

### 1.1 cell 탐색 (findcells / preparecells)

타이머 `'Findcells/preparecells'` (`:227`). 분기 (`:238-252`):
- `md_findcells==0` 또는 MPI(idomain·iglobal 읽기) 이면 `call preparecells(md_netfile, jaidomain, jaiglobal_s, ierr)` (`:242`) — net 파일에서 cell·subdomain 번호 직접 읽어 findcells 회피.
- 그 외/실패 시 `call findcells(0)` (`:250`, 주석 `! shortest walks in network (0 means: look for all shapes, tris, quads, pentas, hexas)`) + `call find1dcells()` (`:251`).

findcells/setnodadm 본체는 prepost 가 아니라 `dflowfm_utils/setnodadm.f90` 에 있음(⚠ 본 노트 범위 밖, source-needed for body). prepost 측은 호출자.

### 1.2 net node activation 코드 kc

`:221-225` 모든 net node `kc(k)/=0 → kc(k)=1` ("all active grid nodes are now kc = 1 : only to cure old net files"). 이후 2D cell corner 는 `kc=2`, 1D node 는 `kc=1` 로 재구분 (`:326-331` `kc(k) = 2 ! all corners of cells are now 2, 1D nodes are still 1`).

### 1.3 품질 필터 — orthogonality·too-short link

- `call cosphiunetcheck(1)` (`:297`, "Check for bad orthogonality on netlinks"). `nlinkbadortho>0` 면 `checknetwork()` 후 `lnx=0; ndx=0; return` (`:298-303`) — 망 자체를 거부.
- too-short flow link 검사 (2D 만, `:474-481`): 임계 `dxlim = 0.9 * removesmalllinkstrsh * 0.5 * (sqrt(ba(n1)) + sqrt(ba(n2)))`, 셀 중심 거리 `dxlink = dbdistance(xz(n1),yz(n1),xz(n2),yz(n2),...)` 가 임계 미만이면 bad link 로 폐기 (`lne(:,L)=0; LNN(L)=0`, `:494-496`). 폐기 수 `nlinktoosmall` 누적·경고 (`:502-518`).

### 1.4 cell 중심·면적

2D cell 루프 (`:392-405`): `call getcellsurface(n, ba(n), xzw(n), yzw(n))` — 면적 `ba` 와 질량중심 `xzw,yzw`. circumcenter `xz,yz` 는 이미 findcells 에서 산출됨 (`:400` 주석). 전체 면적 `sarea` 누적 후 풍속 보정 `fwind = (5.0e6/max(sarea,1.0e4))**0.05` (`:408`, excess temperature model 용).

1D cell 중심 (`:410-462`): 1D net link(`KN(3,L)==1` 또는 3..7) 에 대해 끝 cell 이 음수(`nc<0`)면 net node 좌표를 flow node 좌표로 복사하고 `nd(n)%nod(1)=k` 에 원 net node 저장.

## 2. flow link admin — kcu / ln / ln2lne / lne2ln (핵심)

flow link 갯수 카운트(`:468-501`): `lne(1,L)`·`lne(2,L)` 둘 다 0 아니고 `KN(3,L)/=0` 이면 cell 연결 link → `lnxi++`. 1D 종류면 `lnx1D++`.

채우기 루프 (`:609-692`) — net link L → flow link Lf 매핑:
- `ln(1,Lf)=n1a`, `ln(2,Lf)=n2a` (link 양쪽 flow node) (`:617-618`).
- `ln2lne(Lf)=L`, `lne2ln(L)=Lf` (flow↔net link 상호 색인) (`:619-620`).
- **kcu (link 종류)** = net link 종류 `kn(3,L)` 에서 결정:
  - `kn(3,L)==1|6` → `kcu=1` (1D link) (`:621-622`)
  - `kn(3,L)==4` → 끝 노드 차수(`nmk==1`)이고 1D↔2D 횡단이면 `kcu=4` (1D2D longitudinal), 이때 `WHICH2DNETLINKWASCROSSED` 로 교차된 2D net link 를 찾아 `ln2lne(Lf)` 를 그쪽으로 재지정 (`:623-650`). 교차 못 찾으면 경고·`noncrossinglink=.true.` (`:646`).
  - `kn(3,L)==3|7` → 1D node↔2D cell 연결이어야 `kcu=kn(3,L)` (1D2D internal), 2D 측 `kcs=21` 설정 (`:651-668`).
  - `kn(3,L)==5` → 2D↔2D 도 허용하는 1D2D internal (`:669-683`).
  - `kn(3,L)==2` → `kcu=2` (순수 2D link) (`:684-685`).
- net link 한쪽 cell 만 있는 경계 link 는 `lne2ln(L) = -n2` 또는 `-n1` (음수 부호로 부착 노드 역참조) (`:687-691`).

경계 link 추가: `call addexternalboundarypoints()` (`:698`, open boundary). `ln0 = ln` 백업 (`:700`).

### 2.1 link corner 참조 lncn + 양(positive) 방향 보장

`:703-753` 모든 link 에 대해 `lncn(1,L),lncn(2,L)` (link 양끝 corner net node) 설정. 2D link 는 셀중심 법선 `rnl,rtl` 와 edge 법선 `rn,rt` 의 외적이 음수면 두 corner 를 swap 하여 **local axis 양의 방향** 보장 (`:722-731`, `if (rnl*rt - rtl*rn < 0) ... swap; numswap++`). 주석(`:705-709`): `o---4---o  1,2: flow nodes, 3,4: net nodes / L: 1--2  Ln=ln2lne(L): 3--4 / lncn(:,L) = 3--4, or 4--3 if ||3--4 X 1--2|| < 0, i.e., flux is 'to the right' through net link 3--4.`

### 2.2 node→link admin nd%ln (부호 규약)

2-pass (`:757-783`): 1pass 각 node `nd(k)%lnx++` 카운트, 할당 후 2pass 채우기. **부호 규약**: link 시작 node 에는 `-L` ("outflowing, negative indexnr", `:779`), 끝 node 에는 `+L` ("inflowing, positive indexnr", `:782`). 마지막 `call sort_flowlinks_ccw()` (`:786`) — node 주위 link 반시계 정렬.

## 3. flow link metric (phase 2, label 9002~)

`:812-` 모든 link 에 대해:
- velocity point `xu,yu` = 1D 면 두 flow node 중점, 2D 면 두 corner 중점 (`:818-827`, `half(...)`).
- link 길이 `dx(L) = dbdistance(xz(k1),yz(k1),xz(k2),yz(k2),...)` (`:829`). 1D 는 net link 파일 길이 `dxe(LL)` 가 있으면 override (`:831-836`, "typically 1D with user-defined branch lengths").
- `kcu==4` (1D2D lateral) link 은 2D net link 에 수직(`normalout`) (`:838-839`).

corner 관련 stuff `cn(numk)`, `ucnx/ucny`, `ban(net node area)` 재할당·초기화 (`:793-810`).

## 4. net node 경계 코딩 — makenetnodescoding

`makenetnodescoding.f90:38` `MAKENETNODESCODING()`. 헤더(`:35-37`): `Make a coding of all net nodes for later use in net orthogonalisation, net coupling and 'poltoland' functionality. network_data::NB values: 1=INTERN, 2=RAND, 3=HOEK, 0/-1=DOET NIET MEE OF 1D` (1=내부, 2=경계, 3=코너, 0/-1=불참여 또는 1D).

알고리즘:
- 1pass (`:57-77`): net link 별, 2D/미정 link(`kn(3,L)==2|0`)이고 이웃 cell 0개(`LNN==0`)면 양끝 `NB=-1`(불참여), 1개(`LNN==1`, 경계 edge)면 `NB++`. 1D link 양끝은 `NB=-1` (`:74`).
- 2pass (`:80-118`): `kc(k)==1` 노드에서 `NB∈{1,2}` 일 때 차수 `NMK==2` 면 `NB=3` (볼록 코너 'bolle hoek', `:83-85`). 차수>2 면 경계 edge 의 두 이웃 노드와의 각도 `dcosphi > -CORNERCOS` (cos(105°)=-.25) 이면 `NB=3` (오목 코너 'holle hoek'), 아니면 `NB=2`(경계점) (`:99-108`).
- 후처리(`:119-124`): `nmk(k)<2` 이면 `NB=-1` (hanging node).

## 5. domain partition (MPI 전처리)

### 5.1 명령줄 partition — partition_from_commandline

`partition_from_commandline.f90:49`. 헤더 주석 `>  perform partitioning from command line` (`:33`). 인자에 `md_Ndomains` (METIS 도메인 수, 0=polygon), `md_pmethod` (`partition method: K-way (=1, default), Recursive Bisection(=2), Mesh-dual(=3)`, `:61`), `md_jacontiguous`, `md_partseed` (METIS SEED 재현성) 등.

흐름: dirty 면 `preparecells`/실패 시 `findcells(0)+find1dcells()` (`:79-85`) → `delete_dry_points_and_areas` (`:88`) → `cosphiunetcheck(1)` (`:94`). 그 다음:
- `md_Ndomains>0`: `call partition_METIS_to_idomain(idomain, md_Ndomains, md_jacontiguous, md_pmethod, md_partseed)` (`:97`) — METIS 가 cell 별 도메인 색 `idomain` 채움. polygon 출력 요청 시 `generate_partition_pol_from_idomain` (`:101`).
- polygon(`NPL>1`) 입력 시 `generate_partitioning_from_pol()` (`:105`).
- `ndomains>1` 이면 `partition_write_domains(...)` (`:110`).

### 5.2 도메인 파일 기록 — partition_write_domains

`partition_write_domains.f90:47`. 헤더(`:33-34`): `write the network domains to file / it is assumed that the domain coloring "idomain" is available`.

- 먼저 전체 망 백업 `savenet()` (`:79`) + cell admin 백업 `savecells()` (`:81`, 주석 "save netcell, lne, lnn, idomain, xz, yz, xzw, yzw, ba").
- net 파일명에서 `_net` 위치로 basename 추출, 형식 불일치 시 에러 (`:86-90`, expected `*_net.nc`).
- 도메인 루프 (`:119-137`): 도메인번호 4자리 `_NNNN_net.nc` 파일명 생성 → `partition_make_domain(idmn, numlay_cellbased, numlay_nodebased, jacells, ierror)` (`:125`, 다른 부분 삭제 + ghost layer 추가) → `unc_write_net(filename, janetcell=1, janetbnd=1, jaidomain=jacells, jaiglobal_s=jacells, ...)` (`:131`) → `restore()`+`restorecells()` (`:135-136`) 로 원복.
- ghost level 파라미터는 `partition_setghost_params(icgsolver)` (`:116`) — solver 종류에 따라.

(런타임 MPI ghost 통신·결합은 [[delft3d_dimr_coupling]] 및 m_partitioninfo 참조. update_geom 은 §7.)

## 6. cell·1D cell 생성 admin

### 6.1 makecell

`makecell.f90:46` `subroutine makecell(N, nodlist, linlist, ic, ierror)`. 헤더(`:33-34`): `administer a cell / note: cell circumcenters are not updated (would require up-to-date lnn, lne)`. `increasenetcells(NUMP+1, growfac=1.2)` 로 배열 확장 후 `netcell(ic)%N/%nod/%lin` 채우고 `xz/yz/xzw/yzw/ba` 를 growfac 로 재할당(keepExisting), 마지막 `nump=nump+1` (`:68-100`).

### 6.2 find1dcells

`find1dcells.f90:51`. 헤더(`:48-50`): `find one-dimensional net cells / it is assumed that kc has been allocated / it is assumed that findcells has already been called (for 2d cells)`. `nump1d2d = nump` 에서 시작(`:102`, 2D cell 다음부터). `construct_lne_array` 를 두 번 호출 — preserve_branch_order true/false (`:103-105`, "second one in case branch order cannot be preserved"). 각 1D net node(`kc(k)<0`)에 cell 번호를 부여하고 `netcell(cell)%nod` 채움 (`:120-142`), cell 중심을 net node 좌표로 설정 (`:144-152`). 1D cell 생성 시 `netstat = NETSTAT_CELLS_DIRTY` (`:156`).

## 7. bed level on links — setbobs

`setbobs.f90:39` `subroutine setbobs() ! and set blu, weigthed depth at u point`. flow node bed level `bl(k)` 와 link bed-of-bed `bob(2,L)` 를 `ibedlevtyp`/`ibedlevmode` 에 따라 산출.

- `ibedlevmode==BLMODE_D3D` (`:61-72`): "DPSOPT=MAX equivalent: deepest zk/corner point" — cell 의 corner zk 최소값(가장 깊은). (Delft3D-FLOW 호환 모드. [[delft3d_drying_flooding]] DPSOPT 와 대응.)
- `BLMODE_DFM` (`:73-100`): `ibedlevtyp==1`(WATERLEVEL) 은 ext 파일로 이미 공급, 결측만 `zkuni`; `2..MAX` 는 `bl=1e30` 초기화 후 net node 기반; `==6` 은 corner zk 평균.
- link 루프 (`:103-`): 각 net link 의 flow link `Lf=lne2ln(L)`, `get_bedlevel_at_link(n1,n2,k1,k2,blu,ibot)` 로 link bed level. `jaconveyance2D>=1` 면 `bob(1/2,Lf)=zk(k1/k2)` (corner zk 직접, `:142-152`). 구조물(`iadv∈(20,30)`) link 은 skip (`:128-130`).

bob 의 흐름 계산 사용은 [[delft3d_dflowfm_kernel_scheme]], drying/flooding 임계는 [[delft3d_drying_flooding]] 참조.

## 8. ghost 영역 geometry 보정 — update_geom

`update_geom.f90:44` `subroutine update_geom(iphase)`. 헤더 주석(`:33`): `update geometry data that may have been incorrectly computed in the ghost area`. phase 1 은 `xz,yz` (cell center) ghost 동기화, phase 2 는 `bl` (bed level) 동기화 — `update_ghosts(ITYPE_SALL,...)` + `update_ghostboundvals` 호출 (`:51-61`). MPI 분할 시 ghost cell 의 기하량을 인접 도메인 값으로 덮어쓴다.

## 9. prepost 디렉토리 기타 루틴 (역할 요약, source-needed for bodies)

344 파일 중 본문 미read 항목은 역할만 (파일명=루틴):
- net 위상 편집: `addnetlink.f90` (`addnetlink(x1,y1,x2,y2,L)`, `:44`), `dellink`/`delnode`/`deletecell`/`killcell`, `connect_hanging_nodes`, `m_mergenodes`, `fliplinks`.
- cutcell/마스킹: `cutcells.f90`, `cutcell_list.f90`, `mark_cells_crossed_by_poly.f90`, `m_remove_masked_netcells.f90`, `m_cellmask_from_polygon_set.f90`, `delete_drypoints_from_netgeom.f90`.
- link 가중치/방향: `setlinktocenterweights.f90` (헤더 "set center related linkxy weights", `:41-42`), `setlinktocornerweights.f90`, `setcentertolinkorientations.f90`, `setcornertolinkorientations.f90`, `setwallorientations.f90`, `orthonet_compute_orientation.f90`.
- 구조물/지형 on geom: `fixedweirs_on_flowgeom.f90`, `thindams_on_netgeom.f90`, `crosssections_on_flowgeom.f90`, `crspath_on_flowgeom.f90`, `m_obs_on_flowgeom.f90`, `runupgauges_on_flowgeom.f90`, `find_netcells_for_structures.f90`, `setpillars.f90`.
- bed level 변형: `setbobs_fixedweirs.f90`, `setbobsongullies.f90`, `setbobsonroofs.f90`, `setbedlevelfromextfile.f90`, `setbedlevelfromnetfile.f90`.
- query: `inquire_flowgeom.f90`, `m_find_flowlink.f90`, `m_find_flownode.f90`, `in_flowcell.f90`, `isflowlink.f90`, `isflownode1d2d.f90`.

위 본문은 read 하지 않았으므로 알고리즘 단언 없음(파일명·헤더 기반 역할만). 상세 분석 필요 시 추가 read 요망.

---

## 요약 — prepost 의 책임 경계

1. **net → flow geometry 변환**의 단일 진입점은 `flow_geominit` (2-phase). cell 탐색은 findcells/find1dcells(prepost 는 호출자, 본체는 utils), flow link/node admin(ln·kcu·ln2lne·lne2ln·lncn·nd%ln)은 prepost 내부.
2. **자료구조 이중성**: net(corner·edge·netcell) vs flow geometry(cell·face·node). kcu(1/2/3/4/5/6/7)로 1D·2D·1D2D link 구분.
3. **MPI partition**: METIS(`partition_METIS_to_idomain`, K-way/RB/mesh-dual)로 `idomain` 색칠 → 도메인별 net 파일 기록(`partition_write_domains`), ghost 보정(`update_geom`).
4. 계산 커널(흐름 이산화)은 별도 — [[delft3d_dflowfm_kernel_scheme]]. 본 노트는 그 입력이 되는 기하 admin 에 한정.

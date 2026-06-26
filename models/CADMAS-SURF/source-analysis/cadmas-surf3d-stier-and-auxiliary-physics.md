---
title: "CADMAS-SURF/3D S티어 + 보조물리 카탈로그 — 입출력·MPI 래퍼·BC + 스칼라/온도수송·Okada 단층 쓰나미소스·공기압·파이론 구현·진단 (vf_i*·vf_o*·vf_zxmp*·vf_s1cal·mod_fault·vf_fpvcpp·vf_wstk0)"
model: CADMAS-SURF
component: src (SURF/3D S-tier support + auxiliary physics)
canonical_source: self
verification_method: "CADMAS-SURF/3D 소스 전수 카탈로그 (raw/.../CADMAS-SURF-3D/Source code/, 240 파일 중 C티어 코어 6노트 외 잔여). 입력 vf_ii*.f(카드별 파서)·출력 vf_o*/db_*·MPI 래퍼 vf_zxmp_*/zxmg_*(1:1 MPI)·vf_p0/p1/p3(타이밍+halo)·util vf_z*·BC vf_bs*/bw* 헤더 CDT 인용. 보조물리 firming read: mod_fault.f:7-24(SET_PARAM_FAULT·EN2LB·DISPLACE 港空研 Okada·측지계 Bessel/GRS80/WGS84)·vf_faultt.f:1-5(断層→水位변동)·vf_fpvcpp.f:1-5(공기압)·vf_s1cal/t1cal/sconvd/sdiff/seuler(스칼라/온도 DONOR 수송)·vf_wstk0/wcnd0/wsfmb2(Stokes5/cnoidal3/stream-func 구현, Isobe 1998-2000)·진단 vf_cvort/cdiv00/cwlvl/comak0. file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-24
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md
  - models/CADMAS-SURF/README.md
---

# CADMAS-SURF/3D S티어 + 보조물리 카탈로그

> SURF/3D 240 파일 중 [C티어 코어 6노트](cadmas-surf3d-architecture-source-map.md) 외 **잔여 전부**. (1) 순수 지원(입출력·MPI·util·BC) + (2) C티어 코어 6노트에 안 들어간 **보조 물리**(스칼라/온도 수송·Okada 단층 쓰나미소스·공기압·파이론 내부구현·진단). 경로 루트: `raw/.../CADMAS-SURF-3D/Source code/`.

## A. 순수 지원 (S티어)

### A-1 입력 파서 (vf_i*, 18) — 텍스트 카드 렉서
마스터 `vf_ii1inp.f`(다단계 read, LEVEL<0 격자수/=1 좌표+장애물/≥2 나머지, `:109-111`). 카드별: `vf_iiboun`(B.C.)·`vf_iicomp`(COMP: SCHM·MTRX ILUBCGSTAB `:34-107`)·`vf_iiequa`(EQUATION)·`vf_iifile`(FILE 출력제어 `:35-249`)·`vf_iigrid`(GRID)·`vf_iimate`(MATE 재료/IC)·`vf_iimdl`(MODEL)·`vf_iiobst`(OBST)·`vf_iiopt`(OPTION)·`vf_iipara`(PARALLEL)·`vf_iiporo`(POROUS CM0/CD0/GGV)·`vf_iitime`(TIME)·`vf_iidbg`(DEBUG). 파일읽기 `vf_im1inp/im2inp`(매트릭스데이터)·`vf_ip1inp`(시간의존 공극)·`vf_ir1inp`(리스타트). 물리 없음.

### A-2 출력 (vf_o*·db_*, 19) — 5 스트림
각 `*ini`(헤더)+`*trn`(스텝): 도화 `vf_og1*`+`vf_ogbc*`(BC인덱스)+`db_ini/trn`(低수준 図化 writer)·리스트 `vf_ol1*`+`vf_ol3d{i,r,nf}`·멀티에이전트 `vf_om1*`·리스타트 `vf_or1*`·시계열 `vf_ot1*`. 직렬화만.

### A-3 MPI 래퍼 (2층, 59) — 순수 통신
- `vf_p0/p1/p3*`(21): CPU타이밍(`VF_A2CPUT`)+halo/buffer 후 zxmp 위임. p3=3D halo 송수신
- `vf_zxmp_*`(20, 主 통신)·`vf_zxmg_*`(18, nesting 통신): 1:1 thin MPI(ISEND/IRECV/WAIT/ALLREDUCE/BCAST/BARRIER/GATHER/SCATTER/SPLIT/INIT/FINAL/ABORT/WTIME). `vf_pcdc2p/pcdp2c`(nesting 子↔親 전송)

### A-4 유틸 (vf_z*·vf_a2*·vf_hsort, ~18)
배열채움 `vf_zset{i,r}{1,2,3}`·문자/파싱 `vf_zgetln/zgetim/zstoi/zstor`·시간 `vf_ztimec`·힙정렬 `vf_hsort`·런타임 `vf_a2clos`(파일닫기)·`vf_a2cput`(타이머)·`vf_a2dflt`(디폴트값)·`vf_a2err`(에러+abort)·`dummy.f90`(getcwd/chdir 포팅 stub).

### A-5 BC 헬퍼 (vf_bs*·vf_bw*, 16) — [C티어 경계](cadmas-surf3d-wave-generation-and-boundaries.md) 값 적용
표면(bs): `vf_bspp`(기체셀 P=0)·`vf_bsppfl`(기체→유체 전환셀 P)·`vf_bsss`(표면 스칼라)·`vf_bsuwem`(특수 기체셀 속도)·`vf_bsuwn/bsuwn3`(표면↔기체 법선속도)·`vf_bsuwt/bsuwt2`(자유표면 접선). 벽(bw): `vf_bwff/bwffsf`(경계 VOF-F)·`vf_bwke/bwkelg`(경계 난류)·`vf_bwpp`(경계 P)·`vf_bwss`(경계 스칼라).

## B. 보조 물리 (C티어, 6 코어노트 외)

### B-1 스칼라·온도 수송 (advection-diffusion)
메인루프 `T1CAL`(온도, `vf_a1main.f:1077`)·`S1CAL`(농도, `:1086`) 호출. 동일 DONOR+확산+Euler 패턴([SMAC 이류](cadmas-surf3d-smac-velocity-pressure-solver.md)와 동형):
- `vf_t1cal.f:7`(온도 `TT`)·`vf_s1cal.f:7`(농도 `CC`, LEQC종)
- `vf_sconvd.f:6`(DONOR 이류 플럭스)·`vf_sdiff.f:6`(확산 플럭스)·`vf_seuler.f:6`(Euler 적분)
- 난류 closure: `vf_cdd00.f:5`(난류확산 `D=D₀+νt/Sc_t`)·`vf_clm00.f:5`(난류열전도 `λ=λ₀+νt·ρCp/Pr_t`). [k-ε νt](cadmas-surf3d-turbulence-and-porous-resistance.md) 의존

### B-2 ★ Okada 단층 → 쓰나미 초기수위 (지진 소스)
`mod_fault.f`(모듈, `:3 水位変動量 계산`) — **港空研(PARI) 제공 Okada형 지반변동**:
- `SET_PARAM_FAULT`(`:7` 단층파라미터 초기화)·`SET_UTM`(`:8` UTM 원점)·`EN2LB`(`:9` UTM/19좌표→경위도)·`SHIGOSEN`(`:10` 자오선장)·**`DISPLACE`(`:11` 단층파라미터→지반변동, 港空研 루틴)**·`USCAL/UDCAL`(`:12-13` 하위처리)·`ATN`(`:17` 수정 atan2)
- 측지계 `JSYSTEM`: 1=구일본측지(Bessel)·2=세계측지(GRS80)·3=WGS84 (`mod_fault.f:22-24`), 단층 `FPARAM(ISIZ_PARAM=10,NFLT)`
- `vf_faultt.f:1-5`(`断層パラメータから水位変動량을 계산`, `USE MOD_FAULT`)·`vf_faulti.f`(초기화) → VOF 자유수면 초기조건으로 쓰나미 발생원 주입

### B-3 공기압 / 갇힌 공기 (trapped air)
`vf_fpvcip.f:5`(공기압 계산용 인덱스 설정)·`vf_fpvcpp.f:1-5`(`空気圧計算用圧力を計산` — 갇힌 공기/2상 압력 효과). VOF 자유수면 위 폐쇄 공기영역 압력. [VOF NF 머신](cadmas-surf3d-vof-free-surface.md)의 기체셀(`NF=8`) 관련.

### B-4 파이론 내부 구현 (Stokes5·cnoidal3·stream-function B)
[wave-gen 노트](cadmas-surf3d-wave-generation-and-boundaries.md)에서 디스패치만 다룬 실제 파이론 solver — Isobe(도쿄대 1998-2000) 작성, Sakakiyama/CRIEPI 기증(`vf_wcnd0.f:1-4`·`vf_wsfmb2.f:1-20`):
- `vf_wstk0.f:6`(Stokes 5차 `VF_STK0`+분산함수 `VF_HK` :165)
- `vf_wcnd0.f:6`(cnoidal 3차 `VF_CND0`+타원적분 `VF_ELINT` :190)
- `vf_wsfmb2.f:24`(stream-function 법 B `vf_sfmb02C`+최소자승 `vf_lstsq`·`vf_dife`·`vf_psieta`·`vf_caleta`, 745줄). `vf_comak0.f:24-32`(Airy 소진폭 celerity/파장 Newton, 방사 개경계용)

### B-5 진단·VOF 보조
- 진단: `vf_cvort.f:6`(와도 ∂w/∂y-∂v/∂z)·`vf_cdiv00.f:5`(발산 L2노름, 수렴진단)·`vf_cwlvl.f:5`(수위변동, 시계열출력)·`vf_careap.f:7`(공간 min/max/avg/적분)
- VOF 보조(F1CAL 파이프라인): `vf_fmod1.f:5`(표면셀 전역보정)·`vf_fgene.f`(VOF 소스/싱크)·`vf_fseabt.f`(해저변형 VOF 소스). [vof-free-surface](cadmas-surf3d-vof-free-surface.md) §2 호출순서
- 행렬커널(m1bcgs 형제): `vf_mzax/mzip/mzdcmp/mzfrwd/mzbkwd/mzminv`(ILU-BiCGSTAB 전처리·매트벡, [SMAC solver](cadmas-surf3d-smac-velocity-pressure-solver.md) §5)
- 셋업/인덱스: `vf_cgrid`·`vf_cind{b,c,x}`(INDB/INDC/INDX 인덱스)·`vf_cnfdfl`(NF 디폴트)·`vf_cggv/cggxyz/cglxyz`(시간의존 공극)·`vf_csetup/cpara`·`vf_cwzero`. 모듈 `mod_apara`(nesting 병렬확장)

> 결론: SURF/3D 240 전 파일 포섭. 순수 지원(A) + 보조물리(B, 6 코어노트 외). ★ **Okada 단층 쓰나미소스**(`mod_fault`)·**스칼라/온도 수송**·**파이론 내부구현**이 핵심 보조물리.

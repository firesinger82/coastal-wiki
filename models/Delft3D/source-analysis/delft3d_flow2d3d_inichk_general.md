---
title: "Delft3D flow2d3d 초기화·검사·general 유틸 — inchki/inchkr 오케스트레이션 + chk*/ini* 커널 + 공용 함수"
model: Delft3D
component: flow2d3d/flow2d3d_kernel(inichk·general)
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/inichk·general). inchki/inchkr 의 call 시퀀스(grep -n call), chkgeo/chknum 실행부, nm_to_n_and_m/n_and_m_to_nm 변환식, 각 chk*/ini* subroutine 헤더 Function 주석을 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D flow2d3d 초기화·검사·general 유틸

> flow2d3d 구조격자 커널의 시뮬레이션 시작 단계 — 격자/입력 정합성 검사(`chk*`)와 초기조건 채우기(`ini*`)를 두 드라이버 `inchki`(553L)·`inchkr`(1315L)가 순서대로 호출한다. `general/`은 인덱스 변환·에러출력·시간·기하 공용 함수. (경로: src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/{inichk,general}/)

상위 디스패처/시간루프 흐름은 [[delft3d_flow2d3d_dispatcher]] 참조. 건습(drying/flooding) 알고리즘 본체는 [[delft3d_drying_flooding]], σ/z 수직격자는 [[delft3d_sigma_z]], 난류 초기화 본체는 [[delft3d_turbulence]] 참조 — 본 노트는 **초기화 오케스트레이션과 검사 항목** 자체에 집중한다.

---

## 1. 두 드라이버: inchki → inchkr

`inichk/` 디렉토리는 59개 파일로, 대부분 단일 책임 `chk*`(검사) 또는 `ini*`(초기화) 서브루틴이다. 이들을 **순서대로** 호출하는 오케스트레이터가 두 개 있다.

| 드라이버 | 라인수 | Function 주석 | 역할 |
|---|---|---|---|
| `inchki` | 555 | "Initialises and checks various params. and arrays / defines initial arrays" (`inchki.f90:37`) | **격자·기하·물리·수치 검사** + 초기 배열 정의 |
| `inchkr` | 1315 | "...were arrays can be initialized in INCHKI or come from restart data" (`inchkr.f90:36`) | **시변 강제력·초기 상태**(경계/방류/기상/증발/sed/난류/마찰) 초기화 (restart 데이터 가능) |

즉 `inchki`는 **정적 정합성 검사**, `inchkr`는 **시간의존 초기 상태 채우기** 단계로 책임이 갈린다.

---

## 2. inchki 호출 순서 (정합성 검사 + 격자/기하/물리)

`grep -n "^[[:space:]]*call " inchki.f90` 기준 핵심 순서 (`inchki.f90:350~552`):

| # | call (라인) | 하는 일 |
|---|---|---|
| 1 | `inigrd` (`:350`) | 계산격자 enclosure 파일 읽기, 45도 조건 검사, ICOM 채워 active/inactive 식별 (`inigrd.f90:33-37`) |
| 2 | `nuliar(kcv/kcs)` (`:358-359`) | 정수배열 0 초기화 (`nuliar.f90` Function "Initialize integer array with length INTDIM") |
| 3 | `inibnd` (`:367`) | 개방경계 type 채움/검사, NOB 배열 초기화, 경계구간 45도 배수 규칙 검사 (`inibnd.f90` Function) |
| 4 | `chkbnd` (`:374`) | 개방경계가 active point 안/밖인지·non-water-elev 경계가 enclosure vertex에 있는지 검사 + **IROCOL 테이블 채움** (`chkbnd.f90:32-39`) |
| 5 | `chkkc` (`:387`) | 유속점(velocity point) active mask 배열 설정 (`chkkc.f90:34-35`) |
| 6 | `chkgeo` (`:395`) | 수직격자 검사 — thick 합=1 검증, sig 계산 (§3) |
| 7 | `inigeo` (`:407`) | 기하 파라미터 설정, curvilinear면 depth point 좌표 먼저 읽음 (`inigeo.f90:36-39`) |
| 8 | `griddims_admin`·`dfupdgeo` (`:416,:420`) | 격자 차원 admin + 병렬 기하 halo 갱신 |
| 9 | `iniphy` (`:427`) | 물리상수 초기화 |
| 10 | `chkphy` (`:432`) | 모든 물리계수 검사 (`chkphy.f90:34`) |
| 11 | `chktrt` (`:443`) | trachytope(거칠기 분류) 검사 |
| 12 | `chknum` (`:450`) | 수치 파라미터 검사 (§3) |
| 13 | `chksit` (`:456`) | station/cross-section 위치가 active point인지·cross-section 1점뿐인지 검사 (`chksit.f90` Function) |
| 14 | `calpsh` (`:466`) | 부유구조물(floating structure) 위치/압력 + KSPU/V 설정 (`calpsh.f90` Function) |
| 15 | `chkstr` (`:472`) | 구조물(Local Weir/Rigid Sheet/Gate/Barrier) U/V 점 위치 검사 (`chkstr.f90` Function) |
| 16 | `inirgl` (`:478`) | rigid lid 초기화 |
| 17 | `chkic` (`:485`) | 초기조건 r1/rtur1 음수값 검사 (restart 시 rtur1) (`chkic.f90` Function) |
| 18 | `chkiwe`/`iwecof`/`tkecof` (`:499,:509,:515`) | IWE·TKE 난류계수 검사/계수 |
| 19 | `xyder` (`:525`), `rdveg3d` (`:533`), `allocadv2d` (`:539`), `mirror_bnd` (`:546`), `init_out_heatfluxes` (`:552`) | 미분량·식생·2D advection 할당·경계 mirror·열속 출력 초기화 |

**관찰**: 검사 순서가 의존성에 따라 정렬됨 — 격자(inigrd)→경계(inibnd/chkbnd)→mask(chkkc)→수직격자(chkgeo)→기하(inigeo)→물리(chkphy)→수치(chknum)→관측점/구조물(chksit/chkstr). 검사 실패는 공유 `error` 플래그로 누적되어 `goto 9999`로 조기 종료.

---

## 3. 검사 본체 예시 (실행부)

### chkgeo — σ-layer thick 합 = 100 % 검증
`chkgeo.f90:64-108` 실행부:
- 각 층 `thick(k) <= 0`이면 error1 + `prterr(...,'U004')` (`chkgeo.f90:77-81`)
- `thick(k) = thick(k)/100.` 후 누적 `som` (`:83-84`) — 입력은 백분율
- `abs(som - 1.) > 1.E-5`면 error2 + `prterr(...,'U006')` (`chkgeo.f90:90-93`)
- 검사 통과 후 sig 계산: `sig(1) = -0.5*thick(1)`, 이후 `sig(k) = sig(k-1) - 0.5*(thick(k)+thick(k-1))` (`chkgeo.f90:100-104`)

즉 σ-coordinate 중심값을 층두께에서 유도. (σ/z 격자 일반론은 [[delft3d_sigma_z]].)

### chknum — 마찰식·iter·dryflc 검사
`chknum.f90:66-160`:
- 바닥마찰 `roumet` → `rouflo`: `M`→`MANN`, `C`→`CHEZ`, `W`→`WHIT`, `Z`→`Z` (그 외 error `V045`) (`chknum.f90:84-95`)
- `TIMJAN` = (julday − jan1 julday)*24 시간 계산 (`chknum.f90:101-104`)
- `ITER1` 검사: momsol=='flood'면 기본 1, 아니면 2 (`chknum.f90:106-110`); iter1 < 기본값이면 기본값으로 올리고 경고 `V071` (`:111-115`)
- **DRYFLC 하한 강제**: `dryflc <= 0`이면 경고 `V074` 후 `dryflc = 0.02` (`chknum.f90:124-127`). 주석: "if DRYFLC < 0.02 m an inconsistency for drying and flooding versus calibration of 1/H**2 in CUCNP(2) can occure / Therefore will be set on 0.02" (`chknum.f90:120-123`). `dryflc > 1.0`이면 경고 `V073` (`:128-130`).

이 dryflc 하한이 [[delft3d_drying_flooding]] 임계수심과 연결된다.

---

## 4. inchkr 호출 순서 (시변 강제력·초기 상태)

`grep -n call inchkr.f90` 기준 (`inchkr.f90:747~1307`):

| 단계 | call (라인) | 내용 |
|---|---|---|
| mask 복사 | `copykcuv(kcu/kcv)` (`:747-748`) | kcu/kcv 복사본 |
| 방류·드로그 | `chkdis` (`:752`), `chkdro` (`:766`) | 방류점/드로그가 active point·시뮬구간 내인지 검사 (`chkdis.f90`, `chkdro.f90` Function) |
| 경계 강제력 | `inibct/inibcq/inibcc` (`:784,:794,:804`), `inibcparl` (`:810`) | 경계 시계열(BCT)·QH(BCQ)·농도(BCC) 초기화 + 병렬 경계 |
| 기상 | `checkmeteoresult`·`incmeteo` (다수, `:840~892`) | 기상(바람/기압/태양복사/SDU) 초기화 + 결과 검사 |
| 열·증발 | `initem` (`:847`), `inieva` (`:901`) | 온도·증발 강제력 초기화 |
| 구조물 | `filterstructures` (`:909`) | 구조물 필터 |
| 퇴적 | `inised` (`:919`) | 바닥 총퇴적량 초기화 (`inised.f90` Function "Initialisation total sediment at bed in each horizontal point") |
| z-model | `z_inizm`·`z_chkdry` (`:933,:974`) | z-layer 초기화 + z용 건습 검사 ([[delft3d_sigma_z]]) |
| 건습 | `chkdry` (`:963`) | σ-model 유속점 건습 검사 ([[delft3d_drying_flooding]]) |
| 부피 | `inivol` (`:1018`), `updmassbal` (`:1024`) | 셀 부피·질량수지 초기화 |
| 상태 전이 | `f0isf1` (`:1042`) | f0→f1 상태 복사 |
| 밀도/마찰 | `dens` (`:1064`), `trtrou` (`:1085,:1090`), `initau` (`:1103,:1110`), `taubot` (`:1157,:1174`) | 밀도, trachytope 거칠기, 초기 거칠기높이(`initau.f90` "Computation initial roughness heights"), 바닥전단 |
| 점성/난류 | `chkvic` (`:1196`), `detvic` (`:1229`), `c_vort` (`:1241`), `initur`/`z_initur` (`:1261,:1271`) | 수평점성 안정조건 검사(`chkvic.f90` "stability criterion for horizontal viscosity") + 난류 초기화([[delft3d_turbulence]]) |
| morfac | `flw_gettabledata` (`:1307`) | 형태가속계수 테이블 |

**관찰**: inchkr는 시간루프 진입 전 t0 상태를 완전히 구성 — 경계강제력→기상→퇴적→부피→밀도→마찰→난류 순. restart 시 일부는 파일 데이터로 대체(헤더 주석 `inchkr.f90:35-37`).

---

## 5. caldps / caldpu — 수위점·유속점 수심

건습 옵션에 따라 수심 보간 방식이 갈린다.

**caldps** (`caldps.f90:33-48`) — 수위점 수심 DPS + nfltyp 설정:
- `DPSOPT=MEAN` → 4점 평균 `.25*(dpd(nm)+dpd(nmd)+dpd(ndmd)+dpd(ndm))`, nfltyp=1
- `DPSOPT=MAX` → 4점 최대, nfltyp=2
- `DPSOPT=MIN` → `.5*(MIN(dpd(nm),dpd(ndmd)) + MIN(dpd(nmd),dpd(ndm)))`, nfltyp=3

**caldpu** (`caldpu.f90:38-44`) — 유속점 수심 DPU/V: general local weir면 crest 높이를 local depth로 제한, sediment+bedupd면 upwind 사용. (건습 nfltyp의 의미는 [[delft3d_drying_flooding]].)

---

## 6. general/ 공용 유틸 (53 파일)

### 인덱스 변환 — (n,m) ↔ nm
2D 구조격자를 1D nm 인덱스로 펴는 핵심 변환. ddbound(domain-decomposition halo) 보정 포함.

**n_and_m_to_nm** (`n_and_m_to_nm.f90:57-61`):
$$ nm = n + nmaxddb\cdot(m-1+ddb) + ddb,\quad nmaxddb = nmax + 2\cdot ddbound $$

**nm_to_n_and_m** (`nm_to_n_and_m.f90:64-65`) — 역변환, 음수 nm 안전한 floor 사용:
$$ m = \lfloor (nm-1)/nmaxddb \rfloor + 1 - ddb,\quad n = nm - nmaxddb(m-1+ddb) - ddb $$
주석에 옛 `int(nm/nmaxddb)+1-ddb` 방식이 음수·배수에서 틀린다는 경고 (`nm_to_n_and_m.f90:60-63`).

### 에러·종료
- **prterr** (`prterr.f90:30-39`): 출력장치에 메시지 인쇄. 메시지 번호(G051/U190/Z013/P004/U021 등)로 빈 메시지/경고/에러 구분. 위 모든 chk*가 검사 실패 시 호출하는 표준 통로.
- **d3stop** (`d3stop.f90:30-37`): 에러코드로 실행 종료. CSTOP 드라이버이며 RTC/wave/sobek 통신 동기화 처리 ("Reason to create was the implementation of coupling with RTC") — `use SyncRtcFlow, sync_flowcouple, sync_flowwave, d3d_sobek` (`d3stop.f90:43-46`).

### 기타 공용 함수 (역할 요약)
| 파일 | 역할 (Function 주석) |
|---|---|
| `nuliar.f90` | 정수배열 길이 INTDIM 0 초기화 |
| `keyinp.f90` | 문자열에서 character 파라미터 추출 (`keyinp.f90:31-33`) |
| `read1c/read1i/read1r`·`read2*`·`readnc/readni/readnr` | 입력 1개/2개/N개 char·int·real 읽기 패밀리 |
| `timdat.f90` | actual time(분)+itdate(julian)에서 `yyyymmdd hhmmss` 반환 (`timdat.f90:31-35`) |
| `dattim.f90`·`setcurrentdatetime.f90`·`dtn.f90` | 시스템 일시·현재 datetime 설정·시간 변환 |
| `angle.f90` | 두 점을 잇는 선과 평행선 사이 각 계산 (`angle.f90:32-35`) — inigrd 45도 검사용 |
| `distance_gdp.f90` | 점 간 거리(sferic 고려) |
| `magdir_to_uv.f90` | 크기/방향 → u,v 성분 |
| `nm_to_diag.f90` | nm → 진단출력 좌표 |
| `getcel/open_datdef/delnef/prtnefiserr` | NEFIS comm-file 셀/dat-def 열기·삭제·에러 |
| `checkmeteoresult.f90` | meteo 모듈 결과 success 검사 (inchkr에서 반복 호출) |
| `copykcuv.f90` | kcu/kcv mask 복사 |
| `step_to_screen.f90` | 타임스텝 진행 화면 출력 |
| `flwlic.f90` | 라이선스 검사 |
| `search/srckey/modlen/regel/txtstr/txtmrk/evenquotes` | 문자열 파싱 보조 (키워드 검색·길이·따옴표 검사) |
| `z_taubotmodifylayers.f90`·`z_ainpro.f90` | z-model 바닥전단 층보정·면적 proration |

(read*/string 파싱·NEFIS 헬퍼군의 실행부 세부는 미인용 — **source-needed**. 본 노트는 헤더 Function 주석 및 inchki/inchkr 호출맥락만 검증.)

---

## 7. 요약

1. **inchki = 정적 검사 드라이버** (`inchki.f90:37`): 격자(inigrd)→경계(chkbnd)→mask(chkkc)→수직격자(chkgeo)→물리(chkphy)→수치(chknum)→관측점/구조물(chksit/chkstr) 순으로 정합성을 누적 검사하고 초기 배열을 정의.
2. **inchkr = 시변 초기상태 드라이버** (`inchkr.f90:36`): t0 경계강제력·기상·퇴적·부피·밀도·마찰·난류를 채움 (restart 가능).
3. 검사 실패는 `prterr` 메시지코드 + `error` 플래그로 통일 처리, 치명적 종료는 `d3stop`(RTC/wave 동기화 포함).
4. **dryflc 하한 0.02 m 강제**(`chknum.f90:120-127`), **σ thick 합=100% 검증**(`chkgeo.f90:90-104`)가 대표적 입력 정합성 게이트.
5. general/은 (n,m)↔nm 변환(ddbound 보정), 에러출력, NEFIS·시간·기하·문자열 파싱 공용함수 모음.

---
title: "SWAN swanuse §4.5.5-4.7 command reference — numerics(PROP/NUMERIC) + output(FRAME/BLOCK/TABLE/QUANTITY/SPECOUT) + lock-up(COMPUTE/HOTFILE/STOP) verbatim"
topic: swan
canonical_source: external
external_source: "swanuse.pdf (User Manual, SWAN Cycle III version 41.51) §4.5.5 Numerics + §4.6 Output + §4.7 Lock-up (p.84-114) + node29/31/32/33/34.md. command 구문·default. NUMERIC 는 swantech Ch 3 이론 대응."
citation_status: verified
verification_method: "swanuse website_markdown node29(Numerics 220줄)/node31(output locations 398)/node32(quantities 858)/node34(lock-up 199) 직접 read: PROP/NUMERIC(STOPC/STAT/DIRIMPL/CTHETA/SETUP)/FRAME/CURVE/POINTS/QUANTITY/BLOCK/TABLE/SPECOUT/COMPUTE/HOTFILE/STOP 구문+default verbatim. node32 변수목록은 요약."
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — command 구문·default 값 verbatim"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-command-setup-grid-reference.md
  - models/SWAN/manual-notes/swan-command-physics-reference.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md
---

# SWAN swanuse §4.5.5-4.7 numerics/output/lock-up command reference — verified

> swanuse.pdf (User Manual v41.51) §4.5.5-4.7 직접 read. **수치 scheme·출력·실행** command. NUMERIC default = swantech Ch 3 식 계수와 일치 (★ cross-validation). Start-up/grid/BC 는 [[swan-command-setup-grid-reference]], physics 는 [[swan-command-physics-reference]].

## 1. §4.5.5 Numerics

### 1.1 PROP — propagation scheme
```
PROP <-> BSBT | GSE [waveage] <Sec|MIn|HR|DAy>>
```
- **BSBT** (1차 upwind, stationary·nonstationary) / 미지정 시 **default: stationary=SORDUP, nonstationary=S&L(Stelling-Leendertse)** ([[swan-tech-ch3-discretization]] §1)
- **GSE [waveage]** = garden-sprinkler correction (S&L, 장거리 swell; wave age) ([[swan-tech-ch3-discretization]] §2 Eq 3.11-13)
- 모든 scheme curvilinear 가능. boundary 인접은 BSBT 회귀.

### 1.2 NUMERIC ★ (swantech Ch 3 대응)
```
NUMeric (STOPC [dabs][drel][curvat][npnts] <STAT [mxitst][alfa] | NONSTAT [mxitns]> [limiter]) (DIRimpl [cdd]) (SIGIMpl [css][eps2][outp][niter]) (CTHeta [cfl]) (CSigma [cfl]) (SETUP [eps2][outp][niter])
```
| 옵션 | default | swantech | 의미 |
|---|---|---|---|
| **STOPC** | dabs=**0.005**, drel=**0.01**, curvat=**0.005**, npnts=**99.5** | §3.4 (Eq 3.26 curvature) | Hs **곡률 stopping**: drel **and** curvat **or** dabs, npnts% wet 점. QC 변형 dabs×H_inc |
| STAT `mxitst` | **50** | §3.4 | stationary 최대 iteration (0=입력검증만) |
| STAT `alfa` | **0.00** (제안 0.01) | §3.7 (Eq 3.29-30 τ⁻¹=ασ) | **frequency-dependent under-relaxation**, **diffraction 시 권장** |
| NONSTAT `mxitns` | **1** | | nonstat time step당 iteration |
| `limiter` | **0.1** | §3.7 (Eq 3.27 γ=0.1) | **action density limiter** (omni Phillips level 분율) |
| **DIRimpl** `cdd` | **0.5** | §3.2 (Eq 3.21 ν) | refraction scheme: 0=central(정확,spurious) / 1=upwind(diffusive, 강 gradient 시) |
| **SIGIMpl** `css` | 0.5 | §3.2 | frequency shifting (current·time-varying depth, SIP solver) |
| **CTHETA** `cfl` | **0.9** | **§3.8 (Eq 3.41 α_θ=0.9 REFRLIM)** ★ | **refraction limiter** — coarse bathy 과도 turning 방지 (미지정 시 비활성!) |
| **CSIGMA** `cfl` | 0.9 | §3.8 | frequency-shift limiter |
| SETUP `eps2` | SIP 1e-4 / SOR 1e-6 | §3.3/Ch6 | linear solver 정지 (\|\|AN−b\|\|≤eps2\|\|b\|\|) |
> ★ **CTHETA cfl=0.9 = swantech Eq 3.41 α_θ; limiter=0.1 = Eq 3.27 γ; STOPC = §3.4 curvature** — 이론↔command 정합. ([[swan-tech-ch3-refraction-limiter]], [[swan-tech-ch3-solution-iteration-limiter]])

## 2. §4.6 Output

### 2.1 §4.6.1 Output locations
```
FRAme 'sname' [xpfr][ypfr][alpfr][xlenfr][ylenfr][mxfr][myfr]   ! 직사각 출력 frame
GROUp 'sname' SUBGrid [ix1][ix2][iy1][iy2]                       ! 계산격자 부분
CURve 'sname' [xp1][yp1] < [int][xp][yp] >                       ! 점 연결 곡선(보간)
RAY   'rname' [xp1][yp1][xq1][yq1] < ... >                       ! wave ray
ISOline 'sname' 'rname' <DEPth|BOTtom> [dep]                     ! 수심 등고선
POINts  'sname' < [xp][yp] > | FILE 'fname'                      ! 출력 점
NGRid  'sname' ... <TRIAngle|EASYmesh|...>                       ! nested grid 경계
```
- FRAME/GROUP = 공간 field(BLOCK용), CURVE/POINTS = 점 위치(TABLE/SPECOUT용), ISOLINE = ray 따라 등수심.

### 2.2 §4.6.2 Output quantities
```
QUANTity < output variable list > [...]                          ! 변수 속성(단위·기준·hexp 등)
OUTPut OPTIons 'comment' (TABle [field]) (BLOck [ndec][len]) (SPEC [ndec])
BLOck 'sname' <HEADER|NOHEADER> 'fname' (LAYOUT [idla]) < variables [unit] > ... (OUTPUT [tbegblk][deltblk]<Sec|...>)   ! 공간 field 출력
TABle 'sname' <HEADER|NOHEADER|INDEXED> 'fname' < variables > (OUTPUT [tbegtbl][delttbl]<...>)                          ! 점별 table
SPECout 'sname' <SPEC1D|SPEC2D> <ABS|REL> 'fname' (OUTPUT ...)   ! 스펙트럼 출력
NESTout 'sname' 'fname' (OUTPUT ...)                             ! nest 경계 스펙트럼
```
- 주요 **출력 변수**(QUANTITY/BLOCK/TABLE): `HSIGN`(Hs), `HSWELL`, `DIR`(평균방향), `PDIR`(peak dir), `TM01`/`TM02`/`TMM10`/`RTP`(peak period), `TPS`, `DSPR`(방향 spread), `DEPTH`, `WATLEV`, `BOTLEV`, `VEL`(current), `WIND`, `FRCOEF`(friction), `WLEN`(파장), `STEEPNESS`, `QB`(breaking fraction), `DISSIP`(소산), `QP`(peakedness), `SETUP`, `FORCE`, `UBOT`(bottom orbital), `TMBOT`, `WFORCE`, `XP/YP/DIST`(좌표), `OUT`(time) 등 + `TRANSP`(energy transport) 등.
- BLOCK = 2D field (FRAME/GROUP), TABLE = 점별 (POINTS/CURVE), SPECOUT = 1D/2D 스펙트럼 (절대/상대 freq).

### 2.3 §4.6.3 Intermediate results
```
TEST [itest] [itrace] (POINTS <XY [x][y] | IJ [i][j]>) (PAR 'fname') (S1D 'fname') (S2D 'fname')
```
디버그: test level itest, 특정 점의 source term(PAR)·스펙트럼(S1D/S2D) 출력.

## 3. §4.7 Lock-up

### 3.1 COMPUTE
```
COMPute ( <-> STATionary [time] | NONSTat [tbegc][deltc]<Sec|MIn|HR|DAy>[tendc]> )
```
- **stationary mode**: `COMPUTE` (옵션 없음). **nonstationary mode**: STATIONARY [time](특정 시각 정상해) 또는 NONSTAT [tbegc][deltc][tendc](기간)
- **여러 COMPUTE** (NONSTAT): 종료 wave state = 다음 초기상태 (INIT 없으면) → stationary→nonstationary spin-up·time step 변경·BC 변경 가능 (hotfile 회피). 입력검증: `NUM STOPC MXITST=0`
- **소형(<100km/1°) stationary 권장**, 대형 nonstationary.

### 3.2 HOTFILE / STOP
```
HOTFile 'fname' <FREE|UNFormatted>     ! hotstart 파일 write (다음 run INIT HOTSTART)
STOP                                    ! command 파일 종료
```

## 4. 전형 command 순서

```
PROJECT → SET → MODE → COORDINATES → CGRID → READGRID → INPGRID/READINP(BOT/WIND/...) → WIND
→ BOUND SHAPESPEC → BOUNDSPEC → INITIAL → GEN3 → SSWELL → WCAPPING → FRICTION → BREAKING → TRIAD
→ PROP → NUMERIC → FRAME/POINTS → QUANTITY → BLOCK/TABLE/SPECOUT → COMPUTE → HOTFILE → STOP
```

## 5. 한계

- node32(858줄) 출력 변수 전체 목록·단위·hexp·각 변수 정의는 §2.2 요약 — swanuse Appendix A(변수 정의) + p.94-109 직접.
- QUANTITY 의 [hexp]/[power]/[fmin][fmax] 등 변수별 속성 옵션, BLOCK LAYOUT idla, output time format detail 미상세.
- SIGIMPL/SETUP solver의 niter·outp 옵션 요약.

## 6. 연결

- [[swan-command-setup-grid-reference]] — §4.4-4.5.3 (PROJECT/CGRID/BOUND/INITIAL)
- [[swan-command-physics-reference]] — §4.5.4 physics (GEN/WCAPPING/...)
- [[swan-tech-ch3-solution-iteration-limiter]] — STOPC/limiter/alfa 이론 (§3.4/3.7)
- [[swan-tech-ch3-refraction-limiter]] — CTHETA cfl=0.9 이론 (§3.8 Eq 3.41)
- [[swan-tech-ch3-discretization]] — PROP BSBT/SORDUP/S&L + GSE 이론
- [[swan-documentation-stack]] — 57 command 목록 (이로써 §4 command reference 3노트 완성)

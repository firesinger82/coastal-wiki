---
title: "SWAN swanuse §4.5.5-4.7 command reference — numerics(PROP/NUMERIC) + output(FRAME/BLOCK/TABLE/QUANTITY/SPECOUT) + lock-up(COMPUTE/HOTFILE/STOP) verbatim"
topic: swan
canonical_source: external
external_source: "swanuse.pdf (User Manual, SWAN Cycle III version 41.51) §4.5.5 Numerics + §4.6 Output + §4.7 Lock-up (p.84-114) + node29/31/32/33/34.md. command 구문·default. NUMERIC 는 swantech Ch 3 이론 대응."
citation_status: verified
verification_method: "swanuse website_markdown node29(Numerics 220줄)/node31(output locations 398)/node32(quantities 858)/node34(lock-up 199) 직접 read: PROP/NUMERIC(STOPC/STAT/DIRIMPL/CTHETA/SETUP)/FRAME/CURVE/POINTS/QUANTITY/BLOCK/TABLE/SPECOUT/COMPUTE/HOTFILE/STOP 구문+default verbatim. node32 변수목록은 요약. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — command 구문·default 값 verbatim"
verification_date: 2026-06-02
last_source_check: "2026-10-13 (recovery 대조 반영)"
related:
  - models/SWAN/manual-notes/swan-command-setup-grid-reference.md
  - models/SWAN/manual-notes/swan-command-physics-reference.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md
---

# SWAN swanuse §4.5.5-4.7 numerics/output/lock-up command reference — verified

> swanuse.pdf (User Manual v41.51) §4.5.5-4.7 직접 read. **수치 scheme·출력·실행** command. Start-up/grid/BC 는 [swan-command-setup-grid-reference](swan-command-setup-grid-reference.md), physics 는 [swan-command-physics-reference](swan-command-physics-reference.md).

## 1. §4.5.5 Numerics

### 1.1 PROP — propagation scheme
```
PROP <-> BSBT | GSE [waveage] <Sec|MIn|HR|DAy>>
```
- **BSBT** (1차 upwind, stationary·nonstationary) / 미지정 시 **default: stationary=SORDUP, nonstationary=S&L(Stelling-Leendertse)** ([swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) §1)
- **GSE [waveage]** = garden-sprinkler correction (S&L, 장거리 swell; wave age) ([swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) §2 Eq 3.11-13)
- 모든 scheme curvilinear 가능. boundary 인접은 BSBT 회귀.

### 1.2 NUMERIC ★ (swantech Ch 3 대응)

문서 문법 (swanuse PDF 93쪽 / 인쇄 85쪽):

```
NUMeric (STOPC [dabs][drel][curvat][npnts] <STAT [mxitst][alfa] | NONSTAT [mxitns]> [limiter]) (DIRimpl [cdd]) (SIGIMpl [css][eps2][outp][niter]) (CTHeta [cfl]) (CSigma [cfl]) (SETUP [eps2][outp][niter])
```
| 옵션 | default | swantech | 의미 |
|---|---|---|---|
| **STOPC** | dabs=**0.005**, drel=**0.01**, curvat=**0.005**, npnts=**99.5** | §3.4 (Eq 3.26 curvature) | Hs **곡률 stopping**: drel **and** curvat **or** dabs, npnts% wet 점. QC 변형 dabs×H_inc |
| STAT `mxitst` | **50** | §3.4 | stationary 최대 iteration (0=입력검증만) |
| STAT `alfa` | **0.00** (제안 0.01) | §3.7 (Eq 3.29-30 τ⁻¹=ασ) | **frequency-dependent under-relaxation**, **diffraction 시 권장** |
| NONSTAT `mxitns` | 명령 생략 시 **1** | swanuse PDF 94쪽 / 인쇄 86쪽 | NONSTAT을 명시하면 MXITNS를 입력해야 한다. `src/swanpre1.ftn:1959` `CALL ININTG ('MXITNS' , MXITNS   , 'REQ', 0 )`. |
| `limiter` | **0.1** | §3.7 (Eq 3.27 γ=0.1) | **action density limiter** (omni Phillips level 분율) |
| **DIRimpl** `cdd` | **0.5** | §3.2 (Eq 3.21 ν) | refraction scheme: 0=central(정확,spurious) / 1=upwind(diffusive, 강 gradient 시) |
| **SIGIMpl** `css` | 0.5 | §3.2 | frequency shifting (current·time-varying depth, SIP solver) |
| **CTHETA** `cfl` | **0.9** | swanuse PDF 95쪽 / 인쇄 87쪽 | CTHETA는 Courant 수를 사용해 굴절 속도를 제한한다. **미지정 시 비활성**이다. `src/swancom5.ftn:1708` `!     --- limit Ctheta using Courant number`. |
| **CSIGMA** `cfl` | 0.9 | §3.8 | frequency-shift limiter |
| SIGIMPL `eps2 / outp / niter` | **1e-4 / 0 / 20** | swanuse PDF 95쪽 / 인쇄 87쪽 | SIP는 잔차의 2-노름과 RHS 노름을 비교한다. 문서 식은 $‖A N⃗ₖ − b⃗‖₂ ≤ [eps2] ‖b⃗‖₂$이다. `src/swancom1.ftn:8638` `EPSLIN = REPS*BNORM`. |
| SETUP `eps2 / outp / niter` | **1e-6 / 0 / 1000** | swanuse PDF 95쪽 / 인쇄 87쪽 | SOR의 RESM은 점별 해 갱신량 절댓값의 최댓값이다. 문서 식은 $\lVert\overline\eta_{k+1}-\overline\eta_k\rVert_\infty\leq[\mathtt{eps2}]$이다. `src/swancom1.ftn:12056` `RES = ABS(SETUP(INDX) - SETPI)`. |

SIGIMPL 입력기는 CSS와 EPS2 사이에서 EPS1도 읽는다. 위치 인수로 입력할 때 문서 문법 그대로의 순서를 사용하면 값이 다른 슬롯에 들어갈 수 있다. (`src/swanpre1.ftn:2028` `CALL INREAL ('EPS1' , PNUMS(11), 'UNC', 0.)`.)

`IF ( .NOT. PNUMS(2).NE.-1. ) THEN`에서 `IQCM.EQ.0`이고 ITRIAD=3이면 DABS를 0.01 m로 정한다. 새 실행의 미지정값 또는 명시한 -1이 이 조건에 해당한다. QC는 같은 분기에서 0.05를 쓴다. (`src/swanmain.ftn:6503` `IF ( .NOT. PNUMS(2).NE.-1. ) THEN`; `src/swanmain.ftn:6508` `PNUMS(2) = 0.01`.)

일반 STOPC는 파고와 주기 조건을 함께 검사한다. QC는 주기 조건을 쓰지 않는다. 첫 반복의 정확도 종료도 제한한다. (`src/swancom1.ftn:9877` `( TMCURV.LE.PNUMS(16) .AND.`; `src/swancom1.ftn:2352` `IF ( (ITER.NE.1 .OR. PNUMS(21).EQ.0.) .AND.`.)

Appendix C는 주기 수렴 인수와 옛 ACCUR 선택을 싣는다. (`src/swanpre1.ftn:1948` `CALL INREAL ('DTABS'  , PNUMS(3) , 'STA', 1000.)`; `src/swanpre1.ftn:1949` `CALL INREAL ('CURVT'  , PNUMS(16), 'STA', 1000.)`; `src/swanpre1.ftn:1963` `PNUMS(21) = 0.`; swanuse PDF 141쪽 / 인쇄 133쪽.)

옛 REFRLIM 입력은 FRLIM과 POWER로 주파수별 감쇠 계수를 정한다. REFRLIM의 주파수별 굴절 완화는 CTHETA의 CFL 제한과 다르다. SIGEXPL의 CFL 초기값은 √2/2다. (`src/swancom5.ftn:1671` `FAC = MIN(1.,(SPCSIG(IS)/FRLIM)**PP)`; `src/swanmain.ftn:1307` `PNUMS(19) = 0.5 * sqrt (2.)`; swanuse PDF 141쪽 / 인쇄 133쪽.)

스펙트럼 SWSOR의 검사량은 방정식 잔차가 아니라 최대 갱신량이다. SIP의 상대 잔차 문턱과 다르다. swanuse의 수위 상승 SOR 정지식을 이 루틴의 설명으로 대체하지 않는다. (`src/swancom1.ftn:9258` `RES = ABS(AC2(ID,IS,KCGRD(1)) - AC2I)`; `src/swancom1.ftn:9364` `IF ( RESM.GT.REPS ) ICONV = 0`; swanuse PDF 95쪽 / 인쇄 87쪽.)

## 2. §4.6 Output

### 2.1 §4.6.1 Output locations
```
FRAme 'sname' [xpfr][ypfr][alpfr][xlenfr][ylenfr][mxfr][myfr]   ! 직사각 출력 frame
GROUp 'sname' SUBGrid [ix1][ix2][iy1][iy2]                       ! 계산격자 부분
CURve 'sname' [xp1][yp1] < [int][xp][yp] >                       ! 점 연결 곡선(보간)
RAY   'rname' [xp1][yp1][xq1][yq1] < ... >                       ! ISOLINE과 교차시킬 직선 집합
ISOline 'sname' 'rname' <DEPth|BOTtom> [dep]                     ! 수심 등고선
POINts  'sname' < [xp][yp] > | FILE 'fname'                      ! 출력 점
NGRid  'sname' ... <TRIAngle|EASYmesh|...>                       ! nested grid 경계
```
- FRAME/GROUP = 공간 field(BLOCK용), CURVE/POINTS = 점 위치(TABLE/SPECOUT용), ISOLINE = ray 따라 등수심.

### 2.2 §4.6.2 Output quantities
```
QUANTity < output variable list > [...]                          ! 이름·표시 범위·예외값·정의 인수·기준 좌표
OUTPut OPTIons 'comment' (TABle [field]) (BLOck [ndec][len]) (SPEC [ndec])
BLOck 'sname' <HEADER|NOHEADER> 'fname' (LAYOUT [idla]) < variables [unit] > ... (OUTPUT [tbegblk][deltblk]<Sec|...>)   ! 공간 field 출력
TABle 'sname' <HEADER|NOHEADER|INDEXED> 'fname' < variables > (OUTPUT [tbegtbl][delttbl]<...>)                          ! 점별 table
SPECout 'sname' <SPEC1D|SPEC2D> <ABS|REL> <S|L> 'fname' (OUTPUT ...)   ! 스펙트럼 출력
NESTout 'sname' 'fname' (OUTPUT ...)                             ! nest 경계 스펙트럼
```
- 주요 **출력 변수**(QUANTITY/BLOCK/TABLE): `HSIGN`(Hs), `HSWELL`, `DIR`(평균방향), `PDIR`(peak dir), `TM01`/`TM02`/`TMM10`/`RTP`(peak period), `TPS`, `DSPR`(방향 spread), `DEPTH`, `WATLEV`, `BOTLEV`, `VEL`(current), `WIND`, `FRCOEF`(friction), `WLEN`(파장), `STEEPNESS`, `QB`(breaking fraction), `DISSIP`(소산), `QP`(peakedness), `SETUP`, `FORCE`, `UBOT`(bottom orbital), `TMBOT`, `XP/YP/DIST`(좌표), `TIME`(시각) 등 + `TRANSP`(energy transport) 등.
- BLOCK = 2D field (FRAME/GROUP), TABLE = 점별 (POINTS/CURVE), SPECOUT = 1D/2D 스펙트럼 (절대/상대 freq).

QUANTITY는 단위 문자열 입력 기능이 없다. FORCE가 명령 선택자이다. WForce는 기본 짧은 이름이다. TIME은 시각 출력 물리량이다. OUT은 출력 시각 옵션의 시작이다. (`src/swanmain.ftn:1880` `OVKEYW(IVTYPE) = 'FOR'`; `src/swanmain.ftn:1881` `OVSNAM(IVTYPE) = 'WForce'`; `src/swanpre2.ftn:2468` `IF (KEYWIS ('OUT')) IVTYPE = 98`.)

RAY는 ISOLINE과 교차시킬 직선 집합을 정의한다. 굴절에 따른 파향선을 계산하는 명령이 아니다. (swanuse PDF 99쪽 / 인쇄 91쪽: `the rays thus defined have nothing in common with wave rays`.)

SPECOUT의 S/L 기본값은 S이다. L은 surfbeat의 낮은 주파수 출력을 선택한다. (`src/swanpre2.ftn:1899` `CALL INKEYW ('STA', 'S')`; swanuse PDF 116–117쪽 / 인쇄 108–109쪽.)

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
- **stationary mode**: `COMPUTE` (옵션 없음). **nonstationary mode**: `STATIONARY [time]` (특정 시각 정상해) 또는 `NONSTAT [tbegc][deltc][tendc]` (기간)
- **여러 COMPUTE** (NONSTAT): 종료 wave state = 다음 초기상태 (INIT 없으면) → stationary→nonstationary spin-up·time step 변경·BC 변경 가능 (hotfile 회피). 입력검증: `NUM STOPC MXITST=0`

비정상 시간 간격과 종료 시각은 필수다. (`src/swanpre1.ftn:903` `CALL INITVD ('DELTC', DT, 'REQ', 0D0)`; `src/swanpre1.ftn:904` `CALL INCTIM (ITMOPT,'TENDC',TFINC,'REQ',0D0)`; swanuse PDF 121쪽 / 인쇄 113쪽.)

단계 수는 `MTC = NINT ((TFINC - TINIC)/DT)`로 정한다. 경고는 `IF (MOD(TFINC-TINIC,DT).GT.0.01*DT .AND.` / `MOD(TFINC-TINIC,DT).LT.0.99*DT)`일 때만 발생한다. (`src/swanpre1.ftn:914–916`.)

입력기는 COMPUTE 300개 상한을 검사한다. (`src/swanpre1.ftn:924` `'No more than 300 COMPUTE commands are allowed'`.)
- **소형(<100km/1°) stationary 권장**, 대형 nonstationary.

### 3.2 HOTFILE / STOP
```
HOTFile 'fname' <FREE|UNFormatted>     ! hotstart 파일 write (다음 run INIT HOTSTART)
STOP                                    ! command 파일 종료
```

HOTFILE은 입력기가 해당 행을 읽는 즉시 파일을 쓴다. MPI 실행에서는 프로세스별 접미사가 붙는다. UNFORMATTED 파일은 기록 호환성이 필요하다. (`src/swanpre1.ftn:1333` `CALL BACKUP( AC2, SPCSIG, SPCDIR, KGRPNT, XCGRID, YCGRID )`; `src/swanpre1.ftn:6747` `WRITE (NREF) VERTXT`; swanuse PDF 122쪽 / 인쇄 114쪽.)

## 4. 전형 command 순서

```
PROJECT → SET → MODE → COORDINATES → CGRID → READGRID → INPGRID/READINP(BOT/WIND/...) → WIND
→ BOUND SHAPESPEC → BOUNDSPEC → INITIAL → GEN3 → SSWELL → WCAPPING → FRICTION → BREAKING → TRIAD
→ PROP → NUMERIC → FRAME/POINTS → QUANTITY → BLOCK/TABLE/SPECOUT → COMPUTE → HOTFILE → STOP
```

## 5. 대조 근거

- [R5 PN-089–094](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#26-prop와-numeric)는 SIGIMPL·SETUP의 EPS2·OUTP·NITER와 CTHETA·CSIGMA 입력을 대조한다.
- [R6 출력 대조](../../../_staging/recovery/compare/swan-outputs-vs-code.md#4-노트-대조와-수정안)는 출력 선택자와 파일 형식을 대조한다.

## 6. 연결

- [swan-command-setup-grid-reference](swan-command-setup-grid-reference.md) — §4.4-4.5.3 (PROJECT/CGRID/BOUND/INITIAL)
- [swan-command-physics-reference](swan-command-physics-reference.md) — §4.5.4 physics (GEN/WCAPPING/...)
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — STOPC/limiter/alfa 이론 (§3.4/3.7)
- [swan-tech-ch3-refraction-limiter](swan-tech-ch3-refraction-limiter.md) — CTHETA cfl=0.9 이론 (§3.8 Eq 3.41)
- [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) — PROP BSBT/SORDUP/S&L + GSE 이론
- [swan-documentation-stack](swan-documentation-stack.md) — 57 command 목록 (이로써 §4 command reference 3노트 완성)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD `43e9bbb` (2026-07-13 patch B). (`src/swanmain.ftn:965` `VERNUM = 41.51`.)

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:NT-046 | set-up SOR의 종료 기준 | `manual-notes/swan-command-numerics-output-reference.md:48` `SIP 1e-4 / SOR 1e-6`와 `linear solver 정지`. 노트 48행은 SETUP에도 $\lVert AN-b\rVert\leq eps2\lVert b\rVert$를 적용했다. swanuse PDF 95쪽의 원문은 SIP의 상대 잔차식과 SOR의 $\lVert\overline\eta_{k+1}-\overline\eta_k\rVert_\infty\leq[\mathtt{eps2}]$를 따로 적는다 | `src/swancom1.ftn:11873`의 `RES = ABS(SETUP(INDX) - SETPI)`와 `src/swanmain.ftn:1269`의 `PNUMS(23) = 1.E-6`이 SOR 식에 대응한다. | B 문서 오기 | `NUMERIC SETUP`의 기본 허용 갱신량은 $10^{-6}$ m다. set-up SOR의 정지는 상대 선형계 잔차 기준으로 설명하지 않는다. SIGIMPL의 반복법과 구분한다. [10-13 결론 검증 보완] |
| R4:T1-039 | COMPUTE 뒤 명령 | swanuse PDF 33쪽 / 인쇄 25쪽: “all commands after COMPUTE are ignored” | `src/swanmain.ftn:399` `CALL SWREAD (COMPUT)`이 반복문 안에 있다. | B 문서 오기 | COMPUTE 이후에도 명령 읽기를 재개한다. |
| R5:PN-081 | 회절의 PROP 덮어쓰기 | PROP 기본값의 DIFFRACTION 예외. swanuse PDF 92쪽 / 인쇄 84쪽의 `default S&L` / `default SORDUP`. | `src/swanmain.ftn:4090` `IF ( IDIFFR.EQ.1 ) THEN`, `src/swanmain.ftn:4094` `PROPSN = 1`, `src/swanmain.ftn:4095` `PROPSS = 1`. 4088 주석은 `allocate arrays for diffraction and set prop scheme to BSBT`다. | C 문서 누락 | DIFFRACTION을 켜면 정상·비정상 전파 선택은 BSBT로 바뀐다. |
| R5:PN-082 | FTIM의 DABS | NUMERIC STOPC DABS/DREL/CURVAT/NPNTS. swanuse PDF 94쪽 / 인쇄 86쪽: `[dabs] = 0.005 [m] or` … `0.05 [−] in case of QC model`, `[drel] = 0.01`, `[curvat] = 0.005`, `[npnts] = 99.5`. | `src/swanpre1.ftn:1944` `CALL INREAL ('DABS'   , PNUMS(2) , 'UNC', 0.)`; 1945–1947행은 DREL→PNUMS(1), CURVAT→PNUMS(15), NPNTS→PNUMS(4)를 UNC로 읽는다. `src/swanmain.ftn:1219` `PNUMS(1)  = 0.01`, `src/swanmain.ftn:1227` `PNUMS(4)  = 99.50`, `src/swanmain.ftn:1292` `PNUMS(15) = 0.005`, `src/swanmain.ftn:6505` `IF ( ITRIAD.NE.3 ) THEN`, `src/swanmain.ftn:6506` `PNUMS(2) = 0.005`, `src/swanmain.ftn:6508` `PNUMS(2) = 0.01`, `src/swanmain.ftn:6511` `PNUMS(2) = 0.05`. `src/SwanQCM.ftn90:350` `PNUMS(2) = PNUMS(2) * hsi`. | C 문서 누락 | `IF ( .NOT. PNUMS(2).NE.-1. ) THEN`에서 `IQCM.EQ.0`이고 ITRIAD=3이면 DABS를 0.01 m로 정한다. 새 실행의 미지정값 또는 명시한 -1이 이 조건에 해당한다. QC는 같은 분기에서 0.05를 쓴다. [10-13 결론 검증 정정] |
| R5:PN-083 | STOPC 경계값 | STOPC 부등식. swanuse PDF 93쪽 / 인쇄 85쪽: `less than [drel]`, `less than [curvat]`, `less than [dabs]`, `more than fraction [npnts]%`. | `src/swancom1.ftn:9874–9875` `LCONV = ( HSABS.LE.PNUMS(2) .OR.` / `(HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )`. `src/swancom1.ftn:2353` `ACCUR.GE.PNUMS(4) ) GOTO 470`. `src/SwanConvStopc.ftn90:224` `lconv = ( hsabs <= PNUMS(2) .or. (hsabs <= hsrel .and. hscurv <= curvah) ) .and. &`. | B 문서 오기 | 파고·주기·곡률 오차의 코드 비교는 `.LE.`이다. swantech PDF 91–92쪽 식 (3.22)·(3.23)·(3.26)은 `<`를 명시한다. B는 이 경계값 차이에 한정한다. 만족 격자 비율의 코드 비교는 `.GE.`이며 문서의 `more than` 표현만으로 오기라고 단정하지 않는다. [10-13 결론 검증 보완] |
| R5:PN-084 | STOPC의 주기·첫 반복 | STOPC의 생략된 주기 조건과 첫 반복 조건. swanuse PDF 93쪽 / 인쇄 85쪽는 `significant wave height`의 수렴만 설명한다. | `src/swanpre1.ftn:1948` `CALL INREAL ('DTABS'  , PNUMS(3) , 'STA', 1000.)`, `src/swanpre1.ftn:1949` `CALL INREAL ('CURVT'  , PNUMS(16), 'STA', 1000.)`. `src/swancom1.ftn:9877–9878` `( TMCURV.LE.PNUMS(16) .AND.` / `(TMREL.LE.PNUMS(1) .OR. TMABS.LE.PNUMS(3)) )`. `src/swancom1.ftn:2352` `IF ( (ITER.NE.1 .OR. PNUMS(21).EQ.0.) .AND.`. `src/SwanConvStopc.ftn90:225` `( tmcurv <= curvat .and. tmabs <= max(tmrel,PNUMS(3)) )`. | C 문서 누락 | 일반 STOPC는 파고와 주기 조건을 함께 검사한다. QC는 주기 조건을 쓰지 않는다. 첫 반복의 정확도 종료도 제한한다. swanuse PDF 141쪽 / 인쇄 133쪽·웹 `swanuse/node49.html:305`에는 주기 인수 문법이 있고 swantech PDF 91–92쪽에는 주기 기준의 이력이 있다. 누락은 swanuse §4.5.5의 현 검사 동작 설명에 한정한다. [10-13 결론 검증 보완] |
| R5:PN-087 | NONSTAT MXITNS | STOPC NONSTAT MXITNS. swanuse PDF 94쪽 / 인쇄 86쪽: `Default: [mxitns] = 1.` | `src/swanmain.ftn:1094` `MXITNS = 1`. 그러나 `src/swanpre1.ftn:1959` `CALL ININTG ('MXITNS' , MXITNS   , 'REQ', 0 )`. `src/ocpcre.ftn:825` `CALL MSGERR (2, 'No value for variable '//NAAM_L)`. | B 문서 오기 | NUMERIC STOPC NONSTAT을 적으면 최대 반복 횟수를 명시해야 한다. |
| R5:PN-090 | SIGIMPL EPS1 | SIGIMPL의 위치 인수. swanuse PDF 93쪽 / 인쇄 85쪽 문법: `SIGIMpl [css] [eps2] [outp] [niter]`. | `src/swanpre1.ftn:2028` `CALL INREAL ('EPS1' , PNUMS(11), 'UNC', 0.)`가 CSS와 EPS2 사이에 있다. `src/swanpre1.ftn:2029` `CALL INREAL ('EPS2' , PNUMS(12), 'UNC', 0.)`, `src/swanpre1.ftn:2030` `CALL INREAL ('OUTP' , PNUMS(13), 'UNC', 0.)`, `src/swanpre1.ftn:2031` `CALL INREAL ('NITER', PNUMS(14), 'UNC', 0.)`. | C 문서 누락 | 입력기는 CSS 다음에 EPS1을 추가로 읽는다. 문서의 위치 인수 순서는 실제 입력기와 다르다. |
| R5:PN-092 | SOR의 절대 기준 | NUMERIC SETUP EPS2/OUTP/NITER. swanuse PDF 95쪽 / 인쇄 87쪽: `Relative stopping criterion` … `(SIP or SOR)`, `‖η̄ₖ₊₁ − η̄ₖ‖∞ ≤ [eps2]`, 기본값 `1.e-6`, `0`, `1000`. | `src/swanpre1.ftn:2066` `CALL INREAL ('EPS2' , PNUMS(23), 'UNC', 0.)`, `src/swanpre1.ftn:2067` `CALL INREAL ('OUTP' , PNUMS(24), 'UNC', 0.)`, `src/swanpre1.ftn:2068` `CALL INREAL ('NITER', PNUMS(25), 'UNC', 0.)`. `src/swanmain.ftn:1269` `PNUMS(23) = 1.E-6`, `src/swanmain.ftn:1270` `PNUMS(24) = 0.`, `src/swanmain.ftn:1271` `PNUMS(25) = 1000.`. `src/swancom1.ftn:12056` `RES = ABS(SETUP(INDX) - SETPI)`, `src/swancom1.ftn:12058` `RESM  = RES`, `src/swancom1.ftn:12076` `IF ( RESM.GT.REPS ) THEN`. | F 표기 차이 | SOR의 EPS2는 수위 갱신량의 절대 허용오차다. swanuse PDF 95쪽 / 인쇄 87쪽의 SOR 식 `‖η̄ₖ₊₁ − η̄ₖ‖∞ ≤ [eps2]`도 코드와 같다. SIP와 SOR를 함께 부른 `Relative` 표제의 표현 차이로 분류한다. [10-13 결론 검증 정정] |
| R5:PN-093 | SIP 수치 하한 | SIP 허용오차의 보정. swanuse PDF 95쪽 / 인쇄 87쪽의 EPS2 식에는 하한을 적지 않는다. | `src/swancom1.ftn:8639` `UEPS   = 1000.*UNDFLW*BNORM`, `src/swancom1.ftn:8640` `IF ( EPSLIN.LT.UEPS .AND. BNORM.GT.0. ) THEN`, `src/swancom1.ftn:8649` `EPSLIN = UEPS`. 8854행은 `RNORM.GT.UNDFLW**2`도 요구한다. | C 문서 누락 | SIP는 지나치게 작은 요청 허용오차를 내부 하한으로 올린다. |
| R5:PN-095 | 전파·수치 권고 | PROP·NUMERIC 권고. swanuse PDF 92–93쪽 / 인쇄 84–85쪽: `should correspond to the travel time`, `gradually varying grid`, `conditionally stable`, 더 작은 시간 간격 등의 네 대안. swanuse PDF 94–95쪽 / 인쇄 86–87쪽: ALFA `suggestion` … `0.01`, CFL `suggestion` … `0.9`, 중앙·상류 차분의 정확도 설명. | 입력·수치 계수의 실제 사용은 PN-079–094에 대조했다. | H 코드 대조 대상 아님 | ALFA·CFL·시간 간격 권고를 모든 계산에서 성립하는 정확도 보장으로 쓰지 않는다. |
| R5:PN-098 | COMPUTE 시간 처리 | COMPUTE 시간 검사와 반올림. swanuse PDF 120–121쪽 / 인쇄 112–113쪽은 시작·종료·간격을 정의한다. 비정수 시간 간격 처리는 적지 않는다. | `src/swanpre1.ftn:899` `IF (TINIC .LT. TIMCO) THEN`, `src/swanpre1.ftn:901` `TINIC = TIMCO`, `src/swanpre1.ftn:909` `IF (DIFF .LE. 0.) CALL MSGERR (3,`, `src/swanpre1.ftn:913` `RDTIM = 1./DT`, `src/swanpre1.ftn:914` `MTC = NINT ((TFINC - TINIC)/DT)`, `src/swanpre1.ftn:915–916` `IF (MOD(TFINC-TINIC,DT).GT.0.01*DT .AND.` / `MOD(TFINC-TINIC,DT).LT.0.99*DT)`. | C 문서 누락 | 단계 수는 `MTC = NINT ((TFINC - TINIC)/DT)`로 정한다. 경고는 `IF (MOD(TFINC-TINIC,DT).GT.0.01*DT .AND.` / `MOD(TFINC-TINIC,DT).LT.0.99*DT)`일 때만 발생한다. 나누어떨어지지 않는 모든 경우에 경고한다는 원 결론을 고친다. [10-13 결론 검증 정정] |
| R5:PN-099 | COMPUTE 개수 | 여러 COMPUTE와 INIT. swanuse PDF 120쪽 / 인쇄 112쪽: `wave state at the end of one computation is used as initial state for the next one, unless a command INIT appears`. | `src/swanmain.ftn:394` `DO`, `src/swanmain.ftn:399` `CALL SWREAD (COMPUT)`가 계산과 다음 입력을 반복한다. `src/swanpre1.ftn:923–924` `IF (NCOMPT.GT.300) CALL MSGERR (2,` / `'No more than 300 COMPUTE commands are allowed')`. | C 문서 누락 | 입력기는 COMPUTE 300개 상한을 검사한다. |
| R5:PN-101 | HOTFILE 실행 시점 | HOTFILE 순서. swanuse PDF 122쪽 / 인쇄 114쪽: `This command must be entered immediately after a COMPUTE command.` | `src/swanpre1.ftn:1327` `IF (MXC.LE.0 .AND. OPTG.NE.5) THEN`, `src/swanpre1.ftn:1329` `ELSEIF (MCGRD .LE. 1 .AND. nverts .LE. 0) THEN`, `src/swanpre1.ftn:1333` `CALL BACKUP( AC2, SPCSIG, SPCDIR, KGRPNT, XCGRID, YCGRID )`. | C 문서 누락 | HOTFILE은 읽는 즉시 기록한다. 문서의 순서 의무를 입력기가 별도로 검사하지 않는다. |
| R5:PN-102 | HOTFILE ABI | HOTFILE 바이너리 ABI. swanuse PDF 122쪽 / 인쇄 114쪽: `should follow the same ABI` … `conventions` 다음에 `provided that distinct ABI conventions have been followed`. | `src/swanpre1.ftn:6745` `CALL FOR (NREF, FILENM, 'UU', IOSTAT)`, `src/swanpre1.ftn:6747` `WRITE (NREF) VERTXT`, `src/swanpre1.ftn:6754` `DO IX = 1, MXC`, `src/swanpre1.ftn:6788` `IF (INDX.NE.1) WRITE (NREF) AC2(:,:,INDX)`. 읽기는 `src/swanpre1.ftn:6296` `CALL FOR (NREF, FILENM, 'OU', IOSTAT)`. | B 문서 오기 | UNFORMATTED 파일을 이어 읽으려면 Fortran 레코드와 자료 표현이 호환되어야 한다. distinct ABI라는 문장은 앞 조건과 모순된다. |
| R5:PN-104 | Lock-up 권고·성능 | Lock-up 권고·성능. swanuse PDF 121쪽 / 인쇄 113쪽: `less than 100 km or 1 deg`, `at most 10 minutes`, `Courant number` … `smaller than 10`, `no more than 1 iteration`. swanuse PDF 122쪽 / 인쇄 114쪽: 바이너리는 `less space`·`much faster`. | 계산 시작·반복 수·시간 간격은 PN-086–099의 경로로 제어한다. | H 코드 대조 대상 아님 | 격자 크기·시간 간격·반복 횟수는 문서의 적용 권고다. 바이너리 크기와 속도는 문서의 성능 주장이다. 코드의 강제 조건과 구분한다. |
| R5:PN-173 | DTABS/CURVT·ACCUR | swanuse PDF 141쪽 / 인쇄 133쪽: NUMERIC `STOPC` … `[dtabs] [curvt]`, `ACCUR [drel] [dhoval] [dtoval] [npnts]`. | `src/swanpre1.ftn:1948` `CALL INREAL ('DTABS'  , PNUMS(3) , 'STA', 1000.)`, `src/swanpre1.ftn:1949` `CALL INREAL ('CURVT'  , PNUMS(16), 'STA', 1000.)`, `src/swanpre1.ftn:1963` `PNUMS(21) = 0.`, `src/swanpre1.ftn:1965` `CALL INREAL ('DHOVAL' , PNUMS(15), 'UNC', 0.)`, `src/swanpre1.ftn:1966` `CALL INREAL ('DTOVAL' , PNUMS(16), 'UNC', 0.)`. | C 문서 누락 | Appendix C는 주기 수렴 인수와 옛 ACCUR 선택을 싣는다. 본문 설명에 이 경로를 보충한다. |
| R5:PN-174 | DEP/WNUM·REFRLIM·SIGEXPL | swanuse PDF 141쪽 / 인쇄 133쪽: NUMERIC `DIRimpl [cdd] DEP\|WNUM`, `REFRLim [frlim] [power]`, `SIGEXpl [css] [cfl]`. | `src/swanpre1.ftn:1994` `CALL INKEYW ('STA', 'WNUM')`, `src/swanpre1.ftn:1996` `PNUMS(32) = 0.`, `src/swanpre1.ftn:1998` `PNUMS(32) = 1.`. `src/swanpre1.ftn:2006` `PNUMS(29) = 1.`, 2007–2008행은 FRLIM·POWER를 UNC로 읽는다. `src/swanmain.ftn:1319` `PNUMS(26) = 0.2`, `src/swanmain.ftn:1320` `PNUMS(27) = 2.0`, `src/swanmain.ftn:1307` `PNUMS(19) = 0.5 * sqrt (2.)`. `src/swancom5.ftn:1591`은 수심 기울기 식이다. `src/swancom5.ftn:1593` `CAD_TMP=(CGLOC1/CLOC1)*(ESIN(ID)*DCDX-ECOS(ID)*DCDY)`는 실제 WNUM 경로다. `src/swancom5.ftn:1671` `FAC = MIN(1.,(SPCSIG(IS)/FRLIM)**PP)`, `src/swancom5.ftn:3644` `CFLMAX = PNUMS(19)`. | C 문서 누락 | REFRLIM의 주파수별 굴절 완화는 CTHETA의 CFL 제한과 다르다. SIGEXPL의 CFL 초기값은 √2/2다. |
| R6:O-002 | 중복 이름 | swanuse PDF 96쪽 / 인쇄 88쪽: `the first set is lost (first in the sequence in the command file).` | `src/swanpre2.ftn:598` `COPS%NEXTOPS => OPSTMP`. `src/swanpre2.ftn:2328` `CUOPS => FOPS`. `src/swanpre2.ftn:2330` `IF (CUOPS%PSNAME.EQ.PSNAME) EXIT`. | B 문서 오기 | 출력 집합 이름은 고유해야 한다. 이름이 중복되면 현재 조회 코드는 처음 등록한 집합을 선택한다. |
| R6:O-014 | 주파수 범위 적용 물리량 | swanuse PDF 103쪽 / 인쇄 95쪽: `(For all integral parameters, like HS, (R)TM01 ...)`. | `src/swanpre1.ftn:456–457` `DATA IVOTP /10, 11, 13, 15, 16, 17, 18, 19,` 및 `28, 32, 33, 42, 43, 47, 48    /`. `src/swanpre1.ftn:2311` `'Integration range not allowed for this quantity')`. | B 문서 오기 | 적용 목록은 HSIGN, TM01, DIR, TDIR, DSPR, WLEN, STEEPNESS, TRANSP, RTM01, TM02, FSPR, PER, RPER, TMM10, RTMM10이다. “모든 적분 물리량”은 부정확하다. HSWELL과 QP 등은 이 목록에 없다. |
| R6:O-015 | 방향·벡터의 기준 좌표 | swanuse PDF 104쪽 / 인쇄 96쪽: 기본 `PROBLEMCOORD`. FRAME에서는 `vector components are relative to the x− and y−axes of the frame coordinate system`. swanuse PDF 127쪽 / 인쇄 119쪽의 TRANSP·VEL·WIND는 `except in the case of output with BLOCK command in combination with command FRAME`이라고만 적는다. | `src/swanmain.ftn:3525` `OUTPAR(4) = 0.`. `src/swanout1.ftn:1030` `IF (EQREAL(OUTPAR(4),1.)) THEN`. `src/swanout1.ftn:1032` `ALCQ = -ALPQ`. `src/swanout1.ftn:1035` `ALCQ = 0.`. `src/swanpre1.ftn:2318` `'option not allowed with Nautical convention')`. | B 문서 오기 | 벡터 성분의 기본 기준은 문제 좌표이다. BLOCK와 FRAME을 쓰더라도 QUANTITY FRAME을 지정해야 프레임 좌표로 회전한다. |
| R6:O-017 | OUTPUT OPTIONS 하위 옵션만 입력할 때 | 같은 swanuse PDF 105쪽 / 인쇄 97쪽: `Default: field = 12`, `Default: ndec = 4`, `Default: len = 6`. | `src/swanpre1.ftn:673` `CALL ININTG ('FIELD', FLD_TABLE, 'STA', 11)`. `src/swanpre1.ftn:685` `CALL ININTG ('LEN', NLEN, 'STA', 200)`. `src/swanpre1.ftn:694` `CALL ININTG ('NDEC', DEC_SPEC, 'STA', 5)`. | C 문서 누락 | TABLE만 적으면 11을 사용한다. BLOCK만 적으면 한 줄 길이 200을 사용한다. SPEC만 적으면 5자리 정수 형식을 사용한다. 문서는 명령 생략과 하위 인수 생략을 구분하지 않는다. |
| R6:O-018 | OUTPUT OPTIONS 제한과 SPEC LEN | swanuse PDF 105쪽 / 인쇄 97쪽: field는 8–16이다. ndec의 최댓값은 9이다. len의 최댓값은 9999이다. SPEC 문법에는 `[ndec]`만 있다. | `src/swanpre1.ftn:674` `IF (FLD_TABLE.GT.16) CALL MSGERR (2, '[field] is too large')`. `src/swanpre1.ftn:675` `IF (FLD_TABLE.LT.8)  CALL MSGERR (2, '[field] is too small')`. `src/swanpre1.ftn:696` `CALL ININTG ('LEN', NLEN, 'STA', 200)`. `src/swanpre1.ftn:699` `FORMAT ('(', I4, '(1X,I', I1, '))')`. | C 문서 누락 | 문서의 상한·field 범위는 구현한다. SPEC도 LEN을 받는다. SPEC의 ndec는 소수점 아래 자리 수가 아닌 정수 필드 폭이다. |
| R6:O-029 | TEST 기본값 | swanuse PDF 119쪽 / 인쇄 111쪽: `Default: [itest] = 1`, `Default: [itrace] = 0`. | `src/swanmain.ftn:1614` `ITEST  = 1`. `src/swanpre1.ftn:582` `CALL ININTG ('ITEST' , ITEST , 'STA', 30)`. `src/swanpre1.ftn:591` `CALL ININTG ('ITRACE', ITRACE, 'UNC',  0)`. | C 문서 누락 | TEST를 생략하면 ITEST=1이다. TEST만 적으면 ITEST=30이다. ITRACE 생략은 기존 값을 유지한다. 문서는 두 생략 조건을 구분하지 않는다. |
| R6:O-090 | 분할 출력 수·NOSWLL | swanuse PDF 114쪽 / 인쇄 106쪽: `There will be at most 10 partitions.` QUANTITY 문법에는 NOSWLL이 없다. | `src/swanmain.ftn:3529` `OUTPAR(51) = 5.`. `src/swanpre1.ftn:2256` `CALL INREAL ('NOSWLL', QR(10), 'STA', -999. )`. `src/swanout1.ftn:4818` `NOSWLL = INT(OUTPAR(51))`. `src/swanout1.ftn:4828` `NP = MIN(NP,10)`. | C 문서 누락 | 기본 출력 열은 풍파 1개와 너울 5개이다. 최대 10개라는 제한과 기본 6개를 구분해야 한다. 숨은 NOSWLL 입력은 출력할 너울 수를 바꾼다. |
| R6:O-118 | swan.edt의 출력 문법 완전성 | swanuse PDF 135쪽 / 인쇄 127쪽: `all the commands that can be used with SWAN are specified.` swanuse PDF 142쪽 / 인쇄 134쪽의 TABLE에도 `([unit])`가 있다. | `misc/swan.edt:319` `!             ([unit]) (OUTPUT [tbegtbl] [delttbl] SEC\|MIN\|HR\|DAY)`. `src/swanpre2.ftn:1796` `CALL MSGERR (1, 'UNIT is ignored in this version')`. `src/swanmain.ftn:2146` `OVKEYW(IVTYPE) = 'PER'`. `src/swanmain.ftn:2158` `OVKEYW(IVTYPE) = 'RPER'`. `src/swanmain.ftn:2326` `OVKEYW(IVTYPE) = 'DISV'`. `src/swanmain.ftn:2578` `OVKEYW(IVTYPE)  = 'HICE'`. | B 문서 오기 | swan.edt는 TABLE UNIT을 적지만 구현은 무시한다. 물리량 목록에는 PER·RPER·DISVEG·HICE가 없고 TABLE 목록에는 NPLANTS도 없다. |
| R6:O-119 | 권고·해석·예제 | swanuse PDF 119쪽 / 인쇄 111쪽: `[itest] should be set to 1`은 timing 출력을 위한 권고이다. swanuse PDF 127쪽 / 인쇄 119쪽: BFI는 `quantify the probability of freak waves`에 쓸 수 있다고 한다. swanuse PDF 145–149쪽 / 인쇄 137–141쪽은 example 파일이다. | `src/swanout1.ftn:4769` `VOQ(IP,VOQR(IVTYPE)) = SQRT(PI2)*STPNS*QP`는 BFI 산식만 구현한다. `src/swanpre1.ftn:582`의 TEST 기본 인수는 30이다. | H 코드 대조 대상 아님 | 권고한 TEST 수준은 기본값과 별개이다. BFI의 확률 설명은 출력 코드의 보정확률 구현 주장이 아니다. 예제의 점 수·bin 수·밀도 숫자는 기본값 또는 실행 검증 결과로 해석하지 않는다. |
| R6:O-130 | OUTE | 네 매뉴얼과 웹 원문에서 검색 0건. | `src/swanpre1.ftn:651` `!     OUTE [itest]         (NOT documented)`. `src/swanpre1.ftn:656` `CALL ININTG ('ITEST' , IOUTES , 'STA', 30)`. | C 문서 누락 | 출력 루틴 진단 수준 IOUTES를 별도로 지정한다. 인수를 생략하면 30이다. TEST의 ITEST와 구분한다. |
| R6:O-132 | 이전 명령 별칭 | PPER·DTM·FWID·FS1D·SFD 출력 명세 없음. QUANTITY 문법은 PROBLEMCOORD와 FRAME만 제시한다. | `src/swanpre2.ftn:2463` `IF (KEYWIS ('PPER')) IVTYPE = 12`. `src/swanpre2.ftn:2465` `IF (KEYWIS ( 'DTM')) IVTYPE = 31`. `src/swanpre2.ftn:2466` `IF (KEYWIS ('FWID')) IVTYPE = 33`. `src/swanpre2.ftn:1885` `IF (KEYWIS ('FS1D') .OR. KEYWIS('SPEC1D')) THEN`. `src/swanpre2.ftn:1888` `CALL IGNORE ('SFD')`. `src/swanpre1.ftn:2258` `IF (KEYWIS('PROBLEM') .OR. KEYWIS('USER')) THEN`. | C 문서 누락 | PPER는 RTP이다. DTM은 DRTM01이다. FWID는 FSPR이다. FS1D는 SPEC1D의 별칭이다. SFD는 SPEC2D 경로에서 소비한다. USER는 PROBLEMCOORD의 별칭이다. TABLE의 FIL·PAP 별칭은 swanpre2 1589·1599행에서 받는다. |
| R6:O-135 | 요청 수 상한·공유 QUANTITY 상태 | swanuse PDF 104쪽 / 인쇄 96쪽은 PER의 [power]가 RPER에도 영향을 준다고 명시한다. 공식 변경 이력 609–610행은 출력 요청 상한 250을 명시한다. | `src/swmod2.ftn:205` `INTEGER, PARAMETER :: MAX_OUTP_REQ = 250 ! max. number of output requests`. `src/swanpre2.ftn:1585` `IF (NREOQ.GT.MAX_OUTP_REQ) CALL MSGERR (2,`. `src/swanpre1.ftn:2316` `OUTPAR(4) = QR(7)`. [공식 변경 이력](../raw/manuals/website/modifications/modifications.htm) 609행: `Maximum number of output requests increased from 50 to 250.` `src/swanpre1.ftn:2285–2286`은 PER·RPER의 OUTPAR(2) 공유를 구현한다. | C 문서 누락 | 출력 요청 상한 250은 공식 변경 이력과 일치한다. PER·RPER의 지수 공유는 swanuse PDF 104쪽와 일치한다. C는 기준 좌표가 물리량별 상태가 아니라 공통 OUTPAR(4)에 저장된다는 설명의 누락에 한정한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R6:N-001 | RAY의 의미 | `models/SWAN/manual-notes/swan-command-numerics-output-reference.md:58`: `! wave ray`<br>swanuse PDF 99쪽 / 인쇄 91쪽: `RAY ’rname’ [xp1] [yp1] [xq1] [yq1] < [int] [xp] [yp] [xq] [yq] >`. `by linear interpolation of the start and end positions`. | `src/swanpre2.ftn:650` `TMP%X  = XP1 + REAL(JJ)*(XP-XP1)/REAL(INTD)`. `src/swanpre2.ftn:652` `TMP%XQ = XQ1 + REAL(JJ)*(XQ-XQ1)/REAL(INTD)`. `src/swanpre2.ftn:611` `IF (ONED) THEN`. | B 문서 오기 | RAY는 ISOLINE과 교차시킬 직선 집합을 정의한다. 굴절에 따른 파향선을 계산하는 명령이 아니다. |
| R6:N-002 | 출력 선택자·QUANTITY 속성 | `models/SWAN/manual-notes/swan-command-numerics-output-reference.md:67`: `변수 속성(단위·기준·hexp 등)`. 74행: `WFORCE`, `OUT`(time). | `src/swanmain.ftn:1880` `OVKEYW(IVTYPE) = 'FOR'`. `src/swanmain.ftn:1881` `OVSNAM(IVTYPE) = 'WForce'`. `src/swanpre2.ftn:2468` `IF (KEYWIS ('OUT')) IVTYPE = 98`. | B 문서 오기 | QUANTITY는 이름·표시 범위·예외값·정의 인수·기준 좌표를 바꾼다. 단위 문자열 입력 기능은 없다. FORCE가 명령 선택자이다. WForce는 기본 짧은 이름이다. TIME은 시각 출력 물리량이다. OUT은 출력 시각 옵션의 시작이다. |
| R6:N-003 | SPECOUT 요약 문법 | `models/SWAN/manual-notes/swan-command-numerics-output-reference.md:71`: `SPECout 'sname' <SPEC1D\|SPEC2D> <ABS\|REL> 'fname' (OUTPUT ...)`<br>swanuse PDF 116–117쪽 / 인쇄 108–109쪽: 기본 SPEC2D, ABS, S. S는 infragravity 경계 위이다. L은 경계 아래이다. | swanuse PDF 116–117쪽 / 인쇄 108–109쪽의 S/L. `src/swanpre2.ftn:1899` `CALL INKEYW ('STA', 'S')`. | C 문서 누락 | SPECOUT 문법에 ABS/REL 뒤의 S/L을 추가한다. 기본값은 S이다. L은 surfbeat의 낮은 주파수 출력을 선택한다. |
| R8:T1-001 | COMPUTE 뒤 명령 | swanuse PDF 33쪽·인쇄 25쪽: “all commands after COMPUTE are ignored by SWAN, except HOTFILE and STOP”. 같은 책 PDF 120쪽·인쇄 112쪽은 “In the case MODE NONSTATIONARY several commands COMPUTE can appear” 및 “unless a command INIT appears in between the two COMPUTE commands”라고 적는다. 웹 `website/online_doc/swanuse/node21.html:53–54`와 `node34.html:102–104`도 같은 두 설명을 싣는다 | `src/swanmain.ftn:394–399`, `src/swanmain.ftn:703`의 명령 반복은 `CALL SWREAD (COMPUT)`를 다시 호출한다. `src/swanpre1.ftn:939` `RETURN`은 COMPUTE 처리를 끝낸다. `src/swanpre1.ftn:1309–1312`의 `IF (KEYWIS ('INIT')) THEN`, `CALL INITVA( AC2, SPCSIG, SPCDIR, KGRPNT )`, `GO TO 100`은 INITIAL을 처리한다. | B 문서 오기 | COMPUTE를 마친 SWMAIN은 SWREAD를 다시 호출한다. 사용자 매뉴얼의 MODE NONSTATIONARY 다중 COMPUTE·중간 INIT 설명은 코드와 일치한다. 같은 매뉴얼의 COMPUTE 뒤 명령을 모두 무시한다는 문장은 이 동작과 충돌한다. [10-13 결론 검증 보완] |
| R8:T1-013 | 비정상 시간 간격·반복 권고 | swanuse PDF 121쪽·인쇄 113쪽: “For a nonstationary computation, a time step of at most 10 minutes is advised.” 이어지는 권고는 “For a sufficiently small time step (≤ 10 minutes), no more than 1 iteration per time step is recommended”이다 | `src/swanpre1.ftn:903` `CALL INITVD ('DELTC', DT, 'REQ', 0D0)`; `src/swanpre1.ftn:1959` `CALL ININTG ('MXITNS' , MXITNS   , 'REQ', 0 )`; `src/swanpre1.ftn:935` `ITERMX = MXITNS`. 비정렬·정렬 루프는 T1-007의 ITERMX를 쓴다. | H 코드 대조 대상 아님 | 사용자 매뉴얼은 비정상 계산에 10분 이하 시간 간격을 권고한다. 시간 단계당 반복을 1회보다 많이 하지 말라는 권고는 충분히 작은 시간 간격(≤ 10 minutes)을 전제로 한다. 이 문장들은 DT 또는 MXITNS의 강제 상한이 아니다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R5:PN-152 | NUMERIC FIL | — | `src/swanpre1.ftn:2039` `ELSE IF (KEYWIS ('FIL')) THEN`; `src/swanpre1.ftn:2041` `PNUMS(8) = 3.`; `src/swanpre1.ftn:2042` `CALL INREAL ('DIFFC'  , PNUMS(9), 'UNC', 0.)`; `src/swanmain.ftn:1239` `PNUMS(9) = 0.01`; `src/swancom1.ftn:3702` `ELSE IF (INT(PNUMS(8)).EQ.2 .OR. INT(PNUMS(8)).EQ.3) THEN`; `src/swancom1.ftn:3709` `CALL SOLMT1  (IDCMIN             ,IDCMAX             ,`. | C 문서 누락 | NUMERIC FIL은 PNUMS(8)=3을 설정하고 DIFFC를 읽는다. SOLMT1 호출은 SIGEX와 공유한다. 전체 소스의 PNUMS(9) 참조는 초기 대입·입력·주석뿐이므로 DIFFC의 실제 필터 효과로 설명하지 않는다. [10-13 결론 검증 보완] [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-156 | CDLIM | 웹 `website/modifications/modifications.htm:1227`의 `cdlim removed`는 41.01 아래 patch B 기록이다. | `src/swanpre1.ftn:1988` `CALL INREAL ('CDLIM'  , PNUMS(17), 'STA',-1.)`; `src/swanpre1.ftn:1989` `IF (PNUMS(17).LT.0.) IREFR = 1`; `src/swanpre1.ftn:1990` `IF (EQREAL(PNUMS(17),0.)) THEN`; `src/swanpre1.ftn:1991` `IREFR = 0`. | C 문서 누락 | 옛 수치 제한 제거 기록과 별개로 CDLIM 입력은 남아 있다. 0은 굴절을 끈다. 음수는 굴절을 켠다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R7:ED-040 | NUMERIC | `misc/swan.edt:250` `!   NUMeric (<                                                           >  &`; `misc/swan.edt:261` `!              \| -> SIGIMpl [css] [eps2] [outp] [niter]`; `website/online_doc/swanuse/node49.html:305`은 STOPC 행을 싣는다. | `src/swanpre1.ftn:2028` `CALL INREAL ('EPS1' , PNUMS(11), 'UNC', 0.)`; `src/swanpre1.ftn:1942` `IF (KEYWIS ('STOPC')) THEN`; 2027–2031행은 CSS·EPS1·EPS2·OUTP·NITER를 순서대로 읽는다. | C 문서 누락 | 로컬 swan.edt:250–269에는 STOPC가 없다. 웹 swanuse node49:305와 NUMERIC 본문 node29에는 STOPC가 있다. 따라서 STOPC 누락은 로컬 편집 파일에 한정한다. 로컬 파일과 웹 구문표의 SIGIMPL에는 EPS1이 없지만 판독기는 CSS 다음 EPS1을 읽는다. 기존의 STOPC가 있다는 문장을 정정한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:ED-043 | QUANTITY | `misc/swan.edt:290` `!   QUANTity  <     >   'short'  'long'  [lexp]  [hexp]  [excv]             &`; `misc/swan.edt:293–296`과 `website/online_doc/swanuse/node32.html:91–109`의 QUANTITY 구문 | `src/swanpre1.ftn:2256` `CALL INREAL ('NOSWLL', QR(10), 'STA', -999. )                 41.72`; `src/swanpre1.ftn:2254–2256`은 FMIN·FMAX·NOSWLL 순서로 읽는다. `src/swanpre1.ftn:2291–2295`에서는 해당 IVTYPE일 때 `IF (QR(10).NE.-999.) OUTPAR(51) = QR(10)`을 적용한다. | C 문서 누락 | C는 swan.edt와 swanuse QUANTITY 구문표의 NOSWLL 누락이다. 판독기는 FMAX 다음에 `CALL INREAL ('NOSWLL', QR(10), 'STA', -999. )`를 호출한다. 코드에서 기본값 -999.는 속성 갱신 여부를 구분하는 값이다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:ED-044 | OUTPUT OPTIONS | `misc/swan.edt:298` `!   OUTPut OPTIons  'comment'  (TABle [field])  (BLOck  [ndec]  [len])      &`; `website/online_doc/swanuse/node32.html:442` `(SPEC [ndec])` | `src/swanpre1.ftn:696` `CALL ININTG ('LEN', NLEN, 'STA', 200)`; `src/swanpre1.ftn:693–706`에서 SPEC은 NDEC 다음 LEN을 읽는다. `IF (KEYWIS('QUA')) THEN`은 `command OUTP QUANT is obsolete, use QUANTITY`라는 심각도 3 메시지를 낸다. | C 문서 누락 | C는 편집 파일과 swanuse OUTPUT OPTIONS 구문표가 SPEC의 LEN을 생략한 부분이다. OUTPUT QUANTITY는 폐기 안내 오류 분기이다. 이를 문서에 추가할 지원 옵션처럼 적은 기존 결론은 삭제한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:ED-045 | BLOCK·TABLE 출력량 | `misc/swan.edt:301` `!   BLOCK   'sname'  HEADER \| NOHEADER  'fname' (LAY-OUT [idla])            &`; `misc/swan.edt:305,311–319`; `website/online_doc/swanuse/node32.html:628,1466–1467`은 NPLANTS를 출력량으로 적는다. | `src/swanpre2.ftn:2457` `IF (KEYWIS (OVKEYW(IVT))) THEN                                    40.00`; `src/swanpre2.ftn:1260,1634`의 BLOCK·TABLE 판독기는 모두 `CALL SVARTP (IVTYPE)`를 호출한다. | C 문서 누락 | C는 swan.edt의 TABLE 출력량 목록에 한정한다. 그 목록에는 BLOCK 목록의 NPLANT가 없지만 swanuse 공통 출력량 목록에는 NPLANTS가 있다. 두 명령의 공통 SVARTP 검색에 TABLE만의 NPLANT 제외 조건은 없다. netCDF 등 출력 형식별 검사는 별도 분기이다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:ED-046 | SPECOUT | `misc/swan.edt:321` `!   SPECout 'sname'  SPEC1D\|SPEC2D  ABS\|REL  S\|L  'fname'                   &` | `src/swanpre2.ftn:1930` `!NCF        IF (KEYWIS('MON')) THEN                                           41.40`; `src/swanpre2.ftn:1938–1947`에는 !NCF 표시의 COMP·MDGRID·NOAUX 분기가 있다. `switch.pl:102`은 -netcdf일 때 !NCF를 제거한다. | C 문서 누락 | 편집 파일에는 MONth·ESCAle·COMPress가 있다. 이 분기와 MDGRID·NOAUX는 !NCF를 제거한 netCDF 빌드에서만 활성화된다. C는 편집 파일의 빌드 조건과 MDGRID·NOAUX 누락이다. 네 매뉴얼 판독 기록과 웹 문서에서도 MDGRID·NOAUX 설명은 검색되지 않는다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:ED-052 | QUANTITY POWER·REF 순서 | `misc/swan.edt:293` `!             [power]   [ref]   [fswell]    [fmin]  [fmax]                  &`; `website/online_doc/swanuse/node32.html:96–100`은 POWER를 PER·RPER·WLEN용, REF를 TSEC용으로 구분한다. | `src/swanpre1.ftn:2250` `CALL INCTIM (ITMOPT, 'REF', DVAL, 'STA', -9.99D2)             40.87`; `src/swanpre1.ftn:2252` `CALL INREAL ('POWER', QR(5) , 'STA', -999.)` | B 문서·노트 오기 | 편집 파일의 평면 구문표는 POWER 다음 REF를 적지만 판독기는 REF 다음 POWER를 읽는다. B는 위치 인자 순서에 한정한다. swanuse 본문은 각 인자가 적용되는 출력량을 따로 구분하므로 두 인자가 모든 출력량에 함께 적용된다고 쓰지 않는다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |

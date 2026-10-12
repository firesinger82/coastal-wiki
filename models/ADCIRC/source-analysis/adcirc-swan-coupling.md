---
title: "adcirc swan coupling"
topic: general
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-swan-coupling.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. **SWAN Temporal Controls (PR #498) 절 추가 (2026-05-28)**: GitHub API `gh pr view 498 -R adcirc/adcirc` + `gh pr diff 498` 직접 fetch — PR body verbatim 인용 (SWANTimeControl namelist + RunStartDateTime + fort.26 COMPUTE 카드) + presizes.F / prep.F / couple2swan.F diff hunk 직접 인용 (SwanTimeStep offset 계산 + [1, SWAN_MTC] range gate + sentinel/radiation-stress fallback)."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23 + SWAN Temporal Controls 절 2026-05-28"
note_date: 2026-04~05 (original) / 2026-05-23 (promote) / 2026-05-28 (PR #498 절)
verification_by: "사용자 + codex source-code analysis + Claude Opus 4.7 (1M context) — PR #498 GitHub API 직접 fetch"
verification_date: 2026-04 (base) / 2026-05-28 (PR #498)
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

## Scope

How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

## Source basis

- `couple2swan.F:67-1313` — main coupling module: init, run, finalize, RS computation.
- `driver.F:30-57` — `CSWAN` driver entry/finalize.
- `adcirc.F:428-483` — main loop coupling call.
- `read_input.F:1094-1097, 1790-1817, 2255-2261` — `NRS` parsing and encoding.
- `wind.F:52-60` — allowable NWS table.
- `timestep.F:668-686, 695-725, 1214-1218` — wind passing, RS interpolation, hotfile timing.
- `hstart.F:325-337`, `write_output.F:5058-5201`, `netcdfio.F90:5555-7045, 8017-8085` — hot-start.
- `../thirdparty/swan/SwanReadADCGrid.ftn90:44-158` — SWAN reads `fort.14`.
- `../thirdparty/swan/swanmain.ftn:895-902, 8696-8983` — SWAN-side coupling hooks.
- `../work/makefile:195-663` — build targets.

## A. Entry points

| Routine | Purpose | Lines |
|---|---|---|
| `PADCSWAN_INIT` | Initialize SWAN, exchange grids/initial state | `couple2swan.F:947` |
| `PADCSWAN_RUN(ITIME)` | Per-coupling-step SWAN run + RS update | `:1110` |
| `PADCSWAN_FINAL` | Cleanup | `:1313` |
| `ComputeRadiationStresses` | Integrate SWAN spectra to RS components | `couple2swan.F:112` |
| `ComputeWaveDrivenForces` | Convert RS gradients to nodal forces | `couple2swan.F:210` |

Driver glue (`driver.F:30-57`): imports `CSWAN` driver, calls `PADCSWAN_INIT` then `PADCSWAN_FINAL`.

Time-loop call (`adcirc.F:428-483`):
```
if (mod(ITIME, CouplingInterval) == 0) call PADCSWAN_RUN(ITIME)
```

SWAN-side hooks activated by `switch.pl -adcirc` — only present in coupled binary (`makefile:232-233, 558-560`).

## B. Time stepping

- ADCIRC runs every `DT`; SWAN `DT` imported as `SWAN_DT` (`couple2swan.F:950, 965`).
- **Coupling interval = integer ratio** `SWAN_DT / DT` (`:1103-1105`).
- ADCIRC calls SWAN only on that interval (`adcirc.F:475-483`).
- 이번 단계의 `PADCSWAN_RUN`은 TIMESTEP 뒤에 있다. (`src/adcirc.F:476` `CALL TIMESTEP(ITIME,TimeLoc)`; `src/adcirc.F:481` `IF(MOD(ITIME,CouplingInterval).EQ.0)THEN`; `src/adcirc.F:482` `CALL PADCSWAN_RUN(ITIME)`)
- During SWAN run, interpolation midpoint used for time-centering (`couple2swan.F:1241-1243`); `SWMAIN` 호출은 temporal control gate 안(`:1245-1247`).

**Note**: there is **no `CWTIM_INC` symbol** in this tree; coupling interval comes from SWAN `TIMECOMM:DT` block divided by ADCIRC `DT`.

## C. SWAN → ADCIRC (radiation stress)

1. SWAN spectra integrated into `ADCIRC_SXX/SXY/SYY` (`couple2swan.F:112-119, 177-196`).
2. <a id="swan-force-average"></a>SWAN 파력의 요소 누적식은 방사 응력의 음의 발산을 면적으로 가중한다. (`src/couple2swan.F:399` `SWAN_RSNX2(IP) = SWAN_RSNX2(IP) + 0.5d0*AREAS(NEITABELE(IP,IE))`; `src/couple2swan.F:400` `&                     * ( - DSXXDX(NEITABELE(IP,IE))`; `src/couple2swan.F:401` `&                         - DSXYDY(NEITABELE(IP,IE)) )`; `src/couple2swan.F:402` `SWAN_RSNY2(IP) = SWAN_RSNY2(IP) + 0.5d0*AREAS(NEITABELE(IP,IE))`; `src/couple2swan.F:403` `&                     * ( - DSXYDX(NEITABELE(IP,IE))`; `src/couple2swan.F:404` `&                         - DSYYDY(NEITABELE(IP,IE)) )`) [10-12 전수 검증 보완] `IF(Marcel.AND.(NCELE.EQ.0))THEN`은 해당 절점의 누적을 중단한다. (`src/couple2swan.F:389` `IF(Marcel.AND.(NCELE.EQ.0))THEN`; `src/couple2swan.F:391` `RSNX2(IP) = 0.0d0`; `src/couple2swan.F:392` `RSNY2(IP) = 0.0d0`; `src/couple2swan.F:393` `CYCLE outer`) [10-12 전수 검증 보완] 누적을 마친 절점에서는 TOTALAREA로 나눈다. (`src/couple2swan.F:421` `SWAN_RSNX2(IP) = SWAN_RSNX2(IP) / TOTALAREA`; `src/couple2swan.F:422` `SWAN_RSNY2(IP) = SWAN_RSNY2(IP) / TOTALAREA`) [10-12 전수 검증 보완] 그 뒤 두 성분에 UL을 이용한 상하한 제한을 적용한다. (`src/couple2swan.F:426` `SWAN_RSNX2(IP) = min(UL,max(-UL,SWAN_RSNX2(IP)))`; `src/couple2swan.F:427` `SWAN_RSNY2(IP) = min(UL,max(-UL,SWAN_RSNY2(IP)))`) [10-12 전수 검증 보완] `IF(Marcel)THEN`에서는 수위·유량 경계 절점의 SWAN 파력을 0으로 설정한다. (`src/couple2swan.F:432` `IF(Marcel)THEN`; `src/couple2swan.F:435` `SWAN_RSNX2(NBDV(K,I)) = 0.0d0`; `src/couple2swan.F:436` `SWAN_RSNY2(NBDV(K,I)) = 0.0d0`; `src/couple2swan.F:441` `SWAN_RSNX2(NBVV(K,I)) = 0.0d0`; `src/couple2swan.F:442` `SWAN_RSNY2(NBVV(K,I)) = 0.0d0`) [10-12 전수 검증 보완] [10-12 결론 검증 보완]
   - SWANOutputControl은 현재 일곱 출력의 on/off를 제어한다. (`src/read_input.F:456` `namelistSpecifier = 'SWANOutputControl'`; `src/read_input.F:457` `read(unit=15,nml=SWANOutputControl,iostat=ios,iomsg=ios_nml_error_msg)`; `src/couple2swan.F:746` `SWAN_OutputAgg(1) = SWAN_OutputHS`; `src/couple2swan.F:747` `SWAN_OutputAgg(2) = SWAN_OutputDIR`; `src/couple2swan.F:748` `SWAN_OutputAgg(3) = SWAN_OutputTM01`; `src/couple2swan.F:749` `SWAN_OutputAgg(4) = SWAN_OutputTPS`; `src/couple2swan.F:750` `SWAN_OutputAgg(5) = SWAN_OutputWIND`; `src/couple2swan.F:751` `SWAN_OutputAgg(6) = SWAN_OutputTM02`; `src/couple2swan.F:752` `SWAN_OutputAgg(7) = SWAN_OutputTMM10`; `src/couple2swan.F:770` `IF(.NOT.SWAN_OutputAgg(IW))CYCLE`)
   - 현재 등록한 출력은 HS·DIR·TM01·TPS·WIND·TM02·TMM10이다. (`src/couple2swan.F:727` `Names(1) = "HS"`; `src/couple2swan.F:728` `Names(2) = "DIR"`; `src/couple2swan.F:729` `Names(3) = "TM01"`; `src/couple2swan.F:730` `Names(4) = "TPS"`; `src/couple2swan.F:731` `Names(5) = "WIND"`; `src/couple2swan.F:732` `Names(6) = "TM02"`; `src/couple2swan.F:733` `Names(7) = "TMM10"`)
   - 새 출력의 추가는 couple2swan.F 등록과 GLOBAL 집계 플래그 및 입력 제어와 출력 descriptor를 함께 확인한다. (`src/global.F:318` `LOGICAL                      :: SWAN_OutputAgg(7)`; `src/couple2swan.F:725` `IF(.NOT.ALLOCATED(IGSW))  ALLOCATE(IGSW(1:NumSwanOutput))`; `src/couple2swan.F:727` `Names(1) = "HS"`; `src/read_input.F:457` `read(unit=15,nml=SWANOutputControl,iostat=ios,iomsg=ios_nml_error_msg)`)
   - 문서의 only four 제한은 현재 일곱 항목 등록과 다르다. (`docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:163` `existing SWAN output that you'd like to modify. Keep in mind that you only have`; `docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:164` `four existing files to work with here, so that is ultimately your limit on`; `docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:165` `output parameters as well. You may want to consider renaming your output files`; `src/couple2swan.F:727` `Names(1) = "HS"`; `src/couple2swan.F:733` `Names(7) = "TMM10"`)
   - 출력 파일명은 write_output.F와 couple2swan.F 두 위치에 있다. (`src/write_output.F:5884` `SwanHSDescript % file_basename        = "swan_HS"`; `src/couple2swan.F:735` `FileName(1) = "swan_"//TRIM(Names(1))//".63"//"       "`)
3. ADCIRC extrapolates/interpolates into `RSNX2/RSNY2` for `NRS=3` (`timestep.F:699-707`).
4. <a id="swan-force-momentum"></a>SWAN 파력을 읽는 경로는 `#ifdef CSWAN` 안의 `ELSEIF(NRS==3) THEN`이다. (`src/timestep.F:699` `#ifdef CSWAN`; `src/timestep.F:701` `ELSEIF(NRS==3) THEN`; `src/timestep.F:703` `CALL ComputeWaveDrivenForces()`) [10-12 전수 검증 보완] `IF (Limit_WaveStressGrad.eqv..false.) then`에서는 ramp와 시간 보간을 적용한 RSX·RSY를 풍응력 항에 더한다. (`src/timestep.F:724` `IF (Limit_WaveStressGrad.eqv..false.) then`; `src/timestep.F:726` `RSX = RampWRad*(RSNX1(I) + RStRatio*(RSNX2(I)-RSNX1(I)))`; `src/timestep.F:727` `RSY = RampWRad*(RSNY1(I) + RStRatio*(RSNY2(I)-RSNY1(I)))`; `src/timestep.F:728` `WSX2(I) = WSX2(I) + RSX`; `src/timestep.F:729` `WSY2(I) = WSY2(I) + RSY`) [10-12 전수 검증 보완] 그 `ELSE`에서 파력 크기가 WaveStressGrad_Cap보다 크고 0보다 클 때만 크기를 제한한다. (`src/timestep.F:738` `ELSE !test and limit wave stress`; `src/timestep.F:743` `IF ((RSXYMAG .gt. WaveStressGrad_Cap ).and.`; `src/timestep.F:744` `&               (RSXYMAG.gt.0.0d0)) then`; `src/timestep.F:745` `RSSCALE = WaveStressGrad_Cap/RSXYMAG`; `src/timestep.F:746` `RSXLIM = RSX*RSSCALE`; `src/timestep.F:747` `RSYLIM = RSY*RSSCALE`) [10-12 전수 검증 보완] 그 제한 검사의 `ELSE`에서는 원래 RSX·RSY를 유지한다. (`src/timestep.F:748` `ELSE`; `src/timestep.F:749` `RSXLIM = RSX`; `src/timestep.F:750` `RSYLIM = RSY`) [10-12 전수 검증 보완] 제한 분기는 RSXLIM·RSYLIM을 풍응력 항에 더한다. (`src/timestep.F:752` `WSX2(I) = WSX2(I) + RSXLIM`; `src/timestep.F:753` `WSY2(I) = WSY2(I) + RSYLIM`) [10-12 전수 검증 보완] [10-12 결론 검증 보완]
1999_Luettich02.pdf는 Rx·Ry를 양의 발산으로 정의하고 운동량 우변에 더한다. (`raw/manuals/pdfs/1999_Luettich02.pdf, PDF 쪽 3 / 인쇄 쪽 2`)

1999년 문서와 v56.2.1 코드의 부호 차이를 기록한다. 어느 쪽이 맞는지는 이 대조에서 단정하지 않는다.


([features 보고서 §5 R01 (240줄)<br>R02 (241줄)<br>C34 (683줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 파랑 방사 응력 발산의 부호) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich02.pdf/p001-010.md` PDF 3쪽 / 인쇄 2쪽: `R_x=\frac{1}{\rho_o}\left[\frac{\partial S_{xx}}{\partial x}+\frac{\partial S_{xy}}{\partial y}\right]` (LaTeX 전사)<br>src/couple2swan.F:399 `SWAN_RSNX2(IP) = SWAN_RSNX2(IP) + 0.5d0*AREAS(NEITABELE(IP,IE))`<br>src/couple2swan.F:400 `&                     * ( - DSXXDX(NEITABELE(IP,IE))`<br>src/couple2swan.F:401 `&                         - DSXYDY(NEITABELE(IP,IE)) )`<br>src/couple2swan.F:421 `SWAN_RSNX2(IP) = SWAN_RSNX2(IP) / TOTALAREA`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich02.pdf/p001-010.md` PDF 3쪽 / 인쇄 2쪽: `R_y=\frac{1}{\rho_o}\left[\frac{\partial S_{xy}}{\partial x}+\frac{\partial S_{yy}}{\partial y}\right]` (LaTeX 전사)<br>src/couple2swan.F:402 `SWAN_RSNY2(IP) = SWAN_RSNY2(IP) + 0.5d0*AREAS(NEITABELE(IP,IE))`<br>src/couple2swan.F:403 `&                     * ( - DSXYDX(NEITABELE(IP,IE))`<br>src/couple2swan.F:404 `&                         - DSYYDY(NEITABELE(IP,IE)) )`<br>src/couple2swan.F:422 `SWAN_RSNY2(IP) = SWAN_RSNY2(IP) / TOTALAREA`<br>src/couple2swan.F:189 `!Casey 080602: ADCIRC accepts wave-driven stresses "in units of velocity squared`<br>해석: v34.12의 1999년 PDF는 양의 발산을 운동량 우변에 더한다. 현재 SWAN 결합 경로와 구판 외부 강제력 정의를 같은 식으로 인용할 수 없다. 이 분류는 구판 코드가 실제로 양의 발산을 계산했다는 주장이 아니다. 결론: 판 차이. v56.2.1의 SWAN 결합은 방사 응력의 음의 발산을 풍응력에 더한다.
([features 보고서 §5 R13 (252줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: SWAN POINTS·TABLE 명령과 내부 표기) 근거: docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:20은 `POINTS 'aStringIdForPointsFile' FILE 'theFileNameOfYourPointsFile'`를 제시한다. 32–38줄은 TABLE의 출력 변수와 OUT 뒤의 시작 시각·간격을 설명한다.<br>추가 원문: thirdparty/swan/swanpre2.ftn:536–550의 `IF (KEYWIS ('POIN')) THEN`, `OPSTMP%PSTYPE = 'P'`, `IF (KEYWIS('FILE')) THEN`, `CALL FOR (NDS, FILENM, 'OF', IOSTAT)`는 이름 있는 점 파일을 읽는다. 562줄: `CALL REFIXY (NDS, XP, YP, IERR)`.<br>thirdparty/swan/swanpre2.ftn:1577: `IF (KEYWIS ('TAB')) THEN`. 1588–1600줄은 HEADER를 `RTYPE = 'TABP'`로 처리한다. NOHEADER는 `RTYPE = 'TABD'`로 처리한다. 1838–1839줄: `CALL INCTIM (ITMOPT, 'TBEG', ORQTMP%OQR(1), 'REQ', 0D0)` / `CALL INITVD ('DELT', ORQTMP%OQR(2), 'REQ', 0D0)`.<br>thirdparty/swan/swanout2.ftn:1415–1426은 TABP의 머리말을 쓴다. 1589–1601줄은 TABD와 TABP의 수치 출력 형식을 나눈다.<br>추가 검색: raw와 판독 기록 전체에서 `POINTS`, `NOHEADER`, `KEYWIS.*TAB`, `IVTYPE.*98`, `SWTABP`를 검색했다.<br>해석: 문서의 POINTS·TABLE·HEADER·NOHEADER는 SWAN 파서의 POIN·TAB·TABP·TABD와 대응한다. ADCIRC의 전역 파랑 출력 변수명과 비교한 기존 미확인은 서로 다른 출력 경로의 표기 비교였다. 병렬 파일 배치의 판정은 R14로 분리한다. 결론: 표기 차이. SWAN의 POINTS·TABLE 명령과 내부 출력 유형명은 같은 입력·출력 경로의 표기 차이이다. [10-12 G 재판정]
([features 보고서 §5 R14 (253줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: SWAN TABLE의 실제 병렬 출력 위치) 근거: 문서 원문: `docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:54` `-  In a parallel run, for model versions later than roughly ADCIRC version v52,`<br>`docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:55` `the output should be a single file in the main run directory. In earlier`<br>`docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:56` `versions, the output was written individually by each subdomain to its PE\*`<br>`docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:57` `folder.`<br>코드 원문: `cmake/helper_functions.cmake:64` `COMMAND ${PERL_EXECUTABLE} switch.pl -pun -adcirc -unix -outdir`<br>`cmake/helper_functions.cmake:65` `${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/swan_parallel_source *.ftn *.ftn90`<br>`thirdparty/swan/switch.pl:98` `if ($pun=~/TRUE/) {$newline=~s/^!PUN//;}`<br>`thirdparty/swan/swanpre2.ftn:1616` `IF ( PARLL ) THEN                                               40.30`<br>`thirdparty/swan/swanpre2.ftn:1617` `ILPOS = INDEX ( FILENM, ' ' )-1                              40.30`<br>`thirdparty/swan/swanpre2.ftn:1618` `WRITE(FILENM(ILPOS+1:ILPOS+4),33) INODE                      40.30`<br>`thirdparty/swan/swanpre2.ftn:1619` `END IF                                                          40.30`<br>`thirdparty/swan/swanpre2.ftn:1620` `!PUN          FILENM = TRIM(LOCALDIR)//DIRCH2//TRIM(FILENM)                   40.95`<br>`src/sizes.F:359` `WRITE(LOCALDIR,'(2A)') TRIM(ROOTDIR),TRIM(PREFIX(iprefix))`<br>`src/sizes.F:360` `LNAME = LEN_TRIM(LOCALDIR)`<br>`src/sizes.F:361` `WRITE(LOCALDIR(LNAME-3:LNAME),'(I4.4)') MYPROC`<br>`thirdparty/swan/swanout2.ftn:1400` `FILENM = OUTP_FILES(OQI(2))                                     40.31 40.13`<br>`thirdparty/swan/swanout2.ftn:1401` `IOSTAT = -1                                                     20.75`<br>`thirdparty/swan/swanout2.ftn:1402` `!NCF          INQUIRE(FILE=FILENM, EXIST=EXIST)`<br>`thirdparty/swan/swanout2.ftn:1403` `CALL FOR (NREF, FILENM, 'UF', IOSTAT)`<br>`thirdparty/swan/swanout2.ftn:1572` `!PUN       IF ( MNPROC.EQ.1 .OR. IONOD(IP).EQ.MYPROC ) THEN                   41.36`<br>해석: 결합 병렬 빌드의 `-pun`은 `!PUN` 접두어를 제거한다. TABLE 파일명에는 LOCALDIR가 붙는다. PARLL이 참이면 INODE도 파일명에 붙는다. 이 경로는 문서의 주 실행 디렉터리 단일 파일 설명과 다르므로 B이다. v52 전후의 변경 시점은 이 판정에 사용하지 않는다. 결론: 문서 오기. v56.2.1의 결합 병렬 SWAN TABLE 경로는 LOCALDIR 아래의 파일을 연다. [10-12 G 정리]
([features 보고서 §5 R16 (255줄)<br>R22 (261줄)<br>R24 (263줄)<br>C35 (684줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: SWAN 출력 제어와 추가 절차) 근거: docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:88 `the two methods outlined below: it will not allow you to 'define' your desired`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:89 `SWAN output in either the fort.26 file OR in namelist form at the bottom of`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:90 `fort.15. In other words, you will receive whatever outputs you hardwire into`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:91 `your source code and you cannot easily turn them on or off without again`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:92 `modifying the source code.`<br>src/read_input.F:456 `namelistSpecifier = 'SWANOutputControl'`<br>src/read_input.F:457 `read(unit=15,nml=SWANOutputControl,iostat=ios,iomsg=ios_nml_error_msg)`<br>src/couple2swan.F:746 `SWAN_OutputAgg(1) = SWAN_OutputHS`<br>src/couple2swan.F:747 `SWAN_OutputAgg(2) = SWAN_OutputDIR`<br>src/couple2swan.F:748 `SWAN_OutputAgg(3) = SWAN_OutputTM01`<br>src/couple2swan.F:749 `SWAN_OutputAgg(4) = SWAN_OutputTPS`<br>src/couple2swan.F:750 `SWAN_OutputAgg(5) = SWAN_OutputWIND`<br>src/couple2swan.F:751 `SWAN_OutputAgg(6) = SWAN_OutputTM02`<br>src/couple2swan.F:752 `SWAN_OutputAgg(7) = SWAN_OutputTMM10`<br>src/couple2swan.F:770 `IF(.NOT.SWAN_OutputAgg(IW))CYCLE`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:163 `existing SWAN output that you'd like to modify. Keep in mind that you only have`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:164 `four existing files to work with here, so that is ultimately your limit on`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:165 `output parameters as well. You may want to consider renaming your output files`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:168 `consider renaming swan_DIR.63 to swan_PDIR.63. If you need more than four output`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:169 `parameters and also want to change the filenames, see Method 2 below.`<br>src/couple2swan.F:727 `Names(1) = "HS"`<br>src/couple2swan.F:728 `Names(2) = "DIR"`<br>src/couple2swan.F:729 `Names(3) = "TM01"`<br>src/couple2swan.F:730 `Names(4) = "TPS"`<br>src/couple2swan.F:731 `Names(5) = "WIND"`<br>src/couple2swan.F:732 `Names(6) = "TM02"`<br>src/couple2swan.F:733 `Names(7) = "TMM10"`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:192 `#. Increment an output counter in multiple places (in my example, from 7 to 8`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:193 `because I am only adding the PDIR output)`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:195 `#. Create and insert new variable names in GLOBAL and OUTPUT blocks`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:201 `appropriate additions. Like method 1 above, your only modifications will be in`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:202 `couple2swan.F, but you will need to refer to the IVTYPE values found in`<br>src/global.F:318 `LOGICAL                      :: SWAN_OutputAgg(7)`<br>src/couple2swan.F:725 `IF(.NOT.ALLOCATED(IGSW))  ALLOCATE(IGSW(1:NumSwanOutput))`<br>src/couple2swan.F:727 `Names(1) = "HS"`<br>docs/technical_reference/input_files/fort15.rst:202 ``:ref:`&SWANOutputControl <SWANOutputControl>` :ref:`SWAN_OutputHS=logicalValue <SWANOutputControl>`, :ref:`SWAN_OutputDIR=logicalValue <SWANOutputControl>`, :ref:`SWAN_OutputTM01=logicalValue <SWANOutputControl>`, :ref:`SWAN_OutputTPS=logicalValue <SWANOutputControl>`, :ref:`SWAN_OutputWIND=logicalValue <SWANOutputControl>`, :ref:`SWAN_OutputTM02=logicalValue <SWANOutputControl>`, :ref:`SWAN_OutputTMM10=logicalValue <SWANOutputControl>` /``<br>해석: 같은 판 fort15.rst가 일곱 플래그를 제공한다. 안내문의 only four는 자기 문서의 7 to 8 예와도 모순된다. only modifications in couple2swan.F도 GLOBAL 수정 지시와 모순된다. 새 물리량 정의와 기존 출력 선택은 서로 다른 작업이다. 결론: 문서 오기. v56.2.1의 SWANOutputControl은 등록된 일곱 출력 항목을 선택한다.
([features 보고서 §5 R18 (257줄)<br>R19 (258줄)<br>R20 (259줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: ADCIRC 출력에 없는 SWAN IVTYPE) 근거: `docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:113–118,134–154`는 IVTYPE를 소스에서 바꿔 기존 출력 파일에 다른 물리량을 쓰는 절차이다. 전체 `models/ADCIRC/raw/`에서 `rg -i`로 `IVTYPE|SWAN_OutputAgg|swell.wave.height|peak.wave.direction`를 검색했다. `thirdparty/swan/swanout1.ftn:3534,3764,3839,3933,4142,4280,4341`에 IVTYPE 44·12·14·16·15·17·18의 계산 분기가 있다. `src/couple2swan.F:857–863`의 기본 선택값은 10·13·11·53·26·32·47이다. 결론: H 코드 대조 대상 아님. 원문은 소스 수정 방법을 설명한다. 기본 ADCIRC 출력 선택에 없는 값이라는 사실을 SWAN 구현 부재 D로 분류하지 않는다. [10-12 결론 검증 정정]
([features 보고서 §5 R21 (260줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: SWAN 출력 수정 위치 안내) 근거: docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:150 `Search for the variable IVTYPE. Reassign the IVTYPE values using the values of`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:151 `your desired output. For example, if you want to write the peak wave direction`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:152 `to the “swan_DIR.63” file instead of the mean wave direction, you’d want to`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:153 `change IVTYPE = 13 to IVTYPE = 14. Note that you’ll need to make this change in`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:154 `approximately five places within the couple2swan.F file. The embedded images`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:159 `-  ComputeWaveFrictionProperties`<br>docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:160 `-  SwanOutput`<br>src/couple2swan.F:697 `SWAN_VOQR(13) = 7 + NumSwanOutput`<br>src/couple2swan.F:758 `IF(IW.EQ.2) IVTYPE=13`<br>src/couple2swan.F:858 `IF(IW.EQ.2) IVTYPE=13`<br>해석: couple2swan.F에서 ComputeWaveFrictionProperties·IVTYPE·SWAN_VOQR를 검색했다. 전자는 없고 현재 등록·출력 위치는 :697·758·858이다. 같은 판의 실제 파일 구조와 안내 목록이 모순된다. 결론: 문서 오기. 현재 SWAN 출력 변경 작업은 안내문의 고정된 수정 위치 목록을 그대로 사용할 수 없다.
([features 보고서 §5 K13 (577줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 방사 응력 TYPE=1) 근거: src/rs2.F:95 `if(type.eq.1) then`<br>src/rs2.F:96 `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE, message="RS2INIT: TYPE-1 RS FILE NOT YET SUPPORTED.")`<br>src/rs2.F:97 `C        call rs2init_type1(rsnx,rsny,np)`<br>해석: 해당 입력 경로의 종료 조건이 대조 문서에 빠졌다. 주석 처리한 호출은 지원 기능으로 세지 않는다. 결론: 문서 누락. v56.2.1의 NRS=2 초기화는 TYPE=1 방사 응력 파일을 미지원으로 종료한다.
([features 보고서 §5 K14 (578줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: SWAN 파력 평균과 성분 제한) 결론: C 문서 누락. 면적 평균 뒤의 성분 제한 근거는 [파력 누적 정본](#swan-force-average)에 모았다. [10-12 결론 검증 보완]
([features 보고서 §5 K15 (579줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: Marcel 경계 파력) 결론: C 문서 누락. Marcel의 경계 절점 처리 근거는 [파력 누적 정본](#swan-force-average)에 모았다. [10-12 결론 검증 보완]
([features 보고서 §5 K16 (580줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 파력의 계산값과 출력값) 결론: C 문서 누락. 운동량에 적용하는 파력의 조건부 크기 제한은 [시간 보간·제한 정본](#swan-force-momentum)을 따른다. `src/timestep.F:754`는 `RSNXOUT(I) = RSX`로 제한 전 성분을 출력 배열에 저장한다. 출력값과 운동량 적용값은 제한이 작동할 때 다르다. [10-12 결론 검증 보완]
([features 보고서 §5 K17 (581줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: SWAN 출력 읽기 오류의 처리) 근거: src/read_input.F:456 `namelistSpecifier = 'SWANOutputControl'`<br>src/read_input.F:457 `read(unit=15,nml=SWANOutputControl,iostat=ios,iomsg=ios_nml_error_msg)`<br>src/read_input.F:458 `IF(IOS.GT.0)THEN`<br>src/read_input.F:459 `SWAN_OutputHS=.TRUE.`<br>src/read_input.F:460 `SWAN_OutputTPS=.TRUE.`<br>src/read_input.F:461 `SWAN_OutputDIR=.TRUE.`<br>src/read_input.F:468 `&    " SWAN_OutputTM01=",SWAN_OutputTM01,`<br>src/read_input.F:470 `&    " SWAN_OutputWIND=",SWAN_OutputWIND,`<br>src/read_input.F:471 `&    " SWAN_OutputTM02=",SWAN_OutputTM02,`<br>src/read_input.F:472 `&    " SWAN_OutputTMM10=",SWAN_OutputTMM10`<br>해석: 문서의 출력 목록은 이 읽기 오류 분기를 적지 않았다. IOS<0인 namelist 부재와 IOS>0을 같은 조건으로 해석하지 않는다. 결론: 문서 누락. SWANOutputControl 읽기의 IOS>0 분기는 HS·TPS·DIR만 참으로 설정한다.

## D. ADCIRC → SWAN (water level, currents, wind)

Allocated arrays (`couple2swan.F:67-75, 974-982`):
- `SWAN_ETA2` — water level.
- `SWAN_UU2`, `SWAN_VV2` — currents.
- `SWAN_WX2`, `SWAN_WY2` — winds (if `COUPWIND`).

Init copies ADCIRC `ETA2/UU2/VV2` plus winds (`:999-1015`).

Each coupling step:
- WL/currents updated from ADCIRC (`:1157-1171`).
- Dry nodes set depth zero / current zero.
- Wind passed from ADCIRC met → SWAN if `COUPWIND` (`timestep.F:668-686`).

SWAN-side memory grab post-preprocess (`../thirdparty/swan/swanmain.ftn:8696-8983`).

## E. Mesh sharing

SWAN unstructured ADCIRC reader explicitly opens `fort.14` (`SwanReadADCGrid.ftn90:44-108`):
- Reads `ncells, nverts`, node coords + depth, triangles (`:119-158`).

Coupler uses SWAN `nverts/xcugrd/ycugrd` for output/exchange (`couple2swan.F:596-598, 800-835`).

So **same `fort.14` is used by both ADCIRC and SWAN** — single mesh, no interpolation needed.

## F. NWS encoding (NWS=3xx, not 83/84)

**Important**: `wind.F:52-60` allowable base `NWS` list **excludes 83/84**.

Instead, `read_input.F:1804-1831` parses radiation-stress coupling from **hundreds digit**:
```
NRS = ABS(NWS / 100)        ! strip hundreds
NWS = NWS − 100*sign*NRS    ! remaining is base met forcing
```

`NRS=3` is documented as "WAVES WILL BE COUPLED TO SWAN" (`:2269-2275`).

So:

| Input NWS | NRS | Effective base NWS | Meaning |
|---|---:|---:|---|
| `308` | `3` | `8` | OWI hindcast met + SWAN waves |
| `312` | `3` | `12` | OWI WIN/PRE + SWAN |
| `320` | `3` | `20` | GAHM vortex + SWAN |
| `300` | `3` | `0` | No met, only SWAN waves |
| `8` | `0` | `8` | OWI met only, no waves |

Literal `NWS=83/84` is **invalid** in this code path.

## G. Build / link

`makefile` distinguishes:

| Target | Flags | SWAN |
|---|---|---|
| `padcirc` (parallel ADCIRC) | `FFLAGS3 $(DP)`, no SWAN VPATH | Not built |
| `padcswan` (coupled) | parallel + `-DCSWAN`, SWAN VPATH, SWAN switch `-pun -adcirc` | Built and linked |

References: `makefile:195-233, 480-509, 634-635, 661-663`.

So **always use `padcswan` for coupled runs**; `padcirc` even with `NRS=3` won't have SWAN linked.

## H. Hot-start

ADCIRC hot-start reads base `RSNX/RSNY`; for `NRS=3` also reads `SWAN_RSNX/RSNY` history (`hstart.F:325-337`).

Binary hot-start writes:
- Base RS arrays.
- If `NRS=3`: SWAN RS arrays (`write_output.F:5058-5201`).

NetCDF hot-start defines `swan_rsx1/rsy1/rsx2/rsy2` (`netcdfio.F90:5555-5568`); writes for `nrs==3` (`:6966-7045`).

SWAN spectral hot-start is **separate**:
- ADCIRC sets `SwanHotStartUnit` (`read_input.F:1094-1097`).
- `timestep.F:1218-1222` defers SWAN hotfile write until after next SWAN step.
- SWAN calls `BACKUP` then clears flag (`swanmain.ftn:895-902`).

**Possible issue noted in code**: NetCDF read path inquires SWAN variable IDs but reads `hs%rs1/rs2` IDs into `swan_*` arrays — not `hs%swan_rs*` (`netcdfio.F90:8017-8085`). This may indicate a latent bug in NetCDF restart of SWAN-coupled runs; verify before relying on it.

## Decision Guide

| Goal | Setup |
|---|---|
| Tide + wave coupling, OWI met | Compile `padcswan`; set `NWS=312` (or `308` for OWI ASCII met) |
| GAHM hurricane + waves | `NWS=320` (NRS=3, base=20 GAHM) |
| Wave-only test (no met) | `NWS=300` |
| Coupling interval (5 min, ADCIRC dt=2s) | `SWAN_DT=300` in SWAN input → ratio 150 |
| Tight coupling (every ADCIRC step) | `SWAN_DT = DT` — expensive, rarely needed |
| Hot-start coupled run | `IHOT=67/68` for ADCIRC; SWAN auto via `SwanHotStartUnit` |
| Restart NetCDF coupled | Verify `swan_rs*` arrays write/read correctly; possible latent bug |

## Working Rules

- Use `padcswan` binary; verify with `padcswan --help` or check link map for `swan` symbols.
- `SWAN_DT` typically 60-1800 s; ADCIRC `DT` 0.5-5 s. Ratio 100-300 is normal.
- Set ADCIRC `OutputControl` and SWAN `BLOCK` outputs at compatible intervals for diagnostic plots.
- In log, look for "WAVES WILL BE COUPLED TO SWAN" confirming `NRS=3` parsed.
- `COUPWIND` flag in `couple2swan.F`: if true, ADCIRC met goes to SWAN; if false, SWAN reads its own wind file (rarely used).
- For ADCIRC v55+, NetCDF hot-start is preferred; for older versions, fort.67/68 binary is more stable.
- SWAN spectral hot-start (`HOTSTART` in SWAN input) is separate from ADCIRC hot-start; both must align on time.

## Common Pitfalls

- ▢ Setting `NWS=83` literally — invalid; use `NWS=308` etc.
- ▢ Using `padcirc` with `NWS=308` — base met works but no SWAN linked; runs without waves silently.
- ▢ `SWAN_DT` not divisible by `DT` — coupling interval rounds; output frequency anomalies.
- ▢ Hot-start ADCIRC at time T but SWAN cold-start — wave field absent for first SWAN step; spurious zero RS.
- ▢ Hot-start SWAN before ADCIRC catches up — cyclic dependency; ensure both at same `TIMELOC`.
- ▢ Met forcing time alignment — `STATIM/REFTIM` apply to ADCIRC; SWAN reads `INPGRID` time block independently. Match epochs.
- ▢ NetCDF restart with `NRS=3` — possible bug at `netcdfio.F90:8017-8085` (`hs%rs1/rs2` vs `hs%swan_rs*`); test on small case before production.

## SWAN Temporal Controls (upstream 반영, phase 1 of 2)

PR [#498](https://github.com/adcirc/adcirc/pull/498) 의 phase 1 은 **upstream `main` 에 반영됨** — 커밋 `976fc5b6`("Adding SWAN temporal controls", 17 files), 본 노트 baseline `e8b62a70` 에 포함. 런루프 gate 는 `couple2swan.F:1245-1247`(`SwanTimeStep` 이 `[1, SWAN_MTC]` 일 때만 `SWMAIN` 호출), 미호출 구간은 출력값을 초기화(`:1252-1261`)하고 radiation stress 를 할당·이월(`:1267-1291`). fort.15 namelist 파싱은 `prep/presizes.F:276,742-745`(기본 sentinel `"-99999"`). 사용자가 ADCIRC+SWAN coupled simulation 의 SWAN computation 시간을 storm landfall 즈음으로 제한 가능 → 전체 mesh + 전체 timeframe SWAN 호출 회피로 wall-clock 절감. Spatial controls 은 phase 2 예정 — 다만 같은 커밋이 nodal attribute `swan_local_control` 정의를 추가했다(`src/nodalattr.F:89-90,669`). 그 경로의 완결 여부는 본 baseline 에서 미확인. → [[adcirc-nodal-attributes]] §1. 외부 docs: [CCHT-NCSU/Spatial-Temporal-Controls](https://github.com/ccht-ncsu/Spatial-Temporal-Controls).

### 사용자 입력 (PR body verbatim)

- **fort.15 (ADCIRC)** 끝에 namelist 추가:
  ```
  &SWANTimeControl RunStartDateTime='YYYYMMDD.HHMMSS' /
  ```
  `RunStartDateTime` 은 현 ADCIRC 시뮬레이션의 시작 시각

- **fort.26 (SWAN)** 의 `COMPUTE` 카드를 desired range 로 변경:
  ```
  COMPUTE YYYYMMDD.HHMMSS 1200 SEC YYYYMMDD.HHMMSS
  ```

→ namelist 없거나 `RunStartDateTime` 에 `-` 포함 (default sentinel `"-99999"`) 시 **기존 동작 그대로 (전체 시간 SWAN)**. backward-compat.

### 코드 변경 (PR diff 직접 fetch 2026-05-28)

| 파일 | 변경 | 역할 |
|---|---|---|
| `prep/presizes.F` | +RunStartDateTime 변수 + SWANTimeControl namelist + SIZEUP15 read with default `"-99999"` | namelist 정의 + fort.15 parse |
| `prep/prep.F` | `PREP15` 에서 `SWANTimeControl` namelist write | 파티션 prep 단계 출력 보존 |
| `src/couple2swan.F` | `SwanTimeStep` 초기값 = 0 명시; `PADCSWAN_INIT` 에서 `RunStartDateTime` 파싱 → `SwanTimeStep = NINT((AdcircStartTime - SWAN_TINIC) / SWAN_DT)`; `PADCSWAN_RUN` 에서 `[1, SWAN_MTC]` 범위 밖이면 `SWMAIN` skip + wave output sentinel + radiation stress 0 | 핵심 coupling 제어 |
| 그 외 14 files | (테스트 / build / docs) | (본 노트 scope 밖) |

### Algorithm 요점 (couple2swan.F PADCSWAN_INIT/RUN)

```fortran
! INIT: SWAN timestep offset 결정
IF( INDEX( RunStartDateTime, "-") .GT. 0 ) THEN  ! default sentinel
   SwanTimeStep = 0   ! 기존 동작 (전체 시간 SWAN)
ELSE
   CALL DTRETI( RunStartDateTime, 1, AdcircStartTime )
   SwanTimeStep = NINT( ( AdcircStartTime - SWAN_TINIC ) / SWAN_DT )
ENDIF

! RUN: 매 ADCIRC time step
SwanTimeStep = SwanTimeStep + 1
IF((SwanTimeStep.GE.1).AND.(SwanTimeStep.LE.SWAN_MTC))THEN
   CALL SWMAIN(ITIME,SwanTimeStep)        ! SWAN 실제 호출
ENDIF
IF((SwanTimeStep.LT.1).OR.(SwanTimeStep.GT.SWAN_MTC))THEN
   ! SWAN 호출 skip 한 시점: output 변수 sentinel + radiation stress 0
   Swan_HSOut(:) = -99999.D0  ! 등 6개 출력 sentinel
   ADCIRC_SXX/SXY/SYY(:,:) = 0.D0  ! radiation stress 0 → 파-induced 응력 없음
ENDIF
```

→ 핵심 `SWAN_MTC` 는 SWAN 측 (fort.26) `COMPUTE` 카드로부터 도출되는 MTC (Maximum Time-step Counter). 사용자 fort.26 의 COMPUTE range 가 짧을수록 `SWAN_MTC` 작음 → SWAN 호출 시간 윈도우 짧음.

### 의의 + 한계

- **속도 절감**: storm landfall 시간 (~24-72h) 만 SWAN 실행, 그 외 시간 ADCIRC 만 → 전체 wall-clock 큰 폭 감소 (PR body 명시: "yielded faster run times and similar accuracies")
- **정확성**: storm 외 시간의 wave-induced radiation stress 가 0 으로 설정 → tide-driven 일반 시간 surge response 만 평가. ADCIRC-only 시뮬레이션 효과 (해당 시간 window 에서)
- **Backward compat**: namelist 미지정 시 동작 동일
- **Spatial control 은 phase 2 예정** — landfall 인근 mesh 영역에만 SWAN compute 제한 가능 예정

### 운영 권고

- 사용 시 storm landfall 시각 (best track / fort.22 GAHM record) 으로부터 적절한 buffer (예: ±24h) 잡고 `COMPUTE` 카드 범위 설정
- buffer 너무 좁으면 long-period swell 의 영향 미흡 가능 (off-landfall arrival)
- 검증: 동일 fort.15 + 동일 SWAN COMPUTE 전체 vs 일부 두 run 비교 후 peak surge / wave height 차이 정량화 (PR body 가 명시: latest source code 로 default 시간 frame 동일 시 차이 없음)

## Next expansion

- Build recipe for `padcswan` on Linux/Intel.
- COUPWIND vs separate SWAN met forcing recipe.
- NetCDF hot-start verification test.
- Comparison vs older NWS=83 (legacy) coupling.
- Spatial controls (PR phase 2) 가 merge 되면 본 노트 보강.

## References

- Dietrich et al. 2011 (ADCIRC+SWAN unstructured coupling).
- Booij et al. 1999 (SWAN baseline).
- PR #498 <https://github.com/adcirc/adcirc/pull/498> (OPEN 2026-05-18 update).
- CCHT-NCSU temporal/spatial controls docs <https://github.com/ccht-ncsu/Spatial-Temporal-Controls>.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.

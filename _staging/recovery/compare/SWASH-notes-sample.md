# SWASH 노트 반영 표본 (sonnet) — 30줄: OK 29, 부분 1, 틀림 0

| 노트:줄 | 판정 | 근거(원문 인용) | 고칠 내용 |
|---|---|---|---|
| swash-input-parsing-check.md:363 (SI2-003) | OK | SwashInit:291 `iwind = 0`; SwashCheckPrep:288–291 일치; 8756667:SwashCheckPrep:262–265 `if ( iwind == 0 ) iwind = 1` 일치; swashuse PDF p.73 인용 일치; 최종 보고서 533행 B와 동일 | 없음 |
| swash-boundary-spectral-transfer.md:220 (SI1-548) | OK | SwashBCspecfile:833/836/841/845–846/855 줄 번호·원문 일치; 결론 C 동일 | 없음 |
| swash-bottom-friction-wind.md:296 (ST2-359) | OK | SwashUBotFrict:109/111/121/123/131, SwashExpDepUflow:687/702/758, SwashReadInput:777–803, swash.edt:148 `LINear [k]` 일치; 758은 utot 곱함, 687~ 선형 분기는 곱하지 않음; 결론 C 동일 | 없음 |
| README.md:124 (SO1-170) | OK | SwashQuanOutp:2430–2431 회전, 2459 `dirdeg = (alcq + atan2(...))`; SwashDecOutL:109 `alcq = -alpq`; 최종 보고서 E 강함 | 없음 |
| swash-user-manual.md:306 (SI2-078) | OK | SwashCheckPrep:716–718, 726–729, 746–747 원문 일치; 결론 C 동일 | 없음 |
| swash-output.md:303 (SO1-167) | OK | SwashReqOutQ:131–132, SwashOutput:209–213 일치; swashuse p.113 선택지(read 기록 p109-126 17행)와 p.117–118 `to be used in TABLE only` 일치; 결론 B 동일 | 없음 |
| swash-architecture-source-map.md:122 (RF-008) | OK (참고) | SwashMain:241/247/263 일치; 결론 C 동일. 참고: 행의 `:32` 인용문은 이번 수정으로 지운 옛 문장이다 (현재 :37–42에 대체문). 최종 보고서도 같은 표기 | 선택: `:32`를 "수정 전 :32"로 표기 |
| swash-floating-rigid-body.md:243 (SI1-562) | OK | SwashCheckPrep:1117/1143/1147 일치; swashuse p.100 "the semi-implicit approach must be applied" 확인; alpha=pship(1) 확인 (SwashReadInput:1226); 결론 C 동일 | 없음 |
| swash-user-manual.md:333 (SI2-248) | OK | swashuse p.97 `CANNOT BE USED IN CASE OF UNSTRUCTURED GRIDS.` (BOTCel); SwashFlowUDP:81/92/124/137/168 일치; 8756667 동일(81,124,168) 확인; 결론 B 동일 | 없음 |
| swash-implicit-layered-flow.md:224 (ST1-335) | OK (참고) | SwashImpLay1DHflow:2591–2592 `if ( k == kmax ) fac2 = 0.` / `if ( k == 1 .and. presp(nm) == 1 ) fac1 = 0.`; 1107 `bottom layer only`; 8756667:2507–2511 동일; k=1 최상층 기준에 맞음; 링크 `../../../_staging/recovery/compare/SWASH-git-verify-AD.md` 존재. 참고: `:120` 인용문은 수정 전 옛 문장 (현재 :10행대에 대체) | 선택: 옛 줄 번호 표기 |
| swash-boundary-wave-forcing.md:258 (SI1-538) | OK | SwashUpdateData:541/549, SwashCheckPrep:394/400 일치; 결론 C 동일 | 없음 |
| swash-explicit-layered-flow.md:215 (SO1-300) | OK | SwashHydroLoads:305–309, SwashQuanOutp:931–937, 2234–2243, 2281, SwashReadInput:1502–1508, SwashExpLay1DHflow:514–516·596–598 일치; swashuse p.116 PRESSK; 결론 C 동일 | 없음 (KEL·HERM도 ihydro=1이나 본문 결론에 영향 없음) |
| swash-input-parsing-check.md:348 (SG1-875) | OK | SwashCheckPrep:198, 205–217 원문 일치; REPEATING 설명은 swashuse PDF p.38 (추출 `<<<PAGE 38>>>`): `NOT FOR 1D-MODE AND UNSTRUCTURED GRIDS.` 노트의 p.38이 맞다 (보고서는 p.37로 적었음); 결론 C 동일 | 없음 |
| swash-user-manual.md:308 (SI2-091) | OK | SwashPorousStruc:69 `gamma = 0.34`, 354–356; SwashPorFricDep:96; SwashPorFricLay:133 일치; 완전 다공성 층 원계수(123–125) 일치; 결론 C 동일 | 없음 |
| README.md:80 (ST2-427) | 부분 | `rg`·`ls` 집계: src `.ftn90` 152, `.ftn` 8, 일반 파일 162, source-analysis 21은 맞다. git: 92커밋 중 src 있는 80트리, 파일 수 143(6)·148(12)·156(2)·158(2)·159(2)·160(56) 재계산 일치, 152 없음. 그러나 문장 "현재 `manual-notes/*.md`는 3파일"·"manual-notes의 Markdown 파일은 3개다"는 지금 거짓이다: `ls models/SWASH/manual-notes` = 4개 (swash-build-run-differences.md 추가, 같은 README 54행은 "현재 직접 목록 4개") | 80행의 manual-notes 3개를 "대조 시점(10-15 보고서 집계) 3개, 현재 4개"로 고치거나 4개로 정정 |
| swash-input-parsing-check.md:358 (SG1-895) | OK | SwashCheckPrep:1265–1275, 1285–1302 일치; pnums(5)=0은 1273 조건을 통과(0 초과 아님) 확인; 결론 C 동일 | 없음 |
| swash-scalar-transport.md:254 (SI2-284) | OK | SwashHDiffZplane1DH:285–290, 294; 2DH:315; Van Leer 줄 283은 주석 확인; 결론 C 동일 | 없음 |
| swash-scalar-transport.md:249 (SI2-150) | OK | SwashCheckPrep:804–810, 812–818 일치; swashuse p.23, p.86 인용문 grep 정확히 일치; psed(1,2,10,11,12)=침강속도·입경·TAUCE·TAUCD·ERATE 대응 확인 (SwashReadInput:1416–1439); 결론 C 동일 | 없음 |
| swash-explicit-depthavg-flow.md:366 (ST1-264) | OK | 1000 `cfu = -fcor*v`, 2641 `cfv = fcor*u`, 1360/3000 갱신식 일치; contrib에 +corf(1354, 2994) 포함 → 가속도 (+fv,-fu) 맞음; swashtech p.63 식(3.2) read 기록 일치; 결론 F 동일 | 없음 |
| swash-linear-solvers.md:142 (SI2-279) | OK | SwashImpDep1DHflow:954 `call tridiag` (inewt==0 분기 851); SwashSolvers:1207 `rho = rho + resd*z`, 1213 `rnrm0 = sqrt(rho)` (z=전처리 결과); 결론 C 동일 | 없음 |
| swash-user-manual.md:290 (SG1-909) | OK (참고) | SwashReadInput:917 `'BETA', psurf(2), 'STA', -1.`; SwashCheckPrep:1076–1084 일치; 8756667:956–962, a486d5f:1076–1082 일치; 1065에 beta<alpha 검사 없음 확인; 결론 B 동일. 참고: `swash-user-manual.md:180` 인용문은 수정 전 옛 문장 | 선택: 옛 줄 번호 표기 |
| swash-user-manual.md:347 (SI1-119) | OK | swashuse p.34 `Default: [grav] = 9.81`; SwashInit:135 `grav = 9.813`; SwashReadInput:533; 8756667:SwashInit:130 `9.813`; 전 80 리비전 `grav = 9.813`만 존재 (재집계); 링크 resolve; 결론 B 동일 | 없음 |
| swash-tech-documentation-overview.md:99 (ST1-319) | OK | swashtech 추출 `<<<PAGE 65>>>`: `Chapter 4` 제목 + `This chapter is under preparation.`; p.66은 쪽 머리만; 링크 resolve | 없음 |
| swash-user-manual.md:96 (SI1-120) | OK | SwashReadInput:535–536 TEMP·SALINITY; SwashCheckPrep:889–905 (idens, `rhow /= -999.` 조건) 일치; 지정한 RHOWAT는 유지 | 없음 |
| swash-implicit-depthavg-flow.md:257 (ST2-365 참조) | OK | SwashImpDepUflow:1041 `denom = 1. + dt * ( cbot(iface) + wndimp(iface) )` 일치 | 없음 |
| swash-output.md:261 | OK | 7949227 2026-05-06 `release v12.01`이 swashuse.pdf·swashtech.pdf 마지막 변경 (git log 각각 확인); a486d5f 2026-05-26; SwashInit:79 `VERNUM = 12.01`; 7949227..a486d5f 사이 src 변경은 608ffd7·9554c98 | 없음 |
| swash-timestepping-update-driver.md:460 | OK | SwashCompUnstruc:74–78 `if ( kmax == 1 ) call SwashUpdateUDepths ( u1 )` / `else ... ( udep )`, 줄 75·77 일치 (mermaid 렌더는 확인하지 않음) | 없음 |
| swash-floating-rigid-body.md:82 | OK | SwashCheckPrep:1388–1391 `rhoinf = pship(5)`, 범위 밖이면 지역 `rhoinf = 1.` (pship(5) 자체는 유지) — 본문 "실제 계수 계산에 사용하는 rhoinf" 정확 | 없음 |
| swash-user-manual.md:232 | OK | SwashInit:463 `inewt = -1`; SwashReadInput:1860 `inewt = 0`, 1878 `NEWT → inewt = 1`; SwashCheckPrep:618–624 (비정형이면 1), 1307–1312 (tol 0.01/0.001) 일치 | 없음 |
| swash-implicit-depthavg-flow.md:262 | OK | swash-output.md:261과 동일 문장; 위와 같은 git 확인 | 없음 |

공통 참고 (판정에 반영 안 함): 표 4행 (architecture:122, implicit-layered:224, user-manual:290, 그리고 같은 계열 행)이 "수정 전 노트의 줄 번호"를 인용한다. 인용문이 이번 수정으로 사라져 그 줄에서는 찾을 수 없다. 보고서 원문도 같은 방식이다.
확인하지 않은 것: swashtech p.94·swashuse p.76–77의 본문 세부, SG1-914/935·SI1-710 등 연결 행의 내용, mermaid 렌더.

## Claude 조치 (10-15)

- README.md:80(ST2-427)의 manual-notes 파일 수를 "대조 시점 3개, 10-15 반영 뒤 4개"로 고쳤다(`[10-15 표본 정정]`).
- SG1-875의 쪽 번호를 보고서 `compare/swash-guide-syntax-build-vs-code.md` 두 곳에서 p.37에서 p.38로 고쳤다. 추출 텍스트 `<<<PAGE 38>>>`에 `NOT FOR 1D-MODE AND UNSTRUCTURED GRIDS.`가 있다.

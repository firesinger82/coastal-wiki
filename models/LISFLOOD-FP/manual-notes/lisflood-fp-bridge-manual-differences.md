---
title: "LISFLOOD-FP user manual +bridge.docx — 문서 내부 오기와 코드 차이"
model: LISFLOOD-FP
doc: "user manual +bridge.docx (Code release 4.3.6, 2008-04-25) + user manual.pdf (Code release 6.1.1, 2013-11-25)"
canonical_source: manual
citation_status: verified
verification_method: "2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
verification_by: "Codex (최종 근거 행 전사 대조)"
verification_date: 2026-10-21
last_source_check: "2026-10-21 (recovery 대조 반영)"
note_author: "Codex"
note_date: 2026-10-21
related:
  - lisflood-fp-user-manual.md
  - lisflood-fp-docx-manual-differences.md
source_scope: LISFLOOD-FP/*
---

# LISFLOOD-FP user manual +bridge.docx의 차이

이 노트는 최종 대조 기록의 결론을 옮긴 AI 정리이다.
표의 원문 인용은 결론 문장과 구분한다.
Word 쪽 번호는 변환본의 쪽 번호이다.
코드 인용의 기준은 `../raw/source_code/LISFLOOD-FP/`이다.
`v8.0:`·`v8.1:`·`v8.2:`는 해당 이전 배포본을 뜻한다.

## 문서와 코드 차이 (10-21 대조)

user manual +bridge.docx 표지는 Code release 4.3.6을 적는다 (변환본 p.1). [10-21 전수 검증 보완]
bridge 표지 날짜는 2008-04-25이다 (변환본 p.1). [10-21 전수 검증 보완]
2013 PDF 매뉴얼 표지는 Code release 6.1.1을 적는다 (user manual.pdf p.1). [10-21 전수 검증 보완]
PDF 표지 날짜는 2013-11-25이다 (user manual.pdf p.1). [10-21 전수 검증 보완]
현재 코드는 Zenodo 8.2(10.5281/zenodo.13121102)에 공식 8.3 변경을 적용한 판이다 (`../LISFLOOD-FP-8.3-package/README.md:19–24`; [최종 근거 LB1-408](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md)). [10-21 전수 검증 정정]
체크포인트에 쓰는 내부 숫자 판은 8.1.0이다 (`VersionHistory.h:16–22`). [10-21 전수 검증 보완]
릴리스 이름은 8.3이다 (`VersionHistory.h:23`). [10-21 전수 검증 보완]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| bridge-docx:LB1-001 | 표지 날짜와 자체 판 이력 | user manual +bridge.docx p.1·2(변환본) `Code release 4.3.6`; p.1 `25th April 2008` | `VersionHistory.h:23` `#define LF_Release "8.3"`; 52행 `4.3  Sep 04 2009  Full dynamic and diffusive initial steady state channel solution added and tested by Tim Fewtrell`<br>확인한 원문: user manual +bridge.docx p.1·2·5(변환본); user manual.pdf p.1·2; `VersionHistory.h:21–23,52` | B 문서 오기 | 표지 날짜는 자체 이력 표의 4.3 날짜보다 이르다. user manual.pdf p.1은 `Code release 6.1.1`, `25 November 2013`으로 바꾼다. PDF 머리글은 5.9.6이며 정보 표는 6.0.4이다. 단일 시점의 완결된 판 표기로 해석할 수 없다. |
| bridge-docx:LB1-050 | 입력 파일 종류 수 | user manual +bridge.docx p.21(변환본) `eight file types` | `pars.cpp:481` `if (read_string_param(param_name, line_number, param_value_ptr, "gaugefile", Fnameptr->gaugefilename, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.9·21·27–29·32–33(변환본); `pars.cpp:54–72,481–485` | B 문서 오기 | bridge판 자체의 1.3.2.1–1.3.2.12는 12종을 설명한다. `eight`는 자체 목차와 맞지 않는다. 파일 확장자는 코드가 강제하지 않는다. [10-21 전수 검증 보완] |
| bridge-docx:LB1-099 | touput 철자 | user manual +bridge.docx p.8(변환본) `touput` | `pars.cpp:438`의 실제 키워드는 `"toutput"`이다. 전체 검색 결과는 [보고서 §5 검색 기록 S1](../../../_staging/recovery/compare/lisflood-bridge-docx-vs-code.md#d-검색-기록-s1s2)에 있다.<br>확인한 원문: user manual +bridge.docx p.8·22(변환본); `pars.cpp:437–445`; `VersionHistory.h:405–408`; 현재·v8.0·v8.1·v8.2 전체 트리 검색 | B 문서 오기 | user manual +bridge.docx p.8(변환본)의 `touput`는 `toutput`의 철자 오기이다. 실제 키워드는 `toutput`이다. 출력 경로의 문제는 [최종 근거 LB1-084](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1a.md)에서 별도로 판정했다. [10-21 전수 검증 보완] |
| bridge-docx:LB1-100 | tpouput 철자 | user manual +bridge.docx p.38(변환본) `tpouput` | `pars.cpp:438`의 실제 키워드는 `"toutput"`이다. [보고서 §5 검색 기록 S1](../../../_staging/recovery/compare/lisflood-bridge-docx-vs-code.md#d-검색-기록-s1s2).<br>확인한 원문: user manual +bridge.docx p.22·38(변환본); `pars.cpp:438–445`; 현재·v8.0·v8.1·v8.2 전체 트리 검색 | B 문서 오기 | user manual +bridge.docx p.38(변환본)의 `tpouput`는 `toutput`의 철자 오기이다. 실제 키워드는 `toutput`이다. [10-21 전수 검증 보완] |
| bridge-docx:LB1-101 | ch_dyanmic 철자 | user manual +bridge.docx p.23(변환본) startq 교차참조 `ch_dyanmic` | `pars.cpp:269`의 실제 키워드는 `"ch_dynamic"`이다. [보고서 §5 검색 기록 S1](../../../_staging/recovery/compare/lisflood-bridge-docx-vs-code.md#d-검색-기록-s1s2).<br>확인한 원문: user manual +bridge.docx p.6·23(변환본); `pars.cpp:269–274`; 현재·v8.0·v8.1·v8.2 전체 트리 검색 | B 문서 오기 | user manual +bridge.docx p.23(변환본)의 startq 설명에 있는 `ch_dyanmic`은 `ch_dynamic`의 철자 오기이다. [10-21 전수 검증 보완] |
| bridge-docx:LB1-102 | checkfile 입력 예제 | user manual +bridge.docx p.24(변환본) `#checkfile res_old.chkpnt` | `pars.cpp:569`의 입력 키워드는 `"loadcheck"`이다. 572행은 `Statesptr->checkfile = ON;`이다. [보고서 §5 검색 기록 S2](../../../_staging/recovery/compare/lisflood-bridge-docx-vs-code.md#d-검색-기록-s1s2).<br>확인한 원문: user manual +bridge.docx p.21·24(변환본); `pars.cpp:569–573`; `v8.0:pars.cpp:558–562`; 현재·v8.0·v8.1·v8.2 전체 트리 검색 | B 문서 오기 | user manual +bridge.docx p.24(변환본)의 `#checkfile res_old.chkpnt`는 같은 문서 p.21의 `loadcheck`와 충돌한다. 대체 파일을 지정하는 입력 키워드는 `loadcheck`이다. 내부 상태명 `checkfile`은 입력 키워드가 아니다. [10-21 전수 검증 보완] |
| bridge-docx:LB1-105 | 시간 간격·제한식 교차참조 | user manual +bridge.docx p.22(변환본)의 toutput 식 `[14]`, p.8·38의 최적 시간간격 `[14]`·유량 제한 `[8]` | `fp_flow.cpp:160` `*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));`; 167행 `Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);`<br>확인한 원문: user manual +bridge.docx p.8·22–23·38·48–50(변환본); `fp_flow.cpp:158–167` | B 문서 오기 | bridge판에서 최적 시간간격은 [16]이다. 제한식은 [9]이다. [14]는 일반 확산식의 이산화이다. 식 번호 이동을 반영하지 않은 참조이다. |
| bridge-docx:LB1-147 | 교량 기능 도입 판 | user manual +bridge.docx p.30(변환본) `since version 5.6.5`; 표지 4.3.6·2008년 | `VersionHistory.h:162–163` `Sep 11 2012  5.6.5    Included energy gradient elevation in bridge orifice flow calculation - important for high approach velocities. (MT)` / `Sep 03 2012  5.6.4    Added function for bridge to SGC model. Only operates when bridge soffit is exceeded. (JCN)`<br>확인한 원문: user manual +bridge.docx p.1·30(변환본); user manual.pdf p.40; `VersionHistory.h:162–163`; `v8.0:weir_flow.cpp:138–143` | B 문서 오기 | bridge판의 4.3.6·2008년 표지는 p.30의 5.6.5 교량 설명과 일치하지 않는다. 이력상 교량 기능 도입은 5.6.4이다. 접근 유속의 에너지 수두 추가는 5.6.5이다. |
| bridge-docx:LB1-170 | resroot 명령 줄 옵션 | user manual +bridge.docx p.35(변환본) 명령 줄 표의 `resroot`에 하이픈 없음 | `pars.cpp:1029–1031` `if (argv[i][0] == '-')` / `{` / `param_ptr = &argv[i][1];`; `pars.cpp:164` `if (read_string_param(param_name, line_number, param_value_ptr, "resroot", Fnameptr->res_prefix, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.35(변환본); user manual.pdf p.34; `pars.cpp:164–167,1023–1036` | B 문서 오기 | 명령 줄 옵션은 `-resroot`여야 한다. user manual.pdf p.34는 `-resroot`로 적는다. |
| bridge-docx:LB1-221 | 누락된 식 [6] 본체 | user manual +bridge.docx p.47(변환본) `[6]` 아래 식 본체 빈칸; 본문 `The term in brackets is the diffusion term` | `ch_flow.cpp:840–847`에서 자유수면 기울기 항과 Manning 항을 구성한다. 대표 원문은 `f[2*i+2]-=nSq*w43*q*fabs(q)*pow( a,(C(-10.)/C(3.0)));`이다.<br>확인한 원문: user manual +bridge.docx p.47(변환본) 식 [5]·[6]과 후속 문단; `ch_flow.cpp:840–847` | B 문서 오기 | 쪽 이미지는 식 번호만 담는다. 문서가 지시한 괄호 항은 인쇄되지 않았다. 누락된 식을 코드로부터 복원하여 문서 원문으로 제시하지 않는다. |
| bridge-docx:LB1-238 | 식 번호 교차참조 | user manual +bridge.docx p.48(변환본) `Qy ... equation 6`, 수심 갱신 `equation 5`; p.49 제한자 `equation 7`, 연속·운동량 `Equations (5) and (6)`, 결합 `(8) and (9)`; p.50 Jacobi `equation (11)`, 선형 시간간격 `(14)` | `iterateq.cpp:539–540`은 [7] 갱신이다. `fp_flow.cpp:157,167,160`은 각각 Manning 유량·제한량·시간간격이다.<br>확인한 원문: user manual +bridge.docx p.22–23·38·47–50(변환본) 식 [6]–[17]; `iterateq.cpp:539–540`; `fp_flow.cpp:157,160,167` | B 문서 오기 | bridge판의 홍수터 수심 갱신식은 [7]이다. Manning 유량식은 [8]이다. 제한식은 [9]이다. 단위폭 연속식과 유량식은 [10]·[11]이다. 일반 확산 이산식은 [14]이다. 비선형 적응 시간간격식은 [16]이다. 본문 교차참조는 이 번호들과 맞지 않는다. 빈 식 [6]을 홍수터 식으로 옮기지 않는다. |
| bridge-docx:LB1-240 | 전역 변수·무인수 함수 설명 | user manual +bridge.docx p.41(변환본) 전역 변수로 통신·`void SmoothBanks();`, `DomainVol();`, `ChannelQ();`, `FloodplainQ();`, `UpdateH();` 등의 인수 없는 선언 | `lisflood.h:150–159`의 구조체 설명 `Fnames - Contains all the filenames from the .par file`와 `States - Contains all the state parameters for the simulation`; `util.cpp:151` `void SmoothBanks(Pars *Parptr, Solver *Solverptr, ChannelSegmentType *ChannelSegments, Arrays *Arrptr, vector<ChannelSegmentType> *ChannelSegmentsVecPtr, const int verbose)`<br>확인한 원문: user manual +bridge.docx p.8·19·41(변환본); `VersionHistory.h:391–392`; `lisflood.h:150–159`; `util.cpp:151` | B 문서 오기 | user manual +bridge.docx p.41(변환본)의 전역 변수·무인수 함수 설명은 3.0의 구조체·포인터 도입 이력과 충돌한다. 현재 `SmoothBanks`는 `Pars`·`Solver`·`ChannelSegmentType`·`Arrays`·벡터의 포인터와 verbose 값을 명시적으로 받는다. |
| bridge-docx:LB1-241 | SmoothBanks 기본 htol | user manual +bridge.docx p.41(변환본) SmoothBanks의 `<0.5m`; p.43 `double htol=0.5;` | `lisflood.cpp:181` `ParSolver.htol = C(1.0);`; `VersionHistory.h:339` `htol is now an optional parameter in the par file, but defaults to 1m. The`<br>확인한 원문: user manual +bridge.docx p.23·36·41·43(변환본); `lisflood.cpp:181`; `VersionHistory.h:333–341` | B 문서 오기 | 문서 시점보다 앞선 3.4.0 이력도 1 m를 적는다. user manual +bridge.docx p.23·36(변환본)의 1 m와도 충돌한다. 구판 차이만으로 문서 내부의 두 기본값을 동시에 설명할 수 없다. |
| bridge-docx:LB1-247 | 출력 함수 선언 | user manual +bridge.docx p.42(변환본) `void write_ascii(float *f,FILE *fp);`, `void write_elev();` | `output.cpp:21` `void write_ascfile(const char *root, int SaveNumber, const char *extension, NUMERIC_TYPE *data, NUMERIC_TYPE *dem, int outflag, States *Statesptr, Pars *Parptr)`<br>확인한 원문: user manual +bridge.docx p.42(변환본); `output.cpp:21–24,39–48,96–172`; `VersionHistory.h:401–404` | B 문서 오기 | 현재는 일반 출력 함수와 outflag로 수심·표고·면 유량을 처리한다. `VersionHistory.h:401–402`는 2.7.Sv49에서 출력 이름 표준화와 공통 함수화를 기록한다. 문서가 그 이전 선언을 남겼다. [10-21 전수 검증 보완] |
| bridge-docx:LB1-249 | 시계열 저장·보간 | user manual +bridge.docx p.42·44(변환본) `LoadBCVar`에서 `BCVarlist`, `QVarlist`에 매 반복 시각의 값을 미리 저장 | `input.cpp:2008` `LoadTimeSeries(BCptr->allTimeSeries.back(), Fnameptr->bdyfilename, fp, OFF);`; `lisflood.h:449` `TimeSeries **BC_TimeSeries;`; 782행 `TimeSeries **Q_TimeSeries;`; `boundary.cpp:1464` `res = a1*values[i] + a2*values[i - 1];`<br>확인한 원문: user manual +bridge.docx p.1·42·44(변환본); `input.cpp:1882–1903,2005–2009`; `boundary.cpp:1455–1466`; `lisflood.h:445–449,779–784`; `v8.0:input.cpp:1970–1972` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. 현재는 원래 자료 시각·값을 TimeSeries에 저장한다. 필요 시각에 보간한다. 모든 반복 시각의 결과를 미리 저장하는 배열이 아니다. [10-21 전수 검증 보완] |
| bridge-docx:LB1-252 | 반복 카운터 선언 | user manual +bridge.docx p.42(변환본) `int Nit,ts`; 반복 수·반복 | `lisflood.h:728` `long   Nit, itCount;`<br>확인한 원문: user manual +bridge.docx p.1·42(변환본); `lisflood.h:728`; `v8.0:lisflood.h:708` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. 현재 카운터 이름은 itCount이며 형은 long이다. 옛 전역 변수 선언을 현재 선언으로 인용할 수 없다. |
| bridge-docx:LB1-254 | 출력 간격 자료형 | user manual +bridge.docx p.42(변환본) `int SaveInt,MassInt,op;` | `lisflood.h:669` `NUMERIC_TYPE SaveInt, MassInt;`; `pars.cpp:222`는 `"overpass", &Parptr->op`를 숫자로 읽는다.<br>확인한 원문: user manual +bridge.docx p.1·21·24·42(변환본); `lisflood.h:669–675`; `pars.cpp:204–207,222–225`; `v8.0:lisflood.h:661–667` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. 문서의 선언은 `int SaveInt,MassInt,op;`이다. 현재 SaveInt·MassInt·op는 NUMERIC_TYPE이다. 현재 파서는 세 값을 실수 입력으로 읽는다. |
| bridge-docx:LB1-256 | 상태·verbose 선언 | user manual +bridge.docx p.43(변환본) `ChannelPresent,NCFS,verbose`, `weir` 스위치 | `lisflood.cpp:197–199` `SimStates.ChannelPresent = OFF;` / `SimStates.TribsPresent = ON;` / `SimStates.NCFS = ON;`; 227행 `SimStates.weirs = OFF;`; `pars.cpp:17` `int ReadVerboseMode(int argc, char *argv[])`<br>확인한 원문: user manual +bridge.docx p.1·41·43(변환본); `lisflood.cpp:197–199,227`; `pars.cpp:17–24`; `VersionHistory.h:391–392` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. 현재는 States의 ChannelPresent·NCFS·weirs와 함수 인수 verbose를 사용한다. 단일 전역 `weir` 이름을 현재 상태명으로 쓰지 않는다. |
| bridge-docx:LB1-257 | 파일명 배열 크기 | user manual +bridge.docx p.43(변환본) 80자 파일명 배열 `demfilename`, `chanfilename`, `startfilename`, `Qfilename`, `resrootname`, `qfilename`, `nfilename`, `rivername`, `bcifilename`, `bdyfilename`, `weirfilename`; `mass_fp,QBC_fp,h_fp,op_fp` | `lisflood.h:381–395`에서 `char resrootname[512]; // resrootname will be res_dirname + res_prefix`, `char demfilename[256];`, `char startfilename[256];`, `char chanfilename[256];`, `char qfilename[256];`, `char nfilename[256];`, `char rivername[256];`, `char bcifilename[256];`, `char bdyfilename[256];`, `char weirfilename[256];`<br>확인한 원문: user manual +bridge.docx p.1·43(변환본); `lisflood.h:378–401`; `v8.0:lisflood.h:381–395` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. 현재 Fnames는 256자 파일명과 512자 결합 경로를 둔다. 대문자 Qfilename을 별도 현행 필드로 취급하지 않는다. |
| bridge-docx:LB1-258 | 격자 배열 크기 | user manual +bridge.docx p.43(변환본) `2D raster arrays (xsz x ysz): DEM,H,Qx,Qy,maxH` | `input.cpp:1371–1372` `Arrptr->Qx = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` / `Arrptr->Qy = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));`<br>확인한 원문: user manual +bridge.docx p.1·43(변환본); `input.cpp:1339,1369–1372`; `v8.0:input.cpp:1340–1343` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. 현재 H·maxH는 xsz×ysz 크기로 할당한다. 현재 Qx·Qy는 `(Parptr->xsz + 1)*(Parptr->ysz + 1)` 크기로 할당한다. |
| bridge-docx:LB1-261 | 보 자료 배열 크기 | user manual +bridge.docx p.43(변환본) `1-D RASTERS (chsz)` 아래 `Weir_hc,Weir_Cd,Weir_m,Weir_w,Weir_Identx,Weir_Identy` | `lisflood.h:311–323`의 `int weir_count;`, `//lists of weir data (each have 'weir_count' items)`, 네 NUMERIC_TYPE 포인터, `int *Weir_Identx;`, `int *Weir_Identy;`; `input.cpp:146–147` `Arrptr->Weir_Identx = new int[(Parptr->xsz + 1)*(Parptr->ysz + 1)];` / `Arrptr->Weir_Identy = new int[(Parptr->xsz + 1)*(Parptr->ysz + 1)];`<br>확인한 원문: user manual +bridge.docx p.1·43(변환본); `lisflood.h:311–323`; `input.cpp:134–151`; `v8.0:lisflood.h:311–323` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. 현재 Weir_hc·Weir_Cd·Weir_m·Weir_w는 입력 연결 수 nw만큼 할당한다. Weir_Identx·Weir_Identy는 `(Parptr->xsz + 1)*(Parptr->ysz + 1)` 크기로 할당한다. 연결 없음의 값은 −1이다. |
| bridge-docx:LB1-263 | 가변 경계 시계열 연결 | user manual +bridge.docx p.44(변환본) BC_Val은 HFIX/QFIX 정적값 또는 BCVarlist의 위치; 하도 Q_Val·QVarlist·Q_Ident도 같은 방식 | `lisflood.h:446–449` `NUMERIC_TYPE *BC_Val;` / `// time series indexed by bci (boundary condition index) //TFD` / `// BC_TimeSeries used in case of var e.e. HVAR or QVAR (otherwise set to NULL)` / `TimeSeries **BC_TimeSeries;`; 779–784행 Q_Val·Q_TimeSeries·Q_Ident·Q_Name 선언<br>확인한 원문: user manual +bridge.docx p.1·44(변환본); `lisflood.h:445–449,778–784`; `v8.0:lisflood.h:444–448,753–759` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. 현재 시간변화 자료는 BC_Val의 정수 인덱스가 아닌 별도 TimeSeries 포인터에 연결한다. 고정값 의미는 유지한다. |

## 문서 판과 식 번호

bridge판의 4.3.6·2008년 표지는 p.30의 5.6.5 교량 설명과 일치하지 않는다 (user manual +bridge.docx p.1·30(변환본)).
이력상 교량 기능 도입은 5.6.4이다 (`VersionHistory.h:163`).
접근 유속의 에너지 수두 추가는 5.6.5이다 (`VersionHistory.h:162`).
bridge판의 홍수터 수심 갱신식은 [7]이다 (user manual +bridge.docx p.48(변환본)).
Manning 유량식은 [8]이다 (user manual +bridge.docx p.48(변환본)).
제한식은 [9]이다 (user manual +bridge.docx p.48(변환본)).
비선형 적응 시간간격식은 [16]이다 (user manual +bridge.docx p.50(변환본)).
빈 식 [6]을 홍수터 식으로 옮기지 않는다 (user manual +bridge.docx p.47(변환본)).

## 대조 근거

- bridge-docx: [보고서](../../../_staging/recovery/compare/lisflood-bridge-docx-vs-code.md).
- [최종 근거 LB1a](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1a.md).
- [최종 근거 LB1b](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md).

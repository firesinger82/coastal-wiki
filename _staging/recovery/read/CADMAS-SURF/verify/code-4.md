# CADMAS-SURF code-4 전수 검증

대상 기록의 frontmatter `file:`을 원문으로 사용한다.
기록의 각 구간마다 `nl -ba <원문> | sed -n 'A,Bp'`로 원문을 열어 대조한다.
한 번의 원문 출력은 최대 200행이다.
인용문과 행 번호의 기계 대조를 함께 수행한다.
의미·분기 순서·바깥 블록·일본어 번역은 출력한 원문과 직접 대조한다.
원문과 모델 실행 결과의 일치 여부는 검증하지 않는다.
모델은 실행하지 않는다.

기록 경로의 공통 접두사는 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/`이다.
아래 원문 행은 각 기록의 `file:`에 있는 원문을 가리킨다.
집계 단위는 기록의 구간 행이다.
정정과 보완이 함께 있는 구간은 각각 집계한다.
이상 없음은 수정하지 않은 완료 구간의 수이다.
대조를 완료한 기록은 31개이다(아래 기록별 집계).
대조를 완료한 구간 행은 110개이다(각 기록의 구간 표에서 집계).
대조한 원문은 합계 5,157행이다(각 `file:` 원문의 실제 행 수 합계).
행 번호가 붙은 원문 인용 4,676개를 기계 대조했다(수정 후 대상 기록에서 집계).
인용문·행 번호 불일치는 0개이다.
빈 줄과 내용 없는 주석 줄을 제외한 원문 인용 누락은 0개이다.
모든 원문의 SHA-256은 각 기록의 기존 frontmatter 값과 일치한다.
대상 기록의 frontmatter와 구간 경계는 수정 전 값과 일치한다.
정정과 보완을 함께 적용한 구간은 7개이다(수정 표지를 구간별로 집계).
후속 코드 사실의 수정은 해당 원문 구간의 정정으로 집계했다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 상태 |
|---|---:|---:|---|
| vf_comak0.f.md | 2 | 61 | 완료 |
| vf_cpara.f.md | 3 | 136 | 완료 |
| vf_croot2.f.md | 2 | 69 | 완료 |
| vf_croot3.f.md | 3 | 83 | 완료 |
| vf_csetup.f.md | 6 | 369 | 완료 |
| vf_cvort.f.md | 4 | 216 | 완료 |
| vf_cwlvl.f.md | 2 | 67 | 완료 |
| vf_cwmak0.f.md | 2 | 71 | 완료 |
| vf_cwmak1.f.md | 2 | 49 | 완료 |
| vf_cwmak2.f.md | 2 | 55 | 완료 |
| vf_cwmsrc.f.md | 3 | 155 | 완료 |
| vf_cwmtb1.f.md | 3 | 79 | 완료 |
| vf_cwmtb12.f.md | 3 | 79 | 완료 |
| vf_cwmtb2.f.md | 3 | 73 | 완료 |
| vf_cwmtb22.f.md | 3 | 74 | 완료 |
| vf_cwzero.f.md | 3 | 86 | 완료 |
| vf_f1cal.f.md | 5 | 248 | 완료 |
| vf_faulti.f.md | 3 | 127 | 완료 |
| vf_faultt.f.md | 2 | 99 | 완료 |
| vf_fbubup.f.md | 3 | 77 | 완료 |
| vf_fconv.f.md | 4 | 215 | 완료 |
| vf_fconvs.f.md | 8 | 644 | 완료 |
| vf_fcut01.f.md | 2 | 67 | 완료 |
| vf_fdropf.f.md | 11 | 678 | 완료 |
| vf_feuler.f.md | 2 | 67 | 완료 |
| vf_fgene.f.md | 2 | 79 | 완료 |
| vf_fmod1.f.md | 4 | 209 | 완료 |
| vf_fnfini.f.md | 4 | 206 | 완료 |
| vf_fnfprv.f.md | 4 | 236 | 완료 |
| vf_fpvcip.f.md | 5 | 266 | 완료 |
| vf_fpvcpp.f.md | 5 | 217 | 완료 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 | 구분 |
|---|---|---|---|---|
| vf_cpara.f.md:1–60 | 인덱스 간격이 2 미만이거나 프로세스(process) 수가 분할 수의 곱과 다르면 VF_A2ERR를 호출한다. | `NUMNPI.GT.1`일 때 I 방향 인덱스 간격이 2 미만이면 `CALL VF_A2ERR('VF_CPARA','2 > IC2-IC1.')`를 실행한다. `NUMNPJ.GT.1`일 때 J 방향 인덱스 간격이 2 미만이면 `CALL VF_A2ERR('VF_CPARA','2 > JC2-JC1.')`를 실행한다. `NPROCS.NE.NUMNPI*NUMNPJ`이면 `CALL VF_A2ERR('VF_CPARA','NPROCS <> NPI*NPJ.')`를 실행한다. | 37–60 | 정정 |
| vf_cpara.f.md:61–109 | J와 I 순서로 순위(rank)의 위치를 찾는다. 내부 경계 2칸과 외부 경계 1칸을 반영해 지역 격자 범위를 설정한다. | J를 바깥 루프로 두고 I를 안쪽 루프로 두어 `L.EQ.MYRANK`인 위치를 찾는다. MYMIS·MYMIE·MYMJS·MYMJE의 기본값은 2이다. 각각 `MYGIS.EQ.2`, `MYGIE.EQ.NUMI0-1`, `MYGJS.EQ.2`, `MYGJE.EQ.NUMJ0-1`이면 대응 값을 1로 바꾼다. 75–98행의 인덱스 대입식으로 지역 격자 범위를 설정한다. | 63–98 | 정정 |
| vf_croot2.f.md:23–69 | D<0이면 실근 수를 0으로 돌려준다. | 앞의 `ABS(D).LT.1.0D-20`이 거짓이고 `D.LT.0.0D0`이면 실근 수를 0으로 돌려준다. | 43–50 | 정정 |
| vf_croot3.f.md:59–83 | 시작 시 28행 IF의 33행 ELSE 및 44행 IF 안. | 시작 시 `IF (AA.EQ.0.0D0) THEN`(28)의 `ELSE`(33) 안이다. 이 바깥 IF는 74행 `ENDIF`에서 닫힌다. 시작 시 `IF (D.GT.0.0D0) THEN`(44) 안이다. 이 IF는 60행 `ELSE`를 거쳐 73행 `ENDIF`에서 닫힌다. | 28·33·44·60·73–74 | 보완 |
| vf_csetup.f.md:56–126 | Ursell 수(Ursell number) 25.0으로 자동 파형 종류를 전환하고 VF_CWMAK0·VF_CWZERO로 파장·영점 위상을 계산한다. | `N.EQ.0`일 때만 Ursell 수(Ursell number) 25.0을 기준으로 파형 종류를 전환한다. `CALL VF_CWMAK0(D,T,H,WLN,N)`으로 파장을 계산한다. `N.NE.-3 .AND. N.NE.-4`일 때만 `CALL VF_CWZERO(WT0,N)`을 실행한다. N=-3이면 `WT0=DMTBT0`을 대입한다. 나머지 분기에서는 `WT0=DMTBT02`를 대입한다. | 104–121 | 정정 |
| vf_csetup.f.md:127–185 | 시작 시 57행 JD 루프 및 60행 IF 안. | 시작 시 `DO 140 JD=1,4`(57) 안이며 219행 `140 CONTINUE`에서 닫힌다. 시작 시 `IF (IBCTYP(1,JD).EQ.1) THEN`(60) 안이며 128행 ELSEIF를 거쳐 144행 `ENDIF`에서 닫힌다. 이 IF 사슬에는 ELSE가 없다. | 57·60·128·144·219 | 보완 |
| vf_csetup.f.md:186–251 | 시작 시 57행 JD 루프·154행 IB 비영 분기·155행 방향 분기 안. | 시작 시 `DO 140 JD=1,4`(57) 안이며 219행 `140 CONTINUE`에서 닫힌다. 시작 시 `IF (IB.NE.0) THEN`(154) 안이며 218행 `ENDIF`에서 닫힌다. 시작 시 `IF (JD.EQ.1 .OR. JD.EQ.2) THEN`(155) 안이며 186행 ELSE를 거쳐 217행 `ENDIF`에서 닫힌다. 239–249행의 `IF (INDB(3,L).EQ.6) THEN` 및 `ELSEIF (INDB(3,L).EQ.8) THEN` 사슬에는 ELSE가 없다. | 57·154–155·186·217–219·239–249 | 보완 |
| vf_csetup.f.md:252–301 | 조파 소스(source)의 필수값을 검사한다. N=-3이며 MTBTYP=3이면 오류를 호출한다. | `IF (ISCTYP(1).NE.0) THEN` 안에서 조파 소스(source)의 필수값을 검사한다. 이 IF는 300행에서 닫힌다. 그 안에서 N=-3이며 MTBTYP=3이면 `CALL VF_A2ERR('VF_CSETUP','(WAVE-SRC) MTBTYP ERROR.')`를 실행한다. | 254–300 | 보완 |
| vf_cvort.f.md:69–111 | 시작 시 1–2행 VF_CVORT 루틴 및 67행 LON=0 분기 안. | 시작 시 `IF (LON.EQ.0) THEN`(67) 안이며 202행 `ENDIF`에서 닫힌다. | 67·202 | 보완 |
| vf_cvort.f.md:69–111 | 내부 면의 속도는 격자 폭 가중 보간(interpolation)을 쓰고 경계면은 BCW·BCV를 쓴다. | `IND.EQ.0`이면 YY(2,*)·YY(6,*) 또는 ZZ(2,*)·ZZ(6,*)를 사용하는 79–81·87–89·95–97·103–105행의 식으로 값을 정한다. 각 ELSE에서는 BCW(IND) 또는 BCV(IND)를 쓴다. 해석: 이 식은 격자 폭을 가중치로 쓰는 보간으로 볼 수 있으나 이 구간에는 YY·ZZ의 두 번째와 여섯 번째 성분 정의가 없다. | 77–108 | 정정 |
| vf_cvort.f.md:112–154 | 시작 시 67행 LON=0 분기 및 70행 성분 선택 IF 안. | 시작 시 `IF (LON.EQ.0) THEN`(67) 안이며 202행 `ENDIF`에서 닫힌다. 시작 시 `IF (ISW.EQ.1) THEN`(70)에서 시작하는 IF 사슬 안이며 200행 `ENDIF`에서 닫힌다. | 67·70·200·202 | 보완 |
| vf_cvort.f.md:155–216 | 시작 시 67행 LON=0 분기 및 70행 성분 선택 IF 안. | 시작 시 `IF (LON.EQ.0) THEN`(67) 안이며 202행 `ENDIF`에서 닫힌다. 시작 시 `IF (ISW.EQ.1) THEN`(70)에서 시작하는 IF 사슬 안이며 200행 `ENDIF`에서 닫힌다. | 67·70·200·202 | 보완 |
| vf_cwlvl.f.md:1–34 | VOF 함수의 수직 적분으로 초기 정수면 기준 수위 변동을 구한다. | VOF 함수의 z방향 합산으로 초기 수면 기준 수위 변동을 구한다(같은 원문 38–49행). | 38–49 | 정정 |
| vf_cwlvl.f.md:35–67 | NF=-1 셀은 전체 두께를 더하고 나머지는 FF 비율을 곱한다. | `NF(IP,JP,K).EQ.-1`이면 `ZZ(2,K)*1.0D0`을 더한다. 나머지는 `ZZ(2,K)*FF(IP,JP,K)`를 더한다. 해석: ZZ(2,K)를 셀 두께로 읽으면 각각 전체 두께와 FF 비율을 곱한 두께에 해당하지만 이 구간에는 ZZ(2,K)의 정의가 없다. | 41–45 | 정정 |
| vf_cwmak0.f.md:28–71 | 나머지는 오류다. | 나머지는 `CALL VF_A2ERR('VF_CWMAK0','P.G ERROR.')`를 실행한다. | 60–61 | 보완 |
| vf_cwmak1.f.md:25–49 | 그 외는 오류다. | 그 외는 `CALL VF_A2ERR('VF_CWMAK1','P.G ERROR.')`를 실행한다. | 38–39 | 보완 |
| vf_cwmak2.f.md:27–55 | 그 외는 오류다. | 그 외는 `CALL VF_A2ERR('VF_CWMAK2','P.G ERROR.')`를 실행한다. | 44–45 | 보완 |
| vf_cwmsrc.f.md:101–155 | 소스 면이 지역 범위에 있으면 수직 VOF 함수 적분으로 현재 수위를 구한다. | `IJP.NE.0` 안에서 `N.NE.-3 .OR. MTBTYP.EQ.1`일 때 현재 수위를 계산한다. K=2부터 NUMK-1까지 NW=-1이면 ZZ(2,K)를 더한다. NW=0이면 ZZ(2,K)*FF(I,J,K)를 더한다. 앞의 두 조건이 거짓이고 NW≠8이면 같은 항을 더한 뒤 `GOTO 110`으로 125행 `110 CONTINUE`에 이동하여 K 루프를 벗어난다. 이 NW 조건 사슬에는 ELSE가 없으며 NW=8에서는 누적하지 않는다. | 102–130 | 보완 |
| vf_cwmtb1.f.md:27–64 | 양 끝 위상 밖에서는 끝점 가중치를 쓴다. | 첫 위상 이하이거나 마지막 위상 이상이면 끝점 가중치를 쓴다. | 29–36 | 정정 |
| vf_cwmtb12.f.md:27–64 | 양 끝 위상 밖에서는 끝점 가중치를 쓴다. | 첫 위상 이하이거나 마지막 위상 이상이면 끝점 가중치를 쓴다. | 29–36 | 정정 |
| vf_cwmtb2.f.md:30–54 | 표 밖 좌표에는 끝점 가중치를 쓴다. | 첫 z좌표 이하이거나 마지막 z좌표 이상이면 끝점 가중치를 쓴다. | 31–38 | 정정 |
| vf_cwmtb22.f.md:31–55 | 표 밖 좌표에는 끝점 가중치를 쓴다. | 첫 z좌표 이하이거나 마지막 z좌표 이상이면 끝점 가중치를 쓴다. | 32–39 | 정정 |
| vf_cwzero.f.md:35–59 | 두 끝점 위상이 같으면 기본값 상태로 종료한다. | 앞의 수위 절댓값 검사에서 빠져나가지 않고 `R4TN1.EQ.R4TN2`이면 `GOTO 9000`으로 79행 `9000 CONTINUE`에 이동한다. 이 경우 WVZERO는 33행의 기본값을 유지한다. 42·56행의 `GOTO 9000`도 같은 레이블로 이동한다. | 33·40–58·79 | 보완 |
| vf_f1cal.f.md:154–195 | 해저 변화 보정 후 수평 플럭스를 FFLXX·FFLXY에 보관한다. | `ISEABT.NE.0`이면 `CALL VF_FSEABT(XX,YY,ZZ,FF,GGV,DELH,DELH_IN,NF)`으로 지형 변화에 따른 F 보정을 수행한다. 이 조건 분기 뒤 수평 플럭스를 FFLXX·FFLXY에 보관한다. | 165–175 | 정정 |
| vf_faulti.f.md:55–99 | 각도는 D2R을 곱한다. 경도·위도 극값의 중점으로 XOR·YOR를 구하고 필요하면 LB2LB로 좌표계를 변환한다. | STR·DIP·SLIP·B·L에는 D2R을 곱하여 FPARAM에 저장한다. L과 B의 극값 중점에 D2R을 곱하여 XOR와 YOR를 구한다. `ISYSTEM.NE.JSYSTEM`이면 `CALL LB2LB(XOR,YOR,L,B,ISYSTEM,JSYSTEM)` 뒤 XOR=L과 YOR=B를 대입한다. 해석: D2R을 곱하는 값은 각도이며 L·B는 경도·위도로 보이지만 이 구간에는 해당 정의가 없다. | 67–94 | 정정 |
| vf_faulti.f.md:100–127 | 시간 0 자료 또는 TIM1 뒤의 자료에서 멈춘다. 자료가 끝나면 TIMESB=1.D+99다. 열기·읽기 실패는 VF_A2ERR다. | `TIME.EQ.TIMESB.AND.TIMESB.EQ.0.0D0`이면 TIM1=TIMESB를 대입하고 `GOTO 30`으로 117행에 이동한다. 앞 조건이 거짓이고 `TIM1.LT.TIMESB`이면 같은 레이블로 이동한다. 이 IF 사슬에는 ELSE가 없다. 루프를 소진하면 종료 로그를 쓰고 TIMESB=1.D+99를 대입한다. 열기 실패의 900번 레이블에서는 `CALL VF_A2ERR('VF_FAULTI','CANNOT OPEN fault_cad.txt.')`를 실행한다. 읽기 실패의 910번 레이블에서는 `WRITE(ILPFIL,*) 'LINE NUMBER =',NFLT+1` 뒤 `CALL VF_A2ERR('VF_FAULTI','CANNOT READ fault_cad.txt.')`를 실행한다. | 102–126 | 정정 |
| vf_faultt.f.md:1–54 | 지역 담당 셀의 중심 좌표를 EN2LB로 변환한다. 좌표계가 다르면 LB2LB를 더 호출하고 결과를 지역 배열에 저장한다. | `X1=0.5D0*(XX(1,I)+XX(1,I+1))`과 `Y1=0.5D0*(YY(1,J)+YY(1,J+1))`을 계산하여 EN2LB에 넘긴다. `ISYSTEM.NE.JSYSTEM`이면 LB2LB를 더 호출한다. 결과를 L1ARRAY·B1ARRAY에 저장한다. 해석: X1·Y1은 셀 중심 좌표로 볼 수 있지만 이 구간에는 XX·YY의 첫 번째 성분 정의가 없다. | 37–53 | 정정 |
| vf_faultt.f.md:55–99 | 현재 단층의 주향(strike)·경사(dip)·미끄럼각(slip angle) 삼각함수를 만든다. | FPARAM의 4·5·6번째 성분을 STR·DIP·SLIP에 복사한다. 각 값의 SIN·COS를 PARAM2에 저장한다. 해석: STR·DIP·SLIP은 주향·경사·미끄럼각으로 보이지만 이 구간에는 해당 정의가 없다. | 57–65 | 정정 |
| vf_fbubup.f.md:34–57 | 위에서 아래로 각 층의 두께/WBUB를 통과 시간으로 구한다. 경과 시간이 통과 시간보다 크면 해당 층 기포 셀과 위 셀 사이에서 FMOVE만큼 물을 아래로 옮긴다. | K=NUMK-2부터 2까지 감소시키며 `DTBUB=ZZ(2,K)/WBUB`를 계산한다. `TNOW-TBUB(K).GT.DTBUB` 안에서 `FF(I,J,K).LT.FUPPER .AND. NF(I,J,K ).EQ. 0 .AND. NF(I,J,K1).NE.-1`인 셀만 FF를 갱신한다. `FF(I,J,K1)`에서 FMOVE/V1을 빼고 `FF(I,J,K)`에 FMOVE/V0을 더한다. 해석: ZZ(2,K)를 층 두께로 읽으면 DTBUB는 통과 시간에 해당하지만 이 구간에는 ZZ(2,K)의 정의가 없다. | 35–48 | 정정 |
| vf_fconv.f.md:55–105 | x방향 유효 면에서 속도 부호로 도너(donor)와 억셉터(acceptor)를 정한다. | `INDX(I,J,K).NE.-1`인 면에서 `C=DTNOW*GGX(I,J,K)*UU(I,J,K)`의 부호로 도너(donor)와 억셉터(acceptor) 인덱스를 정한다. | 59–72 | 정정 |
| vf_fconv.f.md:55–105 | 부족한 공급량을 CFX로 보정하고 MIN(FVX,FVM)만큼 플럭스를 누적한다. | `CFX=MAX((FDM-FAD)*AC-(FDM-FD)*V,0.0D0)`으로 보정량을 구한다. FLFU에서 `DBLE(LSN)*MIN(FVX,FVM)`을 뺀다. | 94–99 | 정정 |
| vf_fconv.f.md:106–156 | 이 방향의 상태 선택 집합과 YY 기반 부피 계수를 원문으로 기록한다. | 이 방향의 상태 선택 집합과 `V=YY(2,LD)*GGV(I,LD,K)` 또는 `V=YY(2,LD)`를 원문으로 기록한다. | 124–144 | 정정 |
| vf_fconv.f.md:157–215 | ZZ 기반 부피 계수와 상태 선택 집합으로 FLFW 및 NLIM을 갱신한다. | `V=ZZ(2,LD)*GGV(I,J,LD)` 또는 `V=ZZ(2,LD)`와 상태 선택 집합으로 FLFW 및 NLIM을 갱신한다. | 175–202 | 정정 |
| vf_faulti.f.md:55–99 | 후속 사실에서도 B·L을 경도·위도로 단정했다. | 후속 사실의 변수명을 B·L로 고쳤다. | 57–60·85–89 | 정정 |
| vf_fconvs.f.md:83–174 | S1은 거리 합에 대한 FM-FP이다. | `DM+DP.LE.ZERO`이면 S1=0.0D0이다. 그 외에는 `S1=(FM-FP)/(DM+DP)`이다. 112–124행과 150–162행의 NF0 조건 사슬에는 ELSE가 없다. | 112–124·150–173 | 정정 |
| vf_fconvs.f.md:175–257 | 시작 시 84·85·86행 K·J·I 루프와 90행 계면 대상 셀 분기 안. | 시작 시 `DO 220 K=2,NUMK-1`(84), `DO 210 J=MYJS,MYJE`(85), `DO 200 I=MYIS,MYIE`(86) 안이다. 각 루프는 387·386·385행의 대응 CONTINUE에서 닫힌다. 시작 시 `IF (NF0.GT.0 .AND. FF0.GE.FLOWER .AND. FF0.LE.FUPPER) THEN`(90) 안이며 384행 `ENDIF`에서 닫힌다. | 84–90·384–387 | 보완 |
| vf_fconvs.f.md:258–340 | 시작 시 84·85·86행 K·J·I 루프와 90행 계면 대상 셀 분기 안. | 시작 시 `DO 220 K=2,NUMK-1`(84), `DO 210 J=MYJS,MYJE`(85), `DO 200 I=MYIS,MYIE`(86) 안이다. 각 루프는 387·386·385행의 대응 CONTINUE에서 닫힌다. 시작 시 `IF (NF0.GT.0 .AND. FF0.GE.FLOWER .AND. FF0.LE.FUPPER) THEN`(90) 안이며 384행 `ENDIF`에서 닫힌다. | 84–90·384–387 | 보완 |
| vf_fconvs.f.md:341–394 | 시작 시 84·85·86행 K·J·I 루프와 90행 계면 대상 셀 분기 안. | 시작 시 `DO 220 K=2,NUMK-1`(84), `DO 210 J=MYJS,MYJE`(85), `DO 200 I=MYIS,MYIE`(86) 안이다. 각 루프는 387·386·385행의 대응 CONTINUE에서 닫힌다. 시작 시 `IF (NF0.GT.0 .AND. FF0.GE.FLOWER .AND. FF0.LE.FUPPER) THEN`(90) 안이며 384행 `ENDIF`에서 닫힌다. | 84–90·384–387 | 보완 |
| vf_fconvs.f.md:175–257 | J-1·J+1 이웃에 대해 경계값 또는 격자 폭 가중 VOF 함수로 FM·FP를 구한다. 셀 상태에 맞는 옆 셀을 추가하는 분기를 포함한다. | J-1·J+1 이웃의 NFL과 NF0에 따라 FM·FP·DM·DP를 정한다. 209·247행에서는 YY(2,*)·YY(6,*)·DD0를 사용하는 식을 적용한다. 195–207행과 233–245행의 NF0 조건 사슬에는 ELSE가 없다. | 175–249 | 정정 |
| vf_fconvs.f.md:258–340 | 경계·기체·유체 및 다른 표면 셀 처리 조건을 각각 기록한다. | NFL=-1·8·0과 나머지 값의 처리 조건을 각각 기록한다. 278–290행과 316–328행의 NF0 조건 사슬에는 ELSE가 없다. | 263–332 | 보완 |
| vf_fconvs.f.md:341–394 | 법선을 단위 길이로 바꾼다. | `RN.GE.ZERO`일 때 S1·S2·S3에 `1.0D0/SQRT(RN)`을 곱한다. | 342–347 | 정정 |
| vf_fconvs.f.md:395–475 | 경계면·기울기 없음·x성분 없는 종류 6은 도너·억셉터 방법(donor-acceptor method)을 쓴다. 나머지는 법선 부호와 유속 부호로 절단 폭 DD0를 고르고 | `INDX(I,J,K).GT.1 .OR. ISTYP(LD,J,K).LE.0 .OR. ISTYP(LD,J,K).EQ.6`이면 도너·억셉터 방법(donor-acceptor method)을 쓴다. 나머지는 SX의 부호와 `C=DTNOW*GGX(I,J,K)*UU(I,J,K)`에서 정한 LSN으로 DD0를 고르고 | 402–416·446–449 | 정정 |
| vf_fconvs.f.md:476–555 | 종류 5 등은 도너·억셉터 방법을 쓴다. 기하학적 경사 처리 종류 3·6·7에서는 해당 평면·입체 적분 루틴을 호출한다. | `INDY(I,J,K).GT.1 .OR. ISTYP(I,LD,K).LE.0 .OR. ISTYP(I,LD,K).EQ.5`이면 도너·억셉터 방법을 쓴다. ELSE에서 종류 3·6이면 VF_FSLP2F를 호출한다. 종류 7이면 VF_FSLP3F를 호출한다. 해석: 두 루틴은 평면·입체 적분을 수행하는 것으로 보이지만 이 구간에는 각 루틴 본체가 없다. | 495–550 | 보완 |
| vf_fconvs.f.md:556–644 | 종류 3 등은 도너·억셉터 방법을 쓴다. | `INDZ(I,J,K).GT.1 .OR. ISTYP(I,J,LD).LE.0 .OR. ISTYP(I,J,LD).EQ.3`이면 도너·억셉터 방법을 쓴다. | 575–576 | 보완 |
| vf_fcut01.f.md:33–67 | 셀 부피에 공극률을 곱한다. FF>FUPPER이면 1, FF<FLOWER이면 0으로 바꾸고 변화 전후의 체적 차를 FCUT에 더한다. 보정 후 물 체적은 FSUM에 더한다. | `V=XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)`를 계산한다. FF>FUPPER이면 1로 바꾼다. 앞 조건이 거짓이고 FF<FLOWER이면 0으로 바꾼다. 이 IF 사슬에는 ELSE가 없다. FCUT에는 변경 전 FF에서 변경 후 FF를 뺀 값에 V를 곱하여 더한다. FSUM에는 변경 후 FF*V를 더한다. 해석: XX·YY·ZZ의 두 번째 성분을 셀 폭으로 읽으면 V는 공극 부피이며 FSUM은 물 체적의 합이지만 이 구간에는 해당 성분 정의가 없다. | 39–48 | 보완 |
| vf_fdropf.f.md:1–79 | FF>FLOWER이고 NF=8인 새 물방울의 세 방향 처리 시각을 TNOW로 초기화한다. | `FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8` 안에서 `DROPTX(I,J,K).LT.0.0D0`일 때 세 방향 처리 시각을 TNOW로 초기화한다. | 70–75 | 보완 |
| vf_fdropf.f.md:80–152 | 시작 시 1–3행 VF_FDROPF 루틴·66·67·68행 K·J·I 루프·70행 물방울 분기·72행 신규 물방울 분기 안. | 시작 시 `DO 120 K=2,NUMK-1`(66), `DO 110 J=MYJS,MYJE`(67), `DO 100 I=MYIS,MYIE`(68) 안이다. 각 루프는 295·294·293행의 대응 CONTINUE에서 닫힌다. 시작 시 `IF (FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8) THEN`(70) 안이며 292행 `ENDIF`에서 닫힌다. 시작 시 `IF (DROPTX(I,J,K).LT.0.0D0)THEN`(72) 안이며 253행 ELSEIF를 거쳐 283행 `ENDIF`에서 닫힌다. 이 안쪽 IF 사슬에는 ELSE가 없다. | 66–72·253·283·292–295 | 보완 |
| vf_fdropf.f.md:153–233 | 시작 시 66·67·68행 K·J·I 루프·70행 물방울 분기·72행 신규 물방울 분기 안. | 시작 시 `DO 120 K=2,NUMK-1`(66), `DO 110 J=MYJS,MYJE`(67), `DO 100 I=MYIS,MYIE`(68) 안이다. 각 루프는 295·294·293행의 대응 CONTINUE에서 닫힌다. 시작 시 `IF (FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8) THEN`(70) 안이며 292행 `ENDIF`에서 닫힌다. 시작 시 `IF (DROPTX(I,J,K).LT.0.0D0)THEN`(72) 안이며 253행 ELSEIF를 거쳐 283행 `ENDIF`에서 닫힌다. 이 안쪽 IF 사슬에는 ELSE가 없다. | 66–72·253·283·292–295 | 보완 |
| vf_fdropf.f.md:234–303 | 시작 시 66·67·68행 K·J·I 루프·70행 물방울 분기·72행 신규 물방울 분기 안. | 시작 시 `DO 120 K=2,NUMK-1`(66), `DO 110 J=MYJS,MYJE`(67), `DO 100 I=MYIS,MYIE`(68) 안이다. 각 루프는 295·294·293행의 대응 CONTINUE에서 닫힌다. 시작 시 `IF (FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8) THEN`(70) 안이며 292행 `ENDIF`에서 닫힌다. 시작 시 `IF (DROPTX(I,J,K).LT.0.0D0)THEN`(72) 안이며 253행 ELSEIF를 거쳐 283행 `ENDIF`에서 닫힌다. 이 안쪽 IF 사슬에는 ELSE가 없다. | 66–72·253·283·292–295 | 보완 |
| vf_fdropf.f.md:366–400 | 시작 시 305행 L 루프·336행 I 루프·338행 K 루프·339행 J 루프 안. | 시작 시 `DO 290 L=1,2`(305), `DO 250 I=IST,IEN,IDL`(336), `DO 240 K=2,NUMK-1`(338), `DO 230 J=MYJS,MYJE`(339) 안이다. 각 루프는 404·387·386·385행의 대응 CONTINUE에서 닫힌다. | 305·336–339·385–387·404 | 보완 |
| vf_fdropf.f.md:366–400 | 물이 없어진 셀의 물방울 기록을 지운다. | `FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8`이 거짓이면 물방울 기록을 초기화한다. DROPTX에는 -1.0D10을 넣고 나머지 저장값에는 0.0D0을 넣는다. | 367–384 | 정정 |
| vf_fdropf.f.md:401–444 | 시작 시 305행 x방향 L 루프·389·390·391행 가중 평균 K·J·I 루프 안. | 시작 시 `DO 290 L=1,2`(305), `DO 280 K=2,NUMK-1`(389), `DO 270 J=MYJS,MYJE`(390), `DO 260 I=MYIS,MYIE`(391) 안이다. 각 루프는 404·403·402·401행의 대응 CONTINUE에서 닫힌다. | 305·389–391·401–404 | 보완 |
| vf_fdropf.f.md:445–522 | 시작 시 415행 y방향 L 루프 안. | 시작 시 `DO 390 L=1,2`(415) 안이며 514행 `390 CONTINUE`에서 닫힌다. | 415·514 | 보완 |
| vf_fdropf.f.md:445–522 | 남은 물의 가중값을 더하고 물이 없어진 셀의 기록을 지운다. | `FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8`이면 남은 물의 가중값을 더한다. 거짓이면 DROPTX에는 -1.0D10을 넣고 나머지 저장값에는 0.0D0을 넣는다. | 477–494 | 정정 |
| vf_fdropf.f.md:523–596 | 시간이 충족되면 FF를 옮기고 수직 속도에 -DT*GRZ0를 적용한 가중값을 도착 셀에 더한다. | `FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8 .AND. NF(I,J,K1).NE.-1` 안에서 DT를 계산한다. `DT.GT.0.0D0 .AND. (TNOW-DROPTZ(I,J,K)).GT.DT`이면 FF를 옮긴다. 그 안에서 `NF(I,J,K1).EQ.8`일 때만 수직 속도에서 DT*GRZ0를 뺀 가중값을 도착 셀에 더한다. | 559–595 | 보완 |
| vf_fdropf.f.md:597–653 | 시작 시 525행 z방향 L 루프·552행 K 루프·555행 J 루프·556행 I 루프 안. | 시작 시 `DO 490 L=1,2`(525), `DO 450 K=KST,KEN,KDL`(552), `DO 440 J=MYJS,MYJE`(555), `DO 430 I=MYIS,MYIE`(556) 안이다. 각 루프는 644·618·617·616행의 대응 CONTINUE에서 닫힌다. | 525·552–556·616–618·644 | 보완 |
| vf_fdropf.f.md:597–653 | 빈 셀 기록을 지우고 가중 평균을 계산한다. | `FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8`이 거짓이면 DROPTX에는 -1.0D10을 넣고 나머지 저장값에는 0.0D0을 넣는다. 가중 평균은 이 조건이 참인 셀에서 계산한다. | 598–630 | 정정 |
| vf_feuler.f.md:42–67 | 격자 역폭을 곱한 세 방향 플럭스 차와 DTNOW*QF를 더해 DF를 구한다. | 각 방향 플럭스 차에 XX(4,I)·YY(4,J)·ZZ(4,K)를 각각 곱한 값과 DTNOW*QF를 더해 DF를 구한다. 해석: 이 계수를 격자 역폭으로 볼 수 있지만 이 구간에는 배열의 네 번째 성분 정의가 없다. | 48–51 | 정정 |
| vf_fgene.f.md:1–40 | ISCTYP(1)의 부호로 x 또는 y방향 지역 소스 면을 정한다. | ISCTYP(1)의 부호로 x 또는 y방향 지역 소스 면을 정한다. 35–39행의 IF 사슬에는 ELSE가 없다. ISCTYP(1)=0이면 IWS와 JWS는 초기값 0을 유지한다. | 33–39 | 보완 |
| vf_fgene.f.md:41–79 | 소스 면에서 유체 셀은 격자 역폭과 소스 유속의 2배에 FF를 곱해 QF에 더한다. 표면 셀도 같은 양을 더한 뒤 해당 수직 루프를 빠져나온다. NF=-1과 8은 더하지 않는다. | `IWS.EQ.I`이면 NF=0에서 `Q=2.0D0*XX(4,I)*SRCUV(J,K)`와 `QF(I,J,K)=QF(I,J,K)+FF(I,J,K)*Q`를 계산한다. `JWS.EQ.J`이면 NF=0에서 `Q=2.0D0*YY(4,J)*SRCUV(I,K)`와 같은 QF 누적식을 계산한다. 각 조건 안에서 NF가 -1·0·8 이외이면 해당 방향의 같은 식을 계산한 뒤 `GOTO 110`으로 68행에 이동하여 K 루프를 벗어난다. 두 NF 조건 사슬에는 ELSE가 없다. NF=-1과 8에서는 QF에 더하지 않는다. | 45–68 | 정정 |
| vf_fmod1.f.md:45–83 | VF_P3SRI1로 교환한다. | 59–77행의 N 조건 사슬에는 ELSE가 없다. N이 1–6 이외이면 두 이웃 인덱스는 자기 셀 좌표를 유지한다. VF_P3SRI1로 교환한다. | 53–82 | 보완 |
| vf_fmod1.f.md:84–150 | NLIM=1인 이웃만 물 체적 합에 포함한다. | 98–116행의 N 조건 사슬에는 ELSE가 없다. NLIM=1인 이웃만 물 체적 합에 포함한다. | 98–124 | 보완 |
| vf_fmod1.f.md:151–209 | 표면 FF>1이면 | 165–183행의 N 조건 사슬에는 ELSE가 없다. 표면 FF>1이면 | 165–197 | 보완 |
| vf_fnfini.f.md:44–105 | FF<FLOWER인 셀의 여섯 방향 값을 | NF≠-1이고 FF<FLOWER인 셀의 여섯 방향 값을 | 48–49 | 보완 |
| vf_fnfini.f.md:106–151 | 여섯 이웃 중 기체 NF=8이 있는 계산 셀을 잠정 표면 7로 만들고 INDS에 넣는다. | 자기 NF가 -1도 8도 아닌 셀에서 여섯 이웃 중 NF=8이 하나라도 있으면 자기 NF를 7로 만들고 INDS에 넣는다. | 116–126 | 정정 |
| vf_fnfprv.f.md:42–101 | 시작 시 1행 VF_FNFPRV 루틴·34행 표면 목록 L 루프 안. | 시작 시 `DO 100 L=1,NUMS`(34) 안이며 225행 `100 CONTINUE`에서 닫힌다. | 34·225 | 보완 |
| vf_fnfprv.f.md:102–161 | 시작 시 34행 표면 목록 L 루프 안. | 시작 시 `DO 100 L=1,NUMS`(34) 안이며 225행 `100 CONTINUE`에서 닫힌다. | 34·225 | 보완 |
| vf_fnfprv.f.md:162–236 | 시작 시 34행 표면 목록 L 루프 안. | 시작 시 `DO 100 L=1,NUMS`(34) 안이며 225행 `100 CONTINUE`에서 닫힌다. | 34·225 | 보완 |
| vf_fpvcip.f.md:110–141 | 여러 프로세스(process)에서는 각 순위(rank)에 대한 집계로 지역 영역 번호에 NS를 더하고 영역 수를 합한다. MAXPVC를 넘으면 오류다. | `NPROCS.NE.1`이면 IP=0부터 NPROCS-1까지 집계한다. `MYRANK.GE.IP`인 프로세스는 N=0을 넘긴다. ELSE의 `MYRANK<IP`인 프로세스는 N=NPVCB를 넘긴다. `MYRANK.EQ.IP`인 프로세스만 합계 I를 NS에 저장한다. `IPVC(IJK).GE.1`인 지역 영역 번호에 NS를 더한다. 이어 영역 수를 합한다. `NPVCB.GT.MAXPVC`이면 `CALL VF_A2ERR('VF_FPVCIP','AREA IS FULL.')`를 실행한다. | 111–134 | 보완 |
| vf_fpvcip.f.md:206–266 | 빈 번호를 압축하고 모든 IPVC를 바꾼다. | 빈 번호를 압축한다. 전 격자를 순회하면서 `IPVC(IJK).GE.1`인 값만 `NLIM(IPVC(IJK))`로 바꾼다. | 220–247 | 정정 |
| vf_fpvcip.f.md:206–266 | 반복 횟수가 MAXPVC를 넘으면 오류이며 변경이 있으면 다시 1000번으로 간다. | `NSWAP.GT.MAXPVC`이면 `CALL VF_A2ERR('VF_FPVCIP','P.G ERROR.')`를 실행한다. `ISWAP.GT.0`이면 `GOTO 1000`으로 138행에 돌아간다. | 138·256–257 | 보완 |
| vf_fpvcpp.f.md:115–150 | 표면 셀은 V*(1-FF)만 영역 기체 체적에 더한다. | NF=8 분기가 거짓이고 `NF(I,J,K).GE.1`이면 V*(1-FF)만 PVCVES에 더한다. 이 IF 사슬에는 ELSE가 없다. | 119–134 | 보완 |
| vf_fpvcpp.f.md:151–194 | 기체 셀에서 기존 PPPVC가 1.0D30과 다르면 그 압력의 체적 평균을 구한다. 그 외 셀은 PP를 별도로 평균한다. 열린 경계 접촉 영역의 상대 압력은 0이다. 닫힌 영역은 PAV와 PVCP0 및 PVCGM*DTNOW*PVCDIV로 압력을 갱신한다. | NF=8인 셀만 압력 합에 포함한다. 그 안에서 PPPVC≠1.0D30이면 V*PPPVC와 V를 PVCPES·PVCVES에 누적한다. PPPVC=1.0D30이면 V*PP와 V를 PVCPFS·PVCVFS에 누적한다. `IPVCBC(L).NE.0`이면 PVCPES=0.0D0이다. ELSE에서는 PVCVES>0이면 PVCPES/PVCVES를 PAV에 넣고, 그렇지 않으면 PVCPFS/PVCVFS를 넣는다. 이어 191행 식으로 PVCPES를 갱신한다. | 155–193 | 정정 |

정정 32, 보완 38, 이상 없음 47

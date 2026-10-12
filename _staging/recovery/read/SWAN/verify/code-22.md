# SWAN swanparll.ftn 전수 대조 — code-22

검증일: 2026-10-13.

대상 기록의 구간 행마다 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
원문 출력은 구간별로 최대 172행이었다.
아래 원문 행 수는 대상 기록 표의 구간 경계에서 계산했다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 범위 | 대조한 원문 행 수 |
|---|---:|---|---:|
| [swan/src/swanparll.ftn.md](../swan/src/swanparll.ftn.md) | 58 | 2812–5773 | 2962 |

요청 범위는 원문 2888–5773행이다.
경계에 걸친 기록의 2812–2951 구간을 통째로 대조했다.
따라서 대조 범위에는 요청 시작 행 앞의 76행이 포함된다.

원문은 `models/SWAN/raw/source_code/swan/src/swanparll.ftn`이다.
전처리 접두부 제거 규칙은 `models/SWAN/raw/source_code/swan/switch.pl` 82–105행과 대조했다.
옵션 이름과 처리 순서는 같은 파일의 1–44행 및 78–106행에서 확인했다.

정정과 보완의 집계 단위는 대상 기록의 구간 행이다.
정정과 보완이 함께 있는 8행은 두 항목에 각각 집계했다.
수정한 서로 다른 구간 행은 47행이다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| swan/src/swanparll.ftn.md:2812–2951 | JAC·TIMG 안내만 기재. | [보완] TIMG를 먼저 처리하므로 JAC 제거 뒤에도 주석이 남음을 명시. | 2915–2916; switch.pl 84–85 |
| swan/src/swanparll.ftn.md:2952–3002 | JAC·TIMG 호출로 기술. 이웃 위치와 블록 포인터 계산식을 서술로 축약. | [정정·보완] 호출 행이 주석으로 남는 전처리 순서를 명시. IPNB·IDOM·ISTART·NOVLU·WORK·태그 대입을 원문 인용. | 2962–2995; switch.pl 84–85 |
| swan/src/swanparll.ftn.md:3003–3041 | JAC·TIMG 호출로 기술. 수신 대상과 저장 인덱스 식은 설명으로만 기재. | [정정·보완] SWTSTO 행이 주석으로 남음을 명시. 블록 포인터·태그·FIELD 대입식을 원문 인용. | 3009–3038; switch.pl 84–85 |
| swan/src/swanparll.ftn.md:3042–3166 | WFR·TIMG 안내만 기재. | [보완] TIMG 선처리로 WFR 제거 뒤에도 주석이 남음을 명시. | 3134–3135; switch.pl 84–86 |
| swan/src/swanparll.ftn.md:3167–3201 | WFR·TIMG 호출로 기술. 송신 포인터와 저장식의 백틱 인용 누락. | [정정·보완] SWTSTA 행이 주석으로 남음을 명시. IDOM·ISTART·NOVLU·WORK·태그 대입을 원문 인용. | 3174–3196; switch.pl 84–86 |
| swan/src/swanparll.ftn.md:3202–3229 | WFR·TIMG 호출로 기술. 수신 포인터와 저장식의 백틱 인용 누락. | [정정·보완] SWTSTO 행이 주석으로 남음을 명시. IDOM·ISTART·NOVLU·FIELD·태그 대입을 원문 인용. | 3208–3226; switch.pl 84–86 |
| swan/src/swanparll.ftn.md:3351–3393 | 이웃 위치·IDOM·ITAG·AC2 대입을 서술로 축약. | [보완] 이웃 인덱스와 메시지 태그 및 수신 자료 대입을 원문 인용. | 3360–3386 |
| swan/src/swanparll.ftn.md:3515–3559 | 이웃 위치와 송신 배열·태그를 서술로 축약. | [보완] IPNB·IDOM 인덱스와 WORK 및 ITAG 대입을 원문 인용. | 3524–3548 |
| swan/src/swanparll.ftn.md:3719–3748 | IAMMASTER 종료 행을 생략한 채 두 SWGATHER 호출을 기술. | [보완] IAMMASTER가 3724·3740행에서 닫힘을 명시. 두 수집 호출은 해당 조건 밖임을 명시. | 3720–3725·3731–3746 |
| swan/src/swanparll.ftn.md:3749–3777 | 오프셋 초기값과 시작 경계 상수를 백틱 없이 기재. | [보완] IOFF1·IOFF2의 0과 MXFGL·MYFGL의 1 대입을 원문 인용. | 3753–3754·3759·3764 |
| swan/src/swanparll.ftn.md:3778–3800 | 경계 상수의 백틱 인용과 바깥 가로 크기 조건의 종료 행 누락. | [보완] MXFGL·MYFGL의 1 대입을 원문 인용. 3798·3799행의 종료 대상을 구분. | 3780·3785·3798–3799 |
| swan/src/swanparll.ftn.md:3801–3838 | 압축 배열 복사의 오프셋 대입을 서술로만 기재. | [보완] FLDC(INDXC+IOFF1)를 사용하는 대입식을 원문 인용. | 3818 |
| swan/src/swanparll.ftn.md:4011–4048 | 시간 반복 시작값을 백틱 없이 기재. | [보완] IT0의 0·1 대입을 원문 인용. | 4023·4025 |
| swan/src/swanparll.ftn.md:4049–4083 | LCOMPGRD의 분기별 논리값 대입을 축약. | [보완] TRUE·FALSE 대입문을 원문 인용. | 4071·4073 |
| swan/src/swanparll.ftn.md:4084–4105 | 분기별 상수 대입의 백틱 인용과 ELSE 부재 누락. | [보완] MXK·MYK의 0·1 대입을 원문 인용. PSTYPE 사슬에 ELSE가 없음을 명시. | 4084–4098 |
| swan/src/swanparll.ftn.md:4106–4146 | MXF=MYF=1로 묶어 기재. | [보완] MXF·MYF의 대입문과 각각의 원문 행을 명시. | 4122–4123 |
| swan/src/swanparll.ftn.md:4147–4189 | XC·YC 기본값 인용과 격자 분기 사슬의 ELSE 부재 누락. | [보완] 기본값을 원문 인용. 파일 부재 오류 내용을 명시. OPTG 분기에 ELSE가 없음을 명시. | 4150–4153·4165–4168·4183–4188 |
| swan/src/swanparll.ftn.md:4190–4215 | NCF 선택으로만 활성 조건을 기술. | [보완] 실제 선택 스위치 -netcdf와 미선택 경로를 명시. | 4203–4213; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:4424–4454 | NLINES 초기값을 백틱 없이 기재. | [보완] NLINES = 0을 원문 인용. | 4430 |
| swan/src/swanparll.ftn.md:4455–4478 | RTYPE 분기 사슬의 ELSE 부재를 기재하지 않음. | [보완] TABP/TABI·TABT/TABS 사슬에는 ELSE가 없음을 명시. JVAR 루프의 소속 분기를 명시. | 4458–4476 |
| swan/src/swanparll.ftn.md:4479–4509 | 파일 부재 경로를 MSGERR(4)·RETURN으로만 기술. | [보완] 파일명을 포함한 오류 메시지 구성식과 MSGERR 호출 뒤 RETURN 순서를 명시. | 4493–4496 |
| swan/src/swanparll.ftn.md:4541–4562 | 프로세스 탐색 초기값의 백틱 인용 누락. | [보완] IPROC = 1을 원문 인용. | 4541 |
| swan/src/swanparll.ftn.md:4563–4590 | 문자열 위치·서식 기본값과 시간 필드 대입식을 축약. | [보완] IL·OUTLIN·FSTR·LFIELD 초기값과 시간 필드의 인덱스 대입을 원문 인용. | 4565–4579·4585–4586 |
| swan/src/swanparll.ftn.md:4591–4615 | 공백 설정으로만 기술하여 문자열 인덱스 식을 누락. | [보완] OUTLIN(IL-1:IL)에 두 공백을 대입하는 문장을 원문 인용. | 4606 |
| swan/src/swanparll.ftn.md:4616–4774 | NCF 선택으로만 기술. STPNOW 선언의 활성 조건을 생략. | [보완] NCF 문장과 STPNOW 선언이 -netcdf 선택에서 활성화함을 명시. | 4627·4730·4743; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:4775–4799 | NCF 선택과 NLINES 초기값을 축약. | [보완] -netcdf 활성 조건과 NLINES = 0 원문을 명시. | 4779–4786·4789; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:4800–4819 | OQI(1)=NREF를 ELSE의 NREF=IUT와 묶어 기술. | [정정] 4806행 IF가 4811행에서 닫힘을 명시. OQI 대입은 두 분기 이후 공통 문장으로 정정. | 4806–4812 |
| swan/src/swanparll.ftn.md:4820–4851 | 파일 부재 경로를 MSGERR(4)·RETURN으로만 기술. | [보완] 파일명을 포함한 오류 메시지 구성식과 MSGERR 호출 뒤 RETURN 순서를 명시. | 4834–4837 |
| swan/src/swanparll.ftn.md:4852–4895 | 출력 여부를 나타내는 EMPTY 대입의 백틱 인용 누락. | [보완] EMPTY의 TRUE·FALSE 대입을 원문 인용. | 4877·4884 |
| swan/src/swanparll.ftn.md:4963–5003 | 프로세스 탐색 초기값의 백틱 인용 누락. | [보완] IPROC = 1을 원문 인용. | 4963 |
| swan/src/swanparll.ftn.md:5004–5095 | NCF 선택으로만 활성 조건을 기술. | [보완] SwanGridData·swn_outnc USE의 활성 스위치 -netcdf를 명시. | 5017–5018; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:5096–5186 | VOQ와 VOQR를 함께 할당 가능 배열로 기술. NCF 선택으로만 기술. | [정정·보완] VOQ만 ALLOCATABLE임을 명시. VOQR는 정수 배열 선언으로 정정. -netcdf 스위치를 명시. | 5142·5148–5149; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:5187–5218 | IPD 상수 대입의 백틱 인용과 실제 NCF 스위치명 누락. | [보완] IPD의 1·2·3 대입을 원문 인용. -netcdf 스위치를 명시. | 5196·5199·5201·5214–5215; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:5219–5256 | MatL5 선택으로 활성화한다고 기술. 공통 OQI 대입을 ELSE와 묶음. 초기값 인용 누락. | [정정·보완] MatL5는 -matl4 미선택임을 정정. OQI 대입은 5245행 END IF 뒤임을 명시. -netcdf·OPENED·IREC 인용 보완. | 5225–5254; switch.pl 36–37·102·104–105 |
| swan/src/swanparll.ftn.md:5257–5302 | 파일 부재 경로를 MSGERR(4)·RETURN으로만 기술. | [보완] 파일명을 포함한 오류 메시지 구성식과 MSGERR 호출 뒤 RETURN 순서를 명시. | 5291–5294 |
| swan/src/swanparll.ftn.md:5303–5328 | CTIM 문자와 VOQ·J 초기값의 백틱 인용 누락. | [보완] 문자 대입과 비 RAWPRT 분기의 예외값·J 초기값을 원문 인용. | 5308·5323–5324 |
| swan/src/swanparll.ftn.md:5329–5366 | 범위 밖 IBLKN 값과 범위 안 IPROC 초기값의 백틱 인용 누락. | [보완] IBLKN = 0과 IPROC = 1을 원문 인용. | 5345·5349 |
| swan/src/swanparll.ftn.md:5367–5407 | 두 번째 성분 수집의 IBLKN·IPROC 초기값 백틱 인용 누락. | [보완] IBLKN = 0과 IPROC = 1을 원문 인용. | 5385·5389 |
| swan/src/swanparll.ftn.md:5408–5438 | OVSVTY 분기의 ELSE 부재와 IFAC·DFAC 대입의 소속 분기를 생략. | [보완] OVSVTY=1·2·3 사슬에 ELSE가 없음을 명시. 5430·5432행 종료와 IFAC·DFAC의 범위를 명시. | 5411–5434 |
| swan/src/swanparll.ftn.md:5439–5458 | SBLKPT 인수를 OVUNIT·OVLNAM 배열명으로 기술. NCF 선택으로만 기술. | [정정·보완] 실제 인수 OVUNIT(IVTYPE)·OVLNAM(IVTYPE)로 정정. -netcdf 스위치를 명시. | 5449–5457; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:5459–5497 | 성분명 접두 문자열을 OVLNAM 배열명으로 기술. NCF 선택으로만 기술. | [정정·보완] OVLNAM(IVTYPE)에 X-comp·Y-comp를 붙이는 원문 식으로 정정. -netcdf 스위치를 명시. | 5479–5494; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:5498–5512 | NCF 선택으로만 활성 조건을 기술. | [보완] NetCDF 종료 호출의 활성 스위치 -netcdf를 명시. | 5503; switch.pl 36·102 |
| swan/src/swanparll.ftn.md:5513–5663 | 색 전파를 교대 전파와 조합으로만 요약. | [보완] 맨 왼쪽·아래의 초기 빨강, 나머지 무색, 전파 방향, MCOLR와 ICONV의 의미를 보완. | 5576–5579·5586–5587·5604 |
| swan/src/swanparll.ftn.md:5664–5691 | IBCOL·IXCOL·IYCOL의 초기 색 대입을 백틱 없이 기재. | [보완] 빨강과 흰색 초기화 대입을 JAC 접두부와 함께 원문 인용. | 5668·5682·5684·5687·5689 |
| swan/src/swanparll.ftn.md:5692–5721 | ICONV와 x방향 색 대입을 백틱 없이 기재. | [보완] 수렴 지표의 0·1 대입과 이웃 색에 따른 IXCOL 대입을 원문 인용. | 5698·5713·5715·5717 |
| swan/src/swanparll.ftn.md:5722–5744 | y방향 색과 미수렴 값 대입을 백틱 없이 기재. | [보완] IYCOL의 분기별 대입과 ICONV = 1을 원문 인용. | 5728·5730·5732 |
| swan/src/swanparll.ftn.md:5745–5773 | 최종 색 대입의 백틱 인용과 ELSE 부재 누락. 오류 메시지를 말줄임으로 기재. | [보완] 색 대입과 메시지 구성식을 원문 인용. 색 조합 사슬에 ELSE가 없음을 명시. | 5749–5754·5760–5768 |

이상 없음 11행은 다음 구간이다.
`3230–3350`, `3394–3514`, `3560–3688`, `3689–3718`, `3839–4010`, `4216–4241`, `4242–4267`, `4268–4423`, `4510–4540`, `4896–4934`, `4935–4962`.

대상 구간의 조건문 인용과 원문 행을 다시 대조했다.
대상 구간의 백틱 인용은 해당 원문 구간에서 확인했다.
기록의 frontmatter와 구간 경계는 유지했다.
원문 SHA-256은 `d6e0d8d01f7b6cf439e4e92fe747f6bdad9ff4880c7e586890e208d4e50632e5`로 frontmatter와 일치한다.
모델은 실행하지 않았다.
이번 작업은 원문·노트·git을 수정하지 않았다.
같은 기록의 대상 밖 구간에서 작업 중 확인된 변경은 이번 수정 집계에 포함하지 않았다.

정정 9, 보완 46, 이상 없음 11

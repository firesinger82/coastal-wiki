# CADMAS-SURF code-15 전수 검증

대상은 사용자 지정 19개 판독 기록이다.
원문 경로는 각 기록의 frontmatter `file:`을 따른다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조한다.
원문 인용의 문자·행 번호·비공백 행 포함 여부는 별도로 기계 대조한다.
행 수는 빈 행을 포함한 원문 행 수이다.
정정·보완 수는 아래 변경 목록의 항목 수이다.
이상 없음 수는 완료 기록 중 변경하지 않은 구간 행 수이다.
미완료 기록은 완료 목록에 넣지 않는다.

사용자 지정 19개 기록의 110개 구간 행을 모두 대조했다.
원문 행 수의 합은 5,175행이다.
각 구간의 원문 출력은 200행 이하로 열었다.
모든 비공백 원문 행의 백틱 인용과 행 번호가 원문과 일치했다.
수정 후에도 모든 인용과 구간 연속성을 기계 확인했다.
원문 파일의 SHA-256은 각 기록의 frontmatter 값과 일치했다.
구간 경계와 frontmatter는 변경하지 않았다.
원문·노트·git은 변경하지 않았다.
모델은 실행하지 않았다.

## vf_fdropf.f.md — 완료

대조한 원문: 1–678행 (678행).
대조한 구간 행: 12개.
이상 없는 구간 행: 3개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_fdropf.f.md:117–188 (보완) | 바깥 블록을 조건식·종료 위치 없이 이름으로만 표시 | 바깥 루프는 66행 `DO 120 K=2,NUMK-1`, 67행 `DO 110 J=MYJS,MYJE`, 68행 `DO 100 I=MYIS,MYIE`이다. 각 루프는 295행 `120 CONTINUE`, 294행 `110 CONTINUE`, 293행 `100 CONTINUE`에서 닫힌다. 바깥 70행 `IF (FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8) THEN`은 292행 `ENDIF`에서 닫힌다. 72행 `IF (DROPTX(I,J,K).LT.0.0D0)THEN`은 253행 `ELSEIF (NF(I,J,K-1).LE.-1) THEN`으로 이어진다. 이 사슬에는 ELSE가 없으며 283행 `ENDIF`에서 닫힌다. | vf_fdropf.f:66–72,253,283–295 |
| vf_fdropf.f.md:189–251 (보완) | 바깥 블록을 조건식·종료 위치 없이 이름으로만 표시 | 바깥 루프는 66행 `DO 120 K=2,NUMK-1`, 67행 `DO 110 J=MYJS,MYJE`, 68행 `DO 100 I=MYIS,MYIE`이다. 각 루프는 295행 `120 CONTINUE`, 294행 `110 CONTINUE`, 293행 `100 CONTINUE`에서 닫힌다. 바깥 70행 `IF (FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8) THEN`은 292행 `ENDIF`에서 닫힌다. 72행 `IF (DROPTX(I,J,K).LT.0.0D0)THEN`은 253행 `ELSEIF (NF(I,J,K-1).LE.-1) THEN`으로 이어진다. 이 사슬에는 ELSE가 없으며 283행 `ENDIF`에서 닫힌다. | vf_fdropf.f:66–72,253,283–295 |
| vf_fdropf.f.md:252–303 (보완) | 바깥 블록을 조건식·종료 위치 없이 이름으로만 표시 | 바깥 루프는 66행 `DO 120 K=2,NUMK-1`, 67행 `DO 110 J=MYJS,MYJE`, 68행 `DO 100 I=MYIS,MYIE`이다. 각 루프는 295행 `120 CONTINUE`, 294행 `110 CONTINUE`, 293행 `100 CONTINUE`에서 닫힌다. 바깥 70행 `IF (FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8) THEN`은 292행 `ENDIF`에서 닫힌다. 72행 `IF (DROPTX(I,J,K).LT.0.0D0)THEN`은 253행 `ELSEIF (NF(I,J,K-1).LE.-1) THEN`으로 이어진다. 이 사슬에는 ELSE가 없으며 283행 `ENDIF`에서 닫힌다. | vf_fdropf.f:66–72,253,283–295 |
| vf_fdropf.f.md:252–303 (정정) | 고체 비율이라는 해석을 사실로 서술 | 253행 ELSEIF에서 H1과 H2의 차로 HX와 HY를 계산한다. 279–282행은 GRZ0와 DTNOW를 사용하여 수평 속도를 갱신한다. 해석: GGV를 공극률로 설명한 31행에 따라 1.0D0-GGV를 고체 비율로 읽을 수 있다. | vf_fdropf.f:31,253–282 |
| vf_fdropf.f.md:335–387 (보완) | 바깥 L 루프 범위·종료 위치 누락 | 바깥 루프는 305행 `DO 290 L=1,2`이다. 이 루프는 404행 `290 CONTINUE`에서 닫힌다. | vf_fdropf.f:305,404 |
| vf_fdropf.f.md:388–444 (보완) | 바깥 L 루프 범위·종료 위치 누락 | 바깥 루프는 305행 `DO 290 L=1,2`이다. 이 루프는 404행 `290 CONTINUE`에서 닫힌다. | vf_fdropf.f:305,404 |
| vf_fdropf.f.md:335–387 (정정) | DT를 FMOVE 계산에 사용하는 듯한 요약과 부피 해석 | 344행은 DT를 계산한다. 349행은 `(1.0D0-FF(I1,J,K))*V1`과 `FF(I,J,K)*V0` 중 작은 값을 FMOVE에 대입한다. | vf_fdropf.f:344–351 |
| vf_fdropf.f.md:445–497 (보완) | 바깥 L 루프 범위·종료 위치 누락 | 바깥 루프는 415행 `DO 390 L=1,2`이다. 이 루프는 514행 `390 CONTINUE`에서 닫힌다. | vf_fdropf.f:415,514 |
| vf_fdropf.f.md:498–550 (보완) | 바깥 L 루프 범위·종료 위치 누락 | 바깥 루프는 415행 `DO 390 L=1,2`이다. 이 루프는 514행 `390 CONTINUE`에서 닫힌다. | vf_fdropf.f:415,514 |
| vf_fdropf.f.md:551–618 (보완) | 바깥 L 루프 범위·종료 위치 누락 | 바깥 루프는 525행 `DO 490 L=1,2`이다. 이 루프는 644행 `490 CONTINUE`에서 닫힌다. | vf_fdropf.f:525,644 |
| vf_fdropf.f.md:619–678 (보완) | 바깥 L 루프 범위·종료 위치 누락 | 바깥 루프는 525행 `DO 490 L=1,2`이다. 이 루프는 644행 `490 CONTINUE`에서 닫힌다. | vf_fdropf.f:525,644 |
| vf_fdropf.f.md:445–497 (정정) | 초기화를 빈 셀에만 한정 | FF와 가중 배열을 갱신한다. 477행 `IF (FF(I,J,K).GT.FLOWER .AND. NF(I,J,K).EQ.8) THEN`이 거짓이면 487행 ELSE에서 물방울 상태를 초기화한다. | vf_fdropf.f:477–494 |
| vf_fdropf.f.md:551–618 (정정) | 셀 높이·부피 해석과 가중 누적 조건 생략 | 554행은 `X=SQRT(2.0D0*GRZ0*ZZ(2,K))`를 계산한다. L과 DROPWW 조건에 따라 DT를 계산한다. 575행 조건이 참이면 FF를 갱신한다. 583행 조건이 참이면 `DROPWW(I,J,K)-DT*GRZ0`를 사용하여 WKWW를 가중 누적한다. | vf_fdropf.f:554–592 |

## vf_feuler.f.md — 완료

대조한 원문: 1–67행 (67행).
대조한 구간 행: 2개.
이상 없는 구간 행: 1개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_feuler.f.md:41–67 (정정) | LOOPS에 따른 G0를 무조건 이전 공극률로 단정 | 43–45행 루프에서 NF>-1인 셀의 G0와 DF를 계산하고 FF를 갱신한다. G0는 47행 식에 따라 LOOPS=0이면 GGV이고 LOOPS=1이면 GGV0이다. | vf_feuler.f:46–52 |

## vf_fmod1.f.md — 완료

대조한 원문: 1–209행 (209행).
대조한 구간 행: 4개.
이상 없는 구간 행: 1개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_fmod1.f.md:45–83 (보완) | ELSE 없는 분기 사슬의 기본 동작 누락 | 59–77행의 N 분기 사슬에는 ELSE가 없다. 모든 조건이 거짓이면 IEC·JEC·KEC와 IFC·JFC·KFC는 앞서 대입한 I·J·K를 유지한다. | vf_fmod1.f:53–77 |
| vf_fmod1.f.md:84–150 (보완) | ELSE 없는 분기 사슬의 기본 동작 누락 | 98–116행의 N 분기 사슬에는 ELSE가 없다. 모든 조건이 거짓이면 IEC·JEC·KEC와 IFC·JFC·KFC는 앞서 대입한 I·J·K를 유지한다. | vf_fmod1.f:92–116 |
| vf_fmod1.f.md:151–209 (보완) | ELSE 없는 분기 사슬의 기본 동작 누락 | 165–183행의 N 분기 사슬에는 ELSE가 없다. 모든 조건이 거짓이면 IEC·JEC·KEC와 IFC·JFC·KFC는 앞서 대입한 I·J·K를 유지한다. | vf_fmod1.f:159–183 |

## vf_fnfbub.f.md — 완료

대조한 원문: 1–291행 (291행).
대조한 구간 행: 6개.
이상 없는 구간 행: 4개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_fnfbub.f.md:151–210 (보완) | 바깥 루프 범위·종료 위치 누락 | 바깥 루프는 83행 `DO 200 L=1,NBUB`이다. 이 루프는 270행 `200 CONTINUE`에서 닫힌다. | vf_fnfbub.f:83,270 |
| vf_fnfbub.f.md:211–270 (보완) | 바깥 루프 범위·종료 위치 누락 | 바깥 루프는 83행 `DO 200 L=1,NBUB`이다. 이 루프는 270행 `200 CONTINUE`에서 닫힌다. | vf_fnfbub.f:83,270 |

## vf_fnfini.f.md — 완료

대조한 원문: 1–206행 (206행).
대조한 구간 행: 4개.
이상 없는 구간 행: 2개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_fnfini.f.md:44–105 (정정) | NF 제한과 부정 조건의 의미 생략 | 48행 `IF (NF(I,J,K).GT.-1) THEN` 안에서 FF<FLOWER이면 각 면의 경계값 또는 이웃 FF를 읽는다. 86–91행의 여섯 `.NOT.` 조건이 모두 참일 때만 NF=8을 설정한다. | vf_fnfini.f:48–98 |
| vf_fnfini.f.md:106–151 (정정) | 비기체 셀의 NF>-1 제한 생략 | 116행 `IF (NF(I,J,K).GT.-1) THEN` 안에서 기체에 인접한 비기체 셀을 NF=7로 목록화한다. 그중 유체 이웃이 없는 셀은 NF=8로 바꾼다. | vf_fnfini.f:116–144 |

## vf_fnfprv.f.md — 완료

대조한 원문: 1–248행 (248행).
대조한 구간 행: 5개.
이상 없는 구간 행: 2개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_fnfprv.f.md:102–161 (보완) | 바깥 루프 범위·종료 위치 누락 | 바깥 루프는 34행 `DO 100 L=1,NUMS`이다. 이 루프는 237행 `100 CONTINUE`에서 닫힌다. | vf_fnfprv.f:34,237 |
| vf_fnfprv.f.md:162–221 (보완) | 바깥 루프 범위·종료 위치 누락 | 바깥 루프는 34행 `DO 100 L=1,NUMS`이다. 이 루프는 237행 `100 CONTINUE`에서 닫힌다. | vf_fnfprv.f:34,237 |
| vf_fnfprv.f.md:222–248 (보완) | 바깥 루프 범위·종료 위치 누락 | 바깥 루프는 34행 `DO 100 L=1,NUMS`이다. 이 루프는 237행 `100 CONTINUE`에서 닫힌다. | vf_fnfprv.f:34,237 |

## vf_fpvcip.f.md — 완료

대조한 원문: 1–286행 (286행).
대조한 구간 행: 6개.
이상 없는 구간 행: 2개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_fpvcip.f.md:111–142 (보완) | 프로세스 오프셋의 랭크별 합산 입력 생략 | 114행 `DO 300 IP=0,NPROCS-1`에서 115행 `IF (MYRANK.GE.IP) THEN`이 참인 랭크는 N=0을 합산 호출에 넘긴다. 반대 분기인 MYRANK<IP 랭크는 N=NPVCB를 넘긴다. 122행 `IF (MYRANK.EQ.IP) NS=I`에 따라 해당 랭크만 NS를 저장한다. | vf_fpvcip.f:114–123 |
| vf_fpvcip.f.md:143–206 (보완) | GOTO 반복의 종료 조건·대상 행 생략 | 바깥 반복의 시작은 139행 `1000 CONTINUE`이다. 258행 `IF (ISWAP.GT.0) GOTO 1000`이 참이면 되돌아간다. 거짓이면 261행 이후로 진행한다. | vf_fpvcip.f:139,258–261 |
| vf_fpvcip.f.md:207–255 (보완) | GOTO 반복의 종료 조건·대상 행 생략 | 바깥 반복의 시작은 139행 `1000 CONTINUE`이다. 258행 `IF (ISWAP.GT.0) GOTO 1000`이 참이면 되돌아간다. 거짓이면 261행 이후로 진행한다. | vf_fpvcip.f:139,258–261 |
| vf_fpvcip.f.md:256–286 (보완) | GOTO 반복의 종료 조건·대상 행 생략 | 바깥 반복의 시작은 139행 `1000 CONTINUE`이다. 258행 `IF (ISWAP.GT.0) GOTO 1000`이 참이면 되돌아간다. 거짓이면 261행 이후로 진행한다. | vf_fpvcip.f:139,258–261 |
| vf_fpvcip.f.md:207–255 (정정) | 전체 IPVC를 조건 없이 재매핑한다고 요약 | 빈 번호를 채운다. 전체 격자를 순회하면서 `IPVC(IJK).GE.1`인 항목만 NLIM으로 재매핑한다. NLIM의 최댓값으로 NPVCB를 갱신한다. | vf_fpvcip.f:240–253 |

## vf_ii1inp.f.md — 완료

대조한 원문: 1–363행 (363행).
대조한 구간 행: 6개.
이상 없는 구간 행: 2개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_ii1inp.f.md:143–195 (보완) | 입력 반복의 조건·GOTO 대상 위치 누락 | 입력 반복은 136행 `100 CONTINUE`에서 시작한다. 137행 `IF (IEOF.NE.0) GOTO 5010`은 302행 `5010 CONTINUE`로 빠져나간다. 141행 `IF (NWD.LE.0) GOTO 5000`은 301행 `5000 GOTO 100`으로 이동한다. | vf_ii1inp.f:136–141,301–302 |
| vf_ii1inp.f.md:196–239 (보완) | 입력 반복의 조건·GOTO 대상 위치 누락 | 입력 반복은 136행 `100 CONTINUE`에서 시작한다. 137행 `IF (IEOF.NE.0) GOTO 5010`은 302행 `5010 CONTINUE`로 빠져나간다. 141행 `IF (NWD.LE.0) GOTO 5000`은 301행 `5000 GOTO 100`으로 이동한다. | vf_ii1inp.f:136–141,301–302 |
| vf_ii1inp.f.md:240–302 (보완) | 입력 반복의 조건·GOTO 대상 위치 누락 | 입력 반복은 136행 `100 CONTINUE`에서 시작한다. 137행 `IF (IEOF.NE.0) GOTO 5010`은 302행 `5010 CONTINUE`로 빠져나간다. 141행 `IF (NWD.LE.0) GOTO 5000`은 301행 `5000 GOTO 100`으로 이동한다. | vf_ii1inp.f:136–141,301–302 |
| vf_ii1inp.f.md:196–239 (보완) | 헤더 사슬의 시작 조건·종료 위치 누락 | 바깥 헤더 사슬은 144행 `IF     (TEXT(IS(1):IE(1)).EQ.'PARALLEL') THEN`으로 시작한다. 각 ELSEIF는 앞선 헤더 조건이 거짓일 때 검사한다. 295행 ELSE는 알 수 없는 헤더 처리이며 298행 ENDIF가 사슬을 닫는다. | vf_ii1inp.f:144,295–298 |
| vf_ii1inp.f.md:240–302 (보완) | 헤더 사슬의 시작 조건·종료 위치 누락 | 바깥 헤더 사슬은 144행 `IF     (TEXT(IS(1):IE(1)).EQ.'PARALLEL') THEN`으로 시작한다. 각 ELSEIF는 앞선 헤더 조건이 거짓일 때 검사한다. 295행 ELSE는 알 수 없는 헤더 처리이며 298행 ENDIF가 사슬을 닫는다. | vf_ii1inp.f:144,295–298 |
| vf_ii1inp.f.md:303–363 (정정) | 파일 닫기의 랭크 0 제한 누락 | 305행 `IF (MYRANK.EQ.0) THEN` 안에서만 입력 파일을 닫고 IINFIL을 0으로 만든다. 세 격자 필수 입력 검사는 이 IF 밖에 있다. | vf_ii1inp.f:305–313 |

## vf_iiboun.f.md — 완료

대조한 원문: 1–534행 (534행).
대조한 구간 행: 10개.
이상 없는 구간 행: 3개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_iiboun.f.md:209–262 (보완) | 바깥 물리량 사슬 조건·종료 위치 누락 | 바깥 물리량 사슬은 153–154행 `IF ((TEXT(IS(IP):IE(IP)).EQ.'VP') .OR.` / `     &    (TEXT(IS(IP):IE(IP)).EQ.'VG')       ) THEN`으로 시작한다. 각 ELSEIF는 앞선 물리량 조건이 거짓일 때 검사한다. 523행 ELSE는 알 수 없는 단어 처리이며 525행 ENDIF가 사슬을 닫는다. | vf_iiboun.f:153–154,523–525 |
| vf_iiboun.f.md:263–308 (보완) | 바깥 물리량 사슬 조건·종료 위치 누락 | 바깥 물리량 사슬은 153–154행 `IF ((TEXT(IS(IP):IE(IP)).EQ.'VP') .OR.` / `     &    (TEXT(IS(IP):IE(IP)).EQ.'VG')       ) THEN`으로 시작한다. 각 ELSEIF는 앞선 물리량 조건이 거짓일 때 검사한다. 523행 ELSE는 알 수 없는 단어 처리이며 525행 ENDIF가 사슬을 닫는다. | vf_iiboun.f:153–154,523–525 |
| vf_iiboun.f.md:309–354 (보완) | 바깥 물리량 사슬 조건·종료 위치 누락 | 바깥 물리량 사슬은 153–154행 `IF ((TEXT(IS(IP):IE(IP)).EQ.'VP') .OR.` / `     &    (TEXT(IS(IP):IE(IP)).EQ.'VG')       ) THEN`으로 시작한다. 각 ELSEIF는 앞선 물리량 조건이 거짓일 때 검사한다. 523행 ELSE는 알 수 없는 단어 처리이며 525행 ENDIF가 사슬을 닫는다. | vf_iiboun.f:153–154,523–525 |
| vf_iiboun.f.md:355–415 (보완) | 바깥 물리량 사슬 조건·종료 위치 누락 | 바깥 물리량 사슬은 153–154행 `IF ((TEXT(IS(IP):IE(IP)).EQ.'VP') .OR.` / `     &    (TEXT(IS(IP):IE(IP)).EQ.'VG')       ) THEN`으로 시작한다. 각 ELSEIF는 앞선 물리량 조건이 거짓일 때 검사한다. 523행 ELSE는 알 수 없는 단어 처리이며 525행 ENDIF가 사슬을 닫는다. | vf_iiboun.f:153–154,523–525 |
| vf_iiboun.f.md:416–458 (보완) | 바깥 T 분기의 조건·종료 위치 누락 | 바깥 물리량 사슬은 153–154행 `IF ((TEXT(IS(IP):IE(IP)).EQ.'VP') .OR.` / `     &    (TEXT(IS(IP):IE(IP)).EQ.'VG')       ) THEN`으로 시작한다. 각 ELSEIF는 앞선 물리량 조건이 거짓일 때 검사한다. 523행 ELSE는 알 수 없는 단어 처리이며 525행 ENDIF가 사슬을 닫는다. 구간 시작은 356행 `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'T') THEN` 분기 안이다. T 분기는 437행 C 분기로 이어진다. | vf_iiboun.f:153–154,356,437,525 |
| vf_iiboun.f.md:459–501 (보완) | 바깥 C 분기와 경계종류 사슬 조건·종료 위치 누락 | 바깥 물리량 사슬은 153–154행 `IF ((TEXT(IS(IP):IE(IP)).EQ.'VP') .OR.` / `     &    (TEXT(IS(IP):IE(IP)).EQ.'VG')       ) THEN`으로 시작한다. 각 ELSEIF는 앞선 물리량 조건이 거짓일 때 검사한다. 523행 ELSE는 알 수 없는 단어 처리이며 525행 ENDIF가 사슬을 닫는다. 구간 시작은 437행 `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'C') THEN` 분기 안이다. 안쪽 종류 사슬은 445행 `IF     (TEXT(IS(IP):IE(IP)).EQ.'FIX-A'  ) THEN`에서 시작한다. 이 사슬은 499행 ELSE를 거쳐 501행 ENDIF에서 닫힌다. | vf_iiboun.f:153–154,437,445,499–501,525 |
| vf_iiboun.f.md:502–534 (보완) | 바깥 C 분기의 조건·종료 위치 누락 | 바깥 물리량 사슬은 153–154행 `IF ((TEXT(IS(IP):IE(IP)).EQ.'VP') .OR.` / `     &    (TEXT(IS(IP):IE(IP)).EQ.'VG')       ) THEN`으로 시작한다. 각 ELSEIF는 앞선 물리량 조건이 거짓일 때 검사한다. 523행 ELSE는 알 수 없는 단어 처리이며 525행 ENDIF가 사슬을 닫는다. 구간 시작은 437행 `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'C') THEN` 분기 안이다. C 분기는 523행 ELSE 앞까지이다. | vf_iiboun.f:153–154,437,523–525 |

## vf_iifile.f.md — 완료

대조한 원문: 1–477행 (477행).
대조한 구간 행: 10개.
이상 없는 구간 행: 2개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_iifile.f.md:91–142 (보완) | 바깥 L/P·하위 사슬 조건과 종료 위치 누락 | 바깥 출력종류 사슬은 33행 `IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 466행 ELSE는 알 수 없는 단어 처리이며 468행 ENDIF가 사슬을 닫는다. 구간 시작은 L/P 분기 안이다. 안쪽 사슬은 36행 `IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN`으로 시작하여 139행 ELSE를 거쳐 141행 ENDIF에서 닫힌다. | vf_iifile.f:33,36,139–144,466–468 |
| vf_iifile.f.md:143–204 (보완) | 바깥 출력종류 사슬 조건·종료 위치 누락 | 바깥 출력종류 사슬은 33행 `IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 466행 ELSE는 알 수 없는 단어 처리이며 468행 ENDIF가 사슬을 닫는다. | vf_iifile.f:33,466–468 |
| vf_iifile.f.md:205–236 (보완) | 바깥 출력종류 사슬 조건·종료 위치 누락 | 바깥 출력종류 사슬은 33행 `IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 466행 ELSE는 알 수 없는 단어 처리이며 468행 ENDIF가 사슬을 닫는다. | vf_iifile.f:33,466–468 |
| vf_iifile.f.md:237–292 (보완) | 바깥 출력종류 사슬 조건·종료 위치 누락 | 바깥 출력종류 사슬은 33행 `IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 466행 ELSE는 알 수 없는 단어 처리이며 468행 ENDIF가 사슬을 닫는다. | vf_iifile.f:33,466–468 |
| vf_iifile.f.md:432–477 (보완) | 바깥 출력종류 사슬 조건·종료 위치 누락 | 바깥 출력종류 사슬은 33행 `IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 466행 ELSE는 알 수 없는 단어 처리이며 468행 ENDIF가 사슬을 닫는다. | vf_iifile.f:33,466–468 |
| vf_iifile.f.md:293–343 (보완) | TRN과 하위 ELSE의 조건·종료 위치 누락 | 바깥 출력종류 사슬은 33행 `IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 466행 ELSE는 알 수 없는 단어 처리이며 468행 ENDIF가 사슬을 닫는다. 구간 시작은 238행 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'TRN') THEN` 분기 안이다. 안쪽 사슬은 241행 `IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN`으로 시작한다. 294행 ELSE는 STEP·TIME·W-LEVEL 조건이 모두 거짓인 분기이다. 이 사슬은 431행 ENDIF에서 닫힌다. TRN 분기는 434행 MAM 분기로 이어진다. | vf_iifile.f:33,238–259,294,431–434,468 |
| vf_iifile.f.md:344–368 (보완) | TRN·FORCE 바깥 조건과 종료 위치 누락 | 바깥 출력종류 사슬은 33행 `IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 466행 ELSE는 알 수 없는 단어 처리이며 468행 ENDIF가 사슬을 닫는다. 구간 시작은 238행 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'TRN') THEN` 분기 안이다. 안쪽 사슬은 241행 `IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN`으로 시작한다. 294행 ELSE는 STEP·TIME·W-LEVEL 조건이 모두 거짓인 분기이다. 이 사슬은 431행 ENDIF에서 닫힌다. TRN 분기는 434행 MAM 분기로 이어진다. 328행 `IF (ITRPRM(1,ITRNUM).EQ.11) THEN`의 344행 ELSE는 해당 조건이 거짓인 분기이다. 이 IF는 384행 ENDIF에서 닫힌다. | vf_iifile.f:33,238–259,294,328,344,384,431–434,468 |
| vf_iifile.f.md:369–431 (보완) | 바깥 분기들과 물리량 사슬의 조건·종료 위치 누락 | 바깥 출력종류 사슬은 33행 `IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 466행 ELSE는 알 수 없는 단어 처리이며 468행 ENDIF가 사슬을 닫는다. 구간 시작은 238행 `ELSEIF (TEXT(IS(2):IE(2)).EQ.'TRN') THEN` 분기 안이다. 안쪽 사슬은 241행 `IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN`으로 시작한다. 294행 ELSE는 STEP·TIME·W-LEVEL 조건이 모두 거짓인 분기이다. 이 사슬은 431행 ENDIF에서 닫힌다. TRN 분기는 434행 MAM 분기로 이어진다. 328행 `IF (ITRPRM(1,ITRNUM).EQ.11) THEN`의 344행 ELSE는 해당 조건이 거짓인 분기이다. 이 IF는 384행 ENDIF에서 닫힌다. 물리량 사슬은 345행 `IF     (TEXT(IS(4):IE(4)).EQ.'U') THEN`으로 시작한다. 이 사슬은 381행 ELSE를 거쳐 383행 ENDIF에서 닫힌다. | vf_iifile.f:33,238–259,294,328,344–345,381–384,431–434,468 |

## vf_iigrid.f.md — 완료

대조한 원문: 1–144행 (144행).
대조한 구간 행: 4개.
이상 없는 구간 행: 2개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_iigrid.f.md:66–113 (보완) | ELSE 없는 좌표 저장 분기의 동작 누락 | 86–91행의 좌표 저장 사슬에는 ELSE가 없다. `LG1.LE.NL .AND. NL.LE.LG2`와 `NL.EQ.LG2+1`이 모두 거짓이면 XYZ와 XBUF에 대입하지 않는다. | vf_iigrid.f:85–92 |
| vf_iigrid.f.md:114–144 (정정) | 이전 단계 검사 조건 누락 및 모든 방향에 전역 범위 설정으로 일반화 | NL<3이면 VF_A2ERR를 호출한다. 이전 단계와 같은 격자 수인지의 검사는 `LEVEL.GE.1`일 때만 수행한다. ISW=1이면 NUMI0와 GLXMIN·GLXMAX를 설정한다. ISW=2이면 NUMJ0와 GLYMIN·GLYMAX를 설정한다. 그 외에는 NUML만 설정한다. LEVEL=1이면 VF_CGRID를 호출한다. | vf_iigrid.f:115–131 |

## vf_iihidm.f.md — 완료

대조한 원문: 1–50행 (50행).
대조한 구간 행: 2개.
이상 없는 구간 행: 2개.

## vf_iimate.f.md — 완료

대조한 원문: 1–170행 (170행).
대조한 구간 행: 5개.
이상 없는 구간 행: 2개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_iimate.f.md:69–107 (보완) | 바깥 MATE 사슬 조건·종료 위치 누락 | 바깥 MATE 사슬은 31행 `IF     (TEXT(IS(2):IE(2)).EQ.'W-LEVEL') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 159행 ELSE는 알 수 없는 단어 처리이며 161행 ENDIF가 사슬을 닫는다. | vf_iimate.f:31,159–161 |
| vf_iimate.f.md:108–157 (보완) | 바깥 MATE 사슬 조건·종료 위치 누락 | 바깥 MATE 사슬은 31행 `IF     (TEXT(IS(2):IE(2)).EQ.'W-LEVEL') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 159행 ELSE는 알 수 없는 단어 처리이며 161행 ENDIF가 사슬을 닫는다. | vf_iimate.f:31,159–161 |
| vf_iimate.f.md:158–170 (보완) | 바깥 MATE 사슬 조건·종료 위치 누락 | 바깥 MATE 사슬은 31행 `IF     (TEXT(IS(2):IE(2)).EQ.'W-LEVEL') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 159행 ELSE는 알 수 없는 단어 처리이며 161행 ENDIF가 사슬을 닫는다. | vf_iimate.f:31,159–161 |
| vf_iimate.f.md:108–157 (정정) | C 입력과 LC 검증의 순서가 원문과 다름 | T는 TINI를 읽는다. C는 LC와 SC를 먼저 읽는다. LC 범위 검사 후 `CINI(LC)=SC`를 대입한다. | vf_iimate.f:142–152 |

## vf_iimdl.f.md — 완료

대조한 원문: 1–284행 (284행).
대조한 구간 행: 7개.
이상 없는 구간 행: 1개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_iimdl.f.md:33–69 (정정) | 구간에 정의가 없는 IVAL을 차수로 단정 | FUNC의 STREAM은 여섯 번째 단어를 IVAL로 읽고 1..22 범위를 검사한 뒤 IBCTYP(2,JD)에 저장한다. STK-CND/STOKES/CNOIDAL/MATRIX는 IBCTYP(2,JD)를 0/-2/-1/-3으로 설정한다. | vf_iimdl.f:51–66 |
| vf_iimdl.f.md:70–112 (보완) | WAVE-BC와 하위 사슬 조건·종료 위치 누락 | 바깥 MODEL 사슬은 34행 `IF     (TEXT(IS(2):IE(2)).EQ.'WAVE-BC') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 273행 ELSE는 알 수 없는 단어 처리이며 275행 ENDIF가 사슬을 닫는다. 구간 시작은 WAVE-BC 분기 안이다. 안쪽 사슬은 51행 `IF     (TEXT(IS(4):IE(4)).EQ.'FUNC'  ) THEN`으로 시작한다. 이 사슬은 109행 ELSE를 거쳐 111행 ENDIF에서 닫힌다. | vf_iimdl.f:34,51,109–114,273–275 |
| vf_iimdl.f.md:113–152 (보완) | 바깥 MODEL 사슬 조건·종료 위치 누락 | 바깥 MODEL 사슬은 34행 `IF     (TEXT(IS(2):IE(2)).EQ.'WAVE-BC') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 273행 ELSE는 알 수 없는 단어 처리이며 275행 ENDIF가 사슬을 닫는다. | vf_iimdl.f:34,273–275 |
| vf_iimdl.f.md:153–197 (보완) | 바깥 MODEL 사슬 조건·종료 위치 누락 | 바깥 MODEL 사슬은 34행 `IF     (TEXT(IS(2):IE(2)).EQ.'WAVE-BC') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 273행 ELSE는 알 수 없는 단어 처리이며 275행 ENDIF가 사슬을 닫는다. | vf_iimdl.f:34,273–275 |
| vf_iimdl.f.md:198–244 (보완) | 바깥 MODEL 사슬 조건·종료 위치 누락 | 바깥 MODEL 사슬은 34행 `IF     (TEXT(IS(2):IE(2)).EQ.'WAVE-BC') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 273행 ELSE는 알 수 없는 단어 처리이며 275행 ENDIF가 사슬을 닫는다. | vf_iimdl.f:34,273–275 |
| vf_iimdl.f.md:245–284 (보완) | 바깥 MODEL 사슬 조건·종료 위치 누락 | 바깥 MODEL 사슬은 34행 `IF     (TEXT(IS(2):IE(2)).EQ.'WAVE-BC') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 273행 ELSE는 알 수 없는 단어 처리이며 275행 ENDIF가 사슬을 닫는다. | vf_iimdl.f:34,273–275 |

## vf_iiopt.f.md — 완료

대조한 원문: 1–178행 (178행).
대조한 구간 행: 5개.
이상 없는 구간 행: 1개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_iiopt.f.md:1–39 (정정) | 이름만으로 INCLUDE의 용도를 단정 | 9행은 MOD_FAULT에서 set_utm·icoord·isystem·jsystem만 가져온다. 23행은 `VF_ASEABT.h`를 포함한다. | vf_iiopt.f:9,23 |
| vf_iiopt.f.md:79–118 (보완) | 바깥 OPTION 사슬 조건·종료 위치 누락 | 바깥 OPTION 사슬은 41행 `IF     (TEXT(IS(2):IE(2)).EQ.'SUB-LOOP') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 167행 ELSE는 알 수 없는 단어 처리이며 169행 ENDIF가 사슬을 닫는다. | vf_iiopt.f:41,167–169 |
| vf_iiopt.f.md:119–158 (보완) | 바깥 OPTION 사슬 조건·종료 위치 누락 | 바깥 OPTION 사슬은 41행 `IF     (TEXT(IS(2):IE(2)).EQ.'SUB-LOOP') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 167행 ELSE는 알 수 없는 단어 처리이며 169행 ENDIF가 사슬을 닫는다. | vf_iiopt.f:41,167–169 |
| vf_iiopt.f.md:159–178 (보완) | 바깥 OPTION 사슬 조건·종료 위치 누락 | 바깥 OPTION 사슬은 41행 `IF     (TEXT(IS(2):IE(2)).EQ.'SUB-LOOP') THEN`으로 시작한다. 각 ELSEIF는 앞선 종류 조건이 거짓일 때 검사한다. 167행 ELSE는 알 수 없는 단어 처리이며 169행 ENDIF가 사슬을 닫는다. | vf_iiopt.f:41,167–169 |

## vf_im1inp.f.md — 완료

대조한 원문: 1–207행 (207행).
대조한 구간 행: 5개.
이상 없는 구간 행: 3개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_im1inp.f.md:1–37 (정정) | 이 구간에 없는 조파 용도 단정과 z좌표·무차원 설명 누락 | 21–25행 주석에 따라 행렬 데이터(matrix data)의 무차원 위상·z좌표·수위·수평 및 수직 속도 배열을 받는다. | vf_im1inp.f:21–25 |
| vf_im1inp.f.md:126–179 (보완) | 바깥 ISW 조건식·종료 위치 누락 | 바깥 조건은 107행 `IF (ISW.NE.0) THEN`이다. 이 IF는 179행 ENDIF에서 닫힌다. | vf_im1inp.f:107,179 |

## vf_ip1inp.f.md — 완료

대조한 원문: 1–232행 (232행).
대조한 구간 행: 5개.
이상 없는 구간 행: 3개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_ip1inp.f.md:108–163 (보완) | 초기화 사슬과 시간 반복 탈출 조건·대상 위치 누락 | 바깥 사슬은 43행 `IF (IPRNT.GE.1 .AND. IPRIT.LT.0) THEN`에서 시작한다. 109행 `ELSEIF (IPRNT.GE.1) THEN`은 초기화 조건이 거짓일 때 검사한다. 이 사슬에는 ELSE가 없으며 192행 ENDIF에서 닫힌다. 112–113행 `IF ((IPRIT.NE.0 .AND. PRTNOW.GE.T0) .OR.` / `     &          IPRNT.LE.IPRIT                      ) GOTO 240`은 목표 시각 도달 또는 시간 블록 수 소진 시 170행 `240 CONTINUE`로 이동한다. | vf_ip1inp.f:43,109,112–113,170,192 |
| vf_ip1inp.f.md:164–193 (보완) | 바깥 랭크 조건·종료 위치와 GOTO 대상 누락 | 바깥 사슬은 43행 `IF (IPRNT.GE.1 .AND. IPRIT.LT.0) THEN`에서 시작한다. 109행 `ELSEIF (IPRNT.GE.1) THEN`은 초기화 조건이 거짓일 때 검사한다. 이 사슬에는 ELSE가 없으며 192행 ENDIF에서 닫힌다. 바깥 랭크 조건은 110행 `IF (MYRANK.EQ.0) THEN`이며 182행 ENDIF에서 닫힌다. 168행 `GOTO 200`은 111행 `200 CONTINUE`로 되돌아간다. 반복 탈출은 112–113행 조건에 따라 170행 `240 CONTINUE`로 이동한다. | vf_ip1inp.f:43,109–113,168–182,192 |
| vf_ip1inp.f.md:164–193 (정정) | 전파의 NPROCS 조건 누락 | rank 0 분기 밖의 183행 `IF (NPROCS.NE.1) THEN` 안에서만 IPRIT·시간·배열을 VF_P1BCSI/VF_P1BCSD로 전파한다. | vf_ip1inp.f:183–191 |

## vf_ir1inp.f.md — 완료

대조한 원문: 1–344행 (344행).
대조한 구간 행: 7개.
이상 없는 구간 행: 4개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_ir1inp.f.md:124–179 (정정) | 버전도 검사한다는 요약과 경계 수·병렬 조건 생략 | IV1·IV2 버전 값은 읽기만 한다. 격자 수는 NUMI·NUMJ·NUMK와 같은지 검사한다. 경계 수는 `NUMB.GT.I4`일 때 오류 처리한다. 병렬 구역 정보는 `NPROCS.NE.1`일 때 읽고 검사한다. | vf_ir1inp.f:125–152 |
| vf_ir1inp.f.md:241–284 (보완) | 반복 종료·GOTO 대상과 ELSE 없는 물방울 사슬 동작 누락 | 바깥 반복은 182행 `100 CONTINUE`에서 시작한다. 185행 `READ(IREFIL,END=1000,ERR=9020) NNOW,TNOW,DTNOW`의 EOF와 276행 `IF (NNOW.EQ.IRETYP) THEN` 안의 278행 GOTO는 283행 `1000 CONTINUE`로 이동한다. 282행 `GOTO 100`은 182행으로 되돌아간다. 254–270행의 물방울 사슬에는 ELSE가 없다. LD<1이면 이 사슬에서 ND와 물방울 레코드를 읽지 않는다. | vf_ir1inp.f:182,185,254–283 |
| vf_ir1inp.f.md:285–312 (정정) | 계수 계산 호출의 조건 누락 | 308행은 `LEQK.NE.0`일 때 VF_CNUT0을 호출한다. 309행은 조건 없이 VF_CNU00을 호출한다. 310행은 `LEQT.NE.0`일 때 VF_CLM00을 호출한다. 311행은 `LEQC.GT.0`일 때 VF_CDD00을 호출한다. | vf_ir1inp.f:308–311 |

## vf_jpcoef.f.md — 완료

대조한 원문: 1–207행 (207행).
대조한 구간 행: 5개.
이상 없는 구간 행: 1개.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_jpcoef.f.md:56–91 (정정) | 이 구간에서 정의하지 않은 프로세스 소유 의미를 단정 | 87–90행은 MYMIS·MYMJS·MYMIE·MYMJE가 각각 1일 때 IA=1·JA=1·IB=NUMI·JB=NUMJ로 설정한다. | vf_jpcoef.f:83–90 |
| vf_jpcoef.f.md:92–142 (정정) | 배열 성분 정의 없이 곱을 면적·부피로 단정 | 109행 ELSE에서는 AXY·AXZ·AYZ·AVL을 117–120행 식으로 계산한다. 해석: 이 곱들을 면적과 부피로 읽을 수 있지만 XX·YY·ZZ의 두 번째 성분 의미는 이 구간에서 정의하지 않는다. | vf_jpcoef.f:117–120 |
| vf_jpcoef.f.md:143–187 (정정) | 격자 계수의 중심 간격 역수 의미를 근거 없이 단정 | AXZ와 YY(5,J)·YY(5,JP)의 곱으로 AJM·AJP를 계산한다. AXY와 ZZ(5,K)·ZZ(5,KP)의 곱으로 AKM·AKP를 계산한다. 각 계수의 부호를 바꿔 비대각 성분에 대입한다. YY·ZZ의 다섯 번째 성분을 중심 간격의 역수로 정의하는 근거는 이 구간에 없다. | vf_jpcoef.f:148–182 |
| vf_jpcoef.f.md:188–207 (정정) | 0을 포함할 수 있는 여섯 계수를 모두 양수로 표현 | AD는 AKM·AJM·AIM·AIP·AJP·AKP의 합이며 BB=0이다. 각 이웃 조건이 거짓이면 해당 계수는 0이므로 여섯 계수가 모두 양수인 것은 아니다. | vf_jpcoef.f:125–192 |
| vf_jpcoef.f.md:143–187 (보완) | 바깥 루프·ELSE의 조건과 종료 위치 누락 | 바깥 루프는 93행 `DO 120 K=1,NUMK`, 94행 `DO 110 J=JA,JB`, 95행 `DO 100 I=IA,IB`이다. 각 루프는 198행 `120 CONTINUE`, 197행 `110 CONTINUE`, 196행 `100 CONTINUE`에서 닫힌다. 구간 시작은 98행 `IF (INDC2(I,J,K).EQ.-1) THEN`의 109행 ELSE 안이다. 이 IF는 194행 ENDIF에서 닫힌다. | vf_jpcoef.f:93–98,109,194–198 |
| vf_jpcoef.f.md:188–207 (보완) | 바깥 루프·ELSE의 조건과 종료 위치 누락 | 바깥 루프는 93행 `DO 120 K=1,NUMK`, 94행 `DO 110 J=JA,JB`, 95행 `DO 100 I=IA,IB`이다. 각 루프는 198행 `120 CONTINUE`, 197행 `110 CONTINUE`, 196행 `100 CONTINUE`에서 닫힌다. 구간 시작은 98행 `IF (INDC2(I,J,K).EQ.-1) THEN`의 109행 ELSE 안이다. 이 IF는 194행 ENDIF에서 닫힌다. | vf_jpcoef.f:93–98,109,194–198 |
| vf_jpcoef.f.md:후속 사실 120 (정정) | AVL을 셀 부피로 단정 | 120: `AVL=XX(2,I)*YY(2,J)*ZZ(2,K)`로 계산하지만 이후 이 파일의 실행식에서는 사용하지 않는다. 해석: 이 곱을 셀 부피로 읽을 수 있으나 배열 성분의 정의는 이 구간에 없다. [11-04 전수 검증 정정] | vf_jpcoef.f:120 |

정정 22, 보완 59, 이상 없음 41

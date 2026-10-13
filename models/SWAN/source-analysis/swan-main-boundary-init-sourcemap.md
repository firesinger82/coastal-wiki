---
title: "swanmain.ftn 7469-9156 — 경계 스펙트럼 읽기(RBFILE)·해상도 변환(RESPEC)·비정상 입력장(FLFILE)·기본 초기조건(SWINCO) 소스맵"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "models/SWAN/raw/source_code/swan/src/swanmain.ftn (9343행, SWAN 41.xx 1993-2024 헤더 :7496) 직접 read — 7300-9200 구간 전수 + 전체 서브루틴 인벤토리 실측. I-6 문서축 재검토(2026-07-17) 산출 — Codex ② 5회차 'swanmain=driver S요약' 반박의 해소(실질 로직 4서브루틴 C티어 재분류). 2026-10-13 recovery 대조 보고서 R1–R8 반영." # [10-13 전수 검증 정정]
last_source_check: 2026-10-13 (recovery 대조 반영)
note_author: "Claude Fable 5 (I-6 심층 재검토, 추출 = 병렬 소스 read 에이전트 + 본 세션 검수)"
note_date: 2026-07-17
related:
  - swan-foundation.md
  - swan-grid-readers.md
---

# swanmain 후반부 소스맵 — 경계 입력·해상도 변환·초기조건

> 구 판정("swanmain = driver, S요약 충분")의 정정. 파일 9338행 중 **7469-9156 에 실질 로직 4서브루틴**이 있음:
> RBFILE(7469-8086)·RESPEC(8089-8521)·FLFILE(8524-8860)·SWINCO(8864-9156). 6708행 이전(SWINIT/SWPREP/SWRBC 등)과 SWCLME(9159-9338, 메모리 해제)는 기존 S요약으로 충분.
> 전체 인벤토리: PROGRAM SWAN 29-125 · SWMAIN 128-770 · SWINIT 773-3539 · SWPREP 3543-4258 · SPRCON 4262-4648 · SWRBC 4651-5306 · SVALQI 5309-5709 · SINUPT 5712-5837 · SINBTG 5841-5963 · SINCMP 5966-6131 · WRTEST 6134-6223 · ERRCHK 6226-6705 · SNEXTI 6708-7465 · RBFILE · RESPEC · FLFILE · SWINCO · SWCLME.

## 1. SNEXTI (6708-7465) — 매 시간스텝 경계·입력장 갱신 드라이버

- 경계 갱신: master 노드가 경계파일 연결리스트 FBNDFIL 를 돌며 RBFILE 호출(:6916-6919) 후 BSPECS 를 MPI 브로드캐스트(:6929). 계산 경계점마다 인접 파일 스펙트럼 2개를 공간 보간(가중치는 BGRIDP 에 정수 ×1000 팩킹 — `W1=0.001*REAL(...)`, :6941)해 SINTRP 로 AC2 에 직접 기입(:6945-6946), 부과 Hs 를 COMPDA(:,JHSIBC) 저장(:6948-6960).
- 비정상 입력장 13종을 FLFILE 로 갱신: 바람(:7024)·마찰(:7066)·수위(:7093 — 이후 수심 재구성 :7099-7139)·해류(:7161)·식생(:7248)·난류점성(:7275)·fluid mud(:7302)·얼음 농도/두께(:7329/:7356)·sea-swell 3종(:7383-7437).
- ★**해류 Froude 캡**: $|U|>{\rm PNUMS(18)}\sqrt{gd}$ 이면 해류를 축소하고 ERRPTS 파일에 기록(:7167-7212) — 수치부가 아닌 여기 존재.

## 2. RBFILE (7469-8086) — 경계 스펙트럼 파일 읽기 + 시간 보간

- **파일 타입**(BTYPE, :7698): WAMW/WAMC/WAMF(WAM nest = BOUNDNEST2)·WW3U/WW3F(WAVEWATCH III = BOUNDNEST3)·SWN*/SWNT(SWAN nest = BOUNDNEST1)·TPAR(파라메트릭 시계열 = BOUNDSPEC FILE). unformatted 는 WAMW/WAMC/WW3U 만(:7700-7705).
- **단위 변환은 UFAC 에 내장**(:7804-7812): SWAN 2D 파일 = $180/(2\pi^2)$ (Hz→rad/s **및** deg→rad, :7807) / 그 외 $1/(2\pi)$ / 에너지밀도(J/m²) 파일은 추가로 $/(\rho g)$ (:7812).
- SWAN-nest 헤딩 키워드(:7903-7926): `NODATA`/`ZERO` → 스펙트럼 0 처리·읽기 생략 / `FACTOR` → RFAC 를 UFAC 에 합성 / 그 외(2D) = 치명 오류. 1D 는 헤딩 무시(:7920).
- TPAR: 시간+Hs·주기·방향·확산 4항 → SSHAPE 가 사용자 FSHAPE/DSHAPE 로 파라메트릭 스펙트럼 생성(:7941-7953). 그 외 전부 RESPEC 위임(:7961-7963).
- ★**파일 소진 = 준무음 동결**(:8019-8024): level-1 메시지 1줄 후 `BFILED(1)=-1`·`TIMF2=999999999` — **마지막 스펙트럼이 런 끝까지 재사용**(시간보간 가중치가 1로 고정). 다중 파일 리스트(NDSL)는 EOF 시 다음 파일 자동 오픈(:7987-8002).
- 시간 보간: $W1=(T_{F2}-T)/(T_{F2}-T_{F1})$ (:8034), SPAUX 경유 이중 SINTRP. 정상(stationary) 파일은 1회 읽고 고정(:7786).

## 3. RESPEC (8089-8521) — 스펙트럼 해상도 변환 (재검토 핵심 대상)

1D/2D 입력 스펙트럼 1개를 SWAN 내부 (σ,θ) 해상도로 변환.

- **1D**(:8304–8379)는 주파수별 `ETOT, ADEG, DD`를 읽는다. `BFILED(18)=1`이면 Cartesian 방향각을 도에서 라디안으로 변환한다(:8323–8325). 그 밖의 방향 규약에는 `ADIR = PI * (180.+DNORTH-ADEG) / 180.`을 적용한다(:8328). 도 단위 확산값에는 `DSPR = PI * DD / 180.`을 적용한다(:8331–8340). `IF (DSPR.NE.0.) THEN` 분기는 `MS = MAX (FAC*DSPR**(-2) - 2., 1.)`을 사용한다(:8341–8342). ELSE 분기는 `MS = 1000.`을 사용한다(:8343–8344). FAC는 `DD>23°`이면 1.2이다(:8332–8333). `17°<DD≤23°`이면 FAC는 1.096이다(:8334–8335). 그 밖의 경우 FAC는 1.01이다(:8336–8337). 이 보정 줄의 판 표지는 `41.99`이다. $\cos^{MS}$ 정규화는 MS≤10에서 감마함수를 사용한다(:8360–8361). MS>10에서는 점근식을 사용한다(:8358–8359). `ACOS>0` 분기는 `CDIR = CTOT * MAX (ACOS**MS, 1.E-10)`을 사용한다(:8366–8367). ELSE 분기는 `CDIR = 1.E-10`을 사용한다(:8368–8369). 양의 에너지를 읽은 1D 파일 경계는 반대 방향에도 작은 양의 밀도를 둔다. 입력 에너지가 0이면 결과도 0이다. 두 경우의 근거는 `src/swanmain.ftn:8372`의 `BAUX2(ID,IFRE) = CDIR * ETOT`이다. `SSHAPE`로 만드는 매개변수 경계·초기 스펙트럼은 반대 반원에서 0이다. 근거는 `src/swanser.ftn:4223`의 `CDIR = 0.`이다. [10-13 전수 검증 정정]
- **2D**(:8381-8454): WW3U 전치 읽기(:8386-8393)·DORDER<0 방향 역순(:8395-8401)·WW3F 고정 포맷 `(7E11.3)`(:8408-8410). 방향 재배치 = 주파수별 **CHGBAS**(에너지 보존 piecewise-constant 대역 재분배, swanser.ftn, :8450-8453).
- **주파수 재배치**(:8456-8501): 파일 상한 아래 최고 σ = ISIGTA(:8458-8469) → UFAC 스케일(:8478) → CHGBAS 로 "에너지 일정 유지" 보간(:8482) → **에너지→action 변환 `LSPEC=BAUX4/σ`**(:8489) → ISIGTA 위는 **멱법칙 진단 tail** `(σ_{ISIGTA}/σ)^{PWTAIL(1)+1}` 부가(:8494-8495; +1 = action 지수). 즉 해상도 변환 = 대역 재분배 + tail 연장 — Hs 별도 재정규화 없음.
- ★**읽기오류 경로의 IERR 미설정**(:8505-8519): 정상 IERR=0·EOF/데이터부족 IERR=9 인데 read-error(레이블 920)는 MSGERR(2) 후 IERR=0 인 채 RETURN — 호출부(:7964)는 IERR=9 만 검사하므로 **반쯤 읽힌 스펙트럼으로 계속 진행**되는 비종결 오류.

## 4. FLFILE (8524-8860) — 비정상 입력장 파일 엔진

- INPGRID NONSTATIONARY + READINP 의 런타임 측. 시간 전진: TIMCO 가 IFLEND 를 넘으면 ★**IFLTIM=1.E10 으로 무음 동결**(:8735-8739; EOF 도 동일 :8750-8754) — 마지막 장이 런 끝까지 유지.
- 공간 보간: 구조격자 = SVALQI 쌍선형 + 벡터의 입력격자→계산격자 회전(:8787-8794); 비구조(IGTYPE=3) = 동일 메시 정점 직접 복사(:8807-8808).
- ★**벡터 시간보간 = 크기 보존형**(:8828-8856): 성분 선형보간 후 벡터 길이를 '길이의 선형보간값' $W1\cdot|v_1|+W3\cdot|v_3|$ 로 재스케일(:8844-8850) — 방향 회전 시 크기 손실 방지. 원시 forcing 과 SWAN 내부 바람/해류 비교 시 유의.

크기 보정은 VTOT>0인 분기에 적용된다. `src/swanmain.ftn:8849` `COMPDA(INDX,JX2) = SIZE2*UU/VTOT`.
- 문서블록의 "IERR=9 on EOF"(:8634)는 사문 — 본문 어디서도 IERR≠0 설정 없음.

## 5. SWINCO (8864-9156) — 기본 초기조건 (INITIAL DEFAULT)

- 호출: SWMAIN :551 (NSTATC=1·ICOND=1 시 1회, 이후 ICOND=0 :557). HOTSTART 는 여기 아님(명령 해석부 swanpre 측).
- 초기화 취송거리는 영역 길이와 격자점 수로 만든 대표 간격이다. `src/swanmain.ftn:9003` `TLEN = (XCLEN + YCLEN)/2.`는 직교좌표의 길이 계산이다. `src/swanmain.ftn:9002–9011` `TLEN = LENDEG * (COSYG*XCLEN + YCLEN)/2.`는 구면좌표의 길이 계산이다. 구조 격자의 분모는 `src/swanmain.ftn:9008` `TDXY = FLOAT(MXCGL + MYCGL)/2.`이다. 비정규 격자는 `src/swanmain.ftn:9009` `IF ( nvertsg.NE.0 ) TDXY = FLOAT(nvertsg)`를 적용한다. 최종식은 `src/swanmain.ftn:9011` `FETCH = TLEN/TDXY`다.
- JONSWAP gamma는 공유 PSHAPE(1)을 사용한다. `src/swanser.ftn:4096` `SYF = PSHAPE(1)**PPSHAP`. `src/swanmain.ftn:9012` `SY0   = 3.3` 대입은 SSHAPE의 gamma 읽기가 아니다.
- 구조 격자의 내부점 검사는 해당 점과 x 방향 양쪽 이웃의 `KGRPNT>1`을 요구한다(:9028–9041). `IF (.NOT.ONED) THEN` 분기는 y 방향 양쪽 이웃도 검사한다(:9033–9038). `IF (WSLOC .GT. 1.E-10) THEN` 분기는 국지 바람으로 Kahma & Calkoen (1992) 취송거리 성장식과 Pierson–Moskowitz 상한을 적용한다(:9065–9078). 무차원 취송거리는 `FDLSS = GRAV * FETCH / (WSLOC*WSLOC)`이다(:9071). 무차원 파고는 `HSDLSS = MIN (0.21, 0.00288*FDLSS**0.45)`이다(:9074). 무차원 첨두주기는 `TPDLSS = MIN (1./0.13, 0.46*FDLSS**0.27)`이다(:9077). 이 분기에서 Hs<0.05 m이면 Tp=2 s를 적용한다(:9079). 풍속 조건의 ELSE 분기는 Hs=0.02 m를 대입한다(:9086). 같은 분기의 Tp는 2 s이다(:9087). DEFAULT의 주파수 종류와 방향 표현은 2·2로 고정한다. 근거는 `src/swanmain.ftn:9091`의 `CALL SSHAPE (AC2(1,1,INX), SPCSIG, SPCDIR, 2, 2)`이다. JONSWAP gamma는 공유 PSHAPE(1)을 사용한다. 근거는 `src/swanser.ftn:4096`의 `SYF = PSHAPE(1)**PPSHAP`이다. 비구조 격자에서는 `IF ( vmark(INX) == 0 .or. vmark(INX) >= excmark ) THEN`을 통과한 정점에 같은 초기화식을 적용한다(:9101–9149). [10-13 전수 검증 정정]

## 6. 판정 (I-6 종결)

- **재분류**: RBFILE·RESPEC·FLFILE·SWINCO = **C 티어(실질 로직, 본 노트가 file:line 커버)**. SNEXTI = 본 노트 §1 요약 + Froude 캡 명시로 커버. SWCLME·6708행 이전 = S요약 유지(적정).
- RBFILE은 경계 파일 소진 시 수준 1 메시지를 낸다(:8019). FLFILE은 입력 종료 시각을 넘거나 EOF를 만나면 `IFLTIM(IGR1) = 1.E10`을 적용한다(:8735–8754). RESPEC의 읽기오류 분기는 IERR를 새로 설정하지 않는다(:8507–8512). 1D 방향 분포의 FAC 보정은 §3에 정리했다. SWINCO의 대표 취송거리와 초기 스펙트럼 조건은 §5에 정리했다. 벡터 시간 보간의 크기 보정은 VTOT>0일 때 적용한다(:8844–8853). 1D 방향 분포의 반대 반원에는 `CDIR = 1.E-10`을 대입한다(:8369). [10-13 전수 검증 정정]

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

빈 인용 칸은 `—`로 표시한다. 표의 절 번호는 각 행이 링크한 대조 보고서의 절 번호다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:NT-044 | 초기 취송거리의 정의 | `source-analysis/swan-main-boundary-init-sourcemap.md:54` `"fetch" = 평균 격자셀 1칸`. 노트의 평균 격자셀 표현은 | `src/swanmain.ftn:9003` `TLEN = (XCLEN + YCLEN)/2.`; `src/swanmain.ftn:9008` `TDXY = FLOAT(MXCGL + MYCGL)/2.`; `src/swanmain.ftn:9009` `IF ( nvertsg.NE.0 ) TDXY = FLOAT(nvertsg)`; `src/swanmain.ftn:9011` `FETCH = TLEN/TDXY` | F 표기 차이 | 초기화 취송거리는 영역 길이와 격자점 수로 만든 대표 간격이다. 실제 셀 길이를 전부 산술평균한 값이라고 단정하지 않는다. 직교·구면 좌표의 길이 계산과 비구조 격자의 전체 정점 수 분모를 구분한다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) |
| R3:NT-045 | 1D 파일의 방향 하한 조건 | `source-analysis/swan-main-boundary-init-sourcemap.md:39` `1D 경계 스펙트럼은 어떤 방향 bin 도 정확히 0 이 되지 않음.` | `src/swanmain.ftn:8369` `CDIR = 1.E-10`; `src/swanmain.ftn:8372` `BAUX2(ID,IFRE) = CDIR * ETOT`; `src/swanser.ftn:4223` `CDIR = 0.` | C 문서 누락 | 양의 에너지를 읽은 1D 파일 경계는 반대 방향에도 작은 양의 밀도를 둔다. 입력 에너지가 0이면 결과도 0이다. `SSHAPE`로 만드는 매개변수 경계·초기 스펙트럼은 반대 반원에서 0이다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) |
| R4:T1-011 | 비정상 스칼라의 영역 밖 값 | swanuse PDF 19쪽 / 인쇄 11쪽: 스칼라는 “identical to … nearest boundary”; 유속·풍속은 “0 m/s … outside”. | `src/swanmain.ftn:4896` `WLVL = SVALQI (XP, YP, 7, WLEVL, 1 ,IX ,IY)`; `src/swanmain.ftn:7092` `IF (IFLDYN(7) .EQ. 1) THEN`; `src/swanmain.ftn:7093` `CALL FLFILE ( 7, 0, WLEVL, (/0./),`; `src/swanmain.ftn:8787` `UU = SVALQI (XP, YP, IGR1, ARR, 0, IX, IY)`; `src/swanmain.ftn:8788` `IF (IGR2.EQ.0) THEN`; `src/swanmain.ftn:8789` `COMPDA(INDX,JX3) = UU`; `src/swanmain.ftn:5560` `IF (.NOT.INGRD .AND. ZERO.EQ.0) THEN`; `src/swanmain.ftn:5561` `SVALQI = 0.`; `src/swanmain.ftn:5309`의 함수 선언에서 다섯째 인수는 `ZERO`이다. 위 4896행의 호출은 이 인수에 `1`을 전달한다. `src/swanmain.ftn:8835` `UU = W1 * COMPDA(INDX,JX2) + W3 * COMPDA(INDX,JX3)` | E 코드 결함 후보·강함 | 비정상 수위의 다음 입력장을 읽어 공간 보간할 때 정규 입력 격자의 영역 허용폭 밖에서 새 수위장 `JX3`을 0으로 만든다. 초기 읽기의 경계값 외삽과 다르다. 시간 보간 중의 `JX2`는 이전 값과 이 0을 가중 합한다. 스칼라 수위의 실제 호출 경로가 확인되어 강함으로 판정한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) [10-13 전수 검증 정정]
| R4:T1-192 | DEFAULT 모양 선택 | swanuse PDF 64쪽 / 인쇄 56쪽: “By default … JONSWAP … cos² … (options are available: see command BOUND SHAPE).” | `src/swanmain.ftn:9091` `CALL SSHAPE (AC2(1,1,INX), SPCSIG, SPCDIR, 2, 2)`; `src/swanpre1.ftn:6220` `CALL SSHAPE (AC2(1,1,1), SPCSIG, SPCDIR, FSHAPE, DSHAPE)` | B 문서 오기 | DEFAULT는 주파수 종류와 방향 표현을 2·2로 고정한다. JONSWAP gamma는 공유 PSHAPE(1)을 사용한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-240 | DEFAULT의 미소 초기장 | — | `src/swanmain.ftn:9065` `IF (WSLOC .GT. 1.E-10) THEN`; `src/swanmain.ftn:9079` `IF (SPPARM(1).LT.0.05) SPPARM(2) = 2.`; `src/swanmain.ftn:9086` `SPPARM(1) = 0.02`; `src/swanmain.ftn:9087` `SPPARM(2) = 2.`; `src/swanmain.ftn:9089` `SPPARM(4) = 0.`; `src/swanmain.ftn:9101` `IF ( vmark(INX) == 0 .or. vmark(INX) >= excmark ) THEN` | C 문서 누락 | SWINCO가 DEFAULT를 대입하는 점에서 `IF (WSLOC .GT. 1.E-10) THEN`의 ELSE 분기는 Hs=0.02 m·Tp=2 s를 사용한다. 구조 격자는 내부점 검사 뒤에 대입한다. 비정규 격자는 내부·예외·고스트 정점 분기에 대입한다. 양의 풍속 분기에서도 `IF (SPPARM(1).LT.0.05) SPPARM(2) = 2.`를 적용한다. swanuse PDF 64쪽 / 인쇄 56쪽에는 이 값과 조건이 없다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-305 | DEFAULT의 취송거리·gamma | `source-analysis/swan-main-boundary-init-sourcemap.md:54`의 `γ=3.3 하드코딩` | `src/swanmain.ftn:9011` `FETCH = TLEN/TDXY`; `src/swanser.ftn:4096` `SYF = PSHAPE(1)**PPSHAP`; `src/swanmain.ftn:9012` `SY0   = 3.3` | B 문서 오기 | 취송거리는 `FETCH = TLEN/TDXY`이다. 구조 격자의 `TDXY  = FLOAT(MXCGL + MYCGL)/2.`는 점 수로 만든 값이다. 비정규 격자에서는 `IF ( nvertsg.NE.0 ) TDXY = FLOAT(nvertsg)`를 적용한다. DEFAULT의 주파수 종류와 방향 표현은 2·2로 고정한다. JONSWAP gamma는 공유 PSHAPE(1)을 사용한다. 코드 내부의 SY0 선언 설명·대입과 실제 gamma 참조가 다른 점도 함께 적는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R7:H-1447 | 초기조건의 영 파고 경고 | `website/modifications/modifications.htm:1447–1448` `no warning &quot;Hsig=0&quot; in routine SSHAPE in`과 이어지는 `case of specifying initial conditions`. | `src/swanpre1.ftn:6171–6220` `IF (KEYWIS('PAR')) THEN`; `src/swanser.ftn:4027–4028` `IF (SPPARM(1).LE.0.)`; `src/swanmain.ftn:9085–9091` `SPPARM(1) = 0.02` | C 문서 누락 | 현재 자동 초기화의 무풍 분기는 `SPPARM(1) = 0.02`를 사용한다. 명시적 INIT PAR에서 HSIG를 0으로 주면 유효 격자의 SSHAPE 호출은 비양수 파고 경고를 낸다. 웹 변경 이력은 초기조건 종류를 구분하지 않는다. 이력의 적용 범위를 자동 초기화로 확정하지 않고 현재 두 경로의 조건을 함께 적는다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |

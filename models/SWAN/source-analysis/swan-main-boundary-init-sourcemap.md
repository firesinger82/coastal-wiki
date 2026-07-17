---
title: "swanmain.ftn 7469-9156 — 경계 스펙트럼 읽기(RBFILE)·해상도 변환(RESPEC)·비정상 입력장(FLFILE)·기본 초기조건(SWINCO) 소스맵"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "models/SWAN/raw/source_code/swan/src/swanmain.ftn (9338행, SWAN 41.xx 1993-2024 헤더 :7496) 직접 read — 7300-9200 구간 전수 + 전체 서브루틴 인벤토리 실측. I-6 문서축 재검토(2026-07-17) 산출 — Codex ② 5회차 'swanmain=driver S요약' 반박의 해소(실질 로직 4서브루틴 C티어 재분류)."
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

- **1D**(:8304-8379): 주파수별 `ETOT, ADEG, DD` 읽기. 방향 규약: BFILED(18)=1 이면 Cartesian도(度), 아니면 **Nautical→Cartesian** `ADIR=π(180+DNORTH-ADEG)/180` (:8328). 확산: 도 단위면 $MS=\max(FAC\cdot DSPR^{-2}-2,\,1)$ — ★**비문서화 경험 보정 FAC = 1.2 (DD>23°) / 1.096 (DD>17°) / 1.01** (change 41.99, :8332-8342). $\cos^{MS}$ 정규화는 MS≤10 감마함수·MS>10 점근식(:8357-8362), ★**off-peak 바닥값 1.E-10**(:8367-8369) — 1D 경계 스펙트럼은 어떤 방향 bin 도 정확히 0 이 되지 않음.
- **2D**(:8381-8454): WW3U 전치 읽기(:8386-8393)·DORDER<0 방향 역순(:8395-8401)·WW3F 고정 포맷 `(7E11.3)`(:8408-8410). 방향 재배치 = 주파수별 **CHGBAS**(에너지 보존 piecewise-constant 대역 재분배, swanser.ftn, :8450-8453).
- **주파수 재배치**(:8456-8501): 파일 상한 아래 최고 σ = ISIGTA(:8458-8469) → UFAC 스케일(:8478) → CHGBAS 로 "에너지 일정 유지" 보간(:8482) → **에너지→action 변환 `LSPEC=BAUX4/σ`**(:8489) → ISIGTA 위는 **멱법칙 진단 tail** `(σ_{ISIGTA}/σ)^{PWTAIL(1)+1}` 부가(:8494-8495; +1 = action 지수). 즉 해상도 변환 = 대역 재분배 + tail 연장 — Hs 별도 재정규화 없음.
- ★**읽기오류 경로의 IERR 미설정**(:8505-8519): 정상 IERR=0·EOF/데이터부족 IERR=9 인데 read-error(레이블 920)는 MSGERR(2) 후 IERR=0 인 채 RETURN — 호출부(:7964)는 IERR=9 만 검사하므로 **반쯤 읽힌 스펙트럼으로 계속 진행**되는 비종결 오류.

## 4. FLFILE (8524-8860) — 비정상 입력장 파일 엔진

- INPGRID NONSTATIONARY + READINP 의 런타임 측. 시간 전진: TIMCO 가 IFLEND 를 넘으면 ★**IFLTIM=1.E10 으로 무음 동결**(:8735-8739; EOF 도 동일 :8750-8754) — 마지막 장이 런 끝까지 유지.
- 공간 보간: 구조격자 = SVALQI 쌍선형 + 벡터의 입력격자→계산격자 회전(:8787-8794); 비구조(IGTYPE=3) = 동일 메시 정점 직접 복사(:8807-8808).
- ★**벡터 시간보간 = 크기 보존형**(:8828-8856): 성분 선형보간 후 벡터 길이를 '길이의 선형보간값' $W1\cdot|v_1|+W3\cdot|v_3|$ 로 재스케일(:8844-8850) — 방향 회전 시 크기 손실 방지. 원시 forcing 과 SWAN 내부 바람/해류 비교 시 유의.
- 문서블록의 "IERR=9 on EOF"(:8634)는 사문 — 본문 어디서도 IERR≠0 설정 없음.

## 5. SWINCO (8864-9156) — 기본 초기조건 (INITIAL DEFAULT)

- 호출: SWMAIN :551 (NSTATC=1·ICOND=1 시 1회, 이후 ICOND=0 :557). HOTSTART 는 여기 아님(명령 해석부 swanpre 측).
- ★**"fetch" = 평균 격자셀 1칸**: `FETCH = TLEN/TDXY` (:9011; "the mean delta" 주석 :9001) — 물리적 fetch 아님. γ=3.3 하드코딩(:9012).
- 진짜 내부점만(4방 KGRPNT>1, :9028-9040): 국지 바람으로 **Kahma & Calkoen (1992) fetch 성장 + PM 캡** — $H_s^*=\min(0.21,\,0.00288\,F^{*0.45})$·$T_p^*=\min(1/0.13,\,0.46\,F^{*0.27})$ (:9071-9078). ★하드코딩 바닥: Hs<0.05 m 이면 Tp=2 s(:9079). ★**무풍 = 0 상태가 아니라 미소 시드 Hs=0.02 m·Tp=2 s**(:9086-9089). 스펙트럼 형상은 사용자 BOUND SHAPE 무관 **JONSWAP+cos-power 하드와이어**(SSHAPE 인자 2,2, :9091). 비구조 격자 분기는 동일 로직 중복(:9099-9152).

## 6. 판정 (I-6 종결)

- **재분류**: RBFILE·RESPEC·FLFILE·SWINCO = **C 티어(실질 로직, 본 노트가 file:line 커버)**. SNEXTI = 본 노트 §1 요약 + Froude 캡 명시로 커버. SWCLME·6708행 이전 = S요약 유지(적정).
- 함정 요약(운용 관련성 순): 경계·입력장 **무음 동결 2종** / RESPEC 읽기오류 비종결 / 비문서화 FAC 보정 / SWINCO 셀 1칸 fetch·무풍 시드·JONSWAP 하드와이어 / 벡터 크기보존 보간 / 방향 바닥값 1.E-10.

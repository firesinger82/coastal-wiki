# FUNWAVE 노트 전수 검증 5

- 대상: `models/FUNWAVE/source-analysis/funwave-physics-sources.md`.
- 범위: 작업 시작 시 `git diff -U0 HEAD -- models/FUNWAVE/source-analysis/funwave-physics-sources.md`의 모든 추가 줄. Frontmatter를 포함한다.
- 판정 기준: 현재 코드, 인용한 과거 커밋 원문, 문서 쪽 이미지, 보고서의 최종 검증 기록과 최종 집계.
- 진행 상태: 완료.

## 검증 결과

대상 [funwave-physics-sources.md](../../../models/FUNWAVE/source-analysis/funwave-physics-sources.md)의 추가 줄 282줄을 모두 대조했다. Frontmatter 2줄을 포함한다. 빈 줄 8줄도 범위에 포함했다. 차이 표는 224행이다. 나머지는 본문·Frontmatter·표 설명·빈 줄을 합한 58줄이다.

정정은 12줄이다. 인용 보완은 2줄이다. 한 줄에 여러 표현을 고쳤어도 한 줄로 집계했다. 아래 줄 번호는 검증을 마친 노트의 물리 줄 번호다. 이번 정정으로 줄 번호는 바뀌지 않았다.

차이 표 224행의 분류와 결론은 각 보고서의 최종 검증 기록·최종 집계에 맞는다. A 행 25행의 커밋 HASH·날짜는 git 판정 기록과 맞는다. E 행 9행의 근거 강도도 최종 판정과 맞는다. 이번 정정은 이 분류와 결론 강도를 바꾸지 않았다.

## 대상 줄 대조 기록

범위는 작업 시작 시 저장한 추가 줄 목록이다. 각 범위의 모든 줄을 대조했다. 범위 사이의 기존 줄은 대조 줄 수에 넣지 않았다.

| 노트 줄 | 줄 수 | 대조 내용과 근거 | 결과 |
|---|---:|---|---|
| 5–6 | 2 | Frontmatter의 recovery 반영 설명·날짜. 기존 HEAD 설명과 `FUNWAVE-notes-apply-3.md` 반영 기록. | 일치. |
| 18–27 | 10 | 쇄파 계수·총수심 하한·호출 조건·전처리 분기·roller 상한. `io.F:3076–3103`, `breaker.F:64–66,124–125,248–337`; FT1-280·242, FX1-912, FN1-922. | 일치. |
| 39 | 1 | WK_TIME 입력 형식. `wavemaker.F`의 `WK_WAVEMAKER_TIME_SERIES`; FV2-404·FN1-256. | 일치. |
| 43–45 | 3 | 주파수 성분 입력과 문서의 MATLAB FFT 전처리. 3.0 p.37–38·48, 2.1 p.37·49; FV2-404. | 44행 인용 보완. |
| 61–74 | 14 | SourceX 식·마찰 입력·Smagorinsky 생산 경로·바람 조건·조파식. `sources.F`, `io.F`, `init.F`, `mod_meteo.F`; FT1-238·244·281, FV1-277·563, FV2-409. | 61·73·74행 정정. |
| 78–84 | 7 | 평균 출력 호출자·MASK9·습윤/마름·질량 보정·ETAtmp. `mixing.F:53–78,143–144,259`, `masks.F:64–242`; RF-012·041·050. | 78·79행 정정. |
| 88–108 | 21 | 절 제목·배정표·보고서 링크·A–F 정의·판 정보·표 머리·빈 줄. 배정표 3, 외부 출처 및 git 판정 보고서. | 일치. |
| 109–143 | 35 | theory-numerics의 같은 행 ID 전체. §4 수정안·§5 최종 결론·AD1·E1·원문. | 142행 정정. |
| 144–159 | 16 | inputs의 같은 행 ID 전체. §4 수정안·§5 최종 결론·AD1·E2·원문. | 145·158행 정정. |
| 160–171 | 12 | examples의 같은 행 ID 전체. §4 수정안·§5 최종 결론·AD1·E2·원문. | 일치. |
| 172–219 | 48 | v21-manual의 같은 행 ID 전체. §4 수정안·§5 최종 결론·AD2·E2·원문. | 일치. |
| 220–236 | 17 | v21-examples의 같은 행 ID 전체. §4 수정안·§5 최종 결론·AD2·원문. | 일치. |
| 237–273 | 37 | aux-docs-build의 같은 행 ID 전체. §4 수정안·§5 최종 결론·AD3·원문. | 237·238·245행 정정. |
| 274–325 | 52 | gpu-vs-tvd의 같은 행 ID 전체. §4 수정안·§5 최종 결론·E3·원문. | 315행 정정. 318행 인용 보완. |
| 326–332 | 7 | callflow의 같은 행 ID 전체. §4·§6·§8·최종 렌더 확인 절·E3·원문. | 일치. |
| 합계 | 282 | 원래 추가 줄 목록과 완료 시 추가 줄 목록이 같다. | 정정 12줄. 보완 2줄. |

## 근거와 판정 방법

현재 코드의 `FUNWAVE-TVD/…`와 `FUNWAVE-GPU/…`는 [raw/source_code](../../../models/FUNWAVE/raw/source_code/) 아래 경로다. 아래에서 판을 생략한 현재 `src/…`는 TVD 경로다. `HASH:경로:줄`은 해당 외부 저장소의 `git show HASH:경로`로 연 원문이다.

보고서는 [theory-numerics](../compare/funwave-theory-numerics-vs-code.md), [inputs](../compare/funwave-inputs-vs-code.md), [examples](../compare/funwave-examples-vs-code.md), [v21-manual](../compare/funwave-v21-manual-vs-code.md), [v21-examples](../compare/funwave-v21-examples-vs-code.md), [aux-docs-build](../compare/funwave-aux-docs-build-vs-code.md), [gpu-vs-tvd](../compare/funwave-gpu-vs-tvd.md), [callflow](FUNWAVE-callflow.md)를 사용했다. 끝의 전수 검증 기록과 최종 집계를 우선했다. 이력 판정은 [AD1](../compare/FUNWAVE-git-verify-AD1.md)·[AD2](../compare/FUNWAVE-git-verify-AD2.md)·[AD3](../compare/FUNWAVE-git-verify-AD3.md)와 [E1](../compare/FUNWAVE-git-verify-E1.md)·[E2](../compare/FUNWAVE-git-verify-E2.md)·[E3](../compare/FUNWAVE-git-verify-E3.md)를 사용했다. 판 정보는 [외부 출처 기록](../compare/FUNWAVE-external-sources.md)과 대조했다.

문서 문장은 [쪽별 판독 기록](../read/FUNWAVE/FUNWAVE-TVD/doc/)과 대조했다. 식·숫자는 지정된 300 dpi 쪽 이미지로 판정했다. 직접 연 이미지는 아래 55쪽이다.

| 문서 | 이미지 쪽 번호 | 쪽 수 |
|---|---|---:|
| `funwave_tvd_3.0.pdf` | 1, 10, 18, 21, 22, 25, 26, 27, 29, 31, 32, 37, 38, 39, 40, 41, 45, 46, 47, 48, 51, 52, 55, 59, 61, 62 | 26 |
| `funwave_tvd_2.1_manual.pdf` | 16, 18, 20, 23, 24, 25, 37, 38, 39, 40, 44, 45, 47, 49, 52, 53, 54, 56, 60, 68 | 20 |
| `Intro-to-FUNWAVE-CHL-TN.pdf` | 8, 12, 13, 17, 19, 20 | 6 |
| `funwave_code_analysis.pdf` | 3, 7, 12 | 3 |

전처리 플래그의 부재 주장은 aux-docs-build §2.5가 지정한 빌드 파일 39개와 대조했다. `IGNORE_BIG_SLOPE`, `VIS_DEPTH_RATIO`, `VIS_KENNEDY_ORIGINAL`, `VIS_STATIC_TRANS`의 선택 여부를 확인했다. README와 파일 목록은 빌드 파일 수에서 제외했다.

수정 전 HEAD의 삭제 줄은 5·17·29·48·52행이다. 5행의 반영 이력 추가는 [노트 반영 기록 3](FUNWAVE-notes-apply-3.md)과 맞는다. 17행의 쇄파 설명 교체는 FT1-280·FX1-912·FV1-561·FV2-403·FN1-922가 근거다. 29행의 WK_TIME 입력 설명 교체는 FV2-404·FN1-256이 근거다. 48행의 마찰·소스 설명 교체는 FX1-913·FT1-281·FV1-563·FV2-409가 근거다. 52행의 wet/dry·질량 보정 설명 교체는 RF-041·050이 근거다.

차이 표에 남은 기존 노트 17·48행과 README 18행의 인용은 수정 전 문장을 보존한 것이다. 읽기 전용 HEAD diff의 삭제 문장과 일치한다. 이 인용을 현재 노트의 식이나 현재 물리 줄 번호로 바꾸지 않았다.

## 정정·보완 목록

아래 파일명은 모두 대상 노트 `models/FUNWAVE/source-analysis/funwave-physics-sources.md`다. 각 수정 줄 끝에 해당 전수 검증 표식을 붙였다. 표 행의 표식은 결론 문장 칸 끝에 붙였다.

| 번호 | 구분 | 노트:줄 | 전 → 후 | 근거 원문 |
|---:|---|---|---|---|
| 1 | 보완 | `funwave-physics-sources.md:44` | 3.0 문서 `p.37–38` → `p.37–38·48`. MATLAB FFT 전처리를 직접 설명한 쪽을 보탰다. | `funwave_tvd_3.0.pdf` p.48 이미지의 `fft4wavemaker.m` 설명. FV2-404. |
| 2 | 정정 | `funwave-physics-sources.md:61` | `g·η/DX·(Depthx(I+1)−Depthx(I))` → `GRAV*(Eta(I,J))/DX*(Depthx(I+1,J)-Depthx(I,J))*MASK(I,J)`. 분산항의 `H` → `Max(H(I,J),MinDepthFrc)`. Manning 축약식 `−(g·n²/H^(1/3))` → `-(GRAV*Cd(I,J)**2/Max(H(I,J),MinDepthFrc)**(0.333333_SP))*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))`. `CARTESIAN` 조건을 명시했다. | `FUNWAVE-TVD/src/sources.F:232–260`. FT1-238·244, FV1-563. |
| 3 | 정정 | `funwave-physics-sources.md:73` | `FRICTION_SPONGE/BREAKWATER`, `WindForce`, `VISCOSITY_BREAKING`만 적은 조건 목록 → `CARTESIAN` 마찰 분기와 `METEO`의 `IF(WindForce)THEN`을 명시했다. 풍력식에 `MASK_WIND(I,J)`를 복원했다. 점성 조건은 `IF(VISCOSITY_BREAKING.OR.DIFFUSION_SPONGE.OR.WAVEMAKER_VIS)THEN`으로 고쳤다. HU 확산에는 `PQ_scheme` 거짓 조건을 명시했다. 선박·기압 항의 `VESSEL`·`METEO` 전처리 조건을 명시했다. | `FUNWAVE-TVD/src/sources.F:232,262–266,289–294,355–364,394–439,536–546`. FV1-563. |
| 4 | 정정 | `funwave-physics-sources.md:74` | `tanh(πt/Tr)` → `AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen`. 축약한 좌표·위상식 → `WaveMaker_Mass(I,J)= AA*EXP(-Beta_gen*(xmk_wk(I)-Xc_WK)**2) *SIN(rlamda*(ymk_wk(J)-ZERO)-2.0_SP*PI/Tperiod*TIME)`. | `FUNWAVE-TVD/src/sources.F:109–165`. FT1-244, FV1-563. |
| 5 | 정정 | `funwave-physics-sources.md:78` | “PREVIEW_MEAN 출력이 MIXING_STUFF 내부에서 발생한다” → MIXING_STUFF의 `IF( time >= STEADY_TIME )THEN`은 CALCULATE_MEAN을 호출한다. CALCULATE_MEAN의 `IF(T_sum.GE.T_INTV_mean)THEN`은 PREVIEW_MEAN을 호출한다. | `FUNWAVE-TVD/src/mixing.F:53–78,143–144,259`. callflow §6.1·RF-012. |
| 6 | 정정 | `funwave-physics-sources.md:79` | flooding·drying 축약 → `MASK_STRUC(I,J)==1`, `UseEtaScreen`, 현재 셀의 `Eta(I,J)>-Depth(I,J)` 조건과 내부 셀 Dmass 조건을 명시했다. `MASK(I,J)·MASK(I±1,J±1)` → 중심·상하좌우·대각선을 포함한 실제 9개 MASK 곱으로 고쳤다. `VISCOSITY_BREAKING` 참 분기의 값 1을 명시했다. 거짓 분기의 `ABS(Eta)/MAX(DEPTH,MinDepthFrc)>SWE_ETA_DEP` 조건과 값 0을 명시했다. | `FUNWAVE-TVD/src/masks.F:86–143,175–193`. FT1-013·125·126·250, RF-041·050. |
| 7 | 정정 | `funwave-physics-sources.md:142` | FT1-281의 `GPU FUNWAVE-TVD/src/init.F:332` → `GPU FUNWAVE-GPU/src/init.F:332`. | GPU `src/init.F:332`는 `nu_smg = ZERO`다. TVD `src/init.F:332`는 ghost cells 주석이다. theory-numerics §5 FT1-281. |
| 8 | 정정 | `funwave-physics-sources.md:145` | FI1-032의 `cab9425`(2016-03-02) 이력에 붙은 `FUNWAVE-TVD/src/init.F:332` → `cab9425:init.F:332`. | `git show cab9425:init.F`의 332행은 `nu_smg = ZERO`다. 이 커밋의 파일은 저장소 루트에 있다. git E2 FI1-032. |
| 9 | 정정 | `funwave-physics-sources.md:158` | FI1-280의 `6233886`(2019-06-16) 이력에 붙은 `FUNWAVE-TVD/src/io.F:2609` → `6233886:src/io.F:2609`. | 해당 커밋의 2609행은 `IF(ROLLER) VISCOSITY_BREAKING = .TRUE.`다. 2887행은 `CALL READ_LOGICAL(ROLLER,FILE_NAME,'ROLLER_EFFECT',ierr)`다. 현재 TVD 2609행은 다른 입력의 전처리문이다. git E2 FI1-280. |
| 10 | 정정 | `funwave-physics-sources.md:237` | FN1-009의 `bfc2f8c:src/masks.F:130` → `bfc2f8c:masks.F:130`. | `git show bfc2f8c:masks.F`의 124–134행. 해당 커밋의 파일은 저장소 루트에 있다. |
| 11 | 정정 | `funwave-physics-sources.md:238` | FN1-031의 `bfc2f8c:src/masks.F:130` → `bfc2f8c:masks.F:130`. | `git show bfc2f8c:masks.F`의 124–134행. FN1-009와 같은 원문이다. |
| 12 | 정정 | `funwave-physics-sources.md:245` | FN1-256의 “기존 보고서와 git 판정의 `FUNWAVE-TVD/src/etauv_solver.F:119–120` 인용” → “기존 보고서와 git 판정의 `7948152:src/etauv_solver.F:119–120` 인용”. | `7948152:src/etauv_solver.F:110–120`은 WK_REG다. 같은 파일 130–139행은 WK_TIME이다. 현재 TVD 119–120행은 불규칙파 분기의 좌표 대입이다. aux-docs-build §5 FN1-256. |
| 13 | 정정 | `funwave-physics-sources.md:315` | FG1-458의 GPU 원문·코드 원문 칸에 있는 `FUNWAVE-GPU/src/io.F:2904` 두 곳 → `FUNWAVE-GPU/src/io.F:2905`. | GPU `src/io.F:2904`는 빈 줄이다. 2905행에 SHOW_BREAKING 강제문이 있다. gpu-vs-tvd §5 FG1-458. |
| 14 | 보완 | `funwave-physics-sources.md:318` | FG1-601의 `CPU FUNWAVE-TVD/src/breaker.F:152` → `CPU FUNWAVE-TVD/src/breaker.F:151–172`. | 연령 조건과 중첩 ELSE, DXg·DYg 대입을 모두 포함한 원문 범위다. gpu-vs-tvd §5 FG1-601의 중간 강도는 유지했다. |

## 기계 확인 후보별 판정

번호는 사용자가 제시한 순서다. 중복 후보도 별도 행으로 기록했다. 제시된 29개 조각은 원문과 일치한다. 인접한 다른 인용의 오류는 위 정정 목록에 별도로 기록했다.

| 번호 | 후보·노트 위치 | 판정과 근거 원문 |
|---:|---|---|
| 1 | `src/masks.F:130` 뒤 “에도 같은 조건이 있다” · 109행 FT1-013 | 오탐. `7b93138:src/masks.F:130–131`은 `ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP` 조건이다. 현재 184–185행과 같다. |
| 2 | `src/init.F:332` 뒤 “의” · 111행 FT1-093 | 오탐. GPU `7f892ba:src/init.F:332`는 `nu_smg = ZERO`다. 함께 든 TVD `cab9425:init.F:332`도 같은 대입이다. |
| 3 | `src/masks.F:124` 뒤 “같은 분기…K13. 문서 시점 근거” · 112행 FT1-125 첫 인용 | 오탐. `7b93138:src/masks.F:124–134`는 `VISCOSITY_BREAKING`이 거짓인 ELSE에서 전환비를 검사한다. |
| 4 | `src/masks.F:124` 뒤 “같은 분기…확정 판정” · 112행 FT1-125 둘째 인용 | 오탐. 같은 커밋 124–134행의 ELSE 분기를 재인용한 것이다. AD1 FT1-125와 일치한다. |
| 5 | `src/masks.F:124` 뒤 “같은 분기…K13.” · 113행 FT1-126 첫 인용 | 오탐. `7b93138:src/masks.F:124–134`의 전환비는 점성 쇄파를 선택하지 않은 분기 안에 있다. |
| 6 | `src/masks.F:124` 뒤 “같은 분기…확정 판정” · 113행 FT1-126 둘째 인용 | 오탐. 같은 커밋 124–134행과 일치한다. FT1-013과 같은 조건이라는 설명도 맞는다. |
| 7 | `src/breaker.F:237` 뒤 마침표 · 116행 FT1-130 | 오탐. `7b93138:src/breaker.F:237`의 기본 대입은 `nu_break(I,J) = cap1*tmp2 + nu_bkg`다. |
| 8 | `src/breaker.F:113` 뒤 “의” · 120행 FT1-134 | 오탐. `7b93138:src/breaker.F:113–115`는 `SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`와 Cbrk1·Cbrk2의 곱을 쓴다. |
| 9 | `src/mod_global.F:372` 뒤 “도” · 121행 FT1-135 | 오탐. `7b93138:src/mod_global.F:372`의 Cbrk1은 0.65다. Cbrk2는 0.35다. |
| 10 | `src/sponge.F:590` 뒤 “도 같은 정수식” · 123행 FT1-144 | 오탐. `7b93138:src/sponge.F:590`에도 `R_sponge**(50*(I-1)/(Iwidth-1))`가 있다. 지수의 나눗셈 피연산자는 정수다. |
| 11 | `src/sponge.F:250` 뒤 마침표 · 124행 FT1-149 | 오탐. `7b93138:src/sponge.F:250`은 `tmp_2d_1(i,j)=MAX(CDsponge*TANH(ri/10.0),lim)`이다. |
| 12 | `src/sponge.F:248` 뒤 “도 같은” · 124행 FT1-149 | 오탐. `7b93138:src/sponge.F:248–250`은 `ri=MAX(0.0,REAL(Iwidth-I))`로 격자 인덱스 차를 만든다. 이어 같은 TANH 마찰식을 계산한다. |
| 13 | `src/wavemaker.F:1123` 뒤 마침표 · 127행 FT1-178 | 오탐. `7b93138:src/wavemaker.F:1123`은 `N_spec = 20.0_SP/sigma_theta`다. |
| 14 | `src/wavemaker.F:1122` 뒤 “도 같은 대입…확정 판정” · 127행 FT1-178 | 오탐. `7b93138:src/wavemaker.F:1122–1123`은 sigma_theta를 라디안으로 바꾼 다음 N_spec을 대입한다. |
| 15 | `src/etauv_solver.F:94` 뒤 “에서도 질량 소스였다…K19” · 129행 FT1-180 첫 인용 | 오탐. `7b93138:src/etauv_solver.F:94–106`의 WK 분기는 `R1`에 질량 소스를 더한다. |
| 16 | `src/etauv_solver.F:98` 뒤 “의 질량 소스 경로” · 129행 FT1-180 | 오탐. `7b93138:src/etauv_solver.F:98–106`에 WK_Source 누적과 이를 더하는 R1 대입이 있다. |
| 17 | `src/etauv_solver.F:94` 뒤 “에서도 질량 소스였다…확정 판정” · 129행 FT1-180 둘째 인용 | 오탐. 첫 인용과 같은 `7b93138:src/etauv_solver.F:94–106`의 질량 소스 경로다. AD1 FT1-180과 일치한다. |
| 18 | `src/mixing.F:113` 뒤 마침표 · 131행 FT1-187 | 오탐. `7b93138:src/mixing.F:113`은 `ETA2sum = (Eta-ETAmean)*(Eta-ETAmean)*DT + ETA2sum`이다. 이 대입은 뒤의 ETAmean 갱신보다 앞선다. |
| 19 | `source-analysis/funwave-physics-sources.md:17` 뒤 `tmp1=Cbrk1√(gh)` · 141행 FT1-280 | 오탐. 수정 전 HEAD 17행의 문장을 인용한 것이다. 읽기 전용 diff의 삭제 줄에 같은 식이 있다. 현재 식의 판정은 같은 표의 코드·결론 칸에 있다. |
| 20 | `README.md:18` 뒤 “쇄파를 bore로 처리, hybrid FV/FD” · 143행 FT1-286 | 오탐. `models/FUNWAVE/README.md`의 읽기 전용 HEAD diff에서 삭제된 18행과 일치한다. 보고서가 대조한 수정 전 소개 문장이다. |
| 21 | `src/init.F:324` 뒤 “와” · 145행 FI1-032 | 오탐. `739a08d:src/init.F:324`와 `cab6d74:src/init.F:329`는 모두 `nu_smg = ZERO`다. 같은 행의 다른 cab9425 인용 경로는 정정 목록 8번에서 고쳤다. |
| 22 | `src/io.F:1453` 뒤 “(2017-05-01)의 0 기본값 도입” · 165행 FX1-809 | 오탐. `285a6f6:src/io.F:1453`은 `Time_ramp = 0.0_SP`다. 날짜와 도입 판정은 AD1 FX1-809와 일치한다. |
| 23 | `models/FUNWAVE/source-analysis/funwave-physics-sources.md:17` 뒤 `tmp1=Cbrk1√(gh)` · 170행 FX1-912 문서 원문 칸 | 오탐. 수정 전 HEAD 17행의 식과 일치한다. 현재 줄 번호에 대한 코드 인용이 아니다. |
| 24 | 같은 `models/FUNWAVE/source-analysis/funwave-physics-sources.md:17` 후보 · 170행 FX1-912 코드 원문 칸 | 오탐. 같은 수정 전 HEAD 17행을 재인용했다. 뒤의 실제 breaker·io 인용과 구별되는 기존 노트 문장이다. |
| 25 | `models/FUNWAVE/source-analysis/funwave-physics-sources.md:48` 뒤 `Cd` · 171행 FX1-913 문서 원문 칸 | 오탐. 수정 전 HEAD 48행에 `Cd`와 “기본값 = 0.0(마찰 완전 off, 2026-07-12 확인)”이 있다. |
| 26 | 같은 `models/FUNWAVE/source-analysis/funwave-physics-sources.md:48` 후보 · 171행 FX1-913 코드 원문 칸 | 오탐. 같은 수정 전 HEAD 48행을 재인용했다. 현재 바닥 마찰·마찰 스펀지 구분은 같은 표의 결론에 있다. |
| 27 | `doc/funwave_tvd_3.0.tex:204` 뒤 세미콜론 · 188행 FV1-388 | 오탐. `24a88c3:doc/funwave_tvd_3.0.tex:204`는 Version 2.2가 eddy-viscosity 쇄파 알고리즘을 추가했다고 적는다. AD2 FV1-388의 문서 시점 근거와 일치한다. |
| 28 | `src/io.F:822` 뒤 “와” · 228행 FV2-306 | 오탐. `b9c035d:src/io.F:822`는 `CALL READ_FLOAT(MinDepth,FILE_NAME,'MinDepth',ierr)`다. |
| 29 | `src/io.F:828` 뒤 “두 입력을 따로 읽는다…2017…2018…2023” · 228행 FV2-306 | 오탐. `b9c035d:src/io.F:828`는 `CALL READ_FLOAT(MinDepthFrc,FILE_NAME,'MinDepthFrc',ierr)`다. MIN→MAX→MIN의 `285a6f6`(2017-05-01)·`d69acc3`(2018-05-25)·`93c0053`(2023-11-13)은 AD2 최종 이력 판정과 일치한다. |

## 완료 확인

A 행 25행의 HASH·날짜를 AD1·AD2·AD3 및 gpu-vs-tvd 최종 이력 표와 대조했다. FV1-388의 `cab9425` 날짜는 AD2의 “2016-03-02 first add to repository” 기록으로 확인했다.

E의 강함 3행은 FT1-166·FT1-247·RF-041이다. 중간 6행은 FT1-144·FI1-032·FI1-280·FX1-809·FV1-277·FG1-601이다. 보고서 최종 강도와 모두 일치한다.

노트의 상대 링크는 70건이다. 서로 다른 대상 파일은 18개다. 노트 위치에서 해석한 모든 링크가 실제 파일을 가리킨다. 절대 홈 경로와 위키 링크 표기는 0건이다. 지정된 한계 문구도 0건이다.

대상 노트에는 mermaid 블록이 없다. callflow의 흐름 관련 문장은 §4·§6·§8 및 끝의 렌더 확인 절과 대조했다.

완료 시 노트는 332줄이다. 최초 추가 줄 282줄과 완료 시 추가 줄 282줄의 위치가 모두 같다. 실제 수정한 14줄은 모두 이 범위 안에 있다. 정정 표식 12개와 보완 표식 2개가 해당 줄에 있다. 차이 표의 표식은 모두 결론 문장 칸 끝에 있다.

대조 완료: 282/282줄. 기계 확인 후보 판정 완료: 29/29건. 미해결 항목: 0건.

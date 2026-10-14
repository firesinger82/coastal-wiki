# ROMS 노트 전수 대조 19

- 작업일: 2026-10-14.
- 대상: 사용자 지정 노트 6개.
- 대조 범위: 기존 노트는 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄 전체다. 새 파일 `roms-test-cases-differences.md`는 전체 줄이다. frontmatter와 빈 줄도 줄 수에 포함한다.
- 판정 기준: 원문, 각 보고서 끝의 `전수 검증 기록 (10-14)`, git 판정 보고서와 외부 출처 보고서의 최종 보완 기록을 적용한다.
- 정정·보완 수는 변경한 대상 줄 수로 센다. 같은 줄을 여러 번 바꾸어도 한 줄로 센다.

## 완료 기록

노트별 대조를 마칠 때 아래에 결과를 추가한다.

## 1. roms_utility_numerics.md — 완료

- 대상: [roms_utility_numerics.md](../../../models/ROMS/source-analysis/roms_utility_numerics.md).
- 대조한 줄 수: 작업 시작 diff의 추가 줄 231개.
- 대조 줄: 7–8、20、22–23、75、80–91、97–173、184–199、251–254、256、266、292、310–312、330、334–442. 이 절의 줄번호는 수정 전후에 같다.
- 차이 표의 100행을 배정표와 최종 보고서에 대조했다. A 행의 커밋과 날짜를 A1·A7·A8 판정에 대조했다. E 행의 강함 판정을 E2와 최종 보고서에 대조했다.
- 현재 코드와 위키의 인용 위치를 열었다. 과거 판 인용은 `git show`로 열었다. 백틱 인용이 없는 본문의 file:line도 열었다.
- frontmatter의 반영일과 반영 기록은 apply-19와 일치한다. 삭제 전 문장은 RTN-368·385·405, RT2-397·398, RI1-1046·1048, OMD-N011의 수정안과 대조했다.
- 정정 수: 4줄. 보완 수: 2줄. 429줄은 정정과 보완에 함께 센다. 변경한 서로 다른 줄은 5개이다.
- 상대 파일 링크의 대상은 모두 존재한다. 대상 줄에 절대 홈 경로와 위키 링크 괄호는 없다. 대상 줄에 mermaid 블록은 없다. 대상 줄의 잔존 미분석 문장은 아래와 같이 교체했다.

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| roms_utility_numerics.md:75 | 정정 | 헤더 `set_scoord.F:11-12`, Shchepetkin `:9` → 헤더 `:12-13`, Shchepetkin `:10` | `ROMS/Utility/set_scoord.F:9`는 Arango와 라이선스를 적는다. `:10`은 Alexander F. Shchepetkin을 적는다. `:12-13`은 좌표 변환 변수의 초기화를 설명한다. |
| roms_utility_numerics.md:335 | 정정 | 난수 엔진의 `미세분석 안 함` → 분포와 출력 범위를 설명한 본문 절로 연결 | `ROMS/Utility/gasdev.F:78-81`은 평균 0·분산 1 Gaussian 벡터와 Numerical Recipes 출처를 설명한다. RT2-397·398의 수정안은 본문 251–254줄에 반영되어 있다. |
| roms_utility_numerics.md:420 | 정정 | 백틱 밖으로 분리된 제곱 기호 → 식 전체를 `Csur=-sc_w**2`로 표시 | `ROMS/Utility/set_scoord.F:444·499`의 식은 `Csur=-sc_w**2`이다. OMD-V295의 결론 의미는 유지했다. |
| roms_utility_numerics.md:427 | 보완 | 반례의 코드 근거가 `hwater=h(i,j)`에서 끝남 → 좌표식 `set_depth.F:158-171` 인용 추가 | `cff_w=hc*(sc_w-Cs_w)`, `z_w0=cff_w+Cs_w*hwater`, `z_w=z_w0+Zt_avg1*(1+z_w0/hwater)`가 RTN-340의 `C(s)=s` 반례를 뒷받침한다. |
| roms_utility_numerics.md:429 | 정정·보완 | 함수 1·2 모두 `theta_s≤0`이면 선형 → 함수 1은 `theta_s=0`, 함수 2는 `theta_s≤0`으로 구분하고 조건문 인용 추가 | `ROMS/Utility/set_scoord.F:212`는 `IF (theta_s(ng).ne.0.0_dp) THEN`이다. `:276`은 `IF (theta_s(ng).gt.0.0_dp) THEN`이다. RTN-345의 최종 보고서에도 같은 조건 오기가 남아 있어 직접 연 원문으로 정정했다. |

기계 확인 후보 판정:

- `Variables.wiki:2288`: 표시 글자 일치. 원문의 Ngrids·theta_s·Tcline 위키 링크를 표시 글자로 옮긴 차이이다. 정정 없음.
- `Variables.wiki:2289`: 표시 글자 일치. `theta_b(Ngrids)`의 Ngrids 위키 링크를 제거한 차이이다. 정정 없음.
- `Variables.wiki:2295`: 표시 글자 일치. Ngrids·theta_b·Tcline 위키 링크를 표시 글자로 옮긴 차이이다. 정정 없음.
- `Variables.wiki:2296`: 표시 글자 일치. `theta_s(Ngrids)`의 Ngrids 위키 링크를 제거한 차이이다. 정정 없음.
- `Vertical_S-coordinate.wiki:160`: 표시 글자 일치. `Vtransform = 2`와 `Vstretching = 4`의 링크를 제거한 문장이다. 정정 없음.
- `Vertical_S-coordinate.wiki:29`: 표시 글자 일치. 변환 `(1)`의 내부 링크를 제거한 발췌이다. 정정 없음.

미해결 항목: 없음.

## 2. roms_open_boundaries.md — 완료

- 대상: [roms_open_boundaries.md](../../../models/ROMS/source-analysis/roms_open_boundaries.md).
- 대조한 줄 수: 작업 시작 diff의 추가 줄 69개.
- 대조 줄: 6–7、21、41、67、82、109、120、128–129、133–136、142–143、163、168、172–173、176、185–186、204–249.
- 차이 표의 35행은 배정표와 최종 보고서의 분류·결론에 일치한다. A 행 RMF1-382·390·401의 커밋과 날짜는 A7 판정에 일치한다. E 행은 없다.
- 현재 코드와 위키의 인용 위치를 열었다. 과거 판의 경계 기본값·Chapman 식·T_LBC 선언은 `git show`로 열었다.
- `Cha`와 `Che`의 대응, `gamma2=-1`, 유입 계수와 시간척도의 역수 관계, 방향별 periodic 설정, `FSOBC_REDUCED` 조건, `VolCons`의 면적·유량 합산을 대조했다.
- 본문 교체와 삭제는 RMF1-931·932·933, RI1-1064·1065, RI1-0614·0689, RMF1-877의 근거와 일치한다. frontmatter는 apply-12의 반영 기록과 일치한다.
- 정정 수: 0줄. 보완 수: 0줄. 정정 목록: 없음.
- 대상 줄의 상대 파일 링크는 모두 존재한다. 대상 줄에 절대 홈 경로·위키 링크 괄호·한계 문장은 없다. 대상 줄에 mermaid 블록은 없다.
- 지정된 기계 확인 후보: 없음.

미해결 항목: 없음.

## 3. roms_vertical_mixing.md — 완료

- 대상: [roms_vertical_mixing.md](../../../models/ROMS/source-analysis/roms_vertical_mixing.md).
- 대조한 줄 수: 작업 시작 diff의 추가 줄 84개.
- 대조 줄: 6–7、29、36–41、56–58、70、74、96–99、110–113、124、137–138、140–142、147、168–222. 이 절의 줄번호는 수정 전후에 같다.
- 차이 표의 45행은 배정표와 최종 보고서의 분류·결론에 일치한다. RMF1-279는 최종 기록의 C에서 D로 변경한 판정을 따른다. RMF1-917은 최종 기록의 H에서 B로 변경한 판정을 따른다. A·E 행은 없다.
- RMF1-267의 D 판정은 D1과 일치한다. 외부 출처 보고서의 마지막 보완 표에는 이 노트의 대상 행을 바꾸는 판정이 없다.
- 코드·위키 인용 위치를 열었다. GLS의 nstp 속도와 혼합계수 소비 순서, 길이 상한과 psi 하한, 로그 마찰식, 표면 거칠기 선택, Ric·GLS_CMU0 값, 점성 단위를 대조했다.
- frontmatter와 삭제 전 문장은 apply-17 및 RMF1-913–922, OMD-N007, RTN-395·411, RF1-023의 수정안과 대조했다.
- 정정 수: 3줄. 보완 수: 1줄. 74줄은 두 집계에 포함한다. 변경한 서로 다른 줄은 3개이다.
- 대상 줄의 상대 파일 링크는 모두 존재한다. 대상 줄에 절대 홈 경로·위키 링크 괄호·검수 대기 문장은 없다. 대상 줄에 mermaid 블록은 없다.

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| roms_vertical_mixing.md:70 | 정정 | 신규 적용이 일반적으로 GLS를 선택한다는 문장에 `source-needed`만 부착 → RMF1-915가 적용 권고(H)로 분류한 사실과 보고서 링크 | 보고서 §4 RMF1-915는 신규 적용의 일반적 선택 성향을 코드 대조의 검증 결과로 쓰지 말라고 명시한다. |
| roms_vertical_mixing.md:74 | 정정·보완 | `RI_HORAVG/VERAVG/SPLINES=Ri 평활(stability function 무관)` → 전단 계산 선택과 Richardson 수 평활을 구분하고 Akv·Akt 연결 인용 추가 | `ROMS/Nonlinear/lmd_vmix.F:178-240`의 LMD_RIMIX·RI_SPLINES 분기, `:245-306`의 수평·연직 평활, `:326-356`의 Rig·nu_sx·Akv·Akt 대입. OMD-N007의 최종 보완과 일치시켰다. |
| roms_vertical_mixing.md:124 | 정정 | 적용별 권고 제목의 `source-needed` → 기존 노트 권고에 대한 RMF1-916의 H 분류와 보고서 링크 | 보고서 §4 RMF1-916은 이 표를 기존 노트의 적용별 권고로 분류한다. RTN-411은 권고 조합을 코드 의무 조건으로 옮기지 말라고 명시한다. |

- 지정된 기계 확인 후보: 없음.
- 미해결 항목: 없음.

## 4. roms-exercises-catalog.md — 완료

- 대상: [roms-exercises-catalog.md](../../../models/ROMS/manual-notes/roms-exercises-catalog.md).
- 대조한 줄 수: 작업 시작 diff의 추가 줄 27개.
- 대조 줄: 7–8、38–39、41–47、62–64、99–111. 이 절의 줄번호는 수정 전후에 같다.
- 차이 표의 6행은 배정표와 최종 보고서의 분류·결론에 일치한다. A·E 행은 없다.
- Exercise 2·3·5·6·7·8·9의 PDF 쪽 수와 대상 행의 제목·위치·설명을 원문에 대조했다. Exercise 8은 1–2쪽을 열었다. 나머지 대상 실습은 1쪽을 열었다.
- `tidal_ellipse.pdf` 2쪽은 파일을 추가하지 않고 메모리에서 렌더해 확인했다. ap2ep·ep2ap 변환과 cBEpm 연직 조류속 설명이 62줄에 일치한다.
- 현재 코드의 반복 범위, RPCG·MINRES 분기, Lanczos 근사, Nimpact 단일 외부 반복, ImpOrd=3, OBS_SPACE별 외부 forcing 선택을 대조했다.
- frontmatter와 본문 교체는 apply-8 및 DA1-822·823, RT2-399–403, RF2-008·018, RTG-1989, RTN-412에 대조했다.
- 정정 수: 3줄. 보완 수: 0줄.
- 대상 줄의 상대 파일 링크는 모두 존재한다. 대상 줄에 절대 홈 경로·위키 링크 괄호·한계 문장은 없다. 대상 줄에 mermaid 블록은 없다.

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| roms-exercises-catalog.md:38 | 정정 | 비선형 cost를 연속 선형 최소화로 근사 → 일련의 선형 최소제곱 최소화로 비선형 비용함수의 최소화를 근사하려는 절차 | `roms_test/WC13/I4DVAR/Exercise_2.pdf` 1쪽은 `sequence of linear least-squares minimizations`와 `(hopefully) approximate minimization of the nonlinear cost function`을 적는다. |
| roms-exercises-catalog.md:39 | 정정 | 세 가지 preconditioning → 세 가지 해법 조합 | `roms_test/WC13/RBL4DVAR/Exercise_3.pdf` 1쪽은 같은 R^-1/2 전처리의 CG·MINRES와 B 전처리의 RPCG를 나열한다. RT2-399도 세 해법으로 구분한다. |
| roms-exercises-catalog.md:43 | 정정 | Array modes를 행렬 고유쌍으로 표현 → 행렬 고유쌍으로 구성한 모드로 표현 | `roms_test/WC13/ARRAY_MODES/Exercise_7.pdf` 1쪽은 고유쌍 `(lambda_i, w_hat_i)`와 상태 증분의 모드 `Psi_i(t)`를 구분한다. |

- 지정된 기계 확인 후보: 없음.
- 미해결 항목: 없음.

## 5. roms_representer_model.md — 완료

- 대상: [roms_representer_model.md](../../../models/ROMS/source-analysis/roms_representer_model.md).
- 대조한 줄 수: 작업 시작 diff의 추가 줄 58개.
- 대조 줄: 7–8、22、72–76、113–116、148–149、156–166、199、209–211、217–239、241–246. 이 절의 줄번호는 수정 전후에 같다.
- 차이 표의 4행은 배정표와 최종 보고서의 분류·결론에 일치한다. A·E 행은 없다.
- 명시한 상위 드라이버의 RPM 호출을 열었다. R4DVAR의 prior·analysis RPM, 내부 반복의 ADM·공분산·TLM, DATALESS_LOOPS와 FrequentImpulse 조건을 대조했다.
- Representer 전체장 보정, lambda=1, LF-AM3 include, congrad의 식, 최소화기 호출과 zgrad0·cg_beta·px의 대입을 대조했다.
- frontmatter와 삭제 전 문장은 apply-5 및 RT2-366·390·391, RTN-384·388, RF2-032, callflow-da의 RPM impulse 수정안에 대조했다.
- 정정 수: 2줄. 보완 수: 2줄. 변경한 서로 다른 줄은 4개이다.
- 대상 줄의 상대 파일 링크는 모두 존재한다. 대상 줄에 절대 홈 경로·위키 링크 괄호·미검증 문장은 없다. 대상 줄에 mermaid 블록은 없다.

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| roms_representer_model.md:116 | 정정 | MyRank를 넘기는 wrt_impulse만 제시 → DISTRIBUTE의 MyRank와 그 외의 -1 호출을 구분 | `ROMS/Drivers/r4dvar.F:1376-1380`의 전처리 분기. `:1365-1369`는 분석에 쓸 impulse 파일 기록을 설명한다. |
| roms_representer_model.md:163 | 보완 | NLM의 현재 단계 확산식만 인용 → RPM의 `rp_pre_step3d.F:1337-1364` 추가 | RPM도 `cff3=dt(ng)*(1.0_r8-lambda)`로 현재 단계 추적자 확산을 계산한다. RTN-384의 공통 lambda 설명을 RPM의 직접 근거와 연결했다. |
| roms_representer_model.md:164 | 보완 | NLM의 미래 단계 확산식만 인용 → RPM의 `rp_step3d_t.F:1479-1500` 추가 | RPM은 미래 단계 확산의 `cff=-dt(ng)*lambda`와 `FC`, `tl_FC`를 구성한다. |
| roms_representer_model.md:245 | 정정 | 항목명과 원문 열에 대조 전 미검증 상태를 재전사 → 해법의 항목명만 같은 원문 줄에서 발췌 | RT2-391의 수정안은 congrad의 식과 행렬 작용을 제시한다. 원문 200줄의 `dual(observation-space) cost-function 최소화 알고리즘(켤레경사·Lanczos)·representer 계수 해법`은 그대로 보존했다. C 분류와 최종 결론은 유지했다. |

- 지정된 기계 확인 후보: 없음.
- 미해결 항목: 없음.

## 6. roms-test-cases-differences.md — 완료

- 대상: [roms-test-cases-differences.md](../../../models/ROMS/manual-notes/roms-test-cases-differences.md).
- 대조한 줄 수: 새 파일 전체 27줄. frontmatter와 빈 줄을 포함한다.
- 대조 줄: 1–27.
- frontmatter의 작성·대조 기록은 apply-3과 일치한다. `related`의 roms-wiki-overview.md는 같은 디렉터리에 존재한다.
- 배정표의 RT1-275와 최종 보고서의 B 판정은 27줄에 일치한다.
- `Test_Cases.wiki:141`의 empty 표기와 `SHOREFACE_CASE.wiki:7·14`의 실제 본문을 대조했다. 해빈 경사 1/80, 파고 2 m, 주기 10 s, 입사각 10도, 방향 구간 90개, 주파수 구간 30개, 0.04–0.5 Hz 인용이 모두 일치한다.
- `ROMS/Include/cppdefs.h:709`의 SHOREFACE 설명을 대조했다.
- 정정 수: 0줄. 보완 수: 0줄. 정정 목록: 없음.
- 상대 파일 링크는 모두 존재한다. 절대 홈 경로·위키 링크 괄호·한계 문장은 없다. mermaid 블록은 없다.
- 지정된 기계 확인 후보: 없음.
- 미해결 항목: 없음.

## 최종 집계

| 노트 | 대조한 대상 줄 | 차이 표 행 | 정정 줄 | 보완 줄 | 변경한 서로 다른 줄 |
|---|---:|---:|---:|---:|---:|
| roms_utility_numerics.md | 231 | 100 | 4 | 2 | 5 |
| roms_open_boundaries.md | 69 | 35 | 0 | 0 | 0 |
| roms_vertical_mixing.md | 84 | 45 | 3 | 1 | 3 |
| roms-exercises-catalog.md | 27 | 6 | 3 | 0 | 3 |
| roms_representer_model.md | 58 | 4 | 2 | 2 | 4 |
| roms-test-cases-differences.md | 27 | 1 | 0 | 0 | 0 |
| 합계 | 496 | 191 | 12 | 5 | 15 |

- 대상 줄 수는 기존 노트의 작업 시작 diff와 새 파일 전체에서 셌다. 수정 후 같은 방식으로 다시 센 줄 수는 모두 같다.
- 정정·보완 수는 대상 줄 끝의 이번 작업 태그에서 셌다. 두 태그가 함께 있는 줄은 utility 429줄과 vertical_mixing 74줄이다.
- 차이 표 행 수는 각 노트에서 보고서 약칭과 행 ID가 있는 행을 셌다.
- 지정된 인용 불일치 후보 6개는 원문 표시 글자와 모두 일치한다.
- 최종 대상 줄 검사에서 끊어진 상대 파일 링크, 절대 홈 경로, 위키 링크 괄호, 검수 대기 문장은 발견되지 않았다.
- 대상 줄의 mermaid 블록은 0개이다.
- 대상 노트 6개의 완료 절과 정정 목록을 기록했다. 미해결 항목은 없다.

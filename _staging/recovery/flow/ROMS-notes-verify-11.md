# ROMS 노트 전수 대조 11

- 작업일: 2026-10-14.
- 대상: `roms_biology-differences-1.md` 전체 줄, `roms_stability_gst.md`와 `roms_tracer_timestep_step3d_t.md`의 작업 시작 시점 `git diff -U0 HEAD` 추가 줄.
- 대조 기준: 현재 코드, 인용된 과거 커밋, 로컬 위키 원문, 보고서 끝의 최종 검증 기록.
- 줄 수에는 frontmatter와 빈 줄을 포함한다.
- 정정 수와 보완 수는 변경한 대상 줄 수로 센다.
- 기계 확인 불일치 후보: 사용자 제공 목록에 후보가 없다.

## 완료 — roms_biology-differences-1.md

- 대조한 줄 수: 172줄. 새 파일의 1–172줄 전체를 셌다.
- 정정 수: 0줄.
- 보완 수: 4줄.
- 차이 표 143행을 `roms-biology-vs-code.md` §5 및 끝의 작업 1/2·2/2 검증 기록과 대조했다. 배정표의 143개 행 ID와 일치한다.
- 결론 분류와 결론 문장은 최종 보고서와 일치한다. ES-057의 추가 이력 문장은 `ROMS-git-verify-E1.md:49`의 `4a631f7d`·2004-05-05와 일치한다. 이 날짜는 저장소 도입일이다.
- E 행의 강도는 강함 16행과 중간 3행이다. 노트의 결론 열에서 센 값이며 최종 보고서와 일치한다.
- 수정 전 원문 인용 1,873개를 현재 파일과 과거 커밋에서 열어 대조했다. 보완 후 인용 1,882개도 모두 일치한다.
- frontmatter의 모델 구성·파일 줄 수를 현재 소스와 대조했다. 문서 수집일은 `raw/manuals/wiki/manifest.json`과 일치한다. 코드 판은 보고서의 `57aecf58`·2026-09-18과 일치한다. 4.3 표기는 `ROMS/Modules/mod_ncparam.F:653`과 일치한다.
- 상대 링크와 related 경로는 실제 파일을 가리킨다. Mermaid 블록은 없다. 절대 경로·이중 대괄호·요청된 한계 문구는 없다.
- 기계 확인 후보 판정: 후보 없음.
- 미해결 항목: 없음.

보완 목록의 줄 번호는 보완 후 노트 기준이다. 이번 보완은 줄 수를 바꾸지 않았다.

| 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|
| `roms_biology-differences-1.md:33` (FE-004) | 엽록소 농도 단위 인용 없음 → 코드 원문 칸에 현재 `varinfo.yaml:4450` 인용 추가. 결론 문장 끝에 `[10-14 전수 검증 보완]` 추가. | `ROMS/External/varinfo.yaml:4450`의 `units: milligrams_chlorophyll meter-3`. `roms-biology-vs-code.md` §5 FE-004의 차원 근거. |
| `roms_biology-differences-1.md:91` (UN-004) | 엽록소 농도 단위 인용 없음 → 코드 원문 칸에 현재 `varinfo.yaml:4450` 인용 추가. 결론 문장 끝에 보완 표식 추가. | `ROMS/External/varinfo.yaml:4450`의 엽록소 농도 단위와 `ROMS/Nonlinear/Biology/fennel.h:710–714`의 감쇠식. 최종 보고서 UN-004. |
| `roms_biology-differences-1.md:92` (UN-005) | 엽록소 농도 단위 인용 없음 → 코드 원문 칸에 현재 `varinfo.yaml:4450` 인용 추가. 결론 문장 끝에 보완 표식 추가. | `ROMS/External/varinfo.yaml:4450`의 엽록소 농도 단위와 `ROMS/Nonlinear/Biology/ecb.h:789–794`의 감쇠식. 최종 보고서 UN-005. |
| `roms_biology-differences-1.md:101` (UN-014) | 철 농도의 위키·과거 메타데이터만 인용 → 현재 철 메타데이터의 단위·인덱스·배율 인용 6개 추가. 결론 문장 끝에 보완 표식 추가. | `ROMS/External/varinfo.yaml:4307,4310,4313,4351,4354,4357`. 두 철 추적자의 단위는 `millimole_iron meter-3`이고 배율은 `1.0d0`이다. 인덱스는 `idTvar(iFdis)`와 `idTvar(iFphy)`이다. 최종 보고서 UN-014 및 `ROMS-git-verify-E1.md:70`. |

## 완료 — roms_stability_gst.md

- 대조한 줄 수: 52줄. 작업 시작 시점의 추가 줄은 6–7, 13–14, 19, 36–43, 53, 57, 61–62, 64–98이다.
- 정정 수: 4줄.
- 보완 수: 1줄.
- 차이 표 26행을 da-4dvar·inputs·outputs-metadata·testcases 보고서의 최종 §5와 끝의 검증 기록에 대조했다. 배정표의 26개 행 ID와 일치한다.
- 결론 분류와 문장 의미는 최종 보고서와 일치한다. DA1-702의 문장 분리는 원문의 조건을 보존한다. E 행 11개의 강함 판정은 최종 보고서와 E1 판정을 보존한다.
- A 행 4개의 SOstate 도입·교체 이력은 D1의 최종 판정과 일치한다. `5b09cd6f`의 도입일은 2007-02-06이다. `58dde87b`의 교체일은 2011-03-25이다. 인용된 과거판을 `git show`로 대조했다.
- 수정 전 원문 위치 441개를 열었다. 직접 인용 428개는 원문과 일치했다. 인용문이 없는 13개 위치도 문맥을 대조했다. 수정 후 원문 위치 457개와 직접 인용 429개를 다시 확인했다.
- DA1-808의 NCV 검사 보완은 `read_phypar.F:628–650`과 일치한다. 위키의 NCV 조건과 FTE 후단 오류 처리도 함께 대조했다.
- frontmatter와 연결 경로를 대조했다. 상대 링크는 실제 파일을 가리킨다. Mermaid 블록은 없다. 수정 후 절대 경로·이중 대괄호·한계 문구는 없다.
- 기계 확인 후보 판정: 후보 없음.
- 미해결 항목: 없음.

정정·보완 목록의 줄 번호는 수정 후 노트 기준이다. 이번 수정은 줄 수를 바꾸지 않았다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `roms_stability_gst.md:19` | 정정 | 다른 노트가 다루지 않는 분석이라는 범위 단언 → OP의 안정성 분석과 관측 민감도 드라이버의 역할을 직접 근거로 설명. | `ROMS/Drivers/op_roms.h:10–16`, `obs_sen_i4dvar_analysis.h:10–16`. da-4dvar 보고서 DA1-808의 OP 구분 및 관측 민감도 설명. |
| `roms_stability_gst.md:36` | 정정 | ARPACK이 모델 적분을 반복 호출한다고 설명 → FTE·OP 적분 순서를 구분하고 OP 드라이버가 ARPACK과 전파자를 호출한다고 설명. | `ROMS/Drivers/propagator_fte.h:12–16`, `propagator_op.h:12–17`, `op_roms.h:401–430,487`. da-4dvar 보고서 DA1-702·DA1-808의 드라이버·고유문제 구분. |
| `roms_stability_gst.md:53` | 정정 | pert를 단순 교란 전파로 설명. tlcheck를 내적 검사로 설명. split을 GST까지 일반화 → pert의 INNER_PRODUCT·SANITY_CHECK, tlcheck의 선형화 검사, 세 split 드라이버의 4D-Var 분할을 각각 설명. | `ROMS/Drivers/pert_roms.h:12–31`, `tlcheck_roms.h:10–13`, `split_i4dvar_roms.h:17–36`, `split_r4dvar_roms.h:18–37`, `split_rbl4dvar_roms.h:18–37`. build-options-history 보고서 RBH-0386·RBH-1335·RBH-1545 및 da-4dvar 보고서 DA1-030·DA1-807. |
| `roms_stability_gst.md:57` | 정정 | 근거 없는 81·70·55 집계와 모든 커널의 exact 1:1 대응 및 미작성 설명 → 수반·접선형·representer 추적자 루틴의 원문 역할과 전치 관계 검사 드라이버를 설명. | `ROMS/Adjoint/ad_step3d_t.F:14–18`, `ROMS/Tangent/tl_step3d_t.F:14–18`, `ROMS/Representer/rp_step3d_t.F:14–18`, `ROMS/Drivers/pert_roms.h:12–26`. build-options-history 보고서 RBH-2850 및 da-4dvar 보고서 DA1-824는 exact 설명과 검증 결과를 구분한다. 현재 각 디렉터리 바로 아래 `*.F`와 `*.h` 합계는 83·72·55이다. |
| `roms_stability_gst.md:73` (DA1-023) | 보완 | resid 저장 필요성을 결론에만 명시 → 코드 원문 칸에 resid 할당 줄 추가. | `ROMS/Modules/mod_storage.F:271`의 `allocate ( STORAGE(ng) % resid(Mstr(ng):Mend(ng)) )`. 최종 보고서 DA1-023. |

## 완료 — roms_tracer_timestep_step3d_t.md

- 대조한 줄 수: 79줄. 작업 시작 시점의 추가 줄은 2, 6–7, 21–22, 24, 26–33, 37, 39–43, 45–49, 52–53, 60–66, 73–75, 78–80, 86–91, 94–96, 102–105, 107–132이다.
- 정정 수: 15줄.
- 보완 수: 6줄. 127줄은 정정과 보완에 함께 포함한다. 변경한 고유 줄 수는 20줄이다.
- 차이 표 17행을 callflow-nonlinear §8과 inputs·mixing-bc-forcing·theory-numerics §5 및 끝의 최종 검증 기록에 대조했다. 배정표의 17개 행 ID와 일치한다.
- 모든 차이 행의 결론 분류를 유지했다. RTN-168의 후속 검증 지시 문장은 같은 보고서 §2의 성능 주장 설명으로 바꿨다. 이 변경은 사용자의 한계 문장 제거 지시를 적용한 것이다. 다른 행의 결론 문장은 유지했다.
- 수정안 RF1-024, RI1-1056, RTN-375·384·386·387·392를 본문과 대조했다. mean-age의 두 시간 슬롯, OMEGA_IMPLICIT의 MPDATA 제외 조건, spline·표준 확산의 행렬, lambda=1, 누징과 경계 교환 순서를 원문에서 확인했다.
- 수정 후 원문 위치 표기 176개를 열었다. 이 표기들은 15개 파일의 고유 원문 797줄을 가리킨다. 직접 인용 조각 239개는 위키 표시 글자 정규화 후 모두 일치했다. 이 집계는 코드·위키 인용과 본문의 축약 줄 표기를 대상으로 한다. 보고서가 보존한 수정 전 노트 인용은 해당 보고서 및 작업 시작 시점 diff의 삭제 줄과 따로 대조했다.
- 본문 39–43줄의 Fortran 블록은 `step3d_t.F:905–909`와 공백까지 일치한다.
- frontmatter의 문헌 위치를 정정했다. 상대 링크는 실제 파일을 가리킨다. Mermaid 블록은 없다. 대상 줄에 절대 경로·이중 대괄호·한계 문구는 없다.
- 기계 확인 후보 판정: 사용자 제공 후보 없음. 추가 대조에서 발견한 RI1-0692의 위키 표시 인용 오류는 117줄에서 정정했다.
- 미해결 항목: 없음.

정정·보완 목록의 줄 번호는 수정 후 노트 기준이다. 이번 수정은 줄 수를 바꾸지 않았다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `roms_tracer_timestep_step3d_t.md:2` | 정정 | 제목의 OMEGA_IMPLICIT 연직 이류·확산 묶음 → 조건부 음해 연직 이류와 연직 확산을 구분. | `ROMS/Nonlinear/step3d_t.F:1553,1567,1654–1664`. OMEGA_IMPLICIT 블록은 확산 블록 전에 끝난다. |
| `roms_tracer_timestep_step3d_t.md:6` | 정정 | Zhang 문헌 위치를 생성항 1824–1825로 표기하고 다른 노트의 미커버 상태를 기재 → 문헌 위치 1813–1814와 실제 대조 범위를 기재. | `ROMS/Nonlinear/step3d_t.F:478–481,1813–1814`. 생성항과 서지 주석은 서로 다른 위치이다. RF1-024의 수정 범위와 사용자의 한계 문장 제거 지시. |
| `roms_tracer_timestep_step3d_t.md:33` | 정정 | 축약식 `oHz=1/Hz`와 주석 줄 382 → 실제 대입식 `oHz(i,j,k)=1.0_r8/Hz(i,j,k)`와 두 대입 위치. | `ROMS/Nonlinear/step3d_t.F:388,396`. |
| `roms_tracer_timestep_step3d_t.md:37` | 정정 | 스킴 분기 뒤 보존형 갱신이라는 포괄 설명 → 해당 갱신이 수평 MPDATA를 제외한 ELSE 경로임을 명시. | `ROMS/Nonlinear/step3d_t.F:873,899–909`. RF1-024의 MPDATA 별도 경로와 RTN-392의 flux-form 갱신. |
| `roms_tracer_timestep_step3d_t.md:49` | 정정 | private Ta와 양정치 필요를 묶은 설명 → 수평 MPDATA의 실제 Ta 대입을 명시. | `ROMS/Nonlinear/step3d_t.F:873–880`. RF1-024의 중간장 경로. |
| `roms_tracer_timestep_step3d_t.md:73` | 정정 | 대상이 불명확한 두 경로 → spline 확산과 표준 확산을 명시. | `ROMS/Nonlinear/step3d_t.F:1664–1696,1730–1748`. theory-numerics §4 RTN-387의 수정안. |
| `roms_tracer_timestep_step3d_t.md:74` | 보완 | 전진 소거 범위만 인용하면서 후진 대입까지 설명 → 두 경로의 후진 대입 범위까지 인용. | `ROMS/Nonlinear/step3d_t.F:1686–1709,1752–1788`. 후진 대입은 1707줄과 1787줄에 있다. |
| `roms_tracer_timestep_step3d_t.md:78` | 정정 | 연직 보정 flux 위치 1442를 갱신 위치로 설명하고 Ta 사용을 TLM·ADM 미지원의 원인으로 단정 → 속도 계산·수평 flux·수평 갱신·연직 flux·연직 갱신을 구분. 미지원 사실은 별도 원문 주석으로 인용. | `ROMS/Nonlinear/step3d_t.F:1376–1397,1406–1417,1425–1429,1447–1450,1468–1469`. `ROMS/Tangent/tl_step3d_t.F:25`는 미지원 사실을 명시한다. RF1-024는 Ta와 보정 flux 경로를 근거로 든다. |
| `roms_tracer_timestep_step3d_t.md:86` | 정정 | nnew 슬롯을 쓰는 mean-age 생성항을 무조건적으로 설명 → 수평·연직 MPDATA 조건과 나머지 분기의 슬롯 3을 구분. | `ROMS/Nonlinear/step3d_t.F:1822–1828`. RI1-1056이 인용한 1824–1825의 상위 조건과 ELSE 분기를 함께 적용했다. |
| `roms_tracer_timestep_step3d_t.md:91` | 정정 | 측면 경계조건은 주석 1837로 인용. MPI 교환은 주기 경계 주석 1908로 인용. 누징 조건은 LnudgeTCLM만 기재 → 실제 호출 위치와 각 조건을 명시. | `ROMS/Nonlinear/step3d_t.F:1858–1862,1866–1874,1880–1906,1910–1925`. 측면 경계조건 뒤 누징 순서는 RI1-1056의 기존 노트 대조와 같다. |
| `roms_tracer_timestep_step3d_t.md:94` | 정정 | OMEGA_IMPLICIT의 이류와 확산이라는 묶음 → 이류의 `IF (.not.Vadvection(itrc,ng)%MPDATA) THEN` 조건과 후속 확산 블록을 구분. | `ROMS/Nonlinear/step3d_t.F:1553–1567,1654–1664`. |
| `roms_tracer_timestep_step3d_t.md:103` | 정정 | 연결 노트의 step3d_t 위치 22 → 현재 소스 목록의 23. | `models/ROMS/source-analysis/roms_baroclinic_3d.md:23`. |
| `roms_tracer_timestep_step3d_t.md:105` | 정정 | pre_step3d를 LF-AM3의 짝으로 일괄 설명 → 추적자 predictor와 이류 선택별 Gamma 분기로 설명. | `ROMS/Nonlinear/pre_step3d.F:622–626`. RF1-024와 RTN-127은 모든 경로를 하나의 LF-AM3 이름으로 묶지 않는다. |
| `roms_tracer_timestep_step3d_t.md:116` (RF1-024) | 정정 | 수정 전 노트 인용에 미커버 상태 문장 포함 → 수정 전 인용임을 명시하고 오류 대상인 첫 문장만 발췌. | `ROMS-callflow-nonlinear.md:2211`의 RF1-024 원문. 인용한 첫 문장은 보고서 원문과 같다. 결론은 유지했다. |
| `roms_tracer_timestep_step3d_t.md:117` (RI1-0692) | 정정 | 위키 링크 대상인 Variables#Hout·Variables#Qout·Variables#Aout와 구분자가 표시 인용에 남음 → 표시 글자인 Hout(inert), Qout(inert), Qout(Snert), Aout(inert)만 보존. | `roms.in.wiki:167,175,182`. 원문의 링크 표시 글자와 대조했다. 결론은 유지했다. |
| `roms_tracer_timestep_step3d_t.md:125` (RTN-127) | 보완 | Gamma=1/6 결론에 대응하는 대입 인용 없음 → `Gamma=1.0_r8/6.0_r8` 추가. | `ROMS/Nonlinear/pre_step3d.F:626`. theory-numerics §2 RTN-127. |
| `roms_tracer_timestep_step3d_t.md:127` (RTN-168) | 정정·보완 | Gamma=1/2 대입 인용 없음. 해당 격자에서 별도 검증하라는 지시 → 대입 인용 추가. 위키의 손실 설명이 수치 성능 주장임을 명시. | `ROMS/Nonlinear/pre_step3d.F:624`. `Numerical_Solution_Technique.wiki:533`. theory-numerics §2 RTN-168은 얕은 수심·큰 조차에서의 손실 크기를 성능 주장으로 구분한다. |
| `roms_tracer_timestep_step3d_t.md:130` (RTN-386) | 보완 | 배열 단위 설명의 머리말과 DO문만 인용 → 실제 단위 표와 농도 변환·층 두께 가중 대입을 추가. | `ROMS/Nonlinear/step3d_t.F:23–25,27–28`, `ROMS/Nonlinear/pre_step3d.F:899–901,998–1000`. theory-numerics §4 RTN-386. |
| `roms_tracer_timestep_step3d_t.md:131` (RTN-387) | 보완 | 상수와 DO문만 인용 → 서로 다른 행렬 계수와 같은 형태의 소거식을 추가. | `ROMS/Nonlinear/step3d_t.F:1691–1696,1747–1748,1761–1763`. theory-numerics §4 RTN-387. |
| `roms_tracer_timestep_step3d_t.md:132` (RTN-392) | 보완 | 층 두께 항과 flux 계산의 일부만 인용 → nnew 대입과 flux 발산 합산·갱신까지 추가. | `ROMS/Nonlinear/pre_step3d.F:1000`, `ROMS/Nonlinear/step3d_t.F:907–909`. theory-numerics §4 RTN-392. |

## 최종 집계

| 노트 | 대조한 대상 줄 | 정정 줄 | 보완 줄 | 변경한 고유 줄 |
|---|---:|---:|---:|---:|
| roms_biology-differences-1.md | 172 | 0 | 4 | 4 |
| roms_stability_gst.md | 52 | 4 | 1 | 5 |
| roms_tracer_timestep_step3d_t.md | 79 | 15 | 6 | 20 |
| 합계 | 303 | 19 | 11 | 29 |

대상 줄 수는 작업 시작 시점의 전체 줄 또는 추가 줄에서 셌다. 정정·보완 수는 각 노트의 `[10-14 전수 검증 정정]`·`[10-14 전수 검증 보완]` 표식을 줄별로 셌다. 두 집계에 함께 포함된 줄은 추적자 노트 127줄이다.

최종 읽기 전용 diff에서 기존 두 노트의 추가 줄 집합은 시작 시점과 같다. 이번에 변경한 모든 줄은 처음 지정한 대상 집합 안에 있다. 세 노트의 YAML과 대상 줄의 상대 링크 검사를 통과했다. 모든 대상 줄의 대조를 완료했다.

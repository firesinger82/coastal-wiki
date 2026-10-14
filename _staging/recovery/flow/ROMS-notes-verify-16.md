# ROMS 노트 추가·수정 줄 전수 대조 — 16

대상 줄은 작업 시작 시 `git -C /home/firesinger/coastal-wiki diff -U0 HEAD -- <노트>`에서 센 추가 줄이다.
frontmatter와 빈 줄을 대상 줄 수에 포함했다.
정정 수와 보완 수는 이번 작업에서 바꾼 대상 줄 수로 센다.
노트의 줄 번호는 해당 노트 검증 완료 시점을 기준으로 적는다.
보고서의 최종 「전수 검증 기록 (10-14)」을 결론 판정에 적용한다.

| 대상 노트 | 시작 시 대상 줄 수 | 상태 |
|---|---:|---|
| `models/ROMS/source-analysis/roms_4dvar.md` | 367 | 완료 |
| `models/ROMS/source-analysis/roms_nesting.md` | 101 | 완료 |
| `models/ROMS/source-analysis/roms_barotropic_2d.md` | 71 | 완료 |
| `models/ROMS/source-analysis/roms_adjoint_framework.md` | 38 | 완료 |

시작 시 대상 줄의 합계는 위 표에서 센 577줄이다.

## roms_4dvar.md — 완료

대조한 대상 줄은 시작 시 diff에서 센 367줄이다.
정정은 4줄이다.
보완은 1줄이다.
대조 범위는 `6–7, 16, 20–21, 35–39, 41–45, 49, 51, 56–61, 71–76, 86–95, 97, 99, 105–106, 109–111, 115, 122, 138–139, 296–297, 365, 382, 389, 396–397, 405, 408, 428, 430, 450, 454–455, 462–764`이다.

차이 표의 130행을 해당 보고서의 최종 분류·결론과 대조했다.
표에서 센 A 20행의 커밋 HASH와 날짜를 A5·A6·A8·D1 판정과 대조했다.
DA1-200과 DA1-612·615에는 최종 보고서가 정정한 커밋을 적용한 상태임을 확인했다.
표에서 센 E 9행의 조건과 강도를 최종 보고서 및 E1·E2 판정과 대조했다.
DA1-704의 중간 강도와 RF2-028의 강함은 각 보고서의 최종 판정대로 유지했다.
본문의 삭제·대체 근거는 DA1-800–804, RT2-385–388, OMD-N015 및 호출 흐름 보고서 §6에서 확인했다.
Mermaid 블록 3개는 호출 흐름 보고서 §4와 같다.
각 상자의 호출·정의·분기 줄을 현재 코드에서 확인했다.
인용 직후 발췌가 없는 코드 참조도 해당 원문 구간을 열어 대조했다.
과거 판 참조는 해당 커밋 또는 태그의 `git show` 원문과 대조했다.
frontmatter의 이번 반영 날짜와 검증 방법은 반영 기록 12와 맞는다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 보완 | `models/ROMS/source-analysis/roms_4dvar.md:106` | 내부 반복 잔차만 설명했다. | 관측 파일의 분산과 I4DVAR 작업 배열의 역분산을 구별했다. dual 경로의 분산 유지 조건을 보탰다. | `ROMS/Utility/obs_read.F:273–290`의 관측오차 읽기와 `# ifndef WEAK_CONSTRAINT` 아래 `ObsErr(iobs)=1.0_r8/ObsErr(iobs)`이다. 호출 흐름 보고서 §6.1의 관측 오차 수정안이다. |
| 정정 | `models/ROMS/source-analysis/roms_4dvar.md:109` | DAV 쓰기에 병합 전 `i4dvar.F:723–735,2404–2417`과 `rbl4dvar.F:2773–2780`을 인용했다. | 현재 I4DVAR의 `741–754,2423–2436`과 RBL4DVAR의 `2786–2799`를 인용했다. | `ROMS/Drivers/i4dvar.F:741,749,2423,2431`과 `ROMS/Drivers/rbl4dvar.F:2786,2794`는 두 I/O 경로의 비용 쓰기 호출이다. DA1-803의 최종 일치 판정은 유지했다. |
| 정정 | `models/ROMS/source-analysis/roms_4dvar.md:744` | 읽기 결함 후보의 위치를 `3절`로 적었다. | 이 노트 차이 표의 `OMD-K028`로 적었다. | 출력 보고서 §3의 OMD-K028과 이 노트의 같은 행은 규모별 자료 읽기 결함 후보를 다룬다. 원문의 `3절`은 출력 보고서 안의 위치이다. |
| 정정 | `models/ROMS/source-analysis/roms_4dvar.md:745` | 응력 단위 인용의 `N/m2`가 `models/ROMS/source-analysis/m2`로 바뀌었다. 열 플럭스 단위 인용의 `W/m2`에서 `W/`가 빠졌다. | 반복 인용 두 곳씩을 각각 `N/m2 (Pa)`와 `W/m2`로 복원했다. | `ROMS/Utility/get_state_std_nf90.h:638`은 `scale=1.0_dp/rho0`와 `N/m2 (Pa) to m2/s2`를 적는다. 같은 파일 763줄은 `scale=1.0_dp/(rho0*Cp)`와 `W/m2 to Celsius m/s`를 적는다. |
| 정정 | `models/ROMS/source-analysis/roms_4dvar.md:760` | mono 정의와 헤더 선택을 모두 `tl_convolution_multi.h:121,95–99`로 연결했다. | 두 mono 헤더의 121줄과 두 convolution.F의 95–99줄로 연결했다. | `ROMS/Adjoint/ad_convolution_mono.h:121`과 `ROMS/Tangent/tl_convolution_mono.h:121`은 5인수 정의이다. `ROMS/Adjoint/ad_convolution.F:95–99`와 `ROMS/Tangent/tl_convolution.F:95–99`는 multi·mono 선택이다. RF2-026의 E 강함 판정은 유지했다. |

대상 줄의 상대 링크 35개는 노트 위치에서 실제 파일로 연결된다.
대상 줄에 `/home/firesinger/`와 `[[`는 없다.
대상 줄에 실행·확인 미수행, 미검수 또는 후속 대상으로 남기는 한계 문장은 없다.
사용자가 지정한 기계 확인 후보는 이 노트에 없다.
미해결 항목은 없다.

## roms_nesting.md — 완료

대조한 대상 줄은 시작 시 diff에서 센 101줄이다.
정정은 1줄이다.
보완은 2줄이다.
대조 범위는 `6–7, 33–34, 37, 52–56, 69, 72, 89–90, 110–111, 113–137, 141, 155–213`이다.

차이 표의 50행을 해당 보고서의 최종 분류·결론과 대조했다.
표에서 센 A 17행의 HASH·날짜는 A1·A6 및 출력 보고서의 최종 판정과 맞는다.
표에서 센 E 2행은 최종 보고서와 E1의 강함 판정을 유지한다.
본문 수정·삭제는 RCN-1963–1972, RT1-1528, RTG-1988의 수정안과 대조했다.
각 인용의 현재 코드와 위키를 열었다.
과거 판 인용은 해당 HASH의 `git show` 원문과 대조했다.
`RefineSteps` 식과 공간 비율을 구분한 설명은 원문과 맞는다.
접촉 수·가중치 수·입력 순서·총 적분 시간 검사 조건은 원문과 맞는다.
frontmatter의 이번 반영 날짜와 검증 방법은 반영 기록 18과 맞는다.
대상 줄에는 Mermaid 블록이 없다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 보완 | `models/ROMS/source-analysis/roms_nesting.md:120` | 양방향 갱신 호출에 `main3d.F:1103`의 조건문만 인용했다. | 인용을 `1103–1104`로 넓혔다. | `ROMS/Nonlinear/main3d.F:1103`은 `IF (do_twoway(iNLM, nl, il, ng, istep)) THEN`이다. 1104줄은 `CALL nesting (ng, iNLM, n2way)`이다. RCN-1948의 설명을 유지했다. |
| 보완 | `models/ROMS/source-analysis/roms_nesting.md:135` | 오류 반환에 `read_phypar.F:214–218`을 인용했다. | 인용을 `214–219`로 넓혔다. | `ROMS/Utility/read_phypar.F:218`은 `exit_flag=5`이다. 219줄은 `RETURN`이다. RCN-1969의 조건과 결론은 유지했다. |
| 정정 | `models/ROMS/source-analysis/roms_nesting.md:141` | COAWST·Python 대안을 포함한 도구 후속 작성 항목을 남겼다. | `contact.m`의 함수 이름을 원문에 근거한 문장으로 바꿨다. | `Grid_Processing_Scripts.wiki:99–100`은 `contact.m`의 이름과 접촉점 설정 기능을 적는다. RTG-1988의 최종 결론은 함수 이름을 확인하며 도구 선택 권고와 구분한다. |

수정 후 대상 줄의 상대 링크 20개는 실제 파일로 연결된다.
대상 줄에 `/home/firesinger/`와 `[[`는 없다.
대상 줄에 실행·확인 미수행, 미검수 또는 후속 대상으로 남기는 한계 문장은 없다.
사용자가 지정한 기계 확인 후보는 이 노트에 없다.
미해결 항목은 없다.

## roms_barotropic_2d.md — 완료

대조한 대상 줄은 시작 시 diff에서 센 71줄이다.
정정은 0줄이다.
보완은 0줄이다.
대조 범위는 `6–7, 23, 25, 29–30, 33–37, 68–73, 81–83, 92–94, 96–98, 100, 102–112, 133–165`이다.
정정 목록은 없다.

차이 표의 26행은 해당 보고서의 최종 분류·결론과 일치한다.
표에서 센 A 2행의 `57c231d3`·`2007-03-23`은 A8 판정과 맞는다.
표에서 센 E 2행의 강함은 E2 및 최종 보고서와 맞는다.
RF1-003은 최종 보고서가 바꾼 B 판정을 반영했다.
RTN-218은 최종 보고서가 바꾼 F 판정을 반영했다.
본문 수정·삭제는 RTN-382·406, RI1-1061–1063, 호출 흐름 보고서 §6의 N-03·RF1-019·020·029, OMD-N030과 대조했다.
현재 코드의 각 인용과 과거 HASH 인용을 열어 대조했다.
Legacy의 `nfast+1` 보조 호출, 예측·수정 조건, 2D 전용 입력 검사와 수송 평균식은 원문과 맞는다.
frontmatter의 이번 반영 날짜와 검증 방법은 반영 기록 19와 맞는다.
대상 줄에는 Mermaid 블록이 없다.

기계 확인 후보의 판정은 다음과 같다.

- `models/ROMS/source-analysis/roms_barotropic_2d.md:156`, `Variables.wiki:2499`: 일치한다. 위키 링크와 굵게 표시를 제외한 표시 글자는 `:dimension = ubar(LBi:UBi,LBj:UBj,3)`이다. 노트는 맞으므로 유지했다.
- `models/ROMS/source-analysis/roms_barotropic_2d.md:156`, `Variables.wiki:2500`: 일치한다. 위키 링크와 굵게 표시를 제외한 표시 글자는 `:pointer = OCEAN(ng)%ubar`이다. 노트는 맞으므로 유지했다.
- `models/ROMS/source-analysis/roms_barotropic_2d.md:157`, `Variables.wiki:2550`: 일치한다. 위키 링크와 굵게 표시를 제외한 표시 글자는 `:dimension = vbar(LBi:UBi,LBj:UBj,3)`이다. 노트는 맞으므로 유지했다.
- `models/ROMS/source-analysis/roms_barotropic_2d.md:157`, `Variables.wiki:2551`: 일치한다. 위키 링크와 굵게 표시를 제외한 표시 글자는 `:pointer = OCEAN(ng)%vbar`이다. 노트는 맞으므로 유지했다.

대상 줄의 상대 파일 링크 7개는 실제 파일로 연결된다.
같은 노트의 차이 표로 가는 절 링크 1개도 맞는다.
대상 줄에 `/home/firesinger/`와 `[[`는 없다.
대상 줄에 실행·확인 미수행, 미검수 또는 후속 대상으로 남기는 한계 문장은 없다.
미해결 항목은 없다.

## roms_adjoint_framework.md — 완료

대조한 대상 줄은 시작 시 diff에서 센 38줄이다.
정정은 8줄이다.
보완은 0줄이다.
대조 범위는 `2, 6–7, 20, 22, 25, 28, 30, 33–37, 47–50, 56, 62–64, 69, 73–77, 79–89`이다.

차이 표의 2행은 최종 보고서의 분류와 결론 문장에 일치한다.
CD-003은 C 판정을 유지했다.
RF2-020은 B 판정을 유지했다.
이 표에는 A·E 행이 없다.
본문의 삭제·대체는 DA1-824, RF2-020 및 CD-003과 대조했다.
기존 노트 인용의 43줄은 읽기 전용 diff에 나타난 변경 전 문장과 같다.
현재 코드 참조는 인용 직후 발췌가 없는 위치까지 열어 대조했다.
생물 dispatcher의 실행 include와 주석 처리 조건은 원문과 맞는다.
외부 반복별 NLM·RPM 궤적 구분은 원문과 맞는다.
frontmatter의 이번 반영 날짜는 반영 기록 6과 맞는다.
frontmatter의 파일 수와 파일 이름은 아래 목록대로 정정했다.
세 디렉터리 직하위 `.F` 파일 수의 합계는 65+54+39=158이므로 본문 62줄의 합계는 유지했다.
대상 줄에는 Mermaid 블록이 없다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | `models/ROMS/source-analysis/roms_adjoint_framework.md:6` | `ad_*.F`를 65개로 적었다. Picard 파일 이름을 `picard.h`로 적었다. | 직하위 `.F` 65개를 `ad_*.F` 63개와 `adsen_*.F` 2개로 구분했다. 파일 이름을 `picard_roms.h`로 고쳤다. | 현재 `ROMS/Adjoint/` 직하위 파일 목록의 비접두사 파일은 `adsen_force.F`와 `adsen_initial.F`이다. `ROMS/Drivers/picard_roms.h:10–14`는 Picard 시험 드라이버를 설명한다. |
| 정정 | `models/ROMS/source-analysis/roms_adjoint_framework.md:20` | 출처 없는 `gold standard` 평가를 붙였다. 파일 수의 집계 범위를 생략했다. | 평가 문구를 지웠다. 각 디렉터리 직하위 `.F` 파일 수와 노트의 설명 범위를 적었다. | 현재 `ROMS/Adjoint/`, `ROMS/Tangent/`, `ROMS/Representer/`의 직하위 `.F` 목록은 각각 65개, 54개, 39개이다. DA1-824는 의도된 transpose 관계를 근거로 제시하며 모델 간 우월성 판정을 제시하지 않는다. |
| 정정 | `models/ROMS/source-analysis/roms_adjoint_framework.md:47` | multiscale B·Dirac·CG를 모두 내부 반복으로 설명했다. | 내부 최소화 설명과 별도의 Dirac 상관모델 시험을 구분했다. | `ROMS/Drivers/correlation.h:427–448`은 Dirac Delta 시험과 `ana_perturb`·`convolve` 호출이다. 내부 최소화는 호출 흐름 보고서 §2 및 `ROMS/Drivers/i4dvar.F:1232,1303–1305,1365–1367,1513–1524`와 대조했다. |
| 정정 | `models/ROMS/source-analysis/roms_adjoint_framework.md:63` | D-Flow FM 유동 수치해법 노트를 BMI·OpenDA EnKF/DUD의 근거로 연결했다. | Delft3D-FLOW의 `flow2d3d_openda` DLL 인터페이스와 연동 시험 설명을 연결했다. | `models/Delft3D/raw/source_code/Delft3D/src/third_party_open/openda/tests/doc/README.txt:3–7,35–43`은 DLL 함수와 여러 모델 인스턴스의 진행 시험을 설명한다. 기존 링크의 노트는 `furu`·`s1nod`·`step_reduce_hydro`의 유동 수치해법을 다룬다. |
| 정정 | `models/ROMS/source-analysis/roms_adjoint_framework.md:64` | BMI와 Beach Wizard를 OpenDA·black-box ensemble 설명에 묶었다. | Beach Wizard의 바닥 높이 갱신과 BMI의 외부 제어 인터페이스를 구분했다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/beachwizard.F90:589–603`은 `bchwiz`가 1 또는 2일 때 `s%zb = s%zb - bw%dassim`을 적용한다. 같은 디렉터리의 `xbeach_bmi.f90:43–78`은 C 바인딩 초기화·시간 진행 함수를 정의한다. |
| 정정 | `models/ROMS/source-analysis/roms_adjoint_framework.md:69` | 다른 모델을 모두 외부 자료동화로 묶었다. ADCIRC·SWAN의 주된 방법을 출처 없이 일반화했다. | 직접 근거가 있는 ROMS 변분 드라이버 제공 문장으로 고쳤다. | `Master/roms_kernel.F:153–166`은 I4DVAR·RBL4DVAR·R4DVAR 드라이버를 선택한다. 기존 일반화는 RF2-020·DA1-824의 결론에 없다. XBeach의 내부 바닥 높이 갱신은 위 64줄의 원문으로 확인했다. |
| 정정 | `models/ROMS/source-analysis/roms_adjoint_framework.md:73` | 연결된 노트의 배경오차 공분산·최소화 알고리즘 전체를 내부 반복으로 한정했다. | 연결된 노트가 설명하는 두 주제를 적었다. | `ROMS/Drivers/correlation.h:427–448`의 공분산 시험과 `ROMS/Drivers/i4dvar.F:1513–1524`의 내부 최소화는 별도 경로이다. `roms_4dvar.md`는 두 경로를 설명한다. |
| 정정 | `models/ROMS/source-analysis/roms_adjoint_framework.md:77` | Beach Wizard와 D-Flow FM 유동 수치해법 링크를 모두 OpenDA로 설명했다. | 각 링크를 바닥 높이 갱신 설명과 유동 수치해법 설명으로 구분했다. | `xbeach_beachwizard.md`의 본문과 `beachwizard.F90:589–603`은 바닥 높이 갱신을 다룬다. `delft3d_dflowfm_kernel_scheme.md` §2–4는 `furu`·`s1nod`·`step_reduce_hydro`를 다룬다. |

수정 후 대상 줄의 상대 파일 링크 24개는 실제 파일로 연결된다.
frontmatter의 YAML 구문은 정상이다.
대상 줄에 `/home/firesinger/`와 `[[`는 없다.
대상 줄에 실행·확인 미수행, 미검수 또는 후속 대상으로 남기는 한계 문장은 없다.
사용자가 지정한 기계 확인 후보는 이 노트에 없다.
미해결 항목은 없다.

## 전체 완료

대조한 대상 줄은 네 노트의 시작 시 diff에서 센 577줄이다.
정정은 노트별 기록을 합한 13줄이다.
보완은 노트별 기록을 합한 3줄이다.
기계 확인 후보 4건은 모두 위키 표시 글자가 같은 경우였다.
쓰기 대상은 지정된 노트와 이 기록으로 한정했다.

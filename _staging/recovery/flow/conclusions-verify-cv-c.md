# ADCIRC 묶음 C — 10-12 결론 검증

검증일은 2026-10-12이다. 대상은 작업 시작 때 각 노트에 실행한 `git diff -U0 HEAD -- <노트>`의 추가 줄이다. `+++` 파일 머리글은 제외했다. 빈 줄과 표 구분선도 대상 줄 수에 포함했다. 작업 중 정정한 줄을 다시 새 대상으로 세지 않았다.

원래 추가된 물리적 줄은 267줄이다. 비어 있지 않은 줄은 227줄이다. 각 인용 위치를 `nl -ba`로 확인했다. 조건·연산자·상수·분기와 A–H 결론을 대조했다. PDF는 `_staging/recovery/read/ADCIRC/`의 해당 PDF 쪽별 판독 기록을 원문 전사 근거로 사용했다. 이 기록의 해석 문장을 코드 원문과 혼동하지 않았다.

이 문서에서 `src/`, `wind/`, `work/`, `docs/`, `thirdparty/`의 기준은 `models/ADCIRC/raw/source_code/adcirc/`이다. `asgs/`의 기준은 `models/ADCIRC/raw/source_code/asgs/`이다. `gahm/`의 기준은 `models/ADCIRC/raw/source_code/gahm/`이다. 노트의 줄 번호는 이번 검증 전후에 같다. 보고서의 행 ID는 §5 표의 식별자이다. 보고서의 현재 물리적 줄 번호와 구분한다.

판의 기준은 `models/ADCIRC/raw/source_code/adcirc/CMakeLists.txt:92`의 버전 문자열이다. 이를 배포 태그 v56.2.1과 파일 내용이 모두 같다는 증거로 쓰지 않았다. `_staging/recovery/compare/external-results-ad.md:14`도 이 제한을 기록한다. 내부 조석의 외부 식 판정은 같은 파일의 T09 행을 대조했다. 새 외부 조회나 모델 실행은 하지 않았다.

## 노트별 대조 줄 수

| 노트 | 대상 +줄 | 비빈 줄 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|
| [models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md) | 108 | 106 | 13 | 11 | 84 |
| [models/ADCIRC/manual-notes/19-ice-coverage.md](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md) | 32 | 26 | 9 | 8 | 15 |
| [models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md) | 33 | 25 | 3 | 5 | 25 |
| [models/ADCIRC/source-analysis/adcirc-swan-coupling.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md) | 16 | 14 | 1 | 5 | 10 |
| [models/ADCIRC/source-analysis/adcirc-tidal-forcing.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md) | 19 | 13 | 1 | 9 | 9 |
| [models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md) | 39 | 29 | 1 | 10 | 28 |
| [models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md) | 6 | 4 | 1 | 2 | 3 |
| [models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md) | 10 | 8 | 0 | 6 | 4 |
| [models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md) | 4 | 2 | 0 | 1 | 3 |
| 합계 | 267 | 227 | 29 | 57 | 181 |

정정과 보완은 원래 추가 줄을 단위로 센다. 정정은 사실·근거 인용·분류의 오류를 고친 줄이다. 보완은 조건·반대 근거·정본 링크·보고서 식별자를 더한 줄이다. 한 줄에서 여러 내용을 고쳐도 한 번만 센다. 이상 없음에는 구조만 있는 빈 줄 40줄이 포함된다. 분류 변경 83은 별도 집계이다. 이 값은 중복을 제거한 보고서 행 ID 수이다.

## 정정·보완 목록

| 노트:줄 | 구분 | 이전 요지 | 새 요지 | 근거 |
|---|---|---|---|---|
| [04-theory-pdf-v44xx.md:50](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:50) | 보완 | 반복 결론의 정본 링크가 없음 | 검증된 식의 정본 앵커를 추가 | src/gwce.F:1253–1262 |
| [04-theory-pdf-v44xx.md:52](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:52) | 보완 | 반복 결론의 정본 링크가 없음 | 검증된 식의 정본 앵커를 추가하고 깨진 인용 표기를 정리 | src/momentum.F:513–569; docs/user_guide/model_configuration/physics_parameters/horizontal_eddy_viscosity.rst:33–37 |
| [04-theory-pdf-v44xx.md:56](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:56) | 보완 | 반복 결론의 정본 링크가 없음 | 검증된 식의 정본 앵커를 추가하고 보고서 행 ID를 명시 | src/momentum.F:1746–1762 |
| [04-theory-pdf-v44xx.md:62](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:62) | 보완 | 반복 결론의 정본 링크가 없음 | 검증된 식의 정본 앵커를 추가 | src/adcirc.F:297–307 |
| [04-theory-pdf-v44xx.md:64](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:64) | 보완 | 반복 결론의 정본 링크가 없음 | 검증된 식의 정본 앵커를 추가 | src/vsmy.F:784–800 |
| [04-theory-pdf-v44xx.md:65](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:65) | 보완 | σ 미분의 환산 누락 E | EV 저장과 수심 하한 경로에도 환산이 없음을 추가 | src/vsmy.F:1134,1173–1196 |
| [04-theory-pdf-v44xx.md:68](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:68) | 보완 | 추가 H의 E 후보 | 연직 보간과 EVMIN 하한이 H를 제거하지 않음을 추가 | src/vsmy.F:1986–2022,2057–2058 |
| [04-theory-pdf-v44xx.md:83](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:83) | 정정 | 생략 전 3D 구면식 미구현 D | 유도 단계이므로 H | PDF p.53–55; src/vsmy.F:993,1385 |
| [04-theory-pdf-v44xx.md:85](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:85) | 보완 | src/prep/wind/util 검색에 한정 | raw 전체 검색 후 수위 경계에 한정한 D 유지 | src/gwce.F:1763–1764; src/momentum.F:1149–1169; PDF p.65 |
| [04-theory-pdf-v44xx.md:91](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:91) | 정정 | 범용 factorial 적분기가 없으므로 D | 수학적 항등식이므로 H | PDF p.68; src/gwce.F:538–539; src/vsmy.F:1656 |
| [04-theory-pdf-v44xx.md:94](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:94) | 보완 | 주 소스 디렉터리의 D 검색 | 전체 raw의 보조 프로그램까지 확인한 D | src/read_input.F:3165–3168; src/nodalattr.F:2424–2435; 전체 raw 검색 |
| [04-theory-pdf-v44xx.md:102](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:102) | 정정 | 외부 모드 시험 자동 계산 부재 D | 시험 지표 H; ASGS Courant 계산 존재 명시 | PDF p.57,66; asgs/output/checkAdcircMesh.f90:942–966 |
| [04-theory-pdf-v44xx.md:104](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:104) | 정정 | DSS 시험 축약계와 항등식 부재 D | 검증 설정·유도식이므로 H | PDF p.100,102,104; src/cstart.F:706–707; src/vsmy.F:1125 |
| [04-theory-pdf-v44xx.md:105](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:105) | 정정 | DSS 검증 묶음 실행 부재 D | 해석해·시험 구성 H | PDF p.104,106,110–111,117; src/vsmy.F:1125 |
| [04-theory-pdf-v44xx.md:106](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:106) | 보완 | 일부 디렉터리만 검색한 GM 폐합 D | 전체 raw의 SWAN 경로를 구분하고 ADCIRC DSS 폐합의 D 유지 | PDF p.134–135; src/couple2swan.F:484–487; src/nodalattr.F:2555–2559 |
| [04-theory-pdf-v44xx.md:108](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:108) | 정정 | 지역별 조석 오차 기능 부재 D | 보고서 적용 사례의 평가식 H | 1993 PDF p.23–24,30–31; Hench PDF p.23 |
| [04-theory-pdf-v44xx.md:109](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:109) | 정정 | 지역 지각 자동 변환 부재 D | ACES 입력·관측 전처리이므로 H | 1993 PDF p.116; Hench PDF p.71–72; asgs/tides/tide_fac.f:139–146 |
| [04-theory-pdf-v44xx.md:110](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:110) | 정정 | PBL 자체 해법이 없으므로 D | p15 추가; 식12·13 조건부 F, 식11·14 폐합 대응 G | Blain PDF p.21–22; wind/p15.F:1482–1549,1683–1743,2013–2033; work/makefile:249–250,453 |
| [04-theory-pdf-v44xx.md:115](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:115) | 정정 | Courant·파장 자동 선택 부재 D | 실무 권고 H; ASGS 시간간격 계산 추가 | Report2 PDF p.32; asgs/output/checkAdcircMesh.f90:942–966 |
| [04-theory-pdf-v44xx.md:117](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:117) | 정정 | 시간 가중치 분석·안정성 조건 D | 분석 조건 H; raw 전체 검색 범위 명시 | docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:46–137; src/read_input.F:2500,2521,3010 |
| [04-theory-pdf-v44xx.md:143](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:143) | 정정 | FullTIP은 지정 차수만 사용 | DEFAULT 직접 계산 분기를 포함한 C 유지 | src/tidalpotential.F90:262–319,347 |
| [04-theory-pdf-v44xx.md:146](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:146) | 보완 | 동일 z 보간 문단 중복; 2절 지시어 | 동일 노트 정본 링크 | src/vsmy.F:784–800 |
| [04-theory-pdf-v44xx.md:153](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:153) | 정정 | 분산 공분산 근거를 PDF p.3으로 인용 | PDF p.15의 공분산 정의로 교체; C 유지 | _staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:27; src/vsmy.F:2266–2271 |
| [04-theory-pdf-v44xx.md:155](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:155) | 정정 | 계수2가 G라는 오래된 요약과 중복 근거 | 현재 C 판정 및 식별 가능한 정본 링크 | theory 노트:50,52,56,64; theory 보고서 §5 C12 |
| [19-ice-coverage.md:29](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:29) | 보완 | dry forcing 근거 문단의 반복 | 정본 앵커 추가 | src/couple2swan.F:1033–1047 |
| [19-ice-coverage.md:31](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:31) | 정정 | IICE=3이면 얼음 농도를 SWAN으로 전달 | 결합 버퍼 복사와 SWAN 감쇠 입력을 구분 | src/couple2swan.F:1055–1059,1211–1224; thirdparty/swan/swancom1.ftn:7236–7240 |
| [19-ice-coverage.md:38](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:38) | 정정 | A 판정에 SWAN 실제 농도 전달을 포함 | A 유지; 확인된 dry forcing·버퍼 복사로 한정 | ice PDF p.2; src/couple2swan.F:1033–1059 |
| [19-ice-coverage.md:39](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:39) | 정정 | 풍응력 이외 SWAN 농도 전달을 단정 | B 유지; 버퍼·dry forcing의 정본 링크 | src/couple2swan.F:1033–1059,1211–1224 |
| [19-ice-coverage.md:40](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:40) | 보완 | E 근거의 보고서 4절 지시어가 불명확 | 보고서 이름과 정본 앵커 명시 | src/couple2swan.F:1153,1211–1224; swancom1.ftn:7236–7240,7306–7313; swancom2.ftn:1542,1565–1573 |
| [19-ice-coverage.md:66](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:66) | 보완 | 후속 입력 규칙 근거의 중복 | 정본 앵커 추가 | src/owi_ice.F:119–121,249–273,427–471; src/wind.F:741–788 |
| [19-ice-coverage.md:68](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:68) | 정정 | 1000+ 문구를 구판 입력 규칙 A로 분류 | 같은 페이지 내부 모순 B; 중복 제거 | _staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:18; src/read_input.F:1775–1776,2316 |
| [19-ice-coverage.md:70](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:70) | 보완 | 음수 blank 규칙 근거 중복 | 동일 노트 정본 링크 | src/owi_ice.F:118–121 |
| [19-ice-coverage.md:120](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:120) | 정정 | 루틴명 WindInit; 선행 보정 경로 확인 없음 | 실제 initWindModule 이름; 선행 검사도 문자열 충돌을 해소하지 않음 | src/wind.F:364–424,738–778 |
| [19-ice-coverage.md:121](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:121) | 보완 | NWS 문서 내부 모순 근거 중복 | B 정본 앵커 및 판독 기록 줄 번호 | _staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:13,18; src/read_input.F:1775–1776 |
| [19-ice-coverage.md:122](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:122) | 보완 | 기본 항력의 빌드 조건 문단 반복 | 정본 앵커 추가 | src/wind.F:131–141,767 |
| [19-ice-coverage.md:124](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:124) | 보완 | 4개 주 소스 파일만 검색한 D | 전체 raw 검색; 별도 유동 얼음 항에 한정한 D 유지 | src/wind.F:984–986; src/momentum.F:726–727; src/gwce.F:2007; 전체 raw 검색 |
| [19-ice-coverage.md:126](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:126) | 정정 | 음수 입력은 비얼음 항력 그대로 반환 | WindDrag 대입 후 공통 상한 적용; C 유지 | src/wind.F:758–778,788 |
| [19-ice-coverage.md:127](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:127) | 정정 | 1% 미만이면 비얼음 항력 그대로 반환 | WindDrag 대입 후 공통 상한 적용; C 유지 | src/wind.F:741–746,788 |
| [19-ice-coverage.md:129](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:129) | 보완 | 기본 항력 빌드 조건 반복 | 정본 링크 | src/wind.F:131–141,767 |
| [19-ice-coverage.md:196](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:196) | 정정 | SWAN 전달·dry forcing 근거 반복 | 확인된 동작별 정본 링크 | src/couple2swan.F:1033–1059,1211–1224 |
| [19-ice-coverage.md:210](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:210) | 정정 | SWAN 전달 단정·내부 감쇠 미확인 문구 | 확인된 감쇠 소비 경로와 결함 후보 정본 링크 | src/couple2swan.F:1033–1059,1211–1224; swancom1.ftn:7236–7240 |
| [adcirc-met-forcing-implementation.md:67](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:67) | 보완 | NWS8 모델 선택 문단의 중복 | 정본 앵커 추가 | src/nws08.F90:529–533 |
| [adcirc-met-forcing-implementation.md:119](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:119) | 정정 | NWS=-14는 GRIB2 또는 netCDF+OWI | GRIB2+OWI만 해당; netCDF 거부를 명시 | src/read_input.F:2674–2676; src/wind.F:2973–2974,8231–8240 |
| [adcirc-met-forcing-implementation.md:122](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:122) | 정정 | OWI 오류 처리의 다른 errorVar 분기를 인용 | 빈 errorVar의 종료 줄로 교체; allMessage 종료 여부 확인 | src/owiwind.F:508–519,940–943,1134–1151; src/logging.F90:412–419 |
| [adcirc-met-forcing-implementation.md:140](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:140) | 정정 | 노트 안에서 찾을 수 없는 542행 지시어 | 보고서 행 ID와 정본 링크 | src/read_input.F:273–274,529–534,1794–1802 |
| [adcirc-met-forcing-implementation.md:141](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:141) | 보완 | 한 파일에서만 메타데이터 D 검색 | 전체 raw 검색 후 OWI reader의 실제 읽기 범위로 한정 | src/owiwind_netcdf.F:47,83,120,157,265; 전체 raw 검색 |
| [adcirc-met-forcing-implementation.md:222](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:222) | 보완 | sentinel 조건 근거가 여러 노트에 반복 | 원시 NWS=13 검사 조건의 정본 앵커 | src/read_input.F:1794–1802 |
| [adcirc-met-forcing-implementation.md:235](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:235) | 보완 | NWS14 파일 선택 근거가 여러 노트에 반복 | 빌드·파일 선택 정본 앵커 | src/wind.F:1996–1998,8021–8038 |
| [adcirc-met-forcing-implementation.md:236](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:236) | 보완 | NWS=-14 근거가 같은 노트 앞부분과 반복 | 정정한 정본 링크 | src/wind.F:2973–2974,8231–8240 |
| [adcirc-swan-coupling.md:64](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md:64) | 보완 | 요소 누적·성분 제한 근거의 반복 | 정본 앵커 추가 | src/couple2swan.F:389–442 |
| [adcirc-swan-coupling.md:71](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md:71) | 보완 | 운동량 적용 제한 근거의 반복 | 정본 앵커 추가 | src/timestep.F:699–753 |
| [adcirc-swan-coupling.md:81](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md:81) | 정정 | SWAN IVTYPE의 기본 ADCIRC 출력 부재 D | SWAN 구현 확인; 소스 변경 지침 H | docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:113–154; thirdparty/swan/swanout1.ftn:3534,3764,3839,3933,4142,4280,4341 |
| [adcirc-swan-coupling.md:84](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md:84) | 보완 | 면적 평균·성분 제한 반복 | 정본 링크 | src/couple2swan.F:399–427 |
| [adcirc-swan-coupling.md:85](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md:85) | 보완 | Marcel 경계 처리 반복 | 정본 링크 | src/couple2swan.F:432–442 |
| [adcirc-swan-coupling.md:86](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md:86) | 보완 | 제한 계산 근거 반복 | 정본 링크와 출력 저장 근거만 유지 | src/timestep.F:742–754 |
| [adcirc-tidal-forcing.md:51](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:51) | 보완 | 장주기 함수 근거 반복·추후 작성 지시 | 실제 식과 B 판정의 정본 링크; 노트 누락 C 유지 | src/adcirc.F:297–307; theory PDF-TIDAL-L0 |
| [adcirc-tidal-forcing.md:67](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:67) | 보완 | DEFAULT 분기의 자기 주석만 인용 | 실제 거리·천정각 계산과 C0 보정 인용; 정본 앵커 | src/tidalpotential.F90:262–319 |
| [adcirc-tidal-forcing.md:68](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:68) | 보완 | DEFAULT의 주석 근거 반복 | 실제 계산을 인용한 정본 링크 | src/tidalpotential.F90:262–319 |
| [adcirc-tidal-forcing.md:73](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:73) | 정정 | 모든 선택값은 유한 차수 전개 | DEFAULT 직접 계산 포함; 비선형 해양 응답 보장 B 유지 | src/tidalpotential.F90:262–319,347 |
| [adcirc-tidal-forcing.md:82](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:82) | 보완 | UNTIDE 평균 근거 반복; 시간 단위 변환 생략 | 정본 앵커와 표본 시간 조건·단위 변환 추가 | src/internaltide.F90:67–111; src/read_input.F:2522–2529 |
| [adcirc-tidal-forcing.md:83](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:83) | 보완 | Munk 필터 근거 반복 | 정본 앵커 추가 | src/internaltide.F90:119,149–150 |
| [adcirc-tidal-forcing.md:85](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:85) | 보완 | 내부 조석 마찰 텐서 조건의 반복 | 정본 앵커 추가 | src/nodalattr.F:2619,2656–2750 |
| [adcirc-tidal-forcing.md:89](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:89) | 보완 | 마찰 텐서 식 중복 | 전체 조건을 유지한 정본 링크 | src/nodalattr.F:2693–2750 |
| [adcirc-tidal-forcing.md:90](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:90) | 보완 | 필터 상수·합산식 반복 | 두 정본 링크와 실제 호출 유지 | src/nodalattr.F:2659; src/internaltide.F90:67–111,149–150 |
| [adcirc-tidal-forcing.md:106](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:106) | 보완 | 큰 조건 문단이 표에서 반복 | 정본 링크 | src/nodalattr.F:2619,2656–2750 |
| [adcirc_gahm_vortex_model.md:137](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:137) | 보완 | 노트에 대응하지 않는 5절 지시어 | 보고서 이름과 행 ID 명시 | wind/vortex.F:388–413; features §5 H30·C37 |
| [adcirc_gahm_vortex_model.md:139](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:139) | 보완 | 노트에 대응하지 않는 4절 지시어 | 보고서 이름과 행 ID 명시 | gahm/README.md:7–9; GahmSolver.cpp:59–79; features §4 C36 |
| [adcirc_gahm_vortex_model.md:171](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:171) | 정정 | 외부 ATCF 자료의 통상 간격 D | 외부 자료 제공 관행 H | docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:360–366; gahm/tests/test_files/bal122005.dat:1–8 |
| [adcirc_gahm_vortex_model.md:216](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:216) | 보완 | 최대풍속 반경 안쪽 유입각의 반복 | 정본 앵커 추가 | wind/vortex.F:1147–1154 |
| [adcirc_gahm_vortex_model.md:258](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:258) | 보완 | 방위 보간 끝점 처리의 반복 | 정본 앵커 추가 | wind/vortex.F:966–976 |
| [adcirc_gahm_vortex_model.md:289](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:289) | 보완 | 유입각 식·조건의 중복 인용 | 정본 링크와 문서·활성 호출 근거 유지 | docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:423–427; wind/vortex.F:1147–1154; wind/aswip.F:669,706–709 |
| [adcirc_gahm_vortex_model.md:290](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:290) | 보완 | 노트에 대응하지 않는 5절 지시어 | 보고서 이름과 행 ID 명시 | wind/aswip.F:677–709,2960–2963; features §5 H28·H29 |
| [adcirc_gahm_vortex_model.md:291](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:291) | 보완 | 접합점 연속성의 양의 반경 조건 생략 | rmx>0 조건 및 보고서 ID 명시; F 유지 | wind/vortex.F:1148–1152,883; src/wind.F:6053–6055 |
| [adcirc_gahm_vortex_model.md:294](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:294) | 보완 | 방위 보간 근거 중복 | 정본 링크 | wind/vortex.F:966–976 |
| [adcirc_gahm_vortex_model.md:322](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:322) | 보완 | Rossby 식의 무조건적 대수 동치 | 나눗셈의 비영 조건을 명시; F 유지 | wind/vortex.F:391–392; docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:167 |
| [adcirc_gahm_vortex_model.md:324](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:324) | 보완 | GAHM 기압 제한·단위 변환 반복 | 정본 앵커 추가 | src/wind.F:6207–6216 |
| [adcirc-storm-surge-foundation.md:98](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:98) | 보완 | sentinel 검사 근거의 중복 | 기상 노트 정본 링크 | src/read_input.F:1794–1802 |
| [adcirc-storm-surge-foundation.md:172](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:172) | 정정 | 가리키는 곳이 없는 761행 | 보고서 행 ID L761 링크 및 NWS13 정본 앵커 | src/owiwind_netcdf.F:262; fort15 §5 L761 |
| [adcirc-storm-surge-foundation.md:173](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:173) | 보완 | 날짜 필수 검사 E에 빌드 조건 생략·중복 | ADCNETCDF 조건·후속 경로 검증과 정본 앵커 | src/read_input.F:530,1775–1830; src/owiwind_netcdf.F:326–328 |
| [adcirc-storm-surge-nws-families.md:58](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:58) | 보완 | sentinel 검사 반복 | 기상 노트 정본 링크 | src/read_input.F:1794–1802 |
| [adcirc-storm-surge-nws-families.md:78](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:78) | 보완 | NWS8 모델 선택 문단의 중복 | 정본 링크 | src/nws08.F90:529–533 |
| [adcirc-storm-surge-nws-families.md:95](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:95) | 보완 | GAHM 기압 제한·단위 변환 반복 | 정본 링크 | src/wind.F:6207–6216 |
| [adcirc-storm-surge-nws-families.md:102](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:102) | 보완 | NWS14 초기화·파일 선택 문단 반복 | 기상 노트 정본 링크 | src/wind.F:1996–1998,8021–8038,8231–8240 |
| [adcirc-storm-surge-nws-families.md:116](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:116) | 보완 | NWS13 입력 종류 문단 반복 | foundation 정본 링크 | src/owiwind_netcdf.F:262; docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:10,18 |
| [adcirc-storm-surge-nws-families.md:117](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:117) | 보완 | NWS13 날짜 검사 E 문단 반복 | foundation 정본 링크 | src/read_input.F:1775–1830; src/owiwind_netcdf.F:326–328 |
| [adcirc-tide-forcing-implementation.md:110](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:110) | 보완 | fort.24.nc 우선 입력의 NTIP 조건 생략 | NTIP=2와 ADCNETCDF 조건 명시; C 유지 | src/read_input.F:6367–6382 |

## 분류를 바꾼 행

허용된 `ADCIRC-theory-vs-code.md` §5의 77개 행 ID를 동기화했다. 표의 원래 대상은 324개 행 ID로 유지했다. PBL 식을 두 결론으로 나누어 묶음 표 행 수는 114개에서 115개로 바뀌었다. 현재 집계는 A 125, B 76, C 28, D 10, E 5, F 5, G 2, H 73, X 0이다.

`ADCIRC-features-vs-code.md`의 6개 행 ID도 노트의 결론은 정정했다. 해당 보고서는 사용자 쓰기 허용 목록에 없으므로 수정하지 않았다. 아래 표에 그 미반영 상태를 명시한다. 다른 보고서에 대한 사실 보완도 해당 노트에만 반영했다.

| 보고서 §5 | 행 ID | 이전→새 | 노트 근거 | 보고서 반영 |
|---|---|---|---|---|
| ADCIRC-theory-vs-code.md | 239, 240, 241, 244, 245 | D→H | [04-theory-pdf-v44xx.md:83](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:83) | 반영 |
| ADCIRC-theory-vs-code.md | 299 | D→H | [04-theory-pdf-v44xx.md:91](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:91) | 반영 |
| ADCIRC-theory-vs-code.md | 500, 501, 502, 503, 504, 505 | D→H | [04-theory-pdf-v44xx.md:102](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:102) | 반영 |
| ADCIRC-theory-vs-code.md | 521, 522, 528, 535 | D→H | [04-theory-pdf-v44xx.md:104](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:104) | 반영 |
| ADCIRC-theory-vs-code.md | 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574 | D→H | [04-theory-pdf-v44xx.md:105](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:105) | 반영 |
| ADCIRC-theory-vs-code.md | 646, 647, 653, 654, 765, 766 | D→H | [04-theory-pdf-v44xx.md:108](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:108) | 반영 |
| ADCIRC-theory-vs-code.md | 661, 773, 774 | D→H | [04-theory-pdf-v44xx.md:109](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:109) | 반영 |
| ADCIRC-theory-vs-code.md | 691, 694 | D→G | [04-theory-pdf-v44xx.md:110](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:110) | 반영 |
| ADCIRC-theory-vs-code.md | 692, 693 | D→F | [04-theory-pdf-v44xx.md:110](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:110) | 반영 |
| ADCIRC-theory-vs-code.md | 728, 729 | D→H | [04-theory-pdf-v44xx.md:115](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:115) | 반영 |
| ADCIRC-theory-vs-code.md | 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815 | D→H | [04-theory-pdf-v44xx.md:117](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:117) | 반영 |
| ADCIRC-features-vs-code.md | I15, C19 | A→B | [19-ice-coverage.md:68](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:68) | 쓰기 허용 밖이므로 미반영 |
| ADCIRC-features-vs-code.md | R18, R19, R20 | D→H | [adcirc-swan-coupling.md:81](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md:81) | 쓰기 허용 밖이므로 미반영 |
| ADCIRC-features-vs-code.md | H18 | D→H | [adcirc_gahm_vortex_model.md:171](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:171) | 쓰기 허용 밖이므로 미반영 |

PBL의 식 (12)·(13)은 ST12가 0 이하인 일정 배경풍 경로의 압력 기울기 표현에 한정하여 F이다. 식 (11)·(14)는 문서의 스칼라 항력과 p15의 두 DRAG 성분 사이의 폐합 대응을 확정하지 못해 G이다. BLOWUQ와 COMQUT의 계산 경로는 확인했다. 자체 PBL 해법이 없다는 D 결론은 철회했다.

## 원래 D였던 줄의 전체 raw 재검색

각 줄의 검색은 `rg -n -i --no-ignore --hidden --glob '!**/.git/**' '<검색식>' models/ADCIRC/raw`로 수행했다. 숨김 파일과 보조 프로그램을 포함했다. Git 관리 데이터는 제외했다. 이진 파일은 rg의 기본 처리에 따랐다. 검색 결과 중 주장에 대응하는 소스 위치를 `nl -ba`로 열었다. 키워드 일치 자체를 구현 동치의 증거로 쓰지 않았다.

| 노트:줄 | 검색식 | 결과와 판정 |
|---|---|---|
| [04-theory-pdf-v44xx.md:83](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:83) | `TANPHI\|\b2w\b\|\bSFac\b\|\bCorif\b` | Corif·SFac 경로가 검색된다. 원문 p.55가 생략한다고 명시한 유도 항이므로 H로 정정했다. |
| [04-theory-pdf-v44xx.md:85](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:85) | `NFLUXGBC\|normal.{0,20}gradient\|LBCODEI` | 보조 프로그램의 경계 정보와 momentum.F:1149–1169의 속도 기울기가 검색된다. 수위 법선 기울기 식 (6.18)–(6.20)의 조립은 찾지 못했다. D를 유지했다. |
| [04-theory-pdf-v44xx.md:91](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:91) | `factorial\|Gauss.Legendre\|AreaIE` | gwce.F:538–539의 저차 적분 계수와 vsmy.F:1656의 Gauss–Legendre 구적이 검색된다. 원문은 적분 항등식이므로 H로 정정했다. |
| [04-theory-pdf-v44xx.md:94](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:94) | `Darcy\|Weisbach\|f_DW\|Chezy\|ManningsN` | Manning·Chezy 경로가 검색된다. 문서 외 텍스트의 Darcy·Weisbach·f_DW 검색에는 대응 소스가 없었다. 직접 입력·8로 나누는 변환의 D를 유지했다. |
| [04-theory-pdf-v44xx.md:102](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:102) | `Courant\|Fourier\|CONVCR\|analytical\|E_[1-4]` | asgs/output/checkAdcircMesh.f90:942–966의 Courant 기준 계산을 확인했다. gwce.F의 CONVCR는 반복 수렴 기준이다. 보고서 검증 지표는 H로 정정했다. |
| [04-theory-pdf-v44xx.md:104](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:104) | `DSSSTUP\|DSS\|Legendre\|analytic` | cstart.F:706–707의 DSSSTUP 호출은 주석이다. 현재 VSSOL의 TRIDIAG와 시험 전용 항등식을 구분했다. H로 정정했다. |
| [04-theory-pdf-v44xx.md:105](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:105) | `\bKelvin\b\|\bLegendre\b\|\b(ber\|bei\|ker\|kei)\(\|periodic.test\|analytical` | vsmy.F의 구적·TRIDIAG는 검색된다. PDF의 정상·주기 해석해 구성은 검증 기준이므로 H로 정정했다. |
| [04-theory-pdf-v44xx.md:106](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:106) | `Grant.Madsen\|Madsen\|UstarCW\|U_star_cw\|f_w\|wave.current` | SWAN의 Madsen 파 마찰과 couple2swan.F:487의 Manning2Madsen을 확인했다. ADCIRC DSS의 식 (200)–(205) 연립 폐합과 구분하여 D를 유지했다. |
| [04-theory-pdf-v44xx.md:108](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:108) | `observed\|phase.error\|amplitude.error\|\bRMS\b\|WNAT\|ENPACT` | 조화 분석, 관측 자료 처리, wind/lsq.F의 최소제곱 모듈이 검색된다. 보고서의 지역별 검증 지표는 H로 정정했다. |
| [04-theory-pdf-v44xx.md:109](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:109) | `Greenwich\|epoch\|time.zone\|cotidal\|\bEFA\b` | asgs/tides/tide_fac.f:139–146의 천문 인수 계산을 확인했다. A2는 ACES 입력 변환이다. A3는 관측 비교 전처리이다. H로 정정했다. |
| [04-theory-pdf-v44xx.md:110](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:110) | `HURWIN\|PBL\|BLOWUQ\|COMQUT\|geostrophic` | wind/p15.F의 BLOWUQ·COMQUT와 work/makefile의 p15 빌드를 확인했다. 식 (12)·(13)은 조건부 F이다. 식 (11)·(14)는 G이다. |
| [04-theory-pdf-v44xx.md:115](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:115) | `Courant\|sqrt\(gh\)\|DTDP\|wavelength` | asgs/output/checkAdcircMesh.f90:942–966에 시간간격 계산이 있다. Report 2의 정확도 권고는 H로 정정했다. |
| [04-theory-pdf-v44xx.md:117](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:117) | `A00\|B00\|C00\|Courant\|theta\|TAU0` | A00·B00·C00 직접 입력과 보조 프로그램의 Courant 계산을 확인했다. 분석적 안정성 조건은 H로 정정했다. |
| [19-ice-coverage.md:124](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/19-ice-coverage.md:124) | `CICE\|NCICE\|ice.?friction\|ice.?mass\|WindIceDrag` | owi_ice·wind·couple2swan과 SWAN 얼음 감쇠가 검색된다. ADCIRC 유동의 별도 얼음 마찰·질량 항은 찾지 못했다. 해당 범위의 D를 유지했다. |
| [adcirc-met-forcing-implementation.md:141](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:141) | `conventions\|group_order\|NF90_GET_ATT\|:rank` | 다른 netCDF 속성 처리도 검색된다. OWI reader는 group_order를 읽는다. conventions·rank는 그 reader의 예시 주석에만 있다. D를 유지했다. |
| [adcirc-swan-coupling.md:81](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-swan-coupling.md:81) | `IVTYPE\|SWAN_OutputAgg\|swell.wave.height\|peak.wave.direction` | SWAN swanout1.ftn에 IVTYPE 12·14·15·16·17·18·44 계산이 있다. 문서는 ADCIRC 선택값을 바꾸는 소스 수정 지침이므로 H로 정정했다. |
| [adcirc_gahm_vortex_model.md:171](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:171) | `6.hour\|ATCF\|BEST` | aswip과 ATCF 시험 자료가 검색된다. 같은 시각의 여러 isotach도 확인했다. usually라는 외부 제공 관행은 H로 정정했다. |

## E 후보의 반대 근거 확인

| 후보 | 확인한 반대 경로 | 판단 |
|---|---|---|
| TAU-FRACTION; theory:59 | nodalattr.F:1830은 정수 부분을 얻는다. 1924는 여전히 원래 Tau0를 수심 함수에 넘긴다. LoadTau0 분기는 별도 경로이다. 2149–2159에는 -2.1을 -2로 바꾸는 변환이 없다. | 초기화의 `.not.LoadTau0` 조건에서 E 유지. 수심 100의 대입 비교는 모델 실행값이 아니다. |
| 바닥 응력 진단; theory:65 | vsmy.F:1134의 EV 저장에는 높이 변환이 없다. 1173–1175의 수심 하한은 진단 식에 환산 계수를 곱하지 않는다. 1196의 비영 ISlip 경로는 TK·q를 쓴다. | ISlip=0 진단에 한정하여 E 유지. |
| IEVC=42; theory:68 | vsmy.F:2008–2015의 연직 보간은 H를 나누지 않는다. 2057–2058의 EVMIN은 하한만 적용한다. 40·41·43과 같은 속도 제곱 계열을 비교했다. | 추가 H의 E 유지. Davies 상수 자체의 단위는 확장 판정하지 않았다. |
| ADCIRC 얼음과 SWAN 감쇠; ice:40 | couple2swan.F:1211–1224는 결합 버퍼와 지역 SWAN_PIC를 만든다. swancom1.ftn:7236–7240의 AICE2·PICE 입력과 swancom2.ftn:1542–1573의 감쇠 소비를 대조했다. IICE=2 dry forcing은 별도 경로이다. | IICE=3의 입력 연결 E 유지. SWAN 자체 얼음 감쇠의 부재를 주장하지 않는다. |
| 명시적 얼음 항력 이름; ice:120 | wind.F:364–365의 선행 검사·매핑과 408–424를 확인했다. 원래 DragLawString을 허용 문자열로 바꾸는 대입이 없다. 367의 NWS=0에서는 초기화가 반환된다. | NWS가 0이 아닌 조건에서 initWindModule과 WindIceDrag의 충돌 E 유지. |
| OWI P/W 불일치; met:122 | logging.F90:412–419의 allMessage는 출력만 한다. owiwind.F:518의 빈 errorVar 경로는 iret가 비영이어야 종료한다. 943의 다른 불일치 검사는 상수 1을 넘긴다. | 성공한 READ의 0을 넘기는 종료 누락 E 유지. 종료 인용을 1150–1151로 고쳤다. |
| NWS13 필수 날짜; foundation:173 및 nws:117 | read_input.F:530의 sentinel과 1794–1802의 ADCNETCDF 검사를 확인했다. NRS 분리 1829–1830과 owiwind_netcdf.F:326–328의 공통 읽기는 누락 검사를 보완하지 않는다. | -13·파랑 결합 값의 검사 누락 E 유지. 중복 문단은 foundation 정본으로 연결했다. |

추가 단위 점검: `internaltide.F90:90–91`은 시간 단계 번호에 DTDP를 곱한 뒤 초 단위 Fs로 나눈다. `read_input.F:2522–2529`는 음수 DTDP 입력을 양수 시간간격으로 바꾼다. 이 두 경로에는 wetdry 표본과 같은 단계 번호·초의 직접 비교가 없다. 이 점검에서 새 E 후보를 추가하지 않았다.

## sonnet 수정 목록 반영 여부

| 번호 | 상태 | 이 묶음에서의 처리 |
|---:|---|---|
| 1 | 반영 | theory:110과 theory 보고서 §5 행 ID 691–694를 정정했다. p15의 실제 계산과 빌드 경로를 추가했다. 식별 대응의 한계는 F·G로 구분했다. |
| 2 | 범위 밖 | EFDC ISVARSETTLE 행이다. ADCIRC 묶음 C의 대상 줄이 아니다. |
| 3 | 범위 밖 | wetdry.F:845의 IT·BTIME_END 비교 결론은 원래 대상 +줄에 없다. 이 묶음에 새 wetdry 문단을 추가하지 않았다. |
| 4 | 반영 | theory:153과 theory 보고서 §5 B27의 판독 기록을 p001-018.md:27, PDF p.15로 고쳤다. |
| 5 | 범위 밖 | EFDC 식 5.13 행이다. |
| 6 | 범위 밖 | netcdfio.F90의 nodal 변수명 결론은 원래 대상 +줄에 없다. |
| 7 | 범위 밖 | XDMF 최종화 결론은 원래 대상 +줄에 없다. theory:107의 XDMF 유틸리티 언급은 사각형 요소 비교이며 해당 결론과 다르다. |
| 8 | 범위 밖 | EFDC TOXS·DYES 행이다. |
| 9 | 범위 밖 | subgridLookup.F의 단위 결론은 원래 대상 +줄에 없다. |
| 10 | 범위 밖 | 동적 수위 보정 램프의 기본값 결론은 원래 대상 +줄에 없다. ice:124의 dynamicWaterLevelCorrectionDelta 인용은 GWCE 갱신 문맥이다. |
| 11 | 범위 밖 | SFINCS 누적 강수 문단이다. 이 묶음 안의 중복은 별도로 정본 링크로 줄였다. |
| 12 | 반영 | theory:146·155, met:140, gahm:137·139·290·291·322, foundation:172 등의 지시어를 보고서 행 ID 또는 정본 링크로 바꿨다. '2.7의 단위·의미 결함 판정'이라는 정확한 문자열은 이 묶음의 대상 줄에 없다. |
| 13 | 범위 밖 | EFDC mhkpwr.f90 행이다. |

## 추가 줄 전수 대조 기록

아래 목록은 작업 시작 때 고정한 267개 줄을 한 번씩 기록한다. 근거 칸은 대표 위치이다. 정정·보완의 상세 근거는 위 목록과 해당 노트의 원문 인용을 따른다. 이상 없음은 이번 정적 대조에서 해당 줄의 조건·값·인용·분류를 고칠 사유를 찾지 못했다는 뜻이다.


### models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 9 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 43 | 이상 없음 | 최종 결론 보고서 연결 | ADCIRC-theory-vs-code.md §5 |
| 48 | 이상 없음 | 비교 표 머리글 | 출처 주장 없음 |
| 49 | 이상 없음 | 표 구분선 | 출처 주장 없음 |
| 50 | 보완 | 검증된 식의 정본 앵커를 추가 | src/gwce.F:1253–1262 |
| 51 | 이상 없음 | 무번호 경계 유량 식 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:21`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:8-12` |
| 52 | 보완 | 검증된 식의 정본 앵커를 추가하고 깨진 인용 표기를 정리 | src/momentum.F:513–569; docs/user_guide/model_configuration/physics_parameters/horizontal_eddy_viscosity.rst:33–37 |
| 53 | 이상 없음 | 식 (2.7) | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2470` |
| 54 | 이상 없음 | 식 (2.10)·(2.11) | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p019-036.md:19`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:1634` |
| 55 | 이상 없음 | 식 (2.13)·(2.16) | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p019-036.md:23`; `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:579` |
| 56 | 보완 | 검증된 식의 정본 앵커를 추가하고 보고서 행 ID를 명시 | src/momentum.F:1746–1762 |
| 57 | 이상 없음 | TAU-1 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:200,204-205`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2158` |
| 58 | 이상 없음 | TAU-2 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:210-214`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2149` |
| 59 | 이상 없음 | TAU-FRACTION | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:35-37`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:1924` |
| 60 | 이상 없음 | TAU-UPDATE | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:262-265`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:264` |
| 61 | 이상 없음 | WIND-Z0-MARINE | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/wind_stress.rst:65,67`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2950` |
| 62 | 보완 | 검증된 식의 정본 앵커를 추가 | src/adcirc.F:297–307 |
| 63 | 이상 없음 | 각 문서 식 (4) | `_staging/recovery/read/ADCIRC/manuals/pdfs/1993_Westerink02.pdf/p001-018.md:28`; `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:1539` |
| 64 | 보완 | 검증된 식의 정본 앵커를 추가 | src/vsmy.F:784–800 |
| 65 | 보완 | EV 저장과 수심 하한 경로에도 환산이 없음을 추가 | src/vsmy.F:1134,1173–1196 |
| 66 | 이상 없음 | 3D-ISLIP-1·3 | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/parameter_definitions/index.rst:1273,1278,1287,1291`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2559` |
| 67 | 이상 없음 | 3D-THETA-ROLES | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/parameter_definitions/index.rst:1449,1451`; `models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:2875` |
| 68 | 보완 | 연직 보간과 EVMIN 하한이 H를 제거하지 않음을 추가 | src/vsmy.F:1986–2022,2057–2058 |
| 69 | 이상 없음 | PDF-SOLVER-LU | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p055-072.md:15`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:427` |
| 70 | 이상 없음 | PDF-FE-RULE2A-REMOVED | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p055-072.md:31`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1344` |
| 71 | 이상 없음 | PDF-WETDRY-OLD | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Westerink01.pdf/p019-036.md:27`; `models/ADCIRC/raw/source_code/adcirc/src/wetdry.F:241` |
| 72 | 이상 없음 | 식 (1.15) | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:18`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1537` |
| 73 | 이상 없음 | 식 (6.15) | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p055-072.md:24`; `models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:1100` |
| 74 | 이상 없음 | 식 (83b) | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p037-054.md:20`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1473` |
| 75 | 이상 없음 | 식 (100)·(103) | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p037-054.md:27`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:770` |
| 76 | 이상 없음 | 식 (3)·(9) | `_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Hench.pdf/p001-018.md:25`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:771` |
| 77 | 이상 없음 | 식 (10) | `_staging/recovery/read/ADCIRC/manuals/pdfs/1993_Westerink02.pdf/p001-018.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1447` |
| 81 | 이상 없음 | 빈 줄 | 구조 확인 |
| 82 | 이상 없음 | v44.XX 요소 평균 수심 첨자; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:22`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1336` |
| 83 | 정정 | 유도 단계이므로 H | PDF p.53–55; src/vsmy.F:993,1385 |
| 84 | 이상 없음 | 구면 연속식의 곡률 부호; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p037-054.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:1385` |
| 85 | 보완 | raw 전체 검색 후 수위 경계에 한정한 D 유지 | src/gwce.F:1763–1764; src/momentum.F:1149–1169; PDF p.65 |
| 86 | 이상 없음 | 절점 응력 평균의 구현과 기호 대응; F 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:26`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:897` |
| 87 | 이상 없음 | 선형 마찰계수의 정의; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:30`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/nolibf.rst:31` |
| 88 | 이상 없음 | 비보존형 부분적분 뒤의 수심 근사; F 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p019-036.md:18`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:590` |
| 89 | 이상 없음 | 보존형 부분적분의 불필요한 미분 기호; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p019-036.md:18`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:1634` |
| 90 | 이상 없음 | 수위 방사 경계 지원; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p055-072.md:27`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1743` |
| 91 | 정정 | 수학적 항등식이므로 H | PDF p.68; src/gwce.F:538–539; src/vsmy.F:1656 |
| 92 | 이상 없음 | 1992년 no-slip 적용 높이; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p019-036.md:15`; `models/ADCIRC/raw/source_code/adcirc/src/global_3dvs.F:194` |
| 93 | 이상 없음 | 1992년 로그 마찰의 높이 원점; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p019-036.md:15`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2555` |
| 94 | 보완 | 전체 raw의 보조 프로그램까지 확인한 D | src/read_input.F:3165–3168; src/nodalattr.F:2424–2435; 전체 raw 검색 |
| 95 | 이상 없음 | Manning 변환의 고정 수심과 총 수심; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p019-036.md:21`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2424` |
| 96 | 이상 없음 | 1992년 회전 마찰 텐서·진단 Cf; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p019-036.md:31`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1452` |
| 97 | 이상 없음 | 1992년 GWCE 점성항의 시간 수준; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p037-054.md:15`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:516` |
| 98 | 이상 없음 | 1992년 경계 τ₀Q 시간 가중; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p037-054.md:16`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1741` |
| 99 | 이상 없음 | 1992년 외부 운동량의 암시적 수평 점성; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p037-054.md:16`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:590` |
| 100 | 이상 없음 | 코리올리 계수와 유량의 요소 평균; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p037-054.md:19`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1447` |
| 101 | 이상 없음 | 1992년 V 이류의 미분 방향; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p037-054.md:26`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:586` |
| 102 | 정정 | 시험 지표 H; ASGS Courant 계산 존재 명시 | PDF p.57,66; asgs/output/checkAdcircMesh.f90:942–966 |
| 103 | 이상 없음 | 1992년 DSS 1·2 내부 모드; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p091-108.md:20`; `models/ADCIRC/raw/source_code/adcirc/prep/read_global.F:938` |
| 104 | 정정 | 검증 설정·유도식이므로 H | PDF p.100,102,104; src/cstart.F:706–707; src/vsmy.F:1125 |
| 105 | 정정 | 해석해·시험 구성 H | PDF p.104,106,110–111,117; src/vsmy.F:1125 |
| 106 | 보완 | 전체 raw의 SWAN 경로를 구분하고 ADCIRC DSS 폐합의 D 유지 | PDF p.134–135; src/couple2swan.F:484–487; src/nodalattr.F:2555–2559 |
| 107 | 이상 없음 | 4절점 사각형 유동 요소; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p037-054.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1007` |
| 108 | 정정 | 보고서 적용 사례의 평가식 H | 1993 PDF p.23–24,30–31; Hench PDF p.23 |
| 109 | 정정 | ACES 입력·관측 전처리이므로 H | 1993 PDF p.116; Hench PDF p.71–72; asgs/tides/tide_fac.f:139–146 |
| 110 | 정정 | p15 추가; 식12·13 조건부 F, 식11·14 폐합 대응 G | Blain PDF p.21–22; wind/p15.F:1482–1549,1683–1743,2013–2033; work/makefile:249–250,453 |
| 111 | 이상 없음 | Blain 지수 기압 법칙; F 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Blain03.pdf/p019-036.md:16`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:6636` |
| 112 | 이상 없음 | Report 2 조석의 경도 위상 누락; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Westerink01.pdf/p001-018.md:29`; `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:1539` |
| 113 | 이상 없음 | Report 2 x 운동량의 V 누락; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Westerink01.pdf/p001-018.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:756` |
| 114 | 이상 없음 | Report 2 GWCE의 횡방향 이류; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Westerink01.pdf/p019-036.md:13`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1473` |
| 115 | 정정 | 실무 권고 H; ASGS 시간간격 계산 추가 | Report2 PDF p.32; asgs/output/checkAdcircMesh.f90:942–966 |
| 116 | 이상 없음 | Report 2 이차 마찰의 지수·수위 기호; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Westerink01.pdf/p019-036.md:27`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2462` |
| 117 | 정정 | 분석 조건 H; raw 전체 검색 범위 명시 | docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:46–137; src/read_input.F:2500,2521,3010 |
| 118 | 이상 없음 | 시간과 역시간을 비교한 τ₀ 조건; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:99`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:101` |
| 119 | 이상 없음 | τ₀ 값표의 최소·최대; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:103`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:104` |
| 120 | 이상 없음 | 시간평균 이전 τ₀ 변수 설명; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:229`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/tau0.rst:252` |
| 121 | 이상 없음 | 시간 가변 τ₀의 텐서 마찰; A 유지 | `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:581`; `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:585` |
| 122 | 이상 없음 | NOLIBF=3 허용; A 유지 | `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:1850`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:1851` |
| 123 | 이상 없음 | KG 점성 미분의 방향; B 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:24`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/physics_parameters/horizontal_eddy_viscosity.rst:90` |
| 124 | 이상 없음 | 3D Manning 거칠기의 κ; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/parameter_definitions/index.rst:1307`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2548` |
| 125 | 이상 없음 | IEVC=20의 실제 연직 보간식; C 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/parameter_definitions/index.rst:1374`; `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/parameter_definitions/index.rst:1376` |
| 126 | 이상 없음 | THETA 입력 줄의 IEVC 조건; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/parameter_definitions/index.rst:1445`; `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort15.rst:138` |
| 127 | 이상 없음 | B01 총 수심 GWCE 강성; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:21`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:505` |
| 128 | 이상 없음 | B02 중력·분산 보정; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:21`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:511` |
| 129 | 이상 없음 | B03 수위 기울기 제한; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p019-036.md:23`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:386` |
| 130 | 이상 없음 | B04 수위 흡수층; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:21`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:523` |
| 131 | 이상 없음 | B05 predictor-corrector; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:21`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2522` |
| 132 | 이상 없음 | B06 절점 τ₀ 선택·평균; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:21`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:1830` |
| 133 | 이상 없음 | B07 Smagorinsky와 제한값; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:29`; `models/ADCIRC/raw/source_code/adcirc/src/momentum.F:373` |
| 134 | 이상 없음 | B08 2D 마찰의 시간간격 상한; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2468` |
| 135 | 이상 없음 | B09 Manning 수로·장벽 보정; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p019-036.md:21`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2397` |
| 136 | 이상 없음 | B10 교각 마찰; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2487` |
| 137 | 이상 없음 | B11 NOLIBF=3 운동량 분산; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2790` |
| 138 | 이상 없음 | B12 비등방 내부파 항력; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p019-036.md:29`; `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:581` |
| 139 | 이상 없음 | B13 Garratt 상한; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Blain03.pdf/p019-036.md:15`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:122` |
| 140 | 이상 없음 | B14 Powell·SWAN 끌림 선택; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Blain03.pdf/p019-036.md:15`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:443` |
| 141 | 이상 없음 | B15 얼음의 바람 끌림 보정; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1994_Blain03.pdf/p019-036.md:15`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:982` |
| 142 | 이상 없음 | B16 방향별 육상 거칠기·수관; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:29`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2958` |
| 143 | 정정 | DEFAULT 직접 계산 분기를 포함한 C 유지 | src/tidalpotential.F90:262–319,347 |
| 144 | 이상 없음 | B18 공간별 SAL; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p019-036.md:19`; `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:1556` |
| 145 | 이상 없음 | B19 3D 마찰의 상한·하한; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2559` |
| 146 | 보완 | 동일 노트 정본 링크 | src/vsmy.F:784–800 |
| 147 | 이상 없음 | B21 biharmonic·Leith 점성; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p019-036.md:30`; `models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:271` |
| 148 | 이상 없음 | B22 속도 Gaussian 필터; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p037-054.md:22`; `models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:1149` |
| 149 | 이상 없음 | B23 MY2.5 수면 생산; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p091-108.md:20`; `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/parameter_definitions/index.rst:1426` |
| 150 | 이상 없음 | B24 난류 점성·스칼라 확산 제한; A 유지 | `models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:3082`; `models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:3083` |
| 151 | 이상 없음 | B25 경압 구적·cubic 보간; C 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p055-072.md:28`; `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:2228` |
| 152 | 이상 없음 | B26 스칼라 ALP4·biharmonic 확산; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:5776`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:5777` |
| 153 | 정정 | PDF p.15의 공분산 정의로 교체; C 유지 | _staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p001-018.md:27; src/vsmy.F:2266–2271 |
| 154 | 이상 없음 | B28 JCG scaling·종료; A 유지 | `_staging/recovery/read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p055-072.md:15`; `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:146` |
| 155 | 정정 | 현재 C 판정 및 식별 가능한 정본 링크 | theory 노트:50,52,56,64; theory 보고서 §5 C12 |
| 156 | 이상 없음 | 빈 줄 | 구조 확인 |

### models/ADCIRC/manual-notes/19-ice-coverage.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 14 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 29 | 보완 | 정본 앵커 추가 | src/couple2swan.F:1033–1047 |
| 31 | 정정 | 결합 버퍼 복사와 SWAN 감쇠 입력을 구분 | src/couple2swan.F:1055–1059,1211–1224; thirdparty/swan/swancom1.ftn:7236–7240 |
| 37 | 이상 없음 | 빈 줄 | 구조 확인 |
| 38 | 정정 | A 유지; 확인된 dry forcing·버퍼 복사로 한정 | ice PDF p.2; src/couple2swan.F:1033–1059 |
| 39 | 정정 | B 유지; 버퍼·dry forcing의 정본 링크 | src/couple2swan.F:1033–1059,1211–1224 |
| 40 | 보완 | 보고서 이름과 정본 앵커 명시 | src/couple2swan.F:1153,1211–1224; swancom1.ftn:7236–7240,7306–7313; swancom2.ftn:1542,1565–1573 |
| 41 | 이상 없음 | 빈 줄 | 구조 확인 |
| 51 | 이상 없음 | 코드는 IF | `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1772`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1773` |
| 65 | 이상 없음 | 빈 줄 | 구조 확인 |
| 66 | 보완 | 정본 앵커 추가 | src/owi_ice.F:119–121,249–273,427–471; src/wind.F:741–788 |
| 67 | 이상 없음 | 얼음 문서의 0% 항력 자릿수; B 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:520`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:762` |
| 68 | 정정 | 같은 페이지 내부 모순 B; 중복 제거 | _staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:18; src/read_input.F:1775–1776,2316 |
| 69 | 이상 없음 | 얼음·기상 형식 조합 검사; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2322`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2323` |
| 70 | 보완 | 동일 노트 정본 링크 | src/owi_ice.F:118–121 |
| 71 | 이상 없음 | 빈 줄 | 구조 확인 |
| 94 | 이상 없음 | IceCube 분기는 IF | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:758`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:760` |
| 117 | 이상 없음 | Lupkes 계열 분기는 IF | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:767`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:773` |
| 118 | 이상 없음 | 빈 줄 | 구조 확인 |
| 119 | 이상 없음 | 빈 줄 | 구조 확인 |
| 120 | 정정 | 실제 initWindModule 이름; 선행 검사도 문자열 충돌을 해소하지 않음 | src/wind.F:364–424,738–778 |
| 121 | 보완 | B 정본 앵커 및 판독 기록 줄 번호 | _staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:13,18; src/read_input.F:1775–1776 |
| 122 | 보완 | 정본 앵커 추가 | src/wind.F:131–141,767 |
| 123 | 이상 없음 | IceCube 최대값 규칙의 적용 범위; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:749`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:764` |
| 124 | 보완 | 전체 raw 검색; 별도 유동 얼음 항에 한정한 D 유지 | src/wind.F:984–986; src/momentum.F:726–727; src/gwce.F:2007; 전체 raw 검색 |
| 125 | 이상 없음 | Lupkes 얼음 항력의 계수; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:733`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:767` |
| 126 | 정정 | WindDrag 대입 후 공통 상한 적용; C 유지 | src/wind.F:758–778,788 |
| 127 | 정정 | WindDrag 대입 후 공통 상한 적용; C 유지 | src/wind.F:741–746,788 |
| 128 | 이상 없음 | ICE CUBE 다항식의 출처; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort25.rst:47` |
| 129 | 보완 | 정본 링크 | src/wind.F:131–141,767 |
| 196 | 정정 | 확인된 동작별 정본 링크 | src/couple2swan.F:1033–1059,1211–1224 |
| 210 | 정정 | 확인된 감쇠 소비 경로와 결함 후보 정본 링크 | src/couple2swan.F:1033–1059,1211–1224; swancom1.ftn:7236–7240 |

### models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 11 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 24 | 이상 없음 | 코드는 허용 검사 뒤의 IF(NWS.EQ.0) THEN에서 NRS를 0으로 설정한다. | `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1825`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1826` |
| 49 | 이상 없음 | 빈 줄 | 구조 확인 |
| 50 | 이상 없음 | NWS의 자리 분리 순서; B 유지 | `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1775`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1776` |
| 51 | 이상 없음 | NWS 부호와 응력·풍속 구별; B 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:2170`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:2172` |
| 52 | 이상 없음 | 얼음과 직접 응력의 아홉 조합; B 유지 | `models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:410`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:1775` |
| 53 | 이상 없음 | v53 파랑 입력 표 머리; B 유지 | `models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:408`; `models/ADCIRC/raw/source_code/adcirc/src/cstart.F:312` |
| 54 | 이상 없음 | 트랙 레코드의 생략된 필드; C 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort22.rst:342`; `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort22.rst:355` |
| 55 | 이상 없음 | 기상 입력 후 제한과 혼합; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:6207`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:6208` |
| 56 | 이상 없음 | NWS=10의 얼음 필드; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:1217`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:1219` |
| 57 | 이상 없음 | NWS=6의 격자 범위 처리와 외삽; C 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort22.rst:291`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:3535` |
| 58 | 이상 없음 | GRIB2 압력 선택의 실제 검색 규칙; C 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort22x_grb2.rst:30`; `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort22x_grb2.rst:31` |
| 59 | 이상 없음 | 빈 줄 | 구조 확인 |
| 67 | 보완 | 정본 앵커 추가 | src/nws08.F90:529–533 |
| 83 | 이상 없음 | NWS=±4 reader는 기압 입력에 100을 곱한 뒤 RHOWATG로 나눈다. | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:3411`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:3412` |
| 118 | 이상 없음 | 빈 줄 | 구조 확인 |
| 119 | 정정 | GRIB2+OWI만 해당; netCDF 거부를 명시 | src/read_input.F:2674–2676; src/wind.F:2973–2974,8231–8240 |
| 120 | 이상 없음 | 종합 NWS 표 밖의 추가 선택; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:52`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:53` |
| 121 | 이상 없음 | OWI의 파일 목록과 셋째 기본 격자; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/owiwind.F:798`; `models/ADCIRC/raw/source_code/adcirc/src/owiwind.F:799` |
| 122 | 정정 | 빈 errorVar의 종료 줄로 교체; allMessage 종료 여부 확인 | src/owiwind.F:508–519,940–943,1134–1151; src/logging.F90:412–419 |
| 123 | 이상 없음 | 빈 줄 | 구조 확인 |
| 139 | 이상 없음 | 빈 줄 | 구조 확인 |
| 140 | 정정 | 보고서 행 ID와 정본 링크 | src/read_input.F:273–274,529–534,1794–1802 |
| 141 | 보완 | 전체 raw 검색 후 OWI reader의 실제 읽기 범위로 한정 | src/owiwind_netcdf.F:47,83,120,157,265; 전체 raw 검색 |
| 142 | 이상 없음 | OWI netCDF 결측값·scale·offset; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/owiwind_netcdf.F:687`; `models/ADCIRC/raw/source_code/adcirc/src/owiwind_netcdf.F:691` |
| 143 | 이상 없음 | 빈 줄 | 구조 확인 |
| 170 | 이상 없음 | 빈 줄 | 구조 확인 |
| 171 | 이상 없음 | 기상 snapshot 수와 시간 검사; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:6316`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:6325` |
| 172 | 이상 없음 | NWS=14의 추가 입력·fallback; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:8178`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:8179` |
| 173 | 이상 없음 | 빈 줄 | 구조 확인 |
| 222 | 보완 | 원시 NWS=13 검사 조건의 정본 앵커 | src/read_input.F:1794–1802 |
| 235 | 보완 | 빌드·파일 선택 정본 앵커 | src/wind.F:1996–1998,8021–8038 |
| 236 | 보완 | 정정한 정본 링크 | src/wind.F:2973–2974,8231–8240 |

### models/ADCIRC/source-analysis/adcirc-swan-coupling.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 12 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 64 | 보완 | 정본 앵커 추가 | src/couple2swan.F:389–442 |
| 71 | 보완 | 정본 앵커 추가 | src/timestep.F:699–753 |
| 76 | 이상 없음 | 빈 줄 | 구조 확인 |
| 77 | 이상 없음 | 파랑 방사 응력 발산의 부호; A 유지 | `models/ADCIRC/raw/source_code/adcirc/src/couple2swan.F:399`; `models/ADCIRC/raw/source_code/adcirc/src/couple2swan.F:400` |
| 78 | 이상 없음 | SWAN POINTS·TABLE 명령과 내부 표기; F 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:20`; `models/ADCIRC/raw/source_code/adcirc/thirdparty/swan/swanpre2.ftn:536–550` |
| 79 | 이상 없음 | SWAN TABLE의 실제 병렬 출력 위치; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:54`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:55` |
| 80 | 이상 없음 | SWAN 출력 제어와 추가 절차; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:88`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:89` |
| 81 | 정정 | SWAN 구현 확인; 소스 변경 지침 H | docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:113–154; thirdparty/swan/swanout1.ftn:3534,3764,3839,3933,4142,4280,4341 |
| 82 | 이상 없음 | SWAN 출력 수정 위치 안내; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:150`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:151` |
| 83 | 이상 없음 | 방사 응력 TYPE=1; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/rs2.F:95`; `models/ADCIRC/raw/source_code/adcirc/src/rs2.F:96` |
| 84 | 보완 | 정본 링크 | src/couple2swan.F:399–427 |
| 85 | 보완 | 정본 링크 | src/couple2swan.F:432–442 |
| 86 | 보완 | 정본 링크와 출력 저장 근거만 유지 | src/timestep.F:742–754 |
| 87 | 이상 없음 | SWAN 출력 읽기 오류의 처리; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:456`; `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:457` |
| 88 | 이상 없음 | 빈 줄 | 구조 확인 |

### models/ADCIRC/source-analysis/adcirc-tidal-forcing.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 16 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 50 | 이상 없음 | 빈 줄 | 구조 확인 |
| 51 | 보완 | 실제 식과 B 판정의 정본 링크; 노트 누락 C 유지 | src/adcirc.F:297–307; theory PDF-TIDAL-L0 |
| 52 | 이상 없음 | C10 ETRF 입력·Love 수 선택 누락; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:1540`; `models/ADCIRC/raw/source_code/adcirc/src/tidalpotential.F90:79` |
| 53 | 이상 없음 | 빈 줄 | 구조 확인 |
| 67 | 보완 | 실제 거리·천정각 계산과 C0 보정 인용; 정본 앵커 | src/tidalpotential.F90:262–319 |
| 68 | 보완 | 실제 계산을 인용한 정본 링크 | src/tidalpotential.F90:262–319 |
| 72 | 이상 없음 | 빈 줄 | 구조 확인 |
| 73 | 정정 | DEFAULT 직접 계산 포함; 비선형 해양 응답 보장 B 유지 | src/tidalpotential.F90:262–319,347 |
| 74 | 이상 없음 | 빈 줄 | 구조 확인 |
| 79 | 이상 없음 | 현재 코드는 LoadIT_Fric가 참이고 CBaroclinic.and.abs(IDEN).ge.5인 경로에서 abs(IDEN).ne.7일 때 UNTIDE를 호출한다. | `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2619`; `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2656` |
| 82 | 보완 | 정본 앵커와 표본 시간 조건·단위 변환 추가 | src/internaltide.F90:67–111; src/read_input.F:2522–2529 |
| 83 | 보완 | 정본 앵커 추가 | src/internaltide.F90:119,149–150 |
| 85 | 보완 | 정본 앵커 추가 | src/nodalattr.F:2619,2656–2750 |
| 88 | 이상 없음 | 빈 줄 | 구조 확인 |
| 89 | 보완 | 전체 조건을 유지한 정본 링크 | src/nodalattr.F:2693–2750 |
| 90 | 보완 | 두 정본 링크와 실제 호출 유지 | src/nodalattr.F:2659; src/internaltide.F90:67–111,149–150 |
| 91 | 이상 없음 | 빈 줄 | 구조 확인 |
| 106 | 보완 | 정본 링크 | src/nodalattr.F:2619,2656–2750 |

### models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 15 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 136 | 이상 없음 | 빈 줄 | 구조 확인 |
| 137 | 보완 | 보고서 이름과 행 ID 명시 | wind/vortex.F:388–413; features §5 H30·C37 |
| 138 | 이상 없음 | 관측 isotach 재현 설명의 수렴·대체값 조건 누락; C 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:596–598`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:334–338` |
| 139 | 보완 | 보고서 이름과 행 ID 명시 | gahm/README.md:7–9; GahmSolver.cpp:59–79; features §4 C36 |
| 140 | 이상 없음 | 빈 줄 | 구조 확인 |
| 170 | 이상 없음 | 빈 줄 | 구조 확인 |
| 171 | 정정 | 외부 자료 제공 관행 H | docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:360–366; gahm/tests/test_files/bal122005.dat:1–8 |
| 172 | 이상 없음 | GAHM isotach 개수; C 유지 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:5877`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:5878` |
| 173 | 이상 없음 | GAHM 음의 반경 해; C 유지 | `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:372`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:382` |
| 174 | 이상 없음 | 빈 줄 | 구조 확인 |
| 214 | 이상 없음 | 이 경로는 if | `models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:684`; `models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:706` |
| 216 | 보완 | 정본 앵커 추가 | wind/vortex.F:1147–1154 |
| 232 | 이상 없음 | 빈 줄 | 구조 확인 |
| 233 | 이상 없음 | 폭풍 이동속도 경험 보정; C 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:382`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:389` |
| 234 | 이상 없음 | 이동 보정 비율의 극값 설명에서 빠진 분기; C 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:402`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:829–834` |
| 235 | 이상 없음 | 빈 줄 | 구조 확인 |
| 258 | 보완 | 정본 앵커 추가 | wind/vortex.F:966–976 |
| 260 | 이상 없음 | 해석: case(3)에서 QuadIr4의 1·2·3번 반경을 문서의 R34·R50·R64에 대응시킬 때, else if | `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:1004`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:1005` |
| 262 | 이상 없음 | 해석: case(3)에서 QuadIr4의 1·2·3번 반경을 문서의 R34·R50·R64에 대응시킬 때, else if | `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:1004`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:1005` |
| 264 | 이상 없음 | 해석: case(3)의 첫 반경을 R34에 대응시킬 때 바깥 유지 조건은 r>R34다. | `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:1004`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:1005` |
| 288 | 이상 없음 | 빈 줄 | 구조 확인 |
| 289 | 보완 | 정본 링크와 문서·활성 호출 근거 유지 | docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:423–427; wind/vortex.F:1147–1154; wind/aswip.F:669,706–709 |
| 290 | 보완 | 보고서 이름과 행 ID 명시 | wind/aswip.F:677–709,2960–2963; features §5 H28·H29 |
| 291 | 보완 | rmx>0 조건 및 보고서 ID 명시; F 유지 | wind/vortex.F:1148–1152,883; src/wind.F:6053–6055 |
| 292 | 이상 없음 | 각도 보간의 절대각·상대각; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:532`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:533` |
| 293 | 이상 없음 | GAHM 반경 가중치·바깥 영역; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:575`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:577` |
| 294 | 보완 | 정본 링크 | wind/vortex.F:966–976 |
| 295 | 이상 없음 | GAHM isotach 수별 반경 보간; C 유지 | `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:990`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:991` |
| 296 | 이상 없음 | 빈 줄 | 구조 확인 |
| 318 | 이상 없음 | 빈 줄 | 구조 확인 |
| 319 | 이상 없음 | NWS13과 GAHM; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:10`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:1502` |
| 320 | 이상 없음 | GAHM 주변 기압 기호; B 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:49`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:50` |
| 321 | 이상 없음 | Holland B의 경험 범위; A 유지 | `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:125`; `models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:126` |
| 322 | 보완 | 나눗셈의 비영 조건을 명시; F 유지 | wind/vortex.F:391–392; docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:167 |
| 323 | 이상 없음 | GAHM 남반구 처리; C 유지 | `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:210`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:874` |
| 324 | 보완 | 정본 앵커 추가 | src/wind.F:6207–6216 |
| 325 | 이상 없음 | GAHM 외곽 cutoff의 비활성 상태; C 유지 | `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:906`; `models/ADCIRC/raw/source_code/adcirc/wind/vortex.F:907` |
| 326 | 이상 없음 | 빈 줄 | 구조 확인 |

### models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 16 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 98 | 보완 | 기상 노트 정본 링크 | src/read_input.F:1794–1802 |
| 171 | 이상 없음 | 빈 줄 | 구조 확인 |
| 172 | 정정 | 보고서 행 ID L761 링크 및 NWS13 정본 앵커 | src/owiwind_netcdf.F:262; fort15 §5 L761 |
| 173 | 보완 | ADCNETCDF 조건·후속 경로 검증과 정본 앵커 | src/read_input.F:530,1775–1830; src/owiwind_netcdf.F:326–328 |
| 174 | 이상 없음 | 빈 줄 | 구조 확인 |

### models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 17 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 58 | 보완 | 기상 노트 정본 링크 | src/read_input.F:1794–1802 |
| 78 | 보완 | 정본 링크 | src/nws08.F90:529–533 |
| 82 | 이상 없음 | NWS=19 reader는 advr1(ient)·날짜·TECH·TAU·좌표·풍속·기압·등풍속선·네 반경·배경 기압·RMW·이동 방향·이동 속도·이름·cycle 번호·등풍속선 수·네 | `models/ADCIRC/raw/source_code/adcirc/src/wind.F:5223`; `models/ADCIRC/raw/source_code/adcirc/src/wind.F:5224` |
| 95 | 보완 | 정본 링크 | src/wind.F:6207–6216 |
| 102 | 보완 | 기상 노트 정본 링크 | src/wind.F:1996–1998,8021–8038,8231–8240 |
| 115 | 이상 없음 | 빈 줄 | 구조 확인 |
| 116 | 보완 | foundation 정본 링크 | src/owiwind_netcdf.F:262; docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:10,18 |
| 117 | 보완 | foundation 정본 링크 | src/read_input.F:1775–1830; src/owiwind_netcdf.F:326–328 |
| 118 | 이상 없음 | 빈 줄 | 구조 확인 |

### models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md

| 원래 +줄 번호 | 처리 | 확인 내용 | 대표 근거 |
|---:|---|---|---|
| 21 | 이상 없음 | 검증 날짜 메타데이터 | 사용자 지정 검증일 2026-10-12 |
| 109 | 이상 없음 | 빈 줄 | 구조 확인 |
| 110 | 보완 | NTIP=2와 ADCNETCDF 조건 명시; C 유지 | src/read_input.F:6367–6382 |
| 111 | 이상 없음 | 빈 줄 | 구조 확인 |

## 범위와 확인 결과

이 작업의 쓰기는 허용한 9개 노트와 theory 보고서 §5 및 이 결과물에 한정했다. 보고서 §5 앞부분의 SHA-256은 검증 전후 모두 `a3b79849d891df64a3db96a91f1b430f385b179ca9ee6349fa747d91d640af3c`이다. 보고서 표에서 324개 행 ID가 중복 없이 유지됨을 다시 셌다. 새 정본 링크의 파일과 앵커를 확인했다. `git diff --check`로 변경된 Markdown의 공백 오류를 검사했다. Git 상태를 바꾸는 명령은 사용하지 않았다. 모델 실행과 컴파일은 하지 않았다.

확인하지 않은 것은 PBL 식 (11)·(14)의 전체 폐합 동치와 각 E 후보의 실행 결과이다. 허용 범위 밖 보고서의 6개 분류 변경은 이 결과물에만 보고했다. 대상 추가 줄의 정적 대조는 모두 끝냈다.

정정 29, 보완 57, 분류 변경 83, 이상 없음 181

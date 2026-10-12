# ADCIRC 묶음 A — 10-12 결론 검증

검증일은 2026-10-12이다. 저장소 루트는 `/home/firesinger/coastal-wiki`이다.

시작 시점의 `git diff -U0 HEAD -- <노트>`에서 `+++` 파일 헤더를 제외한 모든 `+` 줄을 고정했다. HEAD는 `ba72e827b37dfdcd7b7d3866cf1a9415e3ee216b`이다. 아래의 ‘원래 줄’은 수정 전 작업 트리의 줄 번호이다. 중복 삭제 뒤의 diff 줄 수를 최초 대상 수로 다시 세지 않았다.

대상은 12개 노트의 365개 추가 줄이다. 메타데이터·빈 줄·제목·표 구분선·도식 줄도 포함했다. 같은 내용이 반복되어도 노트의 각 위치를 별도로 셌다. 아래 전 줄 대조 기록은 이 고정 목록을 모두 포함한다.

사실을 적은 줄의 인용은 `nl -ba`로 열었다. 조건의 상위 분기와 실제 사용식도 대조했다. PDF 판독 기록은 원문 전사와 AI 요약을 구분했다. 외부 EOS 판정은 제공된 `external-results-ad.md`의 접근 범위 안에서 사용했다. UNESCO TP 44를 새로 직접 확인했다고 기록하지 않았다.

정정·보완은 원래 추가 줄을 기준으로 서로 겹치지 않게 셌다. 분류 변경은 실제로 바꾼 보고서의 기존 대상 ID 수이다. 신규 E 후보는 원래 C 줄의 보완으로 세었다. 추가한 대표 노트의 링크 행은 이 수에 중복 가산하지 않았다. 중복 문단의 빈 줄은 내용상 이상 없음으로 세었다.

코드의 `v56.2.1`은 로컬 `CMakeLists.txt:92`의 표시값이다. 공식 release tag와의 동일성은 확인하지 않았다. 모델은 실행하지 않았다. git은 diff·상태·HEAD 조회에만 사용했다. git으로 작업 트리·인덱스·참조를 변경하지 않았다.

## 노트별 대조 수

| 노트 | 대조한 + 줄 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|
| [adcirc-3d-mode.md](../../../models/ADCIRC/source-analysis/adcirc-3d-mode.md) | 53 | 5 | 2 | 46 |
| [adcirc-3d-vssol-vertical-scheme.md](../../../models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md) | 9 | 1 | 0 | 8 |
| [adcirc-baroclinic-coupling.md](../../../models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md) | 43 | 11 | 1 | 31 |
| [adcirc-baseline-anatomy.md](../../../models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md) | 63 | 10 | 4 | 49 |
| [adcirc-boundary-conditions.md](../../../models/ADCIRC/source-analysis/adcirc-boundary-conditions.md) | 14 | 1 | 0 | 13 |
| [adcirc-gwce-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-gwce-implementation.md) | 12 | 1 | 0 | 11 |
| [adcirc-momentum-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-momentum-implementation.md) | 12 | 1 | 0 | 11 |
| [adcirc-nffr-periodic-flux-boundary.md](../../../models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md) | 1 | 0 | 0 | 1 |
| [adcirc-parallel-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-parallel-implementation.md) | 8 | 0 | 0 | 8 |
| [adcirc-timestep-orchestration.md](../../../models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md) | 65 | 4 | 1 | 60 |
| [adcirc-weir-boundary.md](../../../models/ADCIRC/source-analysis/adcirc-weir-boundary.md) | 44 | 4 | 2 | 38 |
| [adcirc-wetting-drying-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md) | 41 | 2 | 2 | 37 |
| 합계 | 365 | 40 | 12 | 313 |

## 정정·보완 목록

첫 열은 `노트:원래 줄→수정 후 줄`이다. 삭제한 문단은 정본 링크가 있는 문단으로 통합했다. 원문 경로에서 `src/`, `prep/`, `wind/`, `work/`, `docs/`의 기준은 `models/ADCIRC/raw/source_code/adcirc/`이다.

| 노트:줄 | 구분 | 이전 요지 | 새 요지 | 근거 |
|---|---|---|---|---|
| [adcirc-3d-mode.md:42→42](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:42) | 정정 | 3D 모드와 경압 결합에 시간 reader 설명 중복 | 경압 결합 입력 절을 정본으로 연결 | couple2baroclinic3D.F:193–246 |
| [adcirc-3d-mode.md:43→43](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:43) | 정정 | 두 노트에 ADCIRC 격자 reader 설명 중복 | 경압 결합 입력 절을 정본으로 연결 | couple2baroclinic3D.F:253–262,499–511 |
| [adcirc-3d-mode.md:118→118](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:118) | 보완 | EOS-3 T·S 제한의 IDEN 조건 생략 | ABS(IDEN)=4 조건 추가 | vsmy.F:4335–4355 |
| [adcirc-3d-mode.md:124→124](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:124) | 보완 | c24 부호 후보의 실행 조건 불명시 | EqnState=3·ABS(IDEN)=4·표층 사용을 명시 | vsmy.F:4335–4368; external-results-ad.md F17 |
| [adcirc-3d-mode.md:126→126](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:126) | 정정 | F17과 같은 부호·Horner 근거를 반복 | F17 정본 참조와 F19의 독립 대응만 유지 | 외부 판정 F19; vsmy.F:3964,4364–4366 |
| [adcirc-3d-mode.md:128→128](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:128) | 정정 | F17·F19와 계수 대조 문단 중복 | 연도 표기 F 근거와 F17 정본 참조 유지 | external-results-ad.md C33; vsmy.F:4338 |
| [adcirc-3d-mode.md:130→130](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:130) | 정정 | EOS 노트가 중복된 대표 후보 표로 되돌아감 | 이 절을 c24 정본으로 고정 | vsmy.F:3964,4364–4366; 외부 판정 F17 |
| [adcirc-3d-vssol-vertical-scheme.md:92→92](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:92) | 정정 | 가리키는 곳 없는 254·255행의 E 인용 | 보고서 L254·L255의 재설계 C로 바로잡음 | vsmy.F:942–1015; fort15 §5 L254,L255 |
| [adcirc-baroclinic-coupling.md:30→30](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:30) | 정정 | Q03를 D(문서에만 있음)로 분류 | Q03를 H로 변경하고 전체 raw 검색 결과 기록 | couple2baroclinic3D.F:137–139; timestep.F:2163–2176; prep/prep.F:2500–2501 |
| [adcirc-baroclinic-coupling.md:68→68](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:68) | 보완 | CDisp 근거에 HBREAK 양수 분기만 인용 | CDisp가 ELSE에 속하는 원문 추가 | couple2baroclinic3D.F:151–159 |
| [adcirc-baroclinic-coupling.md:88→88](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:88) | 정정 | 3D 노트와 EOS 판정 중복 | 3D 노트 정본으로 연결 | 외부 판정 F17,F19,C33 |
| adcirc-baroclinic-coupling.md:90（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| adcirc-baroclinic-coupling.md:92（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| adcirc-baroclinic-coupling.md:94（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| adcirc-baroclinic-coupling.md:96（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| adcirc-baroclinic-coupling.md:98（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| adcirc-baroclinic-coupling.md:100（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| adcirc-baroclinic-coupling.md:102（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| adcirc-baroclinic-coupling.md:103（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| adcirc-baroclinic-coupling.md:104（중복 삭제） | 정정 | 3D 노트와 원문·결함 표 중복 | 중복을 삭제하고 같은 절의 정본 링크로 통합 | 3D 모드 EOS-80 절; vsmy.F:3964,4335–4368 |
| [adcirc-baseline-anatomy.md:102→102](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:102) | 보완 | 로컬 코드 표기와 공식 release 동일성의 구분 없음 | 판정 대상이 로컬 소스임을 한정 | CMakeLists.txt:92; external-results-ad.md 확인하지 않은 것 |
| [adcirc-baseline-anatomy.md:106→106](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:106) | 정정 | EOS-80 원문 판정과 후보 표 중복 | 정본 링크와 실제 사용 조건만 남김 | vsmy.F:4335–4368; external-results-ad.md |
| [adcirc-baseline-anatomy.md:107→107](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:107) | 정정 | 노트 안에 없는 343·348행 인용 | 보고서 행 ID로 교체하고 무관한 NWS=0/1 확대 삭제 | fort15 §5 L343,L346,L348 |
| [adcirc-baseline-anatomy.md:114→114](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:114) | 정정 | DEBUG_WARN_ELEV가 없는 빌드에 E 적용 | DEBUG_WARN_ELEV 정의 및 namelist가 먼저 켜지 않은 조건 | read_input.F:809–830,985–993; timestep.F:1307–1313 |
| [adcirc-baseline-anatomy.md:119→119](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:119) | 정정 | 분 단독 입력 E 설명이 대표 표 두 행과 위어 노트에 중복 | 위어 노트를 정본으로 하고 보고서 두 출처를 한 행에 병합 | weir_boundary.F90:1097,1133–1163; weir 노트 원래88행 |
| [adcirc-baseline-anatomy.md:137→137](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:137) | 보완 | 전역 w-vel3D의 사용 근거는 station 경로 중심 | fort.45 nodal WZ 연결과 저장을 추가 | write_output.F:3332,3338; netcdfio.F90:4903–4922 |
| [adcirc-baseline-anatomy.md:140→140](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:140) | 정정 | 노트 안에서 찾을 수 없는 D32 지시 | 보고서 L549(D32)와 같은 표의 후보를 명시 | outputs §5 L549; write_output.F:6248,6415 |
| [adcirc-baseline-anatomy.md:142→142](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:142) | 보완 | 전역 EOS 출력의 변환 부재 근거는 station 쓰기 중심 | fort.44 nodal 연결과 쓰기 경로 추가 | write_output.F:3263,3278,3293; netcdfio.F90:4873–4899 |
| [adcirc-baseline-anatomy.md:143→143](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:143) | 정정 | 자기 주석을 최종화 근거로 사용하고 병렬 수 문제를 함께 E로 설명 | min 식과 출력 창으로 종료 E 유지. 병렬 수는 조건부·미확인 | xdmfio.F:151–178,264–270,329–341,369–375; write_output.F:1861–1862,4311–4349 |
| adcirc-baseline-anatomy.md:152（중복 삭제） | 정정 | 대표 표의 WEIR-06 후보와 같은 내용 중복 | 원래119행의 정본 링크에 출처를 병합 | weir_boundary.F90:1133–1145 |
| [adcirc-baseline-anatomy.md:155→154](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:154) | 정정 | 하층 EOS 결함 상세 문단 중복 | 3D 모드 F16·K73로 통합 | vsmy.F:4335–4420 |
| [adcirc-baseline-anatomy.md:156→155](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:155) | 정정 | 유형 11 후보 상세 문단 중복 | 위어 노트 K30으로 통합 | vew1d.F90:325–352; flux_specified_boundaries.rst:80–82 |
| [adcirc-baseline-anatomy.md:157→156](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:156) | 보완 | 램프 기본값과 초기화 도달 경로 없음. 상세 중복 | 기본값·실제 호출 순서 추가 및 timestep 정본으로 통합 | wind.F:243–246,7710–7713,7827–7831; adcirc.F:358–363 |
| [adcirc-baseline-anatomy.md:158→157](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:157) | 정정 | 노트 안에 없는 4절 C25 지시 | features 보고서의 C25로 명시 | features §5 C25; couple2swan.F:1153,1211–1224 |
| [adcirc-boundary-conditions.md:67→67](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:67) | 정정 | S06를 D(문서에만 있음)로 분류 | S06를 H로 변경하고 전체 raw 검색 결과 기록 | nodalattr.F:1555–1562; asgs/util/input/nodalattr/nodalattr.f90:88; idealized_channel.rst:66–68 |
| [adcirc-gwce-implementation.md:98→98](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:98) | 정정 | Solver와 Working Rules에 대각 경로 반복 | 세부 대각 계산을 Solver 절로 연결 | gwce.F:2000–2016,3070 |
| [adcirc-momentum-implementation.md:77→77](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:77) | 정정 | timestep과 운동량 노트에 같은 순서 문단 중복 | timestep 정본 연결 | gwce.F:182–222; timestep.F:1073,1107 |
| [adcirc-timestep-orchestration.md:22→22](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:22) | 정정 | ADCIRC_Run 순서 문단이 두 곳에 중복 | 뒤의 호출 흐름을 정본으로 연결 | adcirc.F:475–492 |
| [adcirc-timestep-orchestration.md:52→52](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:52) | 정정 | D02를 D(문서에만 있음)로 분류 | D02를 H로 변경하고 전체 raw 검색 결과 기록 | dynamic_water_level_correction.rst:본문; wind.F:7827–7833; gwce.F:767 이후 |
| [adcirc-timestep-orchestration.md:54→54](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:54) | 보완 | 램프 기본값·초기화 도달 경로 없음 | 0.d0 기본값과 초기 호출의 0/0 도달 추가 | wind.F:243–246,7710–7733,7827–7834; adcirc.F:358–363 |
| [adcirc-timestep-orchestration.md:89→89](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:89) | 정정 | 두 노트에 C05 문단 중복 | 운동량 노트 정본 링크 | theory §5 C05; gwce.F의 TK 사용 |
| [adcirc-timestep-orchestration.md:121→121](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:121) | 정정 | GWCE 노트와 C02 결론 문단 중복 | GWCE 노트 정본 링크 | read_input.F·gwce.F의 시간 가중치와 nodalattr.F의 FTHETA |
| [adcirc-weir-boundary.md:34→34](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:34) | 정정 | BARMIN 문턱을 모든 설정에서 미터로 단정 | 모델 길이 단위로 한정 | weir_boundary.F90:BARMIN·1751·1876; parameter_definitions/index.rst:492 |
| [adcirc-weir-boundary.md:40→40](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:40) | 정정 | B03를 D(문서에만 있음)로 분류 | B03를 H로 변경하고 전체 raw 검색 결과 기록 | flux_specified_boundaries.rst; momentum.F:845; asgs/util/input/nodalattr/eddyvis.f90:129 |
| [adcirc-weir-boundary.md:42→42](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:42) | 보완 | 기존 D 근거의 보조 프로그램 검색 결과 불명시 | D 유지. ASGS 등 보조 프로그램 포함 검색 결과 명시 | mesh.F:2681–2707; ASGS 격자·경계 처리 |
| [adcirc-weir-boundary.md:53→53](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:53) | 정정 | V18를 D(문서에만 있음)로 분류 | V18를 H로 변경하고 전체 raw 검색 결과 기록 | vew1d.F90; adcircpy/mesh/mesh.py:204–214; vertical_element_walls.rst |
| [adcirc-weir-boundary.md:65→65](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:65) | 보완 | 기존 D 근거의 보조 프로그램 검색 결과 불명시 | D 유지. ASGS 등 보조 프로그램 포함 검색 결과 명시 | gwce.F:1888–1897; weir_boundary.F90:2366–2370; ASGS CHKWEIRS |
| [adcirc-weir-boundary.md:67→67](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:67) | 정정 | V08를 D(문서에만 있음)로 분류 | V08를 H로 변경하고 전체 raw 검색 결과 기록 | weir_boundary.F90:2409–2414; prep/read_global.F:313–314; util/xdmf2adcirc.f90:1004–1014 |
| [adcirc-wetting-drying-implementation.md:91→91](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:91) | 보완 | 추가 침수 조건은 C로만 정리 | C 유지 및 IT·BTIME_END 단위 불일치 E 추가 | wetdry.F:172,204–206,841–864; hstart.F:1244–1246; timestep.F:494,505 |
| [adcirc-wetting-drying-implementation.md:99→103](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:103) | 정정 | 전환 사용 여부 미확인이라고 남음 | 현재 문서·검색 결과에 맞춰 활성 전환 미사용 명시 | parameter_definitions/index.rst:698; NODEDRYMIN·NODEWETMIN·NODEREP 검색 |
| [adcirc-wetting-drying-implementation.md:111→115](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:115) | 보완 | 검색 결과를 선언·읽기·로그만으로 설명 | control·XDMF 재기록 경로를 추가하고 상태 전환과 구분 | control.F:927–930; xdmfio.F:907–912; parameter_definitions/index.rst:698 |
| [adcirc-wetting-drying-implementation.md:131→135](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:135) | 정정 | 표에 전환 효과 미확인 유지 | 확인된 미사용 판정과 정본 링크 | parameter_definitions/index.rst:698; wetdry.F 전환 사용 검색 |

대표 노트의 새 `WETDRY-BTIME-UNITS` 링크 행은 [adcirc-baseline-anatomy.md:160](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:160)에 있다. 실제 단위 대조의 정본은 [침수·노출 노트](../../../models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md#wetdry-btime-units)이다.

## 분류 변경과 보고서 반영

| 보고서 행 ID | 이전→새 | 이유 | 보고서 처리 |
|---|---|---|---|
| [features §5 Q03](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | D→H | BPGX·BPGY 입력을 만드는 외부 생성기의 중첩 밀도 적분은 이 소스 묶음만으로 판정하지 않는다. native BPG3D의 밀도 적분은 실제로 존재한다 (`src/timestep.F:2163–2176`). | §5 847행을 같은 내용으로 정정했다. |
| [features §5 S06](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | D→H | OceanMesh2D의 Calc_Sponge는 외부 속성 생성 도구이다. ADCIRC의 속성 읽기·적용과 외부 도구 내부 동작은 구분한다. | §5 864행을 같은 내용으로 정정했다. |
| [features §5 D02](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | D→H | 수위 추종 성능은 개방경계 연결과 점진적 보정에 관한 조건부 주장이다. 정적 코드 대조만으로 사례의 재현 정확도를 판정할 수 없다. | §5 841행을 같은 내용으로 정정했다. |
| [features §5 B03](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | D→H | 경계 유형의 안정성과 경계층 해상도에 관한 선택 권고는 코드 조건문만으로 판정하는 구현 명제가 아니다. | §5 800행을 같은 내용으로 정정했다. |
| [features §5 V18](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | D→H | condensed_nodes가 CFL 제약을 완화한다는 정성적 성능 주장은 정적 코드만으로 검증할 수 없다. 특정 허용 시간 간격도 이 판정에서 도출하지 않는다. | §5 840행을 같은 내용으로 정정했다. |
| [features §5 V08](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | D→H | VEW 월류 계수 1.0은 문서의 권고값이다. 코드가 임의 계수를 읽는 사실만으로 그 권고의 적정성을 판정하지 않는다. | §5 838행을 같은 내용으로 정정했다. |

features §5의 현재 집계는 D 33→27, H 1→7로 바꿨다. 대상 276개와 나머지 분류 수는 유지했다. 이전 판정 과정의 역사 집계는 바꾸지 않았다.

`K04·C03`의 C는 유지했다. 별도 E 후보의 정본 링크를 보고서에 추가했다. `K35`의 E는 유지했다. 기본값과 초기화 직후의 호출 경로를 보고서에도 보완했다.

VSSOL 노트의 ‘254·255행의 E’는 이미 C로 정리된 `fort15 §5 L254, L255`를 잘못 인용했다. 노트와 `fort15 §5 C29(L867)`의 해당 인용을 C로 맞췄다. C29 자체의 B는 유지했다. 이 동기화는 보고서의 새 분류 변경 6개에 더하지 않았다.

변경한 여섯 features ID는 ADCIRC의 source-analysis·manual-notes에서 참조 위치를 다시 검색했다. 해당 features 행을 참조하는 다른 묶음 노트는 찾지 못했다. 다른 보고서의 동명 `D02`·`B03`은 별개 ID로 구분했다.

## 원래 D 줄의 전체 raw 재검색

모든 행에 `rg -i --no-ignore -n -g '!.git/**' '<패턴>' models/ADCIRC/raw`를 실행했다. `.git` 내부 저장 객체만 제외했다. 일반 source 파일·보조 프로그램·유틸리티·동봉된 다른 저장소·문서·입력 자료는 검색 범위에 포함했다. 검색 결과 수는 일치 줄 수와 일치 파일 수이다. 이는 구현 개수가 아니다.

| 원래 D 줄 | 패턴 | 일치 줄 / 파일 | 결과와 판정 |
|---|---|---:|---|
| adcirc-baroclinic-coupling.md:30 | `BPGX\|BPGY\|baroclinic.?pressure\|density.?integr` | 171 / 44 | ADCIRC 본체의 BPG 읽기와 native 적분이 검색되었다. prep는 적분 방식 설정을 전달한다. 외부 BPG 생성기의 중첩 적분 구현은 찾지 못했다. H로 정정했다. |
| adcirc-boundary-conditions.md:67 | `OceanMesh2D\|Calc_Sponge\|sponge_generator_layer` | 215 / 123 | ADCIRC의 nodalattr·prep와 ASGS nodalattr 도구에서 속성 이름·전달 경로가 검색되었다. Calc_Sponge 구현은 찾지 못했다. H로 정정했다. |
| adcirc-timestep-orchestration.md:52 | `dynamicWaterLevelCorrection\|Pamlico\|lag behind` | 1037 / 304 | 보정의 입력·래핑·GWCE·출력 경로와 ASGS 설정·자료 파일이 검색되었다. 이 결과는 Pamlico 사례의 추종 성능을 검증한 실행 결과가 아니다. H로 정정했다. |
| adcirc-weir-boundary.md:40 | `instabilities\|lateral.boundary.layer\|no.tangential.slip` | 217 / 79 | 본체의 no-tangential-slip 분기와 ASGS eddyvis의 안정성 주석이 검색되었다. 이 주석은 문서의 경계 선택·해상도 권고를 수치 검증하지 않는다. H로 정정했다. |
| adcirc-weir-boundary.md:42 | `consecutive\|illegal.overlap\|boundary.*order\|NVELEXT\|LBCODEI` | 766 / 346 | 본체·prep·ASGS 경계 처리에서 부분 검사를 확인했다. 네 입력 규칙 전체의 검사·재배열은 찾지 못했다. 입력 작성 규약의 D를 유지했다. |
| adcirc-weir-boundary.md:53 | `quasi.?1d\|condensed_nodes\|CFL` | 1478 / 336 | VEW 집약 구현과 adcircpy의 일반 CFL 시간 간격 추정이 검색되었다. `adcircpy/mesh/mesh.py:204–214`의 추정은 VEW 완화량의 검증이 아니다. H로 정정했다. |
| adcirc-weir-boundary.md:65 | `BARINHT\|RBARWLL\|condensed_nodes` | 396 / 87 | ASGS CHKWEIRS 등은 장벽 높이를 조정한다. NBVV를 높은 floodplain 쪽으로 재배치하는 경로는 찾지 못했다. 입력 배치 규약의 D를 유지했다. |
| adcirc-weir-boundary.md:67 | `BARINCFSB\|BARINCFSP` | 463 / 78 | 본체·prep·XDMF 유틸리티와 ASGS 격자 도구에서 계수 읽기·전달·출력이 검색되었다. VEW 계수를 1.0으로 강제하는 조건은 확인되지 않았다. H로 정정했다. |

Q03의 native BPG3D 적분은 `src/timestep.F:2163–2176`에 있다. 외부 BPG 생성기의 존재 여부와 이 native 적분을 혼동하지 않았다. S06의 ASGS 속성 이름은 `raw/source_code/asgs/util/input/nodalattr/nodalattr.f90:88`에 있다. V18의 adcircpy CFL 추정은 `raw/source_code/adcircpy/adcircpy/mesh/mesh.py:204–214`에 있다. 이 두 경로를 각각 Calc_Sponge 구현이나 VEW 성능 검증으로 세지 않았다.

## E 후보의 반대 근거 대조

아래는 E 후보마다 확인한 다른 경로·보정·단위·의도 변경의 결과이다. 후보와 같은 문단의 인용 원문도 함께 열었다. ‘없다’는 문장은 명시한 경로와 검색 결과에 대한 정적 판독 결과이다. 실제 오류 발생을 재현했다는 뜻이 아니다. 원래 대표 표의 모든 후보를 포함했다. 다른 노트의 중복 후보는 같은 ID의 대조를 공유했다.

| 원래 대상 위치 | 반대 근거를 확인한 결과 | 핵심 원문 |
|---|---|---|
| adcirc-baseline-anatomy.md:106 | EqnState=3·ABS(IDEN)=4의 표층 사용을 확인했다. 외부 Table 3 대조 기록에서 의도적 부호 변경을 뒷받침하는 근거는 없다. | vsmy.F:3964,4335–4368; external-results-ad.md:F17·F19·C33 |
| adcirc-baseline-anatomy.md:107 | NWS=30의 NCICE 분기는 CICE_TIMINC를 읽는다. NWS=29의 두 READ에는 해당 토큰이 없다. | read_input.F:2746–2770,2820 |
| adcirc-baseline-anatomy.md:108 | coldstart·시간 갱신은 양수 19만 처리한다. hotstart의 ABS(NWS)=19 경로가 다른 경로를 보정하지 않는다. | read_input.F:1782–1784,2693; wind.F:1472,1914,2622 |
| adcirc-baseline-anatomy.md:109 | 진단은 abs(NWS)를 말하지만 실제 거부 조건은 양수만 열거한다. ABS(NWS)=7의 얼음 READ 경로도 확인했다. | read_input.F:2322–2327,2599–2606 |
| adcirc-baseline-anatomy.md:110 | WindInit의 허용 문자열과 WindIceDrag의 CASE를 대조했다. NWS=0 조기 반환은 영향 범위에서 제외했다. | wind.F:367–394,738–767 |
| adcirc-baseline-anatomy.md:111 | namelist 부재 로그는 반환한다. cstart·subprep는 초기화 없는 subdomainOn을 검사한다. 특정 컴파일러의 실제 논리값은 판정하지 않았다. | subdomain.F:44; global.F:1601–1635; cstart.F:114; prep/subprep.F:68–97 |
| adcirc-baseline-anatomy.md:112 | NOUTGE READ 뒤 TVW 값을 재상속하는 대입은 찾지 못했다. 후속 일정식은 먼저 복사한 값을 쓴다. | read_input.F:574–579,4132,4276–4285 |
| adcirc-baseline-anatomy.md:113 | 검사 전에 NCICE는 분리하지만 NRS는 뒤에 분리한다. 공통 NWS13INIT은 검사를 빠진 문자열도 날짜로 읽는다. | read_input.F:1775–1830; owiwind_netcdf.F:326–328 |
| adcirc-baseline-anatomy.md:114 | WarnElevControl의 선행 논리값 설정은 예외로 한정했다. legacy 상세 READ는 #else 안이다. 뒤의 정수→논리 변환은 찾지 못했다. | read_input.F:809–830,985–993; timestep.F:1307–1313 |
| adcirc-baseline-anatomy.md:115 | prep reader와 모델의 후속 40·41 처리는 존재한다. ASCII mesh reader의 거부를 기능 전체의 부재로 해석하지 않았다. | mesh.F:446–554; prep/read_global.F; boundaries.F |
| adcirc-baseline-anatomy.md:116 | FoundEVC의 초기 false와 XDMF의 true 설정을 확인했다. ASCII EVC 헤더에서는 true 설정을 찾지 못했다. | nodalattr.F:467,688,936,1276–1280 |
| adcirc-baseline-anatomy.md:117 | 5성분 소비 경로와 기본값 배열 길이 3을 대조했다. ASCII READ 앞 배열 확장이나 3성분 제한은 없다. | nodalattr.F:255,1321–1322,2661 이후 |
| adcirc-baseline-anatomy.md:118 | mesh의 102·112 허용과 river 처리를 확인했다. simpleFluxBoundaries 할당 CASE에는 두 유형이 없다. | mesh.F:446; boundaries.F:353–354 |
| adcirc-baseline-anatomy.md:119 | VARYTYPE=2의 분 검사와 VARYTYPE=3·ASSIGN_TVW_TIMING의 분 합산을 대조했다. VARYTYPE=1의 종료 검사는 분을 포함하지 않는다. | weir_boundary.F90:1097,1133–1163 |
| adcirc-baseline-anatomy.md:120 | 다른 끝 시각 계산은 TimeEndSec를 쓴다. PARSE_SCHEDULE의 BAR_DEG_END만 TimeStartSec를 더한다. | weir_boundary.F90:1382–1386; ASSIGN_TVW_TIMING |
| adcirc-baseline-anatomy.md:121 | z-x-z 구성과 3열 출력은 전체 행렬을 쓴다. rotation_matrix READ만 각 행의 셋째 열에 단일 값을 대입한다. | mesh.F:4404–4418; fortrotm.rst:34–36 |
| adcirc-baseline-anatomy.md:122 | 공통 openFileForRead의 OPEN에는 unformatted 지정이 없다. 이 연결 뒤 NWS11의 unformatted READ가 실행된다. | io.F90:100–101; wind.F:4187–4196 |
| adcirc-baseline-anatomy.md:123 | NWS=±4의 mbar 변환 방향을 대조했다. NWS11 입력·보간 뒤의 별도 100배 보정은 찾지 못했다. | wind.F:4165,4227–4228; fort200.rst:84 |
| adcirc-baseline-anatomy.md:124 | allMessage(ERROR)는 자체 종료 경로가 아니다. check_owi_err는 iret.ne.0만 종료한다. 성공 READ 뒤 errorIO=0을 그대로 넘긴다. | owiwind.F:508–519,1122–1154 |
| adcirc-baseline-anatomy.md:125 | 모델 reader와 prep pipe 분기는 find(node_dict,...)를 쓴다. 4·24·64의 짝 라벨에는 변환이 없다. | prep/read_global.F:239–253; mesh.F의 내부 장벽 reader |
| adcirc-baseline-anatomy.md:126 | 모델의 고정 형식 READ와 prep의 list-directed READ를 대조했다. 모든 정상 파일의 실패로 확대하지 않았다. | prep/prep.F:3416; fort22.rst:214; wind.F의 NWS=±4 reader |
| adcirc-baseline-anatomy.md:127 | 관측소 순번 J를 쓰는 다른 출력 경로를 확인했다. labels(i)=i인 경우 문제가 가려진다는 조건을 유지했다. | globalio.F:852; mesh.F:72; fort61.rst:16–17 |
| adcirc-baseline-anatomy.md:128 | 관측소 store 경로는 divideByDepth를 처리한다. 전역 storeOne에서는 같은 나눗셈을 찾지 못했다. | write_output.F:1219–1222; timestep.F:1639; 전역 storeOne |
| adcirc-baseline-anatomy.md:129 | 관측소 유속·난류 초기화는 IRType=3이다. 전역은 앞서 IDEN으로 정한 값을 넘긴다. | cstart.F:1041–1043,1081–1086 |
| adcirc-baseline-anatomy.md:130 | 다른 누적 배열은 0으로 초기화한다. everDried_time의 -99999 초기값 뒤에는 DTDP 누적이 남는다. | write_output.F:6248,6411–6415 |
| adcirc-baseline-anatomy.md:131 | 다른 초기 분류 파일의 헤더 호출과 공통 writer를 대조했다. endrisinginun ASCII 초기화의 헤더 호출은 찾지 못했다. | write_output.F:1515,1663,1672; endrisinginun63.rst:18 |
| adcirc-baseline-anatomy.md:132 | 반복 출력 창과 고정 헤더 1을 대조했다. 둘 이상의 자료 세트를 쓰는 경우로 후보를 한정했다. | globalio.F:1464–1468; write_output.F:1861–1862 |
| adcirc-baseline-anatomy.md:133 | NOFF 핫스타트의 요소 매핑을 반대 경로로 확인했다. noff.100은 NE_G 레코드 수와 NP_G 할당·노드 labels를 섞는다. | write_output.F:697,709; globalio.F; mesh.F:72 |
| adcirc-baseline-anatomy.md:134 | G에 따른 m/ft 선택 함수와 변환 없는 DP·barht·pipediam 저장을 대조했다. 별도 m 규약이 있는 PIPEHT는 제외했다. | netcdfio.F90:9691–10032,10455–10458; parameter_definitions/index.rst:492 |
| adcirc-baseline-anatomy.md:135 | 입력의 응력/밀도 정의와 실제 u/v 저장을 대조했다. 속성만의 차원 오류와 u 속성 중복을 수치 자료 오류로 확대하지 않았다. | netcdfio.F90:1267–1278,4552–4553; fort22.rst |
| adcirc-baseline-anatomy.md:136 | NCICE=14·17의 100배 생성 뒤 출력 재정규화는 찾지 못했다. 다른 NCICE 분기까지 일반화하지 않았다. | wind.F:1396–1399,1727–1729; netcdfio.F90:1299–1302,2718–2722,5073–5074 |
| adcirc-baseline-anatomy.md:137 | station·nodal의 실제 수직 유속 배열 연결을 각각 확인했다. copied positive 문자열을 물리 방향 근거로 쓰지 않았다. | write_output.F:3157,3332,3338; netcdfio.F90:836–837,1690–1691,4911–4922 |
| adcirc-baseline-anatomy.md:138 | DTDP 누적과 일반 scalar 저장을 대조했다. 시간 배열을 길이로 변환하는 경로는 없다. | netcdfio.F90:3383–3384,5031–5032; write_output.F의 침수 시간 누적 |
| adcirc-baseline-anatomy.md:139 | ETA2+DP의 최대화와 지면 위 수심 정의를 대조했다. above geoid 문자열을 값의 기준으로 삼지 않았다. | netcdfio.F90:3409–3410,3438–3440; write_output.F의 최대 침수 수심 |
| adcirc-baseline-anatomy.md:140 | 발생 시각을 대입하는 극값 배열과 DTDP를 누적하는 건조 시간 배열을 구분했다. | write_output.F:6411–6415; netcdfio.F90의 time_of_everdried |
| adcirc-baseline-anatomy.md:141 | 일반 scalar writer는 node,time의 start·kount를 넘긴다. weir_dz 정의는 node 차원뿐이다. 실제 라이브러리 오류는 미확인이다. | netcdfio.F90:4642–4643,5073–5074; fort77의 weir_dz 정의 |
| adcirc-baseline-anatomy.md:142 | station 외에 fort.44 nodal 저장까지 확인했다. 같은 SigT·Sal·Temp 배열에 G 기준 속성만 바뀐다. | write_output.F:3263,3278,3293; netcdfio.F90:4873–4899,10455–10458 |
| adcirc-baseline-anatomy.md:143 | 출력 창과 min 식을 대입했다. 별도 finalize 호출은 찾지 못했다. np 대 np_g는 호출 시점·라이브러리 동작 미확인으로 분리했다. | xdmfio.F:329–341,369–375; write_output.F:1861–1862,4311–4349 |
| adcirc-baseline-anatomy.md:144 | 지역 헤더의 관측소 수와 같은 파일의 전역 자료 루프 수를 대조했다. 두 수가 다른 경우로 후보를 한정했다. | prep/post.F:POST71·POST91·POST43 |
| adcirc-baseline-anatomy.md:145 | native writer는 IDEN별 성분 수에 맞는 좌표를 쓴다. POST41의 NVar=1 배열에도 고정 두 원소를 요구하는 부분을 확인했다. | prep/post.F:POST41; write_output.F:3525–3529 |
| adcirc-baseline-anatomy.md:146 | native hotstart writer·reader가 요구하는 RS 자리와 조화 상태를 대조했다. POSTHOT의 보존 누락을 전체 재시작 성공 여부와 구분했다. | prep/post.F:POSTHOT; write_output.F:5255–5305; hstart.F |
| adcirc-baseline-anatomy.md:147 | 헤더의 AND count와 자료 루프의 OR를 직접 대조했다. 한 성분만 비기본값인 정적 반례가 성립한다. | writer.F:vector count와 683–685 |
| adcirc-baseline-anatomy.md:148 | 지역 층 배열 쓰기는 np를 넘긴다. DUU 계열 할당 MNP와 지역 쓰기의 np_g를 대조했다. NP_G>MNP인 경우로 한정했다. | vsmy.F:3571–3574,3617–3619,5285–5294 |
| adcirc-baseline-anatomy.md:149 | EVTOT→EV 연결에서 H 환산을 찾지 못했다. VSSOL 연직 확산과 비영 ISLIP 응력은 물리 높이 또는 TK 변환을 쓴다. | vsmy.F:995,1134,1187–1197; global_3dvs.F:195 |
| adcirc-baseline-anatomy.md:150 | -x.1 출력 선택 뒤 수심 함수에 원래 Tau0를 넘기는 경로를 확인했다. D=100의 -2·-2.1 분기 대입이 다르다. | nodalattr.F:TAU0 함수·2159; tau0.rst |
| adcirc-baseline-anatomy.md:151 | 40·41·43과 42의 식을 대조했다. 42에만 추가 H가 있다. Davies 계수 자체의 단위로 확대하지 않았다. | vsmy.F:1986–2007,2022; parameter_definitions/index.rst:1410–1416 |
| adcirc-baseline-anatomy.md:152 | 원래119행과 같은 후보이다. 해당 행의 반대 경로 대조를 공유하고 중복 행을 제거했다. | weir_boundary.F90:1133–1163 |
| adcirc-baseline-anatomy.md:153 | 2D·3D 모두 Fr를 U²/(gH)로 정한 뒤 다시 제곱한다. 같은 반복은 단위 정의와 식의 제곱 차이를 보정하지 않는다. | nodalattr.F:2483–2487,2562–2566; Yarnell·교각 마찰 원문 |
| adcirc-baseline-anatomy.md:154 | ROTATEBACK은 그룹 크기 2만 통과한다. ROTATE의 .not. 조건은 그 경우 반환한다. 법선 제거 경로를 이 회전 조건의 수정으로 보지 않았다. | vew1d.F90:151–158,189 |
| adcirc-baseline-anatomy.md:155 | 다른 EOS는 층별 T·S를 고른다. EOS-3 추가 적분점도 표층 영압 밀도를 재사용한다. 2022년 적분점 확장 주석은 T·S 의존성 제거를 설명하지 않는다. | vsmy.F:4243–4244,4335–4420 |
| adcirc-baseline-anatomy.md:156 | 다른 법선 투영과 경계 처리를 확인했다. ROTATE_OR_NOT 자체의 1 중복·11 누락은 남는다. 실행 영향은 미확인이다. | vew1d.F90:325–352; momentum.F:761–765 |
| adcirc-baseline-anatomy.md:157 | 같은 시각을 더하는 hotstart 기준과 초기화 직후 호출을 확인했다. 후속 기간 밖 처리는 첫 호출의 0/0을 우회하지 않는다. | wind.F:243–246,7710–7733,7827–7834; adcirc.F:358–363 |
| adcirc-baseline-anatomy.md:158 | SWAN 자체 AICE2·PICE 입력은 존재한다. 지역 SWAN_PIC를 그 입력에 전달하는 경로는 찾지 못했다. IICE=2 dry forcing은 제외했다. | couple2swan.F:1153,1210–1224; swancom1.ftn:7236–7240,7306–7313; swancom2.ftn:1542–1573 |
| adcirc-baseline-anatomy.md:159 | NWS=7은 wvnxout에 응력을 넣는다. netCDF 조건은 이를 속도 자료로 분류한다. 다른 응력 단위 CASE가 NWS=7을 구제하지 않는다. | wind.F:1142–1165; netcdfio.F90:1267–1274 |
| adcirc-baseline-anatomy.md:160 | 같은 case(5,25)의 노드·후속 짝 노드는 WithPipes 배열을 쓴다. IBCONN 속성 읽기만 일반 내부 장벽 배열을 쓴다. | mesh.F:1240–1261,1300–1301 |
| adcirc-wetting-drying-implementation.md:91 | BTIME_END의 다른 대입·사용은 초 시각이다. timestep의 LT 변경·EQ 종료 처리도 IT와의 비교 단위를 바꾸지 않는다. | wetdry.F:172,841–845; hstart.F:1244–1246; timestep.F:473–557 |

ISLIP의 2016년 KSlip→TK 변경 주석은 반대 근거로 채택했다 (`vsmy.F:942,1008,1013`; `nodalattr.F:2570–2572`). 따라서 VSSOL 노트의 낡은 E 지시는 C로 바로잡았다. 이 변경을 no-slip 바닥 응력 진단의 별도 `(a−b)/H` 후보에 그대로 적용하지 않았다.

## sonnet 수정 목록 반영 여부

| 번호 | 상태 | 처리 |
|---:|---|---|
| 1 | 묶음 A의 + 줄에 없음. 쓰기 범위 밖으로 이관 | theory §5의 `691행(11)·692행(12)·693행(13)·694행(14)`은 허용 보고서가 아니다. `wind/p15.F:1482`의 BLOWUQ, :1486–1520의 이동 소용돌이 PBL 계산, `work/makefile:249–250,453`의 p15 빌드를 확인했다. ‘자체 해법 없음’과 D를 철회하고 식 대응을 재판정해야 한다. 식 전체의 대응 판정은 이 묶음에서 수행하지 않았다. |
| 2 | 대상 밖 | EFDC Explorer의 GUI 행이다. ADCIRC 묶음 A에서 수정하지 않았다. |
| 3 | 반영 | wetdry의 기존 C를 유지했다. IT·BTIME_END 단위 불일치를 별도 E 후보로 추가했다. hstart의 초 단위 구성과 timestep의 timeloc 비교를 근거로 썼다. |
| 4 | 묶음 A의 + 줄에 없음. 쓰기 범위 밖으로 이관 | theory §5 `B27(1015행)`의 Duv 근거는 허용 보고서 밖이다. `adcirc_theory_2004_12_08.pdf/p001-018.md:27`에서 PDF p.15의 Duv 정의를 확인했다. 해당 행의 :15(PDF p.3)를 :27로 고칠 필요가 있다. |
| 5 | 대상 밖 | EFDC의 식 5.13이다. 수정하지 않았다. |
| 6 | 해당 변수명 줄 없음 | station 근거로 nodal 변수명을 판정한 해당 행은 이 묶음의 + 줄에 없다. 유사 유형인 대표 노트의 L598·L609 후보에는 fort.45·fort.44 nodal 연결과 쓰기 근거를 보완했다. |
| 7 | 반영 | XDMF 종료 판단은 xdmfio.F:329–341의 min 식과 출력 창 조건으로 정정했다. np 대 np_g는 ‘조건부, 미확인’으로 좁혔다. outputs 보고서는 쓰기 허용 대상이 아니므로 별도 이관했다. |
| 8 | 대상 밖 | EFDC의 TOXS/DYES 초기값이다. 수정하지 않았다. |
| 9 | 해당 단위 줄 없음 | subgrid 단위를 :67 주석으로 판정한 해당 행은 이 묶음의 + 줄에 없다. `subgridLookup.F:375`의 eta2 비교를 확인했다. 이 근거를 wetFracVertTab의 물리 의미를 확인하는 데 사용했다. 다른 노트·inputfiles 보고서는 수정하지 않았다. |
| 10 | 반영 | wind.F:243–244의 두 0.d0 기본값을 추가했다. adcirc.F:358–363의 초기화 직후 호출까지 보완했다. K35 보고서도 같은 내용을 반영했다. |
| 11 | 대상 밖 | SFINCS의 누적 강수 중복이다. 수정하지 않았다. 이 묶음의 EOS·TVW·호출 순서 중복은 별도로 통합했다. |
| 12 | 반영 | 정확히 ‘2.7의’라는 문자열은 대상 + 줄에 없었다. 같은 유형의 ‘254·255행의 E’, ‘343·348행’, ‘D32’, ‘4절 C25’를 보고서 행 ID나 정본 링크로 바꿨다. |
| 13 | 대상 밖 | EFDC mhkpwr.f90의 후보이다. 수정하지 않았다. |

## 쓰기 범위 때문에 남긴 보고서 정정 사항

| 위치 | 필요한 후속 반영 | 이번 처리 |
|---|---|---|
| theory §5 691–694행의 HURWIN/PBL 묶음 | p15 보조 프로그램을 대조 대상으로 추가한다. D와 자체 해법 부재 결론을 철회한다. Blain 식과의 대응은 별도로 판정한다. | 쓰기 허용 보고서가 아니므로 미수정. |
| theory §5 B27 | Duv 정의의 판독 기록 줄을 :15에서 :27로 바꾼다. | 쓰기 허용 보고서가 아니므로 미수정. |
| outputs §5 L952·L1501 | 최종화는 min 식 구조로 근거를 교체한다. np 대 np_g는 조건부·미확인으로 좁힌다. | 대표 노트만 정정했다. 보고서는 미수정. |
| outputs §5 L598·L609 | station과 nodal 근거를 나눠 인용한다. | 대표 노트에 nodal 연결·저장을 보완했다. 보고서는 미수정. |
| fort15 §5 L759 | legacy 상세 READ의 #else 및 DEBUG_WARN_ELEV 정의 조건을 근거에 명시할 수 있다. | 분류 E는 유지했다. 다른 묶음의 fort-files-reference에도 걸리는 공용 행은 수정하지 않았다. |
| features §5 W10·W19·W23·K07 | 검색 결과의 열거에 control·XDMF 제어정보 재기록을 포함할 수 있다. 상태 전환 미사용 결론 A는 유지한다. | 분류 변경이 없어 노트의 검색 설명만 보완했다. |

위 이관 사항은 묶음 A의 365줄 대조 완료와 구분한다. 다른 모델·다른 노트·쓰기 비허용 보고서로 범위를 확장하지 않았다.

## 전 줄 대조 기록

‘유지’는 추가 정정이 필요 없다는 뜻이다. ‘형식’은 빈 줄·메타데이터·제목·표 구조를 확인했다는 뜻이다. ‘근거’는 해당 줄에 인용된 원문 위치이다. 새로 보강한 원문은 위 정정·보완 목록에 적었다. 숫자가 있는 도식 줄은 연결된 원문 주석과 같은 호출 경로로 대조했다.

### adcirc-3d-mode.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 25 | 유지 | src/timestep.F:2163,2169,2172,2174,2176,2306,2309,2313,2331,2340–2341 |
| 27 | 유지 | src/vsmy.F:1019,1021,1023,1025 |
| 37 | 유지 | src/cstart.F:348,350; src/couple2baroclinic3D.F:134,137,139,141,144–148,151–152,154,157,161,163,165 |
| 41 | 유지 | src/read_input.F:3086,3091,3093–3095; docs/technical_reference/input_files/fort11.rst:20 |
| 42 | 정정 | src/couple2baroclinic3D.F:193,210,213,215,222–223,226–228,244,246; src/read_input.F:882 |
| 43 | 정정 | src/couple2baroclinic3D.F:128–129,253,255,257,267,269,499,501–503,509,511 |
| 48 | 형식 | 빈 줄 |
| 49 | 유지 | src/read_input.F:1190–1191,1222–1224,1233,1267,1270–1271,1274,1277–1279; docs/user_guide/model_configuration/model_parameters/im.rst:88–89,95 |
| 50 | 유지 | src/read_input.F:1205–1206,1208,1213–1214,1217,1233,1274,1277,1279,1372–1373 |
| 51 | 유지 | src/read_input.F:5528–5529,5535–5538,5550,5558,5570–5571,5607,5613–5615 |
| 52 | 유지 | src/cstart.F:839–840,863–864,879–880; docs/technical_reference/parameter_definitions/index.rst:1648,1653,1658,1663,1668,1673 |
| 53 | 유지 | src/cstart.F:907–910,927–929; docs/technical_reference/input_files/fort38.rst:45–50 |
| 54 | 유지 | src/cstart.F:900,905–910,920,925–929; docs/technical_reference/parameter_definitions/index.rst:1692; docs/technical_reference/input_files/fort38.rst:45–48; src/transport.F:134,466–469,495–497,1076–1080 |
| 55 | 유지 | src/couple2baroclinic3D.F:136–148,151–165,588–598,1134–1137; docs/technical_reference/input_files/fort11.rst:3; src/nodalattr.F:2452,2828; src/gwce.F:1292–1298 |
| 56 | 유지 | src/cstart.F:1027–1028; src/write_output.F:3040 |
| 57 | 유지 | src/timestep.F:2332,2340,2345; src/mesh.F:1662 |
| 58 | 유지 | src/timestep.F:2282,2345,2352; src/vsmy.F:1021,1023,1025 |
| 59 | 유지 | src/timestep.F:2341,2345,2352; src/vsmy.F:1021,1023,1025 |
| 60 | 유지 | src/timestep.F:2169–2174,2352; src/couple2baroclinic3D.F:136–141,1107–1109,1134–1135 |
| 61 | 유지 | src/timestep.F:2309,2311–2313,2315–2317 |
| 62 | 유지 | src/timestep.F:2304–2306,2344–2345 |
| 63 | 형식 | 빈 줄 |
| 93 | 유지 | src/cstart.F:835,860–862,875–878,940–941 |
| 94 | 유지 | src/cstart.F:835,875–878,890–891,900,920 |
| 104 | 유지 | src/vsmy.F:3961,3964,4362–4366 |
| 106 | 유지 | src/vsmy.F:4387; src/constants.F90:49 |
| 110 | 형식 | 빈 줄 |
| 111 | 유지 | src/timestep.F:2156,2159,2166–2167,2170,2174,2309,2313,2340–2341 |
| 112 | 유지 | src/timestep.F:2166–2167,2174,2178,2272–2273,2309,2311,2313–2316,2340–2341,2345 |
| 113 | 유지 | src/timestep.F:2167,2174; src/vsmy.F:4390; src/constants.F90:49,52 |
| 114 | 유지 | src/timestep.F:2174,2313,2340–2341; src/vsmy.F:4338,4376,4381,4386–4387,4390; docs/technical_reference/parameter_definitions/index.rst:1710 |
| 115 | 유지 | src/vsmy.F:4335,4375–4387,4409–4420; docs/technical_reference/parameter_definitions/index.rst:1710 |
| 116 | 유지 | src/vsmy.F:3961,4362–4364 |
| 117 | 유지 | src/timestep.F:2169–2174,2176 |
| 118 | 보완 | src/vsmy.F:4345–4346,4348–4349,4351–4352,4354–4355 |
| 119 | 형식 | 빈 줄 |
| 120 | 형식 | 절 제목과 아래 대상 줄의 연결 |
| 121 | 형식 | 빈 줄 |
| 122 | 유지 | external-results-ad.md의 F17·F19·C33 원문 판정과 인용 범위 |
| 123 | 형식 | 빈 줄 |
| 124 | 보완 | src/vsmy.F:3964,4364–4366 |
| 125 | 형식 | 빈 줄 |
| 126 | 정정 | src/vsmy.F:3964,4364–4366 |
| 127 | 형식 | 빈 줄 |
| 128 | 정정 | src/vsmy.F:3960–3967,4338,4362–4368 |
| 129 | 형식 | 빈 줄 |
| 130 | 정정 | src/vsmy.F:3964,4364–4366 |
| 131 | 형식 | 빈 줄 |
| 145 | 유지 | src/vsmy.F:1187–1190,1192,1196–1197; src/global_3dvs.F:482–483 |
| 146 | 유지 | src/timestep.F:1073,1143; src/vsmy.F:1200–1202,1213–1214; src/gwce.F:1197,1286; src/global_3dvs.F:488–490 |
| 164 | 유지 | src/timestep.F:813,852,855,1073,1143,2172,2174; src/vsmy.F:1546,1549–1555,1632 |
| 227 | 유지 | src/cstart.F:1027–1028; src/read_input.F:5903–5904; docs/technical_reference/parameter_definitions/index.rst:1475; src/write_output.F:3040,3508–3509,3511,3515,3520,3529,3538,3546–3547 |

### adcirc-3d-vssol-vertical-scheme.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 66 | 유지 | src/timestep.F:599–600; src/vsmy.F:997–998,1000,1002,1010,1015; docs/technical_reference/parameter_definitions/index.rst:1287,1289,1291; src/nodalattr.F:2555–2556,2559,2571–2572 |
| 70 | 형식 | 빈 줄 |
| 71 | 유지 | src/timestep.F:599–600; src/vsmy.F:1010,1015; src/nodalattr.F:2559,2571–2572 |
| 72 | 형식 | 빈 줄 |
| 88 | 유지 | src/timestep.F:594,599–600; src/vsmy.F:997,1002,1009–1010,1014–1015; src/nodalattr.F:2572; src/wetdry.F:473,482–484 |
| 91 | 형식 | 빈 줄 |
| 92 | 정정 | src/timestep.F:594,599–600; src/vsmy.F:1009–1010,1014–1015; src/nodalattr.F:2572; src/wetdry.F:483–484 |
| 93 | 형식 | 빈 줄 |

### adcirc-baroclinic-coupling.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 28 | 형식 | 빈 줄 |
| 29 | 유지 | docs/user_guide/special_features/adcirc2d_plus.rst:22–23 |
| 30 | 정정 | src/couple2baroclinic3D.F:137,139; docs/user_guide/special_features/adcirc2d_plus.rst:48 |
| 31 | 유지 | src/couple2baroclinic3D.F:1068,1107–1109,1111–1113,1134–1135; docs/user_guide/special_features/adcirc2d_plus.rst:37,48 |
| 32 | 유지 | src/read_input.F:902,926–928,931–932; docs/user_guide/special_features/adcirc2d_plus.rst:94 |
| 33 | 유지 | src/couple2baroclinic3D.F:1057,1127 |
| 34 | 유지 | src/couple2baroclinic3D.F:1095–1099 |
| 35 | 유지 | src/couple2baroclinic3D.F:1140–1142,1144–1145 |
| 36 | 유지 | src/couple2baroclinic3D.F:1068,1107–1109,1111–1113,1134–1135; docs/user_guide/special_features/adcirc2d_plus.rst:37,48 |
| 37 | 형식 | 빈 줄 |
| 41 | 유지 | src/couple2baroclinic3D.F:193,210,213,215,222–223,226–228,244,246 |
| 48 | 유지 | src/couple2baroclinic3D.F:151–152,154,499,509,511 |
| 51 | 유지 | src/couple2baroclinic3D.F:128–129,253,255,257,267,269,499,501–504,506–507 |
| 67 | 유지 | src/couple2baroclinic3D.F:1057,1068,1095–1101,1107–1109,1132,1134; docs/user_guide/special_features/adcirc2d_plus.rst:37,48 |
| 68 | 보완 | src/couple2baroclinic3D.F:151–152,157,161,163,165,1132,1136–1137; src/nodalattr.F:2619,2656,2661,2666,2670,2673,2687,2694–2695 |
| 69 | 형식 | 빈 줄 |
| 70 | 형식 | 빈 줄 |
| 71 | 유지 | src/nodalattr.F:2658–2659,2725,2736–2737,2739,2741; docs/user_guide/special_features/adcirc2d_plus.rst:55 |
| 72 | 유지 | src/nodalattr.F:2658–2659,2687,2730–2735; docs/user_guide/special_features/adcirc2d_plus.rst:57–60; src/internaltide.F90:67–68 |
| 73 | 유지 | src/couple2baroclinic3D.F:151–152,155,157–158,161,163,165 |
| 74 | 유지 | src/couple2baroclinic3D.F:145–146,148,151–152,155,157–158,161,163,165,1136–1137; src/nodalattr.F:2656,2673,2739 |
| 86 | 형식 | 절 제목과 아래 대상 줄의 연결 |
| 87 | 형식 | 빈 줄 |
| 88 | 정정 | external-results-ad.md의 F17·F19·C33 원문 판정과 인용 범위 |
| 89 | 형식 | 빈 줄 |
| 90 | 정정 | external-results-ad.md의 F17·F19·C33 원문 판정과 인용 범위 |
| 91 | 형식 | 빈 줄 |
| 92 | 정정 | src/vsmy.F:3960–3967,4362–4368 |
| 93 | 형식 | 빈 줄 |
| 94 | 정정 | src/vsmy.F:3961,4338,4362–4364 |
| 95 | 형식 | 빈 줄 |
| 96 | 정정 | external-results-ad.md의 F17·F19·C33 원문 판정과 인용 범위 |
| 97 | 형식 | 빈 줄 |
| 98 | 정정 | 절 제목과 아래 대상 줄의 연결 |
| 99 | 형식 | 빈 줄 |
| 100 | 정정 | src/vsmy.F:4362–4368 |
| 101 | 형식 | 빈 줄 |
| 102 | 정정 | 표 머리글과 후보 행의 열 대응 |
| 103 | 정정 | 표 구분선의 열 수 |
| 104 | 정정 | src/vsmy.F:3964,4362–4368 |
| 105 | 형식 | 빈 줄 |
| 109 | 유지 | src/couple2baroclinic3D.F:1132,1136–1137; src/nodalattr.F:2619,2656,2687,2694–2695 |

### adcirc-baseline-anatomy.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 11 | 형식 | 검증 일자 메타데이터 |
| 99 | 형식 | 빈 줄 |
| 100 | 형식 | 절 제목과 아래 대상 줄의 연결 |
| 101 | 형식 | 빈 줄 |
| 102 | 보완 | 정적 판독 범위와 뒤의 E 후보 표 |
| 103 | 형식 | 빈 줄 |
| 104 | 형식 | 표 머리글과 후보 행의 열 대응 |
| 105 | 형식 | 표 구분선의 열 수 |
| 106 | 정정 | src/vsmy.F:3964,4362–4368 |
| 107 | 정정 | src/read_input.F:2746–2749,2751–2753,2768–2770,2820; docs/technical_reference/input_files/fort25.rst:8 |
| 108 | 유지 | src/read_input.F:1782–1784,2568,2693; docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:331; src/wind.F:1472–1473,1914–1916,2622–2624 |
| 109 | 유지 | src/read_input.F:2322–2323,2327,2599,2605–2606; docs/user_guide/model_configuration/meteorological_forcing/moteorological_parameter_line.rst:838–839 |
| 110 | 유지 | docs/technical_reference/parameter_definitions/index.rst:2864; src/wind.F:367,371–372,380,391,394,738,749,767 |
| 111 | 유지 | src/cstart.F:105–117; src/read_input.F:489–492,494; docs/technical_reference/parameter_definitions/index.rst:2934; src/subdomain.F:44; src/global.F:1601–1635; prep/subprep.F:42–100 |
| 112 | 유지 | src/read_input.F:574–579,4132,4276,4279–4280,4285; docs/technical_reference/parameter_definitions/index.rst:2989 |
| 113 | 유지 | src/read_input.F:1775–1776,1796–1799,1829–1830; docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:210–211; src/owiwind_netcdf.F:326–328 |
| 114 | 정정 | src/timestep.F:1307,1310,1313; src/read_input.F:809–810,818,830,985,991–992; docs/technical_reference/parameter_definitions/index.rst:266 |
| 115 | 유지 | docs/technical_reference/parameter_definitions/index.rst:105,107; src/mesh.F:446,551,554,2071–2100; prep/read_global.F:225–230 |
| 116 | 유지 | src/nodalattr.F:467,686–688,905–907,916–936,954–955,1278–1280,1353–1355 |
| 117 | 유지 | src/nodalattr.F:255,1321–1322,2656,2661,2663–2664,2681–2684 |
| 118 | 유지 | docs/technical_reference/parameter_definitions/index.rst:113; src/mesh.F:446,1405; src/boundaries.F:353–354 |
| 119 | 정정 | src/weir_boundary.F90:1133–1135,1140–1142,1433–1444; docs/technical_reference/input_files/time_varying_weirs.rst:40,45,49 |
| 120 | 유지 | src/weir_boundary.F90:154–158,1328–1331,1359–1362,1382–1386,1439–1444; docs/technical_reference/input_files/time_varying_weirs.rst:50; raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/schedule-file/index.md:418 |
| 121 | 유지 | src/mesh.F:4404–4406,4414–4418,4773–4775,4777,4791–4793,4795; docs/technical_reference/input_files/fortrotm.rst:34–36 |
| 122 | 유지 | src/wind.F:4113–4114,4187,4195–4196; docs/technical_reference/input_files/fort200.rst:81; src/io.F90:100–101 |
| 123 | 유지 | src/wind.F:3411,4113–4114,4165,4209,4227–4228; docs/technical_reference/input_files/fort200.rst:84,101 |
| 124 | 유지 | src/owiwind.F:508–510,512–517,519,940–943,1134,1144–1145 |
| 125 | 유지 | docs/technical_reference/parameter_definitions/index.rst:63; src/mesh.F:482–487,490–491; prep/read_global.F:239–241,249–251,253 |
| 126 | 유지 | src/wind.F:3400–3401; prep/prep.F:3416; docs/technical_reference/input_files/fort22.rst:214 |
| 127 | 유지 | src/mesh.F:72; src/globalio.F:852; docs/technical_reference/output_files/fort61.rst:16–17; prep/post.F:1353 |
| 128 | 유지 | src/timestep.F:1639; src/write_output.F:1219,1222,2080–2082; src/globalio.F:852; docs/technical_reference/output_files/fort83.rst:23 |
| 129 | 유지 | src/cstart.F:1031,1036,1041–1043,1081–1082,1085–1086; docs/technical_reference/parameter_definitions/index.rst:2250 |
| 130 | 유지 | src/write_output.F:6245,6248,6411–6415; docs/technical_reference/output_files/everdried63.rst:12 |
| 131 | 유지 | src/write_output.F:1515,1523,1528,1531–1532,1633–1634,1662–1663,1672,2000,6296,6301; src/globalio.F:568–571; docs/technical_reference/output_files/endrisinginun63.rst:18 |
| 132 | 유지 | src/write_output.F:1861–1862,1921; src/globalio.F:1464–1465,1467–1468; docs/technical_reference/output_files/nodecode63.rst:18; docs/technical_reference/output_files/noff100.rst:17 |
| 133 | 유지 | src/write_output.F:697,709,4717–4718; src/mesh.F:72; src/globalio.F:850; docs/technical_reference/output_files/noff100.rst:21–22 |
| 134 | 유지 | docs/technical_reference/parameter_definitions/index.rst:58,492; src/netcdfio.F90:4095–4096,4098,4100,4103,4105,4110,9691–9693,9712,9721,9805,9811,9840,9853,9990,10019–10020,10029,10032,10455–10458 |
| 135 | 유지 | src/wind.F:917,948; docs/technical_reference/input_files/fort22.rst:102–103,135,137; src/netcdfio.F90:1273–1276,2475,2588,3124,4549–4550,4552–4553 |
| 136 | 유지 | src/wind.F:1396–1397,1399,1727,1729; src/netcdfio.F90:1299,1302,2718,2722,5073–5074; docs/technical_reference/output_files/fort93.rst:28 |
| 137 | 보완 | docs/technical_reference/parameter_definitions/index.rst:2734; src/write_output.F:3157; src/global_3dvs.F:109,272; src/netcdfio.F90:830,835–837,1685,1690–1691,4388,4397–4398 |
| 138 | 유지 | src/write_output.F:6363–6364; src/netcdfio.F90:3341,3344–3345,3351,3383–3384,5031–5032; docs/technical_reference/output_files/inundationtime63.rst:9 |
| 139 | 유지 | src/write_output.F:6372–6373; src/netcdfio.F90:3395,3405–3406,3409–3410,3438,3440; docs/technical_reference/output_files/maxinundepth63.rst:4 |
| 140 | 정정 | src/write_output.F:6248,6411–6413,6415; docs/technical_reference/output_files/everdried63.rst:12; src/netcdfio.F90:3505,3518,3525,3548,5034–5035 |
| 141 | 유지 | src/netcdfio.F90:2678–2680,4640–4643,5073–5074; docs/technical_reference/output_files/fort77.rst:4 |
| 142 | 보완 | docs/technical_reference/parameter_definitions/index.rst:2704,2709,2714; src/netcdfio.F90:700,715,732,1570,1582,1595,4344–4345,4348–4349,4351–4352,4356–4358,4361–4362,4370–4372,4375–4376,10455,10458 |
| 143 | 정정 | src/write_output.F:484–485,1861–1862,4310–4312,4348–4349; src/xdmfio.F:151,154,166,173–175,178,264–265,269–270,284–285,329–332,335,338,340,351,359–361,369–370,375 |
| 144 | 유지 | prep/post.F:1924,1938,2993,3007,4610,4644; docs/technical_reference/output_files/fort43.rst:15 |
| 145 | 유지 | src/write_output.F:3524–3525,3528–3529; prep/post.F:4292–4293,4305,4336–4338; docs/technical_reference/output_files/fort41.rst:21,38 |
| 146 | 유지 | src/write_output.F:5153,5156,5158,5174,5186,5204,5220,5255,5305; prep/post.F:3454–3456,3616,3649,4023,4026,4155 |
| 147 | 유지 | src/writer.F:559,665–666,674–675,679,683–685 |
| 148 | 유지 | src/vsmy.F:3571–3574,3617,3619,5285,5293–5294; src/global_3dvs.F:417–418,488–489; docs/technical_reference/input_files/fort6768.rst:64 |
| 149 | 유지 | src/vsmy.F:995,1187–1190,1196; src/global_3dvs.F:193–195; read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p019-036.md:27; read/ADCIRC/manuals/pdfs/1992_Luettich02.pdf/p019-036.md:24; read/ADCIRC/manuals/pdfs/adcirc_theory_2004_12_08.pdf/p055-072.md:16 |
| 150 | 유지 | src/nodalattr.F:1825–1826,1830,1924,1989,2149,2153,2159; docs/user_guide/model_configuration/model_parameters/tau0.rst:35–37 |
| 151 | 유지 | src/vsmy.F:1986,1989–1990,2004–2007,2022; docs/technical_reference/parameter_definitions/index.rst:1410,1414,1416 |
| 152 | 정정 | src/weir_boundary.F90:1097,1133–1135,1140–1142,1163; docs/technical_reference/input_files/time_varying_weirs.rst:40,43–50 |
| 153 | 유지 | src/nodalattr.F:2481–2483,2487–2488,2562,2566 |
| 154 | 유지 | src/vew1d.F90:150–151,156,159,161,170–171,189; docs/user_guide/special_features/vertical_element_walls.rst:77 |
| 155 | 정정 | src/vsmy.F:4335,4361,4375–4387,4409–4420; docs/technical_reference/parameter_definitions/index.rst:1710 |
| 156 | 정정 | src/vew1d.F90:328–329,350–352; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:80,82 |
| 157 | 보완 | src/wind.F:7715–7716,7729–7731,7827–7828,7830–7831 |
| 158 | 정정 | src/couple2swan.F:1153,1210–1218; thirdparty/swan/swancom1.ftn:7236–7240; thirdparty/swan/swancom2.ftn:1542 |
| 159 | 유지 | src/wind.F:1142,1157,1164–1165; docs/technical_reference/input_files/fort22.rst:135,137; src/netcdfio.F90:1267–1271,1273–1274 |
| 160 | 유지 | src/mesh.F:1205–1206,1216,1237–1238,1240,1249–1250,1255–1256,1261,1300–1301 |

### adcirc-boundary-conditions.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 62 | 형식 | 빈 줄 |
| 63 | 유지 | src/read_input.F:1687; src/nodalattr.F:547,1560–1562; docs/technical_reference/input_files/fort13.rst:338; src/sponge_layer.F90:297,319–326,332–334,362–368,370–395 |
| 64 | 유지 | docs/technical_reference/input_files/fort13.rst:336; src/sponge_layer.F90:78–80,130,132–133,138; src/momentum.F:745–746,751–752,789–791,793–794 |
| 65 | 유지 | src/nodalattr.F:547,1555–1556,1560–1562; docs/technical_reference/input_files/fort13.rst:338; src/sponge_layer.F90:297,334 |
| 66 | 유지 | docs/technical_reference/input_files/fort13.rst:340; src/sponge_layer.F90:370–372,377–378,384–385,392–393 |
| 67 | 정정 | src/nodalattr.F:1555; docs/user_guide/examples/idealized_channel.rst:66–68 |
| 68 | 유지 | src/sponge_layer.F90:297,333–334,362–364,367 |
| 69 | 유지 | src/sponge_layer.F90:374–375,379–380,386–387,394 |
| 70 | 유지 | src/sponge_layer.F90:78–80,130,132–133 |
| 71 | 유지 | src/sponge_layer.F90:78,191–192,196,203–204,208–209 |
| 72 | 유지 | src/sponge_layer.F90:718–721,725,735–737,747 |
| 73 | 유지 | src/momentum.F:745–746,751–752,789–791,793–794 |
| 74 | 형식 | 빈 줄 |

### adcirc-gwce-implementation.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 20 | 형식 | 빈 줄 |
| 21 | 유지 | src/read_input.F:2505–2506; docs/technical_reference/parameter_definitions/index.rst:531; src/nodalattr.F:1979,1981–1982,2190,2194–2195,2213,2215; docs/user_guide/model_configuration/model_parameters/tau0.rst:270–271 |
| 22 | 유지 | src/read_input.F:2521–2522,2528–2529,2535; src/gwce.F:538,1256 |
| 23 | 유지 | src/read_input.F:3010; src/nodalattr.F:2471; src/gwce.F:516,1540,1543; docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:46 |
| 24 | 유지 | src/read_input.F:2505–2506; src/nodalattr.F:1981–1982 |
| 25 | 유지 | src/read_input.F:1360; src/gwce.F:501–502,505–507,512–513; src/global.F:558; docs/user_guide/model_configuration/tides/ali_dispersion_conrtol.rst:47–48 |
| 26 | 유지 | src/read_input.F:861–862 |
| 27 | 형식 | 빈 줄 |
| 57 | 유지 | src/gwce.F:2009,2011–2014,2016 |
| 98 | 정정 | src/gwce.F:2000,2003,2009,2011–2014,2016,3070 |
| 105 | 유지 | src/read_input.F:2505–2506; src/nodalattr.F:1977,1979,1981–1982 |

### adcirc-momentum-implementation.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 59 | 유지 | src/nodalattr.F:2619,2656,2755,2757,2762–2764,2777–2779,2818,2822,2838–2839; src/momentum.F:770–771 |
| 67 | 유지 | src/read_input.F:1485; src/nodalattr.F:2025,2030,2035,2440,2818,2822,2825,2828 |
| 68 | 유지 | src/nodalattr.F:2468–2472 |
| 72 | 형식 | 빈 줄 |
| 73 | 유지 | src/read_input.F:3168; src/nodalattr.F:2472,2818,2822,2828 |
| 74 | 형식 | 빈 줄 |
| 77 | 정정 | src/timestep.F:1073,1107; src/gwce.F:427,437–439,442–443,445,516,538; src/momentum.F:751 |
| 79 | 유지 | src/timestep.F:594,599,813,1127,1143; src/momentum.F:125 |
| 80 | 형식 | 빈 줄 |
| 81 | 형식 | 빈 줄 |
| 82 | 유지 | src/gwce.F:442–443,445,516,538; src/momentum.F:751 |

### adcirc-nffr-periodic-flux-boundary.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 31 | 유지 | src/cstart.F:198,206,208,210,213,226,233,239,248 |

### adcirc-parallel-implementation.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 73 | 유지 | src/messenger.F90:350–351,357,365,376,390,404,418,455,463,469–470,472,480,488 |
| 107 | 형식 | 빈 줄 |
| 108 | 유지 | src/messenger.F90:339,348,351,355,358,363–364,366,370,379,384,393,398,407,412,421,429,431,448,456–457,464–465,471,475,479,483,487,491; docs/technical_reference/input_files/fort18.rst:9 |
| 109 | 형식 | 빈 줄 |
| 134 | 유지 | src/gwce.F:185,188–189,200,204,216,220,1869,1871,1873–1874,1876,1879,2030–2031 |
| 220 | 유지 | wind/aswip.F:2935,2939–2940 |
| 233 | 유지 | src/timestep.F:1246,1310–1311,1333,1417,1472–1473; src/wetdry.F:1452,1458–1459; src/messenger.F90:1388 |

### adcirc-timestep-orchestration.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 22 | 정정 | src/adcirc.F:475–476,478,481–482,492 |
| 30 | 유지 | src/timestep.F:468,519 |
| 33 | 유지 | src/timestep.F:646–647 |
| 37 | 유지 | src/timestep.F:852,855,859 |
| 40 | 유지 | src/timestep.F:1078–1095 |
| 46 | 유지 | src/timestep.F:1200–1204,1209,1215 |
| 47 | 유지 | src/adcirc.F:485–486,488,492 |
| 51 | 형식 | 빈 줄 |
| 52 | 정정 | src/timestep.F:648–649; src/read_input.F:769–772; src/gwce.F:2007; docs/user_guide/special_features/dynamic_water_level_correction.rst:14–18 |
| 53 | 유지 | src/read_input.F:765; src/wind.F:240; docs/user_guide/special_features/dynamic_water_level_correction.rst:39–41 |
| 54 | 보완 | src/wind.F:7715–7716,7729–7731,7827–7828,7830–7831 |
| 55 | 유지 | src/wind.F:7884,7892,7896 |
| 56 | 형식 | 빈 줄 |
| 84 | 유지 | src/timestep.F:1073,1107; src/gwce.F:427,437–439,442–443,445,516,538; src/momentum.F:751 |
| 88 | 형식 | 빈 줄 |
| 89 | 정정 | src/gwce.F:442–443,445,516,538; src/momentum.F:751 |
| 90 | 형식 | 빈 줄 |
| 95 | 유지 | src/timestep.F:1153,1155,1630–1634,1668,1834 |
| 97 | 유지 | src/timestep.F:1923,1925,1927,1931,1933,1974,1977,1979,1983–1984; src/couple2baroclinic3D.F:137,139 |
| 103 | 유지 | src/timestep.F:1078–1079,1081,1083,1089,1092 |
| 107 | 유지 | src/timestep.F:1078–1079,1083,1092,1107 |
| 108 | 유지 | src/timestep.F:397–398,400,402,411–412,655,728–729,845; src/gwce.F:1154–1155,1181–1182,1395,1697–1698,1701; src/momentum.F:401,445,726 |
| 117 | 유지 | src/gwce.F:2000,2003,2011–2014,2016,3070 |
| 120 | 형식 | 빈 줄 |
| 121 | 정정 | src/read_input.F:3010; src/nodalattr.F:2471; src/gwce.F:516,1540,1543; docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:46 |
| 122 | 유지 | docs/user_guide/special_features/dynamic_water_level_correction.rst:30–32 |
| 123 | 형식 | 빈 줄 |
| 132 | 유지 | src/adcirc.F:475–476,478,481–482,492 |
| 152 | 유지 | src/netcdfio.F90:7904; src/hstart.F:47 |
| 153 | 유지 | src/hstart.F:673–674 |
| 169 | 유지 | src/adcirc.F:417 |
| 170 | 유지 | src/adcirc.F:475,485,487 |
| 185 | 유지 | src/sponge_layer.F90:642,752 |
| 186 | 유지 | src/timestep.F:427,429,432,444 |
| 187 | 유지 | src/timestep.F:55; src/globalio.F:1661 |
| 188 | 유지 | src/timestep.F:519,521,531 |
| 199 | 유지 | src/timestep.F:1511 |
| 200 | 유지 | src/timestep.F:813,845,1521 |
| 202 | 유지 | src/weir_boundary.F90:1726 |
| 203 | 유지 | src/timestep.F:966,982,1030 |
| 205 | 유지 | src/weir_boundary.F90:1949 |
| 206 | 유지 | src/timestep.F:973,979,982 |
| 207 | 유지 | src/weir_boundary.F90:1774,2181 |
| 208 | 유지 | src/weir_boundary.F90:2468 |
| 209 | 유지 | src/timestep.F:1022,1027,1030,1033,1041 |
| 213 | 유지 | src/gwce.F:237 |
| 214 | 유지 | src/gwce.F:427,1000 |
| 216 | 유지 | src/gwce.F:237 |
| 217 | 유지 | src/gwce.F:2011–2012,2014 |
| 221 | 유지 | src/wetdry.F:140; src/subgridLookup.F:352 |
| 222 | 유지 | src/timestep.F:1078–1079,1081,1083,1092; src/wetdry.F:204 |
| 223 | 유지 | gwce.F:182–198; 바로 뒤 도식 주석의 CPRECOR 분기 |
| 224 | 유지 | src/gwce.F:182,192,198 |
| 256 | 유지 | src/timestep.F:382–383; src/vsmy.F:1184–1185; src/gwce.F:1034–1039,1189–1190,2553,2556,2559; src/momentum.F:1180–1181,1894–1895 |
| 260 | 유지 | src/timestep.F:2008–2009; src/wetdry.F:204,1363,1378; src/momentum.F:715–716,720 |
| 261 | 유지 | src/couple2baroclinic3D.F:806,809–810,813–814,817,819,822; src/nodalattr.F:2694–2695,2822,2825,2828 |
| 266 | 유지 | src/timestep.F:689–690,695–699,701,703,705–706,724,726–729; src/gwce.F:1395–1396; src/adcirc.F:478,481 |
| 267 | 유지 | src/timestep.F:855,859,1127,1143,1974,2172,2174; src/vsmy.F:1546,1632,1637,1641–1642 |
| 268 | 유지 | src/vsmy.F:1187,1189–1190,1192,1196–1197,1200–1202,1213–1215; src/gwce.F:1197,1200,1286–1289; src/global_3dvs.F:482–483,488–490 |
| 269 | 유지 | src/timestep.F:1200,1639,1693–1695,1834; src/write_output.F:5044,5046,5142,5144 |
| 270 | 형식 | 빈 줄 |
| 271 | 유지 | src/write_output.F:888–889,893,895,897–898 |
| 272 | 유지 | src/timestep.F:1974,1977,1979,1983–1984; src/couple2baroclinic3D.F:137,139 |
| 273 | 형식 | 빈 줄 |

### adcirc-weir-boundary.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 34 | 정정 | src/weir_boundary.F90:50,1750–1752,1847,1860,1862,1872,1876,1889 |
| 39 | 형식 | 빈 줄 |
| 40 | 정정 | docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:14; src/momentum.F:816 |
| 41 | 유지 | src/cstart.F:961–963; src/mesh.F:1422; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:146,151–154,159–162,167–168; docs/technical_reference/input_files/fort39.rst:6 |
| 42 | 보완 | src/mesh.F:2681–2689,2703–2707; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:210–215 |
| 43 | 유지 | src/gwce.F:1728–1730; src/mesh.F:2416; src/momentum.F:817; read/ADCIRC/manuals/pdfs/1996_Westerink03.pdf/p001-016.md:19–20 |
| 44 | 유지 | src/weir_boundary.F90:50,1750–1752; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:305,307 |
| 45 | 유지 | src/weir_boundary.F90:1750–1751,1753–1755; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:307 |
| 46 | 유지 | src/timestep.F:966,1030,1073; src/gwce.F:1619,1627; src/weir_boundary.F90:107,109,1750–1751,1862–1863; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:309–312,382–386,388 |
| 47 | 유지 | src/weir_boundary.F90:1865–1866,1876,1887,1904,1916; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:346–350,363–367 |
| 48 | 유지 | src/weir_boundary.F90:1865–1866,1887,1895,1916,1925; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:357–359,374–376 |
| 49 | 유지 | src/weir_boundary.F90:2516,2524; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:432–435 |
| 50 | 유지 | src/weir_boundary.F90:2559–2561,2569–2571; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:437,449,461–462,474 |
| 51 | 유지 | src/weir_boundary.F90:2516,2524,2533,2545,2554,2564 |
| 52 | 유지 | src/weir_boundary.F90:2398,2404–2405,2408,2413–2414; docs/user_guide/special_features/vertical_element_walls.rst:158 |
| 53 | 정정 | src/gwce.F:1947–1959; docs/user_guide/special_features/vertical_element_walls.rst:206; src/momentum.F:1058–1063 |
| 54 | 유지 | src/weir_boundary.F90:1872,2511 |
| 55 | 유지 | src/weir_boundary.F90:1842–1843,1847–1848 |
| 56 | 유지 | src/weir_boundary.F90:50,1750–1752,1876 |
| 57 | 유지 | src/weir_boundary.F90:1865,1876,1887–1888,1892–1893,1895; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:357–359 |
| 58 | 형식 | 빈 줄 |
| 61 | 유지 | src/weir_boundary.F90:258–260,2104–2106,2116–2118,2130,2141,2145,2153–2154,2157–2158 |
| 62 | 형식 | 빈 줄 |
| 63 | 형식 | 빈 줄 |
| 64 | 유지 | src/weir_boundary.F90:2362–2363,2376,2380,2383,2387,2400–2401; docs/user_guide/special_features/vertical_element_walls.rst:160 |
| 65 | 보완 | src/gwce.F:1888–1897; src/mesh.F:2625–2627; src/weir_boundary.F90:2366–2370; docs/user_guide/special_features/vertical_element_walls.rst:163 |
| 66 | 유지 | src/mesh.F:2627; prep/prep.F:1644,1724–1730; docs/user_guide/special_features/vertical_element_walls.rst:164 |
| 67 | 정정 | prep/prep.F:1724–1730; docs/user_guide/special_features/vertical_element_walls.rst:158 |
| 68 | 유지 | src/vew1d.F90:112–115,124–129,131–132 |
| 69 | 유지 | src/vew1d.F90:59–66 |
| 70 | 유지 | src/vew1d.F90:293,301,303,305–306,311–312,314–315 |
| 71 | 유지 | src/vew1d.F90:328–329,350–352; docs/user_guide/model_configuration/boundary_conditions/flux_specified_boundaries.rst:80,82 |
| 72 | 유지 | src/weir_boundary.F90:2104–2107 |
| 76 | 유지 | src/weir_boundary.F90:1133–1136,1140–1143,1741–1743,1833–1835 |
| 79 | 유지 | src/weir_boundary.F90:1095–1098,1104–1110,1117–1118 |
| 83 | 유지 | src/weir_boundary.F90:641–642,644–645,647,649–650,659 |
| 84 | 유지 | src/timestep.F:966,1030,1073,1200,1215,1224,1227–1228,1230–1231; src/weir_boundary.F90:1743,1835 |
| 85 | 형식 | 빈 줄 |
| 86 | 형식 | 빈 줄 |
| 87 | 유지 | src/weir_boundary.F90:1328–1331,1335–1336,1338–1339,1363,1367,1369–1370,1375 |
| 88 | 유지 | src/weir_boundary.F90:1097,1133–1135,1140–1142,1163; docs/technical_reference/input_files/time_varying_weirs.rst:40,43–50 |
| 89 | 유지 | src/weir_boundary.F90:1095,1105–1106,1108; docs/technical_reference/input_files/time_varying_weirs.rst:42,77–80 |
| 90 | 유지 | src/weir_boundary.F90:1565–1569,1572–1575 |

### adcirc-wetting-drying-implementation.md

| 원래 + 줄 | 결과 | 대조한 원문 또는 구조 |
|---:|---|---|
| 6 | 형식 | 검증 일자 메타데이터 |
| 40 | 유지 | CMakeLists.txt:92 |
| 41 | 형식 | 빈 줄 |
| 44 | 유지 | src/wetdry.F:126,235,241,244 |
| 49 | 형식 | 빈 줄 |
| 50 | 유지 | src/read_input.F:3021; src/wetdry.F:241 |
| 51 | 유지 | src/wetdry.F:241 |
| 52 | 유지 | src/wetdry.F:126,278 |
| 53 | 유지 | src/read_input.F:3021 |
| 54 | 유지 | src/wetdry.F:126,241,244 |
| 55 | 유지 | src/read_input.F:3020–3021; docs/technical_reference/parameter_definitions/index.rst:693; raw/source_code/adcircpy/adcircpy/fort15.py:1747–1751 |
| 56 | 유지 | src/read_input.F:3021; src/wetdry.F:127,241,370 |
| 57 | 형식 | 빈 줄 |
| 80 | 유지 | src/wetdry.F:275,280,314,845,850–853,863–864 |
| 81 | 형식 | 빈 줄 |
| 82 | 형식 | 빈 줄 |
| 83 | 유지 | src/wetdry.F:213,355,370,416,418,440,1373 |
| 84 | 유지 | src/momentum.F:1134–1137 |
| 85 | 유지 | src/wetdry.F:372,375,420,440 |
| 86 | 유지 | src/wetdry.F:371–372,375,420 |
| 87 | 유지 | src/timestep.F:877–878,1023; src/wetdry.F:813,1087 |
| 88 | 유지 | src/wetdry.F:411–414; read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md:13 |
| 89 | 유지 | src/wetdry.F:236–237,241–242,244–246 |
| 90 | 유지 | src/wetdry.F:375,377 |
| 91 | 보완 | src/wetdry.F:845,851–853,863–864 |
| 92 | 유지 | src/wetdry.F:1087–1088 |
| 93 | 유지 | src/wetdry.F:370–372,375 |
| 94 | 유지 | src/wetdry.F:375,377 |
| 95 | 유지 | src/wetdry.F:845,863–864,1087–1088 |
| 99 | 정정 | src/read_input.F:3020–3021,3025,3032 |
| 110 | 형식 | 빈 줄 |
| 111 | 보완 | src/read_input.F:3021,3025,3032; docs/technical_reference/parameter_definitions/index.rst:698; src/wetdry.F:241,440 |
| 112 | 유지 | src/wetdry.F:101,1373 |
| 113 | 유지 | src/wetdry.F:1114–1115,1373 |
| 114 | 유지 | src/read_input.F:3021–3022,3025,3032; docs/technical_reference/parameter_definitions/index.rst:698 |
| 115 | 형식 | 빈 줄 |
| 122 | 형식 | 빈 줄 |
| 123 | 유지 | src/wetdry.F:388,402–404,416–418 |
| 124 | 형식 | 빈 줄 |
| 131 | 정정 | src/read_input.F:3020–3021 |
| 144 | 유지 | src/read_input.F:3020–3021 |

## 수정 후 확인

추가한 정정·보완 표시가 있는 노트의 상대 링크와 절 앵커를 확인했다. 대표 후보 표와 수정한 보고서 행의 열 수를 확인했다. 지정 노트와 허용 보고서의 `git diff --check`가 통과했다. 원래 대상 줄 365개의 대조 기록과 노트별 집계가 일치한다. 모델 실행과 수치 재현은 하지 않았다.

정정 40, 보완 12, 분류 변경 6, 이상 없음 313

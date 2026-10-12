ShorelineS 판독 기록 전수 검증 — 2026-10-12

사용자가 지정한 기록 26개의 전체 716행을 확인했다. 각 원문 경로는 기록의 frontmatter `file:`에서 읽었다. 원문 대조 범위는 아래 표의 합계 4,005행이다. 구간 표의 154행마다 `nl -ba <원문> | sed -n 'A,Bp'`로 해당 원문을 열었다. 문자열 비교에서는 함수 원문을 ISO-8859-1로 디코딩했다.

기록 전체 행은 frontmatter, 제목, 표 머리말, 빈 줄을 포함한 물리 행 수다. 구간 행은 구간 표의 본문 행이다. 사실 행은 표 아래 사실 목록의 항목 행이다. 정정·보완·이상 없음은 구간 행과 사실 행을 합친 269개 항목의 집계다. 같은 행의 여러 변경은 한 항목으로 센다. 오류 정정과 누락 보완을 함께 반영한 행은 정정으로 센다. 보완은 누락만 추가한 행이다. 이상 없음은 대조 후 수정하지 않은 항목이다.

실행 조건과 계산식을 대조했다. 입력 필드의 기본값 대입을 대조했다. 입력 예제의 설정값과 기본값을 구분했다. 부정, 수량, 분기, 단위, 순서를 대조했다. 변수 용도에 관한 근거를 대조했다. 삭제 대상과 점 개수를 대조했다. 구간 시작 시의 바깥 블록을 대조했다. 사실 목록의 각 문장도 원문과 대조했다.

| 기록 | 기록 전체 행 | 구간 행 | 사실 행 | 원문 대조 행 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|---:|
| [functions/transport.m.md](shorelines/functions/transport.m.md) | 32 | 9 | 6 | 237 | 2 | 0 | 13 |
| [functions/transport_boundary_condition.m.md](shorelines/functions/transport_boundary_condition.m.md) | 23 | 3 | 3 | 122 | 0 | 0 | 6 |
| [functions/transport_bypass.m.md](shorelines/functions/transport_bypass.m.md) | 27 | 5 | 5 | 180 | 4 | 0 | 6 |
| [functions/transport_groynesubmerged.m.md](shorelines/functions/transport_groynesubmerged.m.md) | 23 | 3 | 3 | 79 | 2 | 0 | 4 |
| [functions/transport_mud.m.md](shorelines/functions/transport_mud.m.md) | 27 | 5 | 5 | 200 | 2 | 0 | 8 |
| [functions/transport_revetment.m.md](shorelines/functions/transport_revetment.m.md) | 31 | 7 | 7 | 228 | 2 | 0 | 12 |
| [functions/transport_shadow_treat.m.md](shorelines/functions/transport_shadow_treat.m.md) | 30 | 6 | 7 | 222 | 2 | 0 | 11 |
| [functions/transport_soulsbyvanrijn.m.md](shorelines/functions/transport_soulsbyvanrijn.m.md) | 24 | 3 | 4 | 83 | 0 | 0 | 7 |
| [functions/transport_tidewave.m.md](shorelines/functions/transport_tidewave.m.md) | 24 | 3 | 4 | 88 | 0 | 0 | 7 |
| [functions/update_bathy.m.md](shorelines/functions/update_bathy.m.md) | 25 | 4 | 4 | 108 | 2 | 0 | 6 |
| [functions/update_props.m.md](shorelines/functions/update_props.m.md) | 22 | 3 | 2 | 53 | 0 | 0 | 5 |
| [functions/update_shoreline.m.md](shorelines/functions/update_shoreline.m.md) | 25 | 4 | 4 | 116 | 1 | 0 | 7 |
| [functions/wave_angles.m.md](shorelines/functions/wave_angles.m.md) | 25 | 4 | 4 | 146 | 1 | 0 | 7 |
| [functions/wave_breakingheight.m.md](shorelines/functions/wave_breakingheight.m.md) | 26 | 4 | 5 | 130 | 1 | 0 | 8 |
| [functions/wave_cur_1D.m.md](shorelines/functions/wave_cur_1D.m.md) | 25 | 4 | 4 | 97 | 0 | 0 | 8 |
| [functions/wave_diffraction.m.md](shorelines/functions/wave_diffraction.m.md) | 69 | 33 | 19 | 928 | 7 | 0 | 45 |
| [functions/wave_diffraction_coeff.m.md](shorelines/functions/wave_diffraction_coeff.m.md) | 26 | 4 | 5 | 84 | 0 | 0 | 9 |
| [functions/wave_refraction.m.md](shorelines/functions/wave_refraction.m.md) | 25 | 4 | 4 | 110 | 0 | 0 | 8 |
| [functions/wave_shoalref.m.md](shorelines/functions/wave_shoalref.m.md) | 23 | 3 | 3 | 69 | 0 | 0 | 6 |
| [functions/wave_transmission.m.md](shorelines/functions/wave_transmission.m.md) | 26 | 4 | 5 | 100 | 1 | 0 | 8 |
| [compiled/launchShorelineS.sh.md](shorelines/compiled/launchShorelineS.sh.md) | 24 | 3 | 4 | 36 | 1 | 0 | 6 |
| [README.md.md](shorelines/README.md.md) | 19 | 1 | 0 | 4 | 0 | 0 | 1 |
| [ShorelineS-Publications.txt.md](shorelines/ShorelineS-Publications.txt.md) | 22 | 4 | 0 | 26 | 0 | 0 | 4 |
| [compiled/README.md.md](shorelines/compiled/README.md.md) | 21 | 3 | 0 | 15 | 0 | 0 | 3 |
| [compiled/input.txt.md](shorelines/compiled/input.txt.md) | 31 | 10 | 3 | 62 | 0 | 0 | 13 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md) | 41 | 18 | 5 | 482 | 5 | 12 | 6 |
| 합계 | 716 | 154 | 115 | 4005 | 33 | 12 | 224 |

정정한 행은 다음과 같다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [functions/transport.m.md](shorelines/functions/transport.m.md):85–103 | 숫자가 아닌 인수의 분기를 문자 인수로 한정했다. | isnumeric이 거짓인 분기와 strcmpi의 대소문자 비구분 비교를 그대로 적었다. | [transport.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport.m):85–96 |
| [functions/transport.m.md](shorelines/functions/transport.m.md):124–138 | 임계각 비교 대상을 양의 입사각으로 단정했다. | dPHItdp>dPHIcrit 비교이며 양수 조건은 없다고 명시했다. | [transport.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport.m):125–127 |
| [functions/transport_bypass.m.md](shorelines/functions/transport_bypass.m.md):91–120 | 투영 방향을 해안 법선으로 단정했다. | 투영각은 GROYNE.phigroyne이고 대상은 x_str·y_str의 2:end-1 점이라고 적었다. | [transport_bypass.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_bypass.m):95–99 |
| [functions/transport_bypass.m.md](shorelines/functions/transport_bypass.m.md):121–146 | 입력 필드 bypasscontrfac 자체에 하한을 둔 것으로 서술했다. | maxbypass 초기값의 하한과 그 뒤의 제한 조건을 구분했다. | [transport_bypass.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_bypass.m):129–135 |
| [functions/transport_bypass.m.md](shorelines/functions/transport_bypass.m.md):147–180 | NaN 값을 개별적으로 0으로 바꾸는 것으로 읽힐 수 있었다. | 배열 조건이 참일 때 BPF 전체를 zeros(nw,1)로 교체한다고 적었다. | [transport_bypass.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_bypass.m):155–157 |
| [functions/transport_bypass.m.md](shorelines/functions/transport_bypass.m.md):코드 사실 56 및 122–123 | nq를 계산 후 미사용 변수로 분류했다. | nq는 ibound 대입에 사용된다. 미사용인 변수는 hin·hout다. | [transport_bypass.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_bypass.m):56·75·122–123 |
| [functions/transport_groynesubmerged.m.md](shorelines/functions/transport_groynesubmerged.m.md):50–62 | Slong 최대값을 양수로, 최소값을 음수로 단정했다. | vw 조건으로 선택하는 max(Slong)와 abs(min(Slong))를 부호 단정 없이 적었다. | [transport_groynesubmerged.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_groynesubmerged.m):53–57 |
| [functions/transport_groynesubmerged.m.md](shorelines/functions/transport_groynesubmerged.m.md):63–79 | while의 절대값 비교를 수송값 비교로 요약했다. | abs(Slong)의 크기 비교와 부호 곱 조건을 명시했다. | [transport_groynesubmerged.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_groynesubmerged.m):63–64 |
| [functions/transport_mud.m.md](shorelines/functions/transport_mud.m.md):120–153 | 90도 초과 조건에서 절대값을 생략했다. | abs(WAVE.dPHItdp)>90 조건을 반영했다. | [transport_mud.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_mud.m):121 |
| [functions/transport_mud.m.md](shorelines/functions/transport_mud.m.md):154–175 | 농도 제한이 음의 농도 로그 분기 안에 있는 것으로 요약했다. QS 기울기 계산을 단위 변환으로 묶었다. | 로그 조건과 조건 밖의 C=max(C,0) 대입을 구분했다. diff(QS)./ds 계산과 qm 단위 변환을 구분했다. | [transport_mud.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_mud.m):157–160; 174–175 |
| [functions/transport_revetment.m.md](shorelines/functions/transport_revetment.m.md):129–168 | 0.05*ds0를 연장 비율로 적었다. | 끝 구간 길이로 나눈 L을 사용하므로 연장 길이는 각각 0.05*ds0라고 적었다. | [transport_revetment.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_revetment.m):131–135 |
| [functions/transport_revetment.m.md](shorelines/functions/transport_revetment.m.md):169–198 | 1e-6 비교를 QS 부호 판정으로 요약했다. QS>=0 분기를 양의 수송으로만 설명했다. | 양쪽 QS의 임계값 비교를 그대로 적었다. 0을 포함하는 분기 조건과 두 루프의 인덱스 순서를 적었다. | [transport_revetment.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_revetment.m):170–174; 184–194 |
| [functions/transport_shadow_treat.m.md](shorelines/functions/transport_shadow_treat.m.md):169–198 | 한 셀 차폐점을 찾아 제거한다고 결과를 단정했다. | 차분 배열의 find 결과를 원 배열 선형 인덱스에 사용하는 실제 대입을 적었다. | [transport_shadow_treat.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_shadow_treat.m):170–175 |
| [functions/transport_shadow_treat.m.md](shorelines/functions/transport_shadow_treat.m.md):199–222 | 계수 선택을 양·음 수송으로만 설명했다. | 기본 계수와 QS<0인 위치의 교체를 구분했다. | [transport_shadow_treat.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/transport_shadow_treat.m):202–206 |
| [functions/update_bathy.m.md](shorelines/functions/update_bathy.m.md):67–95 | 상수 100000의 용도를 최대 탐색거리로 단정했다. | 이 파일에서 확인되는 호출의 마지막 인수로 적었다. | [update_bathy.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/update_bathy.m):67–69 |
| [functions/update_bathy.m.md](shorelines/functions/update_bathy.m.md):코드 사실 48·69·85 | 상수 100000의 용도를 거리 탐색으로 서술했다. | 호출의 마지막 인수라는 코드 사실로 한정했다. | [update_bathy.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/update_bathy.m):69 |
| [functions/update_shoreline.m.md](shorelines/functions/update_shoreline.m.md):39–63 | 상수 10000의 용도를 탐색거리로 단정했다. | 이 파일에서 확인되는 호출의 마지막 인수로 적었다. | [update_shoreline.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/update_shoreline.m):50–52 |
| [functions/wave_angles.m.md](shorelines/functions/wave_angles.m.md):70–94 | 주석의 CERC1을 CERC로 적었다. | 주석에 적힌 CERC1을 그대로 구분했다. | [wave_angles.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_angles.m):85–86 |
| [functions/wave_breakingheight.m.md](shorelines/functions/wave_breakingheight.m.md):80–108 | break를 오차가 작은 경우로만 요약했다. | abs(errnew)>eps의 참 분기와 else를 그대로 구분했다. | [wave_breakingheight.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_breakingheight.m):97–105 |
| [functions/wave_diffraction.m.md](shorelines/functions/wave_diffraction.m.md):161–190 | cosd 차이의 부호를 저장한다고 적었다. | cosd(dirstr-dirm)>0의 논리 결과를 int8로 저장한다고 적었다. | [wave_diffraction.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_diffraction.m):176–185 |
| [functions/wave_diffraction.m.md](shorelines/functions/wave_diffraction.m.md):217–240 | 거리 조건을 mindist 이내로 적었다. | 원문의 < 비교에 맞춰 mindist 미만으로 적었다. | [wave_diffraction.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_diffraction.m):218–224 |
| [functions/wave_diffraction.m.md](shorelines/functions/wave_diffraction.m.md):241–270 | 양 선단을 보존하고 idgroyne=0 분기에서 지역 구조물을 갱신한다고 적었다. | 왼쪽 좌표와 기존 itip2를 보존하는 선택을 적었다. insert_section은 조건 밖이라고 명시했다. | [wave_diffraction.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_diffraction.m):242–257 |
| [functions/wave_diffraction.m.md](shorelines/functions/wave_diffraction.m.md):290–314 | idpp 거리 조건을 최대값 이내로 적었다. | distxq<max(...)의 엄격한 부등호를 반영했다. | [wave_diffraction.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_diffraction.m):299–302 |
| [functions/wave_diffraction.m.md](shorelines/functions/wave_diffraction.m.md):574–598 | 거리와 typeS로 첫 최소값 구조물을 고른다고만 적었다. | 두 열 배열의 열별 최소값 비교와 선형 인덱스 선택을 구분했다. | [wave_diffraction.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_diffraction.m):563–570·578–592 |
| [functions/wave_diffraction.m.md](shorelines/functions/wave_diffraction.m.md):727–743 | 교차 검사 선분을 선단 거리의 0.8배로 적었다. | 시작점은 0.001배 위치이고 끝점은 0.8배 위치라고 적었다. | [wave_diffraction.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_diffraction.m):729–734 |
| [functions/wave_diffraction.m.md](shorelines/functions/wave_diffraction.m.md):744–761 | 모든 가장자리는 절반 감쇠이고 내부는 완전 감쇠라고 단정했다. | 인접 논리값의 평균과 양 끝값 복제에 따라 감쇠가 정해짐을 적었다. | [wave_diffraction.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_diffraction.m):744–759 |
| [functions/wave_transmission.m.md](shorelines/functions/wave_transmission.m.md):75–83 | CHIop의 분모를 파형 경사로 적었다. | 분모는 파형 경사 Hs./Lwave의 제곱근이다. | [wave_transmission.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/wave_transmission.m):81 |
| [compiled/launchShorelineS.sh.md](shorelines/compiled/launchShorelineS.sh.md):1–10 | 백틱을 포함한 셸 대입의 닫는 구분자가 세 백틱으로 붙어 있었다. | 두 백틱 구분자를 분리하여 원문 대입이 코드 인용으로 표시되게 했다. | [launchShorelineS.sh](../../../../models/ShorelineS/raw/source_code/shorelines/compiled/launchShorelineS.sh):9 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):21–33 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. execution_count를 해당 셀의 실행 횟수로 설명했다. | 시작 시 2행 cells 배열 안. 저장된 execution_count 값 1을 그대로 적었다. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):2·21; 23·26 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):34–60 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. 코드 셀을 두 번 실행했다고 읽히는 표현을 썼다. | 시작 시 2행 cells 배열 안. 저장된 execution_count 값이 2임을 적었다. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):2·34; 34–39 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):61–88 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. 저장 로그의 fid를 파일 식별자로 단정했다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체 안. 변수명과 값만 확인되며 용도 설명은 없다고 적었다. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63; 61–69 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):324–363 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. 주석 없는 설정을 출력·평활·채움으로 분류하고 -1을 입력 종료 값으로 불렀다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. 설정값과 마지막 s 값이라는 저장 로그의 내용으로 한정했다. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·324; 324–363 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):407–424 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. execution_count를 해당 셀의 실행 횟수로 설명했다. | 시작 시 2행 cells 배열 안. 저장된 execution_count 값 null을 그대로 적었다. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):2·407; 409 |

보완한 행은 다음과 같다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):89–158 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·89 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):159–173 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·159 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):174–204 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·174 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):205–243 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·205 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):244–273 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·244 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):274–298 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·274 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):299–323 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·299 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):364–398 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 34행 코드 셀의 39행 outputs 배열·60행 stdout 출력 객체·63행 text 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):34–63·364 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):399–406 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 2행 cells 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):2·399 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):425–436 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 407행 코드 셀 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):407–425 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):437–452 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 407행 코드 셀의 425행 source 배열 안. Python 코드에서는 433행의 폴더 대기 while 밖이다(435–437). | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):407·425·433–437 |
| [ShorelineS.ipynb.md](shorelines/ShorelineS.ipynb.md):453–482 | 구간 시작 시의 바깥 JSON 블록을 표기하지 않았다. | 시작 시 2행 cells 배열 안. | [ShorelineS.ipynb](../../../../models/ShorelineS/raw/source_code/shorelines/ShorelineS.ipynb):2·453 |

노트북 원문 415행의 JPEG를 직접 열어 보았다. 원문 416행의 PNG도 직접 열어 보았다. 두 저장 그림의 축, 눈금, 날짜, 범례, 선 색, 화살표를 기록과 대조했다.

각 변경 행 끝에 요청한 정정 또는 보완 표식을 붙였다. 원문 26개의 해시는 각 기록의 frontmatter 해시와 일치했다. 구간 경계와 frontmatter는 변경하지 않았다. 단일 행 번호가 붙은 백틱 인용 1,706개는 해당 원문 행의 문자열과 일치했다. 이 문자열 검사는 인용 앞뒤 공백과 Markdown 표의 파이프 이스케이프를 제외했다. 지정된 함수 20개에서 실행 조건 또는 대입문이 있는 행은 모두 해당 구간의 원문 인용에 포함되어 있었다.

수정은 지정된 판독 기록과 이 보고서에 한정했다. 원문과 노트는 수정하지 않았다. git은 상태 조회만 했다. 모델은 실행하지 않았다.

정정 33, 보완 12, 이상 없음 224

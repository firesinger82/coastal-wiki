# Celeris code-6 전수 대조

대조 단위는 판독 기록의 구간 표 행이다. 원문 행 수에는 빈 행과 주석을 포함한다.
정정·보완은 해당 표 행 수로 집계한다. 같은 행에 두 종류가 있으면 각각 집계한다. 이상 없음은 정정·보완이 없는 완료 구간 수이다.
원문은 각 구간마다 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다. 모델은 실행하지 않았다.

| 기록 | 대조 구간 수 | 대조 원문 행 수 | 상태 |
|---|---:|---:|---|
| [SedTrans_Pass3.wgsl.md](../Celeris-WebGPU/shaders/SedTrans_Pass3.wgsl.md) | 7 | 241 | 완료 |
| [SedTrans_Pass3_old.wgsl.md](../Celeris-WebGPU/shaders/SedTrans_Pass3_old.wgsl.md) | 5 | 181 | 완료 |
| [SedTrans_Pass3_wBedUpdate.wgsl.md](../Celeris-WebGPU/shaders/SedTrans_Pass3_wBedUpdate.wgsl.md) | 8 | 255 | 완료 |
| [SedTrans_UpdateBottom.wgsl.md](../Celeris-WebGPU/shaders/SedTrans_UpdateBottom.wgsl.md) | 5 | 122 | 완료 |
| [SedTrans_UpdateBottom_testing.wgsl.md](../Celeris-WebGPU/shaders/SedTrans_UpdateBottom_testing.wgsl.md) | 4 | 90 | 완료 |
| [Ship_pressure.compute.md](../Celeris-WebGPU/shaders/Ship_pressure.compute.md) | 4 | 81 | 완료 |
| [TriDiag_PCRx.wgsl.md](../Celeris-WebGPU/shaders/TriDiag_PCRx.wgsl.md) | 4 | 107 | 완료 |
| [TriDiag_PCRx_COULWAVE.wgsl.md](../Celeris-WebGPU/shaders/TriDiag_PCRx_COULWAVE.wgsl.md) | 4 | 116 | 완료 |
| [TriDiag_PCRy.wgsl.md](../Celeris-WebGPU/shaders/TriDiag_PCRy.wgsl.md) | 4 | 110 | 완료 |
| [TriDiag_PCRy_COULWAVE.wgsl.md](../Celeris-WebGPU/shaders/TriDiag_PCRy_COULWAVE.wgsl.md) | 4 | 119 | 완료 |
| [Update_TriDiag_coef.wgsl.md](../Celeris-WebGPU/shaders/Update_TriDiag_coef.wgsl.md) | 4 | 111 | 완료 |
| [Update_TriDiag_coef_COULWAVE.wgsl.md](../Celeris-WebGPU/shaders/Update_TriDiag_coef_COULWAVE.wgsl.md) | 4 | 117 | 완료 |
| [Update_neardry.wgsl.md](../Celeris-WebGPU/shaders/Update_neardry.wgsl.md) | 3 | 56 | 완료 |
| [fragment.wgsl.md](../Celeris-WebGPU/shaders/fragment.wgsl.md) | 23 | 928 | 완료 |
| [fragment_testing.wgsl.md](../Celeris-WebGPU/shaders/fragment_testing.wgsl.md) | 22 | 867 | 완료 |
| [vertex.wgsl.md](../Celeris-WebGPU/shaders/vertex.wgsl.md) | 2 | 19 | 완료 |
| [vertex3D.wgsl.md](../Celeris-WebGPU/shaders/vertex3D.wgsl.md) | 4 | 86 | 완료 |
| [index.html.md](../Celeris-WebGPU/transect_version/index.html.md) | 29 | 1475 | 완료 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| SedTrans_Pass3.wgsl.md:212–241 | 퇴적 상한에서 침강속도 계수를 생략했다. | [정정] 침강속도 곱을 명시했다. 시간 선택 사슬의 마지막 else 부재를 명시했다. | 212–233 |
| SedTrans_Pass3_old.wgsl.md:151–181 | 퇴적 비교값을 C_here로 적었다. | [정정] 두 배의 C_here와 침강속도 곱을 명시했다. 마지막 else 부재를 명시했다. | 151–173 |
| SedTrans_Pass3.wgsl.md:153–181 | 소류사 주석의 MP&M 표기가 없었다. | [보완] MP&M 표기와 바깥 조건 블록의 종료 행을 추가했다. | 153–210 |
| SedTrans_Pass3_wBedUpdate.wgsl.md:156–184 | 소류사 주석의 MP&M 표기가 없었다. | [보완] MP&M 표기와 바깥 조건 블록의 종료 행을 추가했다. | 156–213 |
| SedTrans_Pass3_wBedUpdate.wgsl.md:233–255 | 시간 선택 사슬의 마지막 else 부재를 설명하지 않았다. | [보완] else 부재와 조건 불일치 시 초기값 유지를 명시했다. | 227–247 |
| SedTrans_UpdateBottom_testing.wgsl.md:70–90 | 최근 변화 저장문의 원문 인용이 없었다. | [보완] 주석 처리된 최근 변화 저장문을 인용했다. | 88 |
| TriDiag_PCRx.wgsl.md:1–18 | P 필드 주석의 JS 기록 순서 설명이 없었다. | [보완] JS가 s 뒤에 uniform을 쓴다는 원문 주석을 추가했다. | 6 |
| TriDiag_PCRx.wgsl.md:89–107 | 주석 처리된 상태 저장문 인용이 없었다. | [보완] 비실행 저장문을 추가했다. | 98 |
| TriDiag_PCRx_COULWAVE.wgsl.md:21–57 | 주석 처리된 두 저장문과 return 인용이 없었다. | [보완] 비실행 저장문과 return을 추가했다. | 32–37 |
| TriDiag_PCRx_COULWAVE.wgsl.md:91–116 | 주석 처리된 상태 저장문 인용이 없었다. | [보완] 비실행 저장문을 추가했다. | 114 |
| TriDiag_PCRy.wgsl.md:1–18 | P 필드 주석의 JS 기록 순서 설명이 없었다. | [보완] JS가 s 뒤에 uniform을 쓴다는 원문 주석을 추가했다. | 6 |
| TriDiag_PCRy.wgsl.md:89–110 | 주석 처리된 상태 저장문 인용이 없었다. | [보완] 비실행 저장문을 추가했다. | 98 |
| TriDiag_PCRy_COULWAVE.wgsl.md:21–57 | 주석 처리된 두 저장문과 return 인용이 없었다. | [보완] 비실행 저장문과 return을 추가했다. | 32–37 |
| TriDiag_PCRy_COULWAVE.wgsl.md:91–119 | 주석 처리된 상태 저장문 인용이 없었다. | [보완] 비실행 저장문을 추가했다. | 114 |
| fragment.wgsl.md:1–69 | 미리보기 상태 주석의 업로드 주체와 출처가 없었다. | [보완] main.js와 calc_constants를 주석 근거로 추가했다. | 59 |
| fragment.wgsl.md:201–254 | 201행 이후를 색 지도 2 가지 안으로 적었다. | [정정] 색 지도 2 가지의 종료와 같은 사슬의 색 지도 3 가지 시작을 구분했다. | 183–201 |
| fragment.wgsl.md:255–292 | 255–292를 색 지도 5 가지 안으로 적었다. | [정정] 색 지도 6 가지와 사슬 종료 후 실행문을 구분했다. | 237–292 |
| fragment.wgsl.md:331–383 | 331행 이후를 표면 4 가지 안으로 적었다. | [정정] 같은 사슬의 다음 가지와 마지막 else 부재를 명시했다. | 287–382 |
| fragment.wgsl.md:401–435 | 두 경계 선택 사슬의 마지막 else 부재와 덮어쓰기 순서가 없었다. | [보완] 각 사슬의 종료와 방향각 갱신 순서를 명시했다. | 401–421 |
| fragment.wgsl.md:571–608 | 색 보간 경로를 젖은 표면으로 한정했다. | [정정] 건조 조건의 else 경로임을 명시했다. | 576–608 |
| fragment.wgsl.md:609–637 | 바깥 else 두 개의 대응 조건이 없었다. | [보완] 건조 표시 조건과 photorealistic 조건의 거짓 가지임을 명시했다. | 576–733 |
| fragment.wgsl.md:638–681 | 바깥 else의 조건과 내부 수심 선택 사슬의 마지막 else 부재가 없었다. | [보완] 대응 조건과 수심 선택 사슬의 else 부재를 명시했다. | 576–733 |
| fragment.wgsl.md:682–734 | 682–734를 성분 6 가지 안으로 적었다. | [정정] 성분 7 이후의 형제 가지와 바깥 조건 및 사슬 종료를 명시했다. | 576–734 |
| fragment.wgsl.md:795–800 | 쇄파 표시 요약에서 표면 11 제외 조건이 없었다. | [정정] 두 가지의 표면 조건과 마지막 else 부재를 명시했다. | 795–801 |
| fragment.wgsl.md:801–853 | 미리보기 주석의 시계열 좌표 변환 설명이 없었다. | [보완] 주석 설명과 tracer 가지의 닫힘 위치를 추가했다. | 801–852 |
| fragment.wgsl.md:854–885 | 마커 색 선택 사슬의 마지막 else 부재가 없었다. | [보완] else 부재와 범위 밖 색 유지를 명시했다. | 878–883 |
| fragment.wgsl.md:886–928 | 문자 덮어쓰기 조건을 흰색이 아님으로 적었다. | [정정] RGB 합의 실제 임계값 조건으로 고쳤다. | 919–921 |
| fragment_testing.wgsl.md:192–245 | 192–245를 색 지도 2 가지 안으로 적었다. | [정정] 191행 대입 종료와 192행 중괄호 및 다음 가지를 구분했다. | 174–192 |
| fragment_testing.wgsl.md:246–283 | 246–283을 색 지도 5 가지 안으로 적었다. | [정정] 색 지도 6 가지와 사슬 종료 후 실행문을 구분했다. | 228–283 |
| fragment_testing.wgsl.md:322–374 | 322행 이후를 표면 4 가지 안으로 적었다. | [정정] 같은 사슬의 다음 가지와 마지막 else 부재를 명시했다. | 278–373 |
| fragment_testing.wgsl.md:401–426 | 경계 선택 사슬의 종료와 마지막 else 부재가 없었다. | [보완] 각 사슬의 종료와 방향각 갱신 순서를 명시했다. | 395–412 |
| fragment_testing.wgsl.md:476–521 | 와도 표현의 한계와 해결안 주석이 없었다. | [보완] 세 주석의 의미와 원문 및 제한 사슬의 else 부재를 추가했다. | 476–507 |
| fragment.wgsl.md:485–530 | 이동량 제한 사슬의 마지막 else 부재가 없었다. | [보완] else 부재와 제한 범위 안의 값 유지를 명시했다. | 513–516 |
| fragment_testing.wgsl.md:600–628 | 바깥 else 두 개의 대응 조건이 없었다. | [보완] 건조 표시 조건과 photorealistic 조건의 거짓 가지임을 명시했다. | 567–724 |
| fragment_testing.wgsl.md:629–672 | 바깥 else의 조건과 내부 수심 선택 사슬의 마지막 else 부재가 없었다. | [보완] 대응 조건과 수심 선택 사슬의 else 부재를 명시했다. | 567–724 |
| fragment_testing.wgsl.md:673–725 | 673–725를 성분 6 가지 안으로 적었다. | [정정] 성분 7 이후의 형제 가지와 바깥 조건 및 사슬 종료를 명시했다. | 567–725 |
| fragment_testing.wgsl.md:726–783 | sampler의 반복 래핑 요구 주석이 없었다. | [보완] 원문 주석의 요구를 추가했다. | 773 |
| fragment_testing.wgsl.md:784–800 | 쇄파·tracer 선택 사슬의 마지막 else 부재가 없었다. | [보완] else 부재와 사슬 종료 행을 명시했다. | 785–791 |
| fragment_testing.wgsl.md:801–824 | 마커 색 선택 사슬의 마지막 else 부재가 없었다. | [보완] else 부재와 범위 밖 색 유지를 명시했다. | 817–822 |
| index.html.md:1–179 | CSS가 일반적인 화면 스타일 설명으로만 요약되어 있었다. | [보완] CSS의 수치·기본 표시 상태·선택자·주석을 원문으로 보완했다. | 9–178 |
| index.html.md:260–322 | 예제 실행과 갱신 대상 주석이 없었다. | [보완] 서버 측 예제와 simPause 갱신 주석을 추가했다. | 260, 261, 303, 312 |
| index.html.md:323–373 | 갱신 대상 주석이 없었다. | [보완] surfaceToPlot과 colorMap_choice의 갱신 대상 주석을 추가했다. | 330, 359 |
| index.html.md:374–400 | 갱신 대상 주석이 없었다. | [보완] colorVal_max·colorVal_min·showBreaking·GoogleMapOverlay 주석을 추가했다. | 374, 382, 390, 400 |
| index.html.md:401–460 | 갱신 대상 주석이 구간에 없었다. | [보완] ShowLogos 표기와 viewType 갱신 주석을 추가했다. | 410, 433, 443 |
| index.html.md:461–541 | 초기 접힘 상태와 갱신 대상 주석이 없었다. | [보완] minimized 속성과 모든 갱신 대상 주석을 추가했다. | 466, 468, 489, 494, 499, 504, 509, 514, 519, 524, 529, 534 |
| index.html.md:542–624 | 갱신 대상과 동적 상수 컨테이너 설명이 없었다. | [보완] 입력 갱신 주석과 동적 컨테이너 및 추가 버튼 주석을 보완했다. | 542, 557, 565, 573, 581, 596, 604, 612, 613, 616 |
| index.html.md:625–683 | 초기 접힘 상태와 갱신 대상 주석이 없었다. | [보완] minimized와 해수면·표면·변경 종류·변화량·반경 갱신 대상을 추가했다. | 632, 634, 643, 654, 664, 672 |
| index.html.md:684–727 | 초기 접힘 상태와 갱신 대상 주석이 없었다. | [보완] minimized와 입사파 입력 갱신 대상을 추가했다. | 689, 691, 704, 712, 720 |
| index.html.md:728–778 | 경계 갱신 대상 주석이 없었다. | [보완] 서·동·남·북 경계 갱신 대상 주석을 추가했다. | 728, 739, 750, 761 |
| index.html.md:779–800 | D50·공극률 갱신 대상 주석이 없었다. | [보완] sedC1_d50·sedC1_n 갱신 주석을 추가했다. | 791, 798 |
| index.html.md:801–843 | 갱신 대상 주석이 구간에 없었다. | [보완] 각 갱신 대상과 임계 Shields 입력 앞 주석의 실제 철자를 추가했다. | 805, 812, 819, 827 |
| index.html.md:844–885 | Crest Amplitude를 파고로 요약했다. | [정정] 파봉 진폭으로 고쳤다. 나머지 공용 입력의 원문 의미도 명시했다. | 878–881 |
| index.html.md:844–885 | 초기 접힘 상태와 갱신 대상 주석이 없었다. | [보완] minimized와 파원 갱신 대상 주석을 추가했다. | 849, 851, 862, 870, 878 |
| index.html.md:886–941 | 갱신 대상과 부피 컨테이너의 동적 채움 설명이 없었다. | [보완] 갱신 대상 주석과 slidevolume-container 설명을 추가했다. | 886, 894, 902, 910, 918, 926, 927 |
| index.html.md:942–983 | 초기 상태와 시계열 시간 입력의 갱신 대상 주석이 없었다. | [보완] minimized와 두 갱신 대상의 정확한 이름을 추가했다. | 947, 949, 972 |
| index.html.md:984–1035 | 갱신 대상과 위치 컨테이너의 동적 채움 설명이 없었다. | [보완] 각 갱신 대상과 timeserieslocs-container 설명을 추가했다. | 984, 1012, 1020, 1028, 1029 |
| index.html.md:1036–1062 | 초기 접힘 상태와 텍스처 초기화 주석이 없었다. | [보완] minimized와 저장·초기화 주석을 추가했다. | 1041, 1043, 1048, 1053 |
| index.html.md:1063–1105 | 초기 상태와 프레임 간격 갱신 대상 및 버튼 주석이 없었다. | [보완] minimized와 AnimGif_dt 및 실제 버튼 주석을 추가했다. | 1068, 1072, 1089, 1096 |
| index.html.md:1106–1139 | JPEG 갱신 대상과 버튼 주석이 없었다. | [보완] JPEGstack_dt·JPEGstack_frames와 버튼 주석을 추가했다. | 1111, 1118, 1125 |
| index.html.md:1140–1183 | 초기 상태와 출력 선택의 갱신 대상 주석이 없었다. | [보완] minimized와 surfaceToWrite 및 JSON 다운로드 주석을 추가했다. | 1145, 1152, 1159 |
| index.html.md:1184–1200 | 출력 갱신 대상 주석이 없었다. | [보완] dt_writesurface·write_eta·write_P 주석을 추가했다. | 1185, 1192, 1200 |
| index.html.md:1201–1246 | 출력 갱신 대상과 저장 시작 주석이 없었다. | [보완] write_Q·write_turb와 저장 시작 주석을 추가했다. | 1208, 1216, 1225 |
| index.html.md:1247–1287 | Theta 기본값의 쇄파 모델 조건과 Courant의 이하 조건이 요약에서 빠졌다. | [정정] 기본값 조건과 기법별 Courant 상한을 명시했다. | 1264–1274 |
| index.html.md:1247–1287 | 초기 접힘 상태와 갱신 대상 주석이 없었다. | [보완] minimized와 모든 갱신 대상 주석을 추가했다. | 1252, 1254, 1263, 1271, 1279 |
| index.html.md:1288–1336 | 각 입력의 갱신 대상 주석이 없었다. | [보완] 마찰과 쇄파 관련 갱신 대상 주석을 모두 추가했다. | 1288, 1296, 1305, 1313, 1321, 1329 |
| index.html.md:1337–1381 | 각 입력의 갱신 대상 주석이 없었다. | [보완] whiteWaterDispersion·whiteWaterDecayRate·infiltrationRate·render_step 주석을 추가했다. | 1337, 1345, 1353, 1361 |
| index.html.md:1382–1437 | 동적 채움 주석과 초기 표시 속성 인용이 없었다. | [보완] simstatus-container와 각 창의 속성 및 동적 채움 주석을 추가했다. | 1384, 1385, 1403, 1412, 1413, 1427, 1428 |
| index.html.md:1438–1453 | 라이브러리 주석의 배치 지시와 용도 설명이 빠졌다. | [보완] popper.js 용도와 Bootstrap 사용 전 배치 지시 및 도입 주석을 추가했다. | 1438, 1439, 1443, 1446, 1450 |
| index.html.md:1454–1475 | 외부 script 주석의 용도 설명이 빠졌다. | [보완] GIF 생성·시계열 그래프·파랑 해 제어 주석을 추가했다. | 1464, 1467, 1470 |
| fragment.wgsl.md:70–91 | 변수 이름의 f16을 반정밀도 자료형의 근거로 서술했다. | [정정] WGSL 선언 자료형과 변수 이름을 구분했다. | 87–89 |
| fragment_testing.wgsl.md:61–82 | 변수 이름의 f16을 반정밀도 자료형의 근거로 서술했다. | [정정] WGSL 선언 자료형과 변수 이름을 구분했다. | 78–80 |
| SedTrans_Pass3.wgsl.md:212–241 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 224–233 |
| SedTrans_Pass3_old.wgsl.md:151–181 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 164–173 |
| fragment.wgsl.md:255–292 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 255–274 |
| fragment.wgsl.md:331–383 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 331–382 |
| fragment.wgsl.md:682–734 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 638–733 |
| fragment.wgsl.md:795–800 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 795–801 |
| fragment_testing.wgsl.md:246–283 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 246–265 |
| fragment_testing.wgsl.md:322–374 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 322–373 |
| fragment_testing.wgsl.md:673–725 | 분기 사슬의 마지막 else 부재 설명이 없었다. | [보완] 마지막 else 부재와 종료 위치를 보완했다. | 629–724 |

대상 기록 18개를 모두 완료했다. 140개 구간의 원문 5,081행을 대조했다. 원문 SHA-256은 각 기록 frontmatter와 일치했다. 단일 행 원문 인용 3,528개의 내용과 행 번호가 일치했다.

정정 17, 보완 63, 이상 없음 71

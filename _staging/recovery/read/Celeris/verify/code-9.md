# Celeris code-9 전수 대조 (11-04)

대상 기록의 frontmatter file: 경로를 원문으로 사용한다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번의 원문 출력은 200행 이하이다.
인용문과 행 번호는 문자 대조를 병행했다.
요약 의미와 분기 맥락은 출력한 원문으로 대조했다.
요청된 대상 기록 28개를 모두 대조했다.
모델은 실행하지 않았다.

기록 경로의 공통 접두사는 _staging/recovery/read/Celeris/Celeris-WebGPU/transect_version/shaders이다.
행 수는 기록의 구간 표 행 수이다.
원문 행 수에는 빈 행과 주석 행을 포함한다.
마지막 집계는 대조를 마친 구간 표 행을 기준으로 한다.
정정과 보완을 함께 한 행은 각 항목에 한 번씩 센다.
이상 없음은 정정·보완이 없는 구간 표 행 수이다.

| 기록 | 대조한 기록 행 수 | 대조한 원문 행 수 | 상태 |
|---|---:|---:|---|
| BoundaryPass.wgsl.md | 13 | 558 | 완료 |
| CalcMeans.wgsl.md | 4 | 105 | 완료 |
| CalcWaveHeight.wgsl.md | 3 | 77 | 완료 |
| Copytxf32_txf16.wgsl.md | 2 | 35 | 완료 |
| ExtractTimeSeries.wgsl.md | 3 | 58 | 완료 |
| MouseClickChange.wgsl.md | 5 | 166 | 완료 |
| Pass0.wgsl.md | 3 | 60 | 완료 |
| Pass1.wgsl.md | 5 | 183 | 완료 |
| Pass1_HighOrder.wgsl.md | 10 | 380 | 완료 |
| Pass2.wgsl.md | 5 | 181 | 완료 |
| Pass2_HighOrder.wgsl.md | 6 | 234 | 완료 |
| Pass3A_COULWAVE.wgsl.md | 3 | 89 | 완료 |
| Pass3B_COULWAVE.wgsl.md | 5 | 175 | 완료 |
| Pass3_Bous.wgsl.md | 12 | 426 | 완료 |
| Pass3_COULWAVE.wgsl.md | 14 | 532 | 완료 |
| Pass3_NLSW.wgsl.md | 8 | 277 | 완료 |
| Pass_Breaking.wgsl.md | 4 | 149 | 완료 |
| SedTrans_Pass1.wgsl.md | 5 | 135 | 완료 |
| SedTrans_Pass3.wgsl.md | 5 | 140 | 완료 |
| SedTrans_UpdateBottom.wgsl.md | 3 | 52 | 완료 |
| Ship_pressure.compute.md | 4 | 81 | 완료 |
| TriDiag_PCRx.wgsl.md | 4 | 97 | 완료 |
| TriDiag_PCRx_COULWAVE.wgsl.md | 4 | 106 | 완료 |
| TriDiag_PCRy.wgsl.md | 4 | 100 | 완료 |
| TriDiag_PCRy_COULWAVE.wgsl.md | 4 | 109 | 완료 |
| Update_TriDiag_coef.wgsl.md | 4 | 111 | 완료 |
| Update_TriDiag_coef_COULWAVE.wgsl.md | 4 | 117 | 완료 |
| Update_neardry.wgsl.md | 3 | 58 | 완료 |

완료 표에서 센 구간 표 행은 149개이다.
완료 표에서 센 원문 행은 4791행이다.
원문의 SHA-256은 각 기록 frontmatter의 값과 일치한다.
모든 구간의 경계와 frontmatter는 유지했다.
원문·노트·git은 수정하지 않았다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| BoundaryPass.wgsl.md:110–138 | hu 반환으로 축약 | eta·hu·hv·0.0의 벡터 반환 [정정] | 131–136 |
| BoundaryPass.wgsl.md:174–201 | 양의 수심 조건 | d_here > 0.0001 조건 [정정] | 182 |
| BoundaryPass.wgsl.md:202–271 | 분기 사슬의 마지막 else 유무 생략 | 활성·주석 사슬 모두 마지막 else 없음 [보완] | 230–269 |
| BoundaryPass.wgsl.md:272–340 | 입사파 사슬의 미일치 처리 생략 | 마지막 else 없음 [보완] | 275–338 |
| BoundaryPass.wgsl.md:401–436 | 401행 이후를 500년 홍수 분기 닫힘으로 요약 | 200년 가지 닫힘·500년 가지 시작과 끝·else 부재 명시 [정정] | 398–409 |
| BoundaryPass.wgsl.md:495–542 | sum_dry를 건조 셀 수로 설명 | 임계값 이하 0이므로 습윤 이웃 수이며 마지막 else 없음 [정정] | 496–508·525–541 |
| CalcWaveHeight.wgsl.md:25–44 | 첫 단계에서 초기화 | 단계 수 <= 1에서 초기화 [정정] | 27–29 |
| ExtractTimeSeries.wgsl.md:48–58 | 48행이 idx.x == 0 가지 안 | 48행에서 해당 가지를 닫고 else 진입·54행에서 else 닫힘 [정정] | 29·48–54 |
| MouseClickChange.wgsl.md:31–60 | 미일치 changeType 처리 생략 | 마지막 else 없음·dH 초기값 유지 [보완] | 50–57 |
| MouseClickChange.wgsl.md:61–96 | 선택 사슬의 마지막 else 유무 생략 | 두 사슬 모두 마지막 else 없음 [보완] | 68–87 |
| MouseClickChange.wgsl.md:132–166 | 132행이 surfaceToChange == 1 가지 안 | 132행은 다음 가지·144행과 162행 사슬 끝·else 부재 [정정] | 97–162 |
| Pass1.wgsl.md:31–53 | 동·서 면 값만 설명 | 반환 벡터의 서·동 순서를 명시 [보완] | 48–51 |
| Pass1_HighOrder.wgsl.md:52–85 | 세 번째 차분을 6으로 나눔 | 제한한 세 차분의 1·-2·1 조합을 6으로 나누어 보정 [정정] | 66–83 |
| Pass1_HighOrder.wgsl.md:263–312 | 수위 차분 최대값 | 수위 차분 절댓값의 최대값 [정정] | 284–290 |
| Pass2.wgsl.md:32–54 | 마지막 else 부재와 사슬 뒤 반환 생략 | else 없이 사슬 뒤 기본 반환 [보완] | 41–52 |
| Pass2.wgsl.md:99–145 | 세 번째 성분 인수가 모두 0 | aplus·aminus 뒤 세 인수만 0.0 [정정] | 131 |
| Pass3_Bous.wgsl.md:154–195 | 2차 수위 기울기 | 2차 정확도 중앙 차분의 x 방향 1차 미분 [정정] | 168 |
| Pass3_Bous.wgsl.md:246–292 | 바닥 수심의 4차 x 미분 | 4차 정확도의 x 방향 1차 미분·블록 끝 291행 [정정] | 194–195·264·267·291 |
| Pass3_Bous.wgsl.md:359–394 | 기울기 사슬의 미일치 처리 생략 | 마지막 else 없음·기존 기울기 유지 [보완] | 360–378 |
| Pass3_Bous.wgsl.md:401–426 | 예측 가지 끝·else 부재 생략 | 402행 가지 전환·406행 시간 적분 끝·415행 표시 사슬 끝 [보완] | 391–415 |
| Pass3_COULWAVE.wgsl.md:158–200 | 2차 수위 기울기 | 2차 정확도 중앙 차분의 x 방향 1차 미분 [정정] | 172 |
| Pass3_COULWAVE.wgsl.md:201–237 | 4차 및 2차 수위 기울기 | 미분 차수 1차·차분 정확도 각각 4차와 2차 [정정] | 224–228 |
| Pass3_COULWAVE.wgsl.md:465–500 | 기울기 사슬의 미일치 처리 생략 | 마지막 else 없음·기존 기울기 유지 [보완] | 466–484 |
| Pass3_COULWAVE.wgsl.md:501–532 | 사슬의 미일치 처리 생략 | 마지막 else 없음·newState 초기값 유지·clearConc == 1 명시 [보완] | 497–526 |
| Pass3_NLSW.wgsl.md:211–246 | 기울기 사슬의 미일치 처리 생략 | 마지막 else 없음·기존 기울기 유지 [보완] | 159·212–230 |
| Pass3_NLSW.wgsl.md:247–277 | 사슬의 미일치 처리 생략 | 마지막 else 없음·시간 적분 사슬 직후 초기값 유지 [보완] | 247–269 |
| Pass_Breaking.wgsl.md:30–86 | 상류 이웃과 현재 시각 표지의 max | P_here > 0이면 왼쪽·그 외 오른쪽·현재 셀의 기존 시각과 max [정정] | 58–85 |
| SedTrans_Pass1.wgsl.md:51–86 | 바닥 차이의 절반·in_이웃.x로 축약 | 절댓값·성분 순서·실제 변수 이름 명시 [정정] | 75–85 |
| SedTrans_Pass3.wgsl.md:124–140 | 시간 적분 사슬의 미일치 처리 생략 | 마지막 else 없음·newState 초기값 유지 [보완] | 124–136 |
| Ship_pressure.compute.md:20–31 | 이차 형식의 제곱을 exp에 입력 | 제곱의 음수를 exp에 넣고 ship_draft를 곱함 [정정] | 30 |
| Ship_pressure.compute.md:62–81 | 전처리 사슬의 기본 가지 생략 | 마지막 #else 없음 [보완] | 64–73 |
| TriDiag_PCRx.wgsl.md:17–52 | x±s의 나머지로 축약 | 나머지 연산 전 +width와 y 유지 명시 [정정] | 35–36 |
| TriDiag_PCRx_COULWAVE.wgsl.md:1–20 | Px를 마지막 단계 자체로 설명 | 마지막 단계 조건 p == Px-1에 사용하는 값 [정정] | 6·95 |
| TriDiag_PCRx_COULWAVE.wgsl.md:21–56 | x±s의 나머지로 축약 | 나머지 연산 전 +width와 y 유지 명시 [정정] | 39–40 |
| TriDiag_PCRy.wgsl.md:17–52 | y±s의 나머지로 축약 | 나머지 연산 전 +height와 x 유지 명시 [정정] | 35–36 |
| TriDiag_PCRy_COULWAVE.wgsl.md:1–20 | Py를 마지막 단계 자체로 설명 | 마지막 단계 조건 p == Py-1에 사용하는 값 [정정] | 6·95 |
| TriDiag_PCRy_COULWAVE.wgsl.md:21–56 | y±s의 나머지로 축약 | 나머지 연산 전 +height와 x 유지 명시 [정정] | 39–40 |
| Update_TriDiag_coef.wgsl.md:49–73 | 바깥 블록을 else 이름만 기재 | 42행 조건의 거짓 가지·71행 닫힘·72행은 바깥 [보완] | 42–47·71–72 |
| BoundaryPass.wgsl.md:401–436 | 홍수 사슬의 마지막 else 유무 생략 | 마지막 else 없음 [보완] | 386–405 |
| BoundaryPass.wgsl.md:495–542 | 주석 사슬의 마지막 else 유무 생략 | 526–540행 사슬에 마지막 else 없음 [보완] | 526–540 |
| MouseClickChange.wgsl.md:132–166 | 표면 편집·패널 사슬의 마지막 else 유무 생략 | 144행·162행에서 마지막 else 없이 사슬 종료 [보완] | 98–162 |

정정 23, 보완 18, 이상 없음 111

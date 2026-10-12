# ADCIRC 외부 원문 판정 반영

작성일: 2026-10-12.

입력은 [external-results-ad.md](../compare/external-results-ad.md)이다. 노트 위치는 [이전 반영 기록](ADCIRC-conclusions-apply.md)의 기존 표 또는 가까운 기존 절 규칙을 따랐다.

입력의 5개 행 ID를 모두 반영했다. 보고서 §5에서는 이 행 ID들이 3개 표 행으로 묶여 있다. 아래 위치는 이번 수정 뒤의 파일 줄 번호이다.

## 반영 행과 위치

| 입력 행 ID | 보고서 §5 위치 | 반영 결론 | 문서와 코드 차이의 노트 위치 |
|---|---|---|---|
| T09 | [ADCIRC-features-vs-code.md:856](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | D(문서에 생성식 없음)와 C(4π·C̃ 정규화 근거 부재) | [adcirc-nodal-attributes.md:168](../../../models/ADCIRC/source-analysis/adcirc-nodal-attributes.md#문서와-코드-차이--it_fric-생성식) |
| F17 | [ADCIRC-features-vs-code.md:885](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | E(c24 부호)와 B(Pandoe의 T³ 지수 누락) | [adcirc-3d-mode.md:124](../../../models/ADCIRC/source-analysis/adcirc-3d-mode.md#문서와-코드-차이--eos-80-외부-원문-판정), [adcirc-baroclinic-coupling.md:88](../../../models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md#문서와-코드-차이--adcirc-자체-3d-밀도식) |
| F19 | [ADCIRC-features-vs-code.md:885](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | E(c24 부호) | [adcirc-3d-mode.md:126](../../../models/ADCIRC/source-analysis/adcirc-3d-mode.md#문서와-코드-차이--eos-80-외부-원문-판정), [adcirc-baroclinic-coupling.md:88](../../../models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md#문서와-코드-차이--adcirc-자체-3d-밀도식) |
| C33 | [ADCIRC-features-vs-code.md:885](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | E(c24 부호)와 B(Pandoe 문서 오기)와 F(UNESCO 1980/1981 표기) | [adcirc-3d-mode.md:128](../../../models/ADCIRC/source-analysis/adcirc-3d-mode.md#문서와-코드-차이--eos-80-외부-원문-판정), [adcirc-baroclinic-coupling.md:88](../../../models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md#문서와-코드-차이--adcirc-자체-3d-밀도식) |
| G: N01 / L1446 | [ADCIRC-outputs-vs-code.md:1667](../compare/ADCIRC-outputs-vs-code.md#5-차이-결론) | A(판 차이): 조회한 NOUTE 태그 검사에서 최초 거부 판은 v56.1.0 | [adcirc-output-writers-implementation.md:585](../../../models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md#n01--binary-거부의-최초-판). 같은 노트 30줄의 미확인 문구도 고쳤다. |

보고서의 3개 대상 표 행은 근거 칸에 외부 서지·URL·식 또는 표·쪽 또는 소스 줄·원문 인용을 포함한다. 각 대상 표 행의 결론 끝에는 `[10-12 외부 원문 판정]`을 붙였다.

F17·F19·C33의 c24 후보는 [adcirc-baseline-anatomy.md:106](../../../models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md#코드-결함-후보-정적-판독)의 표에 한 행으로 추가했다. 같은 후보는 사용자 지정 밀도 노트인 [adcirc-baroclinic-coupling.md:104](../../../models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md#코드-결함-후보-정적-판독)의 표에도 한 행으로 추가했다. 두 표는 위치·어긋남·근거·영향 범위·근거 강도·출처를 기록한다. 근거 강도는 강함이다. 근거는 Fofonoff(1985) Table 3 B 열의 음수 t³ 계수와 사용자 제공 Claude 확인의 양수 c24 선언·Horner 사용이다.

대표 노트의 후보 표는 기존 54행에서 55행이 되었다. 이 개수는 `adcirc-baseline-anatomy.md`의 코드 결함 후보 표 자료 행을 센 값이다. F17·F19·C33은 같은 c24 후보를 공유하므로 후보 표에서 세 행으로 늘리지 않았다.

## 분류별 개수

개수는 두 보고서 §5 첫 열의 행 ID를 펼쳐 센 값이다. 복합 결론은 첫 분류로 한 번만 센다. T09는 D로 센다. F17·F19·C33은 E로 센다. B·C·F 부결론은 중복해서 더하지 않는다.

| 분류 | features 반영 전 | features 반영 후 | outputs 반영 전 | outputs 반영 후 |
|---|---:|---:|---:|---:|
| 대상 행 ID | 276 | 276 | 820 | 820 |
| A 판 차이 | 49 | 49 | 68 | 69 |
| B 문서 오기 | 62 | 62 | 71 | 71 |
| C 문서 누락 | 101 | 101 | 642 | 642 |
| D 문서만 있음 | 32 | 33 | 2 | 2 |
| E 코드 결함 후보 | 14 | 17 | 35 | 35 |
| F 표기 차이 | 13 | 13 | 1 | 1 |
| G 판단 근거 부족 | 0 | 0 | 1 | 0 |
| H 코드 대조 대상 아님 | 1 | 1 | 0 | 0 |
| X 외부 원문 필요 | 4 | 0 | 0 | 0 |

features의 최종 개수는 보고서 739줄과 980줄에 있다. outputs의 최종 개수는 보고서 1510줄과 1695줄에 있다. 두 보고서의 §5에서 X와 G는 모두 0행이다. 외부 원문 판정 전 개수는 과거 집계로 표시했다.

## 고친 노트

- [adcirc-nodal-attributes.md](../../../models/ADCIRC/source-analysis/adcirc-nodal-attributes.md): 내부 조석 절에 T09의 D·C 결론과 Pringle(2018)의 식·쪽 인용을 추가했다.
- [adcirc-3d-mode.md](../../../models/ADCIRC/source-analysis/adcirc-3d-mode.md): 밀도 절에 F17·F19·C33의 결론을 추가했다. 기존 EOS-80 식의 미확인 문구를 제거했다. F18에 남은 c24의 G 분류 문구를 고쳤다.
- [adcirc-baroclinic-coupling.md](../../../models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md): 2D·3D 구분 절에 F17·F19·C33의 결론을 추가했다. ADCIRC 자체 3D 밀도 계산의 c24 후보 표를 추가했다.
- [adcirc-baseline-anatomy.md](../../../models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md): 코드 결함 후보 표에 F17·F19·C33의 c24 후보를 추가했다.
- [adcirc-output-writers-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md): 문서와 코드 차이 절에 L1446(N01)의 A 결론을 추가했다. 형식 요약의 최초 거부 판 미확인 문구를 고쳤다.

위 5개 노트의 frontmatter `last_source_check`는 모두 `2026-10-12 (recovery 차이 결론 반영)`이다. 이 개수는 위 목록의 파일을 센 값이다.

## 원문 범위와 참고문헌 오류

T09에는 `2차 문헌 기준: Pringle et al.(2018)`을 붙였다. Bell(1975)·Nycander(2005)의 원식 대조는 입력 판정에서 수행하지 않았다. 밀도식에는 `2차 문헌 기준: Fofonoff(1985)`를 붙였다. UNESCO TP 44 식 (13)의 원문 대조는 입력 판정에서 수행하지 않았다. 표 인용은 Fofonoff(1985) 저자 열람본 Table 3, 인쇄 p.3337을 사용했다. 외부 판정이 사용한 OCR 부호 교차 확인도 함께 기록했다.

입력 판정표는 쪽 범위 오류를 판정하지 않았다. 입력 판정표는 Part 번호 오류를 판정하지 않았다. 입력 판정표는 존재하지 않는 태그 링크 오류를 판정하지 않았다. 이 세 종류의 오류 문장은 노트에 추가하지 않았다. C33의 UNESCO 1980/1981 표기 차이는 위 밀도 노트 두 곳에 반영했다.

## 확인 범위

§5의 행 ID를 다시 센 결과는 두 보고서의 첫머리·마지막 줄과 일치했다. 두 보고서의 §1–4는 수정 전후 해시가 같았다. 입력 판정표와 이전 반영 기록은 수정 전후 해시가 같았다. 새 후보 표 행의 열 수와 근거 강도 및 출처를 확인했다. 고친 노트의 frontmatter 값을 확인했다.

이번 작업은 제공된 외부 판정의 반영 작업이다. 웹 원문을 새로 조회하지 않았다. 모델을 실행하지 않았다. git으로 상태를 바꾸지 않았다. 밀도 차이 수치는 입력 F17의 별도 다항식 계산에서 가져왔다. 이 수치는 ADCIRC 실행 결과가 아니다.

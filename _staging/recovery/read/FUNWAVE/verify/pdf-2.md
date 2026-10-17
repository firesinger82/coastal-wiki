# FUNWAVE PDF 판독 기록 전수 검증 — pdf-2

검증일은 2026-10-17이다.
원문은 `models/FUNWAVE/raw/source_code/FUNWAVE-TVD/doc/funwave_tvd_3.0.pdf`다.
판정 근거는 지정된 300 dpi 쪽 이미지다.
이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/fwpages/funwave_tvd_3.0-NNN.png`다.
원문 행은 PDF 쪽 번호와 인쇄 문구 또는 그림 위치로 식별한다.

| 기록 | 대상 행 수 | 대조한 행 수 | 정정 | 보완 | 이상 없음 | 상태 |
|---|---:|---:|---:|---:|---:|---|
| [p037-054.md](../FUNWAVE-TVD/doc/funwave_tvd_3.0.pdf/p037-054.md) | 18 | 18 | 11 | 2 | 7 | 완료. p.37–54의 모든 행을 대조했다. |
| [p055-072.md](../FUNWAVE-TVD/doc/funwave_tvd_3.0.pdf/p055-072.md) | 18 | 18 | 17 | 5 | 1 | 완료. p.55–72의 모든 행을 대조했다. |
| 합계 | 36 | 36 | 28 | 7 | 8 | 완료. |

정정과 보완은 각각 해당 표식을 붙인 쪽 행 수로 센다.
한 행에 두 종류가 있으면 각 집계에 한 번씩 포함한다.
보완한 7개 행은 모두 정정한 행에도 포함된다.
이상 없음은 대조 후 변경하지 않은 쪽 행 수다.
이상 없음은 `p037-054.md`의 p.37–43과 `p055-072.md`의 p.55다.

수식과 숫자 및 단위는 쪽 이미지와 대조했다.
입력 매개변수의 이름과 값 및 조건은 쪽 이미지와 대조했다.
한정 표현과 출처 표기 및 그 쪽에 없는 귀속을 확인했다.
절 표제와 그림·표 캡션 및 그림 안의 표기를 확인했다.
이번 검증에서 확인한 같은 쪽 안의 모순은 해당 쪽 행과 끝 절에 함께 적었다.
판독하지 못한 대상 행은 없다.
모델은 실행하지 않았다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| p037-054.md:p.44 (정정) | 쪽 첫머리에 절 4.5 `Model nesting`을 붙였다. | 그 쪽에 없는 절 번호·제목을 삭제했다. 결합 자료 예시의 계속임은 유지했다. | p.44 첫 행 `-1 0 (no data on south side)`. 이 쪽의 절 제목은 `4.6 Output`이다. |
| p037-054.md:p.45 (정정) | 두 모델의 파고 과소·과대 예측을 한정 없이 적었다. | 원문의 `Basically`를 복원했다. | p.45 본문 `Basically, the two models underpredict the peak wave height at breaking and overpredict wave height inside of the surfzone.` |
| p037-054.md:p.46 (정정) | 쪽 첫머리에 절 5.1과 `input.txt`를 붙였다. | 그 쪽에 없는 절 번호·파일명을 삭제했다. 입력 예시의 계속임은 유지했다. | p.46 첫 입력 구획 `TIME`, `DX = 0.025`, `DY = 0.2`. |
| p037-054.md:p.47 (정정) | 쪽 첫머리에 절 5.1을 붙였다. | 그 쪽에 없는 절 번호를 삭제했다. 실제 인쇄된 절 5.2는 유지했다. | p.47 첫 행 `CFL = 0.5`. 아래 절 제목 `5.2 Random wave shoaling and breaking on a slope (in directory /mase_kirby_1d/)`. |
| p037-054.md:p.48 (정정) | 쪽 첫머리에 절 5.2를 붙였다. | 그 쪽에 없는 절 번호를 삭제했다. | p.48 첫 본문 행 `1:20 on the right.`. 이 쪽에는 절 번호·제목이 없다. |
| p037-054.md:p.48 (보완) | 정규화 왜도·비대칭도 식의 적용 대상이 빠졌다. | 계측·모델 수면고 시계열 모두가 계산 대상임을 추가했다. | p.48 식 (106) 앞 `were calculated for both measured and modeled time series of surface elevation`. |
| p037-054.md:p.49 (정정) | 쪽 첫머리에 절 5.2를 붙였다. | 그 쪽에 없는 절 번호를 삭제했다. | p.49 Figure 4·5와 캡션. 절 번호·제목은 없다. |
| p037-054.md:p.50 (정정) | 쪽 첫머리에 절 5.2를 붙였다. 그림의 일부 수심을 쇄파대로 귀속했다. | 그 쪽에 없는 절 번호를 삭제했다. 그 쪽에 없는 쇄파대 귀속을 삭제했다. | p.50 Figure 6. 가로축은 `Water Depth (cm)`다. 쇄파대 경계는 표시하지 않는다. |
| p037-054.md:p.51 (정정) | 쪽 첫머리에 절 5.2를 붙였다. | 그 쪽에 없는 절 번호를 삭제했다. | p.51 첫 본문 행 `Some necessary definitions in the input file, input.txt, are`. |
| p037-054.md:p.52 (정정) | 쪽 첫머리에 절 5.2를 붙였다. 쪽 끝의 `Detailed` 뒤 내용을 기하 설명으로 완성했다. | 그 쪽에 없는 절 번호를 삭제했다. 쪽 끝은 보이는 단어까지만 적었다. | p.52 첫 행 `A_sponge = 5.0`. 실제 절 제목은 5.3이다. 마지막 인쇄 단어는 `Detailed`다. |
| p037-054.md:p.52 (보완) | 이전 FUNWAVE 버전의 실측 파고 재현 성능을 말한 출처가 빠졌다. | 해당 성능을 제시한 출처 `Kirby et al. (1998)`을 복원했다. | p.52 본문 `Kirby et al. (1998) showed that the previous version of FUNWAVE accurately reproduces measured wave heights in the experiments.` |
| p037-054.md:p.53 (정정) | 그 쪽에 없는 절 5.3을 붙였다. Figure 7의 아래쪽 세로축 눈금을 `−5`로 적었다. | 절 번호를 삭제했다. 눈금을 인쇄값 `5`로 고쳤다. 눈금 순서의 불일치를 쪽 행과 끝 절에 적었다. | p.53 Figure 7의 세로축 하단 두 번째 눈금 `5`. 아래 눈금은 `−10`이다. 위 눈금은 `0`이다. |
| p037-054.md:p.54 (정정) | 쪽 첫머리에 절 5.3을 붙였다. | 그 쪽에 없는 절 번호를 삭제했다. | p.54 Figure 8과 캡션. 절 번호·제목은 없다. |
| p055-072.md:p.56 (정정) | 쪽 첫 입력을 그 쪽에 없는 `PHYSICS` 제목으로 묶었다. | 그 쪽에 없는 제목을 삭제했다. 앞 입력 예시의 계속임은 유지했다. | p.56 첫 두 행 `SWE_ETA_DEP = 0.80`, `Cd = 0.0`. 첫 인쇄 구획 제목은 `NUMERICS`다. |
| p055-072.md:p.57 (정정) | 쪽 첫머리에 5.4절을 붙였다. | 그 쪽에 없는 절 번호를 삭제했다. | p.57 Figure 9와 캡션. 절 번호·제목은 없다. |
| p055-072.md:p.58 (정정) | 쪽 첫머리에 5.4절을 붙였다. 그 쪽에 없는 `Transect 4`를 비교 위치로 적었다. | 그 쪽에 없는 절 번호와 측선 번호를 삭제했다. | p.58 Figure 10·11과 캡션. 절 번호와 `Transect 4` 표기는 없다. |
| p055-072.md:p.59 (정정) | 5.4절의 쇄파 시험이라고 붙였다. 첫 입력에 `DEPTH` 구획 제목을 붙였다. | 그 쪽에 없는 절 번호·시험 명칭·구획 제목을 삭제했다. | p.59 첫 행 `DEPTH_FILE = ../depth/dep_ny501mx760.dat`. 첫 구획 제목은 `DIMENSION`이다. |
| p055-072.md:p.60 (정정) | 그 쪽에 없는 5.4절을 붙였다. Dingemans의 비교 대상을 모델만으로 적었다. 재측정의 `all`을 빠뜨렸다. | 5.4절 표기를 삭제했다. 비교 대상에 두 실험자료를 명시했다. 모든 기존 계측지점을 재측정했다는 범위를 복원했다. | p.60 본문 `Comparisons between several weakly nonlinear Boussinesq-type models and experimental data by Beji and Battjes (1993) and Luth et al. (1994)`; `all gauge locations ... were repeated`. |
| p055-072.md:p.60 (보완) | 계측지점을 부르는 방식과 위치 예시가 빠졌다. | 위치로 지칭한다는 설명과 `gauge 2.0 m`, `gauge 15.7 m`를 추가했다. | p.60 마지막 문장 괄호 `to which we refer by their location, e.g., gauge 2.0 m, gauge 15.7 m, etc.`. |
| p055-072.md:p.61 (정정) | 쪽 첫머리에 5.5절을 붙였다. | 그 쪽에 없는 절 번호를 삭제했다. | p.61 Figure 12와 본문·입력 목록. 절 번호·제목은 없다. |
| p055-072.md:p.62 (정정) | 쪽 첫머리에 5.5절의 Case A 입력이라고 붙였다. 스크립트 목록의 예시 성격을 명시하지 않았다. | 그 쪽에 없는 절 번호와 입력 사례 귀속을 삭제했다. `such as`를 복원했다. | p.62 첫 구획 `SPONGE LAYER`. 마지막 설명 `matlab scrips to plot model/data comparisons such as ...`. |
| p055-072.md:p.63 (정정) | 쪽 첫머리에 5.5절을 붙였다. | 그 쪽에 없는 절 번호를 삭제했다. | p.63 Figure 13과 캡션. 절 번호·제목은 없다. |
| p055-072.md:p.64 (정정) | 쪽 첫머리에 5.5절을 붙였다. 세로축 눈금을 좌우 열 구분 없이 적었다. | 그 쪽에 없는 절 번호를 삭제했다. 왼쪽 열의 다섯 눈금과 오른쪽 열의 세 눈금을 구분했다. | p.64 Figure 14. 왼쪽 열 눈금 `−0.04, −0.02, 0, 0.02, 0.04`. 오른쪽 열 눈금 `−0.02, 0, 0.02`. |
| p055-072.md:p.65 (정정) | Figure 15의 빨간 선을 파선으로 적었다. | 긴 선분과 점이 반복되는 일점쇄선으로 고쳤다. | p.65 Figure 15의 빨간 곡선. 특히 Gauge 6의 봉우리 뒤 구간에서 긴 선분과 점의 반복이 보인다. |
| p055-072.md:p.65 (보완) | 검증 연구의 Liu·Chen 인용이 빠졌다. 파고계의 측정 대상을 생략했다. 캡션·그림·본문의 상충을 명시하지 않았다. | `Liu et al 1995`와 `Chen et al, 2000`을 복원했다. 수면고 시계열 측정을 추가했다. 그림 내용과 캡션의 모순 및 시간 설명과 거리축 표기의 불일치를 쪽 행과 끝 절에 적었다. | p.65 본문 `nonlinear shallow water equations (Liu et al 1995) and Boussinesq equations (Chen et al, 2000)`; `Water-surface time histories were measured with 27 wave gages`. Figure 15 캡션 `View of conical island(top) and basin(bottom)`과 네 그래프·`x (m)` 축. |
| p055-072.md:p.66 (정정) | 그 쪽에 없는 5.6절을 붙였다. 빨간 곡선을 파선으로 적었다. | 절 번호를 삭제했다. 빨간 곡선을 일점쇄선으로 고쳤다. | p.66 Figure 16·17의 빨간 곡선은 긴 선분과 점의 반복이다. 절 번호·제목은 없다. |
| p055-072.md:p.66 (보완) | 캡션과 그림을 따로 적었다. 끝 절에 모순을 명시하지 않았다. Figure 16의 단위 불일치도 쪽 행에서 빠졌다. | 두 그림의 캡션·실제 내용 모순을 쪽 행과 끝 절에 명시했다. Figure 16의 `cm`·`m` 불일치도 양쪽에 적었다. | p.66 Figure 16 캡션 `Definition sketch for conical island. All dimensions are in cm`; Figure 17 캡션 `Schematic gauge locations around the conical island`. 실제 두 그림은 `eta (m)`·`x (m)` 축의 파고계 그래프다. |
| p055-072.md:p.67 (정정) | 이 쪽의 내용을 5.6절로 표시했다. | 이 쪽에 인쇄되지 않은 절 번호를 삭제했다. | p.67 전체. Figure 18과 Table 1은 있으나 5.6절 표제는 없다. |
| p055-072.md:p.68 (정정) | 이 쪽의 내용을 5.6절로 표시했다. | 이 쪽에 인쇄되지 않은 절 번호를 삭제했다. | p.68 전체. Figure 19와 Figure 20만 있으며 5.6절 표제는 없다. |
| p055-072.md:p.69 (정정) | 이 쪽의 입력 예시를 5.6절로 표시했다. | 이 쪽에 인쇄되지 않은 절 번호를 삭제했다. | p.69 전체. TIME부터 WET-DRY까지 입력 목록만 있다. |
| p055-072.md:p.70 (정정) | 앞 입력 예시에 인쇄되지 않은 5.6절 번호를 붙였다. 최근 측정했다는 시점과 여러 위치라는 범위 및 산란 양상이 분명히 보인다는 표현을 누락했다. | 5.6절 번호를 삭제했다. recently, many locations, clearly의 뜻을 복원했다. | p.70 OUTPUT 및 5.7절 첫째·셋째 문단: measured recently; at many locations; clearly seen. |
| p055-072.md:p.70 (보완) | seven gauges, NumberStations = 16, 저장 파일 범위 및 sta_0022를 각각 적었지만 모순을 명시하지 않았다. 해빈과 대의 연결 및 Figure 21 기호의 비교 목적과 마지막 전파 설명이 빠졌다. | 관측소 수의 모순과 저장 범위를 벗어난 파일 번호를 쪽 행과 끝 절에 명시했다. 해빈과 대의 연결 및 모델·자료 비교에 쓰인 측정 위치와 전파 예측 설명을 보완했다. | p.70 OUTPUT 및 바로 아래 문단: NumberStations = 16; seven gauges; sta_0001 ... sta_0016; sta_0022 (gauge 22). 5.7절: connected to; used for model/data comparisons; successfully predicts the solitary wave propagation. |
| p055-072.md:p.71 (정정) | 5.7절 번호를 붙였다. 대와 원뿔형 섬이라는 앞 쪽의 지형 설명을 가져왔다. | 이 쪽에 인쇄되지 않은 절 번호를 삭제했다. 지형 설명을 이 쪽 캡션의 수심지형 등고선으로 한정했다. | p.71 Figure 21 및 캡션: Bathymetry contours (in meters) and measurement locations used in model/data comparisons. |
| p055-072.md:p.72 (정정) | 5.7절 번호와 대에 도달하는 파면이라는 앞 쪽의 설명을 붙였다. 섬이라는 이름을 사용했다. | 이 쪽에 인쇄되지 않은 절 번호와 대에 도달한다는 설명을 삭제했다. 그림 설명을 보이는 파면과 원뿔형 지형으로 한정했다. | p.72 Figure 22의 세 패널 및 캡션. 캡션에는 계산 수면과 세 시각만 적혀 있다. |
| p055-072.md:p.72 (보완) | y축 하단의 15와 그 위 -10을 적었지만 눈금 순서의 불일치를 명시하지 않았다. | 하단의 15가 나머지 눈금의 증가 순서에 맞지 않는다는 사실을 쪽 행과 끝 절에 명시했다. | p.72 Figure 22의 세 패널 y축: 아래에서 위로 15, -10, -5, 0, 5, 10, 15. |

정정 28, 보완 7, 이상 없음 8

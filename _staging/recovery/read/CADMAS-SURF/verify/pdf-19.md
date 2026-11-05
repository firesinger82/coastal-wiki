# CADMAS-2F_Manural_English.pdf p.127–144 전수 대조

대조일은 2026-11-04다.
대조 대상은 [p127-144.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf/p127-144.md)다.
원본 PDF는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf`다.
쪽 번호는 PDF 쪽 번호다.
이미지 디렉터리는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`다.
아래 근거의 PNG 파일명은 이 디렉터리를 기준으로 한다.

지정된 300 dpi PNG를 이미지 보기 도구로 모두 열었다.
대조한 쪽 수는 p.127–144의 18쪽이다.
본문을 고친 쪽 수는 p.131·133·140의 3쪽이다.
정정 표기가 있는 쪽은 p.133의 1쪽이다.
보완 표기가 있는 쪽은 p.131·133·140의 3쪽이다.
p.133은 정정과 보완에 각각 포함된다.
일치 표기가 있는 쪽은 나머지 15쪽이다.
표의 쪽 행 수는 기존 18행을 유지했다.
기존 frontmatter에는 요청된 `verified_by` 한 줄만 추가했다.

## 쪽별 대조

| 쪽 | 이미지 | 결과 |
|---|---|---|
| p.127 | `cad-2f-manual-127.png` 직접 열람 | 일치 |
| p.128 | `cad-2f-manual-128.png` 직접 열람 | 일치 |
| p.129 | `cad-2f-manual-129.png` 직접 열람 | 일치 |
| p.130 | `cad-2f-manual-130.png` 직접 열람 | 일치 |
| p.131 | `cad-2f-manual-131.png` 직접 열람 | 보완 |
| p.132 | `cad-2f-manual-132.png` 직접 열람 | 일치 |
| p.133 | `cad-2f-manual-133.png` 직접 열람 | 정정·보완 |
| p.134 | `cad-2f-manual-134.png` 직접 열람 | 일치 |
| p.135 | `cad-2f-manual-135.png` 직접 열람 | 일치 |
| p.136 | `cad-2f-manual-136.png` 직접 열람 | 일치 |
| p.137 | `cad-2f-manual-137.png` 직접 열람 | 일치 |
| p.138 | `cad-2f-manual-138.png` 직접 열람 | 일치 |
| p.139 | `cad-2f-manual-139.png` 직접 열람 | 일치 |
| p.140 | `cad-2f-manual-140.png` 직접 열람 | 보완 |
| p.141 | `cad-2f-manual-141.png` 직접 열람 | 일치 |
| p.142 | `cad-2f-manual-142.png` 직접 열람 | 일치 |
| p.143 | `cad-2f-manual-143.png` 직접 열람 | 일치 |
| p.144 | `cad-2f-manual-144.png` 직접 열람 | 일치 |

p.127의 기호 높이는 원본 해상도로 다시 확인했다.
p.131의 `PL` 기본값은 원본 해상도로 다시 확인했다.
p.132의 독립식과 분리된 `1=`는 원본 해상도로 다시 확인했다.
p.133의 `Fixed Velocoty` 철자는 원본 해상도로 다시 확인했다.
p.140의 와도 식과 병렬 계산 수치는 원본 해상도로 다시 확인했다.
p.133의 철자는 텍스트 추출본과도 대조했다.
판정 근거는 쪽 이미지다.

## 정정·보완 목록

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.131 | `V1`·`V2` 설명은 영어 인용만 있었다. | 보완: `V1`은 V1 구조 안의 물 비율이라는 뜻을 덧붙였다. `V2`는 V2 형상에 따른 물 비율이라는 뜻을 덧붙였다. | `cad-2f-manual-131.png` 하단 변수 표의 `Ratio of water in V1 structure [-]`와 `Ratio of water according to V2 shape [-]`. |
| p.133 | 유체의 고정 속도 항목을 `Fixed Velocity`로 적었다. | 정정: 인쇄된 `Fixed Velocoty`로 바꿨다. 원문의 철자를 끝 절에도 기록했다. | `cad-2f-manual-133.png`의 유체·기체 목록은 모두 `Fixed Velocoty`로 인쇄한다. |
| p.133 | 기체 경계조건은 입력 키워드만 나열했다. | 보완: `VG SLIP`의 `Slip`을 미끄럼으로 설명했다. `VG NON-S`의 `Non slip`을 비미끄럼으로 설명했다. `VG FIX-V [BU] [BV] [BW]`의 `Fixed Velocoty`를 고정 속도로 설명했다. `VG FREE`의 `Free`를 자유로 설명했다. | `cad-2f-manual-133.png`의 `Velocity and pressure boundary condition for gas` 아래 네 항목. |
| p.133 | `Insulation (-A)`와 `Adiabatic (+ A)`의 한국어 뜻이 없었다. | 보완: 두 항목에 단열이라는 뜻을 덧붙였다. | `cad-2f-manual-133.png` 하단 `Temperature boundary condition` 목록. |
| p.140 | `'C' [LC]` 항목을 농도로만 설명했다. | 보완: `LC is below`를 인용했다. `LC`의 설명이 아래에 있다는 뜻을 덧붙였다. | `cad-2f-manual-140.png` 상단의 `'C' [LC]: concentration (LC is below)`. |

## 유지한 원문 표기

각 쪽의 본문 문단과 입력 구문을 대조했다.
변수 표의 이름·설명·형·기본값·제한을 대조했다.
단위와 조건문을 대조했다.
지정 범위에는 그림이 없다.
입력 표에는 표 번호와 캡션이 없다.
독립식은 p.132의 1개와 p.140의 3개다.
독립식 4개의 기호와 식 번호 부재는 기존 기록과 일치한다.
앞 쪽의 절에 속하는 내용은 기존 기록의 계속 표기를 유지했다.
앞 쪽에서 이어진 제목을 해당 쪽의 새 제목으로 바꾼 항목은 없다.
p.135의 `ファイル制御データ`와 `リスタートファイル制御データ`는 기존 인용과 일치한다.
두 제목의 기존 한국어 뜻은 각각 파일 제어 데이터와 재시작 파일 제어 데이터다.
p.140의 `オプションデータ`는 기존 인용과 일치한다.
이 제목의 기존 한국어 뜻은 옵션 데이터다.
`ICGMAT`와 `ICGMAX`의 차이는 p.128 이미지에도 있다.
`LC` 행의 `LS` 표기는 해당 이미지에도 있다.
p.131의 `PL` 기본값 `1 0 D - 4`에는 소수점을 보충하지 않았다.
p.137의 `[KC]`와 끝점 상한의 `<`는 인쇄대로 유지했다.
p.138의 시계열 표에서 `TSTEP` 형은 `*8`로 유지했다.
p.140의 와도 식에서 `@`를 미분 기호로 바꾸지 않았다.
p.140의 최댓값 문장 `The maximum value in parallel calculation is -1. Limited to 0 D + 30`은 유지했다.
p.142의 구문에 없는 `RELAX`는 변수 표에만 기록했다.

열지 못한 이미지는 없다.
판독을 유보한 항목은 없다.
마지막 집계는 쪽 행의 검증 표기를 기준으로 한다.
정정과 보완의 집계는 p.133에서 중복된다.

정정 1, 보완 3, 일치 15

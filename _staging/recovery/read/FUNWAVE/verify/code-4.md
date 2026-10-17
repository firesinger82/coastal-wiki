# FUNWAVE code-4 전수 검증

대상 기록의 frontmatter `file:`이 가리키는 원문을 모든 구간 행과 대조했다.
원문은 `nl -ba <원문> | sed -n 'A,Bp'`로 구간마다 한 번에 200행 이하씩 열었다.
대상 원문의 총 3,508행은 아래 표의 원문 행 수를 합한 값이다.
각 기록의 구간 아래에 있는 코드 사실 목록도 원문과 대조했다.
`init.F.md`의 부가 인용을 확인하기 위해 `bc.F` 616–644행을 추가로 열었다.
이 부가 인용은 대상 원문 행 수에 포함하지 않았다.
대상 원문에는 CUDA Fortran 커널 지시·기동문과 `!$acc`·`!$omp` 지시가 없다.
모델은 실행하지 않았다.
원문·노트·git은 수정하지 않았다.
대상 기록의 frontmatter와 구간 경계는 유지했다.
정정·보완 건수는 해당 표지가 붙은 기록의 구간 행 수로 센다.
한 구간에 두 표지가 있으면 각 유형에 한 건씩 센다.
이상 없음은 수정이 필요하지 않은 구간 행 수로 센다.

| 기록 | 상태 | 대조한 구간 행 수 | 대조한 원문 행 수 |
|---|---|---:|---:|
| FUNWAVE-GPU/src/fluxes.F.md | 완료 | 51 | 1696 |
| FUNWAVE-GPU/src/init.F.md | 완료 | 37 | 1216 |
| FUNWAVE-GPU/src/init_gpu.F.md | 완료 | 15 | 596 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| FUNWAVE-GPU/src/fluxes.F.md:52–90 | 주석 처리된 FOURTHMIN 조건을 인용하지 않음. | 보완: 주석 조건을 원문으로 추가하고 활성 분기 종료 행을 명시함. | fluxes.F:62, 79, 85 |
| FUNWAVE-GPU/src/fluxes.F.md:136–168 | 좌우 상태 복사를 서술만 함. | 보완: FOUT의 두 대입문을 원문으로 인용함. | fluxes.F:153, 155 |
| FUNWAVE-GPU/src/fluxes.F.md:205–238 | DOUT의 0 설정과 주석 식을 인용하지 않음. 전처리 종료 행을 생략함. | 보완: DOUT 대입과 주석 식을 인용함. 전처리 종료 행을 명시함. | fluxes.F:212, 227, 230, 232–233 |
| FUNWAVE-GPU/src/fluxes.F.md:259–291 | DOUT의 0 설정과 주석 식을 인용하지 않음. 전처리 종료 행을 생략함. | 보완: DOUT 대입과 주석 식을 인용함. 전처리 종료 행을 명시함. | fluxes.F:266, 281, 284, 286 |
| FUNWAVE-GPU/src/fluxes.F.md:292–317 | 전처리 종료를 요약만 함. | 보완: 종료 지시와 행 번호를 인용함. | fluxes.F:299 |
| FUNWAVE-GPU/src/fluxes.F.md:346–368 | 가상 셀 인덱스를 가장 가까운 내부 열·행으로만 요약함. | 보완: 각 복사 인덱스와 J 루프 범위를 원문으로 인용함. | fluxes.F:347–365 |
| FUNWAVE-GPU/src/fluxes.F.md:369–392 | y 방향 가상 셀 복사를 요약만 함. | 보완: 가상 셀 루프 범위와 복사 대입문을 인용함. | fluxes.F:383–390 |
| FUNWAVE-GPU/src/fluxes.F.md:393–417 | 가상 셀 인덱스를 가장 가까운 내부 열로만 요약함. | 보완: 각 복사 대입문의 인덱스를 인용함. | fluxes.F:396–401 |
| FUNWAVE-GPU/src/fluxes.F.md:418–458 | 마스크 복사 식과 종료 지시를 인용하지 않음. | 보완: 마스크 인덱스와 IF·전처리 종료를 원문으로 명시함. | fluxes.F:425, 431–435, 456–457 |
| FUNWAVE-GPU/src/fluxes.F.md:459–488 | 두 플래그 미정의 분기의 PL·PR 대입을 인용하지 않음. | 보완: PL·PR 복사 대입문을 인용함. | fluxes.F:482–483 |
| FUNWAVE-GPU/src/fluxes.F.md:489–521 | 중첩 전처리 종료를 묶어서 요약함. | 보완: ZALPHA·CARTESIAN의 종료 행을 각각 인용함. | fluxes.F:519–520 |
| FUNWAVE-GPU/src/fluxes.F.md:522–543 | 전처리 종료 지시를 인용하지 않음. | 보완: 종료 지시를 인용함. | fluxes.F:541 |
| FUNWAVE-GPU/src/fluxes.F.md:544–564 | IF와 전처리 종료를 묶어서 요약함. | 보완: IF·CARTESIAN 종료 행을 각각 명시함. | fluxes.F:562–563 |
| FUNWAVE-GPU/src/fluxes.F.md:565–590 | QL·QR 복사와 중첩 전처리 종료를 요약만 함. | 보완: 대입문과 각 종료 행을 인용함. | fluxes.F:584–588 |
| FUNWAVE-GPU/src/fluxes.F.md:591–611 | 전처리 종료 지시를 인용하지 않음. | 보완: 종료 지시를 인용함. | fluxes.F:609 |
| FUNWAVE-GPU/src/fluxes.F.md:612–648 | 중첩 전처리 종료를 묶어서 요약함. | 보완: 각 전처리 종료 지시와 행을 인용함. | fluxes.F:642–643 |
| FUNWAVE-GPU/src/fluxes.F.md:649–705 | 전처리 종료와 경계 상태 복사를 인용하지 않음. | 보완: 각 전처리 종료 행과 경계 대입문을 인용함. | fluxes.F:668, 687, 696–698 |
| FUNWAVE-GPU/src/fluxes.F.md:706–759 | 전처리 종료와 경계 상태 복사를 인용하지 않음. | 보완: 각 전처리 종료 행과 경계 대입문을 인용함. | fluxes.F:725, 743, 751–753 |
| FUNWAVE-GPU/src/fluxes.F.md:760–799 | 전처리 종료와 마스크 인덱스 대입을 인용하지 않음. | 보완: 종료 지시와 마스크 대입문을 인용함. | fluxes.F:780, 786–790 |
| FUNWAVE-GPU/src/fluxes.F.md:800–829 | 실행 호출·ENDIF까지 주석·빈 줄로 묶음. IF 종료 행을 생략함. | 정정·보완: 주석 범위에서 808–809행을 제외함. IF 종료와 유지되는 전처리 조건을 명시함. | fluxes.F:803–814 |
| FUNWAVE-GPU/src/fluxes.F.md:830–865 | IF 뒤의 식이 속한 전처리 범위를 모호하게 씀. 복사 식을 생략함. | 정정·보완: CARTESIAN 미정의·ZALPHA 정의 조건을 명시함. IF·전처리 종료와 복사 대입을 추가함. | fluxes.F:803, 830–863 |
| FUNWAVE-GPU/src/fluxes.F.md:866–896 | 전처리 종료를 인용하지 않음. | 보완: 종료 지시와 행 번호를 인용함. | fluxes.F:885 |
| FUNWAVE-GPU/src/fluxes.F.md:897–920 | DISPERSION 종료 행을 생략함. | 보완: IF 종료 행과 유지되는 전처리 조건을 명시함. | fluxes.F:897–905 |
| FUNWAVE-GPU/src/fluxes.F.md:921–957 | IF 뒤의 식이 속한 전처리 범위를 모호하게 씀. 복사 식을 생략함. | 정정·보완: CARTESIAN 미정의·ZALPHA 정의 조건을 명시함. IF·전처리 종료와 복사 대입을 추가함. | fluxes.F:897, 921–955 |
| FUNWAVE-GPU/src/fluxes.F.md:958–982 | 전처리 종료 지시를 인용하지 않음. | 보완: 종료 지시를 인용함. | fluxes.F:977 |
| FUNWAVE-GPU/src/fluxes.F.md:983–1034 | Din 초기값과 전처리 종료를 인용하지 않음. | 보완: 초기값과 종료 지시를 인용함. | fluxes.F:1003, 1012 |
| FUNWAVE-GPU/src/fluxes.F.md:1035–1067 | 마스크 분기의 복사·0 설정·주석 등식과 바깥 루프 조건을 생략함. | 보완: 해당 대입과 주석 등식을 인용함. 각 블록의 조건과 종료를 명시함. | fluxes.F:1013–1014, 1038–1066 |
| FUNWAVE-GPU/src/fluxes.F.md:1101–1152 | Din 초기값과 전처리 종료를 인용하지 않음. | 보완: 초기값과 종료 지시를 인용함. | fluxes.F:1121, 1130 |
| FUNWAVE-GPU/src/fluxes.F.md:1153–1186 | 마스크 분기의 복사·0 설정·주석 등식과 바깥 루프 조건을 생략함. | 보완: 해당 대입과 주석 등식을 인용함. 각 블록의 조건과 종료를 명시함. | fluxes.F:1131–1132, 1156–1184 |
| FUNWAVE-GPU/src/fluxes.F.md:1263–1296 | 마스크 복사를 요약만 함. | 보완: 각 마스크 인덱스 대입문을 인용함. | fluxes.F:1281–1285 |
| FUNWAVE-GPU/src/fluxes.F.md:1297–1320 | DISPERSION 밖이라고만 써서 남는 전처리 범위가 모호함. | 정정·보완: IF 종료 행을 추가함. 플럭스 식의 CARTESIAN 조건을 명시함. | fluxes.F:1297–1319 |
| FUNWAVE-GPU/src/fluxes.F.md:1321–1355 | IF 뒤의 식이 속한 전처리 범위를 모호하게 씀. 복사 식을 생략함. | 정정·보완: CARTESIAN 미정의·ZALPHA 정의 조건을 명시함. IF·전처리 종료와 복사 대입을 추가함. | fluxes.F:1297, 1321–1354 |
| FUNWAVE-GPU/src/fluxes.F.md:1356–1384 | 전처리 종료를 인용하지 않음. | 보완: 종료 지시와 행 번호를 인용함. | fluxes.F:1373 |
| FUNWAVE-GPU/src/fluxes.F.md:1385–1408 | IF 밖이라고만 써서 남는 전처리 범위가 모호함. | 정정·보완: IF 종료 행을 추가함. 플럭스 식의 CARTESIAN 조건을 명시함. | fluxes.F:1385–1407 |
| FUNWAVE-GPU/src/fluxes.F.md:1409–1444 | IF 뒤의 식이 속한 전처리 범위를 모호하게 씀. 복사 식을 생략함. | 정정·보완: CARTESIAN 미정의·ZALPHA 정의 조건을 명시함. IF·전처리 종료와 복사 대입을 추가함. | fluxes.F:1385, 1409–1443 |
| FUNWAVE-GPU/src/fluxes.F.md:1445–1467 | 전처리 종료 지시를 인용하지 않음. | 보완: 종료 지시를 인용함. | fluxes.F:1462 |
| FUNWAVE-GPU/src/fluxes.F.md:1468–1512 | Din 초기값을 요약만 함. | 보완: 초기 대입문을 원문으로 인용함. | fluxes.F:1487 |
| FUNWAVE-GPU/src/fluxes.F.md:1513–1544 | 복사·0 설정·주석 등식과 바깥 루프 조건을 생략함. | 보완: 해당 식을 인용함. 조건·루프의 범위와 종료를 명시함. | fluxes.F:1488, 1492, 1516–1543 |
| FUNWAVE-GPU/src/fluxes.F.md:1545–1587 | TMP 복사·VAN 초기값과 바깥 루프 조건을 인용하지 않음. | 보완: 각 대입문을 인용함. 루프 조건과 종료 행을 명시함. | fluxes.F:1488, 1548–1579 |
| FUNWAVE-GPU/src/fluxes.F.md:1588–1627 | Din 초기값을 요약만 함. | 보완: 초기 대입문을 원문으로 인용함. | fluxes.F:1602 |
| FUNWAVE-GPU/src/fluxes.F.md:1628–1659 | 복사·0 설정·주석 등식과 바깥 루프 조건을 생략함. | 보완: 해당 식을 인용함. 조건·루프의 범위와 종료를 명시함. | fluxes.F:1603, 1607, 1631–1658 |
| FUNWAVE-GPU/src/fluxes.F.md:1660–1696 | TMP 복사·VAN 초기값과 바깥 루프 조건을 인용하지 않음. | 보완: 각 대입문을 인용함. 루프 조건과 종료 행을 명시함. | fluxes.F:1603, 1663–1694 |
| FUNWAVE-GPU/src/init.F.md:116–162 | 중첩 전처리 종료를 인용하지 않음. | 보완: 각 ZALPHA·CARTESIAN·ITERATION 종료 지시를 인용함. | init.F:129, 133, 155, 158, 162 |
| FUNWAVE-GPU/src/init.F.md:163–190 | HeightMax·WaveMaker_Mass·점성 배열의 0 초기값을 요약만 함. | 보완: 각 초기 대입문을 인용함. | init.F:166, 169, 183, 188 |
| FUNWAVE-GPU/src/init.F.md:191–210 | 출력 극값 배열의 0 초기값을 요약만 함. | 보완: 각 초기 대입문을 인용함. | init.F:193, 197, 201, 205 |
| FUNWAVE-GPU/src/init.F.md:211–239 | 선언 전처리 종료를 인용하지 않음. | 보완: INTEL·PARALLEL 또는 MGPU 선언 분기의 종료 지시를 인용함. | init.F:226, 233 |
| FUNWAVE-GPU/src/init.F.md:240–292 | 바깥 전처리 조건을 이름만 씀. 유령 셀 복사를 요약만 함. | 보완: 바깥 조건과 직렬 분기 범위를 명시함. 복사 인덱스와 종료 지시를 인용함. | init.F:235, 240–291 |
| FUNWAVE-GPU/src/init.F.md:293–319 | 바깥 조건과 주석 위도 식·종료 지시를 인용하지 않음. | 보완: 바깥 조건·주석 식·각 블록 종료를 원문으로 인용함. | init.F:235, 240, 302–318 |
| FUNWAVE-GPU/src/init.F.md:320–369 | 평균장·도함수·면 상태의 0 초기값을 요약만 함. | 보완: ZERO·정수 0·0.0_SP를 구별하여 모든 초기 대입문을 인용함. | init.F:328–369 |
| FUNWAVE-GPU/src/init.F.md:370–400 | 미분장·시간장·PL 초기값과 전처리 종료를 요약만 함. | 보완: 전처리 종료와 모든 초기 대입문을 인용함. | init.F:371–400 |
| FUNWAVE-GPU/src/init.F.md:401–457 | 면 상태·운동량·마스크·카운터의 초기값을 요약만 함. | 보완: 각 초기 대입문과 CARTESIAN 종료를 인용함. | init.F:401–454 |
| FUNWAVE-GPU/src/init.F.md:458–489 | 주석 좌표 식·기준 좌표 초기값·전처리 종료를 인용하지 않음. | 보완: 주석 식과 초기값·각 종료 지시를 인용함. | init.F:463, 468–487 |
| FUNWAVE-GPU/src/init.F.md:490–517 | 주석 좌표 식·기준 좌표 초기값·전처리 종료를 인용하지 않음. | 보완: 주석 식과 초기값·각 종료 지시를 인용함. | init.F:492, 497–514 |
| FUNWAVE-GPU/src/init.F.md:518–546 | 카운터·DT·쇄파 나이 초기값을 인용하지 않음. 주석의 등식 조건을 요약함. | 보완: 각 대입문과 전처리 종료를 인용함. Gamma3 주석의 0 조건을 구분함. | init.F:519–544 |
| FUNWAVE-GPU/src/init.F.md:547–572 | b2 대입과 중첩 전처리 종료를 인용하지 않음. | 보완: b2 대입문과 각 종료 지시를 인용함. | init.F:552, 568, 570–571 |
| FUNWAVE-GPU/src/init.F.md:573–604 | 직렬 오류 메시지·종료 지시를 요약함. MYID 조건의 범위를 명시하지 않음. | 보완: WRITE·MPI_FINALIZE·STOP의 실행 순서와 MYID 범위를 명시함. 전처리 종료를 인용함. | init.F:580–603 |
| FUNWAVE-GPU/src/init.F.md:605–638 | 수심 복사·초기값·경사 시작 인덱스를 인용하지 않음. 분기 관계를 명시하지 않음. | 보완: 각 대입과 인덱스를 인용함. 독립된 수심 조건과 ELSE 부재를 명시함. | init.F:575, 605–637 |
| FUNWAVE-GPU/src/init.F.md:639–669 | 바깥 전처리 조건을 이름만 씀. 수심 초기값·경사 시작 인덱스를 요약함. | 보완: 바깥 조건·각 종료 지시·초기 대입·인덱스를 인용함. | init.F:614, 647, 654–668 |
| FUNWAVE-GPU/src/init.F.md:670–693 | 경계 처리 VTYPE 설정을 인용하지 않음. | 보완: VTYPE 대입문을 원문으로 인용함. | init.F:675 |
| FUNWAVE-GPU/src/init.F.md:694–735 | 주석 수심 재구성 식과 전역 최대값 복사를 인용하지 않음. | 보완: 주석 식·최대값 대입·전처리 종료를 인용함. | init.F:724, 733–734 |
| FUNWAVE-GPU/src/init.F.md:736–776 | Cd 경계 복사·기본값을 인용하지 않음. 직렬 분기 범위가 명시되지 않음. | 보완: 각 대입과 직렬 분기 범위·전처리 및 IF 종료를 명시함. | init.F:740–773 |
| FUNWAVE-GPU/src/init.F.md:801–809 | 바깥 조건을 이름만 씀. 전처리·IF 종료를 묶어서 요약함. | 보완: 바깥 조건식과 각 종료 지시를 인용함. | init.F:799–807 |
| FUNWAVE-GPU/src/init.F.md:810–837 | 전처리·IF 종료를 묶어서 요약함. | 보완: 각 전처리·IF 종료 지시를 인용함. | init.F:818–819, 828–829 |
| FUNWAVE-GPU/src/init.F.md:838–866 | 마찰 감쇠층 초기값을 요약만 함. | 보완: 초기 대입문을 인용함. | init.F:858 |
| FUNWAVE-GPU/src/init.F.md:867–897 | 마스크 대입을 인용하지 않음. DISPERSION 종료 뒤의 범위를 명시하지 않음. | 보완: 마스크 대입과 각 IF 종료를 명시함. Ubar·Vbar가 DISPERSION 밖임을 명시함. | init.F:878–896 |
| FUNWAVE-GPU/src/init.F.md:898–929 | 직렬 오류 처리와 전처리 종료를 요약함. MYID 조건 범위를 명시하지 않음. | 보완: 오류 메시지·MPI_FINALIZE·STOP의 범위와 각 종료 지시를 명시함. | init.F:904–928 |
| FUNWAVE-GPU/src/init.F.md:930–975 | 오류 처리 범위·방파제 배열 크기·초기값·경계 복사를 요약함. | 보완: 오류 처리의 MYID 범위와 배열 식·대입문·종료 지시를 인용함. | init.F:936–974 |
| FUNWAVE-GPU/src/init.F.md:976–1012 | 바깥 IF·전처리 조건을 이름만 씀. 방파제 경계 복사를 요약함. | 보완: 바깥 조건식·복사 인덱스·종료 지시를 인용함. 공통 호출의 IF 범위를 명시함. | init.F:931, 950, 989–1010 |
| FUNWAVE-GPU/src/init.F.md:1013–1038 | 마스크 교환 전처리 종료를 인용하지 않음. | 보완: 종료 지시를 인용함. | init.F:1035 |
| FUNWAVE-GPU/src/init.F.md:1039–1068 | 주의 주석의 예외 조건과 블록 종료를 생략함. | 보완: 주석의 부정·예외를 보존함. 경사 계산과 제한 조건의 범위를 명시함. | init.F:1043–1067 |
| FUNWAVE-GPU/src/init.F.md:1069–1100 | 주석의 정확도 제한과 수심 복사 식·전처리 종료를 요약함. | 보완: 주석의 제한을 명시함. 플래그·각 대입·종료 지시를 인용함. | init.F:1069–1091 |
| FUNWAVE-GPU/src/init.F.md:1101–1143 | 직렬 오류 출력과 전처리 종료를 요약함. MYID 범위를 명시하지 않음. | 보완: 각 오류 메시지·종료 지시를 인용함. MPI_FINALIZE·STOP의 조건 범위를 명시함. | init.F:1120–1142 |
| FUNWAVE-GPU/src/init.F.md:1144–1172 | ETA 판독이 조건 밖이라고만 써서 전처리 범위가 모호함. 오류 처리·초기값을 요약함. | 정정·보완: ETA 판독의 IF·전처리 범위를 구분함. 오류 처리와 U·V 초기값을 인용함. | init.F:1115, 1142–1165 |
| FUNWAVE-GPU/src/init.F.md:1173–1200 | ETA 판독이 조건 밖이라고만 써서 전처리 범위가 모호함. U·V 초기값을 요약함. | 정정·보완: ETA 판독의 IF·전처리 범위를 구분함. U·V 초기값을 인용함. | init.F:1156, 1171–1194 |
| FUNWAVE-GPU/src/init.F.md:1201–1216 | 바깥 전처리·마스크 조건을 이름만 씀. 마스크 기본값을 요약함. | 보완: 바깥 조건식·종료 지시·기본 대입문을 인용함. | init.F:1156, 1171, 1196–1209 |
| FUNWAVE-GPU/src/init_gpu.F.md:16–54 | 호스트 이름 판독까지 노드 내 순위를 얻는 과정으로 묶음. 장치 번호 대입을 인용하지 않음. | 정정·보완: 순위 획득과 호스트 이름 판독을 구분함. 장치 대입과 주석의 버전 정보를 보완함. | init_gpu.F:35–40 |
| FUNWAVE-GPU/src/init_gpu.F.md:55–91 | 경고 내용을 요약만 함. MYID·메모리 조건의 종료와 출력 단위를 생략함. | 보완: 경고 문구·STOP 순서·각 IF 종료·단위 표기를 명시함. | init_gpu.F:68–87 |
| FUNWAVE-GPU/src/init_gpu.F.md:112–195 | DelxU4_d 등 배열을 4차 배열로 해석함. | 정정: 실제 배열 이름을 적음. 선언에서 미분 차수를 단정하지 않음. | init_gpu.F:174–189 |
| FUNWAVE-GPU/src/init_gpu.F.md:196–228 | 장치 배열 할당을 _d 없는 변수명으로 적음. Ubar 계열을 평균속도 갱신 배열로 단정함. | 정정: 실제 할당 대상인 _d 배열 이름으로 고침. 할당된 배열 이름과 크기를 그대로 적음. | init_gpu.F:205–221 |
| FUNWAVE-GPU/src/init_gpu.F.md:229–266 | 점성·출력 배열의 초기값을 요약만 함. | 보완: 각 초기 대입문을 원문으로 인용함. | init_gpu.F:234–261 |
| FUNWAVE-GPU/src/init_gpu.F.md:267–315 | nu_smg_d를 원문 설명 없이 계수로 단정함. 초기값과 주석 대입을 인용하지 않음. | 정정·보완: 변수 이름으로 고침. 모든 초기 대입문과 주석 대입을 인용함. | init_gpu.F:271–315 |
| FUNWAVE-GPU/src/init_gpu.F.md:316–353 | Ubar0_d·Vbar0_d를 평균속도로 단정함. 초기값·주석 대입을 인용하지 않음. | 정정·보완: 실제 변수명으로 고침. 모든 초기 대입과 주석 대입을 인용함. | init_gpu.F:317–349 |
| FUNWAVE-GPU/src/init_gpu.F.md:354–400 | H를 수심합으로 해석함. 장치 복사 대입을 요약만 함. | 정정·보완: 실제 변수 H로 적음. 모든 장치 복사 대입문을 인용함. | init_gpu.F:356–400 |
| FUNWAVE-GPU/src/init_gpu.F.md:401–442 | 장치 복사 대입을 요약만 함. | 보완: 각 플래그 조합에 속하는 모든 장치 대입문을 인용함. | init_gpu.F:401–440 |
| FUNWAVE-GPU/src/init_gpu.F.md:443–488 | 출력·감쇠층·쇄파·방파제·장애물·경사 배열 대입을 요약만 함. | 보완: 조건별 장치 대입문과 AGE_BREAKING_d 초기값을 인용함. | init_gpu.F:444–487 |
| FUNWAVE-GPU/src/init_gpu.F.md:489–539 | CASE DEFAULT 부재와 TriSolver 종료를 명시하지 않음. | 보완: 기본 분기 부재와 mpi_datatype 호출의 IF·전처리 범위를 명시함. | init_gpu.F:489–536 |
| FUNWAVE-GPU/src/init_gpu.F.md:540–561 | 조파기 장치 배열 복사를 요약만 함. | 보완: 조건별 장치 대입문을 인용함. 독립된 세 IF의 ELSE 부재를 명시함. | init_gpu.F:543–561 |
| FUNWAVE-GPU/src/init_gpu.F.md:562–596 | ELSE와 조파기 배열 복사를 인용하지 않음. 중첩 IF 종료를 묶어서 요약함. | 보완: 각 분기의 대입문·ELSE·IF 종료를 인용함. | init_gpu.F:567–593 |

정정 15, 보완 86, 이상 없음 15

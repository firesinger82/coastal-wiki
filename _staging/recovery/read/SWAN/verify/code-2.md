# SWAN 코드 판독 기록 전수 대조

대조일은 2026-10-13이다.
각 기록의 `file:`에 적힌 원문을 구간별 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
각 원문 출력 구간은 200행 이하로 제한했다.
전처리 표시는 `models/SWAN/raw/source_code/swan/switch.pl` 82–105행과 대조했다.
대조 수의 단위는 기록 표의 구간 행이다.
각 기록 끝의 코드 사실 35행도 같은 원문과 대조했다.
정정·보완 수의 단위는 아래 목록의 항목이다.
같은 구간의 정정과 보완은 각각 센다.
코드 사실의 정정 1건도 목록에 포함한다.
마지막 줄의 이상 없음은 수정하지 않은 구간 행의 수이다.

| 기록 | 대조한 구간 행 수 | 대조한 코드 사실 행 수 | 원문 범위 | 수정 없는 구간 행 수 |
|---|---:|---:|---|---:|
| [SwanBpntlist.ftn90.md](../swan/src/SwanBpntlist.ftn90.md) | 16 | 6 | 1–507 | 12 |
| [SwanBraggScat.ftn90.md](../swan/src/SwanBraggScat.ftn90.md) | 41 | 11 | 1–1491 | 35 |
| [SwanCheckGrid.ftn90.md](../swan/src/SwanCheckGrid.ftn90.md) | 6 | 3 | 1–176 | 6 |
| [SwanCompUnstruc.ftn90.md](../swan/src/SwanCompUnstruc.ftn90.md) | 52 | 13 | 1–1678 | 40 |
| [SwanCompdata.ftn90.md](../swan/src/SwanCompdata.ftn90.md) | 3 | 2 | 1–83 | 2 |
| 합계 | 118 | 35 | 원문 3,935행 | 95 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| SwanBpntlist.ftn90.md:246–274 | 정정. 시작점 재방문이면 vc를 vcf로 변경. | 후보가 vcf이고 vcf가 blistot(k-1)과 다를 때만 변경. | 253·265 |
| SwanBpntlist.ftn90.md:306–327 | 보완. 꼭짓점 분기를 닫는다고만 기록. | 251·263·275행 분기 사슬에 ELSE가 없고 322행에서 닫힘을 명시. | 251·263·275·322 |
| SwanBpntlist.ftn90.md:328–353 | 정정. 진단 조건일 때 출력과 RETURN을 수행. | 진단 출력 IF는 347행에서 닫힘. RETURN은 icntfc 조건 안에서 진단 조건과 무관하게 실행. | 336–350 |
| SwanBpntlist.ftn90.md:439–461 | 보완. JJ 분기의 주석 처리된 MSGERR만 설명. | 453·455행 분기 사슬에 ELSE가 없고 457행에서 닫힘을 명시. | 453–457 |
| SwanBraggScat.ftn90.md:863–889 | 정정. 스펙트럼 최대값이 1.e-6보다 크지 않으면 RETURN. | 스펙트럼 절댓값의 최대값에 1.e-6 기준을 적용. | 867–868 |
| SwanBraggScat.ftn90.md:1148–1191 | 정정. 그 밖의 입력·출력 선언 근거를 1167–1184행으로 표기. | 입력·출력 선언은 1150–1165행으로 수정. 1167–1184행은 지역 변수 선언으로 구분. | 1150–1184 |
| SwanBraggScat.ftn90.md:코드 사실 690–706·867–872 | 정정. SWFBXY와 SWFB는 fb 최대값을 검사. | 두 루틴 모두 fb 절댓값의 최대값을 검사. | 690–691·867–868 |
| SwanCompUnstruc.ftn90.md:180–224 | 보완. 반변 기저 벡터의 성분이라고만 설명. | rdx와 rdy의 주석 수식과 성분 번호를 인용. | 203–204 |
| SwanBraggScat.ftn90.md:614–664 | 보완. kd의 주석 수식 인용이 없음. | kd의 주석 정의 = k * d를 인용. | 647 |
| SwanBraggScat.ftn90.md:823–862 | 보완. kd의 주석 수식 인용이 없음. | kd의 주석 정의 = k * d를 인용. | 847 |
| SwanBraggScat.ftn90.md:996–1038 | 보완. 방향 내적·작용밀도 차·파수차를 이름만 요약. | cosdif·edif·fbdif·kd의 주석 수식을 인용. | 1024·1026·1028·1030 |
| SwanBraggScat.ftn90.md:1148–1191 | 보완. 지역 변수의 주석 수식 인용이 없음. | cosdif·edif·fbdif·kd의 주석 수식을 인용. | 1177·1179·1181·1183 |
| SwanBraggScat.ftn90.md:1300–1335 | 보완. 지역 변수의 주석 수식 인용이 없음. | cosdif·edif·fbdif·kd의 주석 수식을 인용. | 1321·1323·1325·1327 |
| SwanCompUnstruc.ftn90.md:319–347 | 정정. 각 꼭짓점에서 한 번 계산하도록 표시. | 주석의 한 번 계산 범위를 각 반복의 각 꼭짓점으로 명시. | 331–332 |
| SwanCompUnstruc.ftn90.md:629–645 | 보완. ITRIAD 값별 할당과 외부 ELSE만 설명. | 내부 630·633·636행 분기 사슬에 ELSE가 없고 639행에서 닫힘을 명시. | 629–643 |
| SwanCompUnstruc.ftn90.md:717–751 | 보완. 초기 추정에서 변경하는 설정만 설명. | 쇄파·바닥 마찰·세 파 상호작용은 여전히 활성일 수 있다는 주석을 보완. | 734 |
| SwanCompUnstruc.ftn90.md:752–776 | 보완. iter=1·2 분기의 종료만 설명. | 731·752행 분기 사슬에 ELSE가 없고 764행에서 닫힘을 명시. | 731·752–764 |
| SwanCompUnstruc.ftn90.md:777–811 | 보완. SWBIPM이 이중위상 관련 자료를 처리한다고만 설명. | 공간 필터 설명과 필터하지 않은 값의 복사 설명을 각각 원문 주석으로 구분. | 781–784 |
| SwanCompUnstruc.ftn90.md:835–850 | 정정. !GRAPH은 -graph, !FXFRO은 -fxfro 선택 시 활성화. | !GRAPH은 -fixfront 미선택 시 활성화. !FXFRO은 -fixfront 선택 시 활성화. | 839–849; swan/switch.pl 24·87–88 |
| SwanCompUnstruc.ftn90.md:1030–1076 | 보완. vu(1)·vu(2) 조건에 따른 link 대입만 설명. | 1049·1054행 분기 사슬에 ELSE가 없고 1059행에서 닫힘을 명시. | 1049–1059 |
| SwanCompUnstruc.ftn90.md:1111–1129 | 보완. ITRIAD 값별 보간·스케일 계수 복사만 설명. | 1113·1116·1123행 분기 사슬에 ELSE가 없고 1128행에서 닫힘을 명시. | 1113–1128 |
| SwanCompUnstruc.ftn90.md:1228–1269 | 정정. DYNDEP·ICUR·PNUMS(8)의 and/or 조건이라고만 설명. | DYNDEP 거짓과 ICUR=0을 AND로 묶은 경우와 int(PNUMS(8))=0인 경우의 OR로 명시. | 1228 |
| SwanCompUnstruc.ftn90.md:1228–1269 | 보완. 각 해법의 sigma 처리·대각 수와 내부 ELSE 부재가 빠짐. | 주석의 theta·sigma 처리와 삼대각·오대각 해법을 명시. 내부 사슬의 ELSE 부재와 1266·1268행 닫힘을 명시. | 1230–1268 |
| SwanCompUnstruc.ftn90.md:1467–1501 | 정정. 첫 반복에서 accur=-9999와 안내를 출력. | accur에 -9999를 대입하는 동작과 안내 출력 동작을 구분. | 1486–1495 |
| SwanCompUnstruc.ftn90.md:1502–1535 | 보완. 수렴 검사 조건과 iterloop 종료만 설명. | 1469·1502행 분기 사슬의 ELSE 부재와 1531행 닫힘을 명시. iterloop의 1533행 닫힘을 명시. | 1469·1502–1534 |
| SwanCompdata.ftn90.md:70–83 | 정정. bvertg를 부분영역의 전역 꼭짓점 번호로 설명. | 자기 부분영역의 경계 꼭짓점 전역 번호로 범위를 명시. | 73 |

행 번호가 붙은 인용 1,266개는 공백을 제외하고 지정된 원문 행과 일치했다.
다섯 원문의 SHA-256은 대조 시작 전과 같았다.
기록의 frontmatter를 유지했다.
기록의 구간 경계를 유지했다.
모델은 실행하지 않았다.

정정 10, 보완 16, 이상 없음 95

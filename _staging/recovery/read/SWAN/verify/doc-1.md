2026-10-13에 지정된 SWAN 판독 기록 10개를 대조했다.

기록 경로의 기준은 `_staging/recovery/read/SWAN/manuals/website/`다.
각 기록의 `file:`에 지정된 로컬 원문을 사용했다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
원문을 여는 각 명령의 범위는 200행 이하였다.
빈 줄과 마크업을 원문 행 수에 포함했다.
기록의 후속 검토 항목도 해당 원문과 대조했다.

`정정`은 틀리거나 범위가 불명확한 기존 서술을 바로잡은 구간 행 수다.
`보완`은 기존 오류 정정 없이 누락 내용을 추가한 구간 행 수다.
`이상 없음`은 수정하지 않은 구간 행 수다.
한 구간에서 여러 내용을 고쳐도 한 행으로 집계했다.
정정과 보완이 함께 있는 구간은 정정으로 집계했다.

| 기록 | 대조한 원문 범위 | 대조한 원문 행 수 | 대조한 기록 구간 행 수 | 정정 | 보완 | 이상 없음 |
|---|---|---:|---:|---:|---:|---:|
| [download/download.htm.md](../manuals/website/download/download.htm.md) | 1–85 | 85 | 6 | 0 | 1 | 5 |
| [features/features.htm.md](../manuals/website/features/features.htm.md) | 1–127 | 127 | 5 | 0 | 0 | 5 |
| [home.htm.md](../manuals/website/home.htm.md) | 1–83 | 83 | 5 | 0 | 0 | 5 |
| [index.html.md](../manuals/website/index.html.md) | 1–9 | 9 | 1 | 0 | 0 | 1 |
| [items.htm.md](../manuals/website/items.htm.md) | 1–81 | 81 | 5 | 0 | 0 | 5 |
| [modifications/modifications.htm.md](../manuals/website/modifications/modifications.htm.md) | 1–1652 | 1652 | 69 | 7 | 17 | 45 |
| [problems_and_fixes/patches/41.51.A.md](../manuals/website/problems_and_fixes/patches/41.51.A.md) | 1–392 | 392 | 21 | 2 | 17 | 2 |
| [problems_and_fixes/problems_and_fixes.htm.md](../manuals/website/problems_and_fixes/problems_and_fixes.htm.md) | 1–97 | 97 | 6 | 0 | 0 | 6 |
| [references/references.htm.md](../manuals/website/references/references.htm.md) | 1–312 | 312 | 9 | 1 | 7 | 1 |
| [research_and_development/book.htm.md](../manuals/website/research_and_development/book.htm.md) | 1–37 | 37 | 3 | 0 | 0 | 3 |
| 합계 | 각 기록의 전체 원문 | 2875 | 130 | 10 | 42 | 78 |

아래 원문 행 번호는 해당 기록의 `file:`이 가리키는 파일 기준이다.
`swan/switch.pl`은 `models/SWAN/raw/source_code/swan/switch.pl`을 뜻한다.
전처리 표시를 판별하기 위해 이 파일의 82–105행을 추가로 읽었다.
이 보조 원문의 24행은 위 대조 행 수에 포함하지 않았다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| download/download.htm.md:59–71 | 예제의 구성 누락 | 보완: 예제가 명령 파일과 자료로 구성됨을 추가 | 60–61 |
| modifications/modifications.htm.md:1–38 | 주석 속 최초 FTP 버전 누락 | 보완: 30.51의 최초 FTP 배포 주석을 추가 | 32 |
| modifications/modifications.htm.md:106–123 | SPB의 전체 명칭과 제안 연도 누락 | 보완: Stochastic Parametric model과 Becq-Girard et al. (1999)를 추가 | 112–114 |
| modifications/modifications.htm.md:168–206 | 파주기·에너지 보정을 조건 없이 효과로 서술 | 정정: 어린 파랑의 정확도와 연안 너울·풍파 공존 조건 및 보정 가능성을 명시 | 170–183 |
| modifications/modifications.htm.md:616–658 | HPGL 제거 사유의 부정 진술 누락 | 보완: 낡은 기능·유지보수 중단·여러 플랫폼 미지원 사유를 추가 | 621–627 |
| modifications/modifications.htm.md:659–692 | wall-clock timings를 실시간 정보로 서술 | 정정: 계산에 걸린 실제 경과 시간으로 정정 | 672–678 |
| modifications/modifications.htm.md:778–808 | c_q 감소를 규칙으로만 요약 | 보완: kd<3.0인 격자 간격 비율의 제곱과 수렴 변경 효과의 대상을 명시 | 778–807 |
| modifications/modifications.htm.md:928–941 | CMake 지원의 배포 범위 누락 | 보완: GitLab 배포물에 포함되는 지원임을 추가 | 937 |
| modifications/modifications.htm.md:942–963 | 기능별 버전 대응 누락 | 보완: 각 기능이 속한 버전을 명시 | 942–963 |
| modifications/modifications.htm.md:1016–1053 | 스위치 선택만 서술하고 제거 동작 누락 | 보완: 설치에 맞는 스위치 제거를 명시 | 1032–1040 |
| modifications/modifications.htm.md:1054–1078 | 배열 도입과 기능 제거의 목적 누락 | 보완: POOL 사용 회피와 컴파일러 경고 회피를 추가 | 1056–1067 |
| modifications/modifications.htm.md:1079–1104 | POOL 배열의 관계와 도입 목적 누락 | 보완: Equivalent 표기와 컴파일러 경고 회피를 추가 | 1081–1087 |
| modifications/modifications.htm.md:1172–1194 | SPB 배열 변경 방식과 운영체제·컴파일러 버전 누락 | 보완: 할당 가능 배열 전환과 macOS 지원 및 Windows Intel Fortran 17을 추가 | 1180–1183 |
| modifications/modifications.htm.md:1195–1217 | 날짜 수정 연도와 netCDF 메모리 변화·경고 목적 누락 | 보완: 1599·1999·2399년 12월 31일과 메모리 감소 및 경고 목적을 추가 | 1198·1208–1210 |
| modifications/modifications.htm.md:1218–1230 | 이웃 스위프 자체를 제거한다고 서술 | 정정: 회전율 계산에 이웃 스위프를 포함하는 처리를 제거한다고 정정 | 1220–1226 |
| modifications/modifications.htm.md:1252–1276 | TMBOT 정의·보간으로 묶어 서술 | 정정: TMBOT 정의 수정과 별도의 보간 루틴 수정을 구분 | 1254–1258 |
| modifications/modifications.htm.md:1277–1299 | Hswell도 예외값 수정인 것처럼 묶음 | 정정: Hswell 계산 수정과 BOTLEV/WATLEV 예외값 수정을 구분 | 1295–1296 |
| modifications/modifications.htm.md:1300–1321 | 복사응력 일 항까지 TABLE·BLOCK 출력으로 단정 | 정정: TABLE·BLOCK은 작용 수지 각 항에 연결하고 복사응력 일 항은 별도의 도시 가능성으로 서술 | 1309–1314 |
| modifications/modifications.htm.md:1322–1343 | 정상 계산 제한자 비사용으로 일반화 | 정정: 비사용 대상을 Hersbach and Janssen 제한자로 한정 | 1338–1339 |
| modifications/modifications.htm.md:1344–1362 | 기술 문서 확장 항목 누락 | 보완: 기술 문서 정보 추가를 기록 | 1354 |
| modifications/modifications.htm.md:1378–1402 | WAM 개선·중첩의 구분과 매뉴얼 항목 누락 | 보완: WAM4 개선과 WAM의 SWAN 중첩 및 매뉴얼 항목을 추가 | 1381–1383·1389 |
| modifications/modifications.htm.md:1403–1427 | XNL·Windows OpenMP·백파소산·소산 출력의 구체적 대상 누락 | 보완: Fortran90·Intel 듀얼 코어·Alves and Banner·소산 3부분을 추가 | 1415–1417·1422–1424 |
| modifications/modifications.htm.md:1567–1592 | 평균 주기 경계 조건의 유형 누락 | 보완: 매개변수형 경계 조건임을 명시 | 1570–1573 |
| modifications/modifications.htm.md:1593–1624 | WAM 판본 조건과 마지막 출력 오류의 내용 누락 | 보완: 로컬 WAM과 마지막·직전 단계 출력 중복을 명시 | 1603–1606·1613–1617 |
| modifications/modifications.htm.md:1625–1652 | SWAN-SWAN 중첩 오류를 주제만 나열 | 보완: 작동하지 않은 오류임을 명시 | 1633–1634 |
| problems_and_fixes/patches/41.51.A.md:10–40 | 파일 시각의 실제 값 누락 | 보완: 이전·새 파일 시각을 원문대로 추가 | 10–11 |
| problems_and_fixes/patches/41.51.A.md:41–47 | 파일 시각 누락 | 보완: 이전·새 파일 시각을 원문대로 추가 | 41–42 |
| problems_and_fixes/patches/41.51.A.md:48–85 | 시각·diff 구간 단절과 주석 조건의 상태 누락 | 보완: 시각과 GNU 진입 조건·IF 종료행 부재 및 주석임을 추가 | 48–49·69–85 |
| problems_and_fixes/patches/41.51.A.md:86–109 | 주석과 닫는 중괄호의 소속 누락 | 보완: 109행이 Intel 분기 종료임을 명시하고 Windows 바깥 분기의 종료행 부재를 추가 | 88–109 |
| problems_and_fixes/patches/41.51.A.md:110–132 | 바깥 분기와 종료 위치 누락 | 보완: Windows·GNU 분기 및 버전 IF/ELSE 종료 위치를 추가 | 88·110–127·172 |
| problems_and_fixes/patches/41.51.A.md:133–144 | 바깥 GNU 분기와 생성되는 조건문의 실행 주체 누락 | 보완: GNU 분기 범위와 출력 설정 파일의 조건임을 추가 | 110–111·133–144·172 |
| problems_and_fixes/patches/41.51.A.md:145–159 | 바깥 GNU 분기와 생성 조건의 범위 누락 | 보완: GNU 분기와 NETCDFROOT 조건의 ELSE·종료 위치를 추가 | 110–111·145–159·172 |
| problems_and_fixes/patches/41.51.A.md:160–175 | 바깥 분기·ELSE 유무·마지막 분기의 종료 범위 누락 | 보완: GNU 구간과 생성 조건의 종료 및 f90 종료행 부재를 추가 | 110–111·160–175 |
| problems_and_fixes/patches/41.51.A.md:176–193 | FC가 없는 경우로만 조건을 제한 | 정정: FC 값이 Perl에서 거짓인 경우로 바로잡고 검색 중단 조건과 종료행 부재를 추가 | 183–193 |
| problems_and_fixes/patches/41.51.A.md:194–204 | 파일 시각 누락 | 보완: 이전·새 파일 시각을 원문대로 추가 | 194–195 |
| problems_and_fixes/patches/41.51.A.md:205–215 | 파일 시각 누락 | 보완: 이전·새 파일 시각을 추가 | 205–206 |
| problems_and_fixes/patches/41.51.A.md:216–226 | 파일 시각 누락 | 보완: 이전·새 파일 시각을 추가 | 216–217 |
| problems_and_fixes/patches/41.51.A.md:227–243 | 파일 시각과 IF 종료 범위 누락 | 보완: 시각과 IF 종료행 부재를 추가 | 227–243 |
| problems_and_fixes/patches/41.51.A.md:244–262 | 파일 시각과 오류 분기의 diff 단절 누락 | 보완: 시각과 미할당 IF 종료 및 ISTAT 본문·종료행 부재를 추가 | 244–262 |
| problems_and_fixes/patches/41.51.A.md:263–285 | 존재하지 않을 때 삭제하는 파일과 전처리 조건이 불명확 | 정정: STPNOW 검사에서 반환하지 않은 경우 더미 파일 삭제 여부를 판단하는 순서를 명시하고 netCDF 스위치 및 분기 범위를 추가 | 263–285; swan/switch.pl:102 |
| problems_and_fixes/patches/41.51.A.md:286–305 | 파일 시각과 식별 목록 주석 누락 | 보완: 시각과 resident/ghost 식별 목록 주석을 추가 | 286–295 |
| problems_and_fixes/patches/41.51.A.md:306–329 | 시각과 diff 구간 사이의 블록 소속 누락 | 보완: 시각과 NVAR의 ELSE 부재 및 LORQ·ENDIF의 불완전한 범위를 추가 | 306–329 |
| problems_and_fixes/patches/41.51.A.md:330–364 | 시각·오류 출력 순서·IF 종료 위치 누락 | 보완: 시각과 메시지 출력 후 exit 1 및 두 IF 종료를 추가 | 330–363 |
| problems_and_fixes/patches/41.51.A.md:365–382 | 부분 diff의 바깥 분기 범위 누락 | 보완: npmpi IF 종료와 바깥 ELSE·fi에 대응하는 조건 부재를 추가 | 365–382 |
| references/references.htm.md:29–62 | 회의 개최 날짜 누락 | 보완: 1993년 7월 25–28일과 1994년 10월의 원문 날짜 표기를 추가 | 37–38·46 |
| references/references.htm.md:63–100 | 각 문헌에 쪽수가 있다고 서술 | 정정: 학위논문의 97-4는 보고서 번호임을 명시하고 쪽수 서술을 나머지 세 문헌으로 한정 | 63–100 |
| references/references.htm.md:101–154 | 워크숍 날짜와 비교 모델의 세대 누락 | 보완: 워크숍 날짜와 HISWA 2세대·SWAN 3세대를 추가 | 122–123·128–135·144–145·152–153 |
| references/references.htm.md:155–193 | 스펙트럼 문헌의 발표 유형과 회의 날짜 누락 | 보완: 기조발표와 회의 날짜를 추가 | 184–185 |
| references/references.htm.md:194–230 | 2003년 성장·감쇠 문헌의 적용 사례 수 누락 | 보완: 지역 규모 적용 사례 3개를 추가 | 217–219 |
| references/references.htm.md:231–261 | 개별 출판 연도·사건 날짜·자료 기간과 일부 연구 대상 누락 | 보완: 연도 구분과 Floyd 1999·Guyana October 2005·10년 자료 및 연구 대상을 추가 | 231–261 |
| references/references.htm.md:262–292 | 허리케인 대상 연도와 발표 연도 누락 | 보완: Gustav·Ike의 2008년과 두 발표의 2013년을 추가 | 271·283·285·288 |
| references/references.htm.md:293–312 | 소산 모델의 주파수 분포와 정확도 문헌의 대상 조건 누락 | 보완: 주파수별 소산과 속도장의 비영 발산 조건을 추가 | 294·299 |

원문 10개의 SHA-256은 각 기록의 frontmatter와 일치했다.
기록의 구간은 원문 처음부터 끝까지 빈틈과 중복 없이 이어졌다.
구간 경계와 frontmatter는 변경하지 않았다.
변경한 구간 행에는 요청된 검증 표식을 붙였다.
허용된 대상 기록과 이 보고서만 수정했다.
원문과 노트와 git은 수정하지 않았다.
모델은 실행하지 않았다.
HTML 그림의 로컬 사본은 없었다.
그림과 페이지는 렌더링하지 않았다.

정정 10, 보완 42, 이상 없음 78

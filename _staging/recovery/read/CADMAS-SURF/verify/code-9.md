# CADMAS-SURF code-9 전수 검증

검증일: 2026-11-04.

대상 기록 경로: `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/`.
원문은 각 기록 frontmatter의 `file:`을 사용했다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
인용문과 행 번호의 기계 대조에 더해 조건·식·분기·요약·일본어 뜻을 직접 대조했다.
모델은 실행하지 않았다.
구간 경계와 frontmatter는 보존했다.

대조한 행 수는 기록 표의 구간 행 수이다.
원문 행 수는 빈 행과 주석을 포함한다.
정정·보완은 아래 변경 목록의 항목 수이다.
이상 없음은 완료 기록 중 변경하지 않은 구간 행 수이다.
한 구간에 정정과 보완이 함께 있으면 각 항목을 따로 센다.

| 기록 | 상태 | 대조한 구간 행 수 | 대조한 원문 행 수 |
|---|---|---:|---:|
| vf_vpcoef.f.md | 완료 | 15 | 455 |
| vf_vpsol.f.md | 완료 | 4 | 85 |
| vf_wcnd0.f.md | 완료 | 11 | 327 |
| vf_wsfmb2.f.md | 완료 | 37 | 1032 |
| vf_wstk0.f.md | 완료 | 8 | 177 |
| vf_zgetim.f.md | 완료 | 5 | 87 |
| vf_zgetln.f.md | 완료 | 5 | 109 |
| vf_zgetln_mpversion.f.md | 완료 | 5 | 109 |
| vf_zseti1.f.md | 완료 | 3 | 32 |
| vf_zseti2.f.md | 완료 | 3 | 35 |
| vf_zseti3.f.md | 완료 | 3 | 38 |
| vf_zsetr1.f.md | 완료 | 3 | 32 |
| vf_zsetr2.f.md | 완료 | 3 | 35 |
| vf_zsetr3.f.md | 완료 | 3 | 38 |
| vf_zstoi.f.md | 완료 | 4 | 86 |
| vf_zstor.f.md | 완료 | 4 | 112 |
| vf_zstows.f.md | 완료 | 4 | 63 |
| vf_ztimec.f.md | 완료 | 4 | 59 |
| vf_zxmg_abort.f.md | 완료 | 3 | 31 |
| vf_zxmg_allmnd.f.md | 완료 | 3 | 34 |
| vf_zxmg_allsmi.f.md | 완료 | 3 | 34 |
| vf_zxmg_barri.f.md | 완료 | 3 | 31 |
| vf_zxmg_bcastc.f.md | 완료 | 3 | 35 |
| vf_zxmg_bcasti.f.md | 완료 | 3 | 35 |
| vf_zxmg_crank.f.md | 완료 | 3 | 32 |
| vf_zxmg_csize.f.md | 완료 | 3 | 32 |
| vf_zxmg_final.f.md | 완료 | 3 | 30 |
| vf_zxmg_init.f.md | 완료 | 3 | 30 |
| vf_zxmg_irecvd.f.md | 완료 | 3 | 37 |
| vf_zxmg_irecvi.f.md | 완료 | 3 | 37 |
| vf_zxmg_isendd.f.md | 완료 | 3 | 37 |
| vf_zxmg_isendi.f.md | 완료 | 3 | 37 |
| vf_zxmg_split.f.md | 완료 | 3 | 34 |
| vf_zxmg_wait.f.md | 완료 | 3 | 34 |
| vf_zxmg_wtime.f.md | 완료 | 3 | 30 |
| vf_zxmp_allmnd.f.md | 완료 | 3 | 35 |
| vf_zxmp_allmni.f.md | 완료 | 3 | 35 |
| vf_zxmp_allmxd.f.md | 완료 | 3 | 35 |
| vf_zxmp_allsmd.f.md | 완료 | 3 | 35 |
| vf_zxmp_allsmi.f.md | 완료 | 3 | 35 |
| vf_zxmp_barri.f.md | 완료 | 3 | 31 |
| vf_zxmp_bcastc.f.md | 완료 | 3 | 36 |
| vf_zxmp_bcastd.f.md | 완료 | 3 | 36 |
| vf_zxmp_bcasti.f.md | 완료 | 3 | 36 |
| vf_zxmp_crank.f.md | 완료 | 3 | 33 |
| vf_zxmp_csize.f.md | 완료 | 3 | 33 |
| vf_zxmp_gatheri.f.md | 완료 | 3 | 40 |
| vf_zxmp_gathervd.f.md | 완료 | 3 | 44 |
| vf_zxmp_gathervi.f.md | 완료 | 3 | 44 |
| vf_zxmp_irecvd.f.md | 완료 | 3 | 38 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_vpcoef.f.md:75–115 | 부호별 좌표 변환과 상수 계산으로 요약 | 보완: 계산식과 ELSE 부재 및 0인 경우 보완 | vf_vpcoef.f:75–114 |
| vf_vpcoef.f.md:116–147 | AXY·AXZ·AYZ·AVL의 물리적 의미를 단정 | 정정: 면적·체적은 해석으로 구분 | vf_vpcoef.f:137–146 |
| vf_vpcoef.f.md:148–184 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 134, 434–437 |
| vf_vpcoef.f.md:185–221 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 134, 434–437 |
| vf_vpcoef.f.md:222–258 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 134, 434–437 |
| vf_vpcoef.f.md:259–296 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 134, 434–437 |
| vf_vpcoef.f.md:297–340 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 134, 434–437 |
| vf_vpcoef.f.md:341–352 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 134, 434–437 |
| vf_vpcoef.f.md:353–378 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 134, 434–437 |
| vf_vpcoef.f.md:379–391 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 367, 434–437 |
| vf_vpcoef.f.md:392–404 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 380, 434–437 |
| vf_vpcoef.f.md:405–430 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 393, 434–437 |
| vf_vpcoef.f.md:431–455 | 바깥 루프와 분기를 행 번호·이름만으로 표시 | 보완: 바깥 루프 범위·분기 조건·종료 행 명시 | vf_vpcoef.f:117–123, 419, 434–437 |
| vf_vpcoef.f.md:148–184 | GV를 보간으로 단정 | 정정: 보간은 해석으로 구분 | vf_vpcoef.f:152–155 |
| vf_vpcoef.f.md:297–340 | 유형 4 경계 계수를 비영이라고 단정 | 정정: 계산식과 비영 여부를 구분 | vf_vpcoef.f:307–334 |
| vf_vpcoef.f.md:341–352 | VD의 물리 해석 단정 및 두 IF의 순서 미표시 | 정정: 해석 구분 및 뒤 대입의 우선 순서 명시 | vf_vpcoef.f:345–350 |
| vf_vpcoef.f.md:353–378 | BB의 용도 해석 단정 | 정정: 해석으로 구분 | vf_vpcoef.f:364, 377 |
| vf_vpsol.f.md:21–50 | DD 시작 주석 인용 누락 | 보완: DD–AE 주석 전체 인용 | vf_vpsol.f:34–35 |
| vf_wcnd0.f.md:1–43 | C0의 물리적 의미 단정 및 입력 N 표기 | 정정: 입력 N1과 계산식 명시, 파속은 해석으로 구분, 분기 대상 보완 | vf_wcnd0.f:6–42 |
| vf_wcnd0.f.md:44–72 | 루프 종료 및 GOTO 대상 행 생략 | 보완: 루프 종료·GOTO 대상·변경 이력 추가 | vf_wcnd0.f:27, 44–73 |
| vf_wcnd0.f.md:73–109 | 계산형 GOTO와 공유 종결문의 대상 행 생략 | 보완: 대상 행과 범위 밖 순차 진행 추가 | vf_wcnd0.f:73–88, 110, 121 |
| vf_wcnd0.f.md:110–143 | RL을 근거 없이 파장으로 단정 | 정정: 해석 구분 및 공유 종결문 명시 | vf_wcnd0.f:130–141 |
| vf_wcnd0.f.md:144–166 | ZS를 수면 변위로 단정 | 정정: 해석 구분 및 GOTO·루프 종결 위치 명시 | vf_wcnd0.f:144–167 |
| vf_wcnd0.f.md:167–189 | Z의 의미 단정과 W 갱신 제외 조건 생략 | 정정: 해석 구분 및 마지막 반복의 W 갱신 생략 명시 | vf_wcnd0.f:167–184 |
| vf_wcnd0.f.md:190–234 | 근사·타원적분이라는 구간 근거 없는 해석 | 정정: 변수명으로 기술하고 분기 대상 행 추가 | vf_wcnd0.f:191–252 |
| vf_wcnd0.f.md:235–261 | ENTRY 평가 위치만 표시 | 보완: GOTO 대상 행과 조건 명시 | vf_wcnd0.f:252, 269 |
| vf_wcnd0.f.md:262–289 | GOTO 대상 행 생략 | 보완: 각 GOTO 대상 레이블의 행 번호 명시 | vf_wcnd0.f:199, 266–313 |
| vf_wcnd0.f.md:313–327 | 홀수 분기의 대상 행 생략 | 보완: 대상 451의 행 번호 명시 | vf_wcnd0.f:314, 321 |
| vf_wsfmb2.f.md:40–74 | 심해 파장 의미 단정 및 입력 오류 이동 경로 축약 | 정정: 해석 구분 및 조건과 오류 경로 명시 | vf_wsfmb2.f:42–70, 217–221 |
| vf_wsfmb2.f.md:108–157 | 바깥 iterh 루프 이름만 표시 | 보완: 루프 범위와 닫히는 행 명시 | vf_wsfmb2.f:92, 195 |
| vf_wsfmb2.f.md:158–196 | 바깥 iterh 루프 이름만 표시 | 보완: 루프 범위와 닫히는 행 명시 | vf_wsfmb2.f:92, 195 |
| vf_wsfmb2.f.md:197–223 | 입력 오류 시 출력과 반환 설명 생략 | 보완: 입력 오류 메시지·출력값·RETURN 명시 | vf_wsfmb2.f:217–221 |
| vf_wsfmb2.f.md:401–425 | 바깥 itera 루프 이름만 표시 | 보완: 루프 범위와 종료 행 명시 | vf_wsfmb2.f:395, 461 |
| vf_wsfmb2.f.md:426–466 | 바깥 itera 루프 이름만 표시 | 보완: 루프 범위와 종료 행 명시 | vf_wsfmb2.f:395, 461 |
| vf_wsfmb2.f.md:577–605 | 바깥 i·n 루프 이름만 표시 | 보완: 루프 범위·종료 행 명시 | vf_wsfmb2.f:552, 575, 604, 649 |
| vf_wsfmb2.f.md:606–627 | 바깥 i 루프 이름만 표시 | 보완: 루프 범위·종료 행 명시 | vf_wsfmb2.f:552, 649 |
| vf_wsfmb2.f.md:628–650 | 바깥 i 루프 이름만 표시 | 보완: 루프 범위·종료 행 명시 | vf_wsfmb2.f:552, 649 |
| vf_wsfmb2.f.md:606–627 | qq를 베르누이 잔차로 단정 | 정정: 해석으로 구분 | vf_wsfmb2.f:613–614 |
| vf_wsfmb2.f.md:651–665 | sdetaa 자체를 평균하는 것처럼 기술 | 정정: sdetaa를 읽어 detaa에 대입함을 명시 | vf_wsfmb2.f:651–657 |
| vf_wsfmb2.f.md:715–744 | 바깥 루프 생략 및 파봉·파곡 의미 단정 | 정정: 루프 범위·종료 행 및 해석 구분 | vf_wsfmb2.f:690, 715–727 |
| vf_wsfmb2.f.md:775–800 | 바깥 j 루프 이름만 표시 | 보완: 루프 범위·종료 행과 실패 GOTO 대상 명시 | vf_wsfmb2.f:757, 764, 790–792 |
| vf_wsfmb2.f.md:801–829 | 항상 현재 xl2와 xl의 차이로 수면을 재사용한다고 설명 | 정정: GOTO가 ax1 대입을 건너뛰는 경로 명시 | vf_wsfmb2.f:810–825 |
| vf_wsfmb2.f.md:910–941 | 항상 현재 좌표 차이로 eta를 재사용한다고 설명 | 정정: GOTO가 ax5 대입을 건너뛰는 경로 명시 | vf_wsfmb2.f:920–938 |
| vf_wsfmb2.f.md:892–909 | pp1을 압력 수두로 단정 | 정정: 해석으로 구분 | vf_wsfmb2.f:897–906 |
| vf_wsfmb2.f.md:961–980 | 바깥 j 루프의 종료 행 생략 | 보완: 루프 원문과 종료 행 명시 | vf_wsfmb2.f:960, 998 |
| vf_wsfmb2.f.md:981–1000 | 바깥 j 루프의 종료 행 생략 | 보완: 루프 원문과 종료 행 명시 | vf_wsfmb2.f:960, 998 |
| vf_wsfmb2.f.md:1001–1032 | ELSE 없는 분기 사슬 설명 생략 | 보완: ELSE 부재 및 ii 유지 조건 명시 | vf_wsfmb2.f:1014–1020 |
| vf_wsfmb2.f.md:1–39 | 計算時를 계산식으로 번역 | 정정: 제1정의 계산 때의 코드로 정정 | vf_wsfmb2.f:17–18 |
| vf_wstk0.f.md:1–22 | HD를 파고 대 수심비로 기술 | 정정: HD의 분모 2D 명시 및 물리적 의미는 해석으로 구분 | vf_wstk0.f:16–20 |
| vf_wstk0.f.md:23–56 | 계산형 GOTO를 차수만으로 요약 | 보완: N별 대상 행·범위 밖 순차 진행·루프 종결 명시 | vf_wstk0.f:23–57 |
| vf_wstk0.f.md:57–77 | 물리적 의미를 구간 근거 없이 단정 | 정정: 물리적 의미를 해석으로 구분 | vf_wstk0.f:57–66 |
| vf_wstk0.f.md:123–146 | ZS를 수면으로 단정 | 정정: 해석 구분 및 GOTO 대상 행 명시 | vf_wstk0.f:128–147 |
| vf_wstk0.f.md:147–164 | P1을 압력 수두로 단정 | 정정: 해석으로 구분 | vf_wstk0.f:162 |
| vf_zgetln.f.md:44–74 | MAXLIN행 읽기로 요약하고 오류 이동 대상 행 생략 | 보완: EOF 중단 및 END·ERR·GOTO 대상 행 명시 | vf_zgetln.f:53–63, 97 |
| vf_zgetln.f.md:75–90 | 빈 줄 분기의 대상 행 생략 | 보완: GOTO 대상과 DO 종료 행 명시 | vf_zgetln.f:79–84, 92 |
| vf_zgetln_mpversion.f.md:44–74 | MAXLIN행 읽기로 요약하고 오류 이동 대상 행 생략 | 보완: EOF 중단 및 END·ERR·GOTO 대상 행 명시 | vf_zgetln_mpversion.f:53–63, 97 |
| vf_zgetln_mpversion.f.md:75–90 | 빈 줄 분기의 대상 행 생략 | 보완: GOTO 대상과 DO 종료 행 명시 | vf_zgetln_mpversion.f:79–84, 92 |
| vf_zstoi.f.md:21–46 | 부호 분기의 ELSE 부재와 구간 밖 이동 대상 행 생략 | 보완: 조건 불성립 시 변수 유지와 GOTO 대상 행 명시 | vf_zstoi.f:28–45, 79 |
| vf_zstor.f.md:21–47 | 부호 분기의 ELSE 부재와 구간 밖 이동 대상 행 생략 | 보완: 조건 불성립 시 변수 유지와 GOTO 대상 행 명시 | vf_zstor.f:29–46, 105 |
| vf_zstows.f.md:25–34 | 조기 반환 분기의 대상 행 생략 | 보완: 9000·9999 대상 행과 RETURN 명시 | vf_zstows.f:29, 33, 56–62 |
| vf_zxmg_abort.f.md:1–19 | 개요 주석에 없는 전체 통신자 의미를 번역에 추가 | 정정: 주석 번역과 MPI_COMM_WORLD 인수의 22행 근거를 구분 | vf_zxmg_abort.f:5, 22 |
| vf_zxmg_irecvd.f.md:26–29 | N개 원소를 받는다고 기술 | 정정: 호출의 버퍼·원소 수·자료형·송신원 인수와 실제 수신 수를 구분 | vf_zxmg_irecvd.f:27–28 |
| vf_zxmg_irecvi.f.md:26–29 | N개 원소를 받는다고 기술 | 정정: 호출의 버퍼·원소 수·자료형·송신원 인수와 실제 수신 수를 구분 | vf_zxmg_irecvi.f:27–28 |
| vf_zxmg_split.f.md:24–26 | 색상과 키를 모두 통신자 분할 기준으로 요약 | 정정: 호출에 적힌 색상·키·입출력 통신자 인수를 구분 | vf_zxmg_split.f:25 |
| vf_zxmp_gatheri.f.md:1–27 | 개요 주석 번역에 원문에 없는 MPI 마스크를 추가 | 정정: 고정 길이 정수 데이터 수집이라는 주석 내용으로 정정 | vf_zxmp_gatheri.f:5 |
| vf_zxmp_gathervd.f.md:1–31 | 개요 주석 번역에 원문에 없는 MPI 마스크를 추가 | 정정: 가변 길이 실수 데이터 수집이라는 주석 내용으로 정정 | vf_zxmp_gathervd.f:6 |
| vf_zxmp_gathervi.f.md:1–31 | 개요 주석 번역에 원문에 없는 MPI 마스크를 추가 | 정정: 가변 길이 정수 데이터 수집이라는 주석 내용으로 정정 | vf_zxmp_gathervi.f:6 |
| vf_zxmp_irecvd.f.md:27–30 | N개 원소를 받는다고 기술 | 정정: 호출의 버퍼·원소 수·자료형·송신원 인수와 실제 수신 수를 구분 | vf_zxmp_irecvd.f:28–29 |

기존 완료 기록 6개는 다시 대조하지 않았다.
이번 재개에서 나머지 기록 44개의 구간 행 140개와 원문 1,864행을 대조했다.
이번 재개 대상의 원문 인용 1,347개는 인용문과 행 번호의 기계 대조에서도 일치했다.
이번 재개 대상에서 빈 행과 단독 `C` 주석 행을 제외한 원문 행의 인용 누락은 없었다.
전체 대상 50개 기록의 누적 대조 범위는 구간 행 220개와 원문 4,027행이다.
위 수치는 기록별 완료 표와 이번 재개 대상의 원문 인용을 집계한 값이다.

정정 30, 보완 38, 이상 없음 157

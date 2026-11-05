# CADMAS-SURF code-30 전수 대조

검증일: 2026-11-04.
상태: 대상 기록 44개 완료.
기존 code-30.md는 없었다.

기록 경로의 기준은 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/`이다.
아래 표의 기록 이름에는 이 기준 경로를 붙인다.
원문은 각 기록 frontmatter의 `file:` 경로이다.
각 원문 행 번호는 해당 기록의 원문 파일을 기준으로 한다.

대상 기록의 구간표 93행을 원문 1324행과 의미까지 대조했다.
원문 행 수는 빈 줄과 주석을 포함한다.
구간마다 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문 구간은 모두 200행 이하이다.
잘린 출력은 더 작은 묶음으로 다시 열었다.
구간표 뒤의 코드 사실도 원문과 대조했다.

정정과 보완은 표시를 붙인 기록 행 수로 센다.
이상 없음은 정정과 보완이 없는 기록 수로 센다.

## 기록별 대조 결과

| 기록 | 대조한 원문 행 | 원문 행 수 | 구간표 행 수 | 정정 | 보완 | 상태 |
|---|---|---:|---:|---:|---:|---|
| src/yfunc.f.md | 1–22 | 22 | 3 | 1 | 1 | 완료 |
| util/addset.f.md | 1–19 | 19 | 2 | 0 | 0 | 완료·이상 없음 |
| util/addset2.f.md | 1–15 | 15 | 2 | 0 | 0 | 완료·이상 없음 |
| util/addset3.f.md | 1–13 | 13 | 1 | 0 | 0 | 완료·이상 없음 |
| util/addset4.f.md | 1–13 | 13 | 1 | 0 | 0 | 완료·이상 없음 |
| util/addvec.f.md | 1–14 | 14 | 1 | 0 | 0 | 완료·이상 없음 |
| util/areacd2.f.md | 1–33 | 33 | 3 | 3 | 0 | 완료 |
| util/atxb.f.md | 1–30 | 30 | 2 | 0 | 0 | 완료·이상 없음 |
| util/axb.f.md | 1–29 | 29 | 2 | 0 | 0 | 완료·이상 없음 |
| util/chtnsr.f.md | 1–78 | 78 | 4 | 2 | 0 | 완료 |
| util/clear0.f.md | 1–22 | 22 | 2 | 0 | 0 | 완료·이상 없음 |
| util/clear1.f.md | 1–23 | 23 | 2 | 0 | 0 | 완료·이상 없음 |
| util/cross.f.md | 1–14 | 14 | 1 | 0 | 0 | 완료·이상 없음 |
| util/cross1.f.md | 1–14 | 14 | 1 | 0 | 0 | 완료·이상 없음 |
| util/cross2.f.md | 1–18 | 18 | 1 | 0 | 0 | 완료·이상 없음 |
| util/dircos.f.md | 1–18 | 18 | 1 | 0 | 0 | 완료·이상 없음 |
| util/errstp.f.md | 1–10 | 10 | 1 | 1 | 0 | 완료 |
| util/harfab.f.md | 1–31 | 31 | 2 | 0 | 0 | 완료·이상 없음 |
| util/harfb.f.md | 1–44 | 44 | 2 | 0 | 0 | 완료·이상 없음 |
| util/harfc.f.md | 1–30 | 30 | 2 | 0 | 0 | 완료·이상 없음 |
| util/harfta.f.md | 1–33 | 33 | 2 | 0 | 0 | 완료·이상 없음 |
| util/harfta2.f.md | 1–22 | 22 | 2 | 0 | 0 | 완료·이상 없음 |
| util/intpl.f.md | 1–27 | 27 | 3 | 1 | 0 | 완료 |
| util/length.f.md | 1–15 | 15 | 1 | 1 | 0 | 완료 |
| util/matml.f.md | 1–390 | 390 | 20 | 0 | 18 | 완료 |
| util/mean2.f.md | 1–14 | 14 | 1 | 0 | 0 | 완료·이상 없음 |
| util/mean3.f.md | 1–14 | 14 | 1 | 0 | 0 | 완료·이상 없음 |
| util/mean4.f.md | 1–14 | 14 | 1 | 0 | 0 | 완료·이상 없음 |
| util/order.f.md | 1–20 | 20 | 2 | 0 | 1 | 완료 |
| util/order2.f.md | 1–25 | 25 | 2 | 0 | 1 | 완료 |
| util/psfwt.f.md | 1–12 | 12 | 2 | 1 | 0 | 완료 |
| util/rmult1.f.md | 1–21 | 21 | 2 | 0 | 0 | 완료·이상 없음 |
| util/rmult2.f.md | 1–21 | 21 | 2 | 0 | 0 | 완료·이상 없음 |
| util/rmult3.f.md | 1–11 | 11 | 1 | 0 | 0 | 완료·이상 없음 |
| util/rmult4.f.md | 1–42 | 42 | 2 | 0 | 0 | 완료·이상 없음 |
| util/rmult5.f.md | 1–13 | 13 | 1 | 0 | 0 | 완료·이상 없음 |
| util/shift0.f.md | 1–21 | 21 | 2 | 0 | 0 | 완료·이상 없음 |
| util/shift1.f.md | 1–22 | 22 | 2 | 0 | 0 | 완료·이상 없음 |
| util/shiftb0.f.md | 1–10 | 10 | 1 | 0 | 0 | 완료·이상 없음 |
| util/subvec.f.md | 1–14 | 14 | 1 | 0 | 0 | 완료·이상 없음 |
| util/sumvec.f.md | 1–12 | 12 | 1 | 0 | 0 | 완료·이상 없음 |
| util/vecml1.f.md | 1–25 | 25 | 2 | 0 | 0 | 완료·이상 없음 |
| util/vecml2.f.md | 1–13 | 13 | 1 | 0 | 0 | 완료·이상 없음 |
| util/vecml3.f.md | 1–23 | 23 | 2 | 0 | 0 | 완료·이상 없음 |
| 합계 | 전체 | 1324 | 93 | 10 | 21 | 44개 완료 |

## 정정·보완 목록

목록의 새 요지 앞에는 정정 또는 보완을 표시했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| src/yfunc.f.md:7–13 | 정상·전단 성분을 단정하고 6배를 요약에서 생략 | 정정: 성분별 계산과 6배를 명시하고 물리적 의미를 해석으로 구분 | 7–12 |
| src/yfunc.f.md:14–22 | 해당 구간에 ELSE 부재와 미해당 값 처리 미명시 | 보완: ELSE 부재와 IYLD가 1·2가 아닐 때 F 미대입 명시 | 14–20 |
| util/areacd2.f.md:1–14 | X를 네 점 좌표로 단정 | 정정: 배열 복사를 명시하고 좌표 의미는 해석으로 구분 | 6–13 |
| util/areacd2.f.md:15–28 | 면적 의미를 사실로 단정 | 정정: 계산 사실과 좌표를 가정한 면적 해석을 구분 | 15–27 |
| util/areacd2.f.md:29–33 | 면적 좌표 의미를 사실로 단정 | 정정: 대입식과 면적 좌표 해석을 구분 | 29–31 |
| util/chtnsr.f.md:1–21 | SIG·EPS의 물리적 의미를 주석의 명시 사항으로 설명 | 정정: 주석에 있는 기호 관계와 물리적 해석을 구분 | 3–7 |
| util/chtnsr.f.md:22–42 | A를 응력 변환으로 단정 | 정정: 해당 구간에서는 A의 성분 구성으로 설명 | 22–41 |
| util/errstp.f.md:1–10 | 오류 표제와 NO를 모두 I3 형식으로 설명 | 정정: 표제는 A 형식이며 NO는 I3 형식임을 구분 | 5–6 |
| util/intpl.f.md:코드 사실 11–24 | 첫 해당 구간 또는 마지막 두 점의 선형식을 사용한다고 일반화 | 정정: 중복 X0에서 평균을 사용하는 예외를 명시 | 12–24 |
| util/length.f.md:1–15 | GRID1·GRID2를 좌표로 단정 | 정정: 배열 성분의 차이로 명시 | 8–12 |
| util/matml.f.md:58–78 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:79–99 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:100–120 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:121–135 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:136–150 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:151–171 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:172–186 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:187–201 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:202–251 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:252–271 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:272–291 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:292–311 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:312–325 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:326–339 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:340–359 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:360–373 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:374–387 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/matml.f.md:388–390 | 바깥 SELECT CASE의 식과 종료 행 미명시 | 보완: SELECT CASE( ITYP )와 END SELECT 388행 명시 | 30·388 |
| util/order.f.md:1–14 | ELSE 부재와 GOTO 대상 행 미명시 | 보완: 미일치 시 반복 계속과 표지 10의 행 명시 | 5–17 |
| util/order2.f.md:1–16 | ELSE 부재와 GOTO 대상 행 미명시 | 보완: 미일치 시 반복 계속과 두 표지의 행 명시 | 5–22 |
| util/psfwt.f.md:7–12 | 출력 인수를 진행 상태로 단정 | 정정: WRITE 인수 이름을 명시 | 9–10 |

## 확인 범위

조건과 분기별 동작을 대조했다.
루프 범위와 종료 행을 대조했다.
첨자 계산과 대입식의 계수·부호·순서를 대조했다.
고정형식 연속 줄을 포함한 문장 전체를 대조했다.
주석의 수식과 일본어 주석을 대조했다.
INCLUDE와 MPI 호출 인수를 대조했다.
원문에서 확인할 수 없는 물리적 의미와 용도 단정을 정정했다.

모든 실행문·선언문의 원문 인용 누락 여부를 기계 확인했다.
행 번호가 붙은 원문 인용의 내용도 기계 확인했다.
이 확인에서는 행 끝 공백을 제외했다.
표 안의 세로줄 이스케이프는 원래 세로줄로 환원했다.
기계 확인의 불일치는 0건이다.
원문 SHA-256은 각 기록 frontmatter의 값과 일치했다.
기록의 frontmatter와 구간 경계는 유지했다.
원문·노트·git은 변경하지 않았다.
모델은 실행하지 않았다.

정정 10, 보완 21, 이상 없음 34

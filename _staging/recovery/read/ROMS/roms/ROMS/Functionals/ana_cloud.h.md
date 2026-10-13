---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_cloud.h
lines: 147
sha256: 949298618504e6859e0b9ccc2101959abba5e203b98adcb01edd17b6815203d9
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_cloud.h — 판독 구간 기록

구간은 1행부터 147행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | ana_cloud 시작(2), 저작권·라이선스와 구름 비율(cloud fraction) 분석식 설명(4–14). 모듈·인수·MyFile 선언(15–26). `#include "tile.h"` (28)로 tile.h를 끼워 넣는다. ana_cloud_tile에 FORCES(ng)%cloud 전달(30–33). `#ifdef DISTRIBUTE` (37)의 `IF (Lanafile) THEN` (38), `#else` (39)의 `IF (Lanafile.and.(tile.eq.0)) THEN` (40), `#endif` (41) 뒤 ANANAME(4)=MyFile(42). 조건 종료·RETURN·루틴 종료·주석(43–47). |
| 48–84 | ana_cloud_tile 시작(49–52), 공통 모듈(55–56). `#ifdef PAPA_CLM` (58)에서 caldate 사용(59), `#endif` (60). exchange_r2d_tile 사용(61), `#ifdef DISTRIBUTE` (62)에서 mp_exchange2d 사용(63), `#endif` (64). 인수 선언(68–70). `#ifdef ASSUMED_SHAPE` (72)는 assumed-shape 출력 배열(73), `#else` (74)는 명시 크기 출력 배열(75), `#endif` (76). i·j·Cval·yday 선언(80–83), 빈 줄(84). |
| 85–103 | 시작 시 49행 ana_cloud_tile 안. `#ifdef PAPA_CLM` (85). 월별 구름량 Coktas의 고정 배열은 `real(dp), dimension(14) :: Coktas =                               &` (87); `&         (/ 6.29_r8, 6.26_r8, 6.31_r8, 6.31_r8, 6.32_r8,          &` (88); `&            6.70_r8, 7.12_r8, 7.26_r8, 6.93_r8, 6.25_r8,          &` (89); `&            6.19_r8, 6.23_r8, 6.31_r8, 6.29_r8          /)` (90). 연중 날짜 Cyday의 고정 배열은 `real(dp), dimension(14) :: Cyday =                                &` (92); `&          (/  0.0_dp,  16.0_dp,  46.0_dp,  75.0_dp, 105.0_dp,     &` (93); `&            136.0_dp, 166.0_dp, 197.0_dp, 228.0_dp, 258.0_dp,     &` (94); `&            289.0_dp, 319.0_dp, 350.0_dp, 365.0_dp           /)` (95). `#endif` (96). `#include "set_bounds.h"` (98)로 set_bounds.h를 끼워 넣는다. 구름 비율 단위는 %/100, 0은 맑음·1은 전운(overcast)이라는 주석(101). |
| 104–123 | 시작 시 49행 ana_cloud_tile 안. `#if defined PAPA_CLM` (104)에서 OWS Papa 기후값(climatology) 주석(106), caldate(tdays(ng),yd_dp=yday) 호출(108). i=1..13 루프(109)의 `IF ((yday.ge.Cyday(i)).and.(yday.le.Cyday(i+1))) THEN` (110)에서 `Cval=0.125_r8*(Coktas(i  )*(Cyday(i+1)-yday)+                 &` (111); `&                   Coktas(i+1)*(yday-Cyday(i)))/                  &` (112); `&                  (Cyday(i+1)-Cyday(i))` (113)로 옥타(okta)를 0.125로 환산하고 날짜 구간 선형 보간(linear interpolation)을 수행한다. 조건·루프 종료(114–115). `#elif defined BENCHMARK` (116)는 `Cval=0.6_r8` (117), `#elif defined NJ_BIGHT` (118)는 `Cval=0.3_r8` (119), `#else` (120)는 `Cval=0.0_r8` (121), `#endif` (122). 빈 줄(123). |
| 124–147 | 시작 시 49행 ana_cloud_tile 안. j·i 루프에서 cloud(i,j)=Cval 복사(124–128). `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (132)이면 exchange_r2d_tile(...,cloud) 호출(133–135). `#ifdef DISTRIBUTE` (138)에서 mp_exchange2d(...,1,...,NghostPoints,EWperiodic(ng),NSperiodic(ng),cloud) 호출(139–143), `#endif` (144). RETURN·루틴 종료(146–147). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 87–95: PAPA_CLM 날짜 표의 마지막 값은 365.0_dp이며 표 길이는 14로 고정된다.
- 108–115: PAPA_CLM 분기에서 Cval 대입은 날짜 구간 조건 안에만 있다. 이 분기에는 루프 앞 Cval 초기값이나 구간 밖 날짜 처리 문장이 없다. caldate 내부는 판독하지 않았다.

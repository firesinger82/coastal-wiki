---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/obs_depth.F
lines: 88
sha256: e84b3107fa7bfe29676f5b0e554dcdc7aa6deabbf40c3d2d9c19e08ce88c769e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# obs_depth.F — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | cppdefs.h 포함(1). FOUR_DVAR 또는 VERIFICATION, OBSERVATIONS, DISTRIBUTE, SOLVE3D가 필요한 전처리 조건(2–4)에서 obs_depth 시작(5). 저작권·깊이 Zobs 설명·모듈·인수·지역변수 선언(6–40). 주석은 음의 Zobs를 미터 깊이, 양의 Zobs를 1..N의 소수 수직 층 번호(fractional level)로 설명한다(14–18). IniVal은 0.0_r8로 선언 초기화한다(39). set_bounds.h를 포함한다(41). 계산·설정 원문: `real(r8) :: IniVal = 0.0_r8` (39). 전처리 행: `#include "cppdefs.h"` (1); `#if (defined FOUR_DVAR    \|\| defined VERIFICATION) && \` (2); `defined OBSERVATIONS && \` (3); `defined DISTRIBUTE   && defined SOLVE3D` (4); `# include "set_bounds.h"` (41). |
| 43–63 | 시작 시 `#if (defined FOUR_DVAR    \|\| defined VERIFICATION) && \` (2); `defined OBSERVATIONS && \` (3); `defined DISTRIBUTE   && defined SOLVE3D` (4) 안. 또한 5행 obs_depth 안. 주석·빈 줄(43–52). WEAK_CONSTRAINT이면 Mstr=NstrObs(ng), Mend=NendObs(ng), 나머지는 Mstr=1, Mend=Nobs(ng)로 관측 벡터 범위를 정한다(53–59). 타일 밖 깊이를 0으로 만들어 mp_collect 교환을 돕는다는 주석(61–62). 전처리 행: `# ifdef WEAK_CONSTRAINT` (53); `# else` (56); `# endif` (59). |
| 64–88 | 시작 시 `#if (defined FOUR_DVAR    \|\| defined VERIFICATION) && \` (2); `defined OBSERVATIONS && \` (3); `defined DISTRIBUTE   && defined SOLVE3D` (4) 안. 또한 5행 obs_depth 안. iobs=Mstr..Mend 루프(64). rho·u·v 위치의 수평 경계 안에 있는지를 각각 계산하며, 모든 하한은 포함하고 상한은 제외한다(65–76). 세 경계 판정이 모두 거짓일 때만 Zobs를 IniVal로 설정한다(77–79). 루프 종료·반환·루틴 종료(80–83). 전처리 else의 인수 없는 obs_depth는 RETURN만 실행한다(84–87). 끝 전처리 종료(88). 조건 원문: `IF (.not.(r_bound.or.u_bound.or.v_bound)) THEN` (77). 계산·설정 원문: `r_bound=((rXmin(ng) .le.Xobs(iobs)).and.                        &` (65); `&           (Xobs(iobs).lt.rXmax(ng))).and.                        &` (66); `&          ((rYmin(ng) .le.Yobs(iobs)).and.                        &` (67); `&           (Yobs(iobs).lt.rYmax(ng)))` (68); `u_bound=((uXmin(ng) .le.Xobs(iobs)).and.                        &` (69); `&           (Xobs(iobs).lt.uXmax(ng))).and.                        &` (70); `&          ((uYmin(ng) .le.Yobs(iobs)).and.                        &` (71); `&           (Yobs(iobs).lt.uYmax(ng)))` (72); `v_bound=((vXmin(ng) .le.Xobs(iobs)).and.                        &` (73); `&           (Xobs(iobs).lt.vXmax(ng))).and.                        &` (74); `&          ((vYmin(ng) .le.Yobs(iobs)).and.                        &` (75); `&           (Yobs(iobs).lt.vYmax(ng)))` (76). 전처리 행: `#else` (84); `#endif` (88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–18·44–45·64–79: 주석은 Zobs<0인 미터 깊이에 대한 처리를 설명한다. 실행 루프의 조건은 수평 경계 판정뿐이며 Zobs 부호를 검사하지 않는다.
- 31·37·64–79: model은 입력 인수로 선언되지만 실행문에서 참조되지 않는다. itrc는 지역 정수로 선언되지만 실행문에서 참조되지 않는다.
- 65–77: 실행 코드는 r_bound·u_bound·v_bound 중 하나라도 참이면 Zobs를 유지한다. 관측 종류에 따라 경계 판정을 선택하는 분기는 이 파일에 없다.

---
file: models/ROMS/raw/source_code/roms/ROMS/Representer/rp_set_zeta.F
lines: 148
sha256: 37e9b6b02ee47b0ab505af886ce8bf509a1377faba80d3d8c83fc34f150814a5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# rp_set_zeta.F — 판독 구간 기록

구간은 1행부터 148행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. rp_set_zeta_mod 시작·빈 줄(2–3). `#if defined TL_IOMS && defined SOLVE3D` (4)는 구현 전체를 선택한다. 저작권·MIT/X 허가와 접선 선형(tangent linear) 자유수면(free-surface)을 빠른 시간 평균(fast-time average)으로 설정한다는 목적 주석(6–16). implicit none·PRIVATE·rp_set_zeta 공개·CONTAINS·구분 주석(18–25). |
| 26–58 | 시작 시 4행 `#if defined TL_IOMS && defined SOLVE3D` 안. rp_set_zeta 입구(26), mod_param·mod_coupling·mod_ocean 사용(29–31), ng/tile·MyFile 선언(35–40). `# include "tile.h"` (42)로 tile.h 포함. `# ifdef PROFILE` (44), `# endif` (46)는 `wclock_on(ng,iRPM,12,...)` 호출(45). `rp_set_zeta_tile`에 타일(tile) 경계·작업 경계·COUPLING(ng)%tl_Zt_avg1·OCEAN(ng)%tl_zeta를 전달한다(47–51). `# ifdef PROFILE` (52), `# endif` (54)는 `wclock_off` 호출(53). RETURN·루틴 종료·주석(55–58). |
| 59–94 | 시작 시 4행 `#if defined TL_IOMS && defined SOLVE3D` 안. rp_set_zeta_tile 입구(60–63), mod_param·mod_scalars·exchange_r2d_tile 사용(66–69). `# ifdef DISTRIBUTE` (70), `# endif` (72)는 mp_exchange2d를 가져온다. 정수 입력 선언(76–78). `# ifdef ASSUMED_SHAPE` (80)는 tl_Zt_avg1 intent(in)·tl_zeta intent(out)의 열린 끝 배열 선언(81–83). `# else` (84)는 명시 경계 tl_Zt_avg1 입력과 시간 슬롯 크기 3의 tl_zeta 출력 선언(85–87). `# endif` (88), i/j 선언(92). `# include "set_bounds.h"` (94)로 set_bounds.h 포함. |
| 95–111 | 시작 시 4행 `#if defined TL_IOMS && defined SOLVE3D`·60행 루틴 안. 주석은 2차원 방정식 시간 전진 준비를 위해 시간 n에 대응하는 빠른 시간 평균을 초기 자유수면에 설정한다고 적는다(97–99). j=JstrR..JendR·i=IstrR..IendR 루프(102–103)에서 `tl_zeta(i,j,1)=tl_Zt_avg1(i,j)` (107), `tl_zeta(i,j,2)=tl_Zt_avg1(i,j)` (108). 일반 zeta의 시간 슬롯 1·2 복사는 !^ 주석(104–106). 루프 종료·빈 줄(109–111). |
| 112–128 | 시작 시 4행 `#if defined TL_IOMS && defined SOLVE3D`·60행 루틴 안. `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (112)은 주기 경계(periodic boundary)에서 tl_zeta(:,:,1)·tl_zeta(:,:,2)의 `exchange_r2d_tile` 호출(117–119·124–126)을 선택한다. 일반 zeta의 동일 교환은 !^ 주석(113–116·120–123). 조건 종료·빈 줄(127–128). |
| 129–148 | 시작 시 4행 `#if defined TL_IOMS && defined SOLVE3D`·60행 루틴 안. `# ifdef DISTRIBUTE` (129), `# endif` (143)는 iRPM·필드 수 2·NghostPoints·주기 설정을 전달하는 tl_zeta 시간 슬롯 1·2의 `mp_exchange2d` 호출(137–142)을 선택한다. 일반 zeta 두 필드의 iNLM 교환 호출은 !^ 주석(130–136). RETURN·루틴 종료(144–146), `#endif` (147), 모듈 종료(148). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 83·87·107–108·117–126·137–142: tl_zeta는 intent(out)이며 명시 선언의 시간 슬롯 크기는 3이다. 이 루틴은 시간 슬롯 1과 2만 대입하고 교환한다. 시간 슬롯 3을 대입하는 문장은 이 파일에 없다.
